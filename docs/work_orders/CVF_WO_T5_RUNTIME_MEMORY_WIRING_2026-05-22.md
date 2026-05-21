# Work Order — T5 Runtime Memory Hierarchy Wiring

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Worker role: Codex (full Orchestrator → Reviewer → Implementer → Auditor chain)

Date dispatched: 2026-05-22

---

## Purpose

Wire the ephemeral in-memory task-tier store that addresses Review CVF.md
pain point H (runtime memory hierarchy). T5 delivers:

- A retention policy contract (governed markdown) declaring exactly what
  "ephemeral" means in CVF context.
- An in-process, in-memory task store (no file write, no database, no
  external store — lost on process exit by design).
- An extension to `audit-memory-receipt.ts` that surfaces
  `taskMemoryDecision` and `taskMemoryReason` in the audit readout
  without adding new receipt envelope fields.

T5 requires the `new_memory_tiers_beyond_lane_h_scope` blocked-work-class
override. The GC-018 must record operator confirmation of this override
before any implementation begins.

Pre-condition: T4 must be closed before T5 begins.

---

## Authority Chain

- Active roadmap (V2):
  `docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md`
- Predecessor audit:
  `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
- T4 work order (pre-condition):
  `docs/work_orders/CVF_WO_T4_PROVIDER_METHOD_COVERAGE_2026-05-22.md`
- T4 completion review (must be filed before T5 starts):
  `docs/reviews/CVF_T4_PROVIDER_METHOD_COVERAGE_COMPLETION_2026-05-22.md`
- CDH-H audit-memory readout (related prior art):
  `docs/reviews/CVF_CDH_H_AUDIT_MEMORY_READOUT_COMPLETION_2026-05-21.md`
- Source review (original requirement):
  `.private_reference/legacy/CVF 17.05/Review CVF.md`
- GC-018 to be filed:
  `docs/baselines/CVF_GC018_T5_RUNTIME_MEMORY_WIRING_2026-05-22.md`

---

## Agent Roles

- **Orchestrator (Codex):** Confirm T4 is closed. File GC-018 baseline
  before any implementation file is created. The GC-018 must record
  operator confirmation of the `new_memory_tiers_beyond_lane_h_scope`
  override. Operator must confirm override before Orchestrator proceeds
  past S-02.
- **Reviewer (Codex):** Confirm T5 stays ephemeral in-memory only.
  No file write, no database, no external store, no archive tier.
  Confirm the audit-memory readout extension does not add new receipt
  envelope fields and does not enable reinjection.
- **Implementer (Codex):** Author the retention policy contract, the
  task memory store, and the audit-memory readout extension.
- **Auditor (Codex):** Run tests and TypeScript check, run governance
  hook chain, file completion review, update active queue/state/handoff.

---

## Blocked-Work Override Requirement

T5 touches one blocked-work class:

- **`new_memory_tiers_beyond_lane_h_scope`** — adding an ephemeral
  in-memory task-tier store beyond the audit-memory readout hardening
  delivered in CDH-H.

The GC-018 baseline must record:

- Override granted: `new_memory_tiers_beyond_lane_h_scope` for the
  specific bounded scope (ephemeral in-memory task store only; no
  archive, no file-backed, no database, no external, no durable
  persistence).
- Operator confirmation statement.
- Explicit boundary: the override does not authorize durable persistence,
  file-backed storage, or any external memory service. Memory is
  in-process only and is lost on process exit by design.

Operator confirmation of override status is required **before** the
Orchestrator proceeds past S-02 (GC-018). This is an Operator
Checkpoint.

---

## Scope / Target / Owner Boundary

### Write ownership (in scope)

- `governance/toolkit/05_OPERATION/CVF_MEMORY_TIER_RETENTION_POLICY.md`
  (new) — governed retention policy contract.
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/task-memory/`
  (new directory) containing:
  - `task-memory-store.ts` — ephemeral in-memory task store interface
    and implementation.
  - `task-memory-types.ts` — TypeScript types for task memory entries.
  - `index.ts` — re-export.
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/task-memory/__tests__/`
  — unit tests.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit/audit-memory-receipt.ts`
  — add two fields: `taskMemoryDecision` and `taskMemoryReason`. No
  other change to this file.
- Test updates in the existing audit-memory test file for the two new
  fields (must not break CDH-H tests).
- `docs/baselines/CVF_GC018_T5_RUNTIME_MEMORY_WIRING_2026-05-22.md`
  (new).
