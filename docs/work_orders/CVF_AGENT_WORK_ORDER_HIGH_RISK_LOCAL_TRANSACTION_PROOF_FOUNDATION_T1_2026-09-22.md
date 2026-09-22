# CVF Agent Work Order - High-Risk Local Transaction Proof Foundation T1

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

providerExecutionAuthority: FORBIDDEN

independentProbeRequired: YES

Batch ID: CVF-HRLTP-T1

Dispatch base head: `6fc501439a96b1023aacab06a6937e7bf2677f20`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: shared-workspace INTERNAL_AGENT

Reviewer/closer: Local orchestrator/reviewer

Worker return path: `docs/reviews/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_FOUNDATION_T1_WORKER_RETURN_2026-09-22.md`

## Dispatch Prompt Envelope

Role: shared-workspace INTERNAL_AGENT worker for CVF-HRLTP-T1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_HIGH_RISK_LOCAL_TRANSACTION_PROOF_FOUNDATION_T1_2026-09-22.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-09-22; use repository state and checker source, not model memory, as authority.

Do-not-misread notes: this packet authorizes only the ten manifest paths below. It does not authorize ACEL runtime changes, live ceremony execution, real source mutation, session-state edits, public-sync, provider work, or production claims.

Required first actions: read the startup front door, bootstrap model, active handoff, guard orientation, literal-format gotchas, paired baseline, this packet, and every applicable checker source before editing.

Return contract: implement and test the bounded foundation, write the canonical worker return, run the full worker-return fast gate, leave every change uncommitted, and return exactly `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement the reusable governance control authorized by the paired baseline:
new high-risk local transaction work must declare and machine-bind its proof of
real cross-process exclusion, exception-safe guard lifetime, semantic security
rollback, and immutable final evidence.

## Authority Chain

| Authority | Evidence |
| --- | --- |
| Operator decision | Operator approved foundation uplift after AR1 and asked the reviewer to proceed without incremental stops. |
| Paired baseline | `docs/baselines/CVF_GC018_HIGH_RISK_LOCAL_TRANSACTION_PROOF_FOUNDATION_T1_2026-09-22.md` |
| Learning philosophy | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` |
| Active handoff | `AGENT_HANDOFF_V63_2026-09-18.md` |

## Agent Roles

