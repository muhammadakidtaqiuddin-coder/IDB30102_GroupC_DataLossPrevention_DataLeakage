# 06_Results_or_Expected_Output

At the proposal stage, this folder represents **expected/preliminary** outcomes, not final experimental results. All figures below are illustrative targets used to frame the evaluation plan — actual results will be reported in the final project/thesis.

## Files
| File | Description |
|---|---|
| `expected_metrics_comparison.png` | Illustrative bar chart comparing expected Precision/Recall/F1/FPR of the rule-based baseline vs. the proposed ML classifier |

## Evaluation Metrics to Be Used
| Metric | Description |
|---|---|
| Precision | Proportion of flagged content that is actually sensitive |
| Recall | Proportion of actual sensitive content correctly flagged |
| F1-score | Harmonic mean of precision and recall |
| False Positive Rate (FPR) | Proportion of non-sensitive content incorrectly flagged as sensitive — the primary metric this research aims to reduce |
| Detection latency (secondary) | Time taken to classify a given input |

## Expected Detection/Classification Result (Example Format)
| Input Text (excerpt) | Ground Truth | Regex Baseline Prediction | Proposed Classifier Prediction |
|---|---|---|---|
| "Please send the invoice to jane.doe@example.com" | Sensitive | Sensitive (matched EMAIL pattern) | Sensitive |
| "The quarterly report is attached for review" | Non-sensitive | Non-sensitive | Non-sensitive |
| "Contact accounts regarding acct no as discussed" (obfuscated, no literal pattern) | Sensitive | **Non-sensitive (false negative)** | Sensitive (context-aware) |

*This table illustrates the type of comparison the final evaluation will report — actual rows will be populated from real test-set predictions once the full dataset and trained model are available.*

## Expected System Interface
At this stage, no user interface has been developed. The expected interface (for the final prototype) is a simple command-line or lightweight web input where a user submits text and receives a classification result (`sensitive` / `non-sensitive`) with matched categories, consistent with the architecture in `03_Architecture_and_Flowchart/`.

## Explanation of Expected Research Outcomes
The research expects the proposed ML/NLP classifier to achieve a lower False Positive Rate than the rule-based baseline while maintaining comparable or better Recall and F1-score, consistent with findings reported in prior work (e.g. Gupta & Kush, 2023a; Kaliappan et al., 2024). This would support the research aim of reducing false positives in DLP content detection without sacrificing detection reliability. Preliminary pipeline runs using `04_Source_Code/regex_baseline.py` and `04_Source_Code/ml_classifier.py` on a small illustrative sample confirm the end-to-end pipeline executes correctly; full quantitative results will follow once evaluated on the complete AI4Privacy PII-Masking-200k dataset.
