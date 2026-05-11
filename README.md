CRDS Dataset
Context-Rich Design Scenarios for Intelligent Colour Design

Companion dataset for:
Context-Aware Intelligent Colour Design via Multi-Objective Optimisation and Vision–Language Models


License: CC BY-NC 4.0

1. Overview

CRDS (Context-Rich Design Scenarios) is a dataset designed for research on intelligent colour palette generation, accessibility-aware design, and context-aware visual recommendation systems.

Each scenario contains:

a textual design brief,
a domain label,
an audience descriptor,
an optional reference image,
and a five-colour reference palette represented in HEX and CIELAB colour spaces.

The dataset supports research in:

colour palette generation,
computational aesthetics,
accessibility-aware design,
vision–language modelling,
and multi-objective optimisation for visual design.
2. Dataset Structure
CRDS_v1.0/
├── README.md
├── LICENSE.txt
├── schema.json
├── annotation_guidelines.md
├── crds_v1.0_FULL.csv
├── crds_v1.0_FULL.jsonl
├── crds_v1.0_FULL.tsv
├── crds_v1.0_sample_preview.pdf
├── load_crds.py
└── images/
3. Dataset Statistics
Domain	Scenarios
Web / UI	900
Marketing	800
Infographics	700
E-commerce	800
Total	3,200

Average brief length: approximately 42 words.

Approximately 65% of scenarios include a reference image.

4. Audience Categories
Code	Audience
U01	Children (under 12)
U02	Teens (13–17)
U03	Young adults (18–29)
U04	General adults (30–49)
U05	Older adults (50+)
U06	Professional / B2B
U07	Accessibility-first / mixed audience
5. File Description
File	Description
crds_v1.0_FULL.jsonl	Main JSONL dataset
crds_v1.0_FULL.csv	Flat CSV version
crds_v1.0_FULL.tsv	Tab-separated version
schema.json	Dataset schema
annotation_guidelines.md	Annotation instructions
load_crds.py	Example Python loader
crds_v1.0_sample_preview.pdf	Sample dataset preview
LICENSE.txt	License information
6. Scenario Format

Each record contains:

scenario identifier,
design brief,
application domain,
audience information,
optional reference image,
and a five-colour reference palette.

Example:

{
  "scenario_id": "CRDS-WEB-0001",
  "domain": "web_ui",
  "brief": "Modern online-banking dashboard for a regional bank.",
  "audience_id": "U06",
  "reference_palette_hex": [
    "#0F2A44",
    "#1F4E79",
    "#5B9BD5",
    "#D9E2EC",
    "#F2F4F7"
  ]
}
7. Annotation Process

Reference palettes were created and reviewed by professional designers following internal annotation guidelines.

Each scenario was evaluated using:

the design brief,
audience information,
and optional reference imagery.

Final palettes were consolidated to ensure perceptual consistency across the dataset.

No personal or sensitive information is included in this release.

8. Accessibility Considerations

CRDS includes accessibility-aware scenarios intended to support research on:

WCAG-aware colour recommendation,
readability-aware interface design,
perceptual contrast optimisation,
and inclusive visual communication.
9. Reference Images

Reference images were either:

researcher-created,
licensed for research usage,
or sourced from publicly accessible design references for non-commercial academic research purposes.

Images are included solely for research and educational use.

10. Intended Usage

CRDS is intended for non-commercial academic and research use in:

intelligent colour design,
visual recommendation systems,
accessibility-aware design,
computational aesthetics,
and vision–language research.
11. Limitations
The dataset reflects the stylistic conventions represented during annotation.
Only one consolidated reference palette is provided per scenario.
Domain coverage is limited to four application categories.
Some scenarios contain text-only descriptions without reference imagery.
12. License

This dataset is released under:

Creative Commons Attribution–NonCommercial 4.0 International (CC BY-NC 4.0)

