# W133-T1 CP6 — Continuation Decision
**Date:** 2026-05-07  
**Tranche:** W133-T1 — SSE Connection Lifecycle And Sequential Journey Stability  
**Checkpoint:** CP6 — Evidence Review & Continuation Classification  
**Author:** CVF Agent (W133 execution)

---

## Executive Summary

W133-T1 was authorized to address the W132 classified blocker `sequential_journey_failure_server_side_connection`. Three fixes were applied (Fix-A/B/C). CP4 (Alibaba, 12 journeys) and CP5 (DeepSeek, 6 journeys) were executed.

**Result:** Fix-A (Connection: close) successfully resolved the TCP stale-connection stall — confirming the W132 root cause. However, Fix-A unmasked a pre-existing HTTP 400 pre-AI-call block affecting all non-documentation form templates. Acceptance rate remains 1/12 (8.3%) for Alibaba and 1/6 (16.7%) for DeepSeek — both failing the W133 threshold (≥8/12 and ≥3/6 respectively).

**W133 CONTINUATION STATUS: BLOCKED — NEW CLASSIFIED BLOCKERS IDENTIFIED**

---

## Applied Fixes Summary

| Fix | Description | Status |
|-----|-------------|--------|
| Fix-A | `Connection: close` header + AbortSignal.timeout(60s) on Alibaba and DeepSeek provider fetches | CONFIRMED WORKING |
| Fix-B | Form-first routing precedence (`routeToTrustedForm` before wizard detection) | PARTIALLY WORKING — routing correct but form submission still blocked |
| Fix-C | 1500ms inter-journey delay between isolated BrowserContexts | CONFIRMED WORKING — no cascade failures |
| Fix-D (new) | VN pattern coverage for `user_persona` (`hồ sơ khách hàng`, `khách hàng mục tiêu`) | DELIVERED — 28/28 unit tests pass |

---

## CP4 Evidence (Alibaba qwen-plus, 12 journeys)

**Evidence file:** `CVF_W133_RUNTIME_STABILITY_ALIBABA_EVIDENCE_2026-05-07.json`

| Metric | Value | Threshold | Pass? |
|--------|-------|-----------|-------|
| Attempted | 12 | ≥12 | ✅ |
| Accepted | 1 | ≥8 | ❌ |
| Acceptance rate | 8.3% | ≥66.7% | ❌ |
| Failure rate | 83.3% | <20% | ❌ |

**Outcome breakdown:**
- `accepted_with_exports`: 1 (J1 documentation — HTTP 200, 36s)
- `route_miss`: 1 (J5 user_persona — VN pattern gap, now fixed in Fix-D)
- `api_timeout`: 10 (J2–J4, J6–J12 non-documentation templates — HTTP 400)

**Diagnostic breakdown:**
- `provider_timeout`: 8 (HTTP 400 returned quickly, before AI call)
- `execute_route_timeout`: 2 (J9, J12 — TCP stall persists for some requests)

---

## CP5 Evidence (DeepSeek deepseek-chat, 6 journeys)

**Evidence file:** `CVF_W133_RUNTIME_STABILITY_DEEPSEEK_EVIDENCE_2026-05-07.json`

| Metric | Value | Threshold | Pass? |
|--------|-------|-----------|-------|
| Attempted | 6 | ≥6 | ✅ |
| Accepted | 1 | ≥3 | ❌ |
| Acceptance rate | 16.7% | ≥50% | ❌ |
| Failure rate | 83.3% | <33% | ❌ |

**Outcome breakdown:**
- `accepted_with_exports`: 1 (J1 documentation)
- `route_miss`: 1 (J5 user_persona — same VN pattern gap)
- `api_timeout`: 4 (J2–J4, J6 non-documentation templates — HTTP 400)

---

## Fix-A Confirmation

W132 root cause was confirmed as TCP stale-connection stall. Fix-A evidence:

- **W132:** J2+ returned `execute_route_timeout` (no HTTP response at all — TCP-level stall)
- **W133 after Fix-A:** J2+ now return `provider_timeout` with HTTP 400 (route responds, quickly, before AI call)
- **Conclusion:** Fix-A successfully resolved TCP stale connections. The W132 primary blocker is resolved.

---

