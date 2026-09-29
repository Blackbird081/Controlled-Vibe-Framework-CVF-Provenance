# CVF Agent Work Order - ACEL G2 T2 Real-Agent Experiment Design

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

## Dispatch Prompt Envelope

Batch ID: ACEL-G2-T2-REAL-AGENT-EXPERIMENT-DESIGN

Dispatch base head: `9cf7fd62e988bd760a27a2e585b5c6a543cdbbc5`

dispatchBaseHead: `9cf7fd62e988bd760a27a2e585b5c6a543cdbbc5`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

Worker: INTERNAL_AGENT design and source-verification worker.

Role: INTERNAL_AGENT experiment designer and evidence mapper; never reviewer
or closer.

Reviewer/closer: Local reviewer/closer.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_2026-09-16.md`

Worker return path: `docs/reviews/CVF_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_WORKER_RETURN_2026-09-16.md`

Current-time notes: operator explicitly approved G2-T2 on 2026-09-16 at clean
continuity HEAD `9cf7fd62e988bd760a27a2e585b5c6a543cdbbc5`.

Do-not-misread notes: this is design and candidate qualification. It does not
authorize agent/subagent execution, provider/live calls, credential access,
runtime implementation, production wiring or automatic successor execution.

Required first actions: read `AGENTS.md`, startup surfaces, guard orientation,
literal gotchas, the paired baseline, this packet, the nine named source files
and applicable checker sources; capture HEAD and status; run pre-implementation
before writing.

Return contract: create exactly three declared outputs, run the required gates,
leave all changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Produce a source-backed, execution-ready design for a bounded ACEL G2 T2
fixed-versus-dynamic real-agent topology experiment without executing it.
Determine whether an accepted harder task and truthful current composition
seam exist; otherwise park the tranche with exact reopen evidence.

## Authority Chain

1. `ECOSYSTEM/doctrine/` and `ECOSYSTEM/operating-model/`.
2. `AGENTS.md`, canonical standards and active continuity.
3. Operator approval of G2-T2 on 2026-09-16.
4. Paired GC-018 baseline and this work order.
5. Accepted T1 completion and existing MAO/Model Gateway owners.

External research is closed. The shared-workspace worker is INTERNAL_AGENT;
Local owns private verification and final technical disposition.

## Target / Source

The worker must fully read and terminally account for exactly these nine source
artifacts:

1. `docs/reviews/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_COMPLETION_2026-09-16.md`
2. `docs/audits/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_RESULT_2026-09-16.md`
3. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/runtime.topology.experiment.contract.ts`
4. `docs/roadmaps/CVF_MAO_LIVE_PROVIDER_ADAPTER_VALUE_PILOT_ROADMAP_2026-07-12.md`
5. `docs/reviews/CVF_MAO_LIVE_T1_PROVIDER_ADAPTER_VALUE_PILOT_COMPLETION_2026-07-12.md`
6. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/live.provider.value.pilot.ts`
7. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts`
8. `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts`
9. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts`

Provider-specific memory, chat history and external synthesis are not source
authority. Any fact not supported by these or another explicitly cited
CVF-governed source must be marked source-not-found with reason.

## Scope / Methodology

Perform a read-only source and evidence audit, then design one bounded future
experiment. Reconcile the T1 policy vocabulary with current MAO and Model
Gateway owners. Do not assume that source existence means composition exists.

The design must answer:

- what exact current symbol launches a real worker/provider action;
- whether that symbol consumes the T1 route decision;
- whether `A_FIXED` and `B_DYNAMIC` can run the same task, authority, provider,
  rubric and budget without hidden differences;
- whether an accepted candidate satisfies the prior harder-task reopen rule;
- how grading remains independent from the output-producing worker;
- how lane order is predeclared and protected from adaptive prompt tuning;
- how calls, tokens, latency and orchestration overhead are measured;
- what exact condition triggers delegation, parallelization, reclaim or
  escalation in the selected treatment;
- what stops the run and what evidence may never be interpreted as success;
- what exact paths a later implementation/execution packet would own.

## Roadmap-To-Work-Order Trace Matrix

| Upstream requirement | Work-order control | Disposition |
|---|---|---|
| T1 completion requires real tasks, independent grading, order control, cost accounting and stop rules | Required design decisions, acceptance criteria and exact three-output contract | RELEASED_TO_DESIGN |
| MAO-LIVE-T1 prohibits repeating the easy 100/100 task | candidate admission rule and duplicate-task rejection disposition | BINDING |
| MAO-LIVE roadmap caps a reopened run at one provider, four calls, one revision and 50-percent latency overhead | future-execution ceiling and stop-rule requirements | BINDING_FOR_DESIGN |
| Local must decide whether present owners are actually composed | callable-edge source mapping and exact successor-or-blocker manifest | DESIGN_CONTROL_ACCEPTED |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G2-T2-REAL-AGENT-EXPERIMENT-DESIGN
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
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "acel-g2-runtime-topology-experiment",
  "chainMode": "SUCCESSOR",
  "chainOrdinal": 1,
  "predecessor": {
    "path": "docs/reviews/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_COMPLETION_2026-09-16.md",
    "sha256": "5abefe1d068291e33f73ba0999d8a326bb36e5b5f3f1acfec9b7ea34d27d31fa"
  },
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": ["g2_real_agent_value_not_proven", "g2_t2_design_and_candidate_not_yet_qualified"],
    "reopened": [],
    "current": ["g2_real_agent_value_not_proven", "g2_t2_design_and_candidate_not_yet_qualified"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 1
  },
  "claims": [{
    "claimId": "ACEL-G2-T2-DESIGN-DISPATCH",
    "claimClass": "DOCUMENTATION_ONLY",
    "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
    "evidenceRef": "docs/baselines/CVF_GC018_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_2026-09-16.md"
  }],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G2-T2-REAL-AGENT-EXPERIMENT-DESIGN","requestedProfile":"P2_BOUNDED","classification":{"taskKind":"DOC_CHANGE","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/baselines/","docs/work_orders/","docs/audits/","docs/reviews/"],"claims":["a bounded source-backed design can decide whether G2 T2 is executable without spending a provider call"],"requiredProof":["nine-source terminal ledger","candidate admission evidence","policy-to-owner mapping","grader independence","randomization control","cost and stop rules","exact next-manifest or parked blocker","independent Local review"],"operatorCheckpoints":["actual agent execution","provider/live execution","credential use","runtime implementation","production integration","public sync"],"forbiddenEffects":["agent or subagent invocation","provider call","credential access","network effect","source or test mutation","new adapter","worker commit","automatic execution successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/audits/CVF_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_MANIFEST_2026-09-16.json","completenessClaimChanged":false}}
```

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| intake summary | operator-approved successor to accepted G2 T1 |
| scope classification | bounded local design and source verification |
| risk sensitivity | P2 because it composes runtime/live owners but authorizes no execution |
| selected role route | `SINGLE_AGENT_MULTI_ROLE` for design and evidence mapping; Local reviews |
| role separation basis | worker returns three uncommitted docs; Local accepts, repairs and commits |
| escalation condition | any provider/live action, credential need, source mutation, missing authority or scope expansion |

