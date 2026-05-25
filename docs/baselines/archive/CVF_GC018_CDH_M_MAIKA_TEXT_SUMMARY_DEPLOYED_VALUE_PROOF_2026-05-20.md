# CVF GC-018 — CDH-M Maika Text-Summary Deployed Value Proof

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_AND_CLOSED

Date: 2026-05-20

Authority: Operator request, 2026-05-20.

Roadmap / rebuttal authority:

- `docs/reviews/CVF_CDH_M_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- `docs/reviews/CVF_CDH_M_MAIKA_TEXT_SUMMARY_PRIVACY_CONTROLS_COMPLETION_2026-05-20.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

## Purpose

Authorize and record the narrow deployed-value proof for CDH-M:

- deployed Maika Supabase Edge Function invocation;
- authenticated admin-session call;
- minimized text-only payload;
- governed CVF `/api/execute` route;
- live provider-backed summary output;
- CVF receipt metadata returned to Maika;
- no direct provider fallback;
- no raw abnormal health leak.

## Scope / Target / Owner Boundary

In scope:

- Deployed `generate-daily-summary` Supabase Edge Function.
- Temporary public tunnel to the local CVF `/api/execute` route using live
  provider keys already present in the operator environment.
- Sanitized proof metadata only.

Out of scope:

- Permanent Netlify CVF service-token configuration.
- Public-sync or public claim updates.
- Child-data governance proof beyond this minimized text-summary slice.
- Photo, image, or vision runtime proof.
- Maika production-readiness claim.

Owner:

- Operator authorized the proof.
- Codex executed and recorded the bounded evidence.

## Source / Predecessor Evidence

Predecessors:

- CDH-M rebuttal:
  `docs/reviews/CVF_CDH_M_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- Privacy controls completion:
  `docs/reviews/CVF_CDH_M_MAIKA_TEXT_SUMMARY_PRIVACY_CONTROLS_COMPLETION_2026-05-20.md`

Pre-scan / setup facts:

- Deployed CVF Netlify endpoint `https://vibcode.netlify.app/api/execute`
  exists but rejected the local service token with 401.
- Netlify CLI was not logged in, so deployed Netlify service-token alignment
  could not be changed in this tranche.
- Supabase CLI was available through `npx supabase`, and the Maika Supabase
  project was accessible.

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED_AND_CLOSED.

The proof may use deployed Maika plus a temporary public tunnel to local CVF
because the value claim is about the downstream product integration pattern,
not permanent hosting posture.

The retained claim is:

CDH-M proves practical value for one real downstream-product slice:
text-only Maika daily summary, minimized payload, governed CVF route, live
provider-backed output, receipt metadata, and no direct provider fallback.

## Authorized Scope

Allowed operations:

- Deploy Maika `generate-daily-summary` Edge Function.
- Temporarily set Supabase secrets `CVF_EXECUTE_URL` and `CVF_SERVICE_TOKEN`
  for the proof.
- Create an admin test session only for the proof.
- Invoke the deployed Edge Function with an abnormal-health payload.
- Remove temporary Supabase CVF secrets and delete the test admin account
  after proof.

Forbidden operations:

- Printing raw Supabase, CVF, or provider secrets.
- Leaving temporary tunnel secrets configured in Supabase.
- Claiming photo, vision, broad child-data, or public production readiness.

## Key Invariants

- The proof payload must not include child name, parent name, contact data,
  student ID, or photo data.
- Raw abnormal health terms must not appear in the Maika response body.
- CVF receipt metadata must be present.
- The proof must remain bounded to this deployed text-summary slice.

## Done Criteria

- [x] CVF local service-token smoke test returned live receipt metadata.
- [x] Supabase Edge Function deployed.
- [x] Deployed Maika Edge Function returned HTTP 200.
- [x] Deployed Maika response included `summary`.
- [x] Deployed Maika response included `governanceEvidenceReceipt`.
- [x] Receipt decision was `ALLOW`.
- [x] Raw abnormal health leak check was `false`.
- [x] Temporary Supabase CVF secrets were removed after proof.
- [x] Temporary test admin account was deleted after proof.

## Evidence / Verification

CVF local live smoke:

- HTTP status: `200`
- `success`: `true`
- `hasReceipt`: `true`
- decision: `ALLOW`

Deployed Maika Edge Function proof:

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

Cleanup evidence:

- Supabase secrets `CVF_EXECUTE_URL` and `CVF_SERVICE_TOKEN` were unset after
  proof.
- Temporary `admin@maika.test` proof account was deleted from auth and profile.

## Claim Boundary

This GC-018 proves one narrow practical-value slice. It does not prove
permanent production hosting, broad child-data governance, photo/vision
governance, CDH-C/D/H closure, or public release readiness.
