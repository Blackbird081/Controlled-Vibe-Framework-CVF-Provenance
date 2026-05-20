# CVF GC-018 Phase 2.B Receipt Critical Path Migration

Memory class: FULL_RECORD

Status: GC018_ACCEPTED_FOR_BOUNDED_IMPLEMENTATION

docType: baseline

Date: 2026-05-20

---

## Status

Accepted for one bounded dependency-chain implementation tranche.

---

## Source / Predecessor Evidence

- `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/roadmaps/CVF_PHASE_2B_RECEIPT_CRITICAL_PATH_MIGRATION_ROADMAP_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_RECEIPT_CRITICAL_PATH_MIGRATION_CODEX_REBUTTAL_2026-05-20.md`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-envelope.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/gateway.consumer.contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts`

---

## Purpose / Decision / Baseline

Decision: implement the four-row critical path as a single bounded slice:

`E-01 -> E-02 -> E-04 -> M-08`

Baseline: existing receipt payload shapes remain intact and are wrapped in the
canonical `Receipt<TPayload>` envelope.

---

## Decision / Baseline / Proposed Tranche

Proposed tranche: receipt critical-path adapter migration.

Accepted decision: add typed envelope wrappers and tests. Reject provider
runtime, Maika, persistence, live proof, and global freeze lift.

---

## Scope / Proposed Tranche

In scope:

- E-01 agent governed session receipt envelope.
- E-02 gateway consumer receipt envelope.
- E-04 model gateway receipt envelope.
- M-08 model gateway receipt-memory record wrapper.
- Focused tests and package checks.

Out of scope:

- Rows outside E-01/E-02/E-04/M-08.
- Runtime provider calls.
- Persistent memory store.
- Public-sync work.

---

## Evidence / Required Evidence / Verification

Required verification:

- package tests/checks for touched packages;
- docs governance checks;
- completion review with explicit boundary statement.

---

## Claim Boundary

This GC-018 authorizes only the four-row critical path. It does not authorize
broad Phase 2.B migration, live runtime proof, provider execution changes,
Maika changes, persistent memory, or global freeze release.

