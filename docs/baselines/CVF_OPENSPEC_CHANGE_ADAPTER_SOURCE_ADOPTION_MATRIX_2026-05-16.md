Memory class: GOVERNANCE_BASELINE

# CVF OpenSpec Change Adapter Source Adoption Matrix - 2026-05-16

Status: active matrix for OpenSpec absorption.

## Purpose

Map OpenSpec source ideas to CVF-owned runtime behavior.

## Scope

This matrix covers the first Control Plane adapter tranche.

## Source

| Source item | CVF adoption |
|---|---|
| `proposal.md` | INTAKE + DESIGN input only |
| `design.md` | DESIGN + BUILD boundary input |
| `tasks.md` | BUILD task packet input |
| `apply` | governed execution request, never direct authority |
| `verify` | REVIEW evidence input |
| `archive` | FREEZE archive candidate only |
| `sync` | truth-sync candidate only |
| `ADDED` | new governed capability delta |
| `MODIFIED` | changed behavior delta |
| `REMOVED` | disabled/deprecated behavior with rollback note |
| `RENAMED` | migration only; hidden behavior changes blocked |
| CVF extensions | risk, policy, approval, DLP, rollback, evidence fields required |

## Baseline

Prior state was reviewed and classified but not executable.

## Classification

Fit: Medium/High.

Target state: `runtime-owned`.

## Evidence

Runtime owner:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/openspec.change.adapter.contract.ts`

Test owner:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/openspec.change.adapter.contract.test.ts`

## Verification

Tests must prove phase mapping, delta field validation, direct apply block,
archive/sync overwrite block, and deterministic packet identity.

## Claim Boundary

OpenSpec is an input discipline. CVF remains authority over policy, execution,
truth sync, archive, and audit.
