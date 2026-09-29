# CVF Agent Work Order - ACEL G2 T2 Candidate Qualification T0

Memory class: governed-worker-dispatch

docType: work_order

Status: READY_FOR_DISPATCH

Batch ID: ACEL-G2-T2-CANDIDATE-QUALIFICATION-T0

Dispatch base head: `eb88000344966c08209c155be8f70f53b501b0d8`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

Worker: one INTERNAL_AGENT evidence worker

Reviewer/closer: Local

Worker return path: `docs/reviews/CVF_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_WORKER_RETURN_2026-09-16.md`

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT evidence worker for ACEL-G2-T2-CANDIDATE-QUALIFICATION-T0.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_2026-09-16.md`

Paired baseline: `docs/baselines/CVF_GC018_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_2026-09-16.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture `git rev-parse HEAD` before editing; it must equal
the committed dispatch-continuity HEAD supplied by Local.

Current-time notes: packet date is 2026-09-16; current filesystem bytes and
hashes control, not historical memory.

Do-not-misread notes: this is candidate qualification, not fresh calibration,
real-agent execution, provider authority, seam implementation, or G2-T2 value proof.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, paired baseline, this work order, all twelve sources, and applicable
checker sources before creating any output.

Return contract: create exactly three worker-owned paths, run the required
gates, leave changes uncommitted and return `COMPLETE_PENDING_REVIEW` or one
evidence-backed blocker.

## Purpose

Audit whether the existing MAO-OA-T6A hard-task contract is reconstructable
and suitable for a separately governed fresh direct-lane calibration. Preserve
the rejected historical result and prevent task readiness from being confused
with an accepted live score or permission to execute.

## Authority Chain

Operator `next` authorizes the candidate-qualification branch named by active
continuity. The paired GC-018 baseline bounds the corpus and outputs. This work
order binds worker execution. Local remains final reviewer/closer and alone may
author a later calibration packet.

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | selected the candidate-qualification branch |
| Local dispatcher | freezes sources, scope, outputs and forbidden effects |
| INTERNAL_AGENT worker | reads sources and returns three uncommitted evidence paths |
| Local reviewer/closer | verifies semantics, repairs closeable evidence defects, commits or rejects |
| External agent | not invoked; historical research remains advisory only |

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
2. `CVF_SESSION_MEMORY.md`
3. `AGENT_HANDOFF_V60_2026-09-08.md`
4. `docs/reference/guard_orientation/README.md`
5. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
6. paired baseline and this work order
7. all twelve exact sources and applicable output checkers

## Pre-Flight Checks

- Confirm HEAD equals the Local-supplied execution base and worktree is clean.
- Confirm all three worker output paths are absent.
- Run pre-implementation autorun before evidence authoring.
- Stop on any missing/unreadable source or unrelated worktree path.
- Do not run TypeScript, package, provider, credential, network or live commands.

## Write Ownership

Worker write ownership is exactly the three paths in Required Artifact
Manifest. All existing files are read-only. Staging and commits are forbidden.

## Execution Plan

1. Capture HEAD/status and run pre-implementation gate.
2. Hash and terminally account all twelve exact sources.
3. Reconstruct task, parser, rubric, defects and prospective evidence shape.
4. Preserve the historical result rejection.
5. Compare candidate hardness/novelty against the excluded easy task.
6. Select exactly one terminal decision and record downstream blockers.
7. Run worker-return fast gate and return uncommitted evidence.

## Evidence Requirements

Evidence must be source-located, independently reconstructable, secret-safe,
and explicit about unknowns. Every decision field must cite source-ledger row
IDs. Hashes do not substitute for absent scorer input, and source presence does
not prove runtime use.

## Acceptance Criteria

- Exact 12/12 source reconciliation with current hashes and zero unresolved.
- Exact three-path changed set; empty staging; unchanged HEAD.
- Historical T6A score/defect/release claims remain not accepted.
- Qualification decision uses only the three allowed terminal values.
- Candidate comparison covers all seven dimensions in section C.
- Worker-return fast gate and diff hygiene pass.
- Zero provider, agent, credential, network, runtime, public or deploy effect.

## Review Gate

Local evaluates returned evidence without recreating the audit. Reviewer-fast
and pre-commit gates are mandatory before material commit. One consolidated
repair is preferred for any closeable evidence-shape defect.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all three artifacts and gates are
complete. Return `BLOCKED_WITH_REASON` for missing authority, unreadable source,
necessary scope expansion, or forbidden-effect dependency.

