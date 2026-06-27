# CVF Agent Work Order - CGE-T1 CodeGraph External Absorption Triage Matrix

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-20

docType: work_order

dispatchBaseHead: 4d004c42

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Implementer/worker (Claude). Codex is reviewer/closer.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_FOR_CLAUDE_2026-06-20.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: confirm with `git rev-parse --short HEAD` at worker start.

Current-time notes: CGE-T1 is a triage matrix only. It absorbs useful ideas from
the external CodeGraph repo and the local copied CodeGraph package into CVF
governance language without making CodeGraph canonical.

Do-not-misread notes: do not install, initialize, run, benchmark, or wire
CodeGraph. Do not copy CodeGraph files into canonical CVF runtime/reference
paths. Do not edit `EXTENSIONS/**`, `.codegraph/**`, root lifecycle registry,
public-sync, provider/live proof, MCP wiring, watcher/daemon, or ACE-R1.

Required first actions: read this work order, read the CGE-T1 GC-018 baseline,
read the three CGE-T0 packets, read the external absorption chain map and
finding workflow, inventory the local `CodeGraph/CVF_Code_Intelligence_Capability/`
folder, and source-verify existing CVF graph owner surfaces before writing.

Return contract: return `COMPLETE_PENDING_REVIEW` with one uncommitted artifact
at `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md`,
actual `git status --short`, source inventory, required triage rows, CodeGraph
vs KGR dedupe decision, ACE-R1 parking note, worker-return fast gate result, and
no commit. If blocked, return `BLOCKED_WITH_REASON` and name the exact source
or gate that blocked the work.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two agents, one role each: Claude authors triage matrix; Codex reviews/closes |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=4d004c42`; `executionBaseHead` confirmed by Claude; `closureBaseHead` set by Codex before closure commit |
| changedSetScope(phase) | worker creates only the CGE-T1 completion artifact; Codex owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one Claude worker-return trace covers the pending completion artifact; one Codex trace covers review/closure |
| commitOwner(phase) | Claude commits nothing (`WORKER_MUST_NOT_COMMIT`); Codex owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix CGE-T1 worker return with runtime, public-sync, registry mutation, or ACE-R1 changes |
| nextMoveSurfaces | Codex updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | Codex is the designated reviewer and closer |

## Purpose

Create a source-verified triage matrix for CodeGraph external absorption. The
matrix must decide, row by row, what CVF can absorb now as doctrine, adapt to
existing LPF/KGR owners, defer to later GC-018/work orders, reject as direct
import or parallel core, or block until CVF proof exists.

## Agent Roles

| Role | Owner |
|---|---|
| Dispatcher | Codex |
| Worker | Claude |
| Reviewer | Codex |
| Closer | Codex |
| Session-sync steward | Codex after review, only if next-move surfaces change |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-20: Claude should do CGE-T1 | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_2026-06-20.md` | ACCEPT |
| CGE-T0 review packet | `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_REBUTTAL_PACKET_FOR_CLAUDE_2026-06-20.md` | ACCEPT |
| CGE-T0 Claude rebuttal | `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CLAUDE_REBUTTAL_2026-06-20.md` | ACCEPT |
| CGE-T0 Codex classification | `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CODEX_CLASSIFICATION_2026-06-20.md` | ACCEPT |
| External absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | ACCEPT |
| External finding workflow | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- read and cite upstream `https://github.com/colbymchenry/codegraph` if
  accessible in the worker environment;
- read, inventory, and sample the local copied package
  `CodeGraph/CVF_Code_Intelligence_Capability/`;
- read existing CVF graph owner surfaces and prior graph absorption artifacts;
- create the single CGE-T1 completion artifact named in the return contract;
- run local read-only commands and governance gates required by this work order.

Forbidden scope:

- no runtime/source edits under `EXTENSIONS/**`;
- no direct copy/import of CodeGraph package files into CVF canonical runtime,
  docs/reference, tools, scripts, or governance paths;
- no CodeGraph install, dependency install, package execution, `.codegraph/`
  initialization, watcher, daemon, MCP server, or auto-config;
