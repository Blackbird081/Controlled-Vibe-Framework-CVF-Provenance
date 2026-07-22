# CVF External Agent Invocation Control Knowledge Gap And Source Acquisition Map

Status: ACTIVE_REFERENCE

Memory class: FULL_RECORD

docType: reference

Date: 2026-07-22

Batch ID: CVF-EAIC-KR-T0

executionBaseHead: `1e689ed52`

## Purpose

Map current CVF-governed authority for external-agent CLI/MCP invocation
control against the nine knowledge domains named in
`docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md`,
classify each domain into one terminal state, and produce a bounded,
operator-reviewable source-acquisition manifest for every non-owned domain.
This map does not fetch missing knowledge, does not design an
implementation, and does not lift the active global execution moratorium.

## Scope / Applies-To

Applies to repository-local, non-archive CVF source, reference, audit,
roadmap, and review surfaces read between 2026-07-22 dispatch HEAD
`969acaa32` and worker execution HEAD `1e689ed52`. Read-only `rg`,
PowerShell, Git, and Python governance checks were used. No agent CLI, MCP
tool/server, provider/API, API key, account subscription, browser, network
service, external search, or external-repository clone was invoked.

Does not apply to external primary-source acquisition, architecture
ratification, or implementation; those remain gated behind T1-T5 of the
parent roadmap and a fresh operator decision.

## Findings / Position

Position: `READY_FOR_OPERATOR_SOURCE_SELECTION`.

Every one of the nine roadmap domains has one terminal authority disposition
below, every non-owned row carries an exact unresolved question, required
primary-source class, acquisition priority, and operator checkpoint, and no
domain required treating an external proposal or provider-local memory as
CVF authority. The predecessor audit's `CONTROL_NOT_EFFECTIVE_FOR_EXTERNAL_AGENT_CLI`
position and `GLOBAL_ROADMAP_EXECUTION_MORATORIUM_ACTIVE` decision remain
unchanged and are reconfirmed by this map, not superseded by it.

### Authority Ledger

For every candidate source below: exact repo-relative path and
section/symbol, owner surface, authority class, access-mode applicability,
supported claim, and overlap with an existing owner. Authority class values
used are `DIRECT` (the source itself is the CVF-owned control surface),
`ADVISORY` (the source is explicit non-enforcing evidence), `EVIDENCE_ONLY`
(the source records an incident or observation, not a control), and
`NOT_CVF_SOURCE` (external material, retained as design input only).

