# CVF Agent Work Order - ACEL G1 T2A Candidate Evidence Binding Schema Amendment

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-17

Batch ID: ACEL-G1-T2A-CANDIDATE-EVIDENCE-BINDING-SCHEMA-AMENDMENT

Dispatch base head: `a9813bb3e4fbc53ffc245ec19a0f3808ef16f93e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: shared-workspace `INTERNAL_AGENT` schema/design worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md`

Paired baseline: `docs/baselines/CVF_GC018_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md`

Worker return path: `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_WORKER_RETURN_2026-09-17.md`

Commit mode: WORKER_MUST_NOT_COMMIT. Capture `executionBaseHead` at start;
leave HEAD and staging unchanged.

Current-time notes: seven rejected G1 T2 paths already exist untracked. They are
frozen inputs, not this worker's changes. Record their before/after hashes and
do not edit, stage, delete, rename or commit them.

Do-not-misread notes: this is a fresh design amendment, not R3 implementation
repair, acceptance of rejected code, or permission to open G4/live/runtime.

Required first actions: read startup authority, paired baseline, this packet,
R2 review, accepted T1 manifest, seven frozen paths and applicable checkers;
then capture execution base, status, staging and all seven hashes before edits.

Return contract: return `COMPLETE_PENDING_REVIEW` only after exact-three-output reconciliation
and required gates pass; otherwise return `BLOCKED_WITH_REASON`.

## Purpose

Design a fresh root-contract amendment for G1 candidate evidence binding. The
result must close the candidate-scoped fixture, GC-026 record equality,
canonical provenance and checker-recomputation blockers identified by Local
R2 review. Do not repair implementation in this tranche.

## Authority Chain

1. Operator instruction on 2026-09-17: continue the G1-G6 roadmap.
2. Active continuity: `AGENT_HANDOFF_V61_2026-09-16.md` and
   `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
3. Terminal R2 review: `docs/reviews/CVF_ACEL_G1_T2_R2_INDEPENDENT_REVIEW_2026-09-17.md`,
   SHA-256 `c29cf63ff0aed8c294e61f3286e98ac18242b30b4a3f16445dc1a7310eba175f`.
4. Accepted T1 design manifest:
   `docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json`,
   SHA-256 `c8c1f6899e50513141e69113b8ac9faf37669b1fcd785bc2df3b88d8e894505b`.
5. Paired GC-018 baseline named in the dispatch envelope.

If these sources conflict, preserve the contradiction and return blocked. The
R2 review controls the rejection facts; the T1 manifest controls unchanged
design requirements. Provider-local memory or chat summaries are not authority.

## Scope / Methodology

Read and reconcile a bounded source set; define records, ownership edges,
canonicalization, equality constraints, invalidation triggers and negative
cases; then publish human and JSON contracts. The design must be independently
implementable without requiring hidden Claude context.

Allowed worker actions:

- read current governed sources and the seven frozen rejected paths;
- compute local file hashes and run read-only searches/checkers;
- create exactly the three Required Artifact Manifest paths;
- repair only those three paths for allowed-scope gate failures.

Forbidden worker actions:

- modify any of the seven rejected G1 T2 paths;
- modify accepted T1 design, work order, baseline, handoff or session state;
- implement TypeScript/Python, run provider/live calibration, use credentials,
  mutate configuration/runtime, open G4, public-sync, deploy or commit;
- spawn nested subagents. The parent worker may use its own reasoning and
  tools but delegation depth for this dispatch is fixed at zero.

## Agent Roles

| Role | Responsibility |
|---|---|
| Local orchestrator/reviewer | selected recovery lane, owns final disposition and commits |
| INTERNAL_AGENT worker | bounded source auditor and schema author; no commit |
| external Web agent | no role; prior advisory research is not implementation authority |
| operator | selects later implementation/live expansion, not routine document repair |

## Required First Reads

1. `AGENTS.md`, bootstrap, front door and active handoff.
2. Paired baseline and this work order.
3. `docs/reference/guard_orientation/README.md` and literal-format gotchas.
4. R2 independent review and accepted T1 human/JSON design.
5. All seven frozen rejected paths.
6. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/assf.behavioral.evaluation.contract.ts`
   for actual G3 fixture/trace semantics.
