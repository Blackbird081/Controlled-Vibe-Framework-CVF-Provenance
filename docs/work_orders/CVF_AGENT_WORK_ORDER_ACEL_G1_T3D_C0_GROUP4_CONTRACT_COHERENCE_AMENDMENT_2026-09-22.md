# CVF Agent Work Order - ACEL G1 T3D-C0 Group 4 Contract Coherence Amendment

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Batch ID: ACEL-G1-T3D-C0-GROUP4-CONTRACT-COHERENCE-AMENDMENT

Dispatch base head: `e341a9021`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

Worker: shared-workspace `INTERNAL_AGENT`

Reviewer/closer: Local orchestrator/reviewer

Worker return path: `docs/reviews/CVF_ACEL_G1_T3D_C0_GROUP4_CONTRACT_COHERENCE_AMENDMENT_WORKER_RETURN_2026-09-22.md`

## Dispatch Prompt Envelope

Role: bounded shared-workspace `INTERNAL_AGENT` documentation worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C0_GROUP4_CONTRACT_COHERENCE_AMENDMENT_2026-09-22.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture the committed HEAD at worker start and record it in the return.

Current-time notes: Party C is Local verified as SID ending `-1010`; Group 4
is `CONTRACT_REWORK_REQUIRED`; Group 4 tooling, registry, lookup response,
second Party B observation, T3E and consumer binding remain absent.

Do-not-misread notes: documentation amendment only. Do not create tooling or
durable sources, run as Party B or Party C, perform a lookup, use credentials,
stage, commit, or treat a checker pass as runtime/source evidence.

Required first actions: read startup front door/bootstrap/active handoff,
guard orientation, literal gotchas, this packet, its named source owners and
applicable checker sources. Capture HEAD, status, staging, and the thirteen
parked-path SHA-256 values before editing.

Return contract: amend exactly one existing contract and create exactly one
worker return. Freeze all four listed resolutions, run required document gates,
leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

independentProbeRequired: YES

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - documentation-only contract amendment authorizes no local mutation tooling or runtime transaction.

## Purpose

Amend the existing T2F operational-source contract so its Group 4 registry
and lookup-response design is implementation-closeable without creating any
source, tooling, credential, runtime transaction, or verifier consumer.

## Authority Chain

