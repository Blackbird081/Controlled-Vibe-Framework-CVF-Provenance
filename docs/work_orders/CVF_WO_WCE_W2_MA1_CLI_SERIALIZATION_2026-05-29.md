# CVF Work Order — WCE-W2 MA1 CLI Serialization

Memory class: FULL_RECORD

Status: HOLD_UNTIL_W1_AND_W3_PASS

docType: work_order

Date: 2026-05-29

---

## Purpose

Implement MA1 work order JSON serialization in the CLI: `cvf workflow` emits
a `cvf.internalMultiAgentTransfer.ma1.v1` packet at each stage boundary as
structured JSON, so Orchestrator output is consumable by Worker as a typed
input rather than raw text.

Contract version: `cvf.ma1CliSerialization.wce.w2.v1`

This closes Gap B: MA1 standard exists as doc-only; CLI cannot emit or parse
MA1 packets.

**Phase A** (doc connector spec) can run in parallel with W1+W3.
**Phase B** (runtime serialization) waits for W1+W3 CLOSED_PASS.

## Authority Chain

- WCE roadmap: `docs/roadmaps/CVF_WCE_WORKFLOW_CHAIN_EXECUTION_ROADMAP_2026-05-29.md`
- WCE GC-018: `docs/baselines/CVF_GC018_WCE_WORKFLOW_CHAIN_EXECUTION_2026-05-29.md`
- MA1 standard: `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
  — contract version `cvf.internalMultiAgentTransfer.ma1.v1`
- W1 transport: `docs/reviews/CVF_WCE_W1_CVF_WORKFLOW_CLI_COMMAND_COMPLETION_2026-05-29.md`
  — must be CLOSED_PASS
- W3 provider field: `docs/reviews/CVF_WCE_W3_PER_ROLE_PROVIDER_ROUTING_COMPLETION_2026-05-29.md`
  — must be CLOSED_PASS
- CLI execute client: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`

## Agent Roles

Implementer writes Phase A doc connector spec + Phase B `buildMa1Packet()`
helper and `cvf workflow` integration. Reviewer confirms MA1 fields match
standard verbatim; confirms no phantom fields. Auditor confirms W1+W3 gates
satisfied before Phase B.

## Scope

**Allowed (Phase A — can begin now):**

- `docs/reference/CVF_WCE_W2_MA1_CLI_SERIALIZATION_CONNECTOR_SPEC_2026-05-29.md` (new)
- `docs/reviews/CVF_WCE_W2_FAST_LANE_AUDIT_2026-05-29.md` (new)

**Allowed (Phase B — after W1+W3 CLOSED_PASS):**

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/ma1-packet.ts` (new)
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/ma1-packet.test.ts` (new)
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/workflow.client.ts` (update to emit MA1)
- `docs/reviews/CVF_WCE_W2_MA1_CLI_SERIALIZATION_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** `route.ts`, MCP server, UI files, receipt envelope schema, public-sync.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
   — confirm required packet structure: Contract version, Date, Topic, Surface Fidelity Gate,
     Authority Chain, Source Packet, Role Assignment, Execution Instructions, Role Output Schema,
     Dissent Ledger, Integration Decision, Completion Evidence, Claim Boundary
4. `docs/reviews/CVF_WCE_W1_CVF_WORKFLOW_CLI_COMMAND_COMPLETION_2026-05-29.md`
   — confirm W1 CLOSED_PASS (Phase B only)
5. `docs/reviews/CVF_WCE_W3_PER_ROLE_PROVIDER_ROUTING_COMPLETION_2026-05-29.md`
   — confirm W3 CLOSED_PASS (Phase B only)

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| MA1 contract version | `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | Contract version field | `cvf.internalMultiAgentTransfer.ma1.v1` | MA1 standard | ACCEPT |
| MA1 required sections | `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | Required Packet Structure | 13 named sections | MA1 standard | ACCEPT |
| `ExecuteRequestPayload` interface | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` | line 16 | `ExecuteRequestPayload` | execute client | ACCEPT |

New contract fields:

| New symbol | Purpose | Runtime claim blocked? |
| --- | --- | --- |
| `buildMa1Packet()` | Builds MA1-conformant JSON from workflow step data | No — runtime function |
| `Ma1CliPacket` | TypeScript type for CLI-side MA1 packet | No — runtime type |
| `cvf.ma1CliSerialization.wce.w2.v1` | Contract version for CLI MA1 serialization | No — runtime contract |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Phase A: MA1 → CLI schema connector spec | Scope Phase A | `CVF_WCE_W2_MA1_CLI_SERIALIZATION_CONNECTOR_SPEC` | Doc review | OPEN |
| Phase B: `buildMa1Packet()` in CLI | Scope Phase B | `ma1-packet.ts` | Unit tests | OPEN |
| Phase B: `cvf workflow` emits MA1 at stage boundaries | workflow.client.ts update | MA1 JSON in step output | Integration test | OPEN |
| W1+W3 gates confirmed (Phase B) | Authority Chain | completion reviews | Both CLOSED_PASS | OPEN |

## Implementation Design — Phase B

### `ma1-packet.ts`

```typescript
export const MA1_CLI_CONTRACT =
  'cvf.ma1CliSerialization.wce.w2.v1' as const;

