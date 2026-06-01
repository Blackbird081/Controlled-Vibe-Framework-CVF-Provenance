# CVF Work Order - MKG7-T5 Memory Durable Write Readiness

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

docType: work_order

Date: 2026-06-01

## Purpose

Add a bounded read-readiness surface over the existing durable store and pin its
already-fail-closed write behavior with regression tests. The durable store
already exists with write fail-closed at `!actorAuthorized || policyDecision !==
"allow"` (line 201) and read auth-required at `!actorAuthorized` (line 312).
T5 does NOT change these semantics — it wraps them with a readiness helper and
proves them with tests. `durable-memory-store.ts` must not be modified.

Success: new readiness helper returns summary-only read result, regression tests
pin all deny-branches, zero edits to `durable-memory-store.ts`, LPF TypeScript
check PASS, file-size guard PASS, pending and uncommitted.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-01 dispatch MKG7 T2–T7 for worker execution | ACCEPT |
| MKG7-T5 GC-018 | `docs/baselines/CVF_GC018_MKG7_T5_MEMORY_DURABLE_WRITE_READINESS_2026-06-01.md` | ACCEPT |
| MKG7 roadmap | `docs/roadmaps/CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md` | ACCEPT |
| T1 contract | `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | ACCEPT |
| Worker autonomy standard | `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch and review pending output | no silent scope expansion |
| Worker | implement readiness helper + regression tests | no edits to `durable-memory-store.ts`, no commit |
| Reviewer | verify zero edits to store, deny-branches pinned, new write path absent | reject if store modified |

## Scope

Allowed scope:

- create `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-durable-readiness.ts`;
- create `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-durable-readiness.test.ts`;
- create `docs/reviews/CVF_MKG7_T5_MEMORY_DURABLE_WRITE_READINESS_COMPLETION_2026-06-01.md`.

Forbidden scope:

- any edit to `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`;
- any new write path authorized for routes;
- any edit to `index.ts`;
- route changes, provider calls, live proof, public-sync, push, or commit.

Risk ceiling: R1 — additive readiness layer.

## Required First Reads

- `docs/baselines/CVF_GC018_MKG7_T5_MEMORY_DURABLE_WRITE_READINESS_2026-06-01.md`
- `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` — understand fail-closed write branch (line 201) and read auth branch (line 312); must not be modified

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 5e55714d --head HEAD
python governance/compat/check_governed_file_size.py --enforce
```

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Write fail-closed branch | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 201 | `write` | `InProcessDurableMemoryStore` | ACCEPT |
| Write auth condition | LITERAL_INVARIANT | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 201 | `actorAuthorized` | write method | ACCEPT |
| Provenance floor | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 98 | `MIN_PROVENANCE_SCORE` | durable store | ACCEPT |
| Read auth branch | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 312 | `read` | `InProcessDurableMemoryStore` | ACCEPT |
| Receipt summaryOnly invariant | LITERAL_INVARIANT | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | `DurableMemoryReceipt` | `summaryOnly` | receipt | ACCEPT |
| `DurableMemoryStore` interface | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 89 | `DurableMemoryStore` | store interface | ACCEPT |
| `createInProcessDurableMemoryStore` | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 100 | `createInProcessDurableMemoryStore` | factory | ACCEPT |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Read-readiness surface (summary-only) | Execution Plan step 2 | `readMemory()` in readiness helper | focused test | DISPATCHED |
| Pin write deny-branches | Execution Plan step 3 | regression tests | 3+ deny-scenario tests | DISPATCHED |
| Zero edits to durable store | Forbidden scope | `durable-memory-store.ts` unmodified | `git diff --name-status` | DISPATCHED |
| Receipt invariants preserved | Proof Manifest | `summaryOnly`, `canReinject`, `rawMemoryReleased` | focused test | DISPATCHED |

## 6C. Worker Autonomy / No-Question Rule

Proceed autonomously. Ask only for scope expansion, forbidden-path edits, live
proof, secrets, push, commit, or destructive actions.

## 6D. Pending Artifact Evidence Finality

Do not commit. Record actual `git status --short`. Do not cite committed-only
or empty range as proof.

## 6G. Work-Order Fulfillment Manifest

### Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-durable-readiness.ts` | Yes | bounded read-readiness helper |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-durable-readiness.test.ts` | Yes | regression tests |
| `docs/reviews/CVF_MKG7_T5_MEMORY_DURABLE_WRITE_READINESS_COMPLETION_2026-06-01.md` | Yes | pending completion review |

### Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | must not be modified — fail-closed semantics must remain unchanged |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts` | must not expand root barrel |

### Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| Write deny: unauthorized | test file | `actorAuthorized` | Yes |
| Write deny: provenance floor | test file | `MIN_PROVENANCE_SCORE` | Yes |
| Read deny: unauthorized | test file | `durable_memory_policy_denied` | Yes |
| Receipt invariants | test file | `summaryOnly` | Yes |

## 7. Write Ownership

Owned: `memory-durable-readiness.ts`, test file, completion review.
Forbidden: `durable-memory-store.ts`, `index.ts`.

## 8. Execution Plan

1. Capture `baseHead` and git status. Run pre-flight gate.
2. Create `memory-durable-readiness.ts` with:
   - `readMemory(store: DurableMemoryStore, input: DurableMemoryReadInput)` — calls `store.read()`, returns summary-only records (no raw content), receipt;
   - explicit statement that `store.write()` exists and is fail-closed; readiness helper does not bypass it.
3. Create regression tests using `createInProcessDurableMemoryStore`:
   - write denied when `actorAuthorized=false`;
   - write denied when `policyDecision !== "allow"`;
   - write denied when `provenanceScore < 0.7`;
   - read denied when `actorAuthorized=false`;
   - read allowed when authorized + valid tier — verify receipt `summaryOnly:true`, `canReinject:false`, `rawMemoryReleased:false`.
4. Run `npm run check` from LPF. Run file-size guard.
5. Create pending completion review.
6. Leave all files pending and uncommitted.

## Evidence Requirements

- `npm run check` from LPF — PASS;
- file-size guard PASS;
- `git diff --name-status` — zero edits to `durable-memory-store.ts`;
- actual `git status --short`.

## 10. Acceptance Criteria

- [ ] `memory-durable-readiness.ts` exists with summary-only `readMemory()` helper
- [ ] Tests cover all 3 write-deny scenarios and read-deny + read-allow
- [ ] Receipt invariants asserted: `summaryOnly:true`, `canReinject:false`, `rawMemoryReleased:false`
- [ ] `durable-memory-store.ts` zero edits (verified with `git diff`)
- [ ] LPF `npm run check` PASS
- [ ] File-size guard PASS

Fail conditions:

- [ ] Any edit to `durable-memory-store.ts`
- [ ] New write path added that bypasses the existing deny-branch
- [ ] Worker commits or asks whether to fix an allowed-scope failure

## 11. Review Gate

Pre-implementation autorun gate must pass before edits. Closure (by
orchestrator) requires reviewer no-blocking objection and `pre-closure` gate.
A gate failure inside Allowed scope is authorization to repair and rerun.

## 12. Closure Checklist

N/A: worker must not close or commit T5. Return pending files for orchestrator.

## 13. Return-To-Orchestrator Conditions

Return if: pre-flight fails outside the work order's scope; any modification
to `durable-memory-store.ts` would be required; a forbidden-path edit is
required to complete the task.

## Operator Checkpoint

This tranche was authorized and dispatched on 2026-06-01 as part of the MKG7
full-wave dispatch. T5 is ready to execute; `durable-memory-store.ts` is the
primary source authority (read-only).

## Worker Dispatch Prompt

```text
You are assigned MKG7-T5 Memory Durable Write Readiness.

Primary work order:
docs/work_orders/CVF_WO_MKG7_T5_MEMORY_DURABLE_WRITE_READINESS_2026-06-01.md

Critical rules:
- create memory-durable-readiness.ts that wraps existing DurableMemoryStore.read();
- do NOT modify durable-memory-store.ts — it is a forbidden-touch source;
- write regression tests using createInProcessDurableMemoryStore():
  write denied (unauthorized), write denied (policyDecision != allow),
  write denied (provenance < 0.7), read denied (unauthorized),
  read allowed (verify summaryOnly:true, canReinject:false, rawMemoryReleased:false);
- run LPF npm run check and file-size guard.

Worker Autonomy Rule: repair allowed-scope failures and rerun without asking.
Pending Artifact Rule: do not commit; record actual git status.
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

T5 authorizes a bounded readiness layer and regression tests only. No new write
paths, route integration, mutations to `durable-memory-store.ts`, provider
calls, public-sync, or push.
