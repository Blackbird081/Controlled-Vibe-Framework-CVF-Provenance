# CVF Agent Work Order - ACEL G2 T2 Fresh Direct Calibration T1

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Date: 2026-09-16

Batch ID: ACEL-G2-T2-FRESH-DIRECT-CALIBRATION-T1

dispatchBaseHead: `44464b449033d5e2d51ca9baa4a32d5e66198445`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT live-calibration worker.

Canonical packet: this work order and paired baseline.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture the exact clean post-dispatch HEAD at worker start.

Current-time notes: refresh official model price and account Free Quota Only evidence immediately before the call.

Required first actions: read startup, guards and sources; capture HEAD/status; run pre-implementation before edits.

Do-not-misread notes: one direct call maximum, zero retries, historical receipt immutable, parse failure non-admissible.

Return contract: leave exact three worker paths uncommitted, staging empty; return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

providerExecutionAuthority: ORCHESTRATOR_GRANT_REQUIRED
providerExecutionGrantOwner: ORCHESTRATOR
providerExecutionGrantSubject: ACEL-G2-T2-FRESH-DIRECT-CALIBRATION-T1
providerExecutionGrantDelegationId: ACEL-G2-T2-FRESH-DIRECT-CALIBRATION-T1
providerExecutionGrantMaxCalls: 1
providerExecutionGrantExpiresAt: 2026-09-18T23:59:59+07:00

## Purpose

Measure one fresh direct response to the qualified T6A task, with independent
review possible for successful parse. Preserve the rejected historical result.

## Authority Chain

Operator 2026-09-16 agreement -> Local conditional T0 qualification at
`36784f6c6efa2fdca6b497a6d341ece7bcd3a2c8` -> paired GC-018 -> this
bounded work order. No other work order grants calls to this task.

## Agent Roles

Worker owns source retarget, prerequisite checks, one call and pending evidence;
reviewer independently checks original receipt integrity, scorer output,
defects, cost and secret safety; closer owns material commit; session-sync
steward projects accepted disposition separately.

## Required First Reads

`CVF_SESSION_MEMORY.md`; active bootstrap/handoff; paired baseline; T0 audit
and machine ledger; T6A completion review; current runner, task contract,
free-quota ledger/owner and Model Gateway harness; guard orientation and
literal-format gotchas. Provider documentation and actual account quota are
rechecked immediately before the live attempt.

## Pre-Flight Checks

Require exact clean HEAD and empty staging, no receipt collision, Node/tsx
availability, approved alias presence without value disclosure, current
official `qwen3.7-flash` price, International/Singapore endpoint, current
remaining free quota above the bounded request, and account Free Quota Only
enabled. Verify no paid exposure. Record all as secret-safe facts. If any
cannot be proven, stop at zero calls. Never use expired `qwen3.7-plus`.

## Write Ownership

Exactly the three paths in the manifest below. Existing T6A evidence, task
contract, tests, gateway, ledger, source mirror, continuity and credential
file are read-only. No path expansion without a new packet.

## Scope / Target / Owner Boundary

Allowed scope is the one existing runner plus two fresh evidence outputs.
Forbidden scope includes the historical result, scorer, Model Gateway, any
additional call, external CLI/MCP, production and public surfaces. Mandatory
gate defects within these exact owned paths are repaired without asking the
operator; only actual scope or authority expansion requires escalation.

## Work-Order Fulfillment Manifest

The Required Artifact Manifest is the exact fulfillment set. Source and
evidence paths outside it are read-only; Local owns any completion review.

## Worker Autonomy / No-Question Rule

Repair in-scope static, test and packet defects directly. Stop for missing
live prerequisites, source contradiction, out-of-scope mutation, credential
exposure or any need to exceed the one-call budget. Do not rerun a live call.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| intake summary | one fresh qualified direct calibration |
| scope classification | bounded provider live proof with source retarget |
| risk sensitivity | P4 live/provider with credential reference |
| selected role route | `SINGLE_AGENT_MULTI_ROLE`; Local reviewer/closer remains independent |
| role separation basis | worker returns no-commit evidence; Local adjudicates score and commits |
| escalation condition | paid exposure, source contradiction, additional call or model substitution |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| Applicability | one worker retargets and executes the bounded call |
| actor | INTERNAL_AGENT worker |
| role set | source editor, live worker, evidence producer; never Local reviewer/closer |
| Role separation ledger | no worker commit; independent Local score/defect decision |
| Evidence basis independent of memory | exact source, receipt and current account evidence |
| Gate sequence | pre-implementation, offline check, one call, worker-return fast, Local review |
| Self-review boundary | worker score is not accepted threshold evidence |
| escalation condition | any authorization or evidence-shape expansion |

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-oa-t6a-candidate-calibration.ts` | Yes | retarget model and fresh output path only |
| `docs/reviews/evidence/acel-g2-t2-fresh-direct-calibration-t1-2026-09-16.json` | Yes | fresh call or blocked receipt |
| `docs/reviews/CVF_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_WORKER_RETURN_2026-09-16.md` | Yes | worker evidence for Local review |

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| `docs/reviews/evidence/mao-oa-t6a-direct-candidate-calibration-2026-07-17.json` | rejected historical result must remain byte-identical |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/harder.value.candidate.contract.ts` | frozen task and scoring contract |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | no gateway change |

