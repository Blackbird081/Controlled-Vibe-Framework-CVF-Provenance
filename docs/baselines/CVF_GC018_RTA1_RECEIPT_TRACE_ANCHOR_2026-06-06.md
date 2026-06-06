# CVF GC-018 - RTA1 Receipt Trace Anchor

Memory class: FULL_RECORD

docType: gc018_baseline

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-06

dispatchBaseHead: `dcb06f0e`

## Purpose

Authorize the next bounded runtime evidence tranche after RTE1: add a
secret-safe receipt integrity anchor to existing `/api/execute` governance
evidence receipts.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` records RTE1 closed and permits a separate GC-018 for external immutable anchoring/runtime trace service | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V16_2026-06-06.md` names immutable anchoring/runtime trace as a next allowed separate GC-018 lane | ACCEPT |
| RTE1 completion | `docs/reviews/CVF_RTE1_RUNTIME_TELEMETRY_RECEIPT_EXPANSION_COMPLETION_2026-06-06.md` defers external trace or anchor work to a separate GC-018 | ACCEPT |
| Live evidence manifest standard | `docs/reference/CVF_LIVE_EVIDENCE_MANIFEST_AND_RERUN_STANDARD_2026-06-06.md` defines optional HMAC and external anchor semantics at manifest level | ACCEPT |
| Operator authorization | 2026-06-06 request: "Tiếp tục" after RTE1 closure, with prior live-run permission | ACCEPT |

## Source / Predecessor Evidence

| Source | Evidence | Disposition |
| --- | --- | --- |
| RTE1 runtime receipt expansion | Existing receipt now carries runtime telemetry but no route-level integrity anchor. | ACCEPT |
| Manifest builder | `scripts/build_cvf_live_evidence_manifest.py` already signs manifest payloads with `CVF_AUDIT_SIGNING_KEY` and records optional external anchor metadata. | ACCEPT |
| `/api/execute` final response owner | `route-final-response.ts` constructs `governanceEvidenceReceipt` before response emission. | ACCEPT |

## Decision / Baseline / Proposed Tranche

Decision: authorize RTA1 as a bounded additive receipt integrity tranche.

Baseline: CVF can already produce live receipt telemetry and manifest-level
HMAC evidence, but the route receipt itself has no canonical hash/signature
metadata.

Proposed tranche: add optional `receiptIntegrity` metadata to the existing
receipt builder and `/api/execute` final response. The field must include a
canonical receipt hash for every configured call path and an HMAC signature
only when a receipt-signing secret is present.

## Scope

Allowed source changes:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`
- a new focused cvf-web receipt-integrity helper under `src/lib`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts`
- focused builder/helper/route tests and one focused Alibaba live proof test
- RTA1 completion/session continuity artifacts

Forbidden scope:

- third-party anchor service integration without a real configured provider and separate evidence;
- provider routing, model selection, prompt, policy, DLP, approval, memory, or
  durable storage behavior change;
- raw prompt, raw output, provider key, hidden policy, private memory, or raw
  provider payload persistence;
- public-sync, hosted readiness, production readiness, public readiness,
  provider-quality, cost-optimization, benchmark-quality, or third-party
  immutability claim;
- autonomous learning mutation or Learning Plane behavior mutation.

## Required Work Order

The implementation packet must be:

`docs/work_orders/CVF_WO_RTA1_RECEIPT_TRACE_ANCHOR_2026-06-06.md`

It must source-verify existing owner surfaces before implementation starts and
must list newly introduced receipt fields separately.

## Evidence / Verification

Verification completed:

- Pre-dispatch autorun gate over `dcb06f0e..HEAD`: PASS.
- Pre-implementation autorun gate over `dcb06f0e..HEAD`: PASS.
- Focused deterministic tests:
  `npx vitest run src/lib/receipt-integrity-anchor.test.ts src/lib/web-governance-envelope.test.ts src/app/api/execute/route.governance-trace.test.ts`: PASS, 24 tests.
- cvf-web TypeScript: `npm run check`: PASS.
- Focused Alibaba live proof:
  `npx vitest run src/app/api/execute/route.rta1-receipt-integrity.alibaba.live.test.ts --reporter verbose`: PASS, receipt `rcpt-env-mq2iyeyu-cak2p5`.
- Diagnostic for pre-provider safety-filter retry:
  `docs/evidence/CVF_RTA1_LIVE_PROOF_DIAGNOSTIC_2026-06-06.json`.
- Completion review:
  `docs/reviews/CVF_RTA1_RECEIPT_TRACE_ANCHOR_COMPLETION_2026-06-06.md`.

## Claim Boundary

RTA1 may claim only local route-receipt integrity metadata. It does not prove
third-party immutability, hosted freshness, production tracing, provider
reliability, public readiness, or external audit replay unless a later tranche
adds and verifies a real external anchor provider.
