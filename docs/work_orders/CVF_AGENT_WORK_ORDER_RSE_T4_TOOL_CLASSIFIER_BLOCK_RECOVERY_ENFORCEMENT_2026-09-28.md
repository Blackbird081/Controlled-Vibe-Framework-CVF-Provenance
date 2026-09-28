# CVF Agent Work Order - RSE-T4 Tool Classifier Block Recovery Enforcement

Memory class: governed-worker-dispatch

docType: work_order

Status: CLOSED_BLOCKED_BOUNDED

Batch ID: RSE-T4-H1

Dispatch base head: `91a98b2d8`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: one shared-workspace `INTERNAL_AGENT` worker.

Reviewer/closer: Local orchestrator/reviewer.

Worker return path: `docs/reviews/CVF_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_WORKER_RETURN_2026-09-28.md`

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT governance-hardening worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_2026-09-28.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: worker captures clean committed dispatch HEAD.

Current-time notes: packet date is 2026-09-28; no external invocation is authorized.

Do-not-misread notes: this packet governs recovery routing and evidence. It does not disable classifiers, suppress platform dialogs, authorize automatic retry outside the worker's control, reopen NCR, or grant runtime/provider/public effects.

Required first actions: read startup surfaces, guard orientation, literal gotchas, paired baseline, ADIF-0061, RSE T1-T3 owners, the work-order template, all six implementation sources and their focused tests; capture clean HEAD/status and pass pre-implementation before editing.

Return contract: leave exactly the twelve worker-owned paths uncommitted with empty staging; return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` to Local. Do not ask the operator a technical implementation question.

## Purpose

Implement the smallest reusable CVF control that handles tool/classifier edit
blocks without routing ordinary technical recovery to the operator. Add a
canonical RSE-T4 contract, project it through both scaffolds, enforce dispatch
and return evidence with existing gates, and prove positive/negative/hostile
cases locally.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id RSE-T4-H1 --title "Tool Classifier Block Recovery Enforcement" --date 2026-09-28 --base 91a98b2d8 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --root-cause-cluster-id NOT_APPLICABLE_INITIAL_DISPATCH --prior-finding-set-digest NOT_APPLICABLE_INITIAL_DISPATCH --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence NONE --scec-problem-key RSE-TOOL-CLASSIFIER-BLOCK-RECOVERY --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition ROOT_CONTRACT_REQUIRED --scec-successor-scope NO_SUCCESSOR --stdout` |
| generatedProfile | protected-governance-path plus WORKER_MUST_NOT_COMMIT |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, exact scope, recovery semantics, closeability, tests and claim boundary |
| checkerReadAheadConfirmation | all named checker/source/test paths must be read before mutation |
| docOnlyNewFields | fields in Tool / Classifier Block Recovery Contract and return Event block |
| claimBoundary | scaffold provenance only; no external runtime behavior claim |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: RSE-T4-H1
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: INITIAL_DISPATCH
rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: REQUIRED_TRIGGERED
preExecutionReviewTrigger: OPERATOR_EXPLICIT_REQUEST
nextRoutineReviewBoundary: PRE_EXECUTION_REVIEW
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"RSE-TOOL-CLASSIFIER-BLOCK-RECOVERY","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"RSE-T4-RECOVERY-ENFORCEMENT","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0061.md"}],"requiredDisposition":"ROOT_CONTRACT_REQUIRED","successorScope":"NO_SUCCESSOR"}
```

## Authority Chain

Operator instruction -> S11 blocked completion `6a8545e64` -> ADIF-0061 ->
paired RSE-T4 baseline/work order -> one worker -> Local independent review.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"RSE-T4-H1","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"CREATES_OR_CHANGES_AUTHORITY","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"NEW_AUTHORITY"},"pathFamilies":["docs/baselines/","docs/reference/role_switch_envelope/","docs/reference/","governance/compat/","docs/reviews/"],"claims":["dispatch packets declare tool/classifier recovery applicability","applicable worker returns report classifier-block events"],"requiredProof":["focused hostile tests","scaffold output assertions","dispatch checker pass","worker-return checker pass","reviewer-fast"],"operatorCheckpoints":[],"forbiddenEffects":["classifier bypass","platform prompt suppression claim","provider call","NCR mutation","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0061.md","completenessClaimChanged":false}}
```

