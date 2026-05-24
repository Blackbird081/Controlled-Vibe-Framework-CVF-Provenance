# CVF GC-018 - C3 Execute Route Step Sequence Guard - 2026-05-19

Memory class: BASELINE_RECORD

Status: APPROVED - implementation authorized for C3 only.

## Purpose

Authorize a static guard that validates the selected-occurrence order of the
eight canonical `/api/execute` route call sites recorded in C3.

## Scope / Target / Owner Boundary

In scope: `governance/compat/check_execute_route_step_sequence.py`, its JSON
registry, unit tests, policy documentation, local hook-chain wiring, and static
CI wiring.

Out of scope: editing
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`,
adding route steps, validating route semantics, live provider execution, or
covering other route files.

## Source / Predecessor Evidence

- Roadmap:
  `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md`
- Work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_C3_EXECUTE_ROUTE_STEP_SEQUENCE_GUARD_2026-05-19.md`
- C2 completion:
  `docs/reviews/CVF_C2_GOVERNED_PACK_CONTRACT_GUARD_COMPLETION_2026-05-19.md`
- C4 completion:
  `docs/reviews/CVF_C4_CONTINUATION_CHAIN_GUARD_COMPLETION_2026-05-19.md`

## Decision / Baseline / Proposed Tranche

Decision: approve C3 as a static enforcement tranche after C2 and C4 closure.

Baseline: the current `route.ts` has the selected occurrences in this order:

1. `resolveExecutionCVFRole(` at line 336
2. `evaluateExecutionActorRoleGate(` at line 348
3. `checkRoleOutputPermission(` at line 350
4. `evaluateEnforcement(` at line 375
5. `routeWebProvider(` at line 564
6. `buildEvidenceReceipt(` selected by `last` at line 858
7. `buildRouteAuditMemoryCapture(` at line 927
8. `appendAuditEvent(` selected by `last` at line 944

Proposed tranche: create a registry-backed guard that reports missing selected
occurrences or non-increasing selected line order.

## Evidence / Verification

Required verification before closure:

- Current `route.ts` returns zero violations.
- Unit tests cover current pass, missing step, swapped order, first selector
  skipping import/comment lines, and last selector selecting final success-path
  calls.
- Guard runtime against current `route.ts` is under 2 seconds.
- Registry JSON parses successfully.
- Local hook-chain and static CI wiring invoke the guard.

## Maintenance Note

Any future refactor that changes the call order, renames a function, or adds a
mandatory step to `route.ts` MUST update
`CVF_EXECUTE_ROUTE_STEP_SEQUENCE_REGISTRY.json` in the same commit. Failure to
do so will cause the guard to fail on the next CI run.

## Claim Boundary

This GC-018 authorizes static step-order enforcement only. It does not prove
runtime governance behavior and does not replace live release-quality proof for
claims about provider routing, approval flow, audit behavior, or output
validation.
