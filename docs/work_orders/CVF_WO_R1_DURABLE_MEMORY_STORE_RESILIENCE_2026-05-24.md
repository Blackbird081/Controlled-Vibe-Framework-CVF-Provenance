# CVF Work Order: R1 - Durable Memory Store Resilience

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS

docType: work_order

Date: 2026-05-24

Tranche: R1

Roadmap: `docs/roadmaps/CVF_R1_R2_P2_POST_M1_GAP_CLOSURE_ROADMAP_2026-05-24.md`

---

## Purpose

Close the immediate M1 resilience gap found by post-implementation audit:
file-backed durable memory must not crash when the backing JSON file is
missing, corrupt, malformed, or partially invalid. Durable-memory receipts must
also be unique across repeated operations.

---

## Scope / Target / Owner Boundary

Target:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/durable-memory-store.test.ts`

Owner: CVF Learning Plane durable memory store.

Boundary: R1 does not wire durable memory into `/api/execute`, change
reinjection policy, or broaden durable persistence beyond `skill` and
`long-term` tiers.

---

## Authority Chain

- Roadmap: `docs/roadmaps/CVF_R1_R2_P2_POST_M1_GAP_CLOSURE_ROADMAP_2026-05-24.md`
- M1 completion review:
  `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`

---

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Planner | Confirm R1 is localized and does not require route GC-018. |
| Implementer | Patch store resilience and receipt id generation. |
| QA | Run targeted durable-memory tests and LPF TypeScript check. |
| Governance Reviewer | Confirm no reinjection or persistence-scope widening. |
| Release Manager | File completion review and commit. |

---

## Required First Reads

- `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/durable-memory-store.test.ts`

---

## Write Ownership

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/durable-memory-store.test.ts`
- `docs/reviews/CVF_R1_DURABLE_MEMORY_STORE_RESILIENCE_COMPLETION_2026-05-24.md`
- `docs/roadmaps/CVF_R1_R2_P2_POST_M1_GAP_CLOSURE_ROADMAP_2026-05-24.md`

---

## Pre-Flight Checks

- Confirm M1 is `CLOSED_PASS`.
- Confirm no `/api/execute` route edit is required for R1.
- Confirm `canReinject=false` remains out of scope for modification.

---

## Source / Review Input

Post-M1 audit found that `FileBackedDurableMemoryStore.list()` parsed JSON
directly and could throw on corrupt file contents. It also found receipt ids
were based on operation and memory ids, so repeated reads could collide.

---

## Execution Plan

1. Add defensive parse behavior to the file-backed `list()` implementation.
2. Validate list entries before returning them.
3. Generate unique receipt ids per operation.
4. Add unit coverage for corrupt JSON and repeated receipt ids.
5. Run LPF targeted tests and TypeScript check.
6. File completion review.

---

## Evidence Requirements

Required:

- Corrupt JSON test: PASS.
- Unique receipt id test: PASS.
- Existing durable memory tests remain PASS.
- LPF TypeScript check remains PASS.

---

## Acceptance Criteria

- [x] Corrupt JSON returns an empty safe list instead of throwing.
- [x] Non-array or invalid records are not surfaced from file-backed storage.
- [x] Receipt ids are unique across repeated operations.
- [x] `canReinject=false` remains unchanged.
- [x] Completion review filed.

---

## Decision / Recommendation / Disposition

Disposition: `CLOSED_PASS`.

---

## Review Gate

The completion review must confirm corrupt JSON handling, unique receipt ids,
targeted tests, TypeScript check, and no route/reinjection scope expansion.

---

## Operator Checkpoint

Operator supplied the Claude audit. Codex treated R1 as fast-lane corrective
work and left R2/P2 gated.

---

## Closure Checklist

- [x] M1 completion review read.
- [x] Store resilience patched.
- [x] Receipt id uniqueness patched.
- [x] Unit tests updated.
- [x] Targeted tests PASS.
- [x] TypeScript check PASS.
- [x] Completion review filed.

---

## Return-To-Orchestrator Conditions

Return blocked if targeted durable-memory tests fail, TypeScript check fails,
or the fix requires route behavior changes.

---

## Claim Boundary

R1 supports only a resilience claim for the M1 durable store. It does not claim
route integration, live memory benefit through the web UI, autonomous memory
reinjection, or hosted production durability.
