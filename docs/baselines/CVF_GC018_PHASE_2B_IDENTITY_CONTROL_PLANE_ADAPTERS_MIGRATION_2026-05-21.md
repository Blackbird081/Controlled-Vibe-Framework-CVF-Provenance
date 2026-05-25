# CVF GC-018 Phase 2.B Identity Control Plane Adapters Migration

Memory class: FULL_RECORD

Status: GC018_ACCEPTED_FOR_BOUNDED_IMPLEMENTATION

docType: baseline

Date: 2026-05-21

---

## Status

Accepted for one grouped but bounded dependency-chain implementation tranche.

---

## Source / Predecessor Evidence

- `docs/reference/archive/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/roadmaps/CVF_PHASE_2B_IDENTITY_CONTROL_PLANE_ADAPTERS_MIGRATION_ROADMAP_2026-05-21.md`
- `docs/reviews/CVF_PHASE_2B_IDENTITY_CONTROL_PLANE_ADAPTERS_MIGRATION_CODEX_REBUTTAL_2026-05-21.md`
- `docs/reviews/archive/CVF_PHASE_2B_POLICY_RISK_CHAIN_ADAPTERS_MIGRATION_COMPLETION_2026-05-20.md`
- `docs/reviews/archive/CVF_PHASE_2B_AUDIT_TRACE_TASK_RECEIPT_CHAINS_MIGRATION_COMPLETION_2026-05-20.md`

---

## Purpose / Decision / Baseline

Decision: implement the grouped identity/control-plane adapter tranche:

- `I-01 -> I-02 -> I-03 / I-07`
- `I-01 -> I-04 -> I-05`
- `I-03 -> I-06`

Baseline: existing identity/control-plane contract outputs remain intact and
are exposed through additive adapter snapshots or barrel exports.

---

## Decision / Baseline / Proposed Tranche

Proposed tranche: identity/control-plane adapter snapshot migration.

Accepted decision: add bounded adapter helpers, barrel exports, and focused
tests. Reject new role taxonomy, provider runtime, Maika, persistence-store,
database schema migration, live proof, Claude participation, public catalog
claim, kernel owner replacement, and global freeze lift.

---

## Scope / Proposed Tranche

In scope:

- I-01 agent definition boundary adapter.
- I-02 design-plan adapter.
- I-03 orchestration adapter.
- I-04 continuity checkpoint adapter.
- I-05 continuation barrel adapter exports.
- I-06 coordination barrel adapter.
- I-07 phase-governance extension-bridge adapter.

Out of scope:

- Rows outside the listed chains.
- Runtime provider calls.
- New role taxonomy or actor queue.
- Persistent memory store.
- Database schema migration.
- Kernel owner replacement.
- Claude review or Claude-authored work product.
- Public-sync work.

---

## Evidence / Required Evidence / Verification

Required verification:

- Control Plane Foundation targeted/full tests and typecheck;
- Phase Governance Protocol targeted/full tests and typecheck;
- docs governance checks;
- completion review with explicit boundary statement.

---

## Claim Boundary

This GC-018 authorizes only the grouped identity/control-plane adapter snapshot
migration. It does not authorize broad Phase 2.B migration, live runtime proof,
provider execution changes, Maika changes, persistent memory, database schema
migration, new role taxonomy, Claude review, public catalog update, kernel
owner replacement, or global freeze release.
