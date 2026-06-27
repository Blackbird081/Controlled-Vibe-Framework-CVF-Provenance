# CVF CGE-T1 CodeGraph External Absorption Triage Matrix Completion

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

docType: review

Date: 2026-06-20

Batch ID: CGE-T1

From: Claude worker (author)

To: Codex (reviewer and closer)

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: 4d004c42

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_FOR_CLAUDE_2026-06-20.md`

GC-018 baseline:
`docs/baselines/CVF_GC018_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_2026-06-20.md`

## Purpose

Deliver the CGE-T1 source-verified absorption triage matrix for the external
CodeGraph repository and the local copied package, deciding row by row what CVF
adapts to existing owners, defers, rejects as parallel core, or blocks. This
artifact is a documentation and review-only triage packet. It does not
implement, install, or wire CodeGraph and does not make CodeGraph canonical.

## Findings / Position

Position: `CGE-T1` is correctly bounded as a doctrine and governance-first
triage matrix. The two CGE-T0 blockers are confirmed and carried as mandatory
rows: `freezeAllowed` graph-only authority is `BLOCK` (R1), and the local
package LPF-like files are `REJECT_PARALLEL_CORE` (R2). CodeGraph overlaps the
planned CVF KGR retrieval lane and is resolved toward KGR and existing LPF
owners rather than a parallel lane. Upstream performance claims are
benchmark-gated; watcher/daemon and MCP wiring are deferred to separate
governed lanes. ACE-R1 remains parked.

## Target / Source

Target: a source-verified absorption triage matrix that decides, row by row,
what CVF can adapt now, defer, reject as parallel core, or block, for the
external CodeGraph repository and the local copied package.

Primary sources:

- upstream repository `https://github.com/colbymchenry/codegraph` (fetched and
  verified this turn);
- local copied package `CodeGraph/CVF_Code_Intelligence_Capability/` (89 files,
  read-only inventory and sampling);
- current CVF graph owner surfaces under
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/` and
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context_builder/graph/`;
- prior CVF graph absorption surfaces: AIF-B, PBR04, N6, LHW13, MKG1, KGR
  pre-review, memory-derived graph boundary;
- CGE-T0 review packet, Claude rebuttal, and Codex classification.

## Scope / Methodology

1. Confirmed `executionBaseHead` and actual `git status --short`.
2. Read the required first-read artifacts (work order, GC-018, three CGE-T0
   packets, chain map, finding workflow, KGR pre-review, memory-derived graph
   boundary, MKG1 work order) and the five LPF graph owner source files.
3. Inventoried the local copied package and recorded file count plus
   representative files.
4. Fetched and verified upstream CodeGraph public facts directly.
5. Source-verified current CVF graph owner symbols and the KGR retrieval lane.
6. Authored the row-by-row triage matrix, the CodeGraph vs KGR dedupe decision,
   the ACE-R1 parking note, and the trace/evidence blocks.
7. Recorded actual pending status without committing.

## Source Inventory

