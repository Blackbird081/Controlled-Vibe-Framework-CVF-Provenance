# CVF Agent Workspace Skeleton

Memory class: POINTER_RECORD

Status: ACTIVE_SKELETON

docType: reference

## Purpose

Provide the bounded local workspace skeleton for agent-to-agent coordination
before any runtime queue, UI, provider route, public-sync surface, registry
edit, or production/public readiness claim exists.

## Scope / Target / Owner Boundary

Target: stable local folder surface for workspace lane discovery and governed
state-backed coordination.

Owner boundary: this skeleton is a repo-local governance workspace surface. It
does not execute work, schedule workers, call providers, mutate product
runtime, expose public UI, or replace work orders, worker returns, completion
reviews, active session state, or active handoff records.

## Central Core

Stable workspace reference front door:

`docs/reference/agent_workspace/README.md`

Agent Handoff Contract:

`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

Workspace state topology contract:

`docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`

Workspace lane taxonomy:

`docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_LANE_TAXONOMY.md`

Generated active workspace state:

`CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`

Skeleton machine guard:

`governance/compat/check_agent_workspace_skeleton.py`

## Local Views

| Local view | Role |
|---|---|
| `CVF_SESSION/agent_workspace/workspace/lanes/README.md` | Lane folder index |
| `CVF_SESSION/agent_workspace/workspace/lanes/intake/` | Intake lane placeholder |
| `CVF_SESSION/agent_workspace/workspace/lanes/dispatch/` | Dispatch lane placeholder |
| `CVF_SESSION/agent_workspace/workspace/lanes/execution/` | Execution lane placeholder |
| `CVF_SESSION/agent_workspace/workspace/lanes/worker_return/` | Worker-return lane placeholder |
| `CVF_SESSION/agent_workspace/workspace/lanes/review/` | Review lane placeholder |
| `CVF_SESSION/agent_workspace/workspace/lanes/accepted_material/` | Accepted-material lane placeholder |
| `CVF_SESSION/agent_workspace/workspace/lanes/session_sync/` | Session-sync lane placeholder |
| `CVF_SESSION/agent_workspace/workspace/lanes/parked/` | Parked lane placeholder |
| `CVF_SESSION/agent_workspace/workspace/lanes/blocked/` | Blocked lane placeholder |
| `CVF_SESSION/agent_workspace/workspace/lanes/archive_ready/` | Archive-ready lane placeholder |

## Usage Rule

Agents may read this skeleton to orient workspace lane vocabulary. These lane
folders are not runtime queues. Agents must not create active work by dropping
ad hoc files into lane folders. Active
workspace state remains governed by source fragments under
`CVF_SESSION/agent_workspace/state/`, the generator, and the active aggregate.

To change active workspace state, edit the source item, run:

```powershell
python governance/compat/generate_agent_workspace_state.py --generate
```

Then run:

```powershell
python governance/compat/check_agent_workspace_state.py --base <baseHead> --head HEAD --enforce
python governance/compat/check_agent_workspace_skeleton.py --base <baseHead> --head HEAD --enforce
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance workspace skeleton. No public-sync batch is
authorized.

## Claim Boundary

This skeleton is a local governed coordination surface only. It does not build
workspace runtime behavior, queues, UI, provider calls, public-sync, registry
edits, production readiness, or public readiness.
