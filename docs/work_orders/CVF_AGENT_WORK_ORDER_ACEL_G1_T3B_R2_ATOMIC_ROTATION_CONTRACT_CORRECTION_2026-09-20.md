# CVF Agent Work Order - ACEL G1 T3B R2 Atomic Rotation Contract Correction

Memory class: governed-work-order

docType: work_order

Status: CLOSED_PASS_BOUNDED

Batch ID: ACEL-G1-T3B-R2-ATOMIC-ROTATION-CONTRACT-CORRECTION

Dispatch date: 2026-09-20

Dispatch base head: `12d2d0d7437db746e4c4c038cf88eb881e03c23d`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker role: shared-workspace `INTERNAL_AGENT`

Reviewer/closer: Local orchestrator/reviewer

successorTrancheOpened: NO

providerExecutionAuthority: FORBIDDEN

## Quick Start

Read this work order, its paired baseline, the R1 completion review, the T2F
contract and all five owned paths. Capture HEAD/status/staging before edits.
Change exactly the five-path manifest below. Use hermetic fixtures only. Do not
use credentials, `runas`, alternate principals or real Group 2 paths. Do not
stage or commit. Return `COMPLETE_PENDING_REVIEW` only after all focused suites
and the worker-return fast gate pass; otherwise return `BLOCKED_WITH_REASON`.

## Purpose

Replace the contradictory two-active supersession prerequisite with a durable
atomic rotation event and align the controlling contract, decision writer,
checker, tests and worker return. Preserve accepted R1 ACL and per-version hash
behavior. This tranche creates no operational source.

## Scope / Target / Owner Boundary

Role: `INTERNAL_AGENT` correction worker. Phase: hermetic R2 contract and
tooling correction. Decision owner: Local orchestrator/reviewer. External
research is closed and not applicable.

The worker owns only the exact five paths below. The spec writer is accepted
partial R1 evidence and must remain byte-identical. Local owns this work order,
baseline, R1 review, independent probe, commit and session sync. Operator owns
credentials and any later real principal execution.

Escalate only for a contradiction outside the selected atomic model, a needed
sixth path, credential/alternate-user/real-source need, parked drift, or an
irreparable mandatory gate outside the owned paths.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| operator role instruction | operator authorized Local audit, selection and worker dispatch | ACCEPT |
| R1 rejection | `docs/reviews/CVF_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_COMPLETION_2026-09-20.md`; exact hash recorded in convergence evidence | ACCEPT |
| paired R2 baseline | `docs/baselines/CVF_GC018_ACEL_G1_T3B_R2_ATOMIC_ROTATION_CONTRACT_CORRECTION_2026-09-20.md` | ACCEPT |
| controlling source contract | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | ACCEPT_FOR_CORRECTION |

## Intake Role Routing Decision

Route mode: `MULTI_AGENT_MULTI_ROLE` in one shared workspace. Worker owns only
the five-path correction and hermetic evidence. Local owns architecture,
independent review and commit. External research is not applicable.

Intake summary: Local-reviewed internal contract correction reuses accepted R1
evidence; no external intake, principal execution or real source is admitted.

Escalation condition: stop only for a source contradiction, forbidden sixth
path, credential/alternate-user/real-source need, parked drift or irreparable
mandatory gate outside the five owned paths.

Risk sensitivity: HIGH because the transition establishes future authority
activation semantics, but external effect remains NONE in this hermetic tranche.

