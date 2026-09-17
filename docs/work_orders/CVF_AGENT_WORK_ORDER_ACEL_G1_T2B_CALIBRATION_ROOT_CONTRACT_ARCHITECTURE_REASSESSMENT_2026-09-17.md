# CVF Agent Work Order - ACEL G1 T2B Calibration Root Contract Architecture Reassessment

Memory class: governed-worker-dispatch

docType: work_order

Status: APPROVED_FOR_EXECUTION

Batch ID: ACEL-G1-T2B-CALIBRATION-ROOT-CONTRACT-ARCHITECTURE-REASSESSMENT

Dispatch base head: `762ec1be1ba13d8c6f2e1f3771d680038ac0b449`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: one shared-workspace `INTERNAL_AGENT`

Reviewer/closer: Local orchestrator/reviewer

Worker return path: `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_WORKER_RETURN_2026-09-17.md`

## Dispatch Prompt Envelope

Role: architecture-contract designer and evidence producer, not reviewer.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture with `git rev-parse HEAD` before edits.

Current-time note: 2026-09-17; Local has already selected the four architecture decisions below.

Do-not-misread: this is a fresh T2B documentation tranche. Do not repair T2A,
touch the ten parked paths, implement code, call providers, open G4/runtime or
invent a fifth architecture option.

Required first actions: read startup front doors, active handoff, guard
orientation, literal gotchas, paired baseline, this packet and every named
source/checker before writing.

Return contract: create exactly three outputs, run required gates, make no
commit, and return `COMPLETE_PENDING_REVIEW` only with passing required gates;
otherwise return `BLOCKED_WITH_REASON`.

## Purpose

Design a fresh, independently implementable G1 calibration root contract from
the four Local architecture decisions. Success is exact human/JSON parity,
collision-resistant canonicalization, explicit authority and temporal
invalidation semantics, without inheriting T2A's rejected topology.

## Authority Chain

- Operator instruction: 2026-09-17 request to orchestrate and issue a Claude work order.
- Active session: `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V61_2026-09-16.md`.
- Terminal review: `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_R2_INDEPENDENT_REVIEW_2026-09-17.md`.
- GC-018: `docs/baselines/CVF_GC018_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md`.
- Accepted predecessor design: `docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json`.

Local architecture decision in the paired baseline overrides conflicting T2A
worker prose. Repository authority overrides provider memory or narrative.

## Roles And Scope

| Role | Responsibility |
|---|---|
| Local orchestrator/reviewer | selected architecture, owns review, closure and commits |
| INTERNAL_AGENT worker | reads bounded sources and authors exactly three fresh outputs |
| operator | approves later implementation/live expansion, not routine in-scope formatting repair |

Allowed: read named evidence, design the selected schema, create exactly the
three manifest paths, and repair formatting/JSON/gate defects within them.

Forbidden: nested subagents; edits to any existing file; worker commit/staging;
code/tests/checker implementation; provider/network/credential use; real
calibration; G4; runtime; configuration mutation; public sync; deployment.

Delegation depth is fixed at zero. Do not use an Agent/subagent tool.

## Pre-Flight Checks

- Capture `executionBaseHead`, unstaged status and empty staging before edits.
- Verify all three output paths are absent and all ten frozen hashes match.
- Read every required source and applicable checker before authoring.
- Stop with `BLOCKED_WITH_REASON` on authority contradiction or frozen drift.

## Write Ownership

The worker owns writes only to the three Required Artifact Manifest paths.
Local owns every commit, review, continuity change and future implementation
decision. Existing files, including the ten parked paths, are read-only.

## Execution Plan

1. Reconcile sources and the ten-path freeze ledger.
2. Compose one integrated human root contract from the four fixed decisions.
3. Encode the same contract in JSON with a field/rule parity self-check.
4. Create the worker return, run required gates and report exact evidence.

## Evidence Requirements

Return exact source/frozen hashes, start/end HEAD and status, output inventory,
human/JSON parity results, architecture negative-case coverage, commands and
verbatim gate dispositions. Narrative assurance is not substitute evidence.

## Required First Reads

1. `CVF_SESSION_MEMORY.md` and active bootstrap/handoff.
2. `docs/reference/guard_orientation/README.md` and literal gotchas.
3. Paired GC-018 baseline and this work order.
4. T2A terminal R2 review, R1 review, rejected T2A human/JSON/return evidence.
5. Accepted G1 T1 human and JSON design.
6. `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md`, Invariant 5 and NC-05, as pattern evidence only.
7. Applicable checker sources named in the read-ahead block.

## Selected Architecture - Mandatory, Not Optional