- no wrapper/proxy enforcement, direct IDE/shell/git/filesystem interception, or
  arbitrary command execution lane;
- no provider/live proof, benchmark execution, public-sync, push, release,
  production/public readiness, or universal governed-coding-control claim;
- no root lifecycle registry mutation;
- no ACE-R1 reopening or execution.

Risk ceiling: R1 documentation/review-only.

## Required First Reads

- `docs/baselines/CVF_GC018_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_2026-06-20.md`
- `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_REBUTTAL_PACKET_FOR_CLAUDE_2026-06-20.md`
- `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CLAUDE_REBUTTAL_2026-06-20.md`
- `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CODEX_CLASSIFICATION_2026-06-20.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_AND_EXTENSION_PRIORITY_STANDARD_2026-04-13.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
- `docs/reference/CVF_KGR_ABSORPTION_PREREVIEW_2026-06-01.md`
- `docs/reference/CVF_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md`
- `docs/work_orders/CVF_WO_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_2026-06-01.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/graph-schema.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/index/symbol-index.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/storage/graph-sqlite-store.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/authority/graph-authority-gate.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context_builder/graph/task-query-mapper.ts`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 4d004c42 --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 4d004c42 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 4d004c42 --head HEAD --enforce
```

Expected result: gates pass or worker returns `BLOCKED_WITH_REASON` before
writing the completion artifact.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| CGE-T0 accepts Claude `APPROVE_WITH_FINDINGS` and allows CGE-T1 only as doctrine/governance-first triage | `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CODEX_CLASSIFICATION_2026-06-20.md` | lines 76-87 | `APPROVE_WITH_FINDINGS`; `CGE-T1`; `freezeAllowed`; `REJECT_PARALLEL_CORE`; `BLOCK_UNTIL_CVF_BENCHMARK` | CGE-T0 Codex classification | ACCEPT |
| Claude rebuttal requires `freezeAllowed` BLOCK and local LPF-like graph files `REJECT_PARALLEL_CORE` | `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CLAUDE_REBUTTAL_2026-06-20.md` | lines 73-92 and 219-225 | `freezeAllowed`; `REJECT_PARALLEL_CORE` | CGE-T0 Claude rebuttal | ACCEPT |
| External repo or copied folder is a canonical chain-map input type | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | Input Type Router | `External repo or copied folder` | external knowledge absorption chain map | ACCEPT |
| External returned-output rows use the external finding absorption workflow | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | absorption table fields | `Claim boundary` | external finding absorption workflow | ACCEPT |
| Existing CVF graph service owner surface exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/graph-schema.ts` | line 61 | `GraphKnowledgeService` | LPF graph schema | ACCEPT |
| Existing CVF symbol index owner surface exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/index/symbol-index.ts` | lines 13 and 40-80 | `SymbolIndex`; `buildSymbolIndexFromGraph`; `createInMemoryGraphKnowledgeService` | LPF symbol index | ACCEPT |
| Existing CVF graph persistence owner surface exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/storage/graph-sqlite-store.ts` | lines 36-174 | `GraphSQLiteStore` | LPF graph sqlite store | ACCEPT |
| Existing graph authority gate declares advisory authority and no policy bypass | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/authority/graph-authority-gate.ts` | lines 34-36 and 122-124 | `authorityModel`; `canBypassPolicy` | LPF graph authority gate | ACCEPT |
| Existing task graph query mapper owner surface exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context_builder/graph/task-query-mapper.ts` | lines 1 and 56 | `SymbolIndex` | LPF task query mapper | ACCEPT |
| KGR pre-review already covers graph-builder/retrieval overlap and blocks direct external library import without separate work | `docs/reference/CVF_KGR_ABSORPTION_PREREVIEW_2026-06-01.md` | lines 38-72 and 208-242 | `KGR1-T3`; `KGR1-T4`; `Do not import external graph libraries` | KGR absorption pre-review | ACCEPT |
| Memory-derived graph boundary says graph views are derived/advisory and public/runtime claims need separate proof | `docs/reference/CVF_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md` | lines 23-53 | `Derived views`; `graph`; `Public or runtime claims` | memory-derived graph boundary | ACCEPT |

## Non-Authority Input Inventory

| Input | Evidence | Disposition |
|---|---|---|
| Local copied package | `CodeGraph/CVF_Code_Intelligence_Capability/`; dispatch inventory observed 89 files | External/advisory input only; not Source Verification authority |
| Upstream repository | `https://github.com/colbymchenry/codegraph` | Worker verifies directly if accessible; otherwise upstream-dependent rows remain blocked/deferred/benchmark-gated |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | External repo or copied folder -> lifecycle classification candidate -> absorption triage matrix -> CVF owner-surface disposition -> later GC-018/work order only if implementation is separately authorized |
| Owner surface | CGE-T1 completion artifact; existing LPF graph owner surfaces; KGR pre-review; memory-derived graph boundary |
| Disposition | Row-level `ADAPT`, `DEFER`, `REJECT`, or `BLOCK`; no direct import |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Claim boundary | External absorption triage only; no runtime, MCP, benchmark, provider/live proof, public-sync, registry mutation, ACE-R1 reopening, readiness, or universal governed-coding-control claim |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | CGE-T1 external absorption triage work order |
| claimDisposition | N/A with reason: work order rejects runtime/direct-interception/universal-control claims |
| receiptEvidence | N/A with reason: no Delta receipt/action evidence is used |
| actionEvidence | N/A with reason: no execution action is claimed |
| invocationBoundary | no wrapper/proxy, mandatory invocation, direct IDE/shell/git/filesystem interception, or arbitrary command execution |
| interceptionBoundary | no direct interception claim |
| claimLanguage | triage work order only |
| forbiddenExpansion | no runtime, MCP, benchmark, provider/live, public-sync, readiness, registry mutation, ACE-R1 reopening, or universal governed-coding-control claim |

