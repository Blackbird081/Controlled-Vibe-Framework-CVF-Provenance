# CVF Agent Work Order - CGE-T2 CodeGraph LPF/KGR Adaptation Contract

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-20

docType: work_order

dispatchBaseHead: 5cb5a8e1

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Implementer/worker (Claude). Codex is reviewer/closer.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_FOR_CLAUDE_2026-06-20.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: confirm with `git rev-parse --short HEAD` at worker start.

Current-time notes: CGE-T2 is a documentation/reference adaptation contract
only. It turns CGE-T1 CodeGraph adapt rows R7/R8/R9 into owner-surface contract
language for LPF/KGR and future work orders.

Do-not-misread notes: do not implement, install, initialize, run, benchmark, or
wire CodeGraph. Do not edit `EXTENSIONS/**`, tests, tools, scripts, MCP, web UI,
public-sync, root lifecycle registry, or ACE-R1. Do not create `.codegraph/`.

Required first actions: read this work order, read the CGE-T2 GC-018 baseline,
read CGE-T1 completion, read the external absorption chain map, read the memory
derived graph boundary, read KGR pre-review, and source-verify the LPF graph
owner surfaces before writing.

Return contract: return `COMPLETE_PENDING_REVIEW` with two uncommitted
artifacts only:

- `docs/reference/CVF_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_2026-06-20.md`
- `docs/reviews/CVF_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_WORKER_RETURN_2026-06-20.md`

