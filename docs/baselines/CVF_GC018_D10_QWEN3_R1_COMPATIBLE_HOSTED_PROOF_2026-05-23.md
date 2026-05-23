# CVF GC-018 D10 - Qwen3 R1 Compatible Hosted Proof

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

Date: 2026-05-23

## Purpose

Authorize one narrow follow-up hosted proof for
`qwen3-235b-a22b-thinking-2507` using a provider-router-compatible `R1`
payload.

## Scope

In scope:

- no source-code changes unless local preflight exposes a direct blocker;
- one concrete `strategy_analysis` payload;
- requested provider/model: Alibaba `qwen3-235b-a22b-thinking-2507`;
- `cvfRiskLevel=R1`;
- Skill Preflight plus `aiCommit`;
- exactly one hosted proof call.

Out of scope:

- weakening provider routing;
- changing route/auth/safety/receipt/guard semantics;
- broad Qwen3/provider stability;
- hosted SaaS readiness;
- public production readiness;
- retry loops.

## Source / Predecessor Evidence

D9 blocker:

`docs/reviews/CVF_D9_QWEN3_THINKING_ENABLE_TRUE_ADAPTER_BLOCKER_REVIEW_2026-05-23.md`

D9 showed that `R2` payloads are denied by the current web provider router
because Alibaba is bounded at `maxRiskLevel=R1`.

## Decision / Baseline / Proposed Tranche

Decision: continue with one `R1`-compatible hosted proof.

Baseline: adapter code is already public at commit `811e59f6`, and local tests
prove:

- `qwen3-32b` sends `enable_thinking=false`;
- `qwen3-235b-a22b-thinking-2507` sends `enable_thinking=true`;
- `qwen-turbo` sends no `enable_thinking`.

Proposed tranche: run one hosted proof whose risk posture does not violate the
existing provider router.

## Depth Audit

| Candidate | Type | Score | Decision | Rationale |
| --- | --- | ---: | --- | --- |
| Use `R1` proof payload | VALIDATION_TEST | 9/10 | CONTINUE | D9 isolated failure to router risk posture, not provider adapter. |
| Raise Alibaba `maxRiskLevel` | GOVERNANCE_SEMANTIC_CHANGE | 0/10 | REJECT | Would weaken policy to force a proof. |
| Retry D9 unchanged | RETRY_LOOP | 0/10 | REJECT | D9 already proved the `R2` payload is router-denied. |

## Acceptance Criteria

D10 passes only if:

- focused provider tests still pass;
- `cvf-web` check still passes;
- local router preflight shows Alibaba `ALLOW` for `R1`;
- exactly one hosted proof returns HTTP `200`, `success=true`, ALLOW routing
  and enforcement, live evidence, Alibaba provider, requested model id, receipt
  and trace present, and raw secret printed false.

## Evidence / Verification

Verification requires focused provider tests, `cvf-web` check, local router
preflight, one hosted proof result, and governance hook evidence.

## Claim Boundary

D10 can claim only a bounded one-call hosted proof for the corrected Qwen3
thinking adapter under the current `R1` Alibaba provider-router boundary.
It cannot claim broad Qwen3 stability, hosted SaaS readiness, production
readiness, all-risk Alibaba routing, public release readiness, or freeze
release.
