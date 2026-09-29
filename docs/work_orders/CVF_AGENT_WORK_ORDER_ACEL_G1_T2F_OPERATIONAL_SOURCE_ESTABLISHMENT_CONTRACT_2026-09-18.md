# CVF Agent Work Order - ACEL G1 T2F Operational Source Establishment Contract

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-18

Batch ID: ACEL-G1-T2F-OPERATIONAL-SOURCE-ESTABLISHMENT-CONTRACT

dispatchBaseHead: `f0b06d023bcf45feeb1981e4d940e1aa8ed40995`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker role: one shared-workspace `INTERNAL_AGENT`

Reviewer/closer: Local orchestrator/reviewer

## Dispatch Prompt Envelope

Role: internal operational-source contract designer and evidence producer; not
a source owner, implementer, reviewer or closer.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture `git rev-parse HEAD` and full status before edits.

Current-time notes: 2026-09-18; all T2E accountable identities are appointed,
but every operational source remains uncreated and unverified.

Do-not-misread notes: this is contract design only. Proposed paths, schemas and
interfaces are not permission to create or implement them.

Required first actions: read startup/bootstrap/handoff, guard orientation,
literal gotchas, paired baseline, this order, T2E design and four appointment
records, then read applicable checker sources; verify output absence, empty
staging and 13/13 parked-path hashes.

Return contract: create only the two owned outputs, run all named gates, do not
stage or commit; return `COMPLETE_PENDING_REVIEW` only when the integrated
contract and worker evidence are coherent, otherwise `BLOCKED_WITH_REASON`.

## Purpose

Design an integrated, implementation-neutral establishment contract for the
four operational source groups required by T2E. Success means Local can later
issue source-specific implementation work orders without inventing paths,
schemas, identity/version rules, access boundaries or admission evidence.

## Authority Chain And Dependency Release Evidence

| Dependency | Evidence | Release condition | Current disposition |
|---|---|---|---|
| T2E source/owner contract | `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md`, Contracts 1-4 | design input | ACCEPT |
| Party A | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_A_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | identity and bounded responsibilities | ACCEPT |
| Party B | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_B_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | identity and observation scope | ACCEPT |
| Party C | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_C_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | identity and issuer scope | ACCEPT |
| activation approver | `docs/reviews/CVF_ACEL_G1_T2E_CONTRACT_2_ACTIVATION_APPROVER_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | distinct activation authority | ACCEPT |
| T2F readiness decision | `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_READINESS_LOCAL_DECISION_2026-09-18.md` | integrated documentation tranche selected | ACCEPT |
| GC-018 boundary | `docs/baselines/CVF_GC018_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | exact two documentation outputs | ACCEPT |
| source creation or implementation | no verified authorization | later operator/Local packet | BLOCKED_SOURCE_NOT_FOUND |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake summary | internal operational-source contract design |
| scope classification | documentation-only governance/architecture contract |
| risk sensitivity | high trust-boundary sensitivity; no operational effects |
| selected route mode | `SINGLE_AGENT_MULTI_ROLE`: one designer, independent Local review |
| role separation basis | worker cannot create sources, accept its return, stage or commit |
| escalation condition | authority contradiction, frozen drift, circular authority, output collision or forbidden effect |

## Roles, Write Ownership And Scope

Local is dispatcher and reviewer/closer. The worker owns only the two paths in
the Worker Output Inventory. Parties A/B/C and the activation approver are
contract inputs, not worker roles. Existing code, schemas, governance,
continuity, prior reviews and parked paths are read-only.

Allowed work: documentation analysis, proposed exact future paths, field and
interface contracts, lifecycle/state machines, access/separation matrix,
negative cases, validation/admission evidence and implementation-tranche
recommendations.

Forbidden work: create or modify a registry, authority specification,
approval-record source, observation log, lookup adapter, TypeScript/Python,
schema/config, checker, key/credential, live/provider/public/deployment or
continuity surface.

Risk ceiling: `P3_ELEVATED` documentation-only trust-boundary design.

## Required First Reads

Read in order:

