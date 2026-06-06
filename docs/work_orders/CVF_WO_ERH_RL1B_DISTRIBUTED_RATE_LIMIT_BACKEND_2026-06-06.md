# CVF Work Order - ERH-RL1B Distributed Rate Limit Backend

Memory class: WORK_ORDER

docType: work_order

Status: PRE_CLOSURE_READY

Date: 2026-06-06

dispatchBaseHead: `d30accb6`

executionBaseHead: `d30accb6`

closureBaseHead: `d30accb6`

Commit mode: WORKER_MAY_COMMIT

## Purpose

Implement the next bounded ERH-RL1 step by adding a real Redis REST backend
adapter path for `/api/execute` rate-limit admission.

## Scope / Target / Owner Boundary

Target: cvf-web rate-limit helper, one-line `/api/execute` async consume
wiring, focused tests, cvf-web package manifest and lockfile, and ERH-RL1B
closure/session continuity artifacts.

Owner boundary: no hosted Redis resource creation, no raw secret logging, no
route refactor beyond awaiting the existing rate-limit consume call, no
provider execution behavior change, no guard API rate-limiter rewrite, no
public-sync, no hosted-readiness claim, no production-readiness claim, and no
multi-instance enforcement claim without a live Redis service proof.

## Claim / Final / Verification Boundary

Final claim states only that CVF now has an env-gated Upstash Redis REST
adapter path for rate-limit admission and focused tests proving command
semantics through a fake Redis client.

## Claim Boundary

ERH-RL1B is not hosted distributed enforcement proof. It does not prove
multi-instance safety, Redis service availability, production readiness,
public readiness, provider quality, or cost/performance behavior.

## 0. Surface Fidelity Gate

This work order is source-verified against current runtime owner files. The
worker may implement only the fields and owner surfaces verified below.

## 1. Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| GC-018 baseline | `docs/baselines/CVF_GC018_ERH_RL1B_DISTRIBUTED_RATE_LIMIT_BACKEND_2026-06-06.md` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` current mode `erh_rl1a_rate_limit_store_boundary_closed_pass_bounded` and next allowed ERH-RL1B lane | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V16_2026-06-06.md` latest continuity note parks ERH-RL1B | ACCEPT |
| ERH-RL1A completion | `docs/reviews/CVF_ERH_RL1A_RATE_LIMIT_STORE_BOUNDARY_COMPLETION_2026-06-06.md` says real Redis adapter requires separate source-verified tranche | ACCEPT |
| Operator authorization | 2026-06-06 "Next sạch nhất: ERH-RL1B" | ACCEPT |

## 2. Transfer Objective

Install `@upstash/redis` and implement an env-gated Redis REST store for the
existing rate-limit contract. Redis mode must consume user and provider buckets
through Redis commands, preserve the route's `allowed` and `retryAfterSeconds`
contract, update `/api/execute` to await the existing consume call, and fail
closed when Redis env is missing.

## 3. Source Packet

### Source Verification Block

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

### Package Registry Evidence

| Package candidate | Verification command | Registry result | Disposition |
| --- | --- | --- | --- |
| `@upstash/redis` | `npm view @upstash/redis version license dependencies repository dist-tags --json` | version `1.38.0`, license `MIT`, dependency `uncrypto`, repository `upstash/redis-js`, latest dist-tag `1.38.0` | ACCEPT |
| `ioredis` | `npm view ioredis version license dependencies repository dist-tags --json` | version `5.11.1`, license `MIT`, TCP Redis client with multiple runtime dependencies | REJECT for this tranche: TCP topology is less aligned with serverless/Next route deployment than Redis REST |

### New Runtime Fields

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

## 4. Role Assignment

Codex acts as orchestrator, implementer, reviewer, and closer for this bounded
tranche. External worker dispatch is not required.

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| Orchestrator | Codex | Maintain ERH-RL1B scope, package decision, gates, and continuity. |
| Implementer | Codex | Edit only allowed runtime/package/test files. |
| Reviewer | Codex | Verify Redis command semantics, fail-closed env handling, and no distributed overclaim. |
| Closer | Codex | Record evidence and update session state. |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V16_2026-06-06.md`
- `docs/baselines/CVF_GC018_ERH_RL1B_DISTRIBUTED_RATE_LIMIT_BACKEND_2026-06-06.md`
- `docs/reviews/CVF_ERH_RL1A_RATE_LIMIT_STORE_BOUNDARY_COMPLETION_2026-06-06.md`
- source files listed in the Source Verification Block

## Pre-Flight Checks

| Check | Required disposition |
| --- | --- |
| Pre-dispatch autorun gate | PASS |
| Pre-implementation autorun gate | PASS |
| Working tree scope review | Diff remains inside allowed ERH-RL1B scope |

## Operator Checkpoint

None.

## Worker Autonomy / No-Question Rule

The worker owns all machine-gate conformance work inside allowed ERH-RL1B
scope. Any need for hosted Redis resource creation, raw secret handling,
public-sync, provider live quota, destructive actions, or changes outside this
work order changes the artifact status to `BLOCKED` and returns it to
Orchestrator.

## Write Ownership

Allowed write owners are:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json`
- ERH-RL1B GC-018 baseline, work-order, completion, and continuity artifacts

