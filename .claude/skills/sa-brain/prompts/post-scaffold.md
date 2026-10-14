# Post-scaffold

Run after the scaffold has been copied and placeholders populated.

## 1. Routing self-test

Read `INDEX.md`, `CLAUDE.md`, and `.claude/commands/INDEX.md`. Confirm two things resolve cleanly:

### 1a. The 4 ingestion shapes route correctly

These are what `/ingest` infers from the artifact:

- Architecture doc / technical assessment → `source/assessments/`, `ingestion/assessments/`, relevant `hypotheses/<component>.md`, possibly `knowledge/product/features/<slug>.md`.
- Vendor proposal / RFP response → `source/vendor-docs/`, `ingestion/vendor-docs/`, `stakeholders/<vendor-slug>.md`, draft `decisions/` when a recommendation follows.
- Market / technology landscape signal → `source/market/`, `ingestion/market/`, `knowledge/market/` or `trends.md`, possibly `strategy.md § Tensions`.
- Meeting / 1:1 → `source/meetings/`, `ingestion/meetings/`, `stakeholders/<slug>.md`, draft `decisions/` when an architecture decision was made.
- Ad-hoc → `ingestion/adhoc/`, routed to the right durable area in-session, never parked.

### 1b. The 6 commands resolve to their spec files

For each, confirm the spec exists and the loaded/updated paths in the spec match real scaffold paths:

- `/ingest` → `.claude/commands/ingest.md`
- `/prep` → `.claude/commands/prep.md`
- `/review` → `.claude/commands/review.md`
- `/ideate` → `.claude/commands/ideate.md`
- `/risk` → `.claude/commands/risk.md`
- `/plan` → `.claude/commands/plan.md`

If a spec references a path that doesn't exist in the scaffolded brain, that's a bug. Fix it before declaring done. If routing is unclear for any ingestion shape or command, the seeded files have a bug. Fix it before declaring done.

## 2. Link verification

Walk every relative markdown link in the scaffolded files. Resolve each path against the filesystem. Fix broken links.

Common failure mode: miscounting `../` depth when linking across `knowledge/`, `stakeholders/`, `hypotheses/`, `decisions/`. The link layer is the provenance chain — broken links are memory corruption, not cosmetic.

## 2b. Coverage checks (beyond link existence)

Link walking proves a link points somewhere. It does not prove the right links exist. Run these coverage checks:

- **Component → hypothesis.** For every component file in `knowledge/product/features/` with a status in {evaluating, piloting}, expect a corresponding `hypotheses/<slug>.md`. Missing → surface as a next move, not a blocker.
- **Hypothesis ↔ feature.** Every `hypotheses/<slug>.md` should reference its feature file in `## Meta § Feature`. Orphans → flag.
- **Promoted hypothesis → decision.** Every hypothesis with status `promoted` should have a corresponding decision file linking back to it. Missing → draft the decision.
- **Decision → hypothesis (where applicable).** Every decision that resolves a bet should link the originating hypothesis under `## Linked § Hypotheses`. Missing link → flag.
- **Stakeholder touchpoints → ingestion.** Every touchpoint-log entry in `stakeholders/<slug>.md` that came from a meeting should link to its `ingestion/meetings/<file>`. Standalone touchpoints (no ingestion artifact) are fine; orphan links (pointing at missing files) are not.
- **Feature → stakeholders affected.** Every feature file's `## Linked § Stakeholders affected` should list at least one stakeholder, or be marked `TODO: none yet identified`. Empty without acknowledgment → flag.

Coverage gaps are surfaced as immediate next moves (§ 3), not as scaffolding failures. The point is to make missing wiring visible, not to block.

## 3. Surface the habit loop (primary) + scaffold gaps (secondary)

The day-one risk isn't an incomplete scaffold. It's the operator never returning to use the system. Frame next moves as habit-forming actions first, not scaffold completion.

### Three habit actions — lead with these

Always surface these three first, in this order:

1. **Ingest one real artifact today.** "Paste your most recent vendor proposal / architecture assessment / meeting notes. I'll show you what the system does with it."
2. **Prep your next conversation.** "Before your next review with `<highest-influence stakeholder slug>`, run `/prep <slug>`. I'll surface what to ask."
3. **Run `/review` on Friday.** "The maintenance sweep is what keeps this system alive past month three. Set a recurring calendar reminder for Friday afternoon."

These are not optional. The system dies when these don't happen.

### Then: 2-3 scaffold gaps (secondary)

After the three habit actions, surface a small number of concrete completion gaps. Specific, actionable, never more than 3:

- "Your top stakeholder `<slug>` has no concerns logged. Propose 3–4 from the interview, you confirm."
- "Component `<slug>` is being piloted but has no hypothesis file. I can draft one from the evaluation criteria when you have a moment."
- "Strategy section `Explicit non-goals` is empty. This is the highest-leverage thing to fill in next — it prevents scope creep in architecture evaluations."

If there are more than 3 gaps, pick the three highest-leverage. Don't dump a punch list — that's how operators get overwhelmed and abandon the system.

## 4. Surface contradictions (required)

List 1–3 contradictions found during scaffolding, with multi-source evidence per item. These are typically the highest-value items on day one.

Look specifically for:
- Conflicting stakeholder mandates (CTO wants cloud-agnostic, engineering lead wants AWS-native for speed).
- Signals pointing opposite ways (vendor benchmark claims excellent performance; PoC results show overhead).
- Strategy vs. observed work (strategy says operational simplicity; active evaluations lean toward complex distributed systems).
- Inter-document conflicts in migration mode (two strategy docs, two roadmaps, conflicting architecture principles).

Format each as:
- **Signal:** what was observed
- **What it tensions:** which strategic claim or other signal it conflicts with
- **Where it lives in the brain:** `strategy.md § Tensions § Tn`, stakeholder file, hypothesis file

**If no genuine contradictions were found, say so explicitly.** Do not invent.

## 5. Self-test receipt

Print a 3-5 line visible block that proves the self-test ran:

```
Self-test receipt:
- Ingestion shapes routed: 4/4.
- Commands resolved: 6/6 (ingest, prep, review, ideate, risk, plan).
- Links walked: 47. Broken: 3. Fixed: 3.
- Coverage checks: 6/6 categories scanned. 2 gaps flagged as next moves.
- TODO fields (SA-fillable): 12 across 8 files (see list).
- Auto-maintained fields left blank: 9 (correct).
- Contradictions surfaced: 2.
```

This block goes in the final message to the SA, not just internal reasoning.

## 6. Hand off

Final message to the operator. Order matters:

1. **The three habit actions** (do this today / this week / Friday). Specific stakeholder slug, specific feature, specific day.
2. **1–3 contradictions surfaced** (or explicit "none found"). These are the highest-leverage open items.
3. **2–3 scaffold gaps** worth filling soon — no more.
4. **One paragraph** on what was built.

Do NOT lead with "your scaffold is ready" or a folder map. Lead with the action that produces value in the next 24 hours.

Then stop and wait for the operator's first real task.
