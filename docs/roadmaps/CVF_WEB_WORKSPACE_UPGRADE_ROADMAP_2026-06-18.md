# CVF Web Workspace Upgrade Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_ACTIVE_WWU_T3B_CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: roadmap

## Purpose

Upgrade CVF Web as the operator-facing workspace for non-coders while keeping
Local Workspace Runtime and MCP/CLI enforcement as a separate agent-facing
layer.

## Authorization / Decision

Authorized by operator instruction on 2026-06-18 to clarify the absorbed
workspace split and proceed toward a CVF Web upgrade.

Decision: start with `CVF_WEB_WORKSPACE` foundation and source verification.
Keep `CVF_LOCAL_WORKSPACE_RUNTIME` parked until explicit runtime/MCP
authorization.

## Scope / Target / Owner Boundary

Target: CVF Web Workspace planning and future product UI upgrade path.

Owner boundary: this roadmap authorizes foundation clarification and future
bounded Web Workspace work orders. It does not implement UI, mutate Local
Workspace Runtime, implement MCP tools, run providers, public-sync, or claim
production/public readiness.

## Source Authority

| Source | Role |
|---|---|
| `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | Central two-layer workspace architecture |
| `docs/reference/agent_workspace/README.md` | stable workspace front door |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | CVF Web Workspace read model precedent |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | Local Runtime/MCP boundary |
| `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | external package absorption map |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/docs/reference/CVF_W112_WEB_GOVERNANCE_SURFACE_INVENTORY_2026-04-22.md` | existing CVF Web governance-surface inventory |
| `DESIGN.md` | mandatory visual contract before frontend implementation |

## Architecture Decision

CVF Workspace has two first-class layers:

| Layer | Roadmap owner | Disposition |
|---|---|---|
| CVF Web Workspace | this roadmap | operator-facing view, assignment, approval, evidence, and result surface |
| CVF Local Workspace Runtime | future runtime/MCP roadmap or EARC-T4 | agent-facing execution substrate through MCP/CLI/CVF guards |

This roadmap starts with CVF Web Workspace. Local Runtime remains parked unless
the operator explicitly opens runtime/MCP implementation.

## Design Control Gate

Any WWU tranche that edits frontend code must read `DESIGN.md` before
implementation and must include:

- fresh GC-018;
- source-verified work order;
- Agent Handoff Contract Control Block;
- Agent Workspace Design Control Block;
- Workspace Two-Layer Control Block;
- focused UI/type/test evidence.

Any WWU tranche that touches runtime queues, MCP, CLI wrappers, provider/live
proof, or Local Workspace Runtime must be split from Web UI work unless the work
order selects `BOTH_WITH_BOUNDARY` and lists separate proof requirements.

## Tranche Plan

| Tranche | Status | Objective | Owner | Boundary |
|---|---|---|---|---|
| WWU-T0 | CLOSED_PASS_BOUNDED | Canonicalize the two-layer workspace architecture and Web upgrade boundary | Codex | Documentation/reference only |
| WWU-T1 | CLOSED_PASS_BOUNDED | Audit current `cvf-web` surfaces against CVF Web Workspace read-model needs | Codex | Source verification and route/component map only |
| WWU-T2 | CLOSED_PASS_BOUNDED | Implement first bounded CVF Web Workspace operator dashboard/read model | Codex | `CVF_WEB_WORKSPACE` read-only dashboard/read model; no Local Runtime mutation |
| WWU-T2A | CLOSED_PASS_BOUNDED | Add generated workspace state lane summary to the read-only Web Workspace dashboard/read model | Codex | `CVF_WEB_WORKSPACE` read-only lane summary; no generated state mutation |
| WWU-T3 | OPENED_BY_OPERATOR_AUTHORIZATION | Decide Local Workspace Runtime/MCP bridge after Web read model is stable | Codex | Split into narrow runtime/MCP tranches |
| WWU-T3A | CLOSED_PASS_BOUNDED | Implement one deterministic MCP Model Gateway execute preview tool | Codex | `CVF_LOCAL_WORKSPACE_RUNTIME`; no provider/live, public-sync, runtime queue, or readiness claim |
| WWU-T3B | CLOSED_PASS_BOUNDED | Implement an injectable MCP Model Gateway execution adapter | Codex | Module bridge only; no provider/live composition, secret use, public-sync, runtime queue, or readiness claim |

## WWU-T1 Candidate Scope

WWU-T1 should produce a source-backed audit packet, not product code. It should:

- map current `cvf-web` workspace/home/governance surfaces;
- verify existing API read routes and governance evidence routes;
- identify the minimal operator workspace read model for current mode, next
  move, active handoff, roadmap/work-order status, evidence, receipts, and
  parked checkpoints;
- separate read-only Web Workspace data from future governed action requests;
- recommend the smallest WWU-T2 UI implementation scope.

## Work Plan

1. Close WWU-T0 foundation clarification.
2. Open WWU-T1 source-verification audit for current `cvf-web` surfaces.
3. Use WWU-T1 output to dispatch the smallest WWU-T2 Web Workspace UI tranche.
4. Keep WWU-T3 runtime/MCP parked until the operator explicitly opens it.

## Acceptance Criteria

- Two-layer standard exists at a stable indexed reference path.
- Web Workspace is defined as operator-facing read/decision surface.
- Local Workspace Runtime is defined as agent-facing execution substrate.
- WWU-T1 is the next Web upgrade step before product UI edits.
- Runtime/MCP remains parked and cannot be implied by Web UI work.

## Verification / Evidence

| Evidence | Required result |
|---|---|
| `docs/reference/agent_workspace/README.md` | points to the two-layer standard |
| `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | `Status: ACTIVE_STANDARD` |
| `docs/reviews/CVF_WWU_T0_WORKSPACE_TWO_LAYER_FOUNDATION_COMPLETION_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` |
| `python governance/compat/run_worker_return_fast_gate.py` | PASS before commit |

