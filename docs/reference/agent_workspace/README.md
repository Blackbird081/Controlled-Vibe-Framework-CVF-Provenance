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

Workspace design machine guard:

`governance/compat/check_agent_workspace_design.py`

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
| `governance/compat/check_agent_workspace_design.py` | Machine-enforced local view for Agent Workspace Design Control Block |
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
| Session or invocation | 2026-06-17 AHB-Tn.1 agent-interaction workspace analysis/design |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch |
| Target paths | `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `governance/compat/check_agent_workspace_design.py`; `governance/compat/test_check_agent_workspace_design.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Allowed scope source | operator authorization for AHB-Tn.2 workspace-foundation hardening on 2026-06-17 |
| Before status evidence | HEAD `5c79881e`; clean worktree |
| After status evidence | AHB-Tn.2 material closure pending commit |
| Diff evidence | `git diff --name-status 5c79881e..HEAD` |
| Approval boundary | bounded workspace design checker and foundation hardening only |
| Claim boundary | no workspace build, runtime/provider/live/public/registry implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-tn2-agent-workspace-design-checker-2026-06-17` |
| Expected manifest | `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `governance/compat/check_agent_workspace_design.py`; `governance/compat/test_check_agent_workspace_design.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Actual changed set | AHB-Tn.2 material changed set, verified in completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This README is a stable pointer record. It does not authorize runtime behavior,
provider calls, public-sync, autonomous mutation, workspace construction, or
production/public readiness claims.
