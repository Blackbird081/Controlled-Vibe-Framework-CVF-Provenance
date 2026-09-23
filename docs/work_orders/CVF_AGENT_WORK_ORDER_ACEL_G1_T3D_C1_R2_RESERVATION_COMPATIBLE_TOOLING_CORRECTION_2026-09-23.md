# CVF Agent Work Order - ACEL G1 T3D-C1-R2 Reservation-Compatible Tooling Correction

Memory class: governed-work-order

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-23

Batch ID: ACEL-G1-T3D-C1-R2-RESERVATION-COMPATIBLE-TOOLING-CORRECTION

dispatchBaseHead: `c8b9a7bb459738ca7c7614dc3ba60093c42749f3`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_MUST_CAPTURE_AT_CLOSURE`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local orchestrator/reviewer

## Dispatch Prompt Envelope

Role: distinct shared-workspace `INTERNAL_AGENT` worker. A separate Local
reviewer is independent probe executor and commit owner. The operator selected
this distinct actor pair on 2026-09-23. No CLI/MCP invocation or subagent is
authorized by this role assignment.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_CORRECTION_2026-09-23.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Current-time notes: C0-R1 is contract-only accepted; T3D-C1 tooling is
accepted only for its earlier target-absent/hermetic scope. The four source
gaps are recorded at `e79910b5c`.

Do-not-misread notes: this packet authorizes only bounded worker
implementation after the dispatch gate passes. It does not authorize Party
B/C execution, real Group 4 source creation or actual-token proof.

Required first actions: read startup, baseline, source owners,
guard orientation, checker sources; capture execution HEAD/status and confirm
real Group 4 paths are untouched; run pre-implementation gate before edits.

Return contract: exact owned manifest, focused tests, gate
results and worker return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`; leave all worker changes uncommitted and independent
probe `PENDING_REVIEWER_EXECUTION`.

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

High-Risk Local Transaction Proof Applicability: REQUIRED

## Purpose

Correct the accepted T3D-C1 Party C and Party B writer transactions for the
C0-R1 pre-reserved shared-parent model. Build only hermetic/disposable
capability and evidence; later real-principal execution remains a separate
operator-checkpointed order.

## Authority Chain And Intake Role Routing Decision

| Field | Decision |
|---|---|
| source gap | `docs/audits/CVF_ACEL_G1_T3D_GROUP4_ACTUAL_TOKEN_PROOF_TOOLING_GAP_AUDIT_2026-09-23.md` |
| controlling contract | `docs/audits/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md` under T2F owner |
| bounded static proof packet | `docs/audits/CVF_ACEL_G1_T3D_GROUP4_DISPOSABLE_ROOT_PROOF_PACKET_2026-09-23.md` |
| paired GC-018 | `docs/baselines/CVF_GC018_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_CORRECTION_2026-09-23.md` |
| task class | high-risk local tooling correction, no external provider effect |
| role / phase / decision owner | Local dispatch author/reviewer/closer; distinct internal implementation worker |
| worker route | `MULTI_AGENT_MULTI_ROLE`; operator-selected distinct worker and Local reviewer; no subagent assignment |
| external route | `EXTERNAL_AGENT_CLI_MCP` forbidden; internal shared-workspace role only |
| stop condition | any need for real token, credential, source mutation, path widening, or contract change |

Intake summary: bounded internal correction of two Group 4 writers to the
accepted pre-reserved target contract; no external repository, provider or
real-principal source intake is requested.

Selected role route: `MULTI_AGENT_MULTI_ROLE`, operator-selected distinct
shared-workspace worker and Local reviewer. The Local actor retains all
source decisions, independent probe, closure and commits.

Scope classification: high-risk local security and durable transaction
tooling, with disposable-root proof only.

Risk sensitivity: a writer may mutate the wrong reservation, erase unknown
residue or relax the parent/target DACL without immediate test detection.