1. Define immutable `HeldOutFixtureSetAuthority`, issued before candidate
   evaluation by the calibration-round decision owner. It binds task class,
   SEARCH/HELD_OUT partition identity, comparability inputs, exact sorted
   required member identities/classes/content hashes and its canonical hash.
   Each candidate references this exact authority hash; candidates cannot
   author or mutate it.
2. Define separate `requiredEvidence[]` and `supplementalEvidence[]` fields.
   Exact required-member equality is mandatory. Supplemental evidence is
   disclosure-only and cannot satisfy admission, alter preference/value,
   create a regression binding or cure missing required evidence.
3. Define a new profile, suggested ID
   `cvf.taskClassCalibration.rootContractHash.v1`: SHA-256 of UTF-8 RFC 8785
   JCS canonical JSON, fixed named fields, explicit null/empty behavior,
   lexicographic ordering for set-semantic arrays, declared ordering for
   sequence-semantic arrays, decimal values represented as canonical strings,
   and at least one full published preimage/digest vector plus delimiter-
   collision negative vectors. Adapt the pattern; do not claim SOT3 ownership.
4. Separate immutable `OperatingPointAcceptanceBinding` from append-only
   `OperatingPointInvalidationReceipt`. The receipt binds prior acceptance
   hash, trigger, observed current-state snapshot/source, comparison result,
   checked-at time and predecessor receipt hash. Current validity is derived
   from the latest verified receipt; later events never mutate historical
   acceptance provenance.

## Design Requirements

- Define exact field types, authority owner, creation time, mandatory path,
  equality/membership edges, duplicate/missing/extra/malformed behavior,
  bypass behavior and fail-closed result.
- Bind task class, candidate/configuration, authority, complete required
  fixture envelope, G3 result, trace identity/mode/content, full producer
  receipt content, preference policy/authority/value and acceptance state.
- Provide explicit positive and negative matrices, including cross-candidate
  pooling, supplemental laundering, candidate-authored authority, stale or
  forked invalidation receipt, delimiter-shaped strings, array reorder and
  missing current-state source.
- State TypeScript decision-owner versus Python persisted-checker responsibility
  for every edge. Checker proof must be independently recomputable, not shape-only.
- Define migration disposition for all ten parked evidence paths, but do not
  modify or accept them.
- Do not claim the document makes future implementation correct. Name exact
  future implementation/checker/test paths only as planning input.

## Required Artifact Manifest

| Artifact | Required action |
|---|---|
| `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md` | create human-readable root contract and matrices |
| `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_MANIFEST_2026-09-17.json` | create exact machine-readable parallel contract and self-check |
| `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_WORKER_RETURN_2026-09-17.md` | create full no-commit return and evidence packet |

No optional fourth worker artifact is allowed.

## Parked Evidence Freeze

These ten untracked paths are read-only. Recompute hashes at start and return;
any mismatch is `BLOCKED_WITH_REASON`:

| Path | Expected SHA-256 |
|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts` | `5c26e2bc732da98082ed3b0c1ed4c35fdcb40c5c5b16023e281ea6a3a741a37f` |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts` | `24302b66728de7de3173b4fcb999034412ef4a47c8c27f5e17fbf581352b8046` |
| `docs/audits/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md` | `97510bff2a40e4868625d1f016e87d2bbaab9812380ded5a20c2f24b65625708` |
| `docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md` | `3ddb27af5abf0d8197bfdaa28eac2e7b83c422c3342a4b3acb2abf25b65cdb86` |
| `docs/reviews/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_WORKER_RETURN_2026-09-17.md` | `1ac61b304063f57eda3f7db2a8ec3681a0af3d6c8e58ec04c3d5228e7f759594` |
| `governance/compat/check_task_class_calibration_owner_evidence.py` | `761eefa1f093e4cdddb4e73496b04f9694a15622a5ce34dd685d4acae3498d0f` |
| `governance/compat/test_check_task_class_calibration_owner_evidence.py` | `ac85ed1b6ad5288c95aeada7baab45782c58f97bbdfd45cb4a126ea6a124eeec` |
| `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md` | `02b97f0db77b6518000c13aff30bc131b88b426809f9f8aa43c89bad2b5ebbda` |
| `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json` | `0bf99eeaf3e8a979000ffc411639a987abf60d1d5ff556dad38ba354b24f137e` |
| `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_WORKER_RETURN_2026-09-17.md` | `f12688934bcb1ef0fdaaea1ae45186cce14cfcba69fc5061334abbee8e8462f6` |

## Acceptance Criteria

