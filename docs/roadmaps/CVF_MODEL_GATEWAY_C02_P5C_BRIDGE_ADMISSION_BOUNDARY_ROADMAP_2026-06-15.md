# CVF Model Gateway C-02 P5-C Bridge Admission Boundary Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-15

rawMemoryReleased: false

Roadmap class: model-gateway-foundation

## Authorization / Decision

P5-A/P5-B closed at material commit `a4907f2c`. The session front door now
reads mode `model_gateway_c02_p5_closed_p4b_b_hold` and names P5-C as the
next recommended high-foundation roadmap.

The gap closed by P5-C: P5-A/P5-B produce a machine-readable
`AdapterAdmissionRecord`, but `ProviderExecutionBridge` currently accepts any
`ProviderExecutionAdapter` from its `adapters` Map without consulting an
admission record. A user-supplied adapter that has never been through P4C
conformance or P5-A admission can today reach `adapter.execute()` at bridge
line 152. P5-C closes this gap.

Decision: create a P5-C roadmap for a deterministic, provider-agnostic bridge
admission boundary that gates `adapter.execute()` behind an admitted
`AdapterAdmissionRecord`.

## Purpose

P4B-A established a deterministic `ProviderExecutionBridge` with injected
adapters. P4C established conformance evaluation. P5-A/P5-B established
admission records and capability negotiation. The remaining foundation gap is:

1. `ProviderExecutionBridge.execute()` consumes the injected adapter directly
   (bridge line 93-103) without requiring an admission record.
2. CVF has no bridge-side gate that rejects an adapter whose admission status
   is `"blocked"` or `"needs_operator_authorization"`.
3. There is no `BridgeAdmissionGuard` surface that combines the P5-A admission
   result with the bridge's adapter-selection step.

P5-C is valuable because it completes the admission chain: P4C -> P5-A
admission record -> P5-C bridge boundary -> (future) P4B-B live execution. Once
P5-C is in place, a live-proof lane can require a bridge that only calls
admitted adapters.

## Scope

### In Scope

- Define a `BridgeAdmissionGuard` interface (or function) that consumes an
  `AdapterAdmissionRecord` and returns `"pass"` or `"block"` with reason.
- Wire the guard into `ProviderExecutionBridge.execute()` at the adapter-
  selection step (bridge lines 93-103), before `adapter.execute()` is called.
- Ensure the guard check is provider-agnostic and uses only the admission
  record's `status` field - no hardcoded provider IDs in guard logic.
- Define a new bridge error class or receipt reason for `admission_blocked`.
- Keep `liveExecutionAuthorized=false` - P5-C does not open live proof.
- Preserve P4B-A bridge behavior for all non-admission error paths.
- Produce a `BridgeAdmissionBoundaryVersion` constant.
- Cover with deterministic tests using fake admission records.

### Out Of Scope

- Live provider/API calls, network, `fetch`, provider endpoints, `.env.local`,
  runtime secret access, quota spend, or live-run diagnostics.
- Choosing Alibaba, DeepSeek, OpenAI, or any provider as canonical.
- Adding a new provider or model.
- P4B-B concrete live proof.
- Changing `admitProviderAdapter()` or `ProviderAdapterConformanceReport`
  shape (P4C/P5-A owners, read-only).
- EPF wiring, Strategy Layer implementation, AI Gateway absorption, public
  sync, production readiness, or public readiness.
- Legacy folder scan or broad knowledge absorption.
- Changing `ProviderExecutionBridgeOptions` shape in a breaking way - guard
  wiring must be additive or injectable.

## Non-Goals

- Do not prove provider quality, cost, latency, availability, or live behavior.
- Do not build an out-of-band admission service or network endpoint.
- Do not grant autonomous admission authority to the bridge itself.
- Do not bypass P4C conformance or P5-A admission logic.

## Gap Analysis

