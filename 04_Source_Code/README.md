# 📁 04_Source_Code/

This folder contains the preliminary Python prototype of the hybrid DLP framework described in Chapter 3 of the Research Proposal (supports **RO2** and **RO3**).

## Contents

| File | Role | Description |
|---|---|---|
| `content_classifier.py` | Technique 1 — Content Classification | `ContentClassifier` class: TF-IDF vectorization (`max_features=500`, unigrams+bigrams) + `GradientBoostingClassifier` to label text as **Restricted**, **Internal**, or **Unrestricted**. `train()` reports held-out accuracy and a classification report; `classify()` predicts a label for new text. Based on Gupta & Kush (2023). |
| `anomaly_detector.py` | Technique 2 — Behavioral Anomaly Detection | `AnomalyDetector` class: flags a user's transfer volume as anomalous if its **z-score** against that user's own historical baseline is ≥ `2.0`. Based on Yadav & Gupta (2023) and El Moudni & Ziyati (2023). |
| `generate_evaluation_dataset.py` | Evaluation data generation | Builds a labeled synthetic set of transfer events (`evaluation_events.csv`) with an independent **ground-truth leak label**, deliberately including cases a content-only detector would miss (sensitive content, normal volume, external destination) and cases an anomaly-only detector would miss (volume spike, non-sensitive content) — so the comparison in `evaluate_hybrid_model.py` isn't rigged toward the hybrid approach. |
| `evaluate_hybrid_model.py` | RO3 — Evaluation | Compares three prediction strategies — **classification-only**, **anomaly-only**, and the **hybrid** (classifier flags Restricted/Internal **AND** (external destination **OR** anomaly)) — against ground truth, reporting Accuracy, Precision, Recall, F1-score, and False Positive Rate. Writes results to `evaluation_results.csv`. |

## How to Run

The scripts expect sibling folders named `data/` and `output/` (see **Known Issue** below), so either rename/symlink the folders or edit the path constants before running.

```bash
pip install pandas scikit-learn
cd 04_Source_Code
python3 generate_evaluation_dataset.py   # (re)builds evaluation_events.csv
python3 evaluate_hybrid_model.py         # runs the comparison, writes evaluation_results.csv
```

Individual components can also be run standalone for a quick demo:

```bash
python3 content_classifier.py   # trains on sample_documents.csv, classifies 3 sample texts
python3 anomaly_detector.py     # runs a few sample volume checks against user baselines
```

## Known Issues

- **No `requirements.txt` in this folder** — the top-level `README.md` references one, but it isn't present. Dependencies are `pandas` and `scikit-learn` (see imports above).
- **Path mismatch:** all four scripts reference data/output via relative paths `../data/...` and `../output/evaluation_results.csv`, but the actual sibling folders in this repo are named `05_Data_or_Sample_Input/` and `06_Results_or_Expected_Output/`. Running the scripts as-is from this folder will raise a `FileNotFoundError`. Fix by either renaming the folders, adding symlinks (`data` → `05_Data_or_Sample_Input`, `output` → `06_Results_or_Expected_Output`), or updating the `DATA_PATH`/`LOG_PATH`/`RESULTS_PATH` constants in each script.
- **Scope vs. top-level README:** the top-level `README.md` describes a third, rule-based *signature/pattern detector* (`pattern_detector.py`) and an integrated `dlp_framework.py` entry point. Neither file exists in this folder currently — the working prototype here implements only the two-technique hybrid (classification + anomaly). Update one or the other so the documentation matches the code.

## Design Note

Thresholds (z-score = 2.0, TF-IDF `max_features` = 500) are hard-coded for this proof-of-concept stage, consistent with the "Known Limitations" section of the top-level README — a fuller implementation would tune these against a labeled evaluation set.