## Worker Autonomy / No-Question Rule

Repair allowed-scope document/checker defects directly. Do not ask routine
format questions. Stop only for a source contradiction, forbidden-path need,
missing authority, or inability to make a truthful terminal design decision.

## Agent Roles

| Role | Responsibility |
|---|---|
| operator | selected G2-T2; retains actual execution and external-effect checkpoints |
| dispatcher | freezes source corpus, decisions, ceilings and outputs |
| worker | audits sources, qualifies candidate, authors exact three outputs; does not commit |
| reviewer/closer | evaluates returned evidence and owns any bounded repair and commit |
| session-sync steward | updates continuity only after accepted material |

## Required First Reads

- `AGENTS.md`, startup front door, bootstrap model and active handoff.
- `docs/reference/guard_orientation/README.md` and literal-format gotchas.
- Paired baseline and this work order in full.
- All nine sources under Target / Source.
- Applicable checker sources before writing each output.

## Write Ownership

Worker owns exactly the three paths in the Required Artifact Manifest. All
other paths are read-only. The worker may not stage or commit.

## Execution Plan

1. Capture full HEAD and status; require the committed dispatch continuity
   commit in ancestry; run pre-implementation.
2. Fully read the nine-source manifest and record terminal statuses/hashes.
3. Build a source-backed owner/composition matrix; distinguish present owner,
   callable seam, missing wiring and forbidden inference.
