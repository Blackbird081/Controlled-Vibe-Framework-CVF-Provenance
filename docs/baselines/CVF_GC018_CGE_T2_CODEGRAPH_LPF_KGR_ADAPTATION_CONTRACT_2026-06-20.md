# CVF GC-018 - CGE-T2 CodeGraph LPF/KGR Adaptation Contract

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-20

docType: baseline

dispatchBaseHead: 5cb5a8e1

Batch ID: CGE-T2

## Purpose

Authorize CGE-T2 as a bounded documentation/reference tranche that converts the
CGE-T1 CodeGraph absorption triage into an LPF/KGR adaptation contract. The
contract must preserve CVF owner surfaces, normalize external receipt/query-plan
ideas into CVF field language, and define stale-graph fallback and no-authority
rules before any future implementation lane.

## Operator Authorization

The operator instructed Codex to issue the next work order for Claude after
CGE-T1 closure. This baseline interprets that as authorization for the next
bounded CodeGraph external absorption tranche, not for runtime/source/MCP/
watcher/benchmark/provider/public/ACE-R1 execution.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-20 "ra work order cho claude di tiep" | ACCEPT |
| Active session mode | `cge_t1_codegraph_external_absorption_triage_closed_next_lane_selection_ready` | ACCEPT |
| CGE-T1 closure | `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| External absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | ACCEPT |
| Memory-derived graph boundary | `docs/reference/CVF_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md` | ACCEPT |
| KGR pre-review | `docs/reference/CVF_KGR_ABSORPTION_PREREVIEW_2026-06-01.md` | ACCEPT |

## Scope / Owner Boundary

Allowed scope:

- create a reference adaptation contract under `docs/reference/`;
- create a worker-return artifact under `docs/reviews/`;
- source-verify CGE-T1 rows R7, R8, and R9 against current LPF/KGR owner
  surfaces;
- define field-normalization, freshness/fallback, and no-authority rules for
  future work orders;
- identify future checker candidates without implementing them.

Forbidden scope:

- no edits under `EXTENSIONS/**`, `tools/**`, `scripts/**`, runtime source,
  tests, MCP packages, web UI, public-sync, or root lifecycle registry;
- no CodeGraph install, `codegraph init`, `.codegraph/` creation, dependency
  install, watcher/daemon, MCP wiring, auto-config, benchmark, provider/live
  proof, or public push;
- no ACE-R1 reopening;
- no freeze, readiness, production, release, or universal governed-coding
  control claim.

Risk ceiling: R1 documentation/reference only.

## Required Deliverables

Claude must return uncommitted `COMPLETE_PENDING_REVIEW` with exactly these
new artifacts:

- `docs/reference/CVF_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_2026-06-20.md`
- `docs/reviews/CVF_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_WORKER_RETURN_2026-06-20.md`

No other files are authorized for the worker.

## Decision / Baseline / Proposed Tranche

Baseline decision: CGE-T2 is ready for Claude dispatch as a documentation/
reference-only adaptation contract tranche.

Proposed tranche: `CGE-T2 CodeGraph LPF/KGR Adaptation Contract`.

Tranche owner split: Claude authors the reference contract and worker-return
artifact without committing. Codex reviews, converts accepted output to a
reviewer-owned completion packet if needed, commits, and session-syncs.

Baseline evidence:

- CGE-T1 closed at material commit `1db59198`.
- Active continuity sync commit is `5cb5a8e1`.
- CGE-T1 explicitly marked R7/R8/R9 as adaptation candidates and parked ACE-R1.
- Current LPF/KGR source-owner surfaces exist and are source-verified below.

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `5cb5a8e1`.
- `git status --short` was clean except the recurring Windows global-git-ignore
  permission warning.
- Source verification used `rg` against CGE-T1, LPF graph source, KGR
  pre-review, and memory-derived graph boundary.

Required pre-dispatch verification before commit:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 5cb5a8e1 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 5cb5a8e1 --head HEAD --enforce
```

## Required Contract Content

The reference contract must include:

- Source Authority and Non-Authority Input sections;
- LPF/KGR Owner Surface Map for R7/R8/R9;
- Field Normalization Table mapping external CodeGraph-style fields to CVF
  `camelCase` doc-contract names, or marking them `REJECT`/`DEFER`;
- Graph Freshness And Fallback Rule stating graph context is advisory and stale
  or uncertain graph evidence requires direct source read/fallback before any
  review, freeze, finality, or scope-expansion claim;
- No-Authority Rule stating graph impact radius cannot grant freeze, bypass
  policy, widen allowed scope, or replace source authority;
- Future Checker Candidate Ledger, with checker candidates only, no
  implementation;
- Claim Boundary and Public Export Disposition.

The worker-return artifact must include:

- actual `executionBaseHead`;
- actual `git status --short`;
- source inventory and scan-depth ledger;
- External Knowledge Intake Routing block;
- Knowledge Absorption Blind-Spot Control Block;
- Roadmap-to-Work-Order Trace Matrix, or `N/A with reason`;
- Closure Diff Gate against this baseline and the work order;
- Agent Operation Trace Block;
- Finding-To-Governance Learning Disposition;
- Epistemic Process Block;
- Worker Boundary Statement.

## Required Decisions

| Decision | Required disposition |
|---|---|
| `freezeAllowed` | `REJECT_AS_AUTHORITY_SIGNAL`; no true/false freeze grant in graph contract |
| LPF-like copied graph core files | `REJECT_PARALLEL_CORE`; no direct import |
| CodeGraph/KGR overlap | `DEDUP_RESOLVE_TOWARD_KGR_AND_LPF` |
| Upstream performance claims | `BLOCK_UNTIL_CVF_BENCHMARK`; not part of CGE-T2 |
| Watcher/daemon | `DEFER_REQUIRES_RUNTIME_GC018`; not part of CGE-T2 |
| MCP wiring or auto-config | `DEFER_REQUIRES_MCP_BOUNDARY_WORK_ORDER`; not part of CGE-T2 |
| Impact vocabulary | `ADAPT_TO_EXISTING_LPF_GRAPH_CONTRACT` only |
| Stale-index rule | `ADAPT_AS_ADVISORY_FALLBACK_RULE` only |
| Receipt/query-plan templates | `ADAPT_AFTER_FIELD_NORMALIZATION` only |
| ACE-R1 | `PARKED`; not reopened |

## Source Verification Summary

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| CGE-T1 closed with R7/R8/R9 as adapt candidates and no runtime scope | `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md` | lines 165-167 and 176-195 | `ADAPT_TO_EXISTING_LPF_GRAPH`; `ADAPT_AS_GOVERNANCE_RULE`; `ADAPT_AFTER_FIELD_NORMALIZATION`; `DEDUP_RESOLVE_TOWARD_KGR_AND_LPF` | CGE-T1 triage matrix | ACCEPT |
| CGE-T1 parks ACE-R1 | `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md` | lines 195-202 | `ACE-R1 Remains Parked` | CGE-T1 triage matrix | ACCEPT |
| Graph authority receipt exists and is advisory/no-bypass | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/authority/graph-authority-gate.ts` | lines 30-40 and 122-128 | `GraphAuthorityReceipt`; `authorityModel`; `canBypassPolicy`; `queryId` | LPF graph authority gate | ACCEPT |
| Graph service query-impact owner exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/graph-schema.ts` | lines 62-65 | `GraphKnowledgeService`; `queryImpact` | LPF graph schema | ACCEPT |
| Task query mapper already owns query type/scope mapping | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context_builder/graph/task-query-mapper.ts` | lines 14-50 and 55-81 | `TaskQuery`; `mapTaskToGraphQuery`; `resolveGraphContextForTask` | LPF task query mapper | ACCEPT |
| Symbol index owner exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/index/symbol-index.ts` | lines 13 and 40-80 | `SymbolIndex`; `buildSymbolIndexFromGraph`; `createInMemoryGraphKnowledgeService` | LPF symbol index | ACCEPT |
| KGR already owns planned graph-builder/retrieval overlap and blocks external graph library import | `docs/reference/CVF_KGR_ABSORPTION_PREREVIEW_2026-06-01.md` | lines 217-218 and 233 | `KGR1-T3`; `KGR1-T4`; `Do not import external graph libraries` | KGR absorption pre-review | ACCEPT |
| Derived graph views are advisory and cannot overrule source authority | `docs/reference/CVF_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md` | lines 23-42 | `derived views`; `cannot overrule`; `advisory only` | memory-derived graph boundary | ACCEPT |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | external input -> triage matrix -> owner-surface adaptation contract -> future GC-018 only if implementation is separately authorized |
| Owner surface | Existing LPF graph owner surfaces, KGR pre-review, memory-derived graph boundary, CGE-T2 reference contract |
| Disposition | Reference contract only; no direct import |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Claim boundary | no runtime/source/MCP/watcher/benchmark/provider/public/ACE-R1/freeze/readiness/universal-control claim |

## Knowledge Absorption Blind-Spot Control Block

| Gate | Required handling |
|---|---|
| Source coverage | Contract must cite CGE-T1 and current LPF/KGR owners. |
| Prior absorption | Contract must explain why KGR/LPF are owners and CodeGraph is not a new lane. |
| Owner-surface mapping | Every adapted concept must map to an owner or be rejected/deferred. |
| Parallel-core risk | Direct copied graph-core files remain rejected. |
| Authority-leak risk | Graph-only freeze/finality remains rejected. |
| Claim-boundary risk | Performance/runtime/MCP claims remain out of scope. |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation area | external knowledge absorption; graph owner-surface doctrine |
| Stable reference output | `docs/reference/CVF_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_2026-06-20.md` |
| Worker return output | `docs/reviews/CVF_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_WORKER_RETURN_2026-06-20.md` |
| Generated aggregate impact | N/A with reason: no generated JSON aggregate is edited by CGE-T2 |
| Runtime impact | N/A with reason: no runtime/source/test path is authorized |

## Negative Search And Collision Discipline

Claude must distinguish same-token collisions from source authority. If a token
appears only in CGE-T1/T2 packet language, it is not proof of runtime support.

| Token | Collision or occurrence disposition | Binding disposition |
|---|---|---|
| `freezeAllowed` | external copied package blocker and CGE packet token | reject as authority signal |
| `impact radius` | CodeGraph vocabulary and LPF query-impact neighborhood idea | adapt as vocabulary only |
| `receipt` | CVF has multiple receipt concepts | bind only to graph authority/adaptation contract fields named in CGE-T2 |
| `query plan` | external template vocabulary | doc-contract only until future implementation |
| `stale` | generic term across docs | bind only when attached to graph freshness/fallback rule |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance external absorption design/reference tranche. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Rescan Intelligence Hardening

- Original source artifact:
  `https://github.com/colbymchenry/codegraph` and local copied folder
  `CodeGraph/CVF_Code_Intelligence_Capability/`.
- Predecessor intake artifact:
  `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because CGE-T2 moves from triage
  rows to an owner-surface adaptation contract.
- Routing matrix status:
  - `DO_NOW`: author the reference adaptation contract and worker return.
  - `RESOLVED_BY_DESIGN`: keep CodeGraph advisory and map R7/R8/R9 to LPF/KGR.
  - `SEPARATE_RUNTIME_TRANCHE`: runtime/source/test, MCP, watcher/daemon,
    benchmark, provider/live proof.
  - `STRATEGIC_OPERATOR_DECISION`: future operator decision for any
    implementation or ACE-R1 lane after Codex reviews CGE-T2.
  - `OUT_OF_SCOPE`: public-sync, direct interception, freeze/readiness claims.
- Semantic sampling status: `PARTIAL_TARGETED`, limited to owner-surface
  contract readiness and claim boundary.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | CodeGraph remains external/advisory input. |
| CHANGED_DISPOSITION | T1 triage rows become T2 reference-contract requirements. |
| NEW_FINDING | No new source defect claimed; T2 records owner-surface contract language. |
| REMOVED_OR_REJECTED | Runtime/MCP/watcher/benchmark/provider/public/ACE-R1 remain out of scope. |

### Follow-Up Routing Matrix

| Lane | Disposition |
|---|---|
| DO_NOW | CGE-T2 reference contract and worker return. |
| RESOLVED_BY_DESIGN | R7/R8/R9 owner-surface adaptation language. |
| SEPARATE_RUNTIME_TRANCHE | Any implementation, checker code, MCP, watcher, benchmark, provider/live proof. |
| STRATEGIC_OPERATOR_DECISION | Post-CGE implementation or ACE-R1 reopening. |
| DEFER | Runtime/source/test, MCP, watcher/daemon, public-sync, ACE-R1. |
| OUT_OF_SCOPE | Public, production, release, readiness, universal-control claims. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| CGE-T2-RS1 | Required Decisions | `freezeAllowed` rejected | `REJECT_AS_AUTHORITY_SIGNAL` | Could graph evidence grant freeze? | PASS_BLOCKED |
| CGE-T2-RS2 | Required Contract Content | field normalization only | `ADAPT_AFTER_FIELD_NORMALIZATION` | Could templates become runtime schema? | PASS_CONTRACT_ONLY |
| CGE-T2-RS3 | Scope / Owner Boundary | no runtime/MCP/watcher | `OUT_OF_SCOPE` | Could T2 open implementation? | PASS_BOUNDARY |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | CGE-T2 CodeGraph LPF/KGR adaptation contract only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: graph receipt templates are design concepts only, not Delta receipt evidence |
| actionEvidence | N/A with reason: no execution action is claimed |
| invocationBoundary | no wrapper/proxy, mandatory invocation, direct IDE/shell/git/filesystem interception, arbitrary command execution, or EDIT/COMMIT execution |
| interceptionBoundary | no direct interception claim |
| claimLanguage | reference contract only |
| forbiddenExpansion | no runtime, MCP, watcher/daemon, benchmark, provider/live, public-sync, ACE-R1, freeze, readiness, or universal governed-coding-control claim |

## Finding-To-Governance Learning Disposition

- Defect class: `ORCHESTRATOR_PACKET_GAP`
- Learning lane: `GOVERNANCE_CONTROL_PLANE`
- Disposition: `DESIGN_REVIEW_REQUIRED`
- Next action: Claude authors the adaptation contract for Codex review.
- Runtime/provider/cost learning lane: `N/A_WITH_REASON` - runtime,
  provider/live, benchmark, and cost claims remain blocked.

| Finding or lesson | Disposition | Reason |
|---|---|---|
| CGE-T1 needs an owner-surface adaptation contract before implementation | DESIGN_REVIEW_REQUIRED | Prevents external CodeGraph ideas from bypassing LPF/KGR ownership. |
| Graph freshness must stay advisory and fallback-bound | DESIGN_REVIEW_REQUIRED | Prevents graph-only authority or freeze/finality expansion. |

## Epistemic Process Block

Expected Result / Prediction: CGE-T2 should turn CGE-T1's adapt rows into a
bounded owner-surface contract without opening runtime work.

Evidence Comparison: CGE-T1 already isolated R7/R8/R9 as useful adaptation
rows while rejecting or deferring direct runtime/MCP/watcher/benchmark claims.

Contradiction Or Gap Disposition: no contradiction blocks a documentation-only
contract. Implementation remains a separate future decision.

Claim Update: CodeGraph remains external advisory input; CGE-T2 may define
contract language only.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatch author |
| Provider or surface | Codex CLI |
| Session or invocation | 2026-06-20 CGE-T2 dispatch |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, rg, apply_patch, governance gates |
| Target paths | this GC-018 baseline; CGE-T2 work order |
| Allowed scope source | operator request to issue next Claude work order |
| Before status evidence | clean committed base `5cb5a8e1` |
| After status evidence | pending dispatch artifacts only |
| Diff evidence | new baseline and work order only |
| Approval boundary | dispatch authoring only |
| Claim boundary | no implementation/runtime/MCP/watcher/benchmark/provider/public/ACE-R1/freeze/readiness claim |
| Agent type | Codex dispatcher |
| Invocation ID | `cge-t2-codegraph-lpf-kgr-adaptation-contract-dispatch-2026-06-20` |
| Expected manifest | `docs/baselines/CVF_GC018_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_FOR_CLAUDE_2026-06-20.md` |
| Actual changed set | `docs/baselines/CVF_GC018_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_FOR_CLAUDE_2026-06-20.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Claim Boundary

CGE-T2 authorizes only a documentation/reference adaptation contract and
worker-return artifact. It does not authorize CodeGraph runtime adoption, source/test
edits, MCP wiring, watcher/daemon behavior, `.codegraph/`, benchmark proof,
provider/live proof, public-sync, ACE-R1, freeze, readiness, or universal
governed-coding-control claims.
