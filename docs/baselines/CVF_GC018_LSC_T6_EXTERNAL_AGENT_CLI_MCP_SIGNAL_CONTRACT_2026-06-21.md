# CVF GC-018 - LSC-T6 External Agent CLI/MCP Signal Contract

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-21

docType: baseline

dispatchBaseHead: 5ee4b9b5

Batch ID: LSC-T6

## Purpose

Authorize LSC-T6 as the next bounded Learning Signal Chain foundation tranche:
a documentation/reference contract for external-agent portable signal IO across
future CLI/MCP adapters.

LSC-T6 follows closed LSC-T3 at material commit `fd70157a` and session-sync
commit `5ee4b9b5`. It must define the contract boundary only. It must not build
CLI/MCP adapter behavior, runtime provider routing, a ledger store, or any
direct execution surface.

## Operator Authorization

The operator selected the roadmap order on 2026-06-21:

`LSC-T2 -> LSC-T4 -> LSC-T3 -> LSC-T6 -> LSC-T5/T7`.

LSC-T3 is now closed, and active continuity identifies LSC-T6 External Agent
CLI/MCP Signal Contract as the next allowed move.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-21 roadmap order selecting LSC-T6 after LSC-T3 closure | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| LSC-T0 roadmap | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | ACCEPT |
| LSC reference front door | `docs/reference/learning_signal_chain/README.md` | ACCEPT |
| LSC-T1 source-layout and de-dup contract | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | ACCEPT |
| LSC-T2 multi-role capture contract | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | ACCEPT |
| LSC-T3 fast helper readout contract | `docs/reference/learning_signal_chain/CVF_LSC_T3_FAST_HELPER_READOUT.md` | ACCEPT |
| LSC-T4 promotion threshold policy | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | ACCEPT |
| External knowledge absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | ACCEPT |
| AAF helper source | `governance/compat/run_agent_automation_assist.py` | SOURCE_AUTHORITY_FOR_SIGNAL_READOUT_SHAPE |

Provider-specific memory, chat memory, and private agent-local files are not
CVF source authority. External-agent outputs are input only until routed through
the external knowledge absorption chain and promoted by governed CVF artifacts.

## Scope / Owner Boundary

Allowed worker scope:

- create `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md`;
- update `docs/reference/learning_signal_chain/README.md` with an LSC-T6 row;
- create `docs/reviews/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_WORKER_RETURN_2026-06-21.md`;
- define external-agent signal event fields, exact no-signal assertion, helper
  normalization defaults, readout relationship, absorption routing, promotion
  recommendation boundary, and mutation boundary;
- keep the contract adapter-contract-only and documentation/reference-only.

Forbidden worker scope:

- no edits to `governance/compat/**`, `CVF_SESSION/**`, active handoff, root
  startup routers, public-sync, `.github/**`, dependency manifests, web UI,
  MCP packages, runtime provider routes, or Learning Plane runtime source;
- no ledger source directory, generated aggregate, generator, drift checker,
  durable store, runtime Learning Plane mutation, provider/live proof,
  dependency install, queue, daemon, watcher, wrapper/proxy, direct
  IDE/shell/git/filesystem interception, arbitrary command execution, or
  EDIT/COMMIT execution;
- no actual CLI/MCP adapter behavior, MCP tool implementation, shell bridge,
  adapter invocation, read-receipt enforcement, or public catalog update;
- no public/production/release readiness, full-hook equivalence, cost
  optimization, speed claim, or universal governed-coding-control claim;
- no implementation of LSC-T5, LSC-T7, AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7,
  or MLW8.

