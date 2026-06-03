# CVF GC-018 LHW6 Workflow Connector Wave 6

Memory class: SUMMARY_RECORD

Status: ACCEPTED

docType: baseline

Date: 2026-05-28

---

## Purpose

Authorize LHW6 as a bounded documentation-only continuation of the legacy
workflow connector absorption series.

## Scope

LHW6 may create connector specs, work-order updates, completion reviews, and
session-continuity updates for:

- T1 Tool Runtime Bridge Advisory Connector
- T2 CLI Tool Onboarding Governance Connector
- T3 Project Memory Readout Connector

No runtime source, provider route, receipt envelope, memory reinjection path,
CLI execution path, MCP client, public-sync file, hosted-readiness claim, or
production-readiness claim is authorized by this baseline.

## Source / Predecessor Evidence

| Source | Relevance |
|---|---|
| `docs/roadmaps/CVF_LHW6_WORKFLOW_CONNECTOR_WAVE6_ROADMAP_2026-05-28.md` | Roadmap authority |
| `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` | Legacy trigger authority |
| `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md` | W3 tool action taxonomy closure |
| `docs/reviews/archive/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md` | TA1 approval readout closure |
| `docs/reviews/archive/CVF_LHW4_T2_EXECUTION_AUTHORITY_CHAIN_READOUT_CONNECTOR_COMPLETION_2026-05-27.md` | Authority-chain connector closure |
| `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md` | Durable memory closure |
| `docs/reviews/archive/CVF_WR1_WORKFLOW_RECOVERY_STATE_PROOF_COMPLETION_2026-05-25.md` | Workflow recovery closure |
| `docs/reviews/CVF_AIF_C_MEMORY_GATEWAY_PHASE2_COMPLETION_2026-05-24.md` | Memory gateway closure |
| `docs/reviews/archive/CVF_LHW4_T1_MEMORY_SNAPSHOT_GOVERNANCE_CONNECTOR_COMPLETION_2026-05-27.md` | Memory snapshot connector closure |

## Decision / Baseline

LHW6 is accepted as a three-step documentation connector wave.

Execution order is sequential:

1. T1 may dispatch after this GC-018 and dispatch-quality gate pass.
2. T2 remains HOLD until T1 is `CLOSED_PASS`.
3. T3 remains HOLD until T1 and T2 are `CLOSED_PASS`.

## Required Evidence

- Each work order must include a Source Verification Block.
- Each roadmap-derived work order must include a Roadmap-to-Work-Order Trace
  Matrix before ready/dispatch.
- Source Verification `ACCEPT` rows must cite existing source files or
  canonical contracts.
- T2/T3 must not be marked ready/dispatch until prerequisite completion
  evidence exists.
- `governance/compat/check_work_order_dispatch_quality.py --enforce` must pass
  before any work order is treated as ready.

## Verification

Expected pre-dispatch verification:

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base HEAD --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce
python governance/compat/check_docs_governance_compat.py --base HEAD --head HEAD --enforce
```

## Claim Boundary

This GC-018 authorizes documentation-only connector normalization. It does not
authorize runtime tool execution, CLI invocation, MCP bridging, memory
reinjection, raw memory release, receipt-envelope extension, provider behavior,
public-sync work, hosted readiness, production readiness, or public release
readiness.