Escalation condition: any real-token need, path split or scope widening,
contract contradiction, unrepresentable security descriptor, forbidden
source mutation, or unknown transaction residue.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T3D-C1-R2-RESERVATION-COMPATIBLE-TOOLING-CORRECTION","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/baselines/","docs/work_orders/","docs/reviews/","docs/audits/","docs/reference/","scripts/","governance/compat/","CVF_SESSION/","CVF_SESSION_MEMORY.md","AGENT_HANDOFF_V63_2026-09-18.md"],"claims":["reservation-compatible Group 4 tooling correction only; no actual-token or real-source proof"],"requiredProof":["exact own-target reservation claim","exact parent and target security read-back","durable transaction ledger and recovery separation","unknown residue preservation","real peer exclusion in disposable root","independent Local probe"],"operatorCheckpoints":["Party C real registry creation","Party B actual-token observation","Group 4 establishment","T3E wiring","candidate admission"],"forbiddenEffects":["credential access","Party B or Party C execution","real Group 4 source read/write","worker commit","provider/live/public/deployment","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/audits/CVF_ACEL_G1_T3D_GROUP4_ACTUAL_TOKEN_PROOF_TOOLING_GAP_AUDIT_2026-09-23.md","completenessClaimChanged":false}}
```

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` inspected during release read-ahead; no generated artifact was used |
| generatedProfile | protected-governance-path requirements, manually applied to the existing HOLD packet |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | existing held packet was manually promoted only after actor selection; required ready-dispatch fields were added and machine-checked |
| checkerReadAheadConfirmation | routing, scaffold, gate-to-role, dispatch-quality, lifecycle, handoff and worker-return checkers reviewed before release |
| docOnlyNewFields | none |
| claimBoundary | this is dispatch metadata, not implementation, actual-token proof or source creation |

## Agent Roles

The operator owns later actual-token and real-source checkpoints. Local is
dispatch author, reviewer, independent probe executor and committer. After
release, the operator-selected distinct worker is the internal same-workspace implementation actor.
Same-thread role switching cannot supply the required independent actor
identity. The operator selected distinct worker / Local reviewer actors explicitly.

## Required First Reads

Read the active bootstrap/front door/handoff, paired GC-018, the C0-R1
amendment and completion, the four-finding source gap audit, both current
writer scripts, guard orientation, literal gotchas, and applicable checker
sources before the first implementation edit.

## Pre-Flight Checks

Capture exact HEAD, status, staged set and hashes of the two writer scripts;
verify all listed existing paths and confirm the two planned script paths
are absent. Inspect the real Group 4 source path read-only and record whether
it is absent; any surprising source state blocks implementation. Run the
pre-implementation autorun gate on the current execution base.

## Allowed Scope After Explicit Release

Correct only the existing Party C registry writer and Party B response writer;
new scripts may be introduced only for disposable fixture setup/probe and
separately owned ledger-bound Administrator recovery. Preserve the accepted
canonical registry/response schemas and all Group 1-3 sources. No change to
live source paths, checker semantics, session/handoff or public surfaces is
worker-owned. The worker may test in a verified disposable root under its own
token, not as Party B/C, and must not claim actual-token proof.

Expected implementation family:

| Path | Status / purpose |
|---|---|
| `scripts/acel_g1_party_c_group4_registry_writer.ps1` | existing; reservation-compatible own-target transaction |
| `scripts/acel_g1_party_b_group4_lookup_response_writer.ps1` | existing; zero-byte reservation claim and later append boundary |
| `scripts/acel_g1_group4_disposable_acl_probe.ps1` | NEW; source-contained fixture/probe only |
| `scripts/acel_g1_group4_admin_recovery.ps1` | NEW; exact ledger-bound recovery only, never ordinary writer cleanup |
| `docs/reviews/CVF_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_WORKER_RETURN_2026-09-23.md` | NEW pending worker evidence |

