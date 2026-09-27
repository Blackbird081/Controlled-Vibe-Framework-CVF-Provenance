# CVF Agent Work Order - NCR-R1/S10 Test Evidence Audit Instruction-Use Proof

Memory class: governed-worker-dispatch

docType: work_order

Status: HOLD_PENDING_OPERATOR_DECISION

Batch ID: CVF-NCR-R1-S10

Dispatch base head: `acfe300bb`

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

Worker: one shared-workspace `INTERNAL_AGENT` worker after release

Reviewer/closer: Local orchestrator/reviewer

Worker return path: `docs/reviews/CVF_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_WORKER_RETURN_2026-09-28.md`

## Dispatch Prompt Envelope

Role: internal P9 evidence worker. Canonical packet: this file. Commit mode:
`WORKER_MUST_NOT_COMMIT`. Capture `executionBaseHead` before edits. This packet
is held and must not be executed until its status and paired baseline are
changed to `DISPATCH_READY` by Local after an explicit operator live-release
checkpoint. After release, execute the exact manifest and commands without
asking the operator to choose a technical repair.

## Purpose

After release, prove one bounded internal use of
`cvf-engineering-test-evidence-audit` through the existing use-proof adapter:
dry readiness, at most one live provider completion, exact receipt validation,
and a no-commit worker return. Do not open P10.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind package-skill --batch-id CVF-NCR-R1-S10 --title "Test Evidence Audit P9 Instruction-Use Proof" --date 2026-09-28 --base acfe300bb --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | package-skill plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact P9 held scope, target-state contract, commands, manifest and proof boundary |
| checkerReadAheadConfirmation | applicable dispatch, lifecycle, feasibility, adapter and return gates read before authoring |
| docOnlyNewFields | `liveReleaseCheckpoint`; `providerCallCeiling` |
| claimBoundary | dispatch authoring only until checkpoint release |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-R1-S10
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
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "CVF-NCR-TEST-EVIDENCE-AUDIT-P9",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {"prior": [], "resolved": [], "retained": [], "new": [], "reopened": [], "current": []},
  "resolutionEvidence": {},
  "counters": {"partialReadyClosures": 0, "reviewerScopeExpansions": 0, "sameClaimCorrections": 0, "nonDecreasingBlockerTransitions": 0},
  "claims": [{"claimId": "P9-HELD-INSTRUCTION-USE-PROOF", "claimClass": "OTHER", "proofClass": "NAMED_OBSERVABLE_PROOF", "evidenceRef": "docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_2026-09-28.md"}],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| P8 closure | `docs/reviews/CVF_CVF_NCR_R1_S09_R1_ACTIVE_EXTERNAL_ADAPTER_ADMISSION_ROOT_RECONCILIATION_2026-09-28.md`; internal `ACTIVATION_READY` | unchanged ACTIVE/STRICT/internal-only state | RELEASED_FOR_P9 |
| root dispatch hardening | material commit `e14b367b2`; feasibility gate bound to pre-dispatch and pre-implementation | this work order passes exact active-work-order check | RELEASED |
| operator live checkpoint | provider/live parked at dispatch base | operator explicitly releases exactly one live call; Local then changes both packet statuses and runs pre-dispatch | HOLD_PENDING_OPERATOR_DECISION |

## Authority Chain

Roadmap P9 intent -> active session next move -> this paired GC-018/work order
-> operator live-effect checkpoint -> internal worker evidence -> Local review
and closure. Packet authoring grants no execution authority by itself.

## Task Governance Routing Manifest

| Role | Phase | Decision owner | Boundary |
|---|---|---|---|
| Local dispatcher/reviewer | author/release/review/closure | LOCAL | technical disposition and material commit |
| shared-workspace worker | implementation after release | LOCAL packet | exact commands and two output paths; no commit |
| operator | live checkpoint | OPERATOR | authorizes one provider call and quota exposure only |
| external agent | none | N/A | no external research or execution lane |

## External/Local Coordination Binding

