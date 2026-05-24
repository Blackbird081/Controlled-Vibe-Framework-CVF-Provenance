# CVF Lane G Runtime Actor Enforcement Completion

Memory class: SUMMARY_RECORD
Status: CLOSED_WITH_INHERITED_SKILL_MAPPING_BLOCKERS

## Purpose

Record completion of Lane G, which adds `allowedActorRoles` enforcement to the
cvf-web `/api/execute` path for the three governed pack policies.

## Scope

Implemented:

- `validateActorRoleGate()` and policy lookup helpers in
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts`
- `allowedActorRoles` in:
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/app_builder_complete/execution.policy.json`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/documentation/execution.policy.json`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/strategy_analysis/execution.policy.json`
- `/api/execute` actor-role gate wiring after `resolveExecutionCVFRole()`
- 403 response shape `{ error: 'actor_role_not_permitted' }`
- audit payload field `actor_role_gate_result`
- unit and route tests for permitted and rejected paths
- dedicated actor-gate route test file:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.actor-gate.test.ts`
- adjacent correction to
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-runtime-adapter.test.ts`
  so the old 8-role expectation includes `SERVICE_AGENT`

Not implemented:

- no `CVFRole` enum/type change;
- no auth, RBAC, or permission profile change;
- no planner/worker/auditor queue implementation;
- no skill corpus or skill-template-map repair.

## Source / Predecessor Evidence

- `docs/work_orders/CVF_AGENT_WORK_ORDER_LANE_G_RUNTIME_ACTOR_ENFORCEMENT_2026-05-19.md`
- `docs/baselines/CVF_GC018_LANE_G_RUNTIME_ACTOR_ENFORCEMENT_2026-05-19.md`
- `AGENT_HANDOFF_V10_2026-05-19.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`

## Source-Fidelity Pass

The route was exactly 1001 lines before implementation, so inline expansion
would have violated the work-order cap. The implementation keeps policy reading
and gate evaluation in `execute-role-resolver.ts`, and keeps `route.ts` at 1001
lines after wiring.

The governed pack policy JSON imports are type-narrowed with a runtime
`KNOWN_CVF_ROLES` filter before returning roles as `CVFRole[]`. The filter is
kept aligned to `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` and deliberately
does not accept RBAC-only labels such as `ADMIN`. This avoids pretending raw
JSON `string[]` is already a trusted role type.

## Findings / Position

Position: NO_BLOCKING_FINDING for Lane G's bounded runtime actor gate.

Findings:

- `OBSERVER` is now rejected for governed pack policies that exclude it.
- `OPERATOR`, `BUILDER`, `REVIEWER`, and `SERVICE_AGENT` are allowed by the
  three governed pack policies.
- The existing route role-output permission gate remains in place after the
  actor-role gate.
- Full web suite still has skill corpus/template mapping failures that are
  outside Lane G.

## Risk / Corrective Action

Risk classification: R1, because the execute path now rejects requests that
previously could continue when the resolved actor role is not in
`allowedActorRoles`.

Corrective action:

- Keep `allowedActorRoles` as pack policy data, not a new role taxonomy.
- Treat skill corpus/template dead references as a separate guard-backed work
  order.
- Do not claim multi-tenant actor isolation or queue-level worker/planner
  enforcement from this lane.

## Decision / Baseline / Proposed Tranche

Lane G is closed for the bounded claim:

> `/api/execute` enforces `allowedActorRoles` for the three governed pack
> policies and rejects non-permitted actor roles with HTTP 403 before provider
> dispatch.

## Rule

Future agents should use this as the minimum runtime actor-role enforcement
point for governed pack execution. Any expansion into new role types, job
queues, or auth/RBAC semantics requires a new GC-018 and work order.

## Evidence / Verification

Evidence Trace Block:

- Claim: `route.ts` stayed within the resolved 1001-line cap.
- Command: `(Get-Content '.../src/app/api/execute/route.ts').Count`
- Result: `1001`
- Key path:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- Verdict: PASS

Evidence Trace Block:

- Claim: focused actor-role gate unit and route tests pass.
- Command:
  `npm run test:run -- src/lib/execute-role-resolver.test.ts src/app/api/execute/route.test.ts`
- Result: 2 files passed, 41 tests passed.
- Key path: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`
- Verdict: PASS

Evidence Trace Block:

- Claim: adjacent `SERVICE_AGENT` role-count expectation is corrected.
- Command:
  `npm run test:run -- src/lib/guard-runtime-adapter.test.ts src/lib/execute-role-resolver.test.ts src/app/api/execute/route.test.ts src/app/api/execute/route.actor-gate.test.ts`
- Result: 4 files passed, 116 tests passed.
- Key path: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`
- Verdict: PASS

Evidence Trace Block:

- Claim: production build accepts the Lane G changes.
- Command: `npm run build`
- Result: PASS.
- Key path: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`
- Verdict: PASS

Evidence Trace Block:

- Claim: lint accepts the Lane G changes.
- Command: `npm run lint`
- Result: PASS.
- Key path: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`
- Verdict: PASS

Evidence Trace Block:

- Claim: live retrieval route behavior was not broken by actor-role gate.
- Command: `npm run test:run -- src/app/api/execute/route.retrieval.live.test.ts`
- Result: 1 file passed, 4 tests passed.
- Key path: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`
- Verdict: PASS

Evidence Trace Block:

- Claim: full web test suite status after Lane G.
- Command: `npm run test:run`
- Result: FAIL. The previous `SERVICE_AGENT` role-count failure is fixed. The
  suite still reports skill corpus/template mapping failures. One live
  retrieval test failed during the full parallel run with HTTP 400 but passed
  when isolated immediately afterward, so it is recorded as live-suite
  variance rather than a deterministic Lane G regression.
- Key path: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`
- Verdict: INHERITED_BLOCKER_RECORDED

## Tranche Closure Checklist

- [x] GC-018 filed before implementation.
- [x] `validateActorRoleGate()` added and tested.
- [x] `allowedActorRoles` added to all three governed pack policies.
- [x] `OBSERVER` rejected for governed pack policy execution.
- [x] 403 response shape matches `{ error: 'actor_role_not_permitted' }`.
- [x] Provider dispatch is not called on actor-role rejection.
- [x] `actor_role_gate_result` emitted in audit payloads.
- [x] `route.ts` remains at or below 1001 lines.
- [x] No `CVFRole`, auth, RBAC, or permission profile change.
- [x] Build passed.
- [x] Lint passed.
- [x] Focused tests passed.
- [ ] Full web suite clean: blocked by skill corpus/template mapping failures
  outside this lane.
- [x] Final repository hook chain: PASS after proposal structure correction and
  generated skill-index restore.

## Claim Boundary

Lane G proves only route-level `allowedActorRoles` enforcement for the three
governed pack policies. It does not prove queue actor isolation, new worker
roles, planner/reviewer/auditor workflow enforcement, or skill corpus
correctness.
