# GC-018 Model Gateway C-02 P4B-B Live Proof T2 Authorized

Memory class: POINTER_RECORD

rawMemoryReleased: false

Baseline ID: GC018-MODEL-GATEWAY-C02-P4B-B-LIVE-PROOF-T2-AUTHORIZED-2026-06-15

Date: 2026-06-15

Status: AUTHORIZED_P4B_B_LIVE_PROOF_OPERATOR_KEYS

dispatchBaseHead: d46ccd83

## Purpose

Authorize one bounded P4B-B concrete provider live proof using operator-supplied
API keys already present on this machine. This baseline supersedes the negative
sample `CVF_GC018_MODEL_GATEWAY_C02_P4B_B_CONCRETE_PROVIDER_LIVE_PROOF_2026-06-15.md`
for the purpose of live execution. The negative sample is retained for the
dispatch-authoring guard regression and is not dispatched.

The proof verifies that the existing governed Model Gateway chain (routing,
credential boundary, health, quota, P5-A admission, P5-C bridge admission,
ProviderExecutionBridge.execute) can govern one operator-selected available-key
provider end to end with a real provider response.

## Operator Authorization

Operator authorized on 2026-06-15: live proof using existing available API keys
on this machine. Allowed key sources: process environment variables and the
existing `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local`. Allowed key
aliases: `DASHSCOPE_API_KEY`, `ALIBABA_API_KEY`, `CVF_ALIBABA_API_KEY`,
`CVF_BENCHMARK_ALIBABA_KEY`, `DEEPSEEK_API_KEY`.

Secret-safety rule: no raw key value may be printed, copied, logged, or
committed. Only key presence as a boolean and the provider alias used may be
reported.

## Provider Scope Rule

Alibaba/DashScope and DeepSeek are live-test adapters selected only because keys
may be available now. They are not canonical CVF product scope, not preferred,
not ranked, and carry no cost, quality, public-readiness, or production-readiness
claim. A future user may select different adapters.

## Source / Predecessor Evidence

- P5-C closed at material commit `b7a88782`; bridge admission guard wired.
- ProviderExecutionAdapter interface (bridge adapter contract):
  `provider-execution-bridge.ts` line 39.
- ProviderExecutionBridgeOptions.adapters and admissionRecords:
  `provider-execution-bridge.ts` lines 50 and 51.
- Bridge calls adapter.execute after admission guard:
  `provider-execution-bridge.ts` line 173.
- checkBridgeAdmission (P5-C): `provider-bridge-admission-guard.ts` line 33.
- admitProviderAdapter (P5-A): `provider-adapter-admission.ts` line 54.
- AdapterAdmissionRecord: `provider-adapter-admission.ts` line 35.
- CredentialBoundary.resolveSecretForRuntime: `credential-boundary.ts` line 33.
- Existing Alibaba sample adapter implements StreamContract (`.stream`), not the
  bridge ProviderExecutionAdapter (`.execute`):
  `providers/alibaba/stream-adapter.ts` line 36.
- Existing DeepSeek sample adapter implements JsonModeContract (`.jsonMode`):
  `providers/deepseek/json-mode-adapter.ts` line 36.

Implication: a thin bridge-compatible ProviderExecutionAdapter wrapper must be
constructed inside the live-proof harness so the proof flows through
`ProviderExecutionBridge.execute()`. The wrapper is live-proof-only and is not a
new canonical provider, not a new provider-execution semantic, and does not
modify existing adapters.

## Decision / Baseline / Proposed Tranche

Decision: release P4B-B live proof (T1 harness completion plus a single T2 live
call) to Claude under `WORKER_MUST_NOT_COMMIT`. Claude implements the harness,
runs the smallest live proof through the governed bridge, records secret-safe
evidence, and returns uncommitted artifacts for reviewer commit.

Baseline: the proof uses the existing governed chain only. P4C conformance,
P5-A admission, and P5-C bridge admission are not bypassed. The live wrapper
adapter calls the DashScope/Alibaba OpenAI-compatible endpoint via a single
non-streaming completion and returns `ProviderExecutionAdapterResult`.

Optional second provider (DeepSeek) only if it works with current source and a
key is present; otherwise record `N/A with reason`.

## Authority

- Operator instruction on 2026-06-15: execute Model Gateway C-02 P4B-B live
  proof using available operator-supplied API keys after authoring a
  dispatch-clean packet.
- P4B-B roadmap:
  `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4B_B_CONCRETE_PROVIDER_LIVE_PROOF_ROADMAP_2026-06-15.md`.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.