4. Audit existing accepted evidence for a candidate at or below 80/100 or a
   rubric-defined material defect. Spend zero provider calls.
5. Freeze the policy mapping, task/rubric, independent grader, order control,
   metrics, call/token/latency ceilings and stop rules.
6. Emit either an exact next implementation/execution manifest or a parked
   blocker with reopen evidence.
7. Write the worker return, run the worker-return fast gate and return
   uncommitted.

## Required Artifact Manifest

Work-Order Fulfillment Manifest: REQUIRED_EXACT_THREE_PATHS

| Path | Required action |
|---|---|
| `docs/audits/CVF_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_2026-09-16.md` | create human-readable design and terminal disposition |
| `docs/audits/CVF_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_MANIFEST_2026-09-16.json` | create machine-readable source ledger, design contract and exact next manifest/blocker |
| `docs/reviews/CVF_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_WORKER_RETURN_2026-09-16.md` | create complete no-commit worker return |

Every other path is forbidden. No delete, rename, source/test/package change,
session mutation, generated aggregate edit, key access or runtime action.

## Design Contract

### Allowed terminal dispositions

Exactly one:

- `DESIGN_READY_FOR_SEPARATE_EXECUTION_WORK_ORDER`
- `BLOCKED_NO_QUALIFIED_CANDIDATE`
- `BLOCKED_RUNTIME_COMPOSITION_GAP`
- `REJECT_DUPLICATE_MAO_LIVE_T1`

`DESIGN_READY_FOR_SEPARATE_EXECUTION_WORK_ORDER` is allowed only when all
dependency and admission rows pass. It does not itself authorize execution.

### Policy mapping

| Policy | Required design |
|---|---|
| `A_FIXED` | one fixed topology selected before execution; no route change after observed evidence |
| `B_DYNAMIC` | same task/authority/provider/rubric/budget, but one or more T1 actions may occur only through a named callable seam and recorded runtime evidence |

The worker must state how each of `NO_DELEGATE`, `DELEGATE`, `PARALLELIZE`,
`RECLAIM` and `ESCALATE` maps to current owners or is excluded with reason.
Silence is invalid. No action may expand owned paths, risk ceiling, sandbox,
provider grant, call ceiling or commit authority.

### Candidate qualification

The selected task must:

- be materially harder than the closed prime-number task;
- have accepted local direct-lane evidence at most 80/100 or one explicit
  rubric-defined material defect;
- support an objective grader independent from the output-producing worker;
- name the defect class the treatment reviewer can detect;
- be solvable within one provider lane and four total live calls;
- need no production mutation or private data release.

Without all six, return `BLOCKED_NO_QUALIFIED_CANDIDATE`.

### Independent grader

The grader must be deterministic or otherwise independent from the worker
under test. A second provider/model judge call is forbidden in the proposed
ceiling unless it is explicitly counted and independently justified; the
preferred route is a local rubric with exact observable assertions. Worker
self-report is never quality evidence.

### Randomization and contamination control

Predeclare the lane order or deterministic seed before any future call. Freeze
task prompt, rubric, authority, model/provider lane, temperature/options and
budgets. Do not tune prompts or change the candidate after seeing either lane.
If carryover cannot be controlled within four calls, block the design.

