# GC-018 Continuation Candidate — GAP 6 Provider Risk Cap ENV Override

Memory class: FULL_RECORD

Status: AUTHORIZED

Date: 2026-06-06

dispatchBaseHead: `7c6b4578`

## Purpose

Authorize the bounded implementation of GAP 6: externalize per-provider risk
caps from a static constant into ENV-overridable values in the web adapter,
so operators can adjust provider risk ceilings without code changes.

## Operator Authorization

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator direct instruction | 2026-06-06 session: "Làm luôn đi" after GAP 6 analysis and hướng xử lý confirmation | ACCEPT |
| GAP 6 diagnosis | `docs/audits/CVF_EXTERNAL_REVIEW_GAP_ANALYSIS_AND_PROPOSED_SOLUTIONS_2026-06-05.md` GAP 6 section | ACCEPT |

## Scope

In scope:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/provider-router-adapter.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/provider-router-adapter.test.ts`

Out of scope:

- `CVF_CONTROL_PLANE_FOUNDATION` (already configurable — no change)
- Runtime route, execute pipeline, auth, session, memory, public-sync
- Any other provider file, test, or governance document

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `WEB_PROVIDER_DEFINITIONS` hardcodes `maxRiskLevel` per provider | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/provider-router-adapter.ts` | lines 70–119 | `WEB_PROVIDER_DEFINITIONS` | `provider-router-adapter` module | ACCEPT |
| `riskCeiling: 'R2'` hardcoded in `routeWebProvider` | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/provider-router-adapter.ts` | line 252 | `riskCeiling` in `ProviderPolicy` literal | `routeWebProvider` | ACCEPT |
| `ProviderRouterContract` in CVF_CONTROL_PLANE_FOUNDATION already configurable | EXISTS | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/provider.router.contract.ts` | line 20 — `maxRiskLevel: RiskLevel` as struct field | `ProviderDefinition.maxRiskLevel` | `ProviderDefinition` | ACCEPT |
| `process.env` available in Next.js server context | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts` | line 20–21: function `resolveProviderTimeoutMs` reads `process.env.CVF_AI_PROVIDER_TIMEOUT_MS` — confirms `process.env` is already used in this lib directory | `resolveProviderTimeoutMs` | `providers` module | ACCEPT |

## Decisions

| Item | Decision | Boundary |
| --- | --- | --- |
| ENV var naming | `CVF_PROVIDER_RISK_CAP_<PROVIDER_ID_UPPERCASE>` per provider; `CVF_PROVIDER_RISK_CEILING` for policy ceiling | No other env names introduced |
| Invalid value handling | Silently ignored; static default used | No error thrown; backward compatible |
| Resolution timing | Lazy — resolved at `routeWebProvider` call time via `buildProviderDefinitions()` | Enables test-time env mutation; no module-level side effect |
| `WEB_PROVIDER_DEFINITIONS` export | Preserved as static snapshot (for test introspection of defaults) | Export remains; does not reflect runtime env overrides |

## Evidence

| Evidence | Result |
| --- | --- |
| TypeScript type check (`tsc --noEmit`) | PASS — no errors |
| Focused adapter tests (6 tests) | PASS — 6/6 including 4 new ENV override tests |
| Full cvf-web test suite | PASS — exit code 0 |
| Backward compatibility (env vars absent) | PASS — existing tests unchanged; static defaults preserved |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| Provider risk caps hardcoded in web adapter with no ENV override path | RULE_GAP | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | Operator can now override via ENV without code change; static fallback preserved |

## Claim Boundary

This GC-018 authorizes only:

- adding `resolveProviderRiskCap` and `resolveRiskCeiling` helpers reading `process.env`;
- making `WEB_PROVIDER_DEFINITIONS` lazy-resolved at call time via `buildProviderDefinitions()`;
- 4 new tests covering env-override, absent-env, invalid-env, and ceiling-override paths.

This does NOT authorize: changes to `CVF_CONTROL_PLANE_FOUNDATION`, runtime
route behavior, provider key management, auth, session, memory, public-sync,
hosted readiness, production readiness, or any other surface.