| Gap | Location | P5-C closure |
|---|---|---|
| Bridge calls `adapter.execute()` without admission check | `provider-execution-bridge.ts` lines 93-152 | Add `BridgeAdmissionGuard` check before execute call |
| No bridge error for admission-blocked adapters | `buildShieldedErrorResult()` | Add `admission_blocked` error class to bridge error envelope |
| `AdapterAdmissionRecord` produced but not consumed by bridge | P5-A output; bridge ignores it | Bridge receives pre-computed admission record and guards on it |
| Live-proof lane has no upstream admission gate requirement | P4B-B still held | P5-C puts the gate in place so P4B-B can require it when live |

## Design Control Gate

| Control | P5-C decision |
|---|---|
| Foundation value | High: closes the last gap between P5-A admission evidence and bridge execution |
| Provider neutrality | Required: guard checks `record.status` only; no hardcoded provider IDs |
| Live boundary | `liveExecutionAuthorized=false` in all P5-C artifacts; P4B-B remains `HOLD` |
| Bridge backward compatibility | Guard is injectable; `ProviderExecutionBridgeOptions` change must be additive |
| Existing owner reuse | P5-A `AdapterAdmissionRecord`, P4B-A bridge `buildShieldedErrorResult` pattern, bridge error classes |
| Legacy disposition | cite `MGW-001`; no new legacy scan |
| Claim boundary | deterministic local bridge admission gate only |

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Bridge adapter lookup before execute | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | lines 93-103 | `this.adapters.get(providerId)` | `ProviderExecutionBridge.execute` | ACCEPT |
| Bridge calls adapter.execute | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | line 152 | `adapter.execute(...)` | `ProviderExecutionBridge.execute` | ACCEPT |
| Bridge shielded error builder exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | lines 243-267 | `buildShieldedErrorResult` | `ProviderExecutionBridge` | ACCEPT |
| Bridge options interface exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | lines 41-49 | `ProviderExecutionBridgeOptions` | provider execution bridge | ACCEPT |
| P5-A admission record type exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts` | line 34 | `AdapterAdmissionRecord` | provider adapter admission | ACCEPT |
| P5-A admission status type exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts` | line 21 | `AdapterAdmissionStatus` | provider adapter admission | ACCEPT |
| P5-A admitProviderAdapter exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts` | line 53 | `admitProviderAdapter` | provider adapter admission | ACCEPT |
| P4C conformance report type exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | line 35 | `ProviderAdapterConformanceReport` | P4C conformance types | ACCEPT |
| ProviderRegistry class exists (read-only boundary: guard consumes AdapterAdmissionRecord only) | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 30 | `ProviderRegistry` | provider registry | ACCEPT |
| PROVIDER_CAPABILITY_REGISTRY exists (read-only boundary: P5-A already consumed; guard must not re-evaluate) | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 42 | `PROVIDER_CAPABILITY_REGISTRY` | provider capability registry | ACCEPT |

## Proposed P5-C Design

### New surface: `provider-bridge-admission-guard.ts`

```ts
export type BridgeAdmissionVerdict = "pass" | "block";

export interface BridgeAdmissionGuardResult {
  verdict: BridgeAdmissionVerdict;
  admissionStatus: AdapterAdmissionStatus;
  reasonCodes: readonly string[];
  reasons: readonly string[];
}

