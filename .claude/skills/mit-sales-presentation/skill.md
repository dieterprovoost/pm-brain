---
name: mit-sales-presentation
description: >-
  Structures a sales or proposal presentation as a slide-ready document using
  the MIT-inspired sales framework. Maps double-diamond approach content to
  five narrative parts (Hook, Solution, Business Case, Discussion, CTA).
  Use when creating presentation outlines, pitch decks, proposal walkthroughs,
  or when the user mentions MIT sales structure, slide structure, or
  presentation narrative.
---

# MIT-Inspired Sales Presentation

Create a **presentation structure document** — not finished slides. Each section holds the content that will become individual slides later.

## Principles

An MIT-style sales presentation structures the narrative logically by importance and process to maximize engagement and ensure your prospect clearly understands your value proposition. It avoids long texts, relies on clear visual frameworks, and keeps the audience as the hero of the pitch.

When drafting content:

- **Audience as hero** — frame the prospect's ambitions and pain, not the agency's credentials
- **Minimal on-slide text** — 3–5 bullets or labels per slide; detail goes in speaker notes
- **Visual over verbal** — prefer diagrams, workflows, before/after, metrics tables
- **Evidence over claims** — mark validated facts vs hypotheses; never invent ROI or case data
- **Logical flow** — each part answers one question before the next begins

## Inputs

Read before writing:

| Source | Use for |
|---|---|
| `deliverables/approach.md` | Problem space, solution direction, phasing, risks |
| `deliverables/rfp-summary.md` | Prospect context, scope, stated ambitions |
| `input/` | RFP and briefing documents when approach is incomplete |

If approach work is still in Discover, label draft sections and flag items needing validation.

## MIT structure → approach mapping

| Part | MIT goal | Approach source | Prospect question answered |
|---|---|---|---|
| **1. Hook & Baseline** | Frame current status and problem | Diamond 1 → Discover | "Do you understand where we are today?" |
| **2. Core Solution & Technology** | Demystify how you solve their pain | Diamond 2 → Develop | "How would this actually work for us?" |
| **3. Business Case & Social Proof** | Translate features into value | Diamond 1 → Define + Diamond 2 → Deliver | "Why should we invest — and who else has done this?" |
| **4. Interactive Discussion & Tie-Down** | Confirm understanding | Define open questions + prospect priorities | "Does this fit our priorities?" |
| **5. Clear Call to Action** | Drive next steps | Diamond 2 → Deliver | "What happens next?" |

## Workflow

1. **Read inputs** — approach, RFP summary, and any briefing in `input/`
2. **Draft table of contents** — numbered parts and slides; one idea per slide
3. **Write slide blocks** — use the slide template below for every slide
4. **Add speaker notes** — context, evidence sources, and transition lines
5. **Quality check** — run the checklist at the end before saving

## Output

Save to `deliverables/presentation-structure.md`.

Use the document template in [template.md](template.md). Adapt part titles to the project; keep the five MIT parts in order.

## Slide block template

Use for every slide in the structure document:

```markdown
### Slide [part].[number]: [Title]

**Key message:** [One sentence — what the audience must remember]

**On-slide content:**
- [Bullet 1 — max ~8 words]
- [Bullet 2]
- [Bullet 3]

**Visual framework:** [Diagram type: before/after, workflow, architecture map, metric table, timeline, comparison matrix]

**Speaker notes:** [Evidence source, nuance, transition to next slide]
```

## Part-by-part guidance

### 1. The Hook & The Baseline Situation

**Goal:** Frame their current operational status and set the problem.

**Action:** State a relatable truth or baseline that everyone agrees on.

**Example:** Frame where the client is today using a brief Before/After metaphor.

**Typical slides (4–6):**
- Opening hook — shared industry truth or customer expectation shift
- Who we are / why we're here — one slide max; prospect stays central
- Current landscape — architecture or ecosystem diagram (validated as-is)
- Key pain points — 3–5 findings, not a feature list
- The cost of status quo — performance, scale, risk (qualitative if ROI not yet quantified)
- Transition — "This is why a structured approach matters"

### 2. The Core Solution & Technology Overview

**Goal:** Demystify the product and explain how it solves the specific pain points.

**Action:** Keep the technical explanation concise; use visual assets instead of heavy text.

**Example:** Limit the technology explanation to a clear, linear workflow of how your product impacts their process.

**Typical slides (6–10):**
- Our approach at a glance — double-diamond or phased journey (Discover → Deliver)
- Recommended direction — one clear recommendation with brief rationale
- Target architecture — layered diagram (systems, services, data flows)
- How it solves [pain 1] — linear workflow, not a technology laundry list
- How it solves [pain 2] — same pattern
- Phased roadmap — timeline with value per phase (when rollout or migration applies)
- What stays the same / what changes — reduce migration fear

### 3. The Business Case & Social Proof

**Goal:** Translate technical features into concrete, quantitative value (ROI).

**Action:** Cite relevant validation from similar case studies, ensuring you speak to the business impact.

**Example:** Present key metrics on cost reduction or efficiency improvements using clear numerical data.

**Typical slides (4–6):**
- Success criteria — table mapped to prospect's stated goals
- Expected outcomes by phase — mapped to the prospect's stated goals
- Risk mitigation — top risks with mitigations (builds confidence)
- Social proof — relevant agency or sector references **only if documented**; otherwise use benchmark patterns and label as sector reference
- Investment framing — high-level phasing and effort bands if known; otherwise "to be refined in discovery"

Do not invent metrics or case studies. Use `[TBD — validate in discovery]` when data is missing.

### 4. The Interactive Discussion & Tie-Down

**Goal:** Confirm understanding and address any objections.

**Action:** Summarize the information and pause for questions directly related to their pain points.

**Example:** "Based on what we've covered, how does this solution align with the priorities you've set for this quarter?"

**Typical slides (2–3):**
- Summary — three pillars: problem, approach, path forward
- Open questions for alignment — from Define phase; invite prospect input
- Tie-down prompts — 3–4 discussion questions tied to their pain points (see template.md)

This part is designed for live conversation; slides are prompts, not monologue.

### 5. Clear Call to Action (Next Steps)

**Goal:** Drive the deal forward and eliminate open-ended conclusions.

**Action:** Outline a clear, logical step or project timeline.

**Example:** Provide an immediate task to initiate the pilot or schedule the technical review.

**Typical slides (2–4):**
- Proposed next steps — numbered, dated where possible
- Discovery / validation plan — workshops, audits, stakeholder sessions
- Decision timeline — what we need from the prospect and by when
- Close — single clear ask (e.g. align on Phase 1 kickoff workshop)

## Quality checklist

Before saving `deliverables/presentation-structure.md`:

- [ ] Table of contents lists all parts and slides with stable numbering
- [ ] Five MIT parts appear in order; no part skipped
- [ ] Every slide has key message, on-slide content, visual framework, speaker notes
- [ ] On-slide bullets are short; no paragraph text
- [ ] Prospect is the hero; agency credentials are minimal
- [ ] Validated facts are separated from hypotheses (`draft`, `TBD`, `to validate`)
- [ ] No invented ROI, case studies, or client names
- [ ] CTA ends with one concrete next step, not "let us know"

## Related skills

- [double-diamond](../double-diamond/skill.md) — source framework for approach content
- [approach-coach](../approach-coach/skill.md) — produces `deliverables/approach.md`
- [create-rfp-summary](../create-rfp-summary/skill.md) — produces `deliverables/rfp-summary.md`