Scope classification: bounded root-contract and local tooling correction.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T3B-R2-ATOMIC-ROTATION-CONTRACT-CORRECTION","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"MODIFIES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/audits/","docs/reviews/","scripts/","governance/compat/"],"claims":["corrected atomic Group 2 rotation contract and hermetic tooling only; no real source"],"requiredProof":["durable old-and-replacement binding","atomic one-active replay","negative rotation mutations","worker-return fast gate","independent Local probe"],"operatorCheckpoints":["Party A spec creation","Approver decision writes","Local source verification","T3E consumer wiring","candidate admission"],"forbiddenEffects":["credential access","alternate-user execution","real source creation","parked-path mutation","worker commit","provider/live/public/deployment","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/reviews/CVF_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_COMPLETION_2026-09-20.md","completenessClaimChanged":false}}
```

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ACEL-G1-T3B-R2-ATOMIC-ROTATION-CONTRACT-CORRECTION --title "ACEL G1 T3B R2 Atomic Rotation Contract Correction" --date 2026-09-20 --base 12d2d0d74 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 2 --root-cause-cluster-id acel-g1-t3b-group2-atomic-rotation --prior-finding-set-digest 64475b405e5f7886f2f9faecf6f50be13c95c8c7a6e5c1cd97260219630fe62e --new-independent-critical-evidence UNREACHABLE_SUPERSESSION_STATE_AND_UNBOUND_REPLACEMENT --scec-problem-key acel-g1-t3b-group2-source-creation-tooling-problem --scec-chain-mode SUCCESSOR --scec-chain-ordinal 4 --scec-predecessor-path docs/reviews/CVF_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_COMPLETION_2026-09-20.md --scec-predecessor-sha256 64475b405e5f7886f2f9faecf6f50be13c95c8c7a6e5c1cd97260219630fe62e --scec-required-disposition STOP_REASSESS_ARCHITECTURE --scec-successor-scope INTEGRATED_ROOT_CONTRACT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | protected-governance-path plus no-commit rework profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | selected atomic rotation semantics, exact five-path manifest and durable replacement mutation probes |
| checkerReadAheadConfirmation | dispatch-quality, core-guard, gate-to-role, return, scaffold and trace checker sources read |
| docOnlyNewFields | none |
| claimBoundary | dispatch only; no real source or runtime effect |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK

dispatchSurface: INTERNAL_AGENT

parentAssignmentId: ACEL-G1-T3B-R2-ATOMIC-ROTATION-CONTRACT-CORRECTION

reviewRoundCount: 2

rootCauseClusterId: acel-g1-t3b-group2-atomic-rotation

priorFindingSetDigest: 64475b405e5f7886f2f9faecf6f50be13c95c8c7a6e5c1cd97260219630fe62e

dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR

reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS

newIndependentCriticalEvidence: UNREACHABLE_SUPERSESSION_STATE_AND_UNBOUND_REPLACEMENT

regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT

cumulativeExternalInvocationCount: 0

externalInvocationCeiling: 0

externalInvocationDelta: 0

usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT

quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT

nextDispatchDisposition: ONE_CONSOLIDATED_REWORK

reworkGeneration: 2

consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION

preExecutionReviewTrigger: NONE

nextRoutineReviewBoundary: WORKER_RETURN

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

escalationDisposition: ROOT_CONTRACT_CORRECTION_SELECTED

claimBoundary: no external invocation and no real principal/source execution

## Semantic Convergence Control

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3b-group2-source-creation-tooling-problem","chainMode":"SUCCESSOR","chainOrdinal":4,"predecessor":{"path":"docs/reviews/CVF_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_COMPLETION_2026-09-20.md","sha256":"64475b405e5f7886f2f9faecf6f50be13c95c8c7a6e5c1cd97260219630fe62e"},"blockerDelta":{"prior":["acel_g1_group2_real_source_not_created","group2-tooling-r1-not-accepted","unreachable-supersession-state","unbound-durable-replacement","supersession-entry-gap"],"resolved":["group2-tooling-r1-not-accepted"],"retained":["acel_g1_group2_real_source_not_created","unreachable-supersession-state","unbound-durable-replacement","supersession-entry-gap"],"new":["group2-tooling-r2-not-accepted"],"reopened":[],"current":["acel_g1_group2_real_source_not_created","unreachable-supersession-state","unbound-durable-replacement","supersession-entry-gap","group2-tooling-r2-not-accepted"]},"resolutionEvidence":{"group2-tooling-r1-not-accepted":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/reviews/CVF_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_COMPLETION_2026-09-20.md","sha256":"64475b405e5f7886f2f9faecf6f50be13c95c8c7a6e5c1cd97260219630fe62e","locator":"Decision / Disposition"}},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":2,"nonDecreasingBlockerTransitions":2},"claims":[{"claimId":"ACEL-G1-T3B-R2-ATOMIC-ROTATION","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/baselines/CVF_GC018_ACEL_G1_T3B_R2_ATOMIC_ROTATION_CONTRACT_CORRECTION_2026-09-20.md"}],"requiredDisposition":"STOP_REASSESS_ARCHITECTURE","successorScope":"INTEGRATED_ROOT_CONTRACT"}
```

## Dependency Release Evidence

