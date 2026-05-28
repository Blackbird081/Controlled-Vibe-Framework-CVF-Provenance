# GC-018 - Canonical CLI Runtime Gateway

Memory class: SUMMARY_RECORD

Status: ACCEPTED
Date: 2026-05-22
docType: baseline

## Purpose
Authorize a bounded implementation tranche that turns the existing Governance CLI command surface into a unified canonical `cvf` CLI runtime gateway.

## Scope / Target / Owner Boundary
In scope:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/package.json`
- `docs/work_orders/CVF_WO_CANONICAL_CLI_RUNTIME_GATEWAY_2026-05-22.md`
- `docs/reviews/CVF_CANONICAL_CLI_RUNTIME_GATEWAY_COMPLETION_2026-05-22.md`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V11_2026-05-21.md`

Out of scope:

- `/api/execute` route behavior.
- Provider adapter behavior or provider execution semantics.
- New receipt-envelope fields.
- New memory tiers or persistence.
- Public-sync repository updates.
- Hosted/SaaS readiness claims.
- Maika, child-data, photo, or vision claims.
- Freeze release.

## Target / Source Under Review
Source driver: operator request on 2026-05-22 to make CVF have a unified canonical CLI runtime gateway.

Prior evidence:

- `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
- `docs/reviews/archive/CVF_CDH_C_CLI_LIVE_PROOF_COMPLETION_2026-05-21.md`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`

## Source / Predecessor Evidence
Predecessor evidence establishes that `cvf execute` already exists and that the remaining gap is a unified canonical `cvf` gateway posture:

- `docs/reviews/archive/CVF_CDH_C_CLI_LIVE_PROOF_COMPLETION_2026-05-21.md`
- `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`

## Scope / Methodology
This tranche may:

- define `cvf` as the canonical gateway name for the CLI package;
- preserve existing `cvf-guard` behavior as a legacy alias where useful;
- add a typed gateway wrapper around the existing `GovernanceCLI`;
- make command usage consistently describe the canonical `cvf` surface;
- prove `cvf run`, `cvf audit`, `cvf execute`, `cvf skill`, `cvf receipt`, `cvf trace`, and `cvf provider` through tests.

This tranche may not:

- reimplement the web execute route;
- add new provider semantics;
- add live provider claims unless a separate live-proof work order is filed;
- claim public product readiness.

## Evidence Trace Block
Required closure evidence:

- Governance CLI targeted tests pass.
- Governance CLI full tests pass.
- Governance CLI TypeScript check passes.
- `cvf run --dry-run` delegates through the canonical gateway to existing execute payload construction without HTTP I/O.
- `cvf execute --help` remains available.
- `cvf audit` is available under canonical `cvf` usage.
- `cvf skill`, `cvf receipt`, `cvf trace`, and `cvf provider` remain read-only inspection commands.
- Local governance hook chain passes.

## Findings / Position
Accepted as a bounded implementation tranche. The current repository already has `cvf execute` and read-only command wrappers, but not a single canonical gateway abstraction that declares and tests the `cvf` runtime surface as the entrypoint.

## Risk / Corrective Action
Risk: the phrase "canonical execution gateway" could be overread as a public hosted runtime or all-provider execution guarantee.

Corrective action: the completion review must state that the tranche proves a package-level canonical CLI gateway only, reusing existing route/provider behavior.

## Decision / Recommendation / Disposition
Disposition: `ACCEPTED_FOR_IMPLEMENTATION`.

Recommendation: implement this as a narrow package-level CLI gateway tranche and return broader runtime/distribution work to a later GC-018 if needed.

## Verification
Pre-condition satisfied: Review-CVF V2 T1-T5 batch is closed and the operator selected this next tranche explicitly.

## Claim Boundary
This GC-018 authorizes a canonical CLI gateway abstraction and tests inside the existing Governance CLI package. It does not authorize public-sync changes, provider/runtime semantics changes, route changes, new receipt envelopes, durable persistence, hosted readiness, or broad public claims of a coherent governed capability runtime.
