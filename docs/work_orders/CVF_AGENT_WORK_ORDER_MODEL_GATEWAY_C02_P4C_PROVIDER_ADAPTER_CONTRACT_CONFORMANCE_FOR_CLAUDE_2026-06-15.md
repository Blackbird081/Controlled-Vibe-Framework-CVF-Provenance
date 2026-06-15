# CVF Agent Work Order: Model Gateway C-02 P4C Provider Adapter Contract Conformance

Memory class: FULL_RECORD

rawMemoryReleased: false

Date: 2026-06-15

Status: DISPATCH_READY

Worker: Claude

Orchestrator / reviewer / committer: Codex

Worker commit policy: WORKER_MUST_NOT_COMMIT

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 1baba8c9

executionBaseHead: WORKER_MUST_CAPTURE_AFTER_DISPATCH

closureBaseHead: REVIEWER_CAPTURE_AFTER_WORKER_RETURN

riskCeiling: R1_BOUNDED_NO_NETWORK

completionReviewPath:
`docs/reviews/CVF_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_COMPLETION_2026-06-15.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_COMPLETION_2026-06-15.md`
- `AGENT_HANDOFF_V19_2026-06-15.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/state/entries/lastUpdated.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

## Purpose

Provide a precise Claude execution packet for P4C provider-agnostic adapter
conformance. The work order narrows the next Model Gateway step to deterministic
contract validation and keeps all provider-specific live behavior outside
Claude's authority.

## 1. Mission

Implement the deterministic P4C provider adapter contract conformance layer
inside `EXTENSIONS/CVF_MODEL_GATEWAY`. The layer must validate whether a
user-supplied provider adapter satisfies CVF's generic adapter contract before
it is admitted to the P4B-A bridge. The implementation must remain provider
agnostic, no-network, no-secret, and no-live-proof.

Return `COMPLETE_PENDING_REVIEW` with all artifacts uncommitted.

## 2. Authority Chain

- Operator instruction: 2026-06-15, create a Claude work order; Alibaba and
  DeepSeek are current live-run samples only and must not become canonical.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.
- P4B-A completion:
  `docs/reviews/CVF_MODEL_GATEWAY_C02_P4B_A_PROVIDER_EXECUTION_BRIDGE_COMPLETION_2026-06-15.md`.
- Roadmap:
  `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_ROADMAP_2026-06-15.md`.
- GC-018:
  `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_2026-06-15.md`.

Authority boundary: P4C deterministic conformance only. P4B-B live proof is
held.

## 3. Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Orchestrator | Codex | authors and commits dispatch packet |
| Worker | Claude | implementation, tests, GC-051 entries, worker return; no commit |
| Reviewer / committer | Codex | independent diff review, allowed repairs, completion, commits, session sync |
| Operator | Human | any live credential, network, provider selection for live proof, or scope expansion decision |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake summary | Operator corrected provider-specific framing and requested Claude work order |
| Scope classification | Bounded R1 Model Gateway foundation implementation |
| Risk sensitivity | No public sync, provider call, live proof, secret use, provider preference, production claim, or readiness claim |
| Selected role route | `MULTI_AGENT_MULTI_ROLE` |
| Role separation basis | Codex dispatches/reviews/commits; Claude implements and returns uncommitted evidence |
| Escalation condition | Stop for P4B-B, network, credential, concrete provider binding, provider addition, package install, destructive action, or scope expansion |

## 4. Allowed Scope

Claude may change only:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` (create);
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` (additive exports only);
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-conformance.test.ts`
  (create);
