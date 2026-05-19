# CVF Agent Work Order — Lane G: Runtime Actor Enforcement

Memory class: POINTER_RECORD

Status: OPEN — awaiting Codex GC-018 filing before implementation begins.
Prerequisite: Lane F must be closed before Lane G begins.

## Purpose

Dispatch Codex to implement Lane G (Runtime Actor Enforcement) as defined in
`docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_D_E_F_G_2026-05-19.md`.

Lane G adds an `allowedActorRoles` gate to the execute route. Before
dispatching to the AI provider, the route checks that the resolved actor role
is in the `allowedActorRoles` list from the governing workflow pack's
`execution.policy.json`. Requests from roles not in the list are rejected with
a 403.

## Source

- `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_D_E_F_G_2026-05-19.md` — lane G spec
- `docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md` —
  Problem G: worker/planner/reviewer/auditor roles defined but not enforced
- `AGENT_HANDOFF_V9_2026-05-18.md` — active session posture
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` — current mode

## 1. Mission

Add a minimum actor role gate to the execute route: after
`resolveExecutionCVFRole()` resolves the actor's role, check it against
`allowedActorRoles` from the governing pack's `execution.policy.json`. Return
403 if the role is not permitted.

Success means: a request from a VIEWER role is rejected with 403 when VIEWER
is not in `allowedActorRoles`; a request from an allowed role passes through;
unit tests for `validateActorRoleGate()` pass; route integration test for the
403 path passes.

## 2. Authority Chain

- Operator instruction: 2026-05-19 — implement Lane D/E/F/G in sequence
- Roadmap: `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_D_E_F_G_2026-05-19.md`
- Decision pack: `docs/reviews/CVF_MULTI_AGENT_DECISION_PACK_REVIEW_CVF_NEXT_PHASE_2026-05-18.md`
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Active handoff: `AGENT_HANDOFF_V9_2026-05-18.md`
- Prerequisite: Lane F completion packet filed and reviewed

## 3. Agent Roles

- Orchestrator / dispatcher: operator and coordinating agent (Claude)
- Implementer: Codex
- Reviewer: Claude
- Operator approval required for: changing `CVFRole` enum, changing existing
  permission profile logic, adding new role types, any auth system change

## 4. Required First Reads

Before filing GC-018:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
   — exact location of `resolveExecutionCVFRole()` call; understand the
   existing auth/role resolution flow; note current line count (RESOLVED
   tombstone at 1001 lines — any addition must not exceed this cap)
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts`
   — existing `resolveExecutionCVFRole()` and `CVFRole` type; understand the
   return shape before writing `validateActorRoleGate()`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/` —
   current `execution.policy.json` schema in each of the 3 packs; note
   existing fields before adding `allowedActorRoles`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates.ts` —
   understand how templates reference governed packs to confirm the gate
   applies at the correct layer
5. `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` —
   check `route.ts` exception entry (RESOLVED tombstone, 1001 line cap);
   check `execute-role-resolver.ts` line limit before adding functions

Anti-duplication grep:

```powershell
rg -n "allowedActorRoles|validateActorRoleGate|actor_role_gate" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/
rg -n "resolveExecutionCVFRole" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts
```

## 5. Pre-Flight Checks

```powershell
python governance/compat/check_active_session_state.py --enforce
python governance/compat/check_markdown_structural_completeness.py
python governance/compat/check_docs_governance_compat.py
Test-Path "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts"
Test-Path "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts"
(Get-Content "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts").Count
(Get-Content "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts").Count
git status --short
```

CRITICAL: `route.ts` has a RESOLVED tombstone exception at 1001 lines. Any
modification must keep the file at or below 1001 lines. If adding the gate
inline would exceed this cap, extract the gate call to `execute-role-resolver.ts`
and import it — do NOT increase the route.ts line count.

## 6. GC-018 Requirements

Before implementation, file:

```
docs/baselines/CVF_GC018_LANE_G_RUNTIME_ACTOR_ENFORCEMENT_2026-05-19.md
```

The GC-018 must record:

- exact function name: `validateActorRoleGate()`
- exact file: `cvf-web/src/lib/execute-role-resolver.ts`
- exact field name: `allowedActorRoles` (array of `CVFRole` strings)
- exact insertion point in `route.ts` (line or code anchor after
  `resolveExecutionCVFRole()`)
- exact 403 response shape: `{ status: 403, error: 'actor_role_not_permitted' }`
- exact audit event field: `actor_role_gate_result`
- R1 risk statement (existing execute path gating only)
- explicit boundary: no new role types, no CVFRole enum change, no planner/
  worker/auditor job queue
- acceptance criteria
- Tranche Closure Checklist

## 7. Write Ownership

Allowed scope:

```
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts  (MODIFY — add validateActorRoleGate())
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts       (MODIFY — wire gate after resolveExecutionCVFRole())
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/app_builder_complete/execution.policy.json  (MODIFY — add allowedActorRoles)
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/documentation/execution.policy.json         (MODIFY — add allowedActorRoles)
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/strategy_analysis/execution.policy.json     (MODIFY — add allowedActorRoles)
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/execute-role-resolver.test.ts (NEW or MODIFY — gate unit tests)
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/execute-route-actor-gate.test.ts (NEW — route integration test for 403)
docs/baselines/CVF_GC018_LANE_G_RUNTIME_ACTOR_ENFORCEMENT_2026-05-19.md        (NEW)
docs/reviews/CVF_LANE_G_RUNTIME_ACTOR_ENFORCEMENT_COMPLETION_2026-05-19.md     (NEW)
```

Forbidden scope:

```
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/auth.ts        (no auth system changes)
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/permissions.ts (no permission profile changes)
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/cvf-roles.ts (no CVFRole enum changes)
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/   (no new page routes)
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/           (only route.ts in execute/ is touched)
```

Write mode: modify `execute-role-resolver.ts` to add the gate function; wire
gate into `route.ts` at the correct insertion point; update 3 governed pack
`execution.policy.json` files; write tests; create GC-018 and completion packet.

## 8. Execution Plan

Steps are sequential unless marked parallel-safe.

1. Read `route.ts` fully. Note the exact line where `resolveExecutionCVFRole()`
   is called and what follows. Note current line count.
   Read `execute-role-resolver.ts` fully. Note return shape of
   `resolveExecutionCVFRole()`.
   Grep for existing `allowedActorRoles` or `validateActorRoleGate`.
   Stop if: gate already exists — report to reviewer, do not duplicate.

2. Read all 3 governed pack `execution.policy.json` files. Note existing fields.
   Confirm `CVFRole` type values (Owner, Admin, Developer, Reviewer, Viewer
   or equivalent enum values) from `execute-role-resolver.ts` or `types.ts`.
   Stop if: `CVFRole` shape is unclear — report to reviewer before writing.

3. Add `validateActorRoleGate()` to `execute-role-resolver.ts`:
   ```typescript
   export function validateActorRoleGate(
     resolvedRole: CVFRole,
     allowedActorRoles: CVFRole[]
   ): { permitted: boolean } {
     return { permitted: allowedActorRoles.includes(resolvedRole) };
   }
   ```
   Function must be pure (no side effects). Check line count after addition.
   Stop if: would exceed GC-023 limit for this file.

4. Add `allowedActorRoles` to each of the 3 governed pack `execution.policy.json`:
   ```json
   "allowedActorRoles": ["Owner", "Admin", "Developer", "Reviewer"]
   ```
   (VIEWER excluded by default — they may read but not execute.)
   Adjust role names to match the exact `CVFRole` string values in the codebase.

5. Wire gate into `route.ts` immediately after `resolveExecutionCVFRole()`:
   - Import `validateActorRoleGate` from `execute-role-resolver`
   - Read `allowedActorRoles` from the governing pack's `execution.policy.json`
     (already loaded earlier in the route if governed pack is resolved)
   - Call `validateActorRoleGate(resolvedRole, allowedActorRoles)`
   - If `!permitted`: return `NextResponse.json(
       { error: 'actor_role_not_permitted' }, { status: 403 })`
   - Emit `actor_role_gate_result: permitted | rejected` in the audit event
     payload (add field alongside existing audit fields)
   Check line count after modification. Must remain at or below 1001 lines.
   Stop if: addition would push file above 1001 lines.

