# CVF Agent Work Order - MAO-T7 Evidence, Observability, And Operator Readout

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED

Batch ID: MAO-RUNTIME-T7

dispatchBaseHead: `746d8e08c`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: delegated worker

Canonical packet: this file

Commit mode: WORKER_MUST_NOT_COMMIT

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

Current-time notes: use actual clean post-dispatch HEAD.

Do-not-misread notes: no UI, provider, queue, session mutation or T8.

Required first actions: read startup, baseline, packet, workspace topology, cited sources/checkers; capture HEAD/status.

Return contract: produce exactly five outputs, run gates, leave uncommitted, return COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON.

## Purpose

Implement secret-safe local evidence/read-model contracts, tests and catalog candidate.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind held-dependency --batch-id MAO-T7 --title "Evidence Observability And Operator Readout" --date 2026-07-11 --base 3294d555a --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | held dependency promoted to no-commit dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | dependency, anchors, manifest and controls refreshed |
| checkerReadAheadConfirmation | dispatch/workspace/return checkers read |
| docOnlyNewFields | new T7 evidence/readout contract fields |
| claimBoundary | authoring provenance only |

## Worker Autonomy / No-Question Rule

Repair allowed-scope checker defects; return only for source conflict or forbidden expansion.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | roadmap plus accepted T1-T6 evidence |
| Intake role | local evidence/read-model worker |
| Reviewer role | independent reviewer/closer |
| Routing decision | WORKER_MUST_NOT_COMMIT |
| Public route | DEFERRED_PRIVATE_ONLY |
| risk sensitivity | high due secret-safe evidence and authority projection |
| scope classification | bounded local contract/tests/catalog candidate |
| canonical route mode | MULTI_AGENT_SINGLE_ROLE |
| selected role route | worker return to reviewer/closer |
| escalation condition | UI/provider/queue/authoritative workspace/T8 need |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| role separation ledger | worker=implementation; reviewer/closer=review/commit; steward=session sync |
| gate sequence | pre-implementation, worker-return fast, reviewer-fast, pre-closure, session-sync |
| evidence basis independent of memory | current source, tests, git and governed review |
| escalation conditions | self-review, commit, UI/provider/public/T8 blocks worker |

## Scope / Methodology

On release, implement secret-safe evidence/read-model contracts, freshness and
retention checks, milestone projection, and a catalog candidate packet. No UI.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-T1 through T4 | accepted material exists | retained | ACCEPT |
| MAO-T5/T6 | accepted materials `9b225f0e4` and `ee5a1a400`; reviews/tests pass | accepted evidence exists | ACCEPT |

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

| Artifact | Required action |
|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | create secret-safe ledger/read-model contract |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.evidence.readout.contract.test.ts` | create focused tests |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | bounded exports |
| `docs/reviews/CVF_MAO_T7_EVIDENCE_OBSERVABILITY_AND_OPERATOR_READOUT_CATALOG_CANDIDATE_2026-07-11.md` | create catalog-admission candidate packet |
| `docs/reviews/CVF_MAO_T7_EVIDENCE_OBSERVABILITY_AND_OPERATOR_READOUT_WORKER_RETURN_2026-07-11.md` | create worker return |

## Required Artifact Manifest

| Artifact | Owner | Required final status |
|---|---|---|
| source/test/exports/catalog candidate/worker return | worker | PASS |
| completion review and GC-051 entry | reviewer/closer | PASS |

## Execution Plan

Define receipt storage/read projection, redact secrets, enforce retention and
freshness, test drift, then typecheck and gate.

## Acceptance Criteria

- [x] packet stayed held until T6 acceptance;
- [x] receipts and read model are deterministic with denylisted-field redaction;
- [x] workspace remains projection-only;
- [x] no UI and no worker commit.

## Evidence Requirements

Focused tests, typecheck, drift/retention negatives, diff/status and fast gate.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | worker then reviewer/closer |
| phase | EXECUTION |
| baseHeadFor(phase) | dispatchBaseHead=746d8e08c; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exactly five manifest outputs |
| traceScope(phase, actor) | worker execution then reviewer closure |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | clean worktree at `746d8e08c`; T6 fully committed; no overlap |
| Before status evidence | clean worktree at `746d8e08c`; no pending prior paths |
| nextMoveSurfaces | refresh before dispatch |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MAO_T7_EVIDENCE_OBSERVABILITY_AND_OPERATOR_READOUT_COMPLETION_2026-07-11.md` |
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

