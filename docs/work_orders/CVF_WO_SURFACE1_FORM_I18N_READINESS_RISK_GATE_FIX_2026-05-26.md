# CVF Work Order Surface 1 Form i18n Readiness Risk Gate Fix

Memory class: WORK_ORDER_RECORD

docType: work_order

Date: 2026-05-26

Status: READY_FOR_OPERATOR_RETEST

## Purpose

Implement the bounded Surface 1 fix for `app_builder_complete` form body i18n,
Portable Agent Handoff Readiness, and risk-gate consistency.

## Authority Chain

Operator request -> MA1 internal transfer packet -> Surface Fidelity rules ->
GC-018 Surface 1 fix -> this work order.

## Agent Roles

| Role | Scope | Required output |
| --- | --- | --- |
| Orchestrator | Keep work bounded and sequence docs/code/tests/commit | Session updates and commit |
| Implementer | Patch form/export/i18n code | Focused source changes |
| Reviewer | Check source-value preservation and risk consistency | Findings in completion review |
| Auditor | Check live-proof boundary and public/provenance boundary | Claim boundary |
| Integrator | Prepare operator retest state | Completion packet and handoff |

## Required First Reads

- `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
- `docs/reviews/CVF_VI5_T4_T5_OPERATOR_WEB_EXPORT_HOLD_REVIEW_2026-05-26.md`
- `docs/concepts/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/DynamicForm.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx`

## Pre-Flight Checks

- Confirm target is Surface 1 web form/export.
- Confirm `app_builder_complete` only.
- Confirm deterministic local tests are sufficient; no live provider claim.

## Scope / Target / Owner Boundary

Files allowed:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/DynamicForm.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/template-i18n.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governance-context.ts`
- focused tests for the same surfaces
- tranche docs and session state.

Do not modify provider adapters, `/api/execute`, receipt schemas, live
benchmarks, or unrelated templates.

## Write Ownership

Owned writes are limited to bounded Surface 1 form/export source, focused
tests, docs, active handoff, active session state, and public-sync copies after
private verification.

## Execution Plan

1. Add full field-chrome localization helpers for `app_builder_complete`.
2. Wire DynamicForm to render localized template chrome by selected language.
3. Make generated export governance block use user values for risk detection.
4. Add focused tests.
5. Run tests and type check.
6. Commit private provenance and public-sync if appropriate.

## Tasks

- [x] Add app-builder field chrome i18n.
- [x] Wire DynamicForm localized rendering and preview intent.
- [x] Resolve risk-gate contradiction.
- [x] Verify readiness block remains present.
- [x] Add focused tests.
- [x] Run focused tests and `npm run check`.
- [x] Update completion/session/handoff.
- [ ] Commit private provenance.
- [ ] Sync public-safe code if local verification passes.

## Evidence Requirements

- Focused tests pass.
- Type check passes.
- Completion review cites no live provider proof needed.
- Operator retest remains parked.

## Acceptance Criteria

- English mode form body uses English chrome.
- Vietnamese mode form body remains Vietnamese.
- English Full export includes Portable Agent Handoff Readiness.
- Ordinary app-builder English Full export does not show R2 > R1 warning.
- User source values are preserved.

## Review Gate

Reject if the implementation translates user-entered values, broadens beyond
`app_builder_complete`, or claims hosted/external-agent PASS before operator
testing.

## Closure Checklist

- [x] Implementation complete.
- [x] Focused tests complete.
- [x] Type check complete.
- [x] Completion review prepared.
- [x] Active session state updated.
- [ ] Public-sync disposition recorded.

## Return-To-Orchestrator Conditions

Return if tests show language leakage, readiness block regression, risk-gate
contradiction, or unauthorized provider/runtime scope.

## Operator Checkpoint

After completion and hosted redeploy, operator exports a fresh English Full /
Guided spec and tests it with an external agent. Record `PASS`,
`PASS_WITH_MINOR_FIX`, or `HOLD`.

## Claim Boundary

Final claim before operator testing is deterministic readiness only.
