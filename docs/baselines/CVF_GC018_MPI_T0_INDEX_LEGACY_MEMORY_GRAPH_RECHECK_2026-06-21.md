# CVF GC-018 - MPI-T0 INDEX Legacy Memory Graph Recheck

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-21

docType: baseline

dispatchBaseHead: acb2b980

Batch ID: MPI-T0

## Purpose

Authorize the prerequisite Memory Plane Integration tranche before MPI-T1:
bounded legacy memory/KGR/graph/context recheck plus the INDEX classification
standard.

MPI-T0 verifies Claude's memory-plane readout, rechecks relevant raw legacy
folders, separates already absorbed current owner surfaces from unabsorbed
knowledge, and defines INDEX as the classification vocabulary for CVF
plane/layer/surface/corpus work.

## Operator Authorization

The operator clarified on 2026-06-21 that CVF needs another legacy scan pass
for memory/KGR/graph/context knowledge before the Memory Plane upgrade/layer
split, and that INDEX should become the standard vocabulary for classification
work in CVF.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-21 memory/KGR legacy recheck and INDEX standard clarification | ACCEPT |
| MPI roadmap | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | ACCEPT |
| Codex rebuttal | `docs/reviews/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_CODEX_REBUTTAL_2026-06-21.md` | ACCEPT |
| Legacy coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` row `MEM-001` | SOURCE_AUTHORITY_FOR_RECHECK_NEED |
| Corpus registry Graphify entry | `docs/corpus-intelligence/registry/entries/legacy-cvf-important-graphify.json` | SOURCE_AUTHORITY_FOR_GRAPHIFY_STATUS |
| KGR pre-review | `docs/reference/CVF_KGR_ABSORPTION_PREREVIEW_2026-06-01.md` | SOURCE_AUTHORITY_FOR_KGR_BOUNDARY |
| KGR1 roadmap/review | `docs/roadmaps/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_ROADMAP_2026-06-01.md`; `docs/reviews/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_LOCAL_REVIEW_2026-06-02.md` | SOURCE_AUTHORITY_FOR_CURRENT_KGR_OWNER |
| CI1-T11 roadmap and MLW0 map | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md`; `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | SOURCE_AUTHORITY_FOR_PRIOR_MEMORY_ABSORPTION |

Provider-specific memory, chat memory, and private agent-local files are not
CVF source authority. Raw legacy files may be read only as recheck inputs and
must be dispositioned before any value is promoted to governed CVF artifacts.
MPI-T0 is the first governed use case that must apply the INDEX standard.
MPI-T0 does not implement machine enforcement. A follow-up checker tranche
after MPI-T0 closure is required before claiming INDEX is governance-enforced
for future internal/external agent classification work.

## Scope / Owner Boundary

Allowed worker scope:

- create `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md`;
- create `docs/reviews/CVF_MPI_T0_INDEX_LEGACY_MEMORY_GRAPH_RECHECK_WORKER_RETURN_2026-06-21.md`;
- read and enumerate the bounded legacy/source inputs named in this baseline
  and work order;
- classify findings as index inputs, already-absorbed current owners, partial
  recheck gaps, deferrals, or direct-runtime rejections.

Forbidden worker scope:

- no edits to `EXTENSIONS/**`, runtime routes, tests, scan registry aggregate or
  per-entry sources, generated JSON, session state, active handoff, public-sync,
  MCP packages, dependency manifests, or `.github/**`;
- no runtime implementation, vector DB, embedding store, graph persistence,
  `cvf graph` CLI, external graph dependency, provider/live proof, public
  claim, generator run, drift checker run, queue, daemon, watcher, wrapper or
  proxy enforcement, direct interception, arbitrary command execution, or
  EDIT/COMMIT execution;
- no INDEX checker implementation, hook-chain wiring, autorun integration, or
  governance/compat test expansion;
- no implementation of MPI-T1/T2/T3/T4, KGR expansion, MEMCON expansion, LSC,
  AAF, CGE, ACE, or MLW runtime work.

Risk ceiling: R0 documentation/reference recheck only.

## Decision / Baseline / Proposed Tranche

Baseline decision: MPI-T0 is closed with bounded pass after reviewer acceptance
of the INDEX standard and corrected worker return.

Proposed tranche: `MPI-T0 INDEX Legacy Memory/Graph Recheck`.

Dependency release: MPI-T1 is released for worker dispatch by
`docs/reviews/CVF_MPI_T0_INDEX_LEGACY_MEMORY_GRAPH_RECHECK_COMPLETION_2026-06-21.md`.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` with only:

- `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md`
- `docs/reviews/CVF_MPI_T0_INDEX_LEGACY_MEMORY_GRAPH_RECHECK_WORKER_RETURN_2026-06-21.md`

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| MEM-001 requires recheck before new memory/scan foundation work | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | Initial Coverage Ledger | `MEM-001` | Legacy coverage index | VALUE_SET | ACCEPT |
| Graphify corpus is registered with findings and partial absorption | `docs/corpus-intelligence/registry/entries/legacy-cvf-important-graphify.json` | registry entry | `legacy-cvf-important-graphify`; `fileCount`; `findings` | Corpus Scan Registry entry | VALUE_SET | ACCEPT |
| KGR pre-review separates Memory Plane from KGR and records partial reabsorption | `docs/reference/CVF_KGR_ABSORPTION_PREREVIEW_2026-06-01.md` | Why This Is NOT Memory Plane; Prior Absorption History | Memory Plane vs KGR | KGR pre-review | VALUE_SET | ACCEPT |
| KGR1 bounded current owner exists | `docs/roadmaps/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_ROADMAP_2026-06-01.md`; `docs/reviews/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_LOCAL_REVIEW_2026-06-02.md` | Work Plan; Source Verification; Claim Boundary | `knowledge-graph-store.ts`; `knowledge-graph-builder.ts`; `graph_search` | KGR1 roadmap/review | EXISTS | ACCEPT |
| CI1-T11 and MLW0 already cover part of memory/learning absorption | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md`; `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | Purpose and source map | CI1-T11; MLW0 | Prior absorption owners | EXISTS | ACCEPT |
| Raw Graphify legacy folder exists as bounded recheck input | `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/` | filesystem path | legacy folder | Raw legacy source | EXISTS | ACCEPT_AS_RECHECK_INPUT |
| Raw code-review-graph legacy folder exists as bounded recheck input | `.private_reference/legacy/CVF ADD/code-review-graph/` | filesystem path | legacy folder | Raw legacy source | EXISTS | ACCEPT_AS_RECHECK_INPUT |

## Bounded Legacy Recheck Inputs

Worker must enumerate and read, where present:

- `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/`
- `.private_reference/legacy/CVF ADD/code-review-graph/`
- `.private_reference/legacy/CVF 16.5/tolaria/CVF_MARKDOWN_KNOWLEDGE_GRAPH.md`
- `.private_reference/legacy/CVF 16.5/agentmemory/`
- `.private_reference/legacy/CVF_Important/ADDING_LEARNING PLANE/`
- `.private_reference/legacy/CVF_Important/ADDING_RAG ARCHITECTURE/`
- `.private_reference/legacy/CVF_Important/ADDING_CONTEXT ENGINE/`
- `.private_reference/legacy/CVF_Important/ADDING_CONTEXT CONTROL/`
- `.private_reference/legacy/CVF_Important/Knowledge Base_Palace/`
- `.private_reference/legacy/CVF_Important/Knowledge Base_LLM-Powered/`

Unreadable or absent paths must be recorded as `BLOCKED_UNREADABLE` or
`SKIPPED_WITH_REASON`, not silently ignored.

## Required Classification Dispositions

| Disposition | Meaning |
|---|---|
| `ACCEPT_AS_INDEX_INPUT` | useful for INDEX vocabulary or plane/layer map |
| `ALREADY_ABSORBED_CURRENT_OWNER` | value already has governed current owner |
| `PARTIAL_RECHECK_REQUIRED` | value is known but not fully absorbed/verified |
| `DEFER_TO_SEPARATE_GC018` | useful but needs separate tranche |
| `REJECT_DIRECT_RUNTIME_PROMOTION` | legacy idea must not become runtime authority |
| `BLOCKED_UNREADABLE` | source could not be read |
| `SKIPPED_WITH_REASON` | source is absent or outside assigned scope |

## Evidence / Verification

Required pre-dispatch verification before dispatch commit:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base acb2b980 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base acb2b980 --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base acb2b980 --head HEAD --enforce
```

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Legacy source family |
| Chain map route | legacy/corpus input -> coverage index lookup -> bounded recheck -> INDEX standard -> future MPI-T1 dependency release |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | MPI-T0 INDEX Legacy Memory/Graph Recheck |
| Disposition | ADAPT_AS_BOUNDED_RECHECK |
| Claim boundary | legacy files remain input only; no runtime/source mutation or direct authority promotion |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index requirement | APPLICABLE - `MEM-001` |
| Coverage index path | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Coverage-index row evidence | `MEM-001` status `PARTIAL_RECHECK_REQUIRED`; next action requires reconcile before new memory/scan foundation work |
| MPI-T0 disposition | SATISFIES_RECHECK_PREREQUISITE_IF_CLOSED |
| Boundary | bounded recheck and INDEX standard only; no direct legacy runtime promotion |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MPI-T0 legacy recheck and INDEX standard only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no runtime receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | documentation/reference recheck only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | legacy recheck, classification, and INDEX standard wording only |
| forbiddenExpansion | runtime mutation, vector DB, graph persistence, provider/live, public-sync, CLI/MCP adapter, queue/daemon, watcher, readiness, universal control |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation area | INDEX classification standard; Memory/KGR legacy recheck |
| Stable reference output | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` |
| Worker return output | `docs/reviews/CVF_MPI_T0_INDEX_LEGACY_MEMORY_GRAPH_RECHECK_WORKER_RETURN_2026-06-21.md` |
| Generated aggregate impact | N/A with reason: no generated aggregate edit is authorized |
| Runtime impact | N/A with reason: no runtime/source/test edit is authorized |

## Corpus Completeness And Report Integrity

- Corpus task class: BOUNDED_LEGACY_RECHECK.
- Corpus root: bounded inputs listed in `Bounded Legacy Recheck Inputs`.
- Snapshot time: worker records actual execution date/time.
- Enumeration command:
  `Get-ChildItem -LiteralPath <bounded-input-path> -Force -Recurse -File`
  repeated for each listed bounded input path that exists; worker must record
  the actual command and expanded path list.
- Manifest artifact or inline manifest: worker-return artifact must include
  inline manifest.
- Manifest hash: worker may record `N/A_WITH_REASON` unless a manifest file is
  created.
- Processing ledger artifact or inline ledger: worker-return artifact must
  include inline processing ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline worker-return manifest; ledger_terminal=one terminal status per manifest entry; exclusions=declared below; unresolved=0 or explicit `BLOCKED_WITH_REASON`.
- Unresolved files: must be 0 or listed with blocker.
- Declared exclusions: runtime implementation, generated registry mutation,
  provider/live proof, public-sync, and CLI/MCP adapter.
- Unreadable or unsupported files: worker must list each path or state 0.
- Aggregation check: N/A with reason: no generated aggregate is created.
- Drift check: N/A with reason: no generated aggregate is changed.
- Output traceability: Required Deliverables, Manifest, Processing Ledger, and
  Finding Matrix.
- Adversarial verification: reviewer/closer must run reviewer-fast or stricter
  applicable gate before acceptance.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance legacy recheck and INDEX standard only. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Claim Boundary

This baseline authorizes only MPI-T0 bounded legacy memory/KGR/graph/context
recheck and an INDEX classification standard. It does not authorize
runtime implementation, vector DB, embedding store, graph persistence, KGR CLI,
provider/live proof, public-sync, direct interception, queue/daemon, watcher,
readiness, or universal governed-coding control.

## Reviewer Closure Update

| Field | Disposition |
|---|---|
| Completion review | `docs/reviews/CVF_MPI_T0_INDEX_LEGACY_MEMORY_GRAPH_RECHECK_COMPLETION_2026-06-21.md` |
| Worker return | `docs/reviews/CVF_MPI_T0_INDEX_LEGACY_MEMORY_GRAPH_RECHECK_WORKER_RETURN_2026-06-21.md` |
| INDEX standard | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` |
| Final disposition | CLOSED_PASS_BOUNDED |
| Dependency released | MPI-T1 Memory Plane Front-Door Map |
| Reviewer correction | BLI-01 Graphify `Thong_tin.md` corrected from absent to READ/ACCEPT_AS_INDEX_INPUT in worker return |
