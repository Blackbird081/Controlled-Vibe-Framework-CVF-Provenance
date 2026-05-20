<!-- Memory class: SUMMARY_RECORD -->

# CVF Tool Call Trace Sandbox Test And Proof Plan - 2026-05-16

Status: ACTIVE TEST PLAN.

## Purpose

Define the verification bar for making Tool Call Trace / Sandbox knowledge live
inside CVF.

## Scope

Owner surface:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`

Implemented target:

- `ToolCallTraceContract`

## Source

This plan derives from:

- OpenAgentd Tool Call Trace Protocol;
- OpenAgentd Local Sandbox Permission Policy;
- OpenAgentd MCP Tool Boundary Policy;
- OpenAgentd Local Telemetry Receipt Spec.

## Decision

Use deterministic local tests as the proof bar for this tranche because the
implemented surface is a local contract and does not execute a live provider or
external tool.

Live proof is required only for a future tranche that claims this contract is
wired into live MCP, shell, browser, provider, or scheduler execution.

## Test Plan

Required local tests:

- missing policy fails closed as `deny`;
- explicit deny emits `tool_blocked` and audit receipt;
- `requires_approval` prevents start;
- allow path records call, policy, start, end, and receipt;
- error path records call, policy, start, error, and receipt;
- sensitive argument, result, and error fields are redacted;
- raw secret values are absent from serialized traces;
- high-risk or mutating local actions require sandbox;
- factory and read APIs work.

## Proof Plan

Required proof commands:

```bash
cd EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION
npm run check
npx vitest run tests/tool.call.trace.contract.test.ts --config vitest.config.ts
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

## Live Proof Boundary

This tranche does not require a live provider test because it does not claim
live provider/tool execution enforcement. If a future roadmap claims that live
MCP, shell, browser, provider, or scheduler actions are enforced by this
contract, that roadmap must run live proof through the appropriate provider/tool
path.

## Claim Boundary

Passing this plan proves deterministic local contract behavior. It does not
prove production integration across every execution surface.