export function checkBridgeAdmission(
  record: AdapterAdmissionRecord,
): BridgeAdmissionGuardResult
```

Rule: `verdict = "pass"` only when `record.status === "admitted"`. All other
statuses produce `verdict = "block"`.

### Bridge wiring change

In `ProviderExecutionBridge.execute()`, after the adapter identity check
(current lines 93-103) and before `adapter.execute()` (current line 152),
add:

```ts
// P5-C: bridge admission guard
const admissionRecord = this.admissionRecords?.get(providerId);
if (admissionRecord) {
  const guardResult = checkBridgeAdmission(admissionRecord);
  if (guardResult.verdict === "block") {
    return this.buildShieldedErrorResult(
      traceId, "admission_blocked",
      "Adapter admission blocked", providerId, modelId, false,
    );
  }
}
```

`admissionRecords` is an optional `Map<string, AdapterAdmissionRecord>` added
to `ProviderExecutionBridgeOptions`. When absent, the bridge behaves exactly as
before (backward compatible). When present and the adapter is `"admitted"`,
execution proceeds. When present and the adapter is `"blocked"` or
`"needs_operator_authorization"`, the bridge returns `admission_blocked`.

This design keeps the guard injectable and non-breaking.

### Bridge error class addition

Add `"admission_blocked"` to the `GatewayErrorClass` union in
`unified-gateway-interface-contract.ts` (additive only, no breaking change).

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
|---|---|
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Stable row | `MGW-001` |
| Current status | `PARTIAL_RECHECK_REQUIRED` |
| P5-C contribution | Closes bridge admission gap above P5-A; prepares live-proof lane for P4B-B |
| Closure rule | P5-C must not promote `MGW-001` to complete |
| P4B-B rule | Concrete live proof remains held and separate |

No new legacy scan is authorized by this roadmap.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | `BridgeAdmissionGuard` check is provider-agnostic; no hardcoded provider IDs in guard logic | source review and tests |
| AC2 | Bridge rejects adapter with `"blocked"` admission record; returns `admission_blocked` error | deterministic tests |
| AC3 | Bridge rejects adapter with `"needs_operator_authorization"` record | deterministic tests |
| AC4 | Bridge proceeds normally when `admissionRecords` is absent (backward compatible) | deterministic tests |
| AC5 | Bridge proceeds when admission record status is `"admitted"` | deterministic tests |
| AC6 | `liveExecutionAuthorized=false` - no credential, network, or live call in P5-C files | negative search |
| AC7 | `ProviderExecutionBridgeOptions` change is additive only; existing tests remain green | full module test suite |
| AC8 | `"admission_blocked"` is a new additive error class; no existing error class removed | source review |
| AC9 | Source and test files remain below governed file-size thresholds | file-size guard |
| AC10 | Model Gateway type check and full test suite pass | command evidence |
| AC11 | GC-051 entries added for new governed source/test files | registry drift check |

## Verification

Future P5-C implementation work order must require:

- `npm run check` in `EXTENSIONS/CVF_MODEL_GATEWAY`.
- `npm test -- --run` in `EXTENSIONS/CVF_MODEL_GATEWAY`.
- `python governance/compat/generate_corpus_scan_registry.py --check`.
- `python governance/compat/run_worker_return_fast_gate.py`.
- `git diff --check`.
- Negative search for concrete provider preference, network calls, credential
  access, and live-proof vocabulary in new P5-C source/test files.

## Work Plan

| Step | Owner | Output | Stop condition |
|---|---|---|---|
| 1 | Codex | P5-C roadmap (this document) | roadmap gate failure |
| 2 | Codex | GC-018 baseline and source-verified Codex work order | dispatch-quality failure |
| 3 | Codex | deterministic P5-C implementation under `WORKER_MAY_COMMIT` | forbidden scope or source mismatch |
| 4 | Codex | focused tests, GC-051 entries, completion review, material commit | blocking design or governance finding |
| 5 | Codex | session/handoff sync if needed | active-session state failure |

## Risk And Corrective Action

| Risk | Control |
|---|---|
| Bridge guard becomes provider-specific | hard negative search and fake-record tests |
| Guard duplicates P5-A admission logic | guard consumes record; does not re-evaluate capability |
| `ProviderExecutionBridgeOptions` change breaks existing tests | additive optional field only; test suite remains green |
| `liveExecutionAuthorized` slip into P5-C | explicit `false` literal in all P5-C artifacts; P4B-B still held |
| `admission_blocked` error class conflicts with existing union | additive union extension; no removal |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance Model Gateway roadmap. No public-sync batch is
authorized.

## Claim Boundary

This roadmap defines the P5-C bridge admission boundary direction only. It does
not implement P5-C, dispatch Codex, authorize live provider/API calls, read
credentials, add providers/models, wire EPF, implement Strategy Layer, absorb
AI Gateway, public-sync, or claim production/public readiness.

## GFC-T3 Closure Note (2026-06-18)

This roadmap is closed bounded per GFC-T3 Roadmap State Hygiene Remediation
(work order `docs/work_orders/CVF_AGENT_WORK_ORDER_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_FOR_CLAUDE_2026-06-18.md`).
Closure evidence: `docs/reviews/CVF_MODEL_GATEWAY_C02_P5C_BRIDGE_ADMISSION_BOUNDARY_COMPLETION_2026-06-15.md`
(confirmed on disk); guard source `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-bridge-admission-guard.ts`
exists on disk confirming implementation closure. P5C was re-verified and promoted from
`UNDETERMINED` to confirmed-stale for this dispatch. Status line updated from
`ROADMAP_READY_FOR_GC018` to `ROADMAP_CLOSED_PASS_BOUNDED` by GFC-T3 worker.

## Acceptance Receipt Assertion Matrix

| Acceptance criterion | Required value | Observed value | Status |
|---|---|---|---|
| Roadmap Status: line | `ROADMAP_CLOSED_PASS_BOUNDED` | `ROADMAP_CLOSED_PASS_BOUNDED` (updated by GFC-T3 worker) | PASS |
| GFC-T3 Closure Note present | section present | `## GFC-T3 Closure Note (2026-06-18)` appended | PASS |
| Closure evidence on disk | `docs/reviews/CVF_MODEL_GATEWAY_C02_P5C_BRIDGE_ADMISSION_BOUNDARY_COMPLETION_2026-06-15.md` exists | Test-Path returned TRUE before edit | PASS |
| HEAD unchanged | `24848d66` | `24848d66` (no commit by worker) | PASS |

