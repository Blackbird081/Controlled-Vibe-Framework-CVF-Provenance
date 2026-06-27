# CVF Agent Work Order: Model Gateway C-02 P5 Provider Adapter Admission And Capability Negotiation For Codex

Memory class: FULL_RECORD

rawMemoryReleased: false

Date: 2026-06-15

Status: CLOSED_PASS_BOUNDED

Worker / Implementer: Codex

Orchestrator: Codex

Reviewer / closer: Codex, with machine gates

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: 586aa56e

executionBaseHead: fbbec2e4

closureBaseHead: fbbec2e4

riskCeiling: R1_BOUNDED_NO_NETWORK

completionReviewPath:
`docs/reviews/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_COMPLETION_2026-06-15.md`

## Purpose

Provide a Codex-executable implementation packet for P5-A adapter admission
record and P5-B capability negotiation. Codex implements, tests, commits, and
closes this tranche autonomously under the same boundary constraints as the
Claude work order - provider-agnostic, no-network, no-secret, no bridge
mutation, no P5-C, no P4B-B release.

Codex may commit directly. No separate Claude worker phase is required.

## 1. Mission

Implement the deterministic P5 provider adapter admission record
(`provider-adapter-admission.ts`) and capability negotiation helper
(`provider-capability-negotiation.ts`) inside `EXTENSIONS/CVF_MODEL_GATEWAY`.

Constraints:
- consume P4C `ProviderAdapterConformanceReport` as a required input to admission;
- produce machine-readable admission record with status enum, reason codes, and
  trace fields;
- negotiate provider/model/method capability using existing method-gate helpers
  only - do not duplicate their logic;
- never hardcode accepted provider IDs, call network, read secrets, or invoke
  any adapter method.

Split decision: if `provider-adapter-admission.ts` would exceed 300L, implement
P5-A only and flag P5-B for a separate dispatch in the completion review.

## 2. Authority Chain

- Operator instruction: 2026-06-15, authorize P5 roadmap and dispatch.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.
- P4C completion review:
  `docs/reviews/CVF_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_COMPLETION_2026-06-15.md`.
- P5 roadmap:
  `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_ROADMAP_2026-06-15.md`.
- GC-018:
  `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_2026-06-15.md`.

Authority boundary: P5-A adapter admission record and P5-B capability
negotiation only. P4B-B live proof, P5-C bridge mutation, and all parked
lanes remain held and are not released by this work order.

## 3. Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Orchestrator | Codex | scopes, dispatches, and keeps boundary |
| Implementer | Codex | source, tests, GC-051 entries, aggregate, completion review |
| Reviewer / closer | Codex plus machine gates | inspect real diff, run gates, commit, session sync |
| Operator | Human | any live credential, P5-C authorization, scope expansion |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake summary | Operator authorized Claude to create a Codex work order; Codex must audit and execute if gates pass |
| Scope classification | Bounded R1 Model Gateway foundation implementation |
| Risk sensitivity | No public sync, provider call, live proof, secret use, bridge mutation, provider preference, production claim, or readiness claim |
| Selected role route | `SINGLE_AGENT_MULTI_ROLE_CODEX` |
| Role separation basis | Codex executes implementation and reviewer duties, with machine gates and separate material/session commits |
| Escalation condition | Stop for P4B-B, P5-C, network, credential, concrete provider binding, provider addition, package install, destructive action, or scope expansion |

## Single-Agent Multi-Role Control Block

| Field | Control |
|---|---|
| Role separation ledger | Codex records dispatch correction, implementation, review, material commit, pre-closure, and session-sync as distinct steps |
| Evidence basis independent of memory | Source diff, tests, GC-051 generator, reviewer-fast, pre-closure gate, and git status are required evidence |
| Self-review boundary | Independent external review is not claimed; self-review is bounded by machine gates and explicit completion review evidence |
| Escalation conditions | Stop for operator authorization if P4B-B, P5-C, live credential, network, provider binding, package install, destructive action, public sync, or risk expansion appears |
| Gate sequence | pre-dispatch before dispatch commit; focused tests and reviewer-fast before material commit; pre-closure on material range; session-sync steward before continuity commit |

