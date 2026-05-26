# CVF Surface 1 Web Export I18n Coverage Roadmap

Memory class: ROADMAP_RECORD

docType: roadmap

Date: 2026-05-26

Status: APPROVED_FOR_GC018_DISPATCH

---

## Purpose

Define the bounded tranche that fixes the real VI5 Surface Fidelity blocker:
English-mode Surface 1 web export markdown still contains unintended
Vietnamese chrome for `app_builder_complete`.

This roadmap supersedes any attempt to use the prior VI5-T3 Surface 2 portable
handoff convergence as the fix for the operator-held web export artifact.

## Authorization Or Decision

Authority chain:

- Operator accepted the Surface 1 pivot on 2026-05-26 and asked Codex to process
  all actionable parts through the multi-role workflow.
- Surface Fidelity correction:
  `docs/reviews/CVF_VI5_SURFACE_FIDELITY_CODEX_RESPONSE_2026-05-26.md`
- Renderer trace and leak inventory:
  `docs/reviews/CVF_SURFACE1_WEB_EXPORT_RENDERER_TRACE_AND_LEAK_INVENTORY_2026-05-26.md`
- Binding concept:
  `docs/concepts/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md`

Implementation requires the paired GC-018 and work order before code changes.

## Scope / Target / Owner Boundary

Owner surface:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/template-i18n.ts`
- focused `cvf-web` tests for export generation / i18n leak detection
- completion/session/handoff docs

Allowed:

- localize Surface 1 export template name/description for English mode;
- add trusted-template English field labels for `app_builder_complete`;
- add English export intent-pattern coverage for `app_builder_complete`;
- remove Vietnamese examples from English full-mode protocol chrome;
- add deterministic validator/test coverage for unintended-language chrome;
- preserve operator/user-entered Vietnamese values as source data.

Forbidden:

- provider adapter, provider routing, model registry, retry, or prompt changes;
- `/api/execute` response-contract changes;
- receipt envelope changes;
- workflow execution blocking;
- UI shell i18n beyond the export packet surface;
- all-template catalog migration;
- semantic translation of all user-entered values;
- external skill import;
- public-sync, hosted readiness, production readiness, or release claims.

## Non-Goals

This roadmap does not:

- implement broad VI5-T3 portable handoff readiness;
- localize the entire web UI shell;
- migrate every template to full bilingual catalogs;
- semantically translate all user-entered Vietnamese values;
- change provider prompts, provider adapters, route contracts, receipts, or
  workflow execution authority;
- prove hosted, public, production, or release readiness.

## Product Rule

English export mode means:

```text
English packet chrome and instructions
-> localized template metadata and field labels
-> preserved user source values
-> no unintended Vietnamese in agent-control text
```

Vietnamese source values are evidence, not leakage. Vietnamese template labels,
protocol text, headings, and template-authored intent prose are leakage when
the selected export language is English.

## Required Contract

Add a bounded Surface 1 validation/readout for tests and completion evidence.

Suggested contract version:

`cvf.surface1WebExportI18n.vi5.s1.v1`

Required proof fields:

- `surfaceId`: `surface_1_web_export_markdown`
- `templateId`
- `exportLanguage`
- `mode`
- `chromeLanguageTarget`
- `userSourceLanguageAllowed`
- `localizedTemplateMetadata`
- `localizedFieldLabels`
- `localizedIntentPattern`
- `unintendedLanguageLeakCount`
- `allowedSourceValueLeakCount`
- `status`: `pass` | `blocked`

The contract can live in tests/completion evidence if the implementation does
not need a runtime response field.

## Required Evidence / Verification

Deterministic verification:

```powershell
npm run test:run -- src/components/SpecExport*.test.tsx src/lib/template-i18n*.test.ts
npm run check
```

If no existing `SpecExport` test can generate the markdown directly, add a
small exported helper or deterministic renderer harness rather than relying on
manual copy/paste samples.

Live provider proof:

- Not required for the renderer/i18n fix because no AI governance/provider
  behavior is being claimed.
- If a future completion also claims `/api/execute` governance behavior, the
  mandatory live governance proof standard applies separately.

## Acceptance Criteria

1. English-mode `app_builder_complete` web export emits English template
   name/description.
2. English-mode User Input and Input Coverage use English field labels.
3. English-mode Task/intent chrome no longer starts with Vietnamese
   template-authored prose.
4. English full-mode protocol contains no Vietnamese confirmation examples.
5. User-entered Vietnamese values remain visible as source data.
6. Deterministic leak test distinguishes chrome leaks from allowed source data.
7. Prior VI5-T3 Surface 2 work remains on hold and is not claimed as the fix.

## Work Plan

1. Add/export a deterministic renderer harness for Surface 1 markdown if needed.
2. Wire English template name/description for `app_builder_complete`.
3. Add English field-label and intent-pattern coverage for
   `app_builder_complete`.
4. Remove Vietnamese examples from English full-mode protocol chrome.
5. Add leak detection assertions that distinguish chrome from user source data.
6. Run focused tests and `npm run check`.
7. File completion review and update active state/handoff.

## Verification / Evidence

Required evidence:

- focused Surface 1 export/i18n tests pass;
- `npm run check` passes;
- local `cvf-spec-*.md` samples remain uncommitted;
- completion packet states exact claim boundary.

## Rollback / Stop Conditions

Stop and return to operator if:

- the fix requires changing provider prompts or `/api/execute` contracts;
- clean English output would require semantic translation of user values;
- template localization cannot be bounded to trusted templates;
- tests can only pass by hiding user source data.

## Claim / Final / Verification Boundary

This tranche may claim Surface 1 English-mode export i18n coverage for the
audited `app_builder_complete` path only. It must not claim universal
multilingual CVF readiness, all-template i18n, hosted readiness, production
readiness, provider stability, or a governance freeze release.
