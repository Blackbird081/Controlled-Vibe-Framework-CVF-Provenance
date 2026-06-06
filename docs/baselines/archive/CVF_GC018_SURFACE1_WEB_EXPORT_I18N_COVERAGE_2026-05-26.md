# CVF GC-018 Surface 1 Web Export I18n Coverage

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_SURFACE1_WEB_EXPORT_I18N_COVERAGE

docType: baseline

Date: 2026-05-26

---

## Purpose

Authorize a bounded Surface 1 implementation tranche for English-mode web
export i18n coverage after the operator-held sample proved unintended
Vietnamese chrome in `app_builder_complete` export markdown.

## Scope / Target / Owner Boundary

Owner surface:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/template-i18n.ts`
- focused `cvf-web` component/lib tests
- Surface 1 completion/session/handoff docs

Allowed:

- localize English export chrome generated from template metadata;
- add English field-label and intent-pattern coverage for
  `app_builder_complete`;
- remove Vietnamese examples from English full-mode protocol;
- add deterministic leak tests for Surface 1 export;
- keep user-entered Vietnamese source values visible.

Forbidden:

- provider adapter/routing/model/retry/prompt changes;
- `/api/execute` response contract changes;
- receipt envelope changes;
- workflow execution blocking;
- UI shell i18n;
- all-template i18n migration;
- semantic translation of all user values;
- external skill import;
- public-sync, hosted readiness, production readiness, or release claims.

## Decision / Baseline / Proposed Tranche

Decision: authorize bounded implementation of Surface 1 web export i18n
coverage for the audited `app_builder_complete` English export path.

Baseline: Surface 1 English-mode sample contains unintended Vietnamese chrome
from raw template metadata, field labels, intent pattern, and English protocol
examples. Surface 2 VI5-T2 English freeze remains valid but does not fix this
surface.

Proposed tranche: localize the Surface 1 renderer for `app_builder_complete`,
add deterministic chrome-vs-source leak tests, and file a bounded completion.

## Source / Predecessor Evidence

- `docs/concepts/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md`
- `docs/reviews/CVF_VI5_SURFACE_FIDELITY_CODEX_RESPONSE_2026-05-26.md`
- `docs/reviews/CVF_SURFACE1_WEB_EXPORT_RENDERER_TRACE_AND_LEAK_INVENTORY_2026-05-26.md`
- `docs/roadmaps/CVF_SURFACE1_WEB_EXPORT_I18N_COVERAGE_ROADMAP_2026-05-26.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/template-i18n.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/development.ts`

## Surface Fidelity Control Block

- Surface under review:
  Surface 1 web export markdown from `SpecExport.tsx`.
- Artifact family:
  downloadable/copyable markdown packet, not `/api/execute` T2
  `englishSpecFreeze`.
- Target user:
  non-coder and external AI/agent receiving the copied packet.
- Target language:
  English export mode.
- Verified source:
  `docs/reviews/CVF_SURFACE1_WEB_EXPORT_RENDERER_TRACE_AND_LEAK_INVENTORY_2026-05-26.md`
- Blocking confusion to prevent:
  treating Surface 2 T2 English-freeze success as proof that Surface 1 web
  export markdown is clean.
- Verdict:
  CLEAR_FOR_SURFACE1_I18N_IMPLEMENTATION.

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - operator authority / surface fidelity concept: 1 concept file
  - Codex Surface Fidelity response: 1 review file
  - renderer trace and leak inventory: 1 review file
  - current renderer and template i18n files: 2 source files
  - current template definition: 1 source file
- Prior absorption evidence resolved:
  - VI5-T2 is accepted for Surface 2 only.
  - VI5-T3 portable handoff readiness is useful but wrong-target for the
    operator HOLD blocker.
  - Surface Fidelity Gate is now mandatory before convergence/implementation.
- Detailed source files used:
  - `docs/concepts/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md`
  - `docs/reviews/CVF_VI5_SURFACE_FIDELITY_CODEX_RESPONSE_2026-05-26.md`
  - `docs/reviews/CVF_SURFACE1_WEB_EXPORT_RENDERER_TRACE_AND_LEAK_INVENTORY_2026-05-26.md`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/template-i18n.ts`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/development.ts`
- Source families skipped:
  - `.private_reference/legacy/`: skipped because this tranche fixes an
    already identified renderer/i18n defect, not external knowledge intake.
  - provider/model/live-run evidence: skipped because provider behavior is out
    of scope.
- File-level accepted value:
  - `SpecExport.tsx` is the primary Surface 1 owner.
  - `template-i18n.ts` has partial reusable English metadata coverage.
  - `development.ts` proves `app_builder_complete` raw template text is
    Vietnamese.
- Owner-surface normalization:
  - all accepted value normalizes into Surface 1 web export renderer/tests.
- Accept/defer/reject matrix:
  - ACCEPT_NOW: `app_builder_complete` English export metadata, labels, and
    intent-pattern coverage.
  - ACCEPT_NOW: deterministic chrome-vs-source leak test.
  - DEFER_DEMAND_GATED: all-template i18n migration.
  - DEFER_DEMAND_GATED: UI shell i18n.
  - DEFER_DEMAND_GATED: Surface 2 VI5-T3 portable handoff readiness.
  - REJECT_DIRECT: provider prompt tuning as the fix.
  - REJECT_DIRECT: translating/hiding user source values to pass a leak test.
- Adversarial roles completed:
  - Implementer: smallest fix is renderer localization plus tests.
  - Skeptic/Auditor: root risk is fake-clean output that simply omits source.
  - Product/Operator Advocate: English packet chrome must be clean enough to
    copy to another agent without user interpretation.
  - Boundary Owner: no provider, route, receipt, or workflow behavior change.
- Thin proof target:
  deterministic generated export proof for English-mode
  `app_builder_complete`.
- Blind-spot verdict:
  CLEAR.

## Required Evidence / Verification

Required deterministic verification:

```powershell
npm run test:run -- src/components/SpecExport*.test.tsx src/lib/template-i18n*.test.ts
npm run check
```

If the exact test filenames differ, the implementer must record the focused
files actually run and explain the substitution.

Live proof:

- Not required unless a later claim asserts live provider or governance
  behavior.
- If a live proof is run anyway, apply the Mandatory Live Run Diagnostics
  standard before any rerun.

## Claim Boundary

Completion may claim only bounded Surface 1 English-mode export i18n coverage
for the audited `app_builder_complete` path. Completion must not claim
universal multilingual readiness, all-template i18n, provider stability,
hosted/public/production readiness, or freeze release.
