# 📁 01_Research_Papers/

This folder contains the research papers used to support the Research Proposal, particularly **Chapter 2 – Literature Review**.

For each important paper, the following information has been summarized: paper title, author(s), year, research problem, method/technique, dataset/tools, main findings, limitations, and its relevance to the proposed research.

> ⚠️ **Important:** Do not upload copyrighted research papers to a public GitHub repository unless the article is legally available for redistribution. Where necessary, provide the citation, DOI, or official article link instead. Open-access papers may be included where permitted.

---

## 1. Data Loss Prevention Solution for Linux Endpoint Devices

| Item | Required Information |
|---|---|
| **Paper Title** | Data Loss Prevention Solution for Linux Endpoint Devices |
| **Author(s)** | Lukas Daubner, Adam Považanec |
| **Year** | 2023 |
| **Research Problem** | The lack of widely available open-source DLP (Data Loss Prevention) solutions for Linux-based endpoints, specifically for auditing and controlling file system operations and external USB devices to prevent data loss caused by insiders. |
| **Method / Technique** | Comparative analysis of file-system audit/control approaches (fanotify, Linux Security Modules, LD_PRELOAD, system call table hijacking, ftrace hooking) and USB device control (udev + sysfs); implementation of a prototype DLP system called **Failsafe** using kernel hooking based on ftrace. |
| **Dataset / Tools** | Prototype *Failsafe* (libraries `libFSHook` and `libUSBControl`, written in C); tested on Ubuntu 22.04.1 LTS (VM) with scenarios covering web upload (Chrome), instant messaging (Slack), file manager operations (Nautilus), and cloud sync (Dropbox). |
| **Main Findings** | Kernel function hooking using **ftrace** was found to be the most viable approach for auditing/controlling file system operations due to its wide availability on popular distributions, mature API, and broad set of interceptable operations. The combination of **udev + sysfs** proved effective for auditing and controlling USB devices. Performance impact on copy/move/delete operations was minor (grows linearly with the number of operations). |
| **Limitation** | Detection logic relies on application-specific heuristics (hard-coded for Nautilus, Chrome, Dropbox), making generalization to other applications difficult; prone to false positives (e.g., opening a PDF in a browser is detected as an upload); attributes of unauthorized USB devices remain limited and unreliable. |
| **Relevance to Proposed Research** | Serves as a technical reference for an **endpoint-level DLP approach based on kernel hooking (ftrace)** for monitoring file operations and USB devices — relevant as a foundation for the detection/prevention mechanism at the endpoint level in the proposed research. |

---

## 2. A Hybrid Framework for Data Loss Prevention and Detection

| Item | Required Information |
|---|---|
| **Paper Title** | A Hybrid Framework for Data Loss Prevention and Detection |
| **Author(s)** | Atul Srivastava, Vijay Shankar Sharma, Priyam Srivastava, Anuradha Pillai |
| **Year** | 2024 |
| **Research Problem** | Signature-based DLP systems cannot detect new/unknown (zero-day/insider) attacks, while anomaly-based systems suffer from high false positive rates and costly operational overhead since every alert requires manual analysis. |
| **Method / Technique** | A hybrid framework combining **anomaly-based detection** (white-box, automatically builds a model of typical user behavior) with **signature-based prevention** — an operator's feedback on alerts is used to automatically generate/update rules (rule tree) that block similar future transactions. |
| **Dataset / Tools** | **RapidMiner** plugin; synthetic data consisting of security event logs (malware detected, suspicious network activity, unauthorized access) from several source IP addresses. |
| **Main Findings** | The framework reduced the **average time to detect a data breach by 67%**, decreased data breach incidents by 40%, unauthorized access attempts by 35%, and the false positive rate by 50%. |
| **Limitation** | Not tested in a real production environment (evaluation relied on synthetic data); effectiveness of the rule tree depends on the quality of the operator's root-cause analysis; scalability for very large enterprise transaction volumes is not discussed. |
| **Relevance to Proposed Research** | Provides a hybrid approach model (anomaly + signature) with a feedback-loop mechanism that can serve as a reference architecture for combined detection-and-prevention in the proposed DLP system, particularly for balancing new-threat detection with response efficiency. |

---

## 3. Designing Data Loss Prevention System for The Enhancement of Data Integrity in Cyberspace