- Work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4B_B_LIVE_PROOF_T2_FOR_CLAUDE_2026-06-15.md`.

## Authorized Scope

1. Create `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts`
   containing a bridge-compatible `ProviderExecutionAdapter` wrapper for the
   DashScope/Alibaba OpenAI-compatible completion endpoint and a `runLiveProof`
   function with a `liveAuthorized` gate.
2. Create `EXTENSIONS/CVF_MODEL_GATEWAY/tests/p4b-b-dry-run-gate.test.ts`
   covering dry-run-without-key behavior, no-network when `liveAuthorized=false`,
   and bridge construction.
3. Create a runnable live-proof script
   `EXTENSIONS/CVF_MODEL_GATEWAY/scripts/run-p4b-b-live-proof.ts` that loads an
   operator-approved key by alias, builds the governed bridge, runs one small
   prompt, and writes a secret-safe receipt/diagnostic artifact.
4. Create GC-051 entry files for new governed source/test files.
5. Regenerate `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`.
6. Author completion review with secret-safe live evidence.

## Not Authorized

- Printing, copying, logging, or committing any raw API key value.
- Selecting Alibaba, DashScope, or DeepSeek as canonical CVF product scope.
- Bypassing P4C conformance, P5-A admission, or P5-C bridge admission.
- Adding a new provider/model id to the canonical capability registry.
- Modifying existing bridge, admission, conformance, or sample adapter source.
- Inventing a new provider marketplace architecture or new provider-execution
  semantics beyond a thin bridge-adapter wrapper for the live proof.
- EPF wiring, Strategy Layer, AI Gateway, public-sync, external app mutation,
  raw memory release, production readiness, or public readiness claims.
- Committing any artifact (Claude is `WORKER_MUST_NOT_COMMIT`).

## P4B-B Live Tranche Disposition

- T0 (doc/harness skeleton): folded into this authorization.
- T1 (harness and diagnostic readiness): authorized.
- T2 (single operator-selected provider governed live proof): authorized.
- T3 (second-provider parity): optional; only if current source supports it and
  a key is present; otherwise `N/A with reason`.

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
|---|---|
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Row | MGW-001 |
| Current status | PARTIAL_RECHECK_REQUIRED |
| P4B-B live-proof contribution | proves one governed live provider path end to end |
| Closure rule | live proof must not promote MGW-001 to complete |
| Provider-scope rule | live-test adapters are not canonical product scope |

## Verification

- Dispatch packet must pass
  `run_dispatch_packet_author_fast_gate.py --base d46ccd83 --head HEAD --enforce`
  before any live call.
- Claude must run focused tests, the live proof with secret-safe diagnostics,
  negative search for raw key leakage, diff hygiene, and worker-return fast gate.
- Codex owns committed-range pre-closure and session synchronization.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude (GC-018 and work order author) |
| Provider or surface | Claude Code local workspace |
| Session or invocation | 2026-06-15 P4B-B live proof T2 authorization |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read, Write, Bash key-presence and source-line verification |
| Target paths | this GC-018 and the P4B-B live-proof work order |
| Allowed scope source | operator instruction 2026-06-15 with available-key authorization |
| Before status evidence | HEAD `d46ccd83`; P5-C closed; P4B-B held; negative sample retained |
| After status evidence | live-proof GC-018 and work order authored, awaiting fast-gate pass and live run |
| Diff evidence | dispatch range `d46ccd83..HEAD` |
| Approval boundary | one bounded live proof through governed bridge; no canonical provider |
| Claim boundary | no provider preference, ranking, cost, public, or production claim |
| Agent type | Claude Code (GC-018 + work order author role) |
| Invocation ID | `p4b-b-live-proof-t2-gc018-2026-06-15` |
| Expected manifest | `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4B_B_LIVE_PROOF_T2_AUTHORIZED_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4B_B_LIVE_PROOF_T2_FOR_CLAUDE_2026-06-15.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4B_B_LIVE_PROOF_T2_AUTHORIZED_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4B_B_LIVE_PROOF_T2_FOR_CLAUDE_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance live-proof authorization. No public-sync batch is
authorized.

## Claim Boundary

This baseline authorizes only one bounded P4B-B concrete provider live proof
through the existing governed Model Gateway chain using operator-supplied keys.
It does not authorize provider preference, provider ranking, cost claims, new
canonical providers, new provider-execution semantics, EPF wiring, Strategy
Layer, AI Gateway absorption, public-sync, production readiness, public
readiness, or raw memory release.