1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, `CVF_SESSION_MEMORY.md` and `AGENT_HANDOFF_V63_2026-09-18.md`.
2. `docs/reference/guard_orientation/README.md` and `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
3. paired GC-018 baseline and this work order.
4. T2E four-owner contract plus all four appointment records named above.
5. applicable checker sources named in the Checker Source Read-Ahead Block.

Provider memory files are `NOT_CVF_SOURCE`.

## Pre-Flight Checks

Before editing, record:

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
git diff --cached --name-only
Test-Path 'docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md'
Test-Path 'docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_WORKER_RETURN_2026-09-18.md'
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected: exact committed dispatch HEAD; thirteen known untracked parked paths;
empty staging; both outputs absent; pre-implementation gate PASS. Recompute and
compare SHA-256 for all thirteen parked paths using the latest accepted T2E
worker-return ledger. Stop on any mismatch.

Mandatory remediation: repair allowed-scope artifact/gate defects and rerun the
failed gate. Escalate only when repair requires an unowned path, authority
change, source creation, implementation, secret, live/provider/public action or
destructive operation.

## Worker Output Inventory

| Path | Required at handoff | Purpose |
|---|---|---|
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Yes | integrated source inventory, exact proposed contracts, separation/admission matrix and implementation split |
| `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_WORKER_RETURN_2026-09-18.md` | Yes | no-commit trace, source mapping, frozen reconciliation and gate evidence |

## Forbidden Worker Paths

The following thirteen paths are present, untracked, exempted and read/hash-
only. Do not edit, stage, delete, rename, reformat or claim them:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts`
- `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md`
- `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json`
- `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md`
- `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_MANIFEST_2026-09-17.json`
- `docs/audits/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md`
- `docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md`
- `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_WORKER_RETURN_2026-09-17.md`
- `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_WORKER_RETURN_2026-09-17.md`
- `docs/reviews/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_WORKER_RETURN_2026-09-17.md`
- `governance/compat/check_task_class_calibration_owner_evidence.py`
- `governance/compat/test_check_task_class_calibration_owner_evidence.py`

Also forbidden: `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`,
`AGENT_HANDOFF*.md`, and every path not listed in Worker Output Inventory.

## Forbidden Filesystem State At Dispatch

| Path group | Expected state | Actual state | Action if violated |
|---|---|---|---|
| thirteen parked paths | PRESENT_EXEMPTED | PRESENT_EXEMPTED | stop on hash/status drift |
| two worker outputs | ABSENT | ABSENT | stop on pre-existing output |
| staging | EMPTY | EMPTY at committed dispatch | stop if non-empty at worker start |

## Write Ownership

Owned files are exactly the two Worker Output Inventory paths. Write mode is
create-only followed by modify-listed while completing the return. Every
other path is read-only. A gate failure never expands worker ownership.

## Source Contract Requirements

The audit must contain a Source Inventory with exactly these source groups:

1. verifier public-key registry and key-lifecycle receipts;
2. versioned verification-authority specification and independent activation-decision record;
3. tamper-evident append-only observation log covering both registries;
4. issuer registry, real lookup semantics and durable lookup-response records.

For each group define:

- one proposed exact future governed path or bounded path family;
- format/schema and required/optional fields;
- stable source identity and monotonic version/snapshot identity;
- accountable owner, write principal, allowed readers and forbidden roles;
- canonicalization, hashing or integrity rule where applicable;
- lifecycle/state transitions and immutable-history rule;
- correction, rotation, supersession and revocation behavior;
- durable decision/action/observation/lookup receipts;
- at least one named verifier consumer contract;
- validation order, failure taxonomy and fail-closed response;
- evidence required before Local may classify the source as established;
- explicit `SOURCE_NOT_CREATED` and `UNVERIFIED` disposition.

The audit must also include:

- a Cross-Source Identity And Access Matrix;
- a Source-To-Consumer Binding Matrix;
- a Version / Snapshot / Canonical Hash Matrix;
- an Establishment Evidence Checklist;
- negative cases for self-approval, writer/self-observation, issuer self-
  verification, stale/unavailable/conflicting data, in-place history rewrite,
  caller-supplied unbound hash and emergency bypass;
- a proposed implementation order with independently reviewable future
  tranches and operator checkpoints;
- a statement that no successor tranche opens automatically.

Do not choose secret material, generate example private keys, implement
schemas, create empty placeholder source files, claim final path approval or
invent runtime behavior. Proposed paths must be collision-checked and clearly
marked `PROPOSED_LOCAL_REVIEW`.

## Required Handoff Evidence

| Proof | Required literal | Required at handoff |
|---|---|---|
| all source groups remain uncreated | `SOURCE_NOT_CREATED` | Yes |
| admission posture | `UNVERIFIED` | Yes |
| proposed path posture | `PROPOSED_LOCAL_REVIEW` | Yes |
| access separation | `Cross-Source Identity And Access Matrix` | Yes |
| no automatic successor | `successorTrancheOpened: NO` | Yes |
| terminal status | `COMPLETE_PENDING_REVIEW` or honest `BLOCKED_WITH_REASON` | Yes |
| frozen integrity | `13/13` and `ZERO_MISMATCHES` | Yes |
| commit/staging posture | `WORKER_MUST_NOT_COMMIT` and `EMPTY_STAGING` | Yes |

## Execution Plan

1. Capture execution base, full status, empty staging, output absence and parked hashes.
2. Read all authority and checker sources.
3. Build a T2E-requirement-to-T2F-field reconciliation before prose drafting.
4. Select proposed paths only after collision checks; classify every match.
5. Design all four source contracts and the three cross-source matrices in one pass.
6. Audit all circular-authority and fail-closed negative cases together.
7. Define future tranche split without opening or implementing a successor.
8. Complete the worker return, run named gates, repair owned paths and rerun.
9. Recheck exact two-path delta, 13/13 hashes and empty staging; return to Local.

Stop for authority contradiction, output collision, parked drift, need to
change an unowned path, unavoidable source creation, or an unrepairable
required-gate failure outside the two owned outputs.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| four source groups and admission requirements | CURRENT_AUTHORITY | `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md` | Contracts 1-4; Source-Admission Evidence Matrix | source groups 1-4 | T2E design | ACCEPT |
| Party A owns Contracts 1+2 bounded | CURRENT_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_A_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party A Appointment Contract | Party A | operator decision | ACCEPT |
| Party B independently observes both registries | CURRENT_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_B_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party B Appointment Contract | Party B | operator decision | ACCEPT |
| Party C owns issuer authority bounded | CURRENT_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_C_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party C Appointment Contract | Party C | operator decision | ACCEPT |
| activation approver is distinct from Parties A/B/C | CURRENT_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2E_CONTRACT_2_ACTIVATION_APPROVER_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Activation Approver Appointment Contract | independent approver | operator decision | ACCEPT |
| operational sources exist | SOURCE_EXISTENCE | `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_READINESS_LOCAL_DECISION_2026-09-18.md` | Findings / Position | four source groups | Local audit | REJECT |

## Negative Search And Collision Discipline

Exact T2F decision, baseline, work-order and worker-output path checks were
false before dispatch authoring. Exact targeted query:

```
rg -n --hidden --no-ignore -i "ACEL-G1-T2F|OPERATIONAL-SOURCE-ESTABLISHMENT-CONTRACT" docs governance EXTENSIONS ECOSYSTEM CVF_SESSION -g '*.md' -g '*.json' -g '*.py' -g '*.ts'
```

Absent-versus-collision disposition: the pre-authoring query returned zero rows.
Matches in the decision, baseline and this work order are planned dispatch
collisions, not worker-output or source evidence. Same-token collision
`BLOCKED_SOURCE_NOT_FOUND` in T2E records describes the controlling absent-
source posture and is not a T2F source. `UNVERIFIED` is admission posture, not
source proof. T2C-T2E contract and role terms are accepted input collisions.

Same-token collision `T2F` occurs in this dispatch packet and planned paths;
it is a tranche identifier, not completion or source evidence. Same-token
collision `UNVERIFIED` records the fail-closed admission posture and is
non-authoritative for source existence or candidate admission.
Collision `T2F` is a tranche identifier and is non-authoritative for source existence.

The worker must record exact roots, globs, command and disposition for every
proposed future path. Existing-path collisions require a new Local decision;
the worker may not overwrite or silently adopt them.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G1-T2F-OPERATIONAL-SOURCE-ESTABLISHMENT-CONTRACT
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