## 4. Required First Reads

| File | Required use |
|---|---|
| `AGENTS.md` | active governance |
| `CVF_SESSION_MEMORY.md` | current mode and boundary |
| `AGENT_HANDOFF_V19_2026-06-15.md` | active handoff and parked lanes |
| P5 roadmap | design, tranche split decision, acceptance criteria |
| P5 GC-018 | authorization and not-authorized list |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | P4C types consumed as admission input |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | adapter contract shape |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | existing helpers to reuse |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | static registry and alias map |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | barrel for additive exports |

## 5. Allowed Scope

Codex may create or modify only:

| Path | Action |
|---|---|
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts` | create |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-negotiation.ts` | create (or flag deferral if P5-A hits 300L) |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-admission.test.ts` | create |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | additive barrel exports only |
| `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-adapter-admission.json` | create |
| `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-adapter-admission-tests.json` | create |
| `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-capability-negotiation.json` | create (or mark DEFERRED) |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | regenerate via generator only |
| `docs/reviews/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_COMPLETION_2026-06-15.md` | create |
| `AGENT_HANDOFF_V19_2026-06-15.md` | session-sync update once material SHA exists |
| `CVF_SESSION_MEMORY.md` | session-sync update once material SHA exists |
| `CVF_SESSION/state/entries/nextAllowedMove.json` | session-sync update |
| `CVF_SESSION/state/entries/lastUpdated.json` | session-sync update |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | session-sync regeneration |

## Write Ownership

Write ownership is exactly the Allowed Scope table above. All other existing
source files are read-only, including `provider-adapter-conformance.ts` (P4C
owner), `provider-execution-bridge.ts` (bridge execute path), and all
governance checker/gate files.

## 6. Forbidden Scope And Stop Conditions

Stop before:

- reading `.env.local` or resolving a runtime credential;
- calling `CredentialBoundary.resolveSecretForRuntime()`;
- importing, modifying, or invoking concrete provider adapters;
- hardcoding Alibaba, DeepSeek, or any provider as a canonically accepted ID;
- using `fetch`, HTTP clients, provider URLs, or any network;
- modifying `provider-execution-bridge.ts` execute logic (P5-C boundary);
- modifying `provider-adapter-conformance.ts` (read-only P4C owner);
- modifying existing method-gate or capability-registry source outside
  additive `index.ts` exports;
- installing new packages or modifying `package.json`;
- changing EPF, Strategy Layer, AI Gateway, OCR, public-sync, or production
  readiness claims.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| P4C conformance status type | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | line 24 | `ProviderAdapterConformanceStatus` | P4C conformance types | ACCEPT |
| P4C conformance input type | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | line 26 | `ProviderAdapterConformanceInput` | P4C conformance types | ACCEPT |
| P4C conformance report type | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | line 35 | `ProviderAdapterConformanceReport` | P4C conformance types | ACCEPT |
| P4C liveExecutionAuthorized field | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | line 44 | `liveExecutionAuthorized` | ProviderAdapterConformanceReport | ACCEPT |
| P4C evaluator function | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | line 54 | `evaluateProviderAdapterConformance` | P4C conformance evaluator | ACCEPT |
| Provider adapter contract | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | line 37 | `ProviderExecutionAdapter` | provider execution bridge | ACCEPT |
| Method normalization helper | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | line 24 | `normalizeProviderMethodName` | provider method gate | ACCEPT |
| Capability lookup helper | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | line 46 | `findProviderCapability` | provider method gate | ACCEPT |
| Supported method list helper | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | line 89 | `listRegistrySupportedMethods` | provider method gate | ACCEPT |
| Static capability registry | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 42 | `PROVIDER_CAPABILITY_REGISTRY` | provider capability registry | ACCEPT |
| Barrel export file | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | line 1 | additive barrel | index barrel | ACCEPT |

## 7. New Runtime Symbols

### P5-A - Adapter Admission Record (`provider-adapter-admission.ts`)

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

Logic:
1. If `conformanceReport.status === "blocked"` -> `"blocked"` + `conformance_blocked`.
2. Lookup provider/model via `findProviderCapability`; missing -> `"blocked"` +
   `provider_not_in_registry` or `model_not_in_registry`.
3. Check method support via normalized method and `listRegistrySupportedMethods`;
   unsupported -> `"blocked"` + `method_not_supported`.
4. If `options.requireCredentialMetadata` and
   `!conformanceReport.adapterExecutionAuthorized` ->
   `"needs_operator_authorization"` + `credential_metadata_required`.
5. All checks pass -> `"admitted"`.
6. Always: `liveExecutionAuthorized: false`.
7. Generate `traceId` as deterministic string (e.g. `crypto.randomUUID()` or
   `Date.now().toString(36)` - no network); `admissionTimestamp` as ISO string.
8. Never call `adapter.execute()` or any adapter method.

### P5-B - Capability Negotiation (`provider-capability-negotiation.ts`)

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

Logic:
1. Normalize `requestedMethod` via `normalizeProviderMethodName`.
2. Lookup supported methods via `listRegistrySupportedMethods`.
3. If requested method (or normalized form) is directly supported -> `"negotiated"`.
4. If normalized alias differs from original and alias is supported ->
   `"negotiated"` with `effectiveMethod = normalizedMethod`.
5. If `"complete"` requested but only `"chat"` supported -> `"fallback_available"`
   with `effectiveMethod = "chat"`.
6. Otherwise -> `"blocked"` with reason codes.
7. No provider-specific branching. No hardcoded provider IDs in logic.

## 8. Required Deterministic Tests (`provider-adapter-admission.test.ts`)

Minimum 15 cases:

| # | Description | Expected |
|---|---|---|
| 1 | Conformant P4C report + matching registry entry | `admitted` |
| 2 | Blocked P4C report | `blocked` + `conformance_blocked` |
| 3 | Provider absent from registry | `blocked` + `provider_not_in_registry` |
| 4 | Model absent from registry | `blocked` + `model_not_in_registry` |
| 5 | Method unsupported after normalization | `blocked` + `method_not_supported` |
| 6 | Method alias -> normalization reflected in `normalizedMethod` | `admitted` with correct `normalizedMethod` |
| 7 | `requireCredentialMetadata=true`, no credential metadata | `needs_operator_authorization` |
| 8 | `liveExecutionAuthorized` always false | assert `=== false` on every record |
| 9 | `traceId` non-empty string | assert truthy |
| 10 | No hardcoded provider required for conformance | fake provider name passes when registry matches |
| 11 | Serialized record contains no test secret | assert no token-pattern match |
| 12 | Negative: no concrete provider import or network call in source | `rg` assertion |
| 13 | P5-B: `negotiated` for directly supported method | `CapabilityNegotiationStatus === "negotiated"` |
| 14 | P5-B: `fallback_available` when `"complete"` requested and `"chat"` supported | status + `effectiveMethod = "chat"` |
| 15 | P5-B: `blocked` when no supported or fallback method exists | status + reason codes non-empty |

## 9. Pre-Flight Checks

Before any edit:

```powershell
git rev-parse --short HEAD   # capture executionBaseHead
git status --short            # confirm clean tree
python governance/compat/check_active_session_state.py --enforce
```

After implementation, before commit:

```powershell
npm run check                 # in EXTENSIONS/CVF_MODEL_GATEWAY
npm test -- --run             # in EXTENSIONS/CVF_MODEL_GATEWAY
python governance/compat/generate_corpus_scan_registry.py --check
python governance/compat/run_worker_return_fast_gate.py
git diff --check
```

Pre-dispatch autorun gate (Codex runs before material commit):

```powershell
python governance/compat/check_agent_operation_trace.py --base 586aa56e --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 586aa56e --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 586aa56e --head HEAD
```

Pre-closure autorun gate (Codex runs once material SHA exists, before session sync):

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 586aa56e --head HEAD
```

