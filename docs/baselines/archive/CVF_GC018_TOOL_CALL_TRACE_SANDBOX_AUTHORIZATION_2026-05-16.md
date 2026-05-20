<!-- Memory class: SUMMARY_RECORD -->

# CVF GC-018 Tool Call Trace Sandbox Authorization - 2026-05-16

Status: AUTHORIZED FOR LOCAL IMPLEMENTATION.

## Purpose

Authorize a bounded runtime tranche that absorbs the high-fit OpenAgentd tool
trace, sandbox permission, MCP boundary, and telemetry receipt patterns into
CVF without importing OpenAgentd as a runtime.

## Scope

Target owner surface:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`

Source:

- `.private_reference/legacy/CVF 16.5/OpenAgentd/CVF_TOOL_CALL_TRACE_PROTOCOL.md`
- `.private_reference/legacy/CVF 16.5/OpenAgentd/CVF_LOCAL_SANDBOX_PERMISSION_POLICY.md`
- `.private_reference/legacy/CVF 16.5/OpenAgentd/CVF_MCP_TOOL_BOUNDARY_POLICY.md`
- `.private_reference/legacy/CVF 16.5/OpenAgentd/CVF_LOCAL_TELEMETRY_RECEIPT_SPEC.md`

The tranche may implement deterministic local contracts for tool-call lifecycle
trace, deny-by-default policy binding, sandbox-required classification,
redacted argument/result/error metadata, and audit receipt generation.

## Source

Predecessor evidence:

- `docs/baselines/CVF_16_5_LIVING_INTEGRATION_CLASSIFICATION_SUMMARY_2026-05-16.md`
- `docs/reviews/CVF_16_5_EXTERNAL_KNOWLEDGE_INTAKE_REVIEW_CODEX_RESPONSE_TO_CLAUDE_2026-05-16.md`

## Decision

Approved direction: CVF-owned Tool Call Trace / Sandbox contract.

This is an implementation-owner addition inside the Execution Plane, not a
copy of OpenAgentd and not a new external tool runtime.

## Non-Goals

- no direct OpenAgentd dependency;
- no automatic MCP server invocation;
- no shell or filesystem execution implementation;
- no bypass around existing Guard Contract surfaces;
- no live-provider enforcement claim from local unit tests;
- no broad Agent Boundary tranche mixed into this file.

## Evidence

Required evidence before closure:

- source adoption matrix;
- ADR;
- roadmap;
- deterministic unit tests for deny, approval, allow, error, redaction, receipt,
  and sandbox-required behavior;
- package-level typecheck;
- closure note with claim boundary.

## Approval Gate

The operator authorized autonomous continuation of the knowledge absorption
roadmap on 2026-05-16. This file records that authorization for the Tool Call
Trace / Sandbox tranche.
