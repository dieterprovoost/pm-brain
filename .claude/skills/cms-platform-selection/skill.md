---
name: cms-platform-selection
description: >-
  Generates a weighted CMS platform selection scorecard in Excel (.xlsx) for a
  given client RFQ or requirements list. Use when the user asks to evaluate,
  compare, or score CMS platforms, or when creating a CMS selection deliverable
  from an RFQ or requirements file.
---

# CMS Platform Selection Scorecard

Produces a populated Excel scorecard — based on the agency scorecard template — that scores up to three CMS platforms against client-specific requirements extracted from an input file.

## Prerequisites

- `openpyxl` installed in the active Python environment.  
  If missing: `python3 -m venv /tmp/xlsx_env && source /tmp/xlsx_env/bin/activate && pip install openpyxl -q`
- Template at: `templates/CMS-selection-scorecard-template.xlsx`
- Client requirements in `input/` (Excel or other readable format)
- Output will be saved to: `deliverables/[ClientName]-CMS-Platform-Selection-Scorecard.xlsx`

## Workflow

### Step 1 — Read client requirements

Read the requirements file in `input/`. Use Python + openpyxl (or the Read tool for .md/.csv) to extract all requirements. Note:
- MoSCoW priority (Must Have = weight 4–5, Should Have = 3, Could Have = 1–2)
- Domain / epic for category mapping
- Technology column (identifies CMS-owned vs. integration-owned requirements)

### Step 2 — Choose three CMS platforms

Based on the technical context and client requirements, propose three platforms for comparison. Typical candidates:

| Category | Examples |
|---|---|
| Headless SaaS | Sanity, Storyblok, Contentful, Contentstack |
| Composable / DXP | Optimizely SaaS CMS |
| Open-source | Drupal, Craft CMS, WordPress |
| Headless self-hosted | Drupal, Craft CMS, Payload CMS |

Confirm with the user before proceeding if the choice is non-obvious.

### Step 3 — Map requirements to the six standard categories

Organise all CMS-relevant requirements under these categories. Requirements that belong to the integration or front-end layer only (e.g. analytics, hosting infrastructure, QA process) may be omitted or grouped under the closest category.

| # | Category | Typical requirements |
|---|---|---|
| 1 | Architecture & Core Fit | Headless/API, hosting, localisation, GDPR, SSO |
| 2 | Editor Experience | Visual editor, page builder, scheduling, RTL, version history |
| 3 | Editorial Autonomy (No Developer) | Forms, navigation, SEO fields, workflows without dev |
| 4 | Content Architecture & Governance | Blocks, translation, DAM, taxonomy, governance |
| 5 | Product Catalogue & Data Integrations | PIM, CRM, search, data sync, auto-generated pages |
| 6 | SEO, Compliance & Optimisation | SEO control, structured data, WCAG, A/B testing, GDPR |

Aim for 5–7 requirements per category. Assign weights:
- **5** — business-critical Must Have
- **4** — important Must Have
- **3** — Should Have
- **1–2** — Could Have

### Step 4 — Score each platform

Score every requirement for each platform:

| Score | Meaning |
|---|---|
| 3 | Strong native capability |
| 2 | Partial / requires configuration |
| 1 | Weak / plugin-dependent |
| 0 | Not supported (hard blocker) |

Keep comments factual and brief (one sentence per cell). A score of 0 on a Must Have is an automatic disqualifier — flag it explicitly.

### Step 5 — Run the generator script

Fill the `CATEGORIES` data structure in the script (see format below), then execute:

```bash
source /tmp/xlsx_env/bin/activate
cd /path/to/project
python3 skills/cms-platform-selection/scripts/generate_scorecard.py
```

The script reads the template, builds the scorecard, and writes the output to `deliverables/`.

## CATEGORIES data structure

Each entry in `CATEGORIES` is a tuple of `(category_name, requirements_list)`.  
Each requirement is an 8-tuple:

```python
(
    "Requirement label",   # str  — shown in column B
    weight,                # int  — 1–5 (column C)
    p1_score,              # int  — 0–3 for platform 1
    "p1_comment",          # str  — justification for platform 1
    p2_score,              # int  — 0–3 for platform 2
    "p2_comment",          # str  — justification for platform 2
    p3_score,              # int  — 0–3 for platform 3
    "p3_comment",          # str  — justification for platform 3
)
```

Example:

```python
CATEGORIES = [
    ("1. Architecture & Core Fit", [
        ("Headless / API-first architecture",
         5,
         3, "API-first with strong developer flexibility.",
         3, "Headless-first with mature Visual Editing layer.",
         3, "SaaS CMS is fully headless and API-driven."),
        # … more requirements
    ]),
    # … more categories
]
```

## Output

The script produces `deliverables/[CLIENT_NAME]-CMS-Platform-Selection-Scorecard.xlsx` with:
- Platform names in the header row
- Weighted score formulas auto-calculated per requirement
- TOTAL rows per category
- GRAND TOTAL, Max score, and % rows at the bottom

## Key principles

- **Requirements first.** Complete Steps 1–4 before running the script.
- **Must Haves dominate.** A score of 0 on a weight-5 requirement outweighs total scores.
- **One sentence per comment.** Keep justifications factual, not promotional.
- **Flag assumptions.** If a score is inferred rather than verified, note it in the comment.
