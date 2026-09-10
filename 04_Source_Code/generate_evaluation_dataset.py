"""
generate_evaluation_dataset.py
--------------------------------
Builds a labeled synthetic evaluation set of transfer events for RO3
(evaluate detection accuracy of the hybrid model vs. single-technique
baselines).

Each event has a GROUND-TRUTH leak label defined independently of what
either detector individually observes:

    ground_truth_leak = True  if  true_content_sensitivity != "Unrestricted"
                         AND (destination is external OR transfer volume is a spike)

This design intentionally creates cases that a content-only baseline
CANNOT catch (sensitive content sent at normal volume to an external
destination) and cases an anomaly-only baseline CANNOT catch (a volume
spike of non-sensitive content), so the comparative evaluation in
evaluate_hybrid_model.py is a fair test of whether combining both
techniques improves on either alone -- not a rigged result.
"""

import os
import random
import pandas as pd

DOCS_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sample_documents.csv")
LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sample_activity_log.csv")
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "evaluation_events.csv")

EXTERNAL_DESTINATIONS = {"external_usb", "cloud_upload", "personal_email"}
INTERNAL_DESTINATIONS = {"internal_drive"}
ALL_DESTINATIONS = list(EXTERNAL_DESTINATIONS | INTERNAL_DESTINATIONS)

random.seed(42)


def generate(n_events: int = 150):
    docs = pd.read_csv(DOCS_PATH)
    log = pd.read_csv(LOG_PATH)
    users = log["user"].unique().tolist()

    user_baseline = {
        u: log[log["user"] == u]["volume_mb"].mean() for u in users
    }

    rows = []
    for event_id in range(1, n_events + 1):
        doc_row = docs.sample(1, random_state=event_id).iloc[0]
        true_label = doc_row["label"]
        text = doc_row["text"]

        user = random.choice(users)
        destination = random.choice(ALL_DESTINATIONS)

        # 30% chance this event is a volume spike, otherwise near-normal for that user
        is_spike = random.random() < 0.30
        baseline = user_baseline[user]
        if is_spike:
            volume = baseline * random.uniform(8, 40)
        else:
            volume = baseline * random.uniform(0.6, 1.4)

        going_external = destination in EXTERNAL_DESTINATIONS
        ground_truth_leak = (true_label != "Unrestricted") and (going_external or is_spike)

        rows.append({
            "event_id": event_id,
            "user": user,
            "true_label": true_label,
            "text": text,
            "destination": destination,
            "volume_mb": round(volume, 1),
            "is_spike_injected": is_spike,
            "ground_truth_leak": ground_truth_leak,
        })

    df = pd.DataFrame(rows)
    df.to_csv(OUT_PATH, index=False)
    print(f"Generated {len(df)} evaluation events -> {OUT_PATH}")
    print(f"Ground-truth leak rate: {df['ground_truth_leak'].mean():.1%}")
    return df


if __name__ == "__main__":
    generate()
