# CVF EL-2/EL-3 Execution Layer Enforcement Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-05-30

---

## Authorization / Decision

Authorized by operator direction 2026-05-30. Continues the Execution Layer
pipeline after Delta D1 (EL-1 readout, D2 write tools, D3 CLI bridge).

Fresh GC-018:
`docs/baselines/CVF_GC018_EL2_EL3_EXECUTION_LAYER_ENFORCEMENT_2026-05-30.md`

Dispatch status:
EL-2 CLOSED_PASS_BOUNDED.
EL-3 CLOSED_PASS_BOUNDED.

## Purpose

Delta D1 added `pipelineChainReadout` — Orchestrators can see `workerRetryCount`
and `reviewerRetryCount`. But seeing them is not enforcing them.

EL-2 adds enforcement: if a worker step exceeds `WORKER_TIMEOUT_DEFAULT_MS`
(300s), `handleWorkerTimeout()` is called and the response carries a structured
timeout advisory. After `WORKER_TIMEOUT_MAX_RETRIES` (2), escalate to Orchestrator.

EL-3 adds enforcement: if `reviewerRetryCount > REVIEW_DEADLOCK_MAX_RETRIES` (3),
`handleReviewDeadlock()` decomposes work orders or emits `HumanInterventionRequired`.

## Scope / Target / Owner Boundary

Target: `/api/execute` route + new helper modules.
No sandboxed process execution, no automatic process kill, no public-sync.

**Critical constraint:** `route.ts` is at 999 lines (hard limit 1000).
Each tranche MUST extract a helper module — net-zero or shrink route.ts.

## Scope

Target: `/api/execute` route and two new helper modules in `cvf-web/src/lib/`.
Owner: CVF execution surface (route.ts + pipeline-chain-orchestrator.ts).
No MCP server change, no public-sync, no sandboxed process execution.

## Verification

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 0d1bdbef --head <el2-commit> --enforce
```

TypeScript: `npm run check` in cvf-web.
Tests: `npm run test:run` in cvf-web.
Live proof: HTTP POST to `/api/execute`; capture receipt showing `workerTimeoutReadout` (EL-2) or `reviewerDeadlockReadout` (EL-3) field.
Route line count: `wc -l route.ts` must be ≤ 1000 after each tranche.

## Authority Chain

- GC-018: `docs/baselines/CVF_GC018_EL2_EL3_EXECUTION_LAYER_ENFORCEMENT_2026-05-30.md`
- EL-1 completion: `docs/reviews/CVF_DELTA_D1_PIPELINE_CHAIN_READOUT_COMPLETION_2026-05-29.md`
- pipeline-chain-orchestrator.ts:
  - `handleWorkerTimeout()` line 348
  - `WORKER_TIMEOUT_DEFAULT_MS` line 325
  - `WORKER_TIMEOUT_MAX_RETRIES` line 326
  - `handleReviewDeadlock()` line 419
  - `REVIEW_DEADLOCK_MAX_RETRIES` line 395
  - `WorkerTimeoutResult` line 328
  - `ReviewDeadlockResult` line 397

---

## EL-2 — Worker Timeout Enforcement

**Risk:** R2 — runtime enforcement wiring.

**Gap:** `handleWorkerTimeout()` exists with full logic (retry/escalate/stop)
but is never called in the execute route. Workers can exceed 300s with no
governance response.

**Deliverables:**

1. New module: `cvf-web/src/lib/worker-timeout-handler.ts`
   — imports `handleWorkerTimeout`, `WORKER_TIMEOUT_DEFAULT_MS`, `WorkerTimeoutResult`
   — `buildWorkerTimeoutReadout(state, elapsedMs)` — calls `handleWorkerTimeout()` when `elapsedMs >= WORKER_TIMEOUT_DEFAULT_MS`
   — returns `WorkerTimeoutReadout` with: `contractVersion`, `triggered`, `nextAction`, `retryCount`, `escalateToOrchestrator`, `runtimeExecutionAuthorized: false`
2. `route.ts`: import + additive `workerTimeoutReadout` field (net-zero via extraction)
3. New tests: `route.worker-timeout-handler.test.ts`
4. Live proof via provider call with timing

**Contract version:** `cvf.workerTimeoutEnforcement.el2.v1`

---

## EL-3 — Reviewer Deadlock Escalation

**Risk:** R2 — runtime enforcement wiring.

**Status:** CLOSED_PASS_BOUNDED.

**Gap:** `handleReviewDeadlock()` exists but is never called. After 3 reviewer
rejections there is no CVF-governed decomposition or escalation.

**Deliverables (after EL-2):**

1. New module: `cvf-web/src/lib/reviewer-deadlock-handler.ts`
   — imports `handleReviewDeadlock`, `REVIEW_DEADLOCK_MAX_RETRIES`, `ReviewDeadlockResult`
   — `buildReviewerDeadlockReadout(state, workOrderId)` — calls `handleReviewDeadlock()` when `reviewerRetryCount > REVIEW_DEADLOCK_MAX_RETRIES`
   — returns `ReviewerDeadlockReadout` with: `contractVersion`, `triggered`, `nextAction`, `decomposedWorkOrders?`, `runtimeExecutionAuthorized: false`
2. `route.ts`: import + additive `reviewerDeadlockReadout` field (net-zero)
3. New tests
4. Live proof

**Contract version:** `cvf.reviewerDeadlockEscalation.el3.v1`

---

## Non-Goals

- Sandboxed process kill or automatic worker restart
- Automatic model upgrade on deadlock
- Live provider cancellation
- Public-sync repo changes
- Hosted readiness or production readiness

## Work Plan

| Tranche | Deliverable | Risk | Gate |
| --- | --- | --- | --- |
| EL-2 | Worker Timeout Enforcement readout | R2 | CLOSED_PASS_BOUNDED |
| EL-3 | Reviewer Deadlock Escalation readout | R2 | CLOSED_PASS_BOUNDED |

## Acceptance Criteria

- [x] EL-2: `workerTimeoutReadout` in response when elapsed ≥ 300s; tests PASS; TypeScript PASS; live proof receipt
- [x] EL-3: `reviewerDeadlockReadout` in response when `reviewerRetryCount > 3`; tests PASS; TypeScript PASS; live proof receipt
- [x] `route.ts` ≤ 1000 lines after each tranche
- [x] `runtimeExecutionAuthorized=false` in both readouts

## Public Export Disposition

Disposition: `DEFERRED_PRIVATE_ONLY`
Reason: public-sync currently lacks the matching EL-2/EL-3 runtime source,
tests, completion reviews, and live-proof evidence from this provenance batch.
No public catalog claim is made in this provenance closure.
Public-sync verification: not exported in this batch; public-sync update
requires a separate public-safe export work order.
Next action: open a public-sync batch before adding EL-2/EL-3 execution-layer
claims to the public README or technical catalog.

## Claim Boundary

EL-2/EL-3 implement timeout and deadlock detection advisory readouts. They do
not claim sandboxed process kill, automatic provider cancellation, production
safety, hosted readiness, or public release readiness.
