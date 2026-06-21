# CVF MPI Memory Plane Integration Roadmap

Memory class: FULL_RECORD

Status: MPI_T2_CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-21

## Purpose

MKG7 operationalized the LPF Memory runtime kernel as a bounded, fail-closed,
advisory surface (`CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md`,
`CLOSED_PASS_BOUNDED`). MPI does not reopen, replace, or re-implement any MKG7
tranche. MPI closes the three integration gaps that MKG7 left untouched because
MKG7 was scoped to the LPF runtime plane alone:

1. CVF has four memory-facing surfaces (LPF Memory runtime, Corpus Scan
   Registry, `docs/` GC-022 records, Learning Signal Chain reference/readout)
   with no single source-verified front-door map relating their purpose, owner,
   reader, and boundary. This forces every agent to rediscover the plane layout
   from scratch.
2. The Corpus Scan Registry (GC-051) is the largest durable cross-session
   episodic-memory surface actually running (file-count enumeration, manifest
   hash, findings, negative-search), but it is not reachable through the bounded
   Memory readout surface. An internal agent asking "what do we already know
   about domain X" cannot get scan findings through the Memory plane.
3. LSC-T6 defined how an external CLI/MCP agent **writes** a signal into CVF. No
   contract defines how an external CLI/MCP agent **reads** a bounded
   summary-only memory readout out of CVF. This is the missing half of the
   external-agent core value.

MPI is integration and federation of already-built surfaces. It adds no vector
store, no embedding index, no new tier beyond the existing bounded kernel, no
raw release, and no reinjection.

Legacy absorption correction: MPI must also inherit the already-governed
CI1-T11/MLW memory-learning absorption chain. The first draft mapped current
runtime and reference surfaces, but did not make the legacy alignment explicit
enough for dispatch. MPI-T1 must therefore cite CI1-T11, MLW0, and the bounded
MLW1-MLW6 contracts as predecessor absorption authority while still treating
legacy code or vocabulary as non-authoritative until mapped through current CVF
source.

Classification correction: CVF needs two different things that should not be
collapsed into one "memory" label. Governed docs remain human-reviewable source
of truth and stay under line-count/rotation controls. The Memory Plane is a
bounded retrieval/readout layer that may behave like a vector-DB-style fast
index in future tranches, but only as summary/pointer access back to governed
sources. MPI-T1 must name this distinction before any runtime projection or
external-agent read contract is opened.

Index correction: index artifacts are not only for folders or corpus roots.
CVF also needs plane/layer indexes that classify owner surfaces, retrieval
surfaces, structural graph surfaces, and external-agent access surfaces. Before
MPI-T1 creates the Memory Plane front-door map, MPI-T0 must recheck the
memory/KGR/graph/context legacy folders and author the INDEX classification
standard. MPI-T1 then consumes that result as the plane/layer index,
not merely a document table of contents. This keeps KGR visible as a structural
graph/context index adjacent to the Memory Plane while recording any
Graphify/KGR legacy gap that remains after the bounded recheck.

## Relationship To MKG7 (No Parallel Core)

| MKG7 delivered (CLOSED) | MPI relationship |
| --- | --- |
| Memory Plane Operational Contract (`docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md`) | MPI cites it as the authority for the LPF readout surface; MPI does not redefine it. |
| Readout-eligibility lifecycle | MPI reuses; adds no lifecycle state. |
| `/api/execute` advisory wire-in | MPI does not change `/api/execute`. |
| Retrieval attribution | MPI reuses attribution fields for the federated read; adds none. |
| Durable write readiness (fail-closed, unwired) | MPI does not wire a write path and does not change write semantics. |
| Derived-graph boundary | MPI inherits the rebuildable-derived-view rule for the scan-registry projection. |

MPI authority is integration only. Any tranche that would change LPF Memory
runtime semantics, durable write semantics, or readout invariants is out of
scope and belongs to a separate MKG-series GC-018.

## Authorization / Decision

This roadmap is at an operator-selection checkpoint. Future tranches require
their own GC-018 and source-verified work order before implementation.
Operator direction on 2026-06-21: Memory Plane
integration is important and should be implemented, but the sequence must start
with the safest bounded tranche and must not jump directly into runtime,
provider/live, public-sync, or actual CLI/MCP adapter behavior.

## Current State (Source-Verified)

