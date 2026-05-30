# CVF GC-018 N7 - Third Provider Expansion

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

Date: 2026-05-24

## Purpose

Authorize the bounded OpenAI provider lane addition for the operator-nominated
model `gpt-4o` with `maxRiskLevel=R2`.

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_POST_AIF_NEXT_VALUE_ROADMAP_2026-05-24.md`
- `docs/work_orders/CVF_WO_N7_THIRD_PROVIDER_EXPANSION_2026-05-24.md`
- `docs/reviews/archive/CVF_D10_QWEN3_R1_COMPATIBLE_HOSTED_PROOF_COMPLETION_2026-05-23.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`

## Decision / Baseline / Proposed Tranche

Decision: continue with one bounded OpenAI `gpt-4o` provider expansion.

Baseline: `cvf-web` already has an OpenAI executor and OpenAI router definition;
Model Gateway lacks the `gpt-4o` capability registry row.

Proposed tranche: add the registry row, add targeted tests, and run one live
governed `/api/execute` proof.

## Scope

In scope:

- confirm existing `cvf-web` OpenAI executor surface;
- confirm existing web provider router OpenAI `R2` ceiling;
- add Model Gateway provider capability registry entry for OpenAI `gpt-4o`;
- add targeted tests for executor, router, and registry;
- run one live governed `/api/execute` proof using `OPENAI_API_KEY`.

Out of scope:

- broad OpenAI stability;
- universal provider parity;
- receipt schema changes;
- route/auth/enforcement changes;
- public-sync push or production readiness claim.

## Provider Parameters

| Field | Value |
| --- | --- |
| Provider | OpenAI |
| API base URL | `https://api.openai.com/v1` |
| Model | `gpt-4o` |
| Max risk level | `R2` |
| Key env var | `OPENAI_API_KEY` / `CVF_OPENAI_API_KEY` |

## Depth Audit

| Candidate | Score | Decision | Rationale |
| --- | ---: | --- | --- |
| Add OpenAI `gpt-4o` registry entry and proof | 9/10 | CONTINUE | Completes the missing governed capability surface without route churn. |
| Rewrite existing OpenAI executor/router | 1/10 | REJECT | Existing surfaces already match the authorized provider/risk boundary. |
| Claim broad provider parity | 0/10 | REJECT | One live receipt is not a soak or parity proof. |

## Acceptance Criteria

N7 passes only if the three governed surfaces are covered, targeted tests pass,
existing Alibaba/DeepSeek paths remain green, one live receipt returns
`success=true`, `evidenceMode=live`, provider `openai`, model `gpt-4o`, and no
raw secret value is printed.

## Evidence / Verification

Verification requires targeted web provider/router tests, targeted and full
Model Gateway tests, `cvf-web` TypeScript check, one live N7 receipt, and the
mandatory release gate.

## Claim Boundary

N7 can claim one bounded OpenAI `gpt-4o` governed execution proof only. It does
not claim broad stability, production readiness, hosted SaaS readiness, or full
provider parity.
