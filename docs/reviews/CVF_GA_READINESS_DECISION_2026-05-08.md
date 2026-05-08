<!-- Memory class: FULL_RECORD -->
# CVF GA Readiness Decision

**Date:** 2026-05-08
**Decision:** `GA_LOCAL_FIRST_APPROVED_WITH_LIMITS`
**Roadmap:** `docs/roadmaps/CVF_POST_RC2_GA_READINESS_COST_QUOTA_AND_RELEASE_HARDENING_ROADMAP_V2_2026-05-08.md`
**Evidence index:** `docs/reviews/CVF_GA_READINESS_EVIDENCE_INDEX_2026-05-08.md`

## Decision Rationale

CVF can move to local-first GA readiness because the Post-RC2 blockers with the
highest product risk now have evidence:

- Browser redaction closure passed across six streams.
- Web-triggered live release gate now has local cost/quota preflight and audit.
- A live Web `full_live_release_gate` completed release gate 7/7 under CQ.
- DeepSeek smoke/sanity passed 8/8 live governed calls under CQ.
- Public docs were refreshed to avoid hosted-CI, exact-billing, or cloud-storage overclaims.

## Gate Matrix

| Gate | Decision | Evidence |
|---|---|---|
| BR - browser redaction | PASS | `docs/reviews/CVF_C5_BROWSER_REDACTION_6_STREAM_EVIDENCE_2026-05-08.md` |
| CQ - cost/quota guard | PASS | `docs/reviews/CVF_COST_QUOTA_VERIFICATION_EVIDENCE_2026-05-08.md`; `docs/reviews/CVF_COST_QUOTA_PREFLIGHT_EVIDENCE_2026-05-08.md` |
| C5 Web full release gate under CQ | PASS | `docs/reviews/CVF_COST_QUOTA_WEB_OPERATOR_EVIDENCE_2026-05-08.md` |
| CQ audit | PASS | `docs/reviews/CVF_COST_QUOTA_AUDIT_EVIDENCE_2026-05-08.md` |
| DS smoke under CQ | PASS SMOKE | `docs/reviews/CVF_DEEPSEEK_POST_RC2_SMOKE_COVERAGE_2026-05-08.md` |
| Documentation currency | PASS WITH BOUNDARIES | `docs/reviews/CVF_GA_DOCUMENTATION_CURRENCY_AUDIT_2026-05-08.md` |
| Hosted CI2-H | DEFERRED | `docs/reviews/CVF_CI2_HOSTED_LIVE_GATE_FAILURE_MODE_2026-05-08.md` |

## Authorized Claim

CVF has local-first GA readiness for governed Web operations: allowlisted live
jobs can be run from Web, secrets are redacted across the tested browser and
server streams, and local cost/quota controls gate live provider calls before
execution.

## Disallowed Claims

- Do not claim hosted CI2-H PASS until a protected GitHub run is dispatched and
  recorded after the relevant commits are on `origin/main`.
- Do not claim exact provider-dollar cost control; CQ is expected live-call
  budgeting and audit.
- Do not claim multi-tenant cloud quota enforcement.
- Do not claim full DeepSeek regression confirmation from the 8/8 smoke run.
- Do not claim Supabase/Postgres is required for local developer use.

## Next Follow-Up Order

1. Push the current Post-RC2 GA commits.
2. Run CI2-H hosted live gate metadata sanity and protected dispatch from GitHub.
3. If needed, expand DeepSeek from smoke/sanity to N>=14 regression confirmation.
4. Scope optional persistent runtime-job store for managed deployment only, keeping local-file mode as the default developer path.

## 2026-05-09 Post-Push Addendum

The Post-RC2 GA commits are now visible on `origin/main`, and GitHub REST
metadata confirms that `.github/workflows/cvf-protected-live-release-gate.yml`
is active. No hosted run exists yet for this workflow on `main`, and this local
machine still has no `gh` command or GitHub token environment variable.

Decision remains `GA_LOCAL_FIRST_APPROVED_WITH_LIMITS` until an authenticated
operator or GitHub-enabled agent runs CI2-H metadata sanity, dispatches the
protected workflow, and files a hosted PASS artifact.

Follow-up artifacts:

- `docs/reviews/CVF_CI2_HOSTED_LIVE_GATE_POST_PUSH_SANITY_2026-05-09.md`
- `docs/reviews/CVF_CI2_HOSTED_LIVE_GATE_OPERATOR_DISPATCH_RUNBOOK_2026-05-09.md`

## 2026-05-09 Hosted Failure Addendum

Hosted run `25573498275` was dispatched after configuring environment
`cvf-live-release-gate` and environment secret name `DASHSCOPE_API_KEY`. The run
failed before release gate execution at the Guard Contract dependency install
step because the workflow used `npm ci` for a package whose lockfile is not
tracked. No provider call was reached, and no release gate PASS claim is made.

Failure artifact:

- `docs/reviews/CVF_CI2_HOSTED_LIVE_GATE_FAILURE_RUN_2026-05-09.md`

Corrective patch:

- `.github/workflows/cvf-protected-live-release-gate.yml` now uses
  `npm install --no-audit --no-fund` for `EXTENSIONS/CVF_GUARD_CONTRACT` and
  keeps `npm ci` for `cvf-web`.
