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
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/retrieval.contract.ts` | current `RetrievalContract` wraps the legacy `RAGPipeline` and exposes retrieval chunks | the retriever is lexical over an in-memory store; domain/tag filters fall back to unfiltered candidates when no match exists, so they are not strict scope enforcement | `REUSE_AS_CONTROL_PLANE_SOURCE_INPUT` |
| `EXTENSIONS/CVF_PLANE_FACADES/src/knowledge.facade.ts` | exported `retrieveContext()`, `prepareIntake()`, and `consume()` entrypoints compose current Control Plane contracts | no external non-test caller was found, so facade availability is not runtime-adoption evidence | `EXPORTED_SOURCE_ENTRYPOINT_NO_EXTERNAL_NON_TEST_CALLER_FOUND` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-retrieval.ts` | scoped lexical chunk retrieval and formatting for the Web knowledge surface | local token matching only; no vector or embedding behavior | `REUSE_AS_WEB_RETRIEVAL_INPUT` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts` | current Web owner has in-process and file-backed JSON knowledge-store implementations | only collection/chunk `_store` mutations are file-persisted; ephemeral ingest and audit log remain process-local, and P4-A1 has no change authority | `RECORD_NARROW_EXISTING_PERSISTENCE_NO_CHANGE_AUTHORITY` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-knowledge-context.ts` | execute-route helper calls scoped knowledge retrieval, emits scope-filter audit, and prepares context before provider execution by its caller | current route composition is a distinct Web owner, not a universal governed-retrieval owner | `REUSE_AS_ROUTE_COMPOSITION_INPUT` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | route calls deterministic LPCI retrieval, emits receipts, and contains an optional provider-call branch | provider code existence does not authorize invocation or quality claims in P4-A1 | `RECORD_PROVIDER_SURFACE_NO_INVOCATION_AUTHORITY` |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | memory runtime workflow calls `evaluateRetrievalRequest()` and packages summary-only context | composition is memory-specific and retains false raw-release/reinjection flags | `REUSE_AS_MEMORY_RUNTIME_INPUT` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | authenticated POST route calls `buildMemoryRuntimeReadout()` and returns summary-only projection flags | request body exposes no retrieval method and the route injects no graph options, so this route uses the default keyword path | `REUSE_AS_EXISTING_KEYWORD_ROUTE_INPUT` |

## P4-A1 Source-Level Refinement Record - 2026-08-07

Direct current-source inspection narrows the initial roadmap in eight material
ways:

1. CVF has real Web route consumers plus multiple exported or internal Control
   Plane entrypoints. `KnowledgeFacade` has no external non-test caller found,
   so it is not evidence of runtime adoption.
2. The Control Plane source uses a class named `RAGPipeline`, but its current
   retriever is deterministic term/domain/tag scoring over an in-memory
   `DocumentStore`. This is not evidence of vector or embedding behavior.
3. Control Plane domain/tag filtering is a soft preference: when no match
   exists, the retriever retains the prior candidate set. It is not strict
   governed scope enforcement. The default pipeline store is also empty unless
   a caller injects or populates documents.
4. The Web knowledge surface already has file-backed JSON persistence and is
   route-composed into execution context preparation. P4-A1 may inventory this
   source but may not redesign or promote it. Only collection/chunk `_store`
   mutations are durable; ephemeral ingest and audit log are process-local.
5. The LPCI query route contains a provider-call branch after deterministic
   retrieval. Source existence is recorded; no call, credential use, or live
   proof is authorized.
6. The memory policy labels one method `semantic`, but both `keyword` and
   `semantic` use the same substring matcher. The label is not semantic-vector
   proof.
7. The Web memory readout route cannot select `graph_search`; it omits the
   retrieval method and graph dependencies, so it defaults to `keyword`.
   Direct library callers selecting graph search without an injected graph
   service receive a deferred result.
8. Exact non-test reference search finds the MEMCON retrieval-pack helper and
   DSCP receipt builder only at their definitions. Their accepted unwired
   boundaries remain current.

