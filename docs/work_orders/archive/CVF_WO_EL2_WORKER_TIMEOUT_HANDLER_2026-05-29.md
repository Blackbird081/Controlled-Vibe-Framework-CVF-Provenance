# CVF Work Order — EL-2 WorkerTimeout Handler

Memory class: FULL_RECORD

Status: HOLD_UNTIL_EL1_PASS

docType: work_order

Date: 2026-05-29

---

## Purpose

Implement WorkerTimeout detection and recovery bound to the EL-1 pipeline
contract's Worker Execute stage. Produces a live receipt showing timeout
detection, sandbox cleanup, and re-dispatch within the governed pipeline.

Source: CVF 28.05 Gap B — `WorkerTimeoutException` class defined in
`cvf_cli.py` (line 19); recovery logic sketched (lines 104–115: timeout
detection → sandbox clear → restart → re-dispatch). CVF has no equivalent.

## Authority Chain

- EL GC-018: `docs/baselines/CVF_GC018_EXECUTION_LAYER_2026-05-29.md`
- EL Roadmap: `docs/roadmaps/CVF_EXECUTION_LAYER_ROADMAP_2026-05-29.md`
- CVF 28.05: `.private_reference/legacy/CVF 28.05/cvf_cli.py` lines 104–115
- Live run diagnostic standard: `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
- V3 diagnostics: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts`
  — `ExecutionDiagnosticClass`; add `worker_timeout` class here
- **EL-1 gate: `docs/reviews/CVF_EL1_PIPELINE_CHAIN_ORCHESTRATOR_CONTRACT_COMPLETION_2026-05-29.md`
  must be CLOSED_PASS**

## Agent Roles

Implementer adds `worker_timeout` diagnostic class and timeout handler bound
to Worker Execute stage. Reviewer checks: timeout triggers correct diagnostic
class; re-dispatch uses EL-1 contract state machine; max 2 retries before
escalation; live receipt present. No self-review.

## Scope

**Allowed:**

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts`
  — add `worker_timeout` to `ExecutionDiagnosticClass` (bounded edit)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts`
  — add `WorkerTimeoutHandler` implementation
- Corresponding test files
- `docs/evidence/execution-layer/worker-timeout-receipt.md` (new — live proof)
- `docs/reviews/CVF_EL2_WORKER_TIMEOUT_HANDLER_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** New receipt envelope schema, new provider execution semantics,
public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts`
   — existing `ExecutionDiagnosticClass` values at lines 16–38
5. `.private_reference/legacy/CVF 28.05/cvf_cli.py` — timeout recovery lines 104–115
6. `docs/reviews/CVF_EL1_PIPELINE_CHAIN_ORCHESTRATOR_CONTRACT_COMPLETION_2026-05-29.md`
   — confirm EL-1 CLOSED_PASS

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `ExecutionDiagnosticClass` type | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts` | lines 16–38 | `ExecutionDiagnosticClass` | `ExecutionDiagnostic` | ACCEPT |
| CVF 28.05 timeout recovery | canonical-contract: `.private_reference/legacy/CVF 28.05/cvf_cli.py` | lines 104–115 | `WorkerTimeoutException` | `CVFOrchestratorCLI.run_workflow` | ACCEPT |
| Live run diagnostic standard | `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | full document | diagnostic classification | CVF live run standard | ACCEPT |
| EL GC-018 authorization | `docs/baselines/CVF_GC018_EXECUTION_LAYER_2026-05-29.md` | full document | EL-2 authorization | EL GC-018 | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Timeout detection + recovery | Deliverable | TS handler + test | Tests PASS | OPEN |
| `worker_timeout` diagnostic class | Deliverable | diagnostics.ts edit | Class added | OPEN |
| Max 2 retries then escalate | Deliverable | handler logic | Reviewer checks | OPEN |
| Live receipt with timeout evidence | Evidence | receipt `.md` | `evidenceMode=live` | OPEN |
| EL-1 gate confirmed | Authority Chain | EL-1 completion review | Read EL-1 | OPEN |

## Deliverable

- Add `worker_timeout` and `worker_timeout_recovered` to `ExecutionDiagnosticClass`
- Implement `WorkerTimeoutHandler`:
  - Task timeout threshold: 5 minutes (configurable)
  - On timeout: emit `worker_timeout` diagnostic; clear context; restart
  - On recovery: emit `worker_timeout_recovered`; re-dispatch to Worker Execute stage
  - Max retries: 2; after 2 failures → escalate to Orchestrator stage
  - Receipt entry: diagnostic class + retry count + recovery outcome
- Tests: timeout detection (1 test), recovery (1 test), max-retry escalation (1 test)
- Live proof: one governed pipeline call where timeout occurs and recovery succeeds;
  receipt in `docs/evidence/execution-layer/worker-timeout-receipt.md`

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] Gate confirmations checked

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be modified.

## Review Gate

Before committing: all source symbols verified; required evidence present; no forbidden files in diff.

## Return-To-Orchestrator Conditions

Stop if: required gate evidence missing; a cited source file cannot be found; implementing the deliverable requires a forbidden file change.

## Execution Plan

1. Read all required first reads; confirm EL-1 gate.
2. Add `worker_timeout` class to `execution-diagnostics.ts`.
3. Implement `WorkerTimeoutHandler` in pipeline-chain-orchestrator.ts.
4. Write 3 tests; run `npm run test:run`; verify PASS.
5. Make 1 governed pipeline call triggering timeout; capture receipt.
6. Write evidence record.
7. Write completion review.
8. Run governance gates.
9. Update session continuity.
10. Commit.

## Evidence Requirements

- `worker_timeout` diagnostic class added
- Handler with 2-retry max + escalation
- Tests PASS (3 tests)
- Live receipt with `worker_timeout` diagnostic class
- `rawSecretPrinted=false`
- EL-1 gate confirmed

## Acceptance Criteria

- [ ] EL-1 CLOSED_PASS confirmed
- [ ] `worker_timeout` + `worker_timeout_recovered` added to diagnostics
- [ ] `WorkerTimeoutHandler` implemented with 2-retry max
- [ ] Tests PASS
- [ ] Live receipt in evidence file
- [ ] `rawSecretPrinted=false`
- [ ] Session continuity updated

## Closure Checklist

- [ ] EL-1 confirmed
- [ ] Diagnostics extended
- [ ] Handler implemented + tests PASS
- [ ] Live receipt captured
- [ ] Completion review written
- [ ] Governance gates PASS
- [ ] Session continuity updated

## EL-3 Gate Output

EL-3 (ReviewDeadlock) gates on EL-2. After EL-2, the Reviewer stage has
timeout protection; EL-3 adds the retry counter and deadlock escalation.

## Operator Checkpoint

Operator authorized live API key use 2026-05-29.

## Claim Boundary

EL-2 produces a bounded timeout handler. It does not claim broad pipeline
stability, all-provider timeout handling, new receipt envelope schema, hosted
readiness, production readiness, or public release readiness.
