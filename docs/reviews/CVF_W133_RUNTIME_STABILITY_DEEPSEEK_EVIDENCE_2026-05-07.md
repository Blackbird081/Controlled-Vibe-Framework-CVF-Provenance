<!-- Memory class: FULL_RECORD -->
# CVF W133 Runtime Stability — DeepSeek Confirmatory

**Run status:** complete
**Captured:** 2026-05-07T04:07:37.589Z
**Provider:** deepseek / deepseek-chat
**Session isolation:** per_journey_browser_context
**Inter-journey delay:** 1500ms (Fix-C)
**Tranche:** W133-T1 CP5 — DeepSeek Confirmatory Run

## Applied Fixes

| Fix | Description |
|---|---|
| Fix-A | `Connection: close` header + AbortSignal 60s (providers.ts) |
| Fix-B | Form-first routing precedence (intent-router.ts) |
| Fix-C | 1500ms inter-journey delay (this spec) |

## Journey Summary

| Metric | Value |
|---|---|
| Attempted | 6 |
| Accepted with receipt | 1 |
| Failure rate (timeout + fallback + provider_error) | 66.7% |
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
| `api_timeout` | 4 |
| `provider_error` | 0 |
| `mock_fallback_no_receipt` | 0 |
| `ui_flow_error` | 0 |

## Diagnostic Subcode Breakdown

| Subcode | Count |
|---|---|
| `provider_timeout` | 4 |
| `execute_route_timeout` | 0 |
| `missing_provider_key` | 0 |
| `provider_disabled` | 0 |
| `receipt_dropped` | 0 |
| `settings_not_hydrated` | 0 |
| `browser_context_closed` | 0 |
| `download_or_clipboard_blocked` | 0 |

## Journey Log

| # | Form Type | Outcome | Subcode | HTTP | Elapsed | Evidence | Pack | Receipt |
|---|---|---|---|---|---|---|---|---|
| 1 | documentation | `accepted_with_exports` | — | 200 | 40044ms | ✅ | ✅ | ✅ |
| 2 | email_template | `api_timeout` | provider_timeout | 400 | 92832ms | ❌ | ❌ | ❌ |
| 3 | risk_assessment | `api_timeout` | provider_timeout | 400 | 92815ms | ❌ | ❌ | ❌ |
| 4 | competitor_review | `api_timeout` | provider_timeout | 400 | 92886ms | ❌ | ❌ | ❌ |
| 5 | user_persona | `route_miss` | — | — | 16673ms | ❌ | ❌ | ❌ |
| 6 | strategy_analysis | `api_timeout` | provider_timeout | 400 | 92819ms | ❌ | ❌ | ❌ |
