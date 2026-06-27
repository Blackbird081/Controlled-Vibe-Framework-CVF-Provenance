# CVF Agent Work Order: Model Gateway C-02 P5 Provider Adapter Admission And Capability Negotiation

Memory class: FULL_RECORD

rawMemoryReleased: false

Date: 2026-06-15

Status: DRAFT_SUPERSEDED_BY_CODEX_WORK_ORDER

Worker: Claude

Orchestrator / reviewer / committer: Codex

Worker commit policy: WORKER_MUST_NOT_COMMIT

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 586aa56e

executionBaseHead: WORKER_MUST_CAPTURE_AFTER_DISPATCH

closureBaseHead: MATERIAL_COMMIT_SHA_TO_BE_CAPTURED_BY_CODEX

riskCeiling: R1_BOUNDED_NO_NETWORK

Superseded disposition: retained for audit only. The active execution packet is
`docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_FOR_CODEX_2026-06-15.md`.

completionReviewPath:
`docs/reviews/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_COMPLETION_2026-06-15.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_COMPLETION_2026-06-15.md`
- `AGENT_HANDOFF_V19_2026-06-15.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/state/entries/lastUpdated.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

## Purpose

Provide a precise Claude execution packet for P5-A adapter admission record and
P5-B capability negotiation. The work order narrows the next Model Gateway step
to deterministic admission evidence and provider-agnostic capability negotiation.
All provider-specific live behavior, bridge execution mutation, and P5-C bridge
admission boundary remain outside Claude's authority for this tranche.

## 1. Mission

Implement the deterministic P5 provider adapter admission record and capability
negotiation layer inside `EXTENSIONS/CVF_MODEL_GATEWAY`. The layer must:

- consume a P4C conformance report as a required input to admission;
- produce a machine-readable admission record with status, reason codes, and
  trace fields;
- negotiate capability against the provider/model/method boundary using
  existing method-gate helpers;
- never hardcode accepted provider IDs, call network, read secrets, or invoke
  any adapter method.

Split to P5-A only if the combined source file would exceed the 300L governed
threshold. In that case flag P5-B for a separate dispatch and return
`COMPLETE_PENDING_REVIEW` for P5-A alone.

Return `COMPLETE_PENDING_REVIEW` with all artifacts uncommitted.

## 2. Authority Chain

- Operator instruction: 2026-06-15, create P5 roadmap; next move is GC-018 and
  source-verified Claude work order for P5-A/P5-B.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.
- P4C completion:
  `docs/reviews/CVF_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_COMPLETION_2026-06-15.md`.
- Roadmap:
  `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_ROADMAP_2026-06-15.md`.
- GC-018:
  `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_2026-06-15.md`.

Authority boundary: P5-A adapter admission record and P5-B capability
negotiation only. P4B-B live proof, P5-C bridge mutation, and all parked lanes
remain held.

## 3. Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Orchestrator | Codex | authors and commits dispatch packet |
| Worker | Claude | implementation, tests, GC-051 entries, worker return; no commit |
| Reviewer / committer | Codex | independent diff review, allowed repairs, completion, commits, session sync |
| Operator | Human | any live credential, network, provider selection for live proof, P5-C authorization, or scope expansion |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake summary | Operator authorized P5 roadmap; next move is GC-018 + work order dispatch |
| Scope classification | Bounded R1 Model Gateway foundation implementation |
| Risk sensitivity | No public sync, provider call, live proof, secret use, bridge mutation, provider preference, production claim, or readiness claim |
| Selected role route | `MULTI_AGENT_MULTI_ROLE` |
| Role separation basis | Codex dispatches/reviews/commits; Claude implements and returns uncommitted evidence |
| Escalation condition | Stop for P4B-B, P5-C, network, credential, concrete provider binding, provider addition, package install, destructive action, or scope expansion |

## 4. Allowed Scope

Claude may change only:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts` (create);
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-negotiation.ts` (create;
  may be deferred to P5-B dispatch if file-size risk requires split);
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-admission.test.ts`
  (create);
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` (additive exports only);
- new GC-051 entry files under
  `docs/corpus-intelligence/registry/entries/`;
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` by generator only;
- `docs/reviews/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_WORKER_RETURN_2026-06-15.md`
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
- hardcoding Alibaba, DeepSeek, or another provider as a canonical accepted ID;
- using `fetch`, HTTP clients, provider URLs, or any network;
- adding provider/model IDs as canonically accepted values;
- modifying `provider-execution-bridge.ts` execute logic (P5-C boundary);
- modifying `provider-adapter-conformance.ts` (P4C owner, read-only);
- modifying existing Model Gateway source except additive `index.ts` exports;
- changing P4B-A bridge behavior, P4A skeleton, EPF, Strategy Layer, AI
  Gateway, session state, governance guards, public-sync, package manifests, or
  dependencies;