| Source path and symbol | Owner surface | Authority class | Access modes | Supported claim | Prohibited inference | Overlap |
| --- | --- | --- | --- | --- | --- | --- |
| `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`, lane `EVIDENCE_TO_OPERATOR_SURFACE` (`currentPosture: PARTIAL`) | system-chain map | DIRECT | local process (CVF governance CLI/hook readout) | CVF's own checker/hook/readout visibility to the operator is partial | Do not read this lane as proof of external-agent CLI control | none; single owner |
| `docs/reference/system_chain/gaps/entries/gc009_gc010_no_production_caller.json` (GC-009/GC-010; `targetOwner: NONE_WITH_REASON`, `currentStatus: IMPLEMENTED_NOT_INVOCATION_PROVEN`) | system-chain GAP index | DIRECT | local process | `MandatoryGateway` (`EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts`) and `AgentExecutionRuntime` (`EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts`) have no non-test, non-type-only production caller | Do not infer either is wired to an external-agent admission path | none; single owner |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/orchestration.contract.ts`, `TaskAssignment` (`dependencies`, `executionAuthorizationHash`) and `OrchestrationResult` (`orchestrationHash`) | Control Plane orchestration contract | DIRECT | local process | Deterministic assignment/dependency/hash typing exists | No process identity, spawn, streaming monitor, or kill owner is present in this file | none; single owner |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` (header: "Local execution-plane module only; no CLI/MCP/UI/runtime caller."; `recordTimeout()` reads durable state via `resumeRun` then `checkTimeout(startedAt, ceilingMs)`) | MAO operational worker launcher | DIRECT (self-declared boundary) | local process, injected adapter | Execution is through an injected adapter, not a CLI/MCP/UI/runtime caller; timeout is computed post hoc from durable state, not a live interrupt | Do not read a recorded timeout as evidence of in-flight process termination | none; single owner; also named in `docs/baselines/CVF_GC018_MAO_OA_T3_OPERATIONAL_WORKER_LAUNCHER_AND_LIVENESS_WIRING_2026-07-17.md` |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.invocation.contract.ts`, `MCPInvocationContract.invoke(request, status, responsePayload)` (hashes via `computeDeterministicHash(..., status, request.toolArgs)`) | MCP invocation contract | DIRECT | MCP adapter (caller-supplied payload) | `invoke()` hashes the request plus caller-supplied status and payload into a deterministic receipt | Do not read this hash as evidence the contract executed, monitored, or terminated an MCP process | none; single owner. Location differs from the audit's implied `CVF_ECO_v2.5_MCP_SERVER` path; this is a path refinement, not a contradiction, since the audit did not commit to an exact file |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.invocation.consumer.pipeline.contract.ts`, `MCPInvocationConsumerPipelineRequest` (caller-supplied `invocationRequest`, `invocationStatus`, `responsePayload`) composed with `ControlPlaneConsumerPipelineContract` | MCP consumer pipeline | DIRECT | MCP adapter (caller-supplied payload) | Composes the invocation receipt with caller-supplied results into `MCPInvocationConsumerPipelineResult` | Do not read composition as independent verification of the caller-supplied payload | none; single owner |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/generic-agent-adapter.ts` (header: "advisory only ... does not execute governance checks or spawn agent processes"; `runtimeAdapterAuthorized: false`) | MCP generic-agent adapter | ADVISORY | MCP adapter | The adapter is explicitly advisory-only and never authorizes runtime execution | Do not treat `runtimeAdapterAuthorized: false` as a temporary or configurable state; it is a fixed advisory boundary in current source | none; single owner |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` (`spawn(request.executable, ..., { shell: false, detached: false, ... })`; `setTimeout(() => { timedOut = true; child.kill(); }, request.timeoutMs)`; `DEFAULT_COMMAND_TIMEOUT_MS = 600000`) | Governed command launcher | DIRECT | local process | This is a real `spawn()` owner limited to static allowlisted profiles, with child-only `kill()` on timeout | Do not read `child.kill()` as descendant/process-tree termination proof; `detached: false` alone does not establish tree-kill semantics | none; single owner |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` (`ProviderRecord`; `ProviderRegistry`) | Model Gateway provider registry | DIRECT | local process, provider adapter | Provider records, models, status, and capabilities are owned here | Do not create a parallel provider registry | subordinate component of the provider/model roadmap |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` (`PROVIDER_CAPABILITY_REGISTRY`) | Model Gateway capability registry | DIRECT | local process | Capability records exist per provider/model | same | subordinate component of the provider/model roadmap |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts` (`DynamicModelRecord`; `DynamicModelRegistryContract`; `FindOptimalQuery`) | Model Gateway dynamic model registry | DIRECT | local process | Provider/model identity, capability, tier, cost, latency, rate-limit, health metadata exist | same | subordinate component of the provider/model roadmap |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` (`GatewayReceiptInput`; `GatewayReceiptBuilder`; `requestedModelId`; `selectedModelId`; `fallback`) | Model Gateway receipt | DIRECT | local process | Requested/selected model, provider, decision, and fallback receipt fields exist | Do not read this receipt as proof of actual external-agent process identity | subordinate component of the provider/model roadmap |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` (`CredentialReference`; `CredentialMetadata`; `source` field environment-only) | Model Gateway credential boundary | DIRECT | environment key only (current) | Secret-safe environment-backed credential references exist | Do not infer account-subscription credential support exists yet | subordinate component of the provider/model roadmap |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/fallback-policy.ts` (`FallbackPolicyConfig`; `FallbackDecision`; default `maxAttempts` up to three) | Model Gateway fallback policy | DIRECT | local process | A bounded local attempt count exists | Do not read this as a cross-caller cumulative operator envelope | subordinate component of the provider/model roadmap |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` (`ProviderExecutionBridge.execute`; failure tokens `credential_shielded`, `quota_exceeded`, `provider_unavailable`; `this.quota.canUse(...)` checked before adapter call) | Model Gateway execution bridge | DIRECT | provider adapter using the current environment-backed credential boundary | Quota/health/credential checks occur before adapter use; usage is recorded after successful adapter return | Do not infer current account-subscription support or read this as an in-flight, mid-loop stop for an external-agent CLI process; it is request-level, not agent-loop-level | subordinate component of the provider/model roadmap |
| `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` cited path | live-run diagnostic standard | EVIDENCE_ONLY (path drift) | N/A | Several other current governed root-level and roadmap files cite this standard at an un-archived path (not itself CVF source-authority evidence for this domain), but the file now physically resides only at `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`, whose internal `Status:` line still reads `ACTIVE STANDARD` | Do not treat the archived location as evidence the standard is retired; do not treat the un-archived citation path as a confirmed live file without rechecking at time of use | citation-path drift; not a T0 domain finding, recorded here as a source-fidelity caveat for any later tranche that cites this standard |
| `.private_reference/legacy/CVF_MCP 20.07/De_xuat_xay_dung_CVF_MCP.md`, already absorbed by the predecessor audit's Selective Absorption Record | external MCP/CLI architecture proposal | NOT_CVF_SOURCE | N/A | The audit already selectively adapted useful design patterns (layered transport/policy/execution separation, one-core/two-surface projection) and rejected unsupported claims (absolute MCP compliance, prompt-injection prevention, fixed token multiplier) | Do not re-read or re-cite this file as new authority; reuse only the audit's already-recorded ledger | fully reconciled by the predecessor audit; this map does not reopen it |
| `docs/roadmaps/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_ASSIGNMENT_AND_INVOCATION_RECEIPT_ROADMAP_2026-07-20.md`, top-level `Status:` | provider/model roadmap | DIRECT (VALUE_SET) | N/A | `PARKED_BY_GLOBAL_CLI_MCP_INVOCATION_CONTROL_REASSESSMENT`; explicitly superseded for execution by the predecessor audit | Do not treat any of its proposed contract-group fields (A-D) as existing runtime fields; every one is `DOC_ONLY_NEW` per its own Source Verification Block unless separately mapped | subordinate to priority 1 per the parent roadmap's Operator Decision And Priority Register |

## Knowledge Gap And Source Acquisition Map

Nine domains from `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md`
Knowledge Domain Matrix. Each row has exactly one terminal state:
`OWNED`, `PARTIAL`, `OPAQUE_BY_ACCESS_MODE`, or `MISSING_PRIMARY_SOURCE`.

| # | Domain | Terminal state | Owned/partial evidence | Unresolved question | Why current evidence is insufficient | Required primary-source class | Acquisition priority | Operator checkpoint | Blocked architecture decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Launch admission | `MISSING_PRIMARY_SOURCE` | GC-009/GC-010 confirm `MandatoryGateway`/`AgentExecutionRuntime` have no non-test production caller; `operational.worker.launcher.ts` self-declares no CLI/MCP/UI/runtime caller | Which CVF component, if any, is meant to approve or deny an external-agent CLI/MCP launch before it starts? | No source names an admission-check owner for an external-agent launch; existing owners explicitly disclaim the caller role | primary design decision record or provider/runtime capability documentation describing available pre-launch hook points for the target agent CLI/MCP host | CRITICAL | operator must select which agent CLI/MCP host(s) are in scope before an admission owner can be designed | T3 owner-architecture selection cannot start |
| 2 | Process identity | `MISSING_PRIMARY_SOURCE` | `orchestration.contract.ts` provides `TaskAssignment`/`OrchestrationResult` hash typing only; gateway receipt provides requested/selected model fields only | How are caller, OS process, descendant processes, task assignment, and receipt bound into one verifiable identity chain? | No source binds a process tree to an assignment receipt; hash contracts exist without a process-identity field | provider/runtime documentation on process/session identifiers exposed by the target agent CLI/MCP host, plus an operator decision on what identity model CVF should adopt | CRITICAL | operator must confirm whether identity binding is expected per-process, per-session, or per-account before design | T2 identity reconciliation fields cannot be ratified |
| 3 | Cancellation and termination | `PARTIAL` | `governed-command-launcher.ts` proves a real `spawn()` plus `child.kill()` on timeout with `detached: false`; `operational.worker.launcher.ts` proves timeout is read from durable state, not a live interrupt | What semantics apply to graceful cancel, timeout, and full descendant-tree termination for an external-agent CLI/MCP process specifically (not the static command-launcher profile)? | Only a narrower, statically-profiled command launcher has real spawn/kill evidence; no source proves descendant-tree kill or applies this launcher to an agent CLI/MCP process | direct test or documentation evidence of the target agent CLI/MCP host's process-tree shape and its cancellation/kill API or signal contract | HIGH | operator must approve a bounded, disposable test plan before any termination behavior is exercised against a real agent process | T2/T3 termination semantics cannot be ratified beyond the already-owned static launcher |
| 4 | Usage telemetry | `OPAQUE_BY_ACCESS_MODE` | Provider execution bridge records usage after successful adapter return (request-level); operator UI-snapshot evidence exists only as incident evidence in the provider/model roadmap, not as a machine-readable source | Which token, turn, tool, quota, spend, and latency signals are actually observable, and at what access mode (API key vs. account subscription vs. opaque provider session)? | UI percentage snapshots, JSONL token counts, and billed API cost are three distinct measurement classes with no current reconciliation owner; subscription-session usage is not machine-observable in current source | provider-published API/telemetry documentation per access mode, and an operator-supplied reconciled sample linking UI snapshot to JSONL to billed cost for the same session | CRITICAL | operator must decide whether unmeasurable access modes (opaque subscription session) are permitted at all under a fail-closed policy | T2 usage-measurement class field cannot be ratified for opaque access modes |
| 5 | Cumulative budget | `MISSING_PRIMARY_SOURCE` | `fallback-policy.ts` bounds local retry attempts (default up to three); provider execution bridge checks quota before adapter use, not during an in-flight loop | Which owner enforces one envelope across retry, resume, fallback, and subagents for a single operator-approved assignment? | No source aggregates cost/quota/time across an entire external-agent CLI/MCP session, only per-request local counters | operator-approved envelope design document (T1/T2 target) informed by provider quota/billing documentation for each access mode | CRITICAL | operator must approve the envelope's scope (single task vs. session vs. account) before ratification | T1 approval-envelope schema and T2 budget-ceiling fields cannot be ratified |
| 6 | Unknown usage | `MISSING_PRIMARY_SOURCE` | No source defines fail-closed behavior when usage cannot be measured; the interim bounded-invocation profile in the provider/model roadmap is incident-response guidance, not a ratified control | What must fail closed when usage cannot be measured reliably (for example, an opaque subscription session with no live telemetry)? | The interim profile is explicitly recorded as incident evidence, not executable authority, and has no source-verified enforcement owner | operator decision record ratifying a fail-closed default plus provider documentation on which access modes can never expose usage | CRITICAL | operator must ratify the fail-closed default before any bounded live test is authorized again | T2 fail-closed disposition cannot be ratified; blocks T4 negative-proof plan |
| 7 | Bypass and threat surface | `MISSING_PRIMARY_SOURCE` | `generic-agent-adapter.ts` proves the MCP adapter path is advisory-only; no source enumerates shell, IDE, browser, plugin, subprocess, or provider-native bypass paths for an external-agent CLI/MCP host | Which shell, IDE, browser, plugin, subprocess, and provider-native invocation paths can evade any future mediation layer? | Only one advisory-only adapter boundary is documented; the predecessor audit records this as future work, not a completed threat model | dedicated threat-model working session using provider/runtime documentation for the target agent CLI/MCP host's full invocation surface (CLI flags, IDE extension points, MCP tool registration, subprocess spawning) | HIGH | operator must scope which hosts/products are in the threat-model boundary before the exercise starts | T3 owner-architecture selection cannot close without a threat model |
| 8 | Cost-aware task compilation | `MISSING_PRIMARY_SOURCE` | No source defines which governance checks, lint passes, or structural validations can run locally before a paid agent loop starts; F-08 in the predecessor audit records governance-input churn as a cost driver, not a compiled solution | Which work can be compiled and checked locally (deterministic, zero-provider-cost) before a paid agent loop is invoked? | This is design work not yet started; no owner surface performs pre-flight local compilation of governed-artifact requirements today | operator-approved design tranche scoping which checker/gate classes are safe to run fully local before any agent-loop invocation | MEDIUM | operator must decide whether this is in scope for T2/T3 or deferred to a later cost-economics roadmap | Blocks a design decision, not a runtime tranche; can be deferred without blocking T1-T2 |
| 9 | Reconciliation | `PARTIAL` | Gateway receipt provides requested-vs-selected model fields; MCP consumer pipeline composes caller-supplied invocation results into a receipt; no source joins approval, assignment, actual identity, usage, stop reason, and result into one reviewable chain | How do approval, assignment, actual identity, usage, stop reason, and result reconcile without relying on chat history or provider-local memory? | Reconciliation exists only for the narrower requested-vs-selected model pair; the provider/model roadmap's proposed Reviewer Reconciliation Decision (group D) is entirely `DOC_ONLY_NEW`, not implemented | T1-T2 ratified schemas for approval/assignment/invocation receipts, joined and tested against real reconciliation fixtures | HIGH | operator must approve the provider/model roadmap's T1 contract before reconciliation fields can be ratified | T2 reconciliation result field cannot be ratified until T1 approval/assignment schemas exist |

### Domain terminal-state summary

`OWNED`: 0. `PARTIAL`: 2 (cancellation/termination; reconciliation). `OPAQUE_BY_ACCESS_MODE`: 1 (usage telemetry). `MISSING_PRIMARY_SOURCE`: 6 (launch admission; process identity; cumulative budget; unknown usage; bypass/threat surface; cost-aware task compilation).

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact reference-family collision | `Test-Path` on both planned output paths under `docs/reference/external_agent_invocation_control/` returned false before this file was created | ACCEPT |
| roadmap/work-order family collision | prior dispatcher search `rg -n -i "external.agent.invocation.control.knowledge.readiness\|EAIC-KR" docs CVF_SESSION` (recorded in the paired GC-018) returned no pre-existing owner before dispatch | ACCEPT |
| MCP invocation-contract path collision | audit named `MCP invocation contract` and `MCP consumer pipeline` without committing to an exact file path; direct source search located both under `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/`, not under `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/`; recorded as a path refinement, not a contradiction, in the Authority Ledger | ACCEPT |
| live-run diagnostic standard path collision | direct search found the standard only under `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` while the root agent-instructions file, the provider/model roadmap, and other governed files cite the un-archived path; recorded as a source-fidelity caveat, not resolved by this T0 | ACCEPT (caveat recorded, not fixed; fixing a citation elsewhere is outside this work order's Allowed scope) |
| runtime-owner absence for launch admission, process identity, cumulative budget, unknown usage, and bypass surface | each absence above is supported by an explicit source citation (GC-009/GC-010 target-owner field, `operational.worker.launcher.ts` header comment, fallback-policy default, absence of a fail-closed policy file, and the audit's Missing end-to-end control chain table) rather than a bare negative claim | ACCEPT |

## Risk / Corrective Action

No corrective action is authorized by this map. The predecessor audit's
`GLOBAL_ROADMAP_EXECUTION_MORATORIUM_ACTIVE` decision remains in force. The
only risk finding specific to this T0 pass is the live-run diagnostic
standard citation-path drift recorded in the Authority Ledger and Negative
Search table; it does not block T0 closure because no T0 domain depended on
invoking that standard, but a later tranche that cites it should re-verify
the path before use.

## Bounded Recommendation

`READY_FOR_OPERATOR_SOURCE_SELECTION`

Every critical-priority gap (launch admission, process identity, cumulative
budget, unknown usage) has a precise acquisition question and a named
primary-source class above. This recommendation does not authorize T1,
external research, architecture ratification, or implementation. It confirms
only that the operator now has enough bounded, source-backed acquisition
rows to select which primary sources to approve next.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| system-chain map lane exists with PARTIAL posture | RUNTIME_BEHAVIOR | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` | `EVIDENCE_TO_OPERATOR_SURFACE` lane entry | `laneId` | system-chain map | ACCEPT |
| GC-009/GC-010 record no production caller | RUNTIME_BEHAVIOR | `docs/reference/system_chain/gaps/entries/gc009_gc010_no_production_caller.json` | `targetOwner`; `currentStatus` | `targetOwner` | system-chain GAP index | ACCEPT |
| orchestration contract has assignment/dependency/hash typing only | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/orchestration.contract.ts` | `TaskAssignment`; `OrchestrationResult` | `executionAuthorizationHash`; `orchestrationHash` | Control Plane orchestration contract | ACCEPT |
| MAO launcher self-declares no CLI/MCP/UI/runtime caller | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | header comment; `recordTimeout` | `recordTimeout` | MAO operational worker launcher | ACCEPT |
| MCP invocation contract hashes caller-supplied status/payload | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.invocation.contract.ts` | `invoke` method | `invoke` | MCP invocation contract | ACCEPT |
| MCP consumer pipeline composes caller-supplied results | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.invocation.consumer.pipeline.contract.ts` | `MCPInvocationConsumerPipelineRequest` | `invocationStatus` | MCP consumer pipeline | ACCEPT |
| MCP generic-agent adapter is fixed advisory-only | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/generic-agent-adapter.ts` | header comment; field assignment | `runtimeAdapterAuthorized` | MCP generic-agent adapter | ACCEPT |
| governed command launcher performs real spawn with child-only kill | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | timeout handler | `DEFAULT_COMMAND_TIMEOUT_MS` | governed command launcher | ACCEPT |
| provider execution bridge checks quota before adapter use | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | `execute` failure branches | `quota_exceeded` | Model Gateway execution bridge | ACCEPT |
| credential boundary source is environment-only today | VALUE_SET | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | `CredentialMetadata` | `source` | Model Gateway credential boundary | ACCEPT |
| live-run diagnostic standard now resides under the archive path | VALUE_SET | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | top-of-file `Status:` line | `Status` | live-run diagnostic standard | ACCEPT |
| predecessor audit position is CONTROL_NOT_EFFECTIVE_FOR_EXTERNAL_AGENT_CLI | VALUE_SET | `docs/audits/CVF_AGENT_CLI_MCP_INVOCATION_CONTROL_SYSTEM_CHAIN_REASSESSMENT_2026-07-20.md` | Findings / Position | Findings / Position | invocation-control audit | ACCEPT |
| provider/model roadmap is parked and superseded for execution | VALUE_SET | `docs/roadmaps/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_ASSIGNMENT_AND_INVOCATION_RECEIPT_ROADMAP_2026-07-20.md` | top-level `Status:`; Global Invocation-Control Reassessment Override section | `Status` | provider/model roadmap | ACCEPT |

