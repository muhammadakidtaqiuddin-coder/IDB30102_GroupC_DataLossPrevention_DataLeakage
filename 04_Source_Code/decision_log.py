"""
decision_log.py
-----------------
Structured decision log for the Hybrid Classification and Anomaly-Based
Detection Prototype (supports Chapter 3, Methodology, of the Research
Proposal: Improving Data Leakage Detection Accuracy Through a Hybrid
Classification and Anomaly-Based Approach for Organizational Networks).

Each entry records a design decision made while building the prototype:
what was decided, why, what alternatives were considered, and its current
status. Kept as data (not prose) so it can be queried, filtered, exported,
or rendered in different formats.

Run this file directly to print a formatted decision log, or import
DECISIONS / get_decision() / to_markdown() to use it elsewhere.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Decision:
    id: str
    title: str
    decision: str
    rationale: str
    alternatives_considered: str
    status: str
    related_files: List[str] = field(default_factory=list)


DECISIONS: List[Decision] = [
    Decision(
        id="DL-01",
        title="Use two independent detection techniques, combined into one hybrid decision",
        decision=(
            "Build content classification and behavioral anomaly detection as two "
            "separate, independently-testable components, then combine their outputs "
            "into a single hybrid verdict rather than training one end-to-end model."
        ),
        rationale=(
            "Keeping the techniques separate lets each be evaluated on its own as well "
            "as in combination, which is what RO3 requires: a comparative evaluation of "
            "hybrid vs. single-technique baselines, not just a hybrid score in isolation."
        ),
        alternatives_considered=(
            "A single joint model (e.g. one classifier trained on both text and "
            "behavioral features) was rejected for this stage -- it would prevent the "
            "side-by-side baseline comparison the research objective calls for, and adds "
            "complexity that isn't justified at proof-of-concept scale."
        ),
        status="Adopted",
        related_files=["content_classifier.py", "anomaly_detector.py", "evaluate_hybrid_model.py"],
    ),
    Decision(
        id="DL-02",
        title="Content classification: TF-IDF + Gradient Boosting",
        decision=(
            "Represent document text with TF-IDF (max 500 features, unigrams + bigrams) "
            "and classify sensitivity (Restricted / Internal / Unrestricted) with a "
            "Gradient Boosting classifier."
        ),
        rationale=(
            "Directly adapted from Gupta & Kush (2023a), the reference technique cited "
            "for the content-classification half of the hybrid model. TF-IDF + gradient "
            "boosting trains on a small synthetic corpus without a GPU or external "
            "embeddings, which fits a proposal-stage prototype."
        ),
        alternatives_considered=(
            "Transformer-based embeddings or a pretrained NLP model would likely "
            "generalize better but are disproportionate for a 30-document synthetic "
            "dataset and would obscure the direct link to the cited methodology."
        ),
        status="Adopted (preliminary -- see DL-06)",
        related_files=["content_classifier.py"],
    ),
    Decision(
        id="DL-03",
        title="Behavioral detection: single-variable z-score vs. per-user baseline",
        decision=(
            "Flag a transfer as anomalous when its volume deviates from that user's own "
            "historical mean by more than Z_SCORE_THRESHOLD = 2.0 standard deviations."
        ),
        rationale=(
            "Adapted from Yadav & Gupta (2023) and the insider-profiling concept in "
            "El Moudni & Ziyati (2023). A per-user baseline (rather than an "
            "organization-wide threshold) captures that 'normal' transfer volume varies "
            "a lot by role, which a single global cutoff would miss. Roughly 95% of a "
            "normal distribution falls within 2 standard deviations, so z=2.0 flags "
            "about the top ~5% most unusual transfers per user -- a defensible starting "
            "threshold rather than a tuned production value."
        ),
        alternatives_considered=(
            "A multivariate behavioral model (time of day, file type, destination "
            "history) was considered but deferred -- it needs more behavioral signal "
            "than the synthetic activity log currently provides, and a single clear "
            "variable keeps this component's contribution to the hybrid result easy to "
            "isolate and interpret."
        ),
        status="Adopted (preliminary -- see DL-06)",
        related_files=["anomaly_detector.py"],
    ),
    Decision(
        id="DL-04",
        title="Hybrid combination rule: content flag AND (external destination OR anomaly)",
        decision=(
            "The hybrid predicts a leak when the content classifier flags the item as "
            "Restricted/Internal AND either the destination is external or the anomaly "
            "detector fires -- not when either signal fires alone."
        ),
        rationale=(
            "An AND-based gate on content sensitivity, widened by an OR across "
            "destination/behavior, catches cases that defeat either baseline alone: "
            "sensitive content sent externally at normal volume (misses anomaly-only "
            "detection), and a volume spike of non-sensitive content (misses "
            "content-only detection, and correctly should not be flagged as a leak)."
        ),
        alternatives_considered=(
            "A simple OR-of-both-signals rule was rejected -- it would inflate false "
            "positives (any anomaly on non-sensitive content would trigger a flag) and "
            "would not reflect the actual leakage definition in DL-05."
        ),
        status="Adopted -- core mechanism behind the RO3 evaluation result",
        related_files=["evaluate_hybrid_model.py"],
    ),
    Decision(
        id="DL-05",
        title="Ground-truth label defined independently of either detector",
        decision=(
            "ground_truth_leak is computed from the true (not predicted) content "
            "sensitivity plus destination and whether volume was an injected spike -- "
            "never from either detector's own output."
        ),
        rationale=(
            "If ground truth were derived from what the detectors themselves observe, "
            "the 'hybrid outperforms both baselines' result would be circular. Defining "
            "it from the underlying simulated facts keeps the comparison a fair test of "
            "detection accuracy rather than a self-fulfilling one."
        ),
        alternatives_considered=(
            "Deriving ground truth from detector agreement/output was rejected outright "
            "as methodologically circular."
        ),
        status="Adopted",
        related_files=["generate_evaluation_dataset.py"],
    ),
    Decision(
        id="DL-06",
        title="Synthetic data only, explicitly scoped as preliminary",
        decision=(
            "All data (sample_documents.csv, sample_activity_log.csv, "
            "evaluation_events.csv; 150 generated events, fixed random seed 42) is "
            "synthetic. No real, confidential, or organizational data is used."
        ),
        rationale=(
            "Required per Chapter 3, Section 3.8 of the Research Proposal. A fixed seed "
            "also makes the reported evaluation numbers reproducible run to run."
        ),
        alternatives_considered=(
            "Using anonymized or sampled real organizational data was not pursued, "
            "consistent with the ethical scope defined in the proposal."
        ),
        status=(
            "Adopted for proposal stage. Known limitations: classifier trained on only "
            "30 synthetic documents; ground-truth rule is a simplification of real "
            "leakage risk; anomaly detector uses volume only, not time-of-day/file "
            "type/destination history. Revisit before any production-oriented follow-up."
        ),
        related_files=["generate_evaluation_dataset.py", "data/"],
    ),
    Decision(
        id="DL-07",
        title="Repository folder mapping for GitHub submission",
        decision=(
            "Keep local folder names (src/, data/, diagrams/, output/) but map them to "
            "numbered submission folders on GitHub: diagrams/ -> "
            "03_Architecture_and_Flowchart/, src/ -> 04_Source_Code/, data/ -> "
            "05_Data_or_Sample_Input/, output/ -> 06_Results_or_Expected_Output/."
        ),
        rationale=(
            "Matches the submission structure expected for the research proposal "
            "deliverable while keeping the working repo's internal names conventional "
            "for a Python project."
        ),
        alternatives_considered=(
            "Renaming the working folders directly to the numbered scheme was rejected "
            "-- it would make the repo less conventional to develop in day-to-day."
        ),
        status="Adopted -- see README.md for the authoritative mapping table",
        related_files=["README.md"],
    ),
]


def get_decision(decision_id: str) -> Optional[Decision]:
    """Look up a single decision by its ID (e.g. 'DL-03')."""
    for d in DECISIONS:
        if d.id == decision_id:
            return d
    return None


def to_markdown(decisions: List[Decision] = DECISIONS) -> str:
    """Render the decision log as a Markdown document."""
    lines = ["# Decision Log — Hybrid Classification and Anomaly-Based Detection Prototype", ""]
    for d in decisions:
        lines.append(f"## {d.id} — {d.title}")
        lines.append("")
        lines.append(f"**Decision:** {d.decision}")
        lines.append("")
        lines.append(f"**Rationale:** {d.rationale}")
        lines.append("")
        lines.append(f"**Alternatives considered:** {d.alternatives_considered}")
        lines.append("")
        lines.append(f"**Status:** {d.status}")
        if d.related_files:
            lines.append("")
            lines.append(f"**Related files:** {', '.join(d.related_files)}")
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


def print_log() -> None:
    """Print a readable, terminal-friendly version of the decision log."""
    for d in DECISIONS:
        print(f"[{d.id}] {d.title}")
        print(f"  Decision:     {d.decision}")
        print(f"  Rationale:    {d.rationale}")
        print(f"  Alternatives: {d.alternatives_considered}")
        print(f"  Status:       {d.status}")
        if d.related_files:
            print(f"  Files:        {', '.join(d.related_files)}")
        print()


if __name__ == "__main__":
    print_log()