- committing, pushing, merging, deleting, or moving files.

## 6. Required First Reads

| File | Required use |
|---|---|
| `AGENTS.md` | active governance |
| `CVF_SESSION_MEMORY.md` | current mode and boundary |
| P5 roadmap | design and tranche split decision |
| P5 GC-018 | implementation authorization |
| P4C completion review | predecessor closure and reviewer repair context |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | P4C conformance types consumed as admission input |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | adapter contract and bridge shape |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | method normalization and capability lookup helpers |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | static capability registry and alias map |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | additive barrel exports |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| P4C conformance status exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | line 24 | `ProviderAdapterConformanceStatus` | P4C conformance types | ACCEPT |
| P4C conformance input exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | line 26 | `ProviderAdapterConformanceInput` | P4C conformance types | ACCEPT |
| P4C conformance report exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | line 35 | `ProviderAdapterConformanceReport` | P4C conformance types | ACCEPT |
| P4C liveExecutionAuthorized=false field exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | line 44 | `liveExecutionAuthorized` | ProviderAdapterConformanceReport | ACCEPT |
| P4C evaluator exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | line 54 | `evaluateProviderAdapterConformance` | P4C conformance evaluator | ACCEPT |
| Provider adapter contract exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | line 37 | `ProviderExecutionAdapter` | provider execution bridge | ACCEPT |
| Method normalization exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | line 24 | `normalizeProviderMethodName` | provider method gate | ACCEPT |
| Provider capability lookup exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | line 46 | `findProviderCapability` | provider method gate | ACCEPT |
| Supported method listing exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | line 89 | `listRegistrySupportedMethods` | provider method gate | ACCEPT |
| Static capability registry exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 42 | `PROVIDER_CAPABILITY_REGISTRY` | provider capability registry | ACCEPT |
| Barrel export file exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | line 1 | additive barrel | index barrel | ACCEPT |

## New Runtime Symbols (P5-A - Adapter Admission Record)

These symbols are authorized additions, not claims they already exist:

| Symbol | Required role |
|---|---|
| `AdapterAdmissionStatus` | `"admitted"` \| `"blocked"` \| `"needs_operator_authorization"` |
| `AdapterAdmissionReasonCode` | string-literal union of canonical reason codes |
| `AdapterAdmissionRecord` | deterministic admission output with status, reason codes, trace fields, and `liveExecutionAuthorized=false` |
| `admitProviderAdapter()` | pure local admission evaluator consuming P4C report |

Required shape summary for P5-A:

```ts
export type AdapterAdmissionStatus =
  | "admitted"
  | "blocked"
  | "needs_operator_authorization";

export type AdapterAdmissionReasonCode =
  | "conformance_blocked"
  | "provider_not_in_registry"
  | "model_not_in_registry"
  | "method_not_supported"
  | "credential_metadata_required"
  | "live_execution_not_authorized";

export interface AdapterAdmissionRecord {
  status: AdapterAdmissionStatus;
  providerId: string;
  modelId: string;
  requestedMethod: string;
  normalizedMethod: string;
  supportedMethods: readonly string[];
  conformanceStatus: ProviderAdapterConformanceStatus;
  liveExecutionAuthorized: false;
  reasonCodes: readonly AdapterAdmissionReasonCode[];
  reasons: readonly string[];
  admissionTimestamp: string;
  traceId: string;
}

export function admitProviderAdapter(
  conformanceReport: ProviderAdapterConformanceReport,
  capabilityRegistry: readonly ProviderCapabilityFile[],
  options?: { requireCredentialMetadata?: boolean },
): AdapterAdmissionRecord
```

## New Runtime Symbols (P5-B - Capability Negotiation)

These symbols are authorized additions, not claims they already exist.
P5-B may be deferred to a separate dispatch if P5-A source exceeds 300L.

| Symbol | Required role |
|---|---|
| `CapabilityNegotiationStatus` | `"negotiated"` \| `"blocked"` \| `"fallback_available"` |
| `CapabilityNegotiationResult` | negotiation output with status, effective method, reason codes |
| `negotiateProviderCapability()` | pure local negotiation using existing method-gate helpers |

Required shape summary for P5-B:

```ts
export type CapabilityNegotiationStatus =
  | "negotiated"
  | "blocked"
  | "fallback_available";

export interface CapabilityNegotiationResult {
  status: CapabilityNegotiationStatus;
  providerId: string;
  modelId: string;
  requestedMethod: string;
  effectiveMethod: string;
  supportedMethods: readonly string[];
  reasonCodes: readonly string[];
  reasons: readonly string[];
}

export function negotiateProviderCapability(
  providerId: string,
  modelId: string,
  requestedMethod: string,
  capabilityRegistry: readonly ProviderCapabilityFile[],
): CapabilityNegotiationResult
```

## 7. Implementation Requirements

### P5-A (Adapter Admission Record)

1. Create `provider-adapter-admission.ts`.
2. Import only P4C conformance types and existing method-gate/capability types.
3. Consume `ProviderAdapterConformanceReport` as the sole adapter input signal.
4. If conformance report status is `"blocked"`, set admission status to
   `"blocked"` with reason code `conformance_blocked`.
5. Lookup provider/model in capability registry using existing
   `findProviderCapability` helper; if missing, set `"blocked"` with
   `provider_not_in_registry` or `model_not_in_registry`.
6. Verify requested method is supported (after normalization); if not, set
   `"blocked"` with `method_not_supported`.
7. If `requireCredentialMetadata=true` and
   `conformanceReport.adapterExecutionAuthorized=false`, set
   `"needs_operator_authorization"` with `credential_metadata_required`.
8. Set `admitted` only when all checks pass.
9. Always set `liveExecutionAuthorized=false`.
10. Never call `adapter.execute()` or any adapter method inside the evaluator.
11. Generate deterministic `traceId` and `admissionTimestamp` without network.

### P5-B (Capability Negotiation)

1. Create `provider-capability-negotiation.ts`.
2. Use existing `normalizeProviderMethodName` and `listRegistrySupportedMethods`
   helpers; do not duplicate their logic.
3. If requested method is supported directly, return `"negotiated"`.
4. If normalized alias is supported, return `"negotiated"` with effective method
   set to normalized value.
5. If a fallback method is available (e.g., `"chat"` when `"complete"` is
   requested and `"complete"` is absent), return `"fallback_available"`.
6. Otherwise return `"blocked"` with explicit reason codes.
7. No provider-specific branching. No hardcoded provider IDs in logic.

## 8. Required Deterministic Tests

Minimum cases for `provider-adapter-admission.test.ts`:

1. conformant P4C report + matching registry entry -> `admitted`;
2. blocked P4C report -> `blocked` with `conformance_blocked`;
3. provider absent from registry -> `blocked` with `provider_not_in_registry`;
4. model absent from registry -> `blocked` with `model_not_in_registry`;
5. method unsupported -> `blocked` with `method_not_supported`;
6. method alias normalization reflected in admission record;
7. `requireCredentialMetadata=true` with no credential metadata ->
   `needs_operator_authorization`;
8. `liveExecutionAuthorized` is always false;
9. `traceId` is non-empty string;
10. no hardcoded provider is required for admission;
11. serialized record contains no test secret;
12. negative source assertion: no concrete provider import or network call;
13. (if P5-B included) `negotiated` result for directly supported method;
14. (if P5-B included) `fallback_available` when alias maps to supported method;
15. (if P5-B included) `blocked` when no supported or fallback method exists.

## Pre-Flight Checks

Codex dispatch preflight before commit:

- `python governance/compat/check_agent_operation_trace.py --base 4c888aa0 --head HEAD --enforce`;
- `python governance/compat/check_work_order_dispatch_quality.py --base 4c888aa0 --head HEAD --enforce`;
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 4c888aa0 --head HEAD`;
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
| 1 | Claude | Read authority chain and source owners | source-verified implementation plan |
| 2 | Claude | Implement `provider-adapter-admission.ts` (P5-A) | deterministic admission evaluator |
| 3 | Claude | Implement `provider-capability-negotiation.ts` (P5-B) or flag deferral if threshold risk | capability negotiation helper or split flag |
| 4 | Claude | Add fake-provider deterministic tests | admission and negotiation test coverage |
| 5 | Claude | Add additive barrel exports | `src/index.ts` additive only |
| 6 | Claude | Add GC-051 entries and regenerate aggregate | source/test registry coverage |
| 7 | Claude | Run required checks | command evidence |
| 8 | Claude | Author worker return | `COMPLETE_PENDING_REVIEW` packet |

## Evidence Requirements

Worker return must include:

- execution base head and final HEAD comparison;
- actual changed set (with P5-B deferral note if split);
- focused test and full module test results;
- GC-051 generator check result;
- worker fast gate result;
- diff hygiene result;
- negative-search results;
- Agent Operation Trace Block;
- explicit statement that no live provider call, credential read, runtime secret
  resolution, provider addition, provider preference, P5-C bridge mutation, or
  P4B-B release occurred.

## Work-Order Fulfillment Manifest

| Artifact | Required action | Owner |
|---|---|---|
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts` | create | Claude |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-negotiation.ts` | create OR flag deferral | Claude |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-admission.test.ts` | create | Claude |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | additive exports only | Claude |
| `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-adapter-admission.json` | create | Claude |
| `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-adapter-admission-tests.json` | create | Claude |
| `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-capability-negotiation.json` | create (or mark DEFERRED) | Claude |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | regenerate only | Claude |
| `docs/reviews/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_WORKER_RETURN_2026-06-15.md` | create | Claude |