Foreseeable maintainability extraction within `scripts/acel_g1_group4_*.ps1`
requires Local amendment to the manifest before creation; this table does
not grant a broad scripts-directory mutation right.

## Work-Order Fulfillment Manifest

| Obligation | Owned output | Required proof | Completion owner |
|---|---|---|---|
| own-target reservation claim | two existing writers | absent/mismatched/linked/nonzero reservation rejects; correct zero-byte target is claimed without cross-target mutation | worker, then Local reviewer |
| protected security state | two writers and disposable probe | exact parent/target owner, protection and complete ACE read-back; extra/inherited/deny/reordered state rejects | worker, then Local reviewer |
| durable transaction and recovery | writers and named recovery script | pre-mutation ledger, exact residue binding, separate administrative recovery path, unknown residue preservation | worker, then Local reviewer |
| peer exclusion and rollback | named disposable probe | deterministic second-process barrier and injected failure poststate; no real-principal claim | worker, then Local reviewer |
| evidence reconciliation | named worker return | exact five-path manifest, gate commands/results, empty staging, no real-source effect and pending independent probe | worker |

Forbidden paths are all live Group 4 sources, Party B/C credential and profile
locations, checker semantics, session/handoff, public files and any unnamed
script. Required proof is disposable only; actual-token proof is deferred.

## Write Ownership

Only the two existing writer scripts, two named NEW scripts if needed, and
the named worker return belong to the worker. Local alone may revise the
baseline/order, review, commit, handoff or session state. Any additional
path or split needs a Local manifest amendment before the worker edits it.

## Forbidden Scope And Stop Conditions

- Do not access passwords, create accounts, call `runas`, elevate, or invoke
  Party B/C; no real Group 4 directory/file mutation or issuer observation.
- Do not call provider APIs. The offered Alibaba key is irrelevant to NTFS
  effective-rights and transaction proof; do not consume it in this tranche.
- Do not sweep unknown temps, normalize drift, change DACL/owner on another
  principal's target, widen ACEs, or follow reparse/hardlink paths.
- Do not reuse the archived rejected T2/T2A/T2B implementation as authority.
- If exact owner/security tuple or file identity cannot be captured, return
  `BLOCKED_WITH_REASON`; do not substitute a success-shaped placeholder.

## Implementation Contract And Acceptance Matrix

| ID | Positive required behavior | Negative / postcondition oracle |
|---|---|---|
| R2-01 | Party C claims only exact pre-owned zero-byte registry and atomically replaces with validated fresh bytes | absent/nonzero/replaced/linked/wrong-DACL target blocks before mutation |
| R2-02 | Party B claims only exact pre-owned zero-byte response through target-preserving atomic replacement | absent/nonzero/replaced/linked/wrong-DACL target blocks before mutation |
| R2-03 | both writers verify parent, both reserved names, own target and non-target before/after guard | Party C cannot mutate response; Party B cannot mutate registry; parent cannot gain child-delete authority |
| R2-04 | each transaction creates, hardens, flushes and removes only its own temp | stale/unknown sibling or temp blocks and remains untouched |
| R2-05 | durable out-of-parent recovery ledger binds ID, token, target identity, temp, prestate and phase before temp creation | no ledger, mismatch or unproven termination forbids cleanup |
| R2-06 | Administrator recovery is a distinct scoped operation under the same guard | only exact bound residue may be removed; non-target state is invariant |
| R2-07 | second real OS process invokes guarded writer mutation with explicit barrier ordering | ENTERED before PARENT_RELEASE fails; timeout alone proves nothing |
| R2-08 | hermetic peer/crash fixtures exercise positive, negative, rollback and drift cases | no real source path or non-disposable mutation is reachable |
| R2-09 | final return is immutable across final required gate, independent Local probe pending | no worker self-certification of Windows Party B/C proof |

## Execution Plan

