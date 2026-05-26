# CVF 17.05 Phase 2.B Legacy Absorption Audit - 2026-05-18

Memory class: FULL_RECORD

Status: PHASE 2.B PREFLIGHT AUDIT. This audit scopes legacy gaps before the
bounded Phase 2.B fixture-driven wire-up.

## Purpose

Determine whether preserved legacy/external review material blocks the bounded
Phase 2.B runtime wire-up slice, and record which concepts must stay deferred
to a later legacy absorption roadmap.

## Scope / Target / Owner Boundary

Target: Phase 2.B preflight for the 17.05 converged roadmap.

Owner: CVF session-continuity and legacy absorption review surface.

In scope:

- legacy concepts that affect the selected Phase 2.B fixture-driven path;
- ORCHESTRATOR and agent role catalog impact on the selected path;
- state/workflow, guard enforcement, context/memory, and traceability concerns
  raised by `Review CVF_1.md` and `De_xuat.md`;
- go/no-go disposition for Phase 2.B GC-018.

Out of scope:

- implementing ORCHESTRATOR-as-CEO semantics;
- implementing agent role `allowed_outputs` or granular permissions;
- web execute route integration;
- noncoder vertical slice;
- live provider proof or public claims.

## Target / Source Under Review

Sources read:

- `.private_reference/legacy/CVF Edit/Review CVF_1.md`
- `.private_reference/legacy/CVF Edit/De_xuat.md`
- `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_ROLE_CATALOG.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_AGENT_ORCHESTRATOR_ROLE_ABSORPTION_GAP_CODEX_AUDIT_2026-05-17.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md`
- `docs/reviews/CVF_17_05_PHASE_2B_PREFLIGHT_OWNER_MIGRATION_PLAN_2026-05-18.md`

## Scope / Methodology

Method:

1. Identify each legacy concept that could widen Phase 2.B.
2. Compare it to the selected bounded fixture-driven path.
3. Mark each concept as `blocks_phase_2b`, `out_of_scope_deferred`, or
   `covered_by_fixture`.
4. Record deferred concepts in the active legacy absorption gap ledger.

## Findings / Position

Phase 2.B may proceed only as a bounded fixture-driven contract wire-up.

The legacy audit confirms important gaps, but they do not block the selected
fixture path because that path does not claim full agent scheduling, full role
permission governance, ORCHESTRATOR-as-CEO enforcement, web execution, provider
execution, or noncoder workflow maturity.

## Legacy Concept Disposition

| Legacy concept | Source | Phase 2.B impact | Disposition |
|---|---|---|---|
| Workflow state machine/failure states | `De_xuat.md`, `Review CVF_1.md` | Selected fixture validates one workflow chain only | `out_of_scope_deferred` |
| Runtime guard enforcement by permission/action/phase | `De_xuat.md` | Fixture uses canonical policy/risk/guard contracts but does not implement a global permission model | `covered_by_fixture_limited` |
| Self-review checklist validation | `De_xuat.md` | Not required for fixture chain | `out_of_scope_deferred` |
| Context management / context stability | `De_xuat.md` | Fixture does not create context runtime | `out_of_scope_deferred` |
| Specification validation | `De_xuat.md` | Not part of Phase 2.B contract wire-up | `out_of_scope_deferred` |
| Failure handling / retry / rollback | `De_xuat.md` | Fixture has deterministic deny/allow result only | `out_of_scope_deferred` |
| Agent scheduler | `Review CVF_1.md` | Not used by fixture path | `out_of_scope_deferred` |
| Project/decision/knowledge memory | `Review CVF_1.md` | Fixture uses memory tier annotation only | `out_of_scope_deferred` |
| Skill runtime binding `skill.execute()` | `Review CVF_1.md` | Fixture uses `GovernedCapability` without executing a skill | `out_of_scope_deferred` |
| Observability layer / telemetry | `Review CVF_1.md` | Fixture emits canonical receipt only, not telemetry | `out_of_scope_deferred` |
| Agent role `allowed_outputs` | `CVF_AGENT_ROLE_CATALOG.md` | Not required if fixture uses existing `AgentFunctionRole` only | `out_of_scope_deferred` |
| Agent role `default_permissions` | `CVF_AGENT_ROLE_CATALOG.md` | Not required for selected fixture; must not be silently absorbed | `out_of_scope_deferred` |
| Role Deny Rule | `CVF_AGENT_ROLE_CATALOG.md` | Not implemented in selected fixture | `out_of_scope_deferred` |
| ORCHESTRATOR mandatory delegation / overreach guard | ORCHESTRATOR gap audit | Not needed if selected fixture uses non-orchestrator role | `out_of_scope_deferred` |

## Risk / Corrective Action

Risk:

- Treating Phase 2.B as general runtime wire-up would silently absorb multiple
  legacy concepts that deserve their own roadmap.

Corrective action:

- Use a fixture-driven path with no web route, provider call, scheduler, memory
  store, ORCHESTRATOR semantics, or role permission expansion.
- Require tests to assert no new role axis values are introduced.
- Record deferred concepts in the legacy absorption gap ledger.

## Decision / Recommendation / Disposition

Decision: Phase 2.B may proceed under a fresh GC-018 only as the bounded
fixture-driven contract wire-up described in
`docs/reviews/CVF_17_05_PHASE_2B_PREFLIGHT_OWNER_MIGRATION_PLAN_2026-05-18.md`.

Recommendation: keep all broader legacy concepts deferred until a dedicated
legacy absorption audit/roadmap after Phase 2.B.

Disposition: `phase_2b_bounded_go`.

## Claim Boundary

This audit does not complete legacy absorption, does not authorize broad
runtime work, does not implement any legacy role or orchestration semantics,
does not change public claims, does not claim live governance proof, and does
not lift `system_reconvergence_stop`.

