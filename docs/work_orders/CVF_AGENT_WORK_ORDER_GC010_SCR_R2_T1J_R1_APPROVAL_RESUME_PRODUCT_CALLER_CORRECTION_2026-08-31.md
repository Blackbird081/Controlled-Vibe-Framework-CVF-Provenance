# CVF Agent Work Order - GC010 SCR-R2-T1J-R1 Approval Resume Product Caller Correction

Memory class: governed-worker-dispatch

docType: work_order

Status: READY_FOR_DISPATCH

Batch ID: GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION

Dispatch base head: `072dffc3338fd2ed9a6fb98673953a5b807cd7b1`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: orchestrator/reviewer

Worker return path: `docs/reviews/CVF_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_WORKER_RETURN_2026-08-31.md`

## Dispatch Prompt Envelope

Role: delegated decision worker for T1J-R1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_2026-08-31.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: current source and continuity date are 2026-08-31.

Do-not-misread notes: this is a consolidated evidence correction to T1J. It
does not authorize implementation or presume that a second route is valuable.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, this work order, paired baseline, T1J assessment/return, and every
source path in the Source Verification Block.

Return contract: create exactly two named documents, run required gates, do not
stage or commit, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

providerExecutionAuthority: FORBIDDEN

## Purpose

Re-evaluate T1J using the missed approval UI and approval-bound execution
evidence. Select whether the concrete approval-resume product flow justifies an
isolated pending-execution consumer, is better completed through the existing
execute route, remains partial, or must stay parked.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK
dispatchSurface: EXTERNAL_AGENT_CLI_MCP
parentAssignmentId: GC010_SCR_R2_T1J_REGISTERED_PRODUCTION_INVOCATION_OWNER_AND_INVOKED_PATH_COMPOSITION_DECISION
reviewRoundCount: 1
priorFindingSetDigest: 88173edc1fa61883cd1961cce2fdac6a69293944061398af0cf16ba09e89589b
dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR
reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS
newIndependentCriticalEvidence: ApprovalInbox and approval-bound execute path
regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT
cumulativeExternalInvocationCount: 1
externalInvocationCeiling: 2
usageAvailability: KNOWN_FOR_ADMISSION
quotaAdmissionDisposition: ADMITTED_WITHIN_CUMULATIVE_CEILING
nextDispatchDisposition: ONE_CONSOLIDATED_REWORK
rootCauseClusterId: T1J_MISSED_APPROVAL_PRODUCT_SURFACE
reworkGeneration: 1
consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

## Scope / Target / Owner Boundary

In scope: current-source analysis of the approval pages, `ApprovalInbox`,
`ProcessingScreen`, approval routes/store/binding, approval handling in
`/api/execute`, pending-agent-execution core/composition/store/harness, and T1J.

Out of scope: every source/test/roadmap/session change; implementation; route,
adapter, export, provider, admission or audit wiring; provider/live/network;
public sync; deployment; production; successor dispatch.

## Authority Chain

Operator continuation instruction -> active GC010 roadmap -> accepted T1J
closure -> this source-verified R1 correction -> independent reviewer.

## Agent Roles

- Operator authorizes bounded correction.
- Dispatcher owns this packet.
- Worker writes exactly two documents and never commits.
- Reviewer/closer independently verifies, repairs if bounded, and owns commits.

## Required First Reads

Read `CVF_SESSION_MEMORY.md`, bootstrap read model, active handoff, guard
orientation, literal gotchas, paired baseline, this work order, T1J assessment
and every current-source path named below.

## Pre-Flight Checks

Capture full HEAD and status; confirm both outputs absent; run the specified
pre-implementation gate; stop on dirty overlap or source contradiction.

## Write Ownership

Worker owns only the two Required Artifact Manifest paths. All source, tests,
roadmaps, session state and dispatch artifacts are read-only.

## Execution Plan

1. Reproduce the approval UI, decision-route and execute-resume source facts.
2. Trace the actual user and admin flow end to end without running providers.
3. Compare all four candidates and answer all ten questions.
4. Select one terminal, run gates and return two uncommitted documents.

## Evidence Requirements

Every product/caller claim must cite current source. Distinguish an existing
server primitive from an invoked UI flow. Record exact manifest/status and zero
provider/network/live calls.

## Acceptance Criteria

