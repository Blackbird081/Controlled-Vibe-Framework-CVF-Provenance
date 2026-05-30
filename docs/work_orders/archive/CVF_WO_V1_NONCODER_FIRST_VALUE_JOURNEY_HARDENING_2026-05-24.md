# CVF Work Order: V1 Non-Coder First-Value Journey Hardening

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: work_order

Date: 2026-05-24

Tranche: V1

Roadmap: `docs/roadmaps/CVF_VALUE_SCREENED_NEXT_TRANCHE_ROADMAP_2026-05-24.md`

---

## Purpose

Harden the first-value journey so non-coder users see a clear, actionable
diagnostic when a governed live execution fails instead of receiving demo/mock
output with no cause.

## Scope / Target / Owner Boundary

Target:

- `ProcessingScreen.tsx`
- `ProcessingScreen.test.tsx`

Owner: Codex implementer.

Out of scope: route/provider behavior beyond V3, new templates, new analytics
taxonomy beyond existing event use, auth/RBAC changes, public production
readiness claims, or hosted readiness claims.

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_V1_NONCODER_FIRST_VALUE_JOURNEY_HARDENING_2026-05-24.md`
- V3 standard:
  `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
- Roadmap:
  `docs/roadmaps/CVF_VALUE_SCREENED_NEXT_TRANCHE_ROADMAP_2026-05-24.md`

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Product Reviewer | Confirm first-value failure recovery is user-visible. |
| Implementer | Add minimal UI state and no mock fallback for diagnostics. |
| QA | Test diagnostic rendering and no fallback behavior. |
| Governance Reviewer | Confirm no new governance semantics or receipt fields. |
| Release Manager | File closure and update session routing. |

## Required First Reads

- `DESIGN.md`
- `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx`

## Pre-Flight Checks

- Confirm V3 diagnostic contract exists.
- Confirm UI change does not add a new provider/runtime behavior.
- Confirm classified live failures should not fall back to mock output.

## Write Ownership

Allowed:

- ProcessingScreen diagnostic state/rendering.
- ProcessingScreen focused tests.

Forbidden:

- provider adapter behavior changes
- receipt-envelope schema changes
- new templates/routes/auth behavior

## Work Plan

1. Read `DESIGN.md`.
2. Add diagnostic state to ProcessingScreen.
3. Render a compact diagnostic panel with stage/class/userAction.
4. Stop mock fallback when diagnostic exists.
5. Add focused tests.

## Execution Plan

1. Add diagnostic state.
2. Render diagnostic panel.
3. Return success from `executeReal()` for handled diagnostic failures so mock
   fallback does not run.
4. Add test for diagnostic panel and no `onComplete` mock output.

## Evidence Requirements

- Targeted ProcessingScreen test.
- Typecheck.
- Release gate after all V1/V2/V3 changes.

## Acceptance Criteria

- [ ] Diagnostic panel appears for `success=false` + diagnostic.
- [ ] Mock fallback is suppressed for classified live failures.
- [ ] Existing completion flow still works.
- [ ] Targeted tests pass.

## Verification / Evidence

- ProcessingScreen targeted test output.
- cvf-web typecheck.
- Release gate after all V1/V2/V3 changes.

## Review Gate

Closure must confirm the user sees a cause/action and that the result is not
misrepresented as a successful mock output.

## Operator Checkpoint

Operator authorized V1/V2/V3 processing in the 2026-05-24 session.

## Closure Checklist

- [ ] Diagnostic panel implemented.
- [ ] Mock fallback suppressed for classified failure.
- [ ] Tests passed.
- [ ] Closure review filed.
- [ ] Session routing updated.

## Return-To-Orchestrator Conditions

Return blocked if the fix requires new governance semantics, new provider
behavior, or a receipt schema change.

## Claim / Final / Verification Boundary

V1 may claim clearer first-value recovery for implemented diagnostic paths
only. It must not claim production readiness or universal live stability.