### Cost and stop rules

The manifest must include:

- maximum four provider calls and maximum one treatment revision;
- input/output token evidence per call; unknown is never zero;
- wall-clock latency per lane and orchestration-only overhead;
- 50-percent latency-overhead ceiling;
- quality admission before cost comparison;
- hard stop on grant denial, secret exposure, authority drift, incomplete
  receipt, ambiguous grader output, retryable failure without diagnosis, or
  any required fifth call;
- no repeat solely to obtain a preferred result.

### Required next-manifest fields

If ready, list every proposed future path and classify it as existing-modify,
new-create or read-only. Name implementation owner, execution owner, provider
grant subject/delegation/maxCalls/expiry policy, receipt path, result path,
tests, commands and closure owner. No wildcard or directory-wide ownership.

## Evidence Requirements

- Nine source rows with path, SHA-256, terminal status and extracted fact.
- Explicit current composition graph: T1 policy -> topology action -> launcher
  or live bridge -> Model Gateway -> grader -> receipt -> Local review.
- Every missing edge marked `GAP`, never inferred.
- Candidate evidence locator or explicit no-candidate negative result.
- A/B equality matrix for task, authority, provider/model, rubric and budget.
- Five-action owner/disposition table.
- Independent grading and contamination-control proof.
- Exact metric formulas and success/failure thresholds.
- Exact future manifest or parked reopen condition.
- Zero agent/provider calls and zero credential access in this tranche.

## Acceptance Criteria

- Exactly three worker-owned paths and no staging/commit.
- All nine sources terminally accounted; manifest count reconciles 9/9.
- No current owner is promoted from source presence to composed execution.
- Prior MAO-LIVE easy-task result and all five reopen conditions are preserved.
- Candidate is admitted only with accepted evidence; otherwise blocked.
- Design contains the policy, grader, order, cost and stop controls required by
  T1 completion.
- JSON and Markdown agree on disposition, candidate, ceilings and next paths.
- No placeholder, credential value, raw request body or provider-local memory.
- Worker-return fast and `git diff --check` pass.

## Findings / Position

Dispatch position: T2 design is worth executing because T1 closed the
decision-contract gap, but CVF already has a prior easy live comparison that
found no value. The worker must reconcile and reuse those owners rather than
create a duplicate experiment or assume a qualified harder candidate exists.

## Review Gate

Local reviews the returned mapping and manifest without recreating the source
audit. A focused source/hash/candidate sample is sufficient unless a named
contradiction appears. Passing structural gates cannot substitute for the
semantic candidate and composition decision.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with one allowed terminal disposition,
exact three-path status, current gates and zero external effects. Return
`BLOCKED_WITH_REASON` when a source contradiction or forbidden-scope
dependency prevents a truthful terminal design.

## Operator Checkpoint

No additional checkpoint is required inside this design tranche. Stop before
source/runtime implementation, agent/subagent invocation, provider/live run,
credential access, quota consumption, public sync, deployment or production.
A future execution work order is separately governed even if this design is
accepted.

## Pre-Flight And Verification Commands

```powershell
git rev-parse HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --cached --name-only
git status --short
```

The worker must not run any live runner, provider smoke test, release gate
bundle, agent launcher or command that reads `.env.local`.

## Verification Commands

The required verification sequence is the pre-implementation autorun command
above, followed after authoring by:

```powershell
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --cached --name-only
git status --short
```

No individual checker invocation substitutes for the worker-return fast gate.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_WORKER_RETURN_2026-09-16.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

