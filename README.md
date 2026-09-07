# IDB30102_GroupC_DataLossPrevention

## Research Title
A Machine Learning-Based Approach for Robust PII and Sensitive Text Leakage Detection in Data Loss Prevention

## Group Number
Group C

## Group Members and Student IDs
| Name | Student ID |
|---|---|
| Muhammad Akid Taqiuddin bin Dzul Izzudin (Team Lead) | 52215225321 |
| Muhammad Daniel bin Daud | 52215225164 |
| Khairul'Anam bin Mohammad Fairuze | 52215225184 |
| Gibran Budimann bin Muhammad Fadzil | 52215225007 |

## Assigned Research Area
Data Loss Prevention (DLP) — focus on ML/DL-based PII and sensitive text leakage detection

## Research Problem
Existing ML/DL-based DLP models report high detection accuracy but are largely trained and validated on synthetic, simulated, single-source, or English-only datasets. This limits confidence in their reliability and generalizability when deployed in real, multilingual, production-level environments.

## Research Aim
To develop and evaluate a machine learning-based text classification model for detecting personally identifiable information (PII) and sensitive content, with emphasis on improving robustness across more realistic and diverse text conditions.

## Research Objectives
1. To review and analyze existing ML/DL-based approaches for PII and sensitive text leakage detection, and identify their key limitations.
2. To design and develop a text classification model capable of detecting PII/sensitive content with improved robustness to noisy or non-standard text input.
3. To evaluate the proposed model's detection performance using accuracy, F1-score, and false-positive rate, and compare it against baseline approaches identified in the literature.

## Brief Description of the Proposed Solution
The project proposes a supervised machine learning / deep learning text classifier trained to identify PII and sensitive content within text data (e.g., emails, chat logs, documents). The model will be benchmarked against baseline approaches (e.g., TF-IDF/SVM, BERT-based classifiers) identified in the literature review, with emphasis on robustness to noisy, obfuscated, or non-English text.

## Selected Research Methodology and Development Model
- **Research Methodology:** *[To be completed by Member 3 — Chapter 3, e.g., Design Science Research / Experimental]*
- **Development Model:** *[To be completed by Member 3, or "Not applicable" if no system is developed]*

## Proposed Evaluation Plan
- **Baseline for comparison:** *[To be completed by Member 4 — Chapter 3]*
- **Dataset / Test environment:** *[To be completed by Member 4]*
- **Evaluation metrics:** Accuracy, F1-score, False-positive rate

## Proposed System Architecture
*[To be completed by Member 3 — see 03_Architecture_and_Flowchart/]*

## Description of Technical Components in this Repository
| Folder | Contents |
|---|---|
| `01_Research_Papers/` | Summary of 40 research papers supporting the Literature Review |
| `02_Literature_Review/` | Literature review analysis table, comparison of existing techniques, research gap analysis |
| `03_Architecture_and_Flowchart/` | Proposed system architecture and process flowchart |
| `04_Source_Code/` | Preliminary source code / proof-of-concept components |
| `05_Data_or_Sample_Input/` | Sample dataset / dataset description and source links |
| `06_Results_or_Expected_Output/` | Preliminary or expected output, evaluation metrics |
| `07_References/` | Full APA reference list and external resources |

## Programming Languages, Software, Frameworks, Libraries, Datasets and Tools Expected to be Used
*[To be completed by Member 3/4 based on selected methodology — e.g., Python, scikit-learn, PyTorch/TensorFlow, BERT/Transformers]*

## Instructions for Executing Preliminary Code
*[To be completed once preliminary code is added to 04_Source_Code/]*

## Research Objective → Component Mapping
| Research Objective | Supporting Component | GitHub Location |
|---|---|---|
| RO1 – Review existing PII/text leakage detection methods | Literature review and analysis | `01_Research_Papers/`, `02_Literature_Review/` |
| RO2 – Design and develop the proposed classification model | Architecture, flowchart, and preliminary code | `03_Architecture_and_Flowchart/`, `04_Source_Code/` |
| RO3 – Evaluate model performance | Sample data, preliminary/expected results | `05_Data_or_Sample_Input/`, `06_Results_or_Expected_Output/` |
