# CVF Agent Workspace Lane Index

Memory class: POINTER_RECORD

Status: ACTIVE_INDEX

docType: reference

## Purpose

Index the local lane folders for the bounded agent workspace skeleton. These
folders mirror the canonical lane taxonomy so agents can orient quickly without
inventing ad hoc handoff buckets.

## Scope / Target / Owner Boundary

Target: local lane folder index for the bounded agent workspace skeleton.

Owner boundary: this index maps folders to canonical lanes only. It does not
create runtime queues, scheduler queues, provider queues, issue trackers,
public surfaces, or active workspace state.

## Lane Folders

| Lane | Folder | Active-state source |
|---|---|---|
| `intake` | `CVF_SESSION/agent_workspace/workspace/lanes/intake/` | `CVF_SESSION/agent_workspace/state/items/` |
| `dispatch` | `CVF_SESSION/agent_workspace/workspace/lanes/dispatch/` | `CVF_SESSION/agent_workspace/state/items/` |
| `execution` | `CVF_SESSION/agent_workspace/workspace/lanes/execution/` | `CVF_SESSION/agent_workspace/state/items/` |
| `worker_return` | `CVF_SESSION/agent_workspace/workspace/lanes/worker_return/` | `CVF_SESSION/agent_workspace/state/items/` |
| `review` | `CVF_SESSION/agent_workspace/workspace/lanes/review/` | `CVF_SESSION/agent_workspace/state/items/` |
| `accepted_material` | `CVF_SESSION/agent_workspace/workspace/lanes/accepted_material/` | `CVF_SESSION/agent_workspace/state/items/` |
| `session_sync` | `CVF_SESSION/agent_workspace/workspace/lanes/session_sync/` | `CVF_SESSION/agent_workspace/state/items/` |
| `parked` | `CVF_SESSION/agent_workspace/workspace/lanes/parked/` | `CVF_SESSION/agent_workspace/state/items/` |
| `blocked` | `CVF_SESSION/agent_workspace/workspace/lanes/blocked/` | `CVF_SESSION/agent_workspace/state/items/` |
| `archive_ready` | `CVF_SESSION/agent_workspace/workspace/lanes/archive_ready/` | `CVF_SESSION/agent_workspace/state/items/` |

## Boundary

The lane folders are placeholders and retrieval anchors. They are not runtime
queues, scheduler queues, provider queues, issue trackers, or public surfaces.
The machine-readable state source remains
`CVF_SESSION/agent_workspace/state/items/`.

## Claim Boundary

This lane index does not authorize runtime behavior, provider calls,
public-sync, registry edits, production readiness, or public readiness.