- `docs/reviews/CVF_T5_RUNTIME_MEMORY_WIRING_COMPLETION_2026-05-22.md`
  (new).
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` — update T5 entry status.
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` — update `lastUpdated` and
  `t5RuntimeMemoryWiring` field.
- `AGENT_HANDOFF_V11_2026-05-21.md` — GC-020 sync entry.

### Out of scope (forbidden)

- Any file write, database call, or external HTTP call from the task
  memory store.
- Any durable persistence (file-backed, database-backed, or
  external-service-backed).
- Any archive tier or long-term memory tier.
- Any change to `GovernanceEvidenceReceipt` or `types.ts`.
- Any change to `cvf-web/` files other than
  `audit-memory-receipt.ts`.
- Any change to any route file.
- Any change to `vision-contract.ts` or `reasoning-contract.ts`.
- Any provider adapter change (that is T4).
- Any workflow composition change (that is T3).
- Any reinjection of memory into the governance execution path.
- Public-sync repository update.
- Maika, child-data, photo, or vision proof.
- Any change to CDH-H fields (`writesRequireReceipt`,
  `privacyFilters`, `memoryReceiptDecision`, `memoryCaptureMode`,
  `memoryCaptureReason`) — CDH-H fields are read-only.

---

## Required First Reads

- `docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md`
- `docs/work_orders/CVF_WO_T4_PROVIDER_METHOD_COVERAGE_2026-05-22.md`
- `docs/reviews/CVF_T4_PROVIDER_METHOD_COVERAGE_COMPLETION_2026-05-22.md`
  (T4 pre-condition check)
- `docs/reviews/CVF_CDH_H_AUDIT_MEMORY_READOUT_COMPLETION_2026-05-21.md`
  (CDH-H prior art — understand existing audit-memory readout fields)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit/audit-memory-receipt.ts`
  (read current shape — read the exact existing fields before editing)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/`
  (read existing structure before authoring task-memory directory)
- `.private_reference/legacy/CVF 17.05/Review CVF.md` (lines covering
  memory hierarchy pain point H)
- `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`
- `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`

---

## Pre-Flight Checks

Before writing any implementation file:

1. Confirm T4 completion review exists with status
   `CLOSED_T4_PROVIDER_METHOD_COVERAGE`. If T4 is not closed, stop.
2. Read `audit-memory-receipt.ts` fully. Record all existing field names
   and the current line count before any edit. The file must not exceed
   the GC-023 threshold after adding two fields. If adding two fields
   would push it over the threshold, check the exception registry for
   an approved extension; if none, Return-to-Orchestrator.
3. Confirm CDH-H fields (`writesRequireReceipt`, `privacyFilters`,
   `memoryReceiptDecision`, `memoryCaptureMode`, `memoryCaptureReason`)
   are present and unchanged before editing.
4. Confirm `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/` exists. If
   the directory does not exist, Return-to-Orchestrator before creating
   new directories — check whether CVF_LEARNING_PLANE_FOUNDATION is an
   active extension or a placeholder.
5. Confirm `new_memory_tiers_beyond_lane_h_scope` override is recorded
   in the GC-018 before any implementation step (Operator Checkpoint).

---

## Execution Plan

T5 executes in ten sequential steps S-01 → S-10.

## Implementation Steps

### S-01 — Confirm T4 pre-condition

Read T4 completion review. Confirm status is
`CLOSED_T4_PROVIDER_METHOD_COVERAGE`. If not, stop and report.

### S-02 — File GC-018 baseline (with override)

Create `docs/baselines/CVF_GC018_T5_RUNTIME_MEMORY_WIRING_2026-05-22.md`
declaring:

- Pre-condition: T4 closed (cite completion review path).
- Scope locked to write ownership above.
- Blocked-work class: `new_memory_tiers_beyond_lane_h_scope`.
- Override GRANTED (cite operator confirmation).
- Bounded scope of override: ephemeral in-memory task store only; no
  durable persistence; no file write; no database; no external store;
  memory lost on process exit by design.
- Explicit anti-scope: override does NOT authorize durable persistence,
  archive tier, or any form of external memory service.
- Acceptance criteria copied verbatim from V2 roadmap T5.
- Forbidden actions: any out-of-scope item from this work order.

### S-03 — Author retention policy contract

Create
`governance/toolkit/05_OPERATION/CVF_MEMORY_TIER_RETENTION_POLICY.md`
defining:

- Memory tier taxonomy (for CVF context):
  - **Ephemeral** — in-process, in-memory only; lost on process exit;
    no write to disk, no network, no archive. This is the T5 tier.
  - **Durable** — file-backed or database-backed; requires separate
    authorization beyond T5; not authorized in this tranche.
  - **External** — third-party memory service; requires separate
    authorization; not authorized in this tranche.
- T5 authorizes Ephemeral tier only.
- Retention limit for ephemeral tier: within a single process lifetime;
  no cross-session persistence.
- Boundary: any write beyond the ephemeral tier requires a new GC-018
  with a fresh blocked-work override.
- Authority: V2 roadmap T5; this GC-018.

### S-04 — Author task memory store

Create `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/task-memory/task-memory-types.ts`
defining:

```typescript
export interface TaskMemoryEntry {
  taskId: string;
  createdAt: number;    // Unix timestamp ms
  expiresAt: number;    // Unix timestamp ms
  payload: Record<string, unknown>;
}

export interface TaskMemoryStore {
  set(entry: TaskMemoryEntry): void;
  get(taskId: string): TaskMemoryEntry | undefined;
  delete(taskId: string): void;
  list(): TaskMemoryEntry[];
  clear(): void;
}
```

Create `task-memory-store.ts` implementing `TaskMemoryStore` as a
plain in-memory `Map`. Requirements:

- No I/O operations (no `fs`, no `fetch`, no database client).
- `get()` must check `expiresAt` and return `undefined` for expired
  entries.
- `list()` must filter expired entries before returning.
- Expired entries are not automatically evicted; they are filtered on
  read. (Simple, no background timer.)
- Export a factory function `createTaskMemoryStore()` returning a new
  instance. No module-level singleton (tests must be able to create
  isolated instances).

Create `index.ts` re-exporting both.

### S-05 — Extend audit-memory readout

Edit `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit/audit-memory-receipt.ts`
to add two new fields to the exported readout type or the returned
object (whichever pattern the existing file uses):

- `taskMemoryDecision: 'CAPTURED' | 'SKIPPED' | 'EXPIRED' | 'NOT_APPLICABLE'`
- `taskMemoryReason: string`

Logic for populating these fields:

- If the task memory store has an entry for the current task ID at
  readout time: `CAPTURED` with reason `"task memory entry present"`.
- If the task memory store has no entry and the task has completed
  normally: `SKIPPED` with reason `"no task memory requested"`.
- If the task memory store had an entry that is now expired:
  `EXPIRED` with reason `"entry expired before readout"`.
- If the memory store is not initialized for this route context:
  `NOT_APPLICABLE` with reason `"task memory not wired to this context"`.

**Critical constraints:**

- The two new fields must NOT add to `GovernanceEvidenceReceipt`.
- The two new fields must NOT enable reinjection.
- The existing CDH-H fields must remain unchanged.
- `canReinject` binding must remain `false`.
- If `audit-memory-receipt.ts` is at or near the GC-023 line threshold,
  extract the two new fields to a `task-memory-readout.ts` helper and
  import it.

### S-06 — Write unit tests

Create tests under `CVF_LEARNING_PLANE_FOUNDATION/src/task-memory/__tests__/`:

- `task-memory-store.test.ts`:
  - `set()` and `get()` round-trip PASS.
  - Expired entry returns `undefined` from `get()`.
  - `list()` filters expired entries.
  - `delete()` removes entry.
  - `clear()` empties the store.
  - No I/O call is made (no `fs`, no `fetch`).

Update the existing `audit-memory-receipt` test file to cover the two
new fields:

- `taskMemoryDecision` is `'CAPTURED'` when entry is present.
- `taskMemoryDecision` is `'SKIPPED'` when no entry.
- `taskMemoryDecision` is `'EXPIRED'` when entry is expired.
- `canReinject` remains `false` (CDH-H regression check).
- CDH-H fields are unchanged (regression check).

All tests must PASS.

### S-07 — TypeScript check

Run `npm run build` or equivalent TypeScript check for `cvf-web`. Must
complete without errors. Also run TypeScript check for
`CVF_LEARNING_PLANE_FOUNDATION` if a check command exists.

### S-08 — Governance hook chain

Run:

```bash
python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce
python governance/compat/check_governed_file_size.py --enforce
```

Both must report COMPLIANT.

### S-09 — File completion review

Create
`docs/reviews/CVF_T5_RUNTIME_MEMORY_WIRING_COMPLETION_2026-05-22.md`
including:

- Memory class FULL_RECORD, status `CLOSED_T5_RUNTIME_MEMORY_WIRING`.
- Override decision recorded: `new_memory_tiers_beyond_lane_h_scope`
  GRANTED (bounded ephemeral scope).
- Evidence trace: test output, TypeScript check output, hook chain
  results.
- Confirmation that `GovernanceEvidenceReceipt` is unchanged.
- Confirmation that `canReinject` remains `false`.
- Confirmation that CDH-H fields are unchanged.
- Findings per acceptance criterion.
- Claim boundary (ephemeral in-process only; no durable persistence
  claim).

### S-10 — Update active session and commit

Update in this order:

1. `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` — update T5 entry status to
   `CLOSED_T5_RUNTIME_MEMORY_WIRING` with `completionPath` and
   `baselinePath`.
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json` — add `t5RuntimeMemoryWiring`
   field with closure summary; update `lastUpdated`; do not change
   `currentMode` or `freezePosture`.
3. `AGENT_HANDOFF_V11_2026-05-21.md` — append GC-020 sync entry.

Commit:

```text
feat(t5): close runtime memory wiring — ephemeral task store + readout extension

Authority: docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md
GC-018: docs/baselines/CVF_GC018_T5_RUNTIME_MEMORY_WIRING_2026-05-22.md
Completion: docs/reviews/CVF_T5_RUNTIME_MEMORY_WIRING_COMPLETION_2026-05-22.md

Closes T5 from the Review-CVF pain-point delivery gap roadmap V2:
- CVF_MEMORY_TIER_RETENTION_POLICY.md (ephemeral tier defined + bounded)
- Ephemeral in-memory task store (no I/O, lost on process exit by design)
- audit-memory-receipt.ts extended: taskMemoryDecision + taskMemoryReason
- CDH-H fields unchanged; canReinject=false confirmed
- Unit tests PASS; TypeScript check PASS

Blocked-work override: new_memory_tiers_beyond_lane_h_scope (bounded
to ephemeral in-process tier only).

