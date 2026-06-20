# CVF LSC-T0 Learning Signal Chain Reconciliation Roadmap

Memory class: FULL_RECORD

Status: LSC_T1_DISPATCH_READY

docType: roadmap

Date: 2026-06-20

## Purpose

Define a unified Learning Signal Chain for CVF so AAF worker-experience
findings, reviewer/orchestrator/operator friction, external-agent critique,
Finding-To-Governance disposition, RT2/RT3 readouts, and the MLW Learning Plane
contracts become one system chain instead of separate local mechanisms.

This roadmap is a rebuttal packet for review. It does not dispatch
implementation, create runtime behavior, or replace existing Learning Plane
contracts.

## Authorization/Decision

Decision: RECONCILE_BEFORE_IMPLEMENTING

AAF-T5 is not an isolated guard. It is the first capture sensor in a larger
Learning Signal Chain. The correct chain is:

`OBSERVED -> CAPTURED -> NORMALIZED -> TRIAGED -> OWNER_MAPPED -> LEARNING_PROPOSAL -> EVALUATED -> GOVERNANCE_DECISION -> WORK_ORDER_OR_CONTROL -> CLOSED_OR_DEFERRED`

The governing principle is:

`Fast capture, slow promotion.`

Capture must be cheap enough for internal agents and external CLI/MCP agents to
emit without blocking work. Promotion must remain governed, reviewed, and
operator-controlled.

Rebuttal incorporation: Claude's LSC-T0 rebuttal correctly identified a
parallel-core risk. LSC must extend the existing Learning Signal Intake Bridge
record surface instead of defining a second learning signal record.

Authorization status: draft for Claude rebuttal only. Operator has authorized
roadmap drafting for critique; no GC-018 or implementation work order is opened
by this artifact.

## Scope

In scope:

- reconcile AAF-T5 worker-experience capture with existing CVF Learning Plane
  and finding-to-governance surfaces;
- define a system-chain roadmap for worker, reviewer, orchestrator, operator,
  external-agent, runtime, provider, cost, and public-surface learning signals;
- preserve parked work as future candidates rather than deleting it;
- define external-agent CLI/MCP readiness requirements at contract level;
- define latency and promotion boundaries for future work orders.

Out of scope for this roadmap:

- implementing a ledger, checker, helper, CLI, MCP, runtime route, or adapter;
- changing current runtime/provider behavior;
- claiming Learning Plane runtime mutation or readiness;
- public-sync or public catalog claims.

## Non-Goals

- No autonomous memory, policy, prompt, model, provider, or truth mutation.
- No direct IDE, shell, git, filesystem, provider, or MCP interception.
- No queue, daemon, watcher, scheduler, or background service.
- No runtime provider routing, provider/live proof, or public-sync.
- No replacement of RT2, RT3, MLW3, MLW5, MLW6, or existing
  Finding-To-Governance standards.
- No abandonment of AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7, or MLW8.

## Non-Abandonment Rule

Parked work is not rejected work. The following lanes remain active candidates
and must not be erased by this roadmap:

| Parked lane | Current disposition | How LSC treats it |
|---|---|---|
| AAF-T6 Guard Orientation Read-Receipt Gate | parked after AAF-T5 closure | captured as a future read-receipt/control-plane signal tranche |
| AAF-T7 helper/index friction hardening | parked after AAF-T5 closure | becomes a downstream helper/readout tranche inside LSC, not a standalone island |
| CGE-T3 Full Knowledge Absorption Ledger | parked by operator checkpoint | may feed LSC as external-knowledge and absorption-signal input |
| ACE-R1 Agent Coding Evidence Replay Roadmap | parked by operator checkpoint | may feed LSC as coding-evidence replay signal input |
| MLW7/MLW8 optional Learning Plane follow-ups | parked by MLW roadmap | remain separate operator-authorized work, not silently reopened |
| Runtime/provider/live/public-sync/CLI/MCP implementation | parked unless separately authorized | LSC-T0 may define contracts only; implementation requires fresh GC-018 |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| AAF-T5 captures worker friction through worker-return tokens | `docs/reference/worker_experience_retrospective/README.md` | lines 16, 54, 64 | `WORKER_EXPERIENCE_RETRO`; `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` | worker-experience retrospective standard | ACCEPT |
| AAF-T5 does not replace AAF-T6 read receipt | `docs/reference/worker_experience_retrospective/README.md` | lines 98, 103 | claim boundary; AAF-T6 lane | worker-experience retrospective standard | ACCEPT |
| Findings must be dispositioned and routed to learning lanes | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | lines 8, 44 | `Finding-To-Governance Learning Disposition` | finding-to-governance standard | ACCEPT |
| Runtime/provider/cost learning candidates must normalize through Learning Signal Intake before Learning Plane route claims | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | line 31 | Learning Signal Intake Bridge | finding-to-governance standard | ACCEPT |
| RT2 provides finding-to-learning bridge, advisory only | `docs/reviews/CVF_RT2_FINDING_TO_LEARNING_SIGNAL_BRIDGE_COMPLETION_2026-05-31.md` | lines 15, 110, 127 | `buildFindingToLearningRecord` | RT2 bridge | ACCEPT |
| RT3 provides Learning Plane readout route, advisory only | `docs/reviews/CVF_RT3_LEARNING_PLANE_READOUT_ROUTE_COMPLETION_2026-05-31.md` | lines 15, 96 | `/api/learning-plane/readout` | RT3 readout route | ACCEPT |
| MLW3 defines evidence-to-truth signal routing and proposal-only boundary | `docs/reference/CVF_MLW3_EVIDENCE_TO_TRUTH_LEARNING_SIGNAL_PIPELINE_2026-06-05.md` | lines 13, 68, 88, 104 | `signalId`; Learning Signal Intake Bridge | MLW3 contract | ACCEPT |
| Learning Signal Intake Bridge already owns lane, severity, disposition, and autonomous mutation invariant | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | lines 35-65, 123-170 | `LearningSignalIntakeInput`; `LearningSignalIntakeRecord`; `autonomousMutationAuthorized` | LPF intake bridge | ACCEPT |
| MLW roadmap already defines MLW3/MLW5/MLW6 dependency order | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | lines 98, 146-149 | MLW3; MLW5; MLW6 | MLW roadmap | ACCEPT |
| AAF-T5 is closed and next move is operator checkpoint | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | lines 2709-2710 | `aafT5WorkerExperienceRetrospectiveCaptureClosure20260620`; `nextAllowedMove` | active session state | ACCEPT |
| Claude rebuttal identifies parallel-core risk and recommends extending the existing intake record | `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_2026-06-20.md` | B1 and Roadmap Tranche Corrections | `LearningSignalIntakeRecord` extension | advisory rebuttal | ACCEPT |
| Round-2 rebuttal approves LSC-T1 with N4/N5 refinements | `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_ROUND2_2026-06-20.md` | lines 86, 129-145, 199-204 | exact severity mapping; `captureState` derived from `disposition` | advisory rebuttal round 2 | ACCEPT |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | returned output to finding classification to governed roadmap correction |
| Owner surface | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` |
| Disposition | ADAPT as CVF-owned roadmap correction after Codex classification |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Claim boundary | external rebuttal is input only; this roadmap remains the CVF-owned planning surface |

## Current Chain Pieces

| Piece | Current owner | Current role | Gap if left standalone |
|---|---|---|---|
| AAF-T5 worker-experience retrospective | governance helper/checker | capture worker-return friction | captures only one actor class |
| Finding-To-Governance trigger | governance control chain | forces disposition for findings | does not itself store all signal lifecycle states |
| RT2 finding-to-learning bridge | cvf-web advisory bridge | maps findings to learning readout records | advisory, not universal intake |
| RT3 Learning Plane readout route | cvf-web advisory HTTP route | exposes readout without mutation | route exists, but not the whole system chain |
| MLW3 evidence-to-truth signal pipeline | Learning Plane contract | normalizes evidence into proposal candidates | expects governed receipts and source-backed inputs |
| MLW5 audit feedback validation | Learning Plane contract | validates audit/trust feedback | not yet wired to everyday agent friction |
| MLW6 simulation/failure gate | Learning Plane contract | gates high-risk learning updates | not triggered by low-level capture yet |

## Unified Learning Signal Classes

| Signal class | Examples | Default lane | Initial capture surface |
|---|---|---|---|
| WORKER_FRICTION | gate surprise, keyword trap, helper gap, latency | GOVERNANCE_CONTROL_PLANE | AAF-T5 worker-return token |
| REVIEWER_FRICTION | closure package surprise, committed-range finality, reviewer correction | GOVERNANCE_CONTROL_PLANE | future reviewer retro token |
| ORCHESTRATOR_FRICTION | dispatch ambiguity, source verification drift, stale next move | GOVERNANCE_CONTROL_PLANE | future orchestrator/session-sync retro token |
| OPERATOR_CORRECTION | operator finds system blind spot or wrong priority | GOVERNANCE_CONTROL_PLANE | operator finding packet or active checkpoint |
| EXTERNAL_AGENT_CRITIQUE | critique from CLI/MCP-connected external agent | GOVERNANCE_CONTROL_PLANE or DOCUMENTATION_ONLY_LEARNING | external review absorption packet |
| EXTERNAL_REPO_SIGNAL | useful external repo pattern | GOVERNANCE_CONTROL_PLANE or RUNTIME_BEHAVIOR_LEARNING | external knowledge chain map and CGE ledger |
| RUNTIME_SIGNAL | runtime receipt, execution evidence, audit feedback | RUNTIME_BEHAVIOR_LEARNING | MLW3/RT readout and governed receipts |
| PROVIDER_OUTPUT_SIGNAL | model/provider output quality, cost, refusal, latency | PROVIDER_OUTPUT_LEARNING or COST_ECONOMICS_LEARNING | future provider/cost signal packet |
| PUBLIC_SURFACE_SIGNAL | public catalog drift, external evaluator confusion | DOCUMENTATION_ONLY_LEARNING or GOVERNANCE_CONTROL_PLANE | public-sync review packet |

## Minimal Signal Event Contract

This is a doc-only planning contract for review, not an implementation.

Correction after rebuttal: this is not a new parallel learning record. LSC-T1
must define a capture adapter and ledger source that extends or maps into
`LearningSignalIntakeInput` / `LearningSignalIntakeRecord`. Existing intake
fields remain owned by the LPF intake bridge; LSC adds only the missing
operational capture fields needed for multi-role, CLI/MCP, and de-dup.

Existing intake-owned fields that LSC must reuse:

| Field | Existing owner | LSC rule |
|---|---|---|
| `sourceId` / `sourceArtifact` / `sourceSummary` | `LearningSignalIntakeInput` | reuse; do not rename into a parallel identity model |
| `lane` | `LearningSignalIntakeInput` | reuse existing lane enum |
| `defectClass` | `LearningSignalIntakeInput` | reuse existing defect-class enum unless a future source-verified extension is needed |
| `severity` | `LearningSignalIntakeInput` | reuse existing `critical/high/medium/low` enum; map AAF `BLOCKING/HIGH/MEDIUM/LOW/NONE` into it |
| `disposition` | `LearningSignalIntakeInput` | reuse Finding-To-Governance disposition values |
| `nextControlAction` | `LearningSignalIntakeInput` | reuse for promotion action |
| `evidenceBasis` | `LearningSignalIntakeInput` | reuse for source/receipt basis |
| `autonomousMutationAuthorized` | `LearningSignalIntakeRecord` | must remain `false` |

LSC extension fields:

| Field | Meaning | Latency note |
|---|---|---|
| `signalClass` | one of the unified signal classes | required |
| `actorRole` | worker, reviewer, orchestrator, operator, external-agent, runtime, provider, public-surface | role-neutral |
| `rootCauseGroupId` | de-dup key for one lesson across capture/disposition/proposal projections | helper may synthesize, but LSC-T1 must define deterministic rules |
| `repeatRisk` | NONE, POSSIBLE, LIKELY, OBSERVED_REPEATED | default POSSIBLE for CLI/MCP fast capture |
| `captureState` | CAPTURED, TRIAGED, PARKED, PROMOTED, CLOSED | operational lifecycle only; must map to existing disposition values |
| `sourceProjection` | AAF_T5_TOKEN, FINDING_TO_GOVERNANCE_ROW, MLW3_CANDIDATE, CLI_MCP_EVENT, OTHER | prevents double-counting |

Optional expanded fields:

- evidence receipt refs;
- related signals;
- proposed owner surface;
- proposed checker/helper/template target;
- operator checkpoint required;
- cost/runtime/provider metadata.

Minimal CLI/MCP capture payload should be only:

`signalClass`, `actorRole`, `sourceSummary`, `severity`, and `lane`.

Helper or ledger normalization may synthesize `sourceId`, `observedAt`,
`repeatRisk=POSSIBLE`, `captureState=CAPTURED`,
`autonomousMutationAuthorized=false`, and a pending `rootCauseGroupId`. This is
the latency-preserving path for external agents.

## Latency Budget

| Stage | Budget principle | Required behavior |
|---|---|---|
| Capture | cheap and local | one short token/block or one CLI/MCP event |
| Normalization | helper assisted | helper can fill stable defaults and flag missing required fields |
| Triage | batched where possible | do not block every return on deep analysis |
| Promotion | governed and slower | fresh GC-018/work order/checker only when signal justifies it |
| Closure | evidence-backed | no claim of learning completion without artifact and gate evidence |

The system must not force every agent return into a long retrospective. It must
capture enough to prevent loss, then promote only high-value or repeated signals.

Blocking rule for future implementation: unresolved signals should block
closure only when `severity=critical` or `repeatRisk=OBSERVED_REPEATED`.
Lower-severity unresolved signals should appear in helper/readout output, not
block routine closure, unless a work order explicitly tightens the rule.

## External Agent CLI/MCP Readiness Boundary

External agents will not always share Codex or Claude chat context. Therefore
LSC must define portable contracts:

| Surface | Requirement | Boundary |
|---|---|---|
| CLI return packet | can carry a minimal signal event or exact no-signal assertion | no direct execution authority |
| MCP return packet | can carry structured signal event fields | no provider/live claim unless separately proven |
| signal readout | agent can ask for unresolved signals relevant to its task | advisory only until governance promotion |
| promotion recommendation | helper may recommend next action | operator/governance decides |
| public-safe export | public signal summary requires public-sync authorization | provenance remains private source of truth |

T0 must not build CLI/MCP runtime behavior. It defines the source-verified
contract so a future implementation can be agent-neutral.

## Design Control Gate

Future work must pass this gate before dispatch:

| Gate item | Required disposition |
|---|---|
| Existing-chain mapping | cite AAF-T5, Finding-To-Governance, RT2/RT3, MLW3, and relevant MLW roadmap rows |
| Parked-lane preservation | name AAF-T6, AAF-T7, CGE-T3, ACE-R1, and any MLW optional lane affected |
| Latency budget | state capture-fast and promotion-slow behavior |
| External-agent portability | state CLI/MCP-facing packet or event contract boundary |
| Existing intake extension | prove the contract extends `LearningSignalIntakeRecord` instead of creating a parallel record |
| De-dup/root-cause | state how AAF-T5 token, Finding-To-Governance row, and MLW3 candidate share one signal id/root cause |
| Mutation boundary | keep `autonomousMutationAuthorized=false` unless separately authorized |
| Source authority | cite current CVF owner surfaces instead of chat or provider memory |
| Runtime boundary | mark runtime/provider/live/public-sync/direct-interception scope out unless fresh GC-018 releases it |

## Work Plan

| Tranche | Name | Objective | Exit criteria | Depends on |
|---|---|---|---|---|
| LSC-T0 | Learning Signal Chain Reconciliation | map AAF-T5, Finding-To-Governance, RT2/RT3, MLW3/MLW5/MLW6, external agents, and parked lanes into one chain | accepted roadmap and rebuttal resolution; no runtime implementation | current roadmap |
| LSC-T1 | Signal Ledger Source Layout And De-Dup Contract | define durable governed source layout for signal entries and unresolved signal state; bind to `LearningSignalIntakeRecord`; define root-cause grouping and projection de-dup | reference contract, schema/template, generated aggregate decision, deterministic AAF-T5-to-signal mapping, rootCauseGroupId rules | LSC-T0 |
| LSC-T2 | Multi-Role Capture Contract | extend capture beyond workers to reviewer, orchestrator, operator, and external-agent returns | role-neutral shared contract with separate eligibility per role to avoid false positives | LSC-T1 |
| LSC-T3 | Fast Helper Readout | make helper surface unresolved relevant signals and next suggested action without deep gate cost | read-only helper diagnostic and focused tests | LSC-T1/T2 |
| LSC-T4 | Promotion Threshold Policy | define repeated-signal thresholds and blocking-vs-readout behavior after LSC-T1 de-dup exists | promotion matrix and guard plan | LSC-T1 |
| LSC-T5 | Learning Plane Bridge Alignment | align signal ledger entries with RT2/RT3 and MLW3 proposal-only pipeline; map `EVALUATED` to MLW5/MLW6 validators for high-risk promotion | source-verified bridge contract; no autonomous mutation; no new evaluator | LSC-T1/T4 |
| LSC-T6 | External Agent CLI/MCP Signal Contract | define external-agent portable signal IO for CLI/MCP adapters | CLI/MCP schema and boundary contract only | LSC-T0/T1 |
| LSC-T7 | Latency Guard And Fast Path | enforce capture-fast/promotion-slow budget and avoid retrospective overburden | helper/checker latency rules and tests | LSC-T3/T4 |

## Relationship To AAF-T6 And AAF-T7

AAF-T6 and AAF-T7 are not dropped. They are rehomed:

- AAF-T6 becomes a candidate LSC capture/control tranche for guard-orientation
  read receipts.
- AAF-T7 becomes a candidate LSC helper/readout tranche for unresolved signal
  surfacing, keyword-trap diagnostics, committed-range finality distinction,
  and reviewer-owned closure-scope reminders.

If the operator wants AAF-T6 or AAF-T7 first, dispatch can still be opened as a
bounded tranche, but the work order must cite this roadmap and state how it
fits the Learning Signal Chain.

## Learning Plane Relationship

LSC must preserve the Learning Plane boundaries already established:

- learning proposes, governance approves;
- memory is not truth;
- signal intake is proposal-only unless a later runtime tranche proves more;
- high-risk promotion requires audit/simulation/failure validation;
- `EVALUATED` must reuse MLW5 audit feedback validation and MLW6
  simulation/failure gate rather than defining a new evaluator;
- `autonomousMutationAuthorized=false` remains the invariant for LSC-T0 through
  LSC-T7 unless a future operator-approved roadmap explicitly changes it.

## Open Questions For Claude Rebuttal

1. Is the `LearningSignalIntakeRecord` extension boundary complete enough for
   LSC-T1, or should LSC-T1 cite additional runtime/source surfaces before
   dispatch?
2. Should reviewer, orchestrator, operator, and external-agent capture be
   dispatched as separate sub-tranches under LSC-T2 to reduce false positives?
3. Should the ledger use JSON sources plus a generated aggregate only, or a
   JSON-source plus Markdown-readable index pair?
4. Which source should own `rootCauseGroupId`: LSC ledger, Finding-To-Governance
   row, or MLW3 candidate?
5. Should CGE-T3 and ACE-R1 remain parked until after LSC-T0, or should one of
   them provide source input to LSC-T1 after T0 acceptance?

## Acceptance Criteria For Future Work Orders

Future work orders derived from this roadmap must:

- preserve all parked lanes unless the operator explicitly reorders them;
- cite the applicable AAF, Finding-To-Governance, RT2/RT3, MLW3, MLW5, and MLW6
  sources;
- include a Source Verification Block for any runtime/source/interface claim;
- keep capture fast and promotion governed;
- support external CLI/MCP agents as first-class actors without requiring chat
  memory;
- extend `LearningSignalIntakeRecord` and reuse existing lane, severity,
  defectClass, disposition, and autonomous-mutation fields;
- define deterministic de-dup rules so AAF-T5 tokens, Finding-To-Governance
  rows, and MLW3 candidates are projections of one signal, not separate counts;
- state whether it is docs-only, checker-only, helper-only, schema-only,
  adapter-contract-only, or runtime;
- keep `autonomousMutationAuthorized=false` unless a later authorized runtime
  tranche explicitly changes the invariant;
- avoid public-sync, provider/live, runtime router, direct interception, queue,
  daemon, or readiness claims unless separately authorized.

## Verification/Evidence

Verification performed for this draft:

- `git status --short` before authoring showed a clean worktree.
- `rg` source verification located current AAF-T5, Finding-To-Governance,
  RT2/RT3, MLW3, MLW roadmap, and active-state anchors.
- Claude rebuttal added targeted source verification for
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts`;
  Codex verified the same `LearningSignalIntakeRecord` source before folding the
  correction into this roadmap.
