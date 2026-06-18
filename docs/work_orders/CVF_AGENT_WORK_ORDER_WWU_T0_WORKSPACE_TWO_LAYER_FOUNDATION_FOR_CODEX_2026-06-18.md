# CVF Agent Work Order - WWU-T0 Workspace Two-Layer Foundation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: work_order

Batch ID: WWU-T0

Owner: Codex

Worker: Codex

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `f688fa9e`

executionBaseHead: `f688fa9e`

closureBaseHead: `f688fa9e`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Role: Codex implementer/reviewer/closer

Canonical packet: `docs/baselines/CVF_GC018_WWU_T0_WORKSPACE_TWO_LAYER_FOUNDATION_2026-06-18.md`

Commit mode: WORKER_MAY_COMMIT

executionBaseHead: `f688fa9e`

Current-time notes: 2026-06-18; EARC-T3B is closed, and the operator asked to clarify the absorbed two-layer workspace split before upgrading CVF Web.

Do-not-misread notes: do not edit product UI, implement MCP, mutate Local Workspace Runtime, run providers, public-sync, import raw external package files, or claim readiness.

Required first actions: create the stable two-layer standard, wire it into workspace reference front doors, create the CVF Web Workspace upgrade roadmap, add registry coverage, run gates, commit material, and report the next bounded Web tranche.

Return contract: commit accepted material and leave WWU-T1 as the next source-verification audit before any CVF Web UI implementation.

## Purpose

Make the CVF Web Workspace versus CVF Local Workspace Runtime split explicit in
CVF-owned foundation artifacts, then open the CVF Web Workspace upgrade roadmap.

## Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | 2026-06-18 request to clarify the absorbed split and upgrade CVF Web | ACCEPTED |
| Active session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | EARC-T3B_CLOSED_T2_T4_PARKED |
| GC-018 baseline | `docs/baselines/CVF_GC018_WWU_T0_WORKSPACE_TWO_LAYER_FOUNDATION_2026-06-18.md` | CLOSURE_SATISFIED |
| Workspace front door | `docs/reference/agent_workspace/README.md` | ACTIVE_INDEX |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one-agent-many-roles: Codex holds dispatcher, implementer, reviewer, closer roles |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE |
| baseHeadFor(phase) | `dispatchBaseHead=f688fa9e`; `executionBaseHead=f688fa9e`; `closureBaseHead=f688fa9e` |
| changedSetScope(phase) | WWU-T0 foundation documentation, roadmap, registry, and completion only |
| traceScope(phase, actor) | one Codex Agent Operation Trace Block covers this material batch |
| commitOwner(phase) | Codex owns material commit |
| crossBatchIsolation | no product UI, runtime/MCP, public-sync, or provider work in this batch |
| nextMoveSurfaces | WWU roadmap names WWU-T1 as the next Web Workspace audit candidate |
| Closer designation | Codex is the closer |

## Workspace Two-Layer Control Block

