# CVF P4-A1 Governed Retrieval Intake And P3-B Remainder Dependency Map Roadmap

Memory class: FULL_RECORD

Status: P4_A1_INTAKE_OPEN_P3_B_DEPENDENCY_MAP_ONLY

docType: roadmap

Date: 2026-08-07

Owner role: dispatcher

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | `## Checker Source Read-Ahead Block`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `Status:`; `## Authorization / Decision`; `## Purpose`; `## Scope / Target / Owner Boundary`; `## Non-Goals`; `## Design Control Gate`; `## Dispatch Boundary`; `## Work Plan`; `## Acceptance Criteria`; `## Verification / Evidence`; `## Public Export Disposition`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirmation and evidence after checker-source read-ahead, not first discovery |
| claimBoundary | roadmap intake and dependency mapping only; no lifecycle DESIGN, SPEC, WORK ORDER, BUILD, provider, persistence, vector, RAG, runtime, public-sync, or deployment authority |

## Authorization / Decision

The operator authorized one fresh P4-A1 governed-retrieval INTAKE and a
dependency map for the remaining P3-B area on 2026-08-07.

The operator explicitly withheld authority for:

- lifecycle DESIGN;
- lifecycle BUILD;
- provider selection or invocation;
- persistence or durable-store decisions;
- vector retrieval or RAG decisions and implementation.

Decision: `OPEN_P4_A1_INTAKE_AND_MAP_P3_B_REMAINDER_ONLY`.

This roadmap does not dispatch a worker and does not authorize a child work
order. It records the current owner surfaces, unresolved dependencies, and the
fail-closed boundary that must hold before any later design decision.

## Purpose

Create a current, source-backed front door for governed-retrieval planning
without treating the repository's existing partial retrieval capabilities as
one integrated product claim.

P4-A1 answers only these intake questions:

1. Which current CVF surfaces already own a retrieval-related contract,
   helper, receipt, policy, or local deterministic proof?
2. Which dependencies remain partial, unwired, domain-specific, or
   contract-only?
3. Which P3-B remainder items must stay parked because authority or source
   evidence is absent?
4. What evidence would be required before the operator could separately
   authorize lifecycle DESIGN?

## Scope / Target / Owner Boundary

Allowed scope:

- read current CVF-governed source, reference, roadmap, and closure surfaces;
- classify existing retrieval-related owners without changing them;
- distinguish contract, deterministic helper, local runtime, and live-proof
  claim classes;
- map P3-B remainder dependencies and their current release posture;
- record contradictions, overlap, gaps, and concrete reopen evidence;
- identify later decision checkpoints without selecting an architecture.

Forbidden scope:

- no interface, schema, receipt, query, storage, index, or adapter design;
- no source, test, route, package, registry, checker, or generated-state
  implementation;
- no provider, model, network, credential, or live-proof action;
- no persistent store, durable write, graph persistence, or database choice;
- no embedding, vector database, semantic retrieval, or RAG choice;
- no corpus ingestion, re-indexing, migration, or data movement;
- no public-sync mutation, push, deployment, or readiness claim.

Target: one private provenance roadmap that opens P4-A1 INTAKE and carries the
P3-B remainder dependency map.

Owner boundary: existing owner surfaces retain their current authority. This
roadmap does not consolidate, supersede, or integrate them.

## Operator Label Classification

Repository-wide exact search on 2026-08-07 found no existing canonical
artifact declaring `P4-A1` or `P3-B` as governed-retrieval tranche identifiers.
The labels are therefore operator-supplied planning labels introduced by this
roadmap, not pre-existing runtime or contract symbols.

| Label | Classification | Meaning in this roadmap | Authority effect |
|---|---|---|---|
| `P4-A1` | `DOC_ONLY_NEW` | fresh governed-retrieval intake lane | opens intake and mapping only |
| `P3-B` | `DOC_ONLY_NEW` | remainder dependency-map lane named by the operator | creates no implementation or release authority |
| governed retrieval | existing cross-surface concept | bounded retrieval-related contracts and helpers exist in several owner families | no integrated product claim |

If a later governed source establishes different canonical meanings for either
label, the later packet must reconcile the conflict before dispatch.

## Current Owner Surface Inventory

