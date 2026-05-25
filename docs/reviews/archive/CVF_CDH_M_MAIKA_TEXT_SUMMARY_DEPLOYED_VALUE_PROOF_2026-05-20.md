# CVF CDH-M Maika Text-Summary Deployed Value Proof

Memory class: FULL_RECORD

Status: CLOSED_DEPLOYED_VALUE_PROOF_WITH_TEMP_CVF_TUNNEL

docType: review

Reviewer: Codex

Date: 2026-05-20

GC-018:
`docs/baselines/CVF_GC018_CDH_M_MAIKA_TEXT_SUMMARY_DEPLOYED_VALUE_PROOF_2026-05-20.md`

Work order:
`docs/work_orders/CVF_WO_CDH_M_MAIKA_TEXT_SUMMARY_DEPLOYED_VALUE_PROOF_2026-05-20.md`

## Purpose

Record the completed CDH-M deployed-value proof for Maika as a real
downstream product slice.

The proof demonstrates practical value for one narrow feature: text-only daily
summary, minimized payload, governed CVF route, live provider-backed output,
receipt metadata, and no direct provider fallback.

## Scope / Target / Owner Boundary

In scope:

- Deployed Maika Supabase Edge Function `generate-daily-summary`.
- Authenticated admin proof invocation.
- Temporary public tunnel to local CVF `/api/execute`.
- Live provider-backed CVF execution.
- Sanitized evidence recording.

Out of scope:

- Permanent Netlify CVF service-token alignment.
- Public-facing claims.
- Photo, image, or vision proof.
- Broad child-data governance proof.
- CDH-C, CDH-D, or CDH-H closure.

Owner:

- Codex executed and reviewed the proof.

## Target / Source Under Review

Maika source:

- `../CVF-Workspace/Nha tre Maika/supabase/functions/generate-daily-summary/index.ts`
- `../CVF-Workspace/Nha tre Maika/supabase/functions/_shared/daily-summary-privacy.ts`
- `../CVF-Workspace/Nha tre Maika/src/pages/admin/DailyReports.jsx`

CVF route:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`

Governance sources:

- `docs/reviews/CVF_CDH_M_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- `docs/reviews/CVF_CDH_M_MAIKA_TEXT_SUMMARY_PRIVACY_CONTROLS_COMPLETION_2026-05-20.md`

## Scope / Methodology

The proof used:

1. Local CVF `/api/execute` running with live provider keys.
2. A temporary public localtunnel URL for Supabase Edge Function reachability.
3. Temporary Supabase secrets for `CVF_EXECUTE_URL` and `CVF_SERVICE_TOKEN`.
4. Deployed Supabase Edge Function invocation with a test admin session.
5. A minimized payload containing mood, meals, sleep, activities, and a raw
   abnormal health input used only to test redaction.
6. Sanitized output metadata capture.
7. Cleanup of temporary Supabase secrets and proof admin account.

## Findings / Position

Position: CLOSED_DEPLOYED_VALUE_PROOF_WITH_TEMP_CVF_TUNNEL.

Findings:

1. Deployed Maika Edge Function invocation succeeded with HTTP 200.
2. The response included a useful summary.
3. The response included CVF governance receipt metadata.
4. The receipt decision was `ALLOW`.
5. The provider/model recorded in receipt metadata were `openai` /
   `gpt-4o-mini`.
6. Raw abnormal health terms were absent from the response body.
7. No direct provider fallback was introduced in Maika.
8. Temporary proof secrets and the temporary admin account were removed after
   the run.

## Evidence

Sanitized proof result:

```json
{
  "httpStatus": 200,
  "ok": true,
  "responseKeys": ["summary", "governanceEvidenceReceipt"],
  "hasSummary": true,
  "summaryLength": 113,
  "hasGovernanceEvidenceReceipt": true,
  "governanceReceiptId": "rcpt-env-mpdvfd55-beft8s",
  "receiptDecision": "ALLOW",
  "receiptProvider": "openai",
  "receiptModel": "gpt-4o-mini",
  "rawHealthLeak": false,
  "error": null
}
```

Additional verification:

- `deno test --no-lock supabase/functions/_shared/daily-summary-privacy.test.ts`
  passed: 2/2.
- `deno check --node-modules-dir=auto --no-lock supabase/functions/generate-daily-summary/index.ts`
  passed.
- `npm run build` in Maika passed before deployment.
- `npx supabase functions deploy generate-daily-summary --project-ref
  czxoozwydvmjisydyims` deployed the function and uploaded the shared privacy
  helper.

Cleanup:

- Supabase `CVF_EXECUTE_URL` and `CVF_SERVICE_TOKEN` proof secrets were unset.
- Temporary `admin@maika.test` proof account was deleted from auth and profile.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Temporary tunnel mistaken for permanent production setup | Status and claim boundary name `TEMP_CVF_TUNNEL` explicitly |
| Proof overclaimed as broad child-data governance | Scope states minimized text-summary slice only |
| Raw health detail leakage | Frontend and Edge Function minimization controls verified; leak check false |
| Temporary secrets left in Supabase | Secrets were unset after proof |
| Temporary admin account left active | Proof account was deleted after proof |

## Decision / Recommendation / Disposition

Disposition: CLOSED_DEPLOYED_VALUE_PROOF_WITH_TEMP_CVF_TUNNEL.

CDH-M now has enough evidence to claim practical value for the narrow Maika
text-summary slice:

- real downstream product surface;
- deployed Maika Edge Function;
- authenticated admin invocation;
- minimized text-only payload;
- governed CVF route;
- live provider-backed summary;
- CVF receipt metadata;
- no direct provider fallback;
- no raw abnormal health leak.

Remaining work, if productization is desired:

- Configure a permanent deployed CVF service-token endpoint rather than a
  temporary tunnel.
- Re-run the same proof after permanent endpoint configuration.

## Verification

Verification is live but bounded:

- Maika side: deployed Supabase Edge Function.
- CVF side: local CVF exposed through temporary public tunnel.
- Provider side: live provider execution through CVF.

No mock AI mode was used for the value proof.

## Claim Boundary

This packet does not claim Maika production readiness, broad child-data
governance, photo/vision governance, permanent CVF hosting, public release
readiness, or closure of CDH-C/D/H.
