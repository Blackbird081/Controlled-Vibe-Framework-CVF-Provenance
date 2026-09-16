# CVF Agent Work Order - ACEL G1 T1 Empirical Calibration Owner Composition Design

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT design and source-verification worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_2026-09-16.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture full HEAD before edits; it must descend from dispatch base `9058a72d55fff417ca1149fdee58f2b411f68b46`.

Current-time notes: G3 is closed and parked; the research-assisted profile is closed; G1 and G4 remain independent; this packet selects G1 only.

Do-not-misread notes: this is an offline owner-composition design, not permission to run models, benchmarks, providers, calibration, G4 measurement, or implementation.

Required first actions: read `AGENTS.md`, bootstrap/front door, active handoff, guard orientation, literal gotchas, paired baseline, this packet, all ten sources, and applicable checker sources before writing.

Return contract: create exactly three worker-owned artifacts, run required gates, keep staging empty and HEAD unchanged, then return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Batch ID: ACEL-G1-T1-EMPIRICAL-CALIBRATION-OWNER-COMPOSITION-DESIGN

Dispatch base head: `9058a72d55fff417ca1149fdee58f2b411f68b46`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated INTERNAL_AGENT

Reviewer/closer: Local reviewer/orchestrator

Worker return path: `docs/reviews/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_WORKER_RETURN_2026-09-16.md`

providerExecutionAuthority: FORBIDDEN

## Purpose

Design the CVF-native owner composition that closes the missing G1 linkage:

```text
task class
-> candidate configuration set
-> comparable measured evaluation
-> bounded operating-point decision
-> regression/invalidation
```

The design must reuse or extend current CVF owners, define fail-closed semantics,
and produce an exact later implementation manifest. It must not implement or
execute the loop.

## Authority Chain

1. Operator instructed Local to choose and write one bounded work order.
2. Local selected G1 before G4 because G4 depends on comparable evaluation and
   baseline/candidate semantics.
3. Accepted T0 completion authorizes G1 only as `ADAPT`, not `ADOPT` or runtime.
4. This paired baseline and work order authorize documentation-only design.
5. Local alone reviews, closes, commits, or opens a later implementation tranche.

## Target / Source

Read and hash these ten current private-CVF sources completely:

1. `docs/reviews/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_COMPLETION_2026-09-15.md`
2. `docs/audits/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_2026-09-15.md`
3. `docs/audits/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_EVIDENCE_T0_2026-09-15.json`
4. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/performance.benchmark.harness.contract.ts`
5. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/performance.benchmark.harness.contract.test.ts`
6. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/harder.value.candidate.contract.ts`
7. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-oa-t6a-candidate-calibration.ts`
8. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/assf.behavioral.evaluation.contract.ts`
9. `docs/reviews/CVF_ACEL_G3_T2_BEHAVIORAL_EVALUATION_CONTRACT_IMPLEMENTATION_COMPLETION_2026-09-16.md`
10. `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md`

Reference hashes at dispatch authoring are recorded in the paired baseline and
Source Verification Block. Recompute at execution base and report drift.

External return `EXT-ACEL-G1-EMPIRICAL-CALIBRATION-HARNESS-T0_RETURN_2026-09-16.zip`
had relay SHA-256 `9d6bef53514aef2f0f7a0bd8551c969fdc07eb14123ac83d12aa1409f7d18184`.
It is closed advisory context, `NOT_CVF_SOURCE`, and must not be treated as the
design or required worker input. No external source fetch is authorized.

## Scope / Methodology

The worker must decide and document:

1. canonical owner and dependency direction across benchmark instrumentation,
   behavioral evaluation, direct task-specific calibration, and provider readiness;
2. stable task-class and candidate-configuration identity;
3. candidate dimensions allowed in scope and dimensions forbidden from silent comparison;
4. comparable input/case-set, environment, model/provider, budget, and policy conditions;
5. search/training versus held-out acceptance separation;
6. repeat, uncertainty, missing-data, and partial-run semantics;
7. quality/risk eligibility before cost/latency preference;
8. deterministic decision states and tie/incomparability handling;
9. provenance fingerprint and invalidation triggers;
10. regression binding to the accepted operating point without automatic mutation.

The design must preserve `PROPOSAL_ONLY` benchmark evidence and provider-lane
certification boundaries. It may consume admitted G3 evidence structurally but
must not claim that G3 results select or certify an operating point.

## Roadmap-To-Work-Order Trace Matrix

| Accepted input | Work-order control | Disposition |
|---|---|---|
| G1 accepted `ADAPT` | extend current owners; no duplicate subsystem | RELEASED_TO_DESIGN |
| no general operating-point consumer proved | require owner/consumer graph and exact decision contract | BINDING |
| G3 offline evaluation now exists | compose as measured-evidence dependency only | BINDING |
| G4 remains independent | defer marginal-value semantics and outputs | DO_NOT_MERGE |
| one bounded successor at a time | exact three-output design tranche | DESIGN_CONTROL_ACCEPTED |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G1-T1-EMPIRICAL-CALIBRATION-OWNER-COMPOSITION-DESIGN
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-empirical-calibration-owner-composition","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["g1_general_operating_point_owner_not_composed","g1_non_circular_evidence_and_invalidation_semantics_unsettled"],"reopened":[],"current":["g1_general_operating_point_owner_not_composed","g1_non_circular_evidence_and_invalidation_semantics_unsettled"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T1-DESIGN-DISPATCH","claimClass":"DOCUMENTATION_ONLY","proofClass":"PROPOSAL_ONLY_NO_RUNTIME_READINESS","evidenceRef":"docs/baselines/CVF_GC018_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_2026-09-16.md"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T1-EMPIRICAL-CALIBRATION-OWNER-COMPOSITION-DESIGN","requestedProfile":"P2_BOUNDED","classification":{"taskKind":"DOC_CHANGE","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/baselines/","docs/work_orders/","docs/audits/","docs/reviews/"],"claims":["a bounded current-source design can settle G1 owner composition without executing calibration"],"requiredProof":["ten-source terminal ledger","owner and consumer graph","closed-loop contract","non-circular holdout rule","provenance invalidation","exact successor manifest or blocker","Local review"],"operatorCheckpoints":["implementation","provider/live","operating-point mutation","G4","public sync","deployment"],"forbiddenEffects":["source or test mutation","provider call","credential access","network effect","benchmark execution","configuration mutation","worker commit","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json","completenessClaimChanged":false}}
```

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| intake summary | Local-selected G1 successor after independent G1/G4 reconciliation |
| scope classification | bounded current-source owner design |
| risk sensitivity | P2: future selection affects model/configuration decisions, but this tranche is documentation-only |
| selected role route | `SINGLE_AGENT_MULTI_ROLE` for source audit and design; Local reviews |
| role separation basis | worker returns three uncommitted artifacts; Local decides |
| escalation condition | source contradiction, owner conflict, protected-path need, or external effect |

## Worker Autonomy / No-Question Rule

Proceed autonomously for reads, hashes, design decisions, owned document
repairs, and listed gates. Do not ask routine formatting questions. Stop only
for a source contradiction, forbidden-scope requirement, or missing authority
that prevents a truthful terminal result.

## Agent Roles

| Role | Responsibility |
|---|---|
| operator | authorized Local to select and write one work order |
| dispatcher | selected G1 and froze corpus, outputs, boundaries, and gates |
| worker | audits, composes, designs, and returns uncommitted evidence |
| reviewer/closer | Local accepts, rejects, repairs bounded packaging, and commits |
| session-sync steward | Local updates continuity only after accepted material |

## Required First Reads

- `AGENTS.md`, bootstrap/front door, and active handoff.
- `docs/reference/guard_orientation/README.md` and literal-format gotchas.
- paired baseline and this work order.
- all ten Target / Source paths.
- checker sources named in Checker Source Read-Ahead Block.

