# CVF Multi-Agent Orchestration Runtime Foundation Roadmap

Memory class: FULL_RECORD

Date: 2026-07-11

Status: PROPOSED

Roadmap ID: MAO

## Purpose

Define a bounded, evidence-first route from CVF's existing handoff, workspace,
execution, review, commit, and session-sync contracts to a verifiable
multi-agent orchestration runtime foundation. The foundation must make one
worker the default, add independent roles only when risk or evidence value
justifies them, and preserve exactly one designated closer.

This roadmap is design and sequencing authority only. It does not authorize a
runtime implementation, provider call, queue, scheduler, public projection, or
production-readiness claim.

## Authorization / Decision

The operator authorized roadmap authoring after requiring direct verification
of the recorded MAO reopen condition. The verified decision is
`ROADMAP_CANDIDATE_ALLOWED`. This authorizes the roadmap, independent external
critique, and internal critique classification only. It does not authorize a
GC-018 packet, work order, runtime implementation, or provider call.

## Scope / Target / Owner Boundary

Target: a provider-neutral orchestration foundation for bounded CVF tasks.

Roadmap owner: CVF provenance governance and architecture stewardship.

Future runtime owner: the CVF execution-plane foundation, behind existing
control-plane role/risk and approval decisions. The runtime owns orchestration
execution state; it does not own policy, approval authority, commits, or session
truth.

In scope for design and future tranche planning:

- dependency-aware task graph and terminal propagation;
- risk-based role admission;
- provider-neutral delegation adapter;
- reviewer context isolation and dissent;
- bounded revision and escalation;
- designated closer and commit/session interlocks;
- lifecycle recovery and deterministic receipts;
- cost, token, latency, and fan-out limits;
- one bounded representative proof;
- architecture-catalog admission and freshness ownership.

Out of scope in this roadmap session:

- orchestration implementation, production scheduling, or queue mutation;
- live provider calls or claims about live governance behavior;
- Web, UI, dashboard, package lifecycle, R91, ASC semantic, R84, R73F, L4,
  or public-sync changes;
- automatic agent spawning;
- GC-018 or work-order authoring.

## Non-Goals

This roadmap does not seek to maximize agent count, replace existing CVF
governance, reactivate archived artifacts, build an Agent OS, provide a
production orchestration platform, prove provider behavior, or claim that
multi-agent execution is better by default.

## Design Control Gate

Before MAO-T0 packet authoring, an independent external critique and an internal
source-verified finding classification must be accepted. Before any later
implementation tranche, its fresh GC-018/work order must prove dependency
release, active-owner reuse, non-duplication, exact new-field classification,
AHB/workspace control blocks where applicable, bounded cost, and a real changed
range through the applicable pre-dispatch and pre-implementation gates.

## Reopen-Condition Audit

| Condition | CVF-governed evidence | Verdict |
|---|---|---|
| MSEA-R94 must be terminal | `CVF_SESSION/state/entries/mseaR94SystemChainGapClosure20260711.json` records `CLOSED_PASS_BOUNDED`; `docs/roadmaps/CVF_MSEA_R94_SYSTEM_CHAIN_GAP_CLOSURE_ROADMAP_2026-07-11.md` has matching status; completion review is reviewer accepted | SATISFIED |
| R85-style automatic external-absorption intake trigger hardening must be accepted | `CVF_SESSION/state/entries/mseaR95ExternalRepositoryAbsorptionEntryHardeningClosure20260711.json` and `docs/reviews/CVF_MSEA_R95_EXTERNAL_REPOSITORY_ABSORPTION_ENTRY_HARDENING_COMPLETION_2026-07-11.md` record `REVIEWER_ACCEPTED_BOUNDED` | SATISFIED |
| MAO may become a roadmap candidate, not implementation-ready work | `CVF_SESSION/state/entries/multiAgentOrchestrationRuntimeFoundationParked20260711.json` orders roadmap consideration after the two conditions | SATISFIED_WITH_BOUNDARY |

