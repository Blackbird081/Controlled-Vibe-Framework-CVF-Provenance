# CVF Work Order: WC-2 Mock Fallback Elimination

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: work_order

Date: 2026-05-24

Tranche: WC-2

Roadmap: `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`

---

## Purpose

Remove the remaining path where a failed real execution can be replaced by
demo/mock output.

## Scope / Target / Owner Boundary

Allowed:

- ProcessingScreen live-failure handling.
- ProcessingScreen focused tests.

Forbidden:

- Provider adapter changes.
- `/api/execute` route behavior changes.
- Receipt-envelope schema changes.
- New templates or new governance semantics.

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_WC2_MOCK_FALLBACK_ELIMINATION_2026-05-24.md`
- Roadmap:
  `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Product Reviewer | Confirm truthful failure recovery is better than fake output. |
| Implementer | Remove the remaining fallback trigger after a real attempt. |
| QA | Add regression coverage for unclassified live failure. |
| Governance Reviewer | Confirm no new runtime or receipt semantics. |
| Release Manager | Run focused tests, typecheck, release gate, and closure docs. |

## Required First Reads

- `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- `docs/baselines/CVF_GC018_WC2_MOCK_FALLBACK_ELIMINATION_2026-05-24.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.test.tsx`

## Pre-Flight Checks

- Confirm V1 diagnostic no-mock behavior exists.
- Confirm the remaining fallback is localized to ProcessingScreen.
- Confirm no route/provider/receipt behavior is required.

## Write Ownership

Allowed files:

- `ProcessingScreen.tsx`
- `ProcessingScreen.test.tsx`
- WC-2 governance docs

Forbidden files:

- Provider adapters
- `/api/execute` route
- receipt-envelope type definitions
- new template or route files

## Execution Plan

1. Update `ProcessingScreen.tsx` so failed real attempts render a failure state.
2. Preserve no-input demo behavior.
3. Add focused test coverage for unclassified live failure.
4. Run verification and file completion review.

## Evidence Requirements

- Focused ProcessingScreen test run.
- `cvf-web` typecheck.
- Mandatory release gate bundle.
- Completion review with evidence trace.

## Review Gate

The reviewer must confirm:

- no mock output after a failed real attempt;
- V1 diagnostic behavior remains intact;
- no new runtime authority is introduced.

## Closure Checklist

- [ ] Code change complete.
- [ ] Focused test PASS.
- [ ] Typecheck PASS.
- [ ] Release gate PASS.
- [ ] Completion review filed.

## Return-To-Orchestrator Conditions

Return blocked if:

- the fix requires route/provider behavior changes;
- successful real execution regresses;
- release gate fails for a WC-2-caused reason.

## Operator Checkpoint

No additional operator checkpoint is required for WC-2 because the roadmap
marks it Fast Lane and work-order-ready. WC-1 and WC-3 still require fresh
authorization before implementation.

## Acceptance Criteria

- [ ] No mock output after classified diagnostic failure.
- [ ] No mock output after unclassified live failure.
- [ ] No mock output after network/parse-level live failure.
- [ ] Successful real execution remains unchanged.

## Claim Boundary

This work order authorizes only the WC-2 truthful failure correction. It does
not authorize WC-1 workflow-chain proof, WC-3 legacy harvest scan, provider
behavior changes, new governance semantics, or production-readiness claims.