export interface Ma1CliPacket {
  contractVersion: typeof MA1_CLI_CONTRACT;
  ma1ContractVersion: 'cvf.internalMultiAgentTransfer.ma1.v1';
  topic: string;
  date: string;
  sourceRole: string;
  targetRole: string;
  sourceOutput: string;          // previous agent's output
  providerForNextRole?: string;  // from W3 per-role map
  governanceReceiptRef?: string; // receipt ID from previous step
  executionInstructions: string; // plain-language task for next agent
  claimBoundary: string;
}

export function buildMa1Packet(
  step: WorkflowStepResult,
  nextRole: string,
  executionInstructions: string,
  providerMap?: Record<string, string>,
): Ma1CliPacket
```

### `workflow.client.ts` update

When `--receipt` flag is present, after each step emit a `Ma1CliPacket` as
part of `WorkflowStepResult.ma1Packet`. This becomes the structured input for
the next agent's `intent` field.

## Pre-Flight

- [ ] W1 CLOSED_PASS confirmed (Phase B only)
- [ ] W3 CLOSED_PASS confirmed (Phase B only)
- [ ] MA1 standard 13 sections confirmed
- [ ] MA1 contract version confirmed: `cvf.internalMultiAgentTransfer.ma1.v1`

## Write Ownership

Phase A: implementer owns new connector spec doc.
Phase B: implementer owns `ma1-packet.ts`, test file, and `workflow.client.ts` update.

## Execution Plan

**Phase A (now):**
1. Read MA1 standard.
2. Write connector spec mapping MA1 fields → CLI JSON schema.
3. Write Fast Lane audit.

**Phase B (after W1+W3):**
4. Confirm W1+W3 CLOSED_PASS.
5. Implement `buildMa1Packet()` in `ma1-packet.ts`.
6. Update `workflow.client.ts` to emit MA1 packet when `--receipt` flag.
7. Write `ma1-packet.test.ts`.
8. Run `npm test` — all PASS.
9. Run TypeScript check.
10. Run governance gates.
11. Update session continuity; mark WCE CLOSED_PASS.
12. Commit.
13. Write completion review with WCE wave closure summary.

## Evidence Requirements

- Phase A: connector spec covering all 13 MA1 sections → CLI field mapping
- Phase B: `buildMa1Packet()` tested; MA1 packet emitted in workflow step output; TypeScript PASS

## Acceptance Criteria

- [ ] Phase A: connector spec with all 13 MA1 sections individually mapped
- [ ] Phase B (requires W1+W3 first):
  - [ ] `buildMa1Packet()` implemented
  - [ ] `ma1-packet.test.ts` PASS
  - [ ] `cvf workflow --receipt` emits MA1 packets at stage boundaries
  - [ ] TypeScript PASS
  - [ ] Session continuity: WCE CLOSED_PASS

Fail conditions:
- W1 or W3 gate not confirmed before Phase B
- MA1 packet missing required sections
- Tests fail

## Review Gate

W1+W3 confirmed; all 13 MA1 sections present in packet; tests PASS; TypeScript PASS.

## Closure Checklist

- [ ] W1 AND W3 CLOSED_PASS confirmed
- [ ] Phase A connector spec complete
- [ ] `ma1-packet.ts` with `buildMa1Packet()`
- [ ] `ma1-packet.test.ts` PASS
- [ ] `workflow.client.ts` emits MA1 packets
- [ ] TypeScript PASS
- [ ] Session continuity: WCE CLOSED_PASS
- [ ] Completion review with WCE wave closure summary written

## Return-To-Orchestrator Conditions

Stop if: W1 or W3 gate missing; MA1 sections cannot be mapped to CLI types;
tests fail with no clear fix.

## WCE Wave Closure Gate

After W2 committed:
1. `CVF_SESSION/ACTIVE_SESSION_STATE.json`: add `wceWorkflowChainExecution` CLOSED_PASS
2. `CVF_SESSION_MEMORY.md`: update Next Allowed Move with WCE closure
3. Active handoff: add WCE wave closure note

## Operator Checkpoint

Phase A: operator authorized WCE 2026-05-29.
Phase B: HOLD_UNTIL_W1_AND_W3_PASS.

## Claim Boundary

W2 proves MA1 packet serialization in CLI workflow chain. It does not claim
full MA1 runtime enforcement, multi-agent isolation, hosted readiness, or
production readiness.
