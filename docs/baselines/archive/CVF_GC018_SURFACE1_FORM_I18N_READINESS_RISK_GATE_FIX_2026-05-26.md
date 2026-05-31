# CVF GC-018 Surface 1 Form i18n Readiness Risk Gate Fix

Memory class: BASELINE_RECORD

docType: baseline

Date: 2026-05-26

Status: APPROVED

## Purpose

Authorize the bounded Surface 1 form/export fix after the operator found that
the hosted EN/VI toggle localized only a small callout while the form body and
export gate still had blockers.

## Source / Predecessor Evidence

- `docs/reviews/CVF_VI5_T4_T5_OPERATOR_WEB_EXPORT_HOLD_REVIEW_2026-05-26.md`
- `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
- Operator screenshots from `vibcode.netlify.app/home` on 2026-05-26.
- Local source audit of `DynamicForm.tsx`, `SpecExport.tsx`,
  `template-i18n.ts`, and `governance-context.ts`.

## Decision / Baseline / Proposed Tranche

Baseline:

- Export i18n had partial local coverage.
- Dynamic form body still rendered hardcoded Vietnamese template metadata.
- Hosted English Full export had a readiness gap and risk-gate contradiction.

Proposed tranche:

- Complete bounded `app_builder_complete` form body i18n.
- Preserve readiness block.
- Align exported risk evaluation with UI gate for the ordinary non-coder
  app-builder sample.

## Scope / Target / Owner Boundary

Allowed changes:

- `DynamicForm.tsx`
- `SpecExport.tsx`
- `template-i18n.ts`
- `governance-context.ts`
- focused tests
- tranche docs and session state
- public-sync copy after private verification

Blocked changes:

- provider/model adapters;
- `/api/execute`;
- receipt envelopes;
- all-template i18n;
- semantic translation of source values;
- hosted deploy claim;
- external-agent PASS claim.

## Surface Fidelity Control Block

| Control | Result |
| --- | --- |
| Surface verified | Surface 1 web form and markdown export |
| Previous wrong target avoided | yes; not Surface 2 `englishSpecFreeze` |
| Audience verified | non-coder operator and external agent |
| Language invariant | English control chrome when English is selected; source values preserved |
| Operator test dependency | final PASS remains pending operator web export and external-agent review |

## Knowledge Absorption Blind-Spot Control Block

This tranche uses existing CVF source and operator samples; it does not absorb
new external knowledge.

| Control | Result |
| --- | --- |
| Prior absorption evidence resolved | MA1, Surface Fidelity rules, and T4/T5 HOLD review resolved |
| Detailed source files read | `DynamicForm.tsx`, `SpecExport.tsx`, `template-i18n.ts`, `governance-context.ts` |
| Accept/defer/reject dispositions | accept bounded app-builder fix; defer all-template localization and hosted acceptance |
| Adversarial role review | reviewer must reject user-value translation and risk-gate contradictions |
| Blind-spot delta | low; remaining blind spot is hosted deployment and operator external-agent verdict |

## Required Proof

- `npm run test:run -- src/lib/template-i18n.test.ts src/lib/governance-context.test.ts src/components/SpecExport.test.tsx src/components/DynamicForm.test.tsx`
- `npm run check`
- active session compatibility check after commit.

## Claim Boundary

This baseline authorizes deterministic web/export changes only. It does not
authorize provider behavior changes, hosted PASS, external-agent acceptance, or
production readiness.

## Evidence / Verification

Verification must be local deterministic tests and type check. Hosted/operator
acceptance remains a parked checkpoint after implementation.
