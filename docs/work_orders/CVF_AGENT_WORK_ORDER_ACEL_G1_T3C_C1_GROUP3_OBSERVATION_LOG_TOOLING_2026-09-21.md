# CVF Agent Work Order - ACEL G1 T3C-C1 Group 3 Observation Log Tooling

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Batch ID: ACEL-G1-T3C-C1-GROUP3-OBSERVATION-LOG-TOOLING

Dispatch base head: `cf7872810`

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

Worker: shared-workspace `INTERNAL_AGENT`

Reviewer/closer: Local orchestrator/reviewer

Worker return path: `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md`

independentProbeRequired: YES

## Dispatch Prompt Envelope

Role: bounded shared-workspace `INTERNAL_AGENT` tooling worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_2026-09-21.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture committed HEAD at worker start and record it in the return.

Current-time notes: Groups 1 and 2 are Local-verified; Party B exists as exact
SID `S-1-5-21-1644666849-912006174-747199667-1009`; Group 3 remains
`SOURCE_NOT_CREATED`; Party C and Group 4 remain pending T3D.

Do-not-misread notes: build hermetic tooling only. Do not use credentials or
`runas`, execute as Party B, read the real registry as a worker test, create or
append the real log, provision Party C, wire T3E, stage or commit.

Required first actions: read the startup front door/bootstrap/active handoff,
guard orientation, literal gotchas, this packet, its paired baseline, all
Source Verification owners and checker sources named below. Capture HEAD,
status, staging and the thirteen parked-path hashes before editing.

Return contract: implement exactly the four-path manifest, run all required
gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Implement a Party B-bound PowerShell writer and independent Python verifier
for the immutable Group 3 observation log, using disposable fixtures only.

## Authority Chain