providerExecutionAuthority: FORBIDDEN

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T2F-OPERATIONAL-SOURCE-ESTABLISHMENT-CONTRACT","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"DOC_CHANGE","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/audits/","docs/reviews/","docs/baselines/","docs/work_orders/","docs/reference/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/","governance/compat/"],"claims":["integrated source-establishment contract design only; sources remain uncreated"],"requiredProof":["four source contracts","three cross-source matrices","negative cases","thirteen-path reconciliation","worker-return fast gate","Local review"],"operatorCheckpoints":["future source creation","keys/credentials","implementation","live lookup","candidate admission","runtime","public sync","deployment"],"forbiddenEffects":["edit parked evidence","create source","credential access","key generation","code/schema implementation","network call","worker commit","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md","completenessClaimChanged":false}}
```

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t2d-source-owner-establishment","chainMode":"SUCCESSOR","chainOrdinal":2,"predecessor":{"path":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md","sha256":"4fd8145814348fd435ef3a478f5ba4b24c23e348877a9c77d7b6a8e1d77ca202"},"blockerDelta":{"prior":["key_registry_owner_unverified","authority_specification_owner_unverified","observation_log_owner_unverified","issuer_lookup_owner_unverified"],"resolved":["key_registry_owner_unverified","authority_specification_owner_unverified","observation_log_owner_unverified","issuer_lookup_owner_unverified"],"retained":[],"new":["key_registry_source_not_created","authority_specification_source_not_created","observation_log_source_not_created","issuer_registry_lookup_source_not_created"],"reopened":[],"current":["key_registry_source_not_created","authority_specification_source_not_created","observation_log_source_not_created","issuer_registry_lookup_source_not_created"]},"resolutionEvidence":{"key_registry_owner_unverified":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/reviews/CVF_ACEL_G1_T2E_PARTY_A_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md","sha256":"e0b5ba3c588477475c710b9702f341185d927e233062ef437392330c88f7b577","locator":"APPOINT_CVF_OPERATOR_REPOSITORY_OWNER_AS_PARTY_A_BOUNDED"},"authority_specification_owner_unverified":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/reviews/CVF_ACEL_G1_T2E_PARTY_A_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md","sha256":"e0b5ba3c588477475c710b9702f341185d927e233062ef437392330c88f7b577","locator":"APPOINT_CVF_OPERATOR_REPOSITORY_OWNER_AS_PARTY_A_BOUNDED"},"observation_log_owner_unverified":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/reviews/CVF_ACEL_G1_T2E_PARTY_B_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md","sha256":"fb5aca2352c9b4a97dc1869e743f8480962e0908a9c4b4479c4e151c27058bc0","locator":"APPOINT_DEDICATED_SEPARATE_AUDIT_IDENTITY_AS_PARTY_B_BOUNDED"},"issuer_lookup_owner_unverified":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/reviews/CVF_ACEL_G1_T2E_PARTY_C_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md","sha256":"345fb6578e2b527167899b1aeeb822fa2d34e60588f161ce95646ad88559108e","locator":"APPOINT_DEDICATED_ISSUER_GOVERNANCE_IDENTITY_AS_PARTY_C_BOUNDED"}},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":2},"claims":[{"claimId":"ACEL-G1-T2F-SOURCE-CONTRACT-DESIGN","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_READINESS_LOCAL_DECISION_2026-09-18.md"}],"requiredDisposition":"STOP_REASSESS_ARCHITECTURE","successorScope":"INTEGRATED_ROOT_CONTRACT"}
```

T2E resolved accountable identities only. T2F retains all operational-source
blockers and may define contracts without claiming source establishment.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | exact two T2F documentation outputs | design/return only; no source creation, acceptance or commit | baseline and appointed-authority inputs | no runtime adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no selected adapter owner | no external ingress, auth, mutation or public claim | scope exclusion | separately deferred | `DEFERRED_WITH_REASON` |

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | decision, baseline, work order | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | dispatch packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact two outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| source_reconciliation | WORKER_RETURN | worker | IMPLEMENTATION | exact two outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| frozen_input_integrity | WORKER_RETURN | worker | IMPLEMENTATION | read-only thirteen-path ledger | NO_MUTATION | closer | MATERIAL_COMMIT | source_reconciliation |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact two outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | frozen_input_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact two outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted outputs and Local review | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local completion review | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Worker Autonomy / No-Question Rule

