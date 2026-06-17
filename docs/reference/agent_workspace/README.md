# CVF Agent Interaction Workspace Reference Front Door

Memory class: POINTER_RECORD

Status: ACTIVE_INDEX

docType: reference

## Purpose

Provide the stable folder front door for the future CVF agent-interaction
workspace. This folder defines where future agents read workspace design rules
before proposing, building, or modifying any dedicated Claude/Codex/other-agent
interaction workspace.

## Scope / Target / Owner Boundary

Target: long-lived workspace design governance for agent-to-agent interaction
surfaces.

Owner boundary: this folder owns design requirements, storage layout, and
pre-build control boundaries for the agent-interaction workspace family. It
does not build a workspace, create runtime queues, edit product source, run
provider proof, public-sync, or authorize production/public readiness.

## Central Core

Agent handoff contract:

`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

Agent handoff machine-check local view:

`docs/reference/agent_handoff/README.md`

Workspace design standard:

`docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`

Workspace state topology contract:

`docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`

Workspace option-readiness matrix:

`docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md`

Workspace design machine guard:

`governance/compat/check_agent_workspace_design.py`

Generated workspace state aggregate:

`CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`

Generated workspace state machine guard:

`governance/compat/check_agent_workspace_state.py`

Foundation storage standard:

`docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md`

## Required Read Trigger

Read this folder when a task:

- proposes, analyzes, designs, builds, or modifies the dedicated
  agent-interaction workspace;
- introduces agent-to-agent workspace folders, indexes, queues, inboxes,
  review lanes, shared dashboards, or coordination surfaces;
- changes how Claude, Codex, Gemini, or future agents exchange work outside a
  one-off work order;
- needs to decide whether a workspace artifact is a stable foundation file,
  dated execution evidence, or runtime/product implementation;
- records a finding that agents are losing context, memory, routing, or
  boundary evidence between handoff phases.

## Local Views

| Local view | Role |
|---|---|
| `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | Design boundary and pre-build requirements |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | State topology, lane, storage, and archive contract before any workspace state is built |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md` | Stable option matrix for future build, richer lanes, or further hardening decisions |
| `governance/compat/check_agent_workspace_design.py` | Machine-enforced local view for Agent Workspace Design Control Block |
| `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json` | Generated compact active workspace state view |
| `governance/compat/generate_agent_workspace_state.py` | Generator for workspace state source fragments |
| `governance/compat/check_agent_workspace_state.py` | Drift and topology guard for generated workspace state |
| `docs/reference/agent_handoff/README.md` | Handoff contract and machine-enforced work-order local view |
| `docs/reference/foundation_storage/README.md` | Stable folder/index storage rule |
| `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB tranche state and future workspace routing |
| `docs/work_orders/` | Per-batch authorization before workspace work begins |
| `docs/reviews/` | Completion and reviewer evidence |

## Archive Policy

Stable files in this folder are updated in place and proven through GC-018,
work order, completion review, and git history. Superseded stable workspace
design files move to `docs/reference/agent_workspace/archive/` only under a
separate governed archive batch.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-Tn.4 agent workspace state source checker |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, pytest |
| Target paths | `AGENTS.md`; `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/ACTIVE_AGENT_WORKSPACE_STATE_CORE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`; `docs/baselines/CVF_GC018_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_2026-06-17.md`; `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_state.py`; `governance/compat/generate_agent_workspace_state.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/test_agent_workspace_state.py` |
| Allowed scope source | operator authorization to continue workspace foundation hardening on 2026-06-17 |
| Before status evidence | HEAD `f8964c7a`; clean worktree |
| After status evidence | AHB-Tn.4 material closure pending commit |
| Diff evidence | `git diff --name-status f8964c7a..HEAD` |
| Approval boundary | generated workspace state source/checker foundation only |
| Claim boundary | no workspace build, runtime/provider/live/public/registry implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-tn4-agent-workspace-state-source-checker-2026-06-17` |
| Expected manifest | `AGENTS.md`; `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/ACTIVE_AGENT_WORKSPACE_STATE_CORE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`; `docs/baselines/CVF_GC018_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_2026-06-17.md`; `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_state.py`; `governance/compat/generate_agent_workspace_state.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/test_agent_workspace_state.py` |
| Actual changed set | `AGENTS.md`; `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/ACTIVE_AGENT_WORKSPACE_STATE_CORE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`; `docs/baselines/CVF_GC018_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_2026-06-17.md`; `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_state.py`; `governance/compat/generate_agent_workspace_state.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/test_agent_workspace_state.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This README is a stable pointer record. It does not authorize runtime behavior,
provider calls, public-sync, autonomous mutation, workspace construction, or
production/public readiness claims.
