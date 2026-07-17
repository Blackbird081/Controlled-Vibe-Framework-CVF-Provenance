# CVF Agent Work Order - MAO-OA-T3 Operational Worker Launcher And Liveness Wiring

Memory class: FULL_RECORD

Date: 2026-07-17

Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR

Work Order ID: MAO-OA-T3

Risk class: R2

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `adff6895b`

Paired baseline:
`docs/baselines/CVF_GC018_MAO_OA_T3_OPERATIONAL_WORKER_LAUNCHER_AND_LIVENESS_WIRING_2026-07-17.md`

## Dispatch Prompt Envelope

Role: delegated implementation worker for MAO-OA-T3.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T3_OPERATIONAL_WORKER_LAUNCHER_AND_LIVENESS_WIRING_2026-07-17.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture `git rev-parse --short HEAD` before any write.

Current-time notes: MAO-OA-T2 is independently accepted at material commit
`042abf44b`; the 2026-07-17 human release authorizes this exact T3 worker
execution only after the committed dispatch packet and continuity sync exist.

Do-not-misread notes: this is deterministic local execution-plane composition
using the existing fake/local adapter. Do not call a provider, import the
control plane into execution source, add a router, process, queue, CLI/MCP/UI,
or claim durable production liveness.

Required first actions: read `CVF_SESSION_MEMORY.md`, resolve
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, read the active handoff, guard
orientation, literal gotchas, this work order, the paired baseline, canonical
MAO contract/schema, every existing source owner cited below, and applicable
checker source. Then record startup acknowledgment and capture
`executionBaseHead` before editing.

Return contract: implement exactly the six-path manifest, run required tests
and gates, leave all changes uncommitted and unstaged, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement one operational worker-launcher composition owner that resumes the
accepted durable run, invokes the existing provider-neutral fake/local adapter,
uses the deterministic lifecycle controller for heartbeat/timeout/cancellation,
and persists canonical admitted/running/terminal milestones without duplicating
any existing owner.

## Authority Chain

1. Direct operator continuation instruction on 2026-07-17.
2. Active session next move following accepted T2 closure.
3. Governing MAO-OA roadmap T3 row.
4. Paired GC-018 baseline.
5. This source-verified work order.
6. Canonical MAO runtime foundation contract and current source owners.

## Agent Roles

| Role | Responsibility | Commit authority |
|---|---|---|
| dispatcher | source verification, packet authoring, pre-dispatch proof, material dispatch commit | packet paths only |
| delegated worker | exact six-path implementation and evidence return | FORBIDDEN |
| independent reviewer/closer | semantic recomputation, bounded allowed-scope correction if needed, completion review, material closure commit | closure paths only |
| session-sync steward | protected continuity following material decision | separate protected commit only |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- active handoff named by the registry
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- paired baseline, this work order, canonical MAO contract/schema, and every
  current source file cited by Source Verification
- checker sources named by Checker Source Read-Ahead Block

## Pre-Flight Checks

Before writing, record clean status and `executionBaseHead`, confirm all six
allowed paths are the only prospective worker changes, run the ADIF resolver,
and run pre-implementation autorun from the captured base. Any unrelated or
staged change blocks execution.

## Write Ownership

Worker owns only the exact six Allowed Scope paths. Roadmap, baseline, work
order, completion review, protected session files, existing MAO owners, and all
other repository paths are forbidden to the worker. Reviewer/closer owns any
accepted closure conversion and material commit.

## Evidence Requirements

Required evidence is direct source inspection, focused Vitest output, package
typecheck, full package regression output, durable restart/replay assertions,
adapter call-count assertions, GC-051 generation and coverage, worker-return
fast gate, exact status/diff output, and unchanged worker HEAD.

## Operator Checkpoint

