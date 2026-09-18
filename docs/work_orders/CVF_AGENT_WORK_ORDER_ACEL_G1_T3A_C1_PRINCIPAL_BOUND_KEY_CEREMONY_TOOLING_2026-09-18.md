# CVF Agent Work Order - ACEL G1 T3A-C1 Principal-Bound Key Ceremony Tooling

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-18

Batch ID: ACEL-G1-T3A-C1-PRINCIPAL-BOUND-KEY-CEREMONY-TOOLING

Dispatch base HEAD: `40f6a8b514dcd507723cd919561656fecf87b126`

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

Worker role: one shared-workspace `INTERNAL_AGENT`

Reviewer/closer: Local orchestrator/reviewer

Worker return path: `docs/reviews/CVF_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_WORKER_RETURN_2026-09-18.md`

## Dispatch Prompt Envelope

Role: internal security-tooling worker. Build a fail-closed ceremony utility
and hermetic tests; do not perform the Party A ceremony.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_2026-09-18.md`

Paired baseline: `docs/baselines/CVF_GC018_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_2026-09-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture committed HEAD, full status and staging before edits.

Current-time notes: Local verified `cvf-g1-party-a`, SID
`S-1-5-21-1644666849-912006174-747199667-1006`, enabled, password required,
non-admin, expiring 2026-10-18. This fact authorizes tooling assumptions only.

Do-not-misread notes: never request the account password, use run-as, log on as
Party A, open its profile, read the existing DELL-user test key, create a real
key, create Group 1 files, stage, commit, or claim source readiness.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, this order, paired baseline, T2F Group 1, T3A route audit and every
checker listed below. Freeze the thirteen parked paths before writing.

Return contract: satisfy C1-01 through C1-10, run required gates, leave staging
empty, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Create reviewable, deterministic tooling for a later operator-run Ed25519 key
ceremony bound to an exact Windows principal without exposing private bytes.

## Authority Chain And Dependency Release Evidence

| Dependency | Evidence | Release condition | Disposition |
|---|---|---|---|
| operator choice | operator approved a separate local account and continuation | tooling only | ACCEPT |
| principal preflight | Local Windows checks recorded in paired baseline | exact name/SID, enabled, password-required, non-admin | ACCEPT |
| Group 1 contract | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md`, Source Group 1 | preserve public row/lifecycle boundaries | ACCEPT |
| new-key route | `docs/audits/CVF_ACEL_G1_T3A_KEY_CEREMONY_ROUTE_READINESS_2026-09-18.md`, Decision / Disposition | fresh Ed25519, private material outside repo | ACCEPT |
| actual ceremony | no Party A logon/custody proof yet | Local accepts tooling, then operator invokes separately | PARKED_OPERATOR_EXECUTION |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake summary | principal-bound Windows key-ceremony tooling |
| scope classification | bounded code plus hermetic test and evidence return |
| risk sensitivity | secret-adjacent; actual secret generation forbidden |
| selected route mode | `SINGLE_AGENT_MULTI_ROLE`: one no-commit worker then Local review |
| role separation basis | worker cannot use Party A credentials, run ceremony, accept or commit output |
| escalation condition | any need for credentials, account mutation, real Party A execution, extra output, source creation or parked drift |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL

dispatchSurface: INTERNAL_AGENT

parentAssignmentId: ACEL-G1-T3A-C1-PRINCIPAL-BOUND-KEY-CEREMONY-TOOLING

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

## Acceptance Matrix

| ID | Required contract | Positive and negative proof |
|---|---|---|
| C1-01 | Wrapper requires exact expected account name and SID and compares both to current process identity before key generation | hermetic current-user PASS; wrong-name and wrong-SID reject before helper invocation |
| C1-02 | Wrapper rejects elevated/Administrator context and an expired or disabled expected account | mocked/inspection negative cases; no local-account mutation |
| C1-03 | Output directory must resolve outside repository and under current user's LocalAppData; reparse traversal and existing target files reject | temp positive plus repo-path, traversal and collision negatives |
| C1-04 | JavaScript helper uses Node core crypto to generate Ed25519 and returns PKCS8 DER plus raw 32-byte public key through captured process output only | format/length and sign/verify self-test; no stdout logging of helper payload |
| C1-05 | Wrapper protects private PKCS8 immediately with Windows DPAPI CurrentUser, writes only encrypted blob, then clears references best-effort | decrypt/reconstruct/sign/verify in self-test; no plaintext private file |
| C1-06 | Public metadata contains schema/profile, principal name/SID, algorithm, key ID, public key base64url, public SHA-256, creation/expiry, test/ceremony disposition; never private material | schema assertions and secret-pattern negative scan |
| C1-07 | Writes use exclusive-create and failure cleanup; partial files cannot be mistaken for successful ceremony | collision and injected-failure tests |
| C1-08 | Default execution is dry-run/self-test; real ceremony requires explicit `-ExecuteCeremony`, exact principal checks and an interactive confirmation | default produces no durable output; noninteractive execute rejects |
| C1-09 | Worker never invokes real ceremony or Party A context and does not access any existing local test key | trace, command ledger and output hashes |
| C1-10 | Exact three worker outputs, empty staging and thirteen parked paths unchanged | before/after status, hashes and manifest reconciliation |

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `scripts/acel_g1_party_a_key_ceremony.ps1` | CREATE fail-closed wrapper with embedded hermetic self-test mode |
| `scripts/acel_g1_party_a_key_ceremony.js` | CREATE minimal Node Ed25519 generator/helper; never logs private payload independently |
| `docs/reviews/CVF_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_WORKER_RETURN_2026-09-18.md` | CREATE full evidence return |

## Work-Order Fulfillment Manifest

The Required Artifact Manifest is the exact worker output set. No fourth file,
account/profile mutation, generated registry, lifecycle log, deletion, rename,
continuity edit, staging or commit is allowed.

## Write Ownership

Worker owns uncommitted edits to the exact three planned paths. Local owns
review, minor evidence repair, staging and commits. All existing files and the
thirteen parked untracked paths are read-only.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | exact tooling paths and return | hermetic current-user test only, no Party A credentials or real ceremony | this committed packet | shared-workspace tooling | `TOOLING_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | none | no ingress, authentication, approval, secret, raw-data or mutation interface | no external invocation | adapter not opened | `DEFERRED_WITH_REASON` |