The future worker is `INTERNAL_AGENT` regardless of provider/model. External
research is closed. Local owns private-CVF verification and final disposition;
the operator checkpoint authorizes the effect but does not perform technical review.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md` |
| Chain map route | N/A with reason: no external research phase |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Local reviewer/closer |
| Disposition | NOT_APPLICABLE_WITH_REASON: current local owners are sufficient |
| Claim boundary | no external claim promotion or public/private inference |

## Scope And Maximum Worker Path Manifest

After release, the worker may create exactly:

1. `docs/reviews/evidence/cvf-ncr-r1-s10-test-evidence-audit-use-proof.json`
2. `docs/reviews/CVF_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_WORKER_RETURN_2026-09-28.md`

The dry proof writes no artifact. The live adapter alone creates the receipt
path. No source, registry, truth, index, inventory, Web, checker, roadmap,
packet, continuity or handoff path is worker-owned.

## Required Root Contract

1. Stop immediately while status is `HOLD_PENDING_OPERATOR_DECISION`.
2. After release, run pre-implementation before any body read.
3. Run the dry proof once; require `DRY_RUN_READY_FOR_LIVE_PROVIDER_USE_PROOF`.
4. Run the exact live proof once; require HTTP 200, non-empty output and `LIVE_PROVIDER_USE_PROOF_PASS`.
5. Independently recompute receipt ID and output hash from the saved JSON without another provider call.
6. Never rerun a failed/partial/ambiguous live proof. Record a secret-safe diagnostic and return `BLOCKED_WITH_REASON`.
7. Do not run the audited test, mutate lifecycle or open P10.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| P9 requires use-proof receipt and live proof for behavior claim | lifecycle | `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md` | End-To-End Phase Ladder P9 | `USE_PROOF_PASSED` | productionization SOP | ACCEPT |
| adapter dry/live states and receipt | runtime | `governance/compat/run_assf_package_use_proof_adapter.py` | `build_package_use_proof_packet`; `_build_use_proof_receipt` | dry/live dispositions | use-proof adapter | ACCEPT |
| use-proof does not activate lifecycle | authority | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_USE_PROOF_ADAPTER_STANDARD.md` | Adapter Contract; Claim Boundary | `activePromotionAuthorized` | use-proof standard | ACCEPT |
| current target is internal ACTIVATION_READY and externally denied | runtime readout | `governance/compat/run_assf_active_resolver.py`; `run_assf_cli_mcp_adapter_projection.py` | current read-only probes | exact skill ID | resolver/projection | ACCEPT |
| selected model remains within ledger date | value set | `docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.json` | `models` | `qwen3.7-flash-2026-07-15`; `2026-10-22` | free-quota ledger | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| planned baseline/work-order/return/receipt | all four `Test-Path` results false before authoring | NO_COLLISION |
| batch/token search | exact `rg` returned no prior artifact | NO_COLLISION |
| collision decision | fresh P9 phase packet | CREATE_NEW |

## Required First Reads And Pre-Flight

Read startup bootstrap, session front door, active handoff, guard orientation,
literal gotchas, paired baseline, this work order, productionization SOP,
target-state feasibility standard, use-proof standard and every checker named
below. Capture clean `HEAD` and status. Do not read the package body before the
pre-implementation gate passes.

## Agent Roles

- Operator: releases or declines the single provider-call checkpoint.
- Dispatcher: resolves packet semantics, runs pre-dispatch, and commits release.
- Worker: executes exact released scope and returns evidence without commit.
- Reviewer/closer: independently validates receipt integrity and owns closure.
- Session-sync steward: updates continuity only after material disposition.

## Write Ownership

Write mode: create-only for the exact two worker paths. Everything else is
forbidden. `WORKER_MUST_NOT_COMMIT`; no stage, stash, commit, push or public sync.

## Execution Plan

1. Confirm released packet status, clean base and required reads.
2. Run exact pre-implementation gate with the active work order.
3. Run focused adapter tests and read-only activation/projection probes.
4. Run dry adapter command and validate its exact readiness disposition.
5. Run the one live command and write the use-proof JSON.
6. Validate receipt/digests without a second adapter/provider invocation.
7. Scaffold and complete the worker return; run the exact fast gate and scope checks.

## Evidence Requirements

