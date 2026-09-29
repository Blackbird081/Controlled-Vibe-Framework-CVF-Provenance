# CVF Agent Work Order - ACEL AKOE-P2 Durable Intent And Projection Reconciliation

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

providerExecutionAuthority: FORBIDDEN

Batch ID: ACEL-AKOE-P2

Dispatch base head: `81ad480b86074b0d8e40025cde8a95c9051e6a0e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: shared-workspace `INTERNAL_AGENT` runtime-reconciliation role

Reviewer/closer: Local reviewer/closer distinct from the worker phase

Worker return path: `docs/reviews/CVF_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_WORKER_RETURN_2026-09-25.md`

## Dispatch Prompt Envelope

Role: internal worker for bounded AKOE-P2 durable-intent and projection
reconciliation.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_2026-09-25.md`

Paired baseline: `docs/baselines/CVF_GC018_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_2026-09-25.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: worker captures the committed dispatch-continuity HEAD
before edits.

Current-time notes: authored 2026-09-25 from clean dispatch base
`81ad480b86074b0d8e40025cde8a95c9051e6a0e`; bounded P1 closure is evidenced
by `docs/reviews/CVF_ACEL_AKOE_P1_HUMAN_CONTROL_AND_POSITIONING_RECONCILIATION_COMPLETION_2026-09-25.md`
at commit `af0e9a199`.

Do-not-misread notes: audit existing behavior first. Code changes are
conditional on a deterministic failing case. No new runtime, Unreal intake,
network/provider/live action, P3/P4 work, public sync, or commit is authorized.

Required first actions: read startup and role-boundary surfaces, guard
orientation, literal gotchas, the paired baseline, this packet, exact input,
current owners, source/tests, and named checker sources before writing.

Return contract: create the exact worker return, execute the seven-class audit,
make only proved minimal repairs, run required gates, leave all changes
uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Determine with deterministic evidence whether existing MAO and
governed-command launch paths safely own durable admission, effect boundary,
replay/recovery identity, cancellation, projection, and semantic-completion
distinctions. Repair only a demonstrated defect inside the exact manifest.

## Authority Chain

- Operator instruction: `next` on 2026-09-25, authorizing the bounded P2 move.
- Active front door: `CVF_SESSION_MEMORY.md`.
- Active handoff: `AGENT_HANDOFF_V63_2026-09-18.md`.
- Roadmap: `docs/roadmaps/CVF_ACEL_APPLIED_KNOWLEDGE_OWNER_ENRICHMENT_ROADMAP_2026-09-25.md`.
- GC-018: `docs/baselines/CVF_GC018_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_2026-09-25.md`.
- Role owners: `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_EVIDENCE_RELAY_METHOD.md` and `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md`.

Authority boundary: the worker may test and conditionally repair only exact
manifest paths. The Local reviewer owns acceptance, commit, closure, and
continuity; the worker may not expand or accept its own result.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| AKOE roadmap | P2 owner paths, seven test classes, optional-intake boundary, and no-new-runtime rule are explicit | paired packet carries all P2 obligations | SATISFIED |
| AKOE-P1 closure | P1 closed at `af0e9a199`; closure and final marker commits are `3c8378b8b` and `81ad480b8` | P2 does not reopen P1 | SATISFIED |
| operator checkpoint | operator instruction `next`; P1 closure is cited by completion review path and commit `af0e9a199` | only bounded P2 is opened | SATISFIED |
| paired GC-018 | exact baseline is part of this dispatch batch | packet must pass pre-dispatch and be committed before execution | SATISFIED_FOR_DISPATCH |
| dispatch continuity | P2 marker does not exist before material commit | session-sync steward must record material SHA before implementation | REQUIRED_BEFORE_IMPLEMENTATION |

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | owns scope expansion and later roadmap checkpoints |
| Local dispatcher | owns packet correctness and dispatch release |
| Internal worker | owns bounded audit, conditional source/test repair, evidence, and uncommitted return |
| Local reviewer/closer | evaluates returned evidence without recreating work; owns repair disposition, commits, closure, and continuity |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | one already-admitted co-designed async-runtime handoff compared with exact current CVF runtime owners |
| scope classification | named-file executable reconciliation with deterministic tests |
| risk sensitivity | private repository; Git-reversible; executable behavior; no external effect authorized |
| selected role route | `SINGLE_AGENT_SINGLE_ROLE` worker execution followed by distinct Local review/closure |
| role separation basis | worker cannot accept, stage, commit, or synchronize its own changes |
| escalation condition | source/hash contradiction, outside-manifest need, new runtime/owner, Unreal intake, external action, or claim expansion |

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-AKOE-P2","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"STATEFUL_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/baselines/","docs/work_orders/","docs/reviews/","docs/reference/multi_agent_orchestration/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/","EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/"],"claims":["bounded durable-intent and projection audit","conditional minimal repair of existing runtime owners"],"requiredProof":["exact handoff hash","seven-class deterministic evidence matrix","failing-before passing-after evidence for each accepted delta","focused tests and type/build checks","exact changed set","worker-return full gate"],"operatorCheckpoints":["new runtime or owner","optional Unreal source intake","P3 or P4","provider/live/public/deployment action"],"forbiddenEffects":["worker commit","network or provider invocation","new runtime engine","governance checker mutation","public write","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":false,"corpusReceiptRef":"docs/roadmaps/CVF_ACEL_APPLIED_KNOWLEDGE_OWNER_ENRICHMENT_ROADMAP_2026-09-25.md","completenessClaimChanged":false}}
```

