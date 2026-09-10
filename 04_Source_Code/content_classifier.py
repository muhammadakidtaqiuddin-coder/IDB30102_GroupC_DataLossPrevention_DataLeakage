"""
content_classifier.py
----------------------
Content-based classification component (Technique 1 of the hybrid model).

Reference: Gupta, K., & Kush, A. (2023a). A learning oriented DLP system
based on classification model. Uses TF-IDF feature extraction with a
Gradient Boosting classifier to label content sensitivity as Restricted,
Internal, or Unrestricted. Supports RO2 (design/develop) as the
content-based half of the proposed hybrid classification-and-anomaly
model described in Chapter 3.

PRELIMINARY / PROOF-OF-CONCEPT: trained on a small synthetic dataset,
consistent with the proposal-stage scope in the assignment brief.
"""

import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sample_documents.csv")


class ContentClassifier:
    """TF-IDF + Gradient Boosting pipeline for content sensitivity classification."""

    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=500, ngram_range=(1, 2))
        self.model = GradientBoostingClassifier(random_state=42)
        self.is_trained = False

    def train(self, data_path: str = DATA_PATH, test_size: float = 0.25, verbose: bool = True):
        df = pd.read_csv(data_path)
        X_train, X_test, y_train, y_test = train_test_split(
            df["text"], df["label"], test_size=test_size, random_state=42, stratify=df["label"]
        )
        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)

        self.model.fit(X_train_vec, y_train)
        self.is_trained = True

        preds = self.model.predict(X_test_vec)
        acc = accuracy_score(y_test, preds)
        if verbose:
            print(f"[ContentClassifier] Held-out test accuracy: {acc:.2%}")
            print(classification_report(y_test, preds, zero_division=0))
        return acc

    def classify(self, text: str) -> str:
        if not self.is_trained:
            raise RuntimeError("Classifier must be trained before use.")
        vec = self.vectorizer.transform([text])
        return self.model.predict(vec)[0]


if __name__ == "__main__":
    clf = ContentClassifier()
    clf.train()
    samples = [
        "Please review the lunch menu for this week's cafeteria options.",
        "Internal draft budget for Q4, department heads only.",
        "CONFIDENTIAL: customer SSN 555-11-2222 and card number 4111111111111111.",
    ]
    print("\n--- Sample predictions ---")
    for s in samples:
        print(f"[{clf.classify(s)}]  {s}")
