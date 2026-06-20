# CVF GC-018 - CGE-T1 CodeGraph External Absorption Triage Matrix

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-06-20

Batch ID: CGE-T1

dispatchBaseHead: 4d004c42

executionBaseHead: worker-confirms

## Purpose

Authorize CGE-T1 as a bounded external-knowledge absorption triage matrix for
the CodeGraph external repository and the local copied `CodeGraph/` package.

This tranche decides which CodeGraph ideas are blocked, rejected as a parallel
core, adapted to existing CVF graph owners, deferred to later governed work, or
left as reference-only evidence. It does not implement graph runtime behavior.

## Scope / Target / Owner Boundary

Target inputs:

- external upstream repository: `https://github.com/colbymchenry/codegraph`;
- local copied package: `CodeGraph/CVF_Code_Intelligence_Capability/`;
- CGE-T0 Codex packet, Claude rebuttal, and Codex classification;
- existing CVF graph and knowledge-absorption owner surfaces.

Owner boundary: Claude authors the CGE-T1 triage matrix under
`WORKER_MUST_NOT_COMMIT`; Codex reviews, commits, and closes if accepted.

## Source Authority

| Source | Path or value | Role |
|---|---|---|
| Operator instruction | 2026-06-20 request to let Claude perform CGE-T1 | Tranche selection |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Session continuity |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | Current governed mode and next-move boundary |
| External chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | External repo/copy routing |
| External finding workflow | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | Returned-output classification |
| CGE-T0 review packet | `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_REBUTTAL_PACKET_FOR_CLAUDE_2026-06-20.md` | Initial CodeGraph roadmap/rebuttal packet |
| CGE-T0 Claude rebuttal | `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CLAUDE_REBUTTAL_2026-06-20.md` | Returned advisory findings |
| CGE-T0 Codex classification | `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CODEX_CLASSIFICATION_2026-06-20.md` | Accepted blocker rows and T1 eligibility |
| Current graph owner surface | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/` | Existing CVF graph implementation boundary |
| Current graph context mapper | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context_builder/graph/` | Existing graph-to-task query boundary |
| KGR pre-review | `docs/reference/CVF_KGR_ABSORPTION_PREREVIEW_2026-06-01.md` | Prior graph absorption and dedupe reference |
| Memory-derived graph boundary | `docs/reference/CVF_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md` | Derived graph authority boundary |
| MKG1 work order | `docs/work_orders/CVF_WO_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_2026-06-01.md` | Legacy graph owner-surface review pattern |

## Authorization Decision

Proceed with CGE-T1 as a documentation/review-only triage matrix.

Decision: Claude may create one worker-return completion artifact containing a
source inventory, blind-spot note, prior-absorption resolution, CodeGraph vs
KGR dedupe decision, and required triage matrix rows. Claude must not copy
CodeGraph into CVF runtime, install dependencies, run daemons, wire MCP,
perform provider/live proof, public-sync, root registry mutation, or reopen
ACE-R1.

## Baseline Decision

CGE-T1 is approved as a bounded external absorption triage tranche.

The dispatch baseline is `4d004c42`. The local copied package is untracked
input at dispatch time and must be treated as external/advisory until a later
governed decision classifies or imports any part of it.

## Authorized Scope

Authorized:

- read the required first-read files named in the work order;
- verify upstream CodeGraph public facts if network/browser access is available;
- enumerate and sample the local `CodeGraph/CVF_Code_Intelligence_Capability/`
  package without installing or executing it;
- map candidate ideas to existing CVF graph owner surfaces;
- record required blocker and dedupe rows in the CGE-T1 triage matrix;
- create exactly one worker-return artifact:
  `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md`.

## Forbidden Scope

- No runtime/source edits under `EXTENSIONS/**`.
- No copying external package files into canonical CVF runtime or reference
  folders.
- No wrapper/proxy enforcement, direct IDE/shell/git/filesystem interception, or
  arbitrary command execution lane.
- No CodeGraph install, package bootstrap, `.codegraph/` initialization,
  watcher, daemon, server, MCP wiring, or tool auto-configuration.
- No provider/live proof, public-sync, push, release, public/production
  readiness, or universal governed-coding-control claim.
- No root lifecycle registry mutation in CGE-T1.
- No ACE-R1 reopening or execution.

## Required Triage Rows

