# CVF N7 Third Provider Expansion Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS

Date: 2026-05-24

## Purpose

Close N7 after adding the bounded OpenAI `gpt-4o` provider capability surface
and proving one governed live `/api/execute` call.

## Target / Source

Targets:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/provider-router-adapter.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.n7-openai-gpt4o.live.test.ts`

Source: `docs/work_orders/CVF_WO_N7_THIRD_PROVIDER_EXPANSION_2026-05-24.md`.

## Scope / Target / Owner Boundary

In scope: OpenAI `gpt-4o` registry coverage, targeted tests, and one live
governed proof.

Out of scope: broad provider stability, universal provider parity, receipt
schema changes, public-sync, hosted readiness, or production readiness.

## Scope / Methodology

Confirmed the existing web OpenAI executor and router already matched the
operator's R2 scope, added the missing Model Gateway registry row, and proved
the route with one live OpenAI `gpt-4o` receipt.

## Findings / Position

Position: N7 is closed pass. The missing governed surface was the Model Gateway
capability registry, not the web executor/router implementation.

## Risk / Corrective Action

Risk: one receipt could be overstated as broad provider stability. Corrective
action: completion wording is limited to one bounded `gpt-4o` governed call.

## Decision / Recommendation / Disposition

Disposition: CLOSED_PASS.

## Provider Named

Operator confirmed OpenAI, API base `https://api.openai.com/v1`, model
`gpt-4o`, `maxRiskLevel=R2`, and key env var `OPENAI_API_KEY`.

## GC-018 Reference

`docs/baselines/CVF_GC018_N7_THIRD_PROVIDER_EXPANSION_2026-05-24.md`

## Three Surfaces Updated / Verified

| Surface | Result |
| --- | --- |
| `cvf-web/src/lib/ai/providers.ts` | Existing OpenAI executor already routes to OpenAI chat completions; targeted `gpt-4o` test added. |
| `cvf-web/src/lib/ai/provider-router-adapter.ts` | Existing OpenAI router definition already has `maxRiskLevel=R2`; targeted router test added. |
| `CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | Added OpenAI `gpt-4o` registry entry with `complete`, `chat`, `json_mode`, and `vision`. |

## Live Proof Receipt

Full `cvf-web` regression included the N7 live proof:

- HTTP 200
- `success=true`
- provider `openai`
- model `gpt-4o`
- `evidenceMode=live`
- decision `ALLOW`
- routingDecision `ALLOW`
- receipt `rcpt-env-mpisddug-zq11zg`
- trace `env-mpisddug-zq11zg`
- `rawSecretPrinted=false`

Earlier targeted rerun also passed with receipt `rcpt-env-mpisbtzy-jjasvj`.

## Regression Evidence

- `cvf-web` targeted provider tests:
  - `providers.test.ts` + `provider-router-adapter.test.ts`: PASS, 45 tests.
- Model Gateway registry targeted:
  - PASS, 1 file / 8 tests.
- Model Gateway full:
  - PASS, 20 files / 82 tests.
- Model Gateway TypeScript:
  - PASS.
- `cvf-web` TypeScript:
  - PASS.
- Full `cvf-web`:
  - PASS, 221 files / 2753 passed / 2 skipped.

## Bounded Claim

N7 proves one OpenAI `gpt-4o` governed execution receipt through the existing
route. Existing Alibaba and DeepSeek tests remained green in the same full
suite.

## Claim Boundary

N7 does not claim broad OpenAI stability, universal provider parity, hosted
SaaS readiness, production readiness, receipt schema changes, public-sync
update, or freeze release.
