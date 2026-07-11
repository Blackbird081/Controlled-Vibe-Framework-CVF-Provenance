# CVF Agent Work Order - MAO-T5 Designated Closer And Commit/Session Interlock

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED

Batch ID: MAO-T5

dispatchBaseHead: `f1f895f31`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: delegated worker

Canonical packet: this file

Commit mode: WORKER_MUST_NOT_COMMIT

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

Current-time notes: artifact date 2026-07-11; use actual clean HEAD at execution.

Do-not-misread notes: no provider, git mutation, session mutation, or T6 work.

Required first actions: read startup, baseline, this packet, sources and checkers; capture HEAD/status.

Return contract: implement only the manifest, run gates, leave changes uncommitted, and return COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON.

## Purpose

Implement local closer/commit/session interlock contracts and focused tests.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-T5 --title "Designated Closer And Commit Session Interlock" --date 2026-07-11 --base 3294d555a --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic no-commit dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, exact manifest, controls and gates |
| checkerReadAheadConfirmation | dispatch, handoff and worker-return checkers read |
| docOnlyNewFields | integrationDecisionId; sessionProjectionRequired |
| claimBoundary | authoring provenance only |

## Worker Autonomy / No-Question Rule

Repair allowed-scope checker defects directly. Return only for source conflict,
missing authority, or forbidden-scope need.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | CVF roadmap and accepted T4 closure evidence |
| Intake role | local contract/test worker |
| Reviewer role | independent reviewer/closer |
| Routing decision | WORKER_MUST_NOT_COMMIT |
| Public route | DEFERRED_PRIVATE_ONLY |
| risk sensitivity | high because commit/session authority must fail closed |
| scope classification | bounded local execution-plane contract and tests |
| canonical route mode | MULTI_AGENT_SINGLE_ROLE |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | return blocked for source conflict, git mutation need, provider/runtime/public expansion, or missing authority |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| role separation ledger | worker=implementation; reviewer/closer=review and material commit; steward=session sync |
| gate sequence | pre-implementation, worker-return fast, reviewer-fast, pre-closure, session-sync |
| evidence basis independent of memory | cited runtime source, focused tests, git evidence, governed completion review |
| escalation conditions | any self-review, commit, session mutation, provider, public, or T6 scope need blocks worker |

## Scope / Methodology

Add deterministic pure functions/types under the existing MAO package. Reuse
T1 authority, T4 review receipts, AHB closure ownership, and commit-steward
split semantics. Do not run git mutation from runtime code.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| MAO-T4 accepted | material `f71ba01f6`; completion review exists | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`multi-agent orchestration runtime`, role=`worker`, lifecyclePhase=`implementation`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "multi-agent orchestration runtime" --role worker --lifecycle-phase implementation`

Returned defects: NONE_RETURNED

Disclosed defectIds: none.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | exact source table, trace labels, no-commit and reviewer conversion terms |
| gateRunPurpose | dispatch confirmation |
| claimBoundary | structural/source fidelity only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| closer role | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | role type | `MaoTaskRole` | task graph | ACCEPT |
| closer identity | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | authority | `closerActorId` | task graph | ACCEPT |
| review decision input | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/dissent.revision.contract.ts` | receipt | `MaoReviewReceipt` | dissent/revision | ACCEPT |
| commit split | LITERAL_INVARIANT | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | Commit Split Rule | `Commit Split Rule` | commit steward | ACCEPT |

## New Doc-Only Fields

| Field | Owner | Purpose |
|---|---|---|
| integrationDecisionId | MAO-T5 contract | deterministic local decision identity |
| sessionProjectionRequired | MAO-T5 contract | signals separate steward projection without performing it |

## Work-Order Fulfillment Manifest

| Artifact | Required action |
|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/closer.interlock.contract.ts` | create contract |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.closer.interlock.contract.test.ts` | create focused tests |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | bounded exports |
| `docs/reviews/CVF_MAO_T5_DESIGNATED_CLOSER_AND_COMMIT_SESSION_INTERLOCK_WORKER_RETURN_2026-07-11.md` | create worker return |

## Required Artifact Manifest

| Artifact | Owner | Final status |
|---|---|---|
| closer interlock source | worker | PASS |
| focused test | worker | PASS |
| bounded barrel exports | worker | PASS |
| worker return | worker | PASS |
| completion review and GC-051 coverage | reviewer | PASS |

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | capture clean execution HEAD and re-read sources | return trace |
| 2 | implement exactly-one closer and integration decision | focused tests |
| 3 | enforce no-auto-commit and session projection separation | negative tests |
| 4 | typecheck and run worker-return fast gate | command evidence |

## Acceptance Criteria

- [x] exactly one designated closer is required;
- [x] no adapter or worker gains commit authority;
- [x] closure conversion consumes a valid terminal review receipt;
- [x] commit and session-sync intents remain separate projections;
- [x] focused tests and typecheck pass;
- [x] worker returns exactly four paths and does not commit.

## Evidence Requirements