## Operator Checkpoint

An accepted `QUALIFIED_FOR_FRESH_DIRECT_CALIBRATION_PACKET` returns to the
operator before any provider call. It does not auto-dispatch calibration,
callable-seam implementation, or the G2-T2 experiment.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| intake summary | recover one existing private-CVF harder-task candidate from current governed sources |
| scope classification | bounded read-only candidate qualification |
| risk sensitivity | P2 documentation/evidence; principal risk is resurrecting rejected live evidence |
| selected role route | `MULTI_AGENT_MULTI_ROLE` |
| role separation basis | historical external research ended; Local dispatches; one internal worker audits; Local decides |
| escalation condition | source contradiction, fourth output, provider/live need, source/runtime mutation or candidate ambiguity |

## Target / Source

The exact twelve-source corpus is specified by the paired baseline. The worker
must not add supplemental sources silently. A necessary source outside that
manifest produces `BLOCKED_TASK_NOT_RECONSTRUCTABLE` with the missing path and
reason; Local decides whether a later packet expands the corpus.

## Required Artifact Manifest

Work-Order Fulfillment Manifest: REQUIRED_EXACT_THREE_PATHS

| Artifact | Required worker action |
|---|---|
| `docs/audits/CVF_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_2026-09-16.json` | create machine ledger with 12 source rows, hashes, extracted facts, candidate comparison, qualification decision, downstream blockers and zero-effect counters |
| `docs/audits/CVF_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_2026-09-16.md` | create human audit with task/result separation, independent-rescoring analysis and one allowed terminal decision |
| `docs/reviews/CVF_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_WORKER_RETURN_2026-09-16.md` | create full worker return with actual commands, gates, status and no-commit proof |

No baseline, work order, source, test, runner, receipt, registry, session,
handoff, checker, hook, runtime, public, or deployment path may change.

## Acceptance Contract

### A. Source reconciliation

- Exactly twelve manifest rows.
- SHA-256 and byte count recomputed from current bytes.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`,
  `BLOCKED_UNREADABLE`.
- Ready qualification requires all twelve rows `READ`, zero unresolved, and
  byte/hash drift explicitly reported.

### B. Task versus historical result

The worker must keep these propositions distinct:

1. the T6A task contract may be reconstructable;
2. the repaired runner may be capable of persisting sanitized candidate data;
3. the 2026-07-17 provider result remains non-recomputable and `NOT_ACCEPTED`;
4. qualifying the task permits only a later Local dispatch decision.

Any artifact accepting or rescoring the historical 100/100 claim fails review.

### C. Hardness and novelty comparison

Compare T6A with the excluded prime-number task using source-backed fields:

- structured output/schema obligations;
- multi-dimensional deterministic rubric;
- explicit risk and rollback reasoning;
- material-defect classes;
- independent rescoring from sanitized candidate data;
- plausible one-revision review hypothesis;
- semantic non-equivalence to the earlier easy task.

Do not claim that complexity alone proves a low score or value gain.

### D. Evidence readiness

Inspect, without executing, whether current runner and contract code can emit
the sanitized parsed candidate, raw-response hash, provider/model metadata,
usage, latency, call count, retry count, score dimensions, defects and release
boolean needed for independent review. Record missing fields as blockers.

### E. Terminal decision

Exactly one:

- `QUALIFIED_FOR_FRESH_DIRECT_CALIBRATION_PACKET`
- `BLOCKED_TASK_NOT_RECONSTRUCTABLE`
- `REJECTED_DUPLICATE_OR_EASY`

Qualification is a documentation/evidence result only. It does not satisfy
the later direct-lane admission threshold of accepted score at or below 80/100
or an independently accepted material defect.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G2-T2-CANDIDATE-QUALIFICATION-T0
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
  "problemKey": "acel-g2-t2-candidate-qualification-t0-problem",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": ["NO_QUALIFIED_HARDER_CANDIDATE", "NO_CALLABLE_T1_TO_MAO_CONSUMER"],
    "reopened": [],
    "current": ["NO_QUALIFIED_HARDER_CANDIDATE", "NO_CALLABLE_T1_TO_MAO_CONSUMER"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{"claimId":"ACEL-G2-T2-CQ-T0","claimClass":"DOCUMENTATION_ONLY","proofClass":"PROPOSAL_ONLY_NO_RUNTIME_READINESS","evidenceRef":"docs/baselines/CVF_GC018_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_2026-09-16.md"}],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "NO_SUCCESSOR"
}
```

