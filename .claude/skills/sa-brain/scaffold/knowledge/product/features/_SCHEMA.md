# Architecture Component / Platform Decision Schema

Filename: `<slug>.md`. One file per architecture component or platform decision — the operational hub linking hypotheses, decisions, metrics, stakeholders, and ingestion.

An architecture component or platform decision is a technology choice that shapes how the system is built or operated — e.g., "which CMS to adopt", "monolith vs. microservices", "cloud provider selection", "build vs. buy for auth", "data warehouse migration". It is NOT a functional product feature (e.g., "news item needs an image"). Functional requirements belong in product docs; architecture decisions belong here.

## Meta
- Owner: <SA name>
- Status: evaluating | piloting | adopted | deprecated | rejected | archived
- Priority:
- Last updated: YYYY-MM-DD

## Architectural problem / challenge
<!-- What architecture problem or constraint this addresses -->

## Consuming teams / dependent systems
<!-- Which teams implement or depend on this component — links to stakeholders/ or knowledge/users/ -->

## Adoption criteria / technical KPIs
<!-- What measurable outcomes define success: latency targets, operational overhead reduction, migration cost, team capability fit, TCO, vendor SLA compliance, etc. -->

## Risks
<!-- Brief summary; full hypotheses live in hypotheses/<slug>.md — five risk areas: technical, integration, operational, cost/vendor, migration -->

## Dependencies
<!-- Teams, systems, external partners, vendor SLAs, licensing constraints, team capability gaps -->

## Timeline
<!-- Key evaluation milestones, PoC windows, decision deadlines, migration phases if relevant -->

## Evidence
<!-- Links to relevant ingestion artifacts (RFPs, vendor docs, PoC results, assessments, benchmark reports) -->

## Linked
<!-- Paths are relative to THIS file's location (knowledge/product/features/<slug>.md). -->
- Hypotheses: `../../../hypotheses/<slug>.md`
- Decisions (ADRs): `../../../decisions/YYYY-MM-DD-<slug>.md`
- Stakeholders affected: `../../../stakeholders/<slug>.md`

## Open questions

## Post-adoption review
<!-- What to measure after adoption, when to check back, what would trigger a reversal decision -->
