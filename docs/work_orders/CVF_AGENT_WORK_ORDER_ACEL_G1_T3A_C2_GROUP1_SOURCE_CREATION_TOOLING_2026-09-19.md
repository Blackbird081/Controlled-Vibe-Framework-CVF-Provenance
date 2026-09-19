# CVF Agent Work Order - ACEL G1 T3A-C2 Group 1 Source-Creation Tooling

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Batch ID: ACEL-G1-T3A-C2-GROUP1-SOURCE-CREATION-TOOLING

Dispatch base HEAD: `835dfc39d`

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

Worker role: shared-workspace `INTERNAL_AGENT`

Reviewer/closer: Local orchestrator/reviewer

Worker return path: `docs/reviews/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-19.md`

## Dispatch Prompt Envelope

Role: internal security/source-tooling worker. Build a fail-closed,
principal-bound Group 1 source writer plus Local checker and hermetic tests;
do not perform the real Party A source write.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_2026-09-19.md`

Paired baseline: `docs/baselines/CVF_GC018_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_2026-09-19.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture committed HEAD, full status and staging before edits.

Current-time notes: Local independently verified public key
`R5AsDnHQNXWgD5WQEpDi3VABiuPZ7E9U5Kir_bgiwNU`, key ID
`partya-44853ea9a690452c`, digest
`5ae2ddf8433e5eab54001d6fa59586389b9c3ae6956e1155dac811a3cbbcab01`,
Party A SID `S-1-5-21-1644666849-912006174-747199667-1006`, and 365-day
validity. These are public inputs, not an established source.

Do-not-misread notes: never request credentials, use run-as, access the Party
A profile or DPAPI blob, generate another key, execute the real source write,
create either future source file, mutate the thirteen parked paths, stage,
commit, wire a live verifier, claim admission, public sync or deploy.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, this packet, paired baseline, T2F Group 1, T3A-C2 verification audit
and every checker named below. Freeze the thirteen parked paths before edits.

Return contract: satisfy C2-01 through C2-10, run required gates, leave
staging empty, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement deterministic tooling that a later operator can run under the exact
Party A principal to create the first Group 1 registry snapshot and genesis
lifecycle receipt from the already-verified public ceremony metadata. Supply
a Local checker/consumer and hermetic positive/negative tests without creating
the operational sources during worker execution.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3A-C2-GROUP1-SOURCE-ESTABLISHMENT --title "ACEL G1 T3A-C2 Group 1 Source Establishment" --date 2026-09-19 --base 9eabacc8b1daf58fe96cd9da34104c6095f912c5 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch; internal INITIAL; no-commit |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | narrowed real source establishment to exact principal-bound tooling, four outputs, C2 matrix and operator checkpoint |
| checkerReadAheadConfirmation | dispatch, convergence, closeability, structural, scaffold and worker-return checker paths |
| docOnlyNewFields | `SOURCE_CREATED_PENDING_LOCAL_VERIFICATION` is tool result language, not a T2F source-state replacement |
| claimBoundary | scaffold use does not execute Party A or create Group 1 sources |

## Authority Chain And Dependency Release Evidence

| Dependency | Evidence | Release condition | Disposition |
|---|---|---|---|
| Group 1 contract | T2F Source Group 1 and closed preimages | preserve exact fields, hashes, roles and paths | ACCEPT |
| ceremony product | T3A-C2 verification audit, commit `835dfc39d` | strict decode=32 bytes and digest match | ACCEPT |
| Party A identity | name/SID in verified metadata | tool must compare both to current process | ACCEPT_TOOLING_ASSUMPTION |
| real source write | Party A exclusive writer | accepted tooling then separate operator invocation | PARKED_OPERATOR_EXECUTION |
| consumer wiring | Future T3E | checker may consume/validate but no production wiring claim | DEFERRED_WITH_REASON |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake summary | principal-bound Group 1 source-creation tooling and hermetic checker evidence |
| scope | bounded code, hermetic tests and evidence return |
| risk | source-integrity and secret-adjacent, but public input only |
| selected role route | `SINGLE_AGENT_MULTI_ROLE`: one no-commit `INTERNAL_AGENT`, then Local review |
| selected route mode | `SINGLE_AGENT_MULTI_ROLE` |
| separation | worker cannot use Party A credentials or accept/commit its output |
| escalation | stop only for credential need, real alternate-user execution, source creation, extra path or authority contradiction |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL

dispatchSurface: INTERNAL_AGENT

parentAssignmentId: ACEL-G1-T3A-C2-GROUP1-SOURCE-CREATION-TOOLING

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

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T3A-C2-GROUP1-SOURCE-CREATION-TOOLING","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"CREDENTIAL_REFERENCE","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["scripts/","governance/compat/","docs/reviews/","docs/baselines/CVF_GC018_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_2026-09-19.md","AGENT_HANDOFF_V63_2026-09-18.md","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts","docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md","docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json","docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md","docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_MANIFEST_2026-09-17.json","docs/audits/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md","docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md","governance/compat/check_task_class_calibration_owner_evidence.py","governance/compat/test_check_task_class_calibration_owner_evidence.py"],"claims":["principal-bound Group 1 source-creation tooling and hermetic tests only"],"requiredProof":["C2-01 through C2-10","exact four-path delta","parked hashes","worker-return fast gate"],"operatorCheckpoints":["actual Party A source write","Local source verification","key promotion","consumer wiring"],"forbiddenEffects":["credential access","alternate-user execution","operational source creation","worker commit","candidate admission","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"N/A with reason: bounded named files","completenessClaimChanged":false}}
```

Expected route: `P3_ELEVATED`; shadow routing only. Full legacy gates apply.

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3a-c2-group1-source-creation-tooling","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":["real_party_a_ceremony_not_executed","group1_source_not_created"],"resolved":["real_party_a_ceremony_not_executed"],"retained":["group1_source_not_created"],"new":["group1_source_creation_tooling_not_implemented"],"reopened":[],"current":["group1_source_creation_tooling_not_implemented","group1_source_not_created"]},"resolutionEvidence":{"real_party_a_ceremony_not_executed":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/audits/CVF_ACEL_G1_T3A_C2_CEREMONY_PRODUCT_LOCAL_VERIFICATION_2026-09-19.md","sha256":"81b507d19e934c451a4d74ecca9c519f01dfceae42649a59ae4692624db99d3f","locator":"Decision / Disposition","claimId":"ACEL-G1-T3A-CEREMONY-PRODUCT-VERIFIED"}},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T3A-CEREMONY-PRODUCT-VERIFIED","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/audits/CVF_ACEL_G1_T3A_C2_CEREMONY_PRODUCT_LOCAL_VERIFICATION_2026-09-19.md"},{"claimId":"ACEL-G1-T3A-C2-TOOLING-DISPATCH","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/baselines/CVF_GC018_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_2026-09-19.md"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"NO_SUCCESSOR"}
```

## Acceptance Matrix

| ID | Required contract | Positive and negative proof |
|---|---|---|
| C2-01 | writer requires exact Party A name/SID and rejects elevation before any source mutation | exact-current hermetic pass; wrong-name, wrong-SID and elevated probes reject |
| C2-02 | input is strict `cvf.acel.g1.partyAPublicKeyMetadata@1`; base64url is canonical, 32 bytes, digest recomputes, algorithm/key/principal/dispositions match | verified vector passes; one-field mutations reject before output |
| C2-03 | registry row uses exactly T2F `cvf.keyRegistryRow` closed preimage and `cvf.source-record-canonicalization@1`; role=`verificationAuthority`, status=`ACTIVE`, nullable fields present | publish exact preimage bytes and independently recomputed `rowHashHex`; omission/extra/mutation reject |
| C2-04 | envelope contains fresh `registrySnapshotId`, version 1, RFC3339 write time and exactly one row; duplicate key and public-key alias checks fail closed | deterministic fixture plus duplicate/alias negatives |
| C2-05 | genesis lifecycle row uses exact closed preimage: fresh transition ID, versions 0 to 1, prior status `NOT_PRESENT`, new status `ACTIVE`, actor exact Party A, timestamp, `priorEntryHashHex:null`; own `entryHashHex` excluded | exact preimage/digest and chain recomputation tests |
| C2-06 | real-mode output paths are exactly T2F proposed registry and lifecycle paths; repository containment, reparse, collision and partial-write failures reject/clean up | disposable-repository sandbox only in tests; real paths remain absent |
| C2-07 | default mode is hermetic self-test; actual write requires explicit flag plus typed confirmation after all guards | default creates no durable sources; noninteractive execute rejects |
| C2-08 | Local checker reads both files, validates schemas, strict field sets, hashes, chain, uniqueness, alias, time/status/role and expected public product; no warning-pass | positive fixture plus taxonomy negatives, exit codes asserted |
| C2-09 | worker never runs as Party A, reads no Party A profile/private material, and never creates operational source | trace, searches and final absence checks |
| C2-10 | exact four worker outputs, empty staging and thirteen parked paths byte-identical | before/after status, hashes and manifest reconciliation |

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `scripts/acel_g1_party_a_group1_source_writer.ps1` | CREATE fail-closed writer with embedded hermetic self-test; real mode operator-only |
| `governance/compat/check_acel_g1_verifier_key_registry.py` | CREATE strict Local checker/read-only consumer for registry and lifecycle files or explicit fixture paths |
| `governance/compat/test_check_acel_g1_verifier_key_registry.py` | CREATE focused positive and mutation/chain/collision tests |
| `docs/reviews/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-19.md` | CREATE full evidence return |