- dry disposition and zero-call evidence;
- live HTTP status, model, safe trace metadata, receipt and output hashes;
- `providerCallCount: 1` on success or `1` with failure diagnostic;
- exact two-path dirty set and empty cached diff;
- no lifecycle/source/external adapter mutation.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_2026-09-28.md
python -m pytest governance/compat/test_run_assf_package_use_proof_adapter.py -q
python governance/compat/run_assf_active_resolver.py --skill-id cvf-engineering-test-evidence-audit --json
python governance/compat/run_assf_cli_mcp_adapter_projection.py --skill-id cvf-engineering-test-evidence-audit --json
python governance/compat/run_assf_package_use_proof_adapter.py --skill-id cvf-engineering-test-evidence-audit --provider alibaba-dashscope --model qwen3.7-flash-2026-07-15 --task-prompt "Given an asserted source-to-test coverage claim, return one advisory KEEP, REPAIR, CONSOLIDATE, ADD, or DEFER_WITH_REASON label with target, evidence, and reason; do not run or modify tests." --json
python governance/compat/run_assf_package_use_proof_adapter.py --skill-id cvf-engineering-test-evidence-audit --provider alibaba-dashscope --model qwen3.7-flash-2026-07-15 --live --task-prompt "Given an asserted source-to-test coverage claim, return one advisory KEEP, REPAIR, CONSOLIDATE, ADD, or DEFER_WITH_REASON label with target, evidence, and reason; do not run or modify tests." --json --receipt-out docs/reviews/evidence/cvf-ncr-r1-s10-test-evidence-audit-use-proof.json
python governance/compat/check_cvf_skill_usage_receipt_trace.py --enforce
python governance/compat/check_package_skill_productionization_pipeline.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_WORKER_RETURN_2026-09-28.md --title "CVF NCR R1 S10 Test Evidence Audit Instruction-Use Proof Worker Return"
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_2026-09-28.md --pytest-target governance/compat/test_run_assf_package_use_proof_adapter.py
git diff --check
git diff --name-status
git diff --cached --name-status
git status --short --untracked-files=all
```

The worker may use one read-only one-shot Python command to independently
recompute hashes. It must record the exact command and must not write another artifact.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: BLOCKED_PENDING_OPERATOR_DECISION

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| operator_live_release | PRE_DISPATCH | operator | PRE_DISPATCH | checkpoint only | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| target_state_feasibility | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet | EXACT_PATHS | closer | DISPATCH_COMMIT | operator_live_release |
| pre_implementation | WORKER_RETURN | worker | IMPLEMENTATION | exact two paths | EXACT_PATHS | closer | MATERIAL_COMMIT | target_state_feasibility |
| live_use_proof | WORKER_RETURN | worker | IMPLEMENTATION | use-proof JSON | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | worker return | EXACT_PATHS | closer | MATERIAL_COMMIT | live_use_proof |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted set | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | reviewer_fast |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | INTERNAL_AGENT worker -> Local reviewer/closer |
| phase | P9_WORKER_EXECUTION_AFTER_RELEASE |
| baseHeadFor(phase) | dispatchBaseHead=`acfe300bb`; executionBaseHead is worker capture; closureBaseHead is Local-set |
| changedSetScope(phase) | exact two-path worker manifest |
| traceScope(phase, actor) | dry/live receipt and Git scope evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; Local owns commit |
| crossBatchIsolation | no unrelated dirty paths |
| nextMoveSurfaces | worker return to Local only |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: one INTERNAL_AGENT worker after committed release and continuity

laneOwnedPaths: exactly the two worker output paths

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: terminal worker return, exact manifest reconciliation and empty staging

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`package_skill_productionization`, role=`dispatcher`, lifecyclePhase=`dispatch`.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class package_skill_productionization --role dispatcher --lifecycle-phase dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no registered defect changes the held boundary |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_package_skill_target_state_feasibility.py`; `governance/compat/check_package_skill_productionization_pipeline.py`; `governance/compat/check_cvf_skill_usage_receipt_trace.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | held and return status tokens; P9 lifecycle fields; dry/live dispositions; receipt types; Local blocker route |
| gateRunPurpose | confirmation after source-first packet authoring |
| claimBoundary | structural/semantic admission only; not live proof |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_WORKER_RETURN_2026-09-28.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_2026-09-28.md --pytest-target governance/compat/test_run_assf_package_use_proof_adapter.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Scope / Methodology; Findings / Position; Risk /
Corrective Action; Decision; Agent Operation Trace Block; Delta Execution
Claim Boundary Control Block; CVF Skill Usage Receipt Trace; Public Export
Disposition; executionBaseHead; git status --short; External Knowledge Intake
Routing; Rescan Intelligence Hardening; Corpus Completeness And Report
Integrity; Finding-To-Governance Learning Disposition; Epistemic Process
Block; Machine Closure Package. Use explicit N/A with reason where applicable.

Exact required section terms: Purpose; Scope / Methodology; Findings / Position;
Risk / Corrective Action; Claim Boundary; Agent Operation Trace Block;
Delta Execution Claim Boundary Control Block; Public Export Disposition;
executionBaseHead; git status --short.

Exact conditional section terms: External Knowledge Intake Routing; Rescan
Intelligence Hardening; Corpus Completeness And Report Integrity;
Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine
Closure Package. Each must be present in the return with N/A with reason when
it does not apply.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | optional; Local may close in reviewed return if sufficient |
| reviewerOwnedClosurePaths | returned two-path set plus separately authorized continuity |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Worker Autonomy / No-Question Rule

Repair allowed-scope return-shape failures directly. A technical contradiction
must be returned as `BLOCKED_WITH_REASON` to Local, never routed into
`AskUserQuestion`. Operator contact is forbidden during worker execution. The
only operator decision is resolved before dispatch by the live-release checkpoint.

## Parked Effect Checkpoints

Until release: all execution is parked. After release: only one internal
Alibaba/DashScope proof call is open. P10, external adapter, a second provider
call, provider/model changes, public export, deployment and production remain parked.

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: P8 `ACTIVATION_READY`; source status `ACTIVE`.

Target lifecycle state: P9 `USE_PROOF_PASSED`; no source mutation.

Prior phase evidence: S09 root-reconciliation completion and existing P7 receipt path.

Next forbidden skip: P10 production package runtime.

Runtime/provider proof: one dry proof plus at most one released live call.

Claim boundary: use-proof receipt proves one bounded instruction use only.

## Package Skill Target-State Feasibility Contract

```json
{
  "schemaVersion": "cvf.packageSkillTargetStateFeasibility.v1",
  "skillId": "cvf-engineering-test-evidence-audit",
  "sopPhase": "P9",
  "targetState": {
    "status": "ACTIVE",
    "candidateState": "ACTIVE",
    "uatState": "PASSED",
    "certificationState": "CERTIFIED",
    "internalAgentDisposition": "IMPLEMENTED",
    "externalCliMcpDisposition": "DEFERRED_WITH_REASON",
    "truthApprovalStatus": "APPROVED",
    "truthAssuranceLevel": "STRICT",
    "adapterContract": "N/A with reason: internal-only P9 proof",
    "adapterEvidence": "N/A with reason: external use is not claimed"
  },
  "externalUseClaimed": false,
  "expectedDecisions": {
    "internalActivation": "ACTIVATION_READY",
    "externalBodyRead": "DENIED_EXTERNAL_BODY_READ_NOT_IMPLEMENTED",
    "externalOutputUse": "DENIED_EXTERNAL_OUTPUT_USE_NOT_IMPLEMENTED"
  },
  "checkerSources": [
    "governance/compat/check_assf_certified_metadata_admission.py",
    "governance/compat/check_package_skill_productionization_pipeline.py",
    "governance/compat/generate_skill_control_plane_inventory.py",
    "governance/compat/run_assf_active_resolver.py",
    "governance/compat/run_assf_cli_mcp_adapter_projection.py"
  ],
  "mutations": ["USE_PROOF_RECEIPT"],
  "blockerRouting": {
    "technicalDecisionOwner": "LOCAL",
    "workerTerminalReturn": "BLOCKED_WITH_REASON",
    "operatorQuestionAllowed": false
  }
}
```

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: P9_LIVE_INSTRUCTION_USE_AND_RECEIPT_INTEGRITY

independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: worker performs the single live call; Local recomputes receipt hashes and checks saved fields without another call

positiveControl: HTTP 200, non-empty output, exact skill/model, `LIVE_PROVIDER_USE_PROOF_PASS`, valid use-proof receipt

negativeMutationClasses: receipt tamper, output hash mismatch, wrong model, lifecycle mutation, external-use claim, second call or third worker path

expectedInformationGain: distinguish genuine receipt-backed instruction use from dry readiness or body-read-only evidence

rerunCostReason: deterministic offline recomputation avoids consuming another provider call

reviewerDecisionOwner: LOCAL

## Foundation Storage Layout Block

Use the existing `docs/reviews/evidence/` family. No new root, index, database,
queue, watcher or external adapter is created.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF workspace |
| Session or invocation | NCR-R1/S10 held packet authoring, 2026-09-28 |
| Working directory | repository root |
| Command or tool surface | governed reads, source probes, scaffold stdout, apply_patch and Git |
| Target paths | paired baseline and work order |
| Allowed scope source | active next move and operator continuation instruction |
| Before status evidence | clean worktree at `acfe300bb` |
| After status evidence | held packet pending operator live release |
| Diff evidence | `git diff --name-status` |
| Approval boundary | packet authoring only |
| Claim boundary | no body read or provider call |
| Agent type | INTERNAL_AGENT Local orchestrator/reviewer |
| Invocation ID | `cvf-ncr-r1-s10-held-author-20260928` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order only |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | held P9 packet authoring |
| claimDisposition | CLAIM_REJECTED at authoring; live evidence required after release |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no P9 receipt yet |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no P9 action executed |
| invocationBoundary | future exact local adapter invocation only after release |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | held packet defines, but does not perform, one proof |
| forbiddenExpansion | no execution while held; no P10/external/public/production effect |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: after release, the exact ACTIVE/STRICT package should produce dry readiness and one live receipt-backed advisory label without lifecycle mutation.

Evidence Comparison Requirement: worker return compares actual disposition, output, receipt and scope evidence against the prediction.

Contradiction Handling Requirement: any mismatch requires secret-safe diagnostic, no rerun, `BLOCKED_WITH_REASON`, and Local disposition.

Claim Update Requirement: Local records confirmed, narrowed, revised or invalidated P9 claim.

## Return-To-Orchestrator Conditions

While held, do not start. After release, return `COMPLETE_PENDING_REVIEW` only
when every criterion passes. Otherwise return `BLOCKED_WITH_REASON` with the
exact failing command, safe evidence, root cause and proposed Local repair.

## Acceptance Criteria

- [ ] operator live checkpoint released before dispatch;
- [ ] pre-dispatch and pre-implementation gates pass;
- [ ] dry disposition is exactly `DRY_RUN_READY_FOR_LIVE_PROVIDER_USE_PROOF`;
- [ ] exactly one live call yields HTTP 200 and `LIVE_PROVIDER_USE_PROOF_PASS`;
- [ ] saved receipt and independent hashes match;
- [ ] target remains ACTIVE/STRICT/internal `ACTIVATION_READY`, external denied;
- [ ] worker-return fast gate passes and exact two-path scope is cleanly uncommitted.

## Review Gate

Packet cannot dispatch while held. After operator release, Local changes both
statuses, runs exact pre-dispatch and commits packet/continuity separately.
Local later reviews returned evidence without duplicating the live call.

## Closure Checklist

- [ ] held checkpoint released and recorded;
- [ ] P9 evidence accepted or explicitly blocked;
- [ ] no second provider call or P10 expansion;
- [ ] Local owns material and continuity commits;
- [ ] next move remains P10 authoring only after explicit Local release.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `HOLD_PENDING_OPERATOR_DECISION` | PASS |
| P9 evidence | future use-proof JSON and worker return | not executed | BLOCKED with reason: live checkpoint parked |
| Roadmap state | NCR D013 P9 | P9 authored; P10 closed | PASS |
| Session continuity | active session surfaces | update after held packet commit | BLOCKED with reason: packet commit pending |

## Claim Boundary

This work order currently authorizes no worker execution. After an explicit
operator live release and Local status transition, it authorizes exactly one
dry proof, one live provider call, one P9 receipt and one worker return. It
never authorizes a retry, P10, external adapter, public sync, deployment or
production claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private P9 packet and proof evidence.

## Operator Checkpoint

Required decision: release exactly one Alibaba/DashScope live provider call
using `qwen3.7-flash-2026-07-15`, with no automatic retry. Until that explicit
release is recorded, this packet remains held and must not be copied to a
worker as executable authority.