Risk ceiling: R1 documentation/reference contract.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` with only these
worker-owned artifacts changed or created:

- `docs/reference/learning_signal_chain/README.md`
- `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md`
- `docs/reviews/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_WORKER_RETURN_2026-06-21.md`

No session, handoff, public-sync, provider/live, MCP, dependency, queue/daemon,
checker, helper, or runtime mutation path is authorized in worker execution.

## Decision / Baseline / Proposed Tranche

Baseline decision: LSC-T6 is ready for worker dispatch as a bounded
adapter-contract-only tranche after LSC-T3 closure.

Proposed tranche: `LSC-T6 External Agent CLI/MCP Signal Contract`.

Tranche owner split: dispatcher creates this GC-018 baseline and paired work
order; worker authors only the LSC-T6 reference/front-door update and
worker-return artifact without committing; reviewer/closer reviews and commits
accepted material if gates pass.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| LSC-T0 defines minimal CLI/MCP payload fields and helper-synthesized defaults | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 188-195 | `signalClass`; `actorRole`; `sourceSummary`; `severity`; `lane`; `repeatRisk`; `autonomousMutationAuthorized` | LSC-T0 roadmap | ACCEPT |
| LSC-T0 defines external-agent CLI/MCP readiness boundary and blocks runtime behavior | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 215-229 | External Agent CLI/MCP Readiness Boundary | LSC-T0 roadmap | ACCEPT |
| LSC-T0 design-control gate requires CLI/MCP-facing boundary, intake extension, mutation boundary, source authority, and runtime boundary | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 231-245 | Design Control Gate | LSC-T0 roadmap | ACCEPT |
| LSC-T0 defines LSC-T6 as External Agent CLI/MCP Signal Contract | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | line 257 | `LSC-T6`; External Agent CLI/MCP Signal Contract | LSC-T0 roadmap | ACCEPT |
| LSC-T0 future work-order criteria require external CLI/MCP support, intake reuse, docs/schema/adapter-contract classification, and parked public/runtime scope | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 301-321 | Acceptance Criteria For Future Work Orders | LSC-T0 roadmap | ACCEPT |
| LSC-T1 requires reuse of Learning Signal Intake fields rather than parallel record definitions | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | lines 55-70 | `LearningSignalIntakeInput`; `LearningSignalIntakeRecord`; field ownership | LSC-T1 contract | ACCEPT |
| LSC-T1 defines CLI/MCP minimal payload and no-adapter boundary | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | lines 202-210 | CLI/MCP Minimal Payload Boundary | LSC-T1 contract | ACCEPT |
| LSC-T2 defines external-agent returned-output eligibility and no direct raw external capture | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | lines 85-91 | External reviewer / external agent | LSC-T2 contract | ACCEPT |
| LSC-T2 requires external-agent returns to pass through external knowledge absorption before signal mapping | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | lines 170-184 | External Agent Returned-Output Routing | LSC-T2 contract | ACCEPT |
| LSC-T3 defines current `signalReadout` shape for advisory helper output | `docs/reference/learning_signal_chain/CVF_LSC_T3_FAST_HELPER_READOUT.md` | lines 25-58, 134-151 | `signalReadout` | LSC-T3 contract | ACCEPT |
| LSC-T3 states its readout shape is candidate input to LSC-T6 and does not authorize mutation | `docs/reference/learning_signal_chain/CVF_LSC_T3_FAST_HELPER_READOUT.md` | lines 176-179, 245-253 | LSC-T6 routing; mutation boundary | LSC-T3 contract | ACCEPT |
| LSC-T4 defines promotion outcome vocabulary and LSC-T6 relationship | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | lines 61-74, 205-223 | LSC-T4 outcome vocabulary; LSC-T6 Future-Tranche Routing | LSC-T4 policy | ACCEPT |
| External knowledge absorption chain map routes external-agent returned output before governed action | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | lines 55-76 | Mandatory Chain; Input Type Router | External agent review chain map | ACCEPT |
| Current helper JSON and human output expose `signalReadout` but do not provide CLI/MCP adapter behavior | `governance/compat/run_agent_automation_assist.py` | lines 459-539, 754-845 | `SignalReadoutItem`; `AssistReport.to_dict`; `_print_human`; `main` | AAF helper | ACCEPT |
| LSC reference front door currently lists LSC-T1 through LSC-T4 and forbids CLI/MCP adapter/runtime behavior | `docs/reference/learning_signal_chain/README.md` | lines 40-61 | Current Contracts; What This Front Door Does Not Authorize | LSC reference front door | ACCEPT |

## New Doc-Only Terms

| Proposed term | Owner in LSC-T6 | Runtime status | Reason |
|---|---|---|---|
| `externalAgentSignalEvent` | LSC-T6 reference contract | DOC_ONLY_NEW | portable external-agent event shape for future CLI/MCP adapters |
| `externalAgentNoSignalAssertion` | LSC-T6 reference contract | DOC_ONLY_NEW | exact no-signal assertion for external-agent returns |
| `adapterContractOnly` | LSC-T6 reference contract | DOC_ONLY_NEW | declares that no adapter behavior is implemented |
| `normalizationDefaults` | LSC-T6 reference contract | DOC_ONLY_NEW | helper/ledger-synthesized defaults from LSC-T0/T1 |
| `readoutRelationship` | LSC-T6 reference contract | DOC_ONLY_NEW | relationship between LSC-T3 `signalReadout` and external-agent IO |

These terms are reference vocabulary only. They must not be presented as
existing runtime fields, ledger schema fields, MCP tool names, CLI command
flags, or adapter implementation identifiers.

## Required Contract

The worker must author an LSC-T6 reference contract with these properties:

- adapter-contract-only: define portable IO and no-signal assertion only;
- minimal: external event input is limited to `signalClass`, `actorRole`,
  `sourceSummary`, `severity`, and `lane`;
- normalized: helper/ledger may synthesize `sourceId`, `observedAt`,
  `repeatRisk=POSSIBLE`, `captureState=CAPTURED`,
  `autonomousMutationAuthorized=false`, and pending `rootCauseGroupId`;
- intake-aligned: the contract extends/maps to LSC-T1 and Learning Signal Intake
  ownership rather than creating a parallel record;
- readout-aware: LSC-T3 `signalReadout` is candidate advisory output for
  external agents, not an executable instruction;
- threshold-aware: LSC-T4 promotion outcome vocabulary may appear only as an
  advisory recommendation;
- absorption-routed: external returned output must follow the external
  knowledge absorption chain before becoming a structured signal;
- mutation-bounded: `autonomousMutationAuthorized=false` remains invariant;
- public-bounded: public-safe export requires separate public-sync
  authorization;
- runtime-bounded: no runtime/provider/live/direct-interception/queue/daemon/
  watcher/readiness behavior is implemented or claimed.

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `5ee4b9b5`.
- `git status --short` was clean before LSC-T6 dispatch authoring.
- Source verification used direct file reads and `rg -n` lookups against
  current repository files.

Required pre-dispatch verification before dispatch commit:

```powershell
python governance/compat/run_agent_automation_assist.py --base 5ee4b9b5 --head HEAD --json --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 5ee4b9b5 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 5ee4b9b5 --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base 5ee4b9b5 --head HEAD --enforce
```

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | returned output to finding classification to governed baseline/work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | LSC-T6 External Agent CLI/MCP Signal Contract |
| Disposition | ADAPT as CVF-owned external-agent signal IO contract |
| Claim boundary | external-agent returns remain input only until classified and promoted through governed CVF artifacts; LSC-T6 does not implement external-agent CLI/MCP adapter behavior |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LSC-T6 external-agent signal contract dispatch only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | documentation/reference contract authoring only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | external-agent portable signal IO contract and boundary only |
| forbiddenExpansion | wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, CLI/MCP adapter behavior, and universal control remain out of scope |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| External CLI/MCP agents need portable signal IO without chat-memory dependence | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T6 must define adapter-contract-only external-agent signal IO | handled by this dispatch |
| LSC-T6 must not create a parallel Learning Signal record | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | worker must map fields to LSC-T1 and Learning Signal Intake ownership | handled by this dispatch |
| Actual CLI/MCP adapter behavior remains out of scope | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no adapter/runtime implementation in this tranche | handled |
| Public-facing export remains out of scope | RUNTIME_SIGNAL_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | public-sync requires separate authorization | handled |

## Rescan Intelligence Hardening

- Original source artifact: `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`.
- Predecessor intake artifact: `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md`.
- Predecessor capture artifact: `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md`.
- Predecessor readout artifact: `docs/reference/learning_signal_chain/CVF_LSC_T3_FAST_HELPER_READOUT.md`.
- Predecessor promotion artifact: `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because LSC-T6 moves external-agent
  CLI/MCP signal IO from roadmap row into dispatch-ready reference-contract work.