The refinement changes the dependency description, not the gate. The design
gate remains `HOLD_BEFORE_DESIGN`.

## Independent Worker Audit And Reviewer Disposition - 2026-08-07

The operator assigned this agent as reviewer and three agents as read-only
workers. Worker notes were treated as non-canonical leads and reverified against
the current source paths below before acceptance.

| Audit lane | Reviewer disposition | Accepted correction |
|---|---|---|
| Control Plane, ECO, and facade | `ACCEPT_WITH_CORRECTION` | distinguish exported/internal entrypoints from runtime adoption; record soft domain/tag fallback and empty default store |
| Web store, execute route, and LPCI | `ACCEPT_WITH_CORRECTION` | narrow persistence to collection/chunk `_store`; keep ephemeral ingest and audit log process-local |
| Memory policy, readout, and graph | `ACCEPT_WITH_CORRECTION` | Web readout defaults to keyword and cannot select graph search; semantic is substring matching; graph implementations remain unwired outside tests |

Reviewer decision: the corrections improve source fidelity but do not satisfy
or release the design gate. Status remains
`P4_A1_INTAKE_OPEN_P3_B_DEPENDENCY_MAP_ONLY`.

## Bounded Intake Recommendation - 2026-08-07

Three independent read-only value-gap audits were reviewed against current
source and canonical closure evidence.

Cross-owner disposition: `NO_CROSS_OWNER_DESIGN_JUSTIFIED`.

Current evidence does not identify an accepted cross-owner product failure,
runtime adoption gap, or safety requirement that requires a unified retrieval
owner. Existing capabilities remain useful but owner-local. Capability overlap
alone is not value evidence for composition.

One narrower current-owner question is source-backed:

`AUTHORIZE_FRESH_LPCI_DEFECT_INTAKE_DOCUMENTATION_ONLY?`

The proposed intake would decide whether LPCI must require evidence-text
grounding and actor-bound sensitivity clearance before any later LPCI DESIGN,
BUILD, or provider work. It would not authorize those later phases.

| LPCI candidate finding | Current source evidence | Reviewer classification | Current boundary |
|---|---|---|---|
| answer prompt grounding | `buildAnswerBoundaryPrompt()` maps matched records to path, status, and effective date while `LpciIndexRecord` also carries `contentSnippet` | `SOURCE_LEVEL_DEFECT_CANDIDATE` | no provider call was made; a separate intake must decide the required evidence boundary |
| sensitivity-clearance authority | route copies client `filters` into `appliedFilters`; filter pipeline treats `sensitivityClearance=true` as sufficient without binding it to `routeAuth` identity | `SOURCE_LEVEL_SECURITY_DEFECT_CANDIDATE` | current dashboard sends empty filters and current pilot evidence is public; no exploitation or classified-data release is claimed |
| negative provider response | `NO_PROVIDER_CONFIGURED` returns the phase-2 retrieval receipt whose matched records retain the index-record shape | `SOURCE_LEVEL_DISCLOSURE_REVIEW_CANDIDATE` | authorization exists at the route; later intake must assess response minimization and actor-bound clearance together |

Reviewer checkpoint recommendation:

1. accept `NO_CROSS_OWNER_DESIGN_JUSTIFIED` and keep the P3-B cross-owner lane
   value-parked;
2. optionally authorize only a fresh documentation-only LPCI current-owner
   defect intake for the two linked requirements above;
3. keep DESIGN, SPEC, WORK ORDER, BUILD, provider/live, persistence,
   vector/RAG, public-sync, and deployment unauthorized.

Cross-owner DESIGN may reopen only when one committed CVF-governed evidence
packet identifies an exact non-test consumer and owner, an observed blocked or
unsafe behavior, why existing owner-local behavior cannot satisfy it, and one
bounded deterministic positive and fail-closed negative case. A later phase
also requires explicit operator authority, fresh GC-018, and source
verification.

## Negative Search And Collision Discipline