## Intake Role Routing Decision

- Intake summary: operator selected CGE-T1 for Claude after Codex accepted the
  CGE-T0 Claude rebuttal with findings.
- Scope assessment: external repo/copied-folder absorption triage; read-only and
  documentation/review-only.
- Risk sensitivity: R1; no runtime/source/provider/live/public-sync/registry
  action.
- Selected role route: `MULTI_AGENT_SINGLE_ROLE`.
- Role separation basis: Claude authors the triage matrix; Codex reviews,
  commits, and closes if accepted.
- Escalation condition: implementation, CodeGraph execution, registry mutation,
  ACE-R1 reopening, public-sync, provider/live proof, benchmark claims, or
  claim-boundary expansion.

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Legacy coverage applicability | NOT_APPLICABLE_WITH_REASON |
| Reason | CGE-T1 handles an external repo/copied folder and prior graph owner surfaces, not a raw `.private_reference/legacy` corpus scan. |
| Coverage-index relationship | Prior graph coverage artifacts are read as dedupe/owner-surface evidence; no new legacy coverage row is produced in T1. |
| Legacy source search boundary | No broad legacy rescan is authorized. Worker may cite KGR, MKG1, AIF-B, PBR04, N6, LHW13, and memory-derived graph boundary as named prior surfaces. |

## Negative Search And Collision Discipline

Negative search is required for two local views:

- upstream facts that cannot be independently verified by the worker;
- CodeGraph/KGR or CodeGraph/LPF overlap that would create a duplicate owner.

Exact search roots:

- upstream root: `https://github.com/colbymchenry/codegraph`;
- local copied input root: `CodeGraph/CVF_Code_Intelligence_Capability/`;
- CVF owner roots: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/`,
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context_builder/graph/`, and
  named KGR/MKG/reference docs.

Exact search command or query:

- upstream query: direct repository read/search when available to the worker;
- local query: `Get-ChildItem -LiteralPath CodeGraph\CVF_Code_Intelligence_Capability -Recurse -File`
  plus targeted `rg` for row-specific symbols;
- CVF query: targeted `rg` for `LPF`, `KGR`, `freezeAllowed`,
  `GraphKnowledgeService`, `GraphSQLiteStore`, `authorityModel`, and
  `canBypassPolicy`.

