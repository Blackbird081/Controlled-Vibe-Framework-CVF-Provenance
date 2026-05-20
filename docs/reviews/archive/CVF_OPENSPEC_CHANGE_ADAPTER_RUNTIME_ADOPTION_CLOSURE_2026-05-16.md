Memory class: REVIEW_RECORD

# CVF OpenSpec Change Adapter Runtime Adoption Closure - 2026-05-16

Status: closed as `runtime-owned`.

## Purpose

Close OpenSpec Change Adapter absorption and record what is now living in CVF.

## Scope

This closure covers one deterministic Control Plane contract and tests.

## Source

Adopted from:

- `.private_reference/legacy/CVF 16.5/OpenSpec`

## Delivered Behavior

CVF now has a contract that:

- maps OpenSpec artifacts into CVF phases;
- treats `apply` as governed execution request only;
- treats `verify` as REVIEW evidence input;
- treats `archive` and `sync` as candidates only;
- blocks direct apply bypass;
- blocks canonical overwrite;
- validates CVF governance extension fields on deltas;
- blocks hidden behavior changes in rename deltas;
- requires rollback/deprecation note for removal deltas.

## Findings / Position

Position: OpenSpec Change Adapter is now a living CVF primitive.

Finding: OpenSpec improves change structure but remains subordinate to CVF
governance authority.

## Risk / Corrective Action

Risk: direct execution or sync may be attempted in a future tranche.

Corrective action: fresh GC-018 is required before any OpenSpec execution bridge
or canonical mutation path.

## Evidence

Runtime:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/openspec.change.adapter.contract.ts`

Tests:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/openspec.change.adapter.contract.test.ts`

## Verification

Verification completed before commit:

- Control Plane `npm run check` PASS;
- focused `openspec.change.adapter.contract.test.ts` PASS, 1 file / 14 tests;
- full Control Plane Vitest PASS, 125 files / 3418 tests;
- governed file-size guard PASS;
- markdown structural completeness PASS;
- docs governance compatibility PASS.

Full pre-push chain remains required before push.

## Claim Boundary

OpenSpec Change Adapter is `runtime-owned` for deterministic local adapter
semantics only. It does not apply, sync, archive, or overwrite CVF truth.

## Decision

Close OpenSpec Change Adapter as `runtime-owned` after verification passes.