| Item | Required Information |
|---|---|
| **Paper Title** | Designing Data Loss Prevention System for The Enhancement of Data Integrity in Cyberspace |
| **Author(s)** | Isha Yadav, Himanshu Gupta |
| **Year** | 2023 |
| **Research Problem** | Traditional DLP approaches that focus on only a single solution type (e.g., endpoint DLP only or network DLP only) are inadequate for today's complex and evolving cyber threat landscape, making it difficult to maintain data integrity. |
| **Method / Technique** | Proposes a **hybrid DLP methodology** that combines three approaches: **behavior-based DLP**, **machine learning-based DLP**, and **network-based DLP**, through the stages of: identifying sensitive data, implementing endpoint/network/ML DLP, integrating the solutions, and continuous monitoring and reporting. |
| **Dataset / Tools** | Case studies/literature review (e.g., implementations in the financial sector, healthcare/Mayo Clinic, and e-commerce); historical data breach statistics (2011–2018) from secondary sources (Statista, DLP market reports). |
| **Main Findings** | Combining the three DLP approaches provides more comprehensive data protection than a single approach, enabling real-time detection of various threat types (malware, phishing, insider threats), and helping organizations comply with regulations such as GDPR, HIPAA, and PCI-DSS. |
| **Limitation** | Conceptual/methodological in nature, without technical implementation or direct quantitative testing of the proposed system; effectiveness relies on cited third-party case studies rather than the authors' original experiments. |
| **Relevance to Proposed Research** | Supports the justification for adopting a **hybrid/multi-layer** approach (behavior + machine learning + network) in designing the proposed DLP system, and provides an implementation-stage framework that can be adapted. |

---

## 4. Data Leakage Prevention Approach Based On Insider Trust Calculation

| Item | Required Information |
|---|---|
| **Paper Title** | Data Leakage Prevention Approach Based On Insider Trust Calculation |
| **Author(s)** | Mohammed EL MOUDNI, Elhoussine ZIYATI |
| **Year** | 2023 |
| **Research Problem** | Conventional DLP systems generally rely solely on policy enforcement without considering the profile and trust level of insiders, even though most data leaks originate from internal users (insiders) who have legitimate access. |
| **Method / Technique** | A **multi-agent system** approach that collects logs from multiple servers (LDAP, antivirus/endpoint security, proxy), transforms them using **ETL (Extract, Transform, Load)** techniques, then calculates the **insider trust level** based on role (role-based) and contract type (contract-based) via a *trust matrix*, to produce a permit/deny decision. |
| **Dataset / Tools** | Conceptual architecture with agents: Logs Collector (LC), ETL Agent (EA), Trust Calculator (TC), and Decision Maker (DM); log sources include Windows security events, internet proxy logs, and endpoint security logs. |
| **Main Findings** | The proposed model adds a second verification layer (after standard DLP policy checks pass) based on insider trust calculation, offering advantages in scalability, optimized storage, faster processing of logs, and deeper user profiling compared to conventional methods. |
| **Limitation** | The paper is a design proposal — **no experimental or empirical validation** is included yet (explicitly stated to be addressed in a future separate publication); development of a machine learning classifier for detection is also still at the planning stage. |
| **Relevance to Proposed Research** | Relevant as a reference for the **insider profiling & trust calculation** approach as an additional layer (not a replacement) to conventional DLP policies, enriching the behavioral-analysis dimension of the proposed system. |

---

## 5. Data Leakage Prevention System for Internal Security

| Item | Required Information |
|---|---|
| **Paper Title** | Data Leakage Prevention System for Internal Security |
| **Author(s)** | Bhavya Singh Shishodia, Manisha J. Nene |
| **Year** | 2022 |
| **Research Problem** | Organizations struggle to select and deploy the right commercial DLP solution due to limited literature on the installation, integration process, and operational challenges of large-scale industrial DLP deployments. |
| **Method / Technique** | An implementation case study of DLP deployed at the **Social Security Administration (SSA)**; evaluates common DLP techniques (intelligent documents, encryption, hash matching, virtual file systems, minifilters, biometrics, hypervisor) and vendor-selection criteria using a scoring system (0–4) to compare several products. |
| **Dataset / Tools** | **Symantec** DLP product and several comparison vendors (Firm B, C, D); comparison parameters include network monitoring, email/web prevention, data discovery, endpoint protection, etc. |
| **Main Findings** | Symantec DLP was selected after a thorough evaluation, scoring highest on most criteria; real technical challenges were identified, such as an ICAP integration issue (requiring adjustment of request/response limits) and agent resource requirements (min. 30MB RAM, 80MB storage); incident counts declined significantly after gradual policy tuning. |
| **Limitation** | Based on a single organization's case study (SSA), limiting generalizability; vendor comparisons are based on the researchers' own internal scoring rather than an independent benchmark; does not discuss more recent machine learning-based solutions. |
| **Relevance to Proposed Research** | Provides practical insights (lessons learned) into the real-world challenges of **DLP implementation** — vendor selection criteria, system requirements, and policy management — useful for considering operational aspects in the proposed research. |

---

## 6. A Holistic View on Data Protection for Sharing, Communicating, and Computing Environments: Taxonomy and Future Directions