SATISFIED. The operator's direct continuation instruction on 2026-07-17
releases the T3 packet and exact bounded worker execution described here. It
does not release T4-T7 or any real provider/live/public action.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator continuation plus accepted T2 closure and T3 roadmap row |
| Intake role | delegated worker implements the exact bounded launcher composition |
| Reviewer role | independent reviewer recomputes source, tests, durable evidence, and boundaries |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; exact six-path return |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `SINGLE_AGENT_SINGLE_ROLE` |
| selected role route | worker return to independent reviewer/closer |
| escalation condition | return `BLOCKED_WITH_REASON` for source contradiction, forbidden-path need, unrelated worktree state, or missing authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | N/A with reason: this is repository implementation dispatch, not external knowledge absorption |
| Matching local-view guard | N/A with reason: no external knowledge intake is admitted |
| Owner surface | canonical repository source and governed T3 packet |
| Disposition | NOT_APPLICABLE_WITH_REASON: no outside-source fact is admitted by this work order |
| Claim boundary | routing disclosure only; Claude execution output remains evidence pending independent review |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| accepted T2 durable-store closure | material commit `042abf44b`; `docs/reviews/CVF_MAO_OA_T2_COMPLETION_REVIEW_2026-07-16.md`; reviewer-accepted bounded status | durable store and replay owner must exist before launcher wiring | ACCEPT |
| T3 human release | direct operator instruction on 2026-07-17 | active next move required explicit release | ACCEPT |
| dispatch authoring base | clean `adff6895b` | packet authored from clean post-T2 continuity HEAD | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-OA-T3 --title "MAO Operational Worker Launcher And Liveness Wiring" --date 2026-07-17 --base adff6895b --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MAO-OA-T2 accepted closure 042abf44b" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced scaffold blanks with direct source verification, exact launcher behavior, six-path manifest, worker-return shape, and reviewer closure conversion |
| checkerReadAheadConfirmation | dispatch-quality, structural, ADIF, handoff, trace, delta-claim, worker-return, registry, file-size, and public-export checker surfaces reviewed |
| docOnlyNewFields | all proposed launcher symbols are separated below; no new symbol is claimed as current source |
| claimBoundary | dispatch authoring provenance only; no implementation/provider/live/public proof |

## Worker Autonomy / No-Question Rule

