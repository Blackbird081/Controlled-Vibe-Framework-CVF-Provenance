# Worker Return Lane

Memory class: POINTER_RECORD

Status: ACTIVE_LANE_POINTER

docType: reference

## Purpose

Orient agents to the local `worker_return` lane in the bounded agent workspace
skeleton.

## Scope / Target / Owner Boundary

Target: `CVF_SESSION/agent_workspace/workspace/lanes/worker_return/`.

Owner boundary: the lane folder is a retrieval anchor only. Active state
records belong in `CVF_SESSION/agent_workspace/state/items/`.

## Claim Boundary

This lane pointer does not authorize runtime queues, scheduler queues,
provider calls, public-sync, registry edits, production readiness, or public
readiness.

## Related Artifacts

- `docs/reference/agent_workspace/README.md`
- `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_LANE_TAXONOMY.md`
- `CVF_SESSION/agent_workspace/workspace/lanes/README.md`
