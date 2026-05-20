# CVF Work Order - Phase 2.B Audit Trace Task Receipt Chains Migration

Memory class: FULL_RECORD

Status: CLOSED

docType: work_order

Date: 2026-05-20

---

## Purpose

Implement the grouped but bounded Phase 2.B receipt-chain tranche:

- `E-06 -> M-05 -> M-06`
- `E-03 -> M-02 / M-03`
- `E-04 -> E-05`
- `M-07`

---

## Authority Chain

- `docs/baselines/CVF_GC018_PHASE_2B_AUDIT_TRACE_TASK_RECEIPT_CHAINS_MIGRATION_2026-05-20.md`
- `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_AUDIT_TRACE_TASK_RECEIPT_CHAINS_MIGRATION_CODEX_REBUTTAL_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_RECEIPT_CRITICAL_PATH_MIGRATION_COMPLETION_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_EXECUTION_BRIDGE_RECEIPT_CHAIN_MIGRATION_COMPLETION_2026-05-20.md`

---

## Agent Roles

Codex performed all roles in a self-contained CVF chain:

- Operator proxy: apply user's explicit authorization to finish the grouped
  chains.
- Proposer: bound the tranche to receipt/task/index surfaces.
- Reviewer: file Codex rebuttal and scope gate.
- Implementer: make source/test changes.
- Verifier: run package and docs checks.
- Closure reviewer: file completion review.

Claude did not participate.

---

## Scope / Target / Owner Boundary

Targets:

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/audit/trace-emitter.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/audit/sqlite-db.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-envelope.contract.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/execution.pipeline.contract.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/execution.bridge.consumer.contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
- focused tests adjacent to those surfaces

---

## Allowed / Forbidden Scope

Allowed:

- typed envelope wrappers;
- immutable receipt/task marker records;
- index type exports;
- focused tests;
- docs/state/handoff updates.

Forbidden:

- provider runtime behavior;
- Maika changes;
- persistent memory store;
- database schema migration;
- rows outside the listed chains;
- Claude review dependency;
- global freeze lift.

---

## Required First Reads

- `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`
- `docs/reviews/CVF_PHASE_2B_RECEIPT_CRITICAL_PATH_MIGRATION_COMPLETION_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_EXECUTION_BRIDGE_RECEIPT_CHAIN_MIGRATION_COMPLETION_2026-05-20.md`

---

## Pre-Flight Checks

- Confirm requested rows are in the locked Phase 2.B plan.
- Confirm E-03 and E-04 prerequisites are closed.
- Confirm existing payload shapes are preserved.

---

## Write Ownership

Write ownership is limited to target source/test files and this tranche's
governance docs/continuity pointers.

---

## Execution Plan

1. Add E-06 typed guard receipt aliases.
2. Add M-05 trace-emitter envelope helpers.
3. Add M-06 SQLite audit envelope ingestion and row wrapping.
4. Add M-02 execution pipeline envelope/task record helpers.
5. Add M-03 execution bridge task record helper.
6. Add E-05 model-gateway index exports.
7. Add M-07 receipt-envelope receipt-tier record helper.
8. Add tests.
9. Run package and docs checks.
10. File completion review.

---

## Evidence Requirements

- Tests/checks for Guard Contract, Execution Plane Foundation, and Model
  Gateway.
- Docs governance and structural checks.
- Completion review records boundaries and no Claude participation.

---

## Acceptance Criteria

- `Receipt<TPayload>` wrappers use schema version `1.R.0`.
- Existing payloads remain readable as payloads.
- SQLite row shape remains unchanged.
- Task/receipt records are immutable marker records only.
- No provider/Maika/persistent-memory behavior is introduced.

---

## Review Gate

Close only after tests/checks pass and completion review is filed.

---

## Closure Checklist

- [x] GC-018 filed.
- [x] Code implemented.
- [x] Tests added.
- [x] Verification run.
- [x] Completion review filed.

---

## Return-To-Orchestrator Conditions

Return if implementation requires provider runtime changes, persistence-store,
database schema migration, Claude review, or any row outside the listed chains.

---

## Claim Boundary

This work order closes the grouped receipt-chain tranche only. It does not
prove broad runtime coherence or live governance behavior.
