<!-- Memory class: SUMMARY_RECORD -->

# CVF Tool Call Trace Sandbox Runtime Adoption Closure - 2026-05-16

Status: CLOSED - RUNTIME-OWNED.

## Purpose

Close the Tool Call Trace / Sandbox absorption tranche and record what is now
alive inside CVF.

## Target And Source

Target:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`

Source:

- `.private_reference/legacy/CVF 16.5/OpenAgentd/`

## Scope And Methodology

Method:

- use the OpenAgentd trace, sandbox, MCP boundary, and telemetry receipt docs as
  source patterns;
- implement a CVF-owned deterministic contract;
- test deny-by-default, approval block, allow lifecycle, error lifecycle,
  redaction, receipt, and sandbox classification;
- avoid direct OpenAgentd runtime adoption.

## Findings And Position

Position: Tool Call Trace / Sandbox is now a living CVF runtime primitive.

Delivered:

- `ToolCallTraceContract`;
- policy-bound lifecycle trace;
- default-deny behavior;
- approval-required pre-execution block;
- sandbox-required classification for high-risk and mutating local actions;
- redacted arguments, results, and errors;
- deterministic argument/result/error hashes;
- audit receipts for blocked, successful, and failed traces.

## Risk And Corrective Action

Residual risk:

- existing command runtime and MCP invocation surfaces are not yet rewired to
  consume this contract;
- no live tool/provider path is claimed by this tranche.

Corrective action:

- keep the claim at `runtime-owned`;
- require a future GC-018 for live MCP/local-tool enforcement integration.

## Verification

Executed:

```bash
cd EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION
npm run check
npx vitest run tests/tool.call.trace.contract.test.ts --config vitest.config.ts
```

Result:

- typecheck PASS;
- focused vitest PASS, 1 file / 8 tests.

Additional compatibility fix:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` now stores the checked
  `request.policy` in a local constant so strict TypeScript recognizes the
  post-guard non-null boundary.

## Decision And Recommendation

Decision: close Tool Call Trace / Sandbox as `runtime-owned`.

Recommendation: the next absorption tranche should choose either Agent
Boundary / Delegation or MCP Business Adapter. The trace contract can serve as
their shared audit boundary.

## Claim Boundary

This closure does not claim live provider enforcement, production telemetry
persistence, or complete wiring across every existing CVF execution path.

## Final Clause

The OpenAgentd trace/sandbox knowledge is no longer only reviewed; it is now an
executable CVF Execution Plane contract with tests.
