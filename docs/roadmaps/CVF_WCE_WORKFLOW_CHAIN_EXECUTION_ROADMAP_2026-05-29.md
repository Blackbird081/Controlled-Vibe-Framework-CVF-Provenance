# CVF WCE Workflow Chain Execution Roadmap

Memory class: SUMMARY_RECORD

Status: ACTIVE

docType: roadmap

Date: 2026-05-29

---

## Authorization / Decision

Authorized by operator direction 2026-05-29. Completes the multi-agent
pipeline harness after Delta CLI/MCP Wire-In. Three gaps remain before CVF
can run O→A→B→R end-to-end via CLI or MCP.

Fresh GC-018:
`docs/baselines/CVF_GC018_WCE_WORKFLOW_CHAIN_EXECUTION_2026-05-29.md`

Dispatch status:
W1 WORK_ORDER_READY (parallel with W3).
W3 WORK_ORDER_READY (parallel with W1).
W2 HOLD_UNTIL_W1_AND_W3_PASS.

## Scope / Target / Owner Boundary

Target: CLI command registry (`CVF_ECO_v2.2_GOVERNANCE_CLI`) and execute
client for W1 + W3. MA1 doc connector + CLI serialization for W2.

Allowed per tranche: see individual work orders.
No new governance semantics. No public-sync repo change.

## Purpose

After Delta D1/D2/D3:
- Pipeline state is visible (D1)
- MCP can submit receipts and advance stages (D2)
- MCP can invoke CLI (D3)

Still missing:
- **W1**: `cvf workflow` command — runs multiple `cvf execute` calls sequentially,
  passing output of agent N as input to agent N+1, with governance receipt per step
- **W2**: MA1 work order as structured JSON — Orchestrator can emit a
  `cvf.internalMultiAgentTransfer.ma1.v1` packet that Worker can parse as input
- **W3**: `--providers` flag on `cvf execute` / `cvf workflow` — maps provider
  per role (e.g. `orchestrator:deepseek,builder:gemini,reviewer:claude`) matching
  the `agentProviders` setting already in the Web UI

## Authority Chain

- WCE GC-018: `docs/baselines/CVF_GC018_WCE_WORKFLOW_CHAIN_EXECUTION_2026-05-29.md`
- CLI command registry: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- CLI execute client: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
- MA1 standard: `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
- Multi-agent types: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/multi-agent.tsx`
- Per-role setting: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Settings.tsx` line 71

## Parallelism

W1 and W3 are fully independent:
- W1 adds a new `workflow` command that loops `executeGovernedTemplateCommand`
- W3 adds a `--providers` flag parsed in `buildExecutePayload`
- Zero shared functions or files

**Both can be dispatched simultaneously.** Recommended: one agent (Claude/me)
takes W1, second agent (Gemini/Codex) takes W3.

W2 requires W1 to exist (transport) and W3 to be aware of (provider slot in
packet). W2 can write doc connector spec in parallel but runtime serialization
implementation waits for W1+W3 CLOSED_PASS.

---

## W1 — `cvf workflow` CLI Command

**Gap:** `cvf execute` does one agent call. No command runs O→A→B→R in
sequence with output chaining.

**Deliverables:**

1. `workflow` command in `command.registry.ts`:
   `cvf workflow --template <key> --input <json> [--role <role>] [--providers <map>] [--endpoint <url>] [--receipt] [--verbose]`
2. `WorkflowChainClient` in `execute.client.ts` (or new `workflow.client.ts`):
   loops over agents in template, calls `executeGovernedTemplateCommand` per
   agent, passes previous output as next input, collects receipts
3. Tests: `workflow.client.test.ts` — mock provider, verify sequential execution
   and receipt chaining
4. Live proof via `cvf workflow --template fullCycle --input '{"goal":"..."}'`

**Contract version:** `cvf.workflowChainExecution.wce.w1.v1`

---

## W2 — MA1 Work Order JSON Serialization

**Gap:** MA1 packet standard exists as doc-only. No CLI/MCP can emit or consume
a `cvf.internalMultiAgentTransfer.ma1.v1` JSON payload.

**Deliverables (Phase A — doc connector, parallel-eligible):**

1. Connector spec mapping MA1 packet fields → CLI `--input` JSON schema

**Deliverables (Phase B — runtime, after W1+W3):**

2. `buildMa1Packet(role, input, priorOutput, receipt)` helper in CLI
3. `cvf workflow` emits MA1 packet at each stage boundary as part of `--receipt` output
4. Tests: packet schema validation

**Contract version:** `cvf.ma1CliSerialization.wce.w2.v1`

Gate: HOLD_UNTIL_W1_AND_W3_PASS for Phase B.

---

## W3 — Per-Role Provider Routing Flag

**Gap:** `cvf execute` has no `--providers` flag. Web UI has `agentProviders`
per-role setting but CLI has only `--provider` (global). Multi-agent workflows
need to assign different providers per role.

**Deliverables:**

1. `--providers` flag on `cvf execute` and `cvf workflow`:
   `--providers orchestrator:deepseek,builder:gemini,reviewer:claude`
2. `parseProviderMap(raw: string): Record<AgentRole, string>` in execute.client.ts
3. `buildExecutePayload` uses per-role provider when `--providers` present
4. Tests: `provider-map.test.ts` — parse + validate provider map
5. Live proof: `cvf execute --template strategy_analysis --role AI_AGENT --providers ai_agent:alibaba`

**Contract version:** `cvf.perRoleProviderRouting.wce.w3.v1`

---

## Non-Goals

- Multi-user isolation or concurrent agent pools
- Automatic retry loops without operator oversight (EL-2/EL-3 enforcement — Delta scope)
- New governance semantics or receipt envelope changes
- Hosted readiness, production readiness, public release readiness
- Any tranche beyond W3 without a fresh roadmap and GC-018

## Work Plan

| Tranche | Deliverable | Gate | Parallel? |
| --- | --- | --- | --- |
| W1 | `cvf workflow` command + chain execution | None | Yes — with W3 |
| W3 | `--providers` flag + per-role routing | None | Yes — with W1 |
| W2 | MA1 serialization (Phase A doc + Phase B runtime) | W1+W3 CLOSED_PASS | No |

## Acceptance Criteria

- [ ] W1: `cvf workflow` runs sequential pipeline; each step has governance receipt; tests PASS; live proof receipt
- [ ] W3: `--providers` flag parsed correctly; per-role provider used in payload; tests PASS; live proof receipt
- [ ] W2: MA1 packet emitted at stage boundaries with correct schema; tests PASS
- [ ] No new governance semantics in any tranche
- [ ] TypeScript PASS across all changes
- [ ] Session continuity updated

## Verification

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 60fc3b32 --head <wce-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base 60fc3b32 --head <wce-commit> --enforce
python governance/compat/check_docs_governance_compat.py --base 60fc3b32 --head <wce-commit> --enforce
```

## Claim Boundary

WCE proves local single-operator pipeline execution. It does not claim
multi-user isolation, production safety, hosted readiness, or that the Web UI
inherits these features automatically. Web UI integration is a separate tranche.
