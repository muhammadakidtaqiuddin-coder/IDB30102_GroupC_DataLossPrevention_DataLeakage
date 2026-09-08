# 02_Literature_Review

## 2.1 Introduction
One of the most crucial cybersecurity strategies for the detection and prevention of unauthorized access to sensitive organizational data is Data Loss Prevention (DLP). Previously, the research has focused on endpoint monitoring, protection, access-control mechanisms, machine learning, and anomaly detection in the context of DLP. For instance, the detection of policy-based endpoint interception, hybrid behaviour and machine-learning methods, and signature-based anomaly detection are all research areas that have been investigated to limit data leakage incidents. The chapter critically examines and compares these approaches to provide a basis for an effective DLP framework for organizational networks.

### 2.1.1 Endpoint and Network-Based Data Loss Prevention
Endpoint and network-based DLP is directed at tracking data circulation throughout a company's devices and networks. Daubner and Povazanec (2023) discussed Linux endpoint DLP (interception, policy checking, and blocking) and Yadav and Gupta (2023) discussed endpoint, network, and behavioural approach. These studies show a multi-layer approach to organization data leakage prevention.
### 2.1.2 Machine Learning and Hybrid-Based Data Loss Prevention
The use of machine learning and hybrid based DLP techniques enhances detection and classification of potential data leakage. Gupta and Kush (2023) implemented the TF-IDF vectorization and classification technique to minimize the number of false positives, and Srivastava et al. (2024) employed signatures with anomaly detection. The approaches show the importance of intelligent detection in enhancing the accuracy and prevention of DLP.
### 2.1.3 Access, Cloud, and Trust-Based Data Protection
To secure sensitive information, access, cloud and trust based approaches are used to manage access and to assess data or user behavior. The attribute-based encryption technique was combined with machine learning-based content checks by Gupta and Singh (2022), and trust scoring was implemented by El Moudni and Ziyati (2023). Shishodia and Nene (2022) introduced and illustrated an example of an organisation that uses access monitoring and control.

## 2.2 Synthesis of Previous Studies
Previous studies have shown that Data Loss Prevention (DLP) is a new trend that integrates rule-based, machine-learning, behavioural and network-based methods to enhance detection and prevention of data leakage. Daubner and Povazanec (2023) focused on endpoint interception and policy enforcement, and Yadav and Gupta (2023) added behavioural, machine learning and network monitoring for comprehensive protection. Srivastava et al. (2024) used signatures along with anomaly detection, resulting in a 40% decrease in breaches. Likewise, Shishodia and Nene (2022) identified that with monitoring and access control measures, incidents dropped by 93%. Overall, these research studies suggest that a layered approach to DLP can enhance accuracy in the detection phase, mitigate data leakage, and fortify data protection measures across the organisations.

## 2.3 Summary Table of Previous Studies
Previous research shows that Data Loss Prevention (DLP) is increasingly integrating endpoint monitoring, network protection, machine learning, anomaly detection and access control. The researched papers reveal that combinations of different approaches can capture various types of data leakage and hybrid approaches can enhance the accuracy of data leakage detection and minimize false alarms. As well, there have been significant reductions in leakage incidents, as shown by organizational case studies. This study paves the way for building a framework of detection and prevention systems in organizational contexts. But there are a number of variations in the techniques and deployment environments suggesting a more cohesive strategy for data leakage prevention.

| Author(s)           | Year | Focus                        | Method/Technique                 | Key Finding                                 | Relevance to Proposed Study               |
| ------------------- | ---: | ---------------------------- | -------------------------------- | ------------------------------------------- | ----------------------------------------- |
| Daubner & Povazanec | 2023 | Linux endpoint DLP           | Intercept → policy check → block | Detected leaks through applications and USB | Supports endpoint enforcement pipeline    |
| Yadav & Gupta       | 2023 | Hybrid DLP                   | Behaviour + ML + network         | Detected a wider range of breaches          | Supports multi-layer DLP structure        |
| Srivastava et al.   | 2024 | Hybrid DLP                   | Signature + anomaly detection    | Reduced breaches by 40%                     | Supports combined detection methods       |
| Shishodia & Nene    | 2022 | Organizational leakage       | Monitoring + access control      | Incidents decreased by 93%                  | Demonstrates organizational effectiveness |
| Gupta & Singh       | 2022 | Cloud data protection        | ABE + ML content checking        | Achieved minimal leakage rates              | Supports data-state protection            |
| Gupta & Kush        | 2023 | DLP accuracy                 | TF-IDF classification            | Lower false-positive rate than regex        | Supports improved detection accuracy      |
| El Moudni & Ziyati  | 2023 | Enterprise leakage detection | Multi-agent + ETL trust scoring  | Classified different trust levels           | Supports trust-based detection            |