## Scope

Allowed scope:

- recompute the exact input hash and stop on drift;
- inspect the two launchers, their current tests, the MAO contract, and the T3
  launcher baseline;
- create one worker return with the seven-class P2 matrix;
- add deterministic tests inside the two existing test files;
- modify an existing launcher or MAO contract only after a failing test proves
  a defect owned by that path;
- use local package test/typecheck commands and governance gates;
- repair allowed-scope failures without asking routine questions.

Forbidden scope:

- edits outside the maximum manifest;
- new runtime engine, queue, store, projection owner, package, checker, hook,
  catalog, schema family, dependency, or generated aggregate;
- optional Unreal/source-mirror intake, network, browser, external agent,
  provider/model call, credential, or live API proof;
- session/roadmap/dispatch mutation by the worker;
- install, stage, commit, push, publish, deploy, certify, or production action;
- P1 reopening, P3 integration, P4 closure, or G1-G7 successor work.

Risk ceiling: R3 bounded private executable reconciliation with deterministic
local tests, no external effect, no new authority, and no worker commit.

## Maximum Worker Path Manifest

| Path | Action ceiling | Admission rule |
|---|---|---|
| `docs/reviews/CVF_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_WORKER_RETURN_2026-09-25.md` | CREATE | always required; single P2 decision/evidence return |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.operational.worker.launcher.test.ts` | MODIFY_EXISTING | deterministic P2 MAO audit cases and regression proof |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | MODIFY_EXISTING_ONLY_IF_PROVED_GAP | smallest repair linked to failing MAO negative case |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.reconciliation.ts` | MODIFY_EXISTING_ONLY_IF_PROVED_GAP | only if exact replay/recovery identity defect is proved |
| `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | MODIFY_EXISTING_ONLY_IF_PROVED_GAP | only if executable correction requires matching current-owner contract clarification |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.test.ts` | MODIFY_EXISTING | deterministic P2 governed-command audit cases and regression proof |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | MODIFY_EXISTING_ONLY_IF_PROVED_GAP | smallest repair linked to failing governed-command negative case |

