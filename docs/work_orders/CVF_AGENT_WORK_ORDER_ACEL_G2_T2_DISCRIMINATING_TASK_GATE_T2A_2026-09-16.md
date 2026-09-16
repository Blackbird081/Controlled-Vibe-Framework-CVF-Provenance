# CVF Agent Work Order - ACEL G2 T2 Discriminating Task Gate T2A

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-16

Batch ID: ACEL-G2-T2-DISCRIMINATING-TASK-GATE-T2A

dispatchBaseHead: `253751977ee3a68f5360fec4b731d22635160bee`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: one INTERNAL_AGENT implementation worker

Reviewer/closer: Local

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT offline contract/quality-gate worker in the shared CVF
workspace. Local is the independent reviewer/closer and final technical
decision owner.

Canonical packet: this work order and
`docs/baselines/CVF_GC018_ACEL_G2_T2_DISCRIMINATING_TASK_GATE_T2A_2026-09-16.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: this is an offline 2026-09-16 design tranche; no quota
snapshot or prior live grant is reusable authority.

Required first actions: rehydrate startup/handoff, read guard orientation and
literal gotchas, capture exact clean HEAD/status, verify the source and owned
paths, run pre-implementation before edits.

Do-not-misread notes: create an executable offline task/grader, not a new
provider result. T6A 100/100 does not qualify T6B; no external or internal
agent, model, API key, network, live runner, MAO composition, runtime-topology
consumer, public sync or deployment is permitted.

Return contract: exactly four worker-owned paths, uncommitted and unstaged;
return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` with actual gate
evidence. Do not claim that offline fixtures prove real-agent difficulty.

providerExecutionAuthority: FORBIDDEN

## Purpose

Build a frozen, deterministic and adversarially tested G2-T2 candidate task
with a quality gate that can be independently applied to a future direct
agent response. Make it materially different from the trivial 100/100 T6A
task while preserving immutable authority and fail-closed evidence behavior.

## Agent Roles

INTERNAL_AGENT is the sole worker and owns exactly the four output paths.
Local is independent reviewer/closer, owns material and continuity commits,
and may repair bounded reviewer-owned shape defects. The operator owns any
future provider/live or actual-agent trial checkpoint. External Web/CLI/MCP
agents are not invoked.

## Required First Reads

Read `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`,
`CVF_SESSION_MEMORY.md`, active handoff, paired baseline, this work order,
`docs/reference/guard_orientation/README.md`, literal-format gotchas, the
five Source Verification rows and the applicable worker-output checkers.

## Pre-Flight Checks

Record exact clean HEAD/staging, target-path absence, Node/tsx/vitest
availability, source hashes and the current owner of task/scorer behavior.
Run the pre-implementation gate before the first edit. Stop if any worker
path is already occupied or if a required source contradicts the packet.

## Write Ownership

Exactly the four paths in Required Artifact Manifest. Mandatory gate defects
within those owned paths are worker-owned and repaired without asking the
operator. Any fifth path requires Local scope review before mutation.

## Authority Chain

| Layer | Path / decision | Status |
|---|---|---|
| Operator next move | offline discriminating task and quality gate accepted after Local calibration review | ACCEPT |
| Continuity | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Paired baseline | `docs/baselines/CVF_GC018_ACEL_G2_T2_DISCRIMINATING_TASK_GATE_T2A_2026-09-16.md` | ACCEPT |
| Prior bounded result | `docs/reviews/CVF_ACEL_G2_T2_CALIBRATION_T1_LOCAL_DISPOSITION_2026-09-16.md` | ACCEPT_WITH_PROCESS_DEVIATION |
| Prior T2 design | `docs/audits/CVF_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_2026-09-16.md` | ACCEPT_AS_BLOCKED_DESIGN |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T6A scored 100 with no T6B trigger | VALUE_SET | `docs/reviews/CVF_ACEL_G2_T2_CALIBRATION_T1_LOCAL_DISPOSITION_2026-09-16.md` | Findings / Position | `releaseCandidate` | Local direct-calibration review | ACCEPT |
| T2 has no qualified task or composed route consumer | GAP | `docs/audits/CVF_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_2026-09-16.md` | `### 4. Candidate task` and `### 1. Real execution owner` | bounded nine-source audit | T2 design audit | ACCEPT |
| Existing deterministic scorer is read-only | CONTRACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/harder.value.candidate.contract.ts` | `evaluateHarderCandidate` | `parseHarderCandidateResponse`, `scoreHarderCandidate` | T6A task/scorer | ACCEPT |
| Topology action contract is isolated | CONTRACT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/runtime.topology.experiment.contract.ts` | `RouteAction` | `RouteAction` | T1 hermetic topology contract | ACCEPT |
| Existing T1 work order provides no next live grant | AUTHORITY | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_2026-09-16.md` | `## Operator Checkpoint` | one-call T1 only | T1 dispatch | ACCEPT |