Required proof literals in worker return:

- `COMPLETE_PENDING_REVIEW`;
- `WORKER_MUST_NOT_COMMIT`;
- `PROVIDER_AGNOSTIC`;
- `NO_NETWORK_CALL`;
- `NO_RUNTIME_SECRET_RESOLUTION`;
- `P4B_B_HOLD`;
- `P5_C_DEFERRED`.

## Negative Search And Collision Discipline

| Structured query | Search roots | Coverage | Same-token collision result | Disposition |
|---|---|---|---|---|
| `rg -n "AdapterAdmissionRecord\|admitProviderAdapter\|CapabilityNegotiationResult\|negotiateProviderCapability" EXTENSIONS/CVF_MODEL_GATEWAY docs/roadmaps docs/baselines docs/work_orders` | Model Gateway source/tests and governed planning docs | source, tests, docs | Planning-doc occurrences exist and are non-authoritative declarations of proposed symbols | Runtime definitions may be added only at the allowed P5 paths |
| `rg -n "fetch\(\|https?://\|resolveSecretForRuntime\|DASHSCOPE_API_KEY\|DEEPSEEK_API_KEY\|ALIBABA_API_KEY\|\.env\.local" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-negotiation.ts EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-admission.test.ts` | new P5 source and test | source/tests only | Provider URL and key tokens may exist in unrelated samples | New P5 files must produce zero matches |
| `rg -n "providers/alibaba\|providers/deepseek\|createAlibaba\|createDeepSeek" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-negotiation.ts EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-admission.test.ts` | new P5 source and test | source/tests only | Concrete adapter names exist elsewhere as samples | New P5 files must produce zero matches |
| `rg -n "provider-execution-bridge" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-negotiation.ts` | new P5 source only | source only | Bridge import may appear in P4C (read-only) | P5 admission may import bridge adapter type only as a type reference from P4C conformance report; must not call bridge execute |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order section | Disposition |
|---|---|---|
| Provider-agnostic admission record | Allowed Scope, Implementation Requirements | RELEASED |
| P4C conformance as required input | Source Verification Block, Implementation Requirements | RELEASED |
| Machine-readable admission statuses | New Runtime Symbols (P5-A) | RELEASED |
| Capability negotiation with reason codes | New Runtime Symbols (P5-B) | RELEASED (or SPLIT flag) |
| `liveExecutionAuthorized=false` in admission | Implementation Requirements | RELEASED |
| No hardcoded accepted provider IDs | Forbidden Scope, Negative Search | RELEASED |
| GC-051 coverage | Work-Order Fulfillment Manifest | RELEASED |
| Worker no-commit return | Return Contract | RELEASED |
| P4B-B held | Forbidden Scope and Legacy Disposition | NOT_RELEASED_WITH_REASON |
| P5-C deferred | Not Authorized, P5-C Deferral | NOT_RELEASED_WITH_REASON |

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
|---|---|
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Stable row | `MGW-001` |
| Current status | `PARTIAL_RECHECK_REQUIRED` |
| P5 contribution | Adds provider-agnostic adapter admission and capability negotiation above P4C conformance |
| Closure rule | P5 must not promote `MGW-001` to complete |
| P4B-B rule | Concrete live proof remains held and separate |

## Worker Autonomy / No-Question Rule

