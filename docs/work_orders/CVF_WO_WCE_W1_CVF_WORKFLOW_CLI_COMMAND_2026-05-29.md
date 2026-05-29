# CVF Work Order — WCE-W1 cvf workflow CLI Command

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Date: 2026-05-29

---

## Purpose

Implement `cvf workflow` — a new CLI command that runs a multi-agent pipeline
end-to-end by sequentially calling `executeGovernedTemplateCommand` for each
agent in a template, passing the output of agent N as input to agent N+1,
and collecting governance receipts per step.

Contract version: `cvf.workflowChainExecution.wce.w1.v1`

This closes Gap A: no CLI mechanism exists to run O→A→B→R sequentially.

**Can run in parallel with WCE-W3** — they touch different parts of the CLI.

## Authority Chain

- WCE roadmap: `docs/roadmaps/CVF_WCE_WORKFLOW_CHAIN_EXECUTION_ROADMAP_2026-05-29.md`
- WCE GC-018: `docs/baselines/CVF_GC018_WCE_WORKFLOW_CHAIN_EXECUTION_2026-05-29.md`
- CLI command registry: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
  — `executeGovernedTemplateCommand` import at line 11; `cvf execute` usage at line 130
- CLI execute client: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
  — `ExecuteRequestPayload` at line 16; `buildExecutePayload()` at line 52
- Multi-agent templates: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/multi-agent.tsx`
  — `AgentRole` at line 8; `AGENTS` at line 40; `WORKFLOW_TEMPLATES` at line 113

## Agent Roles

Implementer writes `workflow` command + `WorkflowChainClient`. Reviewer verifies
sequential execution with receipt chaining; confirms no governance bypass;
confirms tests PASS. Auditor confirms live receipt captured. No self-review.

## Scope

**Allowed:**

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts` (add `workflow` command)
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/workflow.client.ts` (new)
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/workflow.client.test.ts` (new)
- `docs/reviews/CVF_WCE_W1_FAST_LANE_AUDIT_2026-05-29.md` (new)
- `docs/reviews/CVF_WCE_W1_CVF_WORKFLOW_CLI_COMMAND_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** `route.ts`, MCP server files, governance contracts, `.tsx` UI files,
receipt envelope schema, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
   — understand `executeGovernedTemplateCommand` call pattern (line 11)
   — understand how `cvf execute` is registered (line 130)
4. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
   — confirm `ExecuteRequestPayload` at line 16
   — confirm `executeGovernedTemplateCommand` signature and return type
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/multi-agent.tsx`
   — confirm `AgentRole` at line 8
   — confirm `WORKFLOW_TEMPLATES` at line 113: `fullCycle`, `designOnly`, `buildReview`, `quickBuild`

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `executeGovernedTemplateCommand` import | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts` | line 11 | `executeGovernedTemplateCommand` | command registry | ACCEPT |
| `cvf execute` usage string | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts` | line 130 | `cvf execute` command | command registry | ACCEPT |
| `ExecuteRequestPayload` interface | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` | line 16 | `ExecuteRequestPayload` | execute client | ACCEPT |
| `buildExecutePayload()` function | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` | line 52 | `buildExecutePayload` | execute client | ACCEPT |
| `requestedRole` field | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` | line 24 | `requestedRole` | `ExecuteRequestPayload` | ACCEPT |
| `AgentRole` type | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/multi-agent.tsx` | line 8 | `AgentRole` | multi-agent module | ACCEPT |
| `WORKFLOW_TEMPLATES` const | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/multi-agent.tsx` | line 113 | `WORKFLOW_TEMPLATES` | multi-agent module | ACCEPT |
| `fullCycle` template key | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/multi-agent.tsx` | WORKFLOW_TEMPLATES.fullCycle | `fullCycle` | WORKFLOW_TEMPLATES | ACCEPT |

New contract fields (doc-only during W1):

| New field | Purpose | Runtime claim blocked? |
| --- | --- | --- |
| `cvf.workflowChainExecution.wce.w1.v1` | Contract version for workflow chain | No — this is a runtime contract |
| `WorkflowChainResult` | Aggregates per-step receipts from multi-agent run | No — runtime struct |
| `WorkflowStepResult` | Receipt + output per agent step | No — runtime struct |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| `cvf workflow` command registered | Scope + implementation | `command.registry.ts` diff | grep `workflow` in registry | OPEN |
| Sequential execution with output chaining | `WorkflowChainClient` | `workflow.client.ts` | Tests verify N→N+1 input | OPEN |
| Governance receipt per step | `WorkflowChainClient` | `WorkflowStepResult.receipt` | Test verifies receipt present | OPEN |
| Tests PASS | Scope | `workflow.client.test.ts` | `npm test` | OPEN |
| Live proof receipt | Evidence | receipt in completion review | receipt ID | OPEN |

