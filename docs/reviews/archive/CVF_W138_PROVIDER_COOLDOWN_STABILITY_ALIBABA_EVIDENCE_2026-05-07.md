<!-- Memory class: FULL_RECORD -->
# CVF W138 Runtime Stability — Alibaba Primary

**Run status:** complete
**Captured:** 2026-05-07T16:51:25.908Z
**Provider:** alibaba / qwen-plus
**Session isolation:** per_journey_browser_context
**Inter-journey delay:** 7500ms (Fix-C)
**Tranche:** W138-T1 CP2 — Alibaba Provider Cooldown Full Matrix

## Applied Fixes

| Fix | Description |
|---|---|
| Fix-A | `Connection: close` header + AbortSignal 60s (providers.ts) |
| Fix-B | Form-first routing precedence (intent-router.ts) |
| Fix-C | 7500ms inter-journey delay (this spec) |
| Fix-D | Normalized trusted-form guard action before Guard Runtime (`route.ts`, `ProcessingScreen.tsx`) |
| Fix-E | `competitor_review` output-validation false-positive hardening (W135) |
| Fix-F | Trusted-form token cap + route retry budget guard (W136) |
| CP1 | `/api/execute` response body captured in `JourneyRecord.responseBody` |

## Journey Summary

| Metric | Value |
|---|---|
| Attempted | 12 |
| Accepted with receipt | 10 |
| Failure rate (timeout + fallback + provider_error) | 16.7% |
| Live HTTP status | 200 |
| Live decision | ALLOW |

## Outcome Breakdown

| Outcome | Count |
|---|---|
| `accepted_with_exports` | 10 |
| `accepted_missing_receipt` | 0 |
| `accepted_export_failed` | 0 |
| `route_miss` | 0 |
| `clarification_not_recovered` | 0 |
| `api_timeout` | 2 |
| `provider_error` | 0 |
| `mock_fallback_no_receipt` | 0 |
| `ui_flow_error` | 0 |

## Diagnostic Subcode Breakdown

| Subcode | Count |
|---|---|
| `provider_timeout` | 0 |
| `execute_route_timeout` | 2 |
| `missing_provider_key` | 0 |
| `provider_disabled` | 0 |
| `receipt_dropped` | 0 |
| `settings_not_hydrated` | 0 |
| `browser_context_closed` | 0 |
| `download_or_clipboard_blocked` | 0 |

## Journey Log

| # | Form Type | Outcome | Subcode | HTTP | Elapsed | Evidence | Pack | Receipt |
|---|---|---|---|---|---|---|---|---|
| 1 | documentation | `accepted_with_exports` | — | 200 | 33450ms | ✅ | ✅ | ✅ |
| 2 | email_template | `accepted_with_exports` | — | 200 | 14674ms | ✅ | ✅ | ✅ |
| 3 | risk_assessment | `accepted_with_exports` | — | 200 | 35909ms | ✅ | ✅ | ✅ |
| 4 | competitor_review | `accepted_with_exports` | — | 200 | 28113ms | ✅ | ✅ | ✅ |
| 5 | user_persona | `accepted_with_exports` | — | 200 | 42895ms | ✅ | ✅ | ✅ |
| 6 | strategy_analysis | `accepted_with_exports` | — | 200 | 42829ms | ✅ | ✅ | ✅ |
| 7 | feature_prioritization | `accepted_with_exports` | — | 200 | 21895ms | ✅ | ✅ | ✅ |
| 8 | pricing_strategy | `accepted_with_exports` | — | 200 | 37267ms | ✅ | ✅ | ✅ |
| 9 | documentation | `api_timeout` | execute_route_timeout | — | 92898ms | ❌ | ❌ | ❌ |
| 10 | email_template | `accepted_with_exports` | — | 200 | 13628ms | ✅ | ✅ | ✅ |
| 11 | risk_assessment | `accepted_with_exports` | — | 200 | 35733ms | ✅ | ✅ | ✅ |
| 12 | strategy_analysis | `api_timeout` | execute_route_timeout | — | 92947ms | ❌ | ❌ | ❌ |
