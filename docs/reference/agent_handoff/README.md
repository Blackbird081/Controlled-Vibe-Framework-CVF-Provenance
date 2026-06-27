# CVF Agent Handoff Reference Front Door

Memory class: POINTER_RECORD

Status: ACTIVE_INDEX

docType: reference

## Purpose

Provide the stable folder front door for the Agent Handoff Contract and its
machine-enforced local views.

## Scope / Target / Owner Boundary

Target: long-lived handoff-boundary governance references.

Owner boundary: this folder owns stable lookup for agent handoff semantics. It
does not own individual work-order evidence, worker returns, session state,
provider execution, public-sync, or the future agent-interaction workspace.

## Central Core

Ratified contract:

`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

Machine-check standard:

`docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`

Mandatory checker:

`governance/compat/check_agent_handoff_boundary.py`

## Required Read Trigger

Read this folder when a task:

- authors or reviews a work order with `dispatchBaseHead`,
  `executionBaseHead`, or `closureBaseHead`;
- uses `WORKER_MUST_NOT_COMMIT` or `WORKER_MAY_COMMIT`;
- assigns multiple agents or multiple roles across dispatch, execution,
  closure, or session-sync phases;
- edits agent handoff, dispatch envelope, commit steward, Agent Operation Trace,
  next-move, or session-sync governance;
- records a seam finding about actor identity, changed-set scope, trace scope,
  commit owner, or cross-batch isolation.

## Local Views

| Local view | Role |
|---|---|
| `docs/work_orders/` | Per-batch work-order handoff evidence |
| `docs/reviews/` | Completion, worker-return, and reviewer evidence |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Machine-readable next-move state |
| `CVF_SESSION_MEMORY.md` | Human-readable session front door |
| active handoff named by `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Active continuity handoff |

## Archive Policy

Stable files in this folder are updated in place and proven through GC-018,
work order, completion review, and git history. Superseded stable files move to
`docs/reference/agent_handoff/archive/` only under a separate governed archive
batch.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-T3 unified handoff-boundary checker |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, pytest |
| Target paths | `docs/reference/agent_handoff/README.md`; `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/test_check_agent_handoff_boundary.py` |
| Allowed scope source | operator authorization for AHB-T3 on 2026-06-17 |
| Before status evidence | HEAD `230565e4`; worktree clean |
| After status evidence | AHB-T3 material closure pending commit |
| Diff evidence | `git diff --name-status 230565e4..HEAD` |
| Approval boundary | bounded governance-control checker and stable reference front door |
| Claim boundary | no runtime/provider/live/public/workspace implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-t3-unified-handoff-boundary-checker-2026-06-17` |
| Expected manifest | `docs/reference/agent_handoff/README.md`; `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/test_check_agent_handoff_boundary.py` |
| Actual changed set | `docs/reference/agent_handoff/README.md`; `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/test_check_agent_handoff_boundary.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This README is a stable pointer record. It does not authorize runtime behavior,
provider calls, public-sync, autonomous mutation, workspace construction, or
production/public readiness claims.