| Surface | Verified path / symbol | Boundary status |
| --- | --- | --- |
| LPF Memory readout route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | authenticated (service-token OR session), `rawMemoryReleased:false`, `canReinject:false`, RAW sentinel `RAW_MEMORY_CONTENT_MUST_NOT_LEAK` |
| Memory readout projection | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | strips candidate `content`, summary-only |
| Memory workflow chain | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | local deterministic chain, status `packaged|denied|deferred` |
| Tier lifecycle policy | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` | tier states working/episodic/semantic/procedural/expired/disputed/forgotten |
| Retrieval policy | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | `evaluateRetrievalRequest`, `MemoryRetrievalResult` |
| Durable store (unwired, fail-closed) | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | `write()` denies unless `actorAuthorized && policyDecision==='allow'`, provenance floor 0.7 |
| Corpus Scan Registry generated aggregate | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated front door; 114 per-entry sources under `docs/corpus-intelligence/registry/entries/` |
| Corpus Scan Registry standard | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | GC-051; Finding Discovery Rule, negative-search, drift check |
| Governed file reviewability guard | `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` | GC-023; keeps governed files reviewable by humans through split/rotation discipline |
| Legacy memory/learning absorption roadmap | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | absorbs CI1-T11 memory, learning, RAG/context, execution continuity, and audit feedback scans; does not authorize direct legacy runtime adoption |
| Legacy-to-current source map | `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | maps CI1-T11 legacy vocabulary to current LPF/cvf-web source authority before implementation |
| Bounded MLW core contracts | `docs/reference/CVF_MLW1_GOVERNED_MEMORY_OPERATION_RECEIPT_MODEL_2026-06-05.md`; `docs/reference/CVF_MLW2_DETERMINISTIC_CONTEXT_BUNDLE_WORKFLOW_2026-06-05.md`; `docs/reference/CVF_MLW3_EVIDENCE_TO_TRUTH_LEARNING_SIGNAL_PIPELINE_2026-06-05.md`; `docs/reference/CVF_MLW4_EXECUTION_CONTINUITY_HANDOFF_GATE_2026-06-05.md`; `docs/reference/CVF_MLW5_AUDIT_FEEDBACK_VALIDATION_LANE_2026-06-05.md`; `docs/reference/CVF_MLW6_SIMULATION_FAILURE_GATE_2026-06-05.md` | bounded contract/reference artifacts derived from legacy absorption; no raw reinjection, direct policy mutation, or parallel runtime |
| KGR pre-review and Graphify legacy gap | `docs/reference/CVF_KGR_ABSORPTION_PREREVIEW_2026-06-01.md`; `docs/corpus-intelligence/registry/entries/legacy-cvf-important-graphify.json` | distinguishes Memory Plane from KGR; records Graphify/KGR legacy as partially absorbed / partial recheck, not fully deep reabsorbed |
| KGR1 bounded LPF graph retrieval | `docs/roadmaps/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_ROADMAP_2026-06-01.md`; `docs/reviews/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_LOCAL_REVIEW_2026-06-02.md` | closed bounded local KGR schema/store/builder/`graph_search`; no vector DB, web-route graph integration, durable graph persistence, production readiness, or public release |
| LSC external signal contract (write side) | `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` | `adapterContractOnly=true`; defines external signal IO, no adapter implementation |
| LSC reference/helper-readout surface | `docs/reference/learning_signal_chain/`; `governance/compat/run_agent_automation_assist.py` | bounded signal-chain reference and read-only helper readout; no ledger store, source directory, generator, drift checker, durable store, or runtime Learning Plane mutation |
| Memory record classification (GC-022) | `docs/reference/CVF_MEMORY_RECORD_CLASSIFICATION.md` | FULL/SUMMARY/POINTER class model |

Each tranche work order must produce a finer Source Verification Block with
exact line/symbol evidence before implementation. Roadmap-level ACCEPT rows must
not be treated as a substitute for per-work-order verification.

## Memory Plane Classification

MPI uses this classification to prevent the line-limit/human-reviewability goal
from being confused with machine retrieval needs:

| Class | Purpose | Current owner examples | Retrieval posture | Boundary |
| --- | --- | --- | --- | --- |
| Human-reviewable governed source | canonical authority humans can audit | roadmaps, work orders, reviews, references, GC-022 records | read directly by agents only when needed; kept compact by GC-023 | line limits and rotation protect reviewability; not optimized as the fast memory surface |
| Generated episodic/semantic index | cross-session scan memory over governed sources | Corpus Scan Registry / GC-051 | fastest currently running registry-like memory surface | generated from per-entry sources; not a write authority; no raw source replacement |
| Structural graph/context index | plane/layer structure and codebase relationship retrieval | KGR1 LPF KGR store/builder/retrieval; Graphify/KGR legacy as predecessor input | local `graph_search` style context selection, not Memory durable storage | current KGR is bounded local; legacy Graphify/KGR corpus remains `PARTIAL_RECHECK_REQUIRED`; no graph persistence or web-route integration claim |
| Bounded runtime readout | authenticated summary-only memory access | LPF Memory readout route and projection | current summary-only readout surface | `rawMemoryReleased=false`, `canReinject=false`, RAW sentinel |
| Contract/spec/parked memory architecture | designed but not fully wired memory concepts | LPF `.contract.ts` families; KGR/Graph Memory legacy specs; MLW contracts | design/input for future work orders only | no direct runtime claim unless source-verified and separately authorized |
| Provider/private agent memory | local execution aid | Claude/Codex/provider memories | not CVF authority | must be re-verified against governed CVF sources before use |

MPI-T1 must produce a map that labels every memory-facing surface with both its
authority/reviewability class and its retrieval/readout class. MPI-T2/T3/T4 may
later improve fast access, but they must preserve pointer/summary discipline
and must not make the retrieval layer a substitute for governed source review.

## Plane/Layer Indexing Principle

MPI treats "index" as a governance and retrieval primitive across plane/layer
boundaries, not merely a filesystem inventory:

| Index type | Owner examples | MPI-T1 treatment | Boundary |
| --- | --- | --- | --- |
| Corpus/file-family index | GC-051 registry and per-entry sources | cite as generated episodic memory | no hand-editing aggregate; no source replacement |
| Plane/layer owner index | MPI-T1 Memory Plane map | create a pointer record that maps surfaces, owners, readers, runtime state, and gaps | navigation only; no runtime mutation |
| Structural graph/context index | KGR1 and Graphify/KGR predecessor artifacts | classify as adjacent structural retrieval layer and record partial legacy coverage | no durable graph persistence, vector DB, or web-route graph integration claim |
| Runtime readout/projection index | MKG7 readout; future MPI-T2 projection | requires separate GC-018 after T1 | summary-only; no raw release or reinjection |
| External-agent access index | LSC-T6 write-side signal contract; future MPI-T3 read contract | requires separate GC-018 after T1 | contract-only unless separately implemented |

## INDEX Standard

MPI-T0 is required before MPI-T1 because INDEX is now a forward-only
classification standard, not a local label. The INDEX standard must define how
CVF classifies:

- corpus/file-family indexes;
- plane/layer owner indexes;
- source-of-truth/human-reviewability indexes;
- runtime readout/projection indexes;
- structural graph/context indexes;
- external-agent access indexes;
- provider/private memory indexes that are not CVF authority.

The INDEX standard is forward-only. It does not rewrite historical CVF
artifacts, but future agents must apply it when authoring, reviewing, or
closing classification work after MPI-T0. It must not create runtime routing,
vector DB, graph persistence, direct legacy promotion, or public-facing claims.

Machine enforcement is a separate follow-up. MPI-T0 authors the standard and
uses the legacy recheck as the first governed INDEX use case. After MPI-T0
closure, a small checker tranche should promote INDEX from packet-bound policy
to governance-enforced classification discipline before broad MPI continuation.
That checker tranche must have its own GC-018 and work order, and must not be
silently merged into MPI-T0 worker scope.

## Scope

In scope:

- a source-verified Memory Plane front-door map relating the memory-facing
  surfaces by purpose, owner, reader, and boundary (reference /
  POINTER_RECORD);
- a prerequisite INDEX legacy memory/graph recheck that verifies Claude's
  memory-plane inventory, raw legacy KGR/Graphify/code-review-graph evidence,
  and LPF contract/runtime split before MPI-T1 dispatch;
- a legacy absorption alignment section that routes CI1-T11, MLW0, and
  MLW1-MLW6 into the map as predecessor authority, not as direct runtime source;
- a classification axis that separates human-reviewable governed records from
  machine-retrieval/readout surfaces;
- a plane/layer index axis that makes structural graph/context surfaces such as
  KGR visible without treating them as Memory durable storage;
- a read-only projection that exposes Corpus Scan Registry findings through the
  existing bounded Memory readout surface, reusing the existing summary-only and
  RAW-sentinel invariants;
- an external-agent read contract that mirrors LSC-T6's write-side boundary for
  the read direction, summary-only, over the existing authenticated route;