| Authority step | Evidence | Worker consequence |
|---|---|---|
| Group 4 pre-implementation gap audit | `docs/audits/CVF_ACEL_G1_T3D_GROUP4_PRE_IMPLEMENTATION_CONTRACT_GAP_AUDIT_2026-09-22.md` | resolve all four gaps in one T2F amendment before a T3D-C1 packet is possible |
| Existing Group 4 owner contract | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | amend the current owner; do not create a competing Group 4 contract |
| Party C principal verification | `docs/audits/CVF_ACEL_G1_T3D_PARTY_C_PRINCIPAL_LOCAL_VERIFICATION_2026-09-22.md` | use recorded Party C role separation only; do not provision or authenticate as Party C |
| Party B immutable boundary | `docs/reviews/CVF_ACEL_G1_T2H_PARTY_B_IMMUTABLE_OBSERVATION_RECONCILIATION_WORKER_RETURN_2026-09-18.md` | preserve Party B as independent observer and response-appender, never a registry writer |
| this dispatch | this work order | documentation amendment and pending return only |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake summary | first-party Group 4 contract-coherence amendment |
| scope classification | documentation-only owner-contract correction with identity and least-privilege impact |
| risk sensitivity | exact-byte identity, independent observation, DACL separation and consumer-establishment boundary |
| selected route mode | `SINGLE_AGENT_MULTI_ROLE`: worker authors bounded documents; Local reviews, accepts and commits |
| role separation basis | worker has no authority to provision principals, create source files, run a transaction, stage or commit |
| escalation condition | source contradiction, third output, any runtime/source action, parked drift, credential request, or boundary expansion |

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T3D-C0-GROUP4-CONTRACT-COHERENCE-AMENDMENT","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"DOC_CHANGE","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"NEW_INTERFACE"},"pathFamilies":["AGENT_HANDOFF_V63_2026-09-18.md","CVF_SESSION/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/","docs/audits/","docs/baselines/","docs/reference/","docs/reviews/","docs/work_orders/","governance/compat/"],"claims":["T2F Group 4 contract explicitly fixes four previously ambiguous design joins; no source is established"],"requiredProof":["four-resolution amendment matrix","exact T2F delta","planned adversarial vectors","worker-return fast gate","13/13 parked-path hashes"],"operatorCheckpoints":["T3D-C1 tooling dispatch","Party C registry write","Party B issuer observation","T3E real consumer call","candidate admission"],"forbiddenEffects":["credential access","local account action","registry or response source creation","runtime transaction","provider/live/network","worker commit","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"N/A with reason: bounded named files only","completenessClaimChanged":false}}
```

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3D-C0-GROUP4-CONTRACT-COHERENCE-AMENDMENT --title "ACEL G1 T3D-C0 Group 4 Contract Coherence Amendment" --date 2026-09-22 --base e341a9021 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus documentation-only no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | populated exact two-path amendment manifest, four frozen decisions, worktree exemptions, review boundary and private-only disposition |
| checkerReadAheadConfirmation | dispatch-quality, closeability, worker-return, scaffold-provenance, trace, ADIF and delta-boundary sources read before authoring |
| docOnlyNewFields | Group 4 byte/DACL/consumer-boundary clauses added only to the existing T2F contract |
| claimBoundary | dispatch proves only a bounded documentation task; it does not prove tooling or source behavior |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G1-T3D-C0-GROUP4-CONTRACT-COHERENCE-AMENDMENT
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3d-c0-group4-contract-coherence","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":["G4_GAP_01","G4_GAP_02","G4_GAP_03","G4_GAP_04"],"resolved":[],"retained":["G4_GAP_01","G4_GAP_02","G4_GAP_03","G4_GAP_04"],"new":[],"reopened":[],"current":["G4_GAP_01","G4_GAP_02","G4_GAP_03","G4_GAP_04"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T3D-C0-CONTRACT-ONLY","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"amended T2F Group 4 sections and worker return"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Dependency Release Evidence

| Dependency | Evidence | Release condition | Disposition |
|---|---|---|---|
| Group 4 gap selection | T3D gap audit, Selected Route | four gaps are consolidated and direct tooling is blocked | RELEASED_FOR_DOCUMENT_AMENDMENT |
| existing owner contract | T2F Source Group 4 and T2C consumer-binding sections | amend existing owner rather than duplicate it | RELEASED |
| Party C identity | Party C Local verification, Findings / Position | role exists and remains distinct from Party B | RELEASED_FOR_CONTRACT_ONLY |
| Party B separation | T2H worker return, Party C separation disposition | Party B remains observer/response role, not registry writer | RELEASED |
| T3D-C1 implementation | no accepted T3D-C0 amendment yet | Local acceptance after this return | PARKED_PENDING_T3D_C0_REVIEW |
| T3E consumer call | T2F Group 4 establishment checklist | dedicated future consumer-binding tranche only | PARKED_T3E |

## Independent Review Probe Admission Contract

independentProbeRiskClass: HIGH

independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: REQUIRED_DIFFERENT_EXECUTION_AND_ASSERTION_PATH

positiveControl: Local independently reconstructs both exact JCS byte vectors, recomputes both SHA-256 digests, and compares the amended lifecycle and access matrices with this baseline

negativeMutationClasses: one-byte content drift, padding, BOM, newline, reordered snapshot rows, whole-row content preimage, Party C response access, Party B registry write, and T3D establishment overclaim

expectedInformationGain: distinguish copied constants and self-consistent prose from independently reproducible byte, authority, and lifecycle contracts

rerunCostReason: a focused Local text/vector probe resolves the decision without duplicating broad document authoring

reviewerDecisionOwner: LOCAL

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | exact two documentation outputs | amendment/return only; no local source, transaction, credential, staging or commit | this work order and paired baseline | Markdown artifact authoring | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no owner | no external ingress, mutation, runtime, receipt or public claim | no authority | fresh packet required | DEFERRED_WITH_REASON |

## Planned Artifact Manifest

| Path | Required worker action | Purpose |
|---|---|---|
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | modify in place | add the four frozen Group 4 contract resolutions and vectors |
| `docs/reviews/CVF_ACEL_G1_T3D_C0_GROUP4_CONTRACT_COHERENCE_AMENDMENT_WORKER_RETURN_2026-09-22.md` | create | checker-safe pending evidence return |

## Planned Worker Fulfillment Manifest

The preceding table is the complete worker output set. No registry, response
log, script, checker, test, baseline, account, launcher, or source file may be
created or modified by this dispatch.

## Allowed Scope / Forbidden Scope

Allowed: modify the named T2F audit contract and create the named worker
return; repair document/gate defects confined to those paths. Forbidden:
credentials, account operations, any `governance/sources` creation or read for
execution, mutation tooling, real lookup, Party B or Party C execution,
second observation, T3D-C1, T3E, existing checker/source changes, parked
paths, staging, commit, provider/live work, public sync and deployment.

## Write Ownership

Worker owns uncommitted edits to exactly the two planned paths. Local owns
review, acceptance, any later source/tooling decision, staging, commit and
continuity. Any third path is a stop condition.

## Agent Roles

| Role | Owner | Authority |
|---|---|---|
| dispatcher | Local orchestrator/reviewer | authors and commits the dispatch packet |
| implementer | shared-workspace `INTERNAL_AGENT` | exact two documentation outputs, no commit |
| reviewer/closer | Local orchestrator/reviewer | evaluates returned evidence, repairs only small in-scope defects, stages and commits accepted outputs |
| operator | human operator | later principal passwords and real Party B/Party C execution only; no action in T3D-C0 |

## Pre-Existing Dirty Path Exemptions

| Path | Status at dispatch | Exemption boundary |
|---|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts` | `??` | do not edit, stage, claim or hash-normalize |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts` | `??` | do not edit, stage, claim or hash-normalize |
| `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md` | `??` | do not edit, stage, claim or hash-normalize |
| `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json` | `??` | do not edit, stage, claim or hash-normalize |
| `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md` | `??` | do not edit, stage, claim or hash-normalize |
| `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_MANIFEST_2026-09-17.json` | `??` | do not edit, stage, claim or hash-normalize |
| `docs/audits/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md` | `??` | do not edit, stage, claim or hash-normalize |
| `docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md` | `??` | do not edit, stage, claim or hash-normalize |
| `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_WORKER_RETURN_2026-09-17.md` | `??` | do not edit, stage, claim or hash-normalize |
| `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_WORKER_RETURN_2026-09-17.md` | `??` | do not edit, stage, claim or hash-normalize |
| `docs/reviews/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_WORKER_RETURN_2026-09-17.md` | `??` | do not edit, stage, claim or hash-normalize |
| `governance/compat/check_task_class_calibration_owner_evidence.py` | `??` | do not edit, stage, claim or hash-normalize |
| `governance/compat/test_check_task_class_calibration_owner_evidence.py` | `??` | do not edit, stage, claim or hash-normalize |

## Required First Reads

- `CVF_SESSION_MEMORY.md`, its bootstrap model and `AGENT_HANDOFF_V63_2026-09-18.md`.
- `docs/reference/guard_orientation/README.md` and `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
- This work order and paired GC-018 baseline.
- T3D gap audit, T2F owner contract, Party C Local verification and T2H Party B boundary.
- All checker sources in the read-ahead block.

## Pre-Flight Checks

Capture `git rev-parse --short HEAD`, `git status --short --untracked-files=all`,
`git diff --cached --name-only`, and SHA-256 of the thirteen exempt paths.
Run the pre-implementation autorun with the worker-captured base. Stop on
non-empty staging, changed exempt hash, output collision, source contradiction
or any need to create a non-document artifact.

## Current Runtime Freshness Verification

| Runtime-sensitive claim | Fresh check at dispatch | Disposition |
|---|---|---|
| Group 4 tooling/source absent | targeted path checks at HEAD `e341a9021` found no `REGISTRY.json`, `LOOKUP_RESPONSES.jsonl`, T3D-C1 tooling, or T3D-C0 worker return | VERIFIED_ABSENT_AT_DISPATCH |
| Party C principal | Local verification artifact records exact SID ending `-1010`; this packet does not re-run or mutate the account | VERIFIED_BY_CURRENT_LOCAL_ARTIFACT |
| consumer binding | active handoff and gap audit keep T3E parked; this packet authorizes no runtime probe | VERIFIED_NOT_EXECUTED_AT_DISPATCH |
| freshness boundary | worker must recheck output collision and authority contradiction at execution start | RECHECK_REQUIRED_BY_WORKER |

## Frozen Four-Resolution Authority Contract

