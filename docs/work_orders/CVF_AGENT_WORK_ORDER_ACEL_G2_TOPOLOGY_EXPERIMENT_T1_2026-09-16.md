# CVF Agent Work Order - ACEL G2 Runtime Topology Experiment T1

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

## Dispatch Prompt Envelope

Batch ID: ACEL-G2-TOPOLOGY-EXPERIMENT-T1

Dispatch base head: `c71176f0af24b804de5cc8e6870c93a493a9f6df`

dispatchBaseHead: `c71176f0af24b804de5cc8e6870c93a493a9f6df`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_CAPTURES_AFTER_WORKER_RETURN`

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

Worker: INTERNAL_AGENT shared-workspace implementation worker.

Role: INTERNAL_AGENT experimental implementer and evidence producer; Local is
the independent reviewer, closer and final decision owner.

Reviewer/closer: Local reviewer/closer.

Worker return path: `docs/reviews/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_WORKER_RETURN_2026-09-16.md`

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_2026-09-16.md`.

Current-time notes: operator explicitly selected G2 on 2026-09-16.

Do-not-misread notes: T1 is a hermetic decision-policy experiment, not the
32 real-agent A/B executions and not production runtime-topology authority.

Required first actions: read `AGENTS.md`, the active startup surfaces, guard
orientation, literal gotchas, paired baseline, current delegation/benchmark
owners, this full work order and applicable checker sources; capture HEAD and
clean status; run pre-implementation before writing.

Return contract: create exactly the declared outputs, run required gates,
leave all changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Implement and execute a deterministic G2 experimental harness that produces
exactly 32 proposal-only run records across eight fixtures, two policies and
two repetitions. Prove lifecycle, authority-envelope preservation, quality
admission and metric aggregation before any real-agent T2 experiment.

## Authority Chain

1. `ECOSYSTEM/doctrine/` and `ECOSYSTEM/operating-model/`.
2. `AGENTS.md`, canonical standards and current Control Plane Foundation owners.
3. Paired GC-018 baseline and this work order.
4. Accepted Local T0 review; preserved external handoff is advisory input only.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G2-TOPOLOGY-EXPERIMENT-T1 --title "ACEL G2 Runtime Topology Experiment Harness And Hermetic 32-Run Oracle" --date 2026-09-16 --base c71176f0af24b804de5cc8e6870c93a493a9f6df --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact experiment boundary, eight-path manifest, 32-run matrix, machine bindings and T2 admission rule |
| checkerReadAheadConfirmation | dispatch, convergence, routing, handoff, trace, Delta, external-intake and closeability checkers |
| docOnlyNewFields | taskClass; policy; repetition; runtimeEvidence; routeAction; admitted; qualityOracle; orchestrationMetrics |
| claimBoundary | dispatch provenance only; no experiment result or production topology claim |

## Target / Source

- Baseline: `docs/baselines/CVF_GC018_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_2026-09-16.md`.
- Accepted T0: `docs/reviews/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_COMPLETION_2026-09-15.md`.
- Current delegation owner: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts`.
- Existing proposal-only benchmark pattern: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/performance.benchmark.harness.contract.ts`.
- External handoff remains advisory input only.

## Scope / Methodology

Create an isolated experimental module; do not modify or export it through a
production barrel. Define a closed policy/action vocabulary, immutable Work
Order authority envelope, runtime evidence inputs, fail-closed transition
rules, quality admission and deterministic metrics. Use eight versioned
fixtures: two bounded research/inspection, two local implementation, two
tightly-coupled cross-module reasoning, and two verification/fault-finding.

