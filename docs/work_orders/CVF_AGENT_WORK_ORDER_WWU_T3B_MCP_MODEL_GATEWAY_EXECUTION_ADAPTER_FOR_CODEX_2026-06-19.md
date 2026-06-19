# CVF Agent Work Order - WWU-T3B MCP Model Gateway Execution Adapter For Codex

Memory class: FULL_RECORD

Status: DISPATCHED

Date: 2026-06-19

docType: work_order

Batch ID: WWU-T3B

Owner: Codex worker; Codex reviewer/closer

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `cf76e3e2`

executionBaseHead: `cf76e3e2`

closureBaseHead: `cf76e3e2`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Role: Codex implementer/reviewer/closer under single-agent multi-role control.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T3B_MCP_MODEL_GATEWAY_EXECUTION_ADAPTER_FOR_CODEX_2026-06-19.md`

Commit mode: `WORKER_MAY_COMMIT`.

Base: dispatchBaseHead `cf76e3e2`. Align executionBaseHead and closureBaseHead
to the committed dispatch head before implementation.

Current-time notes: T3A is closed preview-only. The operator authorized
continuation where prerequisites are sufficient. Source audit permits an
injectable module adapter but not live provider composition.

Do-not-misread notes: no provider/live proof, secret handling, public-sync,
queue/scheduler/daemon work, Web UI, broad MCP readiness, or readiness claim.

Required first actions: read startup continuity, this work order and GC-018,
WWU roadmap, workspace/MCP front doors, runtime expansion contract, MCP bridge
boundary, MCP registration source, GatewayExecuteRequest,
ProviderExecutionBridge, and CredentialBoundary.

Return contract: close only after focused tests, package checks, governance
gates, exact changed-set evidence, and explicit bounded claims.

## Purpose

Implement `cvf_model_gateway_execute` as a bounded MCP adapter that calls an
injected executor structurally compatible with `ProviderExecutionBridge.execute`.

## Scope / Target / Owner Boundary

Target: MCP tool registration, one pure adapter module, and focused tests under
`EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER`.

Model Gateway owns routing, credentials, provider adapters, execution, errors,
and receipts. The MCP package owns input validation and tool output. This
tranche does not compose a live executor.

Risk ceiling: R2, with no network, secret, queue, or public action.

## Intake Role Routing Decision

intake summary: operator authorized completion where prerequisites are met.

scope classification: bounded Local Workspace Runtime/MCP module adapter.

risk sensitivity: R2; provider/live and secret use forbidden.

selected role route: `SINGLE_AGENT_MULTI_ROLE`

role separation basis: dispatch, material closure, and session-sync use
separate commits and ranges.

escalation condition: live provider composition, quota/secret use, public-sync,
executable queues, broader enforcement, or readiness claims.

## Agent Roles

| Role | Actor | Responsibility |
|---|---|---|
| Dispatcher | Codex | Author and verify dispatch packet |
| Worker | Codex | Implement adapter and tests |
| Reviewer / closer | Codex | Review diff, run gates, close material |
| Session-sync actor | Codex | Update continuity in a separate commit |
| Operator | Human | Authorize forbidden scope expansion |

## Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator authorization | current request on 2026-06-19 | ACCEPTED for bounded completion where prerequisites are met |
| Active session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | T3A closed; broader T3 needs fresh GC-018/work order |
| WWU roadmap | `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | T3 split into narrow tranches |
| GC-018 | `docs/baselines/CVF_GC018_WWU_T3B_MCP_MODEL_GATEWAY_EXECUTION_ADAPTER_2026-06-19.md` | DISPATCH_READY |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| Applicability | applies because route is `SINGLE_AGENT_MULTI_ROLE` |
| actor | Codex |
| role set | dispatcher, worker, reviewer, closer, session-sync actor |
| Role separation ledger | dispatch, material closure, and session-sync commits remain separate |
| Evidence basis independent of memory | source, diffs, tests, commands, completion packet |
| Gate sequence | pre-dispatch; pre-implementation; tests; pre-closure; session-sync; pre-push |
| Self-review boundary | closure requires exact changed-set and command evidence |
| escalation condition | forbidden scope or claim expansion |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex worker; Codex reviewer/closer; Codex session-sync actor |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=cf76e3e2`; execution/closure align to committed dispatch head |
| changedSetScope(phase) | dispatch files; named MCP/closure files; protected continuity only in session-sync |
| traceScope(phase, actor) | exact changed set for each separate phase range |
| commitOwner(phase) | Codex |
| crossBatchIsolation | clean worktree required before each phase |
| nextMoveSurfaces | update only following accepted material commit in separate session-sync |
| Closer designation | Codex |

## Workspace Two-Layer Control Block

| Field | Disposition |
|---|---|
| targetLayer | `CVF_LOCAL_WORKSPACE_RUNTIME` |
| operatorSurface | N/A with reason: no Web UI |
| agentExecutionSurface | injectable MCP execution adapter |
| sourceOfTruth | Model Gateway contracts and governed artifacts |
| mutationBoundary | one adapter and registration only |
| receiptBoundary | preserve executor-owned receipt |
| forbiddenConflationCheck | module execution does not prove live provider or broad runtime readiness |

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | Add bounded agent-facing MCP ingress to the execution contract |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md`; `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | MCP runtime source/test and dated completion/evidence |
| Handoff fields | AHB block above |
| State ownership | no workspace state mutation |
| Guard owner | handoff, workspace, AOT, dispatch, package tests/build |
| Build boundary | MCP adapter only; Web source: no; queue runtime: no; provider proof: no; public-sync: no; registry edits: GC-051 source and generated aggregate only |

## Runtime Expansion Control Block

| Field | Disposition |
|---|---|
| runtimeMode | `RUNTIME_IMPLEMENTATION_REQUESTED` |
| contractSource | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` |
| frontDoor | `docs/reference/agent_workspace/README.md` |
| stateSourceOfTruth | N/A with reason: no workspace state mutation |
| queueBoundary | N/A with reason: no queue, scheduler, or daemon |
| operatorViewBoundary | N/A with reason: no Web UI |
| providerBoundary | no-provider-live; injected deterministic executor tests only |
| publicBoundary | private-only; no public-sync |
| guardOwner | workspace runtime boundary guard and focused package checks |

## MCP Model Gateway Bridge Control Block

| Field | Disposition |
|---|---|
| MCP tool name | `cvf_model_gateway_execute` |
| MCP role boundary | allow `OPERATOR`, `ORCHESTRATOR`, `AI_AGENT`; reject others before execution |
| Model Gateway method | `ProviderExecutionBridge.execute` |
| Request schema | traceId, prompt, optional systemPrompt, policy/routing fields, optional metadata |
| Response schema | executor response/error and receipt in a secret-safe MCP envelope |
| Credential boundary | reject credential-bearing keys; composition remains outside MCP input |
| Provider selection boundary | optional preferred provider/model only; no ranking or registry mutation |
| Receipt boundary | preserve executor receipt without adding credentials |
| Live-run boundary | no live provider composition or network call |
| Public/export boundary | private provenance only |

## Foundation Storage Layout Block

Use existing baseline, work-order, review, GC-051, and MCP source/test folders.
No new stable folder or archive move.

## Worker Autonomy / No-Question Rule

Codex must repair allowed-scope gate failures and rerun them. Ask the operator
only when a repair requires forbidden paths, provider/live proof, secret/quota
use, public-sync, queue execution, destructive action, or claim expansion.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact:
`docs/reviews/CVF_WWU_T3A_LOCAL_WORKSPACE_RUNTIME_MCP_MODEL_GATEWAY_EXECUTE_PREVIEW_COMPLETION_2026-06-19.md`

freshRecomputeRequired: YES

recomputeReason: a new runtime adapter and registration are introduced.

unicodePathHandling: repo-relative paths; authored files remain ASCII.

## Required First Reads

- startup continuity files and active handoff
- this work order and matching GC-018
- WWU roadmap and workspace/MCP front doors
- runtime expansion and MCP bridge contracts
- source files named below

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| WWU-T3 is open as narrow tranches. | `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | `## Tranche Plan` | `WWU-T3` | WWU roadmap | ACCEPT |
| T3A is preview-only. | `docs/reviews/CVF_WWU_T3A_LOCAL_WORKSPACE_RUNTIME_MCP_MODEL_GATEWAY_EXECUTE_PREVIEW_COMPLETION_2026-06-19.md` | `## Claim Boundary` | `cvf_model_gateway_execute_preview` | T3A completion | ACCEPT |
| MCP execution roles include OPERATOR, ORCHESTRATOR, AI_AGENT. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | D3 source | `D3_ALLOWED_ROLES` | MCP server | ACCEPT |
| Execute request fields are source-defined. | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | `GatewayExecuteRequest` | `GatewayExecuteRequest` | unified gateway interface | ACCEPT |
| Bridge result owns response/error and receipt. | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | `ProviderExecutionBridgeResult` | `ProviderExecutionBridgeResult` | provider execution bridge | ACCEPT |
| Provider bridge owns async execute(request). | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | class source | `execute` | `ProviderExecutionBridge` | ACCEPT |
| Runtime secrets stay behind CredentialBoundary. | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | class source | `resolveSecretForRuntime` | `CredentialBoundary` | ACCEPT |
| MCP boundary forbids raw API-key input. | `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md` | `## Forbidden Scope` | `Raw API-key input through MCP request bodies` | MCP bridge boundary | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Worker deliverable | Verification | Status |
|---|---|---|---|---|
| Narrow WWU-T3 tranche | Purpose and boundaries | one adapter | diff review | PASS |
| Fresh GC-018/source verification | Authority and source blocks | dispatch packet | pre-dispatch | PASS |
| Web/runtime separation | Two-Layer block | no Web edits | changed set | PASS |
| Model Gateway ownership | MCP Bridge block | injected executor port | tests | PASS |
| No live/public/readiness claim | Claim Boundary | deterministic tests | completion | PASS |

