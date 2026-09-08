"""
pattern_detector.py
--------------------
Signature-based detection component.

Reference: Srivastava, A., Sharma, V. S., Srivastava, P., & Pillai, A.
(2024). A hybrid framework for data loss prevention and detection --
signature-based prevention layer. Scans content for known sensitive
data patterns (SSNs, credit card numbers, API keys/passwords, keywords)
using regular expressions. Supports RO2 by providing the rule-based
half of the hybrid detection pipeline.
"""

import re
from dataclasses import dataclass, field
from typing import List


@dataclass
class DetectionResult:
    matched: bool
    matches: List[str] = field(default_factory=list)


PATTERNS = {
    "SSN": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "CREDIT_CARD": re.compile(r"\b(?:\d[ -]*?){13,16}\b"),
    "API_KEY": re.compile(r"\b(?:api[_-]?key|secret[_-]?key)\s*[:=]\s*\S+", re.IGNORECASE),
    "BANK_ACCOUNT": re.compile(r"\bbank account\s*\d{6,}\b", re.IGNORECASE),
}

SENSITIVE_KEYWORDS = [
    "confidential",
    "restricted",
    "do not distribute",
    "do not forward",
    "internal use only",
    "trade secret",
]


class PatternDetector:
    """Rule-based (signature) scanner for sensitive content patterns and keywords."""

    def scan(self, text: str) -> DetectionResult:
        matches = []

        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                matches.append(label)

        lowered = text.lower()
        for keyword in SENSITIVE_KEYWORDS:
            if keyword in lowered:
                matches.append(f"KEYWORD:{keyword}")

        return DetectionResult(matched=len(matches) > 0, matches=matches)


if __name__ == "__main__":
    detector = PatternDetector()
    samples = [
        "Please review the cafeteria menu for this week.",
        "CONFIDENTIAL: employee SSN 512-34-9876, do not distribute.",
        "Customer card number 4539148803436467 flagged for review.",
        "api_key=sk_live_29d8f7ah3k must be rotated immediately.",
    ]
    for s in samples:
        result = detector.scan(s)
        print(f"Matched={result.matched:5} Matches={result.matches}  | {s}")