Allowed-scope source, test, registry, worker-return, formatting, and checker
failures must be corrected directly. Return to orchestrator only when source
contradicts a required invariant, a safe solution requires a forbidden path or
new dependency, the worktree contains unrelated changes, or authority is
missing. Do not ask stylistic or implementation-preference questions when the
source-backed contract determines the answer.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-implementation`, surfaceSelector=`MAO`.

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-implementation --surface-selector MAO --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | no extra ADIF control; canonical work-order and no-commit controls remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_changed_corpus_registry_coverage.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR; Dispatch Prompt Envelope; Role:; Canonical packet:; Commit mode:; executionBaseHead; Dependency Release Evidence; ADIF Defect Registry Disclosure; Source Verification Block; New Doc-Only Fields; Roadmap-To-Work-Order Trace Matrix; Required Artifact Manifest; Worker Return Packet Shape Contract; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Epistemic Process Block; Execution Plan; Verification Commands; Acceptance Criteria; Closure Diff Gate; Machine Closure Package; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm exact source-backed T3 dispatch and worker return contract before material commit |
| claimBoundary | checker conformance does not prove launcher correctness, provider behavior, production liveness, or value |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T3 requires launcher, heartbeat, timeout, cancellation, and provider-neutral adapter wiring | LITERAL_INVARIANT | `docs/roadmaps/CVF_MAO_OPERATIONAL_ADOPTION_AND_AGENT_EXECUTION_ASSURANCE_ROADMAP_2026-07-16.md` | Work Plan And Dependencies T3 row | `MAO-OA-T3` | roadmap tranche table | ACCEPT |
| durable run creation, replay, and append exist | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | lines 98-203 | `MaoFileRunStore`; `createRun`; `resumeRun`; `appendEvent` | `MaoFileRunStore` | ACCEPT |
| durable append replays through the canonical ledger before atomic replacement | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | lines 165-203 | `appendEvent` | `MaoFileRunStore` | ACCEPT |
| fake/local provider-neutral invocation exists | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/delegation.adapter.contract.ts` | lines 149-268 | `MaoDelegationAdapter`; `invoke` | `MaoDelegationAdapter` | ACCEPT |
| adapter handles admission, authority, role, capability, manifest, and idempotency failure | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/delegation.adapter.contract.ts` | lines 168-257 | `invoke` | `MaoDelegationAdapter` | ACCEPT |
| deterministic lifecycle operations exist | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/lifecycle.controller.contract.ts` | lines 240-329 | `MaoLifecycleController` | `MaoLifecycleController` | ACCEPT |
| lifecycle controller exposes timeout, heartbeat, cancellation, duplicate, retry, orphan, and clock controls | VALUE_SET | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/lifecycle.controller.contract.ts` | lines 253-329 | `checkTimeout`; `heartbeat`; `requestCancel`; `acceptCancel`; `mayStartNewChild`; `claimInvocation`; `classifyOrphan`; `advanceClock` | `MaoLifecycleController` | ACCEPT |
| heartbeat is liveness-only | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Idempotency, Retry, Cancel, And Recovery | `Heartbeat proves liveness only` | canonical MAO contract | ACCEPT |
| cancellation is idempotent and blocks child admission once accepted | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Idempotency, Retry, Cancel, And Recovery | `Cancellation is idempotent` | canonical MAO contract | ACCEPT |
| canonical task transitions are fixed | VALUE_SET | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Task Lifecycle State Transition Table | `planned`; `admitted`; `running`; `succeeded`; `cancelled`; `timed_out`; `failed` | canonical MAO contract | ACCEPT |
| `MaoEventType` union exists for canonical milestones | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | lines 41-52 | `MaoEventType` | `MaoEventType` | ACCEPT |
| ledger rejects duplicate keys and invalid transitions before append | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | lines 182-243 | `append` | `MaoEventLedger` | ACCEPT |
| provider policy remains control-plane router ownership | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Provider-Neutral Capability Port | `ProviderRouterContract.route` | canonical MAO contract | ACCEPT |
| MAO local barrel is the additive export surface | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | current export list | `export *` | MAO local barrel | ACCEPT |

## New Doc-Only Fields

The symbols below are new implementation requirements, not existing-source
claims.

| Proposed symbol | Required shape | Disposition |
|---|---|---|
| `MaoOperationalWorkerLauncher` | class or equivalent single owner constructed with explicit durable-store, adapter-invocation, and lifecycle dependencies | DOC_ONLY_NEW |
| `MaoOperationalLaunchRequest` | graph/task admission, capability, input manifest, idempotency key, start time, and optional timeout ceiling | DOC_ONLY_NEW |
| `MaoOperationalLaunchResult` | typed success or fail-closed result carrying invocation/durable evidence or classified reason | DOC_ONLY_NEW |
| `MaoOperationalAdapterPort` | minimal structural port containing the existing adapter `invoke` shape, enabling call-count tests without a second adapter owner | DOC_ONLY_NEW |
| `launch` | durable resume, cancellation/duplicate check, admission milestone, adapter call, running milestone, and terminal milestone | DOC_ONLY_NEW |
| `heartbeat` | graph/task validation plus lifecycle-only heartbeat record | DOC_ONLY_NEW |
| `recordTimeout` | deterministic timeout check and durable timeout milestone only when elapsed | DOC_ONLY_NEW |
| `requestCancellation`; `acceptCancellation` | idempotent lifecycle cancellation; acceptance writes one durable cancelled milestone | DOC_ONLY_NEW |

## Current Runtime Freshness Verification

| Verification | Command/evidence | Result |
|---|---|---|
| clean authoring base | `git status --short --untracked-files=all`; `git rev-parse --short HEAD` | empty; `adff6895b` |
| proposed path absence | six `Test-Path` checks | all `False` |
| proposed symbol absence | `rg -n "MaoOperationalWorkerLauncher|operational.worker.launcher"` over execution source/tests and governed packets | no current owner |
| T3 authority | roadmap and T0/T2 completion reads | exact T3 row plus accepted T2 dependency |
| existing owner APIs | direct reads of store, adapter, lifecycle, ledger, graph, and barrel | symbols above confirmed current |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| second adapter owner | existing `MaoDelegationAdapter` is mandatory and may not be copied or replaced | REJECT_DUPLICATE |
| second lifecycle owner | existing `MaoLifecycleController` is mandatory and may not be copied or modified | REJECT_DUPLICATE |
| second durable/event owner | existing `MaoFileRunStore` and `MaoEventLedger` remain execution truth | REJECT_DUPLICATE |
| provider router import | control-plane `ProviderRouterContract` exists, but execution-to-control import would violate retained dependency direction | REJECT |
| launcher collision | no existing `MaoOperationalWorkerLauncher` or planned source/test path | ACCEPT_NEW_OWNER |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_MAO_OA_T2_COMPLETION_REVIEW_2026-07-16.md`