## Write Ownership

Worker owns exactly the three paths in Required Artifact Manifest, create-only.
Every other path is read-only. The worker must not stage, commit, delete,
rename, edit continuity, generate state, call a provider, or fetch a repository.

## Execution Plan

1. Capture full HEAD and `git status --short`; require clean start and ancestry.
2. Run pre-implementation gate against execution base.
3. Read/hash all ten sources and reconcile 10/10 terminal rows.
4. Re-evaluate G1-C1..C3 against current source without reopening G4.
5. Build owner, dependency, consumer, and evidence-flow graphs.
6. Define complete loop, state machine, decision policy, negative cases, and invalidation.
7. Produce exact later implementation manifest or one allowed blocker.
8. Create worker return, run focused document/schema checks and worker-return fast gate.
9. Leave staging empty, HEAD unchanged, and return to Local.

## Required Artifact Manifest

Work-Order Fulfillment Manifest: REQUIRED_EXACT_THREE_PATHS

| Path | Required action |
|---|---|
| `docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_2026-09-16.md` | create human-readable design and terminal disposition |
| `docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json` | create machine-readable ledger, graphs, contract, negative cases, and successor/blocker |
| `docs/reviews/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_WORKER_RETURN_2026-09-16.md` | create full no-commit worker return |

All other paths are forbidden.

## Design Contract

Allowed terminal dispositions, exactly one:

- `DESIGN_READY_FOR_SEPARATE_IMPLEMENTATION_WORK_ORDER`
- `BLOCKED_OWNER_CONFLICT`
- `BLOCKED_SOURCE_CONTRADICTION`
- `REJECT_DUPLICATE_OWNER`

Ready requires all ten sources reconciled, one canonical composition owner,
explicit dependency directions, complete state/decision semantics, all negative
cases, and an exact successor manifest. The worker must confirm, revise, or
reject this preferred hypothesis from current source:

```text
task-class calibration owner
  consumes candidate identity + comparable G3 evaluation evidence
  references performance/provider evidence without promoting it
  emits a non-mutating operating-point assessment
  binds the accepted choice to regression/invalidation evidence
```

The design must keep actual configuration mutation and promotion under a later
authority owner. G4 may later consume comparable pairs but cannot be folded into
this contract.

## Evidence Requirements

- ten ledger rows: path, SHA-256, status, extracted fact, claim ID;
- G1-C1/C2/C3 reconciliation and freshness delta;
- owner matrix using `REUSE`, `EXTEND`, `ADAPTER_ONLY`, `DEFER`, or `REJECT_DUPLICATE`;
- evidence flow from task class and candidate set through measurement, decision,
  accepted point, and regression;
- predeclared search/heldout partition rule with contamination rejection;
- comparability fingerprint fields and mismatch behavior;
- eligibility-before-preference policy; no default weighted score that can
  trade away required quality or risk constraints;
- decision states for ineligible, eligible/nonpreferred, preferred,
  incomparable, and insufficient evidence, or a justified CVF-native equivalent;
- negative cases for empty candidates, duplicate IDs, mixed task/case sets,
  unequal budgets/policies, missing heldout evidence, reused heldout search data,
  stale fingerprints, incomplete repeats, unknown metrics, ties, and no eligible candidate;
- regression/invalidation triggers without automatic rollback or mutation;
- exact later source/test/checker paths and no more than one separately governed implementation tranche.

## Acceptance Criteria

- Exactly three worker-owned paths; staging empty; no commit.
- All ten sources read, hashed, and terminally reconciled.
- Local repository facts override external advisory suggestions.
- One current owner composition; no parallel benchmark/evaluation/provider owner.
- Loop is closed on paper through regression, not merely benchmark evidence.
- Holdout and provenance rules prevent circular or stale selection.
- Provider readiness and proposal-only evidence are not promoted.
- G4 remains independent and deferred.
- Markdown and JSON agree on owner, states, blockers, and successor manifest.
- No provider/live/runtime/configuration/public effect.

