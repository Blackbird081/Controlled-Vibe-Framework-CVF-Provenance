# CVF GC-018 Baseline - ERH-RL1B Distributed Rate Limit Backend

Memory class: BASELINE

docType: gc018_baseline

Status: PRE_CLOSURE_READY

Date: 2026-06-06

baseHead: `d30accb6`

## Purpose

Authorize the next bounded ERH rate-limit tranche: add a real Redis-compatible
backend adapter for `/api/execute` rate-limit admission while preserving the
ERH-RL1A no-overclaim boundary.

## Decision / Baseline / Proposed Tranche

Decision: proceed with a Redis REST adapter using `@upstash/redis` after source
verification and package-registry verification.

Baseline: ERH-RL1A closed at material commit `3978554c`. ERH-RL1B adds the
bounded adapter path on top of that contract: `@upstash/redis` is installed,
`CVF_RATE_LIMIT_STORE=redis` is env-gated by Upstash REST URL/token, malformed
Redis URL is fail-closed, `/api/execute` awaits the async limiter, and focused
tests prove Redis command semantics with an injected fake client.

Closed tranche: no hosted Redis resource was created and no live Redis service
proof is claimed. A real hosted Redis service proof remains a separate
environment-dependent deployment proof.

## Scope / Target / Owner Boundary

Target:

- cvf-web rate-limit helper and focused tests;
- one-line `/api/execute` await wiring for async Redis store consumption;
- cvf-web package manifest and lockfile for the selected Redis package;
- ERH-RL1B work-order, completion, and session continuity artifacts.

Owner boundary:

- no hosted Redis resource creation;
- no raw secret logging;
- no provider, policy, prompt, approval, DLP, budget, memory, or route-flow
  behavior change outside one-line async rate-limit consume wiring;
- no public-sync, hosted-readiness, production-readiness, or multi-instance
  claim without external Redis service proof.

## Claim Boundary

ERH-RL1B may claim only that CVF has a source-backed Redis REST adapter path
for rate-limit admission and test-proven Redis command semantics. It may not
claim hosted distributed enforcement, production readiness, or public readiness
without a live Redis service proof.

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `/api/execute` imports the runtime rate limiter | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 8 | `getRateLimiter` | `/api/execute` route | ACCEPT |
| `/api/execute` blocks callers when limiter disallows the request | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 90-101 | `limitResult` | `/api/execute` admission control | ACCEPT |
| Async store contract exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | lines 28-30 | `RateLimitStore` | rate-limit helper | ACCEPT |
| Memory store remains process-local default | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | lines 39-59 and 109-117 | `MemoryRateLimitStore` / `ACTIVE_MEMORY_PROCESS_LOCAL` | rate-limit helper | ACCEPT |
| Redis client contract exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | lines 33-37 | `RateLimitRedisClient` | rate-limit helper | ACCEPT |
| Upstash Redis REST store exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | lines 62-88 | `UpstashRedisRateLimitStore` | rate-limit helper | ACCEPT |
| Redis active status is env gated | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | lines 120-187 | `ACTIVE_REDIS_REST` / `BLOCKED_REDIS_ENV_MISSING` / `BLOCKED_REDIS_ENV_INVALID` | `getRateLimitBackendStatus` | ACCEPT |
| `/api/execute` awaits async limiter and preserves 429 contract | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 90-99 | `await limiter.consume` | `/api/execute` admission control | ACCEPT |
| Package manifest declares selected Redis dependency | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | line 20 | `@upstash/redis` | package manifest | ACCEPT |
| Focused tests cover memory, env fail-closed, invalid env, and fake Redis semantics | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.test.ts` | lines 154-265 | `FakeRedisClient` / `CVF_RATE_LIMIT_STORE` | rate-limit test suite | ACCEPT |

## Package Registry Evidence

| Package candidate | Verification command | Registry result | Disposition |
| --- | --- | --- | --- |
| `@upstash/redis` | `npm view @upstash/redis version license dependencies repository dist-tags --json` | version `1.38.0`, license `MIT`, dependency `uncrypto`, repository `upstash/redis-js`, latest dist-tag `1.38.0` | ACCEPT |
| `ioredis` | `npm view ioredis version license dependencies repository dist-tags --json` | version `5.11.1`, license `MIT`, TCP Redis client with multiple runtime dependencies | REJECT for this tranche: TCP topology is less aligned with serverless/Next route deployment than Redis REST |

## New Runtime Fields

| New field or symbol | Owner | Verification class | Disposition |
| --- | --- | --- | --- |
| `UpstashRedisRateLimitStore` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | EXISTS | ACCEPT |
| `RateLimitRedisClient` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | EXISTS | ACCEPT |
| `UPSTASH_REDIS_REST_URL` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | EXISTS | ACCEPT |
| `UPSTASH_REDIS_REST_TOKEN` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | EXISTS | ACCEPT |
| `@upstash/redis` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness check | Disposition |
| --- | --- | --- |
| `/api/execute` rate-limit admission | Current source blocks on `allowed=false` with HTTP 429 and `Retry-After` | PASS |
| Memory default | Current source defaults missing `CVF_RATE_LIMIT_STORE` to `memory` | PASS |
| Redis mode | Current source activates Redis only with complete valid Upstash REST env and otherwise fails closed | PASS |
| Separate guards rate limiter | `src/lib/rate-limiter.ts` remains outside ERH-RL1B because `/api/execute` uses `src/lib/rate-limit.ts` | N/A with reason |

## Required Control Outcome

Redis mode must require explicit `CVF_RATE_LIMIT_STORE=redis` plus
`UPSTASH_REDIS_REST_URL` and `UPSTASH_REDIS_REST_TOKEN`. Missing or malformed
Redis env must fail closed. Memory mode remains the default and continues to
report `distributed=false`.

## Evidence / Verification

Required verification:

- pre-dispatch autorun gate on `d30accb6..HEAD`;
- pre-implementation autorun gate on `d30accb6..HEAD`;
- package manifest and lockfile updated by `npm install @upstash/redis@1.38.0`;
- focused cvf-web rate-limit tests with fake Redis client: PASS, 17/17;
- cvf-web TypeScript check: PASS;
- pre-closure autorun gate before closed-equivalent claim: required after material commit.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ERH-RL1B is private runtime hardening. Public distributed
rate-limit claims require a real external Redis service proof and public-sync
packet.

Next action: separate live Redis service proof if CVF needs a hosted
multi-instance enforcement claim.