6. Write tests:
   a. Unit tests for `validateActorRoleGate()` in `execute-role-resolver.test.ts`
      (new file or extend existing if present):
      - permitted role returns `{ permitted: true }`
      - non-permitted role returns `{ permitted: false }`
      - empty `allowedActorRoles` array → always `{ permitted: false }`
   b. Route integration test in `execute-route-actor-gate.test.ts`:
      - mock `resolveExecutionCVFRole()` to return a VIEWER role
      - mock governed pack policy with `allowedActorRoles` excluding VIEWER
      - assert response is 403 with `{ error: 'actor_role_not_permitted' }`
      - assert permitted role receives non-403 response
   Use Vitest + existing test patterns.

7. Run `npm run build` — must succeed, no TypeScript errors.
   Run `npm run lint` — must be clean (max-warnings=0).
   Run `npm test` — all tests pass including new gate tests.

8. File GC-018 baseline. File completion packet. Update GC-020.

## 9. Evidence Requirements

```powershell
Test-Path "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts"
(Get-Content "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts").Count
rg -n "validateActorRoleGate" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts
rg -n "allowedActorRoles" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/app_builder_complete/execution.policy.json
rg -n "actor_role_gate_result" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts
npm run build       # must succeed
npm run lint        # must be clean
npm test            # all pass
python governance/compat/run_local_governance_hook_chain.py --hook pre-commit
```

Evidence Trace Block required for each claim in completion packet:
- Claim:
- Command:
- Result:
- Key path:
- Verdict:

## 10. Acceptance Criteria

- [ ] `validateActorRoleGate()` added to `execute-role-resolver.ts`
- [ ] Gate wired into `route.ts` immediately after `resolveExecutionCVFRole()`
- [ ] 403 returned with `{ error: 'actor_role_not_permitted' }` when role not in list
- [ ] `actor_role_gate_result` emitted in audit event payload
- [ ] `allowedActorRoles` field added to all 3 governed pack `execution.policy.json`
- [ ] `route.ts` line count remains at or below 1001 (RESOLVED tombstone cap)
- [ ] Unit tests pass for `validateActorRoleGate()` (permitted, rejected, empty list)
- [ ] Route integration test passes for 403 path
- [ ] No CVFRole enum changes
- [ ] No new page routes or auth system changes
- [ ] `npm run build` succeeds — no TypeScript errors
- [ ] `npm run lint` passes — no warnings
- [ ] Governance pre-commit hook chain passes

## 11. Review Gate

Reviewer: Claude.

Reviewer checks:
- Gate function is pure and correctly reads from `execution.policy.json`
- 403 response shape matches the exact spec
- `route.ts` line count is at or below 1001 (RESOLVED tombstone)
- No CVFRole enum or auth system changes
- All acceptance criteria evidenced with Test-Path and test runs
- Audit event field `actor_role_gate_result` is present in payload

## 12. Closure Checklist

- [ ] GC-018 filed and referenced
- [ ] All acceptance criteria PASS
- [ ] Evidence Trace Block present
- [ ] Governance hook chain passes (all 7 checks)
- [ ] GC-020 handoff updated
- [ ] Public catalog: consider adding `allowedActorRoles` actor gate to
      capability table with `defined, unit-tested` status — verify path in
      public-sync before committing
- [ ] Reviewer disposition: NO_BLOCKING_FINDING or operator waiver

## 13. Return-To-Orchestrator Conditions

Stop and escalate if:

- `validateActorRoleGate` already exists — report, do not duplicate
- `route.ts` would exceed 1001 lines after modification — stop, report to
  reviewer; do not proceed without operator waiver on the line cap
- CVFRole enum change is required to make the gate work — stop, out of scope
- Build or lint fails and cannot be fixed within lane scope
- Governed pack `execution.policy.json` schema is incompatible with the gate —
  report exact conflict before modifying

## Claim Boundary

Lane G closes with: `allowedActorRoles` gate enforced in execute route —
`defined, unit-tested`

Not claimed: background job queue enforcement, multi-tenant actor isolation,
planner/worker/auditor as separate session types, enforcement beyond the
`allowedActorRoles` check at the execute route.