| Required row | Minimum disposition | Reason |
|---|---|---|
| `freezeAllowed` derived from graph freshness/confidence/warnings | `BLOCK` | Graph context cannot grant freeze authority |
| LPF-like graph files inside the local copied package | `REJECT_PARALLEL_CORE` | CVF already has an LPF graph owner surface |
| CodeGraph and KGR overlap | `DEDUP_DECISION_REQUIRED` | Avoid duplicate graph-retrieval lanes |
| Upstream token/cost/tool-call performance claims | `BLOCK_UNTIL_CVF_BENCHMARK` | Requires CVF-owned benchmark proof |
| Upstream watcher/daemon/MCP/auto-config concepts | `DEFER` or `REJECT_DIRECT` | Requires separate runtime/MCP authorization if ever pursued |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | CGE-T1 completion artifact includes source inventory and explicitly separates upstream, local copied package, current CVF owners, and prior CVF graph absorption artifacts. |
| AC2 | Completion artifact includes External Knowledge Intake Routing and Knowledge Absorption Blind-Spot controls. |
| AC3 | Required triage matrix includes the five required rows and uses blocker/reject/defer/adapt dispositions without claiming implementation. |
| AC4 | CodeGraph vs KGR dedupe decision is recorded before any future implementation lane is recommended. |
| AC5 | ACE-R1 remains parked. |
| AC6 | No runtime/source/public-sync/provider/live/registry mutation is made. |

## Evidence / Verification

Required pre-dispatch evidence:

```powershell
python governance/compat/check_external_knowledge_intake_routing.py --base 4d004c42 --head HEAD --enforce
python governance/compat/check_external_agent_absorption_table.py --base 4d004c42 --head HEAD --enforce
python governance/compat/check_public_export_disposition.py --base 4d004c42 --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 4d004c42 --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 4d004c42 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 4d004c42 --head HEAD
```

Worker-return evidence:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_worker_return_fast_gate.py
```

If worker access to the upstream repository is blocked, upstream-dependent rows
must be labeled `BLOCKED_SOURCE_NOT_FOUND`, `DEFER`, or
`BLOCK_UNTIL_CVF_BENCHMARK` as appropriate. The worker must not promote upstream
claims from CGE-T0 memory alone.

## Negative Search And Collision Discipline

Negative-search scope is limited to upstream facts that the worker cannot
independently verify and to CodeGraph/KGR collision checks.

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
| `HEAD` | same-token occurrence exists in git/base-head language | non-authoritative collision; not an upstream fact |
| `CGE` | same-token occurrence exists in this batch's tranche identifiers | non-authoritative collision; not an upstream fact |
| `LPF` | same-token occurrence exists as current Learning Plane Foundation owner vocabulary | binding only when cited from current LPF source/docs |
| `KGR` | same-token occurrence exists in prior KGR absorption docs | binding only when cited from KGR pre-review or closure surfaces |
| `BLOCK_UNTIL_CVF_BENCHMARK` | same-token occurrence exists in CGE-T0/T1 packet disposition rows | non-authoritative collision; use only as a blocked benchmark disposition |

Required discipline:

- do not claim an upstream CodeGraph feature exists unless the worker cites the
  upstream repository or a local copied file that actually contains it;
- if upstream access is unavailable, mark upstream-dependent rows as
  `BLOCKED_SOURCE_NOT_FOUND`, `DEFER`, or `BLOCK_UNTIL_CVF_BENCHMARK`;
- compare CodeGraph graph-query, graph-receipt, and impact-radius vocabulary
  against KGR and existing LPF graph owner surfaces before recommending an
  adapt row;
- do not treat a missing upstream verification as proof that the idea is false;
  it only blocks promotion.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | External repo or copied folder -> root/folder lifecycle classification candidate -> absorption map or triage matrix -> CVF owner-surface disposition -> future GC-018/work order only if implementation is later authorized |
| Owner surface | CGE-T1 triage matrix; existing LPF graph owner surfaces; KGR pre-review; memory-derived graph boundary |
| Disposition | `ADAPT`, `DEFER`, `REJECT`, or `BLOCK` by row; no direct import |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; external-agent absorption table guard for returned findings |
| Claim boundary | Triage/absorption classification only; no runtime, MCP, benchmark, public-sync, provider/live proof, registry mutation, ACE-R1 reopening, readiness, or universal governed-coding-control claim |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | CGE-T1 external absorption triage baseline |
| claimDisposition | N/A with reason: baseline rejects runtime/direct-interception/universal-control claims |
| receiptEvidence | N/A with reason: no Delta receipt/action evidence is used |
| actionEvidence | N/A with reason: no execution action is claimed |
| invocationBoundary | no wrapper/proxy, mandatory invocation, direct IDE/shell/git/filesystem interception, or arbitrary command execution |
| interceptionBoundary | no direct interception claim |
| claimLanguage | triage authorization only |
| forbiddenExpansion | no runtime, MCP, benchmark, provider/live, public-sync, readiness, registry mutation, ACE-R1 reopening, or universal governed-coding-control claim |

## Rescan Intelligence Hardening

- Original source artifact:
  `https://github.com/colbymchenry/codegraph` and local copied folder
  `CodeGraph/CVF_Code_Intelligence_Capability/`.