Repair routine content, literal, structure and gate defects inside the two
owned outputs without asking the operator. Missing implementation authority is
an expected boundary, not a question and not permission to create a source.
Stop only for an authority contradiction, output collision, parked drift,
forbidden effect or required repair outside ownership.

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| actor | INTERNAL_AGENT worker |
| role set | source-contract designer and evidence author; not source owner, reviewer or closer |
| delegation depth | zero; no nested agent |
| evidence basis | exact governed sources; provider memory is `NOT_CVF_SOURCE` |
| gate sequence | source/frozen reconciliation; worker-return fast; Local review |
| self-review boundary | worker repairs owned documents but cannot accept them |
| role separation ledger | worker returns pending; Local reviews/commits; operator controls later source creation |
| escalation condition | authority conflict, output collision, frozen drift or forbidden effect |

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| route | `SINGLE_AGENT_MULTI_ROLE`: one internal designer and independent Local reviewer |
| rolePattern | worker designer; Local reviewer/closer; later operator source-creation checkpoint |
| phase | dispatch -> contract design -> Local review -> separate continuity |
| baseHeadFor(phase) | dispatchBaseHead=`f0b06d023bcf45feeb1981e4d940e1aa8ed40995`; worker captures executionBaseHead |
| closureBaseHead | unset; Local records after accepted return |
| changedSetScope(phase) | exact two worker output paths only |
| traceScope(phase, actor) | source reads, collisions, frozen hashes, commands and start/end status |
| commitOwner(phase) | Local only |
| crossBatchIsolation | thirteen parked paths remain byte-identical and uncommitted |
| nextMoveSurfaces | Local updates active continuity only after disposition |

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT source-contract designer after dispatch

laneOwnedPaths: exact two Worker Output Inventory paths

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return, empty staging, exact two-path delta and 13/13 frozen reconciliation

## Foundation Storage Layout Block

N/A with reason: this tranche designs future source/storage contracts but does
not create durable storage, directories, registries or runtime layouts.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_COMPLETION_2026-09-18.md`; Local-owned and created only if required |
| reviewerOwnedClosurePaths | returned outputs, Local disposition and separate continuity |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_WORKER_RETURN_2026-09-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Decision / Disposition; Source Inventory;
Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution
Claim Boundary Control Block; External Knowledge Intake Routing; Epistemic
Process Block; Public Export Disposition; Claim Boundary; Return-Time
Closeability Recheck; git status; No-Commit Statement. Conditional sections
must use explicit N/A with reason.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
git diff --cached --name-only
```

## Evidence Requirements

Return exact T2E-requirement-to-T2F-field mapping; proposed-path collision
ledger; all source/matrix/negative-case results; future-tranche split; 13/13
hashes with zero mismatch; empty staging; exact two-path worker delta; zero
external/provider/live calls; and final command results after the last edit.
Do not claim complete-repository coverage, source existence or implementation
readiness beyond the designed contract.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class DOC_CHANGE --role dispatcher --lifecycle-phase pre-dispatch`

Returned defects: NONE_RETURNED

Returned defect count: 0

Dispatch impact: no matched ADIF entry; normal fail-closed controls remain.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind held-dependency --batch-id ACEL-G1-T2F-OPERATIONAL-SOURCE-ESTABLISHMENT-CONTRACT --title "ACEL G1 T2F Operational Source Establishment Contract" --date 2026-09-18 --base f0b06d023bcf45feeb1981e4d940e1aa8ed40995 --commit-mode WORKER_MUST_NOT_COMMIT --dependency ACEL-G1-T2E-ALL-AUTHORITIES-APPOINTED --stdout` |
| generatedProfile | held-dependency and no-commit worker profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | populated exact source groups, matrices, negative cases, manifests and authority boundaries |
| checkerReadAheadConfirmation | dispatch, structure, closeability and review-cost checker sources read |
| docOnlyNewFields | source identity, proposed path, format/schema, access, lifecycle, receipt, binding and tranche split |
| claimBoundary | scaffold guides packet shape only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | envelope placement and fields; Source Verification schema; closeability graph phases; convergence scalars; internal-only routing; trace labels |
| gateRunPurpose | confirmation of dispatch shape before release, not source discovery or implementation proof |
| claimBoundary | checker PASS cannot create or approve an operational source |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | `internal governed input (no external intake)` |
| Chain map route | accepted T2E design/appointments -> Local readiness -> T2F work order -> internal worker return -> Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and paired Local decision |
| Internal source | `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md` |
| Disposition | `NOT_APPLICABLE_INTERNAL_ONLY_WITH_REASON`: no external source is admitted |
| Claim boundary | internal inputs do not prove source existence or implementation |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: one integrated contract will expose coherent
source identities, access boundaries and evidence gates while keeping all
sources uncreated.

