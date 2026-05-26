# CVF Surface 1 Web Export Renderer Trace And Leak Inventory

Memory class: REVIEW_RECORD

Status: TRACE_COMPLETE_RECOMMENDS_SURFACE1_I18N_TRANCHE

docType: review

Date: 2026-05-26

---

## Purpose

Trace the actual Surface 1 web export renderer behind the operator-held
`cvf-spec-app_builder_complete-full 2.md` sample and classify the English-mode
Vietnamese leaks before any implementation resumes.

This review answers the Surface Fidelity question left open after VI5-T3:
the prior English Spec reliability claim was verified for Surface 2
`englishSpecFreeze`, not for Surface 1 downloadable web export markdown.

## Scope / Target / Owner Boundary

Target surface: Surface 1 web export markdown generated inside `cvf-web`.

Owner boundary: trace and dispatch preparation only. This review does not edit
the renderer, does not use live provider keys, and does not claim a fixed
export.

## Target / Source

Target artifact:

- `cvf-spec-app_builder_complete-full 2.md` local operator sample

Source files:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/template-i18n.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/development.ts`

## Scope / Methodology

Method:

1. Identify the web export markdown renderer.
2. Compare generated sample lines with renderer source lines.
3. Separate template/UI chrome from user-entered source values.
4. Record accepted, deferred, and rejected implementation directions.

## Multi-Role Audit

- Orchestrator: prevent another VI5 convergence loop from targeting the wrong
  surface.
- Surface Fidelity Auditor: bind the observed artifact to its source renderer.
- Renderer Owner: identify the exact code paths that emit leaked chrome.
- I18n Reviewer: separate template/UI chrome leaks from valid user source data.
- Product / Non-Coder Advocate: preserve the operator's HOLD verdict without
  re-auditing it by persona simulation.
- Governance Auditor: keep this as trace and dispatch preparation only; no
  provider/API proof claim is made here.

## Surface Fidelity Gate

| Field | Value |
| --- | --- |
| Surface ID | Surface 1 |
| Surface name | Web export markdown spec |
| Actual artifact | `cvf-spec-app_builder_complete-full 2.md` |
| User-selected language | English export mode |
| Primary renderer | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx` |
| Renderer function | `generateSpec()` |
| Target audience | Non-coder copying a packet to an external AI/agent |
| Verdict | Surface 1 English export is not clean; Surface 2 T2 cannot be used as the fix |

## Renderer Trace

Primary renderer:

- `SpecExport.tsx` imports template data and renders the copy/download markdown
  packet in `generateSpec()`.
- `generateSpec()` correctly switches fixed section labels with
  `labels = lang === 'vi' ? ... : ...`.
- However, it also emits raw template fields that are still Vietnamese:
  `template.name`, `template.description`, `template.fields[].label`, and
  `template.intentPattern`.
