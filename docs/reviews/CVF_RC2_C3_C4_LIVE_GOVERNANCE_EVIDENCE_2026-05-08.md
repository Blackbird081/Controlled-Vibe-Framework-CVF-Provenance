<!-- Memory class: FULL_RECORD -->
# CVF RC2 C3/C4 Live Governance Evidence

**Date:** 2026-05-08  
**Scope:** RC2 pre-push Blocker 2  
**Surface:** `/governance/operations` + `POST /api/system/jobs`  
**Audit log:** `.cvf/runtime/web-governance-jobs.jsonl`  
**Result:** PASS

## Runner Hardening Applied

`provider_check` from the Web operations runner now invokes live validation:

```text
python scripts/cvf_provider_check.py --provider <alibaba|deepseek> --live --json
```

The timeout proof uses a bounded `timeoutMsOverride` that can only reduce the job timeout, not raise it above the allowlisted job cap.

Targeted verification:

```bash
cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npx tsc --noEmit
npx vitest run src/lib/server/web-governance-jobs.test.ts src/app/api/system/jobs/route.test.ts 'src/app/(dashboard)/governance/operations/page.test.tsx'
```

Result: typecheck PASS; 3 files / 14 tests PASS.

## Live Provider Preconditions

Secret-safe live provider checks passed before Web proof:

| Provider | Command | Status |
|---|---|---|
| Alibaba | `python scripts/cvf_provider_check.py --provider alibaba --live --json` | `LIVE_VALIDATED`, HTTP 200 |
| DeepSeek | `python scripts/cvf_provider_check.py --provider deepseek --live --json` | `LIVE_VALIDATED`, HTTP 200 |

Raw key values were not printed.

## C4 Browser Evidence

Screenshots:

- Viewer blocked state: `docs/reviews/rc2-evidence-screenshots/rc2-c4-viewer-blocked.png`
- Operator Alibaba live provider check: `docs/reviews/rc2-evidence-screenshots/rc2-c4-operator-alibaba-provider-check.png`
- Admin DeepSeek + dry readiness + timeout: `docs/reviews/rc2-evidence-screenshots/rc2-c4-admin-deepseek-dry-timeout.png`

## Audit Excerpts

Viewer attempted provider check from an authenticated C4 page context. UI controls were read-only, and the same-origin trigger attempt was blocked and audited:

```json
{
  "eventId": "1d461397-b8bf-4d22-a8e1-fc410cb11d16",
  "jobId": "6279f1de-3a5d-4adc-8d5d-6e646be1cc30",
  "status": "blocked_by_policy",
  "decision": "blocked_by_policy",
  "decisionReason": "read_only_role_cannot_trigger",
  "role": "viewer",
  "providerLane": "alibaba",
  "handlerId": "scripts.cvf_provider_check.json.live",
  "fixedArgv": ["scripts/cvf_provider_check.py", "--provider", "alibaba", "--live", "--json"]
}
```

Operator live Alibaba provider check:

```json
{
  "eventId": "30ada3c6-573f-42ae-abcd-d9c4521e8213",
  "jobId": "48cc47d1-2e1c-4ae9-8029-f86a2575f2e9",
  "status": "succeeded",
  "decision": "allowed",
  "decisionReason": "role_authorized",
  "role": "operator",
  "providerLane": "alibaba",
  "handlerId": "scripts.cvf_provider_check.json.live",
  "fixedArgv": ["scripts/cvf_provider_check.py", "--provider", "alibaba", "--live", "--json"],
  "liveValidation": "HTTP 200"
}
```

Admin live DeepSeek provider check:

```json
{
  "eventId": "c150ea0b-4ba4-418f-ae04-5b2550e4ea28",
  "jobId": "497ded63-4ed4-4fce-a4bd-cb716c100b56",
  "status": "succeeded",
  "decision": "allowed",
  "decisionReason": "role_authorized",
  "role": "admin",
  "providerLane": "deepseek",
  "handlerId": "scripts.cvf_provider_check.json.live",
  "fixedArgv": ["scripts/cvf_provider_check.py", "--provider", "deepseek", "--live", "--json"],
  "liveValidation": "HTTP 200"
}
```

Admin release-gate dry readiness:

```json
{
  "eventId": "cb6ff6da-91dd-49c6-bf5e-043c0f2b87cc",
  "jobId": "b352f051-cb18-41f7-97ff-1d554b5ebd95",
  "status": "succeeded",
  "role": "admin",
  "handlerId": "scripts.run_cvf_release_gate_bundle.dry_run",
  "fixedArgv": ["scripts/run_cvf_release_gate_bundle.py", "--dry-run", "--json"]
}
```

Forced timeout lifecycle:

```json
{
  "eventId": "57b06ae6-ef4d-42b9-b39d-2c4c0a048639",
  "jobId": "14d57744-7beb-469d-9746-c43c751818ac",
  "status": "timed_out",
  "decision": "allowed",
  "decisionReason": "role_authorized",
  "role": "admin",
  "providerLane": "alibaba",
  "timeoutMs": 1,
  "timedOut": true,
  "handlerId": "scripts.cvf_provider_check.json.live"
}
```

## Redaction Proof

Audit log redaction check:

```json
{
  "actualSecretPresent": false,
  "skPattern": false,
  "longBearer": false,
  "checkedSecretNames": ["DASHSCOPE_API_KEY", "ALIBABA_API_KEY", "DEEPSEEK_API_KEY"]
}
```

Boundary: audit summaries may include environment variable names such as `DASHSCOPE_API_KEY` or `DEEPSEEK_API_KEY` as key-source labels. They do not include raw values, bearer tokens, or `sk-...` keys.

