# CVF Work Order - Phase 2.B Receipt Critical Path Migration

Memory class: FULL_RECORD

Status: CLOSED

docType: work_order

Date: 2026-05-20

---

## Purpose

Implement the bounded receipt critical path `E-01 -> E-02 -> E-04 -> M-08`
from the locked Phase 2.B migration plan.

---

## Authority Chain

- `docs/baselines/CVF_GC018_PHASE_2B_RECEIPT_CRITICAL_PATH_MIGRATION_2026-05-20.md`
- `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_RECEIPT_CRITICAL_PATH_MIGRATION_CODEX_REBUTTAL_2026-05-20.md`

---

## Agent Roles

- Operator: user authorization for grouped critical path.
- Implementer: Codex in Worker role.
- Reviewer: Codex completion-review posture.

---

## Scope / Target / Owner Boundary

Targets:

- E-01: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts`
- E-02: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/gateway.consumer.contract.ts`
- E-04/M-08: `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts`
- Receipt helper:
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-envelope.contract.ts`

---

## Allowed / Forbidden Scope

Allowed:

- typed envelope wrappers;
- immutable receipt-tier memory record wrapper;
- focused tests;
- docs/state/handoff updates.

Forbidden:

- provider runtime behavior;
- Maika changes;
- persistent memory store;
- rows outside the four-row path;
- global freeze lift.

---

## Required First Reads

- `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`

---

## Pre-Flight Checks

- Confirm all four rows are in the locked migration plan.
- Confirm no row is Stage C.
- Confirm existing receipt payload shapes are preserved.

---

## Write Ownership

Write ownership is limited to the target source/test files and this tranche's
governance docs/continuity pointers.

---

## Execution Plan

1. Add canonical envelope helper.
2. Add E-01 wrapper.
3. Add E-02 wrapper.
4. Add E-04 wrapper.
5. Add M-08 receipt-memory record wrapper.
6. Add tests.
7. Run package and docs checks.
8. File completion review.

---

## Evidence Requirements

- Tests/checks for Guard Contract, Control Plane Foundation, and Model Gateway.
- Docs governance and structural checks.
- Completion review records boundaries.

---

## Acceptance Criteria

- `Receipt<TPayload>` wrappers use schema version `1.R.0`.
- Existing receipts remain readable as payloads.
- M-08 record is immutable and tiered as `receipt`.
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

Return if implementation requires provider runtime changes, persistence, or any
row outside E-01/E-02/E-04/M-08.

---

## Claim Boundary

This work order closes the four-row receipt critical path only. It does not
prove broad runtime coherence or live governance behavior.

