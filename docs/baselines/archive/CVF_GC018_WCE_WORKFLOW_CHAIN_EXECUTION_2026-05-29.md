# CVF GC-018 — WCE Workflow Chain Execution

Memory class: FULL_RECORD

Status: ACTIVE

docType: gc018_baseline

Date: 2026-05-29

---

## Purpose

Authorize WCE Workflow Chain Execution: three tranches completing the
multi-agent pipeline harness so that CVF can run O→A→B→R (Orchestrator →
Architect → Builder → Reviewer) end-to-end through CLI or MCP — not just as a
single-shot `cvf execute` call. Closes the three remaining gaps identified
after Delta CLI/MCP Wire-In analysis.

---

## Scope

- **WCE-W1** — `cvf workflow` CLI command: sequential agent pipeline execution
  (parallel with WCE-W3)
- **WCE-W2** — MA1 work order JSON serialization via CLI/MCP (gated after
  W1+W3 have test evidence)
- **WCE-W3** — Per-role provider routing flag `--providers` (parallel with WCE-W1)

No new governance semantics. No new receipt envelope schema. No public-sync.

---

## Source Verification

| Surface | File | Key symbol | Status |
| --- | --- | --- | --- |
| `ExecuteRequestPayload` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` | line 16 | VERIFIED |
| `buildExecutePayload()` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` | line 52 | VERIFIED |
| `requestedRole` field | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` | line 24 | VERIFIED |
| `executeGovernedTemplateCommand` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts` | line 11 | VERIFIED |
| `cvf execute` usage string | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts` | line 130 | VERIFIED |
| `AGENTS` const | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/multi-agent.tsx` | line 40 | VERIFIED |
| `AgentRole` type | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/multi-agent.tsx` | line 8 | VERIFIED |
| `WORKFLOW_TEMPLATES` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/multi-agent.tsx` | line 113 | VERIFIED |
| `agentProviders` per-role setting | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Settings.tsx` | line 71 | VERIFIED |
| MA1 standard | `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | contract `cvf.internalMultiAgentTransfer.ma1.v1` | VERIFIED |
| `PipelineChainState` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` | line 173 | VERIFIED |

---

## Parallelism Decision

W1 and W3 are independent — W1 touches CLI command registry + execute client,
W3 touches CLI flags + payload. They share no function. Both are code changes
(R1). They can be dispatched simultaneously to two agents.

W2 is gated: MA1 serialization needs W1 to exist (the `cvf workflow` command
is the transport) and W3 to exist (per-role provider is part of the packet).
W2 can begin doc connector work in parallel but runtime serialization waits
for W1+W3 test evidence.

---

## Knowledge Absorption Blind-Spot Control Block

Prior surfaces used (all verified at HEAD `60fc3b32`):
- `multi-agent.tsx` AGENTS/WORKFLOW_TEMPLATES
- CLI execute.client.ts payload structure
- MA1 standard doc

Blind-spot verdict: CLEAR. No new governance semantics required.

---

## Decision / Baseline

WCE is authorized. W1 and W3 may begin implementation immediately in parallel.
W2 dispatch is gated on W1+W3 CLOSED_PASS evidence.

baseHead: `60fc3b32`

---

## Verification

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 60fc3b32 --head <wce-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base 60fc3b32 --head <wce-commit> --enforce
python governance/compat/check_docs_governance_compat.py --base 60fc3b32 --head <wce-commit> --enforce
```

---

## Claim Boundary

WCE does not claim sandboxed multi-agent isolation, production multi-user
safety, hosted readiness, or public release readiness. It proves the local
pipeline chain from CLI/MCP through governance to provider and back, for
single-operator use.
