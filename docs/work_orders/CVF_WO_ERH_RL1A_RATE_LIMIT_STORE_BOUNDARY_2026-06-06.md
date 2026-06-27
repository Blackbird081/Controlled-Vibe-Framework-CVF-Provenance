# CVF Work Order - ERH-RL1A Rate Limit Store Boundary

Memory class: WORK_ORDER

docType: work_order

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-06

dispatchBaseHead: `4c0bd98d`

executionBaseHead: `4c0bd98d`

closureBaseHead: `4c0bd98d`

Commit mode: WORKER_MAY_COMMIT

## Purpose

Close the highest-value bounded slice of ERH-RL1 by making the current
process-local rate limiter explicit, testable, and fail-safe when an unsupported
distributed backend is requested.

## Scope / Target / Owner Boundary

Target: cvf-web `/api/execute` rate-limit helper, focused rate-limit tests, and
ERH-RL1A closure/session continuity artifacts.

Owner boundary: no Redis package selection, dependency installation, remote
service integration, provider behavior change, route refactor, public-sync,
hosted-readiness claim, or production-readiness claim.

## Claim / Final / Verification Boundary

Final claim may state only that `/api/execute` rate-limit admission now has an
explicit store contract and backend status, defaults to process-local memory,
and fails closed when configured for an unsupported backend.

## Claim Boundary

ERH-RL1A is not distributed rate limiting. It does not prove multi-instance
enforcement, Redis readiness, enterprise deployment readiness, or provider
quality/cost behavior.

## 0. Surface Fidelity Gate

This work order is source-verified against current runtime owner files. The
worker may implement only the fields and owner surfaces verified below.

## 1. Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| GC-018 baseline | `docs/baselines/CVF_GC018_ERH_RL1A_RATE_LIMIT_STORE_BOUNDARY_2026-06-06.md` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` current mode `rta1_receipt_trace_anchor_closed_pass_bounded` and next allowed ERH-RL1 lane | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V16_2026-06-06.md` latest continuity note parks ERH-RL1 | ACCEPT |
| Backlog ERH-RL1 work order | `docs/work_orders/CVF_WO_ERH_RL1_DISTRIBUTED_RATE_LIMITER_BOUNDARY_2026-06-06.md` rejects Redis dependency as source-not-found | ACCEPT |
| Operator authorization | 2026-06-06 "ok, next" after RTA1 closure | ACCEPT |

## 2. Transfer Objective

Implement ERH-RL1A by replacing ad hoc module-level bucket maps with an explicit
rate-limit store contract and memory-backed implementation. Add backend status
readout and fail-closed behavior for unsupported configured backend modes so
future agents cannot silently claim distributed enforcement from process-local
memory.

## 3. Source Packet

### Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `/api/execute` imports the runtime rate limiter | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 8 | `getRateLimiter` | `/api/execute` route | ACCEPT |
| `/api/execute` blocks callers when limiter disallows the request | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 90-101 | `limitResult` | `/api/execute` admission control | ACCEPT |
| Current limiter stores buckets in process memory | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | lines 30-31 | `MemoryRateLimitStore` | rate-limit helper | ACCEPT |
| Current limiter stores provider buckets in process memory | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | line 54 | `providerStore` | rate-limit helper | ACCEPT |
| Current limiter reads per-user request limit from environment | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | line 58 | `CVF_RATE_LIMIT` | `limits` | ACCEPT |
| Current limiter reads provider quota from environment | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | line 59 | `CVF_PROVIDER_QUOTA_PER_MIN` | `limits` | ACCEPT |
| Existing tests cover user identity and provider bucket behavior | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.test.ts` | lines 48-88 | `getRateLimiter` | rate-limit test suite | ACCEPT |
| Redis-compatible runtime dependency exists in cvf-web package manifest | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | lines 19-56 | `dependencies` | package manifest | REJECT: no Redis-compatible dependency is declared |

### New Runtime Fields

| New field or symbol | Owner | Verification class | Disposition |
| --- | --- | --- | --- |
| `RateLimitStore` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | DOC_ONLY_NEW | ACCEPT |
| `MemoryRateLimitStore` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | DOC_ONLY_NEW | ACCEPT |
| `RateLimitBackendStatus` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | DOC_ONLY_NEW | ACCEPT |
| `getRateLimitBackendStatus` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | DOC_ONLY_NEW | ACCEPT |
| `CVF_RATE_LIMIT_STORE` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | DOC_ONLY_NEW | ACCEPT |
| `resetRateLimitStoresForTest` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | DOC_ONLY_NEW | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness check | Disposition |
| --- | --- | --- |
| `/api/execute` rate-limit admission | Current source blocks on `allowed=false` with HTTP 429 and `Retry-After` | PASS |
| Redis backend dependency | Package manifest does not contain a Redis-compatible runtime dependency | PASS |
| Existing rate-limit tests | Existing tests exercise identity, provider, and IP bucket behavior | PASS |
| Separate guards rate limiter | `src/lib/rate-limiter.ts` is outside ERH-RL1A scope because `/api/execute` uses `src/lib/rate-limit.ts` | N/A with reason |

## 4. Role Assignment

Codex acts as orchestrator, implementer, reviewer, and closer for this bounded
tranche. External worker dispatch is not required.

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| Orchestrator | Codex | Maintain ERH-RL1A scope, gates, and continuity. |
| Implementer | Codex | Edit only allowed runtime/test files. |
| Reviewer | Codex | Verify fail-safe semantics and no distributed overclaim. |
| Closer | Codex | Record evidence and update session state. |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V16_2026-06-06.md`
- `docs/baselines/CVF_GC018_ERH_RL1A_RATE_LIMIT_STORE_BOUNDARY_2026-06-06.md`
- `docs/work_orders/CVF_WO_ERH_RL1_DISTRIBUTED_RATE_LIMITER_BOUNDARY_2026-06-06.md`
- source files listed in the Source Verification Block