- a bounded helper/test fast-path for the federated read, advisory and
  non-mutating;
- local deterministic route, TypeScript, and governance gates only for later
  runtime-bearing tranches after separate operator selection.

Out of scope:

- raw Memory content release or prompt reinjection;
- any change to LPF Memory runtime, durable write semantics, or readout
  invariants delivered by MKG7;
- new memory tier, vector store, embedding index, or graph persistence;
- actual CLI/MCP adapter / MCP tool / shell-bridge implementation;
- provider/live calls, public-sync, hosted or production readiness;
- editing frozen baseline layers or `EXTENSIONS/**` runtime in MPI-T1;
- editing `EXTENSIONS/**` runtime in any later MPI tranche unless a separate
  GC-018 and source-verified work order explicitly release that bounded scope;
- reopening MKG7, LSC-T5/T7, AAF-T6/T7, CGE-T3, or ACE-R1.

## Non-Goals

- do not claim MPI makes Memory production-ready or improves model quality
  without separate live proof;
- do not convert the federated scan-registry read into write authority over the
  registry;
- do not let the scan-registry projection become a source of truth that
  overrules the registry per-entry sources (it stays a rebuildable derived view
  per the MKG7 derived-graph boundary);
- do not treat the external read contract as authorization to build an adapter;
  it is a contract boundary only, matching LSC-T6 `adapterContractOnly=true`.

## External Knowledge Intake Routing

Chain map: `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | REVIEW_AND_CLASSIFY_BEFORE_ABSORPTION |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; active session next-move boundary |
| Owner surface | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` |
| Disposition | ADAPT_AS_OPERATOR_SELECTION_ROADMAP |
| Claim boundary | Roadmap candidate only; no implementation, runtime route change, provider/live proof, public-sync, adapter build, or work-order dispatch |

## Current Runtime Freshness Verification

| Claim | Freshness check | Disposition |
| --- | --- | --- |
| Memory readout route exists and is authenticated | Source path named in Current State; per-work-order line verification still required | ACCEPT_FOR_ROADMAP |
| Summary-only flags exist on current route/readout paths | Source path named in Current State; per-work-order line verification still required | ACCEPT_FOR_ROADMAP |
| Corpus Scan Registry is generated and per-entry sourced | GC-051 standard and generated aggregate named in Current State | ACCEPT_FOR_ROADMAP |
| LSC is not a durable ledger/store | LSC closures and active handoff forbid ledger/source/generator/durable-store expansion | REJECT_DURABLE_LSC_WORDING |
| Legacy memory/learning absorption exists | CI1-T11, MLW0, and MLW1-MLW6 artifacts are named in Current State and Source Verification | ACCEPT_FOR_MPI_T1_ALIGNMENT |
| Human-reviewable docs and fast retrieval have different roles | GC-023 and Memory Plane Classification distinguish source-of-truth reviewability from bounded retrieval/readout | ACCEPT_CLASSIFICATION_REQUIRED |
| KGR Graphify legacy coverage is partial | KGR pre-review and corpus registry show current KGR owner exists but Graphify/KGR legacy remains partial recheck, not complete absorption | ACCEPT_WITH_GAP |
| MPI-T1 has no runtime edit requirement | Workstream says POINTER_RECORD navigation only | ACCEPT_FOR_FIRST_TRANCHE |
| MPI-T2/T3/T4 runtime or adapter-adjacent claims | Not authorized by this roadmap alone | PARKED_FOR_SEPARATE_GC018 |

## Design Control Gate

| Control | Required result |
| --- | --- |
| First tranche safety | Start with MPI-T0 INDEX Legacy Memory/Graph Recheck before MPI-T1 |
| INDEX enforcement staging | MPI-T0 authors the standard only; open a separate checker tranche after MPI-T0 before broad MPI continuation |
| No parallel core | Do not re-implement MKG7, GC-051, LSC, or GC-022 |
| Runtime boundary | No `EXTENSIONS/**` runtime edit in MPI-T1 |
| Legacy absorption gate | MPI-T1 must cite CI1-T11, MLW0, and MLW1-MLW6 predecessor artifacts before accepting a Memory Plane map |
| Classification gate | MPI-T1 must classify surfaces as governed source, generated index, runtime readout, contract/spec, or provider/private memory |
| Plane/layer index gate | MPI-T1 must classify KGR as structural graph/context index adjacent to Memory Plane and record its partial legacy coverage |
| LSC boundary | LSC remains signal/reference/readout only until separate ledger/durable-store authorization |
| Adapter boundary | External read contract does not implement CLI/MCP adapter, MCP tool, or shell bridge |
| Public/live boundary | No provider/live, public-sync, hosted readiness, production readiness, or model-quality claim |