## Dependency Gate

| Dependency | Evidence | Status |
|---|---|---|
| Local reviewed direct receipt | `docs/reviews/CVF_ACEL_G2_T2_CALIBRATION_T1_LOCAL_DISPOSITION_2026-09-16.md`, material `b9dd8028df5bc05b97aa68cd501d8d3c42b07e10` | ACCEPT |
| Offline-only scope | paired GC-018 baseline and `providerExecutionAuthority: FORBIDDEN` | ACCEPT |
| Source/test toolchain | existing TypeScript/vitest in Execution Plane Foundation | ACCEPT |
| Future live qualification | separate later operator packet | NOT_IN_THIS_TRANCHE |

## Scope / Target / Owner Boundary

Exactly four worker-owned paths:

| Path | Worker action |
|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/g2.t2.discriminating.task.contract.ts` | create a pure frozen prompt/schema/parser/scorer/defect contract; no I/O |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/g2.t2.discriminating.task.contract.test.ts` | create deterministic replay, positive and adversarial negative fixtures/tests |
| `docs/audits/CVF_ACEL_G2_T2_DISCRIMINATING_TASK_GATE_T2A_2026-09-16.md` | source-backed task/rubric/admission design and limitations |
| `docs/reviews/CVF_ACEL_G2_T2_DISCRIMINATING_TASK_GATE_T2A_WORKER_RETURN_2026-09-16.md` | full no-commit evidence packet |

Forbidden writes: existing T6A contract/tests, T1/MAO/Model Gateway source,
topology T1 source, live/historical receipts, credential files, session state,
governance checkers, generated registries, public repo or deployment files.
No package installation or external research is required.

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/g2.t2.discriminating.task.contract.ts` | Yes | pure prompt/parser/scorer/defect contract |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/g2.t2.discriminating.task.contract.test.ts` | Yes | positive, adversarial and deterministic tests |
| `docs/audits/CVF_ACEL_G2_T2_DISCRIMINATING_TASK_GATE_T2A_2026-09-16.md` | Yes | source-backed design and admission audit |
| `docs/reviews/CVF_ACEL_G2_T2_DISCRIMINATING_TASK_GATE_T2A_WORKER_RETURN_2026-09-16.md` | Yes | full worker return |

## Work-Order Fulfillment Manifest

The Required Artifact Manifest above is the exact fulfillment set. New code
is an isolated offline contract, not a production consumer. If a required
registry/source-owner update is discovered outside the manifest, return a
named closeability gap; Local decides the narrow reviewer repair.

## Task / Quality-Gate Acceptance Contract

1. Freeze one realistic coordination task whose answer requires dependency
   ordering, resource limits, at least one branching failure, stop/rollback,
   and explicit authority-preservation decisions. Distinguish it from the
   already easy two-engineer/48-hour T6A task at a mechanism level.
2. The response schema and parser must reject malformed or missing evidence
   rather than repair it. Every rubric dimension and material-defect class
   must be predeclared before a future provider response exists.
3. The scorer must be deterministic, input-only and independent of model
   self-grading. It must not reward keyword mentions without checking the
   corresponding causal/ordering/authority obligations.
4. Tests include at least one complete valid plan, three distinct material
   defect classes, a plausible-but-wrong plan, malformed JSON, missing
   evidence, authority violation, stop/rollback failure, and repeatability.
   Assert exact score/defect/release fields and non-mutation of inputs.
5. `releaseCandidate` or equivalent only marks a *candidate for later
   calibration* under predeclared <=80/material-defect logic. This offline
   suite must never emit `QUALIFIED_FOR_T2_LIVE` or claim Policy B value.
