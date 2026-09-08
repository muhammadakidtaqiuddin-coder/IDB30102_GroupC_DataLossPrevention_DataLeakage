# IDB30102_GroupC_DataLossPrevention

## Research Title
Design and Implementation of a Data Loss Prevention Framework for Mitigating Data Leakage in Organizational Networks

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
Data Loss Prevention (DLP) — design and implementation of an integrated multi-layer framework (endpoint, network, and content-based detection) for mitigating data leakage in organizational networks

## Research Problem
Existing DLP solutions largely address a single detection layer (endpoint-only, network-only, or content-classification-only), leaving organizational networks exposed to leakage vectors outside that layer's coverage. Frameworks that do propose multi-layer/integrated DLP approaches remain largely conceptual, without empirical implementation or testing to demonstrate real-world feasibility.

## Research Aim
To design and implement a multi-layer Data Loss Prevention framework that integrates endpoint, network, and content-based detection techniques to mitigate data leakage in organizational networks.

## Research Objectives
1. To review existing DLP techniques across endpoint, network, and content-classification layers, and identify gaps in current integrated frameworks.
2. To design and implement a preliminary DLP framework/prototype combining rule-based/anomaly detection and content classification for an organizational network environment.
3. To test and evaluate the feasibility of the proposed framework against simulated data leakage scenarios, using detection accuracy and false-positive rate as evaluation metrics.

## Brief Description of the Proposed Solution
The project proposes a preliminary, multi-layer DLP framework combining endpoint-level monitoring, network-level anomaly/exfiltration detection, and content-based classification (e.g., TF-IDF/ML-based sensitive content detection). The framework will be demonstrated at prototype level against simulated leakage scenarios, benchmarked using detection accuracy and false-positive rate.

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
| RO1 – Review existing DLP techniques across endpoint, network, and content layers | Literature review and analysis | `01_Research_Papers/`, `02_Literature_Review/` |
| RO2 – Design and implement the preliminary multi-layer DLP framework/prototype | Architecture, flowchart, and preliminary code | `03_Architecture_and_Flowchart/`, `04_Source_Code/` |
| RO3 – Test and evaluate framework feasibility against simulated leakage scenarios | Sample data, preliminary/expected results | `05_Data_or_Sample_Input/`, `06_Results_or_Expected_Output/` |
