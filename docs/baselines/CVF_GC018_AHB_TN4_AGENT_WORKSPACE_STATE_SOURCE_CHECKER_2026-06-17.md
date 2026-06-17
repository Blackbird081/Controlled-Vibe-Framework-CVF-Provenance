# CVF GC-018 - AHB-Tn.4 Agent Workspace State Source Checker

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018

Date: 2026-06-17

Batch ID: AHB-Tn.4

Owner: Codex

executionBaseHead: `f8964c7a`

## Purpose

Authorize a bounded foundation tranche that creates generated workspace state
source fragments, a deterministic generator, and a drift/topology checker for
the future agent-interaction workspace.

## Scope / Target / Owner Boundary

Target: generated workspace state foundation only.

Owner boundary: Codex owns dispatch, implementation, review, closure, material
commit, and later session-sync. This GC-018 does not authorize a workspace UI,
runtime queue, provider/live proof, public-sync, registry edit, production
readiness, or public readiness.

## Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | 2026-06-17 continue workspace foundation hardening | ACCEPTED |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPTED |
| AHB-Tn.3 predecessor | `docs/reviews/CVF_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_COMPLETION_2026-06-17.md` | PREDECESSOR_SATISFIED |
| Topology contract | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | ACTIVE_CONTRACT |
| JSON generated aggregate standard | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | ACTIVE_STANDARD |

## Source / Predecessor Evidence

| Source | Evidence | Disposition |
|---|---|---|
| AHB-Tn.3 closure | `docs/reviews/CVF_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_COMPLETION_2026-06-17.md` | PREDECESSOR_SATISFIED |
| State topology contract | required state fields and generated-state candidate layout | ACCEPT |
| Generated aggregate standard | source layout, generator, checker, drift discipline | ACCEPT |
| Existing active session generator | source-generated aggregate implementation pattern | ACCEPT |

## Decision / Baseline / Proposed Tranche

Decision: `APPROVE_BOUNDED_AHB_TN4`.

Baseline: HEAD `f8964c7a` after AHB-Tn.3 material and session-sync closure.

Proposed tranche: create generated workspace state source fragments,
deterministic generator, drift/topology checker, focused tests, autorun/local
hook binding, and stable front-door pointers. Do not build workspace UI,
runtime queues, provider routes, public-sync, registries, or production/public
readiness surfaces.

## Authorized Changed Set

| Path | Disposition |
|---|---|
| `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json` | generated aggregate |
| `CVF_SESSION/agent_workspace/state/ACTIVE_AGENT_WORKSPACE_STATE_CORE.json` | generated source core |
| `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json` | generated source item |
| `governance/compat/generate_agent_workspace_state.py` | generator |
| `governance/compat/check_agent_workspace_state.py` | drift/topology checker |
| `governance/compat/test_agent_workspace_state.py` | focused tests |
| `governance/compat/run_agent_commit_steward_preflight.py` | steward material/session classification update |
| `governance/compat/test_run_agent_commit_steward_preflight.py` | steward focused test update |
| `governance/compat/run_agent_autorun_workflow_gate.py` | autorun binding |
| `governance/compat/run_local_governance_hook_chain.py` | local hook binding |
| `AGENTS.md` | mandatory rule pointer |
| `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | steward protocol pointer |
| `docs/reference/agent_workspace/README.md` | workspace front-door pointer |
| `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | design standard pointer |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | topology contract pointer |
| `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | generated aggregate registry |
| `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | operational front-door index |
| `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | roadmap closure |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_FOR_CODEX_2026-06-17.md` | work order |
| `docs/reviews/CVF_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_COMPLETION_2026-06-17.md` | completion review |
| `docs/baselines/CVF_GC018_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_2026-06-17.md` | this baseline |

## Generated Aggregate Discipline

Disposition: `GENERATED_SOURCE_LAYOUT_ADDED`.

The generated aggregate is:

`CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`

The source layout is:

`CVF_SESSION/agent_workspace/state/`

The generator is:

`governance/compat/generate_agent_workspace_state.py`

The checker is:

`governance/compat/check_agent_workspace_state.py`

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Generated aggregate exists | aggregate and source files committed |
| Aggregate is source-generated | `generate_agent_workspace_state.py --check` PASS |
| Required topology fields enforced | checker and tests PASS |
| Guard is mandatory | autorun and local hook chain include checker |
| Front doors point to state | AGENTS, workspace README, design standard, topology contract, JSON standard, operational index updated |
| No workspace build | completion records no UI/runtime/provider/public/registry scope |

## Evidence / Verification

| Evidence | Command or artifact |
|---|---|
| Generated aggregate drift | `python governance/compat/generate_agent_workspace_state.py --check` |
| Workspace state checker | `python governance/compat/check_agent_workspace_state.py --base f8964c7a --head HEAD --enforce` |
| Focused tests | `python -m pytest governance/compat/test_agent_workspace_state.py governance/compat/test_check_agent_workspace_design.py -q` |
| Autorun/local-hook binding | `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Closure evidence | `docs/reviews/CVF_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_COMPLETION_2026-06-17.md` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance foundation. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-Tn.4 agent workspace state source checker |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, pytest |
| Target paths | `AGENTS.md`; `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/ACTIVE_AGENT_WORKSPACE_STATE_CORE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`; `docs/baselines/CVF_GC018_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_2026-06-17.md`; `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`; `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_state.py`; `governance/compat/generate_agent_workspace_state.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/test_agent_workspace_state.py`; `governance/compat/test_run_agent_commit_steward_preflight.py` |
| Allowed scope source | operator authorization to continue workspace foundation hardening on 2026-06-17 |
| Before status evidence | HEAD `f8964c7a`; clean worktree |
| After status evidence | AHB-Tn.4 material closure pending commit |
| Diff evidence | `git diff --name-status f8964c7a..HEAD` |
| Approval boundary | bounded generated workspace state source/checker foundation |
| Claim boundary | no workspace build, runtime/provider/live/public/registry implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-tn4-agent-workspace-state-source-checker-2026-06-17` |
| Expected manifest | `AGENTS.md`; `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/ACTIVE_AGENT_WORKSPACE_STATE_CORE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`; `docs/baselines/CVF_GC018_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_2026-06-17.md`; `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`; `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_state.py`; `governance/compat/generate_agent_workspace_state.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/test_agent_workspace_state.py`; `governance/compat/test_run_agent_commit_steward_preflight.py` |
| Actual changed set | `AGENTS.md`; `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/ACTIVE_AGENT_WORKSPACE_STATE_CORE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`; `docs/baselines/CVF_GC018_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_2026-06-17.md`; `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`; `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_state.py`; `governance/compat/generate_agent_workspace_state.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/test_agent_workspace_state.py`; `governance/compat/test_run_agent_commit_steward_preflight.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes generated workspace state source/checker foundation
only. It does not authorize workspace construction, runtime behavior, provider
calls, public-sync, registry edits, autonomous mutation, or production/public
readiness claims.