Run each fixture under policy A and policy B twice. The runner must assert
exactly 32 unique `(taskId, policy, repetition)` records and byte-stably emit
the receipt. It must fail nonzero on an oracle mismatch, authority-envelope
change, missing/duplicate run, invalid transition, unadmitted comparative
row or unstable regeneration.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G2-TOPOLOGY-EXPERIMENT-T1
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
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {"prior": [], "resolved": [], "retained": [], "new": ["g2_t1_executable_experiment_not_yet_proven"], "reopened": [], "current": ["g2_t1_executable_experiment_not_yet_proven"]},
  "resolutionEvidence": {},
  "counters": {"partialReadyClosures": 0, "reviewerScopeExpansions": 0, "sameClaimCorrections": 0, "nonDecreasingBlockerTransitions": 0},
  "claims": [{"claimId": "ACEL-G2-T1-DISPATCH", "claimClass": "DOCUMENTATION_ONLY", "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS", "evidenceRef": "docs/baselines/CVF_GC018_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_2026-09-16.md"}],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "NO_SUCCESSOR"
}
```

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G2-TOPOLOGY-EXPERIMENT-T1","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"LOCAL_REVERSIBLE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"NEW_INTERFACE"},"pathFamilies":["docs/baselines/","docs/work_orders/","EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/","EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/","EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/scripts/","docs/audits/","docs/reviews/"],"claims":["a hermetic dynamic-topology decision contract can preserve authority and emit deterministic proposal-only evidence"],"requiredProof":["focused tests","TypeScript check","32 unique run records","byte-identical receipt regeneration","authority invariant evidence","independent Local review"],"operatorCheckpoints":["T2 real-agent execution","production integration","provider/live execution","public sync"],"forbiddenEffects":["production routing mutation","actual subagent invocation","provider call","network effect","new dependencies","lockfile mutation","worker commit","automatic T2"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/reviews/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_COMPLETION_2026-09-15.md","completenessClaimChanged":false}}
```

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| intake summary | accepted Local G2 gap plus operator-selected bounded experiment |
| scope classification | local reversible experimental implementation and hermetic execution |
| risk sensitivity | P3 because a new experimental interface and package script are added |
| selected role route | `SINGLE_AGENT_MULTI_ROLE` within implementation; Local remains independent reviewer/closer |
| role separation basis | worker implements and returns evidence without commit; Local reviews and commits |
| escalation condition | actual agent/provider execution, production owner mutation, dependency addition or scope expansion |

## Worker Autonomy / No-Question Rule

Repair allowed-scope checker/test failures directly. Stop only for a source
contradiction, forbidden-path requirement, need for provider/network/actual
subagent execution, or inability to make the 32-run receipt deterministic.

## Agent Roles

| Role | Responsibility |
|---|---|
| operator | selected G2 and retains T2/production checkpoints |
| dispatcher | freezes authority, matrix, manifest and claim ceiling |
| worker | implements and executes the hermetic experiment; writes exactly eight paths; does not commit |
| reviewer/closer | independently evaluates returned evidence, repairs if necessary and owns material commit |
| session-sync steward | records accepted material SHA later in a separate continuity commit |

## Required First Reads

- `AGENTS.md`, `CVF_SESSION_MEMORY.md`, bootstrap model and active handoff.
- `docs/reference/guard_orientation/README.md` and literal-format gotchas.
- Paired baseline and this work order in full.
- Current delegation and proposal-only benchmark contract plus relevant tests.
- External/local coordination methods and every checker in the read-ahead block.

## Write Ownership

Worker owns exactly the eight paths in the Required Artifact Manifest. Every
other path is read-only. Local reviewer owns the completion review and commits;
the session-sync steward alone owns later continuity projection.

## Execution Plan

1. Capture HEAD, status and pre-implementation gate evidence.
2. Define the closed experimental contract and eight deterministic fixtures.
3. Implement tests first for actions, transitions, authority and admission.
4. Implement the runner and package script without dependency or barrel changes.
5. Execute focused tests, typecheck and the runner twice.
6. Reconcile exactly 32 unique runs and byte-identical receipt hashes.
7. Write result and worker return; run worker-return fast; return uncommitted.

## Evidence Requirements

- Exact code/fixture identities and execution base in the receipt.
- All five Policy B actions represented by a correct fixture oracle.
- Authority-envelope, illegal-transition and reclaim-exclusivity negative tests.
- Quality admission precedes all economic comparison.
- Exact test counts, command exits, receipt hashes and eight-path status.

## Required Artifact Manifest

Work-Order Fulfillment Manifest: REQUIRED_EXACT_EIGHT_PATHS

Worker may modify or create exactly these eight paths:

1. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/runtime.topology.experiment.contract.ts`
2. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/runtime.topology.experiment.contract.test.ts`
3. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/fixtures/runtime.topology.experiment.tasks.v1.json`
4. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/scripts/run-runtime-topology-experiment.ts`
5. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/package.json`
6. `docs/audits/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_32_RUN_RECEIPT_2026-09-16.json`
7. `docs/audits/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_RESULT_2026-09-16.md`
8. `docs/reviews/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_WORKER_RETURN_2026-09-16.md`

Every other path is read-only. No deletion, rename, barrel export, dependency
addition, lockfile mutation, production consumer or session-state mutation.

## Experiment Contract

### Matrix

| Dimension | Required values |
|---|---|
| Task class | `BOUNDED_RESEARCH`, `LOCAL_IMPLEMENTATION`, `COUPLED_REASONING`, `FAULT_FINDING` |
| Fixtures | exactly two per task class, eight unique task IDs |
| Policy | `A_FIXED`, `B_DYNAMIC` |
| Repetition | `1`, `2` |
| Total | exactly 32 unique executions |

### Policy A

Use the fixture's preselected topology and never reallocate after dispatch.
Runtime evidence is recorded but cannot change the route action.

### Policy B

May choose `NO_DELEGATE`, `DELEGATE`, `PARALLELIZE`, `RECLAIM` or `ESCALATE`
only when declared runtime evidence and the immutable authority envelope allow
it. At least one fixture must correctly exercise each action; choosing
`NO_DELEGATE` must be represented as a positive decision.

### Invariants

- Work-order ID, owned paths, forbidden paths, risk ceiling, sandbox tier and
  provider authority cannot expand during a route change.
- Unsupported evidence, unknown actions, illegal transitions and authority
  expansion fail closed.
- A reclaimed route cannot retain write authority in both old and new
  executors.
- An escalation changes experimental executor capability only; it never grants
  provider authority.
- All records and aggregate reports carry `evidenceClass: PROPOSAL_ONLY`.

### Quality admission

A run is `admitted=true` only if the selected action equals its fixture oracle,
all invariants pass, the outcome oracle passes and critical defects are zero.
Failed/unadmitted runs remain in the receipt but are excluded from economic
comparison. A cheaper failed run can never win.

## Acceptance Criteria

- Focused tests cover all actions, both policies, all task classes, duplicate
  detection, illegal transitions, authority expansion, reclaim exclusivity,
  fail-closed unknown input and deterministic regeneration.
- TypeScript check passes.
- Runner exits zero and produces exactly 32 unique records.
- Receipt records fixture hash, code/fixture paths, execution base, runner
  command, per-run decisions, admission, metrics and aggregate comparison.
- Re-running the runner without source changes produces byte-identical JSON.
- Result report states whether T2 real-agent execution is `READY_FOR_REVIEW`
  or `BLOCKED_WITH_REASON`; it must not recommend production adoption.
- Existing delegation and benchmark tests remain passing.
- Exact eight-path manifest, staging empty and HEAD unchanged.

## Findings / Position

Dispatch position: G2 is admitted only as a bounded experiment. The worker must
report the observed hermetic result without converting it into real-agent or
production evidence. A failed oracle or non-deterministic receipt blocks T2.

## Review Gate

Local reviewer evaluates the returned receipt and tests without recreating the
implementation. Reviewer-fast and pre-commit must pass; representative oracle,
authority and deterministic-regeneration evidence must be sampled before T2
can be considered.

## Closure Checklist

- [ ] exact executionBaseHead and clean starting state recorded;
- [ ] exactly eight owned paths changed and staging remains empty;
- [ ] focused tests and TypeScript check pass;
- [ ] exactly 32 unique run records reconcile;
- [ ] two receipt generations are byte-identical;
- [ ] result remains `PROPOSAL_ONLY` and does not open T2 automatically;
- [ ] worker-return fast passes and Local completion review decides closure;
- [ ] material and continuity commits remain separate.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every acceptance criterion and gate
passes with HEAD unchanged and staging empty. Otherwise return
`BLOCKED_WITH_REASON`, naming the first unresolved contract contradiction or
forbidden-scope dependency. N/A with reason must be written for every
conditionally inapplicable packet-shape section; omission is forbidden.

## Operator Checkpoint

No further checkpoint is required for T1 within exact scope. Stop for actual
agents/subagents, provider/live execution, production integration, dependency
new dependencies, public sync, deployment or any T2 execution.

## Pre-Flight And Verification Commands

```powershell
git rev-parse HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
Set-Location EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION
npm test -- --run tests/delegation.contract.test.ts tests/performance.benchmark.harness.contract.test.ts tests/runtime.topology.experiment.contract.test.ts
npm run check
npm run experiment:g2-topology
Set-Location ../..
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --cached --name-only
git status --short
```

Worker must run the experiment command twice and prove the receipt SHA-256 is
unchanged between runs. Do not run pre-closure; Local owns committed closure.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_WORKER_RETURN_2026-09-16.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

Required terms: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; executionBaseHead; exact eight-path manifest; 32-run reconciliation; deterministic receipt hashes; focused test counts; TypeScript result; Agent Operation Trace Block; Claim Boundary; Delta Execution Claim Boundary Control Block; External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package; Public Export Disposition; git status --short; N/A with reason instruction.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | experimental implementer and evidence producer; never reviewer |
| phase | implementation and hermetic execution |
| baseHeadFor(phase) | dispatch base as above; execution base captured before edits; closure base owned by Local |
| changedSetScope(phase) | exact eight paths |
| traceScope(phase, actor) | commands, hashes, tests, 32 records and changed-set evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | no unrelated pending path may be touched |
| nextMoveSurfaces | worker return only; Local review decides T2 admission |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT experimental worker

laneOwnedPaths: exact eight paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return with empty staging and exact changed set

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| Applicability | applies because implementation route is `SINGLE_AGENT_MULTI_ROLE` |
| actor | INTERNAL_AGENT worker |
| role set | contract implementer, test author, runner and evidence producer; never reviewer/closer |
| Role separation ledger | worker return is uncommitted; independent Local review and commits follow |
| Evidence basis independent of memory | source diff, focused tests, typecheck, deterministic receipt and status |
| Gate sequence | pre-implementation; focused tests; typecheck; double runner; worker-return fast; Local review |
| Self-review boundary | worker may repair owned paths but cannot accept or close its own result |
| escalation condition | forbidden effect, authority expansion, non-determinism or manifest expansion |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_COMPLETION_2026-09-16.md` |
| reviewerOwnedClosurePaths | completion review, material commit and later continuity commit |
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
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V60_2026-09-08.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact eight worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact worker manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact worker manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker manifest plus completion review | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | reviewer completion path | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

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
  "parentArtifact": null
}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | external synthesis -> accepted Local T0 -> operator-selected G2 -> internal experimental implementation -> Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and Control Plane Foundation experimental paths |
| Disposition | G2 experiment authorized; production and T2 remain blocked |
| Claim boundary | external experiment shape is advisory; Local contract and evidence decide |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES_BOUNDED_EXPERIMENTAL |
| runtimeMutationAuthorized | YES_EXACT_FOUR_EXPERIMENT_PATHS_PLUS_PACKAGE_SCRIPT |
| freshnessVerificationMode | SOURCE_TEST_TYPECHECK_AND_DETERMINISTIC_32_RUN_RECEIPT |
| reason | executable local experiment without provider/network effects |
| requiredFutureAction | Local review before any T2 or production use |

