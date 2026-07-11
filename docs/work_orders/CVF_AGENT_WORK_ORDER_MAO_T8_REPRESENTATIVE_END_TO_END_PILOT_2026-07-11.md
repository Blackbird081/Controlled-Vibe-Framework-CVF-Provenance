# CVF Agent Work Order - MAO-T8 Representative End-To-End Pilot

Memory class: governed-worker-dispatch

Status: HOLD_UNTIL_MAO_T7_PASS_AND_FRESH_PILOT_SELECTION

Batch ID: MAO-T8

dispatchBaseHead: `3294d555a`

executionBaseHead: `NOT_RELEASED`

closureBaseHead: `NOT_RELEASED`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Define a held representative end-to-end proof envelope.

## Scope / Methodology

One selected bounded task, one worker, independent reviewer, at most one
classified revision, and one designated closer, plus required negative cases.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-T1 through T7 | T5-T7 incomplete | all accepted and anchors refreshed | HOLD |
| fresh pilot selection | absent | operator-approved task, proof class, provider disposition | HOLD |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`multi-agent orchestration runtime`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | pilot selection, live proof and no-commit boundaries |
| gateRunPurpose | held-packet confirmation |
| claimBoundary | no pilot/live execution |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| pilot concurrency ceiling | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | budget validator | `PILOT_MAX_CONCURRENT_ROLES` | task graph | ACCEPT |
| self-approval protection | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/reviewer.isolation.contract.ts` | identity guard | `checkSelfApproval` | reviewer isolation | ACCEPT |

## Work-Order Fulfillment Manifest

Fresh pilot packet, proof artifacts/receipts, negative tests, worker return, and
reviewer completion path; exact paths depend on the selected task.

## Execution Plan

Select task and proof class, refresh sources/anchors, run the bounded chain,
exercise negatives, and record command-backed receipts.

## Acceptance Criteria

- [ ] remains held until T7 and pilot selection;
- [ ] proves one bounded worker-reviewer-revision-closer chain;
- [ ] covers self-approval, duplicate, timeout, cancel, budget negatives;
- [ ] real-provider claims use mandatory live proof and diagnostics;
- [ ] worker does not commit.

## Evidence Requirements

Command-backed receipts, actual provider disposition, diagnostics if live,
diff/status, and independent review.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | worker, independent reviewer, designated closer |
| phase | HOLD |
| baseHeadFor(phase) | dispatchBaseHead=3294d555a; executionBaseHead=NOT_RELEASED; closureBaseHead=NOT_RELEASED |
| changedSetScope(phase) | none until pilot selection |
| traceScope(phase, actor) | per-actor trace required at release |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; one closer designated before execution |
| crossBatchIsolation | single pilot batch only |
| nextMoveSurfaces | update only after accepted pilot closure |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | required MAO-T8 completion review assigned by pilot packet |
| reviewerOwnedClosurePaths | pilot packet, evidence reconciliation, completion review |
| closureOwner | designated closer |
| workerCommitPermission | FORBIDDEN |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Control | Evidence |
|---|---|---|
| representative chain | bounded pilot | receipts |
| negative behavior | explicit scenarios | command evidence |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

Held pilot envelope only; no real-provider or runtime-governance claim exists.

## Authority Chain

Operator -> roadmap -> fresh pilot selection -> baseline -> work order.

## Agent Roles

Dispatcher, worker, independent reviewer, designated closer, session steward.

## Required First Reads

Startup, guards, baseline, work order, all T1-T7 closure evidence and checkers.

## Pre-Flight Checks

Refresh dependencies, select pilot/proof class, anchors, manifest and worktree.

## Write Ownership

No writes while held; pilot packet assigns exact paths and per-actor scope.

## Review Gate

Independent review, receipt reconciliation, negatives and closure preflight.

## Closure Checklist

- [ ] T7 accepted; - [ ] pilot selected; - [ ] receipts complete; - [ ] negatives pass.

## Return-To-Orchestrator Conditions

No execution while held; selected worker returns uncommitted evidence.

## Operator Checkpoint

Required for pilot selection and any live/provider proof.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | private workspace |
| Session or invocation | MAO-T8 held packet 2026-07-11 |
| Working directory | repository root |
| Command or tool surface | source reads and apply patch |
| Target paths | paired T8 packet |
| Allowed scope source | operator and roadmap |
| Before status evidence | T7/pilot selection absent |
| After status evidence | source-complete HOLD packet |
| Diff evidence | `git diff --name-status` |
| Approval boundary | packet preparation only |
| Claim boundary | no pilot/live execution |
| Agent type | dispatcher |
| Invocation ID | `mao-t8-held-2026-07-11` |
| Expected manifest | paired T8 packet |
| Actual changed set | captured before commit |
| Manifest delta | pending gate confirmation |
| Deletion or rename disposition | N/A with reason: none |
