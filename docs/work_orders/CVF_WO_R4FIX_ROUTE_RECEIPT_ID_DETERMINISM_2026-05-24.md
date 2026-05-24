# CVF Work Order: R4-fix — Route Receipt-Id Determinism

Memory class: FULL_RECORD

Status: WORK_ORDER_READY

docType: work_order

Date: 2026-05-24

Tranche: R4-fix

Roadmap: `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Purpose

Replace the non-deterministic `Date.now().toString(36) + Math.random()`
receipt-id pattern in `emptyReceipt()` inside `durable-memory-route.ts` with
`randomUUID()` from `node:crypto`, matching the pattern already adopted in R1
for `durable-memory-store.ts`.

This is a Fast Lane corrective — no behavior change, no route logic change,
no new claim.

operator.checkpoint.waiver: localized one-function fix, no route behavior
change, no public claim change, Fast Lane audit covers governance requirement.

---

## Authority Chain

- Fast Lane audit: `docs/reviews/CVF_R4FIX_ROUTE_RECEIPT_ID_FAST_LANE_AUDIT_2026-05-24.md`
- Roadmap: `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md`
- R1 precedent: `docs/reviews/CVF_R1_DURABLE_MEMORY_STORE_RESILIENCE_COMPLETION_2026-05-24.md`
- R2 target file: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/durable-memory-route.ts`

---

## Scope / Target / Owner Boundary

Target: one function in one file.

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/durable-memory-route.ts`
  — `emptyReceipt()` function, `receiptId` field only.

Out of scope: any other function, file, route logic, receipt schema, or
public claim.

---

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Implementer | Apply the one-line fix; update test assertion. |
| QA | TypeScript check PASS; confirm test asserts UUID pattern. |
| Release Manager | File Fast Lane audit; commit. |

---

## Required First Reads

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/durable-memory-route.ts`
  (current `emptyReceipt()` implementation)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`
  (R1 `randomUUID()` pattern to mirror)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.durable-memory.test.ts`
  (current test assertions for receiptId)

---

## Write Ownership

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/durable-memory-route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.durable-memory.test.ts`
  (update assertions to check UUID pattern)
- `docs/reviews/CVF_R4FIX_ROUTE_RECEIPT_ID_FAST_LANE_AUDIT_2026-05-24.md`

---

## Pre-Flight Checks

- Confirm `durable-memory-route.ts` still has `receiptId: \`r2-read-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 8)}\`` in `emptyReceipt()`.
- Confirm `randomUUID` is already imported in `durable-memory-store.ts` (R1
  precedent) so the import pattern is established.
- Check GC-023 line count on `durable-memory-route.ts` before edit.

---

## Allowed / Forbidden Scope

Allowed:

- Replace `receiptId` generation in `emptyReceipt()` with `randomUUID()`.
- Add `import { randomUUID } from 'node:crypto'` if not already present.
- Update test assertions that were skipping receiptId to assert UUID pattern
  (`/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i`).
- File Fast Lane audit.

Forbidden:

- Any change to route logic, policy gate, store path, prompt building, or
  receipt fields other than `receiptId`.
- Any public catalog change.
- Any new claim.

---

## Execution Plan

1. Read target files (pre-flight).
2. Add `import { randomUUID } from 'node:crypto'` to `durable-memory-route.ts`.
3. Replace `receiptId` in `emptyReceipt()`:
   `receiptId: randomUUID()`
4. Update route test: add UUID pattern assertion for emptyReceipt paths.
5. Run `npm run check` in `cvf-web`. Must PASS.
6. Run targeted route tests. Must PASS.
7. File Fast Lane audit at:
   `docs/reviews/CVF_R4FIX_ROUTE_RECEIPT_ID_FAST_LANE_AUDIT_2026-05-24.md`
8. Commit.

---

## Evidence Requirements

- Diff showing `randomUUID()` in `emptyReceipt()`.
- TypeScript check PASS.
- Route test run PASS with UUID assertion.
- Fast Lane audit filed.

---

## Acceptance Criteria

- [ ] `receiptId` in `emptyReceipt()` uses `randomUUID()`.
- [ ] `import { randomUUID } from 'node:crypto'` present.
- [ ] Route tests assert UUID pattern (not skip).
- [ ] TypeScript check PASS.
- [ ] Fast Lane audit filed.

---

## Review Gate

Fast Lane audit must confirm:

- Change is localized to one function in one file.
- No route behavior change introduced.
- No receipt schema change.
- No new public claim.

---

## Closure Checklist

- [ ] Fix applied.
- [ ] Test assertion updated.
- [ ] TypeScript check PASS.
- [ ] Fast Lane audit filed and committed.

---

## Return-To-Orchestrator Conditions

Return blocked if TypeScript check fails or test introduces a breaking
assertion on another receipt field.

---

## Tasks

| Task | Status | Output |
| --- | --- | --- |
| Fix `emptyReceipt()` receiptId | PENDING | `randomUUID()` in place. |
| Update test assertion | PENDING | UUID pattern asserted. |
| TypeScript check | PENDING | PASS. |
| Fast Lane audit | PENDING | Filed. |

---

## Claim Boundary

R4-fix is a corrective quality fix only. It does not change route behavior,
receipt schema, public claims, or any other tranche's pass conditions.
