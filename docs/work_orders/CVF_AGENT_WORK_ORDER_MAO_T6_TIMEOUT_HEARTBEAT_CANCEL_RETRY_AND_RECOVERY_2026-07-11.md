# CVF Agent Work Order - MAO-T6 Timeout, Heartbeat, Cancel, Retry, And Recovery

Memory class: governed-worker-dispatch

Status: HOLD_UNTIL_MAO_T5_PASS

Batch ID: MAO-T6

dispatchBaseHead: `3294d555a`

executionBaseHead: `NOT_RELEASED`

closureBaseHead: `NOT_RELEASED`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Define the held worker contract for deterministic lifecycle control and tests.

## Scope / Methodology

On release, add one lifecycle controller module, one focused test file, bounded
barrel exports, and one no-commit worker return. No provider or real clock.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-T3/T4 | `052845fa1`; `f71ba01f6` | accepted evidence exists | ACCEPT |
| MAO-T5 | packet only; execution absent | accepted completion, material commit, and refreshed anchors | HOLD |

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

`lifecycle.controller.contract.ts`; its focused test; bounded `src/mao/index.ts`
exports; and the dated MAO-T6 worker return. Exact paths must be refreshed at
dependency release before status can become ready.

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
| phase | HOLD |
| baseHeadFor(phase) | dispatchBaseHead=3294d555a; executionBaseHead=NOT_RELEASED; closureBaseHead=NOT_RELEASED |
| changedSetScope(phase) | no execution changed set while held |
| traceScope(phase, actor) | dispatcher trace only until release |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | release only after T5 worktree closure |
| nextMoveSurfaces | refresh dependency and anchors before dispatch |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | dated MAO-T6 completion review, assigned at release |
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

Source-complete held packet only; no T6 implementation is dispatched.

## Authority Chain

Operator -> roadmap -> baseline -> work order.

## Agent Roles

Dispatcher prepares; worker/reviewer/closer act only after release.

## Required First Reads

Startup, guards, paired baseline, work order, cited sources and checkers.

## Pre-Flight Checks

Refresh T5 evidence, anchors, status, manifest, HEAD and worktree.

## Write Ownership

No worker writes while held; exact paths assigned at release.

## Review Gate

Focused tests, typecheck, reviewer-fast and steward preflight.

## Closure Checklist

- [ ] dependency released; - [ ] manifest exact; - [ ] tests pass; - [ ] no commit.

## Return-To-Orchestrator Conditions

No execution while held; after release return pending review or blocked.

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
| Before status evidence | T5 not accepted |
| After status evidence | source-complete HOLD packet |
| Diff evidence | `git diff --name-status` |
| Approval boundary | packet preparation only |
| Claim boundary | no execution |
| Agent type | dispatcher |
| Invocation ID | `mao-t6-held-2026-07-11` |
| Expected manifest | paired T6 packet |
| Actual changed set | captured before commit |
| Manifest delta | pending gate confirmation |
| Deletion or rename disposition | N/A with reason: none |
