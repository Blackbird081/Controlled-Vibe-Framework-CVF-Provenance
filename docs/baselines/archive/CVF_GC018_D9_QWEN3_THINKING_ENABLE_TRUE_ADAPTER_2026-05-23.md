# CVF GC-018 D9 Qwen3 Thinking Enable True Adapter

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

## Purpose

Authorize a narrow adapter correction after D8 proved the hosted Qwen3 thinking
model reaches provider execution but fails because the request uses
`enable_thinking=false`.

## Scope / Target / Owner Boundary

In scope:

- adjust Alibaba provider request body logic so Qwen3 thinking model ids use
  `enable_thinking=true`;
- keep standard Qwen3 non-streaming models on `enable_thinking=false`;
- add focused provider tests;
- run local checks;
- run exactly one hosted proof call with Skill Preflight and `aiCommit`;
- file completion or blocker review;
- sync public-safe changes through public-sync only after provenance closure.

Out of scope:

- route/auth/safety/receipt/guard changes;
- broad provider parameter tuning;
- retry loops under D9;
- hosted environment variable changes;
- production/hosted readiness claims.

## Source / Predecessor Evidence

Source evidence is D8: hosted route reached Alibaba with live ALLOW evidence,
but the provider rejected `enable_thinking=false` for
`qwen3-235b-a22b-thinking-2507`.

## Decision / Baseline / Proposed Tranche

Decision: authorize D9.

Baseline: D4 broad Qwen3 adapter rule sets `enable_thinking=false` for all
non-streaming Qwen3 models.

Proposed tranche: split the adapter rule so thinking model ids send
`enable_thinking=true`.

## Depth Audit

| Candidate | Type | Score | Decision | Rationale |
| --- | --- | ---: | --- | --- |
| Split Qwen3 thinking parameter branch | BUG_FIX / VALIDATION_TEST | 9/10 | CONTINUE | D8 live provider error directly identifies the wrong parameter value. |
| Keep D4 broad `enable_thinking=false` rule | KNOWN_BAD | 0/10 | REJECT | D8 proved the thinking model rejects it. |
| Disable `enable_thinking` for thinking model | SPECULATION | 2/10 | REJECT | Provider message says the value is restricted to true. |

## Acceptance Criteria

D9 may close PASS only if:

- focused provider tests prove `qwen3-32b` sends `enable_thinking=false`;
- focused provider tests prove `qwen3-235b-a22b-thinking-2507` sends
  `enable_thinking=true`;
- `qwen-turbo` remains without `enable_thinking`;
- `cvf-web` check passes;
- local safety/enforcement/guard preflight passes;
- exactly one hosted proof returns HTTP 200, `success=true`, ALLOW routing and
  enforcement, live evidence, Alibaba provider, corrected model id, receipt and
  trace present, raw secret printed false.

## Evidence / Verification

Verification requires focused provider tests, `cvf-web` check, local route
preflight, one hosted proof result, public-sync verification if deployed, and
governance hook evidence.

## Claim Boundary

D9 can claim only the corrected Qwen3 thinking model adapter proof and bounded
hosted proof result. It cannot claim broad Qwen3 stability, hosted SaaS
readiness, production readiness, provider account coverage beyond the observed
call, public release readiness, or freeze release.

## Handoff Sync Addendum

Handoff V11 records commit `70eced06` as the D9 adapter dispatch head before
public-sync deployment and the single hosted proof attempt.
