<!-- Memory class: SUMMARY_RECORD -->

# CVF Tool Call Trace Sandbox Source Adoption Matrix - 2026-05-16

Status: ACTIVE SOURCE MATRIX.

## Purpose

Map the OpenAgentd Tool Call Trace / Sandbox source files to the CVF runtime
behavior adopted in this tranche.

## Scope

Owner surface:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`

Implemented contract:

- `src/tool.call.trace.contract.ts`

Focused tests:

- `tests/tool.call.trace.contract.test.ts`

## Source

Source folder:

- `.private_reference/legacy/CVF 16.5/OpenAgentd/`

## Decision

Adopt only the trace, sandbox permission, MCP boundary, and telemetry receipt
subset into the Execution Plane for this tranche.

Other OpenAgentd source files remain deferred to their own owner surfaces so
this tranche does not become an unbounded agent-platform rewrite.

## Adoption Matrix

| Source file | Adopted pattern | CVF owner behavior | Status |
|---|---|---|---|
| `CVF_TOOL_CALL_TRACE_PROTOCOL.md` | lifecycle trace and audit receipt | trace events for call, policy, start, end, error, block, and receipt | adopted |
| `CVF_LOCAL_SANDBOX_PERMISSION_POLICY.md` | deny-by-default and sandbox risk policy | missing policy denies; high-risk and mutating local actions require sandbox | adopted |
| `CVF_MCP_TOOL_BOUNDARY_POLICY.md` | MCP cannot bypass governance | MCP calls are represented as governed tool traces with permission domain and decision | adopted |
| `CVF_LOCAL_TELEMETRY_RECEIPT_SPEC.md` | telemetry-to-receipt shape and redaction | events and receipts include source event ids, risk, decision, latency-ready metadata, and redacted payload summaries | adopted |

## Deferred Source

Deferred OpenAgentd files:

- `CVF_AGENT_MD_CONFIG_INTAKE_SPEC.md`
- `CVF_AGENT_TEAM_MAILBOX_PROTOCOL.md`
- `CVF_LOCAL_AGENT_COCKPIT_ADAPTER.md`
- `CVF_MEMORY_SESSION_NOTES_PROTOCOL.md`
- `CVF_MODEL_FALLBACK_ROUTING_POLICY.md`
- `CVF_SCHEDULED_AGENT_EXECUTION_POLICY.md`

Reason:

- these belong to Agent Boundary, Control Plane, Cockpit, Memory, Gateway, and
  Scheduler tranches, not the first Tool Call Trace / Sandbox runtime slice.

## Evidence

Runtime evidence target:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/tool.call.trace.contract.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/tool.call.trace.contract.test.ts`

## Verification

The source matrix is valid only when:

- each adopted source row maps to an owner behavior;
- deferred files are not silently absorbed;
- focused tests prove adopted runtime behavior.

## Claim Boundary

This matrix does not claim full OpenAgentd adoption. It records the bounded
source subset used for the Tool Call Trace / Sandbox tranche.