6. Do not tune thresholds or fixtures using the accepted 100/100 response as
   an answer key. The prior response is evidence that T6A was too easy, not
   training data for a new grader.

## Execution Plan

1. Capture clean `executionBaseHead`, staging, path-collision and source
   hashes. Run `python governance/compat/run_agent_autorun_workflow_gate.py
   --phase pre-implementation --base <executionBaseHead> --head HEAD` before
   editing.
2. Implement the pure task/scorer and tests in the two exact TypeScript paths.
   Complete a source-to-rule table and independent-grade rationale in the
   audit; disclose unknowns and negative fixtures.
3. Run focused vitest, TypeScript check, worker-return fast gate, and
   `git diff --check`. No provider, agent, subagent, network or credential
   call is allowed as a test.
4. Return the four uncommitted paths and actual command evidence to Local.

## Acceptance Criteria

- Four owned paths only; staging empty and HEAD unchanged.
- Exact fixture ledger with reproducible scores, defects and parser outcomes.
- Positive and adversarial negative cases pass with no nondeterministic or
  answer-key-dependent grading.
- No claim of a qualified real-agent task, T6B release, topology superiority,
  callable seam, provider/live proof, public readiness or deployment.

## Evidence Requirements

Return exact source/fixture hashes; prompt/schema/rubric freeze evidence;
negative-fixture matrix; focused test and TypeScript command results; zero
provider/agent/subagent/credential/network calls; actual `git status --short`;
and an explicit recommendation of DESIGN_READY_FOR_LOCAL_REVIEW or
BLOCKED_WITH_REASON. No self-acceptance or real-agent difficulty claim.

## Review Gate

Local reviews the causal difficulty and grader independence, not just green
tests. Any future calibration must use a fresh, separately authorized packet
with model/cost/call budget and immutable frozen task/rubric hashes. A score
of 100 again means NOT_QUALIFIED and no automatic second call.

## Operator Checkpoint

This approval opens offline T2A only. Fresh live calibration, actual-agent
comparison, paid exposure, model choice, callable seam and T6B require a
new operator decision after Local reviews T2A. Do not infer these from the
earlier Alibaba-key permission.

## Closure Checklist

- [ ] Local verifies exact four-path manifest and frozen task/rubric hashes.
- [ ] Local independently checks adversarial fixtures and grader independence.
- [ ] Material and continuity commits plus committed-range gates pass.
- [ ] Candidate remains unqualified for live/actual-agent T2 without new proof.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` with four uncommitted paths and gate receipts,
or `BLOCKED_WITH_REASON` naming a source contradiction, inescapable fifth-path
dependency or inability to create an independently gradeable task. No worker
commit, provider call or silent scope expansion.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G2-T2-DISCRIMINATING-TASK-GATE-T2A
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
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: WORKER_RETURN
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g2-t2-discriminating-task-problem","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["NO_DISCRIMINATING_TASK","NO_CALLABLE_T1_TO_MAO_CONSUMER"],"reopened":[],"current":["NO_DISCRIMINATING_TASK","NO_CALLABLE_T1_TO_MAO_CONSUMER"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G2-T2-T2A-DISPATCH","claimClass":"DOCUMENTATION_ONLY","proofClass":"PROPOSAL_ONLY_NO_RUNTIME_READINESS","evidenceRef":"docs/baselines/CVF_GC018_ACEL_G2_T2_DISCRIMINATING_TASK_GATE_T2A_2026-09-16.md"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"NO_SUCCESSOR"}
```

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | INTERNAL_AGENT implements and tests; Local reviews and closes |
| phase | OFFLINE_DISCRIMINATING_TASK_GATE |
| baseHeadFor(phase) | dispatchBaseHead=`253751977ee3a68f5360fec4b731d22635160bee`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact four worker-owned paths in Required Artifact Manifest |
| traceScope(phase, actor) | source hashes, task/fixture ledger, tests, gates, changed set and zero provider/agent calls |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | no other worker may edit these four paths during this packet |
| nextMoveSurfaces | Local-owned session/handoff only after review |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT offline task/gate worker

