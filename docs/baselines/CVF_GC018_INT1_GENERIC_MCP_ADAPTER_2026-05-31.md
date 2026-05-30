# CVF GC-018 Fast Lane — INT-1 Generic MCP Adapter

Memory class: BASELINE_RECORD

Status: AUTHORIZED

Date: 2026-05-31

Parent: LHW19 T1 `cvf.integrationArchitectureControlPointsAdvisory.lhw19.t1.v1`

---

## Purpose

Authorize INT-1: extend `CVF_ECO_v2.5_MCP_SERVER` with two new tools that close
the CP2 Plan Validator gap (identified in LHW19 T1) and provide a generic event
emission entry point for external agent frameworks. Also deliver one integration
guide document for how external frameworks connect to CVF via MCP.

## Scope / Target / Owner Boundary

Target: `cvf.genericMcpAdapter.int1.v1`
Owner: `CVF_ECO_v2.5_MCP_SERVER`
Boundary: additive tools only; no existing tool modified; no route.ts change;
no receipt-envelope extension; `runtimeExecutionAuthorized=false` for plan
enforcement — `cvf_validate_plan` is advisory readout only, matching CP1-CP5
advisory posture established in LHW19 T1.

## Source / Predecessor Evidence

- LHW19 T1: `docs/reference/CVF_LHW19_T1_INTEGRATION_ARCHITECTURE_CONTROL_POINTS_ADVISORY_CONNECTOR_SPEC_2026-05-30.md`
  — CP2 Plan Validator coverage: PARTIAL
- LHW18 T2: `docs/reference/CVF_LHW18_T2_CVF_POSITIONING_GOVERNANCE_LAYER_ADVISORY_CONNECTOR_SPEC_2026-05-30.md`
  — Integration SDK concept absorbed
- Existing: `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` — 781 lines (hard limit 1000); 10 tools present

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED as Fast Lane R1 tranche (additive MCP tools + guide doc).

Proposed deliverables:
1. `cvf_validate_plan` — MCP tool: receives `{ planSteps, toolsRequired, agentRole }`;
   evaluates plan risk and forbidden steps; returns advisory decision (not enforcement).
   Maps to CP2 Plan Validator in LHW19 T1.
2. `cvf_emit_agent_event` — MCP tool: generic event emitter for external frameworks;
   receives `{ eventType, agentId, payload }`; routes to appropriate CVF gate;
   maps to the 5-event model in LHW19 T2.
3. `docs/guides/CVF_GENERIC_MCP_ADAPTER_INTEGRATION_GUIDE_2026-05-31.md` — how
   external agent frameworks connect to CVF via MCP, with 4 integration points,
   5 events, and code examples.
4. Unit tests: `index.int1-adapter.test.ts` (≥6 tests covering both new tools)

## Evidence / Verification

- Both tools present in MCP server with `withMcpToolAudit` wrapper
- `cvf_validate_plan` returns `planRisk`, `forbiddenStepsDetected`, `advisoryDecision`
- `cvf_emit_agent_event` routes to correct gate by `eventType`
- MCP server `index.ts` stays ≤ 1000 lines after additions
- Unit tests PASS
- TypeScript PASS
- Live proof: call `cvf_validate_plan` via MCP client

## Claim Boundary

`runtimeExecutionAuthorized=false` — both tools are advisory only. No plan
enforcement that blocks execution. No new receipt envelope. No route.ts change.
MCP server line limit: 1000 lines hard limit.

## Fast Lane Risk Assessment

Risk class: R1 (additive MCP tools; advisory only; no security boundary crossed).
Fast Lane authorized: YES — same pattern as Delta D2/D3.
