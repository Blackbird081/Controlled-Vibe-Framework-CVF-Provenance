# CVF GC-018 — Execution Layer

Memory class: FULL_RECORD

Status: ACTIVE

docType: gc018_baseline

Date: 2026-05-29

---

## Purpose

Authorize Execution Layer tranches EL-1 (Pipeline Chain Orchestrator Contract),
EL-2 (WorkerTimeout Handler), EL-3 (ReviewDeadlock + Micro-Task Decomposition).
Closes CVF 28.05 Gaps D, B, C. These tranches require live execution scope
and cannot be closed by doc-only LHW connectors.

Operator direction 2026-05-29: API keys available; build work orders for all
remaining roadmaps.

Prerequisite: LHW12 and LHW13 must both be CLOSED_PASS_BOUNDED before EL-1
dispatch. This ensures connector advisory types (posture tier, worker lifecycle,
outcome taxonomy) are available for the pipeline contract to reference.

---

## Scope

Three tranches — EL-1 is doc-first contract definition; EL-2 and EL-3 involve
runtime binding with live receipts:

- EL-1 — Pipeline Chain Orchestrator Contract (doc-first, then binding)
- EL-2 — WorkerTimeout Handler (runtime binding + receipt)
- EL-3 — ReviewDeadlock + Micro-Task Decomposition (runtime binding + receipt)

Each tranche: fresh work order; GC-018 reference; completion review;
governance gates PASS.

---

## Source / Predecessor Evidence

- CVF 28.05 prototype: `.private_reference/legacy/CVF 28.05/cvf_cli.py`
  — EL-1 from overall pipeline (lines 56–166); EL-2 from WorkerTimeoutException
  (lines 104–115); EL-3 from ReviewDeadlockException (lines 123–148)
- CVF 28.05 gap record: GC-018 LHW11 section "New Source Family: CVF 28.05"
- Execution Layer Roadmap: `docs/roadmaps/CVF_EXECUTION_LAYER_ROADMAP_2026-05-29.md`
- LHW12-T1 posture advisory (prerequisite for EL-1 model tier reference):
  `docs/reference/CVF_LHW12_T1_POSTURE_TO_MODEL_TIER_ADVISORY_CONNECTOR_SPEC_2026-05-29.md`
- LHW12-T3 worker lifecycle advisory (prerequisite for EL-1/EL-2/EL-3):
  `docs/reference/CVF_LHW12_T3_ASYNC_WORKER_LIFECYCLE_BOUNDARY_CONNECTOR_SPEC_2026-05-29.md`
- WR1 `WorkflowRecoveryAction`: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
- MA1 transfer standard: `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
- V3 diagnostic: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts`

---

## Decision / Baseline

EL-1, EL-2, EL-3 are authorized in sequence. EL-2 gates on EL-1 CLOSED_PASS.
EL-3 gates on EL-2 CLOSED_PASS. All three gate on LHW12 + LHW13
CLOSED_PASS_BOUNDED.

Blocked-work-class list in `ACTIVE_SESSION_STATE.json` remains in force.
This authorization does not lift: new_receipt_envelopes, new_role_taxonomies,
new_provider_execution_semantics, broad_external_knowledge_absorption.

---

## Required Evidence

EL-1: pipeline contract spec + work order + completion review; governance
gates PASS; no unauthorized execution claimed.

EL-2: timeout handler implementation + live receipt showing timeout detection
and recovery; work order + completion review; governance gates PASS.

EL-3: deadlock handler + decomposition logic + live receipt showing retry
counter escalation; work order + completion review; governance gates PASS.

---

## Verification

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base a8d2a0eb --head <el-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base a8d2a0eb --head <el-commit> --enforce
```

---

## Claim Boundary

This GC-018 authorizes execution layer contract and handler implementation.
It does not authorize: new provider execution semantics beyond the pipeline
contract, broad multi-agent framework, autonomous agent spawning without
governance gate, new receipt envelope schema, hosted readiness, production
readiness, or public release readiness.
