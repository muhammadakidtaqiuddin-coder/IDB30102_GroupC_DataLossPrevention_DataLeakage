# 05_Data_or_Sample_Input

## Contents
| File | Description |
|---|---|
| `dataset_description.md` | Full dataset description, official link, license, and intended use in this research |
| `sample_text/sample_format_illustration.jsonl` | Hand-written illustration of the dataset schema (NOT an extract of the real dataset — see note below) |

## Quick Summary
- **Dataset:** AI4Privacy PII-Masking-200k
- **Official URL:** https://huggingface.co/datasets/ai4privacy/pii-masking-200k
- **License:** CC BY-NC 4.0 (academic/non-commercial use permitted with attribution)
- Full details, schema, and intended use: see `dataset_description.md`

## Note on the Sample File
The full dataset (~365 MB) is not uploaded to this repository, per the assignment's restriction on dataset size/redistribution. `sample_format_illustration.jsonl` only illustrates the JSON schema (`source_text`, `target_text`, `privacy_mask`) using invented example text — it is not copied from the real dataset. Before final submission, this should ideally be replaced with a small genuine extract (e.g. 20–50 rows) downloaded directly from the source, consistent with the CC BY-NC 4.0 license.