Claude must fix allowed-scope gate failures and rerun the relevant checks
without asking the operator. Ask the operator only if the fix would exceed
Allowed Scope, touch forbidden paths, consume secrets/quota, run live proof,
change risk level, mutate P5-C or P4B-B, or alter the claim boundary.

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
| AC1 | Admission result is provider-agnostic and contains no hardcoded accepted provider IDs | source review and tests |
| AC2 | Blocked P4C conformance report always blocks admission with `conformance_blocked` | deterministic tests |
| AC3 | Missing provider/model in registry blocks admission with explicit reason code | deterministic tests |
| AC4 | Unsupported method blocks admission with `method_not_supported` | deterministic tests |
| AC5 | Method alias normalization reflected in admission record | deterministic tests |
| AC6 | Admission output always has `liveExecutionAuthorized=false` | deterministic tests |
| AC7 | `traceId` is a non-empty string in every record | deterministic tests |
| AC8 | No source/test uses network, provider URL, real key, `.env.local`, concrete adapter import, or `resolveSecretForRuntime()` | negative search |
| AC9 | Type check, full module tests, GC-051 drift check, worker fast gate, and diff hygiene pass | command evidence |
| AC10 | Worker leaves HEAD unchanged | base/head evidence |
| AC11 | P5-B capability negotiation produces `negotiated`, `fallback_available`, or `blocked` with reason codes (or clearly deferred with split flag) | deterministic tests or deferral note |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime-foundation work. Public sync is not
authorized.

## Return Contract

Return one of:

- `COMPLETE_PENDING_REVIEW`;
- `BLOCKED_SCOPE_EXPANSION`;
- `BLOCKED_SOURCE_MISSING`;
- `BLOCKED_BASELINE_RED`.

The return must include actual changed paths, test/gate summaries, exact HEAD
comparison, negative-search results, P5-B deferral note if split, and an Agent
Operation Trace Block.

## Return-To-Orchestrator Conditions

- Return `COMPLETE_PENDING_REVIEW` only when AC1-AC10 (and AC11 if P5-B
  included) and all required gates pass.
- Return `BLOCKED_SOURCE_MISSING` when a cited current source owner is missing
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
- [ ] AC1-AC11 satisfied (AC11: P5-B included or deferred with explicit note)
- [ ] GC-051 entries and aggregate align
- [ ] Negative searches recorded
- [ ] Worker return includes required proof literals
- [ ] Worker leaves all artifacts uncommitted

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PENDING |
| Completion or reviewer artifact | `docs/reviews/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_COMPLETION_2026-06-15.md` | independent reviewer closure | PENDING |
| Roadmap state | `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_ROADMAP_2026-06-15.md` | P5 closed; P4B-B not released; P5-C deferred | PENDING |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated GC-051 aggregate includes P5 source and tests | PENDING |
| System loop interlock | no system-loop mutation authorized | deterministic Model Gateway admission only | N/A with reason |
| Session continuity | dedicated session-sync lane once material SHA exists | excluded from exact-manifest closure commit | N/A with reason |

## Operator Checkpoint

No operator pause is required inside allowed P5-A/P5-B remediation. Explicit
new operator authorization is required for P5-C, P4B-B, credentials, network,
provider binding, provider/model addition, package installation, public sync,
or changed risk/claim boundary.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude orchestrator, corrected by Codex reviewer |
| Provider or surface | Claude Code local workspace plus Codex local workspace |
| Session or invocation | 2026-06-15 P5 work order authoring and Codex dispatch correction |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read, Write, governance pattern inspection |
| Target paths | P5 GC-018 baseline, superseded Claude mirror work order, and active Codex work order |
| Allowed scope source | operator instruction 2026-06-15 + P5 roadmap `4c888aa0` |
| Before status evidence | HEAD `586aa56e`; P4C closed; P4B-B held; P5 roadmap ready |
| After status evidence | P5 GC-018, superseded Claude mirror work order, and active Codex work order authored, awaiting Codex dispatch commit |
| Diff evidence | pre-dispatch range `4c888aa0..HEAD` |
| Approval boundary | provider-agnostic deterministic P5-A/P5-B only |
| Claim boundary | no live provider, credential use, quota spend, provider preference, P5-C, or public claim |
| Agent type | Claude orchestrator |
| Invocation ID | `p5-provider-adapter-admission-work-order-2026-06-15` |
| Expected manifest | `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_FOR_CLAUDE_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_FOR_CODEX_2026-06-15.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_FOR_CLAUDE_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_FOR_CODEX_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This work order authorizes P5-A adapter admission record and P5-B capability
negotiation only. It does not authorize P4B-B, P5-C bridge admission boundary,
provider credentials, network calls, live proof, provider/model addition,
provider preference, EPF wiring, Strategy Layer, AI Gateway absorption, public
sync, production readiness, public readiness, raw memory release, co-work
product development, or autonomous mutation.
