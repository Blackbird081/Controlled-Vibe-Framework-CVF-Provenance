Memory class: GOVERNANCE_BASELINE

# CVF ADR OpenSpec Change Adapter Runtime Ownership - 2026-05-16

Status: accepted.

## Purpose

Record owner placement for OpenSpec Change Adapter runtime behavior.

## Scope

Owner surface:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`

## Source

Source bundle:

- `.private_reference/legacy/CVF 16.5/OpenSpec`

## Baseline

The OpenSpec source is useful as change-packet discipline, but CVF must not let
external apply/sync/archive semantics override governance.

## Context

CVF already has phase gates and governance receipts. OpenSpec is absorbed only
where it makes change structure more explicit.

## Alternatives

Alternative A: copy OpenSpec documents into docs only.

Disposition: rejected because selected knowledge would not become living.

Alternative B: create an OpenSpec execution bridge.

Disposition: rejected for this tranche because it would expand runtime authority.

Alternative C: create a Control Plane adapter contract.

Disposition: accepted.

## Decision

Control Plane owns the adapter:

- `openspec.change.adapter.contract.ts`

## Consequences

CVF gains machine-checkable mapping from OpenSpec artifacts to CVF phases while
blocking direct execution and canonical overwrite.

## Evidence

Evidence is recorded in the closure packet.

## Verification

Focused tests and package checks must pass before commit.

## Claim Boundary

This ADR authorizes adapter semantics only, not OpenSpec runtime execution.
