# CVF Product Depth Roadmap

Memory class: SUMMARY_RECORD

Status: DEMAND_GATED

docType: roadmap

Date: 2026-05-29

---

## Purpose

Define the product-depth scope needed to close CVF 25.05 Gaps 5 and 6 — the
two remaining gaps after LHW12/LHW13 close. This roadmap is a planning record
only. No tranche may begin without explicit operator authorization and a fresh
GC-018.

## Source

- CVF 25.05 Gop_y.md: `.private_reference/legacy/CVF 25.05/Gop_y.md`
  — Gap 5 (Operations Cockpit), Gap 6 (External Capability Admission)
- CVF 25.05 review: `.private_reference/legacy/CVF 25.05/CLAUDE_REVIEW_OF_GOP_Y_2026-05-25.md`
  — GAP 5: "medium-large effort; real product surface, not just docs"
  — GAP 6: "small if extends ES1/C7B/C7C; larger if covers MCP/tool/repo"
- ES1: `docs/reference/CVF_EXTERNAL_SKILL_INTAKE_SCREENING_PACKET_2026-05-25.md`
- C7B/C7C completion: `docs/reviews/CVF_C7B_*/CVF_C7C_*`

## Scope / Target / Owner Boundary

Target: PD-1 — governance operations cockpit specification (docs then UI);
PD-2 — external capability admission contract expansion to MCP/tool/repo scope.

Owner: CVF product and governance steering surface.

Allowed per Phase A: docs files only; no runtime code changes.
Allowed per Phase B: requires explicit GC-018 and operator authorization.

## Why This Roadmap Exists

LHW waves and the Execution Layer Roadmap address connectors and runtime
behaviors. Gaps 5 and 6 are product/UX surfaces — they require different
scope treatment. Recording them here ensures they are not forgotten when CVF
25.05 absorption review is done.

---

## PD-1 — Governance Operations Cockpit Specification

**Gap 5:** CVF has per-call advisory outputs (LHW10-T1, LHW10-T3, LHW11-T1,
W4 scorecard, V3 diagnostic) but no aggregated operator-grade dashboard
specification defining what an operator sees, at what refresh cadence, with
what drill-down paths.

**What to build:**

Phase A (docs-only spec, low risk):
- `docs/product/CVF_GOVERNANCE_OPERATIONS_COCKPIT_SPEC.md`
- Define what the cockpit shows: provider lane health, release gate status,
  latest receipt, policy block/allow ratio, quota/cost preflight, failed
  workflow packs, role rejection events, evidence export queue, benchmark status
- Map each cockpit element to an existing CVF surface (e.g., provider lane
  health → LHW10-T3 `providerHealthAdvisoryType`; release gate → W4
  `clarityStatus`; policy ratio → V3 `ExecutionDiagnosticClass` aggregation)
- Define refresh cadence (per-call vs. session-level vs. daily aggregate)

Phase B (UI surface, medium risk, separate GC-018):
- Wire cockpit spec into `cvf-web` governance dashboard route
- Requires `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/` changes
- Requires live data aggregation from existing receipt store

**Risk class:** Phase A = R0 (docs only); Phase B = R1 (UI extension).

**Prerequisites:** LHW11 CLOSED_PASS_BOUNDED (posture aggregator needed);
LHW10 CLOSED_PASS_BOUNDED (provider health advisory needed); every cockpit
element source path verified before dispatch; fresh GC-018. If the cockpit
includes memory continuity level, LHW13-T2 must close first or that element
must be explicitly deferred.

**CVF 25.05 Gap 5 closure condition:** Phase A spec CLOSED_PASS counts as
gap closed; Phase B is product enhancement beyond gap closure.

---

## PD-2 — External Capability Admission Contract Expansion

**Gap 6:** ES1/C7B/C7C cover **skill-only** external capability admission.
MCP server, tool, repo, and database source admission remain undefined —
not allowed, not forbidden, not governed.

**What to build:**

Phase A (extend ES1 scope, low risk):
- `docs/contracts/CVF_EXTERNAL_CAPABILITY_ADMISSION_CONTRACT.md`
- Define admission gates for each source type:

| Source type | Admission path | Risk |
| --- | --- | --- |
| External skill pack | ES1 + C7B/C7C (already exists) | R1 |
| MCP server | New: MCP admission gate (server origin, tool list, scope limit, sandbox) | R2 |
| CLI tool | LHW6-T2 onboarding classification already covers this | R1 |
| External repo | New: repo admission (provenance, license, dependency scan) | R2 |
| Database source | W3/LHW5-T1 taxonomy covers read-only proof; write remains blocked | R2 |

Phase A can be docs-only extension of ES1 for MCP and repo scope.
Phase B (runtime enforcement) requires live execution scope and separate GC-018.

**Risk class:** Phase A = R0 (docs extension); Phase B = R2 (enforcement).