## Tranche Plan

| Tranche | Name | Goal | Primary outputs | Status |
| --- | --- | --- | --- | --- |
| MPI-T0 | INDEX Legacy Memory/Graph Recheck | Re-scan and classify memory/KGR/graph/context legacy folders plus LPF contract/runtime split; verify Claude's readout; author INDEX classification standard | legacy recheck report, INDEX standard, T1 dependency-release evidence | CLOSED_PASS_BOUNDED |
| INDEX-T1 | Forward-Only INDEX Classification Checker | Promote the MPI-T0 INDEX standard from packet-bound policy to machine-enforced governance for future classification artifacts and agent handoffs | checker, focused tests, guard orientation/template references, hook integration evidence | CLOSED_PASS_BOUNDED |
| MPI-T1 | Memory Plane Front-Door Map | Source-verified map of the memory-facing surfaces: purpose, owner, reader, boundary, what is runtime vs parked | reference POINTER_RECORD map | CLOSED_PASS_BOUNDED |
| MPI-T2 | Scan Registry Episodic Read Projection | Expose GC-051 findings as a read-only summary-only projection consumable through the existing Memory readout surface | projection helper, focused tests, contract section | CLOSED_PASS_BOUNDED |
| MPI-T3 | External Agent Memory Read Contract | Define the summary-only read-direction contract for external CLI/MCP agents, mirroring LSC-T6 write-side boundary | reference contract, `adapterContractOnly=true` | PARKED_AFTER_T1 |
| MPI-T4 | Federated Read Helper Fast-Path | Optional bounded read-only helper/test that returns the federated advisory read deterministically, no mutation | helper, focused tests | OPTIONAL_PARKED |

MPI must not be dispatched as one broad assignment. Each tranche gets its own
GC-018 and work order.

## Work Plan

| Step | Action | Exit condition |
| --- | --- | --- |
| 1 | Operator selects MPI-T0 as prerequisite | explicit operator selection |
| 2 | Dispatcher creates GC-018 and work order for MPI-T0 only | source-verified work order passes pre-dispatch gates |
| 3 | Worker verifies Claude's LPF/KGR/legacy memory readout and creates INDEX outputs | completed; worker returned `COMPLETE_PENDING_REVIEW`, uncommitted |
| 4 | Reviewer validates MPI-T0 source fidelity and boundary | completed; reviewer correction applied and gates pass |
| 5 | Dispatcher opens a small INDEX-T1 checker tranche if operator confirms machine enforcement | completed; INDEX-T1 dispatched at `64516525` and closed after worker return |
| 6 | Dispatcher releases MPI-T1 only after MPI-T0 closure, and after INDEX-T1 if mandatory enforcement is selected before continuation | completed for MPI-T1 by `CVF_MPI_T0_INDEX_LEGACY_MEMORY_GRAPH_RECHECK_COMPLETION_2026-06-21.md`; INDEX-T1 is now closed |
| 7 | Worker creates the Memory Plane Front-Door Map as a reference POINTER_RECORD | completed; worker returned `COMPLETE_PENDING_REVIEW`, reviewer correction applied |
| 8 | Operator decides whether MPI-T2 or MPI-T3 should follow | MPI-T2 selected, implemented, and closed; MPI-T3 remains parked |
| 9 | MPI-T4 remains optional | only opened if T2/T3 closure shows a real helper need |

## Workstream Details

### MPI-T0 INDEX Legacy Memory/Graph Recheck

Create a bounded recheck report and INDEX classification standard.
The worker must:

- enumerate the assigned legacy memory/KGR/graph/context source folders;
- verify Claude's claim that LPF has many contract/spec-like pipeline files and
  separate running runtime/readout surfaces;
- inspect KGR/Graphify/code-review-graph raw legacy source only for
  classification and gap extraction;
- distinguish already absorbed current owners from unabsorbed or partially
  absorbed legacy concepts;
- record terminal dispositions per source or family: `ACCEPT_AS_INDEX_INPUT`,
  `ALREADY_ABSORBED_CURRENT_OWNER`, `PARTIAL_RECHECK_REQUIRED`,
  `DEFER_TO_SEPARATE_GC018`, `REJECT_DIRECT_RUNTIME_PROMOTION`, or
  `BLOCKED_UNREADABLE`;