## New Doc-Only Fields

`authorityClass`, `accessModeEvidenceClass`, `sourceAcquisitionPriority`, and
`blockingKnowledgeGap` are documentation-only T0 vocabulary used in this map's
Authority Ledger and Knowledge Gap And Source Acquisition Map tables. They do
not claim an existing runtime field or schema; they are descriptive column
labels for this reference artifact only.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | NOT_APPLICABLE_WITH_REASON: this map consumes only CVF-governed records already reconciled by the predecessor audit; it does not ingest a new external source |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this reference family and the predecessor audit |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | later primary-source intake requires a fresh operator-approved T1 tranche and a separate packet |

## Epistemic Process Block

### Expected Result / Prediction

The predecessor audit's per-surface dispositions and Missing end-to-end
control chain table were expected to still hold under direct re-verification
at the current `executionBaseHead`, since only two days separated the audit
date and this map's execution date and no source-controlling roadmap tranche
had executed in between.

### Evidence Comparison

Direct re-reads of all nine implied owner-surface files confirmed every one
of the audit's characterizations without exception: the system-chain map
lane, GC-009/GC-010 target-owner absence, the orchestration contract's
assignment/dependency/hash-only scope, the MAO launcher's self-declared
no-caller boundary, the MCP invocation contract and consumer pipeline's
caller-supplied-payload wrapping, the generic-agent adapter's fixed
advisory-only posture, the governed command launcher's real-but-static
spawn/child-kill behavior, and the Model Gateway files' request-level (not
agent-loop-level) control all matched.

### Contradiction Or Gap Disposition

No contradiction was found. Two non-blocking path refinements were found and
recorded in the Authority Ledger and Negative Search And Collision
Discipline table: the MCP invocation contract and consumer pipeline's actual
location under `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/` rather than
the audit's implied MCP-server extension path, and the live-run diagnostic
standard's archive-only physical location versus its still-active internal
`Status:` line and multiple un-archived citation paths elsewhere.

### Claim Update

The predecessor audit's general
`CONTROL_NOT_EFFECTIVE_FOR_EXTERNAL_AGENT_CLI` position is narrowed here into
a per-domain terminal-state matrix with acquisition priorities. This map does
not change the audit's decision, does not lift the moratorium, and does not
claim the two path refinements invalidate any audit finding.

## Claim Boundary

This map authorizes no external research, agent CLI/MCP invocation,
provider/API/account-subscription use, runtime or checker change, secret,
live proof, public-sync, commit, push, deployment, production action,
provider or model selection, architecture ratification, or lift of the
global execution moratorium. It is a bounded, source-backed knowledge and
acquisition map only, current as of `executionBaseHead` `1e689ed52`.
