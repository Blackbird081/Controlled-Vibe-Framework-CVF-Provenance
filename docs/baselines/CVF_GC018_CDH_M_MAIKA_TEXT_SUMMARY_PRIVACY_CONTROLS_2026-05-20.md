# CVF GC-018 — CDH-M Maika Text-Summary Privacy Controls

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

Date: 2026-05-20

Authority: Operator request, 2026-05-20.

Roadmap / rebuttal authority:

- `docs/reviews/CVF_CDH_M_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

## Purpose

Authorize a narrow implementation tranche for the CDH-M privacy gate:
redaction/minimization controls for abnormal health values in the deployed
Maika text-summary path.

This baseline does not authorize deployed live proof, child-data proof, photo
handling, vision runtime, direct provider fallback, public-sync claims, or
bundled CDH closure.

## Scope / Target / Owner Boundary

In scope:

- Maika text-summary payload minimization before the Supabase Edge Function call.
- Maika Edge Function redaction before constructing the CVF `/api/execute`
  body.
- Regression tests for the health redaction/minimization helper.
- Provenance docs for this narrow tranche.

Out of scope:

- Live deployed Supabase invocation proof.
- CVF runtime or provider changes.
- Photo, image, or vision handling.
- Maika database schema, auth model, notifications, or parent portal changes.
- Public-sync edits or claims.

Owner:

- Operator authorized the tranche.
- Codex implements the bounded controls.

## Source / Predecessor Evidence

Predecessor:

- `docs/reviews/CVF_CDH_M_DELTA_CODEX_REBUTTAL_2026-05-20.md`

Pre-scan confirms:

- `../CVF-Workspace/Nha tre Maika/supabase/functions/generate-daily-summary/index.ts`
  currently accepts `health` and can place abnormal health text into
  `currentNotes`.
- `../CVF-Workspace/Nha tre Maika/src/pages/admin/DailyReports.jsx`
  currently sends abnormal `form.health` in the summary payload.

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED.

The accepted posture is to implement minimization by default:

- abnormal health values are treated as sensitive;
- raw abnormal health text must not be sent to CVF;
- health detail is replaced with a non-diagnostic marker before the governed
  summary request is built.

This makes abnormal-health proof possible without exposing raw health details
to CVF. A later deployed proof still needs its own evidence packet.

## Authorized Scope

Files Worker may modify in the Maika sibling workspace:

- `supabase/functions/generate-daily-summary/index.ts`
- `supabase/functions/_shared/daily-summary-privacy.ts`
- `supabase/functions/_shared/daily-summary-privacy.test.ts`
- `src/pages/admin/DailyReports.jsx`

Files Worker may create in the CVF provenance workspace:

- `docs/work_orders/CVF_WO_CDH_M_MAIKA_TEXT_SUMMARY_PRIVACY_CONTROLS_2026-05-20.md`
- `docs/reviews/CVF_CDH_M_MAIKA_TEXT_SUMMARY_PRIVACY_CONTROLS_COMPLETION_2026-05-20.md`

Files Worker must not touch:

- CVF execute route or provider runtime files.
- Maika photo, media, auth, schema, notification, or parent portal files.
- Public-sync clone.

## Key Invariants

- No raw abnormal health value may appear in the CVF request body.
- Frontend payload should avoid sending raw abnormal health details as a
  defense-in-depth minimization layer.
- Edge Function must enforce redaction even if called directly.
- Rule-based local fallback may remain local UI behavior; it is not CVF proof.
- No direct provider SDK import or direct provider fallback may be introduced.

## Done Criteria

- [x] Frontend summary payload no longer sends raw abnormal `form.health`.
- [x] Edge Function replaces abnormal health details with a generic marker
  before building `currentNotes`.
- [x] Regression test proves raw abnormal health terms are absent from
  minimized notes.
- [x] `deno test` for the helper passes.
- [x] `deno check` for `generate-daily-summary/index.ts` passes.
- [x] Completion review records deployment proof remains pending.

## Evidence / Verification

Pre-implementation evidence:

- Source scan confirmed raw abnormal `form.health` was sent from
  `DailyReports.jsx`.
- Source scan confirmed the Edge Function could include raw abnormal health in
  `currentNotes`.

Post-implementation evidence:

- `deno test --no-lock supabase/functions/_shared/daily-summary-privacy.test.ts`
  passed: 2 tests, 0 failures.
- `deno check --node-modules-dir=auto --no-lock supabase/functions/generate-daily-summary/index.ts`
  passed.
- `npm run build` in the Maika workspace passed.
- Completion review filed at
  `docs/reviews/CVF_CDH_M_MAIKA_TEXT_SUMMARY_PRIVACY_CONTROLS_COMPLETION_2026-05-20.md`.

## Claim Boundary

This GC-018 authorizes privacy controls only. It does not claim live deployed
governance proof, Maika production readiness, governed child-data handling in
general, photo/vision governance, or closure of CDH-C/D/H.
