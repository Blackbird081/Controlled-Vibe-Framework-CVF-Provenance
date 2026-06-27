# CVF Agent Workspace Queue Family Index

Memory class: POINTER_RECORD

Status: ACTIVE_INDEX

docType: reference

## Purpose

Index the bounded queue-family pointers for the agent workspace runtime queue
skeleton.

## Scope / Target / Owner Boundary

Target: queue-family navigation for future workspace design.

Owner boundary: `QUEUE_SKELETON_ONLY`. This index is not runtime storage and is
not a scheduler.

## Queue Families

| Queue family | Path | Maps to state lane |
|---|---|---|
| intake | `CVF_SESSION/agent_workspace/runtime_queue/queues/intake/README.md` | `intake` |
| dispatch | `CVF_SESSION/agent_workspace/runtime_queue/queues/dispatch/README.md` | `dispatch` |
| review | `CVF_SESSION/agent_workspace/runtime_queue/queues/review/README.md` | `review` |
| session_sync | `CVF_SESSION/agent_workspace/runtime_queue/queues/session_sync/README.md` | `session_sync` |
| parked | `CVF_SESSION/agent_workspace/runtime_queue/queues/parked/README.md` | `parked` |

## State Source Of Truth

Queue-family pointers do not replace generated workspace state. Current
workspace items live under `CVF_SESSION/agent_workspace/state/items/` and are
generated into `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`.

## Claim Boundary

This index is structural only. It does not authorize runtime queue records,
dequeue/ack semantics, provider calls, public-sync, registry edits, UI, or
production/public readiness.