## Agent Roles

| Role | Responsibility |
|---|---|
| operator | owns Party A password and later interactive ceremony checkpoint |
| Local dispatcher | commits packet and keeps secret boundary explicit |
| INTERNAL_AGENT worker | implements exact tooling and hermetic tests without credentials or commit |
| Local reviewer/closer | reviews security invariants and decides material acceptance |
| session-sync steward | updates continuity only after Local disposition |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| actor | one shared-workspace INTERNAL_AGENT worker |
| role set | PowerShell/JavaScript tooling implementer and evidence author, not reviewer/closer |
| delegation depth | zero |
| evidence basis | governed sources and Local platform preflight, never provider memory |
| gate sequence | pre-implementation, hermetic focused tests, worker-return fast, Local review |
| self-review boundary | worker cannot accept, stage or commit its own output |
| role separation ledger | worker returns pending; Local decides and commits |
| escalation condition | credential, Party A execution, source creation, fourth output or parked drift |

## Required First Reads

1. Startup/front-door/active handoff, guard orientation and literal gotchas.
2. This order, paired baseline, T2F Group 1 and T3A route audit.
3. Applicable checker sources and current Node/PowerShell platform behavior.

## Pre-Flight Checks

- Capture execution HEAD, full status, empty staging and parked hashes.
- Confirm paired dispatch commit exists and three outputs do not.
- Confirm no Party A credential is present in environment or requested.
- Run pre-implementation autorun gate before editing.

## Worker Autonomy / No-Question Rule

Repair all allowed-scope implementation and gate defects directly. Stop only
for credentials, actual alternate-user execution, account mutation, source
creation, a fourth output, parked drift or an irreparable authority conflict.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Group 1 row/lifecycle contract | ACCEPTED_CONTRACT | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 1 | `publicKeyBytesBase64`; `keyId`; `LIFECYCLE_LOG.jsonl` | Group 1 contract | ACCEPT |
| principal/ceremony dependency | ACCEPTED_ORDER | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Proposed Implementation Order | Future T3A | source-establishment order | ACCEPT |
| private-key custody route | ACCEPTED_ROUTE | `docs/audits/CVF_ACEL_G1_T3A_KEY_CEREMONY_ROUTE_READINESS_2026-09-18.md` | Decision / Disposition | new Ed25519 key | T3A route | ACCEPT |
| old DELL-user key is test-only | CURRENT_BOUNDARY | `docs/audits/CVF_ACEL_G1_T3A_KEY_CEREMONY_ROUTE_READINESS_2026-09-18.md` | Post-Decision Local Test Custody Evidence | `TEST_ONLY_NON_OPERATIONAL` | Local evidence | ACCEPT |

## Negative Search And Collision Discipline

