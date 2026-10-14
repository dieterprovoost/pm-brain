---
name: double-diamond
description: >-
  Applies the double-diamond problem-solving framework across two diamonds and
  four phases (Discover, Define, Develop, Deliver). Use when structuring
  discovery work, approach documents, problem framing, solution design,
  workshops, or when the user mentions double-diamond, design thinking, or
  diverge/converge.
---

# Double Diamond

We follow the double-diamond approach consisting of the following:

```
     DISCOVER          DEFINE              DEVELOP           DELIVER
  (diverge) ──► (converge)    (diverge) ──► (converge)
       ◇───────────◇                ◇───────────◇
   Problem space                 Solution space
   (Diamond 1)                   (Diamond 2)
```

## Phase 1: The Problem Space (Diamond 1)

The first diamond explores the underlying problem to ensure you are designing the right thing.

### Discover (Diverge)

**What it is:** Open-minded exploration to gather information, conduct user research, and observe pain points.

**Core skill:** Empathy & Active Listening. Conducting user interviews, contextual inquiries, and surveys without rushing to conclusions.

**Apply:**
- Stay in diverge mode — breadth over commitment
- Capture raw insights, pain points, and context
- Do not solution or scope during this phase

**Exit when:** Enough breadth to see patterns; major unknowns are identified

### Define (Converge)

**What it is:** Synthesizing research to identify the root problem and define a clear, actionable challenge.

**Core skill:** Synthesis & Pattern Recognition. Grouping insights into themes, writing problem statements, and prioritizing focus areas.

**Apply:**
- Separate symptoms from root causes
- Produce a shared problem statement, constraints, and success criteria
- Do not move to Diamond 2 until the problem is agreed

**Exit when:** Stakeholders agree on *what* to solve and *why*; scope boundaries are explicit

## Phase 2: The Solution Space (Diamond 2)

The second diamond focuses on creating and executing the best possible solution to the defined problem.

### Develop (Diverge)

**What it is:** Brainstorming, co-designing, and creating multiple potential solutions.

**Core skill:** Ideation & Prototyping. Sketching ideas, building low-fidelity prototypes, and encouraging out-of-the-box thinking.

**Apply:**
- Generate multiple credible options before choosing one
- Use low-fidelity prototypes, sketches, and trade-off analysis
- Do not commit to the first idea or over-engineer fidelity

**Exit when:** At least two viable directions are explored; key unknowns are reduced

### Deliver (Converge)

**What it is:** Testing, refining, and selecting the most effective solution for implementation.

**Core skill:** Evaluation & Iteration. Running usability tests, measuring metrics, and managing feedback to finalize the product.

**Apply:**
- Validate against Define success criteria, not new assumptions
- Iterate from test evidence; document remaining risks
- Re-enter earlier phases when new evidence changes the problem or options

**Exit when:** Solution is validated and ready to implement or ship

## How to apply

1. **State the current phase.** Declare which phase and mode (diverge/converge) you are in before producing work.
2. **Respect phase order.** Finish Diamond 1 (Discover → Define) before Diamond 2 (Develop → Deliver).
3. **Match mode to phase.** Diverge expands options; converge narrows to a decision.
4. **Gate transitions.** Confirm exit criteria before moving to the next phase.
5. **Make outputs explicit.** Each phase produces a tangible artifact that gates the next.

When the user asks for solutions during Discover or Define, note the phase mismatch — frame options as hypotheses or complete Define first.

When in doubt, do not assume. State what is validated vs. inferred and what further discovery or validation is required.

### Phase declaration template

```markdown
## Current phase: [Discover | Define | Develop | Deliver]
**Diamond:** [1 — Problem space | 2 — Solution space]
**Mode:** [Diverge | Converge]
**Goal:** [one sentence]
**Open questions:** [list]
**Exit criteria:** [list]
```

### Document structure for approach or proposal work

```markdown
# [Project] — Approach

## Diamond 1: Problem space

### Discover
- Context, stakeholders, and key findings (evidence, not assumptions)

### Define
- Problem statement
- Success criteria and constraints
- Items requiring validation

## Diamond 2: Solution space

### Develop
- Options considered and trade-offs
- Recommended direction with rationale

### Deliver
- Validation plan
- Implementation phases and milestones
- Risks and dependencies
```