- author the INDEX classification standard for forward-only CVF classification
  work.

MPI-T0 must not implement runtime, graph persistence, vector DB, KGR CLI,
external dependencies, provider/live proof, public-sync, or Memory readout
changes. MPI-T0 must not implement the INDEX checker. R0
documentation/reference recheck only.

### INDEX-T1 Forward-Only INDEX Classification Checker

Create the small machine-enforcement tranche after MPI-T0 closure if the
operator selects mandatory INDEX governance. This tranche should:

- implement a deterministic checker for future classification artifacts that
  claim, dispatch, review, or close INDEX-governed work;
- add focused tests for missing INDEX blocks, forbidden retroactive rewrites,
  ambiguous classification dispositions, and misplaced runtime claims;
- wire the checker into the narrowest applicable governance hook or autorun
  surface;
- update the guard orientation index and affected templates so internal and
  external agents know when INDEX applies.

INDEX-T1 must not rescan legacy, mutate Memory runtime, implement vector or
graph storage, build CLI/MCP adapters, run provider/live proof, or change
public-sync state unless separately authorized.

### MPI-T1 Memory Plane Front-Door Map

Create a POINTER_RECORD reference (for example
`docs/reference/CVF_MEMORY_PLANE_MAP.md`) that, citing current source, names for
each memory-facing surface:

- purpose (what kind of memory: working / episodic / semantic / signal /
  navigation);
- classification (human-reviewable governed source, generated index, runtime
  readout, structural graph/context index, contract/spec/parked, or
  provider/private memory);
- plane/layer index role (what this surface helps classify or retrieve);
- predecessor absorption owner, when applicable (CI1-T11, MLW0, MLW1-MLW6);
- owner file or registry;
- who may read it and through which authenticated surface;
- what boundary applies (`rawMemoryReleased:false`, `canReinject:false`,
  summary-only, fail-closed write, GC-051 inherit-before-rescan);
- runtime status (running vs contract-only vs parked).

The map is navigation only. It must not duplicate the MKG7 operational contract
content; it cites it. R0.

### MPI-T2 Scan Registry Episodic Read Projection

Add a deterministic, read-only projection that maps Corpus Scan Registry
findings into the existing Memory readout candidate/summary shape, so an
internal agent's "what do we know about domain X" query can surface prior scan
findings as advisory summary candidates.

Required constraints:

- reuse the existing summary-only projection invariants (`rawMemoryReleased:false`,
  `canReinject:false`, RAW sentinel);
- the projection is a rebuildable derived view of the registry per-entry
  sources, never a write path into the registry;
- reuse the GC-051 Finding Discovery Rule for domain-keyword matching; do not
  invent a parallel finding model;
- no provider call; deterministic and testable.

R1/R2 bounded read projection plus focused tests.

### MPI-T3 External Agent Memory Read Contract

Define the read-direction counterpart to LSC-T6. LSC-T6 specifies how an
external CLI/MCP agent submits a signal; MPI-T3 specifies how an external
CLI/MCP agent receives a bounded summary-only memory readout:

- which fields the external read request may carry (mapped to the existing
  `MemoryRuntimeReadoutBody` schema, not a parallel schema);
- the authenticated surface it must use (existing service-token OR session
  route);
- the summary-only response boundary it inherits (`rawMemoryReleased:false`,
  `canReinject:false`, no raw candidate content);
- that it authorizes no adapter, MCP tool, shell bridge, or runtime execution:
  `adapterContractOnly=true`, matching LSC-T6.

This is the tranche that connects the Memory plane to the external-agent core
value. R1 reference contract.

### MPI-T4 Federated Read Helper Fast-Path

Optional bounded helper that returns a federated advisory read (LPF readout
summary plus scan-registry finding summary) in one deterministic, read-only
output, with focused tests proving:

- no mutation of any source surface;
- no raw content and no reinjection flag flip;
- registry projection stays a derived view;
- the helper degrades to advisory and never blocks closure.