## 10. Execution Plan

| Step | Action | Output |
|---|---|---|
| 1 | Read Required First Reads | source-verified plan confirmed |
| 2 | Capture `executionBaseHead`; confirm clean tree | `git rev-parse --short HEAD` |
| 3 | Create `provider-adapter-admission.ts` (P5-A) | deterministic admission evaluator |
| 4 | Create `provider-capability-negotiation.ts` (P5-B) or flag deferral | capability negotiation helper or deferral note |
| 5 | Create `tests/provider-adapter-admission.test.ts` | 15 deterministic test cases |
| 6 | Add additive barrel exports to `src/index.ts` | new P5-A/P5-B exports |
| 7 | Create GC-051 entry JSON files and regenerate aggregate | registry coverage |
| 8 | Run all pre-flight checks; fix in-scope failures | command evidence |
| 9 | Run pre-dispatch autorun gate | gate PASS |
| 10 | Commit material artifacts | material commit SHA recorded |
| 11 | Run pre-closure autorun gate | gate PASS |
| 12 | Author completion review | `CLOSED_PASS_BOUNDED` artifact |
| 13 | Update session continuity (handoff, session memory, state entries) in a separate session-sync commit | front-door sync |

## Negative Search And Collision Discipline

| Structured query | Search roots | Coverage | Same-token collision result | Disposition |
|---|---|---|---|---|
| `rg -n "AdapterAdmissionRecord\|admitProviderAdapter\|CapabilityNegotiationResult\|negotiateProviderCapability" EXTENSIONS/CVF_MODEL_GATEWAY docs/roadmaps docs/baselines docs/work_orders` | `EXTENSIONS/CVF_MODEL_GATEWAY`, `docs/roadmaps`, `docs/baselines`, `docs/work_orders` | source, tests, docs | Planning-doc occurrences are non-authoritative proposed-symbol declarations | Runtime definitions may be added only in P5 allowed source paths |
| `rg -n "fetch\(\|https?://\|resolveSecretForRuntime\|DASHSCOPE_API_KEY\|DEEPSEEK_API_KEY\|\.env\.local" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-negotiation.ts EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-admission.test.ts` | new P5 source and test files only | source/tests | Same-token occurrences in unrelated provider samples are non-authoritative collisions | New P5 files must be absent for these tokens; unrelated collisions are not binding |
| `rg -n "providers/alibaba\|providers/deepseek\|createAlibaba\|createDeepSeek" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-negotiation.ts EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-admission.test.ts` | new P5 source and test files only | source/tests | Concrete adapter names may occur elsewhere as sample/provider-specific code | New P5 files must be absent for these tokens; unrelated collisions are not binding |