After explicit release, implement the reservation-claim core first, then
remove ordinary orphan sweeping, then add the separate ledger/recovery
surface, then verify the disposable positive/negative matrix. Keep the real
source route unreachable from hermetic tests. Capture postconditions for
every expected denial and stop on ambiguous cleanup or security state.

## High-Risk Local Transaction Proof Contract

```json
{
  "transactionTarget": "Group 4 pre-reserved registry and response own-target replacement, full security readback, durable recovery binding and exact rollback",
  "productionPathPeer": {
    "kind": "REAL_SECOND_PROCESS",
    "invocationPath": "scripts/acel_g1_party_c_group4_registry_writer.ps1",
    "mutationPath": "Publish-RegistryTransaction reservation-compatible guarded mutation"
  },
  "deterministicBarrierProtocol": {
    "events": ["READY", "START_ATTEMPT", "ATTEMPTING", "PARENT_RELEASE", "ENTERED", "COMPLETE"],
    "timeoutRole": "DEADLOCK_SAFETY_ONLY"
  },
  "enteredBeforeReleaseOracle": "REJECT_ENTRY_BEFORE_PARENT_RELEASE",
  "postAcquireFailureInjection": {
    "point": "AFTER_ACQUIRE_BEFORE_MUTATION",
    "cleanupProof": "SUBSEQUENT_PEER_ACQUIRES"
  },
  "semanticSecurityTuple": {
    "fields": ["ownerSid", "protectionState", "inheritanceState", "aces"],
    "aceFields": ["sid", "rights", "accessType", "isInherited", "inheritanceFlags", "propagationFlags"],
    "normalization": "SORT_COMPLETE_ACE_TUPLES"
  },
  "rollbackExactness": {
    "comparison": "SEMANTIC_PRESTATE_EQUALS_POST_ROLLBACK",
    "adversaries": ["EXTRA_ALLOW", "DENY", "INHERITED", "WRONG_OWNER"]
  },
  "finalEvidenceHashBinding": {
    "algorithm": "SHA256",
    "scope": "EXACT_RETURN_BYTES",
    "capture": "BEFORE_AND_AFTER_FINAL_REQUIRED_GATE",
    "equality": "REQUIRED",
    "postGateMutation": "FORBIDDEN"
  },
  "independentProbeRequired": {
    "required": true,
    "owner": "LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER",
    "workerReturnDisposition": "PENDING_REVIEWER_EXECUTION"
  }
}
```

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Party C absent-target guard | source fact | `scripts/acel_g1_party_c_group4_registry_writer.ps1` | `Assert-ExactExecutionBoundary` and `Publish-RegistryTransaction` | `REGISTRY_ALREADY_EXISTS` | Party C writer | ACCEPT |
| Party B absent-target guard | source fact | `scripts/acel_g1_party_b_group4_lookup_response_writer.ps1` | `InitializeResponseLog` final branch | `RequireAbsent` | Party B writer | ACCEPT |
| old-temp sweep | source fact | `scripts/acel_g1_party_c_group4_registry_writer.ps1` | `Remove-OrphanTemps` | `.cvf-g4-registry-*.tmp` | Party C writer | ACCEPT |
| old-temp sweep | source fact | `scripts/acel_g1_party_b_group4_lookup_response_writer.ps1` | `Remove-OrphanTemps` | `.cvf-g4-response-*.tmp` | Party B writer | ACCEPT |
| reservation and recovery | owner contract | `docs/audits/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md` | Protected Parent Directory And Administrative Reservation; Hard-termination recovery; Required Actual-Token Proof Matrix | `REGISTRY.json`, `LOOKUP_RESPONSES.jsonl` | T2F subordinate | ACCEPT |
| four blocking joins | Local source audit | `docs/audits/CVF_ACEL_G1_T3D_GROUP4_ACTUAL_TOKEN_PROOF_TOOLING_GAP_AUDIT_2026-09-23.md` | Findings / Position | `G4-PROOF-01` through `G4-PROOF-04` | Local reviewer | ACCEPT |

