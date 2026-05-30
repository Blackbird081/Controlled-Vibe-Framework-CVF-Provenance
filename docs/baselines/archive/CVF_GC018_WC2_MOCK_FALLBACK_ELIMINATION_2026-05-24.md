# GC-018: WC-2 Mock Fallback Elimination

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-24

---

## Purpose

Authorize a bounded WC-2 corrective tranche so failed live execution attempts
never produce fabricated demo output.

## Scope / Target / Owner Boundary

Scope: existing non-coder ProcessingScreen execution failure handling.

Target:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.test.tsx`

Owner: Codex implementer with product, QA, governance, and release review roles.

Out of scope: provider behavior, route semantics, receipt-envelope fields,
new templates, memory reinjection, hosted readiness, production readiness, or
freeze release.

## Depth Audit

Depth score: 8/10.

Rationale:

- V1 already blocked mock fallback for classified V3 diagnostic failures.
- An unclassified `success=false`, parse failure, or network exception could
  still fall through to `runMockExecution()`.
- This is a localized trust correction, not a new governance surface.

## Source / Predecessor Evidence

- WC roadmap:
  `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- V1 closure:
  `docs/reviews/CVF_V1_NONCODER_FIRST_VALUE_JOURNEY_HARDENING_COMPLETION_2026-05-24.md`
- V3 diagnostic standard:
  `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`

## Authorized Change

- Preserve mock/demo execution only for the no-real-input demo path.
- When a real `/api/execute` attempt returns failure without a diagnostic,
  show a user-visible failure state.
- When a real `/api/execute` attempt throws at network/parse level, show a
  user-visible failure state.
- Do not call `generateMockOutput()` after a failed real attempt.

## Decision / Baseline / Proposed Tranche

Decision: continue.

Baseline: V1 blocks mock fallback only when a classified V3 diagnostic is
present.

Proposed tranche: WC-2 removes the remaining fallback path for unclassified
failed real execution attempts.

## Evidence Plan

- Focused ProcessingScreen tests.
- Typecheck.
- Mandatory release gate.

## Acceptance Criteria

- [ ] Unclassified live failures do not call mock completion.
- [ ] Network/parse-level live failures do not call mock completion.
- [ ] Classified V3 diagnostic behavior remains intact.
- [ ] Existing successful execution behavior remains intact.

## Claim Boundary

WC-2 may claim only truthful failure handling for the implemented
ProcessingScreen real-execution paths. It does not claim provider stability,
universal diagnostics, route/provider behavior changes, hosted readiness,
production readiness, or new governance authority.
