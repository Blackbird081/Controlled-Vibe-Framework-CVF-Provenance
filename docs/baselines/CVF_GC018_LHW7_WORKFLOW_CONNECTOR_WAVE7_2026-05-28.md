# CVF GC-018 LHW7 Workflow Connector Wave 7

Memory class: SUMMARY_RECORD

Status: ACCEPTED

docType: baseline

Date: 2026-05-28

---

## Purpose

Authorize LHW7 as a bounded documentation-only continuation of the legacy
workflow connector absorption series, targeting flows where every cited runtime
surface is already CLOSED_PASS_BOUNDED but no connector standard ties them
together.

## Scope

LHW7 may create connector specs, work-order updates, Fast Lane audits,
completion reviews, and session-continuity updates for:

- T1 Workflow Recovery → Tool Bridge Re-Entry Connector
- T2 Project Memory Readout → Context Budget Handoff Connector
- T3 Failure Simulation → Spec-Change Re-Intake Connector

No runtime source, provider route, receipt envelope, memory reinjection path,
CLI execution path, MCP client, public-sync file, hosted-readiness claim, or
production-readiness claim is authorized by this baseline.

## Source / Predecessor Evidence

| Source | Relevance |
|---|---|
| `docs/roadmaps/CVF_LHW7_WORKFLOW_CONNECTOR_WAVE7_ROADMAP_2026-05-28.md` | Roadmap authority |
| `docs/roadmaps/CVF_LHW6_WORKFLOW_CONNECTOR_WAVE6_ROADMAP_2026-05-28.md` | Predecessor wave (CLOSED_PASS_BOUNDED) |
| `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` | Legacy trigger authority |
| `docs/reviews/CVF_WR1_WORKFLOW_RECOVERY_STATE_PROOF_COMPLETION_2026-05-25.md` | WR1 recovery readout closure (T1) |
| `docs/reviews/CVF_LHW6_T1_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_COMPLETION_2026-05-28.md` | Tool bridge advisory connector closure (T1) |
| `docs/reviews/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md` | TA1 approval readout closure (T1) |
| `docs/reviews/CVF_LHW6_T3_PROJECT_MEMORY_READOUT_CONNECTOR_COMPLETION_2026-05-28.md` | Project memory readout connector closure (T2) |
| `docs/reviews/CVF_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT_COMPLETION_2026-05-25.md` | Context budget readout closure (T2) |
| `docs/reviews/CVF_VI2_ROUTE_REQUEST_CONTEXT_PROFILE_READOUT_COMPLETION_2026-05-25.md` | Route request context readout closure (T2) |
| LHW5-T3 failure simulation scenario packet completion review | Failure simulation closure (T3) |
| LHW3 spec-change packet completion review | Spec-change packet closure (T3) |
| LHW3 clarification re-intake packet completion review | Re-intake packet closure (T3) |

## Decision / Baseline

LHW7 is accepted as a three-step documentation connector wave.

Execution order is sequential:

1. T1 may dispatch after this GC-018 and dispatch-quality gate pass.
2. T2 remains HOLD until T1 is `CLOSED_PASS`.
3. T3 remains HOLD until T1 and T2 are `CLOSED_PASS`.

## Required Evidence

- Each work order must include a Source Verification Block with verified
  file/line citations for every cited runtime field.
- Each roadmap-derived work order must include a Roadmap-to-Work-Order Trace
  Matrix before ready/dispatch.
- Source Verification `ACCEPT` rows must cite existing source files or
  canonical contracts (no "confirm later" placeholders).
- T2 must not be marked ready/dispatch until T1 completion evidence exists.
- T3 must not be marked ready/dispatch until T1 and T2 completion evidence
  exists.
- `governance/compat/check_work_order_dispatch_quality.py --enforce` must pass
  before any work order is treated as ready.
- Work Order Closure Quality Gate must pass before any
  `CLOSED_PASS_BOUNDED` transition.

## Verification

Expected pre-dispatch verification per work order:

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base HEAD --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce
python governance/compat/check_docs_governance_compat.py --base HEAD --head HEAD --enforce
```

Expected closure verification per completion review:

- Roadmap acceptance criteria checkbox flipped to `[x]` only after artifacts
  exist on disk.
- Closure diff matches Source Verification Table claims.
- Session continuity updated in the same batch as the completion review.

## Boundary Surfaces Explicitly Locked

The following invariants remain in force across LHW7 and cannot be relaxed by
any tranche without a fresh GC-018:

- `runtimeExecutionAuthorized=false`
- `canReinject=false`
- `rawMemoryReleased=false`
- `externalFetchAuthorized=false`
- `registryPublicationAuthorized=false`

## Claim Boundary

This GC-018 authorizes documentation-only connector normalization between
existing closed surfaces. It does not authorize runtime tool execution, tool
re-execution after recovery, workflow re-execution, CLI invocation, MCP
bridging, memory reinjection, raw memory release, spec-change automation,
re-intake automation, receipt-envelope extension, provider behavior, public-sync
work, hosted readiness, production readiness, or public release readiness.