## Scope And Maximum Worker Path Manifest

The worker may modify/create exactly these twelve paths and no others:

1. `docs/reference/role_switch_envelope/CVF_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ADDENDUM.md`
2. `docs/reference/role_switch_envelope/README.md`
3. `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
4. `governance/compat/build_dispatch_packet_scaffold.py`
5. `governance/compat/test_build_dispatch_packet_scaffold.py`
6. `governance/compat/build_worker_return_skeleton_scaffold.py`
7. `governance/compat/test_run_worker_return_scaffold.py`
8. `governance/compat/check_dispatch_prompt_envelope.py`
9. `governance/compat/test_check_dispatch_prompt_envelope.py`
10. `governance/compat/check_worker_return_quality_gate.py`
11. `governance/compat/test_check_worker_return_quality_gate.py`
12. `docs/reviews/CVF_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_WORKER_RETURN_2026-09-28.md`

No rename/delete. Existing governed files at or above a size threshold must be
byte-neutral or smaller after the change unless their active file-size policy
explicitly permits growth.

## Work-Order Fulfillment Manifest

| Requirement | Worker deliverable | Proof |
|---|---|---|
| canonical recovery semantics | RSE-T4 addendum and README route | reference gates |
| future packet emission | template plus dispatch scaffold | scaffold focused tests |
| durable event capture | worker-return scaffold | worker scaffold tests |
| early admission | dispatch envelope checker | positive/negative/hostile tests |
| return-time evidence | worker-return quality checker | event-count and forced-prompt tests |
| bounded handoff | worker return | fast gate and exact manifest |

## Required Artifact Manifest

| Path | Required at worker handoff | Rule |
|---|---|---|
| `docs/reference/role_switch_envelope/CVF_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ADDENDUM.md` | YES | canonical recovery semantics |
| `docs/reference/role_switch_envelope/README.md` | YES | route canonical addendum |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | YES | future packet contract |
| `governance/compat/build_dispatch_packet_scaffold.py` | YES | emit applicability and applicable block |
| `governance/compat/test_build_dispatch_packet_scaffold.py` | YES | dispatch scaffold coverage |
| `governance/compat/build_worker_return_skeleton_scaffold.py` | YES | emit classifier event block |
| `governance/compat/test_run_worker_return_scaffold.py` | YES | return scaffold coverage |
| `governance/compat/check_dispatch_prompt_envelope.py` | YES | early admission enforcement |
| `governance/compat/test_check_dispatch_prompt_envelope.py` | YES | positive/negative/hostile dispatch fixtures |
| `governance/compat/check_worker_return_quality_gate.py` | YES | event evidence enforcement |
| `governance/compat/test_check_worker_return_quality_gate.py` | YES | positive/negative/hostile return fixtures |
| `docs/reviews/CVF_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_WORKER_RETURN_2026-09-28.md` | YES | exact evidence, commands, manifest and no-commit statement |

## Required Root Contract

The canonical dispatch block is `## Tool / Classifier Block Recovery Contract`
with these exact scalar fields:

```text
toolClassifierBlockRecoveryApplicability: APPLICABLE | NOT_APPLICABLE_WITH_REASON: <reason>
workerAuthoredOperatorQuestionAllowed: NO
platformForcedPromptBoundary: RECORD_NOT_SUPPRESS
atomicEditPreparationRequired: YES
workerControlledEditRetryCeiling: 1
retryScope: SAME_SEMANTIC_EDIT_NO_SCOPE_CHANGE
exhaustedRecoveryRoute: BLOCKED_WITH_REASON_TO_LOCAL
classifierEventCaptureRequired: YES
```

When applicability is `APPLICABLE`, all remaining values above are mandatory.
The one retry applies only when the worker actually regains control and can
submit a smaller semantically equivalent edit; it grants no provider, network,
business-action or hidden retry authority. If a platform forces operator UI,
the worker records it and does not claim suppression.

Every checker-safe worker-return scaffold emits
`## Tool / Classifier Block Event` with:

```text
toolClassifierBlockEventCount: 0
platformForcedOperatorPromptCount: 0
workerAuthoredOperatorQuestionCount: 0
recoveryAttemptCount: 0
recoveryDisposition: NO_EVENT
eventEvidence: NOT_APPLICABLE_WITH_REASON - no classifier block observed
```

Nonzero counts require a bounded path/field, classifier label, recovery
attempt count and final route without secret/prompt payload disclosure.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| operator-question classification | `docs/reference/role_switch_envelope/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_ADDENDUM.md` | classification table | operator-question decision table | RSE-T1 | ACCEPT |
| worker-return jurisdiction | `docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md` | block fields | worker-return jurisdiction block | RSE-T2 | ACCEPT |
| current return-time diagnostic | `governance/compat/run_agent_automation_assist.py` | `_build_jurisdiction_readout` | return-time jurisdiction readout | RSE-T3 | ACCEPT |
| dispatch envelope checker | `governance/compat/check_dispatch_prompt_envelope.py` | `validate_work_order` | dispatch work-order validation | dispatch gate | ACCEPT |
| worker-return checker | `governance/compat/check_worker_return_quality_gate.py` | return validation | worker-return packet validation | worker-return gate | ACCEPT |
| scaffold owners | `governance/compat/build_dispatch_packet_scaffold.py`; `governance/compat/build_worker_return_skeleton_scaffold.py` | emitted work order/return sections | scaffold output builders | scaffold owners | ACCEPT |
| exact defect | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0061.md` | Remediation | ADIF-0061 | ADIF | ACCEPT |

## Negative Search And Collision Discipline

Target-path and token searches are recorded in the paired baseline. No active
owner currently defines the exact contract fields; RSE-T1/T2/T3 remain composed
authority and are not replaced.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | recurring tool/classifier block escalated a technical choice to operator |
| scope classification | private governance docs, scaffolds, checkers and tests |
| risk sensitivity | protected governance paths; no external effects |
| selected role route | one INTERNAL_AGENT worker then Local reviewer |
| escalation condition | source contradiction, thirteenth path, required behavior outside local tooling, or inability to preserve file-size policy |
| canonical route mode | SINGLE_AGENT_SINGLE_ROLE |
| decision owner | Local |

## Required First Reads And Pre-Flight

Read startup surfaces, guard orientation, literal gotchas, paired packet,
ADIF-0061, RSE T1-T3, work-order template, all twelve target files that exist,
and applicable checker/file-size sources. Capture clean HEAD/status and run:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_2026-09-28.md
```

## Agent Roles

- Dispatcher: Local authors, validates and releases the exact packet.
- Worker: implements the exact twelve-path scope and returns without commit.
- Reviewer/closer: Local evaluates returned evidence, runs the independent probe and owns material disposition.
- Session-sync steward: Local updates continuity only after material disposition.

## Write Ownership

Write mode: modify-listed/create-listed only for the exact twelve paths.
Everything else is forbidden. `WORKER_MUST_NOT_COMMIT`; no stage, stash,
commit, push, provider call, public sync or deployment.

## Execution Plan

1. Add the bounded RSE-T4 addendum and route it from the RSE README.
2. Replace/extend the template and dispatch scaffold so every future executable
   packet declares applicability; applicable packets receive the exact contract.
3. Extend the worker-return scaffold with the six event fields.
4. Extend the dispatch checker and worker-return quality checker without
   duplicating RSE semantics across two independent implementations; use shared
   constants/helpers inside the authorized existing sources if useful.
5. Update existing focused tests with positive, negative and hostile fixtures:
   missing applicability; incomplete applicable block; N/A with real reason;
   zero-event return; classifier event with platform-forced prompt; forbidden
   worker-authored operator question; exhausted recovery routed to Local.
6. Run focused and governance gates, reconcile exact paths and return.

## Verification Commands

```powershell
python -m pytest governance/compat/test_build_dispatch_packet_scaffold.py governance/compat/test_run_worker_return_scaffold.py governance/compat/test_check_dispatch_prompt_envelope.py governance/compat/test_check_worker_return_quality_gate.py -q
python governance/compat/check_dispatch_prompt_envelope.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_worker_return_quality_gate.py --enforce --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_2026-09-28.md
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_2026-09-28.md
git diff --check
git diff --name-status
git diff --cached --name-status
git status --short --untracked-files=all
```