| Field | Disposition |
|---|---|
| targetLayer | `BOTH_WITH_BOUNDARY` |
| operatorSurface | `CVF_WEB_WORKSPACE`: clarified as human-facing read/decision surface only |
| agentExecutionSurface | `CVF_LOCAL_WORKSPACE_RUNTIME`: clarified as future MCP/CLI/CVF enforcement substrate only |
| sourceOfTruth | `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` |
| mutationBoundary | no runtime or product mutation in this tranche |
| receiptBoundary | completion review and governance gates only |
| forbiddenConflationCheck | Web Workspace and Local Runtime are explicitly separated and not merged |

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | Clarify workspace architecture and future Web upgrade boundary |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` supplies the workspace-specific architecture rule |
| Front door | `docs/reference/agent_workspace/README.md` |
| Design standard | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Storage class | stable foundation standard plus dated GC-018/work-order/completion/roadmap |
| Handoff fields | AHB block above owns route/base/commit semantics |
| State ownership | no generated workspace state file changed |
| Guard owner | existing workspace guards; no new checker in WWU-T0 |
| Build boundary | runtime source: no; product UI: no; provider proof: no; public-sync: no; registry edits: yes, GC-051 source entry and generated aggregate only; runtime/MCP: no |

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | Convert operator instruction into bounded WWU-T0 packet |
| Implementer | Codex | Add stable standard, roadmap, registry, and reference updates |
| Reviewer / closer | Codex | Run gates and commit accepted material |
| Operator | Human operator | Later approve WWU-T1/T2/T3 sequencing changes if needed |

## Allowed / Forbidden Scope

Allowed:

- `docs/baselines/CVF_GC018_WWU_T0_WORKSPACE_TWO_LAYER_FOUNDATION_2026-06-18.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T0_WORKSPACE_TWO_LAYER_FOUNDATION_FOR_CODEX_2026-06-18.md`
- `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md`
- `docs/reference/agent_workspace/README.md`
- `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md`
- `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md`
- `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md`
- `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md`
- `docs/corpus-intelligence/registry/entries/wwu-t0-workspace-two-layer-foundation.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/reviews/CVF_WWU_T0_WORKSPACE_TWO_LAYER_FOUNDATION_COMPLETION_2026-06-18.md`

Forbidden:

- edit `cvf-web` product source;
- implement product UI;
- implement MCP, CLI wrappers, runtime queues, or Local Workspace Runtime;
- run provider/live proof;
- public-sync;
- import raw external package code;
- claim production/public readiness.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation files touched | `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md`; workspace local-view references |
| Storage class | Central foundation standard inside existing local-view folder |
| Index/front door | `docs/reference/agent_workspace/README.md` |
| Date policy | stable path for durable standard; dated paths for GC-018, work order, roadmap, and completion |
| Archive disposition | N/A with reason: no superseded file is archived in this batch |
| Deferred layout work | N/A with reason: storage/index work is handled now |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Operator-facing workspace view is currently a read model, not UI implementation. | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | `## Purpose`; `## Claim Boundary` | `read model only` | agent workspace operator view plan | ACCEPT |
| Runtime expansion contract blocks runtime queue execution, provider proof, public-sync, registry edits, product UI, and readiness claims. | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | `## Scope / Target / Owner Boundary`; `## Runtime Expansion Boundary` | `blocked until fresh GC-018` | runtime expansion readiness contract | ACCEPT |
| External package absorption map treats raw import as rejected and selective adaptation as the absorption mode. | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | `## Source Package Status` | `Raw import`; `Absorption mode` | workspace external package absorption map | ACCEPT |
| EARC-T3A rejected the hard-coded workflow enum as authority. | `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_WORKSPACE_LAYER_2026-06-18.md` | `## Required Absorption Table` | `EARC-T3A-E05` | external return absorption pilot | ACCEPT |
| CVF Web has an existing governance-surface inventory but not full workspace/runtime inheritance. | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/docs/reference/CVF_W112_WEB_GOVERNANCE_SURFACE_INVENTORY_2026-04-22.md` | `## Non-Claims`; `## Claim Boundary` | `Agent workspace enforcement`; `not the full CVF runtime` | CVF Web governance surface inventory | ACCEPT |

## Required First Reads

