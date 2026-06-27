# CVF Work Order - RTE1 Runtime Telemetry Receipt Expansion

Memory class: WORK_ORDER

docType: work_order

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-06

dispatchBaseHead: `3cef1b73`

executionBaseHead: `3cef1b73`

closureBaseHead: `3cef1b73`

Commit mode: WORKER_MAY_COMMIT

## Purpose

Add source-verified, secret-safe runtime telemetry to the existing
`/api/execute` governance evidence receipt.

## Scope / Target / Owner Boundary

Target: cvf-web receipt type, receipt builder, final response wiring, focused
tests, and RTE1 closure/session continuity artifacts.

Owner boundary: the implementation must stay inside the current receipt/final
response owner surfaces and must not refactor `route.ts` or alter provider,
policy, memory, approval, routing, prompt, or DLP behavior.

## Claim / Final / Verification Boundary

Final claim may state only that `/api/execute` receipts include bounded runtime
telemetry when the route has execution evidence. Verification must be
command-backed and secret-safe.

## Claim Boundary

RTE1 is an additive receipt evidence tranche only.

## 0. Surface Fidelity Gate

This work order is source-verified against current runtime owner files. The
worker may implement only the fields and owner surfaces verified below.

## 1. Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| GC-018 baseline | `docs/baselines/CVF_GC018_RTE1_RUNTIME_TELEMETRY_RECEIPT_EXPANSION_2026-06-06.md` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V16_2026-06-06.md` latest continuity note | ACCEPT |
| Legacy scan audit | `docs/audits/CVF_LIVE_EVIDENCE_MANIFEST_WIRING_LEGACY_SCAN_2026-06-06.md` lines 92-115 defer runtime telemetry fields | ACCEPT |
| Operator authorization | 2026-06-06 next tranche request with live-run permission | ACCEPT |

## 2. Transfer Objective

Implement RTE1 by adding a bounded `runtimeTelemetry` object to
`GovernanceEvidenceReceipt` and wiring it into `/api/execute` final responses.
The field must record only secret-safe telemetry:

- receipt schema version;
- provider latency in milliseconds when present;
- route elapsed time in milliseconds;
- token usage values already normalized by the route;
- estimated cost in USD from the existing pricing helper;
- governance trace entry count;
- explicit redaction and claim-boundary markers.

## 3. Source Packet

### Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `GovernanceEvidenceReceipt` owns response receipt fields | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | lines 99-123 | `GovernanceEvidenceReceipt` | AI runtime type contract | ACCEPT |
| `ExecutionResponse` exposes provider latency | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | lines 125-143 | `executionTime` | `ExecutionResponse` | ACCEPT |
| `ExecutionResponse` exposes normalized usage fields | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | lines 133-139 | `usage` | `ExecutionResponse` | ACCEPT |
| `BuildGovernanceEvidenceReceiptInput` owns receipt builder input fields | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 54-71 | `BuildGovernanceEvidenceReceiptInput` | receipt builder input | ACCEPT |
| `buildEvidenceReceipt` builds the receipt returned by routes | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 234-260 | `buildEvidenceReceipt` | receipt builder | ACCEPT |
| `buildGovernanceTrace` returns sanitized bounded trace entries | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 220-232 | `buildGovernanceTrace` | receipt trace builder | ACCEPT |
| `safeTraceText` redacts unsafe trace values | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 106-113 | `safeTraceText` | receipt trace sanitizer | ACCEPT |
| `/api/execute` final response owns final governance receipt construction | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts` | lines 133-149 | `governanceEvidenceReceipt` | `buildExecuteFinalResponse` | ACCEPT |
| `/api/execute` final response already resolves token usage | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts` | line 128 | `usage` | `buildExecuteFinalResponse` | ACCEPT |
| `/api/execute` final response already receives route start time | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts` | lines 39-46 | `routeStartedAtMs` | `BuildExecuteFinalResponseParams` | ACCEPT |
| `/api/execute` final response returns `governanceEvidenceReceipt` to callers | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts` | lines 356-399 | `governanceEvidenceReceipt` | final JSON response | ACCEPT |
| Token usage resolver exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-telemetry.ts` | lines 14-24 | `resolveTokenUsage` | execution telemetry helper | ACCEPT |
| Cost calculator exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/model-pricing.ts` | lines 29-40 | `calculateTokenCost` | model pricing helper | ACCEPT |
| Existing route governance trace test verifies secret-safe receipt trace behavior | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.governance-trace.test.ts` | lines 97-151 | `governanceTrace` | route receipt test | ACCEPT |
| Existing Alibaba live test pattern resolves key through helper and skips only when absent | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.rw1-finding-to-learning.alibaba.live.test.ts` | lines 36-39 | `resolveAlibabaApiKey` | live route test harness | ACCEPT |

