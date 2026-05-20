Memory class: ROADMAP

# CVF OpenSpec Change Adapter Runtime Adoption Roadmap - 2026-05-16

Status: completed.

## Purpose

Move OpenSpec Change Adapter from `docs-classified` to `runtime-owned`.

## Scope

Implement one deterministic Control Plane contract for OpenSpec change-packet
mapping and governance boundary validation.

## Source

Source bundle:

- `.private_reference/legacy/CVF 16.5/OpenSpec`

## Baseline

OpenSpec was reviewed as useful but not living inside CVF.

## Authorization / Decision

Authorized by operator autonomy instruction for the CVF 16.5 absorption roadmap.

Decision: implement as Control Plane adapter, not OpenSpec executor.

## Non-Goals

This roadmap does not deliver:

- OpenSpec CLI execution;
- direct apply;
- automatic sync/archive;
- canonical truth overwrite;
- provider/runtime changes.

## Work Plan

| Step | Action | Status |
|---|---|---|
| 1 | Create GC-018 authorization and ADR | complete |
| 2 | Create source matrix and proof plan | complete |
| 3 | Implement adapter contract | complete |
| 4 | Add focused tests | complete |
| 5 | Update summary and handoff | complete |
| 6 | Run verification | complete |

## Acceptance Criteria

The tranche is accepted when:

- adapter source exists in Control Plane;
- tests cover mapping, governance fields, direct apply, archive/sync, renamed
  behavior, removal rollback, and determinism;
- Control Plane checks pass;
- full pre-push chain passes before push.

## Evidence

Owner files:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/openspec.change.adapter.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/openspec.change.adapter.contract.test.ts`

## Verification

Verification recorded in the closure packet:

- Control Plane `npm run check` PASS;
- focused OpenSpec adapter Vitest PASS, 1 file / 14 tests;
- full Control Plane Vitest PASS, 125 files / 3418 tests;
- governed file-size guard PASS;
- markdown structural completeness PASS;
- docs governance compatibility PASS.

## Claim Boundary

This roadmap closes adapter semantics only. OpenSpec remains subordinate to CVF.
