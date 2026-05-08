<!-- Memory class: FULL_RECORD -->
# CVF CI2 Hosted Live Gate Pass Run

**Date:** 2026-05-09
**Track:** CI2-H1c - Hosted Protected Live Gate Closure
**Status:** PASS
**Run ID:** `25575296660`
**Run URL:** `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF/actions/runs/25575296660`
**Head SHA:** `1a2fa8862d823436618b093f6690b5fd4de2eab7`
**Result artifact:** `.cvf/runtime/ci2h-hosted/25575296660/cvf-protected-live-release-gate-result.json`

## Summary

| Field | Value |
|---|---|
| Workflow | `CVF Protected Live Release Gate` |
| Event | `workflow_dispatch` |
| Protected environment | `cvf-live-release-gate` |
| Secret name used | `DASHSCOPE_API_KEY` |
| Conclusion | `success` |
| Gate result | `PASS` |
| Passing checks | 7/7 |
| Duration | 5m28s |

## Release Gate Breakdown

| Check | Status | Note |
|---|---|---|
| Web build | PASS | `npm run build` succeeded. |
| TypeScript check | PASS | Guard Contract TypeScript check clean. |
| Provider readiness | PASS | Certified lanes: 2; status `CERTIFIED`. |
| Secrets scan | PASS | No secret patterns detected. |
| Docs governance | PASS | Required RC docs present. |
| E2E Playwright UI mock | PASS | Mock UI suite passed. |
| E2E Playwright Governance live | PASS | Live governance suite passed on hosted GitHub runner. |

## Closure Notes

The hosted PASS followed two fail-closed runs:

- Run `25573498275` failed before release gate execution because Guard Contract
  used `npm ci` without a tracked lockfile.
- Run `25574408974` reached release gate and passed 6/7, then failed live
  governance E2E due the Web Alibaba resolver not accepting
  `DASHSCOPE_API_KEY`.

The corrective patch at head `1a2fa8862d823436618b093f6690b5fd4de2eab7` aligned Web key resolution with the
release-quality proof contract by accepting `DASHSCOPE_API_KEY` directly.

## Secret Handling

- The workflow used GitHub environment secret name `DASHSCOPE_API_KEY`.
- GitHub logs masked secret values.
- No raw provider key value is included in this artifact.

## Decision Impact

CI2-H is no longer deferred. The Post-RC2 GA decision can move from
`GA_LOCAL_FIRST_APPROVED_WITH_LIMITS` to `GA_LOCAL_FIRST_APPROVED`, while still
preserving known limits around exact-dollar billing, multi-tenant cloud quota
enforcement, optional managed Postgres/Supabase mode, and full DeepSeek
regression confirmation.
