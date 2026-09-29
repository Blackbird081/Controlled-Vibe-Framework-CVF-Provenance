# CVF Agent Work Order - ACEL G1 T3B Group 2 Source-Creation Tooling

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Batch ID: ACEL-G1-T3B-GROUP2-SOURCE-CREATION-TOOLING

Dispatch base head: `a4c77bd0f`

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

Worker: shared-workspace `INTERNAL_AGENT`

Reviewer/closer: Local orchestrator/reviewer

Worker return path: `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-20.md`

independentProbeRequired: YES

## Dispatch Prompt Envelope

Role: bounded shared-workspace `INTERNAL_AGENT` tooling worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_2026-09-20.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture the committed HEAD at worker start and record it in
the return.

Current-time notes: Group 1 is verified; Group 2 remains
`SOURCE_NOT_CREATED`; Party A and the approver exist but their credentials and
alternate-user sessions are operator-only.

Do-not-misread notes: this packet builds hermetic tooling. It does not authorize
running as either principal, using `runas`, creating real source files,
approving/activating v1, staging, committing, admission or T3E wiring.

Required first actions: read the startup front door/bootstrap/active handoff,
guard orientation, literal gotchas, this packet, its paired baseline, every
Source Verification owner and the checker sources named below. Capture HEAD,
status, staging and the thirteen parked-path hashes before editing.

Return contract: implement exactly the five-path manifest, run the required
gates, leave all changes uncommitted and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Implement independently checkable PowerShell author/approver tooling and a
Python verifier for the first Group 2 specification and append-only decision
history, using only disposable fixtures during worker execution.

## Authority Chain