Zero source or contract changes is valid if current behavior passes all seven
classes. Test additions and the worker return remain required evidence.

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `docs/reviews/CVF_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_WORKER_RETURN_2026-09-25.md` | Yes | one pending P2 decision and evidence packet |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.operational.worker.launcher.test.ts` | Yes | deterministic MAO coverage for applicable P2 classes |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.test.ts` | Yes | deterministic governed-command coverage for applicable P2 classes |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | Conditional | smallest proved-gap correction only |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.reconciliation.ts` | Conditional | smallest proved recovery correction only |
| `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Conditional | matching existing-owner clarification only |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | Conditional | smallest proved-gap correction only |

## Forbidden Path Manifest

| Path or family | Reason |
|---|---|
| `.private_reference/source_mirrors/`; any Unreal checkout | optional source intake requires separate authority |
| `governance/compat/`; `.githooks/` | checker/hook mutation is outside P2 |
| `CVF_SESSION/`; `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V63_2026-09-18.md` | reviewer/session-sync owned |
| `docs/roadmaps/`; `docs/baselines/`; `docs/work_orders/` | worker may read but not modify authority |
| package manifests and lock files | no dependency or package change is authorized |

## Foundation Storage Layout Block

No new folder, package, runtime engine, store, registry, generated aggregate,
or archive is authorized. Any need for a new durable owner or file outside the
manifest stops P2 and returns to the orchestrator.

## Required First Reads

| Path | Action | Purpose |
|---|---|---|
| `AGENTS.md`; startup bootstrap; `CVF_SESSION_MEMORY.md`; active handoff | FULL_READ | authority, current mode, next move, parked boundaries |
| guard-orientation README and literal-format gotchas | FULL_READ | role gates and checker-safe artifact shape |
| paired baseline, this work order, and AKOE roadmap | FULL_READ | exact P2 authorization and test classes |
| `C:/Users/DELL/Downloads/ASYNC_RUNTIME_CANONICAL_HANDOFF.md` | FULL_READ | co-designed input; not source authority |
| MAO contract, launcher, reconciliation helper, and launcher test | FULL_READ | current MAO owner and executable evidence |
| T3 baseline, governed-command launcher, and its test | FULL_READ | current governed-command owner and executable evidence |
| checker sources named below | FULL_READ | output/gate shape before writing |

## Pre-Flight Checks

