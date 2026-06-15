# CVF Model Gateway C-02 P4B-B Concrete Provider Live Proof Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_AUTHORIZATION_REQUIRED

docType: roadmap

Date: 2026-06-15

rawMemoryReleased: false

Roadmap class: model-gateway-foundation-live-proof

## Purpose

Define the concrete P4B-B live-proof path after P5-C completion.

P4B-A built the deterministic provider execution bridge. P4C added adapter
contract conformance. P5-A/P5-B added adapter admission and capability
negotiation. P5-C wired bridge execution behind adapter admission. P4B-B is the
first lane that may prove a real provider can pass through that governed chain.

This roadmap does not authorize a provider call. It defines the exact
authorization gate, source packet, implementation boundary, evidence packet,
and stop conditions required before a future GC-018/work order may run live.

## Scope

In scope:

- source-verified roadmap for P4B-B live proof;
- operator authorization boundary for live credential and quota use;
- single-provider governed live-proof sequence;
- live-run diagnostic and secret-safety requirements;
- completion evidence and claim boundary.

Out of scope:

- actual provider/API call;
- credential loading or secret inspection;
- runtime/source implementation;
- public-sync or public claim;
- provider preference, cost, quality, or production-readiness claim.

## Non-Goals

- Do not select a provider on behalf of the operator.
- Do not run live proof from this roadmap alone.
- Do not treat Alibaba, DeepSeek, or any sample adapter as canonical CVF
  product scope.
- Do not bypass P4C conformance, P5 admission, or P5-C bridge admission.
- Do not claim public readiness, production readiness, cost optimization, or
  all-provider support.

## Current State

| Item | Current evidence | Disposition |
|---|---|---|
| P4B-A bridge | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | completed, bounded |
| P4C conformance | `docs/reviews/CVF_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_COMPLETION_2026-06-15.md` | completed, bounded |
| P5-A/P5-B admission and negotiation | `docs/reviews/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_COMPLETION_2026-06-15.md` | completed, bounded |
| P5-C bridge admission boundary | `docs/reviews/CVF_MODEL_GATEWAY_C02_P5C_BRIDGE_ADMISSION_BOUNDARY_COMPLETION_2026-06-15.md` | completed, bounded |
| P4B-B live proof | active session state and handoff | authorization required |

## Authorization Decision

P4B-B remains authorization-gated. It must not start execution before the
operator explicitly authorizes a live proof.

Required authorization text for a future GC-018/work order must state:

```text
I authorize Model Gateway C-02 P4B-B concrete provider live proof for
provider(s): <operator-selected provider ids>, using operator-supplied
environment variables only. The agent may run the approved live proof commands
without printing raw secrets.
```

Without that authorization, agents may only prepare documents, source maps,
negative-search evidence, and non-live dry-run tests.

## Provider Scope Rule

P4B-B must not promote any current sample provider into canonical CVF product
scope. Alibaba and DeepSeek may be used only if the operator selects them for a
live proof. A future user may choose different adapters.

Provider-specific proof is evidence that the generic CVF provider control chain
can govern one selected adapter. It is not evidence of provider preference,
provider quality, provider cost superiority, production readiness, or public
readiness.

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Bridge options include credential references, adapters, and admission records | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | lines 43-51 | `ProviderExecutionBridgeOptions` | `ProviderExecutionBridge` | ACCEPT |
| Bridge calls adapter only after routing, credential metadata, health, quota, and admission checks | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | line 173 | `adapter.execute(...)` | `ProviderExecutionBridge.execute` | ACCEPT |
| Bridge uses shielded error envelopes for blocked execution | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | line 264 | `buildShieldedErrorResult` | `ProviderExecutionBridge` | ACCEPT |
| P5-C admission block is available as bridge error class | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | line 16 | `admission_blocked` | `GatewayErrorClass` | ACCEPT |
| Credential metadata is secret-safe | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | line 17 | `CredentialBoundary` | credential boundary | ACCEPT |
| Runtime secret access is explicitly separated | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | line 33 | `resolveSecretForRuntime` | credential boundary | ACCEPT |
| Current Alibaba sample adapter exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/stream-adapter.ts` | line 27 | `createAlibabaQwenTurboStreamAdapter` | sample provider adapter | ACCEPT |
| Current DeepSeek sample adapter exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/deepseek/json-mode-adapter.ts` | line 27 | `createDeepSeekChatJsonModeAdapter` | sample provider adapter | ACCEPT |
| Provider capability registry exists and must not be treated as provider preference | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 42 | `PROVIDER_CAPABILITY_REGISTRY` | provider capability registry | ACCEPT |
| Provider registry surface exists and must be accounted for in negative-search/collision evidence | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | source file exists | `ProviderRegistry` | provider registry | ACCEPT |

## Design Control Gate

