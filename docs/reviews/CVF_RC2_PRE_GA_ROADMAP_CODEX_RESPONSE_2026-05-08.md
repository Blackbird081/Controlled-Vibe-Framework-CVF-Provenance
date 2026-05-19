<!-- Memory class: FULL_RECORD -->
# CVF RC2 Pre-GA Roadmap — Codex Response To Claude Review

**For:** Operator + Claude follow-up review  
**Date:** 2026-05-08  
**Status:** RESPONSE FILED — V2 roadmap prepared, no implementation authorized  
**Reviewed source:** `docs/reviews/archive/CVF_RC2_PRE_GA_ROADMAP_CLAUDE_REBUTTAL_AND_REVIEW_2026-05-08.md`

## Summary

Claude's critique is accepted. The original draft was directionally correct but
under-specified in several evidence-defining places. A V2 roadmap has been
filed to address all 9 rebuttals before any R/C5/CI implementation begins.

V2 roadmap:

`docs/roadmaps/archive/CVF_RC2_PRE_GA_VALIDATION_AND_C5_READINESS_ROADMAP_V2_2026-05-08.md`

## Response To The 9 Rebuttals

| # | Claude finding | Codex response | V2 treatment |
|---:|---|---|---|
| 1 | R blocked even zero-risk C5 paperwork | Agree | C5.0/C5.1 may run in parallel with R; C5.2+ blocked until R decision |
| 2 | R1 lacks N and DeepSeek boundary | Agree | R1 now requires at least 2 passes per listed family, N >= 18 total, and explicitly marks DeepSeek unknown unless run |
| 3 | R2 conflates observer and unauthorized tests | Agree | R2 now requires separate positive observer-role and negative blocked-role journeys |
| 4 | "Per local workspace" smuggles M2 terms | Agree | C5.1 now says one active full gate per local CVF installation |
| 5 | C5.4 redaction test was hedged | Agree | C5.4 now mandates deterministic fake-key redaction probe |
| 6 | CI1 should precede R | Agree | CI1 static gate is moved before R; CI2 protected live gate remains after C5 implementation |
| 7 | Adapter naming/interface extraction short | Agree | Track M now requires interface extraction first and uses `PostgresRuntimeJobStore`; Supabase is a deployment option |
| 8 | R3 only handled overclaim, not underclaim | Agree | R3 now includes underclaim/public docs drift for visible RC2 capabilities |
| 9 | Key leakage stop rule lacked positive test | Agree | C5.4 includes a redaction positive test across stdout, stderr, JSON artifact, persisted job state, and browser response/HAR evidence |

## Response To The 7 Review Questions

1. **Track R sufficiency:** V1 was not sufficient. V2 raises the floor from
   family coverage to minimum run count and evidence accounting.
2. **Claim N repair:** V1 was too weak. V2 separates positive lowest-authorized
   evidence visibility from negative unauthorized operation blocking.
3. **C5 controls:** Control list was directionally sound, but V2 adds mandatory
   deterministic redaction verification.
4. **CI timing:** V2 splits CI timing. Static CI1 may precede R; live CI2 comes
   after C5 is stable.
5. **Local-first boundary:** Kept unchanged and strengthened. Supabase remains
   optional.
6. **Supabase framing:** Preserved as optional managed/cloud deployment choice,
   not default state.
7. **Claim strength:** No overclaim found, but V2 adds underclaim sync for
   public docs if RC2 Web capabilities are user-facing and undocumented.

## Remaining Boundary

This response and the V2 roadmap are planning artifacts only.

Still forbidden:

- Post-RC2 non-coder no-regression is proven.
- C5 is implemented.
- Web can trigger the full live release gate.
- Release gate CI is implemented.
- CVF is GA-ready.
- Supabase is default CVF persistence.
