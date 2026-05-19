<!-- Memory class: FULL_RECORD -->
# CVF W133 Runtime Stability — Alibaba Primary

**Run status:** complete
**Captured:** 2026-05-07T03:58:28.109Z
**Provider:** alibaba / qwen-plus
**Session isolation:** per_journey_browser_context
**Inter-journey delay:** 1500ms (Fix-C)
**Tranche:** W133-T1 CP4 — Alibaba Isolated Stability Run

## Applied Fixes

| Fix | Description |
|---|---|
| Fix-A | `Connection: close` header + AbortSignal 60s (providers.ts) |
| Fix-B | Form-first routing precedence (intent-router.ts) |
| Fix-C | 1500ms inter-journey delay (this spec) |

## Journey Summary

| Metric | Value |
|---|---|
| Attempted | 12 |
| Accepted with receipt | 1 |
| Failure rate (timeout + fallback + provider_error) | 83.3% |
| Live HTTP status | 200 |
| Live decision | ALLOW |

## Outcome Breakdown

| Outcome | Count |
|---|---|
| `accepted_with_exports` | 1 |
| `accepted_missing_receipt` | 0 |
| `accepted_export_failed` | 0 |
| `route_miss` | 1 |
| `clarification_not_recovered` | 0 |
| `api_timeout` | 10 |
| `provider_error` | 0 |
| `mock_fallback_no_receipt` | 0 |
| `ui_flow_error` | 0 |

## Diagnostic Subcode Breakdown

| Subcode | Count |
|---|---|
| `provider_timeout` | 8 |
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
| 1 | documentation | `accepted_with_exports` | — | 200 | 36227ms | ✅ | ✅ | ✅ |
| 2 | email_template | `api_timeout` | provider_timeout | 400 | 92872ms | ❌ | ❌ | ❌ |
| 3 | risk_assessment | `api_timeout` | provider_timeout | 400 | 92913ms | ❌ | ❌ | ❌ |
| 4 | competitor_review | `api_timeout` | provider_timeout | 400 | 92837ms | ❌ | ❌ | ❌ |
| 5 | user_persona | `route_miss` | — | — | 16713ms | ❌ | ❌ | ❌ |
| 6 | strategy_analysis | `api_timeout` | provider_timeout | 400 | 92797ms | ❌ | ❌ | ❌ |
| 7 | feature_prioritization | `api_timeout` | provider_timeout | 400 | 92835ms | ❌ | ❌ | ❌ |
| 8 | pricing_strategy | `api_timeout` | provider_timeout | 400 | 92807ms | ❌ | ❌ | ❌ |
| 9 | documentation | `api_timeout` | execute_route_timeout | — | 92878ms | ❌ | ❌ | ❌ |
| 10 | email_template | `api_timeout` | provider_timeout | 400 | 93018ms | ❌ | ❌ | ❌ |
| 11 | risk_assessment | `api_timeout` | provider_timeout | 400 | 92826ms | ❌ | ❌ | ❌ |
| 12 | strategy_analysis | `api_timeout` | execute_route_timeout | — | 92914ms | ❌ | ❌ | ❌ |
