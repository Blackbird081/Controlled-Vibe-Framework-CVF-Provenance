# CVF Surface 1 Form i18n Readiness Risk Gate Fix Roadmap

Memory class: ROADMAP_RECORD

docType: roadmap

Date: 2026-05-26

Status: AUTHORIZED_FOR_IMPLEMENTATION

## Purpose

Fix the hosted Surface 1 `app_builder_complete` blockers reported by the
operator:

1. English UI toggle does not localize the form body.
2. English Full / Guided export must contain Portable Agent Handoff Readiness.
3. UI Spec Gate PASS must not contradict the exported governance risk block.

This tranche uses MA1 as the internal multi-agent transfer control packet.

## Authorization / Decision

Decision: proceed with a bounded deterministic web/export fix for Surface 1.

Operator will retest after completion by exporting a fresh spec from web and
sending it to an external agent.

## Scope / Target / Owner Boundary

Target surface:

- Surface 1 web form and markdown export for `app_builder_complete`.

In scope:

- English localization for `app_builder_complete` form labels, hints,
  placeholders, examples, title, description, and preview intent;
- preservation of user-entered Vietnamese values as source evidence;
- English Full / Guided export readiness block;
- risk gate consistency between UI auto-detect and exported governance block;
- focused tests and local type check;
- public-sync update if local verification passes and changes are public-safe.

Out of scope:

- semantic translation of user-entered values;
- all-template i18n coverage;
- provider/model route behavior;
- `/api/execute` behavior;
- receipt schema changes;
- live external-agent acceptance verdict;
- hosted deployment guarantee.

## Non-Goals

This tranche does not certify that every external agent will build correctly,
does not introduce runtime subagent scheduling, and does not claim production
readiness. It prepares a deterministic web/export surface for the operator's
next manual acceptance test.

## Surface Fidelity Gate

| Field | Value |
| --- | --- |
| Source code path | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/DynamicForm.tsx`, `SpecExport.tsx`, `template-i18n.ts`, `governance-context.ts` |
| Output artifact | rendered web form body and downloaded/copied `cvf-spec-app_builder_complete-full.md` |
| Audience | non-coder operator and external agent receiving copy-paste |
| Language layer | Layer 2 Guided Wizard plus Layer 4 English control packet inside export |
| Generation trigger | user toggles EN/VI, fills `app_builder_complete`, selects English Full / Guided export |
| Operator verdict path | operator screenshots and exported files from hosted `vibcode.netlify.app/home` |

## Work Plan

1. Add missing template field chrome localization for `app_builder_complete`.
2. Wire DynamicForm to use localized template presentation without mutating
   user-entered values.
3. Align export governance detection with UI gate by evaluating user values
   rather than English control instructions that mention hidden technical terms.
4. Verify Portable Agent Handoff Readiness is present in English Full export.
5. Add focused tests and run local checks.
6. Update private session state and public-sync if appropriate.

## Work Packages

### T2-A Form Body i18n

Deliver English localized labels, hints, placeholders, examples, title,
description, and preview intent for `app_builder_complete`.

### T2-B Readiness Block

Ensure English Full / Guided export includes Portable Agent Handoff Readiness
and source-value handling.

### T2-C Risk Gate Consistency

Ensure UI Spec Gate PASS does not coexist with exported `Risk Level R2` /
`Max Risk R1` warning for the ordinary `app_builder_complete` non-coder
brief case.

## Evidence Plan

Required:

- focused tests for `template-i18n`, `DynamicForm`, `SpecExport`, and
  `governance-context`;
- `npm run check`;
- active session compatibility check.

Live provider/API proof is not required because this tranche changes
deterministic form/export behavior and does not claim provider governance
behavior.

## Acceptance Criteria

- English UI mode shows English `app_builder_complete` form chrome.
- Vietnamese UI mode still shows Vietnamese form chrome.
- User-entered Vietnamese values are preserved, not translated.
- English Full export contains Portable Agent Handoff Readiness.
- English Full export for the ordinary app-builder sample shows risk valid for
  Intake/R1 rather than an R2 > R1 warning.
- Public-safe code changes are ready for hosted redeploy.

## Stop Conditions

Stop if the fix requires provider/adapter changes, changes user-entered values,
or broadens all-template localization without a new tranche.

## Claim Boundary

This roadmap may claim only deterministic Surface 1 form/export readiness for
operator retest. It does not claim external-agent PASS, hosted deployment,
provider behavior, production readiness, or public release readiness.