| Control | P4B-B decision |
|---|---|
| Foundation value | High: first live proof through bridge plus admission chain |
| Operator control | Mandatory explicit authorization before live call |
| Provider neutrality | Operator-selected provider only; no canonical provider claim |
| Secret safety | Environment variable names only; raw values never printed or committed |
| Live diagnostic discipline | Required for every fail, timeout, partial, or rerun-triggering result |
| Backward compatibility | No bridge bypass; proof must use existing governed surfaces |
| Claim boundary | Private provenance proof only unless later public-sync is authorized |

## Roadmap Design

P4B-B is split into four gated tranches. Only T0 is eligible without live
credential authorization.

| Tranche | Status | Purpose | Live/provider use |
|---|---|---|---|
| P4B-B-T0 | ELIGIBLE_DOC_ONLY | Build source-verified live-proof packet, provider-selection matrix, and dry-run proof plan | No |
| P4B-B-T1 | AUTH_REQUIRED | Implement or repair the bounded live-proof harness and secret-safe diagnostics | No live call unless operator authorization is present |
| P4B-B-T2 | AUTH_REQUIRED | Run one operator-selected provider through the governed bridge with admitted adapter record | Yes, only after authorization |
| P4B-B-T3 | OPTIONAL_AUTH_REQUIRED | Add second-provider parity proof if operator selects it | Yes, separate authorization |

## P4B-B-T0: Source-Verified Live-Proof Packet

Goal: prepare the exact GC-018 and work order inputs without consuming live
quota.

Required outputs:

- a GC-018 baseline with explicit live credential boundary;
- a work order with `WORKER_MAY_RUN_LIVE_PROOF_AFTER_AUTHORIZATION`;
- provider-selection matrix that treats every provider as operator-selected,
  not canonical;
- live-run diagnostic requirements copied from the canonical live diagnostic
  standard;
- negative-search plan for raw key prints and forbidden public-sync claims;
- dry-run tests that prove the harness refuses to run without authorization.

Acceptance criteria:

| ID | Criterion |
|---|---|
| T0-AC1 | Work order names exact provider ids selected by operator, or remains authorization-gated |
| T0-AC2 | Work order names exact environment variable aliases allowed for each selected provider |
| T0-AC3 | Work order forbids printing raw secrets, request bodies containing secrets, or full provider responses if unsafe |
| T0-AC4 | Work order requires live-run diagnostic record for fail, timeout, empty output, or retry |
| T0-AC5 | Work order includes Agent Operation Trace Block with exact manifest |
| T0-AC6 | Work order includes Worker Autonomy / No-Question Rule but stops for credential/provider scope expansion |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | No live call is authorized by this roadmap | roadmap status and claim boundary |
| AC2 | Future live proof requires explicit operator-selected provider ids | Authorization Decision section |
| AC3 | Future work order must name allowed env var aliases and forbid raw secret output | Work Order Requirements |
| AC4 | Future proof must pass through `ProviderExecutionBridge.execute()` | P4B-B-T2 execution chain |
| AC5 | Future proof must include admitted adapter evidence from P5 admission | P4B-B-T2 execution chain |
| AC6 | Future proof must preserve P5-C bridge admission boundary | P4B-B-T1/T2 stop conditions |
| AC7 | Live-run failures must be classified before rerun | Live Run Diagnostic Requirements |
| AC8 | Completion claim remains bounded and private unless separately authorized | Completion Claim Boundary and Public Export Disposition |

## P4B-B-T1: Harness And Diagnostic Readiness

Goal: make the live-proof command deterministic and safe before any live call.

Allowed implementation after GC-018:

- create a narrow live-proof script or test under `EXTENSIONS/CVF_MODEL_GATEWAY`
  or `scripts/`, as chosen by GC-018;
- load only operator-approved environment variables;
- construct `ProviderExecutionBridge` with routing, credential references,
  health, quota, receipt builder, selected adapter, and admitted record;
- verify missing-key behavior returns a classified diagnostic without retry
  loops;
- write receipt/diagnostic artifacts that do not contain raw secrets.

Stop conditions:

- raw key would be printed or committed;
- selected provider is not named in operator authorization;
- harness bypasses `ProviderExecutionBridge`;
- harness calls adapter directly instead of bridge;
- harness bypasses P5-C `admissionRecords`;
- failure is unclear and no diagnostic can be captured.

## P4B-B-T2: Single-Provider Governed Live Proof

Goal: prove one operator-selected provider can pass through the generic CVF
provider control chain.

Required execution chain:

1. resolve active session and operator authorization;
2. load approved environment variable(s) without printing values;
3. create credential reference for selected provider;
4. create or import selected provider adapter;
5. create conformance report and admission record;
6. insert admission record into bridge `admissionRecords`;
7. run one small prompt through `ProviderExecutionBridge.execute()`;
8. capture receipt, diagnostic, provider id, model id, status, latency, and
   safe output summary;
9. run post-proof negative search for raw secret leakage;
10. close with bounded claim only.

