<!-- Memory class: SUMMARY_RECORD -->

# CVF MCP Business Adapter Runtime Adoption Roadmap - 2026-05-16

Status: COMPLETED LOCALLY.

## Authorization

Authorized by:

- `docs/baselines/CVF_GC018_MCP_BUSINESS_ADAPTER_AUTHORIZATION_2026-05-16.md`

## Purpose

Turn the high-fit generic MCP business-tool adapter material into an owned CVF
Execution Plane runtime primitive.

## Scope

Owner surface:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`

Runtime files:

- `src/mcp.business.adapter.contract.ts`
- `tests/mcp.business.adapter.contract.test.ts`

## Source

Adopted source subset:

- MCP business tool contract;
- tool registry;
- risk classifier;
- approval gate;
- execution receipt;
- transport policy;
- tool adapter.

## Non-Goals

- no Pancake POS profile adoption;
- no live MCP server call;
- no API key or endpoint handling;
- no business mutation claim.

## Work Plan

| Step | Work | Status |
|---|---|---|
| 1 | GC-018 authorization and source classification | complete |
| 2 | ADR and owner decision | complete |
| 3 | Implement generic MCP Business Adapter contract | complete |
| 4 | Add focused vitest coverage | complete |
| 5 | Run typecheck and focused tests | complete |
| 6 | Update living integration summary and handoff | complete |
| 7 | Run governance/pre-push checks before push | pending at closure write time |

## Acceptance Criteria

The tranche is acceptable only if:

- tools must be registered before execution;
- risk classification handles read, write, destructive, and system config cases;
- high-risk/destructive/system actions require approval;
- transport is checked as a policy boundary;
- rejected attempts still create receipts;
- successful attempts create deterministic receipts;
- Pancake profile remains deferred.

## Verification

Required commands:

```bash
cd EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION
npm run check
npx vitest run tests/mcp.business.adapter.contract.test.ts --config vitest.config.ts
```

## Claim Boundary

This roadmap closes the first runtime-owned generic MCP Business Adapter
primitive. It does not claim live external MCP execution.