Before any worker-owned edit:

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
Get-FileHash -Algorithm SHA256 -LiteralPath C:/Users/DELL/Downloads/ASYNC_RUNTIME_CANONICAL_HANDOFF.md
git log -1 --format=%H -- docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_2026-09-25.md
rg -n "material-SHA marker|ACEL-AKOE-P2" AGENT_HANDOFF_V63_2026-09-18.md
python governance/compat/check_dispatch_release_readiness.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_2026-09-25.md --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_2026-09-25.md
```

Expected: clean committed base, matching input hash, committed packet, later
committed handoff material-SHA marker, dispatch-release PASS, and bound
pre-implementation PASS. Otherwise stop before worker edits.

## Worker Autonomy / No-Question Rule

Repair allowed-scope source, test, documentation, encoding, and gate defects
directly. Do not ask the orchestrator routine implementation questions. Return
only for a source contradiction, forbidden-path need, new authority/runtime,
external action, risk expansion, or missing dispatch continuity.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| durable reservation and `TASK_ADMITTED` precede adapter call | implementation fact | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | lines 313-399 | `launch` | MAO launcher | ACCEPT |
| successful adapter call precedes `INVOCATION_STARTED` append | audit candidate | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | lines 399-445 | `adapter.invoke`; running append | MAO launcher | ACCEPT |
| recovery verifies reservation-bound attempt identity | implementation fact | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | lines 500-663 | `reconcileDelegation` | MAO launcher/delegation store | ACCEPT |
| create-exclusive execution intent precedes runner | implementation fact | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 412-503 | `beginExecution`; `runner.run` | governed-command launcher/store | ACCEPT |
| workspace/conversation state is not execution truth | contract fact | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Workspace relationship; Second governance/state truth | projection boundary | MAO contract | ACCEPT |

Optional Unreal-specific facts are not admitted into this packet. If they
become necessary, the worker stops and requests a separately governed pinned
source-mirror intake.

## Exact Input Evidence

| Input | SHA-256 | Origin class | Authority disposition |
|---|---|---|---|
| `C:/Users/DELL/Downloads/ASYNC_RUNTIME_CANONICAL_HANDOFF.md` | `a85d8fd35495e94257df1d3a8bfa238d3e5661eaa04b52e156b4886987a4525b` | `OPERATOR_AGENT_CO_DESIGNED` | design input only; current CVF source/tests decide |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact packet/return paths | all returned `False` before authoring | CLEAR |
| P2 identity search | exact command `rg -n "ACEL-AKOE-P2|Durable Intent And Projection Reconciliation" docs CVF_SESSION AGENT_HANDOFF_V63_2026-09-18.md`; roots `docs`, `CVF_SESSION`, active handoff; result before authoring: one same-token collision at roadmap line 213 | CLEAR_EXPECTED_OWNER |
| implementation owner search | exact MAO and governed-command source/test paths exist | REUSE_EXISTING_OWNERS |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

The worker recomputes the input hash, runs focused tests from current bytes,
and records commands/results. Prior P1 or T3 PASS evidence is contextual only.
All new text remains UTF-8 and uses repository-relative paths except the exact
operator input path.

## Roadmap-To-Work-Order Trace Matrix

| P2 requirement | Worker obligation | Evidence location |
|---|---|---|
| compare both current paths before implementation | source/symbol comparison before edits | worker return owner map |
| determine identity sufficiency and `INVOCATION_STARTED` crash window | deterministic seam tests, not prose inference | seven-class matrix and test output |
| seven required test classes | one row each, mapped across applicable owners | P2 decision matrix |
| optional Unreal intake only if needed | do not use it; stop with exact trigger | input/source disposition |
| no new runtime engine | exact manifest and no-new-owner attestation | changed-set evidence |

## Required Decision Packet Contract

The worker return must include:

- exact current owner/symbol map and input hash;
- seven-class matrix with pre-change outcome, deterministic command/test,
  disposition, proposed/actual change, post-change outcome, and reviewer state;
- explicit admission -> effect-dispatch -> effect-accepted -> terminal-runtime
  -> artifact/independent-verification -> semantic-completion state analysis;
- identity tuple comparison covering launch/consumption ID, task/profile,
  authority, scope/target, budget, and reservation/binding hash as applicable;
- projection contradiction rule and observable failure behavior;
- changed-file, pre/post hash, failing-before/passing-after, and no-commit proof.

Allowed dispositions: `CONFIRMED_EXISTING`, `ENRICH_EXISTING`,
`DEFER_WITH_TRIGGER`, `REJECT_DIRECT_IMPORT`. Every row ends
`PENDING_LOCAL_REVIEW`.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: the exact operator handoff is a co-designed
input already bound by hash. P2 performs Local current-owner comparison only;
it does not scan, clone, mirror, or absorb an external repository.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON - selected single-file design input and named local
owners; no repository corpus completeness or broad external-source claim is
made.

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| async-runtime durability and projection claims | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | `ENRICH_EXISTING` candidate | exact seven-class behavior may be missing or already covered | deterministic comparison; repair only a proved gap |
| source-specific Unreal behavior | OWNER_SURFACE_NOT_FOUND | `REJECT_DIRECT_IMPORT` | upstream claim is unnecessary for the bounded Local audit | exclude; separately govern intake only if later required |

## Corpus Completeness And Report Integrity

- Corpus task class: SELECTED_INPUT_OWNER_RECONCILIATION
- Corpus root: one exact hash-bound handoff plus seven named current CVF owner,
  implementation, and test files.
- Snapshot time: dispatch authoring 2026-09-25; worker refreshes the input hash
  and repo bytes at `executionBaseHead`.
- Enumeration command: filesystem-backed direct file reads of the explicit
  eight-file list in Exact Input Evidence, Source Verification Block, Required
  First Reads, and Maximum Worker Path Manifest.
- Manifest artifact or inline manifest: inline tables in this work order;
  manifest count=8.
- Manifest hash: external input has exact SHA-256; seven repo files are bound
  by `executionBaseHead` and worker-recorded pre-edit SHA-256 where changed.
- Processing ledger artifact or inline ledger: dispatch planning ledger marks
  eight inputs `DEFERRED`; worker return records terminal per-file use.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=8; ledger_terminal=8; exclusions=0; unresolved=8
  at dispatch.
- Unresolved files: all eight selected inputs await worker full read and test
  reconciliation.
- Declared exclusions: repository-wide and upstream Unreal corpora are outside
  P2.
- Unreadable or unsupported files: none observed; worker stops with
  `BLOCKED_UNREADABLE` if this changes.
- Aggregation check: 1 handoff + 7 repo files = 8 manifest and 8 planning rows.
- Drift check: worker recomputes the handoff hash and binds repo files to the
  execution base.
- Output traceability: every P2 row cites owner symbol, test, result, and
  disposition.
- Adversarial verification: challenge duplicate effects, identity mismatch,
  race ambiguity, projection-as-truth, and fabricated semantic completion.
- Corpus verdict: PARTIAL

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | exact hash-bound handoff -> Local current-source comparison -> deterministic test matrix -> bounded conditional repair -> independent Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | AKOE roadmap, paired packet, MAO and governed-command source/test owners |
| Disposition | comparison-only Local reconciliation; optional upstream intake excluded |
| Claim boundary | handoff is input, not private-CVF runtime proof; Local reviewer owns final disposition |

## External/Local Coordination Binding

Role: shared-workspace `INTERNAL_AGENT`. Phase: bounded P2 executable
reconciliation. Decision owner: Local. External research is closed and may
reopen only through separately authorized pinned-source intake.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":"docs/roadmaps/CVF_ACEL_APPLIED_KNOWLEDGE_OWNER_ENRICHMENT_ROADMAP_2026-09-25.md"}
```

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | work order, exact source/tests, worker return | local audit and conditional repair; no commit/final acceptance | deterministic tests, diff, gates | existing local runtime/test seams | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external adapter | no ingress, invocation, auth, mutation, raw-data, or public authority | zero invocation ceiling | N/A with reason: no external adapter is used or created | N/A_WITH_REASON |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL

dispatchSurface: INTERNAL_AGENT

parentAssignmentId: ACEL-AKOE-P2

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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-akoe-p2-durable-intent-projection","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON

Reason: shared-workspace internal worker; external invocation is forbidden and
does not count against any external budget.

## High-Risk Local Transaction Proof Applicability

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - P2 authorizes local source and hermetic test-fixture changes only; it does not authorize cross-process locking, operating-system security mutation, or real external-state transaction execution.

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: HIGH

independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: REQUIRED_DIFFERENT_FIXTURE_AND_ASSERTION_PATH

positiveControl: independently inspect one same-identity replay and one
post-effect terminal-persistence failure against durable evidence.

negativeMutationClasses: conflicting launch identity; authority/scope/budget
mismatch; cancel/completion ordering; stale projection; missing artifact or
independent-verification evidence.

expectedInformationGain: distinguish worker suite self-consistency from
independently observable fail-closed durable-state behavior.

rerunCostReason: bounded fixtures cover decision-changing P2 claims without
duplicating the full worker audit.

reviewerDecisionOwner: LOCAL

The worker must run the two focused package suites and type/build checks after
final edits. The Local reviewer consumes their exact commands/results and may
run only M5/M10/safety/M20 checks unless a named contradiction justifies more.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: BOUNDED_PATH_FAMILIES

foreseeableFileSplitDisposition: COVERED_BY_BOUNDED_PATH_FAMILY

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact source/test manifest | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| source_reconciliation | WORKER_RETURN | worker | IMPLEMENTATION | seven-class matrix and input hash | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | adif_integrity |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | maximum manifest | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | source_reconciliation |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | worker return and allowed edits | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted worker paths | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material paths | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | reviewer disposition or completion review | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | material and continuity ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one internal worker followed by distinct Local reviewer/closer |
| phase | dispatch, bounded executable reconciliation, pending Local review |
| baseHeadFor(phase) | dispatchBaseHead=`81ad480b8`; executionBaseHead=worker capture after continuity; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exact maximum worker path manifest |
| traceScope(phase, actor) | worker return records full action trace, commands, and actual pending set |
| commitOwner(phase) | worker forbidden; Local closer only after acceptance |
| crossBatchIsolation | clean committed dispatch base; unrelated paths excluded |
| nextMoveSurfaces | worker return, Local review, material commit, separate continuity sync |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: internal worker after dispatch continuity passes

laneOwnedPaths: maximum worker path manifest only

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: terminal worker return, exact changed set, empty staged
set, focused tests, and worker-return full gate

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime-source-reconciliation`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "runtime-source-reconciliation" --role worker --lifecycle-phase implementation --max-results 12 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | deterministic negative cases, exact manifest, independent review, and no-commit boundary remain mandatory |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| literalTokensReviewed | envelope-first rule; exact source table columns; `DISPATCH_READY`; no-question rule; closeability graph; convergence fields; SCEC JSON; handoff scalars; dual-surface matrix; worker-return contract; trace labels; source-not-found spelling |
| gateRunPurpose | confirm completed packet after source/literal inspection; not first discovery or semantic acceptance |
| claimBoundary | static dispatch/output admission only; no P2 defect, fix correctness, runtime readiness, or closure is proved |

## Worker Output Checker Read-Ahead Mandate

Before writing the return or changing a reference owner, read checker sources
for its doc type/path/conditional content. The return uses real sections for:
Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk /
Corrective Action; Decision / Disposition; Checker Source Read-Ahead Block;
External Knowledge Intake Routing; Epistemic Process Block; Agent Operation
Trace Block; Delta Execution Claim Boundary Control Block; Public Export
Disposition; Return-Time Closeability Recheck; Changed Files; No-Commit
Statement. Use N/A with reason for non-applicable conditional sections.

## Work-Order Fulfillment Manifest

| Obligation | Owning artifact | Terminal worker evidence |
|---|---|---|
| exact input/source integrity | worker return | recomputed hash and exact locators |
| seven P2 classes | return plus two test files | row-level deterministic result and test name |
| accepted delta proof | tests and return | failing-before, minimal diff, passing-after |
| durable/projection truth boundary | return and conditional owner edit | state map and contradiction behavior |
| no new runtime or external intake | return | changed-set and forbidden-effect attestation |
| pending Local decision | return | `COMPLETE_PENDING_REVIEW` and row statuses |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_WORKER_RETURN_2026-09-25.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Decision / Disposition; Claim Boundary;
Checker Source Read-Ahead Block; External Knowledge Intake Routing; Epistemic
Process Block; Agent Operation Trace Block; Delta Execution Claim Boundary
Control Block; Public Export Disposition; executionBaseHead; git status
--short; Changed Files; No-Commit Statement; Return-Time Closeability Recheck.

Conditional terms: Rescan Intelligence Hardening; Corpus Completeness And
Report Integrity; Finding-To-Governance Learning Disposition; Machine Closure
Package. Use N/A with reason where inapplicable.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_COMPLETION_2026-09-25.md` only if separate closure evidence is necessary |
| reviewerOwnedClosurePaths | reviewer disposition, accepted source/test/contract edits, optional completion review, roadmap and continuity |
| closureOwner | Local reviewer/closer distinct from worker phase |
| workerCommitPermission | FORBIDDEN |

## Execution Plan

1. Complete startup acknowledgment and all first reads; capture execution base,
   clean status, input hash, material commit, continuity marker, and bound gate.
2. Map current durable identity/state transitions for both launchers without
   editing source.
