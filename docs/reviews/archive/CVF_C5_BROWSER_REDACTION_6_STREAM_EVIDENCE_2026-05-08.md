<!-- Memory class: FULL_RECORD -->
# CVF C5 Browser Redaction 6-Stream Evidence

**Date:** 2026-05-08
**Status:** PASS
**Track:** BR - Browser Redaction Closure
**Provider calls:** 0 live calls

## Design

- Fake key: deterministic sentinel `test_invalid_cvf_redaction_probe_20260508`.
- Injection point: `defaultRunCommand()` runCommand layer before the redaction pipeline.
- Test hook: `CVF_WEB_GOVERNANCE_REDACTION_PROBE=run_command_fake_key` and fake `ALIBABA_API_KEY`.
- API-response-layer mock was not used.

## Stream Coverage

| Stream | Status | Evidence |
|---|---|---|
| stdout | PASS | Existing unit probe plus runCommand stdout injection. |
| stderr | PASS | Existing unit probe plus runCommand stderr injection. |
| returned job object | PASS | `/api/system/jobs` returned redacted job result. |
| persisted runtime state | PASS | Existing persisted state probe remains covered by `web-governance-jobs.test.ts`. |
| browser-visible API response | PASS | Playwright browser `fetch()` response omitted the fake key and contained `[REDACTED]`. |
| network capture | PASS | Playwright response event capture omitted the fake key and contained `[REDACTED]`. |

## Boundary

- This proves redaction behavior only.
- It does not prove live provider governance behavior.
- No real provider key was used.
- No live provider call was made.