The worker must add a clearly headed T3D-C0 amendment inside the existing T2F
owner document. It must resolve all rows below together; it must not change a
separate owner or claim that Group 4 exists.

| Gap | Frozen amendment resolution | Required positive and adversarial vector |
|---|---|---|
| G4-GAP-01 | `REGISTRY.json` bytes are UTF-8 without BOM and exactly equal RFC 8785 JCS serialization of the complete registry envelope. `registrySnapshotHashHex` is lowercase SHA-256 over those JCS bytes. The Group 3 Party B record for `issuer_registry` has strict-decoded `snapshot_content` bytes exactly equal to those JCS bytes and `snapshotHashHex` exactly equal to `registrySnapshotHashHex`; raw parsed-object equivalence is insufficient. The worker must copy baseline vector `G4-SNAPSHOT-JCS-POSITIVE-01` exact bytes and independently recompute digest `d31e0c206da091bc408005d490e69f7aa0eae733dac4b03c67edd280034827f2`. | exact positive equal-byte/hash vector; reject BOM, whitespace/order drift, row reorder, parsed-only equality, wrong digest, response digest drift and Party C self-observation |
| G4-GAP-02 | Each issuer row gains required `canonicalContentBytesBase64`, the strict unpadded base64url encoding of exact RFC 8785 JCS UTF-8 bytes for the issuer-authority content object. Positive content is exactly `{"authority":"ACEL_G1_DECISION_OWNER","issuerIdentity":"issuer-test-001","policyVersion":1}` and its lowercase SHA-256 is `db76dcc22fcec9cc566c5b449b0aaa8eabdb657d157c62cba626aba8b26d12ca`. Validate strict row/schema, strict decode, valid JSON/JCS byte equality, recomputed hash, stored hash, `claimedIssuerHash == issuerAttestedHash == canonicalContentHashHex`, snapshot/Party-B equality, then ACTIVE status. The full row is never the content preimage. Failure classification is separate from durable recording: malformed or incomplete evidence that cannot populate the closed response schema returns a fail-closed in-memory negative and appends nothing; every schema-complete receipt-eligible query appends exactly one terminal confirmed, rejected, or unresolved response. | independently recompute the exact vector; reject padding, malformed/noncanonical encoding, non-JCS/invalid content, mutation, stored/attested/claimed mismatch, and whole-row-as-content; verify zero append for pre-admission failure and exactly one append for each receipt-eligible terminal outcome |
| G4-GAP-03 | `REGISTRY.json` is Party C-owned and protected. Its complete DACL is Party C, SYSTEM and Administrators `FullControl`, plus Party B and Local `Read`; Party A and Approver have no ACE/access. `LOOKUP_RESPONSES.jsonl` is Party B-owned and protected. Its complete DACL is Party B, SYSTEM and Administrators `FullControl`, plus Local `Read`; Party C, Party A and Approver have no ACE/access. No inheritance, deny or extra ACE is allowed. Party C exclusively mutates the registry; Party B exclusively appends responses and cannot mutate the registry. | exact owner/protected complete-ACE positive; reject Party B registry mutation, Party C response access/append, Local write, Party A/Approver access, inherited/extra/deny ACE, wrong owner, concurrent/partial append, or any failed operation without exact byte/security rollback |
| G4-GAP-04 | T3D-C0 concludes only `CONTRACT_ACCEPTED_BOUNDED_SOURCE_NOT_CREATED` and must not claim tooling acceptance. Separately authorized tooling may reach `TOOLING_ACCEPTED_SOURCE_NOT_CREATED`; bounded source creation may reach only `SOURCE_CREATED_LOCAL_VERIFIED_PENDING_CONSUMER_BINDING` after Local source checks. T3D must not check the T2F Group 4 real-verifier-consumer row. T3E exclusively owns the real verifier lookup call, final response-to-consumer comparison and final consumer-binding checklist disposition. | C0 contract-only and later T3D pending-state positives; reject C0 tooling/source wording and any T3D `ESTABLISHED`, `CONSUMER_BOUND`, or final-admission wording; require the T3E-owned final row |