## Non-Goals

- No MCP implementation.
- No Local Workspace Runtime mutation.
- No provider/live proof unless a later UI claim requires it.
- No public-sync.
- No raw external package import.
- No production/public readiness claim.

## WWU-T0 Closure Note (2026-06-18)

WWU-T0 is `CLOSED_PASS_BOUNDED`. It added the stable two-layer architecture
standard and linked it into the agent workspace front door, operator view plan,
runtime expansion contract, and external package absorption map.

## WWU-T1 Closure Note (2026-06-18)

WWU-T1 is `CLOSED_PASS_BOUNDED`. It produced a source-backed audit of current
`cvf-web` surfaces and found that current Web already has governance,
evidence, health, operations, approvals, work-transfer, and chat/session
surfaces, but no dedicated active CVF session-state/handoff/workspace read
model. WWU-T2 then required fresh GC-018 authoring before product UI
implementation could be dispatched.

## WWU-T2 Closure Note (2026-06-18)

WWU-T2 is `CLOSED_PASS_BOUNDED`. It implemented the first read-only CVF Web
Workspace operator dashboard/read model under `cvf-web`: a server-side
continuity projection, `GET /api/workspace/state`, `/workspace` dashboard, and
sidebar navigation. The execution boundary remains `CVF_WEB_WORKSPACE` only:
Local Workspace Runtime, MCP/CLI tooling, provider/live proof, public-sync,
runtime enforcement, action requests, and readiness claims remain parked.

## WWU-T2A Closure Note (2026-06-19)

WWU-T2A is `CLOSED_PASS_BOUNDED`. It adds a bounded read-only Web Workspace
lane summary from `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`
to the existing server read model, `GET /api/workspace/state`, and
`/workspace` dashboard. The tranche does not mutate generated workspace state,
Local Workspace Runtime, MCP/CLI tooling, provider/live proof, public-sync,
runtime enforcement, action requests, or readiness claims.