laneOwnedPaths: exact four paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: terminal worker return with empty staging and exact changed set

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G2_T2_DISCRIMINATING_TASK_GATE_T2A_COMPLETION_2026-09-16.md` if needed |
| reviewerOwnedClosurePaths | optional completion review; material commit; separate continuity commit |
| closureOwner | Local |
| workerCommitPermission | FORBIDDEN |

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | this packet and paired baseline | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | same frozen authorization packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V60_2026-09-08.md` material-SHA marker plus paired exact Local continuity paths | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| pre_implementation_autorun | IMPLEMENTATION | worker | IMPLEMENTATION | exact four worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | contract, tests, audit and return | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity, pre_implementation_autorun |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return disclosure only | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact four worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | exact reviewed material set | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local-only completionReviewPath and disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | paired baseline exact Local continuity authorization | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | exact reviewed material set | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| intake summary | offline discriminating task and executable quality gate |
| scope classification | pure local implementation, named files, no external effect |
| risk sensitivity | P3_ELEVATED because result may later gate a live experiment |
| selected role route | SINGLE_AGENT_MULTI_ROLE, with independent Local reviewer/closer |
| role separation basis | worker returns no-commit artifacts; Local accepts or blocks |
| escalation condition | fifth path, live/provider/agent execution, authority expansion |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| Applicability | one worker authors contract, tests and evidence |
| actor | INTERNAL_AGENT worker |
| role set | task designer, scorer implementer, test author; never Local reviewer/closer |
| Role separation ledger | uncommitted worker return then independent Local review |
| Evidence basis independent of memory | exact current sources, hashes and deterministic fixtures |
| Gate sequence | pre-implementation, focused offline checks, worker-return fast, Local review |
| Self-review boundary | worker cannot qualify its own task for live use |
| escalation condition | source contradiction, outside-manifest change or external effect |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G2_T2_DISCRIMINATING_TASK_GATE_T2A_WORKER_RETURN_2026-09-16.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Claim Boundary; Checker Source Read-Ahead
Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control
Block; Public Export Disposition. Include executionBaseHead, actual git status,
zero-call evidence and N/A-with-reason for conditional blocks.

## Dual Agent Surface Matrix

| Surface | Role | Interface | Authority / risk boundary | Evidence | Adapter boundary | Allowed disposition |
|---|---|---|---|---|---|---|
| INTERNAL_AGENT | offline task/scorer worker | shared workspace, four owned paths | no provider or commit | tests, hashes, return | no runtime consumer | IMPLEMENT_OFFLINE_ONLY |
| EXTERNAL_AGENT_CLI_MCP | none in this tranche | N/A | no remote invocation | `externalInvocationCeiling: 0` | N/A | NOT_USED |
| external Web research | prior advisory only | already closed relay | cannot prove private CVF coverage | prior Local audit | no active adapter | INPUT_NOT_AUTHORITY |

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON

Reason: internal shared-workspace task, zero external invocation allowance.

## Worker Autonomy / No-Question Rule

Fix in-scope static, test and artifact-shape defects directly. Return only
for source contradiction, required outside-manifest mutation, missing task
authority or inability to create an independently gradeable task. Do not ask
permission for ordinary implementation choices inside the contract.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`WORK_ORDER`, role=`DISPATCHER`, lifecyclePhase=`DISPATCH`.

Returned defects: NONE_RETURNED

