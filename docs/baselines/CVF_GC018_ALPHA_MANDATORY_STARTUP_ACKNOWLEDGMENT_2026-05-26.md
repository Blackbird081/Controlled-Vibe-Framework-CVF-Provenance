# CVF GC-018 Alpha Mandatory Startup Acknowledgment

Memory class: BASELINE_RECORD

docType: baseline

Date: 2026-05-26

Status: APPROVED

## Purpose

Authorize the bounded Option Alpha implementation from the cross-agent memory
assessment.

## Source / Predecessor Evidence

- `docs/concepts/CVF_CROSS_AGENT_MEMORY_AND_AUTO_LOAD_ASSESSMENT_2026-05-26.md`
- `docs/concepts/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md`
- `CVF_SESSION_MEMORY.md`
- `AGENTS.md`
- `CLAUDE.md`

## Decision / Baseline / Proposed Tranche

Baseline: CVF already has a repo-governed cross-agent memory front door, but
loading remains instruction-driven. The recent Claude-private memory mismatch
showed that visible startup accountability is useful.

Proposed tranche: add mandatory startup acknowledgment instructions to the two
existing front-door files only.

## Scope / Target / Owner Boundary

Allowed changes:

- `AGENTS.md`
- `CLAUDE.md`
- Alpha roadmap, baseline, work order, completion, and session/handoff state.

Blocked changes:

- runtime memory injection;
- MCP server;
- new tool-specific config files;
- provider, route, receipt, or UI behavior.

## Knowledge Absorption Blind-Spot Control Block

This tranche uses the cross-agent memory assessment as the source packet and
does not absorb new external knowledge.

| Control | Result |
| --- | --- |
| Prior absorption evidence resolved | yes; assessment packet is direct predecessor |
| Detailed source files read | `AGENTS.md`, `CLAUDE.md`, active state, assessment packet |
| Accept/defer/reject dispositions | accept Alpha, defer Beta/Gamma, reject runtime auto-inject claim |
| Adversarial role review | avoid claiming true auto-load or hard enforcement |
| Blind-spot delta | low; remaining weakness is agent honesty/compliance |

## Evidence / Verification

Required verification:

- docs governance compatibility;
- markdown structural completeness;
- active session state compatibility;
- whitespace diff check.

## Claim Boundary

Approved claim is bounded to startup instruction hardening for current
front-door files. It is not a runtime feature and not a substitute for a future
cvf-mcp-server.
