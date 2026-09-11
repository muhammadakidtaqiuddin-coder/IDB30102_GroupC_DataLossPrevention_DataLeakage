# Decision Log — Hybrid Classification and Anomaly-Based Detection Prototype

This log records the key design decisions made while building the prototype supporting
Chapter 3 (Methodology) of the research proposal *Improving Data Leakage Detection Accuracy
Through a Hybrid Classification and Anomaly-Based Approach for Organizational Networks*.

Format: each entry captures what was decided, why, what alternatives were considered, and
the status of the decision.

---

## DL-01 — Use two independent detection techniques, combined into one hybrid decision

**Decision:** Build content classification and behavioral anomaly detection as two
separate, independently-testable components, then combine their outputs into a single
hybrid verdict rather than training one end-to-end model.

**Rationale:** Keeping the techniques separate lets each be evaluated on its own
(`content_classifier.py`, `anomaly_detector.py`) as well as in combination
(`evaluate_hybrid_model.py`), which is what RO3 requires — a *comparative* evaluation of
hybrid vs. single-technique baselines, not just a hybrid score in isolation.

**Alternatives considered:** A single joint model (e.g. one classifier trained on both
text and behavioral features) was rejected for this stage — it would prevent the
side-by-side baseline comparison the research objective calls for, and adds complexity
that isn't justified at proof-of-concept scale.

**Status:** Adopted.

---

## DL-02 — Content classification: TF-IDF + Gradient Boosting

**Decision:** Represent document text with TF-IDF (max 500 features, unigrams + bigrams)
and classify sensitivity (`Restricted` / `Internal` / `Unrestricted`) with a Gradient
Boosting classifier.

**Rationale:** Directly adapted from Gupta & Kush (2023a), which the proposal cites as the
reference technique for the content-classification half of the hybrid model. TF-IDF +
gradient boosting is lightweight enough to train on a small synthetic corpus and needs no
GPU or external embeddings, which fits a proposal-stage prototype.

**Alternatives considered:** Transformer-based embeddings or a pretrained NLP model would
likely generalize better but are disproportionate for a 30-document synthetic dataset and
would obscure the direct link to the cited methodology.

**Status:** Adopted. Flagged as preliminary — see DL-06 (known limitations).

---

## DL-03 — Behavioral detection: single-variable z-score vs. per-user baseline

**Decision:** Flag a transfer as anomalous when its volume deviates from that user's own
historical mean by more than `Z_SCORE_THRESHOLD = 2.0` standard deviations.

**Rationale:** Adapted from Yadav & Gupta (2023) and the insider-profiling concept in
El Moudni & Ziyati (2023). A per-user baseline (rather than an organization-wide
threshold) captures that "normal" transfer volume varies a lot by role, which a single
global cutoff would miss.

**Alternatives considered:** A multivariate behavioral model (time of day, file type,
destination history) was considered but deferred — it needs more behavioral signal than
the synthetic activity log currently provides, and a single clear variable keeps this
component's contribution to the hybrid result easy to isolate and interpret.

**z=2.0 threshold rationale:** ~95% of a normal distribution falls within 2 standard
deviations, so this flags roughly the top ~5% most unusual transfers per user — a
standard, defensible starting threshold for a first pass rather than a tuned production
value.

**Status:** Adopted. Flagged as preliminary — see DL-06.

---

## DL-04 — Hybrid combination rule: content flag AND (external destination OR anomaly)

**Decision:** The hybrid predicts a leak when the content classifier flags the item as
`Restricted`/`Internal` **and** either the destination is external or the anomaly
detector fires — not when either signal fires alone (`evaluate_hybrid_model.py`).

**Rationale:** An AND-based gate on content sensitivity, widened by an OR across
destination/behavior, was chosen so the hybrid can catch cases that defeat either
baseline alone:
- sensitive content sent externally at *normal* volume (misses anomaly-only detection),
- a volume spike of *non-sensitive* content (misses content-only detection, and correctly
  should not be flagged as a leak).

**Alternatives considered:** A simple OR-of-both-signals rule was rejected — it would
inflate false positives (any anomaly on non-sensitive content would trigger a flag) and
would not reflect the actual leakage definition below (DL-05).

**Status:** Adopted. This rule is the core mechanism the RO3 evaluation results support.

---

## DL-05 — Ground-truth label defined independently of either detector

**Decision:** In `generate_evaluation_dataset.py`, `ground_truth_leak` is computed from
the *true* (not predicted) content sensitivity plus destination and whether volume was an
injected spike — never from either detector's own output.

**Rationale:** If ground truth were derived from what the detectors themselves observe,
the "hybrid outperforms both baselines" result would be circular. Defining it from the
underlying simulated facts (true label, true destination, whether a spike was injected)
keeps the comparison a fair test of detection accuracy rather than a self-fulfilling one.

**Status:** Adopted. This is called out explicitly in the source comments and the README
as the basis for treating the RO3 result as valid.

---

## DL-06 — Synthetic data only, explicitly scoped as preliminary

**Decision:** All data (`sample_documents.csv`, `sample_activity_log.csv`,
`evaluation_events.csv`, 150 generated events, fixed random seed 42) is synthetic. No
real, confidential, or organizational data is used or required.

**Rationale:** Required per Chapter 3, Section 3.8 (ethical/data-handling constraints of
the proposal). A fixed seed also makes the reported evaluation numbers reproducible run to
run.

**Known limitations accepted at this stage:**
- Classifier trained on only 30 synthetic documents; a real deployment would need a much
  larger labeled corpus.
- The synthetic ground-truth rule is a simplification of real-world leakage risk; a
  production evaluation would use analyst-labeled historical incidents instead.
- The anomaly detector uses volume only; a fuller model would add time-of-day, file type,
  and destination history as features.

**Status:** Adopted for proposal stage. Revisit before any production-oriented follow-up.

---

## DL-07 — Repository folder mapping for GitHub submission

**Decision:** Keep local folder names (`src/`, `data/`, `diagrams/`, `output/`) but map
them to numbered submission folders on GitHub:

| Local folder | GitHub folder |
|---|---|
| `diagrams/` | `03_Architecture_and_Flowchart/` |
| `src/` | `04_Source_Code/` |
| `data/` | `05_Data_or_Sample_Input/` |
| `output/` | `06_Results_or_Expected_Output/` |

**Rationale:** Matches the submission structure expected for the research proposal
deliverable while keeping the working repo's internal names conventional for a Python
project.

**Status:** Adopted — see README.md for the authoritative mapping table.