If source verification or file-size guards make a helper edit unsafe, MPI-T4 is
recorded `N/A_WITH_REASON` and the contract from MPI-T2/T3 stands alone. R1/R2.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| No parallel core | No MKG7, LSC, or GC-051 surface is re-implemented; MPI only maps, projects, and federates existing surfaces |
| Legacy absorption integrated | MPI-T1 map cites CI1-T11, MLW0, and MLW1-MLW6 as predecessor absorption authority and rejects direct legacy-runtime promotion |
| Classification clarity | MPI-T1 map separates human-reviewable governed records from machine-retrieval/readout surfaces and names GC-023 as the file-reviewability control |
| KGR gap is visible | MPI-T1 map records KGR1 bounded current owner surfaces and marks Graphify/KGR legacy coverage as partial recheck, not fully absorbed |
| Front-door clarity | The map names purpose, owner, reader, boundary, and runtime status for all memory-facing surfaces with source citations |
| Episodic read projection | MPI-T2 helper implemented; scan-registry findings can be projected into existing summary-only readout candidates by caller-supplied parsed entries; route-side automatic data loading remains parked |
| External read contract | PARKED for MPI-T3; a summary-only read contract may mirror LSC-T6 boundary only after separate authorization |
| Safety invariants | `rawMemoryReleased=false` and `canReinject=false` preserved on every MPI surface; RAW sentinel unbroken |
| No write authority | MPI adds no write path to the registry, durable store, or LPF runtime |
| Maintainability | near-threshold source files are split or reduced before growth |
| Governance | work-order dispatch, autorun, structural, public-export, finding-learning, and file-size gates pass per tranche |

## Verification/Evidence

| Verification item | Required command or evidence |
| --- | --- |
| Roadmap review | Codex rebuttal artifact and reviewer-fast result |
| MPI-T0 dispatch | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD` |
| MPI-T1 dispatch | after MPI-T0 closure only; `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD` |
| MPI-T1 worker return | `python governance/compat/run_worker_return_fast_gate.py` |
| MPI-T1 closure | reviewer-fast, commit steward reviewer-return, pre-commit hook |
| Generated state | N/A for roadmap only; required only if session next-move changes |
| Runtime route tests | MPI-T2 focused route/readout/helper tests passed; future route behavior changes still require separate authorization |
| Live proof | N/A unless a later tranche makes provider/live/release governance claims |

## Source Verification Block (Roadmap-Level)

| Claim | Verified path or symbol | Source fact type |
| --- | --- | --- |
| MKG7 closed and owns the LPF operational contract | `docs/roadmaps/CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md` (`Status: CLOSED_PASS_BOUNDED`) | EXISTS |
| Readout route is authenticated and summary-only | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` (`rawMemoryReleased:false`, `canReinject:false`, RAW sentinel) | EXISTS |
| Readout projection strips raw content | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | EXISTS |
| Durable store fails closed and is unwired | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` (`write()` deny branch, `MIN_PROVENANCE_SCORE=0.7`) | EXISTS |
| Scan registry is a generated aggregate over per-entry sources | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/` | EXISTS |
| Scan registry defines Finding Discovery Rule and inherit-before-rescan | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` (Rule 1, Finding Discovery Rule) | VALUE_SET |
| GC-023 keeps governed files reviewable by humans | `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` (`## Purpose`; `## Rule`) | VALUE_SET |
| CI1-T11 consolidated legacy absorption exists | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | EXISTS |
| MLW0 maps legacy memory/learning vocabulary to current source authority | `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | EXISTS |
| MLW1-MLW6 closed bounded contract chain exists | `docs/reviews/CVF_MLW1_MLW6_MEMORY_LEARNING_CORE_WORKFLOW_CHAIN_COMPLETION_2026-06-05.md` | EXISTS |
| KGR pre-review distinguishes Memory Plane from KGR and records partial Graphify/KGR absorption | `docs/reference/CVF_KGR_ABSORPTION_PREREVIEW_2026-06-01.md` | VALUE_SET |
| KGR1 bounded current owner exists | `docs/roadmaps/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_ROADMAP_2026-06-01.md`; `docs/reviews/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_LOCAL_REVIEW_2026-06-02.md` | EXISTS |
| Graphify/KGR corpus registry entry remains partial coverage input | `docs/corpus-intelligence/registry/entries/legacy-cvf-important-graphify.json` | EXISTS |
| LSC-T6 defines external write-side signal IO only, adapter-contract-only | `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` (`adapterContractOnly=true`) | VALUE_SET |
| Memory record classes FULL/SUMMARY/POINTER | `docs/reference/CVF_MEMORY_RECORD_CLASSIFICATION.md` | VALUE_SET |
| LSC remains signal/reference/readout only | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V20_2026-06-19.md` | VALUE_SET |

## Required Work Orders

