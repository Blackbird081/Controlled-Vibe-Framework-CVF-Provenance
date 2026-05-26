# CVF Alpha Mandatory Startup Acknowledgment Roadmap

Memory class: ROADMAP_RECORD

docType: roadmap

Date: 2026-05-26

Status: AUTHORIZED_FOR_IMPLEMENTATION

## Purpose

Implement Option Alpha from the cross-agent memory assessment: strengthen the
existing soft auto-load pattern by requiring agents to acknowledge the active
CVF session front door before material governed work.

## Authorization / Decision

Decision: proceed with the low-cost Alpha bridge because the operator parked
VI5-T4/T5 for later manual acceptance and requested the next tranche.

This tranche is authorized only as a front-door instruction hardening step. It
does not authorize MCP server work, runtime auto-injection, or tool-specific
magic filename expansion beyond current `AGENTS.md` and `CLAUDE.md`.

## Scope / Target / Owner Boundary

Owner surfaces:

- `AGENTS.md`
- `CLAUDE.md`

In scope:

- mandatory startup acknowledgment language;
- exact files agents must read;
- one concise acknowledgment sentence;
- boundary that acknowledgment is accountability, not proof of runtime
  auto-load.

Out of scope:

- cvf-mcp-server;
- Gemini/Cursor/Aider config expansion;
- runtime context injection;
- provider/API behavior;
- public-sync;
- hosted or production readiness.

## Non-Goals

This roadmap does not try to make vendor tools truly auto-load repo memory.
That remains outside repo control. It also does not certify that an agent
actually read every byte; it creates a visible accountability requirement.

## Work Plan

1. Add a mandatory startup acknowledgment section to `AGENTS.md`.
2. Add the same requirement to `CLAUDE.md`.
3. Record the requirement in baseline, work order, completion, session memory,
   active handoff, and active state.
4. Run governance compatibility checks.

## Acceptance Criteria

- Both front doors require reading `CVF_SESSION_MEMORY.md`.
- Both front doors require resolving `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Both front doors require naming current mode, active handoff, and next
  allowed move before material governed work.
- Claim boundary states this is soft accountability, not runtime auto-load.

## Evidence Plan

Required:

- docs governance compatibility;
- markdown structural completeness;
- active session state compatibility;
- git diff whitespace check.

No live provider proof is required because this tranche changes docs-only
startup instructions and does not assert AI governance runtime behavior.

## Stop Conditions

Stop if the edits would require broad startup ceremony, MCP implementation,
tool-specific research, or changes outside `AGENTS.md` and `CLAUDE.md`.

## Claim Boundary

This roadmap may claim only mandatory startup acknowledgment instruction
hardening for Claude/Codex front doors. It does not claim true auto-load,
cross-tool coverage, MCP availability, or enforcement beyond agent
instruction-following accountability.
