<!-- Memory class: FULL_RECORD -->
# CVF W134 Runtime Stability — Alibaba Primary

**Run status:** complete
**Captured:** 2026-05-07T09:35:08.716Z
**Provider:** alibaba / qwen-plus
**Session isolation:** per_journey_browser_context
**Inter-journey delay:** 1500ms (Fix-C)
**Tranche:** W134-T1 CP4 — Alibaba Isolated Stability Run

## Applied Fixes

| Fix | Description |
|---|---|
| Fix-A | `Connection: close` header + AbortSignal 60s (providers.ts) |
| Fix-B | Form-first routing precedence (intent-router.ts) |
| Fix-C | 1500ms inter-journey delay (this spec) |
| Fix-D | Normalized trusted-form guard action before Guard Runtime (`route.ts`, `ProcessingScreen.tsx`) |
| CP1 | `/api/execute` response body captured in `JourneyRecord.responseBody` |

## Journey Summary

| Metric | Value |
|---|---|
| Attempted | 12 |
| Accepted with receipt | 9 |
| Failure rate (timeout + fallback + provider_error) | 25.0% |
| Live HTTP status | 200 |
| Live decision | ALLOW |

## Outcome Breakdown

| Outcome | Count |
|---|---|
| `accepted_with_exports` | 9 |
| `accepted_missing_receipt` | 0 |
| `accepted_export_failed` | 0 |
| `route_miss` | 0 |
| `clarification_not_recovered` | 0 |
| `api_timeout` | 2 |
| `provider_error` | 0 |
| `mock_fallback_no_receipt` | 1 |
| `ui_flow_error` | 0 |

## Diagnostic Subcode Breakdown

| Subcode | Count |
|---|---|
| `provider_timeout` | 0 |
| `execute_route_timeout` | 2 |
| `missing_provider_key` | 0 |
| `provider_disabled` | 0 |
| `receipt_dropped` | 1 |
| `settings_not_hydrated` | 0 |
| `browser_context_closed` | 0 |
| `download_or_clipboard_blocked` | 0 |

## Journey Log

| # | Form Type | Outcome | Subcode | HTTP | Elapsed | Evidence | Pack | Receipt |
|---|---|---|---|---|---|---|---|---|
| 1 | documentation | `accepted_with_exports` | — | 200 | 33316ms | ✅ | ✅ | ✅ |
| 2 | email_template | `accepted_with_exports` | — | 200 | 14172ms | ✅ | ✅ | ✅ |
| 3 | risk_assessment | `accepted_with_exports` | — | 200 | 38541ms | ✅ | ✅ | ✅ |
| 4 | competitor_review | `mock_fallback_no_receipt` | receipt_dropped | 422 | 57264ms | ❌ | ❌ | ❌ |
| 5 | user_persona | `accepted_with_exports` | — | 200 | 42151ms | ✅ | ✅ | ✅ |
| 6 | strategy_analysis | `accepted_with_exports` | — | 200 | 39056ms | ✅ | ✅ | ✅ |
| 7 | feature_prioritization | `accepted_with_exports` | — | 200 | 25217ms | ✅ | ✅ | ✅ |
| 8 | pricing_strategy | `accepted_with_exports` | — | 200 | 36694ms | ✅ | ✅ | ✅ |
| 9 | documentation | `api_timeout` | execute_route_timeout | — | 93201ms | ❌ | ❌ | ❌ |
| 10 | email_template | `accepted_with_exports` | — | 200 | 16046ms | ✅ | ✅ | ✅ |
| 11 | risk_assessment | `accepted_with_exports` | — | 200 | 44212ms | ✅ | ✅ | ✅ |
| 12 | strategy_analysis | `api_timeout` | execute_route_timeout | — | 95677ms | ❌ | ❌ | ❌ |
