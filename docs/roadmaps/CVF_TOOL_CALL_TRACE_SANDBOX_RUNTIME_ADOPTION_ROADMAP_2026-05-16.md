<!-- Memory class: SUMMARY_RECORD -->

# CVF Tool Call Trace Sandbox Runtime Adoption Roadmap - 2026-05-16

Status: COMPLETED LOCALLY.

## Authorization

Authorized by:

- `docs/baselines/CVF_GC018_TOOL_CALL_TRACE_SANDBOX_AUTHORIZATION_2026-05-16.md`

## Purpose

Turn the high-fit OpenAgentd tool-call and sandbox governance material into an
owned CVF Execution Plane runtime primitive.

## Scope

Owner surface:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`

Runtime files:

- `src/tool.call.trace.contract.ts`
- `tests/tool.call.trace.contract.test.ts`

## Source

Adopted source subset:

- OpenAgentd Tool Call Trace Protocol;
- OpenAgentd Local Sandbox Permission Policy;
- OpenAgentd MCP Tool Boundary Policy;
- OpenAgentd Local Telemetry Receipt Spec.

## Non-Goals

- no direct OpenAgentd runtime dependency;
- no shell, filesystem, MCP, browser, or scheduler executor;
- no persistent telemetry database;
- no live provider enforcement claim;
- no Agent Boundary / Delegation tranche in this roadmap.

## Work Plan

| Step | Work | Status |
|---|---|---|
| 1 | GC-018 authorization and source classification | complete |
| 2 | ADR and ownership decision | complete |
| 3 | Implement CVF-owned trace/sandbox contract | complete |
| 4 | Add focused vitest coverage | complete |
| 5 | Run typecheck and focused tests | complete |
| 6 | Update living integration summary and handoff | complete |
| 7 | Run governance/pre-push checks before push | pending at closure write time |

## Acceptance Criteria

The tranche is acceptable only if:

- a tool call cannot start without an `allow` policy decision;
- deny and approval-required paths emit blocked receipts;
- success and error paths emit receipts;
- sensitive metadata is redacted before event/receipt storage;
- high-risk and mutating local actions are sandbox-marked;
- TypeScript check passes;
- focused vitest passes;
- claim boundary remains local deterministic contract behavior.

## Verification

Required commands:

```bash
cd EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION
npm run check
npx vitest run tests/tool.call.trace.contract.test.ts --config vitest.config.ts
```

## Claim Boundary

This roadmap closes the first runtime-owned trace/sandbox primitive. It does
not claim that every CVF tool path is already wired through the contract.