## Execution Plan

1. Capture clean execution HEAD and SHA-256 of historical receipt. Verify all
   live prerequisites and record source/price/account evidence without a key.
2. Run pre-implementation gate. Retarget only `MODEL_ID` to `qwen3.7-flash`, `RESULT_PATH` to the fresh T1
   receipt, and stale comments/run identifiers as needed. Reject a diff that
   changes prompt, rubric, call/retry count, key loader or evidence shape.
3. Run offline static/focused checks.
   Do not run the live script as a test; it calls the provider.
4. If any prerequisite fails, write a blocked zero-call receipt and return.
   Otherwise run the runner once, with no retry on failure or ambiguity.
5. Write the no-commit worker return, run worker-return fast gate, record final
   status and stop for Local review.

## Acceptance Contract

- Exactly zero or one attempted provider call; retry count zero.
- No old receipt write; compare historical SHA-256 before/after.
- No raw key, authorization header, signed payload or raw response persisted.
- Successful parse: sanitized candidate present; Local must independently run
  `evaluateHarderCandidate` and match rubric and defects before admission.
- Parse failure: `sanitizedCandidate=null` is non-reconstructable. Treat score,
  `INVALID_JSON`, material-defect and release claims as `NOT_ACCEPTED` even if
  worker-derived fields are present. No second call.
- Score <=80 or material defect may only be considered after Local independent
  acceptance; this work order does not itself release T6B.
- No G2-T2 A/B or T1-to-MAO callable seam claim.

## Evidence Requirements

Record execution HEAD, source diff, historical receipt hash before/after,
current price and quota source, Free Quota Only account evidence, alias name
but not value, exact command, call count, diagnostic, new receipt hash and
final status. No worker conclusion substitutes for Local recomputation.

## Acceptance Criteria

- [ ] One or zero attempted calls, zero retries, no charge exposure.
- [ ] Three owned paths only and historical receipt hash unchanged.
- [ ] Successful parsed result independently rescorable, or terminal
  fail-closed non-admission with reason.
- [ ] No unsupported T6B, MAO, callable-seam or G2-T2 improvement claim.

## Mandatory Live Run Diagnostic Block

On failed, partial, timed-out or empty result, record secret-safe stage,
class, retryability, operator action, provider/model, HTTP status when known,
latency and call count. Never rerun without a new authorization. Follow
`docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`.

## Operator Checkpoint

The operator authorized this bounded calibration, not model substitution,
paid billing, a second call, evidence-shape mutation or a MAO experiment. Stop
and return for those changes. The Local reviewer decides result admissibility.

## Review Gate

Run pre-dispatch before worker start, pre-implementation before source edit,
worker-return fast gate before handoff, and committed-range pre-closure after
Local material and continuity commits. Reviewer consumes valid returned
evidence and reruns only to resolve a named contradiction.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
```

Focused offline check: run only the existing pure scorer tests before the
live command. The live runner command is one permitted provider attempt,
not an offline test; never rerun it to obtain a green gate.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` without a call for missing Free Quota Only proof,
account quota, key alias, endpoint, source contradiction, expired grant, output
collision, or necessary out-of-scope change. After an attempted call, return
the receipt and diagnostic without retrying.

## Closure Checklist

