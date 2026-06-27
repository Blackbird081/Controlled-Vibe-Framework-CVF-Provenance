# CVF Work Order - RTA1 Receipt Trace Anchor

Memory class: WORK_ORDER

docType: work_order

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-06

dispatchBaseHead: `dcb06f0e`

executionBaseHead: `dcb06f0e`

closureBaseHead: `dcb06f0e`

Commit mode: WORKER_MAY_COMMIT

## Purpose

Add a source-verified, secret-safe receipt integrity anchor to existing
`/api/execute` governance evidence receipts.

## Scope / Target / Owner Boundary

Target: cvf-web receipt type, receipt builder, a focused receipt-integrity
helper, final response wiring, focused tests, live proof, and RTA1
closure/session continuity artifacts.

Owner boundary: the implementation must stay inside current receipt/final
response owner surfaces and must not refactor `route.ts` or alter provider,
policy, memory, approval, routing, prompt, or DLP behavior.

## Claim / Final / Verification Boundary

Final claim may state only that `/api/execute` receipts include bounded local
integrity metadata: canonical receipt hash, optional HMAC signature when a
signing secret is configured, optional external anchor metadata when operator
configuration supplies it, and explicit claim boundary.

## Claim Boundary

RTA1 is an additive receipt evidence tranche only. It is not a third-party
immutability, public readiness, hosted readiness, production readiness, provider
quality, cost, or benchmark claim.

## 0. Surface Fidelity Gate

This work order is source-verified against current runtime owner files. The
worker may implement only the fields and owner surfaces verified below.

## 1. Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| GC-018 baseline | `docs/baselines/CVF_GC018_RTA1_RECEIPT_TRACE_ANCHOR_2026-06-06.md` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` current mode `rte1_runtime_telemetry_receipt_expansion_closed_pass_bounded` and next allowed immutable anchoring/runtime trace lane | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V16_2026-06-06.md` latest RTE1 continuity note | ACCEPT |
| RTE1 completion | `docs/reviews/CVF_RTE1_RUNTIME_TELEMETRY_RECEIPT_EXPANSION_COMPLETION_2026-06-06.md` defers external trace or anchor work to separate GC-018 | ACCEPT |
| Operator authorization | 2026-06-06 "Tiếp tục" after RTE1 closure | ACCEPT |

## 2. Transfer Objective

Implement RTA1 by adding a bounded `receiptIntegrity` object to
`GovernanceEvidenceReceipt` and wiring it into `/api/execute` final responses.
The field must record only secret-safe integrity evidence:

- receipt integrity schema version;
- canonicalization method;
- digest algorithm;
- canonical receipt hash;
- HMAC algorithm and signature status;
- HMAC digest only when a signing secret is configured;
- external anchor status and optional operator-supplied anchor reference;
- explicit redaction and claim-boundary markers.

## 3. Source Packet

### Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `GovernanceEvidenceReceipt` owns response receipt fields | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | lines 115-139 | `GovernanceEvidenceReceipt` | AI runtime type contract | ACCEPT |
| `GovernanceEvidenceReceipt.runtimeTelemetry` is the latest additive receipt field | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | line 138 | `runtimeTelemetry` | AI runtime type contract | ACCEPT |
| `BuildGovernanceEvidenceReceiptInput` owns receipt builder input fields | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 54-71 | `BuildGovernanceEvidenceReceiptInput` | receipt builder input | ACCEPT |
| `buildEvidenceReceipt` builds the receipt returned by routes | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 236-268 | `buildEvidenceReceipt` | receipt builder | ACCEPT |
| `buildGovernanceTrace` returns sanitized bounded trace entries | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 222-233 | `buildGovernanceTrace` | receipt trace builder | ACCEPT |
| `/api/execute` final response owns final governance receipt construction | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts` | lines 149-164 | `governanceEvidenceReceipt` | `buildExecuteFinalResponse` | ACCEPT |
| `/api/execute` final response returns `governanceEvidenceReceipt` to callers | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts` | lines 372-399 | `governanceEvidenceReceipt` | final JSON response | ACCEPT |
| Runtime telemetry live test proves accepted Alibaba key helper pattern | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.rte1-runtime-telemetry.alibaba.live.test.ts` | lines 38-72 | `resolveAlibabaApiKey` | live route test harness | ACCEPT |
| Manifest-level HMAC signing exists | RUNTIME_BEHAVIOR | `scripts/build_cvf_live_evidence_manifest.py` | lines 92-102 | `signature` | live evidence manifest builder | ACCEPT |
| Manifest-level external anchor metadata exists | EXISTS | `scripts/build_cvf_live_evidence_manifest.py` | lines 80-83 | `externalAnchor` | live evidence manifest builder | ACCEPT |
| Manifest claim boundary rejects third-party proof without external anchor | LITERAL_INVARIANT | `scripts/build_cvf_live_evidence_manifest.py` | lines 85-87 | `claimBoundary` | live evidence manifest builder | ACCEPT |

### New Runtime Fields

| New field | Owner | Verification class | Disposition |
| --- | --- | --- | --- |
| `ReceiptIntegrityAnchor` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | DOC_ONLY_NEW | ACCEPT |
| `GovernanceEvidenceReceipt.receiptIntegrity` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | DOC_ONLY_NEW | ACCEPT |
| `BuildGovernanceEvidenceReceiptInput.receiptIntegrity` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | DOC_ONLY_NEW | ACCEPT |
| `buildReceiptIntegrityAnchor` | new cvf-web `src/lib/receipt-integrity-anchor.ts` | DOC_ONLY_NEW | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness check | Disposition |
| --- | --- | --- |
| `/api/execute` final receipt owner | `route-final-response.ts` currently builds `governanceEvidenceReceipt`; RTA1 changes only this owner and shared receipt helper/type files | PASS |
| Provider registry surface | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are outside RTA1 because provider inventory, provider routing, and model capability behavior are unchanged | N/A with reason |
| Provider routing | Existing `routingResult`, `routedProvider`, and `model` inputs remain unchanged; RTA1 signs/hashes the already-built receipt only | PASS |
| External anchor claim | No external immutable anchor is claimed unless operator-supplied anchor metadata exists; metadata alone is not third-party proof | PASS |

## 4. Role Assignment

Codex acts as orchestrator, implementer, reviewer, and closer for this bounded
tranche. External worker dispatch is not required.

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| Orchestrator | Codex | Maintain GC-018 scope, gates, and continuity. |
| Implementer | Codex | Edit only allowed runtime/test files. |
| Reviewer | Codex | Verify deterministic canonicalization, secret safety, and claim boundary. |
| Closer | Codex | Record evidence and update session state. |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V16_2026-06-06.md`
- `docs/baselines/CVF_GC018_RTA1_RECEIPT_TRACE_ANCHOR_2026-06-06.md`
- `docs/reviews/CVF_RTE1_RUNTIME_TELEMETRY_RECEIPT_EXPANSION_COMPLETION_2026-06-06.md`
- source files listed in the Source Verification Block

