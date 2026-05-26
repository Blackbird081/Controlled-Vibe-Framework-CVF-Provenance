# CVF Work Order Beta Cross-Agent Memory Tool Config Coverage

Memory class: WORK_ORDER_RECORD

docType: work_order

Date: 2026-05-26

Status: READY_FOR_OPERATOR_TOOL_VERIFICATION

## Purpose

Implement Beta from the cross-agent memory progression roadmap by adding
per-tool startup acknowledgment config coverage for Gemini, Cursor, and Aider.

## Authority Chain

Operator authorization -> cross-agent memory progression roadmap -> GC-018 Beta
baseline -> this work order.

## Agent Roles

- Orchestrator: keep Beta limited to config coverage.
- Researcher: verify tool-specific config mechanisms from primary docs.
- Implementer: add config files with the Alpha startup acknowledgment contract.
- Reviewer: check false hard-enforcement claims and scope drift.

## Required First Reads

- `docs/roadmaps/CVF_CROSS_AGENT_MEMORY_PROGRESSION_ROADMAP_2026-05-26.md`
- `docs/baselines/CVF_GC018_BETA_CROSS_AGENT_MEMORY_TOOL_CONFIG_COVERAGE_2026-05-26.md`
- `AGENTS.md`
- `CLAUDE.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

## Pre-Flight Checks

- Confirm Beta only, not Gamma/Delta.
- Confirm no runtime/provider/API/route/receipt change is required.
- Confirm tool launch verification can be separated from static config coverage
  if tools are unavailable locally.

## Scope / Target / Owner Boundary

Files owned:

- `GEMINI.md`
- `.cursor/rules/cvf-startup-acknowledgment.mdc`
- `.aider.conf.yml`
- `CONVENTIONS.md`
- Beta governance packets and handoff/session state.

Forbidden:

- MCP server implementation.
- Provider, adapter, route, receipt, benchmark, web UI, hosted, public-sync, or
  production-readiness changes.

## Write Ownership

This work order owns only per-tool startup config coverage and Beta governance
records.

## Execution Plan

1. Add Gemini project memory file.
2. Add Cursor always-apply project rule.
3. Add Aider config and conventions read file.
4. Run static verification and docs/session gates.
5. Record tool-launch verification boundary.
6. Commit and sync active handoff/session state.

## Evidence Requirements

- Static file existence proof.
- Shared acknowledgment phrase present in all tool configs.
- Governance checks pass.
- Completion packet records unavailable local tool launch proof honestly.

## Acceptance Criteria

- Gemini, Cursor, and Aider each have a committed config path.
- Each config instructs the tool/agent to read session memory and active state.
- Each config records the soft-accountability claim boundary.
- Beta does not claim hard auto-load or MCP behavior.
- Gamma remains blocked until Beta evidence is reviewed by the operator.

## Review Gate

Reject if any file claims guaranteed compliance, universal memory transfer, or
runtime auto-load.

## Closure Checklist

- [x] `GEMINI.md` added.
- [x] Cursor rule added.
- [x] Aider config/conventions added.
- [x] Static verification pass.
- [x] Completion packet filed.
- [x] Session/handoff state updated.
- [ ] Operator/tool launch verification completed.

## Return-To-Orchestrator Conditions

Return if a supported tool needs installation, live account setup, GUI launch, or
API spend to verify behavior.

## Operator Checkpoint

Operator/tool launch verification is expected after Beta config coverage. Do not
proceed to Gamma without operator acceptance or explicit waiver.

## Closure Note

Beta config coverage is complete at the static repository level. Local
tool-launch verification is not complete because Gemini, Cursor, and Aider are
not installed in this shell PATH. This work order therefore closes as
`READY_FOR_OPERATOR_TOOL_VERIFICATION`, not as hard auto-load proof.

## Claim Boundary

This work order may close only as Beta config coverage. It cannot claim hard
auto-load, MCP availability, universal tool compliance, hosted readiness,
production readiness, public release readiness, or freeze release.