## Work-Order Fulfillment Manifest

The table above is the exact worker output set. In particular, the worker must
not create `governance/sources/verifier_key_registry/REGISTRY.json` or
`governance/sources/verifier_key_registry/LIFECYCLE_LOG.jsonl`; those are
operator-run Party A outputs after Local accepts this tooling.

## Allowed Scope / Forbidden Scope

Allowed: create and test exactly the four manifest paths using disposable
fixtures, update only the worker-return evidence, and repair failures confined
to those paths. Forbidden: Party A credentials/profile/private blob, run-as,
real source files, existing governed source mutation, parked paths, staging,
commit, T3E wiring, live/provider/public/deployment effects.

## Write Ownership

Worker owns uncommitted edits to the exact four manifest paths. Local owns
review, bounded evidence repair, staging and commits. Every existing path,
both future source files and the thirteen parked paths are read-only.

## Agent Roles

| Role | Responsibility |
|---|---|
| operator | retains Party A password and later real source-write authority |
| Local dispatcher | commits packet and preserves principal/source boundary |
| INTERNAL_AGENT worker | implements exact tooling/checker/tests/return without credentials or commit |
| Local reviewer/closer | reviews invariants, runs bounded probes and decides acceptance |
| session-sync steward | updates continuity after Local disposition |

## Required First Reads

1. Startup front door, bootstrap model, active handoff, guard orientation and literal gotchas.
2. This order, paired baseline, T2F Group 1 and T3A-C2 verification audit.
3. Applicable checker sources, the accepted C1 tool's repaired process/ACL patterns, and output-specific worker-return rules.

## Pre-Flight Checks

- Capture execution HEAD, full status, empty staging and hashes of all thirteen parked paths.
- Confirm the dispatch commit exists and all four worker outputs plus both real source paths are absent.
- Confirm no Party A credential/private artifact is present or requested.
- Run the pre-implementation autorun gate before editing.

## Implementation Contract

- Use only PowerShell/.NET functionality available to the clean Party A
  profile; resolve any required executable by absolute machine path or avoid
  it. Do not repeat the C1 current-user PATH defect.
- Construct DACL-only security descriptors; do not request or persist SACL
  sections requiring `SeSecurityPrivilege`.
- Use UTF-8 without BOM, exclusive create and rollback of partial two-file
  writes. Never overwrite an existing source.
- Canonical JSON preimages must be compact and lexicographically key ordered.
  Publish exact bytes/digests in hermetic evidence and recompute independently
  in the Python checker.
- `issuedAt` and `expiresAt` come exactly from verified ceremony metadata;
  `revokedAt` and `rotatedFromKeyId` are JSON null.
- Real output is still `SOURCE_CREATED_PENDING_LOCAL_VERIFICATION`, never
  admission or T3E consumer wiring. Tool output text must say so explicitly.

## Worker Autonomy / No-Question Rule

Repair all allowed-scope implementation and gate failures directly. Stop only
for credentials, alternate-user/real-source execution, a fifth output, parked
drift or a source-authority contradiction.

## ADIF Defect Registry Disclosure