## WWU-T3A Dispatch Note (2026-06-19)

WWU-T3A is ready to dispatch after operator authorization on 2026-06-19. It
opens the first bounded Local Workspace Runtime/MCP slice: one deterministic
MCP Model Gateway execute preview tool named `cvf_model_gateway_execute_preview`.
The tranche forbids provider/live calls, raw credential handling, public-sync,
runtime queues, schedulers, worker daemons, broad MCP gateway implementation,
and readiness claims.

## WWU-T3A Closure Note (2026-06-19)

WWU-T3A is `CLOSED_PASS_BOUNDED`. It adds
`cvf_model_gateway_execute_preview` as a deterministic, secret-safe MCP preview
tool that maps caller input to a GatewayExecuteRequest-compatible shape and
returns local preview response/error envelopes with receipt fields. The tranche
does not perform provider/live calls, accept raw credential material, open
runtime queues, schedulers, worker daemons, public-sync, or readiness claims.

## WWU-T3B Dispatch Note (2026-06-19)

WWU-T3B is dispatched after the operator authorized completion where current
prerequisites are sufficient. It is limited to an injectable MCP adapter that
calls the source-compatible Model Gateway execution method, fails closed when
no executor is configured, and preserves executor response/error plus receipt.
Provider/live composition, secrets/quota, public-sync, executable queues, broad
runtime enforcement, and readiness claims remain outside this tranche.

## WWU-T3B Closure Note (2026-06-19)