Reopen verdict: `ROADMAP_CANDIDATE_ALLOWED`. Runtime implementation remains
parked until critique reconciliation and a fresh MAO-T0 GC-018/work order.

## Source Authority

Active authority, in descending task-specific order:

1. `AGENTS.md`, active session front doors, and active handoff for scope and
   current next-move control.
2. Agent Handoff Contract ratification and its machine-check standard.
3. Agent Workspace active standards, topology, lane taxonomy, generated-state
   discipline, and guards.
4. Current commit-steward, autorun, work-order, approval, and session-sync
   controls.
5. Current execution/control-plane source for verified existing symbols only.
6. Current architecture catalog and system-chain gap index for as-built
   placement and admission.

Archived MA1, W2-T9, and W2-T14 artifacts are evidence and design history only.
They cannot override active contracts. Provider-local memory and chat are not
CVF authority.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Four canonical role routes | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | CF-01, lines 102-112 | `route` | Agent Handoff Contract | ACCEPT |
| Phase-specific base heads and changed sets | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | CF-03 through CF-06, lines 141-233 | `dispatchBaseHead`, `executionBaseHead`, `closureBaseHead` | Agent Handoff Contract | ACCEPT |
| One closer for three-or-more-agent chains | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | C3, lines 392-440 | `commitOwner(CLOSURE)` | Agent Handoff Contract | ACCEPT |
| No-commit worker closure conversion | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | CF-07, lines 235-259 | `WORKER_MUST_NOT_COMMIT` | Agent Handoff Contract | ACCEPT |
| Workspace generated state is a projection over bounded state units | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | Topology Decision and Workspace State Units, lines 43-79 | `ACTIVE_AGENT_WORKSPACE_STATE.json` | workspace state topology | ACCEPT |
| Workspace item fields and lane transitions | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_LANE_TAXONOMY.md` | topology lines 81-150; taxonomy lines 34-97 | `workspaceItemId`, `lane`, `phase` | workspace item schema and taxonomy | ACCEPT |
| Generated workspace aggregate and checker already exist | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | Storage Topology, lines 120-150 | `generate_agent_workspace_state.py`, `check_agent_workspace_state.py` | generated workspace state | ACCEPT |
| Existing coordination result distributes runtime IDs and emits deterministic hashes | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/execution.multi.agent.coordination.contract.ts` | lines 6-30 and 92-165 | `MultiAgentCoordinationContract` | execution-plane coordination contract | ACCEPT |
| Existing cloud runtime has agent status, heartbeat message vocabulary, role/risk admission, and file locks | `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/cloud/multi.agent.runtime.ts` | lines 22-96 and 178-247 | `MultiAgentRuntime` | phase-governance runtime | ACCEPT |
| Archived MA1 packet has source packet, role assignment, output, dissent, integration, evidence, and claim sections | `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | sections 0-10 | archived packet section set | archived MA1 template | ACCEPT |
| Requested non-archive MA1 standard path is active | `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | path search | requested path | N/A | REJECT - corrected path is archive-qualified and evidence-only |
| W2-T9 provides task distribution and summary contracts | `docs/roadmaps/archive/CVF_W2_T9_EXECUTION_MULTI_AGENT_COORDINATION_EXECUTION_PLAN_2026-03-23.md` | CP1-CP3 | `MultiAgentCoordinationContract` | archived execution plan | ACCEPT |
| W2-T14 provides consumer and batch bridges | `docs/roadmaps/archive/CVF_W2_T14_MULTI_AGENT_COORDINATION_CONSUMER_BRIDGE_EXECUTION_PLAN_2026-03-24.md` | CP1-CP3 | `MultiAgentCoordinationConsumerPipelineContract` | archived execution plan | ACCEPT |
| Current ASC is generated from compact entries and has a governed admission route | `docs/reference/system_architecture_catalog/README.md` | Family Contents, lines 115-124; Governing Documents, lines 153-159 | `CVF_AS_BUILT_SYSTEM_CATALOG_AGGREGATE.json` | ASC generator family | ACCEPT |
| Current gap index is canonical for catalog gaps | `docs/reference/system_chain/gaps/README.md` | Canonical Source and Vocabulary | `CVF_SYSTEM_CHAIN_GAP_INDEX.json` | system-chain gap generator family | ACCEPT |

