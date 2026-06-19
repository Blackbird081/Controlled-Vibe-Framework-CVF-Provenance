# CVF GC-018 - WWU-T3A Local Workspace Runtime MCP Model Gateway Execute Preview

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-19

docType: baseline

Owner: Codex

rawMemoryReleased: false

GC-018 class: local-workspace-runtime-mcp-model-gateway-execute-preview

## Purpose

Authorize WWU-T3A dispatch for the first bounded Local Workspace Runtime/MCP
implementation slice: one deterministic MCP preview tool for Model Gateway
execute ingress.

## Authorization / Decision

Operator authorization was given on 2026-06-19 by the instruction `LAM DI`
after Codex identified WWU-T3 Local Workspace Runtime/MCP as the next roadmap
candidate requiring explicit runtime/MCP authorization, fresh GC-018, and a
source-verified work order.

Decision: AUTHORIZE WWU-T3A dispatch for a narrow MCP tool candidate named
`cvf_model_gateway_execute_preview`.

This baseline does not authorize provider/live calls, public-sync, raw
credential handling, runtime queues, schedulers, worker daemons, provider
ranking, production readiness, public readiness, or external-facing readiness.

Execution authority is limited to:

`docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T3A_LOCAL_WORKSPACE_RUNTIME_MCP_MODEL_GATEWAY_EXECUTE_PREVIEW_FOR_CODEX_2026-06-19.md`

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | AUTHORIZE |
| Baseline | `7879f23f` |
| Proposed tranche | WWU-T3A Local Workspace Runtime MCP Model Gateway Execute Preview |
| Worker | Codex |
| Commit mode | `WORKER_MAY_COMMIT` |
| Reviewer/closer | Codex single-agent multi-role with operator escalation |
| targetLayer | `CVF_LOCAL_WORKSPACE_RUNTIME` |
| runtimeMode | `RUNTIME_IMPLEMENTATION_REQUESTED` |
| MCP tool name | `cvf_model_gateway_execute_preview` |
| Model Gateway method | `execute` |
| Provider/live authorization | Not authorized |
| Public-sync authorization | Not authorized |

## Source Authority

| Source | Role |
|---|---|
| `CVF_SESSION_MEMORY.md` | current next allowed move and operator checkpoint source |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | machine-readable active session source |
| `AGENT_HANDOFF_V19_2026-06-15.md` | active handoff and handoff contract local view |
| `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | WWU tranche authority |
| `docs/reference/agent_workspace/README.md` | stable workspace front door |
| `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | Web/runtime layer split |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | runtime expansion boundary |
| `docs/reference/mcp_gateway/README.md` | MCP gateway front door |
| `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md` | MCP-to-Model-Gateway bridge boundary |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | MCP server tool registration source |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | Model Gateway execution bridge source |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | Model Gateway execute/error contract source |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Active next move required explicit runtime/MCP authorization before WWU-T3. | `CVF_SESSION_MEMORY.md` | `## Next Allowed Move` | `WWU-T3 Local Workspace Runtime/MCP` | active session front door | ACCEPT |
| Operator supplied explicit runtime/MCP authorization after next-roadmap checkpoint. | canonical-contract:operator-current-request-2026-06-19 | operator message | `LAM DI` | operator authorization | ACCEPT |
| WWU roadmap parks WWU-T3 until explicit runtime/MCP authorization. | `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | `## Tranche Plan` | `WWU-T3` | WWU roadmap | ACCEPT |
| Two-layer standard defines Local Workspace Runtime as MCP/CLI/guard execution substrate. | `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | `## CVF Local Workspace Runtime` | `CVF_LOCAL_WORKSPACE_RUNTIME` | two-layer standard | ACCEPT |
| Runtime expansion work must include Runtime Expansion Control Block. | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | `## Required Runtime-Readiness Fields` | `Runtime Expansion Control Block` | runtime expansion contract | ACCEPT |
| MCP bridge boundary requires exact MCP tool name and request/response mapping before implementation. | `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md` | `## Required Bridge Control Fields` | `MCP tool name` | MCP bridge boundary | ACCEPT |
| MCP bridge boundary recommends first executable bridge as a single narrow preview tool. | `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md` | `## Boundary Decision` | `cvf_model_gateway_execute_preview` | MCP bridge boundary | ACCEPT |
| MCP server registers tools with `server.tool(...)`. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | source symbols | `tool` | MCP server entry point | ACCEPT |
| Model Gateway exposes `GatewayExecuteRequest`, `GatewayExecuteResponse`, and `GatewayErrorEnvelope`. | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | source symbols | `GatewayExecuteRequest`; `GatewayExecuteResponse`; `GatewayErrorEnvelope` | unified gateway interface contract | ACCEPT |
| Model Gateway ProviderExecutionBridge exposes `execute(request)`. | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | source symbol | `ProviderExecutionBridge` | provider execution bridge | ACCEPT |