| Authority step | Evidence | Worker consequence |
|---|---|---|
| T2F Group 3 contract | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | implement exact encoding, closed preimage, chain and immutable-ID rules |
| Local T3C route | `docs/audits/CVF_ACEL_G1_T3C_GROUP3_SOURCE_READINESS_ROUTE_2026-09-21.md` | tooling precedes real Party B execution |
| Party B appointment | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_B_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | bind observer role to both registries without registry mutation rights |
| concrete principal evidence | paired GC-018 baseline | real mode binds exact name/SID and fails closed otherwise |
| this dispatch pair | paired baseline and work order | exact four outputs, fixtures only, no commit |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake summary | internal first-party Group 3 observation-log tooling |
| scope classification | bounded code/evidence change with cryptographic and principal-bound sensitivity |
| risk sensitivity | append-only durable source and exact-byte snapshot commitment |
| selected route mode | `SINGLE_AGENT_MULTI_ROLE`: worker implements; separate Local reviewer probes and closes |
| role separation basis | worker cannot use credentials, execute real mode, accept return, stage or commit |
| escalation condition | authority contradiction, fifth path, parked drift, credentials, real-source need or Party C scope |

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T3C-C1-GROUP3-OBSERVATION-LOG-TOOLING","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/baselines/","docs/work_orders/","docs/audits/","docs/reviews/","docs/reference/","scripts/","governance/compat/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/"],"claims":["Party B-bound observation-log tooling and hermetic validation only; no real observation source"],"requiredProof":["exact-byte snapshot hash","base64url rejection","closed JCS preimage","append-only chain","duplicate snapshot rejection","observer separation","independent Local probe","worker-return fast gate"],"operatorCheckpoints":["Party B Group 1 observation","Local source verification","Party C provisioning","Group 4 establishment","issuer observation","T3E consumer wiring","candidate admission"],"forbiddenEffects":["credential access","alternate-user execution","real source creation","real registry read during worker testing","parked-path mutation","worker commit","provider/live/public/deployment","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/audits/CVF_ACEL_G1_T3C_GROUP3_SOURCE_READINESS_ROUTE_2026-09-21.md","completenessClaimChanged":false}}
```

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3C-C1-GROUP3-OBSERVATION-LOG-TOOLING --title "ACEL G1 T3C-C1 Group 3 Observation Log Tooling" --date 2026-09-21 --base cf7872810 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact Group 3 fields, Party B identity, immutable-ID rules, four-path manifest, negative matrix and operator checkpoint |
| checkerReadAheadConfirmation | dispatch-quality, gate-to-role, worker-return, scaffold-provenance and operation-trace checker sources read before authoring |
| docOnlyNewFields | none |
| claimBoundary | dispatch provenance only; no source, observation, runtime, provider, public or deployment claim |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G1-T3C-C1-GROUP3-OBSERVATION-LOG-TOOLING
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3c-c1-group3-observation-log-tooling-problem","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["PARTY_C_AND_GROUP4_PENDING","REAL_OBSERVATION_PENDING","T3E_PENDING"],"reopened":[],"current":["PARTY_C_AND_GROUP4_PENDING","REAL_OBSERVATION_PENDING","T3E_PENDING"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T3C-C1-TOOLING-ONLY","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"governance/compat/test_check_acel_g1_registry_observation_log.py"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Dependency Release Evidence

| Dependency | Evidence | Release condition | Disposition |
|---|---|---|---|
| Group 3 outer contract | T2F Source Group 3 and immutable-identity sections | accepted contract unchanged | RELEASED |
| Party B role | T2E appointment | two-registry observer role remains current | RELEASED |
| Party B principal | Local OS verification | exact name/SID/posture and separation established | RELEASED |
| Group 1 input model | Local-verified `REGISTRY.json` envelope | worker uses equivalent fixture bytes only | RELEASED_FOR_HERMETIC_TOOLING |
| issuer input model | T2F defines it, but no Group 4 source or Party C exists | schema tests only; real mode locked | PARKED_T3D |
| real observation | Local acceptance and operator execution as Party B | separate later checkpoint | PARKED_OPERATOR_EXECUTION |

## Independent Review Probe Admission Contract

independentProbeRiskClass: HIGH

independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: REQUIRED_DIFFERENT_EXECUTION_AND_ASSERTION_PATH

positiveControl: Local independently rebuilds the JCS preimage, hashes exact decoded snapshot bytes and replays a multi-entry chain

negativeMutationClasses: padded or noncanonical base64url, invalid UTF-8/JSON, snapshot-hash drift, closed-preimage drift, broken prior hash, duplicate snapshot ID and observer/writer identity collision

expectedInformationGain: distinguish same-oracle worker tests from independent byte-binding and chain verification

rerunCostReason: focused temporary fixtures provide decision-changing evidence without duplicating the worker suite

reviewerDecisionOwner: LOCAL

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | four exact worker paths | implementation and disposable tests only; no credentials, real sources, staging or commit | this packet and baseline | PowerShell/Python local tooling | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no owner | no external ingress, authentication, mutation, receipt, runtime or public claim | no authority | fresh packet required | DEFERRED_WITH_REASON |

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `scripts/acel_g1_party_b_group3_observation_writer.ps1` | create Party B-bound writer with default non-mutating self-test and explicit real mode |
| `governance/compat/check_acel_g1_registry_observation_log.py` | create independent read-only schema/encoding/hash/chain/identity verifier |
| `governance/compat/test_check_acel_g1_registry_observation_log.py` | create focused disposable positive and negative tests |
| `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md` | create checker-safe evidence return |

## Work-Order Fulfillment Manifest

The table above is the complete worker output set. The worker must not create
or modify `governance/sources/registry_observation_log/LOG.jsonl`.

## Allowed Scope / Forbidden Scope

Allowed: create and test exactly four manifest paths using disposable temporary
directories; repair failures confined to those paths. Forbidden: credentials,
`runas`, Party B execution, real Group 1 reads during worker tests, real Group 3
path, Party C/Group 4 real mode, existing source mutation, thirteen parked
paths, staging, commit, T3E, admission, provider/live, public sync or deployment.

## Write Ownership

Worker owns uncommitted edits to the exact four paths. Local owns review,
independent probes, any launcher, real execution, source acceptance, staging,
commit and continuity. No concurrent dispatcher mutation while the lane is active.

## Agent Roles

| Role | Owner | Authority |
|---|---|---|
| dispatcher | Local orchestrator/reviewer | this packet and scope corrections |
| implementer | shared-workspace INTERNAL_AGENT | exact four paths, no commit |
| reviewer/probe executor | Local | inspect evidence, run independent probes, repair only small reviewer-owned defects |
| operator | human operator | passwords and any later Party B execution |

## Required First Reads

- `CVF_SESSION_MEMORY.md` and bootstrap-selected active handoff.
- `docs/reference/guard_orientation/README.md` and literal-format gotchas.
- This work order and paired GC-018 baseline.
- T2F operational source contract, T3C readiness route and T2E Party B appointment.
- All applicable checker sources named in the read-ahead block.

## Pre-Flight Checks

Capture `git rev-parse --short HEAD`, `git status --short`, `git diff --cached
--name-only`, exact-path absence, and SHA-256 hashes for all thirteen parked
paths. Run pre-implementation autorun from `executionBaseHead`. Stop on a
source contradiction, non-empty staging, changed parked hash or manifest collision.

## Implementation Contract

### Record and canonical preimage

Each JSONL record must contain exactly:
`snapshotId`, `registryName`, `registrySnapshotVersion`, `snapshot_content`,
`snapshotHashHex`, `observedAt`, `authority`, `observerIdentity`,
`priorEntryHashHex`, `entryHashHex`.

The `entryHashHex` preimage is RFC 8785 JCS UTF-8 without BOM over exactly:
`profile`=`cvf.source-record-canonicalization@1`,
`domain`=`cvf.observationLogEntry`, then `snapshotId`, `registryName`,
`registrySnapshotVersion`, `snapshotHashHex`, `observedAt`, `authority`,
`observerIdentity`, `priorEntryHashHex`. It excludes `snapshot_content` and
`entryHashHex`. Digest is lowercase SHA-256 hex. Genesis prior hash is JSON null.

### Snapshot bytes and identity

`snapshot_content` is unpadded canonical base64url of exact raw UTF-8 JSON file
bytes. Decode strictly: reject padding, whitespace, non-URL alphabet,
noncanonical re-encoding, BOM, invalid UTF-8 and invalid JSON. Hash the decoded
bytes without normalization. `registrySnapshotVersion` must equal the parsed
snapshot value and be a positive integer. `snapshotId` is a fresh UUID-derived
globally unique string, immutable and write-once. Any changed/error snapshot
uses a new ID; there is no correction, merge, alias or supersession field.

### Chain, authority and separation

Append only after validating the entire existing chain. Reject duplicate
`snapshotId` before append, chain discontinuity, extra/missing fields, invalid
timestamps, hash mismatch or a registry name outside
`verifier_key_registry|issuer_registry`. `observerIdentity` in real mode is
exact Party B SID `S-1-5-21-1644666849-912006174-747199667-1009`.
Reject Party A SID `...-1006`, approver SID `...-1008`, Local SID `...-1001`,
or any identity declared as the selected registry writer. `authority` is a
non-empty explicit value; the first real Group 1 observation later uses active
Group 2 `authorityId` `ACEL_G1_DECISION_OWNER`.

### Real-mode lock and filesystem boundary

Default invocation is non-mutating self-test. `-ExecuteWrite` requires exact
current account `LAM-RUBY\cvf-g1-party-b`, exact SID `...-1009`, an exact
confirmation phrase, canonical repository root, exact output path
`governance/sources/registry_observation_log/LOG.jsonl`, and exact input path
`governance/sources/verifier_key_registry/REGISTRY.json`. In this tranche real
mode rejects `issuer_registry` and every other input. It validates Group 1 with
the existing checker before reading exact bytes. It writes transactionally,
never truncates a non-empty log, and fails closed if ownership/DACL cannot
restrict operational mutation to Party B while retaining Windows SYSTEM and
Administrators recovery control. The worker must not execute real mode.

### Checker interface and tests

Checker accepts explicit log path plus optional expected observer/name,
registry-writer SID and current-time/freshness inputs. It emits deterministic
secret-safe JSON and nonzero exit on any violation. It exposes read-only
lookup/count semantics proving 0/1/>1 records for an ID. Tests use temporary
fixtures only and cover: genesis and two-entry positives; the published
29-byte vector; exact-byte whitespace drift; every strict-decoding failure;
wrong snapshot hash/version; extra/missing field; uppercase/malformed digest;
broken prior/entry hash; duplicate ID; reused ID with changed content; wrong
observer; observer/writer collision; forbidden registry name; real-mode
identity/path/confirmation failures; no mutation on every negative.

## Worker Autonomy / No-Question Rule

Repair allowed-scope implementation and gate failures directly. Return only
for a true authority contradiction, forbidden fifth path, credential/real-source
need, parked drift or claim-boundary expansion.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| canonicalPrivateWorkspace | current private provenance repository |
| workerMutationSurface | exact four-path manifest |
| disposableFixtureSurface | OS temporary directory only; delete after test |
| durableSourceSurface | forbidden during worker execution |
| publicSurface | none |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | dispatch-ready status, Source Verification columns, Gate-To-Role graph fields, return profile, trace labels and no-commit evidence |
| gateRunPurpose | confirm the source-authored packet and later worker return; not first discovery |
| claimBoundary | structural conformance only; not source creation or implementation correctness |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| immutable Group 3 schema | contract invariant | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Canonicalization Profile; Closed Preimage Field Lists; Source Group 3; Immutable Snapshot Identity | `cvf.observationLogEntry` | operational-source contract | ACCEPT |
| Party B authority | role contract | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_B_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party B Appointment Contract | `RegistryObservationOwner` | operator appointment | ACCEPT |
| tooling route and exclusions | Local decision | `docs/audits/CVF_ACEL_G1_T3C_GROUP3_SOURCE_READINESS_ROUTE_2026-09-21.md` | Route Selection; T3C-C1 Dispatch Boundary | principal-first route | Local orchestrator/reviewer | ACCEPT |
| Party B exact principal | OS fact recorded in paired baseline | paired baseline Evidence / Verification | exact name/SID/posture | Windows account store | ACCEPT |
| Group 1 snapshot envelope | current source | `governance/sources/verifier_key_registry/REGISTRY.json` | top-level envelope | `registrySnapshotVersion` | Group 1 registry | ACCEPT |

## Negative Search And Collision Discipline

Exact pre-author probes found all four worker outputs and the real Group 3 log
absent. Batch/tool-name searches found no implementation predecessor. Worker
must repeat exact checks and stop rather than overwrite a collision.

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
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact four outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact four outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact four outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | returned four paths | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | worker implementation followed by separate Local review/commit |
| phase | implementation then review |
| baseHeadFor(phase) | dispatchBaseHead=cf7872810; executionBaseHead=worker capture; closureBaseHead=reviewer set |
| changedSetScope(phase) | worker exact four paths; Local later accepts or repairs within authorized evidence boundary |
| traceScope(phase, actor) | worker return and Local review evidence |
| commitOwner(phase) | Local only; worker forbidden |
| crossBatchIsolation | thirteen parked paths remain byte-identical and unstaged |
| nextMoveSurfaces | worker return, then Local independent probe and disposition |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT T3C-C1 worker after operator forwards packet

laneOwnedPaths: exact four paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return, empty staging, exact delta and parked reconciliation

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| actor | one shared-workspace `INTERNAL_AGENT` worker |
| role set | PowerShell tooling, Python checker/test and evidence author; not reviewer/closer |
| delegation depth | zero |
| evidence basis | governed T2F/T3C sources and recorded Local OS evidence only; never provider memory or credentials |
| gate sequence | pre-implementation, focused tests, worker-return fast, Local review |
| self-review boundary | worker cannot accept, stage or commit output |
| role separation ledger | worker returns pending; Local independently probes, evaluates and commits |
| escalation condition | credentials, alternate-user/real-source execution, fifth output, parked drift or authority contradiction |

## Worker Output Checker Read-Ahead Mandate

Before writing the return, inspect every checker applying to a self-declared
worker return under `docs/reviews/`; derive exact headings, trace fields,
delta-boundary labels, no-commit evidence and conditional N/A blocks.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

evidenceReadinessContract: REQUIRED_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required real sections: Purpose; Scope / Methodology; Target / Source; Findings
/ Position; Risk / Corrective Action; Claim Boundary; Agent Operation Trace
Block; Delta Execution Claim Boundary Control Block; git status --short;
Changed Files; No-Commit Statement; Public Export Disposition.

Conditional sections must exist with `N/A with reason` where non-applicable.

## Execution Plan

1. Capture base/status/staging/parked hashes and pass pre-implementation.
2. Implement checker first from the closed schema and strict decoding rules.
3. Implement writer against that independent checker contract.
4. Add disposable positives and adversarial negatives; never touch real paths.
5. Run focused tests, checker self-test, worker-return fast gate and final diff.
6. Return uncommitted and stop.

## Evidence Requirements

Return T3C-C1-01 through T3C-C1-10: default non-mutation; published vector;
exact closed preimage; positive chain replay; strict encoding negatives;
duplicate-ID and no-mutation proof; identity separation; real-mode path lock;
focused test counts with exit codes; exact four-path/parked/staging reconciliation.

## Acceptance Criteria

- Exactly four worker paths changed and no staged files.
- Default writer mode is non-mutating and all tests use disposable fixtures.
- Schema, byte encoding, hashes, chain and immutable-ID rules match T2F.
- Real mode is fail-closed to exact Party B/name/SID, Group 1 input and Group 3 output.
- Issuer real mode is rejected; no Party C or full-establishment claim exists.
- Independent checker detects all listed negative classes deterministically.
- Worker return passes its full fast gate and contains no unresolved placeholder.

## Review Gate

Local evaluates returned evidence without routinely recreating the worker suite,
then runs the admitted independent positive and negative probes. Any material
contract defect yields one consolidated rework order; small review-owned
evidence defects may be fixed locally.

## Closure Checklist

- source fidelity and exact manifest verified;
- independent probe PASS;
- no real Group 3 path created by worker;
- no parked/staging drift;
- material commit by Local only;
- continuity sync records real SHA;
- real Party B execution remains a separate operator checkpoint.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all acceptance criteria and gates
pass. Return `BLOCKED_WITH_REASON` only for a source contradiction or required
scope beyond authority. Do not return routine allowed-scope repair to operator.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/test_check_acel_g1_registry_observation_log.py
python governance/compat/check_acel_g1_registry_observation_log.py --self-test
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git diff --cached --name-only
git status --short
```

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_COMPLETION_2026-09-21.md` (optional; prefer reviewer evidence in the worker return) |
| reviewerOwnedClosurePaths | worker return plus a separate Local verification artifact only if needed |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/dispatcher |
| Provider or surface | private CVF workspace and read-only Windows account store |
| Session or invocation | T3C-C1 dispatch authoring, 2026-09-21 |
| Working directory | repository root |
| Command or tool surface | governed reads, OS identity queries, scaffold helper, apply_patch and governance gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | T3C readiness route plus operator-provisioned Party B principal |
| Before status evidence | HEAD cf7872810; tracked worktree clean; staging empty; thirteen pre-existing parked paths isolated; four worker paths and real log absent |
| After status evidence | bounded four-path tooling dispatch; no worker/source execution |
| Diff evidence | `git diff --name-status` before dispatcher commit |
| Approval boundary | hermetic tooling dispatch only |
| Claim boundary | no observation/source/consumer/live/runtime/public effect |
| Agent type | Local reviewer/dispatcher |
| Invocation ID | `acel-g1-t3c-c1-dispatch-local-20260921` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order plus unchanged parked paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | repository tooling and disposable test behavior only |
| claimDisposition | CLAIM_REJECTED: no source establishment, consumer enforcement or runtime interception is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker return does not yet exist |
| actionEvidence | ACTION_EVIDENCE_PRESENT: paired dispatch only |
| invocationBoundary | worker may invoke only fixture/self-test modes |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement or agent-control claim |
| claimLanguage | implemented/tested applies only after Local review; dispatch alone proves no behavior |
| forbiddenExpansion | no credentials, real source, T3E, provider/live/public/deployment without fresh authority |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON

Reason: bounded first-party source tooling; no legacy/external absorption claim.

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
| Chain map route | N/A with reason: direct internal contract to Local dispatch to INTERNAL_AGENT tooling |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T2F Group 3 contract and this dispatch |
| Disposition | local first-party implementation only |
| Claim boundary | no external source authority, corpus, remote implementation or provider claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private principal-bound source tooling with no public-sync authority.

## Claim Boundary

This packet authorizes four uncommitted tooling/evidence artifacts and
disposable tests only. It does not authorize Party B credentials or execution,
real log creation, issuer observation, Group 3 establishment, T3E consumer
binding, candidate admission, provider/live work, public sync or deployment.

## Operator Checkpoint

After Local accepts and commits the tooling, Local may prepare a secret-free
launcher and exact command. Only the operator may authenticate as Party B and
perform the first real Group 1 observation. That action is not authorized now.
