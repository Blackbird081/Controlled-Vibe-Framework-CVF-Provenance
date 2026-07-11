# CVF Agent Work Order - MAO-T7 Evidence, Observability, And Operator Readout

Memory class: governed-worker-dispatch

Status: HOLD_UNTIL_MAO_T6_PASS

Batch ID: MAO-T7

dispatchBaseHead: `3294d555a`

executionBaseHead: `NOT_RELEASED`

closureBaseHead: `NOT_RELEASED`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Define held receipt-ledger and operator read-model implementation work.

## Scope / Methodology

On release, implement secret-safe evidence/read-model contracts, freshness and
retention checks, milestone projection, and a catalog candidate packet. No UI.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-T1 through T4 | accepted material exists | retained | ACCEPT |
| MAO-T5/T6 | no accepted T6 execution | both accepted and anchors refreshed | HOLD |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`multi-agent orchestration runtime`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_workspace_design.py` |
| literalTokensReviewed | held dependency and workspace projection boundary |
| gateRunPurpose | held-packet confirmation |
| claimBoundary | no UI/runtime authority |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| MAO read model | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/read.model.contract.ts` | exported model | `MaoGeneratedReadModel` | read model | ACCEPT |
| review receipt | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/dissent.revision.contract.ts` | receipt type | `MaoReviewReceipt` | dissent/revision | ACCEPT |
| workspace projection boundary | LITERAL_INVARIANT | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | ownership | `stateOwnership` | workspace topology | ACCEPT |

## Work-Order Fulfillment Manifest

Receipt ledger/read-model source, focused tests, bounded exports, catalog
candidate packet, and worker return; exact paths assigned at dependency release.

## Execution Plan

Define receipt storage/read projection, redact secrets, enforce retention and
freshness, test drift, then typecheck and gate.

## Acceptance Criteria

- [ ] packet stays held until T6 acceptance;
- [ ] receipts and read model are deterministic and secret-safe;
- [ ] workspace remains projection-only;
- [ ] no UI and no worker commit.

## Evidence Requirements

Focused tests, typecheck, drift/retention negatives, diff/status and fast gate.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | worker then reviewer/closer |
| phase | HOLD |
| baseHeadFor(phase) | dispatchBaseHead=3294d555a; executionBaseHead=NOT_RELEASED; closureBaseHead=NOT_RELEASED |
| changedSetScope(phase) | none while held |
| traceScope(phase, actor) | dispatcher only |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | release only after T6 closure |
| nextMoveSurfaces | refresh before dispatch |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | dated MAO-T7 completion review assigned at release |
| reviewerOwnedClosurePaths | packet, review, registry/catalog coverage |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Control | Evidence |
|---|---|---|
| ledger/readout | typed secret-safe projection | tests |
| freshness/retention | bounded policies | negative tests |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

Source-complete held packet only; no T7 implementation or UI is dispatched.

## Authority Chain

Operator -> roadmap -> baseline -> work order.

## Agent Roles

Dispatcher prepares; worker/reviewer/closer act only after release.

## Required First Reads

Startup, guards, baseline, work order, workspace topology, sources/checkers.

## Pre-Flight Checks

Refresh T6 evidence, anchors, manifest, HEAD and worktree.

## Write Ownership

No writes while held; exact paths assigned at release.

## Review Gate

Focused tests, secret review, typecheck, reviewer-fast and steward preflight.

## Closure Checklist

- [ ] dependency released; - [ ] secret-safe; - [ ] tests pass; - [ ] no UI/commit.

## Return-To-Orchestrator Conditions

No execution while held; after release return pending review or blocked.

## Operator Checkpoint

Required for UI, provider, authoritative workspace, or public expansion.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | private workspace |
| Session or invocation | MAO-T7 held packet 2026-07-11 |
| Working directory | repository root |
| Command or tool surface | source reads and apply patch |
| Target paths | paired T7 packet |
| Allowed scope source | operator and roadmap |
| Before status evidence | T6 not accepted |
| After status evidence | source-complete HOLD packet |
| Diff evidence | `git diff --name-status` |
| Approval boundary | packet preparation only |
| Claim boundary | no execution/UI |
| Agent type | dispatcher |
| Invocation ID | `mao-t7-held-2026-07-11` |
| Expected manifest | paired T7 packet |
| Actual changed set | captured before commit |
| Manifest delta | pending gate confirmation |
| Deletion or rename disposition | N/A with reason: none |
