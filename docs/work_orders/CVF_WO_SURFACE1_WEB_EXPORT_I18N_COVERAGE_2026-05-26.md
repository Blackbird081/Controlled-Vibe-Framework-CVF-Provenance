# CVF Work Order Surface 1 Web Export I18n Coverage

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-26

---

## Purpose

Implement the bounded tranche authorized by:

`docs/baselines/CVF_GC018_SURFACE1_WEB_EXPORT_I18N_COVERAGE_2026-05-26.md`

## Scope / Target / Owner Boundary

Allowed owner files:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport*.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/template-i18n.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/template-i18n*.test.ts`
- completion/session/handoff docs

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

## Authority Chain

- Roadmap:
  `docs/roadmaps/CVF_SURFACE1_WEB_EXPORT_I18N_COVERAGE_ROADMAP_2026-05-26.md`
- GC-018:
  `docs/baselines/CVF_GC018_SURFACE1_WEB_EXPORT_I18N_COVERAGE_2026-05-26.md`
- Renderer trace:
  `docs/reviews/CVF_SURFACE1_WEB_EXPORT_RENDERER_TRACE_AND_LEAK_INVENTORY_2026-05-26.md`
- Surface Fidelity response:
  `docs/reviews/CVF_VI5_SURFACE_FIDELITY_CODEX_RESPONSE_2026-05-26.md`

## Agent Roles

- Orchestrator: enforce Surface 1 only and commit checkpoints.
- Implementer: make the smallest renderer/i18n changes that clean English
  packet chrome.
- I18n Reviewer: verify source values are preserved while template chrome is
  localized.
- Test Owner: add deterministic export generation/leak checks.
- Governance Auditor: ensure no provider, receipt, route, or workflow
  authority changes enter this tranche.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/baselines/CVF_GC018_SURFACE1_WEB_EXPORT_I18N_COVERAGE_2026-05-26.md`
- `docs/reviews/CVF_SURFACE1_WEB_EXPORT_RENDERER_TRACE_AND_LEAK_INVENTORY_2026-05-26.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/template-i18n.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/development.ts`

## Pre-Flight Checks

- Confirm worktree status.
- Confirm Surface 1 sample exports remain local-only and uncommitted.
- Confirm `SpecExport.tsx` is the renderer under test.
- Confirm existing template i18n helper coverage before adding new mapping.
- Confirm no live provider proof is necessary for renderer-only claims.

## Write Ownership

Implementation writes are limited to the listed Surface 1 renderer/i18n/test
files and continuity/evidence docs. Public-sync, provider, route, receipt,
workflow, and UI shell writes are not authorized.

## Execution Plan

1. Expose or harness deterministic Surface 1 markdown generation for tests.
2. Use localized template name/description in English export mode.
3. Add `app_builder_complete` English field labels and intent-pattern coverage.
4. Clean English full-mode protocol examples.
5. Add tests that assert:
   - English chrome has no unintended Vietnamese;
   - user-entered Vietnamese source values are preserved;
   - `vi` export mode remains Vietnamese.
6. Run focused tests and `npm run check`.
7. File completion review and update active session/handoff.

## Evidence Requirements

Required evidence:

- focused export/i18n tests PASS;
- `npm run check` PASS;
- no local sample export file committed;
- docs gates PASS;
- active state/front door/handoff updated after commit.

## Acceptance Criteria

- English `app_builder_complete` Surface 1 export uses English
  name/description.
- English User Input and Input Coverage labels are English.
- English Task/intent chrome is English.
- English full-mode protocol contains no Vietnamese examples.
- Vietnamese source values still appear as user/source values.
- The completion packet states this is not all-template i18n coverage.

## Review Gate

Before closure, verify:

- generated English export has clean English chrome for template metadata,
  field labels, intent chrome, and full-mode protocol;
- Vietnamese user-entered values remain present as source data;
- tests fail if Vietnamese chrome is reintroduced;
- no `/api/execute`, provider, receipt, workflow, or public-sync file changed.

## Operator Checkpoint

Operator review is not required before the bounded implementation begins
because the operator authorized processing the Surface 1 pivot. Operator review
is required after completion if the packet is used to re-open the Real
Non-Coder Usage Test verdict.

## Return-To-Orchestrator Conditions

Return blocked if implementation requires provider changes, route-contract
changes, all-template migration, semantic translation of user values, or hiding
source evidence to pass the leak detector.

## Closure Checklist

- [x] GC-018 filed
- [x] work order filed
- [x] implementation complete
- [x] focused deterministic tests PASS
- [x] `npm run check` PASS
- [x] completion review filed
- [x] active state/front door/handoff updated
- [x] commits created

## Claim Boundary

This work order authorizes only bounded Surface 1 English-mode export i18n
coverage for `app_builder_complete`. It does not authorize broad VI5-T3,
provider/runtime work, public-sync, hosted readiness, production readiness, or
freeze release.