7. `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md`
   for review-round and stop discipline.
8. Applicable checker sources before authoring governed outputs.

## Pre-Flight Checks

Before writing, capture `executionBaseHead`, clean staging evidence, exact
status, absence/presence of every governed path and SHA-256 for all seven
frozen inputs. Stop on a source contradiction or changed frozen-input hash.

## Write Ownership

The INTERNAL_AGENT owns only the exact three create-only outputs. Local owns
review, acceptance, every commit and continuity. No nested delegation or
write outside the manifest is authorized.

## Execution Plan

Read and reconcile authority; specify the four schema edges; produce human
and JSON artifacts with exact parity; write the no-commit return; then run the
required focused and aggregate gates. Do not repair implementation.

## Evidence Requirements

Return exact paths, symbols, hashes, negative-case matrices, fail behavior,
mandatory-path/bypass semantics, command results, frozen-input before/after
reconciliation and empty staging proof. Claims without repository evidence
remain blocked.

## Frozen Rejected Input Ledger

These paths must remain byte-identical. Recompute all hashes at worker start
and return; a mismatch is `BLOCKED_WITH_REASON`.

| Path | Dispatch-observed SHA-256 | Role |
|---|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts` | `5c26e2bc732da98082ed3b0c1ed4c35fdcb40c5c5b16023e281ea6a3a741a37f` | rejected implementation evidence |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts` | `24302b66728de7de3173b4fcb999034412ef4a47c8c27f5e17fbf581352b8046` | rejected test evidence |
| `docs/audits/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md` | worker recomputes at start | rejected audit evidence |
| `docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md` | worker recomputes at start | rejected reference evidence |
| `docs/reviews/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_WORKER_RETURN_2026-09-17.md` | worker recomputes at start | rejected self-report evidence |
| `governance/compat/check_task_class_calibration_owner_evidence.py` | `761eefa1f093e4cdddb4e73496b04f9694a15622a5ce34dd685d4acae3498d0f` | rejected checker evidence |
| `governance/compat/test_check_task_class_calibration_owner_evidence.py` | `ac85ed1b6ad5288c95aeada7baab45782c58f97bbdfd45cb4a126ea6a124eeec` | rejected checker-test evidence |

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md` | create human design, source/equality/negative-case/migration matrices |
| `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json` | create machine-readable exact schema and successor manifest |
| `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_WORKER_RETURN_2026-09-17.md` | create full no-commit evidence return |

All three paths were absent at dispatch authoring. No optional fourth worker
path is allowed.

## Design Requirements

### Candidate-Scoped Evidence Set

Define one normalized candidate evidence-set record that can express multiple
required fixtures. It must bind task class, candidate identity/configuration,
admitted held-out fixture-set identity, per-fixture G3 evaluation and producer
receipt. Round-level positive/negative diversity cannot be borrowed across
candidates. State exact set-coverage, duplicate, missing, extra, ordering and
malformed behavior.

### GC-026 Authority Topology

Choose exactly one non-ambiguous topology:

- the hashed attestation record is the single source of promotion record/time;
  or
- outer fields remain but must exactly equal hashed inner fields.

Define registry-snapshot meaning and honestly state what can be verified
offline without a real registry lookup. Shape-valid arbitrary hashes cannot be
described as proof of registry membership.

### Canonical Provenance And Invalidation

Define a versioned, typed preimage with unambiguous length/domain separation.
At minimum decide binding for task class, accepted candidate/config, complete
evidence-set/envelope hashes, fixture and trace identities, capture modes,
producer receipt identity/content, preference policy identity, full authority
record or rubric identity and deterministic score/value input. Map every
invalidation trigger to the exact bound field(s).

### Checker And Test Contract

For every equality, membership, coverage and preimage edge, state whether the
TypeScript owner or Python persisted-evidence checker enforces it, the mandatory
path, bypass behavior and fail result. Include positive controls and negative
cases that would have caught all R2-RV-F1 through F4. A test fixture may not
manufacture admission by appending evidence from another candidate.

### Migration / Successor Boundary

Classify each rejected path `REPLACE_IN_SEPARATE_IMPLEMENTATION`,
`REUSE_AFTER_EXACT_CHANGE`, or `DISCARD_WITH_REASON`. Name the exact future
successor paths and whether in-place replacement is safe. Do not modify or
accept any rejected path here.

## Acceptance Criteria

1. Human and JSON artifacts agree on record topology, fields, equality edges,
   canonicalization and negative cases.
2. Every R2-RV-F1 through F4 maps to one design rule and at least one required
   future regression.
3. Preferred status is impossible unless the same candidate covers every
   required held-out fixture with bound `PASS_WITH_EVIDENCE`.
4. GC-026 outer/inner contradiction is structurally impossible or rejected.
5. Every declared invalidation trigger maps to provenance-bound content.
6. Checker responsibility is independent and recomputable, not shape-only.
7. Seven frozen paths remain byte-identical; exactly three worker paths are
   created; HEAD and staging remain unchanged.
8. Required gates pass, or return is truthfully blocked.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G1-T2A-CANDIDATE-EVIDENCE-BINDING-SCHEMA-AMENDMENT
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-empirical-calibration-owner-composition","chainMode":"SUCCESSOR","chainOrdinal":2,"predecessor":{"path":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md","sha256":"4563737b85eed9cd4b55b9a675fc2d896b1bfa19ca1b19fc35e07f1a678426e7"},"blockerDelta":{"prior":["g1_general_operating_point_owner_not_composed"],"resolved":[],"retained":["g1_general_operating_point_owner_not_composed"],"new":["candidate_scoped_required_fixture_coverage_missing","gc026_cross_record_equality_missing","provenance_preimage_incomplete","persisted_checker_recomputation_incomplete"],"reopened":[],"current":["g1_general_operating_point_owner_not_composed","candidate_scoped_required_fixture_coverage_missing","gc026_cross_record_equality_missing","provenance_preimage_incomplete","persisted_checker_recomputation_incomplete"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":1},"claims":[{"claimId":"ACEL-G1-T2A-ROOT-CONTRACT-DISPATCH","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/baselines/CVF_GC018_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md"}],"requiredDisposition":"ROOT_CONTRACT_REQUIRED","successorScope":"INTEGRATED_ROOT_CONTRACT"}
```

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T2A-CANDIDATE-EVIDENCE-BINDING-SCHEMA-AMENDMENT","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"DOC_CHANGE","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/audits/","docs/reviews/","docs/baselines/","docs/reference/agent_system_skills/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/","governance/compat/"],"claims":["fresh G1 candidate-evidence root-contract amendment only"],"requiredProof":["source hash reconciliation","human/JSON parity","negative-case matrix","worker-return fast gate","Local review"],"operatorCheckpoints":["implementation","real calibration","provider/live","configuration mutation","G4","runtime","public sync","deployment"],"forbiddenEffects":["edit rejected implementation","provider call","network effect","credential access","configuration mutation","worker commit","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/reviews/CVF_ACEL_G1_T2_R2_INDEPENDENT_REVIEW_2026-09-17.md","completenessClaimChanged":false}}
```

providerExecutionAuthority: FORBIDDEN

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | operator-selected continuation after G1 R2 rejection |
| scope classification | documentation-only root-contract amendment |
| risk sensitivity | P3 elevated because future acceptance evidence depends on schema integrity |
| selected role route | `SINGLE_AGENT_MULTI_ROLE`; Local independent review |
| escalation condition | source contradiction, frozen-path mutation or required implementation/runtime expansion |

## Worker Autonomy / No-Question Rule

Proceed autonomously inside the exact three output paths. Repair formatting,
JSON, source-ledger and gate defects there without asking. Stop only for a
material source contradiction, frozen-input hash change, missing authority or
need to touch any forbidden path/effect.

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| non-archive authority contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one INTERNAL_AGENT audits/designs; Local reviews/closes |
| phase | dispatch -> worker design -> Local review -> optional continuity |
| baseHeadFor(phase) | dispatchBaseHead=`a9813bb3e4fbc53ffc245ec19a0f3808ef16f93e`; executionBaseHead=worker captures; closureBaseHead=Local captures |
| changedSetScope(phase) | three create-only worker outputs; seven pre-existing frozen inputs excluded from worker delta |
| traceScope(phase, actor) | before/after hashes, exact source ledger, gates, no-commit evidence |
| commitOwner(phase) | Local only |
| crossBatchIsolation | G1 design recovery only; G4 and implementation excluded |
| nextMoveSurfaces | active handoff/state only after Local disposition |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT design worker

laneOwnedPaths: exact three Required Artifact Manifest paths

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return, empty staging, exact worker delta and
byte-identical frozen-input hash reconciliation

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| actor | INTERNAL_AGENT worker |
| role set | source auditor, schema designer, evidence producer; not reviewer/closer |
| delegation depth | zero; no nested subagent for this bounded design tranche |
| evidence basis | current repository paths and exact hashes, not provider memory |
| gate sequence | pre-implementation; source/hash reconciliation; JSON parse; worker-return fast; Local review |
| self-review boundary | worker may repair outputs but cannot accept its design |
| role separation ledger | worker returns pending design; Local independently accepts or rejects it |
| escalation condition | source contradiction, frozen-path mutation, missing authority or forbidden effect |

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
| frozen_input_integrity | WORKER_RETURN | worker | IMPLEMENTATION | read-only seven-path ledger | NO_MUTATION | closer | MATERIAL_COMMIT | source_reconciliation |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact three outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | frozen_input_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact three outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return ADIF disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker outputs and completion review | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | adif_integrity |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_COMPLETION_2026-09-17.md` | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Verification Commands