Dispatcher query `CODE_CHANGE`/`dispatcher`/`dispatch` returned zero defects.
Worker must rerun for `CODE_CHANGE`/`worker`/`implementation` and disclose the
actual result in the return.

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | exact section headings, controlled disposition tokens, trace labels, no-commit and changed-set evidence |
| gateRunPurpose | confirm authored output after source-driven design |
| claimBoundary | structure and governed-path compatibility only; not proof the worker read them |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| exact Group 1 fields/preimages | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Closed Preimage Field Lists; Source Group 1 | `cvf.keyRegistryRow`; `cvf.keyLifecycleReceipt` | Group 1 contract | ACCEPT |
| exclusive Party A writer | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Group 1 Write Principal/Forbidden Roles | Party A | Group 1 access contract | ACCEPT |
| real public input | `docs/audits/CVF_ACEL_G1_T3A_C2_CEREMONY_PRODUCT_LOCAL_VERIFICATION_2026-09-19.md` | Verified Public Metadata; Verification Evidence | key ID and public key digest | ceremony public-product receipt | ACCEPT |
| actual sources absent | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Literal Proposed-Path Collision Ledger | both proposed Group 1 paths, freshly re-probed | Local source boundary (`SOURCE_NOT_CREATED`) | ACCEPT |

## Negative Search And Collision Discipline

All four worker paths and both future source paths were absent at dispatch.
Exact batch/key searches found only the committed verification audit. Any
collision appearing after dispatch is a stop condition unless it is one of
the four lane-owned worker outputs created by this worker.

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
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return ADIF disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact four outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact four outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | returned four paths | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | six continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | Local dispatcher -> no-commit INTERNAL_AGENT worker -> Local reviewer/closer |
| phase | T3A-C2 source-creation tooling; actual Party A source write excluded |
| baseHeadFor(phase) | dispatchBaseHead=`835dfc39d`; executionBaseHead captured by worker; closureBaseHead set by Local |
| changedSetScope(phase) | exact four required outputs |
| traceScope(phase, actor) | reads, commands, tests, hashes, status, cleanup and absence of real sources |
| commitOwner(phase) | Local only |
| crossBatchIsolation | thirteen parked paths byte-identical |
| nextMoveSurfaces | Local review, then separate Party A operator source-write checkpoint |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT T3A-C2 tooling worker after operator forwards this packet

laneOwnedPaths: exact four paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return, empty staging, exact delta and parked reconciliation

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| actor | one shared-workspace `INTERNAL_AGENT` worker |
| role set | PowerShell source-tooling implementer, Python checker/test implementer and evidence author; not reviewer/closer |
| delegation depth | zero |
| evidence basis | governed T2F/T3A sources and public metadata only; never provider memory or private material |
| gate sequence | pre-implementation, focused tests, worker-return fast, Local review |
| self-review boundary | worker cannot accept, stage or commit its output |
| role separation ledger | worker returns pending; Local evaluates and commits |
| escalation condition | credentials, alternate-user/real-source execution, fifth output, parked drift or authority contradiction |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-19.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required real sections: Purpose; Scope / Methodology; Target / Source;
Findings / Position; Risk / Corrective Action; Decision / Disposition; Claim
Boundary; Changed Files; Command Evidence; No-Commit Statement; Agent Operation
Trace Block; Delta Execution Claim Boundary Control Block; Machine Closure
Package; Public Export Disposition. Use `N/A with reason` for conditional
blocks that do not apply.

## Execution Plan

1. Freeze state, parked hashes and output absence; run pre-implementation gate.
2. Implement the PowerShell writer with identity, input, path, confirmation, DACL and atomicity guards.
3. Implement the independent Python checker and focused tests against disposable fixtures.
4. Publish exact preimage bytes/digests and run all positive/negative cases.
5. Create the evidence return, run fast gate, reconcile exact outputs and leave staging empty.

## Evidence Requirements

Return C2-01 through C2-10 with command/result evidence, exact hashes, negative
taxonomy, cleanup/absence proof, empty staging and parked-file reconciliation.
Never include credentials, DPAPI bytes, private-key material or a real source.

## Acceptance Criteria

All C2 rows pass; default invocation is non-mutating; wrong principal,
elevation, malformed metadata, digest drift, unsafe path, collision and
noninteractive execution fail before output. Exactly four worker paths change.