3. Add deterministic tests for all applicable P2 classes; record current
   passes and exact failing negative cases.
4. For each proved failure only, make the smallest manifest-contained repair
   and record failing-before/passing-after evidence.
5. Run both focused suites and package type/build checks; repair in scope.
6. Write the single return from actual evidence, run the worker full gate,
   record exact pending status, and stop without staging or commit.

## Write Ownership

Worker owns create-only access to the exact return and modify access only to
the maximum manifest. Conditional implementation/contract paths require a
proved failing case. Worker owns no session, roadmap, dispatch, checker,
package-manifest, external-source, or commit surface.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE because P2 may change executable
durable-effect behavior.

Expected Result / Prediction: existing paths likely cover admission and simple
duplicate protection, while at least one crash-window, cross-identity, race,
projection, or semantic-completion case may be absent or fail closed only
implicitly.

Evidence Comparison Requirement: test every required class and record evidence
that confirms or contradicts the prediction.

Contradiction Handling Requirement: update disposition from evidence; do not
force a change. Stop when the correction needs a forbidden owner or authority.

Claim Update Requirement: every class receives one allowed P2 disposition and
remains pending Local review.

## Evidence Requirements

- recomputed input hash and `executionBaseHead`;
- exact source/symbol/state map for both paths;
- seven-class matrix with deterministic test names/results;
- failing-before/passing-after output for each accepted delta;
- pre/post SHA-256 for each modified implementation/contract file;
- exact changed and staged sets, with staged set empty;
- focused package tests, type/build checks, bound autorun, and worker full gate;
- zero external invocation, dependency install, live/public action, or commit.

## Verification Commands

```powershell
npm test -- --run tests/mao.operational.worker.launcher.test.ts
npm run check
npm run test:run -- src/cli/governed-command-launcher.test.ts
npm run build
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_2026-09-25.md
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git diff --check
git diff --cached --name-only
git status --short --untracked-files=all
```

Run the first two commands from `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` and
the next two from `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER`.

## Acceptance Criteria

- [ ] Input hash and dispatch release evidence match.
- [ ] Both current launch paths are mapped before any implementation edit.
- [ ] All seven P2 classes have deterministic evidence and one allowed
  disposition with `PENDING_LOCAL_REVIEW`.
- [ ] Every source/contract change has failing-before and passing-after proof.
- [ ] Replay/recovery identity and mismatch cases fail closed without duplicate
  effect, unrelated settlement, or fabricated completion.
- [ ] Projection remains non-authoritative and contradiction is observable.
- [ ] Semantic completion is withheld where artifact or independent
  verification evidence is required but missing.
- [ ] Focused tests, package checks, bound gate, and worker full gate pass.
- [ ] Exact changed set is inside manifest; nothing is staged or committed.

Fail conditions: input drift; missing material/continuity evidence; unsupported
source claim; outside-manifest need; new runtime/owner; nondeterministic-only
finding; external/live/public need; dependency change; or unrepairable gate.

## Review Gate

The Local reviewer consumes worker evidence and does not recreate the full
seven-class audit. Review is bounded to hash/source integrity, test-to-claim
coherence, failing/passing delta proof, changed paths, key safety assertions,
and required gates. Any broad rerun needs a named contradiction, expected
information gain, and review-cost reason.

## Operator Checkpoint

No further checkpoint is required inside the exact packet. A fresh operator
decision is required for a new runtime/owner, Unreal intake, outside-manifest
work, P3/P4, provider/live/public/deployment action, or higher risk.

## Closure Checklist

