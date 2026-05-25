# CVF Phase 2.B Audit Trace Task Receipt Chains Migration Roadmap

Memory class: FULL_RECORD

Status: CLOSED_AUDIT_TRACE_TASK_RECEIPT_CHAINS_MIGRATION

docType: roadmap

Date: 2026-05-20

---

## Status

This roadmap authorizes and records a grouped but bounded Phase 2.B dependency
tranche:

- `E-06 -> M-05 -> M-06`
- `E-03 -> M-02 / M-03`
- `E-04 -> E-05`
- `M-07`

It is not a broad Phase 2.B bulk migration.

---

## Authorization / Decision

Authority chain:

- Phase 2.B migration plan:
  `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- Prior receipt critical path closure:
  `docs/reviews/CVF_PHASE_2B_RECEIPT_CRITICAL_PATH_MIGRATION_COMPLETION_2026-05-20.md`
- Prior execution bridge receipt chain closure:
  `docs/reviews/CVF_PHASE_2B_EXECUTION_BRIDGE_RECEIPT_CHAIN_MIGRATION_COMPLETION_2026-05-20.md`
- HN2.b owner map:
  `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- HN2.c freeze-release rule:
  `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`

Decision: run these chains together because all are receipt-envelope or
receipt-task surfaces, and all can close without provider runtime, Maika,
memory-store, or kernel-owner replacement.

---

## Purpose / Why This Tranche

The previous Phase 2.B slices established canonical `Receipt<TPayload>`
wrappers for the primary receipt and bridge surfaces. This tranche completes the
nearby audit/trace/task/index/formalization rows so the receipt lane can advance
without reopening policy/risk/provider semantics.

---

## Scope

In scope:

- `E-06`: guard-contract typed receipt aliases.
- `M-05`: trace-emitter receipt envelope.
- `M-06`: SQLite audit receipt-envelope insertion and row wrapping.
- `M-02`: execution pipeline receipt envelope and immutable task record.
- `M-03`: execution bridge immutable task record.
- `E-05`: model-gateway index exports for gateway receipt envelope and
  receipt memory record types.
- `M-07`: formal immutable receipt-tier record wrapper for any receipt envelope.
- Codex-only workflow role chain.

---

## Non-Goals

- No Claude review or Claude-authored work product.
- No provider runtime change.
- No Maika change.
- No persistent memory-store implementation.
- No live governance proof claim.
- No database schema migration.
- No broad runtime coherence claim.
- No global freeze lift.
- No public catalog claim.
- No rows outside the listed receipt/task chains.

---

## Work Plan

1. Add typed guard-contract receipt aliases for guard pipeline, audit entry, and
   governance evidence payloads.
2. Add trace-emitter receipt envelope helpers.
3. Add SQLite audit envelope insertion and database-row envelope wrapping
   without changing schema.
4. Add execution pipeline receipt envelope and immutable task record helpers.
5. Add execution bridge immutable task record helper.
6. Export model-gateway receipt envelope/memory-record types from the index.
7. Add formal receipt-envelope receipt-tier record helper.
8. Add focused tests.
9. Run package tests/checks and docs gates.
10. File completion review and update active session pointers.

---

## Acceptance Criteria

- Existing payload shapes remain unchanged.
- New wrappers use `schemaVersion: "1.R.0"`.
- Wrapper payloads are typed, never `any`.
- SQLite audit behavior uses existing row schema.
- Task/receipt records are immutable marker records only, not stores.
- Completion review records no Claude participation and no
  provider/Maika/live-proof/global-freeze/public-catalog claim.

---

## Verification / Evidence

Required:

- `npm test` and `npm run check` in `EXTENSIONS/CVF_GUARD_CONTRACT`
- `npm test` and `npm run check` in
  `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION`
- `npm test` and `npm run check` in `EXTENSIONS/CVF_MODEL_GATEWAY`
- `python governance/compat/check_docs_governance_compat.py`
- `python governance/compat/check_markdown_structural_completeness.py`

---

## Claim Boundary

This roadmap may be cited only as authorization for the listed receipt,
audit/trace, task, index-export, and formal receipt-record chains. It must not
be cited as broad Phase 2.B migration, live runtime proof, provider execution
change, Maika change, persistent memory, Claude review, public catalog update,
or global freeze release.