Coverage across source/tests/docs/JSON/external evidence:

- source: current LPF graph TypeScript owner files;
- docs: CGE-T0 packets, KGR/MKG/reference docs, and local copied package docs;
- JSON/external evidence: local package examples may be sampled as advisory
  evidence; upstream facts require upstream read/search or remain blocked.

Same-token collision result and absent-versus-collision disposition:

| Token | Collision or occurrence disposition | Binding disposition |
|---|---|---|
| `DEFER` | same-token occurrence exists in CVF governance artifacts | non-authoritative collision; use only as row disposition |
| `CodeGraph` | same-token occurrence exists in this dispatch packet and copied-folder references | non-authoritative collision unless cited as upstream/local external input |
| `LPF` | same-token occurrence exists as current Learning Plane Foundation owner vocabulary | binding only when cited from current LPF source/docs |
| `KGR` | same-token occurrence exists in prior KGR absorption docs | binding only when cited from KGR pre-review or closure surfaces |
| `HEAD` | same-token occurrence exists in git/base-head language | non-authoritative collision; not an upstream fact |
| `REJECT_PARALLEL_CORE` | same-token occurrence exists in CGE-T0/T1 packet disposition rows | non-authoritative collision; use only as a parallel-core rejection disposition |
| `DEDUP_DECISION_REQUIRED` | same-token occurrence exists in CGE-T0/T1 packet disposition rows | non-authoritative collision; use only as a KGR/LPF dedupe disposition |
| `BLOCK_UNTIL_CVF_BENCHMARK` | same-token occurrence exists in CGE-T0/T1 packet disposition rows | non-authoritative collision; use only as a blocked benchmark disposition |

If upstream access is unavailable, the worker records `BLOCKED_SOURCE_NOT_FOUND`,
`DEFER`, or `BLOCK_UNTIL_CVF_BENCHMARK` for affected rows. If a CodeGraph idea
collides with KGR or existing LPF owner surfaces, the worker records
`DEDUP_DECISION_REQUIRED`, `REJECT_PARALLEL_CORE`, or an adapt row to the
existing owner, never a parallel-core import.

## Worker Output Requirements

Create exactly:

`docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md`

The artifact must include:

- `Status: COMPLETE_PENDING_REVIEW`;
- source inventory separating upstream, local copied package, current CVF owner
  surfaces, and prior CVF graph absorption surfaces;
- External Knowledge Intake Routing block;
- Knowledge Absorption Blind-Spot Control Block or clearly bounded equivalent;
- prior absorption resolution for AIF-B, PBR04, N6, LHW13, MKG1, KGR, and the
  memory-derived graph boundary;
- required triage matrix rows listed in the GC-018;
- CodeGraph vs KGR dedupe decision;
- ACE-R1 remains parked section;
- Public Export Disposition `DEFERRED_PRIVATE_ONLY`;
- Agent Operation Trace Block;
- actual `git status --short` and gate results.

## Required Triage Matrix Rows

| Candidate | Required disposition | Minimum rationale |
|---|---|---|
| `freezeAllowed` receipt or equivalent graph-derived authority flag | `BLOCK` | Graph evidence may warn, advise, or require review, but must not grant freeze/finality authority. |
| Local copied LPF-like graph core files | `REJECT_PARALLEL_CORE` | Existing LPF graph owner surfaces must be extended, not duplicated. |
| CodeGraph vs KGR overlap | `DEDUP_DECISION_REQUIRED` | Decide reuse/adapt/defer against KGR before future implementation. |
| Upstream token/cost/tool-call performance claims | `BLOCK_UNTIL_CVF_BENCHMARK` | Needs CVF-owned benchmark; do not cite external claims as proof. |
| Upstream watcher/daemon/autosync | `DEFER_REQUIRES_RUNTIME_GC018` or `REJECT_DIRECT` | Not authorized in CGE-T1. |
| Upstream MCP server wiring or tool auto-config | `DEFER_REQUIRES_MCP_BOUNDARY_WORK_ORDER` or `REJECT_DIRECT` | Not authorized in CGE-T1. |
| Impact radius/callers/callees vocabulary | `ADAPT_TO_EXISTING_LPF_GRAPH` if source-verified | May be useful as vocabulary/template only. |
| Stale-index warning policy | `ADAPT_AS_GOVERNANCE_RULE` if source-verified | Advisory freshness guard only, no auto authority. |
| Graph receipt/query-plan templates | `ADAPT_AFTER_FIELD_NORMALIZATION` if source-verified | Align field naming and existing receipt owners before use. |
| Local package scaffold/test-runner proof | `BLOCK_AS_PROOF` unless package metadata/test runner is verified | Local package presence is not proof of runnable capability. |

