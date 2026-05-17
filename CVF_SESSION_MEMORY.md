# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-05-18

## Purpose

This file is the single session-memory entry point for new agents, resumed
agents, future `cvf-cli`, and future `cvf-mcp-server` startup.

It does not replace durable evidence, roadmaps, handoffs, or governance guards.
It routes agents to the current session state before they choose which deeper
materials to load.

## Owner And Source

Owner: CVF governance/session-continuity surface.

Source truth:

- human operator session decision on 2026-05-17
- active state registry at `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- review packets listed in Required First Reads

## Scope Boundary

In scope:

- session-start routing
- active handoff pointer routing
- current blocked-work posture
- startup guard routing for agents and future CLI/MCP entrypoints

Out of scope:

- replacing handoffs
- replacing evidence packets
- replacing governance guards
- implementing `cvf-cli` or `cvf-mcp-server`

## Active State Registry

Machine-readable active state:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

Agents and tools must resolve this registry before treating any root handoff as
current.

## Current Session Mode

- Current mode: `system_reconvergence_stop`
- Freeze posture: `governance_kernel_freeze_recommended`
- Active handoff pointer: `AGENT_HANDOFF_V9_2026-05-18.md`
- Historical handoff archive: `CVF_SESSION/handoffs/archive/`
- Broad absorption, new governance semantics, and runtime expansion are paused
  until the reconvergence/freeze decision is resolved.

## Required First Reads

Read these first for the current 17.05 reconvergence context:

- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_SYSTEM_RECONVERGENCE_STOP_DECISION_2026-05-17.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_AGENT_HANDOFF_AND_MEMORY_GAP_CODEX_AUDIT_2026-05-17.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_SINGLE_SESSION_MEMORY_FRONT_DOOR_PROPOSAL_2026-05-17.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_AGENT_ORCHESTRATOR_ROLE_ABSORPTION_GAP_CODEX_AUDIT_2026-05-17.md`

## Required Startup Guards

Route through:

- `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md`
- `docs/reference/CVF_SESSION_GOVERNANCE_BOOTSTRAP.md`
- `governance/toolkit/05_OPERATION/CVF_SESSION_GOVERNANCE_BOOTSTRAP_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_AGENT_HANDOFF_TRANSITION_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_AGENT_HANDOFF_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_MEMORY_GOVERNANCE_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_GOVERNED_ARTIFACT_AUTHORING_GUARD.md`

## Protocol Requirements

1. Load this file first.
2. Resolve `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
3. Confirm active handoff, current mode, blocked work classes, and next allowed
   move.
4. Load only the first-read packets and guards required by the active state.
5. Treat root handoff files as current only when the active state registry
   points to them.

## Blocked Work Classes

Do not start these work classes from this session state without a later explicit
roadmap or human override:

- broad external knowledge absorption
- new governance semantics
- new role taxonomies
- new policy, risk, or guard engines
- new receipt envelopes
- new memory tiers
- new capability workflow runtime contracts
- new provider execution semantics
- public claims of a coherent governed capability runtime

## Startup Acknowledgment

Before material governed work, an agent should be able to state:

- active session mode
- active handoff path
- required first-read packet set
- blocked work classes
- next allowed move

## Next Allowed Move

Maintain the session-memory front door, active-state registry, and reconvergence
inventory/owner maps. Do not broaden absorption or runtime semantics until the
Governance Kernel Freeze decision is accepted or superseded.

## Enforcement And Verification

Machine check:

- `python governance/compat/check_active_session_state.py --enforce`

Hook chain:

- `governance/compat/run_local_governance_hook_chain.py`

## Boundaries And Non-Goals

- This front door does not assert that CVF already has a unified governed
  capability runtime.
- This front door does not authorize new semantic layers.
- This front door does not make private review packets public.
- This front door does not remove historical handoffs.

## Related Artifacts

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/READ_FIRST.md`
- `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md`
- `CVF_SESSION/handoffs/archive/`
- `AGENTS.md`
- `CLAUDE.md`
- `AGENT_HANDOFF_V9_2026-05-18.md`

## Claim Boundary

This artifact establishes a governed session-memory front door and machine
checkable active-state pointer. It does not complete the broader Governance
Kernel Freeze or system reconvergence work.
