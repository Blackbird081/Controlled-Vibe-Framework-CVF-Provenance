# CVF Agent Work Order - MAO-T6 Timeout, Heartbeat, Cancel, Retry, And Recovery

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MAO-RUNTIME-T6

dispatchBaseHead: `cbf56ff50`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: delegated worker

Canonical packet: this file

Commit mode: WORKER_MUST_NOT_COMMIT

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

Current-time notes: use actual clean HEAD after this dispatch commit.

Do-not-misread notes: deterministic local clock only; no provider, queue, UI or T7.

Required first actions: read startup, paired baseline, this packet, cited sources/checkers; capture HEAD/status.

Return contract: produce exactly four paths, run gates, leave uncommitted, return COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON.

## Purpose

Implement deterministic local lifecycle control and focused tests.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind held-dependency --batch-id MAO-T6 --title "Timeout Heartbeat Cancel Retry And Recovery" --date 2026-07-11 --base 3294d555a --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | held dependency promoted to no-commit dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | dependency, anchors, exact paths and controls refreshed |
| checkerReadAheadConfirmation | applicable dispatch/handoff/return checkers read |
| docOnlyNewFields | lifecycle/retry/recovery fields defined only by new T6 contract |
| claimBoundary | authoring provenance only |

## Worker Autonomy / No-Question Rule

Repair allowed-scope checker defects directly; return only for source conflict,
missing authority or forbidden expansion.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | roadmap plus accepted T3-T5 source/closure evidence |
| Intake role | local lifecycle contract/test worker |
| Reviewer role | independent reviewer/closer |
| Routing decision | WORKER_MUST_NOT_COMMIT |
| Public route | DEFERRED_PRIVATE_ONLY |
| risk sensitivity | high because retry/cancel/recovery must fail closed |
| scope classification | bounded local deterministic contract/tests |
| canonical route mode | MULTI_AGENT_SINGLE_ROLE |
| selected role route | worker return to reviewer/closer |
| escalation condition | source contradiction, real clock/provider/queue need, or T7 expansion |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| role separation ledger | worker=implementation; reviewer/closer=review and commit; steward=session sync |
| gate sequence | pre-implementation, worker-return fast, reviewer-fast, pre-closure, session-sync |
| evidence basis independent of memory | current runtime source, focused tests, git evidence and governed review |
| escalation conditions | self-review, commit, provider, queue, real clock, public, or T7 scope blocks worker |

## Scope / Methodology

On release, add one lifecycle controller module, one focused test file, bounded
barrel exports, and one no-commit worker return. No provider or real clock.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-T3/T4 | `052845fa1`; `f71ba01f6` | accepted evidence exists | ACCEPT |
| MAO-T5 | material `9b225f0e4`; accepted completion review; 54/54 tests | accepted material and review exist | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`multi-agent orchestration runtime`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | HOLD status, dependency evidence, handoff fields |
| gateRunPurpose | held-packet confirmation |
| claimBoundary | not dispatch authorization |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| timeout/cancel terminal outcomes | VALUE_SET | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/read.model.contract.ts` | terminal outcome | `MaoTerminalOutcome` | read model | ACCEPT |
| diagnostics | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/delegation.adapter.contract.ts` | diagnostic type | `MaoDiagnosticClass` | delegation adapter | ACCEPT |

## Work-Order Fulfillment Manifest

| Artifact | Required action |
|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/lifecycle.controller.contract.ts` | create deterministic lifecycle controller |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.lifecycle.controller.contract.test.ts` | create focused tests |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | bounded exports |
| `docs/reviews/CVF_MAO_T6_TIMEOUT_HEARTBEAT_CANCEL_RETRY_AND_RECOVERY_WORKER_RETURN_2026-07-11.md` | create worker return |

## Required Artifact Manifest

| Artifact | Owner | Required final status |
|---|---|---|
| lifecycle source | worker | COMPLETE_PENDING_REVIEW |
| focused test | worker | COMPLETE_PENDING_REVIEW |
| bounded exports | worker | COMPLETE_PENDING_REVIEW |
| worker return | worker | COMPLETE_PENDING_REVIEW |

## Execution Plan

Implement deterministic clock/lifecycle transitions, duplicate/retry/cancel/
orphan rules, then focused tests, typecheck, and worker-return gate.

## Acceptance Criteria

- [ ] packet remains held until MAO-T5 acceptance;
- [ ] deterministic clock tests cover timeout and heartbeat;
- [ ] duplicate, retry, cancel, and orphan paths are classified;
- [ ] worker does not commit.

## Evidence Requirements

Focused test count, typecheck, diagnostics, diff/status, and fast-gate output.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | worker then reviewer/closer |
| phase | EXECUTION |
| baseHeadFor(phase) | dispatchBaseHead=cbf56ff50; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exactly four manifest paths |
| traceScope(phase, actor) | worker execution trace then reviewer closure trace |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | clean worktree verified at `cbf56ff50`; prior T5 batch fully committed; no overlapping batch |
| Before status evidence | clean worktree verified at handoff-sync commit `cbf56ff50`; no pending prior batch paths |
| nextMoveSurfaces | refresh dependency and anchors before dispatch |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MAO_T6_TIMEOUT_HEARTBEAT_CANCEL_RETRY_AND_RECOVERY_COMPLETION_2026-07-11.md` |
| reviewerOwnedClosurePaths | baseline, work order, completion and GC-051 coverage if required |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order control | Evidence |
|---|---|---|
| lifecycle/recovery | deterministic controller | focused tests |
| diagnostics | typed failure classification | negative tests |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

Worker may implement only the four local MAO-T6 paths and must not commit.

## Authority Chain

Operator -> roadmap -> baseline -> work order.

## Agent Roles

Dispatcher prepares; worker/reviewer/closer act only after release.

## Required First Reads

Startup, guards, paired baseline, work order, cited sources and checkers.

## Pre-Flight Checks

Refresh T5 evidence, anchors, status, manifest, HEAD and worktree.

## Write Ownership

Worker owns exactly the four fulfillment-manifest paths.

## Review Gate

Focused tests, typecheck, reviewer-fast and steward preflight.

## Closure Checklist

- [ ] dependency released; - [ ] manifest exact; - [ ] tests pass; - [ ] no commit.

## Return-To-Orchestrator Conditions

Return COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON without commit.

## Operator Checkpoint

Required only for scope/provider/runtime expansion.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | private workspace |
| Session or invocation | MAO-T6 held packet 2026-07-11 |
| Working directory | repository root |
| Command or tool surface | source reads and apply patch |
| Target paths | paired T6 packet |
| Allowed scope source | operator and roadmap |
| Before status evidence | clean worktree at handoff-sync HEAD `cbf56ff50`; T5 accepted at `9b225f0e4` |
| After status evidence | source-verified DISPATCH_READY packet |
| Diff evidence | `git diff --name-status` |
| Approval boundary | packet preparation only |
| Claim boundary | no execution |
| Agent type | dispatcher |
| Invocation ID | `mao-t6-held-2026-07-11` |
| Expected manifest | paired T6 packet |
| Actual changed set | captured before commit |
| Manifest delta | pending gate confirmation |
| Deletion or rename disposition | N/A with reason: none |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MAO_T6_TIMEOUT_HEARTBEAT_CANCEL_RETRY_AND_RECOVERY_WORKER_RETURN_2026-07-11.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
cd EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION
npx vitest run --config vitest.config.ts tests/mao.lifecycle.controller.contract.test.ts
npx tsc -p tsconfig.json --noEmit
cd ../..
python governance/compat/run_worker_return_fast_gate.py
git status --short
```