## Worker Autonomy / No-Question Rule

Repair allowed-scope documentation and gate defects directly. Return only for a
source contradiction, third output, parked drift, request for a credential or
runtime/source action, or an authority/claim-boundary expansion.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| canonicalPrivateWorkspace | current private provenance repository |
| workerMutationSurface | exact two-path documentation manifest |
| durableSourceSurface | forbidden during worker execution |
| localTransactionSurface | forbidden; High-Risk Local Transaction Proof is not applicable |
| publicSurface | none |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch-ready status, source-verification columns, closeability graph, worker-return profile, trace labels, ADIF query, eight delta rows and private export disposition |
| gateRunPurpose | confirm document packet/return structure after authoring; not discover contract decisions |
| claimBoundary | gate conformance does not establish a Group 4 source or consumer behavior |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| four decision-changing Group 4 gaps | Local audit | `docs/audits/CVF_ACEL_G1_T3D_GROUP4_PRE_IMPLEMENTATION_CONTRACT_GAP_AUDIT_2026-09-22.md` | Findings / Position; Selected Route | G4-GAP-01 through G4-GAP-04 | T3D-C0 amendment decision | ACCEPT |
| Group 4 owner schema and lookup boundary | existing contract | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 4; T2C Consumer-Binding Table; Establishment Evidence Checklist | `sourceRegistry.lookup(...)` | operational-source contract | ACCEPT |
| Party B independent observation boundary | role contract | `docs/reviews/CVF_ACEL_G1_T2H_PARTY_B_IMMUTABLE_OBSERVATION_RECONCILIATION_WORKER_RETURN_2026-09-18.md` | Party B separation and immutable observation disposition | Party B observer role | operator-approved reconciliation | ACCEPT |
| Party C concrete identity | Local OS evidence | `docs/audits/CVF_ACEL_G1_T3D_PARTY_C_PRINCIPAL_LOCAL_VERIFICATION_2026-09-22.md` | Findings / Position | `LAM-RUBY\\cvf-g1-party-c`, SID ending `-1010` | Windows local-account store | ACCEPT |
| no real Group 4 path created | current control state | `AGENT_HANDOFF_V63_2026-09-18.md` | Next Allowed Move; Parked Checkpoints | T3D-C1/T3E | active handoff | ACCEPT |

## Negative Search And Collision Discipline

Before editing, verify the worker-return path is absent and the T2F path is
present; search T2F for the four field names and confirm no competing T3D-C0
contract file exists. A collision, source-existence claim or third-path need
is a stop condition, not permission to overwrite or widen scope.

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
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact two outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact two outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact two outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | returned two paths | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted document amendment | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | worker document amendment followed by separate Local review/commit |
| phase | amendment then review |
| baseHeadFor(phase) | dispatchBaseHead=e341a9021; executionBaseHead=worker capture; closureBaseHead=reviewer set |
| changedSetScope(phase) | worker exact two paths; Local accepts or repairs only within the documented owner amendment |
| traceScope(phase, actor) | worker return and Local review evidence |
| commitOwner(phase) | Local only; worker forbidden |
| crossBatchIsolation | thirteen exempt paths remain byte-identical and unstaged |
| nextMoveSurfaces | worker return, then Local contract review and disposition |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT T3D-C0 document worker after operator forwards packet

laneOwnedPaths: exact two paths in Planned Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return, empty staging, exact delta and parked reconciliation

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| actor | one shared-workspace `INTERNAL_AGENT` worker |
| role set | contract amendment author and evidence author; not reviewer/closer |
| delegation depth | zero |
| evidence basis | governed local sources only; never provider memory, credentials or runtime observation |
| gate sequence | pre-implementation, document verification, worker-return fast, Local review |
| self-review boundary | worker cannot accept, stage or commit output |
| role separation ledger | worker returns pending; Local evaluates exact amendment and commits if accepted |
| escalation condition | third path, source/action request, parked drift or authority contradiction |