## Claim Boundary

This work order authorizes experimental code and hermetic executions only.
It does not prove real-agent topology value, authorize actual subagents or
providers, change production routing/delegation, export the experiment through
a production barrel, open T2, sync public GitHub or deploy.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | isolated experimental runtime plus 32 hermetic records |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: bounded hermetic experiment execution claim only |
| receiptEvidence | CVF_RECEIPT_PRESENT required at declared audit JSON path |
| actionEvidence | ACTION_EVIDENCE_PRESENT required through runner output and focused tests |
| invocationBoundary | local TypeScript process and deterministic fixtures only |
| interceptionBoundary | no production interception or provider/subagent execution |
| claimLanguage | proposal-only decision-policy evidence, not topology doctrine |
| forbiddenExpansion | production routing, actual agent A/B, provider/live, public and deployment |

## Verification Commands

Use the commands in `## Pre-Flight And Verification Commands`, run the
experiment twice with receipt SHA-256 capture, then run:

```powershell
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --cached --name-only
git status --short
```

Do not run pre-closure; Local owns committed closure.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Worker execution`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: NONE_RETURNED (`totalCandidates=0`).

## Foundation Storage Layout Block

N/A with reason: T1 adds one isolated experimental module, fixture, test and
runner inside existing Control Plane Foundation folders plus flat audit/review
artifacts. It creates no durable governance foundation, registry, aggregate,
queue, production runtime storage topology or new package dependency.

## Rescan Intelligence Hardening

Original source artifact: accepted G2 rows in `docs/audits/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_EVIDENCE_T0_2026-09-15.json`

Predecessor intake artifact: `docs/reviews/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_COMPLETION_2026-09-15.md`

Delta ledger status: REQUIRED_IN_32_RUN_RECEIPT

Routing matrix status: REQUIRED_BELOW

Semantic sampling status: REQUIRED_ORACLE_AND_AUTHORITY_NEGATIVE_CASES

- Rescan intelligence verdict: PARTIAL

### Original-Intake Delta Ledger

| Category | Required treatment |
|---|---|
| UNCHANGED_FROM_INTAKE | static delegation remains the starting baseline |
| CHANGED_DISPOSITION | T1 may change only experiment readiness after executable proof |
| NEW_FINDING | record new oracle, transition or determinism defects in result/return |
| REMOVED_OR_REJECTED | reject any unsupported production or real-agent inference |

### Follow-Up Routing Matrix

| Lane | Use |
|---|---|
| DO_NOW | isolated contract, fixtures, tests, runner and 32-run receipt |
| SEPARATE_RUNTIME_TRANCHE | T2 real-agent experiment only after Local acceptance |
| STRATEGIC_OPERATOR_DECISION | production adoption or broader topology authority |
| OUT_OF_SCOPE | providers, network, public sync, deployment and unrelated owners |
| RESOLVED_BY_DESIGN | quality admission and immutable authority are mandatory in T1 |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| G2-T1-S1 | accepted G2 matrix | runtime topology actions are partial | experiment admission | prove every action without authority expansion | REQUIRED |
| G2-T1-S2 | external experiment suggestion | dynamic policy may outperform fixed | claim ceiling | hermetic decisions cannot prove real-agent value | REQUIRED |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded experimental fixture corpus.
- Corpus root: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/fixtures/runtime.topology.experiment.tasks.v1.json`.
- Snapshot time: worker records execution time and executionBaseHead.
- Enumeration command: `rg --files --hidden --no-ignore EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/fixtures` plus exact JSON parse of the named fixture.
- Manifest artifact or inline manifest: eight fixture objects in the named fixture JSON.
- Manifest hash: worker records SHA-256 in the receipt.
- Processing ledger artifact or inline ledger: 32 records in `docs/audits/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_32_RUN_RECEIPT_2026-09-16.json`.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=8; ledger_terminal=32; exclusions=0; unresolved=0.
- Unresolved files: 0 within the declared fixture corpus.
- Declared exclusions: all unrelated fixtures, external repositories, real-agent runs and provider/live evidence.
- Unreadable or unsupported files: 0 required; any unreadable fixture blocks the runner.
- Aggregation check: 8 fixtures x 2 policies x 2 repetitions = 32 unique records.
- Drift check: receipt binds executionBaseHead plus fixture/source paths and hashes.
- Output traceability: exact audit receipt, result report and worker return.
- Adversarial verification: duplicates, missing rows, invalid transitions, authority expansion and unadmitted comparison fail closed.
- Corpus verdict: PARTIAL