## Pre-Flight Checks

| Check | Required disposition |
| --- | --- |
| Pre-dispatch autorun gate | PASS before implementation |
| Pre-implementation autorun gate | PASS before code edits |
| Working tree scope review | Diff remains inside allowed ERH-RL1A scope |

## Operator Checkpoint

None.

## Worker Autonomy / No-Question Rule

The worker owns all machine-gate conformance work inside allowed ERH-RL1A
scope. Any need for Redis package selection, remote infrastructure,
public-sync, live provider quota, destructive actions, or changes outside this
work order changes the artifact status to `BLOCKED` and returns it to
Orchestrator.

## Write Ownership

Allowed write owners are:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.test.ts`
- ERH-RL1A GC-018 baseline, work-order, completion, and continuity artifacts

Any Redis package install, provider route execution behavior, guard API
rate-limiter rewrite, public-sync, or production deployment change is outside
this work order.

## Execution Plan

1. Add typed `RateLimitStore` and `MemoryRateLimitStore` around the existing
   bucket behavior.
2. Add backend status resolution for `CVF_RATE_LIMIT_STORE`, defaulting to
   explicit process-local memory.
3. Fail closed when `CVF_RATE_LIMIT_STORE` requests `redis` or any unsupported
   backend before a real adapter exists.
4. Preserve user, service identity, IP, and provider quota behavior.
5. Add focused tests for backend status, unsupported backend fail-closed
   behavior, and process-local claim boundary.
6. Run focused tests, TypeScript check, and autorun gates.

## Evidence Requirements

Evidence must include changed files, focused rate-limit test output, TypeScript
output, and pre-closure gate result.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Existing identity and provider quota behavior is preserved | PASS |
| Default backend status is explicit process-local memory | PASS |
| Unsupported `CVF_RATE_LIMIT_STORE=redis` fails closed | PASS |
| Unsupported non-memory backend fails closed | PASS |
| No Redis or remote service dependency is installed or claimed | PASS |
| `/api/execute` route contract remains compatible with `allowed` and `retryAfterSeconds` | PASS |

## Review Gate

Reviewer must reject closure if the patch claims distributed enforcement,
silently falls back from configured Redis to memory, installs a Redis dependency
without a separate source-verified package decision, changes provider execution
behavior, or omits focused test evidence.

## Closure Checklist

| Item | Closure disposition requirement |
| --- | --- |
| Source scope | checked/PASS or BLOCKED with reason |
| Focused tests | checked/PASS or BLOCKED with reason |
| TypeScript check | checked/PASS or BLOCKED with reason |
| Completion artifact | Public Export Disposition recorded |

## Return Conditions

Return to orchestrator if implementation requires Redis package selection,
remote infrastructure credentials, changes outside the `/api/execute`
rate-limit helper, or a production distributed-rate-limit claim.

## 5. Execution Instructions

1. Keep memory mode as the default behavior.
2. Make memory mode's process-local boundary visible in a typed backend status.
3. Do not silently use memory when an unsupported backend is configured.
4. Do not change the existing `/api/execute` 429 response contract.
5. Do not install or import a Redis package in this tranche.

## 6. Role Output Schema

Completion output must include:

- changed-file list;
- focused test command and result;
- TypeScript command and result;
- autorun gate result;
- explicit non-distributed claim boundary;
- Public Export Disposition.

## 7. Dissent And Review Ledger

| Concern | Resolution |
| --- | --- |
| A store interface can be mistaken for distributed enforcement | Backend status must report `distributed=false` for memory and block unsupported Redis configuration |
| Redis is the eventual likely backend | Package/version/topology selection remains a separate ERH-RL1 tranche |
| Route response compatibility | `consume` must keep `allowed` and `retryAfterSeconds` fields |

## 8. Integration Decision

Proceed only after pre-dispatch and pre-implementation gates pass on the real
range `4c0bd98d..HEAD`.

## 9. Completion Evidence

Completion evidence must be recorded in a dedicated completion review before
any closed-equivalent status is claimed.

## 10. Claim Boundary

This work order cannot be used as evidence that CVF has distributed rate
limiting. It is a store-boundary and fail-safe tranche only.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ERH-RL1A does not create public-facing distributed rate-limit evidence.

Next action: implement bounded store boundary and close privately.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_WO_ERH_RL1A_RATE_LIMIT_STORE_BOUNDARY_2026-06-06.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_RL1A_RATE_LIMIT_STORE_BOUNDARY_COMPLETION_2026-06-06.md` | completion review created | PASS |
| Roadmap state | N/A with reason | ERH-RL1A is GC-018 continuity-derived; no roadmap artifact owns this tranche | N/A with reason |
| Registry JSON | BLOCKED with reason | corpus/search registry ownership is outside this runtime limiter tranche | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | corpus/search registry Markdown ownership is outside this runtime limiter tranche | BLOCKED with reason |
| External evidence digest | N/A with reason | no live provider or external anchor evidence required for store-contract unit tranche | N/A with reason |
| System loop interlock | N/A with reason | no new route or system-loop chain is added | N/A with reason |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V16_2026-06-06.md` | session sync follows material commit | PASS |
