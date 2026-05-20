# CVF GC-018 Phase 2.B Policy Risk Chain Adapters Migration

Memory class: FULL_RECORD

Status: GC018_ACCEPTED_FOR_BOUNDED_IMPLEMENTATION

docType: baseline

Date: 2026-05-20

---

## Status

Accepted for one grouped but bounded dependency-chain implementation tranche.

---

## Source / Predecessor Evidence

- `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/roadmaps/CVF_PHASE_2B_POLICY_RISK_CHAIN_ADAPTERS_MIGRATION_ROADMAP_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_POLICY_RISK_CHAIN_ADAPTERS_MIGRATION_CODEX_REBUTTAL_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_RECEIPT_CRITICAL_PATH_MIGRATION_COMPLETION_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_EXECUTION_BRIDGE_RECEIPT_CHAIN_MIGRATION_COMPLETION_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_AUDIT_TRACE_TASK_RECEIPT_CHAINS_MIGRATION_COMPLETION_2026-05-20.md`

---

## Purpose / Decision / Baseline

Decision: implement the grouped policy/risk adapter tranche:

- `P-01 -> P-06 -> P-05`
- `P-01 -> P-02 + P-03 -> P-04`
- `R-02 -> R-03 -> R-13 / R-14`

Baseline: existing policy/risk decisions remain intact and are exposed through
additive contract snapshots.

---

## Decision / Baseline / Proposed Tranche

Proposed tranche: policy/risk adapter snapshot migration.

Accepted decision: add bounded adapter helpers, index exports, and focused
tests. Reject provider runtime, Maika, persistence-store, database schema
migration, live proof, Claude participation, public catalog claim, kernel owner
replacement, and global freeze lift.

---

## Scope / Proposed Tranche

In scope:

- P-01 governance-engine policy engine adapter.
- P-02 governance-engine API response adapter helper.
- P-03 governance-engine orchestrator adapter.
- P-04 governance-engine main summary adapter.
- P-06 model-gateway routing-policy adapter.
- P-05 model-gateway index export.
- R-02 safety-runtime risk-engine adapter.
- R-03 safety-runtime contamination risk-detector adapter.
- R-13 safety-runtime risk-propagation adapter.
- R-14 safety-runtime contamination risk-scorer adapter.

Out of scope:

- Rows outside the listed chains.
- Runtime provider calls.
- Persistent memory store.
- Database schema migration.
- Kernel owner replacement.
- Claude review or Claude-authored work product.
- Public-sync work.

---

## Evidence / Required Evidence / Verification

Required verification:

- targeted Governance Engine pytest;
- Model Gateway tests/check;
- Safety Runtime compile checks for touched surfaces;
- docs governance checks;
- completion review with explicit boundary statement.

---

## Claim Boundary

This GC-018 authorizes only the grouped policy/risk adapter snapshot migration.
It does not authorize broad Phase 2.B migration, live runtime proof, provider
execution changes, Maika changes, persistent memory, database schema migration,
Claude review, public catalog update, kernel owner replacement, or global
freeze release.