| Dependency | Evidence | Release rule | Disposition |
|---|---|---|---|
| R1 contradiction | named completion review and independent probe | repair both findings together | RELEASED_FOR_ROOT_CONTRACT_REWORK |
| ACL and per-version fixes | passing focused suites plus source inspection | preserve | RELEASED_FOR_REUSE |
| schema migration | real Group 2 files absent | no migration needed | NOT_APPLICABLE_WITH_REASON |
| real author/approver action | separate operator checkpoint after acceptance | forbidden now | PARKED_OPERATOR_EXECUTION |

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeOwner: Local orchestrator/reviewer

independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION

independentProbeRiskClass: NEW_INDEPENDENT_CRITICAL_RISK

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: Local selects named post-return state/digest probes and interprets their results independently of worker prose

expectedInformationGain: prove one-event sole-active convergence, durable replacement binding and PowerShell/Python agreement

rerunCostReason: three focused methods only because they answer the admitted critical state-machine question without broad duplicate execution

reviewerDecisionOwner: LOCAL

decisionQuestion: Does one durable `SUPERSEDED` event cryptographically bind
both versions and move the active set from exactly `{old}` to exactly
`{replacement}` without any intermediate conflict?

positiveControl: Local constructs distinct v1/v2 specs and replays
APPROVED(v1), ACTIVATED(v1), APPROVED(v2), atomic SUPERSEDED(v1->v2).

negativeMutationClasses: null/missing replacement fields; equal/lower or
unapproved replacement; wrong replacement hash; missing replacement file;
standalone activation while old active; event-digest mutation.

repeatBoundary: run only after worker final evidence; no broad duplicate suite
unless the returned proof is contradictory or ambiguous.

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | MODIFY; repair the closed event schema and atomic lifecycle semantics |
| `scripts/acel_g1_approver_group2_decision_writer.ps1` | MODIFY; build, validate and append atomic rotation events |
| `governance/compat/check_acel_g1_verification_authority_spec.py` | MODIFY; replay atomic rotation and verify both durable hashes |
| `governance/compat/test_check_acel_g1_verification_authority_spec.py` | MODIFY; add discriminating positive and negative atomic-rotation cases |
| `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-20.md` | MODIFY; report R2 evidence and exact pending-review disposition |

Exactly these five paths may change. Do not change the spec writer, R1 review,
R2 baseline/work order, session files, real source paths or 13 parked paths.

## Work-Order Fulfillment Manifest

The five rows above are the complete R2 changed set. Worker reconciliation must
show all five and no sixth path. Existing uncommitted files are predecessor
input, not accepted authority.

## Atomic Rotation Contract

### Closed event schema

Add `replacementSpecVersion` and `replacementRecomputedHashHex` to the required
closed preimage and durable record. Both fields are present on every event:

- for `APPROVED`, `REJECTED`, and `ACTIVATED`: both values are JSON `null`;
- for `SUPERSEDED`: `replacementSpecVersion` is a positive integer strictly
  greater than `specVersion`; `replacementRecomputedHashHex` is the exact
  independently recomputed raw-content hash of that replacement's own file.

Reject one-null/one-non-null pairs, extra fields, omitted fields, noncanonical
values and any digest computed without the two fields.

### Replay semantics

1. `APPROVED(v)` records approval only.
2. Ordinary `ACTIVATED(v)` requires prior approval and an empty active set.
3. `SUPERSEDED(old,replacement)` requires exactly `{old}` active; old was
   approved/activated and not superseded; replacement is strictly greater,
   approved, inactive, not rejected, not previously activated/superseded, and
   both spec files/hashes validate independently.
4. Apply the rotation atomically in one event: remove old, add replacement.
   Never materialize a two-active intermediate state.
5. Mark replacement as activated-by-rotation so later duplicate activation is
   rejected and later rotation from that replacement is legal.
6. Full-history replay must finish with zero or one active version and must
   derive the same state in PowerShell and Python.

No latest/largest inference is permitted. The caller must name the old and
replacement versions explicitly; the durable record must retain both.

### Compatibility boundary

There is no operational Group 2 source. Do not implement legacy-event
autodetection, schema union, fallback or migration. All hermetic fixtures must
use the corrected closed schema.

## Allowed Scope / Forbidden Scope

Allowed: edit the five paths; use disposable temporary fixtures; inspect OS
facts read-only; run focused and governance gates; remove own fixtures.