## Finding-To-Governance Learning Disposition

Do not create a new rule or production owner from T1. Any recurring failure may
be proposed only after Local review; the experiment itself remains isolated.

## Epistemic Process Block

- Expected Result / Prediction: dynamic policy decisions can be made deterministically while preserving the immutable authority envelope.
- Evidence Comparison: compare Policy A and B only after each run passes its quality oracle and governance invariants.
- Contradiction Or Gap Disposition: oracle mismatch, invalid transition, authority expansion or unstable regeneration blocks T2.
- Claim Update: only Local review may mark T1 accepted or authorize a separate real-agent T2.

## Machine Closure Package

N/A with reason: this dispatch is pre-execution. The worker provides receipt,
result and return; Local later creates the terminal completion review and owns
material/continuity commits.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher |
| Provider or surface | local private CVF workspace |
| Session or invocation | ACEL-G2-TOPOLOGY-EXPERIMENT-T1 work-order authoring, 2026-09-16 |
| Working directory | repository root |
| Command or tool surface | startup/authority reads, collision searches, scaffold helper, ADIF resolver, apply_patch and dispatch gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | operator message selecting G2 on 2026-09-16 |
| Before status evidence | clean worktree at HEAD `c71176f0af24b804de5cc8e6870c93a493a9f6df` |
| After status evidence | exact two dispatch artifacts pending material commit |
| Diff evidence | `git status --short`; `git diff --check` |
| Approval boundary | internal hermetic experiment dispatch only |
| Claim boundary | no actual agent/provider execution, production mutation, public effect or T2 |
| Agent type | dispatcher |
| Invocation ID | `acel-g2-topology-experiment-t1-work-order-20260916` |
| Expected manifest | paired baseline and this work order |
| Actual changed set | same two paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | dispatch status, role/first actions, routing manifest, no-commit skeleton, exact paths, trace labels, handoff source, closeability graph, coordination JSON and Delta disposition |
| gateRunPurpose | confirm executable dispatch packet shape before worker handoff |
| claimBoundary | checker conformance does not prove experiment correctness or real-agent value |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private experimental work; no public-sync authority.