Resolver returned `totalCandidates: 0` from
`python governance/compat/run_adif_defect_resolver.py --task-class WORK_ORDER --role DISPATCHER --lifecycle-phase DISPATCH --max-results 8 --json`.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| target artifact collision | `rg --files docs/baselines docs/work_orders docs/audits docs/reviews` returned no T2A files before authoring | NO_COLLISION |
| exact token search | `rg -n ACEL-G2-T2-DISCRIMINATING-TASK-GATE-T2A docs CVF_SESSION` returned no match at dispatch base | NO_COLLISION |
| worker file paths | worker must `Test-Path` each target at execution base | RECHECK_AT_WORKER_START |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G2-T2-DISCRIMINATING-TASK-GATE-T2A --date 2026-09-16 --base 253751977ee3a68f5360fec4b731d22635160bee --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface INTERNAL_AGENT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | generic-worker-dispatch, no-commit internal worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, exact four paths, frozen task/gate contract and no-live claim ceiling |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py` |
| docOnlyNewFields | taskGate; candidateQualificationBoundary |
| claimBoundary | authoring scaffold is not a runtime or task-difficulty proof |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `Review-Dispatch Convergence Control: REQUIRED`; `providerExecutionAuthority: FORBIDDEN`; `WORKER_MUST_NOT_COMMIT` |
| gateRunPurpose | confirmation of the source-verified dispatch packet, not discovery of task requirements |
| claimBoundary | checker pass does not prove actual task difficulty, provider qualification or topology value |

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G2-T2-DISCRIMINATING-TASK-GATE-T2A","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"LOCAL_REVERSIBLE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"KNOWN_PATTERN"},"pathFamilies":["docs/baselines/","docs/work_orders/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/","docs/audits/","docs/reviews/"],"claims":["offline task and quality gate can be independently replayed"],"requiredProof":["deterministic exact-score fixtures","adversarial defects","no provider or agent calls","no production consumer"],"operatorCheckpoints":["live calibration","actual-agent comparison","callable seam"],"forbiddenEffects":["provider call","credential access","agent invocation","production binding","public write","deployment","worker commit"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/audits/CVF_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_2026-09-16.md","completenessClaimChanged":false}}
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF workspace; no provider call |
| Session or invocation | T2A offline dispatch 2026-09-16 |
| Working directory | repository root at `253751977ee3a68f5360fec4b731d22635160bee` |
| Command or tool surface | governed source reads, collision search, ADIF resolver, scaffold, pre-dispatch gate |
| Target paths | this work order and paired baseline |
| Allowed scope source | operator authorization of the next offline design step |
| Before status evidence | clean worktree and staging at dispatch base `253751977ee3a68f5360fec4b731d22635160bee` |
| After status evidence | two dispatch artifacts only before continuity sync |
| Diff evidence | `git diff --name-status` against dispatch base |
| Approval boundary | offline contract and tests only; no provider grant |
| Claim boundary | dispatch shape, not task value or execution proof |
| Agent type | LOCAL_ORCHESTRATOR |
| Invocation ID | `acel-g2-t2-discriminating-task-gate-t2a-dispatch-2026-09-16` |
| Expected manifest | paired baseline and work order |
| Actual changed set | same two dispatch paths |
| Manifest delta | MATCH_AT_DISPATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | offline task/scorer proposal |
| claimDisposition | CLAIM_REJECTED: no live execution-control or runtime-enforcement claim |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker has not executed; dispatch only |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no provider/agent task action yet |
| invocationBoundary | source reads and packet authoring only |
| interceptionBoundary | no interception, wrapper or mandatory runtime hook |
| claimLanguage | proposed offline contract, not real-agent qualification |
| forbiddenExpansion | provider/live, callable seam, comparative T2, production, public and deployment |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO_NEW_RUNTIME_CLAIM |
| runtimeMutationAuthorized | isolated pure contract only; no composed consumer |
| freshnessVerificationMode | current exact-path read of `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/harder.value.candidate.contract.ts`, `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/runtime.topology.experiment.contract.ts`, `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`, and `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` |
| reason | prior T2 audit found no route-action consumer; the provider registry and capability registry remain current separate owner surfaces, not evidence of this proposed task's composition |
| requiredFutureAction | Local source recheck before any T2 live/composition packet |

## Foundation Storage Layout Block

N/A with reason: this tranche adds one isolated pure task contract and its
test, plus flat audit/review files. It does not create, split, relocate or
refactor a durable governance foundation, registry, generated aggregate,
index, runtime state, queue or rebuild pipeline.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
cd EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION
npx vitest run --config vitest.config.ts tests/g2.t2.discriminating.task.contract.test.ts
npx tsc --noEmit -p tsconfig.json
cd ../..
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
```

## Reviewer Non-Duplication

Apply `EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION`. Local should
consume deterministic fixture proof and rerun only focused tests or named
contradictions; no broad duplicate implementation or provider call.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private offline G2-T2 candidate design; no public-sync authority.

## Claim Boundary

This work order authorizes an isolated offline contract, tests and evidence.
It does not qualify the task for a live trial, release T6B, create a
T1-to-MAO callable seam, execute a provider/agent or prove dynamic topology
value. Any next trial requires Local review and a separate operator decision.