## Review Gate

Local inspects guard ordering, DACL and two-file rollback, consumes valid
returned evidence and runs bounded checker/mutation probes. Local will not run
the real Party A source write during worker review.

## Closure Checklist

- [ ] C2-01 through C2-10 reviewed.
- [ ] Exact four paths and all parked hashes reconcile.
- [ ] Worker-return fast and reviewer preflight pass.
- [ ] Both real Group 1 source paths remain absent.
- [ ] No credential/private/alternate-user action occurred.
- [ ] Material and continuity commits remain separate.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` only for a credential need, Party A or real-source
execution, fifth output, parked drift, source-authority contradiction or an
irreparable mandatory gate failure. Otherwise return
`COMPLETE_PENDING_REVIEW`, never source/admission readiness.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
pwsh -NoProfile -File scripts/acel_g1_party_a_group1_source_writer.ps1
python governance/compat/test_check_acel_g1_verifier_key_registry.py
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
```

The self-test must use disposable paths only and prove the two real source
paths remain absent. No provider/live release-gate call applies: this tranche
does not assert CVF AI governance behavior or production readiness.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_COMPLETION_2026-09-19.md` (optional; prefer bounded evidence repair in the worker return) |
| reviewerOwnedClosurePaths | exact four worker outputs plus necessary bounded evidence repair |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/dispatcher |
| Provider or surface | private CVF workspace |
| Session or invocation | T3A-C2 tooling dispatch, 2026-09-19 |
| Working directory | repository root |
| Command or tool surface | governed reads, ceremony metadata recomputation, scaffold/read-ahead, apply_patch and gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | T2F Group 1 plus committed T3A-C2 Local verification |
| Before status evidence | HEAD `835dfc39d`; tracked worktree clean; staging empty; thirteen pre-existing parked untracked paths isolated |
| After status evidence | exact paired dispatch paths pending before commit; parked paths unchanged |
| Diff evidence | paired packet staged alone before dispatch commit |
| Approval boundary | tooling and hermetic tests only |
| Claim boundary | no credential, Party A execution, operational source, admission, live/runtime/public effect |
| Agent type | Local dispatcher and later reviewer/closer |
| Invocation ID | `acel-g1-t3a-c2-source-tooling-dispatch-20260919` |
| Expected manifest | paired T3A-C2 baseline and work order |
| Actual changed set | reconciled before dispatch commit |
| Manifest delta | pending exact staging reconciliation |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | source-creation tooling and hermetic validation only |
| claimDisposition | CLAIM_REJECTED for real source creation, runtime enforcement, admission or consumer wiring |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker return does not yet exist |
| actionEvidence | ACTION_EVIDENCE_PRESENT: paired dispatch only |
| invocationBoundary | no Party A or real-mode invocation by worker |
| interceptionBoundary | no runtime wrapper/proxy or agent-control claim |
| claimLanguage | tooling implemented/tested; source remains not created |
| forbiddenExpansion | credentials, alternate user, actual sources, T3E wiring, live/public/deployment |

## Claim Boundary

This order authorizes tooling and hermetic tests only. It does not authorize
the worker to create operational source files, touch private material, claim
Party A authority, promote the key, admit a candidate, wire T3E, run live AI
governance proof, public-sync or deploy.

## Legacy Absorption Coverage Index Disposition

`NOT_APPLICABLE_WITH_REASON`

Reason: bounded first-party Windows and local-source tooling; no legacy or
external corpus is ingested, mapped or absorbed.

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/audits/CVF_ACEL_G1_T3A_C2_CEREMONY_PRODUCT_LOCAL_VERIFICATION_2026-09-19.md` |
| Chain map route | N/A with reason: direct operator ceremony output -> Local verification -> bounded INTERNAL_AGENT tooling |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T2F Group 1 contract and T3A-C2 Local verification audit |
| Disposition | local first-party implementation only |
| Claim boundary | no external source authority, external corpus, remote implementation or provider claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source-control tooling bound to a local principal and a
not-yet-created private source.

## Operator Checkpoint

After Local accepts the worker tooling, the operator alone runs its explicit
real mode under `LAM-RUBY\cvf-g1-party-a`. Key promotion, Local source
verification, T3E consumer wiring and candidate admission remain later
checkpoints; this dispatch opens none of them.