- Four candidates and ten questions completed.
- Existing execute-route completion and isolated pending composition compared.
- Product value and duplication assessed independently.
- Exactly one terminal; successor remains closed.
- Exactly two outputs, no source change, no commit, gates PASS.

## Review Gate

Reviewer reproduces the source trace, rejects governance-only value claims,
checks exact scope, runs worker-return fast and independently selects terminal.

## Closure Checklist

- exact two outputs
- current source citations
- one terminal
- no implementation or live effect
- worker-return gate PASS
- reviewer decision pending

## Return-To-Orchestrator Conditions

Return only for source contradiction, dirty overlap, forbidden-scope need or
missing authority. Otherwise finish the bounded decision autonomously.

## Operator Checkpoint

Even a ready result requires a separately governed T1K work order with exact
source/test authority. T2, provider/live and production remain parked.

## Worker Autonomy / No-Question Rule

Repair allowed-scope document/checker defects directly. Do not ask routine
questions or widen scope. Stop only under Return Conditions.

## Intake Role Routing Decision

routeMode: MULTI_AGENT_MULTI_ROLE
intakeSummary: bounded correction of missed local approval UI and resume-path evidence
scopeClassification: DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT
riskSensitivity: high because a false caller decision can create duplicate provider execution
escalationCondition: source contradiction, forbidden implementation need, dirty overlap, or missing binding authority

The external worker supplies non-authoritative decision evidence; the internal
reviewer owns acceptance and all commits.

## Required Artifact Manifest

Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/assessments/CVF_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_2026-08-31.md` | CREATE correction assessment, comparison, answers and terminal |
| `docs/reviews/CVF_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_WORKER_RETURN_2026-08-31.md` | CREATE checker-safe pending return |

Exactly these two paths may change.

## Mandatory Decision Questions

1. Which current UI initiates execution and which UI decides approval?
2. Does any current UI resubmit `/api/execute` with the approved ID?
3. Does the existing execute route already provide the complete resume product
   behavior, or only a server-side primitive without caller completion?
4. What user/operator outcome is missing after approval today?
5. Can that outcome be completed by a small existing-route UI change without
   creating an AER consumer?
6. What incremental product value would the pending runtime provide: durable
   recovery, claim/concurrency control, exactly-once terminal state, or none?
7. If isolated composition is selected, name the exact caller, trigger,
   construction/import, guard, approval, provider/admission, durable store,
   response and failure owners.
8. Would approval-route-triggered execution improperly couple an admin decision
   to provider effects or actor identity?
9. How is duplicate guard/admission/provider invocation prevented?
10. Which terminal is supported, and why is each alternative defeated?

## Required Candidate Comparison

Compare all four baseline candidates. Do not infer that a visible approval UI
automatically justifies AER; prove value beyond the existing execute route.
Conversely, do not repeat T1J's no-UI conclusion without addressing the exact
pages, components and approval-bound route source named here.

## Terminal Contract

Select exactly one terminal from the paired baseline and keep
`successorTrancheOpened: NO`. A ready terminal means reviewer consideration of
a later T1K packet only; it does not open implementation.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Approval UI calls list and decision routes | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ApprovalInbox.tsx` | `loadRequests`; `handleAction` | fetch calls | `ApprovalInboxContent` | ACCEPT |
| Dashboard approval page mounts the UI | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/approvals/page.tsx` | page body | `ApprovalInbox` | page | ACCEPT |
| Existing execute route validates approved ID and payload/actor binding | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | approval block | `approvalId` | `POST` | ACCEPT |
| Approval PATCH decides and audits but does not execute | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/[id]/route.ts` | `PATCH` | `APPROVAL_DECIDED` | approval route | ACCEPT |
| Processing screen stores approval ID but omits it from execute request | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx` | `executeReal`; approval state | request body | `ProcessingScreen` | ACCEPT |
| Pending runtime supplies approval-bound lifecycle semantics | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | claim/begin/terminal logic | pending record | pending core | ACCEPT |
| T1J missed the UI/product evidence | accepted assessment | `docs/assessments/CVF_GC010_SCR_R2_T1J_REGISTERED_PRODUCTION_INVOCATION_OWNER_AND_INVOKED_PATH_COMPOSITION_DECISION_2026-08-31.md` | questions 3 and 12 | no-caller finding | T1J | ACCEPT |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
```