No runtime field introduced by this roadmap is claimed to exist. MAO-T0 owns
the new schema decisions and must record them as new fields rather than falsely
source-verifying them as existing source.

## Current Runtime Freshness Verification

| Field | Evidence |
|---|---|
| verifiedHead | `d2f54cc6a` |
| verifiedDate | 2026-07-11 |
| sourceSearch | `rg --files` located the active AHB/workspace sources, archived MA1/W2 plans, execution coordination contracts, phase-governance runtime, ASC aggregate, and gap index |
| runtimeSymbolCheck | direct reads verified `MultiAgentCoordinationContract` and `MultiAgentRuntime` at the cited source paths and line ranges |
| archiveBoundaryCheck | repo path search found the MA1 standard only under `docs/reference/archive/` |
| freshnessChecks | current system-chain freshness and ASC drift checks are required before the material roadmap commit |
| disposition | ACCEPT for this roadmap inventory only; new MAO runtime fields remain T0 design work and are not claimed as present source |

## Existing-Owner And Overlap Matrix

| Concern | Existing owner | Current strength | MAO decision |
|---|---|---|---|
| Role route, phase, commit owner, closer | Agent Handoff Contract | active and machine-enforced | REUSE unchanged |
| Work authority and bounded source packet | GC-018/work order plus archived MA1 semantics | active dispatch controls; MA1 archived | ADAPT MA1 section intent into active work-order contract; do not reactivate archive by implication |
| Workspace lanes and compact status view | agent workspace generated state | active foundation, explicitly not runtime queue | REUSE as read projection only |
| Task distribution | W2-T9 coordination contract | deterministic but shallow; no dependency graph or authority envelope | ADAPT algorithmic/hash patterns; reject as complete MAO runtime |
| Consumer bridge | W2-T14 | summary/pipeline bridge only | REUSE only if T0 proves a compatible observer boundary |
| Agent registration and role/risk checks | phase-governance `MultiAgentRuntime` | useful vocabulary and guards; isolated historical implementation | ADAPT verified invariants; no wholesale promotion |
| Provider selection | existing provider router and adapter surfaces | provider routing exists outside orchestration ownership | REUSE behind a new capability adapter; resolver never chooses policy |
| Worker return and review | worker-return scaffold/quality gates and completion review | active governed surfaces | REUSE |
| Commit and continuity | commit steward, AHB, active session generated state | active and enforced | REUSE; runtime cannot bypass |
| Observability/evidence | current AOT, receipts, completion evidence | phase-oriented, not invocation-graph complete | EXTEND through MAO receipts in future tranches |
| Architecture visibility | ASC compact source/generator and gap ledger | active | EXTEND only after implementation proof |

## Reuse / Reject / Adapt Decisions

- REUSE AHB route, phase, base-head, changed-set, trace, commit-owner,
  cross-batch-isolation, and next-move semantics exactly.
- REUSE workspace lanes as operator-facing projection, not execution authority.
- REUSE the work order as the authority envelope and the completion review as
  closure evidence.
- ADAPT W2-T9 deterministic IDs and distribution evidence into task-graph and
  invocation receipts only after MAO-T0 compatibility analysis.
- ADAPT the historical runtime's role/risk, TTL, heartbeat, conflict, and lock
  ideas only where current source and active policy agree.
- ADAPT archived MA1 source-packet, dissent, output, and integration semantics
  into an active schema owned by T0.
