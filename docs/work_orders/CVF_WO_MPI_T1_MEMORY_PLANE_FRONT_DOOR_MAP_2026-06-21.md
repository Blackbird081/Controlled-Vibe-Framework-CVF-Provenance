# CVF Agent Work Order - MPI-T1 Memory Plane Front-Door Map

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-21

docType: work_order

dispatchBaseHead: acb2b980

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_WO_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_2026-06-21.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: confirm with `git rev-parse --short HEAD` at worker start.

Current-time notes: MPI-T1 is released for worker dispatch after MPI-T0 INDEX
Legacy Memory/Graph Recheck closed. Dependency-release evidence:
`docs/reviews/CVF_MPI_T0_INDEX_LEGACY_MEMORY_GRAPH_RECHECK_COMPLETION_2026-06-21.md`.

Do-not-misread notes: do not edit any runtime source, the readout route or
projection, the durable store, the scan registry sources or generated aggregate,
LSC reference contracts, MKG7 contract content, session state, active handoff,
root startup routers, public-sync, `.github/**`, dependency manifests, web UI
routes, or MCP packages. Do not create a read projection, helper, test, schema,
or route. Do not reopen MPI-T2/T3/T4, MKG7, LSC-T5/T7, AAF-T6, AAF-T7, CGE-T3,
ACE-R1, MLW7, or MLW8.

Required first actions: read this work order, read the MPI-T1 GC-018 baseline,
read the MPI roadmap and Codex rebuttal, read the MKG7 operational contract and
roadmap, read the memory readout route and projection source, read the durable
store fail-closed branch, read the Corpus Scan Registry standard, read CI1-T11,
MLW0, and MLW1-MLW6 governed legacy absorption artifacts, read the LSC-T6
contract boundary, read the GC-022 classification, read the governed file size
guard, read KGR pre-review, KGR1 bounded owner evidence, and Graphify registry
entry, confirm actual
`executionBaseHead`, and inspect current `git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with only the required
uncommitted artifacts, actual `executionBaseHead`, actual `git status --short`,
source inventory, scan-depth ledger, gate evidence, and no commit. If blocked,
return `BLOCKED_WITH_REASON` and name the exact source or gate.

The worker-return artifact must include either the structured
`WORKER_EXPERIENCE_RETRO` block or the exact asserting
`WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` line.

## Purpose

Create one POINTER_RECORD navigation reference for the Memory Plane Front-Door
Map after MPI-T0 closed. The worker mission is bounded documentation/reference
work only.

## Agent Roles

| Role | Owner | Commitment boundary |
|---|---|---|
| Dispatcher | Codex/orchestrator | creates GC-018 baseline and this worker packet |
| Worker | external worker/Claude | edits only Required Deliverables and returns uncommitted |
| Reviewer/closer | Codex/orchestrator after worker return | validates, repairs allowed-scope packet defects, commits accepted material, and performs session sync if needed |
| Operator | human operator | checkpoint only for scope expansion, parked-lane reopening, provider/live/public/runtime work, secrets, or destructive action |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator selection | MPI lane selected, MPI-T1 first, on 2026-06-21 | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| MPI-T1 GC-018 baseline | `docs/baselines/CVF_GC018_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_2026-06-21.md` | ACCEPT |
| MPI roadmap | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | ACCEPT |
| Codex rebuttal | `docs/reviews/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_CODEX_REBUTTAL_2026-06-21.md` | ACCEPT |
| MKG7 operational contract and roadmap | `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md`; `docs/roadmaps/CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md` | SOURCE_AUTHORITY_FOR_LPF_READOUT |
| Memory readout route and projection | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | SOURCE_AUTHORITY_FOR_READOUT_SURFACE |
| GC-051 standard, LSC-T6 contract, GC-022 classification | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`; `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md`; `docs/reference/CVF_MEMORY_RECORD_CLASSIFICATION.md` | ACCEPT |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two roles across phases: dispatcher creates packet; worker authors the map and return artifacts; reviewer/closer reviews and commits if accepted |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=acb2b980`; `executionBaseHead` confirmed by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending MPI-T1 artifacts; one reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix MPI-T1 with MPI-T2/T3/T4, MKG7, LSC-T5/T7, AAF-T6/T7, CGE-T3, ACE-R1, MLW7/8, runtime/provider/live, MCP adapter behavior, public-sync, queue/daemon, direct-interception, or any runtime-bearing artifact |
| Before status evidence | committed dispatch base `acb2b980` had worktree clean; MPI roadmap and Codex rebuttal were post-base untracked operator-review intake before MPI-T1 dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_COMPLETION_2026-06-21.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; MPI roadmap status row if accepted; worker-return artifact; reviewer-owned completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW`; accepted with reviewer correction |
| closer | reviewer/closer role |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator selection of MPI lane and MPI-T1 first; MPI roadmap; Codex rebuttal |
| Intake role | worker authors the bounded navigation-reference map |
| Reviewer role | reviewer/closer validates source fidelity, claim boundary, gate evidence, and commit eligibility |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; R0 navigation-reference work |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if runtime edits, read projection, helper/test, schema/route, registry/durable write, MCP/provider/live/public-sync/session-sync, or parked-lane expansion is required |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index requirement | APPLICABLE - `MEM-001` |
| Coverage index path | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Coverage-index row evidence | `MEM-001` Memory / Knowledge / MEMCON workflow-chain; status `PARTIAL_RECHECK_REQUIRED`; next action says before new memory/scan foundation work, reconcile against corpus registry and MEMCON closure packets |
| MPI-T1 disposition | SATISFIED_FOR_R0_NAVIGATION_MAP_WITH_BOUNDARY |
| Evidence used | CI1-T11 consolidated roadmap, MLW0 current source verification map, MLW1-MLW6 completion review, Corpus Scan Registry standard, and MEM-001 coverage-index row |
| Boundary | MPI-T1 reads governed absorption artifacts only; no fresh legacy source-family enumeration, no MEMCON implementation, no runtime source edit, no scan-registry mutation, and no direct legacy runtime promotion |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | external-agent returned roadmap/rebuttal output -> review/classification -> operator-selected MPI-T1 dispatch packet |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | MPI-T1 Memory Plane Front-Door Map work order |
| Disposition | ADAPT as bounded CVF-owned navigation reference dispatch |
| Claim boundary | external-agent input remains advisory until promoted through this source-verified work order; no runtime, provider/live, public-sync, adapter, durable-write, or legacy-runtime adoption |

## Required First Reads

| Source | Reason |
|---|---|
| `docs/reference/guard_orientation/README.md` | task-first guard map and role-neutrality rule |
| `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | MEM-001 coverage-index row for memory/knowledge/MEMCON workflow-chain |
| `docs/baselines/CVF_GC018_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_2026-06-21.md` | GC-018 authorization and claim boundary |
| `docs/work_orders/CVF_WO_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_2026-06-21.md` | current work order and packet shape |
| `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | MPI roadmap, MPI-T1 row, design control gate |
| `docs/reviews/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_CODEX_REBUTTAL_2026-06-21.md` | reviewer recommendation and required revisions |
| `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | MKG7 LPF operational contract to cite, not redefine |
| `docs/roadmaps/CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md` | MKG7 closure and surface inventory |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | readout route auth and summary-only invariants |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | readout projection that strips content |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | durable store fail-closed write branch and unwired status |
| `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | GC-051 generated-from-source, inherit, Finding Discovery rules |
| `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` | GC-023 human-reviewability and split/rotation discipline for governed files |
| `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | governed legacy memory/learning absorption predecessor |
| `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | maps legacy memory/learning vocabulary to current source authority |
| `docs/reviews/CVF_MLW1_MLW6_MEMORY_LEARNING_CORE_WORKFLOW_CHAIN_COMPLETION_2026-06-05.md` | proves bounded MLW1-MLW6 contract chain closure |
| `docs/reference/CVF_KGR_ABSORPTION_PREREVIEW_2026-06-01.md` | distinguishes Memory Plane from KGR and records Graphify/KGR partial absorption boundary |
| `docs/roadmaps/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_ROADMAP_2026-06-01.md` | KGR1 bounded LPF local graph retrieval roadmap |
| `docs/reviews/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_LOCAL_REVIEW_2026-06-02.md` | KGR1 bounded current owner/source verification and claim boundary |
| `docs/corpus-intelligence/registry/entries/legacy-cvf-important-graphify.json` | Graphify/KGR corpus registry entry and partial coverage input |
| `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` | LSC signal/reference boundary and `adapterContractOnly` |
| `docs/reference/CVF_MEMORY_RECORD_CLASSIFICATION.md` | GC-022 FULL/SUMMARY/POINTER classes |

## Pre-Flight Checks

The worker must run or record these checks before returning:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_worker_return_fast_gate.py
```

The worker-return artifact must record command results or a
`BLOCKED_WITH_REASON` if a required command cannot run.

## Evidence Requirements

The worker-return artifact must record:

- exact `executionBaseHead`;
- actual before/after `git status --short`;
- Source Inventory with each required first-read source;
- Scan Depth Ledger, including any unreadable or deferred source;
- changed-path list limited to the two Required Deliverables;
- worker-return fast gate result;
- explicit statement that no runtime, route, projection, helper, test, schema,
  scan-registry, durable-store, session, handoff, public-sync, provider/live, or
  MCP path was edited;
- explicit statement that governed CI1-T11/MLW absorption artifacts were cited
  as predecessor authority only, not direct runtime source;
- exact Claim Boundary and Public Export Disposition.

## Write Ownership

| Path | Owner during worker execution | Disposition |
|---|---|---|
| `docs/reference/CVF_MEMORY_PLANE_MAP.md` | worker | create |
| `docs/reviews/CVF_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_WORKER_RETURN_2026-06-21.md` | worker | create |
| `docs/baselines/CVF_GC018_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_2026-06-21.md` | reviewer/closer | no worker edit |
| `docs/work_orders/CVF_WO_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_2026-06-21.md` | reviewer/closer | no worker edit |
| `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | reviewer/closer | no worker edit |
| `EXTENSIONS/**`, readout route/projection, durable store, scan registry, LSC contracts, MKG7 contract, session state, active handoff, public-sync, MCP packages, dependency manifests, `.github/**` | out of worker scope | forbidden |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/CVF_MEMORY_PLANE_MAP.md` as a POINTER_RECORD navigation
  map;
- describe each memory-facing surface by purpose, owner, reader/authenticated
  surface, boundary, and runtime status;
- cite source files for every runtime claim without copying their content;
- create the worker-return artifact.

Reviewer/closer closure scope:

- update this work order status and closure evidence;
- update the MPI-T1 GC-018 baseline status;
- update the MPI roadmap MPI-T1 row if accepted;
- create the MPI-T1 completion review;
- repair allowed-scope map/return wording, manifests, or packet-shape defects
  required by machine gates before commit.

Forbidden scope:

- no edits to `EXTENSIONS/**` runtime source, readout route/projection, durable
  store, scan registry sources or aggregate, LSC contracts, MKG7 contract
  content, session state, active handoff, root startup routers, public-sync,
  `.github/**`, dependency manifests, web UI routes, or MCP packages;
- no read projection, helper, test, schema, route, registry write, durable
  write, generator run, drift checker run, provider/live proof, dependency
  install, queue, daemon, watcher, wrapper/proxy enforcement, direct
  IDE/shell/git/filesystem interception, arbitrary command execution, or
  EDIT/COMMIT execution;
- no actual CLI/MCP adapter behavior, MCP tool implementation, read-receipt
  enforcement, public catalog update, production/readiness claim, or universal
  governed-coding-control claim;
- no implementation of MPI-T2, MPI-T3, MPI-T4, MKG7, LSC-T5/T7, AAF-T6, AAF-T7,
  CGE-T3, ACE-R1, MLW7, or MLW8.

Risk ceiling: R0 bounded navigation reference.

## Worker Autonomy / No-Question Rule

The worker must repair allowed-scope guard failures and rerun gates without
asking the operator whether to continue.

Escalate to the operator only for:

- scope expansion beyond the navigation map;
- claim-boundary change;
- any runtime, projection, helper, test, schema, route, registry write, or
  durable write requirement;
- provider/live proof, secret or quota use;
- public-sync or push;
- destructive or irreversible actions;
- touching forbidden paths;
- changing risk level or enforcement authority.

## Current Runtime Freshness Verification

| Claim | Freshness evidence | Disposition |
|---|---|---|
| MPI-T1 map path does not already exist | `Get-ChildItem docs/reference -Filter 'CVF_MEMORY_PLANE_MAP.md'` returned no existing file before dispatch authoring | ACCEPT |
| Durable store is present and unwired into a route | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` `write()` exists and fails closed; no route imports it as a write path | ACCEPT |
| LSC has no durable ledger/store implemented | `docs/reference/learning_signal_chain/` holds reference contracts and `governance/compat/run_agent_automation_assist.py` holds a read-only helper readout; no ledger source directory or durable store exists | ACCEPT |
| The provider registry surface is not changed or claimed by MPI-T1 | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and its `PROVIDER_CAPABILITY_REGISTRY` remain untouched; MPI-T1 makes no provider, model-gateway, or provider-registry claim | N/A_WITH_REASON |
| No runtime route, projection, helper, or test is created by MPI-T1 | MPI-T1 creates only the map and worker-return; runtime projection is deferred to MPI-T2 | ACCEPT |
| Provider/live proof is not authorized | Forbidden scope and Claim Boundary in this work order | N/A_WITH_REASON |
| Public-sync is not authorized | Public Export Disposition in this work order | N/A_WITH_REASON |

## Execution Plan

1. Capture `executionBaseHead` with `git rev-parse --short HEAD`.
2. Confirm `git status --short` before editing.
3. Read all Required First Reads.
4. Create the Memory Plane Front-Door Map at the stable path.
5. For each memory-facing surface, record purpose, owner, reader/authenticated
   surface, classification, plane/layer index role, boundary, and runtime
   status with source citations.
6. Separate human-reviewable governed source records from machine-retrieval or
   readout surfaces so GC-023 file-size discipline is not mistaken for Memory
   Plane retrieval design.
7. Record KGR as a structural graph/context index adjacent to Memory Plane, and
   record Graphify/KGR legacy coverage as partial recheck rather than complete
   absorption.
8. Record predecessor absorption alignment for CI1-T11, MLW0, and MLW1-MLW6
   without promoting legacy source code or vocabulary to runtime authority.
9. Record the shared plane invariants and explicitly mark running versus
   contract-only versus parked surfaces.
10. Create the worker-return artifact with actual changed-set status and gate
   evidence.
11. Run required checks.
12. Return `COMPLETE_PENDING_REVIEW` uncommitted, or `BLOCKED_WITH_REASON` with
   exact blocker evidence.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order requirement | Disposition |
|---|---|---|
| MPI-T1 creates a source-verified front-door map of memory-facing surfaces | Required Map Content and Allowed scope | ACCEPT |
| MPI-T1 is navigation only, no runtime edit | Forbidden scope and R0 risk ceiling | ACCEPT |
| Map cites MKG7, GC-051, LSC, GC-022 without re-implementing them | Source Verification Block and no-parallel-core boundary | ACCEPT |
| Map cites CI1-T11, MLW0, and MLW1-MLW6 legacy absorption outputs | Required First Reads and Required Map Content | ACCEPT |
| Map classifies human-reviewable docs separately from fast retrieval/readout surfaces | Required Map Content and Acceptance Criteria | ACCEPT |
| Map classifies KGR as structural graph/context index with partial Graphify/KGR legacy coverage | Required First Reads and Required Map Content | ACCEPT |
| LSC is recorded as bounded signal/reference/readout, not durable memory | Required Map Content LSC row | ACCEPT |
| Running versus contract-only versus parked surfaces are marked truthfully | Required Map Content runtime-status rule | ACCEPT |
| MPI-T2/T3/T4 remain on hold | crossBatchIsolation and Forbidden scope | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| MKG7 closed (bounded pass) and owns the LPF Memory operational contract | `docs/roadmaps/CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md` | lines 5, 145-153 | `Status`; Tranche Plan | MKG7 roadmap | VALUE_SET | ACCEPT |
| Memory readout route is authenticated and returns summary-only invariants | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 136-163, 198-204 | `verifyServiceTokenRequest`; `verifySessionCookie`; `rawMemoryReleased`; `canReinject` | readout route | EXISTS | ACCEPT |
| Readout invariant flags are fixed false on the readout surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 198-204 | `rawMemoryReleased`; `canReinject` | readout route | LITERAL_INVARIANT | ACCEPT |
| RAW sentinel guard rejects serialized raw memory content | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 7, 193-196 | `RAW_MEMORY_CONTENT_MUST_NOT_LEAK` | readout route | LITERAL_INVARIANT | ACCEPT |
| Readout projection strips candidate content and fixes summary-only flags | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | lines 15-54 | `buildMemoryRuntimeReadout`; `rawMemoryReleased`; `canReinject` | readout projection | EXISTS | ACCEPT |
| Durable store write fails closed and is not wired into a route | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 195-211, 98 | `DurableMemoryStore.write`; `MIN_PROVENANCE_SCORE` | durable store | EXISTS | ACCEPT |
| Scan registry is generated-from-source with inherit-before-rescan and Finding Discovery rules | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | lines 51-74, 209-220, 304-315 | Registry Location; Rule 1; Finding Discovery Rule | GC-051 standard | VALUE_SET | ACCEPT |
| Governed file size guard keeps governed files human-reviewable | `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` | Purpose and Rule | human reviewability; split/rotation discipline | GC-023 file size guard | VALUE_SET | ACCEPT |
| CI1-T11 consolidates relevant memory/learning legacy scans | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | Purpose, Source Intake, Tranche Plan, Closure Update | CI1-T11; MLW0; MLW1-MLW6 | CI1-T11 roadmap | EXISTS | ACCEPT |
| MLW0 maps legacy memory/learning vocabulary to current CVF source authority | `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | Purpose and source-verification map | current source mapping for CI1-T11 vocabulary | MLW0 source map | EXISTS | ACCEPT |
| MLW1-MLW6 converted legacy absorption into bounded contracts | `docs/reviews/CVF_MLW1_MLW6_MEMORY_LEARNING_CORE_WORKFLOW_CHAIN_COMPLETION_2026-06-05.md` | closure evidence and authority assets | MLW1-MLW6 bounded artifacts | MLW1-MLW6 completion | EXISTS | ACCEPT |
| KGR pre-review distinguishes Memory Plane from Knowledge Graph Retrieval and records partial Graphify/KGR absorption | `docs/reference/CVF_KGR_ABSORPTION_PREREVIEW_2026-06-01.md` | Why This Is NOT Memory Plane; Prior Absorption History; Blocked Work | Memory Plane vs KGR; partial Graphify re-absorption | KGR pre-review | VALUE_SET | ACCEPT |
| KGR1 bounded LPF local graph retrieval owner exists | `docs/roadmaps/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_ROADMAP_2026-06-01.md`; `docs/reviews/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_LOCAL_REVIEW_2026-06-02.md` | Work Plan; Source Verification; Claim Boundary | `knowledge-graph-store.ts`; `knowledge-graph-builder.ts`; `graph_search` | KGR1 roadmap/review | EXISTS | ACCEPT |
| Graphify registry entry remains a partial coverage input | `docs/corpus-intelligence/registry/entries/legacy-cvf-important-graphify.json` | entry display name and findings | `CVF_Important / Knowledge Base_Graphify` | Corpus Scan Registry entry | EXISTS | ACCEPT |
| LSC-T6 is adapter-contract-only and defines external signal IO without implementing an adapter | `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` | lines 38-50 | `adapterContractOnly` | LSC-T6 contract | LITERAL_INVARIANT | ACCEPT |
| Memory record classes are FULL_RECORD, SUMMARY_RECORD, POINTER_RECORD | `docs/reference/CVF_MEMORY_RECORD_CLASSIFICATION.md` | lines 13-45 | `FULL_RECORD`; `SUMMARY_RECORD`; `POINTER_RECORD` | GC-022 classification | VALUE_SET | ACCEPT |

## New Doc-Only Terms

| Proposed term | Owner in MPI-T1 | Runtime status | Reason |
|---|---|---|---|
| `memoryFacingSurface` | MPI-T1 map | DOC_ONLY_NEW | a CVF surface that stores, indexes, or projects memory-like state |
| `surfaceRuntimeStatus` | MPI-T1 map | DOC_ONLY_NEW | classifies a surface as running, contract-only, or parked |
| `readerSurface` | MPI-T1 map | DOC_ONLY_NEW | the authenticated path through which a reader may access a surface |

These terms are navigation vocabulary only. They must not be presented as
existing runtime fields, schema keys, route names, registry fields, CLI/MCP tool
names, or public API identifiers.

## Required Map Content

The worker must author a POINTER_RECORD map that, for each memory-facing surface,
names purpose, owner, reader/authenticated surface, classification, plane/layer
index role, boundary, and runtime status. The classification values are:

- human-reviewable governed source;
- generated episodic/semantic index;
- bounded runtime readout;
- structural graph/context index;
- contract/spec/parked architecture;
- provider/private memory that is not CVF authority.

- LPF Memory runtime readout (running, authenticated, summary-only);
- LPF durable store (present, fail-closed, unwired);
- Corpus Scan Registry / GC-051 (running, generated-from-source, episodic);
- Learning Signal Chain reference and helper readout (bounded signal-chain
  reference and read-only helper readout only, not a durable ledger or store);
- `docs/` GC-022 memory records (FULL/SUMMARY/POINTER classification);
- governed legacy absorption artifacts (CI1-T11, MLW0, MLW1-MLW6) as
  predecessor authority for memory/learning/RAG/context/continuity/audit
  lessons, not as direct runtime source;
- governed docs and active markdown as human-reviewable source-of-truth records
  controlled by GC-023, not as the fast retrieval layer;
- KGR1 bounded LPF local graph retrieval as a structural graph/context index,
  with Graphify/KGR legacy coverage marked partial recheck rather than fully
  absorbed;
- ephemeral task memory (in-process, lost on exit).

The map must state the shared plane invariants `rawMemoryReleased=false` and
`canReinject=false` on the readout/advisory surface, the RAW sentinel guard, the
fail-closed durable write, and the GC-051 inherit-before-rescan rule. It must
mark which surfaces are running versus contract-only versus parked, and must not
present any parked or contract-only surface as a running capability.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation area | Memory / Knowledge / MEMCON workflow-chain navigation reference |
| Stable reference output | `docs/reference/CVF_MEMORY_PLANE_MAP.md` |
| Worker return output | `docs/reviews/CVF_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_WORKER_RETURN_2026-06-21.md` |
| Generated aggregate impact | N/A with reason: no generated JSON or Markdown aggregate is authorized |
| Runtime impact | N/A with reason: no `EXTENSIONS/**`, route, projection, helper, test, schema, registry, or durable-store path is authorized |
| Legacy absorption impact | reads governed CI1-T11/MLW artifacts as predecessor authority; no fresh legacy source-family enumeration |

## Worker Return Packet Shape Contract

The worker-return artifact must include these required terms and sections:

| Required item | Required value |
|---|---|
| Status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| executionBaseHead | actual `git rev-parse --short HEAD` captured at worker start |
| git status | actual `git status --short` after worker edits |
| Source Inventory | all files read and created |
| Scan Depth Ledger | source-read depth and any unreadable/deferred files |
| Gate Evidence | required command results |
| Changed Files | exact pending changed paths |
| Purpose | worker-return purpose section |
| Scope / Methodology | worker-return scope and methodology section |
| Findings / Position | worker-return findings and final position section |
| Risk / Corrective Action | worker-return risk and corrective action section |
| Claim Boundary | no forbidden runtime/projection/helper/provider/public/adapter/write scope |
| Agent Operation Trace Block | worker role trace |
| Delta Execution Claim Boundary Control Block | N/A rows for execution-control claims |
| Public Export Disposition | `DEFERRED_PRIVATE_ONLY` |
| WORKER_EXPERIENCE_RETRO | structured block or exact N/A token |

Conditional sections must be present or marked `N/A with reason`:

- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package

## Review Gate

Reviewer/closer must reject, repair inside reviewer-owned closure scope, or
return the worker output if:

- any path outside the two Required Deliverables is created or modified by the
  worker;
- the map omits CI1-T11, MLW0, or MLW1-MLW6 predecessor absorption alignment;
- the map treats legacy source code or legacy-only vocabulary as current CVF
  runtime authority;
- the map re-implements MKG7, GC-051, LSC, GC-022, MEMCON, or MLW content
  instead of citing it;
- the map claims runtime projection, adapter behavior, provider/live proof,
  public-sync, durable writes, raw release, reinjection, production readiness,
  or universal governed-coding control;
- required worker-return packet sections or gate evidence are missing.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when the Memory Plane Front-Door Map and
worker-return artifact exist, source inventory covers every required first read,
CI1-T11/MLW alignment is included, and required checks pass or are recorded with
acceptable `N/A with reason` where allowed.

Return `BLOCKED_WITH_REASON` when source verification fails, a required source
cannot be read, a required gate fails outside worker-owned scope, or a necessary
action would exceed Allowed scope.

## Operator Checkpoint

No operator checkpoint is needed for MPI-T1 documentation/reference authoring
inside Allowed scope. Operator checkpoint is required before any MPI-T2/T3/T4
work, runtime/source/test edit, read projection, helper, schema, route,
registry write, durable write, provider/live proof, public-sync, MCP/CLI
adapter behavior, session-sync, parked-lane reopening, risk-level change, or
universal-control claim.

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Front-door map exists | `docs/reference/CVF_MEMORY_PLANE_MAP.md` created as POINTER_RECORD |
| All memory-facing surfaces named | each surface has purpose, owner, reader, classification, plane/layer index role, boundary, runtime status |
| Runtime claims are source-verified | each running claim cites source file/section |
| Legacy absorption is source-verified | map cites CI1-T11, MLW0, and MLW1-MLW6 predecessor artifacts |
| Human-reviewable source is separated from retrieval memory | map cites GC-023 and states retrieval/readout outputs do not replace governed source review |
| KGR structural index status is explicit | map cites KGR pre-review, KGR1 roadmap/review, and Graphify registry entry; no complete KGR legacy absorption claim |
| No parallel core | map cites MKG7/GC-051/LSC/GC-022, does not re-implement them |
| LSC stated truthfully | LSC recorded as bounded signal/reference/readout, not durable memory |
| Runtime status truthful | running versus contract-only versus parked marked correctly |
| Required checks pass | worker-return fast gate passes or blocks with reason |
| Worker does not commit | changed set remains uncommitted for reviewer |
| Forbidden scope untouched | no runtime/projection/helper/route/registry/durable/public path changed |

## Closure Checklist

Reviewer/closer closure evidence must resolve these items:

- Required deliverables exist.
- No forbidden paths changed.
- Source Verification claims remain current.
- Map cites and does not re-implement MKG7/GC-051/LSC/GC-022.
- Map separates human-reviewable governed source from machine-retrieval/readout
  surfaces and cites GC-023.
- Map classifies KGR as structural graph/context index and preserves the
  Graphify/KGR partial-recheck gap.
- Map cites CI1-T11/MLW0/MLW1-MLW6 absorption outputs without promoting legacy
  source to runtime authority.
- LSC remains bounded signal/reference/readout, not durable memory.
- Running versus contract-only versus parked surfaces are marked truthfully.
- Worker-return packet includes required sections and token.
- Reviewer-fast or stricter gate passes.
- Commit ownership remains reviewer/closer only.
- Session-sync is performed only if mode or next-move surfaces change.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_WO_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_2026-06-21.md` | `Status: CLOSED_PASS_BOUNDED` after reviewer update | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_2026-06-21.md` | `Status: CLOSED_PASS_BOUNDED` after reviewer update | PASS |
| Worker return | `docs/reviews/CVF_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_WORKER_RETURN_2026-06-21.md` | `Status: COMPLETE_PENDING_REVIEW`; accepted with reviewer correction | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_COMPLETION_2026-06-21.md` | reviewer-owned `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | roadmap top status and MPI-T1 row updated to closure state | PASS |
| Reference map | `docs/reference/CVF_MEMORY_PLANE_MAP.md` | map exists; stale BLI-01 wording corrected by reviewer | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: MPI-T1 does not authorize generated registry mutation; map records registry as an existing surface only | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: MPI-T1 does not authorize generated registry Markdown mutation; no registry companion update is part of this tranche | BLOCKED with reason |
| External evidence digest | N/A with reason: no external benchmark/provider/live digest created | reference map closure only | N/A with reason |
| System loop interlock | N/A with reason: no runtime/source interlock changed by dispatch | no runtime/source mutation by dispatch | N/A with reason |
| Session continuity | active session front-door/state/handoff after material commit | N/A with reason: no session-sync surfaces are changed in this material closure batch; operator next move is recorded in completion review and chat handoff | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Work order closed | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 baseline closed | `docs/baselines/CVF_GC018_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_2026-06-21.md` `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return accepted | `Status: COMPLETE_PENDING_REVIEW`; reviewer correction applied | PASS |
| Reference map created | `docs/reference/CVF_MEMORY_PLANE_MAP.md` exists | PASS |
| Runtime/source paths untouched | no `EXTENSIONS/**` path changed by MPI-T1 | PASS |
| Registry mutation absent by design | registry rows are `BLOCKED with reason` because MPI-T1 did not authorize mutation | PASS |
| Public export private-only | Public Export Disposition `DEFERRED_PRIVATE_ONLY` | PASS |

## Corpus Completeness And Report Integrity

- Corpus task class: NOT_APPLICABLE_WITH_REASON - MPI-T1 dispatch is a bounded
  navigation-map work order, not a corpus enumeration or legacy scan.
- Corpus root: NOT_APPLICABLE_WITH_REASON - no corpus root is assigned.
- Snapshot time: NOT_APPLICABLE_WITH_REASON - no corpus snapshot is taken.
- Enumeration command: filesystem-backed direct file reads listed in Source
  Verification Block; no corpus enumeration command is authorized.
- Manifest artifact or inline manifest: inline Source Verification Block above.
- Manifest hash: NOT_APPLICABLE_WITH_REASON - no corpus manifest hash is created.
- Processing ledger artifact or inline ledger: inline Source Verification Block
  above.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline Source Verification Block; ledger_terminal=READ for named source rows; exclusions=corpus enumeration and fresh legacy source-family enumeration out of scope; governed CI1-T11/MLW absorption artifacts are included; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: corpus scan, fresh legacy source-family enumeration,
  public-sync copy, runtime/provider/live proof, and CLI/MCP adapter.
- Unreadable or unsupported files: 0.
- Aggregation check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate is created.
- Drift check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate or generated
  corpus registry is changed.
- Output traceability: Required Deliverables and Source Verification Block define
  all worker output traceability.
- Adversarial verification: reviewer/closer must run reviewer-fast or stricter
  applicable gate before acceptance.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch for the Memory Plane front-door map. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MPI-T1 Memory Plane Front-Door Map work order only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | documentation/reference navigation map only |
| interceptionBoundary | no wrapper/proxy enforcement, direct IDE/shell/git/filesystem/provider interception, arbitrary command execution, or EDIT/COMMIT execution claim |
| claimLanguage | dispatch, navigation, source citation, and boundary wording only |
| forbiddenExpansion | no runtime projection, helper, test, schema, route, registry write, durable write, provider/live, public-sync, CLI/MCP adapter behavior, queue/daemon, watcher, readiness, or universal governed-coding-control claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local workspace |
| Session or invocation | MPI-T1 dispatch authoring, 2026-06-21 |
| Working directory | repository root |
| Command or tool surface | startup reads, source verification reads, apply_patch edits, dispatch gates |
| Target paths | `docs/baselines/CVF_GC018_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_2026-06-21.md`; this work order |
| Allowed scope source | operator selection of MPI lane and MPI-T1 first |
| Before status evidence | HEAD `acb2b980`; dispatch base worktree clean; MPI roadmap and Codex rebuttal were post-base untracked operator-review intake before MPI-T1 dispatch authoring |
| After status evidence | dispatch packet created for worker |
| Diff evidence | pre-dispatch gates required before commit |
| Approval boundary | dispatch only; no worker execution, runtime mutation, provider/live, public-sync, or adapter behavior |
| Claim boundary | worker dispatch packet only |
| Agent type | dispatcher |
| Invocation ID | `mpi-t1-memory-plane-front-door-map-dispatch-2026-06-21` |
| Expected manifest | this work order and paired GC-018 baseline |
| Actual changed set | checked by dispatch gates before commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch packet |

## Claim Boundary

This work order dispatches only the MPI-T1 Memory Plane Front-Door Map
navigation reference and worker-return evidence. It does not authorize a read
projection, helper, test, schema, route, registry write, durable write, runtime
mutation, provider/live proof, actual CLI/MCP adapter behavior, public-sync,
direct interception, wrapper/proxy enforcement, queue/daemon, watcher,
readiness, or universal governed-coding control.
