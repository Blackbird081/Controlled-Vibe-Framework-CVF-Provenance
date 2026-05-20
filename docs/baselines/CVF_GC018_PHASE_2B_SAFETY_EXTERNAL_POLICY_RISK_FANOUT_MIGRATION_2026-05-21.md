# CVF GC-018 Phase 2.B Safety External Policy Risk Fanout Migration

Memory class: FULL_RECORD

Status: GC018_ACCEPTED_FOR_BOUNDED_IMPLEMENTATION

docType: baseline

Date: 2026-05-21

---

## Status

Accepted for one grouped but bounded dependency-chain implementation tranche.

---

## Source / Predecessor Evidence

- `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/roadmaps/CVF_PHASE_2B_SAFETY_EXTERNAL_POLICY_RISK_FANOUT_MIGRATION_ROADMAP_2026-05-21.md`
- `docs/reviews/CVF_PHASE_2B_SAFETY_EXTERNAL_POLICY_RISK_FANOUT_MIGRATION_CODEX_REBUTTAL_2026-05-21.md`
- `docs/reviews/CVF_PHASE_2B_POLICY_RISK_CHAIN_ADAPTERS_MIGRATION_COMPLETION_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_IDENTITY_CONTROL_PLANE_ADAPTERS_MIGRATION_COMPLETION_2026-05-21.md`

---

## Purpose / Decision / Baseline

Decision: implement the grouped safety-tail, external/ecosystem risk fanout,
and external policy adapter tranche:

- `R-02 -> R-04 / R-05 / R-15 / R-16`
- `R-01 -> R-06 / R-07 / R-08 / R-09 / R-10 / R-11 / R-12`
- `P-01 -> P-07 / P-08`

Baseline: existing risk and policy outputs remain intact and are exposed
through additive adapter snapshots.

---

## Decision / Baseline / Proposed Tranche

Proposed tranche: safety-tail, external/ecosystem risk fanout, and external
policy adapter snapshot migration.

Accepted decision: add bounded adapter helpers and focused tests. Reject new
risk/policy/guard engines, provider runtime, Maika, persistence-store, database
schema migration, live proof, Claude participation, public catalog claim,
kernel owner replacement, and global freeze lift.

---

## Scope / Proposed Tranche

In scope:

- safety-tail risk evolution, refusal gate, risk lock, and risk scorer
  snapshots;
- external/ecosystem scorer, aggregator, module, gate, hook, and skill-risk
  snapshots;
- external policy decision and certification snapshots;
- focused tests and completion review.

Out of scope:

- rows outside the listed chains;
- new risk/policy/guard engines;
- runtime provider calls;
- Maika behavior;
- persistent memory store;
- database schema migration;
- kernel owner replacement;
- Claude review or Claude-authored work product;
- public-sync work.

---

## Evidence / Required Evidence / Verification

Required verification:

- focused tests for available package toolchains;
- package build/type checks where available;
- docs governance checks;
- completion review with explicit no-live-proof boundary.

---

## Claim Boundary

This GC-018 authorizes only the grouped safety-tail, external/ecosystem risk
fanout, and external policy adapter snapshot migration. It does not authorize
broad Phase 2.B migration, live runtime proof, provider execution changes,
Maika changes, persistent memory, database schema migration, new risk/policy
engine semantics, Claude review, public catalog update, kernel owner
replacement, or global freeze release.