Run these searches against new P5 files only; record exact output in completion review:

```bash
# No network, secret, or provider URL
rg -n "fetch\(|https?://|resolveSecretForRuntime|DASHSCOPE_API_KEY|DEEPSEEK_API_KEY|\.env\.local" \
  EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts \
  EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-negotiation.ts \
  EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-admission.test.ts

# No concrete provider import
rg -n "providers/alibaba|providers/deepseek|createAlibaba|createDeepSeek" \
  EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts \
  EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-negotiation.ts \
  EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-admission.test.ts
```

Expected result for both: zero matches (outside the search-query text itself).

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
|---|---|
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Row | `MGW-001` |
| Current status | `PARTIAL_RECHECK_REQUIRED` |
| P5 contribution | Adds provider-agnostic admission record and capability negotiation above P4C conformance |
| Closure rule | P5 must not promote `MGW-001` to complete |
| P4B-B rule | Concrete live proof remains held and separate |

## Evidence Requirements

Codex must record these evidence classes in the completion review:

- execution base head and material commit SHA;
- actual changed set and exact manifest comparison;
- focused and full Model Gateway test results;
- GC-051 generator check result;
- worker-return fast gate result;
- pre-closure autorun result on the material range;
- diff hygiene result;
- negative-search results for network, secret, provider URL, and concrete
  adapter imports;