- new GC-051 entry files under
  `docs/corpus-intelligence/registry/entries/`;
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` by generator only;
- `docs/reviews/CVF_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_WORKER_RETURN_2026-06-15.md`
  (create).

## Write Ownership

Write ownership is exactly the Allowed Scope list above. Existing source
ownership is limited to additive `src/index.ts` exports. Every other existing
source file is read-only.

## 5. Forbidden Scope And Stop Conditions

Stop with `BLOCKED_SCOPE_EXPANSION` before:

- reading `.env.local` or resolving a runtime credential;
- calling `CredentialBoundary.resolveSecretForRuntime()`;
- importing, changing, or invoking concrete provider adapters;
- hardcoding Alibaba, DeepSeek, or another provider as canonical;
- using `fetch`, HTTP clients, provider URLs, or any network;
- adding provider/model IDs;
- changing existing Model Gateway source except additive `index.ts` exports;
- changing P4B-A bridge behavior, P4A skeleton, EPF, Strategy Layer, AI
  Gateway, session state, governance guards, public-sync, package manifests, or
  dependencies;
- committing, pushing, merging, deleting, or moving files.

## 6. Required First Reads

| File | Required use |
|---|---|
| `AGENTS.md` | active governance |
| `CVF_SESSION_MEMORY.md` | current mode and boundary |
| P4C roadmap | design and checkpoint split |
| P4C GC-018 | implementation authorization |
| P4B-A completion | predecessor closure and reviewer repair context |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | adapter contract |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | method and capability shapes |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | method lookup and support checks |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | current static capability registry |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | additive barrel exports |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Provider adapter input/result/contract exist | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | lines 25-39 | `ProviderExecutionAdapter` | provider execution bridge | ACCEPT |
| Provider execution bridge exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | lines 55-221 | `ProviderExecutionBridge` | provider execution bridge | ACCEPT |
| Provider method names exist | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | lines 1-10 | `ProviderMethodName` | provider method contract | ACCEPT |
| Provider capability file exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | lines 35-40 | `ProviderCapabilityFile` | provider method contract | ACCEPT |
| Method lookup helper exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | lines 47-76 | `getProviderMethodContract` | provider method gate | ACCEPT |
| Method support helper exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | lines 78-87 | `assertRegistryProviderMethodSupported` | provider method gate | ACCEPT |
| Method normalization helper exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | lines 25-27 | `normalizeProviderMethodName` | provider method gate | ACCEPT |
| Static capability registry exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | lines 43-98 | `PROVIDER_CAPABILITY_REGISTRY` | provider capability registry | ACCEPT |
| Alibaba adapter is method-specific sample only | `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/stream-adapter.ts` | lines 28-36 | `createAlibabaQwenTurboStreamAdapter` | Alibaba stream adapter | ACCEPT |
| DeepSeek adapter is method-specific sample only | `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/deepseek/json-mode-adapter.ts` | lines 28-36 | `createDeepSeekChatJsonModeAdapter` | DeepSeek JSON-mode adapter | ACCEPT |

## New Runtime Symbols

These symbols are authorized additions, not claims that they already exist:

| Symbol | Required role |
|---|---|
| `ProviderAdapterConformanceInput` | candidate adapter, provider/model/method, capability registry, and metadata-only boundary inputs |
| `ProviderAdapterConformanceReport` | deterministic status, reasons, supported methods, normalized method, and authorization fields |
| `ProviderAdapterConformanceStatus` | `conformant` or `blocked` |
| `evaluateProviderAdapterConformance` | pure local conformance evaluator |

Required shape summary:

```ts
export type ProviderAdapterConformanceStatus = "conformant" | "blocked";

export interface ProviderAdapterConformanceInput {
  providerId: string;
  modelId: string;
  method: ProviderMethodName;
  adapter: ProviderExecutionAdapter;
  capabilityRegistry: readonly ProviderCapabilityFile[];
  credentialMetadataAvailable?: boolean;
}