### New Doc-Only Fields

No doc-only runtime field is being claimed as pre-existing source. RTE1
introduces `runtimeTelemetry` as a new runtime receipt field under this work
order.

## Current Runtime Freshness Verification

| Runtime surface | Freshness check | Disposition |
| --- | --- | --- |
| `/api/execute` final receipt owner | `route-final-response.ts` currently builds `governanceEvidenceReceipt`; RTE1 changes only this owner and the shared builder/type files | PASS |
| Provider registry surface | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are outside RTE1 because no provider-list, provider-routing, or model-capability behavior is changed | N/A with reason |
| Provider routing | `routingResult.decision`, `routedProvider`, and `model` remain existing inputs to final response; RTE1 only copies already-selected metadata into receipt telemetry | PASS |
| Runtime absence claim | RTE1 does not claim an absent provider registry, absent model registry, or hardcoded provider inventory | PASS |

## 4. Role Assignment

Codex acts as orchestrator, implementer, reviewer, and closer for this bounded
tranche. External worker dispatch is not required.

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| Orchestrator | Codex | Maintain GC-018 scope, gates, and continuity. |
| Implementer | Codex | Edit only allowed runtime/test files. |
| Reviewer | Codex | Verify secret-safe receipt fields and claim boundary. |
| Closer | Codex | Record evidence and update session state. |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V16_2026-06-06.md`
- `docs/baselines/CVF_GC018_RTE1_RUNTIME_TELEMETRY_RECEIPT_EXPANSION_2026-06-06.md`
- `docs/audits/CVF_LIVE_EVIDENCE_MANIFEST_WIRING_LEGACY_SCAN_2026-06-06.md`
- source files listed in the Source Verification Block

## Pre-Flight Checks

- Run pre-dispatch autorun gate before implementation.
- Run pre-implementation autorun gate after dispatch structure passes.
- Confirm working tree diff stays inside allowed RTE1 scope.

## Write Ownership

Allowed write owners are:

- receipt type contract and builder files listed in the GC-018 baseline;
- focused route/builder tests and one focused Alibaba live test;
- RTE1 completion and continuity artifacts.

Any public-sync, provider-routing, policy, prompt, memory, or storage change is
outside this work order.

## Execution Plan

1. Extend receipt type and builder input.
2. Add telemetry construction in final response from existing values.
3. Add focused deterministic tests.
4. Add focused live proof test if not already covered by a reusable owner test.
5. Run gates and record closure evidence.

## Evidence Requirements

Evidence must include changed files, deterministic test output, TypeScript
output, live proof result or diagnostic, and pre-closure gate result.

## Acceptance Criteria

- `runtimeTelemetry` is optional, typed, and additive.
- The field contains only numeric/enumerated/boolean metadata and explicit
  claim-boundary text.
- Cost is labeled as estimated.
- Existing receipt fields continue to work.
- Focused deterministic and live tests pass when a key is available.

## Review Gate

Reviewer must reject closure if the patch adds raw prompt/output capture,
changes provider/policy behavior, omits source-backed test evidence, or claims
cost optimization or production observability.

## Closure Checklist

- [x] Source scope remained within RTE1 allowed files.
- [x] Deterministic tests passed.
- [x] TypeScript check passed.
- [x] Live proof passed or diagnostic recorded.
- [x] Completion artifact records Public Export Disposition.

## Return Conditions

Return to orchestrator if source verification is invalid, required runtime
owner fields are absent, live proof shows a governance behavior regression, or
the implementation needs changes outside RTE1 scope.

## 5. Execution Instructions

1. Add typed `runtimeTelemetry` support to the existing
   `GovernanceEvidenceReceipt` contract.
2. Extend `BuildGovernanceEvidenceReceiptInput` and `buildEvidenceReceipt` so
   the field is optional and omitted unless a caller provides telemetry.
3. Build the telemetry object in `buildExecuteFinalResponse` from existing
   runtime values only: `aiResult.executionTime`, `routeStartedAtMs`,
   `resolveTokenUsage`, `calculateTokenCost`, and the resulting receipt trace
   count.
4. Keep the field summary-only and secret-safe. Do not persist raw prompt, raw
   output, provider key, hidden prompt, private memory, or raw provider payload.
5. Add focused deterministic tests for builder behavior and route receipt
   output.
6. Add or run a focused Alibaba live proof when a live key is available through
   the accepted environment helper.

## 6. Role Output Schema

Completion evidence must report:

- changed files;
- deterministic test command and result;
- live proof command and result, or a secret-safe diagnostic if no accepted key
  is available;
- receipt field sample containing only secret-safe metadata;
- claim boundary and next allowed move.

## 7. Dissent And Review Ledger

| Role | Concern | Resolution |
| --- | --- | --- |
| Reviewer | Cost telemetry can be misread as a pricing guarantee. | Field name must use estimated cost and claim boundary text. |
| Security | Runtime receipt must not leak prompt, output, key, or raw provider payload. | Field may contain only numeric telemetry, provider/model already present on receipt, trace count, and redaction marker. |
| Maintainability | `route.ts` is large and should not absorb this tranche. | Use `route-final-response.ts` and builder files; do not refactor `route.ts`. |

## 8. Integration Decision

Proceed with bounded implementation after pre-dispatch and pre-implementation
autorun gates pass. The new field is additive and optional.

## 9. Completion Evidence

Closure evidence:

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 3cef1b73 --head HEAD`: PASS.
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 3cef1b73 --head HEAD`: PASS.
- `npx vitest run src/lib/web-governance-envelope.test.ts src/app/api/execute/route.governance-trace.test.ts`: PASS, 20 tests.
- `npm run check`: PASS.
- `npx vitest run src/app/api/execute/route.rte1-runtime-telemetry.alibaba.live.test.ts --reporter verbose`: PASS, receipt `rcpt-env-mq2i7h03-ztjxy4`.
- Completion review:
  `docs/reviews/CVF_RTE1_RUNTIME_TELEMETRY_RECEIPT_EXPANSION_COMPLETION_2026-06-06.md`.

## 10. Claim Boundary

RTE1 proves only that existing `/api/execute` receipts can include bounded
runtime telemetry. It does not prove cost reduction, output-quality parity,
production observability, provider reliability, distributed tracing, hosted
readiness, public readiness, or third-party auditability.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_WO_RTE1_RUNTIME_TELEMETRY_RECEIPT_EXPANSION_2026-06-06.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_RTE1_RUNTIME_TELEMETRY_RECEIPT_EXPANSION_COMPLETION_2026-06-06.md` | completion review exists with verification table | PASS |
| Roadmap state | N/A with reason | RTE1 is GC-018 continuity-derived; no roadmap artifact owns this tranche | N/A with reason |
| Registry JSON | BLOCKED with reason | RTE1 has no corpus/search registry ownership; no registry JSON changed by this receipt-only tranche | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | RTE1 has no corpus/search registry ownership; no registry Markdown changed by this receipt-only tranche | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence digest created; focused live receipt sample is in completion review | N/A with reason |
| System loop interlock | N/A with reason | no system-loop route changed by RTE1 | N/A with reason |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V16_2026-06-06.md` | session sync follows material commit | PASS |

## Worker Autonomy / No-Question Rule

The worker must handle in-scope validation failures autonomously.
Escalation is required only for public-sync, external anchoring, production or
hosted readiness claims, risk-level changes, or claim-boundary changes.

## Operator Checkpoint

None for RTE1.

## Knowledge Absorption Blind-Spot Control Block

Prior absorption evidence resolved:

- `docs/audits/CVF_LIVE_EVIDENCE_MANIFEST_WIRING_LEGACY_SCAN_2026-06-06.md`
  explicitly deferred cost/latency/trace receipt fields to this lane.
- `docs/baselines/CVF_GC018_EXTERNAL_REVIEW_GAP4_GAP5_RUNTIME_DURABILITY_2026-06-06.md`
  already closed the first live operational metric and did not add receipt
  telemetry fields.

Detailed source reads completed:

- READ_DEEP: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- READ_DEEP: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`
- READ_DEEP: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-telemetry.ts`
- READ_DEEP: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/model-pricing.ts`
- READ_DEEP:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts`
- READ_DEEP:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.governance-trace.test.ts`
- READ_DEEP:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.rw1-finding-to-learning.alibaba.live.test.ts`

Normalization decision:

- Accepted now: bounded runtime receipt telemetry from existing route/provider
  values.
- Deferred: external trace service, immutable third-party anchor, provider cost
  billing reconciliation, and Learning Plane telemetry routing.
- Rejected for this batch: any raw trace replay or raw provider payload capture.

Adversarial role review:

- Reviewer: if cost is estimated from fallback pricing, the receipt must label
  it as an estimate. Verdict: required.
- Security: any telemetry field must be numerics/enums/booleans, not prompt or
  output text. Verdict: required.
- Runtime reviewer: route behavior must remain unchanged. Verdict: additive
  response field only.

Blind-spot delta:

- Reduced: route receipts can expose latency/cost/trace-count evidence for live
  runs.
- Remaining: independent audit replay and external anchoring still belong to
  separate product decisions.

## Roadmap-To-Work-Order Trace Matrix

N/A with reason: this work is derived from active GC-018 continuity and the
legacy scan follow-up route, not from a multi-task roadmap artifact.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private runtime receipt hardening. Public-facing telemetry or
cost evidence claims require a separate public-sync packet after private review.

Next action: implement and close RTE1 in private provenance scope.