| Artifact | Reason |
|---|---|
| `CVF_SESSION_MEMORY.md` | active front door |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | machine-readable current mode |
| `docs/reference/agent_workspace/README.md` | workspace front door |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | Web Workspace read-model precedent |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | Local Runtime/MCP boundary |
| `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | external package absorption boundary |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work order action | Disposition |
|---|---|---|
| Clarify the two-layer architecture before upgrading CVF Web. | Add stable two-layer standard and wire it into front doors. | DONE |
| Keep CVF Web upgrade separate from Local Runtime/MCP. | Create WWU roadmap with T1 Web audit, T2 UI, T3 runtime/MCP parked. | DONE |
| Preserve CVF-first absorption boundary. | Update external package absorption map to classify Web/runtime areas without importing external code. | DONE |

## Implementation Requirements

- Add `CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md`.
- Update the agent workspace README.
- Update operator view and runtime expansion local views.
- Update the external package absorption map.
- Create the CVF Web Workspace upgrade roadmap.
- Add GC-051 registry coverage and regenerate the aggregate.
- Create completion review and run governance gates.

## Pre-Flight Checks

```powershell
git status --short
git diff --check
python governance/compat/generate_corpus_scan_registry.py --check
python governance/compat/check_work_order_dispatch_quality.py --base f688fa9e --head HEAD --enforce
```

## Write Ownership

Codex may write only the WWU-T0 paths named in the GC-018 and work order
manifest. Product UI, Local Runtime/MCP, provider, public-sync, and raw external
package paths are outside this work order.

## Execution Plan

1. Add the stable two-layer standard.
2. Wire it into workspace reference front doors and local views.
3. Create WWU roadmap and dated execution artifacts.
4. Add GC-051 registry source and regenerate aggregate.
5. Run reviewer-fast and closure gates.
6. Commit accepted material.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| Foundation storage layout gate | PASS |
| Dispatch quality gate | PASS |
| Machine closure package gate | PASS |
| Corpus registry check | PASS |
| Worker return fast gate | PASS before commit |

## Review Gate

Reviewer must reject the batch if it edits product UI, runtime/MCP, provider,
public-sync, or raw external package files, or if the two-layer standard is not
indexed from the workspace front door.

## Closure Checklist

- [x] Stable two-layer standard added.
- [x] Workspace front door updated.
- [x] Operator view and runtime local views updated.
- [x] WWU roadmap added.
- [x] Registry source and aggregate updated.
- [x] Machine Closure Package rows included.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-18 WWU-T0 workspace two-layer foundation |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch |
| Target paths | WWU-T0 GC-018; work order; two-layer standard; workspace README; operator view plan; runtime expansion contract; external package absorption map; WWU roadmap; GC-051 registry entry and aggregate; completion review |
| Allowed scope source | operator instruction to clarify the absorbed split and prepare CVF Web upgrade |
| Before status evidence | base `f688fa9e`; clean worktree |
| After status evidence | WWU-T0 material closure pending commit |
| Diff evidence | `git diff --name-status f688fa9e..HEAD` |
| Approval boundary | documentation/reference foundation and roadmap only |
| Claim boundary | no product UI, Local Runtime mutation, MCP implementation, provider/live call, public-sync, raw external package import, or readiness claim |
| Agent type | Codex implementer/reviewer/closer |
| Invocation ID | `wwu-t0-workspace-two-layer-foundation-2026-06-18` |
| Expected manifest | `docs/baselines/CVF_GC018_WWU_T0_WORKSPACE_TWO_LAYER_FOUNDATION_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T0_WORKSPACE_TWO_LAYER_FOUNDATION_FOR_CODEX_2026-06-18.md`; `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md`; `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md`; `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md`; `docs/corpus-intelligence/registry/entries/wwu-t0-workspace-two-layer-foundation.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/reviews/CVF_WWU_T0_WORKSPACE_TWO_LAYER_FOUNDATION_COMPLETION_2026-06-18.md` |
| Actual changed set | `docs/baselines/CVF_GC018_WWU_T0_WORKSPACE_TWO_LAYER_FOUNDATION_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T0_WORKSPACE_TWO_LAYER_FOUNDATION_FOR_CODEX_2026-06-18.md`; `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md`; `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md`; `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md`; `docs/corpus-intelligence/registry/entries/wwu-t0-workspace-two-layer-foundation.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/reviews/CVF_WWU_T0_WORKSPACE_TWO_LAYER_FOUNDATION_COMPLETION_2026-06-18.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` only after gates pass and WWU-T1 remains the next
bounded Web Workspace audit step.

## Operator Checkpoint

Operator authorization is required before WWU-T2 product UI implementation,
WWU-T3 runtime/MCP implementation, provider/live proof, or public-sync.

## Acceptance Criteria

- The standard explicitly defines `CVF_WEB_WORKSPACE` and `CVF_LOCAL_WORKSPACE_RUNTIME`.
- The front door points to the standard.
- The roadmap names WWU-T1 as source-verification audit before UI implementation.
- No `cvf-web` product source, MCP runtime, provider/live, public-sync, or raw external package files are changed.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_WWU_T0_WORKSPACE_TWO_LAYER_FOUNDATION_COMPLETION_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 | `docs/baselines/CVF_GC018_WWU_T0_WORKSPACE_TWO_LAYER_FOUNDATION_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | `ROADMAP_T0_CLOSED_T1_READY_T2_T3_PARKED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated from source entries | PASS |
| Registry Markdown | BLOCKED with reason: no separate markdown registry is required for this reference family | no path changed | BLOCKED with reason |
| External evidence digest | `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_WORKSPACE_LAYER_2026-06-18.md` | prior governed absorption digest covers the external workspace package; representative sha256 `a267edd4f9702daa1047034520f3e24b0c7321b17d1451a858b12a2845b7cd82` | PASS |
| System loop interlock | BLOCKED with reason: no runtime interlock implementation changed | no path changed | BLOCKED with reason |
| Session continuity | separate session-sync follows material commit | active session surfaces update after material commit if next move changes | N/A with reason |
| Runtime proof | BLOCKED with reason: runtime/provider/MCP proof is out of scope | no runtime proof required | BLOCKED with reason |
| Public export disposition | `DEFERRED_PRIVATE_ONLY` | private provenance foundation work order | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation clarification only.

## Claim Boundary

This work order closes a documentation/reference foundation tranche only.
