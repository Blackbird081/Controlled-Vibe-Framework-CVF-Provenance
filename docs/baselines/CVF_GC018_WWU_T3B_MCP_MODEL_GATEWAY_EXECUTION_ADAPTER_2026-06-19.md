# CVF GC-018 - WWU-T3B MCP Model Gateway Execution Adapter

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-19

docType: gc018_baseline

## Purpose

Authorize one bounded Local Workspace Runtime tranche that replaces preview-only
compatibility with an injectable MCP adapter calling the existing Model Gateway
`ProviderExecutionBridge.execute` contract.

## Authorization

The operator instructed Codex on 2026-06-19 to complete the MCP-to-Model-Gateway
module when conditions are sufficient. Source audit found the module adapter is
ready. Provider/live composition remains separately controlled by secret, quota,
endpoint, and diagnostic requirements.

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| WWU-T3 is open as narrow runtime/MCP tranches. | `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | `## Tranche Plan` | `WWU-T3` | WWU roadmap | ACCEPT |
| T3A closed as deterministic preview only. | `docs/reviews/CVF_WWU_T3A_LOCAL_WORKSPACE_RUNTIME_MCP_MODEL_GATEWAY_EXECUTE_PREVIEW_COMPLETION_2026-06-19.md` | `## Claim Boundary` | `cvf_model_gateway_execute_preview` | T3A completion | ACCEPT |
| MCP tools use a registration surface. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | current source | `tool` | MCP server | ACCEPT |
| Existing MCP execution roles include OPERATOR, ORCHESTRATOR, and AI_AGENT. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | D3 role boundary | `D3_ALLOWED_ROLES` | MCP D3 bridge | ACCEPT |
| Gateway execution requires traceId, prompt, policy, and optional routing/metadata. | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | `GatewayExecuteRequest` | `GatewayExecuteRequest` | unified gateway interface | ACCEPT |
| Bridge execution returns response/error plus receipt. | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | `ProviderExecutionBridgeResult` | `ProviderExecutionBridgeResult` | provider execution bridge | ACCEPT |
| ProviderExecutionBridge owns async execute(request). | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | `ProviderExecutionBridge` | `execute` | `ProviderExecutionBridge` | ACCEPT |
| Raw secrets resolve behind CredentialBoundary. | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | `CredentialBoundary` | `resolveSecretForRuntime` | `CredentialBoundary` | ACCEPT |
| Runtime expansion requires an explicit control block. | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | `## Required Runtime-Readiness Fields` | `Runtime Expansion Control Block` | runtime expansion contract | ACCEPT |

## Authorized Changes

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.test.ts`
- `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md`
- matching completion, evidence, GC-051 source entry, generated registry, this
  baseline, and matching work order

## Required Runtime Boundary

The adapter calls an injected executor whose `execute(request)` surface is
structurally compatible with `ProviderExecutionBridge.execute`. It maps current
`GatewayExecuteRequest` fields, preserves response/error and receipt, rejects
unauthorized roles and credential-bearing input, and fails closed without an
executor.

## Decision / Baseline / Proposed Tranche

Decision: dispatch WWU-T3B as one injectable execution-adapter tranche.
Baseline: T3A proves preview mapping but does not call an executor. Proposed
tranche: call a supplied executor through the current source-compatible method,
with fail-closed validation and no live composition.

## Forbidden Scope

- No provider/live or network call, API-key read, or quota consumption.
- No raw credential value in MCP input or output.
- No concrete provider adapter composition inside the MCP package.
- No cross-package source import that breaks independent MCP build.
- No queue, scheduler, daemon, workspace-state mutation, Web UI, public-sync,
  or readiness claim.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | `cvf_model_gateway_execute` is registered through the MCP server. |
| AC2 | Valid authorized input calls the injected executor exactly once with a source-compatible request. |
| AC3 | Response/error and receipt are preserved without raw secrets. |
| AC4 | Unauthorized role, raw credential input, invalid schema, and absent executor fail closed. |
| AC5 | Focused MCP tests/build and Model Gateway checks pass. |
| AC6 | Closure makes no provider/live/public/runtime-enforcement/readiness claim. |

## Evidence / Verification

Required evidence is focused MCP tests, MCP build, Model Gateway check and
bridge tests, exact changed-set diff/status output, reviewer-fast, steward,
pre-closure, and split pre-push gates.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime adapter; no public-sync authorization.

## Claim Boundary

This GC-018 authorizes an injectable module-level MCP execution adapter only.
It does not authorize live provider composition, secrets/quota use, public-sync,
runtime queues, or production/public/release readiness.