Include actual `git status --short`, actual `executionBaseHead`, source
inventory, scan-depth ledger, required contract decisions, and no commit. If
blocked, return `BLOCKED_WITH_REASON` and name the exact source or gate.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two agents, one role each: Claude authors reference and worker-return artifacts; Codex reviews/closes |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=5cb5a8e1`; `executionBaseHead` confirmed by Claude; `closureBaseHead` set by Codex before closure commit |
| changedSetScope(phase) | worker creates only the two CGE-T2 return artifacts; Codex owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | Claude trace covers the two worker-return artifacts; Codex trace covers review/closure |
| commitOwner(phase) | Claude commits nothing (`WORKER_MUST_NOT_COMMIT`); Codex owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix CGE-T2 with runtime, public-sync, registry mutation, MCP, watcher/daemon, benchmark, or ACE-R1 changes |
| cleanWorktreeBeforeDispatch | YES - Before status evidence: clean worktree at dispatch base `5cb5a8e1`; only recurring Windows global git-ignore permission warning |
| nextMoveSurfaces | Codex updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | Codex is the designated reviewer and closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_COMPLETION_2026-06-20.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; accepted reference contract; accepted worker-return artifact; reviewer-owned closure packet if accepted; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | Codex |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | external repository/copy-derived CodeGraph findings from CGE-T1 closure artifact at material commit `1db59198` |
| Intake role | Claude worker authors bounded reference and worker-return artifacts |
| Reviewer role | Codex validates source fidelity, gates, claim boundary, and commits if accepted |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; no direct runtime/source implementation |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | Claude worker return -> Codex reviewer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if runtime/source/MCP/watcher/benchmark/provider/live/public-sync/ACE-R1/freeze/readiness/universal-control scope is required |

## Worker Autonomy / No-Question Rule

Claude must resolve any machine-check or packet-shape issue inside this work
order's Allowed scope. Claude must stop and return
`BLOCKED_WITH_REASON` only if a needed action would exceed Allowed scope, alter
the claim boundary, open runtime/source/MCP/watcher/benchmark/provider/live/
public-sync/ACE-R1 work, require secrets/quota/network beyond read-only source
inspection, or perform destructive/irreversible actions.

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index requirement | NOT_APPLICABLE_WITH_REASON |
| Reason | CGE-T2 is an external repo/copied-folder absorption contract derived from CGE-T1, not a raw `.private_reference/legacy` corpus scan or LHW wave. |
| Coverage evidence used instead | CGE-T1 source inventory, external absorption chain map, LPF/KGR owner sources, memory-derived graph boundary. |

## Purpose

Create a source-verified LPF/KGR adaptation contract for the useful CodeGraph
ideas that survived CGE-T1 triage: impact vocabulary, stale-index/fallback
discipline, and graph receipt/query-plan templates. The contract prepares
future implementation/checker lanes without performing them.

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
| Operator instruction | 2026-06-20: issue next work order for Claude | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_2026-06-20.md` | ACCEPT |
| CGE-T1 completion | `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md` | ACCEPT |
| External absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | ACCEPT |
| Memory-derived graph boundary | `docs/reference/CVF_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md` | ACCEPT |
| KGR pre-review | `docs/reference/CVF_KGR_ABSORPTION_PREREVIEW_2026-06-01.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- read and cite CGE-T1, LPF graph owner source files, KGR pre-review, and memory
  derived graph boundary;
- create the CGE-T2 reference adaptation contract;
- create the CGE-T2 worker-return artifact;
- define future checker candidates as candidates only;
- run read-only/source-verification commands and governance gates.

Forbidden scope:

- no runtime/source/test edits under `EXTENSIONS/**`;
- no direct copy/import of CodeGraph package files into CVF canonical paths;
- no CodeGraph install, dependency install, execution, `.codegraph/`, watcher,
  daemon, MCP server, auto-config, benchmark, or provider/live proof;
- no root lifecycle registry mutation;
- no public-sync, push, release, production/public readiness, freeze, or
  universal governed-coding-control claim;
- no ACE-R1 reopening.

Risk ceiling: R1 documentation/reference only.

## Required First Reads

- `docs/baselines/CVF_GC018_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_2026-06-20.md`
- `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
- `docs/reference/CVF_KGR_ABSORPTION_PREREVIEW_2026-06-01.md`
- `docs/reference/CVF_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/graph-schema.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/index/symbol-index.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/authority/graph-authority-gate.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context_builder/graph/task-query-mapper.ts`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 5cb5a8e1 --head HEAD
```

Expected result: gates pass or worker returns `BLOCKED_WITH_REASON` before
writing output artifacts.

## Source Verification Block

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

## Worker Output Requirements

Create the reference contract with these required sections:

- Purpose
- Source Authority
- Non-Authority Inputs
- LPF/KGR Owner Surface Map
- Field Normalization Table
- Graph Freshness And Fallback Rule
- No-Authority Rule
- Future Checker Candidate Ledger
- Public Export Disposition
- Claim Boundary

Create the worker-return artifact with these required sections:

- execution base and status evidence;
- Source Inventory;
- Scan Depth Ledger;
- External Knowledge Intake Routing;
- Knowledge Absorption Blind-Spot Control Block;
- Roadmap-to-Work-Order Trace Matrix or `N/A with reason`;
- Closure Diff Gate;
- Finding-To-Governance Learning Disposition;
- Epistemic Process Block;
- Agent Operation Trace Block;
- Worker Boundary Statement.

## Write Ownership

Claude may write only:

- `docs/reference/CVF_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_2026-06-20.md`
- `docs/reviews/CVF_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_WORKER_RETURN_2026-06-20.md`

Codex owns all commits, reviewer completion conversion, closure edits,
session-sync, and any future public-sync decision.

## Execution Plan

1. Confirm `executionBaseHead` with `git rev-parse --short HEAD`.
2. Capture initial `git status --short`.
3. Read all Required First Reads.
4. Source-verify CGE-T1 R7/R8/R9 and LPF/KGR owner symbols.
5. Draft the reference adaptation contract.
6. Draft the worker-return artifact with source inventory, scan-depth ledger,
   evidence, AOT, epistemic block, and worker boundary.
7. Run the requested local gates if available.
8. Return `COMPLETE_PENDING_REVIEW` without committing.

## Evidence Requirements

The worker return must include:

- exact `executionBaseHead`;
- before/after `git status --short`;
- source inventory with authority/non-authority distinctions;
- scan-depth ledger;
- field normalization table evidence;
- AOT expected/actual changed-set manifest with only the two authorized output
  paths;
- gate commands and results, or `NOT_RUN_WITH_REASON`;
- explicit no-runtime/no-public/no-provider/no-ACE-R1 boundary statement.

## Review Gate

Codex must reject or return the worker output if:

- extra files are created or modified;
- reference contract promotes CodeGraph to canonical runtime;
- contract opens runtime/source/test/MCP/watcher/benchmark/provider/public/ACE-R1;
- worker omits Source Inventory, Public Export Disposition, AOT, or Claim
  Boundary;
- gates fail and the repair is inside Allowed scope but not performed.

## Closure Checklist

- [ ] Worker returned `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.
- [ ] Worker created only the two authorized paths.
- [ ] Reference contract preserves LPF/KGR ownership.
- [ ] Worker return includes source inventory and scan-depth ledger.
- [ ] Worker return includes AOT, epistemic block, and public export disposition.
- [ ] Codex reviewer gate passes before commit.
- [ ] Session-sync is updated only if next-move surfaces change.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when both authorized artifacts exist and all
required sections are present.

Return `BLOCKED_WITH_REASON` when source verification fails, required owner
surface cannot be found, or a necessary action would exceed Allowed scope.

## Operator Checkpoint

No operator checkpoint is needed for documentation/reference authoring inside
Allowed scope. Operator checkpoint is required before any implementation,
runtime/source/test edit, MCP, watcher/daemon, benchmark, provider/live,
public-sync, ACE-R1 reopening, freeze/readiness, or universal-control claim.

## Required Contract Decisions

| Decision | Required disposition |
|---|---|
| `freezeAllowed` | `REJECT_AS_AUTHORITY_SIGNAL` |
| copied LPF-like graph core files | `REJECT_PARALLEL_CORE` |
| CodeGraph/KGR overlap | `DEDUP_RESOLVE_TOWARD_KGR_AND_LPF` |
| performance claims | `BLOCK_UNTIL_CVF_BENCHMARK` |
| watcher/daemon | `DEFER_REQUIRES_RUNTIME_GC018` |
| MCP wiring or auto-config | `DEFER_REQUIRES_MCP_BOUNDARY_WORK_ORDER` |
| impact vocabulary | `ADAPT_TO_EXISTING_LPF_GRAPH_CONTRACT` |
| stale-index rule | `ADAPT_AS_ADVISORY_FALLBACK_RULE` |
| receipt/query-plan templates | `ADAPT_AFTER_FIELD_NORMALIZATION` |
| ACE-R1 | `PARKED` |

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

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation area | external knowledge absorption; graph owner-surface doctrine |
| Stable reference output | `docs/reference/CVF_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_2026-06-20.md` |
| Worker return output | `docs/reviews/CVF_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_WORKER_RETURN_2026-06-20.md` |
| Generated aggregate impact | N/A with reason: no generated JSON aggregate is authorized |
| Runtime impact | N/A with reason: no runtime/source/test path is authorized |

## Acceptance Criteria

- [ ] Reference contract exists at the required path.
- [ ] Completion review exists at the required path.
- [ ] Contract maps all adapted ideas to existing LPF/KGR owners or rejects/
  defers them.
- [ ] Contract rejects graph-derived freeze/finality authority.
- [ ] Contract blocks performance claims until a separate CVF benchmark.
- [ ] Contract keeps watcher/daemon, MCP wiring, provider/live, public-sync,
  runtime/source/test edits, and ACE-R1 out of scope.
- [ ] Completion includes actual `git status --short`.
- [ ] Worker commits nothing.

## Fail Conditions

- Any edit under `EXTENSIONS/**`, `tools/**`, `scripts/**`, `.codegraph/**`, MCP,
  web UI, public-sync, root lifecycle registry, or session state.
- Any claim that CodeGraph is canonical CVF runtime.
- Any performance/readiness/provider/public/universal-control claim.
- Any ACE-R1 reopening.
- Missing Source Inventory, AOT block, Public Export Disposition, or Claim
  Boundary in worker artifacts.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance external absorption reference-contract tranche. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | CGE-T2 CodeGraph LPF/KGR adaptation contract work order only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: graph receipt templates are design concepts only, not Delta receipt evidence |
| actionEvidence | N/A with reason: no execution action is claimed |
| invocationBoundary | no wrapper/proxy, mandatory invocation, direct IDE/shell/git/filesystem interception, arbitrary command execution, or EDIT/COMMIT execution |
| interceptionBoundary | no direct interception claim |
| claimLanguage | work-order dispatch only |
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

Expected Result / Prediction: CGE-T2 should produce a reference contract that
preserves useful CodeGraph vocabulary while preventing runtime/authority
expansion.

Evidence Comparison: CGE-T1 already identified R7/R8/R9 as useful adaptation
rows and rejected/deferred the higher-risk surfaces.

Contradiction Or Gap Disposition: no contradiction blocks a reference-only
contract; implementation remains separate.

Claim Update: the only claim is dispatch readiness for a documentation/reference
worker task.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatch author |
| Provider or surface | Codex CLI |
| Session or invocation | 2026-06-20 CGE-T2 CodeGraph LPF/KGR adaptation contract dispatch |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, rg, apply_patch, governance gates |
| Target paths | this work order; CGE-T2 GC-018 baseline |
| Allowed scope source | operator request to issue next Claude work order |
| Before status evidence | clean worktree at committed base `5cb5a8e1`; only recurring Windows global git-ignore permission warning |
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

This work order authorizes only a documentation/reference adaptation contract
and worker-return artifact. It does not authorize CodeGraph runtime adoption,
source/test edits, MCP wiring, watcher/daemon behavior, `.codegraph/`, benchmark
proof, provider/live proof, public-sync, ACE-R1, freeze, readiness, or universal
governed-coding-control claims.