Evidence Comparison Requirement: compare every T2E admission requirement and
appointment restriction to an explicit T2F contract field or negative case.

Contradiction Handling Requirement: record contradictions with a
Contradiction Or Gap Disposition and return blocked rather than inventing a
source or authority.

Claim Update Requirement: distinguish confirmed contract design, revised
proposal and unresolved implementation evidence for every source group.

## Verification And Release Gate

Local must verify exact path isolation, paired-artifact consistency, output
absence, 13/13 frozen hashes, pre-dispatch PASS and exact staging. Worker begins
only from the committed work order and synchronized handoff. Machine PASS is
not source establishment.

## Acceptance Criteria

- [ ] Exactly four source groups are defined and every row says `SOURCE_NOT_CREATED`.
- [ ] Proposed paths are exact or honestly bounded, collision-checked and marked `PROPOSED_LOCAL_REVIEW`.
- [ ] Every group defines schema/fields, identity/version, access, lifecycle, evidence, consumer, failure behavior and establishment proof.
- [ ] Cross-source access, consumer-binding and version/hash matrices reconcile all T2E restrictions.
- [ ] Negative cases reject all circular authority and fail-open behavior.
- [ ] Future implementation order uses independently reviewable tranches and `successorTrancheOpened: NO`.
- [ ] Only two worker paths change; parked hashes match; staging remains empty.
- [ ] All named commands pass or return is honestly blocked.

Fail conditions: created source or placeholder implementation; invented
authority; unclassified path collision; circular authority admitted; parked
drift; unowned mutation; provider/live/public/deployment effect; false source
or candidate-admission claim.

## Review Gate

Local reviews contract/schema/path/authority/consumer/lifecycle/negative-case/
test/range/commit-plan completeness as one consolidated matrix. Reviewer-fast
and pre-commit follow only after bounded acceptance. Worker return is not
closure and does not authorize the proposed paths.

## Closure Checklist

- [ ] Full source-contract and cross-source matrix review completed.
- [ ] Worker-return fast and reviewer-fast evidence valid for their phases.
- [ ] No source or runtime claim exceeds evidence.
- [ ] Material and continuity commits remain split.
- [ ] No successor implementation tranche opens automatically.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for authority contradiction, output collision,
parked drift, unresolvable proposed-path collision, source creation needed to
complete the design, forbidden effect, missing required evidence or any out-
of-scope gate failure.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher |
| Provider or surface | private CVF workspace |
| Session or invocation | T2F packet authoring, 2026-09-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, resolver, path/token checks, scaffold preview, apply_patch and gates |
| Target paths | Local readiness decision, paired baseline and this work order |
| Allowed scope source | completed T2E appointments and active T2F readiness next move |
| Before status evidence | tracked worktree clean at HEAD `f0b06d023`; thirteen parked untracked paths explicitly exempted; five planned paths absent; staging empty |
| After status evidence | exact three dispatch paths pending; worker outputs absent |
| Diff evidence | exact dispatch packet plus unchanged parked context |
| Approval boundary | documentation-only source-establishment contract design |
| Claim boundary | no source, key, credential, implementation, live/runtime/public effect |
| Agent type | Local dispatch author |
| Invocation ID | `acel-g1-t2f-source-contract-dispatch-20260918` |
| Expected manifest | Local decision, paired baseline and work order |
| Actual changed set | Local readiness decision, paired baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | integrated operational-source establishment contract design |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no runtime or source receipt is claimed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: dispatch documentation only |
| invocationBoundary | internal shared-workspace documentation task |
| interceptionBoundary | no IDE, provider, CLI/MCP or runtime interception claim |
| claimLanguage | source-contract design is not source creation or implementation |
| forbiddenExpansion | keys, credentials, source/schema/code creation, live lookup, admission, runtime, public sync, deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source-contract dispatch with no public authorization.

## Operator Checkpoint

After Local accepts the returned T2F design, the operator must separately
authorize the selected source-specific implementation tranche and any concrete
principal, key or credential action. No implementation successor opens from
the worker return alone.

## Claim Boundary

This work order authorizes exactly two documentation outputs. It does not
create or approve implementation of any registry, specification, approval
record, observation log, lookup, schema/code, key, credential, candidate
admission, runtime, provider, public-sync or deployment behavior.
