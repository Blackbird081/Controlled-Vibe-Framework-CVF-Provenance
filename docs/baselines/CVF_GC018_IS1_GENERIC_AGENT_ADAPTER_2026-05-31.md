# CVF GC-018 Continuation Candidate
## IS1 — Generic Agent Adapter

Memory class: BASELINE_RECORD

Status: AUTHORIZED

Date: 2026-05-31

Parent advisory: LHW19 T1 `cvf.integrationArchitectureControlPointsAdvisory.lhw19.t1.v1`
Prerequisite: INT-1 `cvf.genericMcpAdapter.int1.v1` (MCP adapter tools CLOSED_PASS_BOUNDED)

---

## Purpose

Authorize IS1: implement a Generic Agent Adapter that maps external agent framework
events to CVF governance control points (CP1-CP5). This is the first integration SDK
adapter tranche per LHW19 T1 advisory. Target: framework-neutral generic adapter
(not LangChain/CrewAI/AutoGen specific — those require separate tranches).

Per LHW18 T2: CVF is a Governance Layer, not an Agent OS. Frameworks call IN to CVF,
not the reverse. The adapter normalizes framework-agnostic events into CVF governance
intake, plan validation, tool gateway, runtime guard, and result validation signals.

## Scope / Target / Owner Boundary

Target: new `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/generic-agent-adapter.ts`.
Owner: CVF MCP server / integration adapter surface.
Boundary:
- New file in MCP server extension — no route.ts change, no new MCP tools beyond this file
- Re-export type-only from MCP server index if applicable
- Tests in `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/tests/generic-agent-adapter.test.ts`
- Adapter maps 5 event types (intent/plan/tool/execution/result) to CVF CP1-CP5 advisory
- `runtimeAdapterAuthorized: false` always (advisory mapping only)

## Source / Predecessor Evidence

- LHW19 T1 spec: `docs/reference/CVF_LHW19_T1_INTEGRATION_ARCHITECTURE_CONTROL_POINTS_ADVISORY_CONNECTOR_SPEC_2026-05-30.md`
- LHW18 T2 positioning: `docs/reference/CVF_LHW18_T2_CVF_POSITIONING_GOVERNANCE_LAYER_ADVISORY_CONNECTOR_SPEC_2026-05-30.md`
- INT-1: `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` (MCP tools as integration point)
- Delta D3: `cvf_invoke_cli_stage` whitelist (CP3 Tool Gateway existing owner)

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED. Baseline: IS1 Generic Agent Adapter. Parent: LHW19 T1 + INT-1.

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/generic-agent-adapter.ts` — new file
- Tests in `src/generic-agent-adapter.test.ts`
- Fast Lane + completion review

## Authorization Boundary

- Contract: `cvf.genericAgentAdapter.is1.v1`
- Hard invariants: no live framework execution; no new MCP tools added here; `runtimeAdapterAuthorized: false` always

## Evidence / Verification

- New file: `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/generic-agent-adapter.ts` — DELIVERED
- Tests: `src/generic-agent-adapter.test.ts` — 14 tests, 554/554 PASS (22 MCP files)
- Fast Lane: `docs/reviews/CVF_IS1_GENERIC_AGENT_ADAPTER_FAST_LANE_2026-05-31.md` — PASS
- Completion: `docs/reviews/CVF_IS1_GENERIC_AGENT_ADAPTER_COMPLETION_2026-05-31.md` — CLOSED_PASS_BOUNDED

## Claim Boundary

IS1 implements a framework-neutral advisory adapter only. It does not integrate live
LangChain/CrewAI/AutoGen frameworks, spawn agent processes, or claim production readiness.

---

*Authorized: 2026-05-31 | Operator sign-off in-session*
