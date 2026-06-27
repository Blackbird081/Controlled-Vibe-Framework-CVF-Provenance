# CVF Work Order — Delta D3 MCP → CLI Bridge

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Date: 2026-05-29

---

## Purpose

Wire MCP `cvf_invoke_cli_stage` tool to `runCli()` — completing the
"MCP controls CLI" architecture from `.private_reference/legacy/CVF 28.05/CLI & MCP.md`:

```
[Orchestrator] ──► MCP: cvf_invoke_cli_stage ──► runCli() ──► Sandboxed Terminal
[Workers]      ──► MCP: cvf_invoke_cli_stage ──► runCli() ──► Sandboxed Terminal
```

**Operator authorized D3 2026-05-29.** Gate requires: D2 CLOSED_PASS **and**
sandbox boundary specification reviewed and approved before any code. This is the
highest-risk tranche — process spawning requires a full isolation design first.

## Authority Chain

- Delta roadmap: `docs/roadmaps/CVF_DELTA_CLI_MCP_WIREIN_ROADMAP_2026-05-29.md`
- Delta GC-018: `docs/baselines/CVF_GC018_DELTA_CLI_MCP_WIREIN_2026-05-29.md`
- MCP SDK `runCli()`: `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/cli.ts` line 290
- MCP SDK export: `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/sdk.ts` line 69
- **D1 gate: D1 CLOSED_PASS required**
- **D2 gate: D2 CLOSED_PASS required**
- **Sandbox boundary spec: must be authored, reviewed, and approved before implementation**

## Agent Roles

Implementer adds `cvf_invoke_cli_stage` tool + sandbox wrapper. Security
Reviewer reviews process isolation, command whitelist, timeout enforcement,
log capture, and cross-invocation state leakage. Auditor confirms D1+D2 gates
and E2E integration test passes. No self-review.

## Scope

**Allowed (after authorization + sandbox spec approval):**

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` (add `cvf_invoke_cli_stage` tool)
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/` sandbox wrapper module (new)
- MCP test files
- Integration test: `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/integration/`
- `docs/reference/CVF_DELTA_D3_SANDBOX_BOUNDARY_SPEC_2026-05-29.md` (sandbox spec — must precede code)
- `docs/reviews/CVF_DELTA_D3_FAST_LANE_AUDIT_2026-05-29.md` (new)
- `docs/reviews/CVF_DELTA_D3_MCP_CLI_BRIDGE_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** Arbitrary shell execution; commands outside whitelist; reading
outside repo sandbox; network egress from sandbox; public-sync.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/cli.ts`
   — confirm `runCli()` at line 290; understand CliResult interface
4. `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/sdk.ts`
   — confirm `runCli` exported at line 69
5. `docs/reviews/CVF_DELTA_D1_PIPELINE_CHAIN_READOUT_COMPLETION_2026-05-29.md`
   — confirm D1 CLOSED_PASS (already verified: CLOSED_PASS_BOUNDED)
6. D2 completion review — confirm D2 CLOSED_PASS (to be created when D2 closes; gate requirement before D3 code)
7. Sandbox boundary spec — confirm spec approved before writing any code (to be authored as D3 Step 1)

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `runCli()` function | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/cli.ts` | line 290 | `runCli` | `cli.ts` | ACCEPT |
| `runCli` SDK export | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/sdk.ts` | line 69 | `runCli` | `sdk.ts` | ACCEPT |
| MCP server tool count (pre-D3) | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | 14 tools (D2 adds 2 = 16) | existing tools | MCP server | ACCEPT |

New tool (process-spawning, highest risk):

| New MCP tool | Process risk | Required constraints |
| --- | --- | --- |
| `cvf_invoke_cli_stage` | Spawns sandboxed process via `runCli()` | Command whitelist; timeout (5 min max); no network egress; log capture mandatory; per-invocation audit entry; no cross-invocation state |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Sandbox boundary spec before code | Execution Plan Step 1 | `CVF_DELTA_D3_SANDBOX_BOUNDARY_SPEC_2026-05-29.md` | present and approved before implementation | OPEN |
| `cvf_invoke_cli_stage` MCP tool | Implementation Design | `index.ts` + sandbox wrapper module | command whitelist enforced; timeout enforced | OPEN |
| Log capture mandatory | Sandbox Boundary Specification | tool output | all stdout/stderr in structured output | OPEN |
| Integration test E2E | Execution Plan Step 4 | `integration/` test | Operator → Closure full flow PASS | OPEN |
| D1 CLOSED_PASS gate | Authority Chain | D1 completion review | Status = CLOSED_PASS_BOUNDED | PASS |
| D2 CLOSED_PASS gate | Authority Chain | D2 completion review | to be confirmed when D2 closes | OPEN |

## Sandbox Boundary Specification (must precede implementation)

The sandbox boundary spec (`docs/reference/CVF_DELTA_D3_SANDBOX_BOUNDARY_SPEC_2026-05-29.md`)
must define and get approval on:

1. **Command whitelist:** exact list of allowed `cvf-cli` subcommands; no
   arbitrary shell; no `rm`, `curl`, `git push`, or network commands
2. **Timeout:** hard kill at 300s (matches `WORKER_TIMEOUT_DEFAULT_MS`)
3. **Working directory:** restricted to repo root only; no `..` path escape
4. **Log capture:** all stdout/stderr captured and returned as structured output;
   no silent discard
5. **Audit entry:** every invocation logged to MCP audit store before execution
6. **State isolation:** each invocation gets fresh environment; no shared
   in-memory state between invocations
7. **Error handling:** timeout triggers `handleWorkerTimeout()`; process failure
   returns structured error, never crashes MCP server

## Pre-Flight

- [x] D1 CLOSED_PASS confirmed — `docs/reviews/CVF_DELTA_D1_PIPELINE_CHAIN_READOUT_COMPLETION_2026-05-29.md`
- [x] `runCli()` confirmed at `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/cli.ts` line 290
- [x] `runCli` SDK export confirmed at `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/sdk.ts` line 69
- [ ] D2 CLOSED_PASS confirmed (gate — must complete before D3 code)
- [ ] Sandbox boundary spec authored and reviewed (`docs/reference/CVF_DELTA_D3_SANDBOX_BOUNDARY_SPEC_2026-05-29.md`)
- [ ] Command whitelist defined and approved

## Write Ownership

Implementer owns all new and modified files. Only files in Allowed list may
be touched. `route.ts` and any non-MCP app files are off-limits.

## Execution Plan

1. Author sandbox boundary spec — get review and approval before proceeding.
2. Read all required first reads; confirm D1 and D2 gates.
3. Implement `cvf_invoke_cli_stage` tool with sandbox wrapper.
4. Write MCP tests and integration test.
5. Run full MCP test suite — all PASS.
6. Run TypeScript check.
7. Run governance gates with `--base 8b1f5992`.
8. Update session continuity: Delta CLOSED_PASS.
9. Commit.
10. Write Fast Lane audit + completion review with Delta wave closure summary.

## Evidence Requirements

- Sandbox boundary spec approved before implementation
- `cvf_invoke_cli_stage` tool enforces command whitelist and timeout
- Integration test PASS: full Operator → Closure flow on one existing workflow
- All MCP tests PASS
- TypeScript PASS
- No arbitrary shell execution via the tool
- Delta wave closure summary in completion review

## Acceptance Criteria

- [ ] D1 AND D2 CLOSED_PASS confirmed
- [ ] Sandbox boundary spec authored, reviewed, and approved
- [ ] `cvf_invoke_cli_stage` tool: command whitelist enforced; timeout enforced; logs captured; audit entry created
- [ ] Integration test PASS: Operator → Intake → Orchestrator → Worker (CLI via MCP) → Reviewer (MCP submit) → Closure on one existing workflow
- [ ] All existing MCP tests still PASS
- [ ] TypeScript PASS
- [ ] No arbitrary shell execution possible via the tool
- [ ] D3 is the final Delta phase; completion review includes full wave closure summary

## Review Gate

D1 + D2 confirmed; sandbox spec approved; command whitelist verified; timeout
enforced; integration test PASS; no arbitrary shell; TypeScript PASS.

## Closure Checklist

- [ ] D1 AND D2 CLOSED_PASS confirmed
- [ ] Sandbox boundary spec approved
- [ ] `cvf_invoke_cli_stage` implemented with all constraints
- [ ] Integration test PASS
- [ ] All tests PASS
- [ ] TypeScript PASS
- [ ] Fast Lane audit PASS
- [ ] Session continuity: Delta CLOSED_PASS
- [ ] Completion review with Delta wave closure summary written

## Return-To-Orchestrator Conditions

Stop if: D1 or D2 not confirmed; sandbox spec not approved; command whitelist
cannot be bounded; process spawning cannot be isolated; integration test fails
with no clear fix path.

## Delta Wave Closure Gate

After D3 committed:
1. `CVF_SESSION/ACTIVE_SESSION_STATE.json`: add `deltaCLIMCPWireIn` CLOSED_PASS;
   update `nextAllowedMove` referencing Delta closure
2. `CVF_SESSION_MEMORY.md`: update mode to `delta_cli_mcp_wirein_closed_pass`
3. Active handoff: add Delta wave closure note

## Operator Checkpoint

Operator authorized D3 2026-05-29. D2 CLOSED_PASS and sandbox boundary spec
approval are still required as sequential gates before implementation begins.
Process spawning is the highest risk in the CVF codebase to date.

## Claim Boundary

D3 produces MCP → CLI bridge with sandboxed execution. It does not claim
arbitrary shell execution safety, multi-user/remote transport security,
production SaaS readiness, hosted readiness, or public release readiness.
The integration test proves one governed workflow flow only — not broad
stability across all workflows.