- Routing matrix status: `DO_NOW` for adapter-contract-only reference and
  front-door update; `SEPARATE_RUNTIME_TRANCHE` for actual CLI/MCP adapter,
  ledger store, generator, drift checker, runtime bridge, public-sync, or
  latency guard; `STRATEGIC_OPERATOR_DECISION` for LSC-T5/T7 after LSC-T6;
  `OUT_OF_SCOPE` for provider/live/direct-interception/readiness claims.
- Semantic sampling status: sampled LSC-T0 minimal payload, LSC-T0 external
  readiness boundary, LSC-T1 intake ownership, LSC-T2 external return routing,
  LSC-T3 readout shape, LSC-T4 outcome vocabulary, and external absorption map.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | LSC remains capture-fast, promotion-slow, and proposal-only. |
| CHANGED_DISPOSITION | LSC-T6 external-agent signal IO moved from roadmap row into dispatch requirements. |
| NEW_FINDING | External agents need a portable no-chat signal event and exact no-signal assertion before adapters can be safely implemented later. |
| REMOVED_OR_REJECTED | Runtime/provider/live/public-sync/direct-interception/CLI-MCP adapter behavior remains rejected for LSC-T6. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | LSC-T6 external-agent CLI/MCP signal contract, README row, and worker-return packet. |
| SEPARATE_RUNTIME_TRANCHE | actual CLI/MCP adapter, ledger store, generator, drift checker, runtime bridge, latency guard. |
| STRATEGIC_OPERATOR_DECISION | LSC-T5/T7 per active roadmap order after LSC-T6. |
| OUT_OF_SCOPE | provider/live, public-sync, direct interception, readiness, universal control. |
| RESOLVED_BY_DESIGN | define portable IO while preserving no execution authority. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| LSC-T6-S1 | LSC-T0 work plan | LSC-T6 exits with CLI/MCP schema and boundary contract only | mapped into Required Deliverables | prevents adapter implementation under contract work | PASS |
| LSC-T6-S2 | LSC-T1 intake ownership | external payload must map to existing intake fields | Required Contract maps to LSC-T1 fields | prevents parallel signal record | PASS |
| LSC-T6-S3 | LSC-T2 external routing | raw external output is not directly eligible for capture | absorption routing required | prevents raw external agent output becoming authority | PASS |
| LSC-T6-S4 | LSC-T3 readout shape | readout is advisory and non-mutating | readout relationship marked advisory only | prevents executable-helper claim | PASS |
| LSC-T6-S5 | LSC-T4 outcomes | promotion vocabulary is advisory | promotion recommendation boundary required | prevents closure/blocking overclaim | PASS |

