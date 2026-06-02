# CVF MKE1-E2 Memory Durable Write Route Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-06-01

## Purpose

Record the completion of MKE1-E2: a governed `POST /api/memory/write` route
that exposes `DurableMemoryStore.write()` through an authenticated HTTP surface
with raw-content rejection, policy gate, and summary-only receipt.

## Scope / Target / Owner Boundary

Target: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/`
(route.ts, route-constants.ts, route.test.ts).

Owner boundary: cvf-web route only. `durable-memory-store.ts` is read-only
source; not modified.

## Target / Source

Target artifacts:
- `route.ts` (238 lines) — `POST /api/memory/write` handler
- `route-constants.ts` (2 lines) — version constant `cvf.memoryDurableWriteRoute.mke1.e2.v1`
- `route.test.ts` (156 lines) — 6 focused tests

Source authority:
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` — store contract
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` — auth pattern

## Scope / Methodology

Documentation-after-delivery: route was delivered by worker during E3 session
without a prior work order. Retroactive governance packet filed per operator
authorization. Implementation reviewed against acceptance criteria before filing.

## Findings / Position

Route correctly implements:

1. **Auth**: service-token (`verifyServiceTokenRequest`) or session cookie
   (`verifySessionCookie`) — unauthorized returns 401.
2. **Raw content rejection**: `hasRawPayloadField` rejects any body with
   `content`, `rawContent`, or `value` fields with reason
   `raw_memory_payload_rejected` before validation.
3. **Policy gate**: `actorAuthorized: false` or `policyDecision !== 'allow'`
   → denied receipt, no store write.
4. **Store path gate**: `CVF_DURABLE_MEMORY_STORE_PATH` env var required;
   missing → denied receipt (not 500).
5. **Receipt invariants**: all responses carry `rawMemoryReleased: false` and
   `canReinject: false`; store receipts carry `summaryOnly: true`.

No raw content field accepted. No autonomous mutation. No prompt injection.

## Risk / Corrective Action

Risk: store path env var could be set to an uncontrolled path.
Corrective action: `CVF_DURABLE_MEMORY_STORE_PATH` is operator-configured;
route does not validate the path beyond trusting the env var. Acceptable for
local/private use case; production hardening is out of scope for MKE1.

## Verification

| Command | Result |
| --- | --- |
| `npm --prefix EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web run check` | PASS |
| `npx vitest run src/app/api/memory/write/route.test.ts` from cvf-web | PASS, 6/6 tests |
| `python governance/compat/check_governed_file_size.py --enforce` | PASS |

Test coverage:
- unauthorized request → 401
- raw `content` field → 400 `raw_memory_payload_rejected`
- invalid body → 400
- `actorAuthorized: false` → denied receipt
- store not configured → denied receipt
- valid authorized write → allowed receipt with `summaryOnly:true`, `canReinject:false`, `rawMemoryReleased:false`

## Finding-To-Governance Learning Disposition

Defect class: `ORCHESTRATOR_PACKET_GAP` — E2 route was delivered by worker
during E3 session without a prior GC-018 or work order; operator caught this
and required retroactive governance before commit. Root cause: no enforcement
preventing workers from creating files in forbidden-by-roadmap paths during
a later tranche.

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Disposition: `MACHINE_CHECK_CANDIDATE` — work-order scope firewall in GC-049
should be extended to check untracked files against forbidden paths during
pre-implementation gate, not only staged files.

Next action: consider adding untracked-file forbidden-path check to
`check_core_guard_self_protection.py` pre-dispatch phase.

Runtime/provider/cost learning: `N/A_WITH_REASON` — no provider calls in E2.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

MKE1-E2 delivers a governed durable write HTTP route: authenticated, raw-content
rejected, policy-gated, summary-only receipt. Does not claim production readiness,
hosted readiness, raw content intake, autonomous mutation, provider calls,
public-sync, or push.
