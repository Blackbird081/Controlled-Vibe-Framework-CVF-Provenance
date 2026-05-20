# CVF Work Order — CDH-M Maika Text-Summary Deployed Value Proof

Memory class: SUMMARY_RECORD

Status: CLOSED

GC-018:
`docs/baselines/CVF_GC018_CDH_M_MAIKA_TEXT_SUMMARY_DEPLOYED_VALUE_PROOF_2026-05-20.md`

## Authority Chain

- Operator request, 2026-05-20.
- CDH-M rebuttal:
  `docs/reviews/CVF_CDH_M_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- Privacy controls closure:
  `docs/reviews/CVF_CDH_M_MAIKA_TEXT_SUMMARY_PRIVACY_CONTROLS_COMPLETION_2026-05-20.md`
- GC-018 baseline:
  `docs/baselines/CVF_GC018_CDH_M_MAIKA_TEXT_SUMMARY_DEPLOYED_VALUE_PROOF_2026-05-20.md`

## Agent Roles

- Operator: authorizes the deployed-value proof.
- Codex: executes proof, records sanitized evidence, and cleans temporary
  secrets/accounts.
- Future reviewer: preserves the narrow claim boundary.

## Purpose

Prove that Maika, as a real downstream product, can use CVF for one practical
AI slice: a text-only daily-summary feature that sends a minimized payload
through governed CVF `/api/execute`, receives useful output, and carries CVF
receipt metadata.

## Scope

Allowed:

- Deploy Maika Edge Function.
- Temporarily configure Supabase Edge secrets for the proof.
- Invoke the deployed Edge Function with an authenticated admin session.
- Record sanitized proof metadata.
- Clean temporary proof secrets and account.

Forbidden:

- Direct provider fallback.
- Photo, image, or vision proof.
- Broad child-data claim.
- Public-sync or public release claim.
- Raw secret printing or persistence.

## Required First Reads

- `docs/reviews/CVF_CDH_M_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- `docs/reviews/CVF_CDH_M_MAIKA_TEXT_SUMMARY_PRIVACY_CONTROLS_COMPLETION_2026-05-20.md`
- `../CVF-Workspace/Nha tre Maika/supabase/functions/generate-daily-summary/index.ts`

## Pre-Flight Checks

Completed:

- CVF deployed Netlify route exists but local service token is not valid there.
- Local CVF route with live provider keys returns receipt metadata.
- Supabase CLI can access project `czxoozwydvmjisydyims`.
- Maika test admin account did not exist before proof and was created only for
  this proof.

## Write Ownership

Codex owns only:

- Maika Edge Function proof deployment.
- Proof docs in the CVF provenance workspace.
- Session continuity updates.

No CVF runtime/provider source file or public-sync file is in scope.

## Execution Plan

1. Start local CVF on a proof port with live provider env.
2. Expose local CVF through a temporary public tunnel.
3. Set Supabase Edge secrets to the tunnel URL and proof service token.
4. Deploy `generate-daily-summary`.
5. Create authenticated admin proof session.
6. Call deployed Edge Function with minimized abnormal-health payload.
7. Verify summary, receipt metadata, decision, provider/model, and no raw
   health leak.
8. Remove temporary Supabase secrets and proof admin account.
9. File completion review and update continuity.

## Tasks

- [x] CVF live route smoke test.
- [x] Supabase secrets set for proof.
- [x] Maika Edge Function deployed.
- [x] Deployed Edge Function invoked.
- [x] Sanitized proof metadata captured.
- [x] Temporary secrets removed.
- [x] Temporary account removed.

## Acceptance Criteria

- [x] Deployed Maika call returns HTTP 200.
- [x] Response includes `summary`.
- [x] Response includes `governanceEvidenceReceipt`.
- [x] Receipt decision is `ALLOW`.
- [x] Raw abnormal health leak check is false.
- [x] No direct provider fallback is introduced.

## Evidence Requirements

Evidence must include sanitized status fields only: HTTP status, response keys,
summary presence/length, receipt presence/id/decision/provider/model, and raw
health leak boolean. No raw token, API key, user token, or password may appear.

## Review Gate

Close only if the proof uses the deployed Maika Edge Function and returns CVF
receipt metadata without raw abnormal health leakage.

## Closure Checklist

- [x] Completion review filed.
- [x] Active review queue updated.
- [x] Active session state updated.
- [x] Active handoff updated.
- [x] Temporary secrets/account cleanup recorded.

## Return-To-Orchestrator Conditions

Return without closure if deployed Maika cannot reach CVF, if no receipt
metadata is returned, if raw health leaks, or if proof requires photo/vision or
direct-provider behavior.

## Claim Boundary

This work order proves practical value for one deployed Maika text-summary
integration slice only. It does not prove permanent production hosting or broad
CVF child-data governance.
