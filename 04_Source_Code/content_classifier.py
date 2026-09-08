"""
content_classifier.py
----------------------
Content-aware data sensitivity classifier.

Reference: Gupta, K., & Kush, A. (2020). A learning oriented DLP system
based on classification model. Uses TF-IDF feature extraction with a
Gradient Boosting classifier to label documents as Restricted, Internal,
or Unrestricted -- supporting RO2 (design/develop the framework's
classification component).

This is a PRELIMINARY / PROOF-OF-CONCEPT component trained on a small
synthetic dataset for demonstration purposes only, consistent with the
proposal-stage scope described in the assignment brief.
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sample_documents.csv")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "output", "classifier_model.joblib")
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), "..", "output", "vectorizer.joblib")


class ContentClassifier:
    """Wraps a TF-IDF + Gradient Boosting pipeline for document sensitivity classification."""

    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=500, ngram_range=(1, 2))
        self.model = GradientBoostingClassifier(random_state=42)
        self.is_trained = False

    def train(self, data_path: str = DATA_PATH, test_size: float = 0.25):
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
        report = classification_report(y_test, preds, zero_division=0)

        print(f"[ContentClassifier] Training complete. Test accuracy: {acc:.2%}")
        print(report)
        return acc, report

    def classify(self, text: str) -> str:
        if not self.is_trained:
            raise RuntimeError("Classifier must be trained before use. Call .train() first.")
        vec = self.vectorizer.transform([text])
        return self.model.predict(vec)[0]

    def save(self):
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        joblib.dump(self.model, MODEL_PATH)
        joblib.dump(self.vectorizer, VECTORIZER_PATH)

    def load(self):
        self.model = joblib.load(MODEL_PATH)
        self.vectorizer = joblib.load(VECTORIZER_PATH)
        self.is_trained = True


if __name__ == "__main__":
    clf = ContentClassifier()
    clf.train()
    clf.save()

    samples = [
        "Please review the lunch menu for this week's cafeteria options.",
        "Internal draft budget for Q4, department heads only.",
        "CONFIDENTIAL: customer SSN 555-11-2222 and card number 4111111111111111.",
    ]
    print("\n--- Sample predictions ---")
    for s in samples:
        print(f"[{clf.classify(s)}]  {s}")