## Worker Output Checker Read-Ahead Mandate

Before writing the return, inspect every checker applying to a worker return in
the reviews area. Derive exact headings, trace fields, delta labels,
no-commit evidence, source inventory actions and conditional N/A blocks.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T3D_C0_GROUP4_CONTRACT_COHERENCE_AMENDMENT_WORKER_RETURN_2026-09-22.md`

contractProfile: WORKER_RETURN_FAST_DOC_V1

scopeClassification: DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT

evidenceReadinessContract: NOT_APPLICABLE_WITH_REASON: bounded two-document contract amendment has no discovery audit, discovery manifest, source root, or evidence-readiness index output

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C0_GROUP4_CONTRACT_COHERENCE_AMENDMENT_2026-09-22.md`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

publicSyncDisposition: FORBIDDEN

liveRuntimeDisposition: FORBIDDEN

checkerMutationDisposition: FORBIDDEN

workerSelfSelection: FORBIDDEN

Required real sections: Purpose; Target / Source; Scope / Methodology;
Findings / Position; Risk / Corrective Action; Decision / Disposition; Claim
Boundary; Agent Operation Trace Block; Delta Execution Claim Boundary Control
Block; `git status --short`; Changed Files; No-Commit Statement; External
Knowledge Intake Routing; Epistemic Process Block; Public Export Disposition.
Conditional sections must exist with `N/A with reason` where non-applicable.

## Execution Plan

1. Capture base/status/staging/parked hashes; read all named authority and checker sources; run pre-implementation.
2. Amend only T2F, adding one T3D-C0 section that freezes all four rows and their positive/adversarial vectors.
3. Create the worker return from the compact document scaffold, then record exact delta, gate results and no-commit state.
4. Rerun the document checks and worker-return fast gate after the final edit.
5. Return uncommitted and stop; Local alone decides acceptance and any T3D-C1/T3E future work.

## Evidence Requirements

Return T3D-C0-01 through T3D-C0-08: exact two-path manifest; T2F amendment
location; each frozen resolution; all listed positive/adversarial vectors;
no source/tooling action; worker-return gate; staging status; and 13/13
parked-path SHA-256 reconciliation.

## Acceptance Criteria

- T2F is amended in place; no competing Group 4 contract is created.
- Each of G4-GAP-01 through G4-GAP-04 has the frozen resolution and at least one positive and one fail-closed adversarial vector.
- Registry JCS byte identity, hash and Party B observation binding are explicit.
- `canonicalContentBytesBase64` has an exact noncircular preimage and recomputation rule.
- Party C registry authority and Party B response append authority have the exact protected access-control split.
- T3D ends pending consumer binding, and T3E exclusively owns the final real-consumer disposition.
- Exactly two worker paths changed, no staging exists, and all thirteen exempt-path hashes match.
- Worker return passes the compact document fast gate with no unresolved placeholder.

## Fail Conditions

- Any source, tooling, registry, response log, credential, account, transaction or consumer call is created, read for execution or changed.
- A third worker path, a parked-path difference, non-empty staging, or worker commit is present.
- Any frozen resolution is vague, omitted, circular, grants an unauthorized write capability, or advances T3D beyond pending consumer binding.

## Review Gate

Local evaluates the returned evidence without broadly recreating document work.
A named contradiction may admit a targeted source recheck. A material contract
defect returns one consolidated finding set; a small evidence-shape repair may
be Local-owned within the two-path boundary.

## Return-Time Closeability Recheck

Before `COMPLETE_PENDING_REVIEW`, confirm the two output paths remain the full
manifest, every closeability graph gate has a role and repair surface, the
return is checker-safe, staging is empty and all thirteen exempt hashes match.

## Closure Checklist