- REJECT provider names as schema values or orchestration branches.
- REJECT agent count as a quality proxy, unrestricted broadcast, implicit
  self-review, worker conclusions as reviewer authority, unlimited revisions,
  and automatic commits.
- REJECT a second governance/state truth beside work orders, AHB, workspace
  source fragments, and session state.

## Architecture Decision Table

| Decision | Selected design | Owner / reason |
|---|---|---|
| Orchestration state owner | execution-plane MAO runtime module | Runtime lifecycle belongs in execution; policy remains control-plane owned |
| Persistence shape | append-only event/receipt ledger as execution truth plus deterministic generated read models | Events preserve attempts, dissent, retries, and recovery; generated views support operators without becoming authority |
| Task graph source of truth | accepted work-order authority envelope compiled into a versioned immutable task-graph definition; runtime events may advance state but not rewrite authority | Prevents chat/provider output from expanding scope |
| Workspace relationship | projection of lifecycle milestones into existing lanes; no per-heartbeat mirroring and no workspace-as-queue | Preserves workspace boundary and limits churn |
| AHB relationship | AHB controls routes, phases, actor scopes, closer, commit, and session sync; MAO only executes within that envelope | No parallel handoff governance |
| Role resolver ownership | control-plane policy component returning an admission decision and reason receipt | Risk and approval are policy, not provider concerns |
| Runtime adapter boundary | execution-plane provider-neutral invocation port consuming a capability declaration and explicit authority envelope | No Claude/Codex hardcoding |
| Retry semantics | retry only retryable invocation failures with the same authority hash and idempotency key; policy/approval/review failures create repair or escalation, not blind retry | Prevents duplicate side effects and quota waste |
| Cancel semantics | cooperative cancel request followed by terminal cancellation receipt; no new child may start after cancel acceptance; non-cooperative calls become timed-out/orphan candidates | Produces auditability without claiming impossible immediate termination |
| Human checkpoints | required before admitting high-risk fan-out, expanding scope/budget, overriding reviewer dissent, accepting partial results, or authorizing commit/public action | Keeps consequential authority human/CVF governed |
| No-auto-commit boundary | adapters, workers, specialists, and resolver cannot commit; only the AHB-designated closer may invoke commit steward after independent acceptance | Exact closure authority |
| Public/private projection | provenance-only through pilot and closure; any later public export needs a separate public-safe projection packet | No private evidence leakage |
| Freshness ownership | MAO schema/receipt checker owners plus ASC generator/checker after catalog admission; workspace generator owns workspace projection drift | Clear per-surface ownership |
| Catalog admission | only after implemented source, deterministic invocation evidence, tests, operator/evidence route, and proof-classed edges exist | No roadmap-only layer/module promotion |

## Task / Role / State Lifecycle

Planned logical lifecycle (schema names are design vocabulary for MAO-T0, not
claims about current runtime fields):

1. An accepted work order fixes the authority envelope, route, risk inputs,
   budget, files, dependencies, closer, and approval checkpoints.
2. The compiler creates an immutable task graph and authority hash.
3. The role resolver returns either single-worker admission, a bounded role
   plan, operator approval required, or rejection.
4. The runtime transitions dependency-ready tasks from planned to admitted to
   running. A parent cannot complete before all required children are terminal.
5. Failed or blocked dependencies propagate a blocked state to descendants;
   independent siblings may continue only when the graph explicitly permits it.
6. Every invocation records identity, role, authority hash, input manifest,
   idempotency key, budget allocation, timestamps, and outcome.
7. Reviewer tasks receive a source packet independent of worker conclusions.
   Worker output is evidence under review, never reviewer authority.
8. A reviewer accepts, requests a classified repair, records dissent, or
   escalates. Repair loops are bounded by the work-order revision limit.
9. Exactly one designated closer reconciles accepted outputs, dissent, changed
   set, and approval evidence. Only that closer may perform closure conversion.