| Authority step | Evidence | Worker consequence |
|---|---|---|
| T2F accepted Group 2 contract | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | implement exact dual-hash schemas and event state machine |
| Local readiness route | `docs/audits/CVF_ACEL_G1_T3B_GROUP2_SOURCE_READINESS_ROUTE_2026-09-20.md` | tooling precedes all real principal execution |
| operator policy/principal decision | `docs/reviews/CVF_ACEL_G1_T3B_PRINCIPAL_POLICY_OPERATOR_DECISION_2026-09-20.md` | freeze exact v1 bytes and compatible approver name |
| verified account posture | Local read-only evidence recorded in active continuity at material commit `57a948c0f` | bind real mode to exact SID and fail closed otherwise |
| this GC-018 pair | paired baseline and work order | exact five outputs, no commit and no source write |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake summary | internal first-party Group 2 source-tooling implementation |
| scope classification | bounded code and evidence change with high trust-boundary sensitivity |
| risk sensitivity | cryptographic canonicalization plus two-principal durable source writes |
| selected route mode | `SINGLE_AGENT_MULTI_ROLE`: one implementation worker, separate Local reviewer/probe executor |
| role separation basis | worker cannot use credentials, execute real modes, accept its return, stage or commit |
| escalation condition | authority contradiction, sixth path, parked drift, credentials or real-source need |

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T3B-GROUP2-SOURCE-CREATION-TOOLING","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/baselines/","docs/work_orders/","docs/audits/","docs/reviews/","docs/reference/","scripts/","governance/compat/","EXTENSIONS/"],"claims":["principal-bound source tooling and hermetic validation only; no real source"],"requiredProof":["exact v1 byte vector","dual-hash recomputation","decision-chain state machine","identity and DACL negatives","independent Local probe","worker-return fast gate"],"operatorCheckpoints":["Party A spec creation","approver approval","approver activation","Local source verification","T3E consumer wiring","candidate admission"],"forbiddenEffects":["credential access","alternate-user execution","real source creation","parked-path mutation","worker commit","provider/live/public/deployment","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/audits/CVF_ACEL_G1_T3B_GROUP2_SOURCE_READINESS_ROUTE_2026-09-20.md","completenessClaimChanged":false}}
```

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3B-GROUP2-SOURCE-CREATION-TOOLING --title "ACEL G1 T3B Group 2 Source Creation Tooling" --date 2026-09-20 --base a4c77bd0f --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact Group 2 schemas, policy bytes, two-principal state machine, five-path manifest, test matrix and operator checkpoint |
| checkerReadAheadConfirmation | dispatch-quality, gate-to-role, worker-return, scaffold-provenance and operation-trace checker sources read before authoring |
| docOnlyNewFields | none |
| claimBoundary | dispatch provenance only; no source, activation, runtime, provider, public or deployment claim |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G1-T3B-GROUP2-SOURCE-CREATION-TOOLING
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

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "acel-g1-t3b-group2-source-creation-tooling-problem",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": [],
    "reopened": [],
    "current": []
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{"claimId":"ACEL-G1-T3B-TOOLING-ONLY","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"governance/compat/test_check_acel_g1_verification_authority_spec.py"}],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Dependency Release Evidence

| Dependency | Evidence | Release condition | Disposition |
|---|---|---|---|
| Group 2 outer contract | T2F Source Group 2 plus dual-hash/state-machine sections | accepted contract remains unchanged | RELEASED |
| exact decoded v1 policy | operator decision file | byte-for-byte compact JCS fixed | RELEASED |
| Party A author identity | verified Group 1 source | exact name and SID 1006 | RELEASED |
| activation approver identity | Local read-only OS verification | exact name/SID 1008, enabled, password-required, non-admin | RELEASED |
| real author/decision execution | Local acceptance of this worker return | operator acts later under separate principals | PARKED_OPERATOR_EXECUTION |

## Independent Review Probe Admission Contract

independentProbeRiskClass: HIGH

independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: REQUIRED_DIFFERENT_EXECUTION_AND_ASSERTION_PATH

positiveControl: Local independently decodes the fixed policy, recomputes both spec hashes and replays the two-event v1 chain

negativeMutationClasses: policy-byte drift, envelope-field drift, broken prior hash, invalid activation order, self-approval and duplicate active heads

expectedInformationGain: distinguish same-oracle worker tests from independent canonical-byte and event-history verification

rerunCostReason: six focused mutations provide decision-changing evidence without duplicating the worker suite

reviewerDecisionOwner: LOCAL

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | five exact worker paths below | implementation and disposable tests only; no credentials, real source, staging or commit | this packet and paired baseline | PowerShell/Python local tooling only | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no owner in this tranche | no external ingress, authentication, approval, mutation, receipt, runtime or public claim | no source authorizes an external adapter | deferred behind a fresh governed packet | DEFERRED_WITH_REASON |

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `scripts/acel_g1_party_a_group2_spec_writer.ps1` | create; Party A-bound spec-v1 writer with default non-mutating mode and explicit real mode |
| `scripts/acel_g1_approver_group2_decision_writer.ps1` | create; approver-bound append-only `APPROVED`, `REJECTED`, `ACTIVATED`, `SUPERSEDED` writer |
| `governance/compat/check_acel_g1_verification_authority_spec.py` | create; independent read-only schema/hash/chain/state/principal verifier |
| `governance/compat/test_check_acel_g1_verification_authority_spec.py` | create; focused disposable positive and negative tests |
| `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-20.md` | create checker-safe evidence return |

## Work-Order Fulfillment Manifest

The table above is the complete worker output set. The worker must not create
`governance/sources/verification_authority_spec/SPEC_v1.json` or
`governance/sources/verification_authority_spec/ACTIVATION_DECISIONS.jsonl`.

## Allowed Scope / Forbidden Scope

Allowed: create and test exactly the five manifest paths using disposable
temporary directories; repair failures confined to those paths. Forbidden:
credentials, `runas`, Party A or approver profiles, real Group 2 paths, existing
source mutation, the thirteen parked paths, staging, commit, T3E, admission,
provider/live, runtime service, public sync, deployment and production.

## Write Ownership

Worker owns uncommitted edits to the exact five paths. Local owns review,
bounded evidence repair, staging and commits. Party A later owns only new spec
files; the approver later owns only decision rows. Every other path is
read-only.

## Agent Roles

| Role | Responsibility |
|---|---|
| operator | retains both passwords and performs later principal-separated executions |
| Local dispatcher/reviewer | owns packet, review, bounded repairs, commits and independent verification |
| `INTERNAL_AGENT` worker | implements and hermetically tests exact manifest; no credentials or commit |
| Party A | later authors immutable `SPEC_v1.json` only |
| activation approver | later appends separate approval and activation events only |
| session-sync steward | updates continuity after Local disposition |

## Required First Reads

1. Startup front door, bootstrap model, active handoff, guard orientation and literal gotchas.
2. This order, paired baseline, T2F Group 2 contract, T3B readiness route and operator decision.
3. T3A-C1/C2 tooling for repaired PATH, principal, DACL and atomic-write patterns.
4. Applicable dispatch/output checker sources before authoring the return.

## Pre-Flight Checks

- Capture execution HEAD, full status, empty staging and hashes of all thirteen parked paths.
- Confirm exactly five worker paths and both real Group 2 paths are absent.
- Confirm no Party A/approver credential, private profile artifact or secret is requested.
- Run the pre-implementation autorun gate before editing.

## Implementation Contract

### Fixed v1 payload

Decoded bytes must be exact UTF-8 without BOM or trailing newline:

```json
{"admissionRequiredLookupResult":"IDENTITY_CONFIRMED","authorityId":"ACEL_G1_DECISION_OWNER","authoritySpecSchema":"cvf.acel.g1.verificationAuthoritySpec@1","freshnessThresholdSeconds":86400,"issuerVerificationRequirement":"VERIFIED_BY_LIVE_REGISTRY_LOOKUP","receiptDomain":"cvf.verifierReceipt","receiptProfileVersion":"v1"}
```

Encode these bytes as unpadded base64url in `canonicalBytesBase64`. Compute
`specHashHex` directly over the decoded bytes.

### Specification record

Use exact fields `profile`, `domain`, `specVersion`, `canonicalBytesBase64`,
`authorId`, `proposedAt`, `specHashHex`, `specFileRecordHashHex`.
`profile=cvf.source-record-canonicalization@1`, `domain=cvf.specFile`,
`specVersion=1`, and
`authorId=S-1-5-21-1644666849-912006174-747199667-1006`.
Hash compact lexicographically ordered JSON containing every field except
`specFileRecordHashHex`. Write UTF-8 without BOM/newline by exclusive create;
never overwrite or update in place.

### Decision event records

Use exact fields `profile`, `domain`, `decisionEventId`, `eventType`,
`specVersion`, `recomputedHashHex`, `approverId`, `decidedAt`,
`priorEntryHashHex`, `entryHashHex`. Use the same profile,
`domain=cvf.specDecisionEvent`, `specVersion=1`, and
`approverId=S-1-5-21-1644666849-912006174-747199667-1008`.
Each event ID is a new GUID string. Hash compact lexicographically ordered JSON
containing all fields except `entryHashHex`; append one compact JSON line only
after full validation and under an exclusive file handle.

### State machine and integrity

- `APPROVED` and `REJECTED` are mutually exclusive first decisions.
- `REJECTED` is terminal.
- `ACTIVATED` requires exactly one prior matching `APPROVED` and no prior
  `ACTIVATED`, `REJECTED` or `SUPERSEDED` for v1.
- `SUPERSEDED` requires exactly one active version and no earlier supersession
  of it. Version 1 cannot be superseded unless the invocation cites a newer
  independently valid spec version; hermetic tests may construct v2 fixtures.
- Every event independently decodes the spec content, recomputes
  `specHashHex`, and uses the prior row's exact `entryHashHex` or JSON null at
  genesis. Never trust a caller-supplied hash.
- Full history must have unique event IDs, valid links/hashes, valid per-version
  ordering and zero or one active version. Conflicts fail closed; never choose
  latest timestamp or largest version.

### Principal and filesystem boundary

Real author mode requires exact current name/SID for Party A. Real decision
mode requires exact current name/SID for the approver, `Enabled=True`,
`PasswordRequired=True`, and non-membership in local Administrators. Each mode
rejects elevation, wrong identity, unsafe/out-of-repo real paths,
noninteractive confirmation and pre-existing output collisions before write.
Use only DACL sections; do not request `SeSecurityPrivilege`. Each created file
must be owned by its creating principal and hardened against modification by
the other principal while remaining readable for Local verification. Directory
ambient create rights are not source proof; checker acceptance requires exact
file owner, DACL and record identity after real execution.

### Modes and output language

Default invocation is non-mutating and documents intended actions. Explicit
real modes require exact typed confirmations. Provide a hermetic self-test mode
or parameterized fixture root that never targets the repository source paths.
Successful real author mode may say only
`SPEC_CREATED_PENDING_LOCAL_VERIFICATION`; successful decision append may say
only `DECISION_APPENDED_PENDING_LOCAL_VERIFICATION`. Neither may claim source
establishment, activation validity, consumer binding or admission.

## Worker Autonomy / No-Question Rule

Repair all allowed-scope implementation and gate failures directly. Stop only
for credentials, alternate-user/real-source execution, a sixth output, parked
drift, source-authority contradiction or irreparable mandatory-gate failure.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | two PowerShell tools, one Python checker, one focused test and one worker return |
| Storage decision | exact standalone paths; no additional folder, registry, queue, aggregate or runtime store |
| Existing aggregate impact | none during worker execution |
| Generated state impact | none during worker execution |
| Durable governance boundary | checker is read-only; real sources remain absent and operator-gated |

## ADIF Defect Registry Disclosure

Dispatcher query `CODE_CHANGE`/`dispatcher`/`dispatch` returned zero defects.
Worker must rerun for `CODE_CHANGE`/`worker`/`implementation` and disclose the
actual result in the return.

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | exact Source Verification columns, dispatch/control fields, Gate-To-Role graph labels, return headings, trace labels and no-commit evidence |
| gateRunPurpose | confirm authored packet after contract design |
| claimBoundary | packet shape only; worker must separately read output-specific checker sources |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| exact Group 2 fields and hashes | schema/invariant | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Closed Preimage Field Lists; Two Distinct Group 2 Hashes; Source Group 2 | `cvf.specFile`; `cvf.specDecisionEvent` | operational source contract | ACCEPT |
| event state machine | transition invariant | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Explicit Approval, Activation And Supersession | `APPROVED`; `ACTIVATED`; `SUPERSEDED` | activation history contract | ACCEPT |
| exact v1 decoded bytes | literal policy | `docs/reviews/CVF_ACEL_G1_T3B_PRINCIPAL_POLICY_OPERATOR_DECISION_2026-09-20.md` | Operator Decision | compact JCS v1 payload | operator decision | ACCEPT |
| Party A exact identity | identity | `docs/audits/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_LOCAL_VERIFICATION_2026-09-20.md` | Source Verification Result | Party A name and SID 1006 | Group 1 verified source | ACCEPT |
| approver exact identity | identity | `docs/reviews/CVF_ACEL_G1_T3B_PRINCIPAL_POLICY_OPERATOR_DECISION_2026-09-20.md` | Operator Decision; Launcher Artifacts | approver name and SID 1008 | activation authority | ACCEPT |
| no existing Group 2 source | path state | `docs/audits/CVF_ACEL_G1_T3B_GROUP2_SOURCE_READINESS_ROUTE_2026-09-20.md` | Readiness Evidence | proposed spec/decision paths | Local readiness audit | ACCEPT |

## Negative Search And Collision Discipline

All paired packet paths, five worker outputs and two real source paths returned
`False` before authoring. Exact batch/tool/checker search returned no
predecessor. Any later unexpected collision is a stop condition except the
five lane-owned outputs created by this worker.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline/work order | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline/work order | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact five outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact five outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact five outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | returned five paths | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | Local dispatcher -> no-commit INTERNAL_AGENT worker -> Local reviewer/closer |
| phase | T3B source-creation tooling; real Party A/approver execution excluded |
| baseHeadFor(phase) | dispatchBaseHead=`a4c77bd0f`; executionBaseHead captured by worker; closureBaseHead set by Local |
| changedSetScope(phase) | exact five required outputs |
| traceScope(phase, actor) | reads, commands, tests, hashes, status, cleanup and real-source absence |
| commitOwner(phase) | Local only |
| crossBatchIsolation | thirteen parked paths byte-identical |
| nextMoveSurfaces | Local review, then principal-separated operator execution checkpoint |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT T3B tooling worker after operator forwards this packet

laneOwnedPaths: exact five paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return, empty staging, exact delta and parked reconciliation

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| actor | one shared-workspace `INTERNAL_AGENT` worker |
| role set | PowerShell tooling, Python checker/test and evidence author; not reviewer/closer |
| delegation depth | zero |
| evidence basis | governed T2F/T3B sources only; never provider memory or credentials |
| gate sequence | pre-implementation, focused tests, worker-return fast, Local review |
| self-review boundary | worker cannot accept, stage or commit output |
| role separation ledger | worker returns pending; Local evaluates and commits |
| escalation condition | credentials, alternate-user/real-source execution, sixth output, parked drift or authority contradiction |

## Worker Output Checker Read-Ahead Mandate

Before writing each output, read checker source for that file's path family and
content class. The worker return must use real headings and exact trace/delta
labels; a checklist is not a substitute.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-20.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

evidenceReadinessContract: REQUIRED_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required real sections: Purpose; Scope / Methodology; Target / Source;
Findings / Position; Risk / Corrective Action; Decision / Disposition; Claim
Boundary; Changed Files; Command Evidence; No-Commit Statement; Checker Source
Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary
Control Block; Machine Closure Package; Public Export Disposition; git status
--short. Include executionBaseHead and use `N/A with reason` for every
non-applicable conditional section, including External Knowledge Intake
Routing, Rescan Intelligence Hardening, Corpus Completeness And Report
Integrity, Finding-To-Governance Learning Disposition and Epistemic Process
Block.

## Execution Plan

1. Freeze HEAD/status/staging, parked hashes and real-source absence; run pre-implementation gate.
2. Implement the Party A writer and approver event writer with parameterized disposable roots and strict real-mode identity checks.
3. Implement the independent Python verifier and focused tests for schemas, exact bytes, dual hashes, event chain, state machine, unique-active invariant, identity and negative cases.
4. Run hermetic end-to-end v1 author -> approve -> activate proof and adversarial mutation tests; remove fixtures.
5. Create the evidence return, run worker-return fast, reconcile exact outputs and leave staging empty.

## Evidence Requirements

Return T3B-01 through T3B-10 evidence: default non-mutation; exact decoded
bytes; base64url round trip; direct content and record hashes; separate
APPROVED/ACTIVATED events; chain recomputation; state/unique-active negatives;
wrong principal/elevation/path/collision negatives; DACL/ownership fixture
checks; cleanup, real-source absence, empty staging and parked reconciliation.
Never include passwords, private key material or credential-derived content.

## Acceptance Criteria

- Exactly five worker outputs and no other path change.
- Both PowerShell tools default to non-mutating behavior and refuse real mode
  under the worker's principal.
- Independent Python tests cover every T3B-01 through T3B-10 row and pass.
- Positive fixture produces exact policy bytes, two distinct spec hashes, two
  separate valid decision events and exactly one active version.
- Malformed base64, policy drift, wrong hash, wrong link, duplicate event ID,
  invalid transition, self-approval, two active versions, wrong owner/DACL,
  unsafe path and collision fail closed with stable reason codes.
- Both real Group 2 source paths remain absent.

## Review Gate

Local consumes valid returned evidence, inspects identity checks, hash
preimages, append atomicity/DACL behavior and runs bounded independent
checker/mutation probes. Local will not use credentials or perform real
principal-separated source writes during worker review.

## Closure Checklist

- [ ] T3B-01 through T3B-10 reviewed.
- [ ] Exact five paths and all parked hashes reconcile.
- [ ] Worker-return fast and reviewer preflight pass.
- [ ] Both real Group 2 paths remain absent.
- [ ] No credential, alternate-user or real-source action occurred.
- [ ] Material and continuity commits remain separate.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` only for a credential need, alternate-user or
real-source execution, sixth output, parked drift, source contradiction or
irreparable mandatory gate failure. Otherwise return
`COMPLETE_PENDING_REVIEW`, never source/admission readiness.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
pwsh -NoProfile -File scripts/acel_g1_party_a_group2_spec_writer.ps1
pwsh -NoProfile -File scripts/acel_g1_approver_group2_decision_writer.ps1
python governance/compat/test_check_acel_g1_verification_authority_spec.py
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
```

All tests must use disposable paths. No provider/live release-gate call applies
because this tranche makes no AI-governance or production-readiness claim.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_COMPLETION_2026-09-20.md` (optional; prefer bounded evidence repair in the worker return) |
| reviewerOwnedClosurePaths | exact five worker outputs plus necessary bounded evidence repair |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/dispatcher |
| Provider or surface | private CVF workspace and read-only Windows identity checks |
| Session or invocation | T3B tooling dispatch, 2026-09-20 |
| Working directory | repository root |
| Command or tool surface | governed reads, scaffold, account/ACL probes, apply_patch and governance gates |
| Target paths | paired T3B baseline and this work order |
| Allowed scope source | operator approvals plus verified approver posture and active next move |
| Before status evidence | HEAD `a4c77bd0f`; tracked worktree clean; staging empty; thirteen pre-existing parked paths isolated; five outputs and two real sources absent |
| After status evidence | exact paired dispatch paths pending before commit; parked paths unchanged |
| Diff evidence | paired packet staged alone before dispatch commit |
| Approval boundary | tooling and hermetic tests only |
| Claim boundary | no credential, alternate-principal execution, real source, activation, admission, live/runtime/public effect |
| Agent type | Local dispatcher and later reviewer/closer |
| Invocation ID | `acel-g1-t3b-group2-source-tooling-dispatch-20260920` |
| Expected manifest | paired T3B baseline and work order |
| Actual changed set | reconciled before dispatch commit |
| Manifest delta | pending exact staging reconciliation |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | source-creation tooling and hermetic validation only |
| claimDisposition | CLAIM_REJECTED for real source creation, activation validity, runtime enforcement, admission or consumer wiring |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker return does not yet exist |
| actionEvidence | ACTION_EVIDENCE_PRESENT: paired dispatch only |
| invocationBoundary | no Party A, approver or real-mode invocation by worker |
| interceptionBoundary | no runtime wrapper/proxy or agent-control claim |
| claimLanguage | tooling implemented/tested; Group 2 source remains not created |
| forbiddenExpansion | credentials, alternate users, actual sources, T3E, live/public/deployment |

## Legacy Absorption Coverage Index Disposition

`NOT_APPLICABLE_WITH_REASON`

Reason: bounded first-party Windows/local-source tooling; no legacy or external
corpus is ingested, mapped or absorbed.

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` |
| Chain map route | N/A with reason: direct internal contract -> operator decision -> INTERNAL_AGENT tooling |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T2F Group 2 contract and this dispatch |
| Disposition | local first-party implementation only |
| Claim boundary | no external source authority, corpus, remote implementation or provider claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private principal-bound source tooling and not-yet-created private
source; no public-sync authority exists.

## Claim Boundary

This order authorizes exactly five tooling/evidence outputs and disposable
tests. It does not authorize the worker to use credentials, run as Party A or
the approver, write the real source, approve/activate policy, stage, commit,
promote a key, wire T3E, admit a candidate, run live AI proof, public-sync,
deploy or claim production readiness.

## Operator Checkpoint

After Local accepts the tooling, the operator first launches Party A to create
`SPEC_v1.json`, then separately launches the approver to append `APPROVED` and
`ACTIVATED` events. Local independently verifies after each principal phase.
No password is committed or pasted into chat.