Before authoring, literal probes returned false for all paired packet and
worker-output paths. A bounded exact batch-ID search found no predecessor.
The worker must repeat exact output probes and stop on any collision.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T3A-C1-PRINCIPAL-BOUND-KEY-CEREMONY-TOOLING","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"CREDENTIAL_REFERENCE","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["scripts/","docs/reviews/","docs/baselines/CVF_GC018_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_2026-09-18.md","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts","docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md","docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json","docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md","docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_MANIFEST_2026-09-17.json","docs/audits/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md","docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md","governance/compat/check_task_class_calibration_owner_evidence.py","governance/compat/test_check_task_class_calibration_owner_evidence.py"],"claims":["principal-bound ceremony tooling and hermetic tests only"],"requiredProof":["C1-01 through C1-10","exact three-path delta","parked hashes","worker-return fast gate"],"operatorCheckpoints":["actual Party A ceremony","key promotion","source creation"],"forbiddenEffects":["credential access","alternate-user execution","real key generation","account mutation","registry creation","worker commit","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"N/A with reason: bounded named files","completenessClaimChanged":false}}
```

Expected route: `P3_ELEVATED`; shadow routing only. Full legacy gates apply.
The parked exact paths appear only because the route checker reconciles the
whole dirty workspace. They remain excluded from worker ownership and mutation;
the authoritative worker lane is the three-path `laneOwnedPaths` declaration.

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3a-c1-principal-bound-key-ceremony-tooling","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":["real_party_a_ceremony_not_executed","group1_source_not_created"],"resolved":[],"retained":["real_party_a_ceremony_not_executed","group1_source_not_created"],"new":["ceremony_tooling_not_implemented"],"reopened":[],"current":["ceremony_tooling_not_implemented","real_party_a_ceremony_not_executed","group1_source_not_created"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T3A-C1-TOOLING-DISPATCH","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/baselines/CVF_GC018_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_2026-09-18.md"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"NO_SUCCESSOR"}
```

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired T3A-C1 packet | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired T3A-C1 packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact three worker outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return ADIF disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact three worker outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact three outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | returned three paths | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `SINGLE_AGENT_MULTI_ROLE`: one INTERNAL_AGENT worker, then Local reviewer |
| rolePattern | Local dispatcher -> no-commit worker -> Local reviewer/closer |
| phase | T3A-C1 ceremony tooling, actual ceremony excluded |
| baseHeadFor(phase) | dispatchBaseHead=`40f6a8b514dcd507723cd919561656fecf87b126`; executionBaseHead captured by worker; closureBaseHead set by Local |
| changedSetScope(phase) | exact three planned paths |
| traceScope(phase, actor) | reads, commands, hermetic tests, hashes, status and cleanup |
| commitOwner(phase) | Local only; worker forbidden to stage or commit |
| crossBatchIsolation | thirteen parked paths byte-identical |
| nextMoveSurfaces | Local review, then separate operator ceremony checkpoint |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT T3A-C1 tooling worker after dispatch

laneOwnedPaths: `scripts/acel_g1_party_a_key_ceremony.ps1`; `scripts/acel_g1_party_a_key_ceremony.js`; `docs/reviews/CVF_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_WORKER_RETURN_2026-09-18.md`

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return, empty staging, exact three-path delta and parked reconciliation

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/audits/CVF_ACEL_G1_T3A_KEY_CEREMONY_ROUTE_READINESS_2026-09-18.md`

priorVerificationAnchor: `279902d8edad08213d8eb40012ea8e12f1f19564`

freshRecomputeRequired: exact principal guards, DPAPI roundtrip, Ed25519 sign/verify and cleanup

unicodePathHandling: use literal PowerShell paths and UTF-8 JSON; do not assume ASCII workspace roots

extractedTextAuthority: source files and command results only; screenshots and provider memory are not authority

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_WORKER_RETURN_2026-09-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Decision / Disposition; Review-Dispatch
Convergence Control; Semantic Convergence Outcome; Source Inventory; Checker
Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim
Boundary Control Block; External Knowledge Intake Routing; Rescan Intelligence
Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance
Learning Disposition; Epistemic Process Block; Public Export Disposition;
Claim Boundary; Return-Time Closeability Recheck; Frozen-Path Reconciliation;
git status; Changed Files; Command Evidence; Worker Experience Retrospective;
No-Commit Statement.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
pwsh -NoProfile -File scripts/acel_g1_party_a_key_ceremony.ps1 -SelfTest
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
```

The self-test must use the current worker identity and a disposable directory,
must never target `cvf-g1-party-a`, and must clean all temporary key material.

## Execution Plan

1. Freeze execution state and read output-specific checker shapes.
2. Implement the JavaScript generator with no standalone logging path.
3. Implement PowerShell identity, path, confirmation, DPAPI and atomicity gates.
4. Run hermetic positive/negative self-tests under the current worker user.
5. Create return, run gates, reconcile outputs and parked hashes.

## Evidence Requirements

Return C1-01 through C1-10 with command/result evidence, exact output hashes,
negative cases, temporary-path cleanup proof, empty staging and full status.
Never include credentials, DPAPI plaintext, private DER/base64, signature seed,
or an unredacted captured helper payload.

## Acceptance Criteria

