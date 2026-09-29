# CVF Agent Work Order - GC010 SCR-R2-T1J-R2 Approval Resume Atomic Claim Durable Owner Decision

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Batch ID: GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION

Dispatch base head: `ab3d1075c00446dafbd7af4d6737e012a88d41e4`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: orchestrator/reviewer

Worker return path: `docs/reviews/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_WORKER_RETURN_2026-08-31.md`

## Dispatch Prompt Envelope

Role: delegated decision worker for `GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION`.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_2026-08-31.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-08-31; verify current HEAD and source before deciding.

Do-not-misread notes: decision-only; no code/test/route/store edit, provider call, T1K or T2 is authorized.

Required first actions: read the startup front door and bootstrap model, active handoff, guard orientation, literal gotchas, paired baseline, this work order, all named source, and applicable checker source before authoring.

Return contract: create exactly the assessment and worker return, run required gates, leave both uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

providerExecutionAuthority: FORBIDDEN

## Purpose

Select the smallest safe durable owner for atomic approval-resume claim and
recovery while retaining `/api/execute` as the only guard/provider pipeline.
Do not assume that early deletion is safe or that using the pending runtime
necessarily requires a second route.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: EXTERNAL_AGENT_CLI_MCP
parentAssignmentId: GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 1
usageAvailability: KNOWN_FOR_ADMISSION
quotaAdmissionDisposition: ADMITTED_WITHIN_CUMULATIVE_CEILING
nextDispatchDisposition: INITIAL_DISPATCH
rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

## Scope / Target / Owner Boundary

Target only the owner decision left by accepted T1J-R1. Trace current source
from approval creation through validation, claim, guard, admission, provider
attempt, terminal outcome and recovery. Compare the four baseline candidates.
All current source, tests, packages, scripts, continuity and governance files
are read-only.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator continuation | Current operator instruction `next` | ACCEPT |
| Accepted prerequisite | T1J-R1 material `35226ccf785a1092e6d3009c98e5865e5174a4f9` | ACCEPT |
| Current continuity | mode `gc010_scr_r2_t1j_r1_closed_partial_ready_durable_owner_decision_required` | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_2026-08-31.md` | ACCEPT |

## Agent Roles

- Operator authorizes this bounded decision and later checkpoints.
- Dispatcher authors and commits the packet.
- Worker performs source verification and writes exactly two documents.
- Reviewer/closer independently accepts, repairs or rejects the return.
- Session-sync steward updates continuity only after review closure.

## Required First Reads

Read `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`,
`CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V59_2026-08-11.md`, the paired
baseline, this work order, every source path in Source Verification, guard
orientation, literal gotchas, and applicable worker-output checkers.

## Pre-Flight Checks

Capture full `git rev-parse HEAD`; confirm it equals the committed dispatch
HEAD at worker start; confirm `git status --short --untracked-files=all` is
clean; confirm both output paths do not exist; run the pre-implementation gate
before authoring.

## Write Ownership

Worker may create only:

1. `docs/assessments/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_2026-08-31.md`
2. `docs/reviews/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_WORKER_RETURN_2026-08-31.md`

No existing file may change. Worker must not stage or commit.

## Execution Plan

1. Recompute current source facts; do not inherit T1J-R1 prose blindly.
2. Trace all four candidate lifecycles and every pre/post-provider failure.
3. Answer all mandatory questions and select exactly one terminal.
4. Write the two authorized documents, run the fast gate and stop.

## Evidence Requirements

Every runtime claim must cite a current repo path plus symbol or section.
Distinguish atomic file replacement from transactional record claim. Separate
single-node multi-process guarantees from distributed guarantees. Record zero
provider/network/browser/credential/live calls.

## Acceptance Criteria

- Four candidates and twelve mandatory questions are complete.
- Exactly one durable owner or parked result is selected.
- Claim, retry, rollback, crash ambiguity and terminal ownership are explicit.
- A smallest future implementation manifest is named only for the selected
  ready terminal.
- Exactly one allowed terminal is present and `successorTrancheOpened: NO`.
- Worker-return fast gate is `COMPLIANT`; HEAD is unchanged; exact two-file
  untracked manifest is recorded.

## Review Gate

Reviewer must independently verify source semantics, especially whether the
selected design prevents concurrent double execution and preserves a defined
state across every failure window. Structural gate success is insufficient.

## Closure Checklist

- [ ] Exact two-path manifest.
- [ ] Source verification current at execution base.
- [ ] No exactly-once overclaim.
- [ ] One guard and one provider-admission owner preserved.
- [ ] Durable path/configuration and cleanup owners named.
- [ ] Terminal and successor token valid.
- [ ] Worker did not stage or commit.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` only for a current-source contradiction, missing
authority requiring a forbidden edit/effect, or unavoidable worktree drift.
Otherwise finish the bounded decision without routine questions.