10. Commit steward verifies the closure boundary. Session-sync remains a
    separate commit and updates the active continuity surfaces.

Required terminal task outcomes to be finalized in T0: success, rejected,
blocked, cancelled, timed out, exhausted, and failed. T0 must map each outcome
to descendant propagation, retry eligibility, operator action, and receipt
requirements before T1 dispatch.

## Risk-Based Role Model

| Conditions | Default route | Required evidence |
|---|---|---|
| Low risk, narrow reversible scope, deterministic checks, no independence claim | one worker; single-agent route | admission receipt explaining why review separation adds insufficient value |
| Medium risk, governed artifact or non-trivial integration, repair remains reversible | worker plus independent reviewer | separate source packet and reviewer decision |
| High risk, security/privacy/domain consequence, or irreversible external effect | worker, independent specialist, reviewer, designated closer, plus human checkpoint | specialist qualification/capability, dissent ledger, explicit approval |
| Context leakage would defeat independence | reject multi-agent plan or create an isolated reviewer packet | isolation decision and excluded-context manifest |
| Fan-out cost exceeds evidence value, task cannot be safely decomposed, or actors would edit overlapping scope | single worker or operator escalation | cost/context-risk rejection receipt |

Multi-agent admission requires all of: decomposable scopes, non-overlapping or
explicitly serialized writes, measurable evidence value, a bounded budget,
one closer, and a source packet for every role. Failure of any condition blocks
fan-out.

## Cost / Token / Latency Controls

- Default fan-out is 1; initial pilot maximum is 3 concurrent execution roles
  excluding the closer.
- Initial maximum revision depth is 1 worker repair cycle. A second repair
  requires operator approval; a third is forbidden in the pilot.
- Every work order must set total invocation count, token/cost ceiling when the
  provider exposes it, wall-clock ceiling, and per-role allocation.
- Budget exhaustion stops new invocations, requests cancellation of safe
  in-flight work, records partial evidence, and escalates. It never silently
  degrades reviewer independence.
- Additional-agent admission must name the defect/risk/evidence question that
  the actor resolves and the expected benefit over a single worker.
- Provider adapters must return usage and latency when available and explicitly
  record unavailable measurements. Estimated and provider-reported usage must
  not be mixed without labels.

## Runtime Lifecycle Controls

- Timeout is task-specific and produces a terminal attempt receipt; retry uses
  a new attempt identity under the same task and authority hash.
- Heartbeat proves liveness only. It cannot renew authority, extend budget, or
  imply useful progress.
- Cancellation is idempotent and blocks further child admission after accepted.
- Idempotency keys bind task, attempt policy, authority hash, role, and input
  manifest. Duplicate invocation returns the existing receipt or a conflict;
  it does not execute twice.
- Orphan recovery scans non-terminal attempts without valid liveness evidence,
  classifies them, and either resumes from durable evidence, safely retries, or
  escalates. It never infers success from silence.
- Retryable classes are transport interruption, provider-declared transient
  failure, and safe timeout with no side-effect ambiguity. Authority rejection,
  approval denial, invalid output, scope breach, and ambiguous side effects are
  not automatic retries.

## Evidence And Receipt Model

Future MAO schemas must cover:

- graph receipt: graph identity, work-order identity, authority hash,
  dependency manifest, and compiler version;
- role-resolution receipt: inputs, selected route/roles, exclusions, risk
  reason, cost justification, and approval requirement;
- invocation receipt: provider-neutral invocation identity, adapter identity,
  role, capability, authority hash, input manifest hash, idempotency key,
  timing, usage, and diagnostic classification;
- output receipt: output manifest, changed-set evidence, validation result, and
  claim boundary;
- review receipt: isolated source packet hash, recomputed evidence, defects,
  dissent, decision, and repair owner;
- integration receipt: designated closer, accepted outputs, rejected outputs,
  unresolved dissent, final changed set, commit-steward result, and session-sync
  requirement.

