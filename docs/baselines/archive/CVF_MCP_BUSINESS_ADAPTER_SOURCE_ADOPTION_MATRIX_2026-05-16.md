<!-- Memory class: SUMMARY_RECORD -->

# CVF MCP Business Adapter Source Adoption Matrix - 2026-05-16

Status: ACTIVE SOURCE MATRIX.

## Purpose

Map the `pancake-pos-mcp` source files to the CVF runtime behavior adopted in
this tranche.

## Scope

Owner surface:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`

Implemented contract:

- `src/mcp.business.adapter.contract.ts`

Focused tests:

- `tests/mcp.business.adapter.contract.test.ts`

## Source

Source folder:

- `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/`

## Decision

Adopt the generic MCP business adapter pattern. Defer the Pancake POS profile as
domain-specific configuration.

## Adoption Matrix

| Source file | Adopted pattern | CVF owner behavior | Status |
|---|---|---|---|
| `mcp-business-tool-contract.ts` | contract before invocation | `MCPBusinessToolContract` | adopted |
| `mcp-business-tool-registry.ts` | registered tools only | in-memory deterministic registry methods | adopted |
| `mcp-business-risk-classifier.ts` | read/write/destructive/system risk | `classifyRisk()` and mutation override rules | adopted |
| `mcp-business-approval-gate.ts` | dangerous action gating | approval decisions for read, write, destructive, and system config actions | adopted |
| `mcp-business-transport-policy.ts` | transport as risk boundary | transport allowlist decision | adopted |
| `mcp-business-execution-receipt.ts` | audit receipt after attempt | receipt for success and rejection | adopted |
| `mcp-business-tool-adapter.ts` | governed adapter result | `execute()` combines contract, risk, approval, transport, receipt, output | adopted |
| `pancake-pos-mcp.profile.ts` | domain-specific profile | deferred; requires future profile GC-018 | deferred |

## Evidence

Runtime evidence target:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mcp.business.adapter.contract.test.ts`

## Verification

The matrix is valid only when:

- each adopted generic source maps to tested owner behavior;
- Pancake profile remains deferred;
- no source file is silently copied as runtime authority.

## Claim Boundary

This matrix records a generic adapter adoption. It does not claim Pancake POS MCP
runtime integration.