| Owner surface | Current accepted contribution | Current boundary | P4-A1 intake disposition |
|---|---|---|---|
| `docs/reference/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT.md` | summary-only read request/readout mapping with raw-memory release and reinjection held false for the mapped route | contract-only; no adapter, route edit, durable write, or provider/live authority | `REUSE_AS_BOUNDARY_INPUT` |
| `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | MPI-T3 through MPI-T5 are closed bounded; MPI-T6 decided to defer later runtime, vector, and durable work | phase is fully decided private-only and later runtime candidates remain deferred | `REUSE_AS_PARKING_AUTHORITY` |
| `docs/reviews/CVF_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_COMPLETION_2026-06-13.md` | deterministic summary-only filtering helper preserves `summaryOnly=true` and `rawMemoryReleased=false` | helper is unwired; no retrieval behavior, durable store, or vector claim | `REUSE_AS_FILTER_BOUNDARY_INPUT` |
| `docs/reviews/CVF_DSCP_T4_RETRIEVAL_RECEIPT_RUNTIME_BOUNDARY_COMPLETION_2026-06-07.md` | deterministic `buildGovernedRetrievalReceipt()` helper and focused tests | no live query, answer-quality, provider, or ingestion claim | `REUSE_AS_RECEIPT_INPUT` |
| `docs/reviews/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_COMPLETION_2026-06-03.md` | documentation specification for retrieval flow, conflict/freshness handling, and receipt shapes | no runtime code, real corpus retrieval, vector search, or provider call | `REUSE_AS_DOMAIN_SPEC_INPUT` |
| `docs/reviews/CVF_LPCI2_T9_SEARCH_RUNTIME_COMPLETION_2026-06-07.md` | local deterministic filter-first and keyword-ranked Policy_Local search with acceptance receipts | domain-specific pilot; no provider, LLM, vector, or production claim | `REUSE_AS_LOCAL_DETERMINISTIC_INPUT` |
| `docs/reviews/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_LOCAL_REVIEW_2026-06-02.md` | local KGR store, builder, policy integration, and focused tests; separate bounded live proof exists | no production readiness, vector persistence, web-route graph integration, or prompt reinjection | `REUSE_AS_PARTIAL_GRAPH_INPUT` |
| `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` | storage and index discipline for long-lived governance foundation artifacts | governs file layout and discovery, not retrieval-data persistence | `DO_NOT_MISCLASSIFY_AS_PERSISTENCE_AUTHORITY` |

## P3-B Remainder Dependency Map

`P3-B` is a dependency-map label only. The rows below do not prescribe a
design or imply that every dependency must be implemented.

| ID | Remainder concern | Existing evidence or owner | Missing dependency evidence | Current posture | Reopen condition |
|---|---|---|---|---|---|
| `P3-B-01` | source authority and request scope | MPI-T3 contract maps current request/readout fields | later work must reverify every consumed runtime field against current source | `PARTIAL_SATISFIED_INTAKE_ONLY` | fresh source-verification packet proves current fields, owner, and allowed claim class |
| `P3-B-02` | safe candidate eligibility and summary release | MEMCON-T4 filters ineligible summaries; MPI-T3 prevents raw release in its mapped route | no cross-owner integration proof joins the two surfaces | `UNWIRED_DEPENDENCY` | separately authorized design packet proves whether integration is needed and names the owner without changing runtime |
| `P3-B-03` | receipt and attribution | DSCP-T4 deterministic receipt helper; LPCI1-T4 receipt specification | no generic end-to-end receipt owner or accepted cross-domain composition proof | `PARTIAL_MULTI_OWNER` | current owner audit identifies one source-backed receipt authority and conflict policy |
| `P3-B-04` | filter, freshness, conflict, and abstention semantics | LPCI1-T4 specification; LPCI2-T9 deterministic domain pilot | semantics are not proven domain-agnostic or integrated with memory readout | `DOMAIN_BOUNDED` | intake evidence identifies required domains and demonstrates whether reuse or a new owner is justified |
| `P3-B-05` | graph-assisted retrieval | KGR1 local implementation and bounded proof | no production route integration or durable graph persistence authority | `PARKED_NO_CURRENT_AUTHORITY` | explicit operator authority plus fresh owner, route, persistence, and negative-proof evidence |
| `P3-B-06` | caller authentication and access policy | MPI-T3 cites current service-token/session route behavior | P4-A1 has no authority to design credentials, roles, tenancy, or access enforcement | `PARKED_SECURITY_DESIGN_REQUIRED` | separate security/design authority and current source verification exist |
| `P3-B-07` | persistence and durable store | no P4-A1 persistence authority; foundation storage standard is not runtime persistence authority | storage engine, retention, mutation, rollback, tenancy, and durability decisions are absent | `PARKED_NO_AUTHORITY` | operator explicitly authorizes persistence DESIGN and a source-backed owner packet defines the decision boundary |
| `P3-B-08` | vector, embedding, semantic retrieval, or RAG | MPI roadmap and domain closures explicitly exclude these claims | no need, value, threat, cost, or owner decision has been accepted for this lane | `PARKED_NO_AUTHORITY` | operator explicitly authorizes a separate decision intake after concrete value and owner evidence exists |
| `P3-B-09` | provider-backed answer generation or quality proof | existing retrieval surfaces are primarily contract/local deterministic; historical bounded proofs do not release this lane | no current provider, model, quota, diagnostic, or live-proof authority | `PARKED_NO_AUTHORITY` | fresh operator checkpoint names the exact governance behavior claim and live-proof boundary |
| `P3-B-10` | adapter or consumer integration | MPI-T3 is contract-only and existing helpers retain their local owner boundaries | no accepted consumer, adapter, or composition owner is selected | `PARKED_BEFORE_DESIGN` | current source evidence identifies a real consumer and the operator authorizes design of that one boundary |
| `P3-B-11` | public or deployment surface | this roadmap is private provenance planning | no public artifact, export packet, deployment target, or readiness evidence | `DEFERRED_PRIVATE_ONLY` | separate public-safe or deployment packet receives explicit authority |

## Dependency Ordering Constraints

The intake dependency order is evidence-first, not an implementation sequence:

1. establish current owner and claim class;
2. identify overlap and contradictions across owners;
3. decide whether a real consumer/value gap exists;
4. obtain explicit operator authority for one later lifecycle phase;
5. only then author the matching GC-018 and source-verified work order.

No row may skip from intake evidence directly to BUILD. Persistence and
vector/RAG are optional candidate lanes, not implied prerequisites for
governed retrieval.

## Design Control Gate

Gate status: `HOLD_BEFORE_DESIGN`.

| Gate question | Current answer | Effect |
|---|---|---|
| Does operator authority cover lifecycle DESIGN? | No | no architecture, schema, interface, or technology choice may be made |
| Is one integrated governed-retrieval owner source-backed? | No | preserve multi-owner boundaries and record overlap only |
| Is a concrete consumer/value gap accepted? | Not yet | no composition or runtime route may be proposed as ready |
| Is persistence authorized? | No | no durable-store or retention decision |
| Is vector/RAG authorized? | No | no embedding, semantic-search, vector-store, or RAG decision |
| Is provider/live work authorized? | No | no model, credential, quota, network, or live proof |
| Can a work order be dispatched from this roadmap? | No | a later explicit authority decision and fresh GC-018 are required |

Design-gate exit requires an operator instruction that selects one bounded
decision question and names the newly authorized lifecycle phase. Silence,
historical proof, helper existence, or dependency-map completion cannot release
the gate.

## Dispatch Boundary

No worker dispatch is authorized by this roadmap.

The only allowed continuation without expanded authority is further read-only
P4-A1 intake evidence that corrects the owner inventory or P3-B dependency map.
Any child GC-018 or work order must remain uncreated until the operator grants
the relevant authority.

Future dispatch packets must keep these lanes separate:

- retrieval contract and claim-boundary decision;
- consumer and composition decision;
- security and access-control decision;
- persistence decision;
- vector/RAG decision;
- provider/live-proof decision;
- public or deployment decision.

## Work Plan

| Step | Intake-only action | Output | Stop condition |
|---|---|---|---|
| `P4-A1.1` | inventory current governed-retrieval owner surfaces | owner surface table | stop if a claimed owner cannot be source-backed |
| `P4-A1.2` | classify each surface as contract, helper, local runtime, bounded proof, or parking authority | claim-class matrix | stop before any integration proposal |
| `P4-A1.3` | dependency-map the P3-B remainder | dependency and reopen ledger | stop before DESIGN |
| `P4-A1.4` | record overlap, contradiction, and missing-authority findings | operator checkpoint inputs | stop before selecting technology or provider |
| `P4-A1.5` | return a bounded intake recommendation | one next decision question or `NO_DESIGN_JUSTIFIED` | operator decides whether any later phase opens |

## Non-Goals

This roadmap does not:

- define a unified retrieval architecture;
- choose a search algorithm or ranker;
- define new schemas, fields, receipts, or APIs;
- choose a database, persistence model, retention policy, or migration plan;
- choose embeddings, vector infrastructure, or a RAG pattern;
- select or call a provider or model;
- claim retrieval completeness, semantic correctness, latency, cost, answer
  quality, production readiness, or universal CVF control;
- reopen MPI-T6 or any parked historical lane;
- mutate public or deployment surfaces.

## Dual Agent Surface Matrix

| Consumer class | Interface or surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | this roadmap and cited CVF-governed sources | may read and refine intake evidence only | source inventory and dependency map | no adapter | `INTAKE_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no executable interface in this tranche | may not call, mutate, or claim CVF retrieval behavior | MPI-T3 contract-only boundary | no adapter implementation | `NOT_AUTHORIZED` |
| `FUTURE_WORKER` | future separately authorized packet | may act only after fresh GC-018 and source verification | operator authority plus then-current sources | separate adapter decision if applicable | `PARKED` |

