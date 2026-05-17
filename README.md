# CRDS — Context-Rich Design Scenarios

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Version](https://img.shields.io/badge/Version-1.0-blue.svg)](#9-versioning)
[![Scenarios](https://img.shields.io/badge/Scenarios-3%2C200-brightgreen.svg)](#3-statistics)
[![Paper](https://img.shields.io/badge/Paper-Scientific%20Reports%202026-orange.svg)](#10-citation)

A curated dataset of **3,200 context-rich design scenarios** for research on intelligent colour-palette generation, accessibility-aware design, and vision–language modelling.

**Companion dataset for**: Liu, F. *Context-Aware Intelligent Colour Design via Multi-Objective Optimisation and Vision–Language Models*, *Scientific Reports*, 2026.

---

## Contents

1. [Overview](#1-overview)
2. [Quick start](#2-quick-start)
3. [Statistics](#3-statistics)
4. [Repository structure](#4-repository-structure)
5. [Record schema](#5-record-schema)
6. [Construction methodology](#6-construction-methodology)
7. [Ethics](#7-ethics)
8. [Limitations](#8-limitations)
9. [Versioning](#9-versioning)
10. [Citation](#10-citation)
11. [Contact and licence](#11-contact-and-licence)

---

## 1. Overview

Existing public colour-palette benchmarks (O'Donovan, Schloss–Palmer, Adobe Kuler, InfoColorizer) provide only short captions or layout primitives — not full design briefs with explicit audience and domain context. CRDS fills this gap by pairing each scenario with:

- a textual **design brief** (≈42 words on average);
- an **application-domain code** (web/UI, marketing, infographic, e-commerce);
- an **audience descriptor** drawn from seven categories (children through accessibility-first);
- an optional **reference image** (present in ≈65% of scenarios);
- a **5-colour gold palette** in both RGB hex and CIELAB (D65) coordinates;
- **inter-annotator agreement** at the scenario level (Krippendorff's α).

CRDS is intended as supplementary evaluation evidence; the main quantitative claims of the accompanying paper are reported on the established public benchmarks.

---

## 2. Quick start

```bash
git clone https://github.com/fanglin3234-sudo/Context-Aware-Color-Design-Dataset.git
cd Context-Aware-Color-Design-Dataset
python load_crds.py crds_v1.0_FULL.jsonl
```

The reference loader prints a summary (totals by domain and audience, mean inter-annotator agreement) and the first record in full.

Minimal programmatic use:

```python
import json

with open("crds_v1.0_FULL.jsonl") as f:
    records = [json.loads(line) for line in f]

web_ui = [r for r in records if r["domain"] == "web_ui"]
print(f"{len(web_ui)} web/UI scenarios, mean κ = "
      f"{sum(r['annotator_kappa'] for r in web_ui) / len(web_ui):.3f}")
```

Three equivalent flat-file forms are provided so the dataset is loadable with any common data-science stack:

| File | Use this if you prefer… |
|---|---|
| `crds_v1.0_FULL.jsonl` | streaming / line-by-line / preserving nested arrays |
| `crds_v1.0_FULL.csv`   | pandas `read_csv`, spreadsheet inspection |
| `crds_v1.0_FULL.tsv`   | tab-delimited tooling, R `read.delim` |

---

## 3. Statistics

| Domain code | Domain name        | Scenarios | Avg. brief length |
|-------------|--------------------|-----------|-------------------|
| `web_ui`    | Web / UI            | 900       | 38 ± 16 words     |
| `marketing` | Marketing posters   | 800       | 47 ± 19 words     |
| `infographic` | Data infographics | 700       | 41 ± 17 words     |
| `ecommerce` | E-commerce listings | 800       | 43 ± 18 words     |
| **Total**   |                    | **3,200** | **42 ± 18**       |

**Inter-annotator agreement**: pooled Krippendorff's α = **0.78** across the three independent annotators, treating each colour position as an ordinal rating on 11 perceptual hue bins in CIELAB. Per-scenario α is stored in the `annotator_kappa` field.

**Audience distribution** (7 categories):

| Code  | Audience                              | Accessibility profile |
|-------|---------------------------------------|------------------------|
| `U01` | Children (under 12)                    | high-contrast         |
| `U02` | Teens (13–17)                          | standard              |
| `U03` | Young adults (18–29)                   | standard              |
| `U04` | General adults (30–49)                 | standard              |
| `U05` | Older adults (50+)                     | high-contrast         |
| `U06` | Professional / B2B                     | standard              |
| `U07` | Mixed / accessibility-first            | WCAG-AA compliance    |

---

## 4. Repository structure

```
Context-Aware-Color-Design-Dataset/
├── README.md                       — this file
├── LICENSE.txt                     — CC BY-NC 4.0 (dataset licence)
├── crds_v1.0_FULL.jsonl            — main dataset, one scenario per line
├── crds_v1.0_FULL.csv              — flat CSV form (same data)
├── crds_v1.0_FULL.tsv              — tab-separated form (same data)
├── crds_v1.0_sample_preview.pdf    — printable preview of a representative subset
├── schema.json                     — JSON Schema (Draft-07) for one scenario
├── annotation_guidelines.md        — instructions given to annotators
└── load_crds.py                    — reference Python loader (no external deps)
```

**Reference images**: each scenario record exposes a `reference_image` field of the form `images/CRDS-{DOMAIN}-NNNN.jpg`. Approximately 65% of scenarios have a non-null entry. To respect the licensing terms of the original source imagery, image files are *not* redistributed in this repository; researchers who require them should contact the maintainer (see §11). The textual brief alone is sufficient for the experiments reported in the accompanying paper.

**Train / val / test splits**: not bundled. We recommend an 80/10/10 random split *stratified by domain* (so each domain's proportional representation is preserved) with a fixed seed for reproducibility.

---

## 5. Record schema

Each line of `crds_v1.0_FULL.jsonl` is a single JSON object. The full schema (machine-readable in `schema.json`) is:

| Field | Type | Description |
|---|---|---|
| `scenario_id` | string | Format `CRDS-{WEB\|MKT\|INF\|ECM}-NNNN`; unique. |
| `domain` | string | One of `web_ui`, `marketing`, `infographic`, `ecommerce`. |
| `domain_index` | integer (0–3) | Numeric domain index matching the table in §3. |
| `brief` | string (20–2000 chars) | Designer-facing scenario description. |
| `audience_id` | string | `U01`–`U07` (see §3). |
| `audience_label` | string | Human-readable audience name. |
| `reference_image` | string \| null | Relative path, or `null` if image-free. |
| `gold_palette_hex` | array[5] of `#RRGGBB` | Five sRGB hex codes. |
| `gold_palette_lab` | array[5] of [L, a, b] | Five CIELAB (D65) triplets. |
| `annotator_ids` | array[3] of string | Pseudonymised annotator identifiers. |
| `annotator_kappa` | number ∈ [−1, 1] | Per-scenario Krippendorff's α. |
| `design_intent_tags` | array[2–4] of string | Keywords characterising design intent. |
| `annotation_date` | string | Date the scenario was annotated. |
| `version` | string | Dataset version this record belongs to. |

### 5.1 Example record

```json
{
  "scenario_id": "CRDS-WEB-0001",
  "domain": "web_ui",
  "domain_index": 0,
  "brief": "Educational quiz application for teens (13–17), dark-mode-first, primarily viewed on mobile. Status indicators (success, warning, error) must be clearly distinguishable.",
  "audience_id": "U02",
  "audience_label": "Teens (13–17)",
  "reference_image": "images/CRDS-WEB-0001.jpg",
  "gold_palette_hex": ["#FFB00C", "#F37C0A", "#2095C2", "#93CDF0", "#02374E"],
  "gold_palette_lab": [
    [77.49,  18.29,  79.35],
    [64.56,  40.21,  70.14],
    [57.75, -15.23, -32.01],
    [79.70,  -9.99, -23.14],
    [21.19,  -6.50, -18.58]
  ],
  "annotator_ids": ["A1", "A2", "A3"],
  "annotator_kappa": 0.87,
  "design_intent_tags": ["friendly", "dynamic", "professional"],
  "annotation_date": "2024-04-01",
  "version": "1.0"
}
```

### 5.2 CSV column order

The flat CSV and TSV forms expand nested arrays into individual columns:

```
scenario_id, domain, domain_index, brief, audience_id, audience_label,
reference_image,
hex_1, hex_2, hex_3, hex_4, hex_5,
lab_L_1, lab_a_1, lab_b_1,
lab_L_2, lab_a_2, lab_b_2,
lab_L_3, lab_a_3, lab_b_3,
lab_L_4, lab_a_4, lab_b_4,
lab_L_5, lab_a_5, lab_b_5,
annotator_a1, annotator_a2, annotator_a3, annotator_kappa,
design_intent_tags, annotation_date, version
```

`design_intent_tags` is encoded as a `;`-separated string in the flat forms (e.g. `trust;clarity;professional`).

---

## 6. Construction methodology

### 6.1 Brief generation
Briefs were drafted by the principal investigator drawing from real-world design specifications and stylistic conventions across the four domains. Every brief was reviewed for clarity and de-duplicated against all earlier briefs in the same domain.

### 6.2 Annotator selection
Three professional designers were recruited as paid contractors. Each held 5–11 years of professional experience in screen design, agreed to the project terms, and was compensated at standard professional contractor rates for the region. No personal information about the annotators is included in this release.

### 6.3 Annotation procedure
Each annotator was given the brief, the audience descriptor, and the optional reference image, and was asked to produce a 5-colour palette in CIELAB that, in their professional judgement, best served the scenario. Annotators worked independently and no inter-annotator discussion was permitted during the labelling phase.

### 6.4 Gold-palette consolidation
For each scenario, the three independent palettes were consolidated into a single gold-standard palette by a fourth experienced designer (the consolidator), who was instructed to choose the most representative palette or, when no single palette dominated, to construct a hybrid that respected the consensus across the three annotators. The consolidator's identity was blinded from the annotators.

### 6.5 Inter-annotator agreement
We report Krippendorff's α for the underlying three-rater data, treating each colour position as an ordinal rating on 11 perceptual hue bins in CIELAB. Pooled α across the dataset is **0.78**; per-scenario α is recorded in `annotator_kappa`.

---

## 7. Ethics

CRDS construction is a standard ML-dataset annotation activity carried out with paid professional contractors, not a human-subjects study. No personal data, behavioural data, or psychological measurement was collected from the annotators. Accordingly, no ethics committee approval was required, in line with the institution's standard guidance for paid contractor work on labelling tasks.

Reference images included in the optional `images/` distribution are either researcher-created, licensed for research use, or sourced from publicly accessible design references for non-commercial academic research purposes.

---

## 8. Limitations

1. **Cultural and stylistic bias.** All three annotators trained and worked in Western screen-design conventions. The dataset reflects those stylistic priors and should not be assumed to generalise to traditions outside that scope without further validation.
2. **Single consolidated palette.** Only one gold-standard palette per scenario is released. Researchers wanting per-annotator variability (the raw three-palette inputs prior to consolidation) should contact the maintainer.
3. **Domain coverage.** Four domains is small relative to a full design taxonomy. Extension to additional domains (e.g. branding, packaging, editorial) is encouraged.
4. **Optional reference imagery.** Approximately 35% of scenarios are text-brief only. Researchers building text-only baselines can ignore this; researchers building joint vision–text models should account for the asymmetry.
5. **No live user study.** Palette quality is evaluated against annotator-consolidated gold palettes, not direct end-user response. A live user study would complement, not replace, this evaluation.

---

## 9. Versioning

| Version | Date       | Changes                                              |
|---------|------------|------------------------------------------------------|
| 1.0     | 2024       | Initial release: 3,200 scenarios across 4 domains.   |

Future versions will preserve the JSONL schema and version each record via the `version` field. Breaking schema changes will increment the major version.

---

## 10. Citation

If you use CRDS, please cite the accompanying paper:

```bibtex
@article{liu2026caim,
  title   = {Context-Aware Intelligent Colour Design via
             Multi-Objective Optimisation and Vision--Language Models},
  author  = {Liu, Fang},
  journal = {Scientific Reports},
  year    = {2026},
  note    = {DOI to be assigned upon publication}
}
```

---

## 11. Contact and licence

**Maintainer**: Fang Liu, Academy of Arts, Qilu Normal University, Jinan, Shandong, 250013, China.
**Email**: <fanglin3234@gmail.com>

For questions, data requests (including raw per-annotator palettes or the reference-image bundle), or to report issues, please contact the maintainer or open an issue on this repository.

**Licence**: CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0 International). See `LICENSE.txt` for the full text. By using this dataset you agree to cite the accompanying paper and to use the data for non-commercial research purposes only.
