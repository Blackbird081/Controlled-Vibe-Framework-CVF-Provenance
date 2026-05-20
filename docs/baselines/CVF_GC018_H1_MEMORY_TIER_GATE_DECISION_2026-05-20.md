# CVF GC-018 H1 Memory Tier Gate Decision

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-20

---

## Purpose

Authorize exactly one memory-tier contract path.

---

## Source or Predecessor Evidence

- `docs/work_orders/CVF_WO_RESIDUAL_H1_MEMORY_TIER_GATE_2026-05-20.md`
- `docs/reviews/CVF_H2_AUDIT_MEMORY_POLICY_REFINEMENT_COMPLETION_2026-05-19.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled.memory.gateway.contract.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled.memory.subcontracts.ts`

---

## Decision / Baseline

Decision: Path B, single classifier contract.

Path B is chosen because the five proposed tiers share one discrimination
shape: tier identity plus privacy/persistence semantics. Five separate files
would duplicate the same structure without runtime enforcement.

Rejected path: Path A, five typed-per-tier files, because it would create
parallel reference contracts for labels that are better represented as one
discriminated union.

---

## Scope or Proposed Tranche

Authorized:

- Create `memory-tier-classifier.contract.ts`.
- Add pure-function tests.

Forbidden:

- Shipping Path A files.
- Runtime memory wiring.
- Provider prompt reinjection.
- Persistence or retrieval changes.

---

## Evidence / Required Evidence / Verification

Required verification:

- `npm test` in `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION`
- `npm run check` in `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION`

---

## Claim Boundary

This baseline authorizes a contract classifier only. It does not claim runtime
memory hierarchy, organizational memory, retrieval, injection, or provider
integration.
