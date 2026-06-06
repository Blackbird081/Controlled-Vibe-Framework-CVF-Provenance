# CVF WO DEP2 Next-Auth Stable Migration Decision

Memory class: POINTER_RECORD

Status: BACKLOG_SOURCE_VERIFIED

## Purpose

Prevent repeated `next-auth` beta findings from being resolved with an
unsupported downgrade or an unverified stable target.

## Authority Chain

- Operator P1-P5 remediation request, 2026-06-06.
- ERH-DEP1 dependency risk workflow chain.
- Active handoff: `AGENT_HANDOFF_V16_2026-06-06.md`.

## Objective

Resolve the `next-auth` beta debt only when there is a source-backed migration
target or explicit authority for an API migration.

## Agent Roles

Orchestrator verifies package metadata and migration authority. Implementer owns
the auth diff only after release conditions are met. Reviewer checks source
fidelity, auth behavior, and dependency risk evidence.

## Required First Reads

- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/baselines/CVF_ERH_T4_NEXT_AUTH_BETA_DECISION_BASELINE_2026-06-04.md`
- `docs/reviews/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`

## Pre-Flight Checks

- `npm view next-auth version dist-tags --json`
- `rg -n '"next-auth"|NextAuth\\(' EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD`

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Web package declares `next-auth` beta range | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | line 30 | `next-auth` | cvf-web package manifest | ACCEPT |
| Lockfile root dependency keeps same beta range | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` | line 21 | `next-auth` | cvf-web lockfile | ACCEPT |
| Auth runtime uses v5-style `NextAuth` export | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | line 113 | `NextAuth(nextAuthConfig)` | Auth.js runtime adapter | ACCEPT |
| Next route delegates to exported handlers | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/auth/[...nextauth]/route.ts` | line 3 | `handlers` | Next.js auth route | ACCEPT |
| Stable v5 package target exists | npm registry metadata, command `npm view next-auth version dist-tags --json` on 2026-06-06 | `latest=4.24.14`, `beta=5.0.0-beta.31` | `next-auth` | npm package metadata | REJECT - stable v5 not available |

## Allowed Scope

- Refresh npm metadata.
- Review official Auth.js migration notes when stable v5 becomes available.
- Produce migration diff only if the package target and runtime API are source
  verified.
- Add tests for auth session, credential login, OAuth callback stubs, and route
  handler behavior.

## Forbidden Scope

- Do not downgrade to v4 as a "small fix" without a full migration plan.
- Do not remove auth, weaken auth checks, or commit provider secrets.
- Do not claim production auth readiness while this work order remains on hold.

## Write Ownership

Allowed after release: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`,
`package-lock.json`, auth route/runtime files, and focused auth tests.

Forbidden without new authority: public-sync claims, provider secrets, unrelated
dependency upgrades, and non-auth runtime refactors.

## Execution Plan

1. Refresh package metadata and choose a source-backed target.
2. Review Auth.js runtime API differences.
3. Implement the smallest compatible migration.
4. Add or update auth tests.
5. Run web and governance gates.

## Release Conditions

This work order may move to execution only when one condition is met:

- npm metadata shows a stable v5-compatible target; or
- operator explicitly authorizes a v4 migration with Auth.js API review; or
- CVF replaces Auth.js with a different approved stable auth provider.

## Evidence Requirements

- `npm view next-auth version dist-tags --json`
- `npm audit --audit-level=high`
- auth unit tests
- web lint/build/tests
- pre-closure autorun gate with real base/head range

## Acceptance Criteria

- Auth dependency target is stable or explicitly authorized.
- Runtime handlers still export `GET` and `POST`.
- Credentials and OAuth route behavior remain covered by tests.
- No secrets are printed or committed.

## Review Gate

Reviewer must reject migration if the package target is not source-backed or if
the diff weakens auth behavior to satisfy dependency hygiene.

## Closure Checklist

- [x] Backlog packet source facts verified.
- [ ] Release condition satisfied.
- [ ] Migration diff implemented.
- [ ] Auth tests and web gates passed.
- [ ] Autorun pre-closure passed with real committed range.

## Return-To-Orchestrator Conditions

Return if stable target remains unavailable, package metadata conflicts with
runtime API, or migration requires product auth policy changes.

## operator.checkpoint.waiver

Required before v4 downgrade, provider replacement, public production-auth
claim, or any secret-bearing live auth proof.

## Claim Boundary

This packet records a source-verified dependency decision. It does not authorize
or claim a completed auth migration.