## Worker Autonomy / No-Question Rule

Repair allowed-scope artifact defects directly after reading the failing
checker. Return early only for source contradiction, unreadable required
source, necessary out-of-scope mutation, or authority expansion.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | one INTERNAL_AGENT performs source audit, qualification analysis and evidence packaging; Local reviews/closes |
| phase | CANDIDATE_QUALIFICATION |
| baseHeadFor(phase) | dispatchBaseHead=`eb88000344966c08209c155be8f70f53b501b0d8`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact three worker paths |
| traceScope(phase, actor) | source hashes, task/result separation, comparison, terminal decision, gates and status |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | clean worktree required; no other lane or path may be touched |
| nextMoveSurfaces | worker return only; Local decides whether to author fresh calibration or park |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT evidence worker

laneOwnedPaths: exact three paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return with empty staging and exact changed set

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | optional; prefer Local repair in worker return when closeable |
| reviewerOwnedClosurePaths | optional completion review, material commit, then separate continuity commit |
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
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | active continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| source_reconciliation | WORKER_RETURN | worker | IMPLEMENTATION | exact three worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact three worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | source_reconciliation |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | pre_commit |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| Applicability | applies because one worker audits and packages the evidence |
| actor | INTERNAL_AGENT worker |
| role set | source auditor, candidate analyst, evidence producer; never reviewer/closer |
| Role separation ledger | worker returns uncommitted; Local independently decides |
| Evidence basis independent of memory | twelve exact governed sources and hashes |
| Gate sequence | pre-implementation, source reconciliation, worker-return fast, Local review |
| Self-review boundary | worker cannot accept its own qualification result |
| escalation condition | missing source, contradiction, external effect or out-of-scope mutation |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | twelve-source audit and three output documents | read-only evidence work; zero execution | exact source hashes and terminal ledger | later calibration requires a separate work order | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | none | no CLI/MCP ingress, provider call, credential or mutation | external invocation ceiling zero | separate adapter contract required | `DEFERRED_WITH_REASON` |

## External/Local Coordination Binding

```json
{
  "contractId": "cvf.external-local-absorption-coordination@1",
  "invariants": {
    "externalRole": "ADVISORY_RESEARCH_AND_PATTERN_MAPPING",
    "externalContext": "PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ",
    "localRole": "SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION",
    "finalDecisionOwner": "LOCAL",
    "localCoverageBasis": "SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST",
    "externalEvidenceAuthority": "INPUT_NOT_PRIVATE_CVF_PROOF"
  },
  "contractSha256": "92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c",
  "parentArtifact": "docs/baselines/CVF_GC018_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_2026-09-16.md"
}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | historical external research -> Local ACEL T0/T1 -> blocked G2-T2 design -> Local T6A candidate recovery audit |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and three private evidence outputs |
| Disposition | external research remains closed; no external agent is invoked |
| Claim boundary | private current sources decide qualification; historical external priority is not evidence |

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON

Reason: read-only internal evidence dispatch; no external invocation or runtime
implementation is authorized.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO_NEW_RUNTIME_CLAIM |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | current exact-path reads, hashes, source symbol inspection and non-executing evidence-shape analysis |
| reason | task qualification must use current source without executing it |
| requiredFutureAction | fresh Local calibration packet if qualification is accepted |

## Corpus Completeness And Report Integrity

- Corpus task class: AUDIT
- Corpus root: exact twelve paths in the paired baseline
- Snapshot time: worker executionBaseHead
- Enumeration command: filesystem-backed direct reads of the twelve exact paths
- Manifest artifact or inline manifest: worker JSON output
- Manifest hash: worker records SHA-256 of canonical source-ledger rows
- Processing ledger artifact or inline ledger: twelve terminal rows in worker JSON
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=12; ledger_terminal=12; exclusions=0; unresolved=0 required for qualification
- Unresolved files: worker records count and paths
- Declared exclusions: every source outside the exact twelve-path manifest
- Unreadable or unsupported files: worker records count and paths
- Aggregation check: each qualification claim links to one or more source rows
- Drift check: current hashes compared with the work-order source verification evidence
- Output traceability: source ledger -> comparison -> terminal decision -> worker return
- Adversarial verification: reject historical score resurrection, task/result conflation, complexity-as-hardness and permission escalation
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Knowledge System Reconciliation

- Knowledge task class: ARCHITECTURE_MAP
- Source manifest: exact twelve-path worker ledger
- Source manifest hash: worker-generated canonical ledger hash
- Enumeration safety: filesystem-backed exact-path reads
- Intake registry or ledger: candidate qualification JSON
- Authority assets: paired dispatch, current blocked design and accepted MAO-OA Local reviews
- Derived views: human qualification audit and worker return
- Semantic region ledger: task, rubric, defect rules, evidence shape, historical result, novelty and downstream blockers
- Region reconciliation: assets=12; mapped=12; deferred=0; unmapped=0 required for qualification
- Orphan or unmapped assets: none
- Cross-region links: claim IDs bind source rows to each decision field
- Drift check: PASS
- Rebuildability check: JSON ledger and named sources rebuild the human decision
- Retrieval boundary: task qualification only; live score and G2-T2 value remain outside
- Adversarial verification: historical rejected result must remain rejected
- Knowledge-map verdict: RECONCILED_WITH_DECLARED_GAPS

## Worker Output Checker Read-Ahead Mandate

Before writing each output, read checker source for its path family and
conditional content. The worker return must contain Purpose, Scope /
Methodology, Findings / Position, Risk / Corrective Action, Claim Boundary,
Checker Source Read-Ahead Block, Agent Operation Trace Block, Delta Execution
Claim Boundary Control Block, Public Export Disposition, executionBaseHead,
actual git status, corpus reconciliation, knowledge reconciliation, external
routing, epistemic process, governance-learning disposition and machine
closure N/A-with-reason.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_WORKER_RETURN_2026-09-16.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
```