export interface ProviderAdapterConformanceReport {
  status: ProviderAdapterConformanceStatus;
  providerId: string;
  modelId: string;
  requestedMethod: ProviderMethodName;
  normalizedMethod: ProviderMethodName;
  supportedMethods: readonly ProviderMethodName[];
  adapterExecutionAuthorized: boolean;
  liveExecutionAuthorized: false;
  reasons: readonly string[];
}
```

## 7. Implementation Requirements

1. Create `provider-adapter-conformance.ts`.
2. Import only generic Model Gateway contract/helper types from current source.
3. Check `adapter.providerId === providerId`.
4. Use existing method-gate semantics to resolve provider/model capability and
   method support.
5. Return `blocked` with reasons for provider mismatch, missing capability,
   unsupported method, or missing credential metadata when the caller asks P4C
   to require metadata.
6. Return `conformant` only when the adapter identity and provider/model/method
   capability are aligned.
7. Set `adapterExecutionAuthorized=true` only for conformant local admission.
8. Set `liveExecutionAuthorized=false` in every report.
9. Do not call `adapter.execute()` inside the conformance evaluator.
10. Do not import or reference concrete provider adapters in implementation.

## 8. Required Deterministic Tests

Minimum cases:

1. conformant fake adapter with matching provider/model/method passes;
2. adapter provider mismatch blocks;
3. missing provider capability blocks;
4. missing model capability blocks;
5. unsupported method blocks;
6. method alias normalization is reflected in the report;
7. optional credential metadata requirement blocks when unavailable;
8. `liveExecutionAuthorized` is always false;
9. evaluator never calls `adapter.execute()`;
10. no hardcoded provider is required for conformance;
11. serialized report contains no test secret;
12. negative source assertion proves no concrete adapter import or network call.

## Pre-Flight Checks

Codex dispatch preflight before commit:

- `python governance/compat/check_agent_operation_trace.py --base 1baba8c9 --head HEAD --enforce`;
- `python governance/compat/check_work_order_dispatch_quality.py --base 1baba8c9 --head HEAD --enforce`;
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 1baba8c9 --head HEAD`;
- `git diff --check`.

Claude implementation preflight after dispatch:

- capture `executionBaseHead` with `git rev-parse --short HEAD`;
- confirm HEAD equals dispatch commit before editing;
- read the Required First Reads;
- run `npm run check` and `npm test -- --run` in `EXTENSIONS/CVF_MODEL_GATEWAY`
  before final worker return when feasible.

## Execution Plan

| Step | Owner | Action | Output |
|---|---|---|---|
| 1 | Claude | Read authority and source owners | source-verified implementation plan |
| 2 | Claude | Implement `provider-adapter-conformance.ts` | deterministic conformance helper |
| 3 | Claude | Add fake-provider tests | conformance test coverage |
| 4 | Claude | Add additive barrel exports | `src/index.ts` export only |
| 5 | Claude | Add GC-051 entries and regenerate aggregate | source/test registry coverage |
| 6 | Claude | Run required checks | command evidence |
| 7 | Claude | Author worker return | `COMPLETE_PENDING_REVIEW` packet |

## Evidence Requirements

Worker return must include:

- execution base head and final HEAD comparison;
- actual changed set;
- focused test and full module test results;
- GC-051 generator check result;
- worker fast gate result;
- diff hygiene result;
- negative-search results;
- Agent Operation Trace Block;
- explicit statement that no live provider call, credential read, runtime secret
  resolution, provider addition, or provider preference occurred.

## Work-Order Fulfillment Manifest