WWU-T3B is `CLOSED_PASS_BOUNDED`. The MCP package now registers
`cvf_model_gateway_execute`, maps source-compatible execute fields, calls an
injected executor, preserves response/error plus receipt, and fails closed for
unauthorized roles, credential-bearing input, invalid requests, missing runtime
composition, and thrown executor errors. The default MCP server deliberately
registers no live executor. Provider/live composition remains a separate
authorization boundary.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T1_CVF_WEB_WORKSPACE_SURFACE_AUDIT_FOR_CODEX_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_WWU_T1_CVF_WEB_WORKSPACE_SURFACE_AUDIT_COMPLETION_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Audit packet | `docs/audits/CVF_WWU_T1_CVF_WEB_WORKSPACE_SURFACE_AUDIT_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | this file | `ROADMAP_ACTIVE_WWU_T3B_CLOSED_PASS_BOUNDED` | PASS |
| WWU-T2 GC-018 | `docs/baselines/CVF_GC018_WWU_T2_CVF_WEB_WORKSPACE_OPERATOR_DASHBOARD_READ_MODEL_2026-06-18.md` | `Status: DISPATCH_READY` | PASS |
| WWU-T2 work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T2_CVF_WEB_WORKSPACE_OPERATOR_DASHBOARD_READ_MODEL_FOR_CODEX_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| WWU-T2 completion | `docs/reviews/CVF_WWU_T2_CVF_WEB_WORKSPACE_OPERATOR_DASHBOARD_READ_MODEL_COMPLETION_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| WWU-T2 evidence | `docs/reviews/evidence/wwu-t2-cvf-web-workspace-operator-dashboard-read-model-2026-06-18.json` | `status=CLOSED_PASS_BOUNDED` | PASS |
| WWU-T2A GC-018 | `docs/baselines/CVF_GC018_WWU_T2A_CVF_WEB_WORKSPACE_LANE_SUMMARY_READ_MODEL_2026-06-19.md` | `Status: DISPATCH_READY` | PASS |
| WWU-T2A work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T2A_CVF_WEB_WORKSPACE_LANE_SUMMARY_READ_MODEL_FOR_CODEX_2026-06-19.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| WWU-T2A completion | `docs/reviews/CVF_WWU_T2A_CVF_WEB_WORKSPACE_LANE_SUMMARY_READ_MODEL_COMPLETION_2026-06-19.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| WWU-T2A evidence | `docs/reviews/evidence/wwu-t2a-cvf-web-workspace-lane-summary-read-model-2026-06-19.json` | `status=CLOSED_PASS_BOUNDED` | PASS |
| WWU-T3A GC-018 | `docs/baselines/CVF_GC018_WWU_T3A_LOCAL_WORKSPACE_RUNTIME_MCP_MODEL_GATEWAY_EXECUTE_PREVIEW_2026-06-19.md` | `Status: DISPATCH_READY` | PASS |
| WWU-T3A work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T3A_LOCAL_WORKSPACE_RUNTIME_MCP_MODEL_GATEWAY_EXECUTE_PREVIEW_FOR_CODEX_2026-06-19.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| WWU-T3A completion | `docs/reviews/CVF_WWU_T3A_LOCAL_WORKSPACE_RUNTIME_MCP_MODEL_GATEWAY_EXECUTE_PREVIEW_COMPLETION_2026-06-19.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| WWU-T3A evidence | `docs/reviews/evidence/wwu-t3a-local-workspace-runtime-mcp-model-gateway-execute-preview-2026-06-19.json` | `status=CLOSED_PASS_BOUNDED` | PASS |
| WWU-T3B GC-018 | `docs/baselines/CVF_GC018_WWU_T3B_MCP_MODEL_GATEWAY_EXECUTION_ADAPTER_2026-06-19.md` | `Status: DISPATCH_READY` | PASS |
| WWU-T3B work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T3B_MCP_MODEL_GATEWAY_EXECUTION_ADAPTER_FOR_CODEX_2026-06-19.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| WWU-T3B completion | `docs/reviews/CVF_WWU_T3B_MCP_MODEL_GATEWAY_EXECUTION_ADAPTER_COMPLETION_2026-06-19.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| WWU-T3B evidence | `docs/reviews/evidence/wwu-t3b-mcp-model-gateway-execution-adapter-2026-06-19.json` | `status=CLOSED_PASS_BOUNDED` | PASS |
| Central standard | `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | `Status: ACTIVE_STANDARD` | PASS |
| Front door | `docs/reference/agent_workspace/README.md` | points to two-layer standard | PASS |
| Web local view | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | cites two-layer standard | PASS |
| Runtime local view | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | cites two-layer standard | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated from source entry | PASS |
| Registry Markdown | BLOCKED with reason: no separate markdown registry is required for this reference family | no path changed | BLOCKED with reason |
| External evidence digest | `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_WORKSPACE_LAYER_2026-06-18.md` | prior governed absorption digest covers the external workspace package; representative sha256 `a267edd4f9702daa1047034520f3e24b0c7321b17d1451a858b12a2845b7cd82` | PASS |
| System loop interlock | N/A with reason: no runtime interlock implementation changed | no path changed | N/A with reason |
| Session continuity | separate session-sync follows material commit | active session surfaces update after material commit if next move changes | N/A with reason |
| Runtime proof | N/A with reason: runtime/provider/MCP proof is out of scope | no runtime proof required | N/A with reason |
| Public export disposition | `DEFERRED_PRIVATE_ONLY` | private provenance foundation roadmap | PASS |

## Acceptance Receipt Assertion Matrix

| Criterion | Required value | Observed value | Status |
|---|---|---|---|
| WWU-T3A tool | `cvf_model_gateway_execute_preview` | implemented in MCP server | PASS |
| Runtime execution claim | none | deterministic preview only | PASS |
| Provider/live proof | forbidden | no provider/live command claimed | PASS |
| Public-sync | forbidden | no public-sync performed | PASS |
| Future expansion | fresh GC-018 required | recorded in claim boundary | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Web Workspace foundation. Public-facing wording
requires separate public-sync authorization.

## Claim Boundary

This roadmap clarifies and sequences the Web Workspace upgrade path. It does
not implement UI, Local Runtime, MCP, provider calls, public-sync, or
production/public readiness.