Required terms: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; executionBaseHead; nine-source
reconciliation; terminal disposition; candidate admission; composition graph;
exact three-path manifest; zero provider calls; Agent Operation Trace Block;
Claim Boundary; Delta Execution Claim Boundary Control Block; External
Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness
And Report Integrity; Knowledge System Reconciliation;
Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine
Closure Package; Public Export Disposition; git status --short; N/A with reason
instruction.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | source auditor, experiment designer and evidence producer; never reviewer/closer |
| phase | design and candidate qualification |
| baseHeadFor(phase) | dispatchBaseHead=`9cf7fd62e988bd760a27a2e585b5c6a543cdbbc5`; executionBaseHead captured at start; closureBaseHead owned by Local |
| changedSetScope(phase) | exact three worker paths |
| traceScope(phase, actor) | source hashes, terminal ledger, candidate evidence, design decisions, gates and status |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | clean worktree required; no unrelated path or active lane may be touched |
| nextMoveSurfaces | worker return only; Local decides design acceptance and any later packet |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT design worker

laneOwnedPaths: exact three paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return with empty staging and exact changed set

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| Applicability | applies because the worker audits, maps and designs within one no-commit role |
| actor | INTERNAL_AGENT worker |
| role set | source auditor, design author and evidence producer; never reviewer/closer |
| Role separation ledger | worker returns uncommitted; Local independently accepts or rejects |
| Evidence basis independent of memory | governed source paths, hashes, terminal ledger and machine gates |
| Gate sequence | pre-implementation; source reconciliation; worker-return fast; Local review |
| Self-review boundary | worker may repair owned docs but cannot accept its own design |
| escalation condition | missing authority, candidate evidence, callable seam, or need for external effect |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_COMPLETION_2026-09-16.md` |
| reviewerOwnedClosurePaths | optional completion review, work-order status, material commit and later continuity commit |
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
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker paths plus reviewer closure | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | reviewer completion path | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | T1, MAO and Model Gateway owner mapping in the three design outputs | read-only source audit; no execution or mutation | exact governed sources and hashes | future internal execution seam must be explicitly selected | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no T2 CLI/MCP execution owner in this tranche | no ingress, auth, credential, mutation or public authority | source-not-opened boundary | separate adapter contract/work order required if later selected | `DEFERRED_WITH_REASON` - not needed to decide the internal experiment design |

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
  "parentArtifact": "docs/reviews/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_COMPLETION_2026-09-16.md"
}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | historical external synthesis -> accepted Local T0 -> T1 executable proof -> operator-selected internal T2 design -> Local decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and three private design outputs |
| Disposition | external research is closed; no external agent is invoked in this tranche |
| Claim boundary | historical external input set priority only; current private sources decide feasibility and disposition |

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON

Reason: internal no-call design dispatch; no external invocation and no runtime
implementation is authorized.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO_NEW_RUNTIME_CLAIM |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | current source reads, exact hashes, symbol and consumer mapping |
| reason | design must bind to present owners without executing them |
| requiredFutureAction | separately governed implementation/execution packet if design is accepted |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded nine-source experiment-design corpus.
- Corpus root: exact paths under Target / Source; no directory-wide claim.
- Snapshot time: worker executionBaseHead.
- Enumeration command: filesystem-backed direct reads of the exact nine-path manifest.
- Manifest artifact or inline manifest: machine JSON design manifest.
- Manifest hash: SHA-256 of sorted path/hash/status rows recorded by worker.
- Processing ledger artifact or inline ledger: nine terminal source rows in the machine manifest.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=9; ledger_terminal=9; exclusions=declared; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: unrelated MAO history, provider keys, live receipts outside cited owners, external repositories and production consumers.
- Unreadable or unsupported files: worker records numeric count and paths.
- Aggregation check: every design claim cites one or more terminal source rows.
- Drift check: PASS
- Output traceability: source ledger -> design decisions -> terminal disposition -> worker return.
- Adversarial verification: reject owner-presence-as-composition, easy-task reuse, self-grading and unknown-as-zero.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Knowledge System Reconciliation

- Knowledge task class: T1-to-T2 runtime experiment design projection.
- Source manifest: exact nine-path bounded manifest.
- Source manifest hash: worker-generated from path/hash/status rows.
- Enumeration safety: filesystem-backed exact-path reads.
- Intake registry or ledger: machine design manifest.
- Authority assets: paired baseline, this work order and accepted T1 completion.
- Derived views: human design and worker return.
- Semantic region ledger: policy, execution owner, candidate, grader, order, cost, stop and next-manifest regions.
- Region reconciliation: assets=9; mapped=9; deferred=0; unmapped=0 required for ready disposition.
- Orphan or unmapped assets: none.
- Cross-region links: claim IDs bind source rows to decisions.
- Drift check: PASS
- Rebuildability check: machine manifest plus named sources rebuild the human decision.
- Retrieval boundary: design readiness only.
- Adversarial verification: no runtime/source presence may be promoted to composed execution without a callable edge.
- Knowledge-map verdict: RECONCILED_WITH_DECLARED_GAPS

## Finding-To-Governance Learning Disposition

Do not create a new governance rule from design observations. If the audit
finds a recurring owner/composition defect, record it in the design as a
candidate only; Local decides later promotion.

Runtime/provider/cost learning lane: record exact runtime-owner, provider-call,
token/cost/latency and stop-rule requirements, but make no observed live claim.

## Foundation Storage Layout Block

N/A with reason: this tranche creates three flat design/evidence documents and
does not create or mutate durable foundation storage, registries, generated
aggregates, runtime state, queues, indexes or rebuild pipelines.

## Epistemic Process Block

- Expected Result / Prediction: current owners may support a bounded experiment design, but a qualified harder task or composition seam may still be missing.
- Evidence Comparison: compare source-visible owners and accepted receipts against every candidate and composition admission rule.
- Contradiction Or Gap Disposition: missing candidate or callable seam produces a terminal parked blocker, not invented readiness.
- Claim Update: only Local review may accept an execution-ready design; no execution or value claim follows automatically.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | source-backed G2 T2 experiment design and candidate qualification only |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception or live behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created in this design tranche |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no agent, topology or provider action is executed |
| invocationBoundary | local file reads, hashes and governance gates only |
| interceptionBoundary | no agent/provider/IDE/shell/git/filesystem interception claim |
| claimLanguage | design readiness or parked blocker, never observed real-agent value |
| forbiddenExpansion | source/runtime mutation, agent/provider/live call, credential access, production, public and deployment |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033 and ADIF-0044; resolver result was
truncated at 10 of 24 candidates.

Dispatch impact: exact bounded manifest; CVF-governed authority only; checker
read-ahead; explicit no-absorption boundary; per-source evidence; no protected
path; no provider authority; no timeout longer than the parent lane.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G2-T2-DESIGN --title "ACEL G2 Real-Agent Topology Experiment Design" --date 2026-09-16 --base 9cf7fd62e988bd760a27a2e585b5c6a543cdbbc5 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic no-commit worker dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact three-path design scope, nine-source ledger, prior MAO reopen rules, candidate/composition gates and zero-call boundary |
| checkerReadAheadConfirmation | dispatch, prompt, convergence, routing, handoff, closeability, trace, provider authority, external routing and Delta checkers |
| docOnlyNewFields | candidateAdmission; policyMapping; graderIndependence; orderControl; costCeiling; stopRules; compositionGap; nextManifest |
| claimBoundary | dispatch authoring only; no runtime or live readiness |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T1 is proposal-only executable proof | CLAIM_BOUNDARY | `docs/reviews/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_COMPLETION_2026-09-16.md` | Purpose; Decision | T2 checkpoint | Local completion | ACCEPT |
| T2 requires task, grader, order, cost and stop rules | VALUE_SET | `docs/reviews/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_COMPLETION_2026-09-16.md` | Risk / Corrective Action | five controls | Local completion | ACCEPT |
| prior live easy task tied 100/100 and added latency | RISK_FACT | `docs/reviews/CVF_MAO_LIVE_T1_PROVIDER_ADAPTER_VALUE_PILOT_COMPLETION_2026-07-12.md` | Findings / Position | accepted value-not-proven verdict | MAO-LIVE completion | ACCEPT |
| new live proposal requires accepted harder candidate and explicit ceilings | VALUE_SET | `docs/roadmaps/CVF_MAO_LIVE_PROVIDER_ADAPTER_VALUE_PILOT_ROADMAP_2026-07-12.md` | Next Allowed Move | concrete reopen condition | MAO-LIVE roadmap | ACCEPT |
| T1 defines five topology actions with provider forbidden | LITERAL_INVARIANT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/runtime.topology.experiment.contract.ts` | types and AuthorityEnvelope | `RouteAction`; `providerExecutionAuthority` | T1 contract | ACCEPT |
| MAO bridge supplies direct and governed live lanes | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/live.provider.value.pilot.ts` | lane functions | `runDirectLane`; `runMaoLane` | MAO live bridge | ACCEPT |
| operational launcher is separate from live bridge | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | class and adapter port | `MaoOperationalWorkerLauncher` | MAO launcher | ACCEPT |
| Model Gateway harness is the existing call owner | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | live proof function | `runLiveProof` | Model Gateway | ACCEPT |
| provider calls require exact bounded grant | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` | grant evaluator | `evaluateProviderExecutionAuthority` | delegation contract | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact five proposed paths | all returned `False` before authoring | NO_COLLISION |
| exact token search | no prior ACEL G2-T2 artifact found in `docs` or `CVF_SESSION` | NO_COLLISION |
| related owner search | T1, MAO-LIVE, MAO launcher and Model Gateway owners exist | REUSE_OR_DECLARE_GAP |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_core.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | ready status, first prompt section, source columns, initial dispatch sentinels, successor convergence fields, route enums, exact return contract, gate graph, trace fields and forbidden provider authority |
| gateRunPurpose | confirm the packet shape before pre-dispatch, not discover semantics after dispatch |
| claimBoundary | checker compliance does not prove candidate qualification or runtime composition |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher |
| Provider or surface | local private CVF workspace |
| Session or invocation | ACEL-G2-T2 real-agent experiment design dispatch, 2026-09-16 |
| Working directory | repository root |
| Command or tool surface | startup reads, governed-source inspection, collision search, ADIF resolver, scaffold stdout, apply_patch and dispatch gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | user authorization `Dong y G2-T2` on 2026-09-16 |
| Before status evidence | clean worktree at HEAD `9cf7fd62e988bd760a27a2e585b5c6a543cdbbc5` |
| After status evidence | exact two dispatch artifacts pending material commit |
| Diff evidence | `git status --short`; `git diff --check` |
| Approval boundary | internal design/candidate qualification only |
| Claim boundary | no actual agent/provider execution, runtime mutation, public effect or production claim |
| Agent type | dispatcher |
| Invocation ID | `acel-g2-t2-real-agent-design-dispatch-20260916` |
| Expected manifest | paired baseline and work order |
| Actual changed set | same two paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This work order authorizes three uncommitted design/evidence documents only.
It does not authorize implementation, actual agent or subagent execution,
provider/live calls, credentials, quota, network access, runtime/production
wiring, public sync or deployment. Acceptance can make a later work order
eligible for authoring; it cannot execute that work automatically.

## Closure Checklist

- [ ] Worker captured and reported the exact execution base HEAD.
- [ ] Exactly nine source rows have terminal statuses and hashes.
- [ ] Exactly three worker-owned outputs exist; no other path changed.
- [ ] One allowed terminal disposition is explicit and evidence-backed.
- [ ] Candidate admission and callable composition are accepted or truthfully blocked.
- [ ] Pre-implementation and worker-return fast gates pass.
- [ ] Staging is empty and no provider, credential, network or live effect occurred.
- [ ] Local reviewer records the final accept, repair or reject decision.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private G2-T2 experiment design; no public-safe artifact is authorized.
