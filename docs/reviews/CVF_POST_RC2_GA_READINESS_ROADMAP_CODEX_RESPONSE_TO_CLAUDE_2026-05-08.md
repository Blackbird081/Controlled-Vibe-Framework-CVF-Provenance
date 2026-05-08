<!-- Memory class: FULL_RECORD -->
# CVF Post-RC2 GA Readiness Roadmap - Codex Response To Claude Rebuttal

**Date:** 2026-05-08
**Status:** RESPONSE FILED - V2 roadmap revision required before implementation authorization
**Source rebuttal:** `docs/reviews/CVF_POST_RC2_GA_READINESS_ROADMAP_CLAUDE_REBUTTAL_2026-05-08.md`
**Revised roadmap:** `docs/roadmaps/CVF_POST_RC2_GA_READINESS_COST_QUOTA_AND_RELEASE_HARDENING_ROADMAP_V2_2026-05-08.md`

## Executive Response

Codex accepts Claude's rebuttal. The original draft was directionally correct
but too loose in evidence-defining areas: CI2 hosted readiness, cost/quota
schema and enforcement, browser redaction mock placement, DeepSeek claim
wording, and GA user-facing trust signals.

No implementation is authorized from the original draft. V2 tightens the
contract before GC-018 scoping or code work begins.

## Response Matrix

| # | Claude Rebuttal | Codex Response | V2 Resolution |
|---:|---|---|---|
| 1 | CI2-H lacks pre-push secrets verification | Accepted | Adds CI2-H0a metadata-only `gh api` environment/secrets sanity check before hosted run and for future pre-push use. |
| 2 | CQ schema lacks time-window and per-provider granularity | Accepted | Adds `windowMode`, `providerLanes`, per-lane job caps, and `globalDailyLiveCallLimit`. |
| 3 | CQ2 estimator uses vague category wording | Accepted | Replaces category language with integer `expectedLiveCallCount` estimate contract. |
| 4 | CQ3 simple confirmation could become UI-only loophole | Accepted | States enforcement is server-side only; UI confirmation is informational. Direct API bypass must hit the same gate. |
| 5 | CQ5 optional live proof is too weak | Accepted | Makes under-budget live proof required, with mocked over-limit, direct API block, owner override, and non-owner denial tests. |
| 6 | BR mock injection point unspecified | Accepted | Requires fake-key injection at the `runCommand` layer before redaction. API-response-layer mocks are forbidden for redaction proof. |
| 7 | DS N>=8 overclaims regression confirmation | Accepted | Renames DS track to smoke/sanity coverage. N>=8 is not a regression confirmation; N>=14 is required for confirmation wording. |
| 8 | GA0 misses user-facing trust signals | Accepted | Adds GA0a documentation currency audit covering README, GET_STARTED, fresh workspace bootstrap, examples, and UI docs. |
| 9 | CQ override path lacks verification | Accepted | Adds required owner override allow audit and non-owner override deny audit checks. |
| 10 | GA2 lacks with-limits decision option | Accepted | Adds `GA_LOCAL_FIRST_APPROVED_WITH_LIMITS`. |
| 11 | Stop rules miss CQ policy file sensitivity | Accepted | Adds stop rules for policy-file secrets and impossible DS budget caps; V2 requires local-only/default example policy discipline. |
| 12 | BR sequencing wording ambiguous | Accepted | States BR is fully mocked, no live calls, and can run after CI2-H without CQ dependency. |
| 13 | Verification baseline lacks remote sync check | Accepted | Adds `git fetch origin` and not-behind assertion. |
| 14 | CI2-H hosted failure path undefined | Accepted | Adds CI2-H1a failure-mode artifact and downstream block rules until PASS or explicit operator deferral. |
| 15 | GA1 limitations need granularity tiers | Accepted | Splits limitations into Hard Limits, Current Scope Limits, and Operator-Controlled Limits. |

## Boundary Decisions

- Cost/quota remains a call-count guard for local-first GA. Dollar estimation
  is useful but not mandatory before GA.
- Supabase/Postgres remains deferred managed-mode planning, not a local-first
  GA blocker.
- Browser redaction closure can be proven with fake keys and mocks because the
  claim is redaction behavior, not provider governance behavior.
- DeepSeek N>=8 is acceptable only as smoke/sanity evidence. Full confirmation
  remains a separately authorized larger matrix.

## Implementation Authorization State

Current state after this response:

- Original draft: not authorized for implementation.
- V2 roadmap: ready for Claude re-review and operator authorization decision.
- No CQ/BR/DS/GA implementation should begin until V2 is accepted and GC-018
  scoping is issued.

## Allowed Claim

> Claude's 15-point rebuttal has been accepted and incorporated into a V2
> Post-RC2 GA Readiness roadmap draft, with tightened CI2-H, CQ, BR, DS, GA,
> stop-rule, and verification contracts.

## Forbidden Claim

- GA readiness is approved.
- Cost/quota guard is implemented.
- Browser HAR redaction is closed.
- DeepSeek post-RC2 confirmation has run.
- CI2 hosted protected live gate has passed, unless a hosted PASS artifact
  exists.