- Search roots: `EXTENSIONS` with package exclusions stated per row.
- Search commands: `rg -n --glob "*.ts" --glob "!**/*.test.ts" --glob "!**/tests/**" "GraphSQLiteStore|createInMemoryGraphKnowledgeService|graphKnowledgeService:|kgrStore:" EXTENSIONS`; corresponding exact-symbol `rg` queries were used for the facade, MEMCON, and DSCP rows.
- Coverage: current source, tests, docs, JSON, and external evidence were considered; binding absence claims below are deliberately limited to non-test TypeScript source.
- Same-token collision results: `SQLite` occurs in the graph store definition, tests, and exports; graph symbols occur in definitions, exports, and tests; facade and helper symbols occur in their owning packages, tests, or docs.
- Disposition: these collisions are non-authoritative for external non-test caller or composition proof. The tokens are not globally absent, and their existence is not binding evidence of runtime adoption.

| Claim under test | Exact search scope | Exclusions | Result | Disposition |
|---|---|---|---|---|
| external runtime adoption of `KnowledgeFacade` | non-test TypeScript under `EXTENSIONS` for `createKnowledgeFacade`, `KnowledgeFacade`, and `cvf-plane-facades` outside `CVF_PLANE_FACADES` | tests, package-local definitions, docs, changelogs, generated dependency trees, and Git internals | no external non-test source caller returned | retain source-entrypoint claim only; do not claim runtime adoption |
| non-test graph composition | non-test TypeScript under `EXTENSIONS` for `GraphSQLiteStore`, `createInMemoryGraphKnowledgeService`, `graphKnowledgeService:`, and `kgrStore:` | tests, definitions, barrel exports, generated dependency trees, and Git internals | only definitions and exports returned outside tests | retain implementation-source claim; composition and persistence ownership remain unwired |
| cross-owner use of MEMCON and DSCP helpers | non-test TypeScript under `EXTENSIONS` for `buildMemconRetrievalPackBoundary` and `buildGovernedRetrievalReceipt` | tests, comments, generated dependency trees, and Git internals | each symbol returned only at its defining source | retain accepted unwired boundary |

These negative searches are bounded to the stated source classes and do not
prove universal absence outside the repository or excluded surfaces. A later
packet must repeat them against its current base before relying on them.

## P3-B Remainder Dependency Map

`P3-B` is a dependency-map label only. The rows below do not prescribe a
design or imply that every dependency must be implemented.