- [ ] Seven-class matrix and both owner maps are complete.
- [ ] Proved defects alone produced minimal changes.
- [ ] Focused suites and package checks pass.
- [ ] Forbidden paths/actions remain untouched.
- [ ] Worker full gate passes after final edits.
- [ ] Actual pending set is recorded; staged/committed worker set is empty.
- [ ] Return-Time Closeability Recheck has no unresolved outside-authority blocker.
- [ ] Local review, material commit, and continuity remain pending.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` before edits when dispatch release evidence is
absent. Stop during execution for any fail condition above. Otherwise return
`COMPLETE_PENDING_REVIEW` only after final evidence and gates pass. A fully
`CONFIRMED_EXISTING` audit is valid completion, not a blocker.

Only those two terminal worker states are allowed. Do not claim closure,
commit, partial readiness, or request routine in-scope choices.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher/orchestrator |
| Provider or surface | private shared CVF workspace |
| Session or invocation | ACEL-AKOE-P2 dispatch authoring, 2026-09-25 |
| Working directory | repository root |
| Command or tool surface | governed reads, exact hashes/searches, scaffold preview, patching, gates, Git |
| Target paths | paired P2 baseline and work order |
| Allowed scope source | operator `next` plus accepted AKOE P2 roadmap row |
| Before status evidence | clean worktree at HEAD `81ad480b8`; P1 closed; P2 checkpoint pending operator and then authorized |
| After status evidence | paired bounded P2 packet; implementation still gated by material and continuity commits |
| Diff evidence | exact paired paths against dispatch base |
| Approval boundary | dispatch authoring/release only; no worker implementation or P2 acceptance |
| Claim boundary | no defect finding, fix correctness, provider/live, external, public, P3/P4, or production claim |
| Agent type | Local orchestrator/reviewer as dispatch author |
| Invocation ID | `acel-akoe-p2-dispatch-20260925` |
| Expected manifest | paired baseline and work order |
| Actual changed set | verified before handoff |
| Manifest delta | expected zero after authoring repair |
| Deletion or rename disposition | N/A with reason: none authorized or performed |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | bounded local tests and conditional repair of two existing execution paths |
| claimDisposition | N/A with reason: dispatch only; runtime behavior is not accepted until worker evidence and Local review |
| receiptEvidence | N/A with reason: dispatch authoring creates no runtime or external-action receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source locators, hashes, diffs, local tests, and governance gates |
| invocationBoundary | existing MAO adapter and governed-command runner test seams; no real external action |
| interceptionBoundary | no IDE/shell/filesystem/provider interception or mandatory wrapper claim |
| claimLanguage | deterministic local reconciliation pending independent Local acceptance |
| forbiddenExpansion | new runtime/owner, Unreal intake, checker/package changes, external/provider/live/public/P3/P4/deployment, worker commit |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-AKOE-P2 --title "ACEL AKOE-P2 Durable Intent And Projection Reconciliation" --date 2026-09-25 --base 81ad480b86074b0d8e40025cde8a95c9051e6a0e --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/roadmaps/CVF_ACEL_APPLIED_KNOWLEDGE_OWNER_ENRICHMENT_ROADMAP_2026-09-25.md --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence NONE --scec-problem-key acel-akoe-p2-durable-intent-projection --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope EXECUTABLE_IMPLEMENTATION --stdout` |
| generatedProfile | generic worker initial dispatch with no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | completed exact authority, scope, source, test, path, closeability, convergence, evidence, and stop contracts |
| checkerReadAheadConfirmation | dispatch, structure, trace, ADIF, closeability, convergence, handoff, lifecycle, routing, review-probe, public, and encoding checker sources inspected |
| docOnlyNewFields | seven-class matrix, state-transition map, identity tuple, and failing-before/passing-after trace |
| claimBoundary | dispatch provenance only; no worker result, runtime acceptance, external action, or closure claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: P2 is private-provenance source/test reconciliation with no public-sync
remote, public commit, artifact path, or publication authority.

## Claim Boundary

This order authorizes one no-commit internal worker to audit the seven P2
classes, add deterministic tests to the two existing test owners, create the
single worker return, and conditionally make minimal proved-gap repairs within
the exact manifest. It does not authorize a new runtime, Unreal intake,
checker/package/session changes, external/provider/live work, P3/P4, public
sync, certification, deployment, production, or worker commit.
