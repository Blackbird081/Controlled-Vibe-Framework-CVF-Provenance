# CVF CDH-M Maika Text-Summary Privacy Controls Completion

Memory class: SUMMARY_RECORD

Status: CLOSED_PRIVACY_CONTROLS_ONLY_DEPLOYED_PROOF_SEPARATE

docType: review

Reviewer: Codex

Date: 2026-05-20

GC-018:
`docs/baselines/CVF_GC018_CDH_M_MAIKA_TEXT_SUMMARY_PRIVACY_CONTROLS_2026-05-20.md`

Work order:
`docs/work_orders/CVF_WO_CDH_M_MAIKA_TEXT_SUMMARY_PRIVACY_CONTROLS_2026-05-20.md`

## Purpose

Record completion of the CDH-M redaction/minimization controls for abnormal
health values in the Maika text-summary path.

This completion closes the privacy-control gap only. It does not prove the
deployed Supabase Edge Function path, CVF live governance behavior, child-data
handling in general, photo handling, vision runtime, public claims, or bundled
CDH closure.

2026-05-20 update: the separate deployed-value proof is now filed at
`docs/reviews/CVF_CDH_M_MAIKA_TEXT_SUMMARY_DEPLOYED_VALUE_PROOF_2026-05-20.md`.
This packet remains the privacy-control closure packet.

## Scope / Target / Owner Boundary

In scope:

- Maika text-summary frontend payload minimization.
- Maika Edge Function health redaction before CVF request construction.
- Local regression evidence for the privacy helper.

Out of scope:

- Deployed Supabase invocation proof.
- CVF runtime/provider changes.
- Photo, vision, public-sync, or broad child-data proof.

Owner:

- Codex implemented and reviewed this privacy-control tranche.

## Target / Source Under Review

Changed Maika source:

- `../CVF-Workspace/Nha tre Maika/src/pages/admin/DailyReports.jsx`
- `../CVF-Workspace/Nha tre Maika/supabase/functions/generate-daily-summary/index.ts`
- `../CVF-Workspace/Nha tre Maika/supabase/functions/_shared/daily-summary-privacy.ts`
- `../CVF-Workspace/Nha tre Maika/supabase/functions/_shared/daily-summary-privacy.test.ts`

Governance sources:

- `docs/reviews/CVF_CDH_M_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- `docs/baselines/CVF_GC018_CDH_M_MAIKA_TEXT_SUMMARY_PRIVACY_CONTROLS_2026-05-20.md`
- `docs/work_orders/CVF_WO_CDH_M_MAIKA_TEXT_SUMMARY_PRIVACY_CONTROLS_2026-05-20.md`

## Scope / Methodology

The review checked whether raw abnormal health details could enter the CVF
`/api/execute` request body after implementation. It used source inspection,
targeted Deno helper tests, Edge Function typechecking, and Maika frontend
build verification.

## Implemented Controls

Maika sibling workspace changes:

- `supabase/functions/_shared/daily-summary-privacy.ts`
  - Adds `buildPrivacyBoundCurrentNotes()`.
  - Omits normal health values.
  - Replaces abnormal health details with a generic non-diagnostic marker:
    `Sức khỏe: Có ghi chú cần nhà trường theo dõi riêng; chi tiết không được gửi vào CVF.`
- `supabase/functions/_shared/daily-summary-privacy.test.ts`
  - Covers normal health omission.
  - Covers abnormal health redaction and verifies raw condition text and
    measurement detail are absent.
- `supabase/functions/generate-daily-summary/index.ts`
  - Imports the shared helper.
  - Builds `currentNotes` through the privacy-bounded helper before creating
    the CVF `/api/execute` request body.
  - Updates `readerGoal` to exclude sensitive health detail.
- `src/pages/admin/DailyReports.jsx`
  - Changes the summary payload from raw abnormal `form.health` to the generic
    marker `health_follow_up_present`.

## Findings / Position

Position: CLOSED_PRIVACY_CONTROLS_ONLY.

Findings:

1. The frontend no longer sends raw abnormal health values to the Edge
   Function.
2. The Edge Function enforces redaction again before the CVF request body is
   built, so direct Edge Function calls cannot bypass the minimization rule.
3. The local rule-based fallback remains outside CVF proof; it was not changed
   into a governance claim.
4. Deployed proof and CVF receipt/audit evidence remain pending.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Raw health detail leaks to CVF request body | Edge Function replaces abnormal health with a generic marker |
| Frontend sends raw health before Edge redaction | Frontend now sends `health_follow_up_present` only |
| Privacy-control closure overclaimed as live proof | Completion status explicitly keeps deployed proof pending |
| CDH-M used as child-data/photo/vision proof | Claim boundary forbids broader CDH claims |

## Evidence

Verification run in `d:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Nha tre Maika`:

```text
deno test --no-lock supabase/functions/_shared/daily-summary-privacy.test.ts
ok | 2 passed | 0 failed

deno check --node-modules-dir=auto --no-lock supabase/functions/generate-daily-summary/index.ts
Check supabase/functions/generate-daily-summary/index.ts

npm run build
vite build ... built
```

Static evidence:

- The frontend payload no longer sends raw abnormal health values to the Edge
  Function.
- The Edge Function redacts abnormal health even if called directly.
- No direct provider SDK or direct provider fallback was introduced.
- No photo, media, schema, auth, notification, parent portal, CVF runtime, or
  public-sync file was modified.

## Decision / Disposition

Disposition: CLOSED_PRIVACY_CONTROLS_ONLY.

CDH-M may now use abnormal-health entries in a later deployed text-summary
proof without sending raw health details to CVF, provided that proof still
records the minimization evidence and does not broaden into child-data,
photo, vision, direct-provider, or public-claim proof.

Remaining CDH-M gap:

- Deployed Supabase Edge Function invocation with authenticated admin/teacher
  session remains pending.
- CVF receipt/audit evidence for the deployed path remains pending.

## Claim Boundary

This packet claims only that redaction/minimization controls were implemented
and locally verified. It does not claim live governance proof or deployment
readiness.