| Artifact | Required action | Owner |
|---|---|---|
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | create | Claude |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-conformance.test.ts` | create | Claude |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | additive exports only | Claude |
| `docs/corpus-intelligence/registry/entries/model-gateway-c02-p4c-provider-adapter-conformance.json` | create | Claude |
| `docs/corpus-intelligence/registry/entries/model-gateway-c02-p4c-provider-adapter-conformance-tests.json` | create | Claude |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | regenerate only | Claude |
| `docs/reviews/CVF_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_WORKER_RETURN_2026-06-15.md` | create | Claude |

Required proof literals in worker return:

- `COMPLETE_PENDING_REVIEW`;
- `WORKER_MUST_NOT_COMMIT`;
- `PROVIDER_AGNOSTIC`;
- `NO_NETWORK_CALL`;
- `NO_RUNTIME_SECRET_RESOLUTION`;
- `P4B_B_HOLD`.

## Negative Search And Collision Discipline

| Structured query | Search roots | Coverage | Same-token collision result | Disposition |
|---|---|---|---|---|
| `rg -n "ProviderAdapterConformance|evaluateProviderAdapterConformance" EXTENSIONS/CVF_MODEL_GATEWAY docs/roadmaps docs/baselines docs/work_orders` | Model Gateway source/tests and governed planning docs | source, tests, docs, JSON/external N/A with reason | Planning-doc occurrences exist and are non-authoritative declarations of proposed symbols | Runtime definitions may be added only at the allowed P4C paths |
| `rg -n "fetch\\(|https?://|resolveSecretForRuntime|DASHSCOPE_API_KEY|DEEPSEEK_API_KEY|ALIBABA_API_KEY|\\.env\\.local" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-conformance.test.ts` | new P4C source and test | source/tests only | Provider URL and key tokens may exist in unrelated provider samples | New P4C files must produce zero matches except query text in worker return |
| `rg -n "providers/alibaba|providers/deepseek|createAlibaba|createDeepSeek" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-conformance.test.ts` | new P4C source and test | source/tests only | Concrete adapter names exist elsewhere as samples | New P4C files must produce zero matches |
| `rg -n "AC1|AC10|BLOCKED_SCOPE_EXPANSION|BLOCKED_BASELINE_RED|COMPLETE_PENDING_REVIEW|DEFERRED_PRIVATE_ONLY|HEAD" docs governance CVF_SESSION AGENT_HANDOFF_V19_2026-06-15.md` | governed docs, governance, session, handoff | docs, JSON, governance source | Same-token collisions exist for workflow/status vocabulary | Retain as workflow vocabulary; do not treat as runtime-source search results |

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
|---|---|
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Stable row | `MGW-001` |
| Current status | `PARTIAL_RECHECK_REQUIRED` |
| P4C contribution | Adds provider-agnostic adapter conformance before live binding |
| Closure rule | P4C must not promote `MGW-001` to complete |
| P4B-B rule | Live proof remains a separate operator-authorized checkpoint |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order section | Disposition |
|---|---|---|
| Provider-agnostic conformance helper | Allowed Scope, Implementation Requirements | RELEASED |
| No provider-specific canonicalization | Forbidden Scope, Provider sample boundary | RELEASED |
| Deterministic no-network tests | Required Deterministic Tests | RELEASED |
| GC-051 coverage | Work-Order Fulfillment Manifest | RELEASED |
| Worker no-commit return | Return Contract | RELEASED |
| P4B-B held | Forbidden Scope and Legacy Disposition | NOT_RELEASED_WITH_REASON |

## Worker Autonomy / No-Question Rule

Claude must fix allowed-scope gate failures and rerun the relevant checks
without asking the operator. Ask the operator only if the fix would exceed
Allowed Scope, touch forbidden paths, consume secrets/quota, run live proof,
change risk level, or alter the claim boundary.

## Verification

Claude must run and report:

- `npm run check` in `EXTENSIONS/CVF_MODEL_GATEWAY`;
- `npm test -- --run` in `EXTENSIONS/CVF_MODEL_GATEWAY`;
- `python governance/compat/generate_corpus_scan_registry.py --check`;
- `python governance/compat/run_worker_return_fast_gate.py`;
- `git diff --check`;
- negative searches listed above.

Codex reviewer will run reviewer-fast, inspect the real diff, perform allowed
repairs, author completion review, commit, run committed-range pre-closure, and
sync session state.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | P4C implementation is provider-agnostic and contains no hardcoded accepted provider IDs | source review and tests |
| AC2 | Adapter provider identity mismatch blocks admission | deterministic tests |
| AC3 | Missing provider/model capability blocks admission | deterministic tests |
| AC4 | Unsupported method blocks admission through existing method-gate semantics | deterministic tests |
| AC5 | Supported aliases normalize correctly without provider-specific branching | deterministic tests |
| AC6 | Conformant fake adapter returns `adapterExecutionAuthorized=true` and `liveExecutionAuthorized=false` | deterministic tests |
| AC7 | Evaluator does not call `adapter.execute()` | deterministic tests |
| AC8 | No source/test uses network, provider URL, real key, `.env.local`, concrete adapter import, or `resolveSecretForRuntime()` | negative search |
| AC9 | Type check, full module tests, GC-051 drift check, worker fast gate, and diff hygiene pass | command evidence |
| AC10 | Worker leaves HEAD unchanged | base/head evidence |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime-foundation work. Public sync is not
authorized.

## Return Contract

Return one of:

- `COMPLETE_PENDING_REVIEW`;
- `BLOCKED_SCOPE_EXPANSION`;
- `BLOCKED_SOURCE_NOT_FOUND`;
- `BLOCKED_BASELINE_RED`.

The return must include actual changed paths, test/gate summaries, exact HEAD
comparison, negative-search results, and an Agent Operation Trace Block.

## Return-To-Orchestrator Conditions

- Return `COMPLETE_PENDING_REVIEW` only when AC1-AC10 and all required gates
  pass.
- Return `BLOCKED_SOURCE_NOT_FOUND` when a cited current source owner is missing
  or materially changed at execution HEAD.
- Return `BLOCKED_BASELINE_RED` when the pre-existing module baseline is red.
- Return `BLOCKED_SCOPE_EXPANSION` before any forbidden action.

## Review Gate

Codex must inspect the real diff, verify all source/test behavior, rerun
focused and governance gates, author the completion review, and commit.
Worker-authored PASS text is not independent review evidence.

## Reviewer Closure Conversion

Codex must convert a valid `COMPLETE_PENDING_REVIEW` worker return into closure
through separate reviewer-owned artifacts. Claude must not edit reviewer-owned
closure paths or session continuity paths.

Reviewer conversion steps:

1. run reviewer-fast and focused checks on the uncommitted worker return;
2. inspect source, tests, registry entries, and worker evidence;
3. perform allowed-scope repairs if needed;
4. author the completion review;
5. commit material artifacts;
6. run committed-range pre-closure;
7. sync session/front-door/handoff in a separate commit if next allowed move
   changes.

## Closure Checklist

- [ ] Claude captured execution base head
- [ ] Source verification refreshed against execution head
- [ ] Allowed scope respected
- [ ] Forbidden scope avoided
- [ ] AC1-AC10 satisfied
- [ ] GC-051 entries and aggregate align
- [ ] Negative searches recorded
- [ ] Worker return includes required proof literals
- [ ] Worker leaves all artifacts uncommitted

## Operator Checkpoint

No operator pause is required inside allowed P4C remediation. Explicit new
operator authorization is required for P4B-B, credentials, network, provider
binding, provider/model addition, package installation, public sync, or changed
risk/claim boundary.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-15 P4C dispatch |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | source inspection, apply_patch, governance gates |
| Target paths | P4C roadmap, GC-018, and Claude work order |
| Allowed scope source | operator instruction 2026-06-15 |
| Before status evidence | HEAD `1baba8c9`; P4B-A closed; P4B-B held |
| After status evidence | P4C dispatch packet ready |
| Diff evidence | pre-dispatch range `1baba8c9..HEAD` |
| Approval boundary | provider-agnostic deterministic conformance only |
| Claim boundary | no live provider, credential use, quota spend, provider preference, or public claim |
| Agent type | Codex orchestrator |
| Invocation ID | `p4c-provider-adapter-conformance-dispatch-2026-06-15` |
| Expected manifest | `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_ROADMAP_2026-06-15.md`; `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_FOR_CLAUDE_2026-06-15.md` |
| Actual changed set | `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_ROADMAP_2026-06-15.md`; `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_FOR_CLAUDE_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This work order authorizes P4C deterministic provider-adapter conformance only.
It does not authorize P4B-B, provider credentials, network calls, live proof,
provider/model addition, provider preference, EPF wiring, Strategy Layer, AI
Gateway absorption, public sync, production readiness, public readiness, raw
memory release, co-work product development, or autonomous mutation.
