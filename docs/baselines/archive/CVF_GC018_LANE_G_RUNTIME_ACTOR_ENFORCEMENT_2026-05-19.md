# CVF GC-018 Lane G Runtime Actor Enforcement

Memory class: SUMMARY_RECORD
Status: AUTHORIZED

## Purpose

Authorize Lane G to enforce governed pack `allowedActorRoles` on the cvf-web
`/api/execute` route before dispatching work to an AI provider.

## Scope

In scope:

- add pure `validateActorRoleGate()` to
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts`;
- add `allowedActorRoles` to the three governed pack `execution.policy.json`
  files for `app_builder_complete`, `documentation`, and `strategy_analysis`;
- wire the actor-role gate into
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
  after `resolveExecutionCVFRole()` and before provider dispatch;
- return `{ error: 'actor_role_not_permitted' }` with HTTP 403 when the
  resolved role is not allowed by the governing pack policy;
- include `actor_role_gate_result` in route audit payloads;
- add focused unit and route tests.

Out of scope:

- new `CVFRole` values;
- auth, RBAC, or permission-profile redesign;
- planner/worker/auditor queue implementation;
- enforcement outside the existing `/api/execute` route;
- skill corpus dead-reference repair.

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_D_E_F_G_2026-05-19.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LANE_G_RUNTIME_ACTOR_ENFORCEMENT_2026-05-19.md`
- `AGENT_HANDOFF_V10_2026-05-19.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/*/execution.policy.json`

## Source-Fidelity Pass

Pre-flight checks confirmed:

- no existing `validateActorRoleGate` implementation;
- no existing `allowedActorRoles` policy field in the three governed pack
  policy files;
- `resolveExecutionCVFRole(session, isServiceAllowed)` already resolves to
  existing `CVFRole` values including `OPERATOR`, `BUILDER`, `REVIEWER`,
  `OBSERVER`, and `SERVICE_AGENT`;
- `route.ts` is exactly 1001 lines before Lane G, matching the resolved
  tombstone cap, so the route wiring must keep net line count at or below 1001;
- `execute-role-resolver.ts` is 86 lines before Lane G and is the correct place
  to hold pure actor role gate helpers.

## Decision / Baseline / Proposed Tranche

Decision: implement Lane G as an R1 execute-path gate.

Exact function:

```text
validateActorRoleGate()
```

Exact file:

```text
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts
```

Exact policy field:

```text
allowedActorRoles
```

Exact policy value for each governed pack:

```json
["OPERATOR", "BUILDER", "REVIEWER", "SERVICE_AGENT"]
```

Exact route insertion point:

```text
Immediately after `resolveExecutionCVFRole()` is evaluated and before provider
dispatch. Because route.ts is already at 1001 lines, helper logic must live in
execute-role-resolver.ts and route changes must be line-count neutral.
```

Exact 403 response:

```json
{ "error": "actor_role_not_permitted" }
```

Exact audit field:

```text
actor_role_gate_result
```

Risk ceiling: R1 because this changes the existing execute path to reject a
resolved actor role when a governed pack policy excludes that role. It does not
change role taxonomy, provider behavior, auth, or RBAC.

## Rule

Lane G may claim:

> The execute route enforces `allowedActorRoles` for the three governed pack
> policies and rejects non-permitted roles with HTTP 403 before provider
> dispatch.

Lane G must not claim:

> Full background job actor isolation, new planner/worker/auditor roles, auth
> redesign, or enforcement outside the `/api/execute` route.

## Evidence / Verification

Required commands:

```powershell
npm run test:run -- src/lib/execute-role-resolver.test.ts src/app/api/execute/route.test.ts
npm run build
npm run lint
```

Run in:

```text
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
```

Repository guard:

```powershell
python governance/compat/run_local_governance_hook_chain.py --hook pre-commit
```

## Tranche Closure Checklist

- `validateActorRoleGate()` exists and is pure.
- `allowedActorRoles` exists in all three governed pack policy files.
- Route rejects non-permitted actor roles with 403 and exact error shape.
- Provider dispatch is not called on actor-role rejection.
- Permitted actor role path still reaches the existing execute flow.
- `actor_role_gate_result` is emitted in audit payloads.
- `route.ts` remains at or below 1001 lines.
- No `CVFRole`, auth, RBAC, or permission-profile change is made.
- Focused tests pass.
- Current governance hook chain passes without bypassing hooks or any residual
  blocker is recorded honestly.

## Claim Boundary

This authorization covers only the `allowedActorRoles` gate on `/api/execute`
for the three governed pack policies. It does not resolve the separate skill
corpus/template dead-reference failures surfaced by full web tests.