| Item | Required Information |
|---|---|
| **Paper Title** | A Holistic View on Data Protection for Sharing, Communicating, and Computing Environments: Taxonomy and Future Directions |
| **Author(s)** | Ishu Gupta, Ashutosh Kumar Singh |
| **Year** | 2022 (arXiv preprint, cs.CR) |
| **Research Problem** | Sensitive data is spread across various computing devices and network access points, making it vulnerable to leakage; a comprehensive mapping (taxonomy) of the challenges, solutions, and research gaps in data protection is needed. |
| **Method / Technique** | **Literature review & taxonomy** — classifies Data Leakage Protection Systems (DLPTS) based on data state (at rest, in use, in transit), deployment schema, and analysis techniques (statistical, watermarking, fingerprinting, machine learning). |
| **Dataset / Tools** | No primary experiment/dataset — analysis is based on a compilation of prior studies and secondary data breach statistics (e.g., Ponemon Institute reports, Privacy Rights Clearinghouse, Statista). |
| **Main Findings** | Identifies five key research gaps in existing DLP solutions: high overhead, static request handling, single-objective approaches (detection *or* prevention only, not both), reliance on data modification, and high false-positive rates; recommends future research directions toward multi-objective, machine-learning-based approaches. |
| **Limitation** | As a survey paper, it does not propose or empirically test a new solution; the broad scope of the taxonomy means each technique is discussed relatively briefly. |
| **Relevance to Proposed Research** | Highly relevant as the **state-of-the-art literature review foundation** — the identified taxonomy and research gaps can be used to position the contribution/originality of the proposed research relative to prior DLP studies. |

---

## 7. A Learning Oriented DLP System based on Classification Model

| Item | Required Information |
|---|---|
| **Paper Title** | A Learning Oriented DLP System based on Classification Model |
| **Author(s)** | Kishu Gupta, Ashwani Kush |
| **Year** | 2020 |
| **Research Problem** | An accurate automated document classification mechanism is needed to determine the sensitivity level of data (restricted/internal/unrestricted) before it is allowed to leave an organization, in order to prevent data leakage. |
| **Method / Technique** | A **statistical & machine learning** approach to document classification: **Bag-of-Words (BoW)** for feature extraction, **TF-IDF** for term weighting, **Vectorization**, and a proposed algorithm called **IGBCA (Improvised Gradient Boosting Classification Algorithm)**, validated using K-Fold Cross Validation (StratifiedKFold) and RandomizedSearchCV. |
| **Dataset / Tools** | A labeled document dataset with three classes (Restricted, Internal, Unrestricted); **scikit-learn** libraries (TfidfVectorizer, SelectKBest/chi2, GradientBoostingClassifier, StratifiedKFold, RandomizedSearchCV). |
| **Main Findings** | The IGBCA model achieved an overall accuracy of approximately **96%**, with sensitivity of 95.1%, specificity of 96.5%, precision of 93.3%, and F1-score of 94.3%, and an error rate of only ~3.96% — indicating strong document classification performance to support DLP decisions (allow/block/encrypt). |
| **Limitation** | The authors note that classification speed and other system overheads still need to be addressed in future work; the size/diversity of the training dataset is limited, so generalization to other document domains has not been tested. |
| **Relevance to Proposed Research** | Provides a reference technique for **machine-learning-based content classification (TF-IDF + Gradient Boosting)** that can be adopted as a content-aware detection component in the proposed DLP system, complete with evaluation metrics that can serve as a benchmark. |

---

## Source File List

| No | Title | Source/Venue |
|---|---|---|
| 1 | `Data Loss Prevention Solution for Linux Endpoint Devices` | ARES 2023 (ACM), DOI: [10.1145/3600160.3605036](https://doi.org/10.1145/3600160.3605036 ) |
| 2 | `A Hybrid Framework for Data Loss Prevention and Detection` | IEEE SPARC 2024, DOI: [10.1109/SPARC61891.2024.10828891](https://doi.org/10.1109/sparc61891.2024.10828891) |
| 3 | `Designing Data Loss Prevention System for The Enhancement of Data Integrity in Cyberspace` | IEEE ICAC3N 2023, DOI: [10.1109/ICAC3N60023.2023.1054182](https://doi.org/10.1109/icac3n60023.2023.10541823) |
| 4 | `Data Leakage Prevention Approach Based On Insider Trust Calculation` | IEEE WINCOM 2023, DOI: [10.1109/WINCOM59760.2023.10322935](https://doi.org/10.1109/wincom59760.2023.10322935) |
| 5 | `Data Leakage Prevention System for Internal Security` | IEEE INCOFT 2022, DOI: [10.1109/INCOFT55651.2022.10094509](https://doi.org/10.1109/INCOFT55651.2022.10094509) |
| 6 | `A HOLISTIC VIEW ON DATA PROTECTION FOR SHARING, COMMUNICATING, AND COMPUTING ENVIRONMENTS: TAXONOMY AND FUTURE DIRECTIONS` | arXiv:2202.11965 [cs.CR](https://arxiv.org/abs/2202.11965) |
| 7 | `A Learning oriented DLP System based on Classification Model` | INFOCOMP, v.19, no.2, 2020 [cs.CR](https://arxiv.org/abs/2312.13711) |
