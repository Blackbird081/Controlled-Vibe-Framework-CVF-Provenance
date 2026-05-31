# CVF Work Order Alpha Mandatory Startup Acknowledgment

Memory class: WORK_ORDER_RECORD

docType: work_order

Date: 2026-05-26

Status: CLOSED_PASS_BOUNDED

## Purpose

Implement Option Alpha: mandatory startup acknowledgment for the existing
cross-agent front doors.

## Authority Chain

Operator request to move to next tranche -> cross-agent memory assessment
Option Alpha -> GC-018 Alpha baseline -> this work order.

## Agent Roles

- Orchestrator: keep scope limited to Alpha.
- Implementer: edit front-door docs.
- Reviewer: verify no hard auto-load or MCP claim is introduced.

## Required First Reads

- `docs/concepts/CVF_CROSS_AGENT_MEMORY_AND_AUTO_LOAD_ASSESSMENT_2026-05-26.md`
- `AGENTS.md`
- `CLAUDE.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

## Pre-Flight Checks

- Confirm VI5-T4/T5 remains parked at `READY_FOR_OPERATOR_ACCEPTANCE`.
- Confirm Alpha does not depend on operator external-agent test results.
- Confirm no live provider proof is required.

## Scope / Target / Owner Boundary

Files allowed:

- `AGENTS.md`
- `CLAUDE.md`
- Alpha governance packets and session/handoff state.

Forbidden scope:

- runtime auto-load;
- MCP server;
- Beta tool config expansion;
- provider/API/receipt/runtime changes.

## Write Ownership

The work order owns only root front-door instruction docs and the Alpha
governance/handoff packets.

## Execution Plan

1. Add matching startup acknowledgment requirement to `AGENTS.md`.
2. Add matching startup acknowledgment requirement to `CLAUDE.md`.
3. Update work order and completion status.
4. Run docs/session gates.
5. Commit and sync active handoff.

## Evidence Requirements

- Changed front-door files contain the acknowledgment requirement.
- Governance checks pass.
- Completion packet records soft-accountability boundary.

## Acceptance Criteria

- New/resumed agents are instructed to read `CVF_SESSION_MEMORY.md`.
- Agents are instructed to resolve `ACTIVE_SESSION_STATE.json`.
- Agents must state or record current mode, active handoff, and next allowed
  move before material governed work.
- Claim boundary remains soft accountability only.

## Review Gate

Reject the work if it claims true runtime auto-load, universal tool support,
or MCP functionality.

## Closure Checklist

- [x] `AGENTS.md` updated.
- [x] `CLAUDE.md` updated.
- [x] Alpha completion packet filed.
- [x] Session/handoff state updated.
- [x] Governance checks pass.

## Return-To-Orchestrator Conditions

Return if the implementation requires changes outside Alpha scope or if the
startup requirement becomes too broad for routine agent work.

## Operator Checkpoint

No manual operator checkpoint is required for this docs-only Alpha bridge.
Operator can later accept Beta/Gamma as separate tranches.

## Claim Boundary

This work order may close only as front-door instruction hardening. It cannot
claim hard enforcement, true auto-load, MCP availability, or cross-tool
coverage beyond `AGENTS.md` and `CLAUDE.md`.