| ID | Remainder concern | Existing evidence or owner | Missing dependency evidence | Current posture | Reopen condition |
|---|---|---|---|---|---|
| `P3-B-01` | source authority and request scope | MPI-T3 contract maps current request/readout fields | later work must reverify every consumed runtime field against current source | `PARTIAL_SATISFIED_INTAKE_ONLY` | fresh source-verification packet proves current fields, owner, and allowed claim class |
| `P3-B-02` | safe candidate eligibility and summary release | MEMCON-T4 filters ineligible summaries; MPI-T3 prevents raw release in its mapped route | no cross-owner integration proof joins the two surfaces | `UNWIRED_DEPENDENCY` | separately authorized design packet proves whether integration is needed and names the owner without changing runtime |
| `P3-B-03` | receipt and attribution | DSCP-T4 deterministic receipt helper; LPCI1-T4 receipt specification | no generic end-to-end receipt owner or accepted cross-domain composition proof | `PARTIAL_MULTI_OWNER` | current owner audit identifies one source-backed receipt authority and conflict policy |
| `P3-B-04` | filter, freshness, conflict, and abstention semantics | LPCI1-T4 specification; LPCI2-T9 deterministic domain pilot | semantics are not proven domain-agnostic or integrated with memory readout | `DOMAIN_BOUNDED` | intake evidence identifies required domains and demonstrates whether reuse or a new owner is justified |
| `P3-B-05` | graph-assisted retrieval | KGR1 local implementation; `memory-retrieval-policy.ts` accepts injected `kgrStore` or `graphKnowledgeService`; SQLite graph storage source exists | the Web memory route exposes no retrieval method and defaults to keyword; direct graph callers need injected dependencies; non-test graph composition and persistence owners were not found | `PARTIAL_IMPLEMENTATION_ROUTE_UNWIRED` | explicit operator authority plus fresh owner, route-selection/injection, persistence-boundary, confidentiality/scope metadata, and negative-proof evidence |
| `P3-B-06` | caller authentication and access policy | MPI-T3 cites current service-token/session behavior; LPCI query route has route-governance authorization | LPCI sensitivity clearance is client-filter supplied rather than actor-bound; P4-A1 has no authority to design credentials, roles, tenancy, or access enforcement | `PARKED_SECURITY_DESIGN_REQUIRED` | operator may first authorize the bounded LPCI documentation-only defect intake; any security DESIGN still requires separate authority and current source verification |
| `P3-B-07` | persistence and durable store | Web `knowledge-store.ts` file-persists collection/chunk `_store` mutations; graph SQLite storage source also exists | ephemeral ingest and audit log are process-local; graph storage has test-only composition; no authority selects either owner for cross-plane use or resolves retention, rollback, tenancy, failure, and durability policy | `EXISTING_LOCAL_OWNER_PARKED_NO_CHANGE_AUTHORITY` | operator explicitly authorizes persistence DESIGN and a source-backed owner packet defines whether existing local persistence is reused, isolated, or rejected |
| `P3-B-08` | vector, embedding, semantic retrieval, or RAG | Control Plane `RAGPipeline` is lexical over an in-memory store; memory `semantic` uses the same substring matcher as `keyword`; MPI and domain closures exclude vector claims | no vector/embedding behavior proof, accepted need, value, threat, cost, or owner decision exists for this lane | `PARKED_NO_AUTHORITY_NAME_NOT_PROOF` | operator explicitly authorizes a separate decision intake after concrete value and owner evidence exists |
| `P3-B-09` | provider-backed answer generation or quality proof | the LPCI query route contains an optional provider-call branch; its current prompt lists source metadata but not `contentSnippet`; historical proofs do not release P4-A1 | no current provider, model, quota, diagnostic, or live-proof authority; evidence-text grounding is a current-owner defect candidate, not a provider-call authorization | `SOURCE_EXISTS_INVOCATION_PARKED` | operator may authorize a documentation-only LPCI defect intake; any provider proof requires a later checkpoint naming the exact claim and live-proof boundary |
| `P3-B-10` | adapter or consumer integration | Web execute, LPCI query, and memory readout are route consumers; Control Plane has internal composition and exported facade entrypoints; MPI-T3 remains contract-only | `KnowledgeFacade` has no external non-test caller found, no one consumer is selected for a new integrated boundary, and no accepted value gap justifies composition | `MULTI_CONSUMER_PARKED_BEFORE_DESIGN` | operator selects one bounded consumer/value question and authorizes design of that boundary |
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
| Is a concrete cross-owner consumer/value gap accepted? | No | retain `NO_CROSS_OWNER_DESIGN_JUSTIFIED`; no composition may be proposed as ready |
| Is one current-owner defect intake question source-backed? | Yes, bounded LPCI documentation-only checkpoint | operator may authorize that intake without releasing DESIGN or BUILD |
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

## Current Runtime Freshness Verification