## Authorized Changes

WWU-T3A execution may edit:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute-preview.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute-preview.test.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package-lock.json`
- `docs/reviews/CVF_WWU_T3A_LOCAL_WORKSPACE_RUNTIME_MCP_MODEL_GATEWAY_EXECUTE_PREVIEW_COMPLETION_2026-06-19.md`
- `docs/reviews/evidence/wwu-t3a-local-workspace-runtime-mcp-model-gateway-execute-preview-2026-06-19.json`
- `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md`

Dispatch-only authoring may also edit:

- this GC-018 baseline;
- `docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T3A_LOCAL_WORKSPACE_RUNTIME_MCP_MODEL_GATEWAY_EXECUTE_PREVIEW_FOR_CODEX_2026-06-19.md`;
- `docs/corpus-intelligence/registry/entries/wwu-t3a-local-workspace-runtime-mcp-model-gateway-execute-preview.json`;
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`.

## Required Runtime Boundary

The implementation must:

- expose only `cvf_model_gateway_execute_preview`;
- map a narrow request to `GatewayExecuteRequest`;
- return either `GatewayExecuteResponse` or `GatewayErrorEnvelope` plus
  receipt metadata;
- use deterministic/local preview execution only;
- keep raw credential values outside MCP input and output;
- keep provider/live calls forbidden.

## Forbidden Scope

WWU-T3A must not:

- implement broad MCP gateway functionality;
- add runtime queues, queue records, schedulers, or worker daemons;
- run provider/live calls or consume secrets/quota;
- accept raw API keys, authorization headers, or secret material through MCP;
- return raw keys, authorization headers, or secret values from MCP;
- mutate `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json` or its source fragments;
- public-sync;
- import raw external workspace package code;
- claim runtime enforcement beyond this deterministic preview tool;
- claim production readiness, public readiness, release-facing readiness, or external-facing readiness.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | One MCP tool candidate `cvf_model_gateway_execute_preview` is registered or exposed through the MCP server path. |
| AC2 | Tool input maps to source-verified `GatewayExecuteRequest` fields. |
| AC3 | Tool output maps to `GatewayExecuteResponse` or `GatewayErrorEnvelope` and includes receipt evidence without raw secrets. |
| AC4 | Focused tests cover success, policy denial, invalid request, and secret-safety behavior. |
| AC5 | MCP package typecheck/build and focused tests pass. |
| AC6 | Model Gateway checks remain passing if the implementation imports or exercises Model Gateway runtime source. |
| AC7 | Completion records no provider/live/public-sync/readiness/runtime-queue claim. |

## Evidence / Verification

Required before WWU-T3A closure:

- `git rev-parse --short HEAD`;
- `git status --short`;
- source-symbol re-verification using `rg -n`;
- MCP focused tests;
- MCP build or typecheck;
- Model Gateway `npm run check` and focused tests if the implementation imports Model Gateway source;
- `git diff --check`;
- `python governance/compat/run_worker_return_fast_gate.py`;
- committed-range `pre-closure` on the material range.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Local Runtime/MCP dispatch. No public-sync batch is
authorized.

## Claim Boundary

This GC-018 authorizes only WWU-T3A dispatch for one deterministic MCP Model
Gateway execute preview. It does not authorize provider/live calls, public-sync,
runtime queues, schedulers, worker daemons, raw credential handling, broad MCP
gateway implementation, production readiness, public readiness, release-facing
readiness, or external-facing readiness.
