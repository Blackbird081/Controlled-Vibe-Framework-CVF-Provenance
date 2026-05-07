<!-- Memory class: FULL_RECORD -->
# CVF W137 Runtime Stability — DeepSeek Confirmatory

**Run status:** complete
**Captured:** 2026-05-07T16:39:17.778Z
**Provider:** deepseek / deepseek-chat
**Session isolation:** per_journey_browser_context
**Inter-journey delay:** 1500ms (Fix-C)
**Tranche:** W137-T1 CP3 — DeepSeek Confirmatory Full Matrix

## Applied Fixes

| Fix | Description |
|---|---|
| Fix-A | `Connection: close` header + AbortSignal 60s (providers.ts) |
| Fix-B | Form-first routing precedence (intent-router.ts) |
| Fix-C | 1500ms inter-journey delay (this spec) |
| Fix-D | Normalized trusted-form guard action before Guard Runtime (`route.ts`, `ProcessingScreen.tsx`) |
| Fix-E | `competitor_review` output-validation false-positive hardening (W135) |
| Fix-F | Trusted-form token cap + route retry budget guard (W136) |
| CP1 | `/api/execute` response body captured in `JourneyRecord.responseBody` |

## Journey Summary

| Metric | Value |
|---|---|
| Attempted | 6 |
| Accepted with receipt | 6 |
| Failure rate (timeout + fallback + provider_error) | 0.0% |
| Live HTTP status | 200 |
| Live decision | ALLOW |

## Outcome Breakdown

| Outcome | Count |
|---|---|
| `accepted_with_exports` | 6 |
| `accepted_missing_receipt` | 0 |
| `accepted_export_failed` | 0 |
| `route_miss` | 0 |
| `clarification_not_recovered` | 0 |
| `api_timeout` | 0 |
| `provider_error` | 0 |
| `mock_fallback_no_receipt` | 0 |
| `ui_flow_error` | 0 |

## Diagnostic Subcode Breakdown

| Subcode | Count |
|---|---|
| `provider_timeout` | 0 |
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
| 1 | documentation | `accepted_with_exports` | — | 200 | 33401ms | ✅ | ✅ | ✅ |
| 2 | email_template | `accepted_with_exports` | — | 200 | 17132ms | ✅ | ✅ | ✅ |
| 3 | risk_assessment | `accepted_with_exports` | — | 200 | 38601ms | ✅ | ✅ | ✅ |
| 4 | competitor_review | `accepted_with_exports` | — | 200 | 28832ms | ✅ | ✅ | ✅ |
| 5 | user_persona | `accepted_with_exports` | — | 200 | 36454ms | ✅ | ✅ | ✅ |
| 6 | strategy_analysis | `accepted_with_exports` | — | 200 | 31323ms | ✅ | ✅ | ✅ |
