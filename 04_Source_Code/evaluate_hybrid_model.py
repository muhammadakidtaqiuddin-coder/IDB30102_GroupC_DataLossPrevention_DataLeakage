"""
evaluate_hybrid_model.py
--------------------------
RO3: Evaluates the detection accuracy of the hybrid classification-and-
anomaly model against single-technique baselines (content-classification-
only, and anomaly-detection-only), using the labeled evaluation set from
generate_evaluation_dataset.py.

Three prediction strategies are compared, each producing a binary
leak/no-leak prediction for every event:

  1. Classification-only  : predicted_leak = classifier says
                             Restricted/Internal (ignores destination
                             and behavior entirely)
  2. Anomaly-only          : predicted_leak = behavioral anomaly flagged
                             (ignores content sensitivity entirely)
  3. Hybrid (proposed)     : predicted_leak = classifier says
                             Restricted/Internal AND (external
                             destination OR anomaly flagged)

Metrics: Accuracy, Precision, Recall, F1-score, False Positive Rate,
per Chapter 3, Section 3.9 of the Research Proposal.
"""

import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

from content_classifier import ContentClassifier
from anomaly_detector import AnomalyDetector

EVAL_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "evaluation_events.csv")
RESULTS_PATH = os.path.join(os.path.dirname(__file__), "..", "output", "evaluation_results.csv")

EXTERNAL_DESTINATIONS = {"external_usb", "cloud_upload", "personal_email"}


def compute_metrics(y_true, y_pred, name):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[False, True]).ravel()
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0
    return {
        "approach": name,
        "accuracy": round(acc, 3),
        "precision": round(prec, 3),
        "recall": round(rec, 3),
        "f1_score": round(f1, 3),
        "false_positive_rate": round(fpr, 3),
    }


def main():
    if not os.path.exists(EVAL_PATH):
        raise FileNotFoundError(
            f"{EVAL_PATH} not found. Run generate_evaluation_dataset.py first."
        )
    events = pd.read_csv(EVAL_PATH)

    classifier = ContentClassifier()
    classifier.train(verbose=False)
    anomaly_detector = AnomalyDetector()

    classification_only_preds = []
    anomaly_only_preds = []
    hybrid_preds = []

    for _, row in events.iterrows():
        predicted_label = classifier.classify(row["text"])
        anomaly_result = anomaly_detector.check_event(row["user"], row["volume_mb"])
        going_external = row["destination"] in EXTERNAL_DESTINATIONS
        content_flagged = predicted_label in ("Restricted", "Internal")

        classification_only_preds.append(content_flagged)
        anomaly_only_preds.append(anomaly_result.is_anomalous)
        hybrid_preds.append(content_flagged and (going_external or anomaly_result.is_anomalous))

    y_true = events["ground_truth_leak"].tolist()

    results = [
        compute_metrics(y_true, classification_only_preds, "Classification-only (baseline)"),
        compute_metrics(y_true, anomaly_only_preds, "Anomaly-only (baseline)"),
        compute_metrics(y_true, hybrid_preds, "Hybrid classification + anomaly (proposed)"),
    ]

    results_df = pd.DataFrame(results)
    os.makedirs(os.path.dirname(RESULTS_PATH), exist_ok=True)
    results_df.to_csv(RESULTS_PATH, index=False)

    print("\n=== Evaluation: Hybrid Model vs. Single-Technique Baselines ===")
    print(results_df.to_string(index=False))
    print(f"\nFull results written to: {RESULTS_PATH}")


if __name__ == "__main__":
    main()