## Pre-Flight Checks

| Check | Required disposition |
| --- | --- |
| Pre-dispatch autorun gate | PASS before implementation |
| Pre-implementation autorun gate | PASS before code edits |
| Working tree scope review | Diff remains inside allowed RTA1 scope |

## Write Ownership

Allowed write owners are:

- receipt type contract and builder files listed in the GC-018 baseline;
- new focused receipt-integrity helper and focused tests;
- execute final response assembly;
- one focused Alibaba live proof test;
- RTA1 completion and continuity artifacts.

Any public-sync, provider-routing, policy, prompt, memory, or storage change is
outside this work order.

## Execution Plan

1. Add typed `receiptIntegrity` support to the existing receipt contract.
2. Add a focused helper that canonicalizes safe receipt metadata, computes
   `sha256`, and optionally computes `hmac-sha256`.
3. Extend `BuildGovernanceEvidenceReceiptInput` and `buildEvidenceReceipt` so
   integrity is added after the base receipt is built.
4. Wire `/api/execute` final response to pass signing and optional anchor
   configuration through environment variables without printing secrets.
5. Add focused deterministic tests and one focused Alibaba live proof.
6. Run gates and record closure evidence.

## Evidence Requirements

Evidence must include changed files, deterministic test output, TypeScript
output, live proof result or diagnostic, and pre-closure gate result.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| `receiptIntegrity` is optional, typed, and additive | PASS |
| Receipt hash is deterministic over canonical safe receipt data | PASS |
| HMAC digest appears only when a signing secret is configured | PASS |
| Serialized receipt never includes the signing secret | PASS |
| External anchor status is explicit and never overclaims third-party proof | PASS |
| Existing receipt fields continue to work | PASS |
| Focused deterministic and live tests pass when a key is available | PASS |

## Review Gate

Reviewer must reject closure if the patch captures raw prompt/output, stores a
provider key or signing secret, claims external immutability without external
anchor evidence, changes provider/policy behavior, omits source-backed test
evidence, or claims production observability.

## Closure Checklist

| Item | Closure disposition requirement |
| --- | --- |
| Source scope | checked/PASS or BLOCKED with reason |
| Deterministic tests | checked/PASS or BLOCKED with reason |
| TypeScript check | checked/PASS or BLOCKED with reason |
| Live proof | checked/PASS or diagnostic with reason |
| Completion artifact | Public Export Disposition recorded |

## Return Conditions

Return to orchestrator if source verification is invalid, required runtime
owner fields are absent, live proof shows a governance behavior regression, or
the implementation needs changes outside RTA1 scope.

## 5. Execution Instructions

1. Add typed `receiptIntegrity` support to the existing
   `GovernanceEvidenceReceipt` contract.
2. Implement deterministic canonicalization with sorted object keys and no raw
   prompt/output/provider payload inputs.
3. Compute a `sha256` receipt hash for the base receipt before
   `receiptIntegrity` is attached.