## Findings / Position

Dispatcher position: `ADAPT_G1_FIRST`. G1 provides the comparison and decision
semantics that G4 will later require. This position is a dispatch selection,
not acceptance of any particular design.

## Review Gate

Local applies `EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION`. Reviewer
checks hashes, 10/10 ledger reconciliation, graph/contract parity, negative
cases, output manifest, staging/HEAD, and required gates. No broad rerun without
a named contradiction, safety reason, or expected information gain.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when exactly three outputs exist, all
criteria pass, staging is empty, and HEAD equals execution base. Otherwise
return `BLOCKED_WITH_REASON` with the exact blocker and safest next action.

## Operator Checkpoint

No worker checkpoint is expected inside this design pass. Local/operator review
is mandatory before implementation, provider/live work, operating-point
promotion/mutation, G4, runtime wiring, public sync, or deployment.

## Pre-Flight Commands

```powershell
git rev-parse HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

## Verification Commands

Required full return gate: `python governance/compat/run_worker_return_fast_gate.py`

```powershell
python -m json.tool docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json > $null
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
git diff --cached --name-only
git status --short
```

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_WORKER_RETURN_2026-09-16.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Scope / Methodology; Findings / Position; Risk / Corrective Action; Claim Boundary; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git status --short; Changed Files; Command Evidence; No-Commit Statement.

Conditional blocks must appear with accurate N/A-with-reason dispositions:
External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus
Completeness And Report Integrity; Finding-To-Governance Learning Disposition;
Epistemic Process Block; Machine Closure Package.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one INTERNAL_AGENT audits and designs; Local reviews/closes |
| phase | dispatch -> worker execution -> Local review -> optional continuity |
| baseHeadFor(phase) | dispatchBaseHead=`9058a72d55fff417ca1149fdee58f2b411f68b46`; executionBaseHead=worker capture; closureBaseHead=Local capture |
| changedSetScope(phase) | exact three create-only worker paths |
| traceScope(phase, actor) | commands, source hashes, artifacts, tests, status, and no-commit evidence |
| commitOwner(phase) | Local reviewer/closer only |
| crossBatchIsolation | G1 only; G4 and all other tranches read-only and excluded |
| nextMoveSurfaces | active handoff/state only after Local acceptance |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT design worker

laneOwnedPaths: exact three Required Artifact Manifest paths

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return with empty staging and exact changed set

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| Applicability | worker audits, maps, and designs in one no-commit role |
| actor | INTERNAL_AGENT worker |
| role set | source auditor, design author, evidence producer; never reviewer/closer |
| Role separation ledger | worker returns pending artifacts; Local independently accepts or rejects |
| Evidence basis independent of memory | governed paths, hashes, ledger, and machine gates |
| Gate sequence | pre-implementation; source reconciliation; design/schema checks; worker-return fast; Local review |
| Self-review boundary | worker repairs owned documents but cannot accept its design |
| escalation condition | missing authority, irreconcilable source, protected-path need, or forbidden effect |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-16.md` if Local needs a separate closeout |
| reviewerOwnedClosurePaths | work-order status, optional completion review, continuity after material acceptance |
| closureOwner | Local reviewer/orchestrator |
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
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V61_2026-09-16.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact three worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| source_reconciliation | WORKER_RETURN | worker | IMPLEMENTATION | exact three worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact three worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | source_reconciliation |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact three worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker paths plus reviewer closure | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | reviewer completion path | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | documentation-only G1 design | no code/runtime/provider/configuration mutation | current private-CVF sources | later implementation work order required | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no G1 external adapter | no calls, credentials, receipts, or external decisions | none authorized | separate owner/authority required | `DEFERRED_WITH_REASON` |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":"docs/reviews/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_COMPLETION_2026-09-15.md"}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | external advisory research closed -> Local integrity/reconciliation -> G1 `ADAPT` -> separate INTERNAL_AGENT design work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | current private-CVF sources in Target / Source; Local reviewer |
| Disposition | ADAPT existing owners; advisory contract is not the default design |
| Claim boundary | no external source authority, remote implementation, or merged G1/G4 lane |

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON

Reason: internal documentation-only dispatch; zero external invocation budget.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO_NEW_RUNTIME_CLAIM |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | clean execution base, ten current source reads/hashes, and Local review |
| reason | design concerns owner composition only |
| requiredFutureAction | separate implementation and later empirical authority before any runtime claim |

## Corpus Completeness And Report Integrity

- Corpus task class: exact bounded ten-source design audit.
- Corpus root: the ten Target / Source paths only.
- Snapshot time: worker execution base.
- Enumeration command: filesystem-backed direct reads of the exact ten paths.
- Manifest artifact or inline manifest: `docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json`.
- Manifest hash: worker-generated SHA-256 of sorted path/hash/status rows.
- Processing ledger artifact or inline ledger: ten terminal source rows in the machine manifest.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`, `BLOCKED_UNREADABLE`.
- Reconciliation: manifest=10; ledger_terminal=10; exclusions=0; unreadable=0; unresolved=0 for ready disposition.
- Unresolved files: 0 required for ready disposition; otherwise list exact paths and block.
- Declared exclusions: external ZIP payload, G4, unrelated repository paths, runtime and provider execution.
- Unreadable or unsupported files: record count and exact paths; zero required for ready disposition.
- Aggregation check: every design claim cites source-row claim IDs.
- Drift check: recompute SHA-256 and compare G1-C1..C3 with current source.
- Output traceability: source ledger -> owner graph -> loop contract -> disposition -> worker return.
- Adversarial verification: reject circular holdout, stale fingerprint, incomparable candidates, score laundering, and provider-readiness promotion.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS - required for ready disposition.

## Knowledge System Reconciliation

- Knowledge task class: current-owner G1 composition design.
- Source manifest: exact ten-path manifest and hash.
- Source manifest hash: worker-generated SHA-256 over sorted path/hash/status rows.
- Enumeration safety: filesystem-backed exact-path reads only.
- Intake registry or ledger: machine-readable design manifest.
- Authority assets: paired dispatch, accepted T0 completion/audit/ledger, and current owners.
- Derived views: human design and worker return.
- Semantic region ledger: identity, comparability, partition, measurement, eligibility, decision, provenance, invalidation, regression, successor.
- Region reconciliation: assets=10; mapped=10; deferred=0; unmapped=0. G4 is an excluded domain, not a corpus asset.
- Orphan or unmapped assets: none
- Cross-region links: claim IDs bind source rows to owner and contract decisions.
- Drift check: PASS
- Drift precondition: current-hash and T0 comparison must succeed.
- Drift method: compare accepted G1-C1..C3 against current bytes and symbols.
- Rebuildability: manifest plus exact sources rebuild the design.
- Rebuildability check: PASS only when JSON and Markdown agree on owner, states, blockers, and successor.
- Retrieval boundary: design readiness only.
- Adversarial verification: reject circular evidence, stale reuse, provider-certification substitution, and G4 coupling.
- Knowledge-map verdict: RECONCILED_WITH_DECLARED_GAPS

## Finding-To-Governance Learning Disposition

Do not add a global rule, hook, or checker. Record any reusable defect in the
worker audit for Local disposition. Runtime/provider/cost learning is N/A with
reason: no execution occurs.

## Foundation Storage Layout Block

Three flat audit/review artifacts only. No durable store, queue, registry,
generated aggregate, runtime service, or relocation is created.

## Epistemic Process Block

Epistemic Process Applicability: BOUNDED_GOVERNANCE_DESIGN

Expected Result / Prediction: existing benchmark, G3 evaluation, direct
calibration, and provider-readiness pieces can compose a single offline G1
owner contract without new architecture or G4 coupling.

Evidence Comparison Requirement: compare that prediction against all ten
sources, including negative and boundary behavior.

Contradiction Handling Requirement: block or revise the hypothesis when source
authority, comparability, or dependency direction conflicts; Local truth wins.

Claim Update Requirement: report design-ready pending Local review, a duplicate
owner rejection, or one exact blocker; never claim calibrated runtime behavior.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | documentation-only G1 owner composition |
| claimDisposition | CLAIM_REJECTED: no runtime execution, selection, enforcement, or configuration mutation is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no benchmark/provider/runtime receipt is produced |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source hashes, design artifacts, schema validation, and governance gates only |
| invocationBoundary | local read-only source inspection and document/test tooling |
| interceptionBoundary | no wrapper, runtime gate, provider call, or agent action interception |
| claimLanguage | design-ready pending Local review; never empirically calibrated or runtime-ready |
| forbiddenExpansion | implementation, provider/live, G4, configuration mutation, runtime, public, deployment |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044. Returned count: 10;
resolver reported truncation. Dispatch impact is incorporated through exact
sources/outputs, checker read-ahead, private authority, no protected worker
paths, no external calls, and bounded return evidence.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T1-EMPIRICAL-CALIBRATION-OWNER-COMPOSITION-DESIGN --title "ACEL G1 T1 Empirical Calibration Owner Composition Design" --date 2026-09-16 --base 9058a72d55fff417ca1149fdee58f2b411f68b46 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_COMPLETION_2026-09-15.md --include-worker-return-skeleton --no-evidence-readiness-applicable --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --scec-problem-key acel-g1-empirical-calibration-owner-composition --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout` |
| generatedProfile | generic no-commit initial dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | G1 selection, exact corpus, three-output manifest, design contract, G4 firewall, gates, and role boundaries |
| checkerReadAheadConfirmation | dispatch, convergence, routing, coordination, closeability, trace, handoff, provider, and Delta checker families |
| docOnlyNewFields | calibrationLoopContract; operatingPointDecisionContract; invalidationContract |
| claimBoundary | dispatch provenance only; no design or behavior is accepted yet |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| G1 `ADAPT` is accepted | AUTHORITY | `docs/reviews/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_COMPLETION_2026-09-15.md` | Findings / Position | G1 row | Local T0 completion | ACCEPT |
| G1-C1..C3 prove pieces but not closed loop | GAP_FACT | `docs/audits/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_2026-09-15.md` | G1 section | G1-C1..C3 | ACEL audit | ACCEPT |
| machine evidence is current and explicit | EVIDENCE | `docs/audits/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_EVIDENCE_T0_2026-09-15.json` | `claims` | G1-C1..C3 | evidence ledger | ACCEPT |
| instrumentation is proposal-only | CONTRACT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/performance.benchmark.harness.contract.ts` | module and types | `EvidenceClass`; `generateReport` | benchmark owner | ACCEPT |
| benchmark lifecycle has tests | TEST | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/performance.benchmark.harness.contract.test.ts` | test suites | lifecycle/negative tests | benchmark tests | ACCEPT |
| deterministic candidate rubric exists | CONTRACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/harder.value.candidate.contract.ts` | exports | `evaluateHarderCandidate` | task-specific evaluator | ACCEPT |
| existing runner is fixed-scope | IMPLEMENTATION | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-oa-t6a-candidate-calibration.ts` | runner | fixed candidate calibration | task-specific runner | ACCEPT |
| comparable behavioral evidence owner exists | DEPENDENCY | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/assf.behavioral.evaluation.contract.ts` | exports | grading and baseline pair admission | G3 owner | ACCEPT |
| G3 is accepted and parked | DEPENDENCY | `docs/reviews/CVF_ACEL_G3_T2_BEHAVIORAL_EVALUATION_CONTRACT_IMPLEMENTATION_COMPLETION_2026-09-16.md` | Terminal Decision | G3 parked | Local completion | ACCEPT |
| provider certification is adjacent only | CLAIM_BOUNDARY | `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` | Status Key; Claim Boundary | `CERTIFIED` | provider readiness | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| five exact dispatch/output paths | all absent before authoring | NO_COLLISION |
| exact batch and artifact tokens | no match across governed/source/checker roots | NO_COLLISION |
| existing generalized owner | bounded accepted G1 audit proves no composed owner | ADAPT; NO_NEW_COMPONENT_BY_DEFAULT |
| external advisory contract | outside repository and non-authoritative | NOT_DEFAULT_DESIGN |
| G4 | independent audit question | EXCLUDED_AND_DEFERRED |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | ready status, prompt envelope, source columns, convergence schema, route manifest, coordination binding, full return profile, trace fields, provider authority |
| gateRunPurpose | confirm complete dispatch shape before relay |
| claimBoundary | checker pass proves packet structure, not design correctness |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local reviewer/orchestrator acting as dispatcher |
| Provider or surface | private CVF workspace only |
| Session or invocation | ACEL G1 T1 design dispatch, 2026-09-16 |
| Working directory | repository root |
| Command or tool surface | startup/source reads, archive integrity read, hashes, searches, resolver, scaffold stdout, apply_patch, dispatch gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | operator instruction to choose and write one work order |
| Before status evidence | clean worktree at HEAD `9058a72d55fff417ca1149fdee58f2b411f68b46` |
| After status evidence | exact two dispatcher artifacts pending commit |
| Diff evidence | `git status --short`; `git diff --check` |
| Approval boundary | internal documentation-only G1 design dispatch |
| Claim boundary | no design acceptance, implementation, provider/live, runtime, public, or deployment claim |
| Agent type | dispatcher |
| Invocation ID | `acel-g1-t1-empirical-calibration-owner-composition-design-dispatch-20260916` |
| Expected manifest | paired baseline and work order |
| Actual changed set | same two paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This work order authorizes exactly three uncommitted documentation/evidence
outputs for G1 owner composition. It does not authorize implementation,
benchmark or provider execution, credentials, network access, configuration
selection/mutation, threshold promotion, G4, runtime wiring, hook/CI changes,
public sync, deployment, production, or an automatic successor.

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: documentation-only G1 owner design.

Target lifecycle state: unchanged.

Prior phase evidence: accepted ACEL T0 G1 audit and accepted G3 offline contract.

Next forbidden skip: implementation or promotion without Local acceptance and a separate work order.

Runtime/provider proof: N/A with reason: forbidden.

Claim boundary: no package/skill state is read as permission or modified.

## Closure Checklist

- [ ] Worker captured exact execution base and clean start.
- [ ] Exactly three worker-owned paths exist; every other path unchanged.
- [ ] Ten sources reconcile 10/10 with hashes.
- [ ] Owner/dependency/consumer graphs and closed-loop contract agree.
- [ ] Non-circular, comparability, invalidation, and negative cases are complete.
- [ ] G4 remains independent and excluded.
- [ ] JSON parses; worker-return fast passes; staging empty; HEAD unchanged.
- [ ] Local reviewer records terminal disposition.

## Machine Closure Package

NOT_APPLICABLE_WITH_REASON: dispatch artifact only. Machine closure packaging
belongs to Local after returned evidence is reviewed and materially committed.

## Acceptance Receipt Assertion Matrix

| Assertion | Required at worker return | Dispatch state |
|---|---|---|
| source ledger | 10/10 exact hashes and terminal statuses | PENDING_WORKER |
| owner composition | one owner plus explicit dependencies | PENDING_WORKER |
| closed loop | task through regression/invalidation | PENDING_WORKER |
| G4 isolation | no merged contract or output | BINDING |
| provider authority | zero calls; forbidden | BINDING |
| worker commit | forbidden; Local owns commit | BINDING |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design dispatch; no public-sync action is authorized.
