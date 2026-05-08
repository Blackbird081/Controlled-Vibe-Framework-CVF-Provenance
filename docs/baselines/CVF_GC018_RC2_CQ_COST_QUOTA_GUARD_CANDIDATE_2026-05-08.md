<!-- Memory class: SUMMARY_RECORD -->
# CVF GC-018 Candidate - RC2 CQ Cost/Quota Guard

**Date:** 2026-05-08
**Status:** AUTHORIZED BY OPERATOR FOR IMPLEMENTATION
**Roadmap:** `docs/roadmaps/CVF_POST_RC2_GA_READINESS_COST_QUOTA_AND_RELEASE_HARDENING_ROADMAP_V2_2026-05-08.md`
**Claude authorization:** `docs/reviews/CVF_POST_RC2_GA_READINESS_ROADMAP_V2_CLAUDE_AUTHORIZATION_2026-05-08.md`

## Scope Lock

Allowed:

- Implement local-first call-count policy, integer estimates, cooldown,
  server-side preflight, direct API blocking, and override audit.
- Add Web operator UX that displays estimate/current usage/cap/block reason.
- Use live proof only for the under-budget allow path.
- Use no-live tests for over-limit, cooldown, direct API bypass, and role
  override cases.

Forbidden:

- Dollar billing reconciliation claims.
- UI-only confirmation as a budget guard.
- Committing operator-specific policy with secrets.
- Supabase/Postgres as a default requirement.

## Exit Evidence

- `docs/reviews/CVF_COST_QUOTA_GUARD_THREAT_MODEL_2026-05-08.md`
- `docs/reviews/CVF_COST_QUOTA_LOCAL_POLICY_CONTRACT_2026-05-08.md`
- `docs/reviews/CVF_COST_QUOTA_PREFLIGHT_EVIDENCE_2026-05-08.md`
- `docs/reviews/CVF_COST_QUOTA_WEB_OPERATOR_EVIDENCE_2026-05-08.md`
- `docs/reviews/CVF_COST_QUOTA_AUDIT_EVIDENCE_2026-05-08.md`