## Roadmap-To-Work-Order Trace Matrix

N/A with reason: CGE-T1 is derived from the operator-approved CGE-T0
classification/rebuttal sequence, not from an existing roadmap. The CGE-T0
classification maps directly to the required rows above.

## Foundation Storage Layout Block

N/A with reason: CGE-T1 creates dated dispatch/review artifacts only and adds
`CodeGraph/` to `.gitignore` so raw external input is not committed. It does
not create, split, relocate, or refactor a stable foundation folder or index.

## Worker Autonomy / No-Question Rule

Claude proceeds without operator confirmation for read-only inventory, local
search, source verification, triage-matrix authoring, and allowed gate reruns.

Escalate only for any need to mutate runtime/source, install or run CodeGraph,
edit root lifecycle registry, open ACE-R1, run provider/live proof, public-sync,
push, change risk level, or widen the claim boundary.

## Pending Artifact Evidence Finality

This is `WORKER_MUST_NOT_COMMIT`. The worker return is not closure. The worker
must record actual pending status and must not claim a clean tree after creating
the completion artifact. Codex performs review, commit, closure gates, and any
session sync after accepting the return.

## Evidence Requirements

Required evidence:

- local CodeGraph inventory command/result and count;
- upstream access result: verified source facts or explicit blocked/unavailable
  disposition;
- current CVF graph owner-surface verification;
- row-by-row triage matrix;
- CodeGraph/KGR dedupe decision;
- worker-return fast gate result or blocked reason;
- actual `git status --short`.

## Write Ownership

Worker-owned path:

- `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md`

Codex-owned closure paths after review:

- this work order status update if accepted;
- material commit of the accepted worker return;
- closure gate evidence and any session-sync update if next-move surfaces
  change.

Forbidden write paths:

- `EXTENSIONS/**`;
- `CodeGraph/**` except read-only inventory;
- `.codegraph/**`;
- `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json`;
- public-sync sibling clone;
- ACE-R1 roadmap, work order, or closure artifacts.

## Execution Plan

1. Confirm `executionBaseHead` and actual `git status --short`.
2. Read the required first-read artifacts.
3. Inventory the local copied CodeGraph package and record file count plus
   representative files.
4. Verify upstream CodeGraph public facts if accessible; otherwise record
   upstream-dependent rows as blocked, deferred, or benchmark-gated.
5. Source-verify current CVF graph owner surfaces and prior KGR/MKG graph
   absorption surfaces.
6. Author the CGE-T1 completion artifact with required routing, blind-spot,
   triage, dedupe, ACE-R1 parking, public export, and trace sections.