No runtime tests or provider calls are required; this is source-backed
decision work.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_WORKER_RETURN_2026-08-31.md`
contractProfile: WORKER_RETURN_FAST_DOC_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED
scopeClassification: DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT
publicSyncDisposition: FORBIDDEN
liveRuntimeDisposition: FORBIDDEN
checkerMutationDisposition: FORBIDDEN
workerSelfSelection: FORBIDDEN

Required sections: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Evidence / Verification; Risk / Corrective Action; Conditional
Controls Disposition; Checker Source Read-Ahead Block; Agent Operation Trace
Block; Delta Execution Claim Boundary Control Block; Epistemic Process Block;
Public Export Disposition; Claim Boundary; git status --short; Changed Files;
No-Commit Statement.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | operator -> dispatcher -> external worker -> reviewer/closer -> session-sync steward |
| phase | T1J-R1 decision correction |
| baseHeadFor(phase) | dispatchBaseHead=`072dffc3338fd2ed9a6fb98673953a5b807cd7b1`; executionBaseHead=worker capture; closureBaseHead=reviewer set |
| changedSetScope(phase) | exactly two worker documents |
| traceScope(phase, actor) | source reads, commands, exact manifest and zero external effects |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer owns commits |
| crossBatchIsolation | all unrelated paths remain unchanged |
| nextMoveSurfaces | reviewer updates continuity only after acceptance |

## Dual Agent Surface Matrix

| Surface | Role | Disposition |
| --- | --- | --- |
| INTERNAL_AGENT | reviewer/closer | independently verifies and commits or rejects |
| EXTERNAL_AGENT_CLI_MCP | worker | decision-only two-file return |
| Adapter boundary | operator-mediated file return | external text is non-authoritative until review |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_COMPLETION_2026-08-31.md` (optional; reviewer creates only if necessary) |
| reviewerOwnedClosurePaths | material commit, then continuity-only commit |
| closureOwner | orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`decision assessment`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | ready status, source rows, rework convergence fields, handoff fields, dual surfaces, trace labels and no-commit terms |
| gateRunPurpose | Confirmation after source-led authoring. |
| claimBoundary | Gate shape cannot select the product topology. |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GC010_SCR_R2_T1J_R1_APPROVAL_SURFACE_PRODUCT_CALLER_CORRECTION --title "GC010 SCR R2 T1J R1 Approval Surface Product Caller Correction" --date 2026-08-31 --base 072dffc3338fd2ed9a6fb98673953a5b807cd7b1 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 1 --root-cause-cluster-id T1J_MISSED_APPROVAL_PRODUCT_SURFACE --prior-finding-set-digest 88173edc1fa61883cd1961cce2fdac6a69293944061398af0cf16ba09e89589b --cumulative-external-invocation-count 1 --external-invocation-ceiling 2 --new-independent-critical-evidence "ApprovalInbox and approval-bound execute path" --stdout` |
| generatedProfile | no-commit consolidated rework |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added missed-source correction, decision questions, exact manifest and boundaries. |
| checkerReadAheadConfirmation | Applicable sources inspected before material authoring. |
| docOnlyNewFields | candidate comparison and approval-resume decision questions |
| claimBoundary | Provenance only. |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | GC010 T1J-R1 dispatch, 2026-08-31 |
| Working directory | repository root |
| Command or tool surface | source reads, `rg`, scaffold helper, `apply_patch`, governance gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | operator instruction to continue GC010 system-chain |
| Before status evidence | clean at `072dffc3338fd2ed9a6fb98673953a5b807cd7b1` |
| After status evidence | two dispatch documents only before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | decision dispatch only |
| Claim boundary | no implementation or external effect |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `gc010-t1j-r1-dispatch-2026-08-31` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | documentation-only correction dispatch |
| claimDisposition | CLAIM_REJECTED: no runtime behavior is claimed |
| receiptEvidence | N/A with reason: no runtime receipt is created |
| actionEvidence | ACTION_EVIDENCE_PRESENT: two dispatch documents and local gate outputs |
| invocationBoundary | local read/write and gates only |
| interceptionBoundary | no wrapper, proxy or runtime interception |
| claimLanguage | source evidence justifies re-evaluation, not implementation |
| forbiddenExpansion | source/test/runtime/provider/live/public/deploy/production |

## Claim Boundary

Worker may decide only. Worker must not implement, stage, commit, call a
provider, edit continuity or open a successor.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision rework.
