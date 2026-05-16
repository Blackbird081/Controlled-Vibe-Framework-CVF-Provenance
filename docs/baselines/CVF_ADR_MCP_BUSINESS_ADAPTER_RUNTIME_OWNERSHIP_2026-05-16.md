<!-- Memory class: SUMMARY_RECORD -->

# CVF ADR MCP Business Adapter Runtime Ownership - 2026-05-16

Status: ACCEPTED.

## Purpose

Record the ownership decision for adopting generic MCP business-tool adapter
knowledge into CVF as executable Execution Plane behavior.

## Scope

This ADR covers the first bounded MCP Business Adapter tranche inside:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`

## Context

`pancake-pos-mcp` demonstrates a real business MCP surface with read, write,
destructive, and system configuration actions across orders, inventory,
employees, webhooks, promotions, and related domains.

CVF should learn the adapter governance shape, not copy a business integration
into core runtime.

## Decision

Implement a CVF-owned `MCPBusinessAdapterContract` in the Execution Plane.

The contract owns:

- business tool contract registration;
- risk classification;
- approval gate;
- transport policy;
- execution receipt;
- governed adapter result.

## Alternatives

Alternative 1: copy all eight proposed source files and the Pancake profile.

Rejected because this tranche needs a compact owner-native primitive, and the
Pancake profile is domain-specific.

Alternative 2: wire a live external MCP call immediately.

Rejected because live tool execution requires secrets, transport setup, and a
fresh live-proof roadmap.

Alternative 3: keep the material as docs-only.

Rejected because the operator requires absorbed knowledge to become alive inside
CVF.

## Consequences

Positive:

- business MCP tools can be represented as governed contracts before invocation;
- dangerous business mutations are stopped before execution;
- transport becomes a policy boundary;
- every attempt can produce an audit receipt, including rejected attempts.

Costs:

- this is a deterministic local contract, not a live MCP client;
- domain profiles still need future owner approval before adoption.

## Verification

Verification must include:

- Execution Plane package typecheck;
- focused vitest coverage for the MCP Business Adapter contract;
- governance markdown and file-size checks before commit;
- full pre-push chain before provenance push.

## Claim Boundary

This ADR claims runtime ownership of the generic MCP business adapter primitive
only. It does not claim live Pancake POS or external MCP enforcement.
