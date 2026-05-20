# CVF Work Order — CDH-M Maika Text-Summary Privacy Controls

Memory class: SUMMARY_RECORD

Status: CLOSED

GC-018:
`docs/baselines/CVF_GC018_CDH_M_MAIKA_TEXT_SUMMARY_PRIVACY_CONTROLS_2026-05-20.md`

## Authority Chain

- Operator request, 2026-05-20.
- CDH-M rebuttal:
  `docs/reviews/CVF_CDH_M_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- GC-018 baseline:
  `docs/baselines/CVF_GC018_CDH_M_MAIKA_TEXT_SUMMARY_PRIVACY_CONTROLS_2026-05-20.md`

## Agent Roles

- Operator: authorizes the privacy-control tranche.
- Codex: implements the bounded controls and files completion evidence.
- Future reviewer/operator: must not infer deployed proof from this closure.

## Purpose

Implement the redaction/minimization controls required by the CDH-M
`NON_BLOCKING_WITH_PRIVACY_GATE` verdict.

## Scope

Allowed scope:

- Maika text-summary frontend payload helper.
- Maika `generate-daily-summary` Edge Function.
- A small shared privacy helper and Deno regression test.
- Completion review in the provenance repo.

Forbidden scope:

- Live deployed Supabase proof.
- CVF runtime/provider changes.
- Direct provider fallback.
- Photo, image, or vision work.
- Child-data proof beyond this minimized text-summary path.
- Public-sync claim changes.

## Required First Reads

- `docs/reviews/CVF_CDH_M_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `../CVF-Workspace/Nha tre Maika/supabase/functions/generate-daily-summary/index.ts`
- `../CVF-Workspace/Nha tre Maika/src/pages/admin/DailyReports.jsx`

## Pre-Flight Checks

Completed before implementation:

- Confirmed the Maika Edge Function already existed.
- Confirmed the frontend sent raw abnormal `form.health` in summary payload.
- Confirmed the Edge Function could place raw abnormal health into
  `currentNotes`.
- Confirmed the requested work is privacy controls only, not deployed proof.

## Write Ownership

Codex owns only the files named in this work order and the matching GC-018.
No CVF runtime/provider, public-sync, photo, vision, schema, auth, or
notification file is in scope.

## Execution Plan

1. Create a shared privacy helper for summary-note minimization.
2. Route Edge Function `currentNotes` through that helper.
3. Minimize the frontend health payload to a generic marker.
4. Add regression tests for normal-health omission and abnormal-health
   redaction.
5. Run targeted Deno checks and Maika build.
6. File completion review and update session continuity.

## Tasks

1. Add a shared Maika helper that builds privacy-bounded notes.
2. Ensure abnormal health values are replaced with a generic non-diagnostic
   marker before the CVF request body is built.
3. Change the frontend summary payload so raw abnormal health values are not
   sent to the Edge Function.
4. Add Deno regression coverage proving raw abnormal health text is not present
   in `currentNotes`.
5. Run targeted Deno verification.
6. File a completion review and update active continuity surfaces.

## Acceptance Criteria

- [x] Raw values such as `Sốt nhẹ`, `Ho`, `Đau bụng`, or `Dị ứng` are not sent
  in the CVF `/api/execute` body.
- [x] A generic marker indicates that a health follow-up exists without naming
  the condition.
- [x] Tests cover normal-health omission and abnormal-health redaction.
- [x] Deployed proof remains explicitly pending.

## Evidence Requirements

Completion evidence must include:

- Maika changed paths.
- Deno helper test result.
- Deno Edge Function typecheck result.
- Maika build result.
- Explicit statement that deployed proof remains pending.

## Review Gate

The work is closeable only if raw abnormal health values are not present in
the CVF request body construction path and no broader CDH claim is introduced.

## Closure Checklist

- [x] Shared privacy helper added.
- [x] Frontend payload minimized.
- [x] Edge Function request body path redacts abnormal health.
- [x] Targeted tests/checks/build pass.
- [x] Completion review filed.
- [x] Continuity state updated.

## Return-To-Orchestrator Conditions

Return to operator/reviewer without closing if:

- Edge Function cannot be typechecked.
- Redaction cannot be enforced inside the Edge Function.
- The requested proof requires raw child health details.
- Any implementation path would require photo, vision, direct-provider, CVF
  runtime, or public-sync changes.

## Claim Boundary

This work order closes the redaction/minimization control gap only. It does not
prove the deployed Maika integration or any broader child-data/photo/vision
governance claim.