| Role | Responsibility |
| --- | --- |
| dispatcher | Owns the committed baseline and work order. |
| INTERNAL_AGENT worker | Implements only the manifest, tests it, writes the return, and does not commit. |
| Local orchestrator/reviewer | Evaluates returned evidence, runs the independent probe, repairs only minor closure defects, and owns any accepted commit. |
| session-sync steward | Updates continuity only after material acceptance. |

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "CVF-HRLTP-T1",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "CREATES_OR_CHANGES_AUTHORITY",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NONE",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [
    "docs/baselines/CVF_GC018_HIGH_RISK_LOCAL_TRANSACTION_PROOF_FOUNDATION_T1_2026-09-22.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_HIGH_RISK_LOCAL_TRANSACTION_PROOF_FOUNDATION_T1_2026-09-22.md",
    "docs/reference/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_STANDARD_2026-09-22.md",
    "docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md",
    "docs/reference/guard_orientation/README.md",
    "governance/compat/check_high_risk_local_transaction_proof.py",
    "governance/compat/test_check_high_risk_local_transaction_proof.py",
    "governance/compat/local_governance_hook_catalog_reviewer_fast.py",
    "governance/compat/local_governance_hook_catalog_pre_commit.py",
    "governance/compat/local_governance_hook_catalog_pre_push.py",
    "governance/compat/test_run_local_governance_hook_chain.py",
    "docs/reviews/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_FOUNDATION_T1_WORKER_RETURN_2026-09-22.md"
  ],
  "claims": ["static authoring admission for high-risk local transaction proof contracts"],
  "requiredProof": ["focused adversarial checker tests", "three-hook membership", "stable final return digest", "reviewer independent probe pending"],
  "operatorCheckpoints": ["scope expansion", "runtime or public effect"],
  "forbiddenEffects": ["worker commit", "network", "provider calls", "target runtime mutation", "public sync", "legacy gate suppression"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

## Required First Reads

| Path | Required action |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `AGENT_HANDOFF_V63_2026-09-18.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| paired baseline and this work order | READ |
| every changed owner and applicable checker source | SOURCE_VERIFIED before edit |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id CVF-HRLTP-T1 --title "High-Risk Local Transaction Proof Foundation T1" --date 2026-09-22 --base 6fc501439 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled authority, exact ten-path manifest, Core Guard authorization, implementation contract, adversarial acceptance matrix, verification commands, and no-commit return contract. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_worker_return_quality_gate.py` |
| docOnlyNewFields | High-Risk Local Transaction Proof Applicability and the nine contract fields defined in the paired baseline |
| claimBoundary | Dispatch provenance only; no implemented enforcement is claimed. |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-HRLTP-T1
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
  "problemKey": "high-risk-local-transaction-proof-foundation-t1",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {"prior": [], "resolved": [], "retained": [], "new": [], "reopened": [], "current": []},
  "resolutionEvidence": {},
  "counters": {"partialReadyClosures": 0, "reviewerScopeExpansions": 0, "sameClaimCorrections": 0, "nonDecreasingBlockerTransitions": 0},
  "claims": [],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Worker Autonomy / No-Question Rule

Repair allowed-scope defects directly by reading the failing source. Return to
the reviewer only for a real authority contradiction, forbidden-scope need, or
failure outside the manifest that cannot be resolved without expansion.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`governance-guard-authoring`, role=`INTERNAL_AGENT`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "governance-guard-authoring" --role INTERNAL_AGENT --lifecycle-phase implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF entry changes this work order; record a new repeated non-obvious defect if implementation discovers one. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_finding_to_governance_learning.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block; Required Artifact Manifest; Core Guard Self-Protection Authorization; Worker Return Packet Shape Contract; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Finding-To-Governance Learning Disposition; Public Export Disposition |
| gateRunPurpose | Confirmation evidence after source read-ahead, not first discovery. |
| claimBoundary | Dispatch author read-ahead only; worker must inspect the owners it changes and the new checker/test before authoring its return. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Repeated defects justify rule, checker, and earliest gate. | EXISTS | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | learning sequence | rule/check/gate | CVF learning philosophy | ACCEPT |
| The ACEL correction contract identifies real peer, deterministic barrier, post-acquire exception, semantic rollback, and digest stability obligations. | EXISTS | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_AR1_TRANSACTION_ARCHITECTURE_PROOF_CLOSURE_2026-09-22.md` | correction and acceptance sections | AR1 proof obligations | ACEL AR1 work order | ACCEPT |
| The accepted return records the concrete evidence pattern to generalize. | EXISTS | `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md` | findings and verification | accepted AR1 evidence | ACEL worker return | ACCEPT |
| Compatibility checkers and hook catalogs are protected paths. | EXISTS | `governance/compat/check_core_guard_self_protection.py` | protected-path logic | `governance/compat/` | Core Guard checker | ACCEPT |
| Hook membership is regression-tested through the extracted catalogs imported by the runner. | EXISTS | `governance/compat/test_run_local_governance_hook_chain.py` | hook membership tests | `LocalGovernanceHookChainTests` | local hook chain tests | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned packet and implementation paths | All planned new paths returned `False` before authoring. | PASS |
| Reusable-rule search | No existing reusable high-risk local transaction proof standard or checker was found; only the closed ACEL-specific requirement matched. | PASS |
| Collision decision | Create one general control without rewriting historical packets or the closed ACEL tranche. | PASS |

## Dated Owner Dependency Discovery

| Dated owner | Classification | Reason |
| --- | --- | --- |
| `docs/reference/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_STANDARD_2026-09-22.md` | BINDING_REFERENCE_ACTIVE_WINDOW | New canonical owner created by this tranche. |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | BINDING_REFERENCE_ACTIVE_WINDOW | Current canonical work-order template named by AGENTS.md. |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| Intake summary | Convert an accepted internal defect pattern into reusable private-CVF governance. |
| Scope classification | Bounded protected-governance-path implementation. |
| Risk sensitivity | Medium: changes blocking compatibility checks but does not touch target runtime. |
| Selected role route | routeMode=`SINGLE_AGENT_SINGLE_ROLE`; INTERNAL_AGENT implementation followed by Local reviewer closure. |
| Role separation basis | Worker must not commit; reviewer owns independent probe and acceptance. |
| Escalation condition | Source contradiction, forbidden path requirement, or unrepairable out-of-scope gate failure. |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher-authored packet to one INTERNAL_AGENT worker, then Local reviewer conversion |
| phase | implementation |
| baseHeadFor(phase) | dispatchBaseHead=`6fc501439a96b1023aacab06a6937e7bf2677f20`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | Exactly the ten worker-owned paths in Required Artifact Manifest. |
| traceScope(phase, actor) | Worker return reconciles expected and actual changed sets and records commands without secrets. |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns accepted material commit. |
| crossBatchIsolation | Preserve all parked paths and do not edit ACEL runtime, session, public-sync, provider, or unrelated governance surfaces. |
| nextMoveSurfaces | Worker cannot edit next-move surfaces; reviewer owns continuity after acceptance. |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: shared-workspace INTERNAL_AGENT worker
laneOwnedPaths: exactly the ten Work-Order Fulfillment Manifest paths
dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE
laneReleaseEvidence: terminal worker return, exact manifest reconciliation, stable final digest, and empty staging area

The dispatch lane has a clean worktree for tracked dispatch-owned paths. The
13 pre-existing untracked paths are explicitly parked, excluded from this lane,
and must remain byte-unchanged. After dispatch commit and continuity sync, the
dispatcher will not mutate worker-owned paths until lane release.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0
closeabilityDisposition: CLOSEABLE
implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT
foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET
returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline and work order | EXACT_PATHS | reviewer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired dispatch packet | EXACT_PATHS | reviewer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker and exact continuity paths | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| pre_implementation_autorun | IMPLEMENTATION | worker | IMPLEMENTATION | exact ten worker paths | EXACT_PATHS | reviewer | MATERIAL_COMMIT | dispatch_continuity |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | checker, focused test and hook membership test | EXACT_PATHS | reviewer | MATERIAL_COMMIT | dispatch_continuity, pre_implementation_autorun |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return disclosure | EXACT_PATHS | reviewer | MATERIAL_COMMIT | focused_checker_tests |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact worker manifest and final return bytes | EXACT_PATHS | reviewer | MATERIAL_COMMIT | adif_integrity |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted exact material paths | EXACT_PATHS | reviewer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted exact material paths | EXACT_PATHS | reviewer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | canonical return or optional completion review | EXACT_PATHS | reviewer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | exact Local continuity paths | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | accepted committed material range | EXACT_PATHS | reviewer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_FOUNDATION_T1_COMPLETION_2026-09-22.md` (optional; prefer reviewer corrections in the canonical worker return when small) |
| reviewerOwnedClosurePaths | Paired baseline, this work order, optional completion review, and continuity surfaces only after acceptance. |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

Conventional completion review path, if needed:
`docs/reviews/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_FOUNDATION_T1_COMPLETION_2026-09-22.md`.

## Pre-Flight Checks

Before the first edit, capture `executionBaseHead`, run `git status --short`,
confirm the ten manifest paths against parked worktree paths, and run the
pre-implementation autorun gate using the captured base.

## Write Ownership

The worker owns exactly the ten paths below and must leave them uncommitted.
The reviewer owns the paired dispatch docs, optional completion review,
material commit, and later continuity update.

## Work-Order Fulfillment Manifest And Required Artifact Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_STANDARD_2026-09-22.md` | Create canonical rule, applicability triggers, required evidence fields, fail-closed semantics, examples, and claim boundary. |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Add a concise conditional contract block and routing instruction; do not duplicate the standard. |
| `docs/reference/guard_orientation/README.md` | Route high-risk local mutation/rollback work to the new standard and checker. |
| `governance/compat/check_high_risk_local_transaction_proof.py` | Create changed-file checker with `--base`, `--head`, and `--enforce`; fail closed on omitted/partial contracts. |
| `governance/compat/test_check_high_risk_local_transaction_proof.py` | Add focused positive and adversarial unit tests. |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | Add the checker at the earliest relevant reviewer admission point. |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | Add the checker to pre-commit. |
| `governance/compat/local_governance_hook_catalog_pre_push.py` | Add the checker to pre-push. |
| `governance/compat/test_run_local_governance_hook_chain.py` | Assert membership in reviewer-fast, pre-commit, and pre-push. |
| `docs/reviews/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_FOUNDATION_T1_WORKER_RETURN_2026-09-22.md` | Create canonical no-commit return with focused evidence, full fast-gate result, independent probe disposition, and stable final digest. |

No path substitution, omission, or addition is allowed without reviewer authorization.

## Allowed And Forbidden Scope

Allowed scope is exactly the ten manifest rows above. Forbidden scope includes
all `CVF_SESSION/**` paths, `CVF_SESSION_MEMORY.md`, active or archived handoffs,
ACEL runtime scripts, real governance source data, public-sync, providers,
secrets, Web/UI, package lifecycle, MCP/CLI adapters, and model routing.

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Foundation path class | existing root reference, work-order template, guard orientation, and compatibility checker/test/catalog families |
| Storage decision | create one root reference owner and extend existing owners; no new folder or parallel foundation tree |
| Existing aggregate impact | none |
| Generated state impact | none during worker implementation; continuity is reviewer-owned later |
| Durable governance boundary | standard owns semantics; checker owns admission; tests own regressions; catalogs own earliest execution |

## Core Guard Self-Protection Authorization

Authorization status: EXPLICITLY_AUTHORIZED.

Protected paths authorized: the six `governance/compat/` paths in the manifest.

Reason: this tranche intentionally creates one compatibility checker, its test,
wires it into three extracted hook catalogs, and updates the hook membership
test. No other protected path is authorized. The worker must preserve
fail-closed behavior and may not weaken, skip, silence, or remove any existing
check.

## Implementation Contract

The new standard and checker must use this exact disposition label:

`High-Risk Local Transaction Proof Applicability: REQUIRED`

or:

`High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - <reason>`

At minimum, detect current work orders that authorize any combination of
cross-process locking, durable append/write with rollback, ownership/DACL
mutation, or post-acquire failure handling. A triggered work order without an
applicability declaration fails. Historical unchanged artifacts are out of
scope.

When `REQUIRED`, require non-placeholder values for all fields:

- `transactionTarget`
- `productionPathPeer`
- `deterministicBarrierProtocol`
- `enteredBeforeReleaseOracle`
- `postAcquireFailureInjection`
- `semanticSecurityTuple`
- `rollbackExactness`
- `finalEvidenceHashBinding`
- `independentProbeRequired`

The standard must define their semantics:

- production-path peer means a real second process invoking the actual guarded
  mutation path, not a shape-only mutex call;
- deterministic barriers establish attempt-before-release and entry-after-
  release without treating timeout as proof;
- post-acquire injection occurs after ownership is obtained and before the
  protected mutation, with a subsequent peer acquisition proving cleanup;
- semantic security state includes owner SID, protection/inheritance state,
  and normalized complete ACE tuples including allow/deny and inherited ACEs;
- rollback exactness compares semantic pre-state with semantic post-rollback
  state and exercises extra allow, deny, inherited, and wrong-owner cases;
- final evidence binding hashes the exact return bytes before and after the
  final required gate and forbids post-gate mutation;
- independent probe is reviewer-owned and remains pending at worker return.

Checker implementation must parse changed files robustly, avoid global false
positives from prose examples, print actionable diagnostics, and return exit 1
only under `--enforce`. Tests must include each missing-field case, all risk
trigger families, safe non-applicable behavior, no historical retroactivity,
and hook membership.

## Execution Plan

1. Inspect the current template, orientation, hook catalogs, and their tests.
2. Write the standard first, including applicability and semantic definitions.
3. Implement the changed-file checker and adversarial tests.
4. Wire the checker into all three extracted catalogs and extend membership
   regression coverage.
5. Update the template and orientation to route future packets to the standard.
6. Run focused tests, pre-implementation gate, and aggregate worker-return gate.
7. Freeze the return, capture pre/post final-gate digests, then make no further
   mutation.

## Acceptance Criteria

1. Exact ten-path manifest; no collateral edits.
2. New checker focused tests all pass and report their real count.
3. Hook-chain tests pass and prove all three memberships.
4. Standard, template, orientation, checker, and tests agree on exact tokens.
5. `reviewer-fast`, `pre-commit`, and `pre-push` catalogs retain all prior
   commands and add the new check once each.
6. Worker return reports `independentProbeDisposition: PENDING_REVIEWER_EXECUTION`.
7. Worker return's SHA-256 is identical before and after the final worker-return
   fast gate; no file may be edited after the post-gate hash capture.
8. Work remains uncommitted and the 13 pre-existing parked paths are preserved.

## Verification Commands

```powershell
git rev-parse HEAD
git status --short
python -m unittest governance.compat.test_check_high_risk_local_transaction_proof
python -m unittest governance.compat.test_run_local_governance_hook_chain
python governance/compat/check_high_risk_local_transaction_proof.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
git status --short
```

If the aggregate gate exposes an allowed-scope defect, repair it and rerun the
whole required sequence. Do not replace the aggregate gate with individual
checker success.

## Evidence Requirements

The return must include execution base, exact test counts, command exit codes,
checker diagnostics for representative negative fixtures, hook membership,
changed-set reconciliation, parked-path preservation, Core Guard result,
pre/post final-gate return digest, and independent probe disposition. Claims
without command or file evidence are not acceptance evidence.

## Review Gate

Reviewer will consume valid returned evidence without rebuilding the worker's
implementation. Reviewer independently checks the manifest, executes the new
checker against at least one positive and one adversarial temporary fixture,
confirms hook membership, and runs the reviewer-fast gate. Any material
semantic gap returns as a consolidated rework order.

## Independent Review Probe Admission Contract

independentProbeRiskClass: HIGH

independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: REQUIRED_DIFFERENT_EXECUTION_AND_ASSERTION_PATH

positiveControl: reviewer-created complete required contract fixture that the new checker accepts

negativeMutationClasses: omitted applicability, each missing required field, false non-applicable disposition, shape-only peer, timeout-as-proof, incomplete ACL tuple, and unstable final digest

expectedInformationGain: prove the generalized checker rejects unseen semantic-class variants rather than replaying only worker fixtures

rerunCostReason: two focused reviewer-owned fixtures have higher information gain than repeating the worker suite

reviewerDecisionOwner: LOCAL

## Closure Checklist

- exact ten-path manifest and no parked-path mutation;
- no commit by worker;
- standard/template/orientation/checker token convergence;
- focused tests and hook membership tests pass;
- aggregate worker-return fast gate passes;
- stable final return digest and no post-gate edit;
- independent probe explicitly pending for reviewer;
- no runtime, provider, public, or production overclaim.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_FOUNDATION_T1_WORKER_RETURN_2026-09-22.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Scope / Methodology; Findings / Position; Risk /
Corrective Action; Claim Boundary; Agent Operation Trace Block; Delta Execution
Claim Boundary Control Block; Finding-To-Governance Learning Disposition;
Public Export Disposition; executionBaseHead; git status --short;
independentProbeDisposition; preGateReturnSha256; postGateReturnSha256;
NO_POST_GATE_MUTATION.

Use `N/A with reason` for non-applicable conditional blocks. Do not claim final
acceptance, commit, or reviewer probe completion.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | shared-workspace INTERNAL_AGENT worker |
| Provider or surface | operator-selected internal worker surface |
| Session or invocation | CVF-HRLTP-T1, 2026-09-22 |
| Working directory | repository root |
| Command or tool surface | repository reads, patch edits, local Python and governance gates |
| Target paths | exact Required Artifact Manifest |
| Allowed scope source | this committed work order |
| Before status evidence | tracked dispatch-owned worktree clean; capture `git status --short` and execution base before edits; preserve 13 explicitly parked untracked paths |
| After status evidence | worker return must include final `git status --short` |
| Diff evidence | `git diff --name-status`; `git diff --check` |
| Approval boundary | bounded implementation only; no commit |
| Claim boundary | evidence returned for reviewer evaluation, not self-acceptance |
| Agent type | INTERNAL_AGENT |
| Invocation ID | `cvf-hrltp-t1-2026-09-22` |
| Expected manifest | ten paths |
| Actual changed set | worker must populate |
| Manifest delta | worker must populate as NONE or return blocked |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | Documentation and static changed-file governance enforcement for high-risk local transaction proof contracts. |
| claimDisposition | CLAIM_REJECTED: no target runtime transaction, direct interception, or production enforcement is claimed by this work order. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is claimed; worker return is repository evidence only. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no target runtime action is claimed; repository edits are implementation evidence only. |
| invocationBoundary | Internal local commands; no provider/live/public invocation. |
| interceptionBoundary | The checker evaluates governed repository artifacts; it does not intercept target runtime writes or OS security calls. |
| claimLanguage | Machine-checkable authoring admission, not proof that any particular transaction implementation is safe. |
| forbiddenExpansion | No ACEL runtime, provider, live, public, package, Web, MCP, or model-router work. |

## Finding-To-Governance Learning Disposition

Disposition: GOVERNANCE_UPLIFT_REQUIRED_AND_AUTHORIZED.

Source findings: the four accepted AR1 defect classes listed in the paired
baseline. Conversion target: written standard, changed-file checker,
adversarial tests, and reviewer-fast/pre-commit/pre-push wiring. Closure of
this work order proves only that the reusable guard exists and passes its
tests; it does not retroactively certify other transaction implementations.

## External Knowledge Intake Routing

Canonical chain map:
`docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`.

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md` |
| Chain map route | local-only governance dispatch; external branch not entered |
| Matching local-view guard | `governance/compat/check_high_risk_local_transaction_proof.py` plus Local reviewer decision |
| Owner surface | paired baseline and new standard |
| Disposition | NOT_APPLICABLE_WITH_REASON: no external source or research is admitted |
| Claim boundary | no external research, repository, provider, CLI/MCP, Web, or public authority |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Epistemic Process Block

| Field | Value |
| --- | --- |
| known | The accepted AR1 defect pattern, existing work-order template, protected checker boundary, and extracted hook owners. |
| inferred | The four defects are general enough to justify one reusable authoring admission contract. |
| unknown | Whether future implementations satisfy the contract; that remains tranche-specific evidence. |
| validation | Focused checker tests, hook membership tests, aggregate worker-return gate, and reviewer independent probe. |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this tranche converts a current Local defect into a
new governance check; it does not absorb legacy payloads or claim legacy
coverage-index closure.

## Claim Boundary

This work order authorizes only the exact ten-path governance foundation. It
does not authorize worker commit, continuity edits, ACEL execution, real source
creation, public export, runtime/provider/live proof, or production claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening; no public-sync artifact is in
scope.

## Operator Checkpoint

operator.checkpoint.waiver: operator already authorized the foundation uplift
and asked the orchestrator/reviewer to proceed continuously. No additional
operator checkpoint is required before worker execution. Any scope expansion
still requires a new authorization.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every manifest path is present,
tests and aggregate gate pass, digest binding is stable, independent probe is
explicitly pending, and all changes remain uncommitted. Otherwise return
`BLOCKED_WITH_REASON` with the exact blocker and current changed set.