Required live-proof evidence:

| Evidence item | Required content |
|---|---|
| Provider selection | operator-selected provider id and model id |
| Credential boundary | env var name only, no raw value |
| Admission evidence | admission status `admitted`, reason codes, liveExecutionAuthorized remains governed by work order |
| Bridge evidence | result passed through `ProviderExecutionBridge.execute()` |
| Receipt evidence | trace id, provider/model, decision, credential fingerprint only |
| Diagnostic evidence | success or classified failure per live-run diagnostic standard |
| Leakage evidence | negative search confirms no raw key committed or printed |

## P4B-B-T3: Optional Second-Provider Parity

T3 is not required for P4B-B closure. It may run only if the operator selects a
second provider and accepts additional live quota use.

T3 may prove adapter portability across two selected providers. It must not rank
providers, prefer providers, or make cost/quality claims unless a separate
benchmark roadmap authorizes that analysis.

## Work Plan

| Step | Owner | Output | Stop condition |
|---|---|---|---|
| 1 | Codex/orchestrator | this roadmap | roadmap gate failure |
| 2 | Operator | explicit provider/live authorization text | no authorization, no live work |
| 3 | Orchestrator | fresh GC-018 baseline with live boundary | missing source verification or credential boundary |
| 4 | Worker | source-verified work order and dry-run harness checks | provider/call scope mismatch |
| 5 | Worker | one governed live proof through bridge | diagnostic missing, raw secret risk, or provider failure |
| 6 | Reviewer | completion review and material/session split commits | gate failure or overbroad claim |

## Required Gates

Before dispatch:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base <baseHead> --head HEAD --enforce
```

Before live execution:

```powershell
python governance/compat/check_active_session_state.py --enforce
python governance/compat/generate_corpus_scan_registry.py --check
npm run check
npm test -- --run
```

After live execution:

```powershell
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <materialBase> --head HEAD
git diff --check
```

## Verification / Evidence

The future P4B-B completion review must include:

- command evidence for type check and tests;
- command evidence for the live proof or classified failure;
- receipt path or trace id;
- diagnostic path for any fail/timeout/partial run;
- negative-search output for secret leakage;
- Agent Operation Trace exact manifest;
- committed material range;
- separate session-sync range if front-door state changes.

Release-quality public/governance claims require the mandatory release gate:

```powershell
python scripts/run_cvf_release_gate_bundle.py --json
```

If that command is not applicable to the exact P4B-B proof, the completion
review must state `N/A with reason` and keep the claim private/provenance-only.

## Live Run Diagnostic Requirements

Every failed, partial, timed-out, empty-output, or rerun-triggering live run
must record:

- stage;
- failure class;
- retryability;
- user action required;
- provider/model when known;
- HTTP status/latency when available;
- receipt or trace id when available;
- safe human-readable message.

The agent must not rerun the same unclear live proof until the failure is
classified or a changed condition is recorded.

## Negative Search Discipline

The completion review must record exact negative-search commands for:

```bash
rg -n "DASHSCOPE_API_KEY=|ALIBABA_API_KEY=|DEEPSEEK_API_KEY=|sk-|dashscope_" .
rg -n "console\\.log\\(.*(apiKey|secret|Authorization)|Authorization: `Bearer" EXTENSIONS/CVF_MODEL_GATEWAY scripts docs/reviews
rg -n "production readiness|public readiness|provider preference|best provider|preferred provider" docs/reviews docs/roadmaps docs/work_orders
```

Same-token collisions in documentation must be classified. Raw secret values
must never be included in completion artifacts.

## Completion Claim Boundary

Allowed P4B-B closure claim:

`CLOSED_PASS_BOUNDED`: one operator-selected concrete provider completed a
secret-safe, receipt-backed, diagnostic-backed live proof through the governed
Model Gateway bridge with admitted adapter evidence.

Forbidden closure claims:

- production readiness;
- public readiness;
- provider preference;
- provider quality ranking;
- provider cost optimization;
- broad adapter marketplace support;
- all-provider support;
- EPF wiring;
- Strategy Layer implementation;
- AI Gateway absorption;
- public-sync publication.

## Work Order Requirements

The future work order must include:

- exact operator authorization text;
- exact provider ids and model ids;
- exact env var aliases allowed;
- Source Verification Block;
- Worker Autonomy / No-Question Rule;
- Evidence Requirements;
- Review Gate;
- Closure Checklist;
- Return-To-Orchestrator Conditions;
- Agent Operation Trace Block;
- Machine Closure Package;
- Finding-To-Governance Learning Disposition;
- Public Export Disposition.

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: this roadmap defines a private provenance live-proof path. No
public-sync batch or public claim is authorized.

## Claim Boundary

This roadmap does not authorize live provider execution. It authorizes planning
only. P4B-B may proceed to GC-018/work order dispatch only after explicit
operator authorization for selected provider(s), credential boundary, and live
quota use.