## Corpus Completeness And Report Integrity

- Corpus task class: NOT_APPLICABLE_WITH_REASON - LSC-T6 dispatch is a bounded
  reference-contract work order, not a corpus enumeration or legacy scan.
- Corpus root: NOT_APPLICABLE_WITH_REASON - no corpus root is assigned.
- Snapshot time: NOT_APPLICABLE_WITH_REASON - no corpus snapshot is taken.
- Enumeration command: filesystem-backed direct file reads listed in Source
  Verification Block and Required First Reads; no corpus enumeration command is
  authorized.
- Manifest artifact or inline manifest: inline Source Verification Block above.
- Manifest hash: NOT_APPLICABLE_WITH_REASON - no corpus manifest hash is
  created.
- Processing ledger artifact or inline ledger: inline Source Verification Block
  and semantic sampling tables above.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline Source Verification Block; ledger_terminal=READ for named source rows; exclusions=corpus enumeration and legacy scan surfaces out of scope; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: corpus scan, legacy source-family enumeration,
  public-sync copy, runtime/provider/live proof, CLI/MCP adapter, and parked lanes.
- Unreadable or unsupported files: 0.
- Aggregation check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate is
  created.
- Drift check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate or generated
  corpus registry is changed.
- Output traceability: Required Deliverables and Source Verification Block
  define all worker output traceability.
- Adversarial verification: reviewer/closer must run reviewer-fast or stricter
  applicable gate before acceptance.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch for Learning Signal Chain contract work. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Closure Disposition

LSC-T6 is closed as `CLOSED_PASS_BOUNDED` after reviewer acceptance of the
no-commit worker return and reviewer-owned source-fidelity repairs. The closure
accepts the adapter-contract-only reference contract, LSC front-door row, worker
return, and completion review.

No CLI/MCP adapter behavior, runtime route, provider/live proof, public-sync,
ledger store, generator, drift checker, durable store, latency guard, direct
interception, wrapper/proxy enforcement, queue/daemon, watcher, readiness,
cost optimization, full-hook equivalence, or universal governed-coding-control
claim is made.

## Claim Boundary

This baseline authorizes only LSC-T6 adapter-contract-only documentation for
external-agent portable signal IO and no-signal assertion. It does not implement
a ledger store, source directory, generator, drift checker, durable store,
runtime Learning Plane mutation, provider/live proof, CLI/MCP adapter behavior,
public-sync, direct interception, wrapper/proxy enforcement, queue/daemon,
watcher, readiness, cost optimization, full-hook equivalence, or universal
governed-coding control.
