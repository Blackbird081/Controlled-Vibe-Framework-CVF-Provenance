# Capability Preflight Bootstrap

Memory class: POINTER_RECORD

Status: ACTIVE_INDEX

## Purpose

This folder owns durable CVF reference material for capability-environment
preflight and bootstrap boundaries. Runtime code remains in its existing
script or package owner; this folder does not grant execution authority.

## Current Surfaces

- `CVF_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_CONTRACT.md` maps the
  mixed-origin candidate fields to existing CVF owners, explicit gaps, and
  rejected or parked lanes.
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/controlled-acquisition.contract.ts`
  is the absorbed RSPB-AI-T3 contract kernel for deterministic plan digests,
  exact approval binding, fail-closed authorization, receipt reconciliation,
  and bounded repair-stop decisions. It is pure decision logic and cannot
  download, install, mutate, roll back, or invoke a provider.

## Scope / Applies To

Applies to owner reconciliation, bounded environment-snapshot design, and
future work orders that enrich the existing CVF runtime doctor.

## Claim Boundary

The read-only snapshot seam is implemented in the existing
`scripts/cvf_doctor.py` owner. The controlled-acquisition contract kernel is
runtime-testable in Guard Contract, but any executor and any actual
acquisition, mutation, credential, network, provider, public-sync, deployment,
or production action remain separately governed.