priorVerificationAnchor: material commit `042abf44b`

recomputeReason: T3 composes current runtime owners and therefore requires a
fresh source read plus new behavior tests from the committed execution base

freshRecomputeRequired: YES; re-read current owner source and rerun focused,
typecheck, package, registry, and governance checks

unicodePathHandling: literal paths and UTF-8-safe readers are required

extractedTextAuthority: N/A with reason

## Roadmap-To-Work-Order Trace Matrix

| Roadmap T3 requirement | Work-order instruction | Required evidence | Disposition |
|---|---|---|---|
| governed worker launcher | one new launcher composition owner | focused launch success/rejection/duplicate tests | ACCEPT |
| provider-neutral adapter wiring | inject and call existing `MaoDelegationAdapter.invoke` shape | call-count and receipt-preservation tests using fake/local behavior | ACCEPT |
| heartbeat | delegate to lifecycle controller; liveness-only | fresh/stale and no-authority-renewal assertions | ACCEPT |
| timeout | use lifecycle clock/check and persist timeout only when elapsed | before/after ceiling tests and durable replay | ACCEPT |
| cancellation | request/accept through lifecycle; block new child; persist accepted cancel | idempotency, block, and durable cancelled state tests | ACCEPT |
| durable progress | append canonical admission/start/terminal events through T2 store | resume/replay assertions | ACCEPT |
| diagnostics | typed fail-closed result for store, adapter, transition, cancel, and timeout errors | negative-path tests | ACCEPT |
| bounded claim | fake/local and temp-directory only | worker return and completion-review boundary | ACCEPT |

## Design Control Carry-Forward

The worker must preserve these invariants:

1. store, adapter, lifecycle, ledger, graph, and router policy owners are reused;
2. no execution-plane source imports a control-plane owner;
3. launcher dependencies are explicit and testable, not global singletons;
4. heartbeat remains in-memory liveness evidence only;
5. accepted cancellation blocks a new child and writes at most one durable
   terminal cancel milestone;
6. timeout writes no event before the strict ceiling is exceeded;
7. the same launch idempotency key never calls the adapter twice;
8. adapter rejection never becomes success and produces a typed failure;
9. durable append failure stops later milestones and is surfaced; and
10. no silence, heartbeat, or local adapter receipt is upgraded into provider,
    production, or user-value proof.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| storage owner | existing `MaoFileRunStore` only |
| root selection | caller-supplied temporary/local root; launcher does not select a global repository path |
| durable truth | graph plus canonical `MaoEventLedgerEntry` sequence |
| generated aggregate | GC-051 aggregate remains generator-owned |
| new dependency | forbidden |
| database/migration/retention/lock | forbidden |

## Allowed Scope

Worker may change exactly:

1. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts`
2. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts`
3. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.operational.worker.launcher.test.ts`
4. `docs/corpus-intelligence/registry/entries/mao-oa-t3-operational-worker-launcher-surfaces.json`
5. `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` through the existing generator
6. `docs/reviews/CVF_MAO_OA_T3_WORKER_RETURN_2026-07-17.md`

## Forbidden Scope

- every existing MAO source/test other than the local barrel;
- both package-root barrels;
- control-plane source/tests and `ProviderRouterContract`;
- package manifests, lockfiles, dependencies, install commands, databases,
  schemas, canonical MAO reference contracts, or transition enums;
- queue, process, thread, shell, provider SDK, credentials, network, CLI, MCP,
  Web/UI, workspace state, or operator projection;
- reviewer/closer/dissent/commit/session execution;
- roadmap, baseline, work order, completion review, session, handoff, Catalog,
  GAP, ADIF, checker, hook, CI, public-sync, or push mutation; and
- T4-T7 implementation or evidence claims.

## Work-Order Fulfillment Manifest

| Requirement | Fulfillment owner | Required output | Dispatch state |
|---|---|---|---|
| source implementation | worker | launcher source plus local-barrel export | RELEASED |
| behavioral proof | worker | focused deterministic test file and package checks | RELEASED |
| corpus accountability | worker | per-entry GC-051 source plus generated aggregate | RELEASED |
| no-commit evidence | worker | full worker return at the exact governed path | RELEASED |
| independent acceptance | reviewer/closer | completion review and material closure commit | PASS |
| continuity | session-sync steward | separate protected sync following material decision | N/A with reason: follows material commit |

## Required Artifact Manifest

| Path | Required action | Owner |
|---|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | create bounded composition owner | worker |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | add one local export | worker |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.operational.worker.launcher.test.ts` | create focused deterministic temp-directory tests | worker |
| `docs/corpus-intelligence/registry/entries/mao-oa-t3-operational-worker-launcher-surfaces.json` | create narrow source entry covering all cited T3 execution surfaces | worker |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | regenerate, never hand-edit | worker |
| `docs/reviews/CVF_MAO_OA_T3_WORKER_RETURN_2026-07-17.md` | create checker-complete no-commit return | worker |

Expected worker changed-set cardinality: exactly 6 paths.

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | capture clean `executionBaseHead`, startup acknowledgment, and exact source reads | worker return |
| 2 | create launcher with explicit injected existing-owner dependencies and typed results | source inspection |
| 3 | export launcher from MAO local barrel only | barrel diff and import test |
| 4 | add launch, duplicate, rejection, heartbeat, timeout, cancel, and durable-replay tests | focused Vitest output |
| 5 | add GC-051 source entry and regenerate aggregate | generator and coverage checks |
| 6 | create full worker return, run fast gate, confirm exactly six uncommitted unstaged paths | return evidence |

## Required Launcher Behavior

### Launch sequence

For a fresh durable run, `launch` must:

1. call durable resume and fail closed when the graph cannot be loaded;
2. verify the requested task exists and cancellation permits a new child;
3. prevent duplicate execution using a stable key bound to the caller's launch
   idempotency key;
4. append `TASK_ADMITTED` with resulting state `admitted` through the durable
   store;
5. call the injected existing adapter `invoke` exactly once;
6. on adapter rejection, append a legal blocked milestone when possible and
   return the exact diagnostic/reason without claiming execution success;
7. on adapter success, append `INVOCATION_STARTED` with `running`, then
   `INVOCATION_COMPLETED` with `succeeded`; and
8. return the adapter receipt plus durable milestone evidence.

Every internal durable event idempotency key must be deterministically derived
from the caller's launch key and milestone name so replay cannot collide across
different milestones. A repeated caller launch key must stop before a second
adapter call.

### Heartbeat

`heartbeat` must validate the durable graph/task, call the existing lifecycle
controller, and return its `livenessOnly: true` record. It must not write a
per-heartbeat durable event, renew authority, extend budget or timeout, imply
progress, or claim restart durability.

### Timeout

`recordTimeout` must locate the latest persisted invocation-start timestamp,
use `MaoLifecycleController.checkTimeout`, write nothing at or below the
ceiling, and append exactly one `TIMEOUT_DETECTED` / `timed_out` milestone only
after the strict ceiling is exceeded. Repeated timeout recording must fail
closed without a duplicate durable event.

### Cancellation

