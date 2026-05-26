# CVF GC-018 MA1 Internal Multi-Agent Work Transfer Packet

Memory class: BASELINE_RECORD

docType: baseline

Date: 2026-05-26

Status: APPROVED

## Purpose

Authorize MA1: a bounded, English-only internal multi-agent work-transfer
packet standard for CVF role orchestration.

## Source / Predecessor Evidence

- `docs/reference/CVF_MULTI_ROLE_ORCHESTRATED_CONVERGENCE_CAPTURE_FORM_2026-05-25.md`
- `docs/concepts/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md`
- `docs/reference/CVF_AGENT_EXECUTION_WORKFLOW_SOP_2026-05-19.md`
- `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md`
- `docs/reference/CVF_AGENT_DELEGATION_AND_SUBAGENT_BOUNDARY_STANDARD_2026-05-19.md`
- Operator instruction on 2026-05-26 to complete a 100% English internal
  multi-agent transfer spec before using it to test the Surface 1 fix tranche.

## Decision / Baseline / Proposed Tranche

Baseline: CVF has multi-role convergence forms and role/delegation standards,
but it lacks one copy-ready transfer packet for orchestrator-to-role handoff.

Proposed tranche: create the MA1 standard as an English-only control packet,
then use it immediately as the control artifact for the Surface 1 i18n/export
fix.

## Scope / Target / Owner Boundary

Allowed changes:

- MA1 roadmap, GC-018, work order, reference standard, completion review;
- active session memory/handoff/state updates.

Blocked changes:

- runtime subagent scheduler;
- provider/model routing;
- MCP server behavior;
- `/api/execute` behavior;
- receipt envelopes;
- public-sync claims.

## Surface Fidelity Control Block

| Control | Result |
| --- | --- |
| Surface verified | Internal CVF agent-to-agent work transfer |
| Wrong-target guard | Packet must identify target surface before role work begins |
| Audience verified | CVF-aware agents, reviewers, auditors, integrators |
| Language invariant | 100% English packet chrome |
| Operator role | Product authority; not an internal audit worker |

## Knowledge Absorption Blind-Spot Control Block

This tranche normalizes existing CVF internal governance knowledge rather than
absorbing new external material.

| Control | Result |
| --- | --- |
| Prior evidence resolved | Existing convergence, role matrix, SOP, and authority/surface fidelity docs read |
| Detailed source files read | Multi-role convergence form, authority/surface fidelity concept, active session state |
| Accept/defer/reject dispositions | Accept transfer-packet standard; defer runtime scheduling and live subagent isolation |
| Adversarial role review | Auditor role must reject claims of runtime enforcement or public readiness |
| Blind-spot delta | Low; remaining gap is future runtime implementation, out of MA1 scope |

## Required Proof

- File existence check for MA1 artifacts.
- Markdown structural review against required sections.
- `python governance/compat/check_active_session_state.py` after commit/sync.

## Claim Boundary

MA1 is a documentation/control standard only. It does not claim live multi-agent
runtime, hard provider isolation, MCP enforcement, hosted readiness, production
readiness, or freeze release.

## Evidence / Verification

Required verification is local and deterministic. No live provider/API call is
required.
