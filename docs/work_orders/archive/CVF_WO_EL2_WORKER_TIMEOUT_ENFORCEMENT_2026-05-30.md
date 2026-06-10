# CVF Work Order — EL-2 Worker Timeout Enforcement

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-30

---

## Purpose

Wire `handleWorkerTimeout()` from `pipeline-chain-orchestrator.ts` into the
`/api/execute` route as an additive `workerTimeoutReadout` field. When elapsed
execution time exceeds `WORKER_TIMEOUT_DEFAULT_MS` (300s), the readout surfaces
the timeout advisory with retry count, next action, and escalation flag.

Contract version: `cvf.workerTimeoutEnforcement.el2.v1`

Pattern: same additive readout approach as D1 `pipelineChainReadout`.

**Critical constraint:** `route.ts` is at 999 lines (hard limit 1000).
Implementation must extract a `worker-timeout-handler.ts` helper module.
`route.ts` must end with the same or fewer lines.

## Authority Chain

- EL-2/EL-3 roadmap: `docs/roadmaps/CVF_EL2_EL3_EXECUTION_LAYER_ENFORCEMENT_ROADMAP_2026-05-30.md`
- EL-2/EL-3 GC-018: `docs/baselines/CVF_GC018_EL2_EL3_EXECUTION_LAYER_ENFORCEMENT_2026-05-30.md`
- EL-1 completion (gate): `docs/reviews/CVF_DELTA_D1_PIPELINE_CHAIN_READOUT_COMPLETION_2026-05-29.md`
- pipeline-chain-orchestrator.ts:
  - `handleWorkerTimeout()` line 348
  - `WORKER_TIMEOUT_DEFAULT_MS = 300_000` line 325
  - `WORKER_TIMEOUT_MAX_RETRIES = 2` line 326
  - `WorkerTimeoutResult` line 328
- route.ts: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
  — 999 lines at near-hard limit

## Scope

**Allowed:**
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/worker-timeout-handler.ts` (new)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` (additive field + import; net-zero lines)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.worker-timeout-handler.test.ts` (new)
- `docs/reviews/CVF_EL2_FAST_LANE_AUDIT_2026-05-30.md` (new)
- `docs/reviews/CVF_EL2_WORKER_TIMEOUT_ENFORCEMENT_COMPLETION_2026-05-30.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** MCP server files, new receipt envelope schema, public-sync, process killing, sandboxed execution.

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `handleWorkerTimeout()` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` | line 348 | `handleWorkerTimeout` | `pipeline-chain-orchestrator.ts` | ACCEPT |
| `WORKER_TIMEOUT_DEFAULT_MS` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` | line 325 | `WORKER_TIMEOUT_DEFAULT_MS` | `pipeline-chain-orchestrator.ts` | ACCEPT |
| `WORKER_TIMEOUT_MAX_RETRIES` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` | line 326 | `WORKER_TIMEOUT_MAX_RETRIES` | `pipeline-chain-orchestrator.ts` | ACCEPT |
| `WorkerTimeoutResult` interface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` | line 328 | `WorkerTimeoutResult` | `pipeline-chain-orchestrator.ts` | ACCEPT |
| `route.ts` near hard limit | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | file root | `route.ts` | route handler | ACCEPT |
| EL-1 D1 gate | `docs/reviews/CVF_DELTA_D1_PIPELINE_CHAIN_READOUT_COMPLETION_2026-05-29.md` | Status field | `CLOSED_PASS_BOUNDED` | D1 completion | ACCEPT |

New fields:

| New field | Derived from | Runtime claim blocked? |
| --- | --- | --- |
| `workerTimeoutReadout.contractVersion` | `cvf.workerTimeoutEnforcement.el2.v1` | Yes — advisory readout only |
| `workerTimeoutReadout.triggered` | `elapsedMs >= WORKER_TIMEOUT_DEFAULT_MS` | Yes |
| `workerTimeoutReadout.retryCount` | `WorkerTimeoutResult.retryCount` | Yes |
| `workerTimeoutReadout.nextAction` | `WorkerTimeoutResult.nextAction` | Yes |
| `workerTimeoutReadout.escalateToOrchestrator` | `WorkerTimeoutResult.escalateToOrchestrator` | Yes |
| `workerTimeoutReadout.runtimeExecutionAuthorized` | literal `false` | Yes — invariant |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| `workerTimeoutReadout` in response | Scope + Implementation | `worker-timeout-handler.ts` + route | field present in response | PASS |
| `route.ts` net-zero lines | Pre-Flight | route.ts line count | `wc -l` check | PASS |
| `runtimeExecutionAuthorized=false` | New fields table | readout field | grep check | PASS |
| Tests PASS | Scope | `route.worker-timeout-handler.test.ts` | `npm run test:run` | PASS |
| EL-1 D1 gate | Authority Chain | D1 completion | CLOSED_PASS_BOUNDED | PASS |

## Agent Roles

Implementer: create `worker-timeout-handler.ts`, update `route.ts`, write tests.
Reviewer: verify `route.ts` line count net-zero; `runtimeExecutionAuthorized=false` explicit; tests PASS.
Auditor: verify EL-1 D1 gate satisfied; live proof receipt captured.
No self-review.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` — confirm `handleWorkerTimeout()` at line 348
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` — confirm current line count is 999
5. `docs/reviews/CVF_DELTA_D1_PIPELINE_CHAIN_READOUT_COMPLETION_2026-05-29.md` — confirm D1 CLOSED_PASS

## Write Ownership

Implementer owns all new and modified files. Only files in Allowed list may be touched.