- `CVF_WO_MPI_T0_INDEX_LEGACY_MEMORY_GRAPH_RECHECK_2026-06-21.md`;
- `CVF_WO_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_2026-06-21.md`;
- `CVF_WO_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_2026-06-21.md`;
- `CVF_WO_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_2026-06-22.md`;
- `CVF_WO_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT_2026-06-21.md`;
- `CVF_WO_MPI_T4_FEDERATED_READ_HELPER_FAST_PATH_2026-06-21.md`.

Each work order must include a Source Verification Block, Roadmap-to-Work-Order
Trace Matrix, Allowed and Forbidden Scope, Public Export Disposition, and Claim
Boundary, per `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`.

## Risk Register

| Risk | Control |
| --- | --- |
| MPI re-implements MKG7 / GC-051 / LSC | Relationship table plus per-work-order Source Verification Block; integration-only framing |
| Scan-registry projection treated as source of truth | Enforce rebuildable-derived-view rule from MKG7 derived-graph boundary |
| External read contract drifts into adapter build | `adapterContractOnly=true`, mirroring LSC-T6; no adapter authorized |
| Raw content leakage through federation | Reuse RAW sentinel and summary-only projection; forbidden-field assertions in tests |
| Reinjection by accident | Preserve `canReinject=false` on all MPI surfaces |
| Write authority creep into registry/durable store | MPI adds no write path; any write requires separate GC-018 |
| Public/private boundary drift | Public Export Disposition remains `DEFERRED_PRIVATE_ONLY` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MPI is a private provenance roadmap. No public-sync remote, public
repository commit, hosted proof, public artifact path, or public README claim is
included.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Roadmap state | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | `Status: MPI_T2_CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_WO_MPI_T0_INDEX_LEGACY_MEMORY_GRAPH_RECHECK_2026-06-21.md`; `docs/work_orders/CVF_WO_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_2026-06-21.md`; `docs/work_orders/CVF_WO_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_2026-06-21.md`; `docs/work_orders/CVF_WO_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_2026-06-22.md` | MPI-T0 closed; MPI-T1 closed; INDEX-T1 closed; MPI-T2 closed | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_CODEX_REBUTTAL_2026-06-21.md`; `docs/reviews/CVF_MPI_T0_INDEX_LEGACY_MEMORY_GRAPH_RECHECK_COMPLETION_2026-06-21.md`; `docs/reviews/CVF_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_COMPLETION_2026-06-21.md`; `docs/reviews/CVF_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_COMPLETION_2026-06-21.md`; `docs/reviews/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_COMPLETION_2026-06-22.md` | Codex rebuttal absorbed; MPI-T0 closure released MPI-T1; MPI-T1 closure accepted map with reviewer correction; INDEX-T1 closure accepted checker with reviewer repair; MPI-T2 closure accepted helper/test/reference/map | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no registry JSON update; MPI-T2 consumes parsed registry entries as a derived view and writes no registry aggregate; drift check passes | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no registry Markdown update; MPI-T2 does not mutate registry reports | PASS |
| External evidence digest | N/A | no external evidence digest; Claude roadmap is absorbed through External Knowledge Intake Routing | N/A with reason |
| System loop interlock | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | no system loop interlock change in roadmap selection draft | N/A with reason |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V20_2026-06-19.md` | session-sync follows MPI-T2 material closure commit | N/A with reason |
| Operator selection | active session next-move surfaces | operator selected MPI-T2 after INDEX-T1 closure checkpoint | PASS |
| Dispatch authority | MPI-T0 GC-018/work order; INDEX-T1 GC-018/work order; MPI-T1 GC-018/work order; MPI-T2 GC-018/work order | MPI-T0 closed; MPI-T1 closed; INDEX-T1 closed; MPI-T2 dispatched and closed | PASS |
| Runtime implementation | `docs/work_orders/CVF_WO_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_2026-06-22.md` | bounded projection helper/test/reference only; route edit, registry write, durable write, provider/live, public-sync, and adapter behavior remain forbidden | PASS |
| Public export | `Public Export Disposition` | `DEFERRED_PRIVATE_ONLY` | PASS |
| Next action | operator checkpoint after MPI-T2 closure | select MPI-T3, hold, or open a fresh governed tranche; MPI-T4 remains optional parked | PASS |

## Claim Boundary

This roadmap authorizes planning for Memory plane integration only. It does not
authorize live/provider proof, public-sync, prompt injection, Memory
reinjection, raw Memory release, registry write authority, durable write
semantic change, new memory tiers, vector or embedding stores, graph
persistence, CLI/MCP adapter implementation, production readiness, or autonomous
mutation. MPI federates and maps already-built, already-bounded CVF memory
surfaces; it does not build a new memory system.