Worker must run and report exact results:

```powershell
git rev-parse HEAD
git status --short
git diff --cached --name-only
python -m json.tool docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json
git diff --check
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
```

The worker must additionally recompute SHA-256 for all seven frozen paths and
compare them with its own start ledger. Do not substitute the dispatch-observed
partial hash table for the worker's complete before/after ledger.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Include Purpose, Target / Source, Scope / Methodology, Findings / Position,
Risk / Corrective Action, Claim Boundary, Checker Source Read-Ahead Block,
Agent Operation Trace Block, Delta Execution Claim Boundary Control Block,
Public Export Disposition, executionBaseHead, exact status, changed files,
command evidence, frozen-input reconciliation and no-commit statement.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only if all eight acceptance criteria pass.
Otherwise return `BLOCKED_WITH_REASON` with the exact source, hash, gate or
authority blocker. No self-approval, worker commit or automatic implementation
successor.

## Closure Checklist

- all three outputs exist and no fourth worker path changed;
- human and JSON designs agree on every required field and failure rule;
- all seven frozen inputs are byte-identical before/after;
- focused validation and worker-return fast gate pass;
- staging is empty and HEAD is unchanged;
- disposition is `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` only.

## Review Gate

Local independently reviews source fidelity, schema completeness, migration
disposition and gate evidence. Worker self-review cannot close this tranche;
the named completion review is mandatory before a material commit.