Every command must pass. Do not substitute individual checks for the final
worker-return fast gate.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | twelve worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | six sources and four test sources | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | worker return | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted twelve-path set | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | completion review | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material set | EXACT_PATHS | closer | MATERIAL_COMMIT | terminal_completion_review |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | material and continuity ranges | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | INTERNAL_AGENT worker -> Local reviewer/closer |
| phase | RSE_T4_LOCAL_GOVERNANCE_HARDENING |
| baseHeadFor(phase) | dispatchBaseHead=`91a98b2d8`; executionBaseHead=worker capture; closureBaseHead=Local-set |
| changedSetScope(phase) | exact twelve paths |
| traceScope(phase, actor) | contract/scaffold/checker/test diffs and command evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; Local owns commit |
| crossBatchIsolation | NCR and unrelated dirty paths remain untouched |
| nextMoveSurfaces | worker return to Local only |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: one INTERNAL_AGENT worker after committed release
laneOwnedPaths: exactly the twelve paths above
dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE
laneReleaseEvidence: terminal return, exact manifest and empty staging

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH` |
| Returned defect count | 10 (bounded resolver result; truncated=true) |
| Returned defects | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044 |
| Disclosed defectIds | returned top ten plus origin ADIF-0061 |
| Dispatch impact | ADIF-0033 requires protected-path authorization; ADIF-0020 requires checker read-ahead; ADIF-0061 supplies the recovery contract objective |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch status; applicability declaration; worker-return status; protected paths; exact trace labels; size/no-growth enforcement |
| gateRunPurpose | confirmation after source-first packet authoring |
| claimBoundary | local structural enforcement only; no platform prompt suppression claim |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_WORKER_RETURN_2026-09-28.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_2026-09-28.md`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Decision; Tool / Classifier Block Event;
Claim Boundary; Checker Source Read-Ahead Block; Agent Operation Trace Block;
Delta Execution Claim Boundary Control Block; Public Export Disposition;
executionBaseHead; git status --short; Command Evidence; No-Commit Statement.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_COMPLETION_2026-09-28.md` if Local needs a separate correction/closure artifact |
| reviewerOwnedClosurePaths | completion review and continuity only; not worker-owned |
| closureOwner | Local reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Autonomy / No-Question Rule

Repair allowed-scope failures directly. A source contradiction or impossible
scope returns `BLOCKED_WITH_REASON` to Local. A tool/classifier block follows
the Required Root Contract; it never becomes a worker-authored operator
question. A platform-forced prompt is recorded, not claimed suppressed.

## Tool / Classifier Block Recovery Contract

toolClassifierBlockRecoveryApplicability: APPLICABLE
workerAuthoredOperatorQuestionAllowed: NO
platformForcedPromptBoundary: RECORD_NOT_SUPPRESS
atomicEditPreparationRequired: YES
workerControlledEditRetryCeiling: 1
retryScope: SAME_SEMANTIC_EDIT_NO_SCOPE_CHANGE
exhaustedRecoveryRoute: BLOCKED_WITH_REASON_TO_LOCAL
classifierEventCaptureRequired: YES

## Dual Agent Surface Matrix

| Consumer | Interface | Boundary | Evidence | Disposition |
|---|---|---|---|---|
| INTERNAL_AGENT | governed files, scaffolds and local checkers | documentation/local deterministic validation only | focused tests and return | IMPLEMENTED_BY_TRANCHE_IF_ACCEPTED |
| EXTERNAL_AGENT_CLI_MCP | none | no adapter, remote execution or platform interception | explicit boundary | DEFERRED_WITH_REASON |

## High-Risk Local Transaction Proof Applicability

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - this local documentation/scaffold/checker tranche authorizes no concurrent writer, durable external-state transaction, filesystem ownership/DACL mutation, or post-acquire failure handling.

## Independent Review Probe Admission Contract

independentProbeRequired: YES
independentProbeRiskClass: PROTECTED_GOVERNANCE_CHECKER_AND_SCAFFOLD_CHANGE
independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER
implementationOracleSeparation: worker uses focused unit fixtures; Local independently invokes both checkers against temporary positive and hostile artifacts without reusing worker assertions
positiveControl: applicable dispatch and zero-event return pass with exact canonical values
negativeMutationClasses: missing applicability, incomplete applicable block, worker-authored operator question, inconsistent counts, false platform-suppression claim, exhausted recovery not routed Local
expectedInformationGain: prove both earliest dispatch admission and return-time event evidence enforce one shared RSE contract
rerunCostReason: provider-free temporary local fixtures; bounded high-value independent semantic probe
reviewerDecisionOwner: LOCAL

## Current Runtime Freshness Verification

runtimeClaimPresent: NO_WITH_REASON - local documentation/scaffold/checker behavior only.

The external tool classifier is not a repository runtime owner. This tranche
records the S11 signal through ADIF-0061 and does not claim access to or control
over the platform classifier implementation.

The current provider-registry surface remains
`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and
`PROVIDER_CAPABILITY_REGISTRY`; this local blocked tranche neither changes nor
claims absence of those surfaces.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: modify exactly the template, two scaffolds,
two existing checkers and their four focused test files named in the manifest,
plus RSE reference/README and worker return.