## Write Ownership

Allowed scope:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.test.ts`
- `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md`
- this work order, matching baseline, completion/evidence, and GC-051 entry/aggregate

Forbidden paths: Web UI, workspace state, runtime queues, provider registry or
credentials, public-sync clone, and unrelated sources.

## Execution Plan

1. Align committed execution base and re-verify symbols.
2. Implement executor port, pure handler, and fail-closed registration.
3. Test success/error, role/secret/schema/executor rejection, and exception shielding.
4. Run MCP tests/build and Model Gateway checks.
5. Close roadmap/work order/evidence/registry and governance gates.

## Pre-Flight Checks

- worktree clean at dispatch base;
- source symbols re-verified;
- fresh GC-018 and work order present;
- pre-dispatch and dispatch steward pass;
- execution base aligned to committed dispatch head before source edits.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | MCP registers `cvf_model_gateway_execute`. |
| AC2 | Authorized input calls injected executor once with compatible fields. |
| AC3 | Executor response/error and receipt remain intact. |
| AC4 | Role, secret, schema, missing-executor, and thrown-executor paths fail closed. |
| AC5 | Package checks and governance gates pass. |
| AC6 | No provider/live/public/queue/readiness action or claim. |

## Evidence Requirements

Source search, focused tests/build, Model Gateway checks, diff/status evidence,
reviewer-fast, steward, pre-closure, split pre-push, completion, and JSON digest.

## Review Gate

Fail closure for secret echo, unauthorized execution, network call,
cross-package source import, missing receipt propagation, test/build failure,
scope drift, stale roadmap state, or readiness claim.

## Return-To-Orchestrator Conditions

Return blocked if runtime composition requires provider endpoint, secret, quota,
new package topology, queue execution, public-sync, or claim expansion.

## Operator Checkpoint

No checkpoint is required for allowed-scope implementation. Provider/live
composition, secret/quota use, public-sync, queue execution, or readiness
claims require a new operator checkpoint and fresh governed tranche.

## Closure Checklist

| Item | Dispatch state |
|---|---|
| Source Verification Block recomputed | PASS |
| Fresh GC-018 | PASS |
| Dispatch Prompt Envelope first | PASS |
| Required control blocks | PASS |
| Runtime implementation | OPEN |
| Focused verification | OPEN |
| Completion/evidence/registry | OPEN |
| Closure/pre-push gates | OPEN |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime adapter; no public-sync authorization.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `RUNTIME_SIGNAL_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `DISPATCHED_BOUNDED` |
| Next control action | prove module adapter before live composition |
| Worker blame | N/A with reason: intentional preview-to-execution module gap |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-19 WWU-T3B dispatch |
| Working directory | repository root |
| Command or tool surface | PowerShell, rg, apply_patch, governance gates |
| Target paths | Allowed scope above |
| Allowed scope source | this work order and GC-018 |
| Before status evidence | clean worktree at `cf76e3e2` |
| After status evidence | dispatch gate output |
| Diff evidence | dispatch range diff |
| Approval boundary | bounded module adapter |
| Claim boundary | no provider/live/secret/public/queue/readiness claim |
| Agent type | Codex |
| Invocation ID | `wwu-t3b-mcp-model-gateway-execution-adapter-dispatch-codex-2026-06-19` |
| Expected manifest | baseline; work order; roadmap; GC-051 source and aggregate |
| Actual changed set | baseline; work order; roadmap; GC-051 source and aggregate |
| Manifest delta | MATCH |

## Claim Boundary

WWU-T3B may close only an injectable MCP adapter calling the Model Gateway
execution contract. It does not authorize or prove provider network behavior,
credential/quota use, queues, broad runtime enforcement, public-sync, or
production/public/release/external-facing readiness.