Forbidden: passwords, credential stores, `runas`, alternate-user execution,
real `governance/sources/verification_authority_spec/` writes, spec-writer
mutation, parked paths, staging, commit, provider/live/runtime/public/deploy,
consumer wiring, promotion or admission.

## Write Ownership

Worker owns only the five-path manifest. Local owns review, bounded reviewer
repair, commit and session sync. Operator owns all secrets and real principal
checkpoints.

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | owns passwords and later real Party A/Approver invocations |
| Dispatcher | selects atomic rotation and fixes the exact manifest |
| Worker | corrects five paths and returns hermetic evidence without commit |
| Local reviewer/closer | executes independent probes, accepts/rejects, commits and synchronizes session |

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
2. `CVF_SESSION_MEMORY.md` and the active handoff.
3. `docs/reference/guard_orientation/README.md`.
4. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
5. paired R2 baseline, this work order and R1 completion review.
6. controlling T2F contract and all five owned paths in full.
7. checker sources named in the read-ahead block.

## Pre-Flight Checks

1. Capture exact HEAD and full status; require staging empty.
2. Confirm the exact five owned paths, frozen spec-writer hash, 13 parked paths and both absent real-source paths.
3. Run the pre-implementation gate from Verification Commands.
4. Stop before any sixth path, credential or real-principal need.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| unreachable and unbound R1 supersession | independent finding | `docs/reviews/CVF_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_COMPLETION_2026-09-20.md` | Findings / Position; Independent Probe Evidence | T3B-R1-RV-1/2 | Local reviewer | ACCEPT |
| current closed schema and lifecycle contradiction | contract invariant | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 2; Explicit Approval, Activation And Supersession | `cvf.specDecisionEvent` | Group 2 contract | ACCEPT |
| accepted partial ACL/per-version evidence | worker evidence | `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-20.md` | Findings / Position; Command Evidence | R1 corrections | worker return | ACCEPT |
| no operational Group 2 source | local state | `docs/audits/CVF_ACEL_G1_T3B_GROUP2_SOURCE_READINESS_ROUTE_2026-09-20.md` | Findings / Position | Group 2 route | Local audit | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION

priorVerificationArtifact: `docs/reviews/CVF_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_COMPLETION_2026-09-20.md`

priorVerificationAnchor: SHA-256 `64475b405e5f7886f2f9faecf6f50be13c95c8c7a6e5c1cd97260219630fe62e`

freshRecomputeRequired: atomic event preimage, two spec hashes, transition state and all changed focused tests

unicodePathHandling: use literal repository-relative paths and UTF-8-safe readers; never reconstruct the workspace path from lossy output

extractedTextAuthority: direct local file reads are authoritative; screenshots and terminal summaries are contextual only

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_independent_review_probe_admission.py` |
| literalTokensReviewed | dispatch fields, Source Verification columns, protected-path list, convergence controls, exact worker-return status and trace fields |
| gateRunPurpose | confirmation after authored contract, not first discovery |
| claimBoundary | structural dispatch evidence only; not implementation acceptance |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: modify only the R2 checker and focused
test named below to implement the selected atomic rotation contract.

Protected paths:

- `governance/compat/check_acel_g1_verification_authority_spec.py`
- `governance/compat/test_check_acel_g1_verification_authority_spec.py`
- `governance/compat/check_task_class_calibration_owner_evidence.py`
- `governance/compat/test_check_task_class_calibration_owner_evidence.py`

The final two paths are pre-existing parked evidence listed only for changed-set
accounting; mutation, staging and commitment remain forbidden.

Operator authorization: standing instruction that Local audit, select the
architecture and issue work orders; Local selected the atomic correction after
independent evidence showed the R1 contract impossible.

Rollback boundary: revert only the five R2 worker paths if rejected; preserve
committed R1 dispatch/review artifacts, Group 1 source and all parked files.

Not authorized: hook wiring, unrelated checker semantics, credentials, real
source creation, principal execution, consumer/runtime/provider/live/public or
deployment behavior.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`.

Returned defects: NONE_RETURNED. The controlling findings are the named Local
R1 completion review, not an inferred registry entry.

## Worker Autonomy / No-Question Rule

Repair routine failures inside the five owned paths without operator
interruption. Return only for a genuine source contradiction, sixth-path need,
credential/alternate-principal/real-source requirement, parked drift or an
irreparable gate failure outside scope.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing T2F contract, decision writer, checker/test and return |
| Storage decision | no new durable path or runtime store |
| Existing aggregate impact | none |
| Generated state impact | none |
| Durable governance boundary | corrected proposed schema before first real source |