Raw prompts, secrets, provider-private memory, and unrestricted model traces are
not required receipt content. Evidence must be secret-safe and reconstructable
from governed sources.

## Work Plan And Dependencies

### MAO-T0 - Source Inventory, Overlap, Decisions, And Schemas

Dependency: this roadmap must pass external critique and internal critique
classification first.

Deliverables: fresh GC-018/work order; definitive source inventory; compatibility
analysis; active MAO contract front door; task graph, event, receipt, capability,
authority-envelope, and read-model schemas; lifecycle/state transition table;
storage/retention decision; threat and failure model.

Acceptance: every new field is classified as new; all overlap has reuse/reject/
adapt disposition; retry/cancel/approval/no-commit semantics are machine-testable;
no runtime implementation.

### MAO-T1 - Task Graph And State Contract

Dependency: T0 accepted.

Deliverables: deterministic graph compiler/validator, dependency and parent-child
evidence, terminal/blocked propagation, immutable authority binding, event ledger,
generated read model, focused unit and corruption tests.

### MAO-T2 - Risk-Based Role Resolver

Dependency: T1 contract accepted.

Deliverables: control-plane resolver with single-worker default, specialist and
reviewer admission logic, human checkpoint result, rejection reasons, and budget
plan. No provider invocation.

### MAO-T3 - Provider-Neutral Delegation Adapter

Dependency: T1 and T2 accepted.

Deliverables: capability contract, invocation identity, authority-envelope
enforcement, idempotency boundary, diagnostic envelope, and fake/local adapter
contract tests. Named providers are integration configurations, not schema forks.

### MAO-T4 - Reviewer Isolation, Dissent, And Revision Loop

Dependency: T1-T3 accepted.

Deliverables: isolated reviewer packet builder, excluded-context manifest,
evidence recomputation contract, self-approval guard, dissent ledger, defect
classes, repair ownership, revision counter, stop/escalation controls.

### MAO-T5 - Designated Closer And Commit/Session Interlock

Dependency: T4 accepted.

Deliverables: exactly-one-closer invariant, integration decision, closure
conversion, commit-steward interlock, no-auto-commit guard, and separate
session-sync projection. No adapter receives commit authority.

### MAO-T6 - Timeout, Heartbeat, Cancel, Retry, And Recovery

Dependency: T3-T5 accepted.

Deliverables: lifecycle controller, duplicate protection, retry classifier,
cooperative cancel, orphan detector/recovery policy, deterministic clock tests,
and failure diagnostics.

### MAO-T7 - Evidence, Observability, And Operator Readout

Dependency: T1-T6 accepted.

Deliverables: receipt ledger, secret-safe operator read model, workspace milestone
projection, freshness/drift checks, retention limits, and catalog admission
candidate packet. No UI implementation.

### MAO-T8 - Representative End-To-End Pilot

Dependency: T1-T7 accepted and a fresh pilot packet selects a real bounded task.

Deliverables: one worker to independent reviewer to one classified revision to
designated closer proof; negative self-approval, duplicate, timeout, cancel, and
budget tests; command-backed receipts. Use a real provider only if the pilot
claims provider/runtime governance behavior, in which case the mandatory live
governance bundle and diagnostics apply.

### MAO-T9 - Independent Critique, Reconciliation, And Closure

Dependency: T8 evidence complete.

Deliverables: independent critique, source-backed classification of every
finding, repairs or explicit rejection reasons, closure diff gate, public export
decision, ASC/gap admission disposition, and separate session sync.

## Dependency Chain

`external roadmap critique -> internal classification -> MAO-T0 -> MAO-T1 ->
MAO-T2 -> MAO-T3 -> MAO-T4 -> MAO-T5 -> MAO-T6 -> MAO-T7 -> MAO-T8 -> MAO-T9`