- Predecessor intake artifact:
  `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CODEX_CLASSIFICATION_2026-06-20.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because CGE-T1 moves from operator
  candidate to dispatch-ready triage authorization.
- Routing matrix status:
  - `DO_NOW`: Claude authors CGE-T1 triage matrix.
  - `RESOLVED_BY_DESIGN`: T1 maps external ideas to existing LPF/KGR owners.
  - `SEPARATE_RUNTIME_TRANCHE`: implementation, MCP, watcher/daemon, benchmark,
    provider/live proof, and root registry mutation.
  - `STRATEGIC_OPERATOR_DECISION`: whether to open any post-T1 implementation
    lane.
  - `OUT_OF_SCOPE`: public-sync, direct interception, universal governed-coding
    control, ACE-R1 reopening.
- Semantic sampling status: `PARTIAL_TARGETED`, limited to triage readiness and
  blocker carry-forward.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | CodeGraph remains external/advisory input. |
| CHANGED_DISPOSITION | Operator approved CGE-T1 as a Claude-authored triage matrix. |
| NEW_FINDING | Required rows cover `freezeAllowed`, LPF parallel-core risk, KGR overlap, and benchmark-gated upstream claims. |
| REMOVED_OR_REJECTED | Runtime/source/MCP/public-sync/provider/live/ACE-R1 work remains out of scope. |

### Follow-Up Routing Matrix

| Lane | Disposition |
|---|---|
| DO_NOW | Claude authors CGE-T1 completion artifact under `WORKER_MUST_NOT_COMMIT`. |
| RESOLVED_BY_DESIGN | Existing LPF/KGR owners are cited before adapt recommendations. |
| SEPARATE_RUNTIME_TRANCHE | Implementation, MCP, watcher/daemon, benchmark, provider/live proof, root registry mutation. |
| STRATEGIC_OPERATOR_DECISION | Whether to open a post-T1 implementation or ACE-R1-adjacent lane. |
| DEFER | Implementation, benchmark, MCP, watcher/daemon, root registry mutation, ACE-R1. |
| OUT_OF_SCOPE | Public-sync, provider/live proof, direct interception, universal governed-coding-control claim. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| CGE-T1-RS1 | Authorized Scope | T1 creates triage only | `OUT_OF_SCOPE` | Could this baseline authorize copying CodeGraph into LPF? | PASS_BOUNDARY |
| CGE-T1-RS2 | Required Triage Rows | `freezeAllowed` must be blocked | `DO_NOW` | Could graph-derived `freezeAllowed` be accepted as authority? | PASS_BLOCKED |
| CGE-T1-RS3 | Required Triage Rows | performance claims need benchmark | `SEPARATE_RUNTIME_TRANCHE` | Could upstream performance claims become proof? | PASS_BENCHMARK_GATED |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance absorption triage. No public-sync batch is authorized.

## Claim Boundary

CGE-T1 authorizes a source-verified absorption triage matrix only. It can decide
which CodeGraph ideas are blocked, rejected, adapted, or deferred. It cannot
make CodeGraph canonical, mutate runtime/source, prove performance, claim
governed-coding control, or publish public-facing CVF updates.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher; Claude worker; Codex reviewer/closer |
| Provider or surface | Codex local workspace; Claude worker handoff |
| Session or invocation | 2026-06-20 CGE-T1 dispatch |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, governance checkers |
| Target paths | this GC-018; CGE-T1 work order; one future CGE-T1 completion artifact |
| Allowed scope source | operator instruction to let Claude perform CGE-T1 |
| Before status evidence | clean worktree at committed base `4d004c42`; known untracked CodeGraph and CGE-T0 input packets present for dispatch authoring |
| After status evidence | dispatch packet pending gates |
| Diff evidence | `git diff --name-status`; `git status --short` |
| Approval boundary | documentation/review-only external absorption triage |
| Claim boundary | no implementation, runtime, MCP, provider/live, public-sync, benchmark, registry mutation, ACE-R1 reopening, readiness, or universal governed-coding-control claim |
| Agent type | Codex orchestrator; Claude worker |
| Invocation ID | `cge-t1-codegraph-external-absorption-triage-dispatch-2026-06-20` |
| Expected manifest | `.gitignore`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/cge-t1-lpf-graph-owner-source-surfaces.json`; `docs/baselines/CVF_GC018_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_FOR_CLAUDE_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_REBUTTAL_PACKET_FOR_CLAUDE_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CLAUDE_REBUTTAL_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CODEX_CLASSIFICATION_2026-06-20.md`; `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md` |
| Actual changed set | `.gitignore`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/cge-t1-lpf-graph-owner-source-surfaces.json`; `docs/baselines/CVF_GC018_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_FOR_CLAUDE_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_REBUTTAL_PACKET_FOR_CLAUDE_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CLAUDE_REBUTTAL_2026-06-20.md`; `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_CODEX_CLASSIFICATION_2026-06-20.md`; `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |
