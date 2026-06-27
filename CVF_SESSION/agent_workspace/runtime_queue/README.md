# CVF Agent Workspace Runtime Queue Skeleton

Memory class: POINTER_RECORD

Status: ACTIVE_QUEUE_SKELETON

docType: reference

## Purpose

Provide a bounded local folder front door for future agent workspace runtime
queue design. This is a queue skeleton, not an executable queue.

## Scope / Target / Owner Boundary

Target: future queue-oriented workspace design.

Owner boundary: `QUEUE_SKELETON_ONLY`. This folder may contain README guidance
and queue-family pointers. It must not contain executable queue items,
schedulers, dequeue/ack logic, provider calls, secrets, product UI state,
public-sync content, registry edits, or production readiness claims.

## Central Core

| Surface | Role |
|---|---|
| `docs/reference/agent_workspace/README.md` | stable workspace front door |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | runtime expansion boundary |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | generated state source of truth |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | operator read-model plan |
| `governance/compat/check_agent_workspace_runtime_boundary.py` | runtime boundary guard |

## Local Views

| Path | Role |
|---|---|
| `CVF_SESSION/agent_workspace/runtime_queue/queues/README.md` | queue-family index |
| `CVF_SESSION/agent_workspace/runtime_queue/queues/intake/README.md` | intake queue pointer |
| `CVF_SESSION/agent_workspace/runtime_queue/queues/dispatch/README.md` | dispatch queue pointer |
| `CVF_SESSION/agent_workspace/runtime_queue/queues/review/README.md` | review queue pointer |
| `CVF_SESSION/agent_workspace/runtime_queue/queues/session_sync/README.md` | session-sync queue pointer |
| `CVF_SESSION/agent_workspace/runtime_queue/queues/parked/README.md` | parked queue pointer |

## Queue Skeleton Rules

- Queue folders are documentation pointers only.
- Workspace state remains governed by
  `CVF_SESSION/agent_workspace/state/items/` and generated into
  `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`.
- No scheduler, daemon, worker loop, runtime mutation, provider call, live
  proof, public-sync, registry edit, product UI, or production claim is
  authorized by this skeleton.
- Future executable queue work must open a fresh GC-018 and Runtime Expansion
  Control Block.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance workspace foundation. No public-sync batch is
authorized.

## Claim Boundary

This is a local queue skeleton only. It does not execute work, store live queue
items, run providers, public-sync, edit registries, build UI, or claim
production/public readiness.