## Acceptance Criteria

| ID | Criterion | Required disposition |
|---|---|---|
| `AC-01` | P4-A1 and P3-B are identified as new operator planning labels, not existing runtime symbols | `PASS_REQUIRED` |
| `AC-02` | current owner surfaces are inventoried without claiming integrated retrieval | `PASS_REQUIRED` |
| `AC-03` | each P3-B remainder row names existing evidence, missing evidence, current posture, and a checkable reopen condition | `PASS_REQUIRED` |
| `AC-04` | lifecycle DESIGN and BUILD remain blocked | `PASS_REQUIRED` |
| `AC-05` | provider, persistence, and vector/RAG lanes remain separately parked | `PASS_REQUIRED` |
| `AC-06` | no work order, runtime mutation, live proof, public mutation, or deployment is released | `PASS_REQUIRED` |
| `AC-07` | further continuation is limited to read-only intake correction or a new operator authority decision | `PASS_REQUIRED` |

## Verification / Evidence

| Evidence item | Command or artifact | Observed result |
|---|---|---|
| Authoring base | `git rev-parse --short HEAD` | `e5bf6902d` |
| Initial worktree | `git status --short` | clean |
| Operator-label negative search | repository-wide exact search for `P4-A1`, `P3-B`, and governed-retrieval wording, excluding generated dependency trees and Git internals | no canonical P4-A1 or P3-B governed-retrieval tranche declaration found |
| Lifecycle authority boundary | `docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md` | INTAKE is distinct from DESIGN, SPEC, WORK ORDER, and BUILD |
| Summary-only memory contract | `docs/reference/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT.md` | contract-only mappings and safety invariants exist; later adapter/runtime work remains separate |
| MPI parking authority | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | MPI-T6 decided to defer later runtime/vector/durable candidates |
| Retrieval-pack filter boundary | `docs/reviews/CVF_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_COMPLETION_2026-06-13.md` | deterministic unwired helper; summary-only/raw-release boundary retained |
| Receipt boundary | `docs/reviews/CVF_DSCP_T4_RETRIEVAL_RECEIPT_RUNTIME_BOUNDARY_COMPLETION_2026-06-07.md` | deterministic receipt helper only; no live retrieval query |
| Domain retrieval specification | `docs/reviews/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_COMPLETION_2026-06-03.md` | specification only; runtime/vector/provider excluded |
| Local deterministic search | `docs/reviews/CVF_LPCI2_T9_SEARCH_RUNTIME_COMPLETION_2026-06-07.md` | filter-first/keyword-rank domain pilot; provider/LLM/vector excluded |
| Graph retrieval boundary | `docs/reviews/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_LOCAL_REVIEW_2026-06-02.md` | local bounded capability; production route and persistence excluded |
| Foundation file-layout boundary | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` | governs foundation artifact storage/index layout, not retrieval-data persistence |

## Epistemic Process Block

Expected Result / Prediction: current CVF sources would show several bounded
retrieval-related owners but no single source-backed integrated
governed-retrieval product authority.

Evidence Comparison: the current sources show contract-only memory read
mapping, deterministic filtering and receipt helpers, a domain-specific local
search pilot, and bounded graph retrieval. Their accepted boundaries retain
unwired, domain-specific, no-persistence, no-vector, or no-production limits.

Contradiction Or Gap Disposition: no contradiction requires reopening a closed
lane. The material gap is cross-owner integration and consumer authority, which
this intake records without solving.

Claim Update: open P4-A1 INTAKE and retain the P3-B remainder as a dependency
map. Do not advance to DESIGN unless the operator later selects one bounded
decision question and grants that phase authority.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance intake roadmap and dependency map. No
public-sync mutation, public artifact, or public claim is authorized.

## Claim Boundary

This roadmap opens source-backed intake and dependency mapping only. It does
not authorize lifecycle DESIGN, SPEC, WORK ORDER, BUILD, provider or model
selection, provider invocation, persistence, durable storage, graph
persistence, vector retrieval, embeddings, semantic retrieval, RAG, runtime
integration, corpus ingestion, public-sync, deployment, or readiness claims.
Existing bounded retrieval-related artifacts remain owned by their current
surfaces and are not promoted into one integrated product claim.
