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

## Redaction Positive Test

C5.4 includes a deterministic fake-key redaction probe in
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.test.ts`
under test name:

```text
redacts an environment-backed fake live key from full release gate output
```

Fake key used:

```text
test_invalid_cvf_redaction_probe_20260508
```

The test sets the fake key through `ALIBABA_API_KEY`, injects it into simulated
full release gate `stdout` and `stderr`, submits the `full_live_release_gate`
job, then serializes both the returned result and persisted job list. The
assertion requires the fake key to be absent and `[REDACTED]` to be present.

Covered streams:

| Stream | Coverage | Result |
|---|---|---:|
| Command stdout summary | fake key injected as `provider_key=...` | PASS |
| Command stderr summary | fake key injected as `ALIBABA_API_KEY=...` | PASS |
| Job result JSON object | serialized returned `submitGovernanceJob()` result checked | PASS |
| Persisted runtime state | serialized `listGovernanceJobs()` result checked | PASS |

Not covered by this RC2 C5.4 deterministic probe:

| Stream | Status | Follow-up |
|---|---:|---|
| Browser-visible `/api/system/jobs` response body | COVERED BY BR | See `docs/reviews/CVF_C5_BROWSER_REDACTION_6_STREAM_EVIDENCE_2026-05-08.md` |
| HAR/network capture | COVERED BY BR | See `docs/reviews/CVF_C5_BROWSER_REDACTION_6_STREAM_EVIDENCE_2026-05-08.md` |

Boundary: this is a deterministic unit/in-process positive redaction probe, not
a live provider call. The live Web-triggered release gate evidence above proves
the actual C5 full-gate path; the fake-key probe proves the server-side
redaction and persistence path for four non-browser streams. The later BR
artifact closes the two browser-visible streams with a runCommand-layer
fake-key probe and no live provider call.

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
