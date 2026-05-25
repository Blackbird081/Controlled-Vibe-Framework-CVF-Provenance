# CVF GC-018 Phase 2.B Audit Trace Task Receipt Chains Migration

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
- `docs/roadmaps/CVF_PHASE_2B_AUDIT_TRACE_TASK_RECEIPT_CHAINS_MIGRATION_ROADMAP_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_AUDIT_TRACE_TASK_RECEIPT_CHAINS_MIGRATION_CODEX_REBUTTAL_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_RECEIPT_CRITICAL_PATH_MIGRATION_COMPLETION_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_EXECUTION_BRIDGE_RECEIPT_CHAIN_MIGRATION_COMPLETION_2026-05-20.md`

---

## Purpose / Decision / Baseline

Decision: implement the grouped receipt-chain tranche:

- `E-06 -> M-05 -> M-06`
- `E-03 -> M-02 / M-03`
- `E-04 -> E-05`
- `M-07`

Baseline: existing audit, trace, execution, gateway, and receipt-envelope
payload shapes remain intact and are wrapped or re-exported through typed
canonical Phase 1.R surfaces.

---

## Decision / Baseline / Proposed Tranche

Proposed tranche: audit/trace/task/index/formal receipt-chain migration.

Accepted decision: add typed envelope wrappers, immutable marker records, index
exports, and focused tests. Reject provider runtime, Maika, persistence-store,
database schema migration, live proof, Claude participation, public catalog
claim, and global freeze lift.

---

## Scope / Proposed Tranche

In scope:

- E-06 guard-contract typed receipt aliases.
- M-05 trace-emitter receipt envelopes.
- M-06 SQLite audit envelope ingestion and row envelopes.
- M-02 execution pipeline receipt envelope and task record.
- M-03 execution bridge task record.
- E-05 model-gateway receipt index type exports.
- M-07 receipt-envelope receipt-tier record helper.

Out of scope:

- Rows outside the listed chains.
- Runtime provider calls.
- Persistent memory store.
- Database schema migration.
- Claude review or Claude-authored work product.
- Public-sync work.

---

## Evidence / Required Evidence / Verification

Required verification:

- package tests/checks for touched packages;
- docs governance checks;
- completion review with explicit boundary statement.

---

## Claim Boundary

This GC-018 authorizes only the grouped audit/trace/task/index/formal
receipt-chain migration. It does not authorize broad Phase 2.B migration, live
runtime proof, provider execution changes, Maika changes, persistent memory,
database schema migration, Claude review, public catalog update, or global
freeze release.