4. Compute `hmac-sha256` only when `CVF_RECEIPT_HMAC_SECRET` or
   `CVF_AUDIT_SIGNING_KEY` is present. Do not print or return the secret.
5. Record external anchor metadata only from optional environment variables and
   mark `externalAnchorStatus` as `NOT_PROVIDED` when absent.
6. Add focused deterministic tests for canonicalization, HMAC behavior, and
   secret safety.
7. Add or run a focused Alibaba live proof when a live key is available through
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
| Reviewer | Receipt hash could be misread as immutable third-party proof. | Field must carry local-integrity claim boundary and external anchor status. |
| Security | HMAC secret could leak through receipt serialization or test output. | Secret is input-only; tests must assert serialized receipt excludes it. |
| Runtime reviewer | Integrity helper must not mutate route behavior or provider routing. | Hash/sign only the already-built receipt; no provider/policy inputs change. |

## 8. Integration Decision

Proceed with bounded implementation only after pre-dispatch and
pre-implementation autorun gates pass. The new field is additive and optional.

## 9. Completion Evidence

Closure evidence:

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base dcb06f0e --head HEAD`: PASS.
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base dcb06f0e --head HEAD`: PASS.
- `npx vitest run src/lib/receipt-integrity-anchor.test.ts src/lib/web-governance-envelope.test.ts src/app/api/execute/route.governance-trace.test.ts`: PASS, 24 tests.
- `npm run check`: PASS.
- `npx vitest run src/app/api/execute/route.rta1-receipt-integrity.alibaba.live.test.ts --reporter verbose`: PASS, receipt `rcpt-env-mq2iyeyu-cak2p5`.
- Diagnostic for pre-provider safety-filter retry:
  `docs/evidence/CVF_RTA1_LIVE_PROOF_DIAGNOSTIC_2026-06-06.json`.
- Completion review:
  `docs/reviews/CVF_RTA1_RECEIPT_TRACE_ANCHOR_COMPLETION_2026-06-06.md`.

## 10. Claim Boundary

RTA1 proves only that existing `/api/execute` receipts can include local
receipt integrity metadata. It does not prove third-party immutability,
production tracing, provider reliability, hosted readiness, public readiness,
or external audit replay.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_WO_RTA1_RECEIPT_TRACE_ANCHOR_2026-06-06.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_RTA1_RECEIPT_TRACE_ANCHOR_COMPLETION_2026-06-06.md` | completion review exists with verification table | PASS |
| Roadmap state | N/A with reason | RTA1 is GC-018 continuity-derived; no roadmap artifact owns this tranche | N/A with reason |
| Registry JSON | BLOCKED with reason | corpus/search registry ownership is outside this receipt-only tranche | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | corpus/search registry Markdown ownership is outside this receipt-only tranche | BLOCKED with reason |
| External evidence digest | N/A with reason | focused live receipt sample is recorded in completion review; no external anchor digest claimed | N/A with reason |
| System loop interlock | N/A with reason | no new route or system-loop chain is expected | N/A with reason |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V16_2026-06-06.md` | session sync follows material commit | PASS |

## Worker Autonomy / No-Question Rule

The worker must handle in-scope validation failures autonomously. Escalation is
required only for public-sync, real external anchor provider integration,
production or hosted readiness claims, risk-level changes, or claim-boundary
changes.

## Operator Checkpoint

None for RTA1.

## Knowledge Absorption Blind-Spot Control Block

Prior absorption evidence resolved:

- RTE1 completion explicitly deferred external trace or anchor work to a
  separate GC-018.
- The live evidence manifest standard and script already define manifest-level
  HMAC and optional external anchor semantics.

Detailed source reads completed:

- READ_DEEP: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- READ_DEEP: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`
- READ_DEEP:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts`
- READ_DEEP:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.rte1-runtime-telemetry.alibaba.live.test.ts`
- READ_DEEP: `scripts/build_cvf_live_evidence_manifest.py`

Normalization decision:

- Accepted now: local receipt hash and optional HMAC signature metadata on the
  existing receipt.
- Deferred: real external immutable anchor provider, hosted trace service,
  third-party replay service, and public audit portal.
- Rejected for this batch: raw trace replay, raw provider payload capture, and
  any public/production readiness claim.

Adversarial role review:

- Reviewer: hash/signature alone is not external immutability. Verdict:
  explicit boundary required.
- Security: HMAC secret must be input-only. Verdict: required.
- Runtime reviewer: route behavior must remain unchanged. Verdict: additive
  response field only.

Blind-spot delta:

- Reduced: live receipts can be locally integrity-checked and optionally signed.
- Remaining: independent third-party anchoring still requires a separate
  external provider/service tranche.

## Roadmap-To-Work-Order Trace Matrix

N/A with reason: this work is derived from active GC-018 continuity after RTE1,
not from a multi-task roadmap artifact.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private runtime receipt hardening. Public-facing signed receipt
or external-anchor claims require a separate public-sync packet after private
review and external-anchor evidence.

Next action: implement and close RTA1 in private provenance scope.
