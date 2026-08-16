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

## Scope / Applies To

Applies to owner reconciliation, bounded environment-snapshot design, and
future work orders that enrich the existing CVF runtime doctor.

## Claim Boundary

The current accepted seam is an enrichment candidate for the existing
`scripts/cvf_doctor.py` diagnostic owner. Candidate acquisition, mutation,
credential, network, provider, public-sync, deployment, and production work
remain separately governed.
