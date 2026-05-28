# CVF GC-018 — Product Depth

Memory class: FULL_RECORD

Status: ACTIVE

docType: gc018_baseline

Date: 2026-05-29

---

## Purpose

Authorize Product Depth tranches PD-1 Phase A (Governance Operations Cockpit
specification) and PD-2 Phase A (External Capability Admission Contract
expansion to MCP/tool/repo scope). Closes CVF 25.05 Gop_y.md Gaps 5 and 6
at the Phase A documentation level.

Operator direction 2026-05-29: build work orders for all remaining roadmaps.

---

## Scope

Two documentation-only tranches (Phase A only):

- PD-1 — Governance Operations Cockpit Specification
  (`docs/product/CVF_GOVERNANCE_OPERATIONS_COCKPIT_SPEC.md`)
- PD-2 — External Capability Admission Contract Expansion
  (`docs/contracts/CVF_EXTERNAL_CAPABILITY_ADMISSION_CONTRACT.md`)

Phase B (UI wiring for PD-1; runtime enforcement for PD-2) requires separate
GC-018 and operator authorization. Not covered here.

No `.ts` / `.tsx` / `.js` / `.py` file change. No `EXTENSIONS/` source.
No receipt envelope schema. No public-sync repo. No MCP execution.

---

## Source / Predecessor Evidence

- CVF 25.05 review: `.private_reference/legacy/CVF 25.05/CLAUDE_REVIEW_OF_GOP_Y_2026-05-25.md`
  — GAP 5 (Operations Cockpit): "medium-large effort; real product surface"
  — GAP 6 (External Capability): "small if extends ES1/C7B/C7C"
- Product Depth Roadmap: `docs/roadmaps/CVF_PRODUCT_DEPTH_ROADMAP_2026-05-29.md`
- ES1 screening packet: `docs/reference/CVF_EXTERNAL_SKILL_INTAKE_SCREENING_PACKET_2026-05-25.md`
- LHW11-T1 posture aggregator: `docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_SPEC_2026-05-28.md`
- LHW10-T3 provider health: `docs/reference/CVF_LHW10_T3_PROVIDER_HEALTH_DEGRADATION_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- W4 benchmark scorecard: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts`
- V3 diagnostic: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts`
- LHW9-T1 MCP approval: `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`

---

## Decision / Baseline

PD-1 and PD-2 Phase A are authorized as documentation-only spec files.
PD-2 may begin in parallel with PD-1 — no shared dependencies. PD-1 dispatch
is blocked until every cockpit element has an existing source/canonical
contract or the unverified element is explicitly deferred in the work order.

---

## Required Evidence

Per tranche: spec doc with all required sections; work order with Source
Verification Table; completion review; both governance gates PASS; no code
file in diff; session continuity updated.

---

## Verification

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base a8d2a0eb --head <pd-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base a8d2a0eb --head <pd-commit> --enforce
```

---

## Claim Boundary

This GC-018 authorizes documentation spec files only. It does not authorize
UI wiring, runtime enforcement, MCP execution, external asset ingestion,
hosted readiness, production readiness, or public release readiness.