T2 may begin detailed design alongside late T1 review, but cannot dispatch
implementation before T1 acceptance. T5 cannot precede T4 because closer
semantics consume reviewer/dissent output. T7 cannot become authoritative until
all lifecycle producers have stable receipts.

## Acceptance Criteria

- Single-worker execution remains the default and has an explicit admission
  reason.
- Every multi-agent run binds to one governed authority envelope and immutable
  graph definition.
- Reviewer authority derives from an independent source packet and recomputed
  evidence, not worker conclusions.
- Exactly one closer owns integration and closure; no execution adapter can
  commit.
- Every task and attempt ends terminally or has named recovery action.
- Retry, cancellation, timeout, duplicate, orphan, and blocked propagation are
  deterministic and negatively tested.
- Fan-out and revisions stay inside declared budget and approval thresholds.
- Receipts reconstruct role assignment, inputs, outputs, review, dissent,
  integration, and session-sync need without secrets.
- Workspace state remains a generated milestone projection, not runtime truth.
- Existing AHB, work-order, approval, commit-steward, and session-sync guards are
  reused rather than duplicated.
- ASC admission occurs only after proof-backed implementation and generator
  validation.

## Verification / Evidence Plan

Each implementation tranche must include focused unit tests, schema validation,
negative fixtures, `git diff --check`, relevant generated-state drift checks,
governed file-size enforcement, applicable autorun phase gate with a real base
range, commit-steward preflight, and pre-commit validation.

T8 uses one representative task rather than an exhaustive sweep. Minimum proof
sequence: admitted graph; worker output; independent reviewer rejection or
repair request; one repaired output; closer integration; commit-steward result;
session-sync requirement. Negative evidence covers unauthorized fan-out,
self-approval, stale authority hash, duplicate invocation, overlapping write
scope, non-retryable failure, budget exhaustion, cancellation, and orphan
classification.

## Negative And Fail Conditions

The roadmap or a future tranche fails if it:

- promotes archived MA1/W2 artifacts as active authority without ratification;
- introduces guessed existing fields or source paths;
- hardcodes a provider or assumes provider capability from brand identity;
- allows worker output to become reviewer authority;
- permits more than one closer, self-approval, implicit commit, or combined
  material/session-sync commit;
- treats workspace generated state as the runtime queue or event source;
- retries approval, policy, scope, validation, or ambiguous-side-effect failures
  automatically;
