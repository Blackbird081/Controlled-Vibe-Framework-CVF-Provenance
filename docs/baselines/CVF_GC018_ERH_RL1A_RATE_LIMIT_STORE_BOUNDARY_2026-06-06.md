# CVF GC-018 Baseline - ERH-RL1A Rate Limit Store Boundary

Memory class: BASELINE

docType: gc018_baseline

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-06

baseHead: `4c0bd98d`

## Purpose

Bound the current `/api/execute` rate limiter as process-local memory and add a
source-backed store boundary that prevents future distributed-rate-limit claims
without an installed backend adapter.

## Decision / Baseline / Proposed Tranche

Decision: proceed with ERH-RL1A as a bounded store-contract tranche.

Baseline: `/api/execute` rate limiting now uses an explicit process-local
memory store in `src/lib/rate-limit.ts`; no Redis-compatible package is
declared in the cvf-web manifest.

Proposed tranche: add explicit memory backend status, a rate-limit store
contract, and fail-closed unsupported-backend handling while deferring real
distributed backend selection to a later source-verified ERH-RL1 tranche.

## Scope / Target / Owner Boundary

Target:

- cvf-web `/api/execute` rate-limit helper;
- focused cvf-web rate-limit tests;
- ERH-RL1A work-order and closure/session continuity artifacts.

Owner boundary:

- no Redis package selection or dependency installation;
- no provider, policy, prompt, approval, DLP, budget, memory, or route-flow
  behavior change beyond rate-limit admission fail-safe;
- no public-sync or production-readiness claim.

## Claim Boundary

ERH-RL1A may claim only that the existing rate limiter has an explicit
`RateLimitStore` contract, preserves process-local memory behavior by default,
and fails closed when an unsupported non-memory backend is requested. It does
not prove distributed enforcement, Redis readiness, multi-instance safety, or
hosted production readiness.

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `/api/execute` imports the runtime rate limiter | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 8 | `getRateLimiter` | `/api/execute` route | ACCEPT |
| `/api/execute` consumes the limiter after body parsing and before provider execution | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 90-101 | `consume` | `/api/execute` admission control | ACCEPT |
| Current limiter stores buckets in process memory | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | lines 30-31 | `MemoryRateLimitStore` | rate-limit helper | ACCEPT |
| Current limiter stores provider buckets in process memory | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | line 54 | `providerStore` | rate-limit helper | ACCEPT |
| Current limiter reads per-user request limit from environment | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | line 58 | `CVF_RATE_LIMIT` | `limits` | ACCEPT |
| Current limiter reads provider quota from environment | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | line 59 | `CVF_PROVIDER_QUOTA_PER_MIN` | `limits` | ACCEPT |
| Existing tests cover user identity and provider bucket behavior | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.test.ts` | lines 48-88 | `getRateLimiter` | rate-limit test suite | ACCEPT |
| Redis-compatible runtime dependency exists in cvf-web package manifest | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | lines 19-56 | `dependencies` | package manifest | REJECT: no Redis-compatible dependency is declared |

## New Runtime Fields

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
| `/api/execute` rate-limit admission | Current source calls `limiter.consume(request, limitIdentity, body.provider)` and blocks on `allowed=false` | PASS |
| Redis backend dependency | Package manifest does not contain a Redis-compatible runtime dependency | PASS |
| Existing rate-limit tests | Existing tests exercise identity, provider, and IP bucket behavior | PASS |
| Separate guards rate limiter | `src/lib/rate-limiter.ts` is a different guard API helper and is outside ERH-RL1A scope | N/A with reason |

## Required Control Outcome

The runtime must keep memory mode explicit and local by default. If
`CVF_RATE_LIMIT_STORE=redis` or another unsupported value is configured before a
real adapter exists, the limiter must fail closed and expose a backend status
that makes the missing distributed backend visible to tests and reviewers.

## Evidence / Verification

Completed verification:

- pre-dispatch autorun gate on `4c0bd98d..HEAD`: PASS;
- pre-implementation autorun gate on `4c0bd98d..HEAD`: PASS;
- focused cvf-web rate-limit tests: PASS, 13 tests;
- cvf-web TypeScript check: PASS.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ERH-RL1A is private runtime hardening and does not add public-facing
distributed rate-limit evidence.

Next action: execute the paired source-verified work order.