`requestCancellation` must use the existing controller and immediately block a
new child in that controller instance. `acceptCancellation` must be idempotent,
require a valid request/running task, use the existing controller, and persist
exactly one `CANCEL_ACCEPTED` / `cancelled` milestone. A restarted launcher must
also fail closed when durable replay already shows the task terminal-cancelled.

### Failure vocabulary

Worker may define a compact T3-specific failure union but must not change any
existing reason enum. It must distinguish at least durable-store rejection,
unknown/non-runnable task, cancellation boundary, duplicate launch, adapter
rejection, and lifecycle milestone persistence failure. It must carry existing
adapter diagnostic evidence rather than translating rejection into success.

## Focused Test Matrix

Required tests include:

- successful fresh launch persists admitted, running, and succeeded in order;
- durable resume after creating a new store instance reproduces terminal state;
- same launch key calls adapter once and returns typed duplicate/replay outcome;
- adapter authority/admission/capability rejection remains a failure;
- durable append rejection stops later milestones;
- heartbeat is liveness-only and creates no durable event;
- heartbeat staleness follows deterministic clock advancement;
- timeout writes nothing at the ceiling and one timed-out milestone above it;
- cancellation request blocks launch before adapter invocation;
- cancellation acceptance is idempotent and persists one cancelled milestone;
- terminal cancelled state remains closed after creating a new launcher/store;
- unknown graph/task and invalid state fail closed;
- source imports contain no control-plane/router/provider/network owner; and
- local barrel exports the new owner.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MAO_OA_T3_WORKER_RETURN_2026-07-17.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required section names: Purpose; Target / Source; Scope / Methodology; Findings
/ Position; Risk / Corrective Action; Checker Source Read-Ahead Block; Agent
Operation Trace Block; Delta Execution Claim Boundary Control Block; Public
Export Disposition; External Knowledge Intake Routing; Rescan Intelligence
Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance
Learning Disposition; Epistemic Process Block; Claim Boundary; git status
--short; Changed Files; Worker Experience Retrospective; Command Evidence;
No-Commit Statement.

Do not pass a Vitest TypeScript path to `--pytest-target`. Use the package npm
test command for source tests and run the worker-return fast gate without an
inapplicable pytest target.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | delegated implementation worker; independent reviewer/closer follows |
| phase | DISPATCH then EXECUTION then REVIEWER_CLOSURE |
| baseHeadFor(phase) | dispatchBaseHead=`adff6895b`; executionBaseHead=worker captures committed dispatch/sync HEAD; closureBaseHead=reviewer captures unchanged worker HEAD |
| changedSetScope(phase) | dispatch=roadmap plus baseline plus work order; execution=exact six worker paths; closure=worker paths plus reviewer-owned closure paths only |
| traceScope(phase, actor) | each actor records only paths changed in that actor's phase |
| commitOwner(phase) | dispatcher commits packet; worker must not commit; reviewer/closer owns material closure; session-sync steward owns separate continuity commit |
| crossBatchIsolation | clean worktree required; T4-T7 and every unrelated lane parked |
| nextMoveSurfaces | worker forbidden; reviewer/closer updates roadmap and protected continuity only after accepted material closure |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MAO_OA_T3_COMPLETION_REVIEW_2026-07-17.md` |
| reviewerOwnedClosurePaths | governing roadmap; paired baseline; this work order; worker return; completion review; allowed source/test review repairs; narrow GC-051 source/aggregate repair if independently required |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Epistemic Process Block

Epistemic Process Applicability: BOUNDED_GOVERNANCE_IMPLEMENTATION

Expected Result / Prediction: existing durable, adapter, lifecycle, ledger, and
graph owners can be composed behind one local launcher without source changes
to those owners or any real provider call.

Evidence Comparison Requirement: worker and reviewer compare source imports,
exact event sequence, adapter call count, deterministic liveness/cancel/timeout
behavior, durable replay, focused/package tests, and registry/gate evidence
against that prediction.

Contradiction Or Gap Disposition: any need to change an existing owner, import
the control plane, add a provider/router/network/process dependency, or invent
an incompatible transition blocks the worker and returns to orchestrator.

Claim Update Requirement: closure must state whether the local composition
prediction is confirmed, narrowed, or rejected. It must not promote fake/local
evidence into provider, production, or user-value proof.

## Verification Commands

Run from repository root. For npm commands use
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` as working directory.

