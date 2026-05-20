# CVF GC-018 Phase 2.B Memory Tail Adapters Migration

Memory class: FULL_RECORD

Status: GC018_ACCEPTED_FOR_BOUNDED_IMPLEMENTATION

docType: baseline

Date: 2026-05-21

---

## Status

Accepted for one grouped but bounded memory-tail implementation tranche.

---

## Source / Predecessor Evidence

- `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/roadmaps/CVF_PHASE_2B_MEMORY_TAIL_ADAPTERS_MIGRATION_ROADMAP_2026-05-21.md`
- `docs/reviews/CVF_PHASE_2B_MEMORY_TAIL_ADAPTERS_MIGRATION_CODEX_REBUTTAL_2026-05-21.md`
- `docs/reviews/CVF_PHASE_2B_RECEIPT_CRITICAL_PATH_MIGRATION_COMPLETION_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_SAFETY_EXTERNAL_POLICY_RISK_FANOUT_MIGRATION_COMPLETION_2026-05-21.md`

---

## Purpose / Decision / Baseline

Decision: implement the bounded memory-tail adapter tranche:

- `E-01 closed -> M-01`
- `M-04` standalone memory-gateway adapter

Baseline: existing receipt and memory-gateway outputs remain intact and are
exposed through additive adapter snapshots.

---

## Decision / Baseline / Proposed Tranche

Proposed tranche: `M-01` and `M-04` memory-tail adapter snapshot migration.

Accepted decision: add bounded adapter helpers and focused tests. Reject
persistent memory, new memory tiers, reinjection runtime expansion, provider
runtime, Maika, database schema migration, live proof, Claude participation,
public catalog claim, and global freeze lift.

---

## Scope / Proposed Tranche

In scope:

- `M-01`: `AgentGovernedSessionContract` working-memory adapter snapshot.
- `M-04`: `ControlledMemoryGatewayContract` adapter snapshot for existing
  capture, retrieve, and reinjection-result outputs.
- Focused tests and completion review.

Out of scope:

- rows outside `M-01` and `M-04`;
- persistent memory store;
- new memory tier;
- new reinjection runtime;
- runtime provider calls;
- Maika behavior;
- database schema migration;
- Claude review or Claude-authored work product;
- public-sync work.

---

## Evidence / Required Evidence / Verification

Required verification:

- focused/full Control Plane Foundation tests and typecheck;
- focused/full Learning Plane Foundation tests and typecheck;
- docs governance checks;
- completion review with explicit no-live-proof boundary.

---

## Claim Boundary

This GC-018 authorizes only the `M-01` and `M-04` memory-tail adapter snapshot
migration. It does not authorize broad Phase 2.B migration, live runtime proof,
provider execution changes, Maika changes, persistent memory, new memory tiers,
database schema migration, Claude review, public catalog update, runtime
coherence claims, or global freeze release.