- explicit statement that no live provider call, credential read, runtime secret
  resolution, provider addition, provider preference, P5-C bridge mutation, or
  P4B-B release occurred.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order section | Disposition |
|---|---|---|
| Provider-agnostic admission record | Allowed Scope, New Runtime Symbols | RELEASED |
| P4C conformance as required input | Source Verification Block, Implementation Logic | RELEASED |
| Machine-readable admission statuses | New Runtime Symbols (P5-A) | RELEASED |
| Capability negotiation with reason codes | New Runtime Symbols (P5-B) | RELEASED or SPLIT flag |
| `liveExecutionAuthorized=false` always | Implementation Logic | RELEASED |
| No hardcoded accepted provider IDs | Forbidden Scope, Negative Search | RELEASED |
| GC-051 coverage | Allowed Scope, Execution Plan | RELEASED |
| P4B-B held | Forbidden Scope | NOT_RELEASED_WITH_REASON |
| P5-C deferred | Forbidden Scope | NOT_RELEASED_WITH_REASON |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Codex may create new P5 source, tests, and
GC-051 entries; add additive barrel exports; regenerate the corpus registry
aggregate; author the completion review; and update session-continuity files
once material SHA exists. No checker, guard, hook, or unrelated governance file
may be changed in this batch.

Protected paths (Codex must include in completion review Expected manifest):

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-negotiation.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-admission.test.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
- `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-adapter-admission.json`
- `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-adapter-admission-tests.json`
- `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-capability-negotiation.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/reviews/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_COMPLETION_2026-06-15.md`
- `AGENT_HANDOFF_V19_2026-06-15.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/state/entries/lastUpdated.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

Operator authorization: operator confirmed P5 dispatch on 2026-06-15.

Rollback boundary: if P5 gates fail, revert only this P5 material batch. Do not
revert P4C material commit `8d8f0871`, P4C closure-doc commit `64a80684`,
P5 roadmap commit `4c888aa0`, or session-sync commit `586aa56e`.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Admission evaluator is provider-agnostic; no hardcoded accepted provider IDs | source review + negative search |
| AC2 | Blocked P4C report always blocks admission with `conformance_blocked` | tests case 2 |
| AC3 | Missing provider/model blocks admission with explicit reason code | tests cases 3-4 |
| AC4 | Unsupported method blocks with `method_not_supported` | test case 5 |
| AC5 | Method alias normalization reflected in `normalizedMethod` field | test case 6 |
| AC6 | `liveExecutionAuthorized=false` in every record | test case 8 |
| AC7 | `traceId` is a non-empty string | test case 9 |
| AC8 | No network, secret, provider URL, or concrete adapter import in P5 files | negative search |
| AC9 | Type check, full module tests, GC-051 drift check, worker fast gate, diff hygiene all PASS | command evidence |
| AC10 | Completion review records execution base head and material commit SHA | completion review |
| AC11 | P5-B negotiation covers `negotiated`, `fallback_available`, `blocked` (or explicit deferral note) | tests cases 13-15 or deferral |

## Worker Autonomy / No-Question Rule

Codex must fix allowed-scope gate failures and rerun the relevant checks
without asking the operator. Ask the operator only if the fix would exceed
Allowed Scope, touch forbidden paths, consume secrets/quota, run live proof,
change risk level, mutate P5-C or P4B-B, or alter the claim boundary.

## Review Gate

Codex must inspect the real diff, verify source/test behavior, rerun focused
and governance gates, author the completion review, commit material artifacts,
run committed-range pre-closure, and sync session state in a separate commit if
the next allowed move changes.

Worker-authored or self-authored PASS prose is not independent evidence unless
it is backed by command output, committed diff evidence, or machine-gate output.

## Closure Checklist

- [x] Execution base head captured
- [x] Source verification refreshed against execution head
- [x] Allowed scope respected
- [x] Forbidden scope avoided
- [x] AC1-AC11 satisfied, or AC11 explicitly deferred with split reason
- [x] GC-051 entries and aggregate align
- [x] Negative searches recorded
- [x] Completion review authored
- [x] Material commit created
- [x] Material-range pre-closure gate passed
- [x] Session-sync commit separated from material exact manifest if continuity changes

## Return-To-Orchestrator Conditions

Codex may close as `CLOSED_PASS_BOUNDED` only when AC1-AC10 and AC11 pass, or
when P5-B is explicitly deferred with a source-backed split reason. Return or
stop as `BLOCKED_SOURCE_MISSING` if a cited source owner is missing or
materially changed at execution HEAD. Stop as `BLOCKED_SCOPE_EXPANSION` before
any forbidden action.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_COMPLETION_2026-06-15.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion review | `docs/reviews/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_COMPLETION_2026-06-15.md` | independent reviewer closure | PASS |
| Roadmap state | `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_ROADMAP_2026-06-15.md` | P5-A/P5-B closed; P4B-B not released; P5-C deferred | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 aggregate includes P5 source and tests | PASS |
| Registry Markdown | `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-adapter-admission.json`; `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-adapter-admission-tests.json`; `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-capability-negotiation.json`; `docs/corpus-intelligence/registry/entries/model-gateway-provider-method-contract.json`; `docs/corpus-intelligence/registry/entries/model-gateway-provider-method-gate.json` | GC-051 entry sources and generated aggregate updated | PASS |
| External evidence digest | N/A | N/A with reason: no external evidence digest consumed or produced | N/A with reason |
| Session continuity | dedicated session-sync lane once material SHA exists | split from exact-manifest material commit | N/A with reason |
| System loop interlock | no interlock mutation authorized | deterministic Model Gateway admission only | N/A with reason |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |

## Operator Checkpoint

No operator pause required inside allowed P5-A/P5-B implementation. Explicit
new operator authorization required for P5-C, P4B-B, credentials, network,
provider binding, package installation, public sync, or changed risk boundary.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-15 P5 implementation and closure |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch, npm, governance scripts |
| Target paths | P5 source, tests, registry entries, aggregate, completion review, and this work order |
| Allowed scope source | operator instruction 2026-06-15 + P5 roadmap `4c888aa0` + P5 GC-018 |
| Before status evidence | executionBaseHead `fbbec2e4`; P5 dispatched to Codex; P4B-B held |
| After status evidence | P5-A/P5-B implemented and closure packet authored |
| Diff evidence | material range `fbbec2e4..HEAD` before commit |
| Approval boundary | provider-agnostic deterministic P5-A/P5-B only |
| Claim boundary | no live provider, credential use, quota spend, provider preference, P5-C, or public claim |
| Agent type | Codex implementer/reviewer/closer |
| Invocation ID | `p5-provider-adapter-admission-codex-implementation-2026-06-15` |
| Expected manifest | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-negotiation.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-admission.test.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`; `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-adapter-admission.json`; `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-adapter-admission-tests.json`; `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-capability-negotiation.json`; `docs/corpus-intelligence/registry/entries/model-gateway-provider-method-contract.json`; `docs/corpus-intelligence/registry/entries/model-gateway-provider-method-gate.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/reviews/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_COMPLETION_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_FOR_CODEX_2026-06-15.md` |
| Actual changed set | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-negotiation.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-admission.test.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`; `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-adapter-admission.json`; `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-adapter-admission-tests.json`; `docs/corpus-intelligence/registry/entries/model-gateway-c02-p5-provider-capability-negotiation.json`; `docs/corpus-intelligence/registry/entries/model-gateway-provider-method-contract.json`; `docs/corpus-intelligence/registry/entries/model-gateway-provider-method-gate.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/reviews/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_COMPLETION_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_FOR_CODEX_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime-foundation work. Public sync is not
authorized.

## Claim Boundary

This work order authorizes Codex to implement P5-A adapter admission record and
P5-B capability negotiation. It does not authorize P4B-B, P5-C bridge admission
boundary, provider credentials, network calls, live proof, provider/model
addition, provider preference, EPF wiring, Strategy Layer, AI Gateway
absorption, public sync, production readiness, public readiness, raw memory
release, co-work product development, or autonomous mutation beyond the Allowed
Scope table.
