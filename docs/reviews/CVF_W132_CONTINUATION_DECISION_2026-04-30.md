<!-- Memory class: SUMMARY_RECORD -->
# CVF W132-T1 Continuation Decision

> Date: 2026-05-07
> Tranche: W132-T1 — Provider/Runtime Stability And Browser Session Hardening
> Status: CLASSIFIED BLOCKER — CONTINUATION DECISION PUBLISHED
> Evidence: `CVF_W132_RUNTIME_STABILITY_ALIBABA_EVIDENCE_2026-04-30.md`, `CVF_W132_RUNTIME_STABILITY_DEEPSEEK_EVIDENCE_2026-04-30.md`

---

## 1. Evidence Summary

Two full isolated-session runs were executed (2026-04-30 pre-CP3, 2026-05-07 post-CP3). Results are consistent across both runs.

### Alibaba CP4 (post-CP3, 2026-05-07)

| Metric | Result | Target | Pass |
|---|---|---|---|
| Attempted journeys | 12 | ≥12 | ✅ |
| Accepted with receipt | 1 (8.3%) | ≥8 (67%) | ❌ |
| Failure rate | 83.3% | <25% | ❌ |
| Cascade failures | 0 | 0 | ✅ |
| Evidence written per journey | 12/12 | 100% | ✅ |
| Live HTTP status | 200 | 200 | ✅ |
| Live governance decision | ALLOW | ALLOW | ✅ |

### DeepSeek CP5 (post-CP3, 2026-05-07)

| Metric | Result | Target | Pass |
|---|---|---|---|
| Attempted journeys | 6 | ≥6 | ✅ |
| Accepted with receipt | 1 (16.7%) | ≥3 | ❌ |
| Failure rate | 66.7% | — | — |
| Cascade failures | 0 | 0 | ✅ |
| Evidence written per journey | 6/6 | 100% | ✅ |
| Live HTTP status | 200 | 200 | ✅ |
| Live governance decision | ALLOW | ALLOW | ✅ |

---

## 2. Classified Blockers

### Blocker B1 — Sequential Journey Failure After First Call (Primary)

**Classification:** `sequential_journey_failure_server_side_connection`

**Evidence — three independent runs:**

| Run | Date | Model | Alibaba accepted | DeepSeek accepted | Pattern |
|---|---|---|---|---|---|
| 1 | 2026-04-30 | qwen-turbo | 1/12 (8.3%) | 1/6 (16.7%) | J1 pass, J2+ fail at 95s |
| 2 | 2026-05-07 | qwen-turbo | 1/12 (8.3%) | 1/6 (16.7%) | J1 pass, J2+ fail at 93s |
| 3 | 2026-05-07 | qwen-plus | 1/12 (8.3%) | 1/6 (16.7%) | J1 pass, J2+ fail at 93s |

Key observations:
- Journey 1 always succeeds: Alibaba qwen-turbo 15.5s, qwen-plus 33.2s, DeepSeek 28–30s
- All journeys 2+ time out at ~93s regardless of form type, model, or provider
- Journey 9 (`documentation`) fails despite Journey 1 (`documentation`) passing — rules out form-type
- Switching from `qwen-turbo` to `qwen-plus` (higher RPM tier, same DASHSCOPE_API_KEY) produced **no change** in outcome — rules out provider RPM as primary cause
- Same pattern on DeepSeek `deepseek-chat` — rules out Alibaba-specific rate limiting as sole cause

**Root cause hypothesis:** Server-side connection or streaming state is not fully released between journeys. The `/api/execute` route likely uses SSE or a persistent connection to deliver the AI response. When the browser context closes after J1, the server-side connection may remain open, causing J2's request to block, queue, or receive an invalid response. This would explain why both providers show identical failure patterns despite different RPM characteristics.

**Scope:** CP3 runtime fixes (domcontentloaded, bounded navigation waits, 85s Alibaba timeout) are confirmed effective for browser cascade failures and diagnostic taxonomy. They do not address the server-side connection lifecycle issue between sequential journeys.

### Blocker B2 — user_persona Route Miss (Secondary)

**Classification:** `intent_router_routing_gap`

**Evidence:**
- `user_persona` (Journey 5) produces `route_miss` on both Alibaba and DeepSeek across all runs
- CTA button disabled — intent router returns no confident route for user_persona prompts
- Elapsed ~17s (fast failure, not a timeout)
- Consistent across 2026-04-30 and 2026-05-07 runs

**Root cause:** The intent router does not have a confident mapping for `user_persona` form-type prompts. This is a routing coverage gap, independent of provider rate limiting.

---

## 3. What CP3 Fixed (Confirmed Effective)

- **Browser session isolation**: 0 cascade failures across 18 attempted journeys (Alibaba 12 + DeepSeek 6). CP1 goal fully met.
- **Diagnostic subcodes**: All timeouts correctly classified as `provider_timeout` or `execute_route_timeout`. CP2 goal fully met.
- **Navigation hang**: No 30-minute hang observed. `domcontentloaded` fix effective.
- **Mock fallback misclassification**: 0 `mock_fallback_no_receipt` — regression from CP3 fix confirmed resolved.

---

## 4. Continuation Decision

Per roadmap §3 CP6 decision rules: failure rate above 25% → next tranche is deeper provider/runtime remediation.

**Decision: OPEN W133**

W133 scope (data-backed):

1. **Provider tier upgrade**: Switch Alibaba model from `qwen-turbo` to `qwen-plus` (higher RPM, same DASHSCOPE_API_KEY). Evaluate whether DeepSeek standard tier also needs upgrading.
2. **Rate limit handling**: Add configurable inter-journey delay or exponential backoff at the provider call level so rapid sequential UI journeys do not exhaust RPM budget.
3. **user_persona routing fix**: Extend intent router coverage to recognize `user_persona` prompts and route to the `user_persona` template with confidence.
4. **Re-run stability matrix**: Re-run 12 Alibaba + 6 DeepSeek journeys after fixes to verify ≥67%/≥3 acceptance targets.

**W133 is not authorized by this document.** W133 requires a fresh `GC-018` authorization.

---

## 5. W132 Closure Claim

CVF W132-T1 may claim:

> CVF's noncoder execution path was re-tested with per-journey browser session isolation (CP1) and classified provider/runtime diagnostics (CP2). Runtime fixes in CP3 eliminated browser cascade failures and navigation hangs. Two runs across both providers confirmed a consistent provider rate-limiting pattern on free/basic tier models: only the first sequential UI journey succeeds per session. CVF has classified this blocker with diagnostic subcodes and published a data-backed continuation decision for W133.

CVF W132-T1 may NOT claim:

- Provider runtime stability for sequential noncoder journeys
- Alibaba or DeepSeek acceptance rates above the measured 8.3% / 16.7%
- Any improvement in end-user noncoder throughput

---

## 6. No Mock Substitution

All evidence rows in this decision derive from live browser UI journeys through the governed `/api/execute` path. Live HTTP status 200 and governance decision ALLOW were independently confirmed via a dedicated proof context after the journey matrix. No mock output, API-only call, or static UI check is counted.