## Current Runtime Freshness Verification

NOT_APPLICABLE_WITH_REASON: this roadmap's GFC-T3 closure note adds governance metadata only; no runtime source symbols were modified or introduced. Guard source `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-bridge-admission-guard.ts` exists on disk confirming implementation was pre-existing.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_FOR_CLAUDE_2026-06-18.md` | GFC-T3 work order authorizes this status-line change; GC-018 baseline approves scope (P5C re-verified from UNDETERMINED) | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_PACKET_2026-06-18.md` | worker packet Status: COMPLETE_PENDING_REVIEW; this row marked REMEDIATED | PASS |
| Roadmap state | `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P5C_BRIDGE_ADMISSION_BOUNDARY_ROADMAP_2026-06-15.md` | `Status: ROADMAP_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | governance-doc-only tranche | no GC-051 registry mutation authorized or required | BLOCKED with reason: governance-doc-only status remediation |
| Registry Markdown | governance-doc-only tranche | no registry markdown update authorized or required | BLOCKED with reason: governance-doc-only status remediation |
| External evidence digest | all evidence is repo-local and git-tracked | no external artifacts or digests needed | N/A with reason |
| System loop interlock | no runtime system loop required | no API interlock needed for governance status remediation | N/A with reason |
| Session continuity | session mode unchanged | no session state file modification authorized for GFC-T3 worker | N/A with reason |
| Tranche completion review | `docs/reviews/CVF_MODEL_GATEWAY_C02_P5C_BRIDGE_ADMISSION_BOUNDARY_COMPLETION_2026-06-15.md` | file exists on disk; guard source `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-bridge-admission-guard.ts` confirmed | PASS |
| Public-sync | N/A with reason: private provenance, `DEFERRED_PRIVATE_ONLY` | N/A | N/A with reason |
