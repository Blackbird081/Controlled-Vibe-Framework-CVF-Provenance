<!-- Memory class: FULL_RECORD -->
# CVF Post-RC2 GA Readiness Roadmap V2 — Claude Final Authorization

**For:** Operator + Codex implementation authorization  
**Date:** 2026-05-08  
**Status:** AUTHORIZED FOR GC-018 SCOPING — V2 fully addresses 15 rebuttal points  
**Reviewed source:** `docs/roadmaps/CVF_POST_RC2_GA_READINESS_COST_QUOTA_AND_RELEASE_HARDENING_ROADMAP_V2_2026-05-08.md` + Codex response  
**Original rebuttal:** `docs/reviews/CVF_POST_RC2_GA_READINESS_ROADMAP_CLAUDE_REBUTTAL_2026-05-08.md`

---

## Executive Verdict

**V2 roadmap is AUTHORIZED for GC-018 scoping.** All 15 rebuttals are fully addressed with specific, verifiable fixes. Codex went beyond the minimum in two places (BR sequencing, schema versioning). Three micro-notes follow but none block authorization.

---

## Part 1 — Verification of 15 Rebuttal Fixes

### Rebuttal 1 (Critical): Pre-push secrets verification — ✅ FIXED

V2 adds **CI2-H0a — Pre-Run/Pre-Push Secrets Metadata Sanity** with explicit `gh api` commands:
- Lists environment existence
- Lists secret names (no values)
- Forbids fetching/printing/copying secret values
- Failure recorded before any hosted PASS claim

Resolution exact to spec. ✓

---

### Rebuttal 2 (High): CQ schema time-window + per-provider — ✅ FIXED

V2 schema:
```json
{
  "version": 1,
  "windowMode": "rolling_24h",
  "globalDailyLiveCallLimit": 120,
  "providerLanes": {
    "alibaba": { "dailyLiveCallLimit": 100, "perJobLiveCallLimit": {...} },
    "deepseek": { "dailyLiveCallLimit": 30, "perJobLiveCallLimit": {...} }
  },
  "cooldownSeconds": {...},
  "requireOwnerOverrideAboveLimit": true,
  "auditMode": "append_only_jsonl"
}
```

**Bonus improvement:** Codex added `version: 1` (forward-compat) and split DeepSeek caps into `deepseek_post_rc2_smoke` (8) vs `deepseek_post_rc2_confirmation` (14) — matches the DS rebuttal #7 fix at the schema level. ✓+

---

### Rebuttal 3 (High): Integer call estimates — ✅ FIXED

V2 CQ2 replaces "category" with TypeScript interface:
```typescript
interface LiveCallEstimate {
  jobType: string;
  providerLane: 'alibaba' | 'deepseek' | 'mixed';
  expectedLiveCallCount: number;
  estimateConfidence: 'high' | 'low';
  estimateBasis: string;
  policyWindowMode: 'rolling_24h' | 'utc_calendar_day';
}
```

Integer-typed. Bonus: `policyWindowMode` makes the estimate window-aware (defends against window mismatch bugs). ✓+

---

### Rebuttal 4 (High): Server-side enforcement — ✅ FIXED

V2 CQ3 explicit:
> "the enforcement contract is server-side only"  
> "Server-side preflight in the Web job path and `/api/system/jobs` MUST block over-limit jobs regardless of UI state"  
> "A direct API call that bypasses the UI must hit the same server gate"  
> "The UI confirmation is informational. It is not a budget control by itself"

Loophole closed. Forbidden claim added: "UI confirmation alone is a budget guard." ✓

---

### Rebuttal 5 (Medium): CQ5 not optional — ✅ FIXED

V2 CQ5 makes verification mandatory. Smart trade-off:
- **Live call required** only for under-budget allow path (1 run).
- **Mock-acceptable** for over-budget block, direct API bypass, owner override, non-owner denial, cooldown.

Note from V2: "No live provider call is required for over-limit blocking tests. The live call requirement applies only to the under-budget allow path." Saves quota without sacrificing rigor. ✓

---

### Rebuttal 6 (Critical): BR mock injection point — ✅ FIXED

V2 BR0 explicit:
> "mock injection MUST happen at the `runCommand` layer before the redaction pipeline runs"

V2 BR0 forbidden design:
> "mocking the API response after redaction; serving a pre-redacted response body directly to the browser; treating API-response-layer mocks as redaction proof"

Plus exit-claim forbidden: "browser redaction is closed if the fake key is injected after redaction." Defense-in-depth wording. ✓

---

### Rebuttal 7 (Medium): DS wording — ✅ FIXED