Protected paths:

- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`
- `governance/compat/build_worker_return_skeleton_scaffold.py`
- `governance/compat/test_run_worker_return_scaffold.py`
- `governance/compat/check_dispatch_prompt_envelope.py`
- `governance/compat/test_check_dispatch_prompt_envelope.py`
- `governance/compat/check_worker_return_quality_gate.py`
- `governance/compat/test_check_worker_return_quality_gate.py`

Operator authorization: operator explicitly instructed Local to park NCR after
review and harden the CVF foundation for this recurring error.

Rollback boundary: restore only these RSE-T4 worker changes to the committed
dispatch HEAD if rejected; preserve S11 closure `6a8545e64`, continuity
`91a98b2d8`, ADIF-0061 and all prior RSE/NCR history.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation surface | existing RSE references, work-order template, scaffolds and gates |
| Storage decision | update existing owners; add one versioned RSE addendum only |
| Stable filename disposition | exact addendum and worker-return paths in manifest |
| Generated aggregate discipline | none added |
| Authority boundary | addendum owns semantics; gates validate shape; platform remains external |
| Forbidden expansion | no new root, daemon, proxy, interceptor, runtime adapter or provider behavior |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF workspace |
| Session or invocation | RSE-T4 packet authoring, 2026-09-28 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, ADIF resolver, scaffold stdout, `apply_patch`, Git |
| Target paths | paired RSE-T4 baseline and work order |
| Allowed scope source | operator instruction, S11 completion and ADIF-0061 |
| Before status evidence | clean worktree at HEAD `91a98b2d8`; NCR parked |
| After status evidence | paired packet pending validation/commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | exact local governance-hardening dispatch only |
| Claim boundary | no implementation/provider/runtime/public effect during authoring |
| Agent type | INTERNAL_AGENT Local orchestrator/reviewer |
| Invocation ID | `rse-t4-work-order-author-20260928` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order only at authoring |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | local RSE contract, scaffold and checker enforcement |
| claimDisposition | CLAIM_REJECTED: no direct runtime enforcement or platform interception is claimed |
| receiptEvidence | N/A with reason: deterministic governance tests only |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no external action |
| invocationBoundary | cooperating agents that consume governed packets/scaffolds |
| interceptionBoundary | no IDE, tool, filesystem, shell, provider or platform interception |
| claimLanguage | packet-shape and return-evidence enforcement only |
| forbiddenExpansion | classifier bypass, automatic external prompt handling, NCR, provider/live, public/deploy |

## Epistemic Process Block

Epistemic Process Applicability: GOVERNANCE_MACHINE_HARDENING.

Expected Result / Prediction: a shared explicit contract plus dispatch/return
gates should prevent future packets from silently omitting recovery routing and
should force durable capture when a classifier-block event reaches a return.

Evidence Comparison Requirement: worker compares generated scaffold text and
positive/hostile checker results against every Root Contract row.

Contradiction Handling Requirement: if an existing gate cannot enforce the
contract without false positives or file-size violation, return blocked with
the exact source/fixture evidence; do not invent runtime interception.

Claim Update Requirement: distinguish local enforcement achieved from external
platform behavior still outside CVF control.

## Acceptance Criteria

- RSE addendum and README establish one canonical contract and non-suppression boundary.
- Template and both scaffolds emit the required declarations/event fields.
- Dispatch checker rejects missing/incomplete applicable blocks and accepts reasoned N/A.
- Worker-return checker rejects inconsistent/noncompliant event evidence.
- Focused positive, negative and hostile tests pass.
- Existing tests remain green; governed file-size gates pass without debt growth.
- Exact twelve paths, empty staging, no commit/provider/network/public action.

## Dated Owner Dependency Discovery

| Owned dated reference path | Classification | Registry evidence | Disposition |
|---|---|---|---|
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | `NOT_BINDING_REFERENCE_WITH_REASON: existing governed template is an edited source owner in this bounded material set, not a newly released dated dependency` | AGENTS.md task routing and dispatch-quality checker | ACCEPT |

## Evidence Requirements

- pre-implementation PASS at the committed dispatch base;
- generated dispatch and return scaffolds containing the canonical blocks;
- focused positive, negative and hostile test results;
- dispatch and worker-return checker PASS results;
- exact twelve-path dirty set, empty staging and no external invocation;
- worker return containing the event block even when all counts are zero.

## Review Gate

Implementation begins only after committed packet/continuity binding and exact
pre-implementation PASS. Closure requires worker-return fast PASS, Local's
independent positive/hostile probe, reviewer-fast PASS, terminal completion
review and material pre-commit PASS. Worker handoff is not closure.

## Closure Checklist

- RSE addendum owns one canonical recovery meaning and platform boundary.
- Template and both scaffolds emit the required fields.
- Both gates reject missing or contradictory evidence through hostile tests.
- Local independent probe confirms dispatch-time and return-time enforcement.
- Exact worker manifest is reconciled and staging remains empty.
- Material and continuity commits remain separate; NCR stays parked.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for source contradiction, thirteenth path, required
new checker/hook/catalog path, file-size debt growth, inability to preserve
existing behavior, or platform/runtime implementation need. Do not ask the
operator to choose a technical repair.

## Operator Checkpoint

NOT_REQUIRED_WITH_REASON: the operator already delegated Local authority to
park NCR and harden this recurring governance defect. This tranche has no
provider, network, public, deployment, expense or business-action effect; all
technical contradictions return to Local as `BLOCKED_WITH_REASON`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance hardening; no public-sync authority.

## Claim Boundary

This order authorizes exact local RSE documentation, scaffold, checker and test
changes. It does not guarantee that an external platform will stop prompting,
weaken a safety classifier, automate UI choices, reopen NCR, call a provider,
publish, deploy or establish universal agent compliance.

Closure note: Local rejected `COMPLETE_PENDING_REVIEW`; the mandatory template
deliverable was reverted and an independent hostile probe found four checker
false negatives. Returned implementation sources were restored to dispatch
base; only review evidence is retained.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_BLOCKED_BOUNDED` | PASS |
| Completion or reviewer artifact | named completion and worker return | rejection, rollback and evidence retention | PASS |
| Roadmap state | N/A with reason: foundation defect tranche | NCR remains parked; corrective packet required | N/A with reason |
| Registry JSON | GC-051 registry | no classification/corpus registry mutation authorized by this blocked tranche | BLOCKED with reason |
| Registry Markdown | GC-051 registry companion | no classification/corpus registry mutation authorized by this blocked tranche | BLOCKED with reason |
| External evidence digest | N/A with reason: no provider call | providerCallCount 0 | N/A with reason |
| System loop interlock | named completion | incomplete implementation cannot activate | PASS |
| Session continuity | active handoff/state | separate continuity commit follows material commit | N/A with reason |
| Completion review | `docs/reviews/CVF_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_COMPLETION_2026-09-28.md` | reviewer rejection and restore | PASS |
| Worker return | named worker return | retained; claimed completion rejected | PASS_WITH_BLOCKED_DISPOSITION |
| Independent probe | `docs/reviews/evidence/rse-t4-h1-independent-probe-2026-09-28.json` | four semantic false negatives | BLOCKED |
| Source manifest | returned implementation sources | restored to dispatch base | PASS |
| Corrective successor | fresh committed packet | not auto-opened by this closure | BLOCKED |