| Class | Item | How inspected | Authority |
|---|---|---|---|
| Upstream | `https://github.com/colbymchenry/codegraph` | WebFetch read of repo landing page | External advisory input only |
| Local copied package | `CodeGraph/CVF_Code_Intelligence_Capability/` (89 files) | `find` inventory + sampled docs/source | External advisory input only |
| Local blocker source | `CodeGraph/.../graph-receipt-service.ts` | full-file read (CGE-T0) | External advisory input only |
| Local LPF-like files | `CodeGraph/.../copied learning-plane graph files` (11 files) | path enumeration | External advisory input only |
| Current CVF owner | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/graph-schema.ts` | grep-verified `GraphKnowledgeService` line 62 | CVF source authority |
| Current CVF owner | `.../knowledge/graph/index/symbol-index.ts` | grep-verified `SymbolIndex` line 13, `buildSymbolIndexFromGraph` line 40 | CVF source authority |
| Current CVF owner | `.../knowledge/graph/storage/graph-sqlite-store.ts` | path-verified | CVF source authority |
| Current CVF owner | `.../knowledge/graph/authority/graph-authority-gate.ts` | grep-verified `authorityModel` line 34, `canBypassPolicy: false` lines 36 and 124 | CVF source authority |
| Current CVF owner | `.../context_builder/graph/task-query-mapper.ts` | path-verified | CVF source authority |
| Prior absorption | `docs/reference/CVF_KGR_ABSORPTION_PREREVIEW_2026-06-01.md` | grep-verified KGR1-T3/T4 and no-external-lib stance | CVF authority |
| Prior absorption | `docs/reference/CVF_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md` | grep-verified derived-advisory stance | CVF authority |
| Prior absorption | AIF-B, PBR04, N6, LHW13, MKG1 | path-verified existence | CVF authority |

## Scan Depth Ledger (anti-overclaim)

| Source surface | Scan method performed | Depth | Not done |
|---|---|---|---|
| Upstream CodeGraph repo landing page | WebFetch read this turn | FETCH_VERIFIED | clone/build, deep source-file read, independent benchmark replication |
| Local package tree | `find` full count (89) + directory enumeration | STRUCTURE_ENUMERATED | line-by-line read of all 89 files |
| Local package docs/protocols/templates/guards | `find` enumeration + targeted grep | ENUMERATED_PLUS_GREP | full read of every doc |
| `graph-receipt-service.ts` blocker | full-file read (carried from CGE-T0) | FULL_READ | none |
| 11 local LPF-like files | path enumeration | PATHS_ENUMERATED | line-by-line read |
| 5 current CVF graph owner files | path + targeted grep of owner symbols/stance | PATH_PLUS_GREP | full line-by-line read |
| KGR pre-review | targeted grep of KGR1-T3/T4 and external-lib stance | GREP_CONFIRMED | full-file read |
| AIF-B, PBR04, N6, LHW13, MKG1 | path-exist verification | PATH_VERIFIED_ONLY | content body audit |

Confidence boundary: upstream facts in this matrix are FETCH_VERIFIED from the
public landing page only; they are external claims, not CVF-proven. Local
package blocker B1 and parallel-core B2 rest on FULL_READ and PATHS_ENUMERATED
evidence. Prior-absorption rows rest on grep-level or path-level checks
sufficient to establish owner existence and overlap, not full re-audit of each
closure body.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | External repo or copied folder -> lifecycle classification candidate -> absorption triage matrix -> CVF owner-surface disposition -> future GC-018/work order only if implementation is separately authorized |
| Owner surface | This CGE-T1 triage matrix; existing LPF graph owner surfaces; KGR pre-review; memory-derived graph boundary |
| Disposition | Row-level `ADAPT`, `DEFER`, `REJECT`, or `BLOCK`; no direct import |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Claim boundary | External absorption triage only; no runtime, MCP, benchmark, provider/live proof, public-sync, registry mutation, ACE-R1 reopening, readiness, or universal governed-coding-control claim |

## Knowledge Absorption Blind-Spot Control Block

| Gate | Result | Note |
|---|---|---|
| G1 source coverage | CLEAR | Upstream fetched; local package enumerated; CVF owners verified. |
| G2 prior absorption evidence | CLEAR | KGR, MKG1, AIF-B, PBR04, N6, LHW13, memory-derived boundary cited as prior owners. |
| G3 owner-surface mapping | CLEAR | Each adapt candidate mapped to an existing LPF/KGR owner before recommending. |
| G4 parallel-core risk | CLEAR | 11 local LPF-like files flagged `REJECT_PARALLEL_CORE`. |
| G5 authority-leak risk | CLEAR | `freezeAllowed` flagged `BLOCK`. |
| G6 claim-boundary risk | CLEAR | Upstream performance claims gated behind CVF benchmark; no runtime/public claim made. |
| G7 raw-legacy-scan necessity | CLEAR | Governed prior surfaces sufficient for T1; no broad raw legacy rescan needed. |

Verdict: `CLEAR`. This block does not claim a complete raw legacy scan; it
claims bounded coverage adequate for an external absorption triage matrix.

## Prior Absorption Resolution

| Prior surface | What it already owns | Effect on CodeGraph absorption |
|---|---|---|
| AIF-B graph knowledge Phase 1 | Graph schema + symbol index foundation | CodeGraph symbol/search vocabulary is already partly owned; adapt as vocabulary only. |
| PBR04 graph SQLite persist | Optional durable graph store | CodeGraph SQLite storage is not a missing capability; reject parallel store. |
| N6 graph_search activation | Advisory `graph_search` boundary | CodeGraph search/query must route through advisory boundary, not new authority. |
| LHW13-T3 graph context resolver boundary | `interface_only` / `text_retrieval` graph context boundary | CodeGraph resolver concepts must preserve this current-state boundary. |
| MKG1 owner-surface review | 47-asset Memory/Knowledge/Graph owner map | CodeGraph absorption must map into existing owners, not a new graph subsystem. |
| KGR pre-review | Planned in-process graph builder + retrieval wiring | CodeGraph overlaps KGR retrieval lane directly; dedupe required. |
| Memory-derived graph boundary | Graph views are derived/advisory, cannot overrule source | CodeGraph receipts must stay advisory; freeze authority is blocked. |

## Triage Matrix

| ID | Candidate (source-verified) | Source basis | Existing CVF owner | Disposition | Rationale |
|---|---|---|---|---|---|
| CGE-T1-R1 | `freezeAllowed` derived from index freshness/confidence/warnings | `graph-receipt-service.ts` lines 28-31 (full read) | `graph-authority-gate.ts` `canBypassPolicy: false` (lines 36, 124) | `BLOCK` | Graph signals may warn or require review but must not grant freeze/finality authority. Remove or rename and never let a true value imply freeze. |
| CGE-T1-R2 | Local LPF-like graph core files (11) under copied `CVF_LEARNING_PLANE_FOUNDATION/` paths | path enumeration; e.g. `sqlite-graph-store.ts`, `local-symbol-index.ts`, `graph-context-resolver.ts`, `graph-query-planner.ts` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/` (GraphKnowledgeService, SymbolIndex, GraphSQLiteStore) | `REJECT_PARALLEL_CORE` | CVF already owns these via AIF-B/PBR04. No package file may land under an existing LPF graph path; extend existing owners only. |
| CGE-T1-R3 | CodeGraph graph-retrieval vs CVF KGR retrieval lane | upstream tools; KGR1-T3 `buildKnowledgeGraph(files)`, KGR1-T4 retrieval wiring (lines 217-218) | KGR pre-review owns the planned retrieval lane | `DEDUP_DECISION_REQUIRED` | CodeGraph and KGR both target in-repo graph retrieval. Decide reuse/adapt/defer against KGR before any implementation lane (see Dedupe Decision). |
| CGE-T1-R4 | Upstream performance claims: ~16% cheaper, 47% fewer tokens, 58% fewer tool calls, 22% faster | upstream landing page (FETCH_VERIFIED as upstream claim) | none (no CVF benchmark owner yet) | `BLOCK_UNTIL_CVF_BENCHMARK` | These are upstream-measured across their 7 codebases. They cannot become CVF claims without CVF-owned benchmark proof. |
| CGE-T1-R5 | Upstream watcher/daemon auto-sync (FSEvents/inotify, 2s debounce, `daemon` command) | upstream landing page | none (CVF has no watcher lane) | `DEFER_REQUIRES_RUNTIME_GC018` | Watcher/daemon is runtime behavior. Not authorized in CGE-T1; requires a separate runtime GC-018 if ever pursued. |
| CGE-T1-R6 | Upstream MCP server wiring + agent auto-config (8 `codegraph_*` tools across 8 agents) | upstream landing page | CVF MCP server is a separate owned surface | `DEFER_REQUIRES_MCP_BOUNDARY_WORK_ORDER` | Agent config mutation and MCP routing are high-risk. Requires a dedicated MCP boundary work order, not direct adoption. |
| CGE-T1-R7 | Impact radius / callers / callees / files / status vocabulary | upstream tools; local `impact-analysis-service`, `CVF_GRAPH_BACKED_REVIEW_PROTOCOL.md` | `graph-schema.ts` `queryImpact` (line 64); `task-query-mapper.ts` | `ADAPT_TO_EXISTING_LPF_GRAPH` | Useful vocabulary only. `queryImpact` already exists; scope is vocabulary/template alignment, not new capability. |
| CGE-T1-R8 | Stale-index warning and fallback discipline | local `graph-staleness-service.ts`, `CVF_GRAPH_STALENESS_AND_SYNC_POLICY_2026-06-19.md` | memory-derived graph boundary (derived/advisory only) | `ADAPT_AS_GOVERNANCE_RULE` | Absorb as advisory freshness/fallback rule. Must not auto-grant authority; direct-read fallback required before review/freeze claims. |
| CGE-T1-R9 | Graph context receipt and query-plan templates | local `docs/templates/code-intelligence/*.template.md`; `CVF_GRAPH_CONTEXT_RECEIPT_PROTOCOL_2026-06-19.md` | existing receipt/authority surfaces; `GraphAuthorityReceipt` | `ADAPT_AFTER_FIELD_NORMALIZATION` | Docs use `snake_case`; CVF TS/JSON use `camelCase`. Normalize to `camelCase` and extend existing receipt owner before use (CGE-T2). |
| CGE-T1-R10 | Local package scaffold/test-runner proof | no `package.json`/test runner in capability folder (`find` returned none) | n/a | `BLOCK_AS_PROOF` | Local package presence is not proof of runnable capability. Treat as scaffold/reference, not runtime proof. |
| CGE-T1-R11 | Upstream `init` creating `.codegraph/` index + local SQLite/FTS5 store | upstream landing page | PBR04 already owns optional SQLite persistence | `REJECT_DIRECT` | CVF must not run `codegraph init` or adopt `.codegraph/`. Durable graph store is already a closed CVF capability. |