- The existing English localization helper
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/template-i18n.ts`
  already contains English name/description for `app_builder_complete`, but
  `SpecExport.tsx` does not use it.

Primary cause points:

- `SpecExport.tsx:660-663` uses `field?.label || key` for User Input labels.
- `SpecExport.tsx:753-756` uses `field.label` for Input Coverage rows.
- `SpecExport.tsx:764`, `771`, and `773` emit raw template name/description.
- `SpecExport.tsx:738` renders raw `template.intentPattern`.
- `SpecExport.tsx:181-183` contains Vietnamese confirmation examples inside
  the English full-mode protocol.
- `templates/development.ts:60-120` defines `app_builder_complete` name,
  description, field labels, and intent pattern in Vietnamese.

Secondary note:

- `src/lib/templates/index.ts` has an older complete-spec generator pattern
  that also uses raw template metadata. It was not identified as the current
  operator sample renderer, but should not be treated as proof of Surface 1
  cleanliness.

## Leak Inventory

Observed English-mode sample: `cvf-spec-app_builder_complete-full 2.md`.

| Sample line(s) | Leak type | Source cause | Disposition |
| --- | --- | --- | --- |
| 4, 11 | Template title chrome | raw `template.name` | FIX in Surface 1 renderer |
| 13 | Template description chrome | raw `template.description` | FIX in Surface 1 renderer |
| 27-33 | User Input field-label chrome | raw `template.fields[].label` | FIX with field-label localization |
| 42-48 | Input Coverage field-label chrome | raw `template.fields[].label` | FIX with field-label localization |
| 56 | Task/intent chrome | raw `template.intentPattern` Vietnamese intro | FIX with English intent pattern/override |
| 58, 62, 65, 68, 71, 114, 117 | User/source values | operator-entered Vietnamese values | PRESERVE, do not translate by default |
| 249-250 | Protocol chrome | English full-mode protocol includes Vietnamese confirmation examples | FIX in English protocol text |

Important distinction:

- Vietnamese user-entered business values are valid source data and should be
  preserved unless a separate semantic translation feature is explicitly
  authorized.
- Vietnamese fixed labels, template metadata, protocol instructions, and
  template-authored intent prose are Surface 1 i18n coverage gaps when the
  export language is English.

## Diagnosis

The root cause is deterministic renderer/i18n coverage, not provider/model
behavior. No API key is needed to prove this trace.

The Surface 1 English export currently has partial i18n:

- fixed packet headings and CVF governance sections switch to English;
- template metadata and template-authored workflow text remain Vietnamese;
- user source values are preserved, as they should be.

Therefore, a clean English Surface 1 export requires renderer-level i18n
coverage for the selected template, plus a validator that can distinguish
chrome leakage from source data.

## Findings / Position

Position: Surface 1 English-mode export is not yet reliable. The right fix is a
bounded Surface 1 renderer/i18n tranche, not a rerun of VI5-T3 Surface 2
handoff readiness.

Key findings:

- Surface 1 has partial English chrome but raw Vietnamese template metadata.
- Existing `template-i18n.ts` can be reused for name/description but is not
  currently wired into `SpecExport.tsx`.
- Field labels and intent patterns need explicit English coverage.
- User-entered Vietnamese values should remain visible as source evidence.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Wrong target repeats | Require Surface Fidelity Gate before implementation |
| Fake-clean export hides source values | Validator must allow source values while blocking chrome leaks |
| Scope expands into all-template i18n | Limit first proof to audited `app_builder_complete` path |
| Provider/model work is mistaken as fix | Keep route/provider/prompt changes forbidden |

## Recommended Corrective Scope

Open a fresh Surface 1 web export i18n coverage tranche.

Minimum implementation should:

1. Localize template name/description in `SpecExport.tsx` using existing
   `template-i18n` helpers.
2. Add trusted-template English field-label coverage for `app_builder_complete`.
3. Add an English intent-pattern/export override for `app_builder_complete`.
4. Remove Vietnamese confirmation examples from the English full-mode protocol.
5. Add deterministic validation that reports unintended-language chrome leaks
   while allowing user-entered source values.
6. Prove the sample class with a generated English-mode export test.

## Out Of Scope

- Do not dispatch the prior VI5-T3 portable handoff readiness implementation
  as the fix for this blocker.
- Do not translate user-entered Vietnamese values by default.
- Do not change `/api/execute`, provider prompts, provider adapters, receipt
  envelopes, or workflow execution authority for this renderer fix.
- Do not claim all-template English export coverage from a single
  `app_builder_complete` proof.
- Do not use local sample exports as committed evidence files.

## Decision / Recommendation / Disposition

Decision: recommend dispatch of a fresh Surface 1 web export i18n coverage
roadmap/GC-018/work order.

Disposition:

- ACCEPT: Surface 1 renderer trace and leak inventory.
- ACCEPT: bounded `app_builder_complete` export-i18n implementation.
- DEFER: all-template i18n and broader VI5-T3 handoff readiness.
- REJECT: provider prompt/model tuning as the fix.

## Claim Boundary

This packet proves source trace and leak classification only. It does not prove
the renderer has been fixed, does not prove live governance behavior, and does
not modify runtime provider behavior.
