# 📁 06_Results_or_Expected_Output/

This folder holds the output produced by running the evaluation prototype, supporting **RO3** (test and evaluate the proposed solution).

## Contents

| File | Description |
|---|---|
| `evaluation_results.csv` | Output of `04_Source_Code/evaluate_hybrid_model.py`. Compares three detection strategies on the 150-event synthetic set from `evaluation_events.csv`. |

## Current Results

| Approach | Accuracy | Precision | Recall | F1-score | False Positive Rate |
|---|---|---|---|---|---|
| Classification-only (baseline) | 0.793 | 0.748 | 0.939 | 0.832 | 0.382 |
| Anomaly-only (baseline) | 0.613 | 0.682 | 0.549 | 0.608 | 0.309 |
| **Hybrid classification + anomaly (proposed)** | **0.933** | **0.939** | **0.939** | **0.939** | **0.074** |

**Interpretation:** on this synthetic evaluation set, the hybrid approach outperforms either single-technique baseline on every metric, most notably cutting the false-positive rate from 0.31–0.38 down to 0.074 while matching or improving recall — directly supporting the research aim of reducing false positives without sacrificing detection of true leakage events.

> These figures are illustrative only, generated from a small, deterministic (`random.seed(42)`) synthetic dataset — consistent with the proposal-stage / preliminary-prototype scope stated in the top-level README, not a claim about real-world performance.

## Note on Naming

The top-level repository `README.md` describes this folder's output as `decision_log.csv` (from a `dlp_framework.py` pipeline). The prototype currently in `04_Source_Code/` instead produces `evaluation_results.csv` via `evaluate_hybrid_model.py`. Update the top-level README to reflect the current pipeline, or regenerate a `decision_log.csv` if that per-event log format is still needed for the final report.

## Regenerating

```bash
cd ../04_Source_Code
python3 evaluate_hybrid_model.py
```

(See `04_Source_Code/README.md` for the path fix needed before this will run without errors.)