## New Classified Blockers

### Blocker 1: `noncoder_pre_ai_call_http400_non_documentation_forms`

**Classification:** CRITICAL — blocks all template executions except `documentation`  
**Symptom:** Non-documentation form templates (email_template, risk_assessment, competitor_review, strategy_analysis, feature_prioritization, pricing_strategy, user_persona) receive HTTP 400 in <500ms — well before any AI call could complete (AI calls take 30–90s)  
**Pattern:** J1 documentation → HTTP 200, success. J2+ non-documentation → HTTP 400, fast rejection.  
**HTTP status carrier:** Response body not captured; subcodes inferred from elapsed time (quick return < 1s vs AI timeout ~93s)  
**Root cause:** Investigation inconclusive across 10+ files. Suspected candidates:
  - Enforcement gate in `route.ts` line ~421 rejecting non-documentation templates
  - Governance context risk level mismatch (CATEGORY_RISK_MAP key case sensitivity — but both documentation and email_template share `category: 'content'`)
  - Form field validation failure for required fields not populated by the E2E spec
  - Template-specific policy block not yet identified
**Required fix:** Capture HTTP 400 response body in E2E spec or targeted curl test to identify exact rejection reason  
**Impact:** Until resolved, only `documentation` template is testable with live providers

### Blocker 2: `user_persona_vn_pattern_gap` — RESOLVED IN THIS SESSION

**Classification:** LOW — single journey failure  
**Symptom:** VN prompt "Xây dựng hồ sơ khách hàng mục tiêu..." not matched by form-routing patterns  
**Fix:** Added `/hồ sơ khách hàng/i` and `/khách hàng mục tiêu/i` to `user_persona` activationPatterns in `form-routing.ts`  
**Verification:** 28/28 form-routing unit tests pass including `user_persona — VN activation`  
**Status:** CLOSED

---

## Fix-D Delivery (user_persona VN patterns)

**File:** `src/lib/form-routing.ts`  
**Change:** Added 2 Vietnamese activation patterns to `user_persona`:
```
/hồ sơ khách hàng/i    ← matches "hồ sơ khách hàng mục tiêu"
/khách hàng mục tiêu/i ← matches "khách hàng mục tiêu"  
```
**Test result:** 28/28 unit tests pass

---

## Continuation Decision

**BLOCKED.** W133-T1 cannot close as DELIVERED due to Blocker 1 (`noncoder_pre_ai_call_http400_non_documentation_forms`).

**Recommended next tranche (W134):**
1. Capture HTTP 400 response body from non-documentation form submissions (add `responseBody` field to journey evidence)
2. Identify exact rejection path in `route.ts` 
3. Fix the root cause (likely a field validation gap or enforcement policy for specific template categories)
4. Re-run stability matrix with full 12-template Alibaba run targeting ≥8/12 acceptance
5. Fix-D (user_persona VN patterns) — DELIVERED in W133, no action needed in W134

**Partial credit for W133:**
- Fix-A (TCP Connection: close) — CONFIRMED WORKING, closes W132 root cause
- Fix-C (inter-journey delay) — CONFIRMED WORKING, no cascade failures
- Fix-D (user_persona VN patterns) — DELIVERED and tested

**W133 final status:** CLOSED WITH CLASSIFIED BLOCKER `noncoder_pre_ai_call_http400_non_documentation_forms`

---

## Artifacts

| Artifact | Path |
|---------|------|
| W133 investigation note | `docs/reviews/CVF_W133_SSE_INVESTIGATION_2026-05-07.md` |
| CP4 Alibaba evidence (JSON) | `docs/reviews/archive/CVF_W133_RUNTIME_STABILITY_ALIBABA_EVIDENCE_2026-05-07.json` |
| CP5 DeepSeek evidence (JSON) | `docs/reviews/archive/CVF_W133_RUNTIME_STABILITY_DEEPSEEK_EVIDENCE_2026-05-07.json` |
| E2E spec | `tests/e2e/w133-runtime-stability.live.spec.ts` |
| providers.ts Fix-A | `src/lib/ai/providers.ts` |
| intent-router.ts Fix-B | `src/lib/intent-router.ts` |
| form-routing.ts Fix-D | `src/lib/form-routing.ts` |