All five GC-018 required rows are present: R1 (`freezeAllowed` BLOCK), R2
(LPF-like `REJECT_PARALLEL_CORE`), R3 (CodeGraph/KGR `DEDUP_DECISION_REQUIRED`),
R4 (performance `BLOCK_UNTIL_CVF_BENCHMARK`), R5/R6 (watcher/MCP DEFER or
REJECT_DIRECT).

## CodeGraph vs KGR Dedupe Decision

Decision: `DEDUP_RESOLVE_TOWARD_KGR_AND_LPF`.

Basis (source-verified): KGR pre-review already plans the in-repo graph
retrieval lane that CodeGraph targets. KGR1-T3 plans
`buildKnowledgeGraph(files)` as a deterministic in-process graph with no
external AST library (line 217), and KGR1-T4 wires graph nodes into
`MemoryRetrievalCandidate` via `evaluateRetrievalRequest` (line 218). KGR
explicitly forbids importing external graph libraries (line 233). CVF already
owns the graph core (GraphKnowledgeService, SymbolIndex, GraphSQLiteStore).

Therefore CodeGraph is not a new lane. Useful CodeGraph ideas (impact-radius
vocabulary R7, stale-index discipline R8, receipt/query-plan templates R9) are
adapted into the existing LPF graph owners and the KGR plan. The CodeGraph
implementation, MCP wiring, watcher, and SQLite store are rejected or deferred
because CVF already owns or has deferred equivalents. No parallel
graph-retrieval lane is opened.

## ACE-R1 Remains Parked

ACE-R1 (Agent Coding Evidence Replay) remains parked. CGE-T4 checker candidates
(reject graph-only freeze; require stale-index fallback before review/freeze;
prevent graph impact radius from auto-expanding work-order scope) are useful
feeders for ACE-R1 but are not prerequisites. This matrix does not reopen,
re-source-verify, or reorder ACE-R1. Reopening requires a separate operator
decision and is lower leverage than completing CGE absorption first.

## Negative Search And Collision Result

| Token | Result | Disposition |
|---|---|---|
| `freezeAllowed` | found only in copied package, not in current CVF source | external finding; BLOCK row, not a current CVF defect |
| `GraphKnowledgeService` | found in current LPF `graph-schema.ts` line 62 | binding CVF owner |
| `GraphSQLiteStore` | found in current LPF storage owner | binding CVF owner; package SQLite store is parallel-core reject |
| `KGR` | found in KGR pre-review (planned retrieval lane) | binding prior owner; dedupe target |
| upstream performance facts | fetched from upstream landing page only | upstream claim; benchmark-gated, not CVF proof |

No CodeGraph idea was promoted as a parallel core. Where a CodeGraph idea
collided with KGR or LPF, it was routed to adapt-to-existing-owner or
dedupe/reject, never parallel import.