Any hosted Redis resource setup, provider-route execution behavior beyond the
rate-limit await, guard API rate-limiter rewrite, public-sync, or production
deployment change is outside this work order.

## Execution Plan

1. Install `@upstash/redis`. - PASS
2. Add `RateLimitRedisClient` and `UpstashRedisRateLimitStore` around the
   existing `RateLimitStore` contract. - PASS
3. Resolve Redis backend status only when `CVF_RATE_LIMIT_STORE=redis` and both
   Upstash REST env vars are present. - PASS
4. Update `/api/execute` to await the existing rate-limit consume call. - PASS
5. Use Redis command semantics for increment plus expiry. - PASS through fake client tests
6. Preserve user, service identity, IP, and provider quota behavior. - PASS
7. Add fake Redis client tests for allow, block, provider isolation, missing env
   fail-closed, malformed env fail-closed, and memory default. - PASS
8. Run focused tests, TypeScript check, and autorun gates. - PASS through focused tests/check; committed pre-closure gate required next

## Evidence Requirements

Evidence includes changed files, package install result, focused rate-limit
test output, TypeScript output, and pre-closure gate result in the completion
review.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| `@upstash/redis` is declared in package manifest and lockfile | PASS |
| Memory remains default and reports `distributed=false` | PASS |
| Redis mode requires URL and token env | PASS |
| Missing Redis env fails closed | PASS |
| Redis command semantics enforce user and provider limits | PASS |
| No raw Redis token is serialized or logged | PASS |
| Existing route contract awaits `consume` and remains compatible with `allowed` and `retryAfterSeconds` | PASS |
| No hosted distributed enforcement claim is made without live Redis proof | PASS |

## Review Gate

Reviewer must reject closure if the patch silently falls back from requested
Redis to memory, logs Redis secrets, claims hosted distributed enforcement
without external service proof, changes provider execution behavior, or omits
focused Redis semantics tests.

## Closure Checklist

| Item | Closure disposition requirement |
| --- | --- |
| Source scope | checked/PASS or BLOCKED with reason |
| Package install | checked/PASS or BLOCKED with reason |
| Focused tests | checked/PASS or BLOCKED with reason |
| TypeScript check | checked/PASS or BLOCKED with reason |
| Completion artifact | Public Export Disposition recorded |

## Return Conditions

Return to orchestrator if implementation requires hosted Redis provisioning,
provider API live quota, public-sync, route refactor beyond awaiting the
existing consume call, or a production distributed-rate-limit claim.

## 5. Execution Instructions

1. Keep memory mode as the default behavior.
2. Redis mode must be explicit through `CVF_RATE_LIMIT_STORE=redis`.
3. Redis mode must require `UPSTASH_REDIS_REST_URL` and
   `UPSTASH_REDIS_REST_TOKEN`.
4. Missing Redis env must block instead of using memory silently.
5. Do not print or serialize raw Redis URL/token values.
6. Update `/api/execute` only to await the existing consume call.
7. Do not change `/api/execute` 429 response contract.

## 6. Role Output Schema

Completion output must include:

- changed-file list;
- package install evidence;
- focused test command and result;
- TypeScript command and result;
- autorun gate result;
- explicit hosted-proof boundary;
- Public Export Disposition.

## 7. Dissent And Review Ledger

| Concern | Resolution |
| --- | --- |
| Adapter code can be mistaken for deployed distributed enforcement | Completion must distinguish adapter readiness from hosted Redis proof |
| Redis credentials may be absent locally | Missing env is a tested fail-closed path; no live Redis proof claimed |
| Upstash REST package adds vendor-specific dependency | Package registry evidence and explicit env naming are recorded; alternative TCP client rejected for this tranche |

## 8. Integration Decision

Proceed only after pre-dispatch and pre-implementation gates pass on the real
range `d30accb6..HEAD`.

## 9. Completion Evidence

Completion evidence must be recorded in a dedicated completion review before
any closed-equivalent status is claimed.

## 10. Claim Boundary

This work order cannot be used as evidence of hosted distributed enforcement or
production rate-limit readiness without a separate live Redis service proof.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ERH-RL1B does not create public-facing distributed rate-limit evidence
without hosted Redis proof.

Next action: separate live Redis service proof if CVF needs a hosted
multi-instance enforcement claim.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_WO_ERH_RL1B_DISTRIBUTED_RATE_LIMIT_BACKEND_2026-06-06.md` | `Status: PRE_CLOSURE_READY` before committed pre-closure gate | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_RL1B_DISTRIBUTED_RATE_LIMIT_BACKEND_COMPLETION_2026-06-06.md` | completion review path reserved for closure | PASS |
| Roadmap state | N/A with reason | ERH-RL1B is GC-018 continuity-derived; no roadmap artifact owns this tranche | N/A with reason |
| Registry JSON | BLOCKED with reason | corpus/search registry ownership is outside this runtime limiter tranche | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | corpus/search registry Markdown ownership is outside this runtime limiter tranche | BLOCKED with reason |
| External evidence digest | N/A with reason | no live Redis service evidence required for adapter-contract tranche | N/A with reason |
| System loop interlock | N/A with reason | no new route or system-loop chain is added | N/A with reason |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V16_2026-06-06.md` | session sync follows material commit | PASS |
