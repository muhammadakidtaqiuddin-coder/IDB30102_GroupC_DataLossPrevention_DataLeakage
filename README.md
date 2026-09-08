# DLP Framework Prototype — Preliminary Source Code

Preliminary technical component supporting **Chapter 3 (Methodology)** of the Research Proposal:
*Design and Implementation of a Data Loss Prevention Framework for Mitigating Data Leakage in
Organizational Networks.*

This is a **proof-of-concept prototype**, consistent with the proposal-stage scope defined in the
assignment brief ("students are not required to develop a complete final system... relevant
preliminary technical components should be provided to demonstrate technical direction and
feasibility"). It is intended for `04_Source_Code/` in the GitHub repository.

---

## What this prototype demonstrates

A **hybrid DLP pipeline** combining three detection layers, following the multi-layer approach
justified in Chapter 3 (Yadav & Gupta, 2023) and the anomaly+signature hybrid architecture of
Srivastava et al. (2024):

| Component | File | Technique | Reference |
|---|---|---|---|
| Content Classification | `src/content_classifier.py` | TF-IDF + Gradient Boosting | Gupta & Kush (2020) |
| Signature Detection | `src/pattern_detector.py` | Regex pattern/keyword matching | Srivastava et al. (2024) |
| Behavioral Anomaly Detection | `src/anomaly_detector.py` | Z-score deviation from user baseline | Yadav & Gupta (2023); El Moudni & Ziyati (2023) |
| Integration Pipeline | `src/dlp_framework.py` | Combined decision logic + logging | — |

## Pipeline flow

```
Transfer Event (user, file content, volume, destination)
        │
        ▼
 [1] Content Classifier  ──► Sensitivity: Restricted / Internal / Unrestricted
        │
        ▼
 [2] Pattern Detector    ──► Signature matches: SSN, credit card, API key, keywords
        │
        ▼
 [3] Anomaly Detector    ──► Behavioral deviation (z-score) vs. user baseline
        │
        ▼
 [4] Decision Engine     ──► ALLOW / ALERT / BLOCK  (+ logged reason)
        │
        ▼
   decision_log.csv  (continuous monitoring/reporting output)
```

This directly mirrors the architecture diagram and flowchart described in Chapter 3, Section 3.5,
and should be kept consistent with the diagrams placed in `03_Architecture_and_Flowchart/`.

## Mapping to Research Objectives

| Objective | How this prototype supports it |
|---|---|
| RO1 — Study existing methods | Techniques (TF-IDF classification, hybrid signature+anomaly detection) are directly adapted from the reviewed literature (see Chapter 2 / `01_Research_Papers/`) |
| RO2 — Design and develop | This prototype **is** the preliminary implementation of the proposed framework's three detection layers and decision engine |
| RO3 — Test and evaluate | `output/decision_log.csv` and classifier accuracy/F1 metrics provide the basis for the Evaluation Plan in Chapter 3, Section 3.8 |

## How to run

```bash
pip install pandas scikit-learn joblib
cd src
python3 dlp_framework.py
```

This will:
1. Train the content classifier on `data/sample_documents.csv` (prints accuracy/F1 report)
2. Evaluate 5 sample transfer events through the full pipeline
3. Write the full decision log to `output/decision_log.csv`

Individual components can also be run/tested standalone:
```bash
python3 content_classifier.py
python3 pattern_detector.py
python3 anomaly_detector.py
```

## Sample data

- `data/sample_documents.csv` — 30 synthetic labeled documents (Restricted / Internal / Unrestricted) for training the classifier
- `data/sample_activity_log.csv` — synthetic per-user daily file-transfer volumes, used to establish behavioral baselines

**No real, confidential, or organizational data is used** — all data is synthetic, created for
demonstration purposes only, per the assignment's data-handling requirements.

## Known limitations (preliminary stage)

- Classifier is trained on a very small synthetic dataset (30 samples) — accuracy/F1 figures are
  illustrative only, not representative of real-world performance.
- Anomaly detection uses a simple z-score threshold; as observed in testing, an *unusually low*
  transfer volume can also trigger a false anomaly flag — a known weakness of simple statistical
  baselining also noted in the reviewed literature (Srivastava et al., 2024 report similar false
  positive challenges with anomaly-only approaches).
- Decision rules are hard-coded thresholds for demonstration; a fuller implementation would tune
  these against a labeled evaluation set, per the Evaluation Plan in Chapter 3.

## Folder mapping for GitHub submission

| This prototype folder | Maps to GitHub repo folder |
|---|---|
| `src/` | `04_Source_Code/` |
| `data/` | `05_Data_or_Sample_Input/` |
| `output/` | `06_Results_or_Expected_Output/` |