## Risk / Corrective Action

Risk level: R1 documentation/review-only.

Corrective action carried to any future lane: implementation, checker/template
authoring, watcher/daemon, MCP wiring, benchmark execution, root registry
mutation, and ACE-R1 work each require a separate governed packet. This matrix
authorizes none of them.

## Evidence

executionBaseHead: `4d004c42` (confirmed via `git rev-parse --short HEAD`).

Local CodeGraph inventory: `find CodeGraph/CVF_Code_Intelligence_Capability -type f`
returned 89 files. `.gitignore` line 72 already contains `CodeGraph/`.

Upstream access result: VERIFIED via WebFetch of
`https://github.com/colbymchenry/codegraph`. Confirmed 8 `codegraph_*` tools,
CLI including `init/index/sync/daemon/telemetry`, MCP server wiring across 8
agents, native file watcher with ~2s debounce, SQLite + FTS5 store at
`.codegraph/codegraph.db`, and benchmark claims (~16% cheaper, 47% fewer
tokens, 58% fewer tool calls, 22% faster across 7 codebases) recorded as
upstream claims only.

Current CVF owner verification: `GraphKnowledgeService` (graph-schema.ts:62),
`SymbolIndex` + `buildSymbolIndexFromGraph` (symbol-index.ts:13,40),
`authorityModel` + `canBypassPolicy: false` (graph-authority-gate.ts:34,36,124),
`queryImpact` (graph-schema.ts:64).

Actual `git status --short` at return:

```text
 M .gitignore
?? docs/baselines/CVF_GC018_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_2026-06-20.md
?? docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CLAUDE_REBUTTAL_2026-06-20.md
?? docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CODEX_CLASSIFICATION_2026-06-20.md
?? docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_REBUTTAL_PACKET_FOR_CLAUDE_2026-06-20.md
?? docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md
?? docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_FOR_CLAUDE_2026-06-20.md
```

Worker-return fast gate: deferred to Codex review run
(`python governance/compat/run_worker_return_fast_gate.py`); worker records the
pending status above and commits nothing.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | CGE-T1 external absorption triage completion artifact |
| claimDisposition | N/A with reason: this artifact rejects runtime/direct-interception/universal-control claims |
| receiptEvidence | N/A with reason: no Delta receipt/action evidence is used |
| actionEvidence | N/A with reason: no execution action is claimed |
| invocationBoundary | no wrapper/proxy, mandatory invocation, direct IDE/shell/git/filesystem interception, or arbitrary command execution |
| interceptionBoundary | no direct interception claim |
| claimLanguage | triage completion only |
| forbiddenExpansion | no runtime, MCP, benchmark, provider/live, public-sync, readiness, registry mutation, ACE-R1 reopening, or universal governed-coding-control claim |

## Rescan Intelligence Hardening

- Original source artifact: `https://github.com/colbymchenry/codegraph` and
  local copied folder `CodeGraph/CVF_Code_Intelligence_Capability/`.
