"""
anomaly_detector.py
--------------------
Behavior-based anomaly detection component (Technique 2 of the hybrid model).

Reference: Yadav, I., & Gupta, H. (2023). Designing data loss prevention
system for the enhancement of data integrity in cyberspace -- behavioral
monitoring layer. El Moudni, M., & Ziyati, E. (2023) -- insider
trust/profiling concept, adapted here as a per-user statistical baseline
deviation check. Supports RO2 as the behavior-based half of the hybrid
model.

PRELIMINARY implementation: z-score threshold vs. each user's own
historical transfer-volume baseline.
"""

import os
import pandas as pd
from dataclasses import dataclass

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sample_activity_log.csv")
Z_SCORE_THRESHOLD = 2.0


@dataclass
class AnomalyResult:
    user: str
    volume_mb: float
    baseline_mean: float
    baseline_std: float
    z_score: float
    is_anomalous: bool


class AnomalyDetector:
    """Flags transfer volumes that deviate significantly from a user's baseline."""

    def __init__(self, log_path: str = DATA_PATH, z_threshold: float = Z_SCORE_THRESHOLD):
        self.df = pd.read_csv(log_path)
        self.z_threshold = z_threshold

    def check_event(self, user: str, volume_mb: float) -> AnomalyResult:
        history = self.df[self.df["user"] == user]
        if history.empty:
            return AnomalyResult(user, volume_mb, 0, 0, float("inf"), True)

        mean = history["volume_mb"].mean()
        std = history["volume_mb"].std(ddof=0) or 1e-6
        z = (volume_mb - mean) / std
        return AnomalyResult(
            user=user,
            volume_mb=volume_mb,
            baseline_mean=round(mean, 2),
            baseline_std=round(std, 2),
            z_score=round(z, 2),
            is_anomalous=abs(z) >= self.z_threshold,
        )


if __name__ == "__main__":
    detector = AnomalyDetector()
    print("--- Sample anomaly checks ---")
    for user, vol in [("alice", 12), ("alice", 900), ("bob", 22), ("carol", 1100)]:
        r = detector.check_event(user, vol)
        flag = "  <-- ANOMALY" if r.is_anomalous else ""
        print(f"{r.user:6} vol={r.volume_mb:>6} z={r.z_score:>6}{flag}")