**Prerequisites:** ES1 + C7B + C7C CLOSED_PASS_BOUNDED; LHW9-T1 MCP approval
advisory CLOSED_PASS_BOUNDED; fresh GC-018 for Phase A.

**CVF 25.05 Gap 6 closure condition:** Phase A contract doc CLOSED_PASS counts
as gap closed for MCP and repo scope. Enforcement (Phase B) is product depth
beyond gap closure.

---

## CVF 25.05 Full Absorption Closure Conditions

| Gap | Closed by | Status |
| --- | --- | --- |
| Gap 1 — Agent Reading Protocol | LHW13-T1 | WORK_ORDER_READY |
| Gap 2 — Outcome Pack Taxonomy | LHW12-T2 | WORK_ORDER_READY (after T1) |
| Gap 3 — Provider Method Live Proof | `CVF_PROVIDER_METHOD_LIVE_PROOF_ROADMAP` PM-1/PM-2/PM-3 | DEMAND_GATED |
| Gap 4 — Memory L0-L3 | LHW13-T2 | WORK_ORDER_READY (after T1) |
| Gap 5 — Operations Cockpit | PD-1 Phase A | DEMAND_GATED |
| Gap 6 — External Capability Admission | PD-2 Phase A | DEMAND_GATED |
| Gap 7 — Async Worker Lifecycle | LHW12-T3 | WORK_ORDER_READY (after T1+T2) |
| Gap 8 — Action taxonomy detail | W3/TA1/LHW waves partially; per-action rollback detail DEMAND_GATED | PARTIALLY_CLOSED |
| Gap 9 — Graph context resolver | LHW13-T3 | WORK_ORDER_READY (after T1+T2) |

CVF 25.05 (`Gop_y.md`) will be **fully absorbed** when:
- [ ] LHW12 CLOSED_PASS_BOUNDED
- [ ] LHW13 CLOSED_PASS_BOUNDED
- [ ] Provider Method Live Proof PM-1/PM-2/PM-3 CLOSED_PASS
- [ ] PD-1 Phase A CLOSED_PASS
- [ ] PD-2 Phase A CLOSED_PASS

---

## Sequencing

```
LHW12/LHW13 (in progress, parallel)
  ↓ after both close
Provider Method Live Proof (PM-1 → PM-2 → PM-3, parallel with PD)
Product Depth (PD-1 Phase A → PD-2 Phase A, parallel with PM)
```

PD-1 and PD-2 can run in parallel with Provider Method Live Proof — no shared
source dependencies.

## Unlock Conditions

- Operator explicitly authorizes PD-1 or PD-2
- LHW12/LHW13 are not global prerequisites for PD-1/PD-2 Phase A, but any
  element that cites an LHW12/LHW13 connector must remain HOLD until that
  connector exists and is source-verified.
- Fresh GC-018 per sub-tranche

## Authorization / Decision

Status: DEMAND_GATED. Operator must authorize PD-1 or PD-2 individually and
issue a fresh GC-018 per sub-tranche. LHW12/LHW13 are not blanket
prerequisites for Phase A, but PD-1 dispatch is blocked while any cockpit
element depends on a future LHW connector or missing evidence path.

## Non-Goals

- Phase B (runtime wiring) without a separate GC-018
- Full external marketplace readiness (beyond admission contract docs)
- Claiming cockpit is operational before Phase B wiring is complete
- MCP execution or tool execution (admission contract is governance docs only)

## Work Plan

| Tranche | Deliverable | Gate |
| --- | --- | --- |
| PD-1 Phase A | Cockpit spec doc mapping CVF surfaces to dashboard elements | Operator authorization + fresh GC-018 + all cockpit element sources verified |
| PD-1 Phase B | UI surface wiring in cvf-web | PD-1 Phase A CLOSED_PASS + fresh GC-018 |
| PD-2 Phase A | External Capability Admission Contract doc (MCP + repo scope) | Operator authorization + fresh GC-018 |
| PD-2 Phase B | Runtime enforcement wiring | PD-2 Phase A CLOSED_PASS + fresh GC-018 |

## Acceptance Criteria

PD-1 Phase A: `docs/product/CVF_GOVERNANCE_OPERATIONS_COCKPIT_SPEC.md` — maps
each cockpit element to an existing CVF surface with verified source path;
GC-018 + work order + completion review; governance gates PASS.

PD-2 Phase A: `docs/contracts/CVF_EXTERNAL_CAPABILITY_ADMISSION_CONTRACT.md`
— defines admission gates for MCP, tool, repo, database scope; extends ES1;
GC-018 + work order + completion review; governance gates PASS.

CVF 25.05 full absorption: LHW12 + LHW13 + PM-1/PM-2/PM-3 + PD-1 Phase A +
PD-2 Phase A all CLOSED_PASS.

## Verification

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base <pre-PD-commit> --head <PD-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base <pre-PD-commit> --head <PD-commit> --enforce
```

## Claim Boundary

This roadmap is a planning record. It does not authorize implementation and
does not claim any governance cockpit or external capability contract is
currently operational.
