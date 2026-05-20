<!-- Memory class: SUMMARY_RECORD -->

# CVF ADR Tool Call Trace Sandbox Runtime Ownership - 2026-05-16

Status: ACCEPTED.

## Purpose

Record the ownership decision for adopting OpenAgentd tool-call governance
knowledge into CVF as executable runtime contract behavior.

## Scope

This ADR covers the first bounded Tool Call Trace / Sandbox tranche inside:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`

It does not cover Agent Boundary / Delegation, cockpit UI, scheduler execution,
or persistent telemetry stores.

## Context

OpenAgentd contains useful doctrine for local agents:

- local execution is not automatically trusted;
- default permission is deny;
- MCP is a tool boundary, not a governance bypass;
- tool calls need lifecycle trace and audit receipt;
- sensitive arguments and telemetry metadata must be redacted.

CVF already has Execution Plane contracts for policy gates, MCP invocation,
command runtime, and audit summaries. The missing high-fit runtime primitive is
a small contract that binds one tool call to policy decision, sandbox posture,
redacted telemetry, and receipt.

## Decision

Implement a CVF-owned `ToolCallTraceContract` in the Execution Plane.

The contract owns:

- `tool_call`, `policy_check`, `tool_start`, `tool_end`, `tool_error`,
  `tool_blocked`, and `audit_receipt` events;
- deny-by-default behavior when no explicit policy is supplied;
- approval-required behavior that prevents execution until a later approved
  contract exists;
- sandbox-required classification for high-risk, shell, filesystem mutation, and
  mutating MCP actions;
- deterministic hashes for raw arguments, result, and error payloads;
- recursive redaction of sensitive argument/result/error fields before storage;
- receipt generation for blocked, successful, and failed traces.

## Alternatives

Alternative 1: keep OpenAgentd documents as reference only.

Rejected because the operator asked for absorbed knowledge to be alive inside
CVF, and docs-only intake would be easy for future agents to forget.

Alternative 2: copy OpenAgentd protocols directly into CVF.

Rejected because CVF needs owner-native types, deterministic tests, and claim
boundaries rather than a mirrored external document set.

Alternative 3: wire a live MCP or shell executor immediately.

Rejected because this tranche is the boundary contract. Live tool execution
requires a separate GC-018 with provider/tool-specific safety proof.

## Consequences

Positive:

- tool calls can no longer be represented as opaque runtime side effects in the
  Execution Plane contract layer;
- MCP/local-tool governance now has a reusable receipt-producing primitive;
- future Agent Boundary and MCP Business Adapter tranches can consume the same
  trace contract.

Costs:

- this is a local deterministic contract, not a production telemetry store;
- existing command and MCP invocation contracts are not yet rewired to call it.

## Verification

Verification must include:

- package typecheck for Execution Plane;
- focused vitest coverage for the trace contract;
- governance markdown and file-size checks before commit;
- no live-provider claim unless a future tranche wires this contract into live
  governed execution.

## Claim Boundary

This ADR claims runtime ownership of the trace/sandbox primitive only. It does
not claim production live enforcement across every CVF tool path.