## Negative Search And Collision Discipline

Both paired packet paths were absent at dispatch-base HEAD. `rg -n
"C1-R2|reservation-compatible tooling correction" docs/baselines
docs/work_orders docs/audits` found historical C1-R2 mentions but no
existing reservation-compatible owner packet. New script names above are
planned, not claimed to exist. No alternate source authority is inferred.

## Current Runtime Freshness Verification

At dispatch-base HEAD, `rg -n
"REGISTRY_ALREADY_EXISTS|RequireAbsent|Remove-OrphanTemps|Assert-ExactExecutionBoundary|Assert-PrincipalAndPaths|PeerMode|CrashMode"
scripts/acel_g1_party_c_group4_registry_writer.ps1
scripts/acel_g1_party_b_group4_lookup_response_writer.ps1` returned the
current Party C target-absent checks at lines 144/314, Party B
`RequireAbsent` initializer at line 135, and both pattern-based orphan
cleanup functions. The real modes also bind exact principal plus canonical
Git-root source paths; their disposable peer/crash modes use test policy.
The C0-R1 amendment at its reservation and recovery sections instead
requires pre-owned zero-byte targets and ledger-bound prior cleanup. This
comparison applies to the two named writer files only; no repository-wide
absence claim is made. Before release, refresh these source-region facts
against the then-current HEAD and amend this HOLD packet if they changed.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G1-T3D-C1-R2-RESERVATION-COMPATIBLE-TOOLING-CORRECTION
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
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: REQUIRED_TRIGGERED
preExecutionReviewTrigger: OPERATOR_EXPLICIT_REQUEST
nextRoutineReviewBoundary: PRE_EXECUTION_REVIEW

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3d-c1-r2-reservation-tooling","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["RESERVATION_COMPATIBLE_TOOLING_PENDING","ACTUAL_TOKEN_PROOF_PENDING","GROUP4_SOURCE_NOT_CREATED","T3E_NOT_OPEN"],"reopened":[],"current":["RESERVATION_COMPATIBLE_TOOLING_PENDING","ACTUAL_TOKEN_PROOF_PENDING","GROUP4_SOURCE_NOT_CREATED","T3E_NOT_OPEN"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T3D-C1-R2-HOLD-PACKET","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_CORRECTION_2026-09-23.md"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class CODE_CHANGE --role dispatcher --lifecycle-phase dispatch --json`

Returned defects: NONE_RETURNED; `totalCandidates: 0`; `truncated: false` at authoring.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| literalTokensReviewed | high-risk nine-field JSON; one SCEC block; `HOLD_PENDING_PACKET_REVIEW`; source table headings |
| gateRunPurpose | confirmation/evidence for pre-read packet requirements, not first discovery or Windows proof |
| claimBoundary | static check cannot prove token rights or implementation |

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON: no external CLI/MCP dispatch; Local owns technical decision.

## Worker Autonomy / No-Question Rule

After release, the worker may repair in-scope implementation and test defects
without seeking operator approval for each local edit. Any request to widen
paths, run Party B/C, use credentials, change source or reduce proof is outside
scope and must return `BLOCKED_WITH_REASON`.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline and work order | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | dispatch packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact five worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact five worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact five worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| independent_local_probe | PRE_MATERIAL_COMMIT | reviewer | REVIEW | disposable fixture only; optional completion review | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | exact worker range and optional completion review | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | independent_local_probe |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local completion disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; active handoff is `AGENT_HANDOFF_V63_2026-09-18.md`.

| Field | Decision |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Local dispatcher/reviewer/closer and a distinct shared-workspace internal implementation worker after release; no subagent assigned now |
| phase | DISPATCH_AUTHORING_TO_CLOSURE |
| baseHeadFor(phase) | dispatchBaseHead=`c8b9a7bb459738ca7c7614dc3ba60093c42749f3`; executionBaseHead=worker capture after release; closureBaseHead=reviewer capture before closure |
| changedSetScope(phase) | exact worker script/return manifest; later continuity in separate commit |
| traceScope(phase, actor) | Local records each role transition, paths, commands and outcome |
| commitOwner(phase) | worker role must not commit; Local closer owns material and continuity commits |
| crossBatchIsolation | clean worktree at release; no concurrent writer to same paths |
| nextMoveSurfaces | active handoff, front door, source state and generated state after acceptance |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: distinct internal worker role after explicit HOLD release

laneOwnedPaths: exact five paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: terminal worker return, exact manifest and empty staged set

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_WORKER_RETURN_2026-09-23.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

evidenceReadinessContract: NOT_APPLICABLE_WITH_REASON: this bounded local tooling correction has no new discovery audit or corpus manifest artifact

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_CORRECTION_2026-09-23.md`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Decision / Disposition; Claim Boundary;
Changed Files; Command Evidence; No-Commit Statement; Checker Source
Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary
Control Block; Machine Closure Package; External Knowledge Intake Routing;
Epistemic Process Block; Public Export Disposition; exact executionBaseHead and
full `git status --short --untracked-files=all`.

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_COMPLETION_2026-09-23.md` if a distinct review artifact is needed

reviewerOwnedClosurePaths: accepted worker manifest plus optional completion review; continuity separately owned

Local reviewer consumes valid return evidence, runs reviewer-fast and an
independent adversarial probe, repairs only bounded findings, commits material
paths, then syncs active handoff/state separately. No worker self-closure.

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: HIGH

independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: REQUIRED_DIFFERENT_EXECUTION_AND_ASSERTION_PATH

positiveControl: reviewer independently exercises reserved-target mutation
in a disposable fixture and verifies exact bytes, identity and semantic
security state with a separate assertion method.

negativeMutationClasses: stale temp, missing/mismatched ledger, wrong owner,
inherited/deny/extra ACE, cross-target mutation, early peer entry and
unexpected non-target/parent poststate.

expectedInformationGain: detect false hermetic PASS or unauthorized cleanup
that worker-owned tests might miss.

rerunCostReason: one bounded disposable fixture is proportionate to the
high-risk cross-principal mutation boundary; no broad duplicate review.

reviewerDecisionOwner: LOCAL

## Required Artifact Manifest

The expected worker change set is the two existing writer scripts, any
predeclared NEW disposable/recovery scripts actually necessary, and the named
worker return. No other script or governance path is implicitly allowed.
Each omitted planned new script must be justified; each added path requires
Local manifest amendment before mutation. No source file or public path is
an artifact of this tranche.

## Evidence Requirements

The worker return must carry execution base/status, exact changed-path
manifest, source-region diff, positive and negative fixture result counts,
deterministic peer event trace, failure-injection/rollback evidence,
pre/post security tuples, residue inventory, focused and full gate commands
with exit codes, detached exact-return SHA-256 receipt, and explicit
`PENDING_REVIEWER_EXECUTION`. No password, key or signed header is included.

## Acceptance Criteria

All R2-01 through R2-09 rows must be demonstrated on the returned exact
manifest, not inferred from a single PASS string. Both writer self-tests and
the disposable matrix must pass; every forbidden operation must preserve
the captured non-target/parent state. Any changed canonical source schema,
real-principal action or missing required negative case is a rejection.

## Verification Commands

Before release: `python governance/compat/run_agent_autorun_workflow_gate.py
--phase pre-dispatch --base <dispatchBaseHead> --head HEAD`.
After implementation: both writer `-SelfTest` modes, focused disposable-root
positive/negative tests, `python governance/compat/run_worker_return_fast_gate.py
--active-work-order <this-work-order>`, and reviewer-fast on the exact worker
range. The worker must report exact commands, exit codes, counts and SHA-256
evidence. Neither self-test nor static gate may be called actual-token proof.

## Review Gate

Local runs reviewer-fast against `executionBaseHead`, checks the full
contract/schema/path/authority/test range once, then performs a separately
executed adversarial disposable probe. Repair is bounded to the declared
manifest. Pre-commit and committed-range closure follow the material commit
and separate GC-020 continuity commit, not the worker's pending return.

## Closure Checklist

- [x] HOLD status released for the selected worker after pre-dispatch compliance (83/83); the
  Local author recorded the actor assignment before worker implementation.
- [ ] Worker return gives exact manifest, tests, gate outputs and final hash.
- [ ] Local independent probe accepts all nine criteria.
- [ ] No Party B/C execution, real Group 4 source or T3E effect occurred.
- [ ] Material commit and separate continuity sync pass their exact gates.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only if every required hermetic proof and
gate passes without scope drift. Return `BLOCKED_WITH_REASON` for an
unrepresentable security tuple, unsupported own-target replacement,
unknown residue, missing principal-independent oracle, extra path or need
for a contract change. Do not silently choose split paths or mediator.

## Operator Checkpoint And Claim Boundary

The operator's Alibaba free key is available only if a later provider-governance
test actually requires a real provider call. This NTFS tranche does not. No
key is read or used. No account switching, Party B/C run, Group 4 source,
issuer observation, lookup response, T3E, public-sync or deployment is
authorized. The packet is released only for the bounded internal worker scope
after Local pre-dispatch verification; it is not a source-execution release.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | five-path hermetic reservation-compatible tooling correction |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: dispatch and disposable tests create no production receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: exact worker return and later independent reviewer probe required |
| invocationBoundary | internal workspace edits and verified disposable fixtures only |
| interceptionBoundary | no IDE, shell, Git, filesystem or provider interception claim |
| claimLanguage | corrected tooling pending Local acceptance; no actual-token proof |
| forbiddenExpansion | credentials, alternate principal, real source, Group 4 establishment, T3E, admission, provider/live/public/deploy |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/audits/CVF_ACEL_G1_T3D_GROUP4_ACTUAL_TOKEN_PROOF_TOOLING_GAP_AUDIT_2026-09-23.md` |
| Chain map route | N/A with reason: direct internal tooling correction |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T2F Group 4 contract and this bounded order |
| Disposition | local first-party correction only |
| Claim boundary | no external source authority, corpus, remote implementation or provider claim |

## External/Local Coordination Binding

Role: `INTERNAL_AGENT`; phase: bounded local implementation; decision owner:
Local reviewer. External research is outside this work order and conveys no
private-CVF verification authority.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF workspace |
| Session or invocation | G1 T3D-C1-R2 HOLD packet, 2026-09-23 |
| Working directory | repository root |
| Command or tool surface | governed source reads, apply_patch, gates, Git |
| Target paths | paired baseline and work order |
| Allowed scope source | operator continuation; committed four-finding gap audit |
| Before status evidence | HEAD `c8b9a7bb4`; exact packet paths absent; clean worktree before release edit at HEAD `d3a440aa3` |
| After status evidence | HOLD packet only; no implementation |
| Diff evidence | exact two-file packet delta before commit |
| Approval boundary | packet authoring, not worker invocation |
| Claim boundary | no Windows actual-token or source proof |
| Agent type | Local dispatch author |
| Invocation ID | acel-g1-t3d-c1-r2-hold-packet-20260923 |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order pending commit |
| Manifest delta | MATCH pending commit |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private local Windows tooling correction.

## Claim Boundary

This order is not dispatch-ready and supplies no runtime proof. C0-R1
contract acceptance is preserved; Group 4 remains
`TOOLING_ACCEPTED_SOURCE_NOT_CREATED` until later independently reviewed
tooling and real-principal source checkpoints.