V2:
- Track renamed: "DeepSeek Post-RC2 **Smoke/Sanity Coverage**"
- Artifact renamed: `CVF_DEEPSEEK_POST_RC2_SMOKE_COVERAGE_2026-05-08.md`
- N≥8 → smoke/sanity (allowed claim)
- N≥14 → regression confirmation (allowed claim, requires ~2 per family)
- Stop rule: "DS lane budget cap is lower than the selected evidence minimum, making the test impossible"

Properly tiered. Schema (rebuttal #2) reflects both lanes. ✓

---

### Rebuttal 8 (Medium): GA0a documentation currency — ✅ FIXED

V2 adds **GA0a — Documentation Currency Audit**:
- README mentions current RC2 capabilities
- GET_STARTED reproducible for Day-1 user
- `new-cvf-workspace.ps1` succeeds end-to-end on clean Windows
- Optional macOS/Linux verified or explicitly listed as not covered
- Public examples work from fresh clone or marked archived
- App onboarding/design references match shipped UI
- Docs do not imply Supabase/Postgres required for local-first CVF

7 concrete trust signals. ✓

---

### Rebuttal 9 (Medium): CQ override verification — ✅ FIXED

V2 CQ5:
- "owner over-budget override is allowed when policy permits it and records `override_used`"
- "non-owner over-budget override is blocked and records `override_denied`"

CQ4 audit trail: override events include role, reason, timestamp, job ID, provider lane, estimated live call count, no raw provider key. Complete RBAC test pair. ✓

---

### Rebuttal 10 (Low): GA decision middle option — ✅ FIXED

V2 GA2:
| Decision | Meaning |
|---|---|
| `GA_LOCAL_FIRST_APPROVED` | all evidence passes without material known limits |
| `GA_LOCAL_FIRST_APPROVED_WITH_LIMITS` | publish with explicit known-limits register |
| `RC3_REQUIRED` | release-facing blockers remain |
| `HOLD_FOR_MANAGED_MODE` | operator chooses managed as GA requirement |

4 options now span the realistic range. ✓

---

### Rebuttal 11 (Medium): Stop rules expansion — ✅ FIXED

V2 stop rules add:
- CI2 hosted fails without failure-mode artifact
- CI2 hosted fails without explicit operator decision (PASS retry vs deferral)
- direct API over-budget bypass not blocked
- override audit failures
- `.cvf/config/cost-quota-policy.json` contains a raw provider key, auth token, or secret-pattern match
- DS lane budget cap < selected evidence minimum
- BR mock injection occurs after redaction

7 new conditions. Comprehensive. ✓

---

### Rebuttal 12 (Low): BR sequencing — ✅ FIXED + IMPROVED

V2 sequencing:
| Order | Track | Dependency |
|---:|---|---|
| 0 | CI2-H | push complete; metadata sanity before hosted run |
| **1** | **BR** | fully mocked, no live calls; can run after CI2-H scoping |
| 2 | CQ | before new live matrices |
| 3 | DS | CQ controls active |

**Bonus:** Codex promoted BR from Order 2 to Order 1 (before CQ). Reasoning is sound — BR has no dependency on CQ (no live calls), and BR closes the most important C5.4 gap. Earlier BR closure = earlier full redaction proof. ✓+

---

### Rebuttal 13 (Low): Remote sync verification — ✅ FIXED

V2 verification baseline:
```bash
git fetch origin
git status --short --branch
# assert the branch line does not show "behind"
python scripts/run_cvf_static_ci_gate.py --json
```

Exact to spec. ✓

---

### Rebuttal 14 (Medium): CI2-H failure path — ✅ FIXED

V2 adds **CI2-H1a — Hosted Run Failure Path**:
- Classify failure mode (5 categories + unknown)
- Capture run URL, job conclusion, redacted log summary, fail-closed verification
- File bounded failure artifact
- Block downstream tracks until PASS retry OR explicit operator deferral

CI2-H2 has two claim-sync paths (PASS vs deferred known-limit). ✓

---

### Rebuttal 15 (Low): GA1 tiers — ✅ FIXED

V2 GA1 splits into:
- **Hard Limits (Architecture)** — local-first only, single-machine JSONL, multi-tenant not GA
- **Current Scope Limits (May Expand Later)** — DS smoke vs full, call-count vs dollars, BR streams, provider parity
- **Operator-Controlled Limits (Configurable)** — caps, cooldown, override toggles

Clear granularity. A user reading the limitations register can tell what's permanent vs configurable. ✓

---

## Part 2 — Responses to V2's 7 Re-Review Questions

### Q1: Does V2 close critical evidence-definition gaps for CI2-H and BR?

**Yes, fully.**
- CI2-H0a (metadata sanity) + CI2-H1a (failure path) + CI2-H2 (two-mode claim sync) cover the full lifecycle.
- BR0 forbids API-response-layer mocking explicitly; only `runCommand`-layer injection counts.

Both critical rebuttals are evidence-defining and now spec-bound. ✓

---

### Q2: Is CQ now strict enough for local-first GA without dollar-pricing?

**Yes.** With per-provider lane separation, integer estimates, server enforcement, cooldown, override audit, and direct-API-bypass coverage, CQ is a real call-count guard. Dollar pricing remains explicit non-goal:

> "The estimator does not need exact dollar pricing for local-first GA readiness."

Forbidden claim list includes: "exact provider billing reconciliation; cloud FinOps dashboard." Boundary clean. ✓

---

### Q3: Are CQ override and direct API bypass checks sufficient?

**Yes.** CQ5 verification covers all four boundary cases:
1. Owner override allowed → audit `override_used`
2. Non-owner override blocked → audit `override_denied`
3. UI direct API bypass → blocked by server gate
4. Audit fields validated (role, reason, timestamp, no raw key)

Stop rules also cover override audit failure. ✓

---

### Q4: Is DS smoke/sanity wording acceptable for N≥8, with N≥14 for confirmation?

**Yes.** Two separate claim tiers:
- N≥8 PASS → "DeepSeek has bounded post-RC2 smoke/sanity coverage"
- N≥14 PASS with 2/family → "DeepSeek has bounded post-RC2 regression confirmation"

Forbidden after N≥8 only: "DeepSeek regression confirmation, full DeepSeek parity, full 40-form replay, cost/performance equivalence."

Tier discipline is correct. ✓

---

### Q5: Is GA0a documentation currency audit scoped to right public trust signals?

**Yes.** 7 signals cover the realistic Day-1 user journey:
- Read README → does it mention current capabilities?
- Run GET_STARTED → does it work?
- Bootstrap workspace → does it succeed?
- macOS/Linux coverage explicit?
- Examples work fresh?
- Design references match UI?
- Local-first claim consistent?

Scope is tight without being incomplete. ✓

---

### Q6: Is `GA_LOCAL_FIRST_APPROVED_WITH_LIMITS` the right middle decision state?

**Yes.** 4 options span the realistic decision matrix:
- All-green → GA approved
- Partial coverage with explicit limits → GA approved with limits
- Blocker remains → RC3
- Operator wants managed → Hold

Prevents both "force all-green delays GA" and "silent overclaim" failure modes. ✓

---

### Q7: Does V2 preserve local-first while deferring Supabase/Postgres?

**Yes.** Track M is "Deferred Track M — Optional Managed State", not part of this roadmap's implementation. Stop rule explicit:
> "any artifact would imply Supabase/Postgres is required for local-first CVF"

Local-first boundary is solid throughout. ✓

---

## Part 3 — Three Micro-Notes (Non-Blocking)

These are minor clarity improvements; they do not block authorization.

### N1: `requireOwnerOverrideAboveLimit` semantics

**V2 schema field:** `"requireOwnerOverrideAboveLimit": true`

**Question:** When `true`, does it mean:
- (a) Owner override is **required** to proceed over-limit (i.e., over-limit always blocks until owner overrides), or
- (b) Owner override is **the only path** to bypass the limit (non-owners are silently blocked)?

CQ5 covers both interpretations through the test pairs (owner allowed + non-owner denied), so behavior is testable. But the field name allows ambiguity. Implementation might benefit from a clearer name like `overrideMode: "disabled" | "owner_only" | "owner_or_admin"`.

**Suggestion (post-implementation):** Rename or add a comment to schema clarifying the semantics. Not a roadmap blocker.

---

### N2: CI2-H deferred → GA decision constraint should be explicit

**Current V2:** GA0 evidence index includes "CI2 hosted PASS or explicit CI2-H known-limit deferral." GA2 decision options don't explicitly say which decisions are valid when CI2-H is deferred.

**Suggestion:** Add to GA2:
> If CI2-H is deferred (no hosted PASS artifact), the GA decision must be at most `GA_LOCAL_FIRST_APPROVED_WITH_LIMITS`. `GA_LOCAL_FIRST_APPROVED` (all-green) is forbidden when any CI2-H is deferred.

Logical implication is already there (CI2-H deferral = material known limit), but making it explicit prevents borderline-case overclaim. Not a blocker.

---

### N3: BR before CQ — re-run guard if CQ touches redaction pipeline

**Risk:** BR is now Order 1. If CQ implementation modifies the redaction pipeline (CQ4 audit writes redacted data, CQ2 estimator might log redacted previews), BR evidence could become stale.

**Realistic risk:** Low. CQ touches preflight (before runCommand) and audit (after redaction); the redaction pipeline itself shouldn't change.

**Suggestion:** Add note to CQ2/CQ4 spec:
> CQ implementation must not modify the redaction pipeline. If redaction logic is changed by CQ work, BR evidence must be re-run before BR exit-claim remains valid.

Defensive but cheap; prevents silent regression.

---

## Part 4 — Compliance Matrix

| Rebuttal | Severity | V2 Status | Note |
|---|---|---|---|
| 1. Pre-push secrets | Critical | ✅ Fixed | `gh api` metadata-only |
| 2. CQ schema | High | ✅ Fixed+ | Plus `version: 1` and DS smoke/conf split |
| 3. Integer estimates | High | ✅ Fixed+ | Plus `policyWindowMode` field |
| 4. Server enforcement | High | ✅ Fixed | UI = informational only |
| 5. CQ5 not optional | Medium | ✅ Fixed | Live for allow path; mock for blocks |
| 6. BR mock layer | Critical | ✅ Fixed | runCommand-layer required |
| 7. DS wording | Medium | ✅ Fixed | Tiered N≥8 / N≥14 |
| 8. GA doc currency | Medium | ✅ Fixed | 7 trust signals |
| 9. CQ override tests | Medium | ✅ Fixed | Owner allow + non-owner deny |
| 10. GA middle option | Low | ✅ Fixed | 4 decisions |
| 11. Stop rules | Medium | ✅ Fixed | 7 new conditions |
| 12. BR sequencing | Low | ✅ Fixed+ | Promoted to Order 1 |
| 13. Remote sync | Low | ✅ Fixed | `git fetch` + assert not behind |
| 14. CI2-H failure | Medium | ✅ Fixed | CI2-H1a + 2 claim modes |
| 15. GA tiers | Low | ✅ Fixed | Hard/Scope/Operator |

**15/15 fixed.** 4 fixes went beyond minimum (marked +).

---

## Part 5 — Final Verdict

**V2 Roadmap is AUTHORIZED to proceed to GC-018 candidate scoping.**

| Criterion | Status |
|---|---|
| All 15 rebuttals addressed | ✅ 15/15 |
| Evidence-defining specs tightened | ✅ |
| Sequencing (CI2-H → BR → CQ → DS → GA) logical | ✅ |
| Local-first preserved | ✅ |
| Server-side enforcement explicit | ✅ |
| Stop rules comprehensive | ✅ |
| Decision options span reality | ✅ |
| Implementation NOT yet authorized | ✅ (planning only) |

---

## Part 6 — Authorized Next Actions

1. **Operator:** Review V2 + this authorization. If approved, authorize GC-018 candidates per track.

2. **Codex:** Upon operator approval, file GC-018 candidates one at a time:
   - `CVF_GC018_RC2_CI2H_HOSTED_LIVE_GATE_CANDIDATE_2026-05-08.md`
   - `CVF_GC018_RC2_BR_BROWSER_REDACTION_CANDIDATE_2026-05-08.md`
   - `CVF_GC018_RC2_CQ_COST_QUOTA_GUARD_CANDIDATE_2026-05-08.md`
   - `CVF_GC018_RC2_DS_DEEPSEEK_COVERAGE_CANDIDATE_2026-05-08.md`
   - `CVF_GC018_RC2_GA_READINESS_PACKET_CANDIDATE_2026-05-08.md`

3. **Claude:** Stand by for GC-018 candidate review and per-track evidence verification. Evidence rigor bar remains:
   - CI2-H: hosted PASS artifact OR failure-mode artifact + operator deferral
   - BR: runCommand-layer mock injection only
   - CQ: integer estimates, server enforcement, all 5 verification cases incl. live under-budget
   - DS: tiered claim wording (N≥8 = smoke; N≥14 = confirmation)
   - GA: documentation currency audit + tiered known limits

---

## Claim Boundary

Allowed after this authorization:

> CVF Post-RC2 GA Readiness Roadmap V2 is authorized for GC-018 scoping. All
> 15 rebuttal points are addressed; sequencing is risk-ranked CI2-H → BR → CQ
> → DS → GA; local-first is preserved; Supabase/Postgres remains deferred.

Still forbidden:

- GA readiness is approved.
- CI2-H hosted PASS exists (until H1 actually runs).
- BR redaction closure is proven (until BR1/BR2 run).
- CQ guard is implemented or proven.
- DS coverage exists (smoke or confirmation).
- Implementation has begun on any track.
- Supabase is the default CVF persistence.

---

## Closing Note

This is the second successful execution of the rebuttal-driven loop:
- Pre-GA V1 → 9-point rebuttal → V2 → authorization → implementation → verification
- Post-RC2 GA V1 → 15-point rebuttal → V2 → authorization

Codex's pattern of accepting valid critique, going beyond minimum (BR promotion, schema versioning, DS lane split), and asking sharp re-review questions makes the loop fast and honest.

V2 is sound. The 3 micro-notes can be addressed during implementation; they don't block the roadmap.

Ready to move forward to GC-018 scoping. ✓
