# CVF WO ERH-RL1 Distributed Rate Limiter Boundary

Memory class: POINTER_RECORD

Status: BACKLOG_SOURCE_VERIFIED

## Purpose

Prevent repeated multi-instance rate-limit findings from being closed by a
process-local implementation or placeholder Redis claim.

## Authority Chain

- Operator P1-P5 remediation request, 2026-06-06.
- External review operations-debt finding.
- Active handoff: `AGENT_HANDOFF_V16_2026-06-06.md`.

## Objective

Replace the current process-local runtime rate limiter with a distributed
backend only after the target deployment topology and Redis-compatible package
choice are source-backed.

## Agent Roles

Orchestrator chooses infra/package authority. Implementer owns the store
contract and runtime integration. Reviewer verifies multi-instance semantics and
fallback behavior.

## Required First Reads

- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.test.ts`

## Pre-Flight Checks

- `rg -n "getRateLimiter|CVF_RATE_LIMIT|CVF_PROVIDER_QUOTA_PER_MIN" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src`
- package-risk review for the chosen Redis-compatible dependency;
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD`.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Current limiter stores buckets in process memory | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | line 6 | `buckets` | runtime rate limiter | ACCEPT |
| Current limiter supports request cap env | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | line 11 | `CVF_RATE_LIMIT` | runtime rate limiter | ACCEPT |
| Current limiter supports provider quota env | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | line 12 | `CVF_PROVIDER_QUOTA_PER_MIN` | runtime rate limiter | ACCEPT |
| Execute route consumes the limiter | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 90 | `getRateLimiter` | governed execute route | ACCEPT |
| Redis runtime dependency exists in package manifest | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependencies section | `redis` | cvf-web package manifest | BLOCKED_SOURCE_NOT_FOUND |

## Allowed Scope

- Add a `RateLimitStore` interface.
- Preserve the current in-memory implementation as dev/default mode.
- Add a Redis-backed implementation only after package and infra decision.
- Add tests proving per-user and per-provider buckets remain compatible.

## Forbidden Scope

- Do not claim multi-instance safety while only process-local memory is used.
- Do not add a Redis package without package-risk review.
- Do not require Redis for local development unless an explicit fallback exists.

## Write Ownership

Allowed after release: rate-limit implementation/tests, execute-route tests,
package manifest/lockfile for the approved Redis dependency, and docs for env
configuration.

Forbidden without new authority: auth migration, provider routing changes,
PostgreSQL/SSO implementation, and production-readiness claims.

## Execution Plan

1. Define `RateLimitStore` contract.
2. Preserve in-memory local/dev default.
3. Implement Redis-compatible store when package authority exists.
4. Prove per-user and per-provider limits across the store boundary.
5. Document environment variables and fallback behavior.

## Release Conditions

This work order may move to execution only when:

- Redis-compatible package and version are chosen;
- deployment env names are approved;
- tests can run without a real Redis service through a store contract or local
  test adapter.

## Evidence Requirements

- package diff and lockfile diff;
- rate-limit unit tests;
- governed execute route regression test;
- web lint/build/tests;
- pre-closure autorun gate with real base/head range.

## Acceptance Criteria

- Multi-instance safety is claimed only for the distributed store mode.
- Local development still works without Redis.
- Provider quota and user/IP limits preserve existing behavior.
- Failure mode is explicit when Redis is configured but unreachable.

## Review Gate

Reviewer must reject any implementation that keeps process-local memory while
claiming distributed protection.

## Closure Checklist

- [x] Backlog packet source facts verified.
- [ ] Redis package/infra decision recorded.
- [ ] Store contract and tests implemented.
- [ ] Web and autorun gates passed.

## Return-To-Orchestrator Conditions

Return if no Redis-compatible package is approved, no deployment topology is
available, or test coverage cannot prove existing limit behavior.

## operator.checkpoint.waiver

Required before adding paid managed Redis, changing production env names, or
claiming hosted multi-instance readiness.

## Claim Boundary

This packet identifies the exact process-local boundary. It does not claim
distributed rate limiting, Redis availability, or production multi-instance
safety.