## Execution Plan

1. Freeze HEAD/status/staging, exact five owned paths, spec-writer hash, parked
   hashes and real-source absence.
2. Repair T2F closed schema and lifecycle prose first.
3. Update PowerShell event/preimage builders and replay to one atomic rotation.
4. Update Python schema validation and replay identically.
5. Replace the non-discriminating R1 supersession positive with the exact
   atomic sequence and add every listed negative.
6. Update the existing return to R2, run final commands once, reconcile exact
   paths and leave staging empty.

## Evidence Requirements

Record exact commands, exit codes and counts for decision-writer self-test,
Python compile/tests, worker-return fast gate, real-source absence, frozen
spec-writer hash, parked-path reconciliation and empty staging. Include one
table mapping each R2 requirement to a failing-before/passing-after regression.

## Acceptance Criteria

- Exactly five R2 paths change; spec writer and all parked paths remain byte-identical.
- Event closed schema durably binds old and replacement versions and hashes.
- Exact v1-to-v2 atomic sequence passes and finishes with v2 as the sole active version.
- Replacement mutation classes fail closed with specific taxonomy IDs.
- Ordinary activation while another version is active remains rejected.
- PowerShell and Python replay semantics agree.
- Accepted ACL and per-version binding regressions remain green.
- Worker return binds to R2, reports exact `COMPLETE_PENDING_REVIEW`, and has `independentProbeDisposition: PENDING_REVIEWER_EXECUTION`.
- Focused tests and worker-return fast gate pass; staging is empty; real source paths remain absent.

Fail conditions: any sixth path, legacy fallback, caller-controlled path,
latest/largest inference, two-active intermediate state, replacement citation
not stored in the event digest, real principal/source action, staging/commit or
failed owned-lane final gate.

## Closure Checklist

- [x] Exact five R2 paths and frozen spec writer reconcile; 13 parked paths unchanged.
- [x] Atomic rotation positive and every named mutation negative pass in PowerShell and Python.
- [x] Worker-return fast gate passes and staging is empty.
- [x] Both real Group 2 source paths remain absent.
- [x] Material closure and continuity synchronization remain separate commits.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` only for a source contradiction, sixth-path,
credential/alternate-user/real-source requirement, parked drift or irreparable
out-of-scope gate. Otherwise repair owned-lane failures and return
`COMPLETE_PENDING_REVIEW`.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 12d2d0d7437db746e4c4c038cf88eb881e03c23d --head HEAD
pwsh -NoProfile -File scripts/acel_g1_approver_group2_decision_writer.ps1
python -m py_compile governance/compat/check_acel_g1_verification_authority_spec.py governance/compat/test_check_acel_g1_verification_authority_spec.py
python governance/compat/test_check_acel_g1_verification_authority_spec.py
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
git diff --cached --name-only
```

No live release-gate command applies because this is hermetic source tooling,
not a provider or production-readiness claim.

## Review Gate

Local consumes evidence, checks exact five-path/frozen-path reconciliation and
performs only the admitted atomic positive plus replacement-field mutation
probes. Local does not use credentials or write real Group 2 sources.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

evidenceReadinessContract: NOT_APPLICABLE_WITH_REASON: bounded local contract/tooling correction has no discovery audit or manifest artifact

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required return fields include: exact status, dispatch work order, response
work order, execution base, changed files, command evidence, git status,
no-commit statement, claim boundary, independent probe disposition, checker
read-ahead, operation trace, corpus reconciliation, learning disposition and
public export disposition.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | reviewer-owned R2 completion artifact created only if needed for closure evidence |
| reviewerOwnedClosurePaths | accepted five worker outputs plus bounded repair inside those paths only |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |
| materialCommitBoundary | accepted R2 implementation first |
| sessionSyncBoundary | separate commit following the material commit |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Local dispatcher -> no-commit INTERNAL_AGENT worker -> Local reviewer/closer |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC; real principal execution excluded |
| baseHeadFor(phase) | dispatchBaseHead=`12d2d0d7437db746e4c4c038cf88eb881e03c23d`; executionBaseHead captured by worker; closureBaseHead set by Local |
| changedSetScope(phase) | exact five worker paths; three reviewer-owned dispatch artifacts |
| traceScope(phase, actor) | reads, commands, tests, hashes, status, cleanup and absence evidence |
| commitOwner(phase) | Local only |
| crossBatchIsolation | thirteen parked paths plus accepted spec writer remain byte-identical |
| nextMoveSurfaces | Local review, then separately authorized principal checkpoint |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT R2 worker after operator relays this packet

