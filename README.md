# IDB30102_GroupC_DataLossPrevention

**Research Title:** IMPROVING DATA LEAKAGE DETECTION ACCURACY THROUGH A HYBRID CLASSIFICATION AND ANOMALY-BASED APPROACH FOR ORGANIZATIONAL NETWORKS

> **[Fill in before submission — bracketed items are placeholders]**

---

## Group Information

| Field | Details |
|---|---|
| **Group Number** | Group C |
| **Group Members & Student IDs** | [Muhammad Akid Taqiuddin Bin Dzul Izzuidn — 52215225321]<br>[Muhammad Daniel bin Daud — 52215225164]<br>[Khairul'Anam bin Mohammad Fairuze — 52215225007]<br>[Gibran Budimann bin Muhammad Fadzil — Student ID] |
| **Course** | IDB30102 — Research Methodology (BCS) |
| **Assigned Research Area** | Data Loss Prevention (DLP) |
| **Suggested Focus** | Data leakage |

---

## Research Problem

Existing Data Loss Prevention (DLP) solutions largely rely on either static, signature-based detection or single-layer approaches (endpoint-only or network-only), leading to two persistent weaknesses:

1. **[Problem Statement 1]** — Existing DLP solutions rely heavily on static, signature-based detection, resulting in high false-positive rates and an inability to detect previously unseen (zero-day or insider-driven) leakage attempts.
2. **[Problem Statement 2]** — Many organizations lack a unified framework that combines detection and prevention across endpoint, content, and behavioral layers, leaving gaps that isolated, single-purpose DLP tools cannot address.

These gaps are identified in the literature reviewed in Chapter 2 (see `01_Research_Papers/` and `02_Literature_Review/`), most directly by Gupta and Singh (2022), who highlight high overhead, single-objective focus, and high false-positive rates as recurring weaknesses across current DLP research.

---

## Research Aim

To design and implement a hybrid Data Loss Prevention framework that combines content classification, signature-based detection, and behavioral anomaly detection to more effectively mitigate data leakage in organizational networks.

## Research Objectives

- **RO1:** To study existing DLP methods, techniques, and their limitations through a review of current literature.
- **RO2:** To design and develop a hybrid DLP framework prototype that combines content classification, signature detection, and behavioral anomaly detection to reduce false positives and improve detection of insider-driven leakage.
- **RO3:** To test and evaluate the proposed framework against a defined baseline and evaluation metrics.

---

## Proposed Solution — Brief Description

The proposed framework is a **hybrid DLP pipeline** that intercepts a simulated data-transfer event and evaluates it through three parallel detection layers before making an ALLOW / ALERT / BLOCK decision:

1. **Content Classification** — a TF-IDF + Gradient Boosting model labels document content as *Restricted*, *Internal*, or *Unrestricted*.
2. **Signature Detection** — a rule-based scanner flags known sensitive patterns (SSNs, credit card numbers, API keys/passwords) and sensitive keywords.
3. **Behavioral Anomaly Detection** — a statistical (z-score) model flags transfer volumes that deviate significantly from a user's established baseline behavior.

The three signals are combined by a decision engine, and every decision is logged with its reasoning to support continuous monitoring and reporting, following the hybrid architecture justified in Chapter 3 of the Research Proposal.

At this proposal stage, the repository contains a **preliminary prototype** demonstrating the technical feasibility of this design — not a production-ready system, consistent with the assignment brief's proposal-stage scope.

---

## Selected Research Methodology and Development Model

| Layer | Selection | Justification |
|---|---|---|
| **Research Methodology (Layer 1)** | Design Science Research (DSR) — Peffers et al. (2007); Hevner et al. (2004) | The project's primary contribution is a designed artefact (the DLP framework) evaluated against defined objectives, matching DSR's problem-identification → design → demonstration → evaluation structure. |
| **Development Model (Layer 2)** | Prototyping | Supports early construction of a working subset (the three detection components) that can be evaluated and refined within a single-semester timeline, and is easily evidenced through GitHub commit history. |

Full phase-by-phase description is provided in Chapter 3 of the Research Proposal.

---

## Proposed Evaluation Plan

| Item | Description |
|---|---|
| **What is measured** | Detection accuracy, false-positive rate, and time-to-detect for simulated leakage scenarios |
| **Baseline** | Single-layer approaches reported in prior work — signature-only detection (Srivastava et al., 2024) and heuristic-only endpoint detection (Daubner & Považanec, 2023) |
| **Dataset / test environment** | Sandboxed environment with synthetic sensitive/non-sensitive documents and simulated user activity logs (see `05_Data_or_Sample_Input/`) |
| **Metrics** | Accuracy, Precision, Recall, F1-score, False Positive Rate |
| **Success threshold** | **[e.g., the proposed framework achieves a lower false-positive rate and/or higher detection accuracy than the single-layer baseline approaches reviewed in Chapter 2]** |

---

## Proposed System Architecture

See `03_Architecture_and_Flowchart/` for the full diagrams.

- **Figure 3.1 — Architecture Diagram:** shows data sources (endpoint, network, document content) flowing into an event interceptor, through the three-layer hybrid detection stage, into a decision engine, and out to logging/reporting with a feedback loop for rule refinement.
- **Figure 3.2 — Process Flowchart:** shows the sequential decision logic — classify → scan → check behavior → apply decision rules → log → refine.

Both diagrams are generated directly from, and kept consistent with, the logic implemented in `04_Source_Code/dlp_framework.py`.

---

## Description of Technical Components in This Repository

| Folder | Contents |
|---|---|
| `01_Research_Papers/` | Summarized details of 7 key papers supporting Chapter 2 (title, authors, method, findings, limitations, relevance) |
| `02_Literature_Review/` | Literature analysis table, comparison of existing techniques, research gap analysis |
| `03_Architecture_and_Flowchart/` | Architecture diagram (Figure 3.1) and process flowchart (Figure 3.2), in `.png` and `.svg` |
| `04_Source_Code/` | Preliminary Python prototype: content classifier, signature detector, anomaly detector, and the integrated framework pipeline |
| `05_Data_or_Sample_Input/` | Synthetic labeled documents and synthetic user activity logs used to train/test the prototype |
| `06_Results_or_Expected_Output/` | Decision log output (`decision_log.csv`) from running the prototype on sample transfer events |
| `07_References/` | Full APA reference list |

---

## Mapping Technical Work to Research Objectives

| Research Objective | Supporting Component | GitHub Location |
|---|---|---|
| RO1 — Study existing methods and techniques | Literature review and paper summaries | `01_Research_Papers/`, `02_Literature_Review/` |
| RO2 — Design and develop the proposed solution | Hybrid DLP prototype (classifier, signature detector, anomaly detector, decision engine) | `03_Architecture_and_Flowchart/`, `04_Source_Code/` |
| RO3 — Test and evaluate the proposed solution | Sample data, decision log output, evaluation metrics | `05_Data_or_Sample_Input/`, `06_Results_or_Expected_Output/` |

---

## Programming Languages, Software, Frameworks, Libraries, Datasets and Tools

- **Language:** Python 3.10+
- **Libraries:** pandas, scikit-learn (TfidfVectorizer, GradientBoostingClassifier), joblib
- **Diagramming:** Graphviz (DOT)
- **Data:** Synthetic sample documents and synthetic user activity logs (no real or confidential data used)

---

## Instructions for Executing Preliminary Code

```bash
# 1. Install dependencies
pip install -r 04_Source_Code/requirements.txt

# 2. Run the full framework pipeline
cd 04_Source_Code
python3 dlp_framework.py
```

This will:
1. Train the content classifier on `05_Data_or_Sample_Input/sample_documents.csv` and print accuracy/F1 metrics
2. Evaluate 5 sample transfer events through the full hybrid pipeline
3. Write the decision log to `06_Results_or_Expected_Output/decision_log.csv`

Individual components can also be run standalone for testing:
```bash
python3 content_classifier.py
python3 pattern_detector.py
python3 anomaly_detector.py
```

---

## Data and Ethical Note

No real, confidential, or organizational data is used anywhere in this repository. All datasets under `05_Data_or_Sample_Input/` are synthetic, created solely for demonstration and evaluation of the prototype, consistent with the ethical and legal considerations stated in Chapter 3 of the Research Proposal.

---

## Known Limitations (Preliminary Stage)

- The content classifier is trained on a small synthetic dataset (30 samples); reported accuracy/F1 figures are illustrative only.
- The anomaly detector uses a simple z-score threshold, which can occasionally flag unusually *low* transfer volumes as anomalous — a known limitation of simple statistical baselining also discussed in the reviewed literature.
- Decision thresholds are currently hard-coded for demonstration and would be tuned against a labeled evaluation set in a fuller implementation.

---

## References

Daubner, L., & Považanec, A. (2023). Data loss prevention solution for Linux endpoint devices. In *Proceedings of the 18th International Conference on Availability, Reliability and Security (ARES 2023)*. https://doi.org/10.1145/3600160.3605036

El Moudni, M., & Ziyati, E. (2023). Data leakage prevention approach based on insider trust calculation. In *2023 International Wireless Communications and Mobile Computing Conference (WINCOM)*. https://doi.org/10.1109/WINCOM59760.2023.10322935

Gupta, I., & Singh, A. K. (2022). A holistic view on data protection for sharing, communicating, and computing environments: Taxonomy and future directions. *arXiv preprint*. https://arxiv.org/abs/2202.11965

Gupta, K., & Kush, A. (2020). A learning oriented DLP system based on classification model. *INFOCOMP Journal of Computer Science, 19*(2). https://arxiv.org/abs/2312.13711

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly, 28*(1), 75–105.

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77.

Shishodia, B. S., & Nene, M. J. (2022). Data leakage prevention system for internal security. In *2022 International Conference on Futuristic Technologies (INCOFT)*. https://doi.org/10.1109/INCOFT55651.2022.10094509

Srivastava, A., Sharma, V. S., Srivastava, P., & Pillai, A. (2024). A hybrid framework for data loss prevention and detection. In *2024 IEEE International Conference on Smart Power Applications, Communications and Advanced Computing (SPARC)*. https://doi.org/10.1109/SPARC61891.2024.10828891

Yadav, I., & Gupta, H. (2023). Designing data loss prevention system for the enhancement of data integrity in cyberspace. In *2023 International Conference on Advances in Computation, Communication and Networking (ICAC3N)*. https://doi.org/10.1109/ICAC3N60023.2023.10541823
