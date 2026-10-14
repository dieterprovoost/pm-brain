# Interview

Run before scaffolding. Ask in **batches of 3–4 questions**, not one-by-one. Tone: short, direct, no lecturing.

In migration mode, **skip batches already covered by source artifacts** and ask only the unknowns. Tell the SA what you already know before asking what you don't.

## Batch A — Architecture context
1. Organization name, product/system, and one-line description of what it does technically.
2. Stage (greenfield / active-growth / legacy-modernization / migration-in-progress) and rough scale (users, traffic, team size, infrastructure footprint — whatever they know).
3. Their SA scope: which systems / domains / teams do they own or advise?
4. Top 3 architecture priorities for the next 1–2 quarters (e.g., "evaluate CMS platform", "migrate auth to platform X", "reduce operational overhead") — rough is fine; we'll refine.

## Batch B — Stakeholders and rituals
1. Name + role of their top 5–10 stakeholders (CTO, engineering leads, DevOps lead, security lead, product owner, key vendors if applicable).
2. Which 2–3 of those are **highest-friction or highest-leverage** right now?
3. Standing rituals worth encoding: architecture review board, design reviews, post-mortems, vendor review cadence, etc.

## Batch C — Active architecture work
1. What architecture components / platforms are **currently being evaluated or decided**? (list 2–6, slug-ify them — e.g., `cms-evaluation`, `auth-platform`, `data-warehouse-migration`)
2. What's the **next big bet** being scoped but not yet started?
3. Any recently **adopted** technology they're still measuring or validating?

## Batch D — Inputs and decision process
1. How are architecture decisions currently made? (RFPs, PoCs, benchmarks, architecture review board, incident post-mortems, vendor-led evaluations, engineering team spikes)
2. Where do architecture docs, PoC results, and vendor proposals currently live? Is there an existing ADR practice?
3. What technology landscape / market signals do they track? (vendor roadmaps, industry conference outputs, ecosystem shifts, competitor architecture choices)

## Batch E — Operating preferences
1. Autonomy level: should the system **act and tell** (default), or **propose and wait**? Recommend "act and tell" for anything reversible. Stored in `CLAUDE.md § Operating preferences § Autonomy mode`.
2. Maintenance cadence preference: weekly review? on-demand only? both? Stored in `CLAUDE.md § Operating preferences § Maintenance cadence`.
3. Anything explicitly **off-limits** beyond the defaults? Defaults: avoid PII, avoid verbatim vendor NDA content (note existence + link instead). Synthetic names and work emails are allowed. Stored in `CLAUDE.md § Off-limits`.

## After the interview

1. **Summarize back what you heard in 6–10 bullets.**
2. **Surface contradictions.** Examples: "You said greenfield but listed 5 active evaluations — which is real?" "Your top stakeholder is high-friction *and* you said architecture review cadence is quarterly — is that the right rhythm for your decision pace?"
3. **Confirm before scaffolding.** Do not move on without explicit confirmation.

## What the answers feed

| Batch | Question | Populates |
| --- | --- | --- |
| A | Q1-2 org/system/stage | `knowledge/strategy.md` (top section), `README.md` (system line, optional) |
| A | Q3 SA scope | `knowledge/org/team.md` |
| A | Q4 priorities | `knowledge/strategy.md § 1–2 quarter architecture priorities` |
| B | Q1 stakeholders | `stakeholders/<slug>.md` (one per person), `stakeholders/INDEX.md` (roster) |
| B | Q2 friction/leverage | `stakeholders/<slug>.md § Snapshot` (influence + friction), `stakeholders/INDEX.md` |
| B | Q3 rituals | `knowledge/org/rituals.md` |
| C | Q1 active evaluations | `knowledge/product/features/<slug>.md` (one per component), `knowledge/product/roadmap.md § Now` |
| C | Q2 next big bet | `knowledge/product/roadmap.md § Next` |
| C | Q3 recently adopted | `knowledge/product/roadmap.md § Now` (with status: piloting or measuring), component file |
| D | Q1 decision process | `knowledge/org/tools.md`, `rules/data.md § Source of truth per metric` |
| D | Q2 docs / ADR practice | `rules/discovery.md § Cadence`, `rules/discovery.md § Where architecture docs live` |
| D | Q3 technology signals | `knowledge/market/landscape.md`, `knowledge/market/trends.md` |
| E | Q1 autonomy | `CLAUDE.md § Operating preferences § Autonomy mode` |
| E | Q2 maintenance cadence | `CLAUDE.md § Operating preferences § Maintenance cadence` |
| E | Q3 off-limits | `CLAUDE.md § Off-limits` |

Keep provenance: every populated field should be traceable back to a specific Batch question or a source artifact. If a Batch answer has no clear home, flag it in the post-scaffold "immediate next moves" rather than silently dropping it.

## Provenance vocabulary, not provenance workflow

When you write claims into hypotheses, insights, or decisions, tag each row with a provenance marker from the enum in `hypotheses/_SCHEMA.md`. Claims born in this interview (no artifact behind them) are legitimate inputs — tag them `(stakeholder-verbal, <SA>, <date>)` or `(chat, no artifact)` rather than fabricating an ingestion record. The auditability promise is "every claim wears its source," not "every claim went through synthesis."
