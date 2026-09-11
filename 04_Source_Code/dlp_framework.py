"""
dlp_framework.py
------------------
Main entry point for the hybrid classification-and-anomaly DLP framework
(Figure 3.1, Chapter 3). Wires together the two detection techniques and
the decision engine into a single pipeline:

    Transfer Event (content, user, volume, destination)
            |
            v
    Hybrid Detection
      Technique 1: ContentClassifier   (content_classifier.py)
      Technique 2: AnomalyDetector     (anomaly_detector.py)
            |
            v
    Decision Engine (combines classification + anomaly signals)
            |
            v
    Response Action: ALLOW / ALERT / BLOCK
            |
            v
    Logging: decision_log.csv

Decision policy
----------------
Content sensitivity and behavioral anomaly are combined using the same
"content_flagged AND (external destination OR anomaly)" leak condition
already used for the hybrid baseline in evaluate_hybrid_model.py, then
split by content severity so the response action has three levels
instead of a binary leak/no-leak call:

    * Unrestricted content, OR
      sensitive content that stays internal with normal-looking volume  -> ALLOW
    * Internal content leaving the org or behaving anomalously          -> ALERT
    * Restricted content leaving the org or behaving anomalously        -> BLOCK

This keeps the decision engine consistent with, and easy to compare
against, the binary hybrid predictor used for RO3 evaluation.
"""

import os
from dataclasses import dataclass, asdict
from typing import Optional

import pandas as pd

from content_classifier import ContentClassifier
from anomaly_detector import AnomalyDetector
from evaluate_hybrid_model import EXTERNAL_DESTINATIONS

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "evaluation_events.csv")
DECISION_LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "output", "decision_log.csv")

RESTRICTED = "Restricted"
INTERNAL = "Internal"
UNRESTRICTED = "Unrestricted"

ALLOW = "ALLOW"
ALERT = "ALERT"
BLOCK = "BLOCK"


@dataclass
class TransferEvent:
    """A single content-transfer event, as shown at the top of Figure 3.1."""
    user: str
    text: str
    volume_mb: float
    destination: str
    event_id: Optional[int] = None


@dataclass
class DecisionLogEntry:
    """One row of decision_log.csv."""
    event_id: Optional[int]
    user: str
    destination: str
    volume_mb: float
    predicted_content_label: str
    baseline_mean_mb: float
    baseline_std_mb: float
    z_score: float
    is_anomalous: bool
    decision: str


class DecisionEngine:
    """Combines the content-classification and anomaly signals into a
    three-way response action (ALLOW / ALERT / BLOCK)."""

    def __init__(self, external_destinations=EXTERNAL_DESTINATIONS):
        self.external_destinations = external_destinations

    def decide(self, content_label: str, destination: str, is_anomalous: bool) -> str:
        going_external = destination in self.external_destinations
        content_flagged = content_label in (RESTRICTED, INTERNAL)

        # Neither signal raises concern -> let it through.
        if not content_flagged or (not going_external and not is_anomalous):
            return ALLOW

        # From here, content is sensitive AND (leaving the org or behaving
        # anomalously) -- severity of the response depends on how sensitive.
        if content_label == RESTRICTED:
            return BLOCK
        return ALERT


class DLPFramework:
    """Top-level orchestrator: trains/holds the two detectors and the
    decision engine, and evaluates individual transfer events or a batch
    CSV of events end to end."""

    def __init__(self):
        self.content_classifier = ContentClassifier()
        self.content_classifier.train(verbose=False)
        self.anomaly_detector = AnomalyDetector()
        self.decision_engine = DecisionEngine()

    def evaluate_event(self, event: TransferEvent) -> DecisionLogEntry:
        content_label = self.content_classifier.classify(event.text)
        anomaly = self.anomaly_detector.check_event(event.user, event.volume_mb)
        decision = self.decision_engine.decide(content_label, event.destination, anomaly.is_anomalous)

        return DecisionLogEntry(
            event_id=event.event_id,
            user=event.user,
            destination=event.destination,
            volume_mb=event.volume_mb,
            predicted_content_label=content_label,
            baseline_mean_mb=anomaly.baseline_mean,
            baseline_std_mb=anomaly.baseline_std,
            z_score=anomaly.z_score,
            is_anomalous=anomaly.is_anomalous,
            decision=decision,
        )

    def run_batch(self, events_path: str = DATA_PATH, log_path: str = DECISION_LOG_PATH) -> pd.DataFrame:
        events_df = pd.read_csv(events_path)
        entries = []
        for _, row in events_df.iterrows():
            event = TransferEvent(
                event_id=row.get("event_id"),
                user=row["user"],
                text=row["text"],
                volume_mb=row["volume_mb"],
                destination=row["destination"],
            )
            entries.append(asdict(self.evaluate_event(event)))

        log_df = pd.DataFrame(entries)

        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        log_df.to_csv(log_path, index=False)
        return log_df


def main():
    framework = DLPFramework()
    log_df = framework.run_batch()

    print(f"Processed {len(log_df)} transfer events -> {DECISION_LOG_PATH}")
    print("\nResponse action counts:")
    print(log_df["decision"].value_counts().reindex([ALLOW, ALERT, BLOCK]).fillna(0).astype(int))

    print("\n--- Sample live-event checks ---")
    samples = [
        TransferEvent(user="alice", text="Quarterly team lunch is scheduled for Friday at noon.",
                      volume_mb=12, destination="internal_drive"),
        TransferEvent(user="alice", text="Internal use only: preliminary sales figures for the current quarter.",
                      volume_mb=180, destination="personal_email"),
        TransferEvent(user="alice", text="CONFIDENTIAL: customer SSN 555-11-2222 and card number 4111111111111111.",
                      volume_mb=6000, destination="external_usb"),
    ]
    for event in samples:
        entry = framework.evaluate_event(event)
        print(f"[{entry.decision:5}] user={entry.user:6} dest={entry.destination:15} "
              f"label={entry.predicted_content_label:12} z={entry.z_score:>7} :: {event.text[:60]}")


if __name__ == "__main__":
    main()