1. Human and JSON artifacts agree field-for-field and rule-for-rule.
2. All four Local decisions are implemented without an alternative topology.
3. Candidate preference is impossible without exact required-member coverage
   and bound PASS evidence from the same candidate.
4. Supplemental evidence is provably non-authoritative for every decision path.
5. Every hash has one complete JCS preimage definition and reproducible vector;
   delimiter-shaped distinct inputs cannot collide before SHA-256.
6. Acceptance provenance and later invalidation event evidence are distinct,
   linked, independently verifiable and fail closed on stale/forked chains.
7. Every owner/mandatory path/bypass/fail behavior is explicit.
8. Ten parked paths remain byte-identical; exactly three fresh paths exist;
   staging empty and worker made no commit/subagent/provider call.
9. Required gates pass. A failed gate, even out of worker scope, requires
   `BLOCKED_WITH_REASON`; disclose scope without relabeling it PASS.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G1-T2B-CALIBRATION-ROOT-CONTRACT-ARCHITECTURE-REASSESSMENT
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t2b-root-contract-architecture","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["fixture_authority_not_composed","required_supplemental_topology_not_composed","canonical_hash_profile_not_composed","temporal_invalidation_receipt_not_composed"],"reopened":[],"current":["fixture_authority_not_composed","required_supplemental_topology_not_composed","canonical_hash_profile_not_composed","temporal_invalidation_receipt_not_composed"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T2B-ARCHITECTURE-DISPATCH","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/baselines/CVF_GC018_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md"}],"requiredDisposition":"ROOT_CONTRACT_REQUIRED","successorScope":"INTEGRATED_ROOT_CONTRACT"}
```

Worker return must carry a successor SCEC block but must not mark blockers
resolved or cite `ACCEPTED_REVIEW` before Local review. Retain them as current
and describe candidate closure evidence for Local disposition.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T2B-CALIBRATION-ROOT-CONTRACT-ARCHITECTURE-REASSESSMENT","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"DOC_CHANGE","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["AGENT_HANDOFF_V61_2026-09-16.md","docs/audits/","docs/reviews/","docs/baselines/","docs/work_orders/","docs/reference/agent_system_skills/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/","governance/compat/"],"claims":["fresh G1 T2B calibration root-contract architecture only"],"requiredProof":["source and ten-path hash reconciliation","human/JSON parity","canonicalization vectors","negative-case matrix","worker-return fast gate","Local review"],"operatorCheckpoints":["implementation","real calibration","provider/live","configuration mutation","G4","runtime","public sync","deployment"],"forbiddenEffects":["edit parked evidence","provider call","network effect","credential access","configuration mutation","worker commit","nested subagent","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_R2_INDEPENDENT_REVIEW_2026-09-17.md","completenessClaimChanged":false}}
```

providerExecutionAuthority: FORBIDDEN

## Worker Autonomy / No-Question Rule

Proceed without operator confirmation for non-destructive edits within the
three output paths. Repair JSON, formatting, source-ledger and gate defects
there. Stop only for missing/contradictory authority, frozen-path drift,
forbidden-scope need or any required gate that cannot pass within scope.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class DOC_CHANGE --role dispatcher --lifecycle-phase pre-dispatch`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | status; prompt envelope; SCEC; closeability graph; worker-return headings; trace/Delta labels |
| gateRunPurpose | confirmation after architecture decision and source verification, not first discovery |
| claimBoundary | checkers prove packet shape only, not root-contract correctness |

## Source Verification Block

Use the paired baseline's source table. Recompute the three named source hashes
and all ten frozen hashes before writing. Provider memory is `NOT_CVF_SOURCE`.

## Negative Search And Collision Discipline

Pre-authoring checks found all five T2B baseline/work-order/output paths absent
and the exact batch ID/title absent from `docs` and `CVF_SESSION`. T2B is a
fresh successor name. The worker must also supply semantic collision vectors
for comma, pipe, quote, backslash, Unicode escape, empty/null and array reorder.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | baseline and work order | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | baseline and work order | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V61_2026-09-16.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact three outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| source_reconciliation | WORKER_RETURN | worker | IMPLEMENTATION | exact three outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| frozen_input_integrity | WORKER_RETURN | worker | IMPLEMENTATION | read-only ten-path ledger | NO_MUTATION | closer | MATERIAL_COMMIT | source_reconciliation |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact three outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | frozen_input_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact three outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return ADIF disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker outputs and completion review | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | adif_integrity |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | future Local completion review | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Non-archive authority contract source: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | one INTERNAL_AGENT audits/designs/returns evidence; Local independently reviews |
| phase | dispatch -> design -> Local review -> optional continuity |
| baseHeadFor(phase) | dispatchBaseHead=`762ec1be1ba13d8c6f2e1f3771d680038ac0b449`; executionBaseHead=worker captures; closureBaseHead=Local captures |
| changedSetScope(phase) | exact three fresh worker paths |
| traceScope(phase, actor) | start/end HEAD, source/frozen hashes, commands, gates, no-commit evidence |
| commitOwner(phase) | Local only |
| crossBatchIsolation | ten parked paths read-only; unrelated worktree changes reported, never repaired |
| nextMoveSurfaces | Local updates active handoff/state only after disposition |

Before status evidence: tracked worktree clean at dispatch base
`762ec1be1ba13d8c6f2e1f3771d680038ac0b449`; exactly ten named frozen untracked
paths were present and the three future worker paths were absent.

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT design worker

laneOwnedPaths: exact three Required Artifact Manifest paths

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return, empty staging, exact worker delta and
byte-identical ten-path hash reconciliation

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_COMPLETION_2026-09-17.md` |
| reviewerOwnedClosurePaths | work-order status, completion review and continuity after acceptance |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_WORKER_RETURN_2026-09-17.md`

contractProfile: `WORKER_RETURN_FULL_GATE_V1`

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

Required sections: Purpose; Scope / Methodology; Findings / Position; source
and frozen hash reconciliation; human/JSON parity; architecture self-check;
Risk / Corrective Action; Semantic Convergence Outcome; Return-Time
Closeability Recheck; Checker Source Read-Ahead Block; Agent Operation Trace
Block; Delta Execution Claim Boundary Control Block; Public Export
Disposition; Epistemic Process Block; Claim Boundary; command evidence;
`git status --short`; no-commit/no-subagent statement.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python -m json.tool docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_MANIFEST_2026-09-17.json
git diff --check
git status --short
git diff --cached --name-only
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer as dispatcher |
| Provider or surface | private CVF workspace |
| Session or invocation | G1 T2B root-contract architecture dispatch, 2026-09-17 |
| Working directory | repository root |
| Command or tool surface | governed reads, source/hash verification, scaffold helper, apply_patch and gates |
| Target paths | paired baseline/work order only; three future worker paths named |
| Allowed scope source | operator instruction plus terminal T2A review |
| Before status evidence | tracked worktree clean at HEAD `762ec1be1`; ten named untracked parked evidence paths present; T2B paths absent |
| After status evidence | dispatch packet pending gates/commit |
| Diff evidence | exact paired dispatch paths |
| Approval boundary | documentation-only fresh root contract design |
| Claim boundary | no implementation/provider/live/runtime/G4/public/deploy effect |
| Agent type | dispatcher |
| Invocation ID | `acel-g1-t2b-root-contract-dispatch-20260917` |
| Expected manifest | baseline plus work order |
| Actual changed set | baseline plus work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | dispatch documentation and selected architecture only |
| claimDisposition | CLAIM_REJECTED: no implemented execution-control capability claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime/provider receipt created |
| actionEvidence | ACTION_EVIDENCE_PRESENT: Local source review and dispatch authoring only |
| invocationBoundary | local documentation operations only |
| interceptionBoundary | no OS/IDE/provider/CLI/MCP interception claim |
| claimLanguage | fresh design task dispatched pending worker and Local review |
| forbiddenExpansion | implementation, provider/live, G4, runtime, public sync, deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private root-contract architecture dispatch; no public-sync authority.

## Closure Checklist

- Exactly three fresh worker outputs exist and agree semantically.
- Ten frozen paths retain their expected hashes; staging and worker commits are absent.
- Required gates pass and the worker return contains reproducible evidence.
- Local independent review, not worker self-assessment, decides acceptance.

## Review Gate

Local applies contradiction probes to authority ownership, exact required-set
coverage, supplemental non-authority, canonical preimages and invalidation
chain behavior. Gate-green output is necessary but not sufficient for closure.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every acceptance criterion and gate
passes. Otherwise return `BLOCKED_WITH_REASON` with the exact blocker, scope
classification and evidence; do not modify an existing or frozen path.

## Operator Checkpoint

No operator checkpoint applies to bounded documentation corrections. Operator
approval remains parked for any later implementation, live/provider, runtime,
G4, public-sync or deployment expansion.

## Claim Boundary

This work order authorizes exactly three fresh documentation outputs. It does
not accept T2A, permit edits to parked evidence, authorize implementation or
empirical value, call a provider, open G4/runtime, publish or deploy. Worker
self-review cannot close the tranche; Local independent review is mandatory.