- Predecessor intake artifact:
  `docs/baselines/CVF_GC018_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_2026-06-20.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because CGE-T1 converts the
  authorized triage scope into row-level dispositions.
- Routing matrix status:
  - `DO_NOW`: this triage matrix maps external ideas to existing LPF/KGR owners.
  - `RESOLVED_BY_DESIGN`: adapt rows cite existing owners before recommendation.
  - `SEPARATE_RUNTIME_TRANCHE`: implementation, MCP, watcher/daemon, benchmark,
    provider/live proof, root registry mutation.
  - `STRATEGIC_OPERATOR_DECISION`: whether to open any post-T1 implementation
    lane.
  - `OUT_OF_SCOPE`: public-sync, direct interception, universal governed-coding
    control, ACE-R1 reopening.
- Semantic sampling status: `PARTIAL_TARGETED`, limited to triage rows and
  blocker carry-forward bounded by the Scan Depth Ledger.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | CodeGraph remains external/advisory input. |
| CHANGED_DISPOSITION | CGE-T0 blockers became mandatory T1 rows R1 and R2. |
| NEW_FINDING | 11 local LPF-like files enumerated; upstream facts FETCH_VERIFIED as upstream claims. |
| REMOVED_OR_REJECTED | Runtime/source/MCP/watcher/public-sync/provider/live/ACE-R1 remain out of scope. |

### Follow-Up Routing Matrix

| Lane | Disposition |
|---|---|
| DO_NOW | This CGE-T1 triage matrix maps external ideas to existing LPF/KGR owners. |
| RESOLVED_BY_DESIGN | Adapt rows R7/R8/R9 cite existing owners before recommendation. |
| SEPARATE_RUNTIME_TRANCHE | Implementation, MCP wiring, watcher/daemon, benchmark, provider/live proof, root registry mutation. |
| STRATEGIC_OPERATOR_DECISION | Whether to open a post-T1 implementation or ACE-R1-adjacent lane. |
| DEFER | CodeGraph implementation, MCP, watcher/daemon, root registry mutation, ACE-R1. |
| OUT_OF_SCOPE | Public-sync, provider/live proof, direct interception, universal governed-coding-control claim. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| CGE-T1-RS1 | Triage Matrix R1 | `freezeAllowed` is graph-only | `BLOCK` | Could graph freshness alone grant freeze? | PASS_BLOCKED |
| CGE-T1-RS2 | Triage Matrix R2 | package ships LPF-like core files | `REJECT_PARALLEL_CORE` | Could these be copied as bridge files? | PASS_BOUNDARY |
| CGE-T1-RS3 | Triage Matrix R4 | upstream performance numbers | `BLOCK_UNTIL_CVF_BENCHMARK` | Could upstream numbers become CVF claims? | PASS_BENCHMARK_GATED |

## Claim Boundary

This completion artifact records a source-verified absorption triage matrix
only. It does not make CodeGraph canonical, mutate runtime or source, install
or run CodeGraph, wire MCP, enable watcher/daemon behavior, prove performance,
publish public-facing updates, reopen ACE-R1, or claim governed-coding control,
production, or readiness.

## Epistemic Process Block

Expected Result / Prediction: before verification, the prediction was that
CVF already owns a graph foundation, so most CodeGraph implementation surfaces
would be redundant; that the local package would carry a graph-derived freeze
authority leak; and that CodeGraph would overlap the planned KGR retrieval lane.

Evidence Comparison: the prediction held. `graph-receipt-service.ts` lines
28-31 confirmed the graph-only `freezeAllowed` leak. The current LPF owners
(`GraphKnowledgeService` graph-schema.ts:62, `SymbolIndex` symbol-index.ts:13,
`canBypassPolicy: false` graph-authority-gate.ts:36) confirmed the graph
foundation exists. KGR1-T3/T4 (lines 217-218) confirmed the overlapping
retrieval lane. Upstream WebFetch confirmed the 8-tool/MCP/daemon/SQLite shape
and the four benchmark numbers as upstream claims.

Contradiction Or Gap Disposition: one expectation was partially corrected.
The packet framed package LPF files as bridge files; enumeration showed 11
parallel-core files, so the disposition was hardened from copy-soft to
`REJECT_PARALLEL_CORE`. No source contradicted a BLOCK or DEFER row. Remaining
gap: upstream facts are landing-page level only, not independently
benchmark-replicated, which is why R4 stays `BLOCK_UNTIL_CVF_BENCHMARK`.

Claim Update: updated belief is that CodeGraph contributes vocabulary, stale-
index discipline, and receipt/query-plan templates as adapt candidates, while
its implementation, MCP wiring, watcher, and SQLite store are rejected or
deferred against existing CVF/KGR owners. No CVF runtime, performance, or
readiness claim is asserted by this matrix.

## Finding-To-Governance Learning Disposition

- Defect class: `ORCHESTRATOR_PACKET_GAP`
- Learning lane: `GOVERNANCE_CONTROL_PLANE`
- Disposition: `DESIGN_REVIEW_REQUIRED`
- Next action: carry R1/R2 blockers and the CodeGraph/KGR dedupe into any future
  CGE implementation decision; do not open implementation from this matrix.
- Runtime/provider/cost learning lane: `N/A_WITH_REASON` - upstream performance
  and cost claims remain blocked until a separate CVF benchmark or proof lane.

| Finding or lesson | Disposition | Reason |
|---|---|---|
| Graph-derived `freezeAllowed` is an authority-leak pattern to block at receipt level | DESIGN_REVIEW_REQUIRED | Graph evidence must stay advisory; freeze authority belongs to review/test/fallback. |
| External packages can ship parallel-core files under existing owner paths | DESIGN_REVIEW_REQUIRED | Owner-surface mapping must precede any copy; parallel cores are rejected. |
| Upstream performance claims require CVF benchmark before any CVF use | DESIGN_REVIEW_REQUIRED | External-measured savings are not CVF proof. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance external absorption triage. No public-sync remote,
public commit, public artifact path, or public claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude worker material |
| Provider or surface | Claude worker workspace |
| Session or invocation | 2026-06-20 CGE-T1 CodeGraph external absorption triage |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read/Grep/find inventory, WebFetch of upstream, git status |
| Target paths | this completion artifact plus pending CGE-T0 dispatch/rebuttal/classification artifacts in the same reviewer batch |
| Allowed scope source | CGE-T1 work order and GC-018 |
| Before status evidence | clean committed base `4d004c42` with known untracked CGE inputs present |
| After status evidence | `git status --short` recorded above; current reviewer batch contains `.gitignore`, CGE-T1 baseline/work order, CGE-T0 rebuttal/classification packets, and this completion artifact |
| Diff evidence | reviewer batch pending as uncommitted governed artifacts; no runtime/source/test/public/provider files changed |
| Approval boundary | external absorption triage only |
| Claim boundary | no implementation, runtime, MCP, benchmark, provider/live proof, public-sync, registry mutation, ACE-R1 reopening, readiness, or universal governed-coding-control claim |
| Agent type | Claude worker |
| Invocation ID | `cge-t1-codegraph-external-absorption-triage-matrix-2026-06-20` |
| Expected manifest | `.gitignore`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/cge-t1-lpf-graph-owner-source-surfaces.json`; `docs/baselines/CVF_GC018_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CLAUDE_REBUTTAL_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CODEX_CLASSIFICATION_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_REBUTTAL_PACKET_FOR_CLAUDE_2026-06-20.md`; `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_FOR_CLAUDE_2026-06-20.md` |
| Actual changed set | `.gitignore`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/cge-t1-lpf-graph-owner-source-surfaces.json`; `docs/baselines/CVF_GC018_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CLAUDE_REBUTTAL_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CODEX_CLASSIFICATION_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_REBUTTAL_PACKET_FOR_CLAUDE_2026-06-20.md`; `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_FOR_CLAUDE_2026-06-20.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Worker Boundary Statement

Actions taken: read-only file reads, directory enumeration, targeted grep, one
WebFetch of the public upstream repository, and git status. Actions not taken:
no CodeGraph install, no `codegraph init`, no npm install, no MCP wiring, no
watcher or daemon, no `.codegraph/` creation, no runtime/source/test edits, no
root registry mutation, no commit, no provider/live or benchmark execution, no
public-sync, and no ACE-R1 reopening.

## Return Disposition

`COMPLETE_PENDING_REVIEW`. One uncommitted artifact created at the required
path. Codex owns review, worker-return fast gate run, any allowed repair,
committed-range closure gates, final commit, and session sync if next-move
surfaces change.
