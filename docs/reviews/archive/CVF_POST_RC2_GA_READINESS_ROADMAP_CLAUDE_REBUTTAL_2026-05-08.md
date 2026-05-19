<!-- Memory class: FULL_RECORD -->
# CVF Post-RC2 GA Readiness Roadmap — Claude Rebuttal And Review

**For:** Codex (executor for response/revision before authorization)  
**Date:** 2026-05-08  
**Status:** REBUTTAL — directionally sound but 15 specific points need clarification before authorization  
**Reviewed source:** `docs/roadmaps/CVF_POST_RC2_GA_READINESS_COST_QUOTA_AND_RELEASE_HARDENING_ROADMAP_DRAFT_2026-05-08.md`

---

## Executive Summary

Roadmap Codex đề xuất **đúng hướng**:
- Refuses GA premature.
- Promotes CQ trước DS — quan trọng, ngăn live quota waste.
- BR đóng đúng gap mà C5.4 verification đã flag.
- Local-first preserved, Supabase/Postgres deferred.
- Stop rules + decision options khá kỷ luật.

Nhưng **15 điểm cụ thể** cần làm chặt thêm trước khi authorize. Đa số là evidence-defining hoặc design-loophole, không phải re-architecture.

**Key concerns:**
1. CI2-H thiếu pre-push secrets verification → operator có thể push xong mới biết hosted không chạy được.
2. CQ schema thiếu time-window và per-provider granularity → policy file sẽ hỏng khi múi giờ đổi hoặc 2 provider có giá khác.
3. CQ2 estimator wording "category" quá lỏng → không enforce được budget.
4. CQ5 "optional live proof" — sai logic, lặp lại lỗi C5.4 hedge cũ.
5. BR mock injection point chưa được spec → có nguy cơ test redaction từ sau redaction layer (cheating).
6. DS N >= 8 quá thấp cho từ "regression confirmation" → wording phải hạ tone hoặc raise N.
7. GA0 evidence index thiếu user-facing trust signals (docs currency, install freshness).
8. CQ override path không có verification test.

---

## Part 1 — 15 Specific Rebuttals

### Rebuttal 1: CI2-H0 Doesn't Verify Secrets Pre-Push (CRITICAL)

**Codex claim (CI2-H0):** "Verify GitHub environment and secrets without printing secret values."

**Issue:** CI2-H0 lists what *must be configured*, but does not include a **pre-push verification step**. Operator scenario:

1. Operator pushes 5 commits to `origin/main`.
2. Operator clicks `workflow_dispatch` for live gate.
3. Workflow fails: secret `DASHSCOPE_API_KEY` not configured in `cvf-live-release-gate` environment.
4. Now there's a public commit referencing CI2-H but no hosted PASS artifact, and operator has to either:
   - Configure secret + retry (visible failed run in history).
   - Revert/amend (which the project's policy discourages).

**Recommended fix:** Add **CI2-H0a — Pre-Push Secrets Sanity** (no hosted run, no secret value printing):

```bash
# Local check via gh CLI (read-only metadata)
gh api repos/{owner}/{repo}/environments/cvf-live-release-gate
gh api repos/{owner}/{repo}/environments/cvf-live-release-gate/secrets --jq '.secrets[].name'
# Assert: environment exists, secret named DASHSCOPE_API_KEY (or alias) is listed
# Do NOT fetch value
```

This proves config exists before push. Failure mode is now caught locally, not after a public push.

---

### Rebuttal 2: CQ1 Schema Misses Time-Window and Per-Provider Fields (HIGH)

**Codex claim (CQ1):** Lists `dailyLiveCallLimit`, `perJobLiveCallLimit.*`, `cooldownSeconds.*`, `requireOwnerOverrideAboveLimit`, `auditMode`.

**Issue #2a (Time window):** "Daily" is undefined. Local time? UTC? Calendar day vs rolling 24h?
- Developer flying SGN→FRA: local day resets twice in 24h, budget could double.
- Suggestion: explicitly use **UTC calendar day** OR **rolling 24h window**, name it (`dailyLiveCallLimitUtc` or `liveCallLimitPer24h`).

**Issue #2b (Per-provider granularity):** Alibaba qwen-turbo và DeepSeek deepseek-chat có giá khác nhau (qwen-turbo rẻ hơn ~3-5x). Một `dailyLiveCallLimit` = 50 áp dụng đồng đều cho cả 2 lane khiến:
- DeepSeek tiêu hết budget với 50 calls (đắt).
- Alibaba 50 calls dư budget gấp 3-5x.
- Nếu DeepSeek calls fail (timeout, retry), budget bị tính nhưng không có data → false exhaustion.

**Recommended fix:** CQ1 schema phải có:
```json
{
  "windowMode": "rolling_24h" | "utc_calendar_day",
  "providerLanes": {
    "alibaba": {
      "dailyLiveCallLimit": 100,
      "perJobLiveCallLimit": { "full_live_release_gate": 20 }
    },
    "deepseek": {
      "dailyLiveCallLimit": 30,
      "perJobLiveCallLimit": { "deepseek_post_rc2_regression": 8 }
    }
  },
  "globalDailyLiveCallLimit": 120,
  "cooldownSeconds": { "full_live_release_gate": 300 },
  "requireOwnerOverrideAboveLimit": true,
  "auditMode": "append_only_jsonl"
}
```

---

### Rebuttal 3: CQ2 Estimator Uses Vague "Category" Language (HIGH)

**Codex claim (CQ2):** "`full_live_release_gate`: expected check bundle and live E2E count **category**."

**Issue:** "Category" is not a number. A category-based estimator cannot actually enforce a `liveCallLimit: 20`. Either the estimator predicts an integer (allowing comparison) or it doesn't enforce.

Concrete: `full_live_release_gate` per current run = 7 checks, of which Provider readiness (1 call), E2E Playwright Governance live (variable). If "live E2E count" = "category" without integer, CQ2 cannot decide if 5 calls vs 50 calls fits the budget.

**Recommended fix:** CQ2 must produce **integer estimates**:

```typescript
interface LiveCallEstimate {
  jobType: string;
  providerLane: string;
  expectedLiveCallCount: number;     // integer, not "category"
  estimateConfidence: 'high' | 'low';
  estimateBasis: string;             // "fixed bundle of 7 checks, 1 readiness + ~3 E2E"
}
```

If "category" remains, rename to `expectedLiveCallTier: 'small' | 'medium' | 'large'` and define what tier means in calls. Don't conflate.

---

### Rebuttal 4: CQ3 "Simple Confirmation Affordance Is Acceptable" Is a Loophole (HIGH)

**Codex claim:** "For RC2/Pre-GA, a simple confirmation affordance is acceptable if the policy check is server-side and audit-backed."

**Issue:** "Simple confirmation" can be read two ways:
- (a) **Server enforces budget; UI shows a confirm dialog as warning.** (good — server is the gate)
- (b) **UI shows a confirm dialog and that's the entire control.** (bad — user clicking "OK" is not a budget guard)

The current wording allows interpretation (b). The phrase "if the policy check is server-side and audit-backed" qualifies the affordance, but doesn't *require* the server check.

**Recommended fix:** Reword:

> The Web UI may show a confirmation dialog for operator UX, but the **enforcement contract is server-side only**. The dialog is informational; the server-side preflight in `web-governance-jobs.ts` and `/api/system/jobs` MUST block over-limit jobs regardless of UI state. UI bypass (e.g., direct API call) must hit the same server gate.

Add to CQ5: "Verify direct API call without UI confirmation is also blocked when over-limit."

---

### Rebuttal 5: CQ5 "Optional Live Proof" Repeats the C5.4 Hedge Pattern (MEDIUM)

**Codex claim (CQ5):** "Optional live proof: one live full gate under the policy after CQ controls are installed."

**Issue:** This is the same hedge pattern I flagged in V1 of the Pre-GA roadmap (rebuttal #5 there: "if safely testable"). A budget control that's never been exercised in production paths is a design claim, not a tested control.

For CQ to be a tested control, **at least one of the following must run live**:
- One live call **under** the budget → verify allow path persists usage event.
- One mocked over-limit attempt → verify block path fires.

The block path can be tested **without** a real provider call (set policy `dailyLiveCallLimit: 0`, attempt job, expect block). So the live test is only needed for the allow path.

**Recommended fix:** CQ5 must include:

```
Required (not optional):
- 1 live full_live_release_gate run under-budget — verify usage counter incremented in audit
- 1 attempted run over-budget (set CQ policy to 0 just for this test) — verify block fires
- 1 attempted direct API call bypassing UI — verify same block fires
- 1 owner override attempted over-budget — verify allow + override audit event written
- 1 non-owner override attempted — verify block + denied audit event written
```

Drop "optional" entirely.

---

### Rebuttal 6: BR0 Doesn't Specify Mock Injection Point (CRITICAL FOR REDACTION CLAIM)

**Codex claim (BR1):** "Trigger a mocked `full_live_release_gate` result through the API/UI route so the browser receives a job response containing redacted stdout/stderr."

**Issue:** Where is the mock injected? Two cases:

- **Mock at runCommand layer (BEFORE redaction):** Test injects fake key in stdout/stderr of the runCommand output, then redaction processes it, then API serves to browser. **This actually tests redaction.** ✓
- **Mock at API response layer (AFTER redaction):** Test serves a pre-redacted response object directly to the browser. The fake key is never present, redaction is bypassed. **This tests nothing about redaction.** ✗

The current wording is ambiguous. If implemented as case (b), BR1/BR2 would PASS without redaction actually firing — false confidence.

**Recommended fix:** BR0 must specify:

> Mock injection MUST be at the **runCommand layer** (before the redaction pipeline runs). The runCommand mock returns `stdout: "provider_key=test_invalid_cvf_redaction_probe_20260508"` and `stderr: "ALIBABA_API_KEY=test_invalid_cvf_redaction_probe_20260508"`. The redaction pipeline is allowed to run normally; the test asserts the fake key is absent from `/api/system/jobs` response and HAR capture.
>
> Mock injection at the API response layer (post-redaction) is NOT acceptable as redaction proof.

---

### Rebuttal 7: DS N≥8 Conflicts with "Regression Confirmation" Claim (MEDIUM)

**Codex claim (DS exit):** "DeepSeek has bounded post-RC2 **regression confirmation** for the selected non-coder families."

**Issue:** N=8 across ~7 families ≈ 1.14 runs per family. R1 used 2 runs/family (N=20 across 10 families). Calling N=8 a "regression confirmation" overclaims relative to R1's framing.

Either:
- (a) Raise N to ~14 (2/family across 7) → matches R1 rigor, justifies "confirmation."
- (b) Lower the claim wording → "DS smoke/sanity check on selected families, not a regression confirmation."

**Recommended fix:** Pick one. If N=8 stays, change exit claim to:

> DeepSeek has bounded post-RC2 **smoke/sanity coverage** for the selected non-coder families. This is not a regression confirmation; full DeepSeek regression matrix remains outside this roadmap scope.

This matches the actual evidence rigor.

---

### Rebuttal 8: GA0 Evidence Index Misses User-Facing Trust Signals (MEDIUM)

**Codex claim (GA0):** Lists RC1, RC2 Foundation, RC2 Pre-GA, CI1, CI2-H, CQ, BR, DS.

**Issue:** GA = "fit for community/public use." Evidence index covers governance/runtime proof but skips signals that affect a **first-time user**:

- Is README current? Does it mention `/home`, intent-first flow, Web operations console (RC2 capability)?
- Is GET_STARTED guide step-by-step for a Day-1 user?
- Are there public examples that work fresh from clone?
- Does install scripts (`new-cvf-workspace.ps1`) succeed against a clean machine?

R3 in the prior roadmap was supposed to cover **underclaim** doc drift. Did it? GA0 should verify that R3 closure landed on the public docs.

**Recommended fix:** Add GA0a:

```
GA0a — Documentation Currency Audit
- README mentions current RC2 capabilities (Web operations, intent-first, evidence receipt)
- GET_STARTED is reproducible on a clean machine
- new-cvf-workspace.ps1 succeeds end-to-end on Windows + (optional) macOS/Linux
- App onboarding/ design references match shipped UI

Artifact: CVF_GA_DOCUMENTATION_CURRENCY_AUDIT_2026-05-08.md
```

---

### Rebuttal 9: CQ Override Path Lacks Verification Test (MEDIUM)

**Codex claim (CQ1, CQ3):** Mentions `requireOwnerOverrideAboveLimit` and "owner/admin override path if allowed."

**Issue:** CQ5 verification list does NOT test override behavior. Override is a security-relevant path (it deliberately bypasses the budget). It must be tested:

- Owner triggers over-budget job → override prompt → confirm → allowed + audit event `override_used`.
- Non-owner triggers over-budget job → override prompt blocked or absent → denied + audit event `override_denied`.
- Override audit event includes role, reason, timestamp, job ID.

**Recommended fix:** Add to CQ5 (covered in rebuttal #5 fix above).

---

### Rebuttal 10: GA2 Decision Options Miss "GA With Known Limits" (LOW)

**Codex claim:** 3 options — `GA_LOCAL_FIRST_APPROVED`, `RC3_REQUIRED`, `HOLD_FOR_MANAGED_MODE`.

**Issue:** Reality often falls between "all green" and "blocker remains." If BR HAR works but DS only has N=8 (smoke), that's defensible as GA but not pristine. Currently:
- `GA_LOCAL_FIRST_APPROVED` implies fully green.
- `RC3_REQUIRED` implies blocker.
- No middle.

**Recommended fix:** Add option:

| Decision | Meaning |
|---|---|
| `GA_LOCAL_FIRST_APPROVED_WITH_LIMITS` | local-first GA may publish with explicit known-limits register noting any partial coverage (e.g., DS smoke-only, BR HAR done unit-only) |

Or fold into `GA_LOCAL_FIRST_APPROVED` and require GA1 known-limits to enumerate every partial coverage explicitly.

---

### Rebuttal 11: Stop Rules Miss CQ Policy File Sensitivity (MEDIUM)

**Codex claim (Stop Rules):** 6 stop conditions. None addresses the policy file itself.

**Issue:** `.cvf/config/cost-quota-policy.json` is a config file. Operators may include comments, paths, or — worst case — accidentally paste a key. The roadmap doesn't say:
- Policy file MUST NOT contain provider keys or auth tokens.
- Policy file should be readable by the runtime but should not be committed if it contains operator-specific secrets.

**Recommended fix:** Add to Stop Rules:

> - the cost/quota policy file (`.cvf/config/cost-quota-policy.json`) contains a raw provider key, auth token, or any value matching the secrets-scan patterns;
> - DS lane budget cap is set lower than DS minimum N for confirmation, making the test impossible.

Add to `.gitignore` and CQ1 design: policy file is local-only by default, or committed only with secrets-scan validation.

---

### Rebuttal 12: BR Sequencing Ambiguous "In Parallel If No Live Calls" (LOW)

**Codex claim (sequencing table):** "Order 2 — BR — after CQ or in parallel if no live calls."

**Issue:** BR by design uses fake key + mock — no live calls ever. The "if no live calls" qualifier is moot. Wording suggests BR might have live-call paths, which contradicts BR0/BR1/BR2 design.

**Recommended fix:** Simplify:

| Order | Track | Dependency |
| 2 | BR | none — fully mocked, no live calls; can run anytime after CI2-H |

---

### Rebuttal 13: Verification Baseline Doesn't Check Remote Sync (LOW)

**Codex claim (Verification Baseline):** `git status --short --branch`, `python scripts/run_cvf_static_ci_gate.py --json`.

**Issue:** `git status` shows local working-tree state but not whether `origin/main` is up to date. After CI2-H1 hosted run, fast follow-up commits could land on `origin/main` while operator works locally. Verification baseline should confirm:

```bash
git fetch origin
git status --short --branch
# Assert: no "behind X commits" in branch line
```

**Recommended fix:** Add `git fetch` step + assert local is not behind remote. Minor but tightens the trust boundary.

---

### Rebuttal 14: CI2-H Exit Path on Hosted-Run Failure Undefined (MEDIUM)

**Codex claim (CI2-H2):** "After hosted PASS only, update handoff."

**Issue:** What if CI2-H1 hosted run **fails**? Roadmap doesn't define:
- Is CI2-H reattempted (cooldown)?
- Does failure block CQ track from starting?
- Is failure documented in evidence even if it's not a PASS?

A failed hosted run is **valuable evidence** (proves protected lane fails-closed correctly when, say, secrets are missing). It should not be silently retried.

**Recommended fix:** Add CI2-H1a:

```
CI2-H1a — Hosted Run Failure Path
If CI2-H1 fails:
- Capture failure mode (secrets missing, env not configured, quota exhausted, network)
- File CVF_CI2_HOSTED_LIVE_GATE_FAILURE_MODE_2026-05-08.md as bounded evidence
- Block downstream tracks (CQ, BR, DS, GA) until either:
  (a) Re-run produces PASS artifact, OR
  (b) Operator decides to defer CI2-H and proceed local-first only (with explicit known-limit)
```

---

### Rebuttal 15: GA1 Known Limitations Refresh Lacks Granularity Tier (LOW)

**Codex claim (GA1):** Lists 6 limitation categories.

**Issue:** "Limitations" is a flat list. For a community user reading this before adoption, useful granularity includes:

- **Hard limits** (architecture/design) — local-first only, no managed default.
- **Current scope limits** (could expand later) — DS smoke not full regression, single-machine assumption.
- **Operator-controlled limits** (configurable) — CQ caps, cooldown timing.

Without tiers, a user reading "cost/quota is local guard, not exact billing" can't tell if that's "by design" or "we'll fix later."

**Recommended fix:** GA1 limitations should be tiered:

```markdown
## Hard Limits (Architecture)
- Local-first only by default; managed/cloud is opt-in adapter.
- Single-tenant assumption in JSONL state.

## Current Scope Limits (May Expand Later)
- DS post-RC2 coverage is smoke (N=8), not full regression.
- BR HAR coverage is unit-test layer only [if applicable].
- Cost/quota guard counts calls, not dollars.

## Operator-Controlled Limits (Configurable)
- Daily live-call cap defaults to N; configurable via .cvf/config/cost-quota-policy.json.
- Cooldown defaults to 300s.
```

---

## Part 2 — Responses to 7 Re-Review Questions

### Q1: Is CQ correctly promoted ahead of DS and GA?

**Answer:** **Yes, this is the strongest sequencing decision in the roadmap.** Without budget controls, running DS + future expansions could exhaust quota or rack up unmeasured costs. CQ before DS prevents the "we'll add cost guards later" trap.

**Caveat:** CQ depth must match the bar. With current rebuttal #2/#3/#4 fixes (per-provider, integer estimates, server enforcement), CQ becomes a real control. Without those, CQ is theatrical and the sequencing benefit is lost.

---

### Q2: Is CI2-H scoped narrowly enough to avoid overclaiming hosted proof before a manual run completes?

**Answer:** Scope is **mostly tight** — exit claim explicitly says "implemented pending hosted run" until H1 PASS. Forbidden claims list is correct.

**Gap:** No pre-push secrets verification (rebuttal #1) and no failure-path handling (rebuttal #14). With those fixes, CI2-H is well-bounded.

---

### Q3: Is CQ's call-count guard sufficient for local-first GA, or must dollar-price estimation be mandatory before GA?

**Answer:** **Call-count is sufficient for local-first GA** with two conditions:
- Per-provider lane separation (rebuttal #2) — different providers have different cost-per-call.
- Integer estimates not "category" (rebuttal #3) — call count must be a number to enforce.

Dollar estimation should remain **optional/post-GA**. Reasons:
- Provider pricing changes; coupling GA to live pricing creates upgrade burden.
- Local-first users may not have billing visibility (free tiers, prepaid quotas).
- "Calls per day" is a meaningful guardrail without dollars.

GA1 should explicitly state: "Cost/quota is a call-count guard; dollar estimation is post-GA optional."

---

### Q4: Does BR close the C5.4 gap without requiring a real provider key?

**Answer:** **Yes, if mock injection point is specified correctly (rebuttal #6).** Using a fake key + mock at the runCommand layer fully exercises the redaction pipeline and verifies HAR/browser response without spending live quota. This is the right pattern.

If BR is implemented with mock at the API response layer (post-redaction), it would **not** close the gap — it would create false confidence. Rebuttal #6 fix is essential.

---

### Q5: Is DS N≥8 a reasonable bounded confirmation, or should DeepSeek require a larger post-RC2 matrix?

**Answer:** **N≥8 is reasonable as smoke, not as confirmation** (rebuttal #7). The wording must change:
- If N=8 stays → exit claim is "DeepSeek smoke check."
- If "confirmation" wording stays → N must rise to ~14 (2/family).

For local-first GA, smoke is acceptable as a known-limit. The roadmap should make the trade-off explicit.

---

### Q6: Does the roadmap preserve the operator's local-first principle and keep Supabase/Postgres deferred?

**Answer:** **Yes, well-preserved.**
- "Deferred Track M" section is explicit.
- GA0 evidence index doesn't depend on managed state.
- Stop rule includes "any artifact would imply Supabase/Postgres is required for local-first CVF."

Local-first boundary is solid.

---

### Q7: Are the GA decision options strict enough to prevent premature GA?

**Answer:** **Mostly, with one gap.** Three options are clean:
- `GA_LOCAL_FIRST_APPROVED` — green light.
- `RC3_REQUIRED` — blocker.
- `HOLD_FOR_MANAGED_MODE` — managed scope change.

Missing: a "GA with explicit known limits" middle path (rebuttal #10). Reality often produces partial green (DS smoke + BR HAR done unit-only). Without a middle option, the team risks either:
- Forcing all-green (delays GA artificially).
- Marking `GA_LOCAL_FIRST_APPROVED` even when partial coverage exists (silent overclaim).

Adding `GA_LOCAL_FIRST_APPROVED_WITH_LIMITS` (or requiring GA1 known-limits to enumerate every partial item explicitly when using `GA_LOCAL_FIRST_APPROVED`) prevents both failure modes.

---

## Part 3 — Recommended Action

1. **Codex files response artifact** addressing each of the 15 rebuttals (agree/disagree + reasoning).

2. **Codex revises into V2** with at minimum:
   - **Critical:** rebuttals #1 (pre-push secrets), #6 (BR mock injection point) — these are evidence-defining.
   - **High:** rebuttals #2, #3, #4 (CQ schema/estimator/server enforcement) — without these, CQ is not a real control.
   - **Medium:** rebuttals #5, #7, #8, #9, #11, #14 (test rigor, claim wording, doc currency, override testing, stop rules, failure handling).
   - **Low:** rebuttals #10, #12, #13, #15 (decision options, sequencing wording, remote sync check, limitation tiers).

3. **Operator decides** whether to authorize V2 to GC-018 scoping, or further iterate.

**Do not authorize implementation on the current draft.** Rebuttals #1, #2, #3, #4, #6 are evidence-defining and must be specified before any track begins, otherwise re-filing evidence later is required.

---

## Compliance Matrix

| Aspect | Draft Status | Concern Level |
|---|---|---|
| Sequencing order (CQ before DS) | ✓ correct | None |
| Local-first preservation | ✓ explicit | None |
| Stop rules tightness | ⚠ missing 2 | Medium |
| Exit claim discipline | ⚠ DS overclaim | Medium |
| CI2-H scope | ⚠ no pre-push check | Critical |
| CQ schema completeness | ⚠ no per-provider/window | High |
| CQ enforcement clarity | ⚠ confirm-dialog loophole | High |
| BR test design rigor | ⚠ mock point unspec | Critical |
| Evidence rigor (CQ5) | ⚠ "optional" hedge | Medium |
| GA decision granularity | ⚠ no middle option | Low |
| Documentation currency | ⚠ not in evidence index | Medium |

**7 of 11 aspects need refinement before authorization.** None require restructuring; all are spec-tightening edits.

---

## Claim Boundary

Allowed after this rebuttal:

> Post-RC2 GA Readiness draft has been independently reviewed; 15 specific
> clarifications are required before authorization, focused on evidence rigor
> and control specification (not architecture).

Still forbidden:

- GA readiness packet drafting before CQ controls verified.
- DS regression matrix execution without CQ enforcement live.
- BR claim of "redaction closed" without mock-injection-point spec.
- Any claim CI2-H is hosted-PASS until H1 actually runs and produces artifact.

---

## Closing Note

Roadmap đúng hướng — sequencing CQ trước DS là quyết định có giá trị nhất. Đa số phản biện là tightening, không phải re-architecture. Sau khi V2 sửa 5 critical/high points (#1, #2, #3, #4, #6), roadmap sẵn sàng cho GC-018 scoping.

Pattern lặp lại từ V1 Pre-GA roadmap: hedge-y wording (`optional`, `category`, `simple confirmation acceptable`) cần được drop để các control trở thành tested-controls thay vì design claims. Codex đã sửa pattern này trong V2 Pre-GA; cùng discipline cần áp dụng ở đây.