- [ ] Local verifies exact manifest, receipt integrity and historical hash.
- [ ] Local independently accepts or rejects score/defect evidence.
- [ ] Worker-return, material commit, continuity and range gates pass.
- [ ] Calibration outcome and remaining callable-seam blocker remain distinct.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G2-T2-FRESH-DIRECT-CALIBRATION-T1
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

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g2-t2-fresh-direct-calibration-t1-problem","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["NO_ACCEPTED_FRESH_DIRECT_CALIBRATION","NO_CALLABLE_T1_TO_MAO_CONSUMER"],"reopened":[],"current":["NO_ACCEPTED_FRESH_DIRECT_CALIBRATION","NO_CALLABLE_T1_TO_MAO_CONSUMER"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G2-T2-CAL-T1","claimClass":"DOCUMENTATION_ONLY","proofClass":"PROPOSAL_ONLY_NO_RUNTIME_READINESS","evidenceRef":"docs/baselines/CVF_GC018_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_2026-09-16.md"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"NO_SUCCESSOR"}
```

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | INTERNAL_AGENT runs bounded direct calibration; Local reviews and closes |
| phase | FRESH_DIRECT_CALIBRATION |
| baseHeadFor(phase) | dispatchBaseHead=`44464b449033d5e2d51ca9baa4a32d5e66198445`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact three worker paths |
| traceScope(phase, actor) | prerequisite checks, call ledger, secret-safe receipt, gates and status |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | clean worktree; no concurrent mutation |
| nextMoveSurfaces | Local reviewer return only |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: INTERNAL_AGENT worker
laneOwnedPaths: exact three paths in Required Artifact Manifest
dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE
laneReleaseEvidence: worker return, empty staging, exact changed set

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_COMPLETION_2026-09-16.md`, reviewer-owned if needed |
| reviewerOwnedClosurePaths | optional completion review; material commit; separate continuity commit |
| closureOwner | Local |
| workerCommitPermission | FORBIDDEN |

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline and work order | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline and work order | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | AGENT_HANDOFF_V60_2026-09-08.md material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact three worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact three worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact three worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted worker paths plus reviewer closure | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | reviewer completion path | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_WORKER_RETURN_2026-09-16.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must include Target/Source, Scope/Methodology,
Findings/Position, Risk/Corrective Action, Decision/Disposition, External
Knowledge Intake Routing and Epistemic Process Block. Start with the canonical
worker-return scaffold and run the fast gate before long prose.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G2-T2-FRESH-DIRECT-CALIBRATION-T1","requestedProfile":"P4_CRITICAL","classification":{"taskKind":"LIVE_PROOF","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NETWORK_WRITE","dataSensitivity":"CREDENTIAL_REFERENCE","reversibility":"PARTIALLY_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"KNOWN_PATTERN"},"pathFamilies":["docs/baselines/","docs/work_orders/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/","docs/reviews/evidence/","docs/reviews/"],"claims":["one fresh direct candidate calibration can create independently reviewable successful-parse evidence"],"requiredProof":["current quota and Free Quota Only admission","one-call zero-retry receipt","historical receipt hash unchanged","Local independent rescore or fail-closed rejection"],"operatorCheckpoints":["model substitution","paid exposure","second call","callable seam","G2-T2 experiment"],"forbiddenEffects":["paid exposure","second provider call","historical receipt overwrite","MAO lane","public write","deployment","worker commit"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/audits/CVF_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_2026-09-16.json","completenessClaimChanged":false}}
```

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id ACEL-G2-T2-FRESH-DIRECT-CALIBRATION-T1 --title "G2 T2 Fresh Direct Candidate Calibration" --date 2026-09-16 --base 44464b449033d5e2d51ca9baa4a32d5e66198445 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "ACEL G2 T2 candidate qualification material 36784f6c6" --stdout --include-worker-return-skeleton` |
| generatedProfile | runtime-provider-live plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | current model, fresh receipt, fail-closed parse evidence and one-call ceiling |
| checkerReadAheadConfirmation | dispatch, grant, routing, handoff and closeability sources read |
| docOnlyNewFields | fresh calibration admission, parse-failure rejection, old receipt hash |
| claimBoundary | dispatch provenance only; no provider result |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033 and ADIF-0044; truncated 10/24.
Impact: exact call/path scope, independent receipt review and secret boundary.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_semantic_convergence_control.py` |
| literalTokensReviewed | grant fields, dispatch shape, SCEC, review telemetry, trace labels |
| gateRunPurpose | confirm source-verified dispatch, not discover first requirements |
| claimBoundary | checker agreement is not live proof |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher |
| Provider or surface | local private CVF workspace |
| Session or invocation | ACEL G2 T2 calibration authoring, 2026-09-16 |
| Working directory | repository root |
| Command or tool surface | startup reads, source inspection, official docs, apply_patch, governance gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | operator agreement 2026-09-16 and accepted T0 qualification |
| Before status evidence | clean worktree at `44464b449033d5e2d51ca9baa4a32d5e66198445` |
| After status evidence | two draft dispatch artifacts |
| Diff evidence | `git status --short`; `git diff --check` |
| Approval boundary | bounded calibration packet; worker execution only after dispatch-ready gate |
| Claim boundary | no call during packet authoring |
| Agent type | dispatcher |
| Invocation ID | `acel-g2-t2-fresh-direct-calibration-t1-dispatch-20260916` |
| Expected manifest | paired baseline and work order |
| Actual changed set | same two paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

One direct calibration point only. No historical result resurrection,
production effect, public export, callable seam or A/B value claim.
