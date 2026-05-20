Memory class: GOVERNANCE_BASELINE

# CVF OpenSpec Change Adapter Test And Proof Plan - 2026-05-16

Status: active proof plan.

## Purpose

Define proof for closing OpenSpec Change Adapter as living CVF behavior.

## Scope

Required checks:

- focused Vitest;
- Control Plane typecheck;
- full Control Plane Vitest;
- governed file-size guard;
- markdown structural guard;
- docs governance guard;
- full pre-push chain before push.

## Source

Proof maps to OpenSpec intake files and CVF runtime adoption norms.

## Test Matrix

| Area | Required proof |
|---|---|
| Phase mapping | proposal/design/tasks/apply/verify/archive/sync map to CVF phases |
| Authority boundary | direct apply is blocked |
| Archive/sync | canonical overwrite is blocked |
| Delta grammar | ADDED/MODIFIED/REMOVED/RENAMED are validated |
| Governance fields | risk/policy/approval/DLP/rollback/evidence are required |
| Determinism | same packet and timestamp produce same packet id |

## Baseline

No live provider proof is required; this is deterministic local Control Plane
behavior.

## Evidence

Evidence will be recorded in the closure packet.

## Verification

Commands:

```bash
cd EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION
npm run check
npx vitest run tests/openspec.change.adapter.contract.test.ts --config vitest.config.ts
```

## Claim Boundary

Passing tests supports `runtime-owned` adapter behavior only.