## Operator Checkpoint

No new checkpoint is required for the bounded documentation return. Operator
approval remains required before implementation, live/provider execution,
configuration mutation, G4 opening, runtime expansion, public sync or deploy.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_COMPLETION_2026-09-17.md` |
| reviewerOwnedClosurePaths | work-order status, completion review and continuity after acceptance |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md"}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | N/A with reason: no new external intake in T2A |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | accepted T1 design plus Local R2 review |
| Disposition | local root-contract recovery only |
| Claim boundary | no external contract is promoted to private-CVF authority |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO_NEW_RUNTIME_CLAIM |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | current frozen source hashes and direct symbol inspection |
| reason | schema design only; no operating-point execution |
| requiredFutureAction | separate Local-accepted implementation work order |

## Foundation Storage Layout Block

Three flat audit/review outputs only. No store, registry, generated aggregate,
runtime service or file relocation is created.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py` with exact invocation recorded in the paired baseline |
| generatedProfile | generic internal no-commit dispatch |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | complete G1 root-contract recovery packet |
| checkerReadAheadConfirmation | dispatch, convergence, closeability, structural, trace and boundary guards |
| docOnlyNewFields | candidate evidence set, GC-026 equality, canonical provenance, migration disposition |
| claimBoundary | design dispatch only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044; count 10, truncated
from 24 candidates. Exact paths, frozen-input hashes, provider-local
non-authority, checker read-ahead, zero delegation depth and no-commit return
address the applicable patterns.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R2 is rejected and parked | REVIEW_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2_R2_INDEPENDENT_REVIEW_2026-09-17.md` | Independent Review Disposition | `REVIEW_REJECTED_PARKED_REDESIGN_REQUIRED` | Local reviewer | ACCEPT |
| all held-out fixtures must bind PASS | DESIGN_AUTHORITY | `docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json` | acceptance pipeline | `all required held-out G3 fixtures` | G1 T1 design | ACCEPT |
| current pooling crosses candidates | DEFECT_EVIDENCE | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts` | lines 492-507 | `roundFixturePool`, `admitFixtureSet` | rejected implementation | ACCEPT |
| GC-026 equality is incomplete | DEFECT_EVIDENCE | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts`; `governance/compat/check_task_class_calibration_owner_evidence.py` | R2-RV-F2; checker lines 293-413 | `gc026Attestation` | rejected implementation/checker | ACCEPT |
| provenance formula omits required inputs | DEFECT_EVIDENCE | `docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts` | manifest provenance formula; source lines 886-904 | `provenanceFingerprint` | G1 design/implementation | ACCEPT |
| G3 fixture/trace grader exists | DEPENDENCY | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/assf.behavioral.evaluation.contract.ts` | exported evaluator/admission symbols | `gradeBehavioralEvaluation`, `admitFixtureSet` | G3 owner | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | first Dispatch Prompt Envelope; DISPATCH_READY; exact no-commit terms; convergence JSON; closeability rows; read-ahead fields; trace and Delta labels |
| gateRunPurpose | confirm authored packet conformance after substantive source review; not first discovery |
| claimBoundary | gates prove packet shape, not schema correctness |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer as dispatcher |
| Provider or surface | private CVF workspace |
| Session or invocation | G1 T2A schema-amendment dispatch, 2026-09-17 |
| Working directory | repository root |
| Command or tool surface | governed reads, SHA-256, resolver, scaffold helper, apply_patch and gates |
| Target paths | paired baseline and work order |
| Allowed scope source | operator instruction to continue G1-G6 and R2 review reopen condition |
| Before status evidence | clean worktree: NO globally; HEAD `a9813bb3e`; exact seven pre-existing rejected untracked paths isolated outside dispatcher ownership |
| After status evidence | paired dispatch artifacts plus unchanged seven rejected paths |
| Diff evidence | `git status --short`; `git diff --check` |
| Approval boundary | documentation-only G1 schema recovery dispatch |
| Claim boundary | no implementation, provider/live, calibration or runtime effect |
| Agent type | dispatcher |
| Invocation ID | `acel-g1-t2a-schema-amendment-dispatch-20260917` |
| Expected manifest | two dispatcher paths plus seven pre-existing frozen inputs |
| Actual changed set | same at authoring |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | documentation-only G1 root-contract amendment dispatch |
| claimDisposition | CLAIM_REJECTED: no implemented execution-control or calibration capability claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no provider/runtime/calibration receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: Local source review, hashes and dispatch gates only |
| invocationBoundary | local documentation and read-only verification |
| interceptionBoundary | no direct interception, wrapper, runtime gate or model-router action |
| claimLanguage | schema recovery dispatched pending worker and Local review |
| forbiddenExpansion | rejected-path edit, R3 repair, implementation, G4, provider/live, runtime, public, deployment |

## Claim Boundary

This work order authorizes exactly three uncommitted design/evidence outputs.
It neither accepts nor repairs the rejected implementation and does not
authorize any implementation successor without a separate Local review and
operator-selected work order.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private G1 design-recovery dispatch; no public export requested.