laneOwnedPaths: exact five paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return, empty staging, exact delta and frozen-path reconciliation

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | exact five R2 outputs | hermetic contract/tooling work only | this packet | local file/test surface | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | none | no external execution authority | no adapter source | fresh packet required | DEFERRED_WITH_REASON |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF workspace |
| Session or invocation | ACEL-G1-T3B-R2 dispatch, 2026-09-20 |
| Working directory | repository root |
| Command or tool surface | governed reads, in-memory probe, scaffold stdout, apply_patch, governance gates and Git |
| Target paths | R1 completion review plus paired R2 baseline/work order |
| Allowed scope source | standing Local orchestrator/reviewer authority and R1 Review Gate |
| Before status evidence | R1 COMPLETE_PENDING_REVIEW; eighteen untracked paths; staging empty |
| After status evidence | R1 rejected; exact five-path R2 atomic correction ready for relay |
| Diff evidence | exact reviewer dispatch manifest before material commit |
| Approval boundary | reviewer disposition and no-commit correction dispatch only |
| Claim boundary | no real source, principal, activation, admission, live/public/deployment effect |
| Agent type | Local dispatcher/reviewer |
| Invocation ID | `acel-g1-t3b-r2-atomic-rotation-dispatch-20260920` |
| Expected manifest | R1 completion review, R2 baseline, R2 work order |
| Actual changed set | reconciled before commit |
| Manifest delta | pending final gate |
| Deletion or rename disposition | none |

## External/Local Coordination Binding

Role: `INTERNAL_AGENT`; phase: R2 implementation; decision owner: Local
reviewer. External research ends outside this packet and has no authority here.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` |
| Chain map route | N/A with reason: direct internal contract correction |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T2F Group 2 contract and R2 dispatch |
| Disposition | local first-party correction only |
| Claim boundary | no external source authority, corpus, remote implementation or provider claim |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO_NEW_RUNTIME_CLAIM |
| runtimeMutationAuthorized | no runtime mutation; repository-local tooling correction only |
| freshnessVerificationMode | current exact-path checks of `governance/sources/verification_authority_spec/SPEC_v1.json` and `governance/sources/verification_authority_spec/ACTIVATION_DECISIONS.jsonl`, plus direct reads of the five returned tooling paths |
| reason | both real Group 2 source paths remain absent; accepted evidence is hermetic tooling behavior only |
| requiredFutureAction | execute the separately controlled Party A and Approver steps, then perform Local source verification before promotion or admission |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ACEL_G1_T3B_R2_ATOMIC_ROTATION_CONTRACT_CORRECTION_COMPLETION_2026-09-20.md` | terminal status and independent-probe binding | PASS |
| Roadmap state | active ACEL program continuity | T3B R2 accepted; operational Group 2 execution remains next | PASS |
| Registry JSON | no registry mutation in tooling scope | exact five-path manifest | BLOCKED with reason: GC-051 registry mutation is outside this bounded tooling correction |
| Registry Markdown | no registry mutation in tooling scope | exact five-path manifest | BLOCKED with reason: GC-051 registry mutation is outside this bounded tooling correction |
| External evidence digest | no external evidence admitted | internal-input routing table | N/A with reason: local repository evidence only |
| System loop interlock | T2F contract, writer and Python verifier | 74/74 PowerShell, 58/58 Python and 3/3 reviewer probes | PASS |
| Session continuity | active handoff and generated session state | dedicated post-material synchronization | BLOCKED with reason: pending material commit SHA |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private corrective dispatch; no public artifact or sync authority.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: no legacy or external corpus absorption occurs.

## Operator Checkpoint

No operator action is needed during R2. Real Party A creation and Approver
decision execution remain separate checkpoints only following Local acceptance.

## Claim Boundary

This work order authorizes only the exact five-path hermetic R2 correction. It
does not establish Group 2, execute Party A or Approver, activate a real spec,
wire a consumer, promote a key, admit a candidate, or authorize provider/live,
runtime, public-sync, deployment or production behavior.