Record focused test count, typecheck, `git diff --name-status`, actual
`git status --short`, worker-return fast gate, and claim boundaries.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | worker then independent reviewer/closer |
| phase | EXECUTION |
| baseHeadFor(phase) | dispatchBaseHead=f1f895f31; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | four manifest paths only |
| traceScope(phase, actor) | worker traces execution; reviewer traces closure |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns accepted material commit |
| crossBatchIsolation | no second batch while worker paths are pending |
| nextMoveSurfaces | session-sync steward updates only after accepted material commit |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MAO_T5_DESIGNATED_CLOSER_AND_COMMIT_SESSION_INTERLOCK_COMPLETION_2026-07-11.md` |
| reviewerOwnedClosurePaths | paired baseline/work order; completion review; minimum GC-051 registry source/aggregate if required |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order control | Evidence |
|---|---|---|
| exactly-one closer | closer contract | focused positive/negative tests |
| integration and closure conversion | receipt-bound decision | deterministic tests |
| commit/session interlock | no-auto-commit and separate projection | negative tests |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MAO_T5_DESIGNATED_CLOSER_AND_COMMIT_SESSION_INTERLOCK_WORKER_RETURN_2026-07-11.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
cd EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION
npx vitest run --config vitest.config.ts tests/mao.closer.interlock.contract.test.ts
npx tsc -p tsconfig.json --noEmit
cd ../..
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | private provenance workspace |
| Session or invocation | MAO-T5 packet authoring 2026-07-11 |
| Working directory | repository root |
| Command or tool surface | source reads, apply patch, gates |
| Target paths | paired T5 baseline and work order |
| Allowed scope source | operator request and roadmap MAO-T5 |
| Before status evidence | clean worktree at session release commit `f1f895f31`; MAO-T4 closed at `f71ba01f6` |
| After status evidence | source-verified packet ready for worker |
| Diff evidence | `git diff --name-status` |
| Approval boundary | packet authoring and bounded T5 worker dispatch |
| Claim boundary | no implementation evidence yet |
| Agent type | dispatcher |
| Invocation ID | `mao-t5-dispatch-2026-07-11` |
| Expected manifest | paired T5 baseline/work order plus held T6-T9 packets |
| Actual changed set | captured before dispatch commit |
| Manifest delta | pending gate confirmation |
| Deletion or rename disposition | N/A with reason: none planned |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | dispatch packet only |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker has not executed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: packet authoring only |
| invocationBoundary | future local pure-function tests |
| interceptionBoundary | no git/provider/runtime interception |
| claimLanguage | authorized contract-and-test implementation only |
| forbiddenExpansion | provider, durable runtime, public, UI, MAO-T6+ implementation |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

Worker may implement MAO-T5 local contracts/tests only and must not commit.

## Authority Chain

Operator request -> MAO roadmap -> paired GC-018 -> this work order.

## Agent Roles

Dispatcher authors; worker implements without commit; reviewer/closer accepts
and commits; session-sync steward updates continuity separately.

## Required First Reads

Startup front doors, guard orientation, literal gotchas, paired baseline, this
work order, source-verification files, and applicable checker sources.

## Pre-Flight Checks

Capture HEAD/status, confirm dependency and exact manifest, then run the
pre-implementation autorun gate after release.

## Write Ownership

Worker owns only four fulfillment-manifest paths. Reviewer owns closure paths.

## Review Gate

Independent semantic review, focused tests, typecheck, reviewer-fast, and
commit-steward preflight are required.

## Closure Checklist

- [x] dependency/session release refreshed;
- [x] worker manifest exact;
- [x] tests and typecheck pass;
- [x] no-commit honored;
- [x] continuity update assigned separately.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| implementation | T5 source/test/barrel | 54/54 Vitest; typecheck PASS | PASS |
| review | dated completion review | REVIEWER_ACCEPTED_BOUNDED | PASS |
| corpus coverage | GC-051 source/aggregate | generator check PASS | PASS |
| next move | held MAO-T6 packet | dependency refresh required | PASS |
| Work order status | this work order | CLOSED_PASS_BOUNDED | PASS |
| Completion or reviewer artifact | dated T5 completion review | REVIEWER_ACCEPTED_BOUNDED | PASS |
| Roadmap state | MAO roadmap T5 | accepted; T6 held | PASS |
| Registry JSON | GC-051 aggregate | generated | PASS |
| Registry Markdown | N/A with reason: no Markdown registry changed | N/A | PASS |
| External evidence digest | N/A with reason: local evidence only | N/A | N/A with reason: local evidence only |
| System loop interlock | current interlock registry | unchanged | PASS |
| Session continuity | session-sync steward | pending separate commit | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| T5-Q1 | focused test output | N/A | 54 passing | 54 passing | PASS |
| T5-Q2 | typecheck output | N/A | exit 0 | exit 0 | PASS |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`; never commit.

## Operator Checkpoint

No checkpoint for local T5 implementation after session release. Any provider,
git mutation, runtime, public, or T6+ expansion returns to operator.
