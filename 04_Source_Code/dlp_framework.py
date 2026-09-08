"""
dlp_framework.py
-----------------
Main integration pipeline for the proposed hybrid DLP framework.

Combines:
  1. Content Classification  (content_classifier.py)   -> sensitivity label
  2. Pattern/Signature Detection (pattern_detector.py)  -> known sensitive patterns
  3. Behavioral Anomaly Detection (anomaly_detector.py) -> deviation from user baseline

Decision logic follows the hybrid feedback-style pipeline of Srivastava
et al. (2024) and the four-stage hybrid methodology of Yadav & Gupta
(2023): classify -> detect (signature + behavior) -> decide -> log/report.

This corresponds to DSR Phase 3 (Design & Development) and Phase 4
(Demonstration) described in Chapter 3 of the Research Proposal.
"""

import os
import csv
from dataclasses import dataclass, asdict
from datetime import datetime

from content_classifier import ContentClassifier
from pattern_detector import PatternDetector
from anomaly_detector import AnomalyDetector

OUTPUT_LOG = os.path.join(os.path.dirname(__file__), "..", "output", "decision_log.csv")


@dataclass
class TransferEvent:
    event_id: int
    user: str
    filename: str
    content: str
    volume_mb: float
    destination: str


@dataclass
class Decision:
    event_id: int
    user: str
    filename: str
    destination: str
    sensitivity_label: str
    signature_matches: str
    anomaly_flag: bool
    z_score: float
    action: str
    reason: str
    timestamp: str


class DLPFramework:
    """Orchestrates classification, signature detection, and anomaly detection
    into a single allow/alert/block decision per event."""

    def __init__(self):
        self.classifier = ContentClassifier()
        self.classifier.train()  # preliminary: retrain each run for demo purposes
        self.pattern_detector = PatternDetector()
        self.anomaly_detector = AnomalyDetector()

    def evaluate(self, event: TransferEvent) -> Decision:
        # Stage 1: Content classification
        sensitivity = self.classifier.classify(event.content)

        # Stage 2: Signature/pattern detection
        pattern_result = self.pattern_detector.scan(event.content)

        # Stage 3: Behavioral anomaly detection
        anomaly_result = self.anomaly_detector.check_event(event.user, event.volume_mb)

        # Decision logic (hybrid rule combining all three signals)
        action, reason = self._decide(sensitivity, pattern_result, anomaly_result, event)

        return Decision(
            event_id=event.event_id,
            user=event.user,
            filename=event.filename,
            destination=event.destination,
            sensitivity_label=sensitivity,
            signature_matches=";".join(pattern_result.matches) if pattern_result.matches else "none",
            anomaly_flag=anomaly_result.is_anomalous,
            z_score=anomaly_result.z_score,
            action=action,
            reason=reason,
            timestamp=datetime.now().isoformat(timespec="seconds"),
        )

    @staticmethod
    def _decide(sensitivity, pattern_result, anomaly_result, event: TransferEvent):
        """
        Combined decision rule:
        - BLOCK   : Restricted content leaving via an external destination,
                    OR restricted content with a signature match AND anomalous transfer.
        - ALERT   : Internal/Restricted content with any single risk signal
                    (signature match OR anomalous behavior), but not both.
        - ALLOW   : Unrestricted content with no signature matches and normal behavior.
        """
        external_destinations = {"external_usb", "cloud_upload", "personal_email"}
        going_external = event.destination in external_destinations

        if sensitivity == "Restricted" and going_external:
            return "BLOCK", "Restricted content attempted transfer to an external destination."

        if sensitivity == "Restricted" and pattern_result.matched and anomaly_result.is_anomalous:
            return "BLOCK", "Restricted content with signature match and anomalous transfer volume."

        if sensitivity in ("Restricted", "Internal") and (pattern_result.matched or anomaly_result.is_anomalous):
            return "ALERT", "Sensitive content flagged by signature detection or behavioral anomaly."

        if sensitivity == "Unrestricted" and not pattern_result.matched and not anomaly_result.is_anomalous:
            return "ALLOW", "No sensitivity, signature, or behavioral risk detected."

        return "ALERT", "Default caution: partial risk signal detected."

    def run_batch(self, events):
        decisions = [self.evaluate(e) for e in events]
        self._log(decisions)
        return decisions

    @staticmethod
    def _log(decisions):
        os.makedirs(os.path.dirname(OUTPUT_LOG), exist_ok=True)
        with open(OUTPUT_LOG, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(asdict(decisions[0]).keys()))
            writer.writeheader()
            for d in decisions:
                writer.writerow(asdict(d))


def sample_events():
    return [
        TransferEvent(1, "bob", "team_lunch_invite.txt",
                      "Reminder: team lunch is scheduled for Friday at noon in the cafeteria.",
                      5, "internal_drive"),
        TransferEvent(2, "dave", "q3_roadmap.txt",
                      "Internal draft of the Q3 roadmap, please do not forward outside the department.",
                      12, "internal_drive"),
        TransferEvent(3, "alice", "payroll_export.txt",
                      "CONFIDENTIAL employee salary data, SSN 512-34-9876, restricted distribution.",
                      850, "external_usb"),
        TransferEvent(4, "carol", "customer_export.txt",
                      "Restricted database export with customer card number 4539148803436467.",
                      1200, "cloud_upload"),
        TransferEvent(5, "bob", "internal_notes.txt",
                      "Internal use only: draft meeting notes for next week's planning session.",
                      20, "internal_drive"),
    ]


if __name__ == "__main__":
    framework = DLPFramework()
    events = sample_events()
    decisions = framework.run_batch(events)

    print("\n=== DLP Framework Decision Log ===")
    for d in decisions:
        print(f"[{d.action:6}] user={d.user:6} file={d.filename:22} "
              f"sensitivity={d.sensitivity_label:12} sig={d.signature_matches:15} "
              f"anomaly={d.anomaly_flag} z={d.z_score:>6}  -> {d.reason}")

    print(f"\nFull decision log written to: {OUTPUT_LOG}")
