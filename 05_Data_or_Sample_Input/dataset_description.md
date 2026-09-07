# Dataset Description

## Dataset
**AI4Privacy PII-Masking-200k**

- **Source / Publisher:** Ai4Privacy
- **Official URL:** https://huggingface.co/datasets/ai4privacy/pii-masking-200k
- **DOI:** 10.57967/hf/1532
- **License:** CC BY-NC 4.0 (non-commercial use with attribution, suitable for this academic FYP; not for commercial redistribution)

## Description
The dataset contains approximately 209,000 synthetically generated text samples across four languages (English ~43k, French ~62k, German ~52k, Italian ~50k), each annotated with spans of personally identifiable information (PII) covering dozens of entity classes (e.g. names, email addresses, phone numbers, ID numbers, financial account references, addresses). Because the text is entirely synthetic, no real individuals' data is exposed, which avoids the PDPA-related restrictions that would apply to a real corporate or personal dataset.

Each record follows a JSONL schema with three key fields:
- `source_text` — the raw text sample (unmasked)
- `target_text` — the same text with PII spans replaced by placeholder labels
- `privacy_mask` — the list of PII entity spans, their labels, and character offsets

## Why This Dataset Is Used
This project's artefact is a content-aware DLP classification engine intended to reduce false positives relative to a rule-based baseline (Section 3, Chapter 3). The `source_text` and `privacy_mask` fields provide a ready-made ground truth for training and evaluating a classifier that must decide whether a given piece of text contains sensitive content, without requiring any real personal or organisational data to be collected or uploaded.

## Intended Use in This Research
- The English subset (`english_pii_43k.jsonl`, ~43,000 samples) will be used as the primary source for the sensitive-content class.
- A non-sensitive (negative) class will be constructed by sampling benign text passages containing no PII spans (or from a general-purpose text corpus), to allow binary classification.
- The dataset will be split into training and held-out test sets.
- The same held-out test set will be run through both (a) the proposed ML/NLP classifier and (b) a rule-based/regex baseline, to compute the evaluation metrics defined in Section 3.7 of Chapter 3 (Precision, Recall, F1, False Positive Rate).

## Upload Note
Per the assignment brief, the full dataset (~365 MB across all four languages) is **not** uploaded to this repository. Instead:
- This folder contains a small **illustrative sample** (`sample_text/sample_format_illustration.jsonl`) showing the schema/format only, it is a hand-written example in the same structure as the real dataset, not an extract of the actual data, since redistributing dataset content is subject to the source's CC BY-NC 4.0 terms.
- The full dataset should be downloaded directly from the official link above (or via the `datasets` Python library — see below) when running the project code.

```python
from datasets import load_dataset
dataset = load_dataset("ai4privacy/pii-masking-200k")
```

## Other Data Types Not Applicable
This project does not use image, network log, or sensor data, only text, so the `Sample images`, `Sample network logs`, and `Sample sensor data` subfolders listed in the repository template are not applicable and are omitted.
