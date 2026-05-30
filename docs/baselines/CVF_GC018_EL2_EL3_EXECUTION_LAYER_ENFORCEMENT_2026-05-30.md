# CVF GC-018 — EL-2/EL-3 Execution Layer Enforcement

Memory class: FULL_RECORD

Status: ACTIVE

docType: gc018_baseline

Date: 2026-05-30

---

## Purpose

Authorize EL-2 (Worker Timeout Enforcement) and EL-3 (Reviewer Deadlock
Escalation) — the next two Execution Layer phases after Delta D1 (EL-1 readout).

EL-1 (D1) wired `PipelineChainState` as a readout in `/api/execute` response.
EL-2 wires `handleWorkerTimeout()` to be called when a worker step exceeds
the 300s threshold. EL-3 wires `handleReviewDeadlock()` when a reviewer rejects
more than 3 times.

---

## Source / Predecessor Evidence

- Delta D1 completion: `docs/reviews/CVF_DELTA_D1_PIPELINE_CHAIN_READOUT_COMPLETION_2026-05-29.md` — CLOSED_PASS_BOUNDED
- pipeline-chain-orchestrator.ts: `handleWorkerTimeout()` line 348, `handleReviewDeadlock()` line 419
- D1 `pipelineChainReadout` proves types are importable; EL-2/EL-3 extend the same pattern

## Decision / Baseline

Decision: proceed with EL-2 (Worker Timeout Enforcement) as WORK_ORDER_READY
and EL-3 (Reviewer Deadlock Escalation) as HOLD_UNTIL_EL2_PASS. Both use the
additive readout pattern from D1. `route.ts` is at 999 lines (hard limit 1000);
each tranche must extract a helper module to maintain net-zero.

Proposed tranches: EL-2 `workerTimeoutReadout` + EL-3 `reviewerDeadlockReadout`.

## Evidence / Verification

Before closure of each tranche:
- Helper module created (`worker-timeout-handler.ts` / `reviewer-deadlock-handler.ts`)
- `route.ts` ≤ 1000 lines after change
- `runtimeExecutionAuthorized=false` explicit in readout
- Tests PASS; TypeScript PASS; live proof receipt

## Authorization Basis

- Delta D1 completion: `docs/reviews/CVF_DELTA_D1_PIPELINE_CHAIN_READOUT_COMPLETION_2026-05-29.md`
  — Status: CLOSED_PASS_BOUNDED; EL-1 contract `cvf.pipelineChainReadout.delta.d1.v1`
- EL-1 source: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts`
  — `handleWorkerTimeout()` at line 348; `handleReviewDeadlock()` at line 419
  — `WORKER_TIMEOUT_DEFAULT_MS = 300_000` at line 325
  — `REVIEW_DEADLOCK_MAX_RETRIES = 3` at line 395
  — `WorkerTimeoutResult` at line 328; `ReviewDeadlockResult` at line 397
- Operator authorization: operator direction 2026-05-30
- Risk: R2 — runtime enforcement wiring into execute route

---

## Verified Gap

At HEAD `0d1bdbef` (Delta D2/D3 commit):

| Component | Expected | Actual |
| --- | --- | --- |
| `handleWorkerTimeout()` | Called when worker exceeds 300s | Contract + types only; never called in route |
| `handleReviewDeadlock()` | Called after 3 reviewer rejections | Contract + types only; never called in route |
| `workerRetryCount` | Incremented and checked in route | Only visible in `pipelineChainReadout` — no enforcement |
| `reviewerRetryCount` | Incremented and checked in route | Only visible in `pipelineChainReadout` — no enforcement |

---

## Scope — Two Phases

### EL-2 (WORK_ORDER_READY) — Worker Timeout Enforcement

Wire `handleWorkerTimeout()` into the execute route — when a worker step
exceeds `WORKER_TIMEOUT_DEFAULT_MS` (300s), call `handleWorkerTimeout()`,
increment `workerRetryCount`, and return a structured timeout response.
Advisory only — no actual process kill in this phase.

Allowed: new `worker-timeout-handler.ts` + route additive field + tests.
Forbidden: sandboxed process execution, public-sync, new receipt envelope.

### EL-3 (DEMAND_GATED after EL-2) — Reviewer Deadlock Escalation

Wire `handleReviewDeadlock()` when `reviewerRetryCount > REVIEW_DEADLOCK_MAX_RETRIES`.
Returns decomposed work orders or `HumanInterventionRequired` signal.

Gate: EL-2 CLOSED_PASS.

---

## Critical Constraint

`route.ts` is at 999 lines (after D1 delta). Hard limit 1000.
EL-2 implementation MUST extract a helper module — net-zero or shrink `route.ts`.

---

## Claim Boundary

EL-2/EL-3 implement timeout detection and deadlock detection advisory logic.
They do not claim: sandboxed process kill, automatic worker restart, live
provider cancellation, production readiness, or hosted readiness.