| Freshness item | Current verification | Disposition |
|---|---|---|
| Verification date and base | 2026-08-07 at repository base `5bbb75147` before this recommendation edit | current for this intake pass |
| LPCI route behavior | direct read of `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` covering route authorization, request filters, negative receipts, answer prompt construction, and optional provider branch | source-level behavior claim accepted; no provider invocation claim |
| LPCI filter and record shape | direct read of `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.ts`, `retrieval.ts`, and `types.ts` | client clearance input and retained `matched_records` shape accepted as current source facts |
| LPCI dashboard caller | direct read of `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx` | current UI sends an empty filter object; this does not prove every caller behaves the same |
| Provider registry context | current provider registry remains `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`; P4-A1 neither changes nor makes an absence claim about it | provider selection and invocation remain parked |
| Freshness boundary | exact searches and direct reads cover current repository source, not deployed state or external callers | repeat against the then-current base before any later packet relies on these facts |

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
| Control Plane retrieval source | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/retrieval.contract.ts`; `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/retriever.ts`; `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/document.store.ts`; `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/rag.pipeline.ts` | lexical scorer and in-memory store exist; domain/tag fallback is soft and the default pipeline starts empty |
| Exported Control Plane entrypoints | `EXTENSIONS/CVF_PLANE_FACADES/src/knowledge.facade.ts`; Control Plane intake, consumer, gateway-consumer, and batch contracts | internal composition and facade exports exist; no external non-test facade caller was found |
| Web retrieval and persistence | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-retrieval.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts` | lexical retrieval uses file-backed JSON outside tests, but only collection/chunk `_store` is persisted |
| Web route composition | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-knowledge-context.ts` | execute context helper calls scoped retrieval and records scope-filter audit before caller provider execution |
| Memory route composition | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts`; `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | summary-only route is wired and defaults to keyword; route exposes neither graph selection nor graph dependencies; semantic uses substring matching |
| Graph implementation boundary | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/index/symbol-index.ts`; `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/storage/graph-sqlite-store.ts` | traversal and SQLite source exist, but exact non-test composition search found only definitions/exports outside tests |
| LPCI provider surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | deterministic retrieval precedes an optional provider-call branch; source inspected only and no invocation performed |
| LPCI prompt grounding candidate | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | prompt maps path/status/date but index records also carry `contentSnippet`; requirement decision remains documentation-only |
| LPCI clearance candidate | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx` | client filter controls sensitivity clearance; dashboard sends empty filters; no actor-bound clearance proof or classified-release claim |
| Prior runtime-candidate value decision | `docs/baselines/CVF_GC018_MPI_T6_RUNTIME_CANDIDATE_DECISION_PACKET_2026-06-22.md`; `docs/reviews/CVF_MPI_T6_RUNTIME_CANDIDATE_DECISION_PACKET_COMPLETION_2026-06-22.md` | prior lane deferred speculative expansion absent an explicit product need, repeated missing-capability findings, or integration-partner requirement |
| Helper negative-reference search | exact symbol search across non-test TypeScript under `EXTENSIONS` for `buildMemconRetrievalPackBoundary` and `buildGovernedRetrievalReceipt` | each helper appears only at its definition outside tests; no cross-owner caller found |

## Epistemic Process Block

Expected Result / Prediction: current CVF sources would show several bounded
retrieval-related owners but no single source-backed integrated
governed-retrieval product authority.

Evidence Comparison: the current sources show contract-only memory read
mapping, deterministic filtering and receipt helpers, internal/exported Control
Plane entrypoints, real Web route consumers, narrowly file-persisted Web
collection/chunk state, a domain-specific local search pipeline with a
provider-capable route, and bounded graph implementation source.
The class named `RAGPipeline` currently performs lexical scoring over an
in-memory store rather than vector or embedding retrieval.

Contradiction Or Gap Disposition: the initial intake was too broad when it
described persistence and consumers only as missing future dependencies.
Current source proves narrow local persistence and multiple consumer surfaces,
but not runtime adoption for every exported facade or strict scope behavior for
every filter. The corrected gap is selection, safety semantics, and authority
for any new cross-owner boundary, not basic source existence. No closed lane is
reopened.

Claim Update: keep P4-A1 INTAKE open, correct the P3-B remainder map to account
for existing local persistence and consumers, accept
`NO_CROSS_OWNER_DESIGN_JUSTIFIED`, and retain `HOLD_BEFORE_DESIGN`. The only
source-backed next question is whether to authorize a fresh documentation-only
LPCI current-owner defect intake. Do not infer later phase authority from that
recommendation.

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