Boundary: ephemeral in-memory only. No durable persistence, no file
write, no database, no external store. GovernanceEvidenceReceipt
unchanged.
```

---

## Evidence Requirements

Every closure claim must be backed by:

- T4 completion review path and status.
- GC-018 override decision record.
- Test output (all new + regression tests PASS).
- TypeScript check output (no errors).
- Hook chain COMPLIANT output.
- `GovernanceEvidenceReceipt` field count before and after (must be
  equal — no new receipt fields added in T5).
- Confirmation that `canReinject` is `false` after the edit.
- Confirmation that CDH-H field names are unchanged.
- Closure commit SHA.

---

## Acceptance Criteria

Closure requires **all** of:

1. T4 pre-condition confirmed.
2. GC-018 filed with `new_memory_tiers_beyond_lane_h_scope` override
   GRANTED and bounded scope documented.
3. Retention policy contract filed with tier taxonomy and bounded
   ephemeral-only scope for T5.
4. Task memory store authored (in-memory only, no I/O).
5. `get()` returns `undefined` for expired entries.
6. `audit-memory-receipt.ts` extended with `taskMemoryDecision` and
   `taskMemoryReason` — and no other change.
7. `GovernanceEvidenceReceipt` shape unchanged (zero diff on `types.ts`).
8. `canReinject` remains `false` (CDH-H regression check PASS).
9. CDH-H fields unchanged (regression check PASS).
10. All unit tests authored and PASS.
11. TypeScript check: no errors.
12. No file outside write ownership modified.
13. Markdown structural completeness: COMPLIANT.
14. File size guard: COMPLIANT.
15. Local governance hook chain: PASS.
16. Completion review filed with all required sections.
17. Active queue, state, and handoff updated with closure SHA.

---

## Review Gate

Before commit, Codex acting in Reviewer role must confirm:

1. Override decision in GC-018 matches implementation (ephemeral in-memory
   only; no I/O in the store implementation).
2. `GovernanceEvidenceReceipt` is unchanged (diff of `types.ts` is
   zero lines).
3. `canReinject` is still `false` in `audit-memory-receipt.ts`.
4. CDH-H fields (`writesRequireReceipt`, `privacyFilters`,
   `memoryReceiptDecision`, `memoryCaptureMode`, `memoryCaptureReason`)
   are unchanged.
5. No route file was modified.
6. No provider adapter or `CVF_MODEL_GATEWAY/` file was modified.
7. No `fs`, `fetch`, or database import in the task memory store.
8. All tests PASS with zero failures.
9. No active-session blocked-work class other than
   `new_memory_tiers_beyond_lane_h_scope` is touched.

---

## Closure Checklist

- [ ] T4 pre-condition confirmed.
- [ ] GC-018 filed with bounded override GRANTED.
- [ ] Retention policy contract filed.
- [ ] Task memory store authored (no I/O).
- [ ] Expiry check in `get()` and `list()` working correctly.
- [ ] `audit-memory-receipt.ts` extended with `taskMemoryDecision` +
      `taskMemoryReason` only.
- [ ] `GovernanceEvidenceReceipt` unchanged (zero diff on `types.ts`).
- [ ] `canReinject=false` confirmed (CDH-H regression).
- [ ] CDH-H fields confirmed unchanged (regression).
- [ ] All unit tests authored and PASS.
- [ ] TypeScript check: no errors.
- [ ] Markdown structural completeness gate: COMPLIANT.
- [ ] Governed file size guard: COMPLIANT.
- [ ] Local governance hook chain pre-commit: PASS.
- [ ] Local governance hook chain pre-push: PASS.
- [ ] Active review queue updated with T5 closure status.
- [ ] Active session state updated with `t5RuntimeMemoryWiring` field.
- [ ] Handoff updated with GC-020 sync entry and closure SHA.
- [ ] Completion review filed at the expected path with all required
      sections.

---

## Operator Checkpoint

**This work order has one mandatory Operator Checkpoint.**

Before the Orchestrator proceeds past S-02 (GC-018), the operator must
explicitly confirm the `new_memory_tiers_beyond_lane_h_scope` override:

- Confirmation must name the bounded scope: ephemeral in-memory only;
  no durable persistence; no file write; no database; no external store;
  memory lost on process exit by design.
- Generic confirmation ("proceed") is not sufficient.
- The GC-018 must record the operator's confirmation statement verbatim.
- The override does NOT authorize durable persistence in any form.
  Any durable persistence requires a separate GC-018 with a separate
  blocked-work override.

If T5 encounters a Return-to-Orchestrator condition, the operator must
be consulted before the work order is reopened.

---

## Return-to-Orchestrator Conditions

Return this work order to the Orchestrator (do not close) if **any**:

- T4 is not closed when T5 begins.
- Operator does not confirm `new_memory_tiers_beyond_lane_h_scope`
  override before GC-018 is filed.
- `CVF_LEARNING_PLANE_FOUNDATION` does not exist as an active extension
  directory.
- `audit-memory-receipt.ts` is at or near GC-023 threshold and the
  extension would exceed it, and no exception registry entry exists.
- Any acceptance criterion fails and the cause is unclear within
  bounded debug time.
- Any implementation step would require a file write, database call, or
  external HTTP call from the task memory store.
- Any out-of-scope file change would be necessary to make T5 close.

When returning, file a return note at
`docs/reviews/CVF_T5_RUNTIME_MEMORY_WIRING_RETURN_2026-05-22.md`.

---

## Forbidden Patterns (Anti-Pattern Guardrails from V2)

T5 closure must not occur via any of:

- **Closure by rejection.** T5 cannot close by arguing memory hierarchy
  is already addressed by CDH-H.
- **Closure by scope redefinition.** T5 cannot close by classifying the
  ephemeral store as "out of scope for this tranche."
- **Closure by contract-only.** T5 cannot close by delivering only the
  retention policy without the task store and audit-memory extension.
- **Implicit scope inflation.** T5 cannot quietly add durable persistence
  or an archive tier without a fresh GC-018 amendment.
- **Persistence via `taskMemoryDecision` CAPTURED state.** The
  `CAPTURED` state describes that an in-memory entry was present at
  readout time, not that the entry is persisted. No closure review may
  describe `CAPTURED` as implying durability.

---

## Claim Boundary

This work order authorizes only:

- The retention policy contract (ephemeral tier boundary).
- The ephemeral in-memory task store.
- The `taskMemoryDecision` and `taskMemoryReason` audit-memory readout
  extension.
- Unit tests, GC-018 baseline, completion review, and active-session
  updates.

It does not authorize any durable persistence, file-backed storage,
database implementation, external memory service, new receipt envelope
field, new provider adapter, UI change, live provider call, public-sync
update, release claim, freeze lift, or any
Maika/child-data/photo/vision claim.