Worker may create exactly five local T7 outputs and must not commit; no UI.

## Authority Chain

Operator -> roadmap -> baseline -> work order.

## Agent Roles

Dispatcher prepares; worker/reviewer/closer act only after release.

## Required First Reads

Startup, guards, baseline, work order, workspace topology, sources/checkers.

## Pre-Flight Checks

Refresh T6 evidence, anchors, manifest, HEAD and worktree.

## Write Ownership

Worker owns exactly five manifest outputs.

## Review Gate

Focused tests, secret review, typecheck, reviewer-fast and steward preflight.

## Closure Checklist

- [x] dependency released; - [x] denylisted fields redacted; - [x] tests pass; - [x] no UI/commit.

## Return-To-Orchestrator Conditions

Return COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON without commit.

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
| Before status evidence | clean worktree at `746d8e08c`; T6 accepted at `ee5a1a400` |
| After status evidence | source-verified packet, later reviewer-accepted bounded |
| Diff evidence | `git diff --name-status` |
| Approval boundary | packet preparation only |
| Claim boundary | no execution/UI |
| Agent type | dispatcher |
| Invocation ID | `mao-t7-held-2026-07-11` |
| Expected manifest | paired T7 packet |
| Actual changed set | captured before commit |
| Manifest delta | pending gate confirmation |
| Deletion or rename disposition | N/A with reason: none |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MAO_T7_EVIDENCE_OBSERVABILITY_AND_OPERATOR_READOUT_WORKER_RETURN_2026-07-11.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | milestone projection target only; not authoritative runtime state |
| Contract source | archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Design standard | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Storage class | no workspace state mutation; projection contract only |
| Handoff fields | existing AHB fields remain authoritative |
| State ownership | execution-plane ledger owns runtime evidence; workspace is read-only projection |
| Guard owner | `governance/compat/check_agent_workspace_design.py` |
| Build boundary | runtime source: T7 evidence contract only; provider proof: no; public-sync: no; registry edits: catalog candidate only, no admission |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | execution-plane MAO source/test plus dated catalog candidate |
| Storage decision | extend existing `src/mao/`; keep candidate under `docs/reviews/` |
| Existing aggregate impact | bounded barrel export only |
| Generated state impact | none; workspace generated state is not changed |
| Durable governance boundary | no new hidden store; receipt ledger contract remains local/in-memory foundation |

## Verification Commands

```powershell
cd EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION
npx vitest run --config vitest.config.ts tests/mao.evidence.readout.contract.test.ts
npx tsc -p tsconfig.json --noEmit
cd ../..
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MAO_T7_EVIDENCE_OBSERVABILITY_AND_OPERATOR_READOUT_COMPLETION_2026-07-11.md` | reviewer acceptance | PASS |
| Roadmap state | `docs/roadmaps/CVF_MULTI_AGENT_ORCHESTRATION_RUNTIME_FOUNDATION_ROADMAP_2026-07-11.md` | T7 bounded implementation complete; roadmap remains active through T9 | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated GC-051 aggregate | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no Markdown regeneration required for source coverage entry | PASS |
| External evidence digest | N/A with reason: T7 uses repository-local source and tests only | no external source ingestion | N/A with reason: not applicable |
| System loop interlock | `docs/reviews/CVF_MAO_T7_EVIDENCE_OBSERVABILITY_AND_OPERATOR_READOUT_CATALOG_CANDIDATE_2026-07-11.md` | candidate remains pending admission; no aggregate mutation | PASS |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json` and active handoff | refreshed in separate session-sync change after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| focused receipt/readout tests | PASS | 35/35 PASS | PASS |
| graph-bound evidence admission | mismatched graph rejected | `TASK_GRAPH_ID_MISMATCH` and no stored record | PASS |
| worker commit boundary | no worker commit | five outputs returned uncommitted | PASS |