## Execution Plan

1. Read all required first reads; confirm D1 CLOSED_PASS gate.
2. Identify extraction candidate in `route.ts` to maintain net-zero lines.
3. Create `worker-timeout-handler.ts` with `buildWorkerTimeoutReadout()`.
4. Add import + field to `route.ts`; verify line count ≤ 1000.
5. Write tests; run `npm run test:run` — all PASS.
6. Run `npm run check` (TypeScript).
7. Run live proof via Alibaba qwen-turbo; capture receipt.
8. Run governance gates with `--base 0d1bdbef`.
9. Update session continuity; commit.
10. Write Fast Lane audit + completion review.

## Evidence Requirements

- `worker-timeout-handler.ts` created; exports `buildWorkerTimeoutReadout()`
- `route.ts` final line count ≤ 1000
- `workerTimeoutReadout` field in `/api/execute` response
- `runtimeExecutionAuthorized: false` in readout
- All tests PASS; TypeScript PASS
- Live proof receipt from Alibaba qwen-turbo

## Acceptance Criteria

- [x] `worker-timeout-handler.ts` created with `buildWorkerTimeoutReadout()`
- [x] `route.ts` ≤ 1000 lines
- [x] `workerTimeoutReadout` in response with all required fields
- [x] `runtimeExecutionAuthorized: false` explicit
- [x] Tests PASS; TypeScript PASS
- [x] Live proof receipt captured
- [x] EL-3 gate answer in completion review

## Fail Conditions

- `route.ts` line count exceeds 1000 after change
- Process or provider cancellation added (not in scope)
- Tests fail

## Review Gate

`route.ts` ≤ 1000 lines; `workerTimeoutReadout` present; `runtimeExecutionAuthorized=false`; tests PASS; TypeScript PASS; live receipt.

## Operator Checkpoint

operator.checkpoint.waiver: Operator authorized EL-2 directly 2026-05-30.

## Implementation Design

### `worker-timeout-handler.ts`

```typescript
// Advisory readout only — does not kill processes or cancel providers.
import {
  handleWorkerTimeout,
  WORKER_TIMEOUT_DEFAULT_MS,
  type PipelineChainState,
  type WorkerTimeoutResult,
} from './pipeline-chain-orchestrator';

export const WORKER_TIMEOUT_READOUT_VERSION =
  'cvf.workerTimeoutEnforcement.el2.v1' as const;

export interface WorkerTimeoutReadout {
  contractVersion: typeof WORKER_TIMEOUT_READOUT_VERSION;
  triggered: boolean;
  retryCount: number;
  nextAction: 'retry' | 'escalate' | 'stop' | 'not_triggered';
  escalateToOrchestrator: boolean;
  runtimeExecutionAuthorized: false;
}

export function buildWorkerTimeoutReadout(
  state: PipelineChainState,
  elapsedMs: number,
): WorkerTimeoutReadout {
  if (elapsedMs < WORKER_TIMEOUT_DEFAULT_MS) {
    return {
      contractVersion: WORKER_TIMEOUT_READOUT_VERSION,
      triggered: false,
      retryCount: state.workerRetryCount,
      nextAction: 'not_triggered',
      escalateToOrchestrator: false,
      runtimeExecutionAuthorized: false,
    };
  }
  const result: WorkerTimeoutResult = handleWorkerTimeout(state, elapsedMs);
  return {
    contractVersion: WORKER_TIMEOUT_READOUT_VERSION,
    triggered: true,
    retryCount: result.retryCount,
    nextAction: result.nextAction,
    escalateToOrchestrator: result.escalateToOrchestrator,
    runtimeExecutionAuthorized: false,
  };
}
```

### `route.ts` change

Add 1 import + 1 call + 1 field. Extract equivalent lines from existing
response object to maintain net-zero. Use `routeStartedAtMs` (already tracked)
to compute `elapsedMs = Date.now() - routeStartedAtMs`.

## Pre-Flight

- [x] EL-1 D1 CLOSED_PASS confirmed
- [x] `handleWorkerTimeout()` confirmed at pipeline-chain-orchestrator.ts line 348
- [x] `WORKER_TIMEOUT_DEFAULT_MS` confirmed at line 325
- [x] `WorkerTimeoutResult` confirmed at line 328
- [x] `routeStartedAtMs` exists in route.ts (already tracked at line 45)
- [x] route.ts current line count confirmed as 999
- [x] Extraction candidate identified (lines to remove to offset new import + call + field)

## Closure Checklist

- [x] `worker-timeout-handler.ts` created with `buildWorkerTimeoutReadout()`
- [x] `route.ts` ≤ 1000 lines after change
- [x] `workerTimeoutReadout` in response with all required fields
- [x] `runtimeExecutionAuthorized=false` invariant
- [x] Tests PASS; TypeScript PASS
- [x] Live proof receipt
- [x] Fast Lane audit PASS
- [x] Session continuity updated
- [x] EL-3 gate answer in completion review

## Return-To-Orchestrator Conditions

Stop if: `route.ts` would exceed 1000 lines with no extraction candidate;
`WorkerTimeoutResult` type cannot be imported cleanly; TypeScript errors.

## EL-3 Gate Output

**Expected YES:** EL-2 timeout readout exists. EL-3 can now add reviewer
deadlock detection using `handleReviewDeadlock()` — same additive pattern.

## Claim Boundary

EL-2 adds an advisory timeout readout field. It does not claim actual process
killing, automatic worker restart, live provider cancellation, production
readiness, or hosted readiness.