## Operator Checkpoint

Even a ready owner terminal permits only reviewer consideration of a later
T1K implementation packet. No implementation opens automatically.

## Worker Autonomy / No-Question Rule

Repair allowed-scope document/checker defects directly. Do not widen scope or
ask preference questions. Stop on a genuine return condition.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "GC010-SCR-R2-T1J-R2",
  "requestedProfile": "P2_BOUNDED",
  "classification": {
    "taskKind": "DOC_CHANGE",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": ["docs/baselines", "docs/work_orders", "docs/assessments", "docs/reviews"],
  "claims": ["current source can support one bounded durable-owner decision without implementation"],
  "requiredProof": ["four-candidate comparison", "twelve decision answers", "exact terminal", "independent review"],
  "operatorCheckpoints": ["source contradiction", "implementation successor", "provider/live", "public sync", "deployment"],
  "forbiddenEffects": ["source edit", "test edit", "worker commit", "provider call", "network call", "public write", "deployment", "automatic successor"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

## Intake Role Routing Decision

routeMode: MULTI_AGENT_MULTI_ROLE
intakeSummary: bounded current-source durable-owner decision
scopeClassification: DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT
riskSensitivity: high because an incorrect claim owner can permit duplicate provider effects or lose resume authority
escalationCondition: source contradiction, forbidden implementation need, dirty overlap, or missing binding authority

The selected role route is one operator-mediated external decision worker
followed by independent local orchestrator/reviewer closure. Provider/live and
public/export routes are forbidden.

## Required Artifact Manifest

Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/assessments/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_2026-08-31.md` | CREATE decision assessment, comparison, questions, terminal and future manifest if ready |
| `docs/reviews/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_WORKER_RETURN_2026-08-31.md` | CREATE checker-safe pending return |

## Mandatory Decision Questions

1. What atomicity does `ApprovalStore` provide today, and what does atomic
   file replacement not guarantee across concurrent callers or processes?
2. What exact race exists from approval validation to deletion and provider
   admission?
3. If approval is consumed before later validation/configuration/admission,
   how is a pre-provider failure retried or rolled back safely?
4. If a provider call starts but the process crashes before response/terminal
   persistence, which state prevents silent replay?
5. What creation point and identifier bind an approval record to a pending
   execution without drift or two uncoordinated truths?
6. Can the existing approval store be extended with enough lifecycle state
   without rebuilding the pending core? Name exact states and CAS boundary.
7. Can the pending runtime be composed inside `/api/execute` without a second
   guard, provider admission or route? Name exact call order.
8. Does pending composition duplicate durable approval facts, or can immutable
   approval binding and mutable execution lifecycle have distinct owners?
9. Where do `APPROVAL_CONSUMED`, begin, provider-attempt and terminal evidence
   occur, and what ordering is safe?
10. Who owns SQLite path/configuration, runtime lifetime, connection closure,
    stale/expired cleanup and single-node process safety?
11. What is the smallest exact future source/test manifest for each viable
    owner, including concurrency and crash-window negative tests?
12. Which terminal is supported, and why is every alternative defeated?

## Required Candidate Comparison

Compare exactly: existing approval-store atomic lifecycle; narrow in-route
pending-runtime lifecycle; minimal atomic consume-before-work; and retain
parked. A separate approval-resume route with its own guard/provider pipeline
is outside the candidate set because T1J-R1 already rejected it.

## Terminal Contract

Select exactly one baseline terminal and keep `successorTrancheOpened: NO`.
Ready means a later T1K decision may be authored by the orchestrator; it does
not authorize implementation.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Approval store lacks CAS/lifecycle transitions | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` | `ApprovalStore` implementation | Map methods and `persist` | approval store | ACCEPT |
| Execute route separates approval validation, deletion and provider admission | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | approval validation; `APPROVAL_CONSUMED`; provider attempt | `approvedRequestRecord`; `admitAndInvokeProvider` | `POST` | ACCEPT |
| Pending core owns CAS lifecycle and ambiguous crash terminal | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | store/claim/begin/terminal functions | `compareAndSwap`; `resolveAmbiguousExecutingCrash` | pending core | ACCEPT |
| SQLite adapter implements IMMEDIATE-transaction conditional CAS | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts` | `compareAndSwap` | `runCas.immediate()` | SQLite store | ACCEPT |
| Composition module exposes bounded lifecycle and caller-supplied dbPath | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-composition.ts` | runtime interface/builder | `buildPendingAgentExecutionRuntime` | composition owner | ACCEPT |
| T1J-R1 accepted caller evidence but left durable owner open | accepted assessment | `docs/assessments/CVF_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_2026-08-31.md` | Decision; Independent Reviewer Correction | partial-ready terminal | T1J-R1 | ACCEPT |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
```

No runtime test or provider call is required; this is source-backed decision
work.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_WORKER_RETURN_2026-08-31.md`
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
| phase | T1J-R2 durable-owner decision |
| baseHeadFor(phase) | dispatchBaseHead=`ab3d1075c00446dafbd7af4d6737e012a88d41e4`; executionBaseHead=worker capture; closureBaseHead=reviewer set |
| changedSetScope(phase) | exactly two worker documents |
| traceScope(phase, actor) | source reads, commands, exact manifest and zero external effects |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer owns commits |
| crossBatchIsolation | all unrelated paths remain unchanged |
| nextMoveSurfaces | reviewer updates continuity only after acceptance |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | orchestrator/reviewer | verifies and closes decision only | paired baseline/work order and current source | N/A with reason: internal review uses repository artifacts directly | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | operator-mediated delegated worker | two-file decision return; no runtime/provider authority | exact manifest and no-commit contract | file-return adapter boundary; external output remains non-authoritative until review | `DEFERRED_WITH_REASON` |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_COMPLETION_2026-08-31.md` (optional; reviewer creates only if necessary) |
| reviewerOwnedClosurePaths | material commit, then continuity-only commit |
| closureOwner | orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`decision assessment`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | ready status, source rows, convergence scalars, handoff fields, dual-agent columns, trace labels and no-commit terms |
| gateRunPurpose | Confirmation after source-led authoring. |
| claimBoundary | Gate shape cannot select the durable owner. |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION --title "GC010 SCR R2 T1J R2 Approval Resume Atomic Claim Durable Owner Decision" --date 2026-08-31 --base ab3d1075c00446dafbd7af4d6737e012a88d41e4 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added durable-owner candidates, twelve questions, source evidence, terminal and exact manifest. |
| checkerReadAheadConfirmation | Applicable checker sources inspected before material authoring. |
| docOnlyNewFields | Durable lifecycle owner and crash-window comparison. |
| claimBoundary | Provenance only; no runtime behavior is changed. |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | GC010 T1J-R2 dispatch, 2026-08-31 |
| Working directory | repository root |
| Command or tool surface | source reads, `rg`, scaffold helper, `apply_patch`, governance gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | operator instruction `next` and accepted T1J-R1 next checkpoint |
| Before status evidence | clean worktree at `ab3d1075c00446dafbd7af4d6737e012a88d41e4` |
| After status evidence | paired dispatch documents only before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | decision dispatch only |
| Claim boundary | no implementation or external effect |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `gc010-t1j-r2-dispatch-2026-08-31` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | documentation-only durable-owner decision dispatch |
| claimDisposition | CLAIM_REJECTED: no runtime behavior is claimed |
| receiptEvidence | N/A with reason: no runtime receipt is created |
| actionEvidence | ACTION_EVIDENCE_PRESENT: two dispatch documents and local gate outputs |
| invocationBoundary | local source read, document write and gates only |
| interceptionBoundary | no wrapper, proxy or runtime interception |
| claimLanguage | source evidence authorizes a decision, not implementation |
| forbiddenExpansion | source/test/runtime/provider/live/public/deploy/production |

## Claim Boundary

Worker may decide only. Worker must not implement, stage, commit, call a
provider, edit continuity, open T1K/T2 or claim production readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision dispatch.
