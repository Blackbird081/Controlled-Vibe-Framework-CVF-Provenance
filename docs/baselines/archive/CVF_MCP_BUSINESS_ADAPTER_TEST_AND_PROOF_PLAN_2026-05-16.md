<!-- Memory class: SUMMARY_RECORD -->

# CVF MCP Business Adapter Test And Proof Plan - 2026-05-16

Status: ACTIVE TEST PLAN.

## Purpose

Define the verification bar for making MCP Business Adapter knowledge live
inside CVF.

## Scope

Owner surface:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`

Implemented target:

- `MCPBusinessAdapterContract`

## Source

This plan derives from the generic MCP business adapter files in
`pancake-pos-mcp`.

## Decision

Use deterministic local tests because the implemented surface is an adapter
boundary contract and does not call a live MCP server.

Live proof is required only for a future tranche that claims live MCP execution.

## Test Plan

Required local tests:

- registry stores and lists tool contracts;
- destructive mutation overrides lower default risk;
- unregistered tool is denied with receipt;
- read-only tool is allowed through allowed transport;
- high-risk write requires approval;
- approved high-risk write is allowed with receipt;
- destructive action requires explicit reason;
- disallowed transport rejects execution;
- receipts are deterministic;
- factory works.

## Proof Plan

Required proof commands:

```bash
cd EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION
npm run check
npx vitest run tests/mcp.business.adapter.contract.test.ts --config vitest.config.ts
```

Repository-level proof before push:

```bash
python governance/compat/run_local_governance_hook_chain.py --hook pre-push
```

## Evidence

Expected evidence:

- typecheck pass;
- focused vitest pass;
- governance markdown/file-size checks pass;
- full pre-push chain pass before provenance push.

## Claim Boundary

Passing this plan proves deterministic local adapter behavior. It does not prove
live external MCP execution.
