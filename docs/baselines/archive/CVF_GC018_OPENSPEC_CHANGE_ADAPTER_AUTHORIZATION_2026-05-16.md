Memory class: GOVERNANCE_BASELINE

# CVF GC-018 OpenSpec Change Adapter Authorization - 2026-05-16

Status: candidate authorized by operator autonomy instruction for CVF 16.5
knowledge absorption.

## Purpose

Authorize a bounded OpenSpec Change Adapter runtime tranche.

## Scope

This tranche may add a Control Plane contract that maps OpenSpec-style
proposal/design/tasks/apply/verify/archive/sync artifacts into CVF phase and
authority boundaries.

In scope:

- artifact-to-phase mapping;
- delta grammar validation;
- CVF governance extension fields;
- direct apply bypass block;
- archive/sync canonical overwrite block;
- deterministic tests.

Out of scope:

- running OpenSpec;
- modifying canonical CVF docs;
- direct apply/sync/archive execution;
- live provider proof.

## Source

Primary source:

- `.private_reference/legacy/CVF 16.5/OpenSpec`

## Baseline

OpenSpec was previously `docs-classified`. CVF had reviewed the pattern but did
not enforce it as runtime-readable Control Plane behavior.

## Decision

Proceed with a Control Plane contract. Treat OpenSpec as structured input, not
as governance authority.

## Evidence

Expected evidence:

- source contract;
- focused Vitest coverage;
- Control Plane typecheck and test suite;
- governance pre-push chain.

## Verification

No live provider proof is required because the tranche does not assert live
provider enforcement.

## Claim Boundary

Passing this tranche may claim `runtime-owned` OpenSpec Change Adapter behavior.
It may not claim OpenSpec execution, canonical sync, or direct apply.
