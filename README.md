# CRDS — Context-Rich Design Scenarios

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Version](https://img.shields.io/badge/Version-1.0-blue.svg)](#9-versioning)
[![Scenarios](https://img.shields.io/badge/Scenarios-3%2C200-brightgreen.svg)](#3-statistics)
[![Paper](https://img.shields.io/badge/Paper-Scientific%20Reports%202026-orange.svg)](#10-citation)

A curated dataset of **3,200 context-rich design scenarios** for research on intelligent colour-palette generation, accessibility-aware design, and vision–language modelling.

**Companion dataset for**: Liu, F. *Context-Aware Intelligent Colour Design via Multi-Objective Optimisation and Vision–Language Models*, *Scientific Reports*, 2026.

---

## 1. Overview

Existing public colour-palette benchmarks (O'Donovan, Schloss–Palmer, Adobe Kuler, InfoColorizer) provide only short captions or layout primitives — not full design briefs with explicit audience and domain context. CRDS fills this gap by pairing each scenario with:

- a textual **design brief** (≈42 words on average);
- an **application-domain code** (web/UI, marketing, infographic, e-commerce);
- an **audience descriptor** drawn from seven categories (children through professional/design-aware);
- a **reference image** for each scenario;
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
| `U01` | Children (5–12)                        | high-contrast         |
| `U02` | General adults                         | standard              |
| `U03` | Elderly (60+)                          | high-contrast         |
| `U04` | Low-vision                             | WCAG-AA compliance    |
| `U05` | Colour-vision-deficient                | CVD-safe palettes     |
| `U06` | Visually impaired (extended)           | maximum contrast      |
| `U07` | Professional (design-aware)            | standard              |

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
├── load_crds.py                    — reference Python loader (no external deps)
└── images/                         — 3,200 reference images (JPEG, 512×512)
```

**Reference images**: each scenario record exposes a `reference_image` field of the form `images/CRDS-{DOMAIN}-NNNN.jpg`. All 3,200 scenarios include a reference image. To respect the licensing terms of the original source imagery, image files are *not* redistributed in this repository; researchers who require them should contact the maintainer (see §11).

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

---

## 6. Construction methodology

### 6.1 Brief generation
Textual briefs were drafted by the author drawing from real-world design specifications and stylistic conventions across the four domains. Every brief was reviewed for clarity and de-duplicated against all earlier briefs in the same domain.

### 6.2 Annotator selection
Three professional designers were recruited as paid contractors. Each held 5–11 years of professional experience in screen design, agreed to the project terms, and was compensated at standard professional contractor rates for the region. No personal information about the annotators is included in this release.

### 6.3 Annotation procedure
Each annotator was given the brief, the audience descriptor, and the reference image, and was asked to produce a 5-colour palette in CIELAB that, in their professional judgement, best served the scenario. Annotators worked independently and no inter-annotator discussion was permitted during the labelling phase. The annotation workflow per scenario was: (1) read the brief and view the reference image; (2) browse a recommended set of palettes from a small in-tool generator; (3) iteratively refine until satisfied; (4) submit the final palette with a confidence rating.

### 6.4 Gold-palette consolidation
For each scenario, the three independent palettes were consolidated into a single gold-standard palette by a fourth experienced designer (the consolidator), who was instructed to choose the most representative palette or, when no single palette dominated, to construct a hybrid that respected the consensus across the three annotators. The consolidator's identity was blinded from the annotators.

### 6.5 Inter-annotator agreement
We report Krippendorff's α for the underlying three-rater data, treating each colour position as an ordinal rating on 11 perceptual hue bins in CIELAB. Pooled α across the dataset is **0.78**; per-scenario α is recorded in `annotator_kappa`.

---

## 7. Ethics

CRDS construction is a standard ML-dataset annotation activity carried out with paid professional contractors, not a human-subjects study. No personal data, behavioural data, or psychological measurement was collected from the annotators. Accordingly, no ethics committee approval was required, in line with the institution's standard guidance for paid contractor work on labelling tasks.

Reference images included in the `images/` distribution are either researcher-created, licensed for research use, or sourced from publicly accessible design references for non-commercial academic research purposes.

---

## 8. Limitations

1. **Cultural and stylistic bias.** All three annotators trained and worked in Western screen-design conventions. The dataset reflects those stylistic priors and should not be assumed to generalise to traditions outside that scope without further validation.
2. **Single consolidated palette.** Only one gold-standard palette per scenario is released. Researchers wanting per-annotator variability (the raw three-palette inputs prior to consolidation) should contact the maintainer.
3. **Domain coverage.** Four domains is small relative to a full design taxonomy. Extension to additional domains (e.g. branding, packaging, editorial) is encouraged.
4. **Reference imagery not redistributed.** Image files are not included in this release due to licensing constraints. Researchers who require them should contact the maintainer.
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

## 11. Contact

Maintainer: Fang Liu — fanglin3234@gmail.com