- leaves non-terminal tasks without timeout/recovery responsibility;
- admits fan-out without cost/evidence justification;
- claims provider/runtime governance from mock evidence;
- changes public-sync, UI, packages, R91/ASC semantics, L4, R84, or R73F;
- dispatches T0 before critique reconciliation and a fresh governed packet.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Owning tranche | Required work-order evidence |
|---|---|---|
| Schemas, source truth, storage, overlap | T0 | source verification, new-field table, decision records |
| Task graph and propagation | T1 | transition matrix, deterministic tests, corruption fixtures |
| Role/risk admission and budgets | T2 | risk cases, rejection reasons, approval thresholds |
| Provider-neutral invocation | T3 | capability and authority envelope, adapter contract tests |
| Independent review and revision | T4 | isolation manifest, self-approval negatives, dissent/repair receipts |
| One closer and commit boundary | T5 | AHB control block, closer invariant, commit/session separation |
| Runtime lifecycle recovery | T6 | retry/cancel/idempotency/orphan state table and fault tests |
| Receipts/readout/freshness | T7 | event-to-read-model proof, drift and secret-safety checks |
| Bounded representative proof | T8 | real task packet, full receipt chain, negative proof |
| Critique and closure | T9 | finding classification, closure diff, catalog/public disposition |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Memory class:`; `Status:`; `Authorization / Decision`; `Non-Goals`; `Design Control Gate`; `Source Verification Block`; `Roadmap-To-Work-Order Trace Matrix`; `Public Export Disposition`; `Machine Closure Package`; `PROPOSED` |
| gateRunPurpose | confirmation and evidence after source-backed roadmap authoring; not first discovery; no implementation or closure claim |
| claimBoundary | roadmap and critique sequencing only; no dispatch, runtime, provider, public, or production claim |

## Independent External Critique Gate

Before MAO-T0 packet authoring, send this roadmap to Claude or another external
reviewer with the roadmap and cited CVF source packet. The reviewer has no
implementation authority. An internal reviewer must source-verify and classify
every finding as accepted, calibrated, rejected with evidence, or blocked by
missing source. Only an accepted reconciliation artifact may release T0.

## Parked / Rejected Scope

- Production scheduler, durable distributed queue, horizontal scale, hosted
  tenancy, and an "Agent OS" claim are value-parked. Reopen only after T8 proves
  bounded local orchestration value and a new roadmap names a measurable need.
- More than three concurrent execution roles is parked until at least three
  representative tasks show that bounded fan-out leaves material independent
  evidence value after cost and latency.
- More than one automatic revision is parked; reopen only when two accepted
  pilots fail solely because one bounded repair was insufficient and operator
  review supports the added cost.
- Public MAO projection is parked until T9 has a secret-safe artifact inventory
  and an explicit public-sync packet.
- UI/operator dashboard remains separately authorized work after a stable T7
  read model exists.
- L4 promotion, T3B, R73F retirement, and R84 effectiveness remain under their
  existing conditions and are not absorbed into MAO.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap is provenance-only architecture planning and includes
private system/source mapping. A later T9 decision must identify a bounded
public-safe projection and use the sibling public-sync clone through a separate
authorized packet.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: T0 packet is forbidden before critique reconciliation | roadmap remains PROPOSED | N/A with reason |
| Completion or reviewer artifact | N/A with reason: external critique has not started | next allowed move names critique | N/A with reason |
| Roadmap state | this roadmap | PROPOSED | N/A with reason |
| Registry JSON | N/A with reason: no registry change authorized | no registry path changed | N/A with reason |
| Registry Markdown | N/A with reason: no registry change authorized | no registry path changed | N/A with reason |
| External evidence digest | N/A with reason: critique is the next move | no external evidence claimed | N/A with reason |
| System loop interlock | current R91 and ASC freshness surfaces | unchanged and checked separately | N/A with reason |
| Session continuity | active front doors | separate protected sync follows material roadmap commit | N/A with reason |

## Epistemic Process Block

### Expected Result / Prediction

Existing CVF contracts would cover governance boundaries but not a complete
runtime graph, independent-review execution chain, recovery model, or receipt
ledger.

### Evidence Comparison

The inventory confirmed strong active owners for handoff, workspace projection,
worker return, commit, and session sync. It also found deterministic but partial
W2-T9/W2-T14 coordination and a separate historical multi-agent runtime. The
requested MA1 standard is archive-qualified, which prevents treating it as
active authority.

### Contradiction Or Gap Disposition

No contradiction requires a parallel governance layer. Missing runtime graph,
adapter, isolation, revision, lifecycle, and receipt semantics become bounded
T0-T7 design/implementation work. Historical overlaps receive explicit adapt or
reject decisions.

### Claim Update

MAO is eligible for roadmap and external critique only. It is not implementation
ready, provider proven, public ready, or a production orchestration platform.

## Next Allowed Move

Send this roadmap to an independent external reviewer. Then perform an internal
source-verified classification of every critique. If and only if that
reconciliation is accepted, author a fresh MAO-T0 GC-018 and source-verified work
order. Stop before implementation.

## Claim Boundary

This artifact defines a provenance-only roadmap. It claims that MAO reopen
conditions are satisfied for roadmap consideration and records source-backed
architecture decisions and tranche dependencies. It does not claim runtime
implementation, live provider behavior, automatic delegation, production queue
or scheduler capability, UI, public export, package lifecycle change, R91/ASC
semantic change, L4 promotion, R84 effectiveness, R73F retirement, or
production readiness.
