# CVF GC-018 Phase E E.2 Role Permission Gate - 2026-05-18

Memory class: FULL_RECORD
Status: GC018_FILED

## Candidate ID

`CVF_GC018_PHASE_E_E2_ROLE_PERMISSION_GATE_2026-05-18`

## Date

2026-05-18

## Parent Roadmap

- `docs/reviews/CVF_PHASE_E_GOVERNED_EXECUTION_CHAIN_ROADMAP_2026-05-18.md`
- Tranche: E.2 - Role Permission Gate
- Prerequisite audit:
  `docs/reviews/CVF_PHASE_E_EXECUTION_CHAIN_AUDIT_2026-05-18.md`

## Purpose

Authorize the bounded E.2 runtime wire-up that consumes the existing Phase D
role-permission contract in the live web execute path.

## Scope / Target / Owner Boundary

Target:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-route-guards.ts`
- new resolver/test files under
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/`

Owner boundary:

- CVF web execute path owns request-boundary role normalization.
- `CVF_GUARD_CONTRACT` remains the source of truth for `CVFRole`,
  `RolePermissionOutputClass`, `getRolePermissionProfile()`, and
  `isOutputAllowedForRole()`.
- No public-sync catalog edit is authorized by this tranche.

## Proposed Scope

Wire `role-permission.contract.ts` into the live `cvf-web`
`POST /api/execute` route for the selected `Create Product Brief` execution
path.

Implementation scope:

- add `resolveExecutionCVFRole()` at the web execution boundary;
- add `resolveExecutionOutputClass()` for deterministic output-class mapping;
- add `checkRoleOutputPermission()` helper around
  `isOutputAllowedForRole()`;
- deny unknown/unsupported roles before provider dispatch;
- map `app_builder_complete` to output class `artifact`;
- expose role permission result in the route response/audit evidence where
  appropriate;
- add deterministic tests for resolver mappings, denial behavior, and golden
  path allowance.

## Continuation Class

`bounded_runtime_wire_up`

This is not a new governance concept. It consumes an existing Phase D contract
inside one selected live route.

## Quality-First Decision

Proceed.

The E.1 audit verified the route already has governance surfaces but does not
consume Phase D role-permission contracts. E.2 is the smallest runtime slice
that closes the role/output-class wiring gap before any workflow binding is
dispatched.

## Source / Predecessor Evidence

| Source | Evidence | Result |
| --- | --- | --- |
| E.1 audit | Role resolution and output class gate rows are `wiring_gap` | ACCEPTED |
| Phase D role-permission contract | Contract exists and exposes profiles plus `isOutputAllowedForRole()` | ACCEPTED |
| Operator prompt | Requires GC-018 before E.2 implementation and forbids live proof for E.2 | ACCEPTED |

## Decision / Baseline / Proposed Tranche

Decision: APPROVE_E2_ROLE_PERMISSION_GATE_IMPLEMENTATION.

Baseline:

- live route has raw `session?.role` metadata;
- Phase D role-permission contract exists but is not consumed by `cvf-web`;
- `app_builder_complete` is the selected golden-path template.

Proposed tranche:

- implement resolver and permission-gate helpers;
- wire gate before provider dispatch;
- prove behavior with deterministic unit/route tests.

## Quality Protection Commitments

- Preserve the existing authenticated/session and service-token behavior.
- Do not silently widen unknown RBAC roles.
- Do not introduce additional output-class mappings beyond the selected flow
  unless demanded by an existing tested route path.
- Keep unbound/non-Product-Brief requests backward compatible.
- Run deterministic tests; no live provider proof is required for E.2.
- Respect GC-023 file-size preflight before editing existing files.

## Why Now

Phase E is operator-authorized on 2026-05-18 after Claude V2 applied the Codex
rebuttal. E.2 is the first implementation tranche after E.1 and is required
before E.4 can wire workflow binding into dispatch.

## Active-Path Impact

The live `/api/execute` path changes:

- authenticated/service requests now resolve to a normalized `CVFRole`;
- selected output class is checked before provider dispatch;
- unauthorized role/output-class combinations return a structured policy
  denial instead of reaching the provider.

The selected golden path remains:

- `app_builder_complete` / `Create Product Brief`;
- normalized builder/operator-equivalent roles allowed to produce `artifact`;
- provider dispatch still uses existing routing after permission passes.

## Risk If Deferred

If deferred, Phase E cannot honestly claim the role-permission checkpoint fires
in a real request. E.4 workflow binding would then run without the caller role
and output class gate required by Phase D.

## Live Proof Boundary

No live provider proof is required for E.2.

E.2 changes a deterministic pre-dispatch permission check. Existing web tests
and targeted route tests are the required proof. Live Alibaba proof is reserved
for E.4 and E.6 per the operator prompt.

## Required Evidence

- `Test-Path EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-permission.contract.ts`
  returns `True`.
- Resolver unit tests prove:
  - service-token execution maps to `SERVICE_AGENT` equivalent behavior;
  - owner/admin map to `OPERATOR`;
  - developer maps to `BUILDER`;
  - reviewer maps to `REVIEWER`;
  - viewer maps to `OBSERVER`;
  - unknown/undefined roles deny.
- Output-class resolver tests prove `app_builder_complete -> artifact`.
- Route tests prove allowed Product Brief execution reaches provider dispatch.
- Route tests prove a role/output-class denial returns a policy-denied
  response before provider dispatch.
- Existing targeted web tests pass.

## Evidence Trace Block

| Claim | Evidence | Result |
| --- | --- | --- |
| Phase D role-permission contract exists | `Test-Path EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-permission.contract.ts` returned `True` | ACCEPTED |
| E.1 identified role permission as selected-flow wiring gap | E.1 audit row `CVF role resolution` and `Output class gate` are `wiring_gap` | ACCEPTED |
| E.2 does not require live provider proof | Operator prompt explicitly says "Live proof required: NO" for E.2 | ACCEPTED |

## Claim Boundary

This GC-018 authorizes only Tranche E.2. It does not authorize workflow
binding dispatch, receipt binding, public catalog claims, provider method
expansion, or any change to `system_reconvergence_stop`.
