# 📁 03_Architecture_and_Flowchart/

This folder contains the visual design of the proposed DLP framework, referenced in Chapter 3 of the Research Proposal.

## Contents

| File | Description |
|---|---|
| `architecture.png` | **Figure 3.1 — Architecture Diagram.** Shows how a data-transfer event (content, user, volume, destination) is processed by two parallel detection techniques — a **Content Classifier** (TF-IDF + Gradient Boosting; labels content as Restricted / Internal / Unrestricted) and a **Behavioral Anomaly Detector** (z-score vs. a per-user baseline) — before a **Decision Engine** combines both signals into an ALLOW / ALERT / BLOCK response. All decisions are logged for evaluation, with a feedback loop shown for refining the model over time. |
| `flowchart.svg` | **Figure 3.2 — Process Flowchart.** A Graphviz-generated diagram (v2.43.0) showing the step-by-step decision logic of the pipeline described above, in vector format. |

## Relationship to the Prototype

Both diagrams describe a **two-technique hybrid model** (content classification + behavioral anomaly detection). This matches the current implementation in `04_Source_Code/` (`content_classifier.py` + `anomaly_detector.py`, combined in `evaluate_hybrid_model.py`).

> **Note:** The top-level repository `README.md` describes an earlier three-layer design that also included a rule-based *signature/pattern detector*. That third component is not present in the current diagrams or source code — if the group intends to keep the three-layer version, `architecture.png` and `flowchart.svg` should be regenerated to include it; otherwise the top-level `README.md` should be updated to match the two-technique version shown here.

## Notes

- Diagrams were produced with **Graphviz (DOT)**, per the "Programming Languages, Software, Frameworks..." section of the top-level README.
- If the underlying `.dot` source file(s) exist locally, consider committing them alongside the rendered `.png`/`.svg` so the diagrams can be regenerated or edited later.