- source fidelity, four-resolution completeness and exact two-path delta verified;
- no high-risk local transaction, source creation or runtime action occurred;
- worker-return fast, reviewer-fast, pre-commit and committed-range closure remain reviewer/closer work;
- worker commit prohibition and material/continuity choreography are truthful;
- public-private boundary remains deferred private only.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only after every acceptance criterion and
required gate passes. Return `BLOCKED_WITH_REASON` for a source contradiction,
third output, credential/runtime/source need, parked drift or boundary
expansion. Do not return ordinary permitted documentation repair to the operator.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C0_GROUP4_CONTRACT_COHERENCE_AMENDMENT_2026-09-22.md
git diff --name-status
git diff --cached --name-only
git status --short --untracked-files=all
```

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G1_T3D_C0_GROUP4_CONTRACT_COHERENCE_AMENDMENT_COMPLETION_2026-09-22.md` only if Local needs a separate completion review |
| reviewerOwnedClosurePaths | worker return plus a separate Local review artifact only if necessary |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/dispatcher |
| Provider or surface | private CVF workspace |
| Session or invocation | T3D-C0 Group 4 contract-coherence dispatch authoring, 2026-09-22 |
| Working directory | repository root |
| Command or tool surface | governed reads, ADIF resolver, Git status, apply_patch and governance gates |
| Target paths | this work order; later only named T2F amendment and worker return |
| Allowed scope source | T3D gap audit and standing Local dispatch authority |
| Before status evidence | HEAD e341a9021; dispatch-owned worktree clean and staging empty; exactly thirteen pre-existing untracked parked paths are isolated |
| After status evidence | bounded two-path document dispatch only; Group 4/T3E remain absent |
| Diff evidence | `git diff --name-status` before dispatcher commit |
| Approval boundary | contract-coherence documentation only |
| Claim boundary | no source, tooling, transaction, observation, consumer, live, public or deployment effect |
| Agent type | Local reviewer/dispatcher |
| Invocation ID | `acel-g1-t3d-c0-contract-coherence-dispatch-local-20260922` |
| Expected manifest | paired baseline and this work order at dispatch; worker later owns exact two outputs |
| Actual changed set | this work order pending dispatcher handling; parked paths excluded |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

Delta execution claim boundary: REQUIRED

| Field | Value |
|---|---|
| claimScope | documentation-only T2F Group 4 contract amendment and pending evidence return |
| claimDisposition | CLAIM_REJECTED: no runtime/source/consumer behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker return does not yet exist |
| actionEvidence | ACTION_EVIDENCE_PRESENT: bounded dispatch packet only |
| invocationBoundary | worker may invoke document and governance checks only |
| interceptionBoundary | no shell, filesystem, registry, account, provider or runtime interception claim |
| claimLanguage | dispatch authorizes contract clarification, not operational behavior |
| forbiddenExpansion | no credential, source, transaction, T3D-C1, T3E, provider/live, public sync or deployment without fresh authority |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON

Reason: bounded first-party contract amendment; no legacy or external absorption claim.

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/audits/CVF_ACEL_G1_T3D_GROUP4_PRE_IMPLEMENTATION_CONTRACT_GAP_AUDIT_2026-09-22.md` |
| Chain map route | N/A with reason: direct internal T2F contract amendment to INTERNAL_AGENT documentation worker |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T3D gap audit, T2F owner contract and this work order |
| Disposition | local first-party documentation only |
| Claim boundary | no external source authority, corpus, remote implementation or provider claim |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: one T2F amendment can remove all four
implementation-blocking ambiguities while leaving Group 4 and consumer binding
unestablished.

Evidence Comparison Requirement: worker return compares actual amendment text
and vectors against every frozen row.

Contradiction Handling Requirement: a contradictory source requires a
Contradiction Or Gap Disposition and claim-boundary update.

Claim Update Requirement: worker return records whether the contract claim was
confirmed, revised, narrowed, or invalidated.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private CVF owner-contract amendment and local principal references
have no public-sync authority.

## Operator Checkpoint

No operator action is required for this documentation-only T3D-C0 worker
execution. After Local accepts the amendment, a separate T3D-C1 decision must
explicitly ratify Party B's narrow response-recorder duty and the exact two
protected DACL matrices before any real Group 4 source creation. Passwords and
alternate-principal execution remain operator-only future checkpoints.

## Claim Boundary

This packet authorizes exactly two uncommitted documentation/evidence outputs.
It does not authorize Party C or Party B execution, any issuer registry or
lookup-response creation, a second observation, T3D-C1 tooling, T3E consumer
wiring, promotion, admission, provider/live work, public sync, deployment or
production behavior.