7. Run worker-return fast gate if available and record actual pending status.
8. Return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` without committing.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | One CGE-T1 completion artifact exists at the required path. |
| AC2 | The artifact includes all required routing, blind-spot, source-inventory, triage, dedupe, ACE-R1 parking, public-export, and trace sections. |
| AC3 | Required blocker/reject/defer rows are present and do not authorize implementation. |
| AC4 | Existing CVF graph/KGR owners are cited before any adapt recommendation. |
| AC5 | No forbidden path or action is touched. |
| AC6 | Worker returns under `WORKER_MUST_NOT_COMMIT` with actual pending status. |

Fail conditions:

- missing `freezeAllowed` `BLOCK` row;
- missing LPF-like graph `REJECT_PARALLEL_CORE` row;
- missing CodeGraph/KGR dedupe row;
- upstream performance claims accepted without CVF benchmark;
- runtime/source/public-sync/provider/live/registry/ACE-R1 action;
- worker commit.

## Closure Checklist

- [ ] CGE-T1 completion artifact exists at the required path.
- [ ] Source inventory separates upstream, local copied package, current CVF
  owners, and prior graph absorption surfaces.
- [ ] Required blocker/reject/defer/adapt rows are present.
- [ ] CodeGraph/KGR dedupe decision is recorded.
- [ ] ACE-R1 remains parked.
- [ ] Public Export Disposition is `DEFERRED_PRIVATE_ONLY`.
- [ ] Worker records actual `git status --short`.
- [ ] Worker commits nothing.

## Review Gate

Codex review is required before closure. Codex must reject the return if the
artifact imports external authority, hides a blocker row, opens implementation,
or treats upstream claims as proof.

No-commit worker returns should run:

```powershell
python governance/compat/run_worker_return_fast_gate.py
```

## Reviewer Closure Conversion

Because this work order is `WORKER_MUST_NOT_COMMIT`, Codex owns closure
conversion.

- completionReviewPath:
  `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md`
- reviewerOwnedClosurePaths:
  - review and possible status transition of this work order;
  - material commit of accepted worker return;
  - committed-range closure gates;
  - any session-sync commit if next-move surfaces change.

The worker must not set closed-equivalent status or commit.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when the completion artifact exists, all
required rows and evidence sections are filled, no forbidden path/action was
used, and the worker has recorded actual pending status.

Return `BLOCKED_WITH_REASON` if upstream/local sources are inaccessible in a way
that prevents the required matrix, if a required gate fails outside allowed
scope, or if satisfying the task would require implementation, public-sync,
runtime/source mutation, root registry edits, provider/live proof, ACE-R1, or a
claim-boundary change.

## Operator Checkpoint

Operator approval is required before implementation, runtime/source mutation,
CodeGraph install/run, public-sync, provider/live proof, root registry mutation,
ACE-R1 reopening, benchmark claims, or any public/production/readiness claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance external absorption triage. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude worker material; Codex reviewer closure |
| Provider or surface | Claude worker workspace; Codex local workspace |
| Session or invocation | 2026-06-20 CGE-T1 CodeGraph external absorption triage |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read/search/inventory commands, governance gates |
| Target paths | required completion artifact only for worker; this work order and GC-018 for dispatch |
| Allowed scope source | operator instruction to have Claude perform CGE-T1 |
| Before status evidence | clean worktree at committed dispatch base `4d004c42`; known untracked CodeGraph and CGE-T0 input packets present for dispatch authoring |
| After status evidence | worker records actual `git status --short` |
| Diff evidence | worker and Codex record `git diff --name-status` |
| Approval boundary | external absorption triage only |
| Claim boundary | no implementation, runtime, MCP, benchmark, provider/live proof, public-sync, registry mutation, ACE-R1 reopening, readiness, or universal governed-coding-control claim |
| Agent type | Claude worker; Codex reviewer/closer |
| Invocation ID | `cge-t1-codegraph-external-absorption-triage-matrix-2026-06-20` |
| Expected manifest | `.gitignore`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/cge-t1-lpf-graph-owner-source-surfaces.json`; `docs/baselines/CVF_GC018_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_FOR_CLAUDE_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_REBUTTAL_PACKET_FOR_CLAUDE_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CLAUDE_REBUTTAL_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CODEX_CLASSIFICATION_2026-06-20.md`; `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md` |
| Actual changed set | `.gitignore`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/cge-t1-lpf-graph-owner-source-surfaces.json`; `docs/baselines/CVF_GC018_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_FOR_CLAUDE_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_REBUTTAL_PACKET_FOR_CLAUDE_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CLAUDE_REBUTTAL_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CODEX_CLASSIFICATION_2026-06-20.md`; `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Claim Boundary

This work order authorizes CGE-T1 triage only. It does not authorize CodeGraph
runtime implementation, graph authority expansion, freeze/finality control,
MCP/tool wiring, watcher/daemon behavior, benchmark proof, public-sync, ACE-R1,
or any public/production/release/readiness claim.
