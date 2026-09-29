# CVF Agent Work Order - ACEL G1 T2 Task-Class Calibration Owner Implementation

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

## Dispatch Prompt Envelope

Batch ID: ACEL-G1-T2-TASK-CLASS-CALIBRATION-OWNER-IMPLEMENTATION

Dispatch base head: `899f162dece18abf42980cb82dab671626d6672e`

dispatchBaseHead: `899f162dece18abf42980cb82dab671626d6672e`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_TO_SET

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

Role: shared-workspace `INTERNAL_AGENT` offline implementation worker.

Reviewer/closer: Local reviewer/orchestrator.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md`

Worker return path: `docs/reviews/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_WORKER_RETURN_2026-09-17.md`

Current-time notes: Local selected G1 T2 from parked accepted G1 design at
clean HEAD `899f162dece18abf42980cb82dab671626d6672e`.

Do-not-misread notes: implement a pure offline decision contract, not actual
calibration, configuration deployment, G4 value measurement, or runtime use.

Required first actions: read `AGENTS.md`, compact bootstrap/front door,
active V61 handoff, guard orientation, literal gotchas, paired baseline,
this order, accepted G1 design/manifest and relevant checker sources. Capture
HEAD, status and staging, verify source hashes and path collisions, and run
pre-implementation before editing.

Return contract: create exactly seven declared outputs, leave HEAD unchanged
and staging empty; return `COMPLETE_PENDING_REVIEW` only after required gates
pass, otherwise `BLOCKED_WITH_REASON` with exact blocker.

## Purpose

Implement G1's task-class calibration decision layer as pure local TypeScript,
adversarial tests, a read-only Python evidence checker with focused tests, and
one normative reference contract. The worker also creates an implementation
audit and full return for Local review. No real operating point is selected.

## Authority Chain

1. `ECOSYSTEM/doctrine/`, `ECOSYSTEM/operating-model/`, `AGENTS.md`.
2. Operator's instruction to continue; V61 permits one Local-selected bounded delta.
3. G1 T1 design completion and its five-path machine successor manifest.
4. Paired GC-018 baseline and this order; Local alone decides closure/commit.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| accepted G1 design | `docs/reviews/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-17.md`, SHA-256 `4c8a4978ba9da86af8fe45276dbe7f875bc442e296fcd600f8b834e0d95e4644`, `CLOSED_PASS_BOUNDED` | separate implementation authority required | RELEASED_BY_THIS_ORDER |
| exact successor | `docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json`, SHA-256 `c8c1f6899e50513141e69113b8ac9faf37669b1fcd785bc2df3b88d8e894505b` | five paths and zero blockers | RELEASED_BY_THIS_ORDER |

## Scope / Methodology

Use the accepted human and machine G1 design as the normative behavior
boundary. Compose, without replacing, G3 admission/grading, optional rubric evidence,
the proposal-only benchmark harness and provider-lane readiness. The new
owner validates immutable candidate/configuration-to-fixture/trace/result
envelopes and emits deterministic offline decision records. All inputs are
synthetic or supplied data; no provider or benchmark run occurs. The Python
checker validates explicit evidence paths without modifying them.

## Normative Implementation Contract

- Declare task-class identity, N-way candidate IDs, canonical versioned
  `declaredDimensions` and `candidateConfigHash`; reject duplicate IDs/hashes
  rather than overwriting or double-counting.
- Require candidate evidence envelope fields from the accepted manifest,
  including fixture/trace/result hashes and `producerReceiptRef`; verify
  actual supplied bytes and producer-to-candidate binding. G3 output alone
  cannot attest candidate/configuration identity.
- Predeclare SEARCH and HELD_OUT membership separately from G3 `baselineRole`;
  reject shared ID, input/source/content hash or known tuning exposure.
- Apply the exact comparability fingerprint and distinguish allowed varying
  candidate dimensions from forbidden silent-comparison dimensions.
- Reuse G3 fixture admission and repeat semantics; missing traces/repeats are
  `insufficient_evidence`, complete bound substantive defects are `ineligible`.
- Apply exclusive precedence: `incomparable`, `insufficient_evidence`,
  `ineligible`, then eligible preference. Assign one state to every candidate.
- Treat readiness as an allowed-status eligibility gate. Scores cannot reverse
  eligibility failure. Raw `PROPOSAL_ONLY` benchmark values allow exploratory
  ranking only, never `preferred` or `RegressionBinding`.
- An admissible preference basis requires a separately GC-026-promoted
  performance reference or predeclared comparable version-bound deterministic
  rubric. No basis, tie, or no eligible candidate produces no preferred point.
- Emit `OperatingPointAssessment` and optional `RegressionBinding` with the
  accepted provenance fingerprint. On declared invalidation, mark binding
  `STALE` and require a fresh assessment; never rollback/mutate configuration.

## Required Negative Tests

Cover every `negativeCases` row in the G1 machine manifest: empty set,
duplicate identity/hash, mixed fixture sets, budget/policy mismatch, missing
or ambiguous binding, heldout contamination, stale fingerprint, incomplete
repeats, unknown metric/unit, tie, no eligible candidate, and proposal-only
advantage. Also test complete positive deterministic/stochastic evidence,
candidate misattribution despite a passing G3 result, exclusive-state
precedence, immutable inputs, no preference evidence, and every invalidation
trigger. Use synthetic fixtures only; no real provider or benchmark run.

## Python Evidence Checker Contract

Expose a reusable read-only validator and CLI accepting explicit evidence
paths or test-injected roots. Reject malformed/unknown schema, absent or stale
source/fixture/configuration/trace/result hashes, missing producer receipt,
contaminated holdout, unsupported preference authority, `preferred` without
exclusive admissible evidence, and stale regression binding claimed current.
It must not impose G1 adoption on unrelated existing packages or mutate
registries, tracker state, generated files, configuration or lifecycle data.
Focused tests use hermetic temporary files and cover positive plus each
fail-closed class.

## Roadmap-To-Work-Order Trace Matrix

| Accepted input | Work-order control | Disposition |
|---|---|---|
| G1 T0 `ADAPT` | one owner composition, not duplicate engines | RELEASED_TO_IMPLEMENTATION |
| G1 T1 five-path successor | exact five implementation paths | BINDING |
| G3 result lacks candidate identity | bound envelope verification | BINDING |
| benchmark `PROPOSAL_ONLY` | exploratory only unless GC-026 promoted | BINDING |
| G4 independent audit | no G4 output or value claim | PARKED |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G1-T2-TASK-CLASS-CALIBRATION-OWNER-IMPLEMENTATION
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-empirical-calibration-owner-composition","chainMode":"SUCCESSOR","chainOrdinal":1,"predecessor":{"path":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_2026-09-16.md","sha256":"72a672175a43503d514187d0928667e676b7f4af159e45447a8afdde0ea0c1ea"},"blockerDelta":{"prior":["g1_general_operating_point_owner_not_composed","g1_non_circular_evidence_and_invalidation_semantics_unsettled"],"resolved":["g1_non_circular_evidence_and_invalidation_semantics_unsettled"],"retained":["g1_general_operating_point_owner_not_composed"],"new":[],"reopened":[],"current":["g1_general_operating_point_owner_not_composed"]},"resolutionEvidence":{"g1_non_circular_evidence_and_invalidation_semantics_unsettled":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/reviews/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-17.md","sha256":"4c8a4978ba9da86af8fe45276dbe7f875bc442e296fcd600f8b834e0d95e4644","locator":"Decision / Recommendation / Disposition"}},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T2-IMPLEMENTATION-DISPATCH","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/baselines/CVF_GC018_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md"}],"requiredDisposition":"READY_WITH_EXECUTABLE_PROOF","successorScope":"EXECUTABLE_IMPLEMENTATION"}
```

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T2-TASK-CLASS-CALIBRATION-OWNER-IMPLEMENTATION","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"NEW_INTERFACE"},"pathFamilies":["docs/baselines/","docs/reference/agent_system_skills/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/","governance/compat/","docs/audits/","docs/reviews/"],"claims":["pure offline decision contract and checker implement accepted G1 design"],"requiredProof":["TypeScript focused tests and typecheck","Python focused tests","implementation audit","worker-return fast gate","Local review"],"operatorCheckpoints":["Local closure","empirical calibration","provider/live","configuration mutation","G4","runtime","public sync","deployment"],"forbiddenEffects":["provider call","credential access","network effect","benchmark execution","configuration mutation","runtime action","worker commit","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json","completenessClaimChanged":false}}
```

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| intake summary | Local-selected bounded G1 implementation from accepted T1 design |
| scope classification | pure local implementation, no external effects |
| risk sensitivity | P3 elevated: future decision evidence, no live effect here |
| selected role route | `SINGLE_AGENT_MULTI_ROLE` implementation; Local review |
| escalation condition | source contradiction, forbidden path/effect, or uncloseable gate |

## Worker Autonomy / No-Question Rule

Proceed autonomously within exact owned paths. Repair allowed-scope compiler,
test or formatting defects and rerun affected gates without routine
clarification. Stop only for material contradiction, missing authority, or a
forbidden-scope need. Any machine-gate failure within owned paths is repaired
by the worker before return.

## Agent Roles

| Role | Responsibility |
|---|---|
| Local dispatcher/reviewer | selects scope, reviews/repairs, closes and commits |
| INTERNAL_AGENT worker | implements seven outputs and returns uncommitted evidence |
| external Web agent | advisory research phase closed; no internal authority |
| operator | approves later expansion checkpoints, not routine worker repairs |

## Required First Reads

`AGENTS.md`; compact bootstrap/front door and active V61 handoff; guard
orientation; literal gotchas; paired baseline and this order; G1 human design,
manifest and completion; G3 contract and tests; benchmark evidence class;
provider-readiness matrix; applicable checker sources for each output.

## Pre-Flight Checks

Capture full HEAD, clean/dirty worktree and empty staging; verify exact
predecessor hashes and seven output collisions; run pre-implementation at the
captured execution base before editing. Stop for unexplained drift.

## Execution Plan

Implement pure decision contract and normative reference, then adversarial
TypeScript tests; add read-only checker and focused Python tests; produce the
audit/return; run named gates and return without staging or committing.

## Write Ownership

The worker may create only seven exact paths below. Do not edit existing
sources/tests/checkers, protected Core/state, baseline/order, handoff, hooks,
catalogs, or public repo. If a path appears before execution, stop for
collision. No `git add`, `git commit`, or worker closure.

## Required Artifact Manifest

Work-Order Fulfillment Manifest: REQUIRED_EXACT_SEVEN_PATHS

| Path | Action |
|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts` | CREATE pure decision layer |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts` | CREATE adversarial suite |
| `governance/compat/check_task_class_calibration_owner_evidence.py` | CREATE read-only validator/CLI |
| `governance/compat/test_check_task_class_calibration_owner_evidence.py` | CREATE checker suite |
| `docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md` | CREATE normative contract |
| `docs/audits/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md` | CREATE source/implementation audit |
| `docs/reviews/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_WORKER_RETURN_2026-09-17.md` | CREATE full return |

## Evidence Requirements

Record exact predecessor hashes, source verification, symbols/tests and
mandatory-path/bypass/fail behavior. Audit human and machine semantics against
the accepted G1 design; disclose every deviation or unsupported case. Report
focused test/typecheck counts, all changed paths, HEAD and staging, and zero
provider/live invocations. Structural gates do not prove empirical value.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: execution-base source freshness is necessary before binding implementation to the accepted G1 design.

priorVerificationArtifact: `docs/reviews/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-17.md`

freshRecomputeRequired: YES, because the implementation decision requires current
predecessor bytes and source identity at execution base. Reuse its semantic
review, but recompute current SHA-256 only for named sources; no broad binary
corpus scan. Read repository-relative paths literally and preserve UTF-8 text;
no extracted-text or Unicode-path artifact is in scope.

unicodePathHandling: use literal paths for every named file and UTF-8-safe readers for text.

extractedTextAuthority: N/A with reason

extractedTextReason: no extracted text is an input.

## Acceptance Criteria

1. Five-path implementation matches the accepted G1 design and reuses G3,
   benchmark, and readiness owners without modifying them.
2. Binding, partition, comparability, exclusive states, preference authority,
   regression and invalidation all fail closed on negative cases.
3. Every declared negative case and focused Python checker failure has tests.
4. TypeScript focused tests/typecheck, Python tests, pre-implementation and
   worker-return fast gate pass; or truthful `BLOCKED_WITH_REASON`.
5. Exactly seven worker paths are created; HEAD and staging unchanged.

## Review Gate

Local uses `EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION` and
reviewer-fast. Check exact source hashes, design-to-code parity, full negative
matrix, read-only behavior, scope and gate receipts before a single
consolidated repair or closure. No routine duplicate broad rerun.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only if all acceptance criteria pass.
Otherwise return `BLOCKED_WITH_REASON`, naming exact source/test/gate or
authority blocker. No self-approval or automatic successor.

## Verification Commands

Before edits: `git rev-parse HEAD`, `git status --short`,
`git diff --cached --name-only`, source SHA-256 checks, path collision checks,
and `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD`.
After edits: focused TypeScript test and typecheck commands appropriate to the
execution-plane package; `python -m unittest governance.compat.test_check_task_class_calibration_owner_evidence`; JSON/evidence checker fixtures;
`git diff --check`; repeat pre-implementation with the same execution base;
`python governance/compat/run_worker_return_fast_gate.py`. Report actual
results, not inferred PASS. No live release-quality claim is made here.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Include Purpose, Target / Source, Scope / Methodology, Findings / Position,
Risk / Corrective Action, Claim Boundary, Checker Source Read-Ahead Block,
Agent Operation Trace Block, Delta Execution Claim Boundary Control Block,
Public Export Disposition, `executionBaseHead`, git status, Changed Files,
Command Evidence and No-Commit Statement. Resolve conditional sections with
evidence or N/A-with-reason, not placeholders.

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":"docs/reviews/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-17.md"}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: advisory research ended before Local implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Local G1 decision-layer implementation |
| Disposition | NOT_APPLICABLE_NO_NEW_EXTERNAL_INPUT |
| Claim boundary | external return is not CVF source or design authority |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | INTERNAL_AGENT implements; Local reviews/closes |
| phase | dispatch -> worker execution -> Local review -> continuity |
| baseHeadFor(phase) | dispatchBaseHead=`899f162dece18abf42980cb82dab671626d6672e`; executionBaseHead=worker capture; closureBaseHead=Local capture |
| changedSetScope(phase) | exact seven create-only worker paths |
| traceScope(phase, actor) | source hashes, tests, gates, changed set, no commit |
| commitOwner(phase) | Local only |
| crossBatchIsolation | G1 only; G4 and other tranches excluded |
| nextMoveSurfaces | active continuity only after Local acceptance |

Before status evidence: clean worktree at dispatch base `899f162dece18abf42980cb82dab671626d6672e`; `git status --short` empty and staging empty; no pre-existing worker paths.

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: INTERNAL_AGENT implementation worker
laneOwnedPaths: exact seven Required Artifact Manifest paths
dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE
laneReleaseEvidence: full worker return, empty staging, exact changed set

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| actor | INTERNAL_AGENT worker |
| role set | implementer/tester/evidence producer, not reviewer/closer |
| role separation | worker returns uncommitted, Local accepts or rejects |
| evidence basis | governed sources, hashes, focused tests and gates |
| Gate sequence | pre-implementation; focused tests; source reconciliation; worker-return fast; Local review |
| Self-review boundary | worker repairs owned paths but cannot accept or close own implementation |
| escalation | source contradiction, forbidden effect, uncloseable gate |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | Local may create a separate dated completion review |
| reviewerOwnedClosurePaths | work-order status, review, continuity after acceptance |
| closureOwner | Local reviewer/orchestrator |
| workerCommitPermission | FORBIDDEN |

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0
closeabilityDisposition: CLOSEABLE
implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT
foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET
returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline and work order | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline and work order | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V61_2026-09-16.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact seven worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| source_reconciliation | WORKER_RETURN | worker | IMPLEMENTATION | exact seven worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact seven worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | source_reconciliation |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact seven worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker paths and completion review | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | completion review | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO_NEW_RUNTIME_CLAIM |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | predecessor/current source hashes and synthetic tests |
| reason | pure offline decision owner |
| requiredFutureAction | separate empirical/live/runtime authority |

## Foundation Storage Layout Block

Seven flat files only. No durable store, generated aggregate, registry,
runtime service or file relocation is authorized.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | pure offline G1 decision contract and checker |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: implementation requires worker tests and Local review |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no real calibration/provider receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: dispatch hashes and gates; worker tests pending |
| invocationBoundary | local synthetic inputs and read-only evidence files |
| interceptionBoundary | no runtime wrapper, provider call or dispatcher action |
| claimLanguage | contract implemented pending review, never empirically calibrated |
| forbiddenExpansion | G4, real calibration, provider/live, runtime, public, deployment |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T2-TASK-CLASS-CALIBRATION-OWNER-IMPLEMENTATION --title "ACEL G1 T2 Task-Class Calibration Owner Implementation" --date 2026-09-17 --base 899f162dece18abf42980cb82dab671626d6672e --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-17.md --include-worker-return-skeleton --no-evidence-readiness-applicable --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --scec-problem-key acel-g1-empirical-calibration-owner-composition --scec-chain-mode SUCCESSOR --scec-chain-ordinal 1 --scec-predecessor-path docs/reviews/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-17.md --scec-predecessor-sha256 4c8a4978ba9da86af8fe45276dbe7f875bc442e296fcd600f8b834e0d95e4644 --scec-required-disposition READY_WITH_EXECUTABLE_PROOF --scec-successor-scope EXECUTABLE_IMPLEMENTATION --stdout` |
| generatedProfile | manual governed dispatch |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | exact G1 contract, seven paths, roles, gates, boundary |
| checkerReadAheadConfirmation | dispatch, route, convergence, closeability, trace and claim boundary |
| docOnlyNewFields | none |
| claimBoundary | dispatch provenance, not implementation proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`. Returned ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044; count 10, truncated from 24 candidates.

## Closure Checklist

- [ ] Worker captures execution base and no-commit status.
- [ ] Exact predecessor and current source hashes reconcile.
- [ ] Seven outputs stay in scope and all negative tests/gates pass.
- [ ] Local reviews and records terminal disposition separately.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `DISPATCH_READY` | PASS |
| Completion or reviewer artifact | future Local completion review | worker has not returned | BLOCKED with reason: pre-execution |
| Roadmap state | active ACEL continuity | G1 T2 selected; G4 parked | PASS |
| Registry JSON | G1 T1 design manifest | five-path successor | PASS |
| Registry Markdown | G1 T1 human design | accepted by Local review | PASS |
| External evidence digest | N/A with reason: no new external input | advisory phase closed | N/A with reason |
| System loop interlock | no runtime consumer | pure offline contract | N/A with reason: runtime forbidden |
| Session continuity | active handoff/front door/state | post-dispatch sync required | BLOCKED with reason: follows material dispatch commit |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| predecessor release | accepted G1 design and five paths | exact hashes and no collisions | PASS |
| implementation | pure decision layer, checker, tests and audit | pending worker return | BLOCKED with reason: pre-execution |
| worker commit | forbidden | pending worker execution | BLOCKED with reason: pre-execution |
| provider/runtime | forbidden | zero dispatch calls/mutations | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | G1 pure decision contract | seven uncommitted paths | current private-CVF design and tests | Local review | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | none | zero calls or authority | advisory research closed | separate adapter authority | `DEFERRED_WITH_REASON` |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| G1 separate implementation is design-ready | DEPENDENCY | `docs/reviews/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-17.md` | Decision / Recommendation / Disposition | `DESIGN_READY_FOR_SEPARATE_IMPLEMENTATION_WORK_ORDER` | Local completion | ACCEPT |
| exact five paths and semantics | MANIFEST | `docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json` | `successorManifest`, `negativeCases` | five paths | G1 design | ACCEPT |
| G3 is a grader/admission input | CONTRACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/assf.behavioral.evaluation.contract.ts` | `gradeBehavioralEvaluation`, `admitFixtureSet` | G3 owner | pure G3 contract | ACCEPT |
| benchmark reports are proposal-only | CONTRACT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/performance.benchmark.harness.contract.ts` | `EvidenceClass` | `PROPOSAL_ONLY` | benchmark harness | ACCEPT |
| readiness is a gate, not ranking | BOUNDARY | `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` | Scope And Claim Boundary | provider-lane status | readiness matrix | ACCEPT |

## Negative Search And Collision Discipline

All nine dispatch/worker target paths were absent at clean base
`899f162dece18abf42980cb82dab671626d6672e`. No broad absence claim is
made; the exact-path successor manifest is an accepted design proposal.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | first-section envelope, ready status, source verification, seven-path fulfillment, closeability graph, no-commit return |
| gateRunPurpose | pre-dispatch confirmation, not semantic proof |
| claimBoundary | offline implementation pending worker evidence and Local review |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer as dispatcher |
| Provider or surface | private CVF workspace |
| Session or invocation | ACEL G1 T2 dispatch, 2026-09-17 |
| Working directory | repository root |
| Command or tool surface | governed reads, SHA-256, apply_patch, gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | operator continue instruction, V61 bounded selection |
| Before status evidence | clean worktree at `899f162dece18abf42980cb82dab671626d6672e`; `git status --short` empty |
| After status evidence | exact two dispatch artifacts pending verification |
| Diff evidence | `git status --short`; `git diff --check` |
| Approval boundary | pure offline G1 implementation dispatch only |
| Claim boundary | no measured calibration, provider/live or runtime claim |
| Agent type | dispatcher |
| Invocation ID | `acel-g1-t2-task-class-calibration-dispatch-20260917` |
| Expected manifest | paired baseline and work order |
| Actual changed set | same two paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This order authorizes seven uncommitted G1 offline implementation outputs.
No empirical operating point, G4 measurement, provider/live action,
configuration mutation, Core/runtime wiring, public sync or deployment.

## Operator Checkpoint

Real evaluation/calibration, provider/live, configuration selection or
mutation, G4 experiment, Core/runtime, public sync and deployment remain
parked for separate Local selection and operator authority.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