- `git diff --check` passed after draft creation.
- Public export disposition and markdown structural completeness checks passed
  on the uncommitted changed-set scan for this roadmap and companion review
  artifacts.

Evidence boundary: this is roadmap-authoring evidence only. It is not closure
evidence for any implementation tranche.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| AAF-T5 alone captures only worker-return friction | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T0 chain reconciliation | handled by this roadmap draft |
| Reviewer/orchestrator/operator friction can still remain chat-only | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | LSC-T2 multi-role capture contract | deferred |
| External CLI/MCP agents need portable signal IO | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T6 external-agent signal contract | deferred |
| Learning Plane already has proposal-only contracts that LSC must reuse | RULE_EXISTS | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | cite RT2/RT3/MLW3 in future work orders | handled |
| Runtime/provider/cost signal routing requires Learning Plane normalization | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | RUNTIME_LEARNING_CANDIDATE | LSC-T5 bridge alignment after T0/T1 | deferred |
| Minimal Signal Event Contract risked duplicating `LearningSignalIntakeRecord` | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T1 must extend existing intake record and define projection de-dup | handled by rebuttal incorporation |

## Rebuttal Incorporation Ledger

| Rebuttal item | Codex disposition | Roadmap change |
|---|---|---|
| B1 parallel-core risk from duplicating `LearningSignalIntakeRecord` | ACCEPT | Minimal Signal Event Contract now extends/maps to `LearningSignalIntakeInput` / `LearningSignalIntakeRecord`; source verification row added |
| N1 AAF-T5 token and signal event must be one source | ACCEPT | LSC-T1 requires deterministic `WORKER_EXPERIENCE_RETRO -> signal` mapping |
| N2 `promotionState` overlaps disposition vocabulary | ACCEPT | renamed to `captureState` and required mapping to existing disposition values |
| N3 de-dup is core risk | ACCEPT | de-dup/rootCauseGroupId moved into LSC-T1 exit criteria |
| Add `EVALUATED` state | ACCEPT_WITH_BOUNDARY | chain includes `EVALUATED`, mapped to MLW5/MLW6 only |
| Multi-role capture split by role | ACCEPT | LSC-T2 exit criteria require separate eligibility per role |
| Ledger format JSON source plus generated aggregate | ACCEPT_FOR_T1_REVIEW | LSC-T1 must decide generated aggregate shape and drift check |
| Minimal CLI/MCP payload | ACCEPT | external payload reduced to five fields with helper-synthesized defaults |
| CGE-T3 and ACE-R1 remain parked | ACCEPT | Non-Abandonment Rule unchanged |
| Round-2 N4 exact AAF-to-intake severity mapping | ACCEPT | LSC-T1 dispatch requires `NONE` and exact NA assertion to produce no signal entry, and `BLOCKING` to map to `critical` unless a stronger source rule exists |
| Round-2 N5 `captureState` authority | ACCEPT | LSC-T1 dispatch requires `disposition` as governed source of truth and `captureState` as derived/advisory unless a strict allowed-pairs table is defined |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: LSC-T0 is private provenance roadmap/rebuttal planning. Public export
requires separate public-sync authorization and public-safe claim calibration.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LSC-T0 roadmap reconciliation only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | roadmap authoring and advisory classification only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | learning-signal governance planning only |
| forbiddenExpansion | wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |

## Claim Boundary

This roadmap proposes a Learning Signal Chain reconciliation plan only. It does
not implement a signal ledger, runtime Learning Plane mutation, provider/live
proof, CLI/MCP adapter behavior, public-sync, direct IDE/shell/git/filesystem
interception, wrapper/proxy enforcement, queue/daemon, watcher, readiness,
cost optimization, full-hook equivalence, or universal governed-coding control.
