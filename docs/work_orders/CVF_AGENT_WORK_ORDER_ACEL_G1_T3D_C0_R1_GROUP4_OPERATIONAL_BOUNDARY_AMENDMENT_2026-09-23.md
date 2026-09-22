# CVF Agent Work Order - ACEL G1 T3D-C0-R1 Group 4 Operational Boundary Amendment

Memory class: governed-work-order

Status: DISPATCH_READY

docType: work-order

Date: 2026-09-23

Batch ID: ACEL-G1-T3D-C0-R1-GROUP4-OPERATIONAL-BOUNDARY-AMENDMENT

Dispatch base HEAD: `47a20fe89857a15b046df9679ae19bd205c0db1d`

dispatchBaseHead: `47a20fe89857a15b046df9679ae19bd205c0db1d`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `NOT_EXECUTED_YET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local orchestrator/reviewer.

## Dispatch Prompt Envelope

Role: `INTERNAL_AGENT` contract worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`.

Current-time notes: C1 is accepted at material parent `dbce8d074`; the two
Group 4 sources are absent; the readiness audit blocks real C2 execution.

Do-not-misread notes: this is contract prose only. Do not edit code, checker,
test, launcher, source, session or handoff paths; do not use credentials,
`runas`, elevation, Party B/C execution, provider/live calls or network.

Required first actions: read startup surfaces, guards, the baseline/order and
all named sources/checkers; capture HEAD/status/staging, parked hashes and
forbidden-path state; run the pre-implementation gate before edits.

Return contract: modify exactly T2F plus the named worker return, complete the
bounded gates, leave staging empty, do not commit, and return only
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`; independent probe stays
`PENDING_REVIEWER_EXECUTION`.

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - contract-only documentation amendment; no target transaction, DACL mutation, durable write or executable tooling change is authorized.

## Purpose

Amend the existing T2F Group 4 contract so later tooling and source creation
cannot invent parent-directory authority, reuse test-vector identity as a real
source, or bypass the required Party B issuer observation.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake summary | bounded documentation amendment to the existing Group 4 owner contract |
| scope classification | named-file contract correction with no executable or external effect |
| active role | INTERNAL_AGENT contract worker |
| phase | C0-R1 documentation amendment |
| decision owner | Local orchestrator/reviewer |
| risk sensitivity | Windows parent-directory authority and cross-principal source integrity |
| implementation authority | FORBIDDEN |
| real-source authority | FORBIDDEN |
| selected route mode | `SINGLE_AGENT_MULTI_ROLE`: one contract worker and a separate Local reviewer |
| escalation condition | authority contradiction, third output, parked drift, or need for code/source/credential action |

## Authority Chain

| Authority | Source | Binding |
|---|---|---|
| current route | `docs/audits/CVF_ACEL_G1_T3D_C2_SOURCE_CREATION_READINESS_GAP_AUDIT_2026-09-23.md` | C2 blocked; C0-R1 selected |
| contract owner | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | amend this owner in place |
| accepted tooling boundary | `docs/reviews/CVF_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_COMPLETION_2026-09-22.md` | C1 remains accepted; source absent |
| dispatch baseline | `docs/baselines/CVF_GC018_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md` | exact contract obligations |
| current continuity | `AGENT_HANDOFF_V63_2026-09-18.md` | Local audit/select authority; no real execution |

## Agent Roles

| Role | Responsibility | Boundary |
|---|---|---|
| operator | owns later credential and real-principal checkpoints | no action in this work order |
| worker | amend two documentation paths only | must not commit |
| Local reviewer/closer | semantic review, independent probe, repair if bounded, commit/continuity | final decision owner |
| external reviewer | none | no external dispatch |

## Scope / Target / Owner Boundary

This is a documentation-only repair of one accepted owner contract. It does
not authorize implementation of the design it specifies. The future runtime
principals remain Party C SID ending `-1010`, Party B SID ending `-1009`, and
Local SID ending `-1001`; mentioning them is contract data, not authorization
to invoke them.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T3D-C0-R1-GROUP4-OPERATIONAL-BOUNDARY-AMENDMENT","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"DOC_CHANGE","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/","docs/audits/","docs/baselines/","docs/reference/","docs/reviews/","docs/work_orders/","governance/compat/"],"claims":["existing T2F contract gains parent-directory, fresh-input and issuer-observation operational boundary; no executable or source effect"],"requiredProof":["one controlling amendment","exact two-path worker delta","thirteen parked hashes","worker-return fast gate","Local independent review"],"operatorCheckpoints":["C0-R1 Local acceptance","C1-R2 tooling dispatch","real-token isolation proof","Party C registry creation","Party B issuer observation","response-log initialization","T3E"],"forbiddenEffects":["code or checker change","credential access","alternate-principal execution","operating-system security mutation","source creation","lookup","worker commit","provider/live/network","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"N/A with reason: bounded named files only","completenessClaimChanged":false}}
```

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchSurface: INTERNAL_AGENT

