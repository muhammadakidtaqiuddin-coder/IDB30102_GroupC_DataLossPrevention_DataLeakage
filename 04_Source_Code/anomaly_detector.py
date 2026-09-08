"""
anomaly_detector.py
--------------------
Behavior-based anomaly detection component.

Reference: Yadav, I., & Gupta, H. (2023). Designing data loss prevention
system for the enhancement of data integrity in cyberspace -- behavior-based
DLP layer. El Moudni, M., & Ziyati, E. (2023) -- insider trust/profiling
concept, adapted here as a simple statistical baseline-deviation check
per user. Supports RO2 by flagging transfer volumes that deviate sharply
from an individual user's established baseline behavior.

PRELIMINARY implementation: uses a simple mean + standard-deviation
(z-score) threshold per user as the baseline model. A production system
would use a more sophisticated model (e.g., the GAT/Transformer approach
of Ren, 2026, or a trust-scoring model as in El Moudni & Ziyati, 2023).
"""

import pandas as pd
import os
from dataclasses import dataclass

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sample_activity_log.csv")

Z_SCORE_THRESHOLD = 2.0


@dataclass
class AnomalyResult:
    user: str
    day: int
    volume_mb: float
    baseline_mean: float
    baseline_std: float
    z_score: float
    is_anomalous: bool


class AnomalyDetector:
    """Flags user data-transfer events that deviate significantly from that user's baseline."""

    def __init__(self, log_path: str = DATA_PATH, z_threshold: float = Z_SCORE_THRESHOLD):
        self.log_path = log_path
        self.z_threshold = z_threshold
        self.df = pd.read_csv(log_path)

    def detect(self) -> list:
        results = []
        for user, group in self.df.groupby("user"):
            mean = group["volume_mb"].mean()
            std = group["volume_mb"].std(ddof=0) or 1e-6  # avoid divide-by-zero

            for _, row in group.iterrows():
                z = (row["volume_mb"] - mean) / std
                results.append(
                    AnomalyResult(
                        user=user,
                        day=int(row["day"]),
                        volume_mb=row["volume_mb"],
                        baseline_mean=round(mean, 2),
                        baseline_std=round(std, 2),
                        z_score=round(z, 2),
                        is_anomalous=abs(z) >= self.z_threshold,
                    )
                )
        return results

    def check_event(self, user: str, volume_mb: float) -> AnomalyResult:
        """Check a single new event against a user's historical baseline."""
        history = self.df[self.df["user"] == user]
        if history.empty:
            # Unknown user -> treat as anomalous by default (no baseline to compare against)
            return AnomalyResult(user, -1, volume_mb, 0, 0, float("inf"), True)

        mean = history["volume_mb"].mean()
        std = history["volume_mb"].std(ddof=0) or 1e-6
        z = (volume_mb - mean) / std
        return AnomalyResult(
            user=user,
            day=-1,
            volume_mb=volume_mb,
            baseline_mean=round(mean, 2),
            baseline_std=round(std, 2),
            z_score=round(z, 2),
            is_anomalous=abs(z) >= self.z_threshold,
        )


if __name__ == "__main__":
    detector = AnomalyDetector()
    print("--- Historical log anomaly scan ---")
    for r in detector.detect():
        flag = "  <-- ANOMALY" if r.is_anomalous else ""
        print(f"{r.user:6} day{r.day} vol={r.volume_mb:>7} z={r.z_score:>6}{flag}")

    print("\n--- New event check ---")
    new_event = detector.check_event("alice", 850)
    print(new_event)
