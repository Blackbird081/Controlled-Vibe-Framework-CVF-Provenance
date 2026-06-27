# CVF Agent Work Order - LSC-T6 External Agent CLI/MCP Signal Contract

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-21

docType: work_order

dispatchBaseHead: 5ee4b9b5

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_FOR_WORKER_2026-06-21.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: confirm with `git rev-parse --short HEAD` at worker start.

Current-time notes: LSC-T6 is an adapter-contract-only documentation/reference
tranche. Its prerequisites are satisfied by closed LSC-T1/T2/T3/T4 artifacts,
LSC-T3 material closure commit `fd70157a`, and session-sync commit `5ee4b9b5`.
It follows the operator-selected roadmap order:
`LSC-T2 -> LSC-T4 -> LSC-T3 -> LSC-T6 -> LSC-T5/T7`. The mission is to define
portable external-agent signal IO and exact no-signal assertion for future
CLI/MCP adapters without implementing those adapters.

Do-not-misread notes: do not build a ledger store, source directory, generator,
drift checker, durable store, CLI/MCP adapter, MCP tool, runtime bridge,
provider route, public-sync artifact, queue/daemon, watcher, read-receipt
enforcement, or latency enforcement gate. Do not edit session state, active
handoff, root startup routers, public-sync, `.github/**`, dependency manifests,
web UI, MCP packages, runtime provider routes, Learning Plane runtime source, or
`governance/compat/**`. Do not reopen LSC-T5, LSC-T7, AAF-T6, AAF-T7, CGE-T3,
ACE-R1, MLW7, or MLW8.

Required first actions: read this work order, read the LSC-T6 GC-018 baseline,
read the LSC-T0 roadmap, read the LSC reference front door, read the LSC-T1,
LSC-T2, LSC-T3, and LSC-T4 contracts, read the external knowledge absorption
chain map, confirm actual `executionBaseHead`, and inspect current
`git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with only the required
uncommitted artifacts, actual `executionBaseHead`, actual `git status --short`,
source inventory, scan-depth ledger, gate evidence, and no commit. If blocked,
return `BLOCKED_WITH_REASON` and name the exact source or gate.

The worker-return artifact must include either the structured
`WORKER_EXPERIENCE_RETRO` block or the exact asserting
`WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` line.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two roles across phases: dispatcher creates packet; worker authors reference/front-door/return artifacts; reviewer/closer reviews and commits if accepted |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=5ee4b9b5`; `executionBaseHead` confirmed by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending LSC-T6 artifacts; one reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix LSC-T6 with LSC-T5, LSC-T7, AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7/8, runtime/provider/live, MCP adapter behavior, public-sync, queue/daemon, direct-interception, ledger/generator implementation, or latency guard enforcement |
| Before status evidence | clean worktree at committed dispatch base `5ee4b9b5`; `git status --short` was clean before LSC-T6 dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_COMPLETION_2026-06-21.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; accepted LSC reference-front-door and LSC-T6 contract updates; worker-return artifact; reviewer-owned completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer role |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator roadmap order, LSC-T0 roadmap, closed LSC-T1/T2/T3/T4 reference contracts |
| Intake role | worker authors bounded external-agent signal IO contract |
| Reviewer role | reviewer/closer validates source fidelity, claim boundary, gate evidence, and commit eligibility |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; adapter-contract-only documentation/reference work |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if runtime/source beyond allowed reference paths, MCP/provider/live/public-sync/session-sync/parked-lane expansion is required |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index requirement | NOT_APPLICABLE_WITH_REASON |
| Reason | LSC-T6 is derived from the current LSC roadmap and accepted LSC-T1/T2/T3/T4 reference contracts, not a raw `.private_reference/legacy` corpus scan or LHW wave. |
| Coverage evidence used instead | LSC-T0 roadmap, LSC reference front door, LSC-T1 contract, LSC-T2 contract, LSC-T3 contract, LSC-T4 policy, external knowledge absorption chain map, and AAF helper signal readout source. |

## Required First Reads

The worker must read these sources before editing:

| Source | Reason |
|---|---|
| `docs/reference/guard_orientation/README.md` | task-first guard map and role-neutrality rule |
| `docs/baselines/CVF_GC018_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_2026-06-21.md` | GC-018 authorization and claim boundary |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_FOR_WORKER_2026-06-21.md` | current work order and packet shape |
| `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | LSC roadmap, external-agent readiness boundary, and LSC-T6 row |
| `docs/reference/learning_signal_chain/README.md` | LSC reference front door to update |
| `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | intake ownership, minimal CLI/MCP payload, and no-adapter boundary |
| `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | external-agent returned-output routing and eligibility |
| `docs/reference/learning_signal_chain/CVF_LSC_T3_FAST_HELPER_READOUT.md` | current `signalReadout` shape and advisory readout boundary |
| `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | promotion vocabulary and blocking-vs-readout policy |
| `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | external returned-output route before governed action |
| `governance/compat/run_agent_automation_assist.py` | current helper `signalReadout` source shape for reference only |

## Pre-Flight Checks

The worker must run or record these checks before returning:

```powershell
git rev-parse --short HEAD
git status --short
python -m unittest governance.compat.test_run_agent_automation_assist
python governance/compat/run_agent_automation_assist.py --base 5ee4b9b5 --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py
```

The worker-return artifact must record command results or a
`BLOCKED_WITH_REASON` if a required command cannot run.

## Write Ownership

| Path | Owner during worker execution | Disposition |
|---|---|---|
| `docs/reference/learning_signal_chain/README.md` | worker | may update only to add the LSC-T6 row |
| `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` | worker | create |
| `docs/reviews/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_WORKER_RETURN_2026-06-21.md` | worker | create |
| `docs/baselines/CVF_GC018_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_2026-06-21.md` | reviewer/closer | no worker edit |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_FOR_WORKER_2026-06-21.md` | reviewer/closer | no worker edit |
| session state, active handoff, public-sync, runtime routes, provider code, MCP packages, dependency manifests, `governance/compat/**` | out of worker scope | forbidden |

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope remediation inside
this work order. Operator checkpoint is required only if execution would require
runtime routes, MCP/provider/live/public-sync scope, parked-lane reopening,
dependency installation, secrets/quota, destructive action, or a change to the
claim boundary.

## Purpose

Define the LSC-T6 external-agent signal IO contract so future CLI/MCP-connected
agents can exchange a minimal signal event or exact no-signal assertion without
sharing chat context, while preserving CVF's governed promotion and mutation
boundaries.

Success means the contract tells a future adapter author:

- which five fields an external signal event may carry;
- which defaults helper/ledger normalization may synthesize later;
- how external returned output routes through absorption before signal mapping;
- how LSC-T3 readout and LSC-T4 recommendations appear as advisory output;
- that no direct execution, mutation, adapter behavior, public export, or
  runtime proof is authorized by LSC-T6.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Dispatcher | dispatch author role |
| Worker | LSC-T6 reference/front-door/return author role |
| Reviewer | review role after worker return |
| Closer | closer role after acceptance |
| Session-sync steward | session-sync steward role if session-sync is required |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-21 roadmap order selecting LSC-T6 after LSC-T3 closure | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| LSC-T6 GC-018 | `docs/baselines/CVF_GC018_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_2026-06-21.md` | ACCEPT |
| LSC-T0 roadmap | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | ACCEPT |
| LSC reference front door | `docs/reference/learning_signal_chain/README.md` | ACCEPT |
| LSC-T1 contract | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | ACCEPT |
| LSC-T2 contract | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | ACCEPT |
| LSC-T3 contract | `docs/reference/learning_signal_chain/CVF_LSC_T3_FAST_HELPER_READOUT.md` | ACCEPT |
| LSC-T4 policy | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | ACCEPT |
| External knowledge absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | ACCEPT |
| AAF helper source | `governance/compat/run_agent_automation_assist.py` | SOURCE_AUTHORITY_FOR_SIGNAL_READOUT_SHAPE |

## Scope / Target / Owner Boundary

Allowed scope:

- update `docs/reference/learning_signal_chain/README.md` to list LSC-T6;
- create `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md`;
- create `docs/reviews/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_WORKER_RETURN_2026-06-21.md`;
- update `docs/baselines/CVF_GC018_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_2026-06-21.md` status during reviewer/closer closure;
- create `docs/reviews/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_COMPLETION_2026-06-21.md` during reviewer/closer closure;
- define documentation-only external event shape and no-signal assertion;
- map all fields to existing LSC-T1/Learning Signal Intake ownership;
- describe normalization defaults, readout relationship, absorption routing,
  promotion recommendation boundary, latency boundary, and mutation boundary.

Reviewer/closer closure scope:

- update this work order status and closure evidence;
- update the LSC-T6 GC-018 baseline status;
- create the LSC-T6 completion review;
- repair allowed-scope reference/front-door/return wording, manifests, or
  packet-shape defects required by machine gates before commit.

Forbidden scope:

- no edits to session state, active handoff, root startup routers, public-sync,
  `.github/**`, dependency manifests, web UI, MCP packages, runtime routes,
  provider routes, Learning Plane runtime source, or `governance/compat/**`;
- no ledger source directory, generated aggregate, generator, drift checker,
  durable store, helper implementation, CLI/MCP adapter, MCP tool, runtime
  bridge, provider/live proof, dependency install, queue/daemon/watcher,
  wrapper/proxy enforcement, direct IDE/shell/git/filesystem interception,
  arbitrary command execution, EDIT/COMMIT execution, or read-receipt
  enforcement;
- no public catalog update, public/production/release readiness, full-hook
  equivalence, cost optimization, speed claim, or universal
  governed-coding-control claim;
- no implementation of LSC-T5, LSC-T7, AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7,
  or MLW8.

Risk ceiling: R1 documentation/reference contract.

## Execution Plan

1. Confirm `executionBaseHead` and current `git status --short`.
2. Read all Required First Reads and record a source inventory in the worker
   return.
3. Create the LSC-T6 reference contract with all Required Contract Content.
4. Update the LSC reference front door with an LSC-T6 row that states
   adapter-contract-only scope and no runtime/adapter implementation.
5. Create the worker-return artifact with required packet shape and
   worker-experience token.
6. Run required checks and record results.
7. Return `COMPLETE_PENDING_REVIEW` uncommitted, or `BLOCKED_WITH_REASON` with
   exact source/gate if blocked.

## Evidence Requirements

The worker-return artifact must record:

- actual `executionBaseHead`;
- actual `git status --short`;
- source inventory and scan-depth ledger;
- changed-path list;
- focused unittest result;
- helper smoke result with `--json --enforce`;
- worker-return fast gate result;
- explicit statement that no session/handoff/public-sync/provider/MCP/runtime/
  `governance/compat/**` paths were edited;
- explicit statement that no ledger/generator/drift checker/CLI-MCP adapter was
  implemented;
- exact claim boundary and public export disposition.

## Worker Return Packet Shape Contract

The worker-return artifact must include these sections or exact N/A-with-reason
dispositions where listed, so reviewer-fast can validate the packet without
reviewer repair:

| Packet item | Worker-return disposition |
|---|---|
| Status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| `executionBaseHead` | exact value from `git rev-parse --short HEAD` at worker start |
| `dispatchBaseHead` | `5ee4b9b5` |
| `git status --short` | exact output after worker changes |
| Purpose section | MUST_INCLUDE |
| Scope / Methodology section | MUST_INCLUDE |
| Findings / Position section | MUST_INCLUDE |
| Risk / Corrective Action section | MUST_INCLUDE |
| Claim Boundary section | MUST_INCLUDE |
| Agent Operation Trace Block section | MUST_INCLUDE |
| Delta Execution Claim Boundary Control Block section | MUST_INCLUDE |
| Public Export Disposition section | MUST_INCLUDE |
| External Knowledge Intake Routing section | MUST_INCLUDE |
| Rescan Intelligence Hardening section | MUST_INCLUDE_OR_NA_WITH_REASON |
| Corpus Completeness And Report Integrity section | MUST_INCLUDE_OR_NA_WITH_REASON |
| Finding-To-Governance Learning Disposition section | MUST_INCLUDE |
| Epistemic Process Block section | MUST_INCLUDE_OR_EPISTEMIC_PROCESS_NA_WITH_REASON |
| Machine Closure Package section | MUST_INCLUDE_OR_NA_WITH_REASON; worker must not mark closure |
| Worker-experience token | structured `WORKER_EXPERIENCE_RETRO` or exact asserting `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` |

Conditional sections that do not apply must still be present with `N/A with
reason` or `NOT_APPLICABLE_WITH_REASON` rows. The worker must not record a
clean `git status --short` when the worker-return file or other deliverables
are untracked or modified.

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker must repair machine-gate, helper smoke,
packet-shape, reference-front-door, claim-boundary, public-disposition, or
source-fidelity defects and rerun the relevant gate without asking the operator
or dispatcher.

The worker must stop and return `BLOCKED_WITH_REASON` only when the repair would
exceed Allowed scope, change the claim boundary, require session/handoff/
public-sync/runtime/provider/live/MCP/CLI-adapter/dependency/`governance/compat`
edits, consume secrets or quota, alter parked-lane ordering, touch forbidden
paths, or perform destructive or irreversible actions.

## Acceptance Criteria

The worker return is acceptable only if:

- all Required Deliverables exist and no unauthorized paths are changed;
- LSC-T6 reference contract is adapter-contract-only and documentation-only;
- the external event shape is limited to the five LSC-T0/T1 fields:
  `signalClass`, `actorRole`, `sourceSummary`, `severity`, and `lane`;
- helper/ledger-synthesized defaults are documented without claiming an active
  helper or ledger implementation;
- the contract maps to LSC-T1/Learning Signal Intake ownership instead of
  creating a parallel record;
- exact no-signal assertion is defined for external-agent returns;
- external-agent returned output routes through the external absorption chain
  before structured signal capture;
- LSC-T3 `signalReadout` is described as advisory output only;
- LSC-T4 outcome vocabulary is advisory only and does not authorize dispatch or
  mutation;
- `autonomousMutationAuthorized=false` remains invariant;
- public-safe export is marked separate/public-sync-authorized only;
- the README row states no ledger store, generator, drift checker, CLI/MCP
  adapter behavior, runtime mutation, provider/live proof, or public-sync
  behavior is implemented.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Source evidence | Work-order mapping | Disposition |
|---|---|---|---|
| LSC-T0 minimal CLI/MCP payload is five fields plus synthesized defaults | LSC-T0 lines 188-195 | Required Contract and Acceptance Criteria | SATISFIED_BY_DISPATCH |
| External CLI/MCP agents need contract boundary without direct execution authority | LSC-T0 lines 215-229 | Purpose, Scope, Forbidden scope, Required Contract | SATISFIED_BY_DISPATCH |
| Future work must name CLI/MCP-facing packet/event boundary and source authority | LSC-T0 lines 231-245 | Source Verification Block and Required Contract Content | SATISFIED_BY_DISPATCH |
| LSC-T6 row requires CLI/MCP schema and boundary contract only | LSC-T0 line 257 | Required Deliverables and Write Ownership | SATISFIED_BY_DISPATCH |
| Future work orders must preserve parked lanes and avoid runtime/public/provider/direct-interception claims | LSC-T0 lines 301-321 | Forbidden scope, Claim Boundary, Public Export Disposition | SATISFIED_BY_DISPATCH |
| LSC-T1 requires Learning Signal Intake field reuse | LSC-T1 lines 55-70, 202-210 | Required Contract maps to existing intake fields | SATISFIED_BY_DISPATCH |
| LSC-T2 requires external-agent returns to route through absorption before signal capture | LSC-T2 lines 170-184 | External Knowledge Intake Routing and Required Contract | SATISFIED_BY_DISPATCH |
| LSC-T3 `signalReadout` shape can inform LSC-T6 | LSC-T3 lines 134-151, 176-179 | Required Contract readout relationship | SATISFIED_BY_DISPATCH |
| LSC-T4 promotion vocabulary can be advisory in LSC-T6 | LSC-T4 lines 61-74, 205-223 | Required Contract promotion recommendation boundary | SATISFIED_BY_DISPATCH |

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

## Required Contract Content

The LSC-T6 reference contract must include these sections:

- Purpose
- Scope
- Relationship To Existing LSC Records
- External-Agent Signal Event Shape
- External-Agent No-Signal Assertion
- Normalization Defaults
- Readout Relationship
- Promotion Recommendation Boundary
- External Returned-Output Absorption Routing
- Mutation Boundary
- Latency Budget
- Parking Ledger
- Public Export Disposition
- Delta Execution Claim Boundary Control Block
- Agent Operation Trace Block
- Claim Boundary

Required policy assertions:

- LSC-T6 is adapter-contract-only and documentation/reference-only.
- The minimal external-agent event contains only `signalClass`, `actorRole`,
  `sourceSummary`, `severity`, and `lane`.
- Helper/ledger defaults are future normalization behavior, not current runtime
  implementation.
- LSC-T6 extends/maps to LSC-T1 and Learning Signal Intake field ownership.
- External returned output is not directly eligible for structured signal
  capture until routed through the external knowledge absorption chain.
- LSC-T3 `signalReadout` remains advisory.
- LSC-T4 promotion outcomes remain advisory and do not create work.
- `autonomousMutationAuthorized=false` remains invariant.
- No CLI/MCP adapter behavior, provider/live proof, public-sync, direct
  interception, queue/daemon, watcher, readiness, full-hook equivalence, cost
  optimization, or universal governed-coding control is implemented.

## Review Gate

The reviewer/closer must run reviewer-fast or a stricter applicable gate before
accepting the worker return. Acceptance requires checking source fidelity,
contract-only behavior, external-agent absorption routing, public/provenance
boundary, finding-to-governance disposition, Delta boundary N/A, and the
worker-return packet shape.

## Closure Checklist

Reviewer/closer closure evidence must resolve these items:

- Required deliverables exist.
- No forbidden paths changed.
- Source Verification claims remain current.
- Contract remains adapter-contract-only and documentation/reference-only.
- README row states no adapter/runtime/public/provider behavior.
- External event shape stays limited to LSC-T0/T1 minimal fields.
- No-signal assertion is exact and non-mutating.
- External returned-output routing requires absorption before capture.
- LSC-T3 readout and LSC-T4 outcomes are advisory only.
- Worker-return packet includes required sections and token.
- Reviewer-fast or stricter gate passes.
- Commit ownership remains reviewer/closer only.
- Session-sync is performed only if mode or next-move surfaces change.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_FOR_WORKER_2026-06-21.md` | `Status: CLOSED_PASS_BOUNDED` after reviewer/closer patch | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_2026-06-21.md` | `Status: CLOSED_PASS_BOUNDED` after reviewer/closer patch | PASS |
| Worker return | `docs/reviews/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_WORKER_RETURN_2026-06-21.md` | `Status: COMPLETE_PENDING_REVIEW`; accepted by reviewer/closer with source-fidelity repairs | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_COMPLETION_2026-06-21.md` | reviewer-owned `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | LSC-T6 accepted by this closure; roadmap remains the governing LSC-T0 plan | PASS |
| Reference front door | `docs/reference/learning_signal_chain/README.md` | LSC-T6 row present and bounded to adapter-contract-only documentation/reference behavior | PASS |
| Reference contract | `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` | `Status: ACTIVE_REFERENCE` | PASS |
| Session continuity | active session front-door/state/handoff after material commit | session-sync follows material closure commit | N/A with reason |
| Registry JSON | N/A with reason: no generated JSON registry created or changed by LSC-T6 closure | no registry mutation | PASS |
| Registry Markdown | N/A with reason: no generated Markdown index created in LSC-T6 closure | no generated Markdown registry | PASS |
| External evidence digest | N/A with reason: no external benchmark/provider/live digest created | reference-contract closure only | N/A with reason |
| System loop interlock | N/A with reason: no runtime/source interlock changed | no runtime/source mutation | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence | N/A with reason: LSC-T6 creates no runtime receipt | N/A_WITH_REASON |
| Query acceptance evidence | N/A with reason: LSC-T6 performs no query acceptance | N/A_WITH_REASON |
| Worker-return acceptance | worker return present and accepted by reviewer/closer | PASS |
| Closure claim | `CLOSED_PASS_BOUNDED` adapter-contract-only reference closure | PASS |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all Required Deliverables are created
and required gate evidence is recorded. Return `BLOCKED_WITH_REASON` if the task
requires forbidden paths, runtime route changes, provider/live proof,
public-sync, MCP/CLI adapter behavior, dependency install, destructive actions,
or parked-lane reopening.

## Current Runtime Freshness Verification

| Claim | Freshness evidence | Disposition |
|---|---|---|
| LSC-T6 contract path does not already exist | `Get-ChildItem docs/reference/learning_signal_chain -Filter '*LSC_T6*'` returned no existing file before dispatch authoring | ACCEPT |
| LSC-T6 work order and baseline paths do not already exist | `Get-ChildItem docs/work_orders -Filter '*LSC_T6*'`; `Get-ChildItem docs/baselines -Filter '*LSC_T6*'` returned no existing file before dispatch authoring | ACCEPT |
| Current helper exposes `signalReadout` only as helper output | `governance/compat/run_agent_automation_assist.py` lines 459-539, 754-845 | ACCEPT |
| Runtime route implementation is not authorized | Allowed and Forbidden scope in this work order | N/A_WITH_REASON |
| CLI/MCP adapter behavior is not authorized | Forbidden scope and Claim Boundary | N/A_WITH_REASON |
| Provider/live proof is not authorized | Forbidden scope and Claim Boundary | N/A_WITH_REASON |
| Public-sync is not authorized | Public route and Public Export Disposition | N/A_WITH_REASON |

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
| SEPARATE_RUNTIME_TRANCHE | actual CLI/MCP adapter, ledger store, source directory, generator, drift checker, runtime bridge, latency guard. |
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

- Corpus task class: NOT_APPLICABLE_WITH_REASON - LSC-T6 is a bounded reference
  contract dispatch, not a corpus enumeration or legacy scan.
- Corpus root: NOT_APPLICABLE_WITH_REASON - no corpus root is assigned.
- Snapshot time: NOT_APPLICABLE_WITH_REASON - no corpus snapshot is taken.
- Enumeration command: filesystem-backed direct file reads listed in Source
  Verification Block and Required First Reads; no corpus enumeration command is
  authorized.
- Manifest artifact or inline manifest: inline Source Verification Block above.
- Manifest hash: NOT_APPLICABLE_WITH_REASON - no corpus manifest hash is
  created.
- Processing ledger artifact or inline ledger: inline Source Verification Block
  and Roadmap-To-Work-Order Trace Matrix above.
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

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch for Learning Signal Chain contract work. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher role |
| Provider or surface | local workspace |
| Session or invocation | LSC-T6 dispatch authoring, 2026-06-21 |
| Working directory | repository root |
| Command or tool surface | local file edits and governance gates |
| Target paths | `docs/baselines/CVF_GC018_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_2026-06-21.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_FOR_WORKER_2026-06-21.md` |
| Allowed scope source | operator-selected LSC roadmap order and active session next allowed move |
| Before status evidence | clean worktree at committed base `5ee4b9b5`; `git status --short` clean before dispatch authoring |
| After status evidence | two uncommitted dispatch artifacts created for pre-dispatch review |
| Diff evidence | new GC-018 baseline and new worker dispatch packet |
| Approval boundary | dispatcher role may create dispatch artifacts only; worker remains `WORKER_MUST_NOT_COMMIT` |
| Claim boundary | adapter-contract-only dispatch; no runtime/provider/MCP/public-sync implementation |
| Agent type | dispatcher role |
| Invocation ID | `lsc-t6-external-agent-cli-mcp-signal-contract-dispatch-2026-06-21` |
| Expected manifest | LSC-T6 GC-018 and LSC-T6 worker dispatch packet |
| Actual changed set | `docs/baselines/CVF_GC018_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_2026-06-21.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_FOR_WORKER_2026-06-21.md` |
| Manifest delta | MATCH |
| Dispatch Signal | no dispatch-author learning signal beyond expected LSC-T6 packet authoring; source verification matched roadmap and predecessor contracts |

## Claim Boundary

This work order authorizes only LSC-T6 adapter-contract-only documentation for
external-agent portable signal IO and no-signal assertion. It does not implement
or authorize a ledger store, source directory, generator, drift checker, durable
store, runtime Learning Plane mutation, provider/live proof, CLI/MCP adapter
behavior, public-sync, direct interception, wrapper/proxy enforcement,
queue/daemon, watcher, readiness, cost optimization, full-hook equivalence,
read-receipt enforcement, or universal governed-coding control.
