<!-- Memory class: FULL_RECORD -->
# CVF RC2 Developer Live Spot-Check

**Date:** 2026-05-08  
**Scope:** RC2 pre-push Blocker 3, Claim D  
**Claim:** A developer can diagnose the local clone, validate providers, reach Web visibility pages, and trigger a non-destructive governed job with audit evidence.  
**Result:** PASS WITH ACCEPTED LOCAL WARN

## CLI Evidence

Local Windows clone path:

`D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF`

Doctor:

```bash
python scripts/cvf_doctor.py --json
```

Result: `WARN`, with all core readiness checks PASS. The warning was expected because port 3000 was already listening for the RC2 proof app server.

Provider checks:

```bash
python scripts/cvf_provider_check.py --provider alibaba --live --json
python scripts/cvf_provider_check.py --provider deepseek --live --json
```

Results:

| Provider | Status | Live validation |
|---|---|---|
| Alibaba | `LIVE_VALIDATED` | HTTP 200 |
| DeepSeek | `LIVE_VALIDATED` | HTTP 200 |

Setup:

```bash
python scripts/cvf_setup.py --provider alibaba --live-provider-check --json
```

Result: `READY`; provider step `PASS`, live validation HTTP 200; start-web and first-governed-run steps marked `READY`.

## Web Evidence

Screenshots:

- Health UI: `docs/reviews/rc2-evidence-screenshots/rc2-claim-d-health.png`
- Runtime module registry: `docs/reviews/rc2-evidence-screenshots/rc2-claim-d-modules.png`
- Governance evidence readout: `docs/reviews/rc2-evidence-screenshots/rc2-claim-d-evidence.png`
- C4 operations UI: `docs/reviews/rc2-evidence-screenshots/rc2-claim-d-operations.png`

Non-destructive C4 job audit:

```json
{
  "jobType": "provider_check",
  "providerLane": "deepseek",
  "role": "admin",
  "status": "succeeded",
  "decision": "allowed",
  "handlerId": "scripts.cvf_provider_check.json.live",
  "fixedArgv": ["scripts/cvf_provider_check.py", "--provider", "deepseek", "--live", "--json"],
  "liveValidation": "HTTP 200"
}
```

Raw provider keys were not printed. Audit redaction check confirmed no raw configured secret values, no bearer token, and no `sk-...` pattern in `.cvf/runtime/web-governance-jobs.jsonl`.

## Boundary

Windows local proof only. macOS/Linux remain `DEFERRED_PLATFORM` under the RC2 A2 boundary. This spot-check proves the current clone and Web surfaces can be operated by a developer; it is not GA certification.

