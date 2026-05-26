# CVF Surface 1 Form i18n Readiness Risk Gate Fix Completion

Memory class: REVIEW_RESULT_RECORD

docType: review

Date: 2026-05-26

Status: READY_FOR_OPERATOR_RETEST

## Purpose

Close the deterministic implementation for Surface 1 `app_builder_complete`
form-body i18n, Portable Agent Handoff Readiness retention, and risk-gate
consistency.

## Target / Source

Target:

- Surface 1 web form body and markdown export for `app_builder_complete`.

Source:

- Operator screenshot showing EN/VI toggle localized only the intro callout
  while the form body stayed Vietnamese.
- Operator-exported hosted markdown files showing missing readiness block and
  UI/export risk-gate contradiction.
- MA1 transfer packet:
  `docs/work_orders/CVF_MA1_TRANSFER_SURFACE1_FORM_I18N_READINESS_RISK_GATE_FIX_2026-05-26.md`

## Scope / Target / Owner Boundary

Implemented:

- English field chrome for `app_builder_complete`: labels, placeholders,
  hints, and examples.
- `DynamicForm` now renders localized template title, description, field
  chrome, example prefix, and preview intent based on selected UI language.
- `SpecExport` now localizes missing-required labels and evaluates exported
  governance risk from user-entered values instead of control text.
- Existing English Full / Guided export readiness block remains bounded to
  `app_builder_complete` + English + Full mode.

Not implemented:

- semantic translation of user-entered values;
- all-template i18n coverage;
- provider/API behavior;
- hosted deployment proof;
- external-agent PASS verdict.

## Scope / Methodology

Method:

- Read current Surface 1 renderer code.
- Applied MA1 control packet role split.
- Patched deterministic form/export source.
- Added focused regression tests covering form chrome language, source value
  preservation, readiness block retention, and risk-detection input source.
- Ran focused tests and type check.

## Evidence Trace Block

| Claim | Evidence |
| --- | --- |
| English form body is now localized for `app_builder_complete`. | `DynamicForm.test.tsx` verifies English title, description, labels, hints, examples, and absence of known Vietnamese chrome strings. |
| Vietnamese form body remains Vietnamese. | `DynamicForm.test.tsx` verifies Vietnamese labels, hints, and `VD:` example prefix. |
| User-entered Vietnamese values are preserved. | `DynamicForm.test.tsx` and `SpecExport.test.tsx` assert Vietnamese source values remain in preview/export. |
| English Full export readiness block remains present. | `SpecExport.test.tsx` asserts `Portable Agent Handoff Readiness`, `READY_FOR_EXTERNAL_AGENT_REVIEW`, and operator review gate content. |
| Risk-gate contradiction is corrected for ordinary sample. | `SpecExport.test.tsx` asserts exported governance detection receives user values, not control chrome containing `databases`, and passes R1/INTAKE state to the governance block. |
| Local deterministic verification passed. | `npm run test:run -- src/lib/template-i18n.test.ts src/lib/governance-context.test.ts src/components/SpecExport.test.tsx src/components/DynamicForm.test.tsx` PASS, 4 files / 104 tests; `npm run check` PASS. |

## Findings / Position

The root cause of the form i18n gap was that `DynamicForm` rendered template
metadata directly from the Vietnamese template registry. Prior export fixes
used `template-i18n.ts`, but the form body had no equivalent localized field
chrome path.

The root cause of the risk contradiction was that generated export governance
detection used the full English control intent. That control text mentions
hidden technical terms such as databases as things the non-coder should not
choose, causing a false R2 escalation in an Intake packet. The UI gate already
used user values; export now does the same.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| English UI still leaks Vietnamese chrome | Added field chrome map and DynamicForm regression tests. |
| User values get translated or lost | Tests assert Vietnamese source values remain. |
| Readiness block disappears again | Existing SpecExport regression retained and re-run. |
| UI PASS conflicts with packet risk warning | Export risk detection now uses user values, matching UI behavior for the ordinary sample. |
| Hosted site still stale | Public source is synced; hosted redeploy freshness remains separate, and operator retest is required after deploy. |

## Decision / Recommendation / Disposition

Decision: `READY_FOR_OPERATOR_RETEST`.

Disposition:

- Form-body i18n: `COMPLETE_BOUNDED`.
- Portable readiness retention: `COMPLETE_BOUNDED`.
- Risk-gate consistency: `COMPLETE_BOUNDED`.
- Final Surface 1 operator acceptance: `PENDING_OPERATOR_RETEST`.

Recommended next action: after hosted redeploy, operator exports a fresh English
Full / Guided spec from web and tests it with an external agent.

## Verification

Commands run from `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`:

```text
npm run test:run -- src/lib/template-i18n.test.ts src/lib/governance-context.test.ts src/components/SpecExport.test.tsx src/components/DynamicForm.test.tsx
```

Result: PASS, 4 files / 104 tests.

```text
npm run check
```

Result: PASS.

Public-sync verification:

- Remote verified:
  `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`
- Public commit: `b08af291`
  (`fix(web): localize app builder Surface 1 export gate`)
- Same focused test command: PASS, 4 files / 104 tests.
- Same `npm run check`: PASS.

## Public Catalog Disposition

Public catalog update: N/A for this private commit. This is a bounded web
Surface 1 defect fix and not a new proven public capability claim. Public-safe
code is synchronized in public commit `b08af291` so the hosted web surface can
be retested after deployment.

## Post-Review Risk Addendum

Risk 1 - hosted deployment gate:

- Public source is synced, but `vibcode.netlify.app` must be proven to serve a
  build containing public commit `b08af291` before operator retest can PASS.
- Netlify build logs showing `ENOENT` during trace copy for
  `app/(dashboard)/page_client-reference-manifest.js` are treated as a hosted
  deploy freshness blocker until deploy status and hosted asset content are
  verified.
- Required retest precondition: hosted form body in English mode shows English
  `app_builder_complete` chrome before exporting a fresh spec.

Risk 2 - MA1 first-use evidence:

- MA1 was used successfully as the control packet for this Surface 1 fix, but
  one use case is not enough to freeze the MA1 standard as mature.
- After two or three additional MA1-governed transfers, run a bounded
  retrospective to decide whether the MA1 schema needs refinement.

Risk 3 - template coverage boundary:

- This tranche only covers `app_builder_complete`.
- Other template families may still leak Vietnamese form body text in English
  mode and must not inherit this PASS claim.
- Follow-up should scale the same i18n/readiness/risk-gate pattern to the
  remaining high-value public templates only after hosted `app_builder_complete`
  retest is clean.

## Claim Boundary

This completion proves deterministic source/public-code readiness only. It does
not prove hosted deploy freshness, external-agent acceptance, provider
behavior, production readiness, public release readiness, or all-template i18n
coverage.