No TypeScript runner, test, provider harness, package script, network command,
credential resolver, or live proof command is authorized.

## Foundation Storage Layout Block

N/A with reason: this tranche creates three flat audit/review evidence files
only. It does not create, split, relocate or refactor a durable foundation,
registry, generated aggregate, index, runtime state, queue or rebuild pipeline.

## Finding-To-Governance Learning Disposition

Do not create a new governance rule in this tranche. Record any recurring
task/result conflation or missing evidence-shape issue as a candidate note;
Local decides later promotion. Runtime/provider/cost learning is documentation
only because no call occurs.

## Epistemic Process Block

- Expected Result / Prediction: the T6A task may be qualification-ready even though its historical live result is not accepted.
- Evidence Comparison: compare contract, tests, prospective runner evidence fields, historical receipt and both Local closure assessments.
- Contradiction Or Gap Disposition: missing reconstructability produces a named blocker; it is not repaired by inference or a new call.
- Claim Update: qualification may make a fresh direct-calibration packet eligible for authoring and nothing more.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | read-only source-backed candidate qualification |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception or live behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: historical receipt is inspected but its score/defect claim remains not accepted; no new receipt is created |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no agent, runner, test or provider action is executed |
| invocationBoundary | local file reads, hashes and governance gates only |
| interceptionBoundary | no agent/provider/IDE/shell/git/filesystem interception claim |
| claimLanguage | qualified task or parked blocker, never accepted live score or value gain |
| forbiddenExpansion | provider/live, credential, network, source/runtime mutation, callable seam, public, deploy and production |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033 and ADIF-0044; resolver result was
truncated at 10 of 24 candidates. Impact: exact corpus and output manifests,
per-source authority, checker read-ahead, role-route agreement, no protected
mutation, no external/provider authority, and bounded execution time.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G2-T2-CANDIDATE-QUALIFICATION-T0 --title "ACEL G2 T2 Candidate Qualification" --date 2026-09-16 --base eb88000344966c08209c155be8f70f53b501b0d8 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic no-commit worker dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | twelve-source T6A recovery audit, three-output contract, task/result separation and terminal decisions |
| checkerReadAheadConfirmation | dispatch, convergence, handoff, provider, corpus and external-routing checkers read |
| docOnlyNewFields | taskQualification; historicalResultDisposition; evidenceShape; noveltyComparison; downstreamBlockers |
| claimBoundary | dispatch authoring only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| G2-T2 is blocked first by missing qualified candidate | GAP | `docs/reviews/CVF_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_WORKER_RETURN_2026-09-16.md` | Findings / Position | terminal blocker | Local worker return | ACCEPT |
| T6A result is not independently recomputable | CLAIM_BOUNDARY | `docs/reviews/CVF_MAO_OA_T6A_HARDER_CANDIDATE_DIRECT_BASELINE_CALIBRATION_COMPLETION_REVIEW_2026-07-17.md` | R3-R5; Disposition | missing sanitized candidate | Local completion review | ACCEPT |
| threshold is score at most 80 or material defect | VALUE_SET | `docs/reviews/CVF_MAO_OA_T6A_HARDER_CANDIDATE_DIRECT_BASELINE_CALIBRATION_COMPLETION_REVIEW_2026-07-17.md` | R4 | T6B release rule | Local completion review | ACCEPT |
| current contract defines fixed task, parser, rubric and defects | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/harder.value.candidate.contract.ts` | exported task and evaluator | `evaluateHarderCandidate` | harder candidate contract | ACCEPT |
| prospective runner persists sanitized candidate | EVIDENCE_SHAPE | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-oa-t6a-candidate-calibration.ts` | evidence creation | sanitized candidate field | T6A runner | ACCEPT |
| historical JSON lacks reconstructable scorer input | EVIDENCE_GAP | `docs/reviews/evidence/mao-oa-t6a-direct-candidate-calibration-2026-07-17.json` | evidence payload | sanitized candidate null | T6A evidence | ACCEPT |
| T7 retains result rejection and T6B non-release | CLAIM_BOUNDARY | `docs/reviews/CVF_MAO_OA_T7_FINAL_ROADMAP_CLOSURE_COMPLETION_REVIEW_2026-07-17.md` | Decision | T6B_NOT_RELEASED | Local final closure | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact five proposed paths | all returned `False` before authoring | NO_COLLISION |
| batch token search | no existing governed artifact before authoring | NO_COLLISION |
| owner search | three runtime source/test/runner owners and seven evidence/authority owners found | REUSE_CURRENT_OWNERS |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` |
| literalTokensReviewed | READY_FOR_DISPATCH, first prompt section, source columns, INITIAL dispatch fields, predecessor hash, role route, exact return contract, corpus fields and forbidden authority |
| gateRunPurpose | confirm packet closeability before pre-dispatch |
| claimBoundary | gate compliance does not qualify the T6A task or authorize calibration |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher |
| Provider or surface | local private CVF workspace |
| Session or invocation | ACEL-G2-T2 candidate qualification dispatch, 2026-09-16 |
| Working directory | repository root |
| Command or tool surface | startup reads, governed source inspection, hashes, collision search, ADIF resolver, scaffold stdout, apply_patch and gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | operator request `next` at the explicit candidate-qualification checkpoint |
| Before status evidence | clean worktree at `eb88000344966c08209c155be8f70f53b501b0d8` |
| After status evidence | exact two dispatch artifacts pending material commit |
| Diff evidence | `git status --short`; `git diff --check` |
| Approval boundary | read-only candidate qualification only |
| Claim boundary | no fresh calibration, provider/live, runtime mutation or public effect |
| Agent type | dispatcher |
| Invocation ID | `acel-g2-t2-candidate-qualification-t0-dispatch-20260916` |
| Expected manifest | paired baseline and work order |
| Actual changed set | same two paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This work order authorizes exactly three uncommitted evidence documents and
read-only inspection of twelve current sources. It does not authorize running
the T6A script or tests, invoking an agent/provider, accessing credentials,
performing fresh calibration, implementing the callable seam, executing G2-T2,
mutating runtime/source, public sync, deployment, or production routing.

## Closure Checklist

- [ ] executionBaseHead captured before edits.
- [ ] twelve source rows reconcile with hashes and byte counts.
- [ ] historical result remains explicitly not accepted.
- [ ] task qualification is separated from live-result admission.
- [ ] exactly three worker paths exist and staging is empty.
- [ ] one allowed terminal decision is recorded.
- [ ] pre-implementation and worker-return fast gates pass.
- [ ] zero agent/provider/network/credential/runtime effects recorded.
- [ ] Local reviewer independently accepts, repairs, or rejects the result.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private candidate-selection packet; no public artifact is authorized.