All C1 rows pass; default invocation is non-mutating; execution fails before
key generation for wrong identity/SID, elevated context, unsafe path or
collision. Hermetic DPAPI/signature roundtrip passes without durable plaintext.
Exactly three outputs change and worker never stages or commits.

## Review Gate

Local reads both scripts, audits ordering and cleanup, consumes valid returned
evidence and independently runs bounded negative probes. Local will not run the
real Party A ceremony during worker review.

## Closure Checklist

- [ ] C1-01 through C1-10 reviewed.
- [ ] Exact three paths and parked hashes reconcile.
- [ ] Worker-return fast and reviewer preflight pass.
- [ ] No secret or alternate-user execution occurred.
- [ ] Material and continuity commits remain separate.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for any credential need, alternate-user execution,
account mutation, source creation, fourth output, parked drift or mandatory
gate failure. Otherwise return `COMPLETE_PENDING_REVIEW`, never ceremony or
source readiness.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_COMPLETION_2026-09-18.md` (optional; prefer Local disposition inside the worker return) |
| reviewerOwnedClosurePaths | exact three returned paths plus necessary Local evidence repair |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3A-C1-PRINCIPAL-BOUND-KEY-CEREMONY-TOOLING --title "ACEL G1 T3A-C1 Principal-Bound Key Ceremony Tooling" --date 2026-09-18 --base 40f6a8b514dcd507723cd919561656fecf87b126 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | generic worker dispatch; internal INITIAL; no-commit |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact principal, secret boundary, three outputs and C1 matrix |
| checkerReadAheadConfirmation | dispatch, convergence, closeability, structural and worker-return checker sources |
| docOnlyNewFields | no operational schema field; tool metadata remains pre-source |
| claimBoundary | scaffold use does not prove custody or execute ceremony |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | INITIAL round zero; Source Verification columns; closeability phases; full return profile; trace and export fields |
| gateRunPurpose | confirm packet before dispatch |
| claimBoundary | gate PASS cannot establish a Party A key or source |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class CODE_CHANGE --role dispatcher --lifecycle-phase pre-dispatch`

Returned defects: NONE_RETURNED

Returned defect count: 0

Dispatch impact: no matched entry; C1 security matrix remains binding.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Chain map route | operator authorization plus Local Windows verification -> INTERNAL_AGENT tooling -> Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and paired baseline |
| Internal source | `docs/audits/CVF_ACEL_G1_T3A_KEY_CEREMONY_ROUTE_READINESS_2026-09-18.md` |
| Disposition | `NOT_APPLICABLE_INTERNAL_ONLY_WITH_REASON`: no external source admitted |
| Claim boundary | Local remains final private-CVF technical decision owner |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Legacy Absorption Coverage Index Disposition

`NOT_APPLICABLE_WITH_REASON`

Reason: bounded first-party Windows tooling; no legacy or external corpus intake.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/dispatcher |
| Provider or surface | private CVF workspace |
| Session or invocation | T3A-C1 tooling dispatch, 2026-09-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, Windows principal checks, Node self-test, scaffold/read-ahead, apply_patch and gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | operator account authorization and Local verified principal state |
| Before status evidence | HEAD `40f6a8b51`; tracked worktree clean; staging empty; thirteen pre-existing parked untracked paths isolated |
| After status evidence | exact paired dispatch paths pending before commit |
| Diff evidence | paired packet staged alone before dispatch commit |
| Approval boundary | tooling and hermetic tests only |
| Claim boundary | no credential, real ceremony, registry, live/runtime/public effect |
| Agent type | Local dispatcher and later reviewer/closer |
| Invocation ID | `acel-g1-t3a-c1-tooling-dispatch-20260918` |
| Expected manifest | paired T3A-C1 baseline and work order |
| Actual changed set | reconciled before dispatch commit |
| Manifest delta | pending exact staging reconciliation |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | principal-bound ceremony tooling dispatch |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no real ceremony receipt exists |
| actionEvidence | ACTION_EVIDENCE_PRESENT: paired dispatch only |
| invocationBoundary | shared-workspace tooling task under current worker user |
| interceptionBoundary | no credential, run-as, account, provider or runtime interception |
| claimLanguage | dispatch-ready tooling, not ceremony-ready source |
| forbiddenExpansion | real key, alternate-user execution, registry, admission, provider, public sync or deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private principal-bound ceremony tooling; no public-sync approval.

## Operator Checkpoint

The operator created the separate local principal. Actual login and ceremony,
public-key promotion, source creation and any key lifecycle transition remain
separate checkpoints after Local accepts the tooling.

## Claim Boundary

This order authorizes exactly two tooling files and one evidence return. It
does not authorize credentials, running as Party A, generating its real key,
creating registry/lifecycle files, signing receipts, verifier integration,
candidate admission, live/provider use, public sync or deployment.