parentAssignmentId: ACEL-G1-T3D-C0-R1-GROUP4-OPERATIONAL-BOUNDARY-AMENDMENT

dispatchKind: REWORK

reviewRoundCount: 1

rootCauseClusterId: T3D-C2-OPERATIONAL-BOUNDARY

priorFindingSetDigest: `sha256:pending-dispatch-artifact-finalization`

cumulativeExternalInvocationCount: 0

externalInvocationCeiling: 0

newIndependentCriticalEvidence: YES - Local read-only probes identified the
shared-parent delete/replace boundary and missing issuer-observation route.

One consolidated worker return is allowed. No drip rework or automatic
successor is authorized. Reviewer checks at M5/M10/safety/M20 only and consumes
valid returned evidence without recreating implementation.

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "acel-g1-t3d-c0-r1-operational-boundary-problem",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},
  "resolutionEvidence": {},
  "counters": {"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},
  "claims": [{"claimId":"ACEL-G1-T3D-C0-R1-CONTRACT-DISPATCH","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md"}],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

The full finding class is frozen here: parent directory and reservation,
fresh operational identity/time/content, issuer-observation order, real-token
adversarial proof, and strict C0/C1/C2/T3E lifecycle ceilings. A worker finding
outside this class returns `BLOCKED_WITH_REASON` without widening scope.

## Independent Review Probe Admission Contract

The worker records `independentProbeDisposition: PENDING_REVIEWER_EXECUTION`.
Local independently verifies the final contract against T2F, C1 code behavior
and Windows rights semantics. Worker self-review or model difference is not an
independent actor.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority/risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | shared-workspace two-path contract worker | no credentials, code, source or commit | this order and pending return | no runtime adapter | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | none | out-of-band invocation has no authority | explicit exclusion | separate source-verified adapter order required | `DEFERRED_WITH_REASON` |

## Single-Agent Multi-Role Control Block

| Field | Value |
|---|---|
| implementation role | worker, contract prose only |
| review role | Local reviewer after return |
| independence | reviewer execution is separate; same-thread/model changes alone do not prove independence |
| handoff | worker returns pending; no self-closure |
| evidence basis | governed repository sources only; provider memory and credentials are not authority |
| gate sequence | bounded document checks, worker-return fast gate, Local reviewer-fast, reviewer commit gates |
| self-review boundary | worker cannot accept, stage, commit or open the successor |
| role separation ledger | worker authors the amendment/return; Local evaluates and closes |
| escalation condition | third output, authority conflict, parked drift, executable/source need or credential action |

## Dependency Release Evidence

| Dependency | Evidence | State |
|---|---|---|
| T3D-C1 tooling | accepted completion at material parent `dbce8d074` | ACCEPT |
| T3D-C2 readiness | blocking audit dated 2026-09-23 | ACCEPT |
| T2F contract owner | existing governed audit path | ACCEPT |
| implementation correction | requires later accepted C0-R1 | PARKED |
| real source and T3E | separate operator/Local checkpoints | PARKED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3D-C0-R1-GROUP4-OPERATIONAL-BOUNDARY-AMENDMENT --title "ACEL G1 T3D-C0-R1 Group 4 Operational Boundary Amendment" --date 2026-09-23 --base 47a20fe89857a15b046df9679ae19bd205c0db1d --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | generic contract-only worker dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | populated exact sources, two-path ownership, contract decisions and bounded verification |
| checkerReadAheadConfirmation | dispatch-quality, closeability, handoff, convergence, high-risk applicability and public-export checker sources reviewed |
| docOnlyNewFields | parent-directory reservation, fresh operational input and issuer-observation ordering clauses |
| claimBoundary | dispatch artifact only |

## Required Artifact Manifest

| Path | Owner | Required state |
|---|---|---|
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | worker | modified in place with one controlling C0-R1 amendment |
| `docs/reviews/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_WORKER_RETURN_2026-09-23.md` | worker | new pending-review return |

## Work-Order Fulfillment Manifest

The exact worker manifest is the two paths above. No alternate return, copy,
fixture, script, test, launcher, source, receipt or side-channel artifact is
permitted.

## Forbidden Path Manifest

| Path family | Reason |
|---|---|
| `scripts/` | C1-R2 implementation not authorized |
| `governance/compat/` | checker/test change not authorized |
| `governance/sources/issuer_registry/` | real Group 4 source forbidden |
| `governance/sources/registry_observation_log/` | second observation forbidden |
| `CVF_SESSION/` and `AGENT_HANDOFF_V63_2026-09-18.md` | reviewer/closer continuity only |
| thirteen parked paths below | unrelated operator-owned evidence |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `governance/sources/issuer_registry/REGISTRY.json` | ABSENT | ABSENT | stop; return to orchestrator |
| `governance/sources/issuer_registry/LOOKUP_RESPONSES.jsonl` | ABSENT | ABSENT | stop; return to orchestrator |
| unresolved P4-C1 safety marker | ABSENT | ABSENT | stop; adjudicate before worker dispatch |

## Pre-Existing Dirty Path Exemptions

The worker must preserve these untracked paths byte-identically and never
stage them:

| Path | SHA-256 |
|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts` | `5c26e2bc732da98082ed3b0c1ed4c35fdcb40c5c5b16023e281ea6a3a741a37f` |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts` | `24302b66728de7de3173b4fcb999034412ef4a47c8c27f5e17fbf581352b8046` |
| `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md` | `02b97f0db77b6518000c13aff30bc131b88b426809f9f8aa43c89bad2b5ebbda` |
| `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json` | `0bf99eeaf3e8a979000ffc411639a987abf60d1d5ff556dad38ba354b24f137e` |
| `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md` | `5147bf905113e4c750f6b7f4aa84e1aeb4575417299258ad10dcf8ebbbb5575a` |
| `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_MANIFEST_2026-09-17.json` | `5bfe577495bac91b99344827172d859ff0389cf1f67e14097d5af113a16eaeb9` |
| `docs/audits/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md` | `97510bff2a40e4868625d1f016e87d2bbaab9812380ded5a20c2f24b65625708` |
| `docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md` | `3ddb27af5abf0d8197bfdaa28eac2e7b83c422c3342a4b3acb2abf25b65cdb86` |
| `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_WORKER_RETURN_2026-09-17.md` | `f12688934bcb1ef0fdaaea1ae45186cce14cfcba69fc5061334abbee8e8462f6` |
| `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_WORKER_RETURN_2026-09-17.md` | `25963195262048746436daee2ab4b2304fa96d54c8197ed375ab98e5e7dd29ce` |
| `docs/reviews/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_WORKER_RETURN_2026-09-17.md` | `1ac61b304063f57eda3f7db2a8ec3681a0af3d6c8e58ec04c3d5228e7f759594` |
| `governance/compat/check_task_class_calibration_owner_evidence.py` | `761eefa1f093e4cdddb4e73496b04f9694a15622a5ce34dd685d4acae3498d0f` |
| `governance/compat/test_check_task_class_calibration_owner_evidence.py` | `ac85ed1b6ad5288c95aeada7baab45782c58f97bbdfd45cb4a126ea6a124eeec` |

## Planned Worker Proof Matrix

| Proof | Required evidence |
|---|---|
| contract ownership | one controlling amendment inside T2F, no second owner |
| completeness | parent/reservation, fresh input, lifecycle order and actual-token probes all present |
| non-execution | no code/source/credential/elevation action |
| exact delta | only two worker paths pending; index empty |
| parked integrity | 13/13 hashes match before and after |
| return integrity | exact return bytes hash stable around final required gate |

## Required First Reads

1. `AGENTS.md` and active continuity front doors.
2. `docs/reference/guard_orientation/README.md` and literal-format gotchas.
3. The baseline and this work order.
4. The readiness audit, T2F Group 4 amendment, C1 completion, and all three
   accepted writers/checkers named by the readiness audit.
5. Applicable checker sources before authoring the return.

## Pre-Flight Checks

- capture full `git rev-parse HEAD` as execution base;
- capture `git status --short --untracked-files=all` and empty staged diff;
- recompute all parked hashes;
- confirm both Group 4 source paths remain absent;
- confirm no unresolved P4-C1 safety marker exists;
- stop on contradiction before editing.

## Write Ownership

Allowed paths are exactly the two entries in Required Artifact Manifest.
Forbidden paths are every other repository path. Worker commit permission is
`FORBIDDEN`. Rollback boundary is only the worker's uncommitted two-path delta.

## Reference Contract Amendment Requirements

Add a controlling T3D-C0-R1 subsection to T2F that:

1. freezes the complete protected parent-directory security candidate and
   labels it `FEASIBLE_WITH_REQUIRED_WINDOWS_PROOF`;
2. reserves both exact target names as zero-byte placeholders with their final
   owner/file DACL before either principal may publish;
3. forbids directory `CreateDirectories`, `DeleteChild`, `Delete`, `WriteDac`
   and `WriteOwner` for Party B/C, and defines exact allowed rights;
4. requires C1-R2 target-reservation claim semantics, identity/security drift
   rejection, same-directory pre-hardened temp use and publication-owned
   rollback;
5. keeps the accepted positive vector hermetic-only and requires fresh global
   snapshot identity/current timestamps for operational input;
6. requires a dedicated Party B `issuer_registry` observation production path
   without weakening Group 3 immutable-chain semantics;
7. fixes the ordered lifecycle and status ceilings stated in the baseline;
8. enumerates actual-token positive and cross-principal adversarial probes;
9. states the fallback: if shared-directory rights proof fails, stop for a
   separately reviewed path-layout or privileged-mediator amendment.

Do not change the existing accepted file-level hashes/vectors except to mark
their hermetic versus operational roles unambiguously.

## Worker Autonomy / No-Question Rule

Resolve editorial details within this contract. Stop only for a source
contradiction, parked drift, need for a third output, implementation/source
action, or an authority decision outside the frozen alternatives.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: N/A with reason: neither allowed worker
path is `AGENTS.md`, a checker, hook, guard registry or generated session file.

Protected paths: none.

Operator authorization: bounded contract repair follows the Local-selected
readiness audit.

Rollback boundary: only the uncommitted two-path worker delta.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | self-declared return marker, Responds to work order, return headings, executionBaseHead, exact changed paths, independent probe disposition, learning and epistemic labels, trace labels and private export token |
| gateRunPurpose | confirm final packet shape after source-read authoring; not discover required literals |
| claimBoundary | contract-only evidence |

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION

priorVerificationArtifact: `docs/reviews/CVF_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_COMPLETION_2026-09-22.md`

priorVerificationAnchor: material parent `dbce8d074`

freshRecomputeRequired: T2F final SHA-256, return SHA-256, exact delta, staged
state and 13/13 parked hashes.

unicodePathHandling: use literal repository-relative paths and UTF-8-safe
readers; do not shell-reconstruct paths containing spaces.

extractedTextAuthority: direct filesystem reads of the named governed files.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| C2 execution is blocked and C0-R1 selected | `docs/audits/CVF_ACEL_G1_T3D_C2_SOURCE_CREATION_READINESS_GAP_AUDIT_2026-09-23.md` | Findings / Position; Selected Route | `BLOCKED_T3D_C2_DISPATCH` | Local readiness decision | REVIEWED_DECISION | ACCEPT |
| Group 4 exact paths, rows, file DACLs and lifecycle are the accepted base being enriched | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 4; G4-GAP-01 through G4-GAP-04 | Group 4 contract | T2F owner | CONTRACT_INVARIANT | ACCEPT |
| accepted C1 source ceiling and hashes | `docs/reviews/CVF_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_COMPLETION_2026-09-22.md` | Decision / Disposition; Final Evidence | `TOOLING_ACCEPTED_SOURCE_NOT_CREATED` | C1 closure | REVIEWED_EVIDENCE | ACCEPT |
| current Group 3 writer excludes issuer registry | `scripts/acel_g1_party_b_group3_observation_writer.ps1` | real-mode description and constants | `InputRelativePath`; `RegistryName` | Group 3 writer | EXECUTABLE_FACT | ACCEPT |

## Negative Search And Collision Discipline

Use `rg --files --hidden --no-ignore` only as bounded collision support. Do not
claim corpus completeness. Reject any third worker output, alternate contract
owner, source path creation, or duplicate active work order.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | C0-R1 baseline and order | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | three dispatch artifacts | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact two worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | canonical worker return | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact two worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | canonical return and T2F | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| final_return_hash | REVIEW | worker | WORKER_RETURN | canonical return | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | returned two paths | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | final_return_hash |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted two paths | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split material and continuity ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Local dispatcher/reviewer; one bounded contract worker; Local independent probe executor; Local closer/session-sync steward |
| phase | DISPATCH_TO_WORKER_RETURN |
| baseHeadFor(phase) | dispatchBaseHead=`47a20fe89857a15b046df9679ae19bd205c0db1d`; executionBaseHead=worker capture; closureBaseHead=reviewer set |
| changedSetScope(phase) | exact two worker paths |
| traceScope(phase, actor) | each actor records invocation, paths, commands, result and boundary |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; Local closer only |
| crossBatchIsolation | clean governed worktree except thirteen enumerated parked paths; all non-manifest paths remain read-only and unstaged |
| nextMoveSurfaces | worker return to Local; no successor opens automatically |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: one shared-workspace INTERNAL_AGENT worker after committed dispatch and continuity

laneOwnedPaths: exactly two paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: terminal worker return, exact manifest reconciliation, empty staging and 13/13 parked hashes

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_WORKER_RETURN_2026-09-23.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

evidenceReadinessContract: NOT_APPLICABLE_WITH_REASON: bounded named-file contract amendment has no discovery-audit manifest

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must self-declare `Self-declared worker-return artifact: yes`
and `Responds to work order:` with this exact path. Required section names are:
Purpose, Target / Source, Scope / Methodology, Findings / Position, Risk /
Corrective Action, Claim Boundary, Checker Source Read-Ahead Block, Agent
Operation Trace Block, Delta Execution Claim Boundary Control Block, Public
Export Disposition, git status --short, Changed Files, Command Evidence,
No-Commit Statement, Return-Time Closeability Recheck, Rescan Intelligence
Hardening, External Knowledge Intake Routing, Epistemic Process Block, and
Finding-To-Governance Learning Disposition. Conditional sections may use an
explicit reasoned N/A. Record actual pending paths honestly.

## Execution Plan

1. Capture preflight evidence and read sources/checkers.
2. Amend T2F once with the consolidated controlling subsection.
3. Create and finalize the worker return.
4. Run bounded checks, recompute hashes/status/staging and parked ledger.
5. Capture return SHA-256 before and after the final required fast gate; they
   must match and no post-gate mutation is permitted.
6. Return pending review; do not commit or open C1-R2.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | one existing canonical operational-source contract and one bounded worker return |
| Storage decision | amend the existing T2F contract in place; create only the exact return path named by this order |
| Existing aggregate impact | none; no index, registry aggregate or generated state is changed |
| Generated state impact | none |
| Durable governance boundary | no new reference-family owner, source directory, registry row, receipt or runtime artifact is created |
| Duplicate-owner control | the T2F contract remains the sole owner; the worker must not create a parallel Group 4 contract |

## Evidence Requirements

- exact final two-path name-status and hashes;
- execution base and empty index;
- 13/13 parked reconciliation;
- source paths absent and no credential/principal action;
- one locator matrix mapping each readiness gap to T2F clauses and future
  adversarial proofs;
- stable detached return digest around the final fast gate;
- independent probe pending for Local.

## Acceptance Criteria

- [ ] one existing T2F owner is amended; no duplicate owner is created;
- [ ] all parent/reservation rights and forbidden rights are explicit;
- [ ] the shared-directory design is conditional on real Windows proof;
- [ ] fixture and operational identity/time semantics are unambiguous;
- [ ] issuer observation is ordered before C2 closure and T3E;
- [ ] implementation/source actions remain forbidden;
- [ ] exactly two worker paths, empty staging, 13/13 parked hashes;
- [ ] worker-return fast gate is compliant and return hash is stable;
- [ ] independent probe disposition remains pending reviewer execution.

## Verification Commands

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
git diff --name-status
git diff --cached --name-only
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_high_risk_local_transaction_proof.py --base 47a20fe89857a15b046df9679ae19bd205c0db1d --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD --json
```

The worker must not run commands that mutate governed source, accounts, ACLs,
credentials, provider state, public repositories or deployments.

## Review Gate

Local evaluates returned evidence without recreating implementation. Local
runs reviewer-fast, checks the whole contract class, and issues one consolidated
finding set. Review does not imply source or runtime acceptance.

## Pre-Dispatch Gate Disposition

| Field | Value |
|---|---|
| phase | pre-dispatch |
| command | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 47a20fe89857a15b046df9679ae19bd205c0db1d --head HEAD` |
| result | BOUNDED_ACTIVE_PACKET_PASS_AGGREGATE_REJECTED_BY_PARKED_HISTORY |
| active packet evidence | all 82 applicable non-history checks passed, including dispatch quality, prompt envelope, closeability, semantic convergence, storage layout and scaffold provenance |
| aggregate rejection | `independent review probe admission` rejected exactly three pre-existing untracked T2/T2A/T2B worker returns whose referenced historical work orders predate the required `independentProbeRequired` declaration |
| ownership boundary | those three returns and their owner work orders are among the 13 parked paths; this order neither owns nor authorizes their repair |
| scope | three dispatcher artifacts only; parked paths excluded and preserved byte-identical |

## Closure Checklist

- [ ] worker return reviewed semantically;
- [ ] independent Local probe completed;
- [ ] reviewer-fast and applicable commit gates pass;
- [ ] material commit contains accepted contract/return/closure only;
- [ ] continuity is updated separately;
- [ ] C1-R2 remains closed until explicit dispatch.

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_COMPLETION_2026-09-23.md` if a distinct reviewer artifact is needed

reviewerOwnedClosurePaths: accepted two worker paths plus optional completion review; continuity remains separate

| Field | Value |
|---|---|
| workerDisposition | COMPLETE_PENDING_REVIEW |
| acceptedDisposition | CONTRACT_ACCEPTED_BOUNDED_SOURCE_NOT_CREATED |
| workerCommitPermission | FORBIDDEN |
| reviewerRepairBoundary | same two worker paths only for minor defects |
| successorAuthority | none automatic |

## Machine Closure Package

On acceptance, Local closes this work order, writes a reviewer-owned completion
if required, commits material artifacts, then updates source continuity and
generated session state in a separate bounded commit. No source registry row
or runtime receipt is part of C0-R1 closure.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF Local dispatch author |
| Provider or surface | local private provenance workspace with read-only internal probes |
| Session or invocation | ACEL G1 T3D-C0-R1 dispatch authoring, 2026-09-23 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, sub-agent audit, `apply_patch`, governance gates and Git |
| Target paths | this work order, paired baseline and readiness audit |
| Allowed scope source | active handoff next move and Local-selected readiness route |
| Before status evidence | HEAD `47a20fe89857a15b046df9679ae19bd205c0db1d`; governed worktree clean; thirteen enumerated parked paths present and excluded; Group 4 sources absent |
| After status evidence | contract-only two-path worker dispatch authored; no worker execution |
| Diff evidence | exact three-path dispatch batch before commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no worker execution, credential, operating-system security effect, source, provider/live, public or deployment action |
| Agent type | Local orchestrator/dispatcher |
| Invocation ID | `acel-g1-t3d-c0-r1-dispatch-20260923` |
| Expected manifest | readiness audit; baseline; this work order |
| Actual changed set | readiness audit; baseline; this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | documentation-only amendment to existing T2F owner |
| claimDisposition | N/A with reason: documentation contract only; no Delta execution claim |
| receiptEvidence | N/A with reason: no runtime receipt is created |
| actionEvidence | N/A with reason: no Delta action is authorized |
| invocationBoundary | local filesystem reads and document gates |
| interceptionBoundary | no shell/account/ACL/provider interception claim |
| claimLanguage | contract amendment, not implementation or source creation |
| forbiddenExpansion | code, checker, launcher, credential, principal execution, source, lookup, T3E, admission, provider/live, public or deployment |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/audits/CVF_ACEL_G1_T3D_C2_SOURCE_CREATION_READINESS_GAP_AUDIT_2026-09-23.md` |
| Chain map route | N/A with reason: direct Local-to-internal contract route |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired C0-R1 baseline and this work order |
| Disposition | local first-party documentation only |
| Claim boundary | no remote research, external corpus, CLI/MCP adapter or provider claim |

## External/Local Coordination Binding

Role: `INTERNAL_AGENT`; phase: contract worker; decision owner: Local. No
external advisory or CLI/MCP lane is used.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Epistemic Process Block

### Expected Result / Prediction

One amendment to the existing owner can close all readiness gaps without
executable or source effects.

### Evidence Comparison

The readiness audit identifies one coherent dependency class and the baseline
provides a feasible-but-unproven shared-directory candidate plus fallback.

### Contradiction Or Gap Disposition

Any infeasible Windows-rights result is retained as a blocker for a later
path-layout/mediator decision; the worker may not assert runtime proof.

### Claim Update

Dispatch is documentation-only and does not advance T3D beyond tooling
accepted/source not created.

## Finding-To-Governance Learning Disposition

Defect class: `ORCHESTRATOR_PACKET_GAP`.

Learning lane: `GOVERNANCE_CONTROL_PLANE`.

Disposition: `DESIGN_REVIEW_REQUIRED`.

Next action: Local review of C0-R1 before separately dispatching C1-R2.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private machine-specific operational security contract; public sync is
not authorized.

## Claim Boundary

This work order authorizes only a two-path documentation return. It does not
implement or execute the directory model, change a writer/checker/test,
create a launcher/source/observation/response, use a credential, run as Party
B/C, perform a lookup, open T3E, promote/admit, call a provider, export
publicly, deploy, stage or commit.

## Operator Checkpoint

No operator action is required for C0-R1. Later real-token proof, credentials
and source creation require a separately reviewed packet and explicit operator
execution.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with the exact two paths, empty staging,
stable final return hash, compliant worker-return gate, 13/13 parked hashes and
`PENDING_REVIEWER_EXECUTION`. Return `BLOCKED_WITH_REASON` for any authority
conflict, third output, parked drift, implementation/source need or unresolved
contract contradiction.