```powershell
git status --short --untracked-files=all
git rev-parse --short HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
npm test -- tests/mao.operational.worker.launcher.test.ts
npm run check
npm test
python governance/compat/generate_corpus_scan_registry.py --generate
python governance/compat/generate_corpus_scan_registry.py --check
python governance/compat/check_changed_corpus_registry_coverage.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
git status --short --untracked-files=all
git rev-parse --short HEAD
```

## Acceptance Criteria

- exactly six allowed paths changed and none staged;
- HEAD equals captured `executionBaseHead`;
- no forbidden import, dependency, owner, or later-tranche behavior;
- launch sequence and typed failure behavior match this packet;
- duplicate launch cannot call the adapter twice;
- heartbeat, timeout, and cancellation tests match canonical semantics;
- durable replay proves terminal launch/timeout/cancel milestones survive a new
  store instance;
- focused tests, typecheck, full package tests, registry checks, file-size
  check, worker-return fast gate, and diff hygiene pass;
- every failure is disclosed rather than waived; and
- worker return is `COMPLETE_PENDING_REVIEW`, not a closure claim.

## Review Gate

Independent reviewer must inspect every changed line, recompute adapter call
count and event order, rerun focused/typecheck/package tests, reproduce durable
restart evidence, verify registry coverage, and confirm no provider/router,
T4-T7, session, public, or push scope entered the worker batch.

## Closure Diff Gate

Reviewer compares roadmap T3 row, canonical MAO lifecycle/adapter rules, paired
baseline, this work order, exact six-path worker diff, tests, worker claims,
completion review, registry state, and final roadmap/session state. Every item
must be PASS, N/A with reason, or BLOCKED with return action.

## Closure Checklist

| Item | Required closure disposition |
|---|---|
| exact six-path worker set | reviewer recomputed |
| no-commit boundary | reviewer verified |
| existing-owner reuse and dependency direction | reviewer proven |
| launch event order and adapter call count | reviewer proven |
| duplicate, rejection, heartbeat, timeout, and cancel negatives | reviewer rerun |
| durable restart/replay evidence | reviewer rerun |
| focused, typecheck, and full package tests | reviewer rerun |
| GC-051 source/aggregate alignment | reviewer rerun |
| roadmap and session continuity | reviewer/closer and session-sync steward only |
| public export | DEFERRED_PRIVATE_ONLY unless separately authorized |

## Reviewer Closure Decision

`REVIEWER_ACCEPTED_BOUNDED_WITH_REPAIR`.

The worker implementation is accepted after independent recomputation, one
reviewer-owned real-adapter rejection test expansion, and one worker-return
fast-gate evidence correction. T4-T7 remain parked.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR` | PASS |
| Completion or reviewer artifact | T3 completion review | `Status: REVIEWER_ACCEPTED_BOUNDED_WITH_REPAIR` | PASS |
| Roadmap state | governing MAO-OA roadmap | `Status: MAO_OA_T3_PASS_BOUNDED_OPERATOR_CHECKPOINT_NEXT` | PASS |
| Registry JSON | T3 source entry and generated aggregate | generator check and zero coverage violations | PASS |
| Registry Markdown | GC-051 JSON source and aggregate; no separate Markdown owner | generator and coverage checks | PASS |
| External evidence digest | N/A with reason: no external evidence consumed | none | N/A with reason |
| System loop interlock | N/A with reason: no repository governance loop/process launcher mutation | none | N/A with reason |
| Session continuity | protected active state, front door, and handoff | separate session-sync commit follows material closure | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Required evidence | Dispatch state |
|---|---|---|
| local launcher behavior | 22/22 focused fake/local temp-directory tests | PASS |
| provider acceptance | N/A with reason: provider invocation forbidden | N/A_WITH_REASON |
| reviewer acceptance | independent completion review | PASS |
| public acceptance | N/A with reason: public action forbidden | N/A_WITH_REASON |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` without scope expansion when:

- safe behavior requires modifying an existing MAO owner or transition enum;
- execution-plane must import control-plane router/policy source;
- provider/network/process/queue/package dependency becomes necessary;
- durable/event semantics cannot express the required legal state changes;
- exact six-path manifest cannot be preserved;
- unrelated worktree changes appear;
- a new repeated/non-obvious defect needs ADIF mutation outside worker scope; or
- worker commit/staging becomes necessary.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | Codex local private provenance workspace |
| Session or invocation | MAO-OA-T3 dispatch authoring, 2026-07-17 |
| Working directory | repository root |
| Command or tool surface | governed reads, source searches, ADIF resolver, scaffold preview, apply_patch, governance gates, git |
| Target paths | governing roadmap; paired T3 baseline; this T3 work order |
| Allowed scope source | direct human release, active next move, accepted T2 closure, governing roadmap, canonical MAO contract |
| Before status evidence | clean worktree at `adff6895b`; planned T3 packet/source paths absent |
| After status evidence | exact three-path dispatch packet pending verification and material commit |
| Diff evidence | `git diff --name-status`; `git diff --check`; pre-dispatch range from `adff6895b` |
| Approval boundary | T3 local fake-adapter launcher/liveness implementation dispatch only |
| Claim boundary | no worker implementation, real provider action, T4-T7, live, public, session, or push action by dispatcher |
| Agent type | dispatcher |
| Invocation ID | `mao-oa-t3-dispatch-2026-07-17` |
| Expected manifest | `docs/roadmaps/CVF_MAO_OPERATIONAL_ADOPTION_AND_AGENT_EXECUTION_ASSURANCE_ROADMAP_2026-07-16.md`; `docs/baselines/CVF_GC018_MAO_OA_T3_OPERATIONAL_WORKER_LAUNCHER_AND_LIVENESS_WIRING_2026-07-17.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T3_OPERATIONAL_WORKER_LAUNCHER_AND_LIVENESS_WIRING_2026-07-17.md` |
| Actual changed set | `docs/roadmaps/CVF_MAO_OPERATIONAL_ADOPTION_AND_AGENT_EXECUTION_ASSURANCE_ROADMAP_2026-07-16.md`; `docs/baselines/CVF_GC018_MAO_OA_T3_OPERATIONAL_WORKER_LAUNCHER_AND_LIVENESS_WIRING_2026-07-17.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T3_OPERATIONAL_WORKER_LAUNCHER_AND_LIVENESS_WIRING_2026-07-17.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | local execution-plane launcher composition using existing durable store, fake/local adapter, lifecycle controller, and event ledger |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE after deterministic focused tests and independent review only |
| receiptEvidence | CVF_RECEIPT_PRESENT only as existing fake/local invocation receipt and durable MAO event entries; no provider receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT only for bounded temp-directory filesystem and fake/local adapter tests |
| invocationBoundary | package-local focused tests, typecheck, temp-directory I/O, fake/local adapter, registry generation, and governance checks |
| interceptionBoundary | no IDE/shell/git/provider interception, wrapper/proxy enforcement, runtime gate, or agent coding-control claim |
| claimLanguage | bounded internal operational-launcher component; not a production or provider orchestrator |
| forbiddenExpansion | no real provider/router/network/process/queue, T4-T7, live/public/session/push work |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch. No public artifact,
public-sync operation, or public claim is authorized.

## Claim Boundary

This work order authorizes exactly one execution-plane launcher composition
owner, one local-barrel export, focused deterministic tests, narrow GC-051
source/aggregate coverage, and one no-commit worker return. It does not
authorize or prove real provider routing or execution, durable heartbeat across
restart, distributed concurrency, process isolation, CLI/MCP/UI ingress,
reviewer/closer execution, automatic commit/session mutation, live governance,
public or production readiness, scale, shipment, or user value.