## Implementation Design

### `workflow.client.ts`

```typescript
export const WORKFLOW_CHAIN_CONTRACT =
  'cvf.workflowChainExecution.wce.w1.v1' as const;

export interface WorkflowStepResult {
  agentRole: string;
  input: string;
  output: string;
  receipt?: unknown;       // GovernanceEvidenceReceipt when --receipt flag
  success: boolean;
  error?: string;
}

export interface WorkflowChainResult {
  contractVersion: typeof WORKFLOW_CHAIN_CONTRACT;
  templateKey: string;
  steps: WorkflowStepResult[];
  finalOutput: string;
  success: boolean;
}

export async function executeWorkflowChain(
  templateKey: string,
  initialInput: string,
  options: { endpoint: string; role: string; receipt: boolean; verbose: boolean; providers?: Record<string, string> }
): Promise<WorkflowChainResult>
```

### `command.registry.ts` addition

Add `workflow` command that:
1. Parses `--template`, `--input`, `--role`, `--providers`, `--endpoint`, `--receipt`, `--verbose`
2. Calls `executeWorkflowChain()` with parsed args
3. Prints step-by-step output + final summary
4. Exits 0 on success, 1 on any step failure

### Template resolution

Import `WORKFLOW_TEMPLATES` agent list from `multi-agent.tsx` OR duplicate the
agent sequence locally in CLI to avoid cross-package dependency. Duplicating
is safer (CLI must remain standalone). Define `CLI_WORKFLOW_TEMPLATES` mapping
`fullCycle` → `['OPERATOR', 'AI_AGENT', 'AI_AGENT', 'REVIEWER']`.

## Pre-Flight

- [ ] Working tree clean
- [ ] `executeGovernedTemplateCommand` signature confirmed — understand return type
- [ ] CLI package test command confirmed (`npm test` in CLI package)
- [ ] `WORKFLOW_TEMPLATES` keys confirmed: `fullCycle`, `designOnly`, `buildReview`, `quickBuild`

## Write Ownership

Implementer owns all new and modified files. Only files in Allowed list may be
touched.

## Execution Plan

1. Read all required first reads.
2. Confirm `executeGovernedTemplateCommand` return type and call pattern.
3. Create `workflow.client.ts` with `executeWorkflowChain()`.
4. Register `workflow` command in `command.registry.ts`.
5. Write `workflow.client.test.ts` with mock provider — verify sequential execution.
6. Run `npm test` in CLI package — all PASS.
7. Run TypeScript check.
8. Run live proof: `cvf workflow --template fullCycle --input '{"goal":"hello"}' --role OPERATOR`.
9. Run governance gates with `--base 60fc3b32`.
10. Update session continuity.
11. Commit.
12. Write Fast Lane audit + completion review.

## Evidence Requirements

- `cvf workflow` command registered and working
- `WorkflowChainResult` with per-step receipts returned
- `workflow.client.test.ts` all PASS
- TypeScript PASS
- Live proof receipt from at least one template execution
- No MCP server or route.ts change in diff

## Acceptance Criteria

- [ ] `workflow` command registered in `command.registry.ts`
- [ ] `workflow.client.ts` implements sequential execution with output chaining
- [ ] `WorkflowStepResult` contains receipt when `--receipt` flag used
- [ ] Tests PASS
- [ ] TypeScript PASS
- [ ] Live proof receipt captured
- [ ] No governance bypass (each step goes through `executeGovernedTemplateCommand`)
- [ ] Session continuity updated

Fail conditions:
- Steps execute without governance receipt
- Output chaining broken (step N+1 does not receive step N output)
- Tests fail

## Review Gate

Sequential execution verified; receipt per step present; output chaining
confirmed; tests PASS; TypeScript PASS; live receipt present.

## Closure Checklist

- [ ] `workflow` command in registry
- [ ] `workflow.client.ts` with `executeWorkflowChain()`
- [ ] Tests PASS
- [ ] TypeScript PASS
- [ ] Live proof receipt
- [ ] Fast Lane audit PASS
- [ ] Session continuity updated
- [ ] Completion review with W2 gate answer written

## Return-To-Orchestrator Conditions

Stop if: `executeGovernedTemplateCommand` signature incompatible with chaining;
TypeScript errors cannot be resolved in bounded scope; live proof fails with
no clear fix.

## W2 Gate Output

**Expected YES:** W1 workflow chain exists. W2 can now emit MA1 work order
JSON at stage boundaries as part of `--receipt` output. The packet schema
needs W1 transport and W3 provider field to be complete.

## Operator Checkpoint

operator.checkpoint.waiver: Operator authorized WCE directly 2026-05-29.

## Claim Boundary

W1 proves local sequential pipeline execution. It does not claim multi-user
isolation, sandboxed agent pools, production safety, hosted readiness, or
Web UI integration.
