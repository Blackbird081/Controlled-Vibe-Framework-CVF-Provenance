<!-- Memory class: FULL_RECORD -->
# CVF CI2 Hosted Live Gate Release-Gate Failure Run

**Date:** 2026-05-09
**Track:** CI2-H1b - Hosted Release Gate Failure Path
**Status:** FAILED AT LIVE GOVERNANCE E2E
**Run ID:** `25574408974`
**Run URL:** `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF/actions/runs/25574408974`
**Head SHA:** `29dea1d796d56a13595115a2fe88491d5902d479`
**Result artifact:** `.cvf/runtime/ci2h-hosted/25574408974/cvf-protected-live-release-gate-result.json`

## Summary

| Field | Value |
|---|---|
| Workflow | `CVF Protected Live Release Gate` |
| Event | `workflow_dispatch` |
| Conclusion | `failure` |
| Release gate command reached | yes |
| Release gate artifact uploaded | yes |
| Gate result | `FAIL` |
| Passing checks | 6/7 |
| Failing check | `E2E Playwright Governance (live)` |
| Failure class | `hosted_live_governance_e2e_failure` |

## Release Gate Breakdown

| Check | Status | Note |
|---|---|---|
| Web build | PASS | `npm run build` succeeded. |
| TypeScript check | PASS | Guard Contract TypeScript check clean. |
| Provider readiness | PASS | Certified lanes: 2; provider metadata reached. |
| Secrets scan | PASS | No secret patterns detected. |
| Docs governance | PASS | Required RC docs present. |
| E2E Playwright UI mock | PASS | Mock UI suite passed. |
| E2E Playwright Governance live | FAIL | Three Alibaba live governance assertions failed. |

## Failing Live Assertions

The uploaded release-gate JSON records assertion failures for:

- `governance-gate-live.spec.ts` - normal governed request completes without block.
- `governance-gate-live.spec.ts` - bypass detection handles high-risk output correctly.
- `noncoder-governance-live.spec.ts` - governance controls fire on real Alibaba AI response, L-008.

The result artifact only included the Playwright failure names and screenshot
paths, not the response body or error context files.

## Root Cause Candidate

The hosted environment configured the protected secret name
`DASHSCOPE_API_KEY`. The release gate script accepts this name directly, but Web
`/api/execute` resolved Alibaba provider keys through
`src/lib/alibaba-env.ts`, which recognized `ALIBABA_API_KEY`,
`CVF_BENCHMARK_ALIBABA_KEY`, and `CVF_ALIBABA_API_KEY`, but not
`DASHSCOPE_API_KEY`.

That mismatch can explain the observed pattern: provider readiness passed while
Web live governance assertions failed when `/api/execute` attempted the
Alibaba lane.

## Corrective Action

- Add `DASHSCOPE_API_KEY` to the Web Alibaba key resolver and its unit tests.
- Upload Playwright diagnostics from the protected workflow on failure so future
  hosted failures include screenshots and error contexts.
- Retry CI2-H only after this patch is pushed.

## Secret Handling

- GitHub logs masked the protected key as `***`.
- No raw provider key value is included in this artifact.
- This run did reach live-governance execution, but did not prove CI2-H PASS.

## Boundary

This run preserves fail-closed behavior and does not authorize upgrading
`GA_LOCAL_FIRST_APPROVED_WITH_LIMITS` to full hosted GA. Hosted CI2-H remains
open until a protected run records release gate 7/7 PASS.
