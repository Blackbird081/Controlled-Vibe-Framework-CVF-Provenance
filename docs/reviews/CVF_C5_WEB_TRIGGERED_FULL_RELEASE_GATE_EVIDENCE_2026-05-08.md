<!-- Memory class: FULL_RECORD -->
# CVF C5 Web-Triggered Full Live Release Gate Evidence

**Date:** 2026-05-08
**Roadmap item:** C5 — Full live release gate trigger from Web
**Command executed by Web job:** `python scripts/run_cvf_release_gate_bundle.py --json`
**Web surface:** `/governance/operations`
**Audit path:** `.cvf/runtime/web-governance-jobs.jsonl`
**Job ID:** `4b6d375e-7c55-4696-9627-e01cb5006c63`
**Job status:** succeeded
**Gate result:** PASS
**Checks passed:** 7/7

## Control Evidence

| Control | Evidence |
|---|---|
| Web trigger, not CLI-only | Browser probe logged in as admin and clicked the `Full Live Release Gate` job card. |
| Fixed command contract | `python scripts/run_cvf_release_gate_bundle.py --json` |
| Role-bound trigger | Job role recorded as `admin`; anonymous/viewer paths remain blocked by policy tests. |
| Provider lane | `alibaba` |
| Handler | `scripts.run_cvf_release_gate_bundle.live` |
| Redaction | `applied` |
| Cost/quota warning | Web card warns that the action consumes live provider quota and is not dry readiness. |
| Runtime isolation | Full gate child process uses `NEXT_DIST_DIR=.next-cvf-release-gate` and `CVF_PLAYWRIGHT_PORT=3011` to avoid corrupting the controlling Web dev server. |

## Release Gate Breakdown

| Check | Status |
|---|---:|
| Web build (npm run build) | PASS |
| TypeScript check (guard contract) | PASS |
| Provider readiness | PASS |
| Secrets scan | PASS |
| Docs governance (RC docs present) | PASS |
| E2E Playwright UI (mock) | PASS |
| E2E Playwright Governance (live) | PASS |

## Boundary

This proves C5.2 for operator/admin Web triggering of the full live release
gate. The persistent job store remains local JSONL for RC2; managed database
storage is future optional infrastructure, not the default CVF dev path.
