# CVF Internal Multi-Agent Work Transfer Packet - Surface 1 Form i18n Readiness Risk Gate Fix

Memory class: WORK_ORDER_RECORD

docType: work_order

Contract version: cvf.internalMultiAgentTransfer.ma1.v1

Date: 2026-05-26

Status: INTEGRATED

## Purpose

Dispatch the Surface 1 fix through the MA1 internal transfer packet so role
scope, evidence, and claim boundaries stay explicit.

## Scope / Target / Owner Boundary

Target: `app_builder_complete` Surface 1 web form and English Full / Guided
markdown export.

Allowed scope: bounded deterministic web/export source, focused tests, tranche
docs, and session state.

Forbidden scope: provider behavior, `/api/execute`, receipt envelopes, broad
all-template i18n, hosted PASS claim, production readiness, or public release
claim.

## Agent Roles

- Orchestrator: sequence docs, code, tests, commits, and public boundary.
- Implementer: patch bounded Surface 1 source.
- Reviewer: check i18n, source-value preservation, readiness, and risk gate.
- Auditor: enforce live-proof, public/provenance, and claim boundaries.
- Integrator: close completion packet and prepare operator retest.

## Required First Reads

- `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
- `docs/reviews/CVF_VI5_T4_T5_OPERATOR_WEB_EXPORT_HOLD_REVIEW_2026-05-26.md`
- `docs/concepts/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md`

## Pre-Flight Checks

- Surface target is Surface 1 web form/export, not Surface 2 server freeze.
- Template scope is `app_builder_complete`.
- Live provider proof is not required for deterministic renderer changes.

## Write Ownership

Owned writes are limited to bounded Surface 1 source/tests, this transfer
packet, tranche docs, active handoff, active session memory, active session
state, and public-safe sync copies after local verification.

## Execution Plan

1. Patch i18n field chrome and DynamicForm rendering.
2. Patch export risk detection and missing-label localization.
3. Verify readiness block retention.
4. Run focused tests and type check.
5. Commit private provenance, then public-sync if appropriate.

## Evidence Requirements

- Focused tests for template-i18n, governance-context, SpecExport, DynamicForm.
- `npm run check`.
- Session/handoff state updated.

## Acceptance Criteria

- English form chrome is English.
- Vietnamese form chrome remains Vietnamese.
- User-entered Vietnamese source values are preserved.
- English Full export contains readiness block.
- Ordinary English Full export no longer reports R2 > R1 warning.

## Review Gate

Reject if the patch translates user source values, expands beyond bounded
template scope, or claims hosted/external-agent PASS before operator retest.

## Closure Checklist

- [x] MA1 transfer packet used.
- [x] Source patches prepared.
- [x] Focused tests passed.
- [x] Type check passed.
- [x] Completion docs prepared.

## Return-To-Orchestrator Conditions

Return to orchestrator if hosted retest still shows Vietnamese chrome leakage,
missing readiness block, or risk-gate contradiction.

## Operator Checkpoint

Operator retests after public/hosted update by exporting a fresh English Full /
Guided packet and sending it to an external agent.

## 0. Surface Fidelity Gate

- Target surface: Surface 1 web form body and markdown export.
- Source code path or governed artifact path:
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/DynamicForm.tsx`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/template-i18n.ts`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governance-context.ts`
- Output artifact path or response field: web-rendered form body and
  downloaded/copied `cvf-spec-app_builder_complete-full.md`.
- Audience: non-coder operator and external agent receiving copy-paste.
- Language layer: Layer 2 Guided Wizard plus Layer 4 English export control.
- Generation trigger: operator toggles EN/VI, fills app-builder form, selects
  English Full / Guided export.
- Operator verdict, if any, references this same surface: yes, hosted web
  screenshots and exported files.
- Surface fidelity verdict: PASS.

## 1. Authority Chain

- Operator instruction: fix MA1 first, then fix i18n/readiness/risk gate and
  commit progress.
- Active session mode: `gamma_t1_t5_mcp_memory_bootstrap_closed_pass_bounded`.
- Active handoff: `AGENT_HANDOFF_V13_2026-05-25.md`.
- Governing roadmap:
  `docs/roadmaps/CVF_SURFACE1_FORM_I18N_READINESS_RISK_GATE_FIX_ROADMAP_2026-05-26.md`
- GC-018 baseline:
  `docs/baselines/CVF_GC018_SURFACE1_FORM_I18N_READINESS_RISK_GATE_FIX_2026-05-26.md`
- Work order:
  `docs/work_orders/CVF_WO_SURFACE1_FORM_I18N_READINESS_RISK_GATE_FIX_2026-05-26.md`
- Relevant standards:
  - `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
  - `docs/concepts/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md`
- Blocked work classes: provider behavior, receipt schema, broad all-template
  localization, hosted PASS claim, production readiness.

## 2. Transfer Objective

- Outcome required: deterministic Surface 1 form/export ready for operator
  retest.
- Why this role/lane is needed: operator found actual hosted EN/VI and export
  blockers after earlier local tests targeted only partial renderer paths.
- Definition of done: focused tests pass, type check passes, private commit
  records state, public-safe code is synced if appropriate.
- Non-goals: external-agent acceptance verdict, live provider proof, hosted
  deploy guarantee.

## 3. Source Packet

- Source artifacts to read: work order, HOLD review, DynamicForm, SpecExport,
  template-i18n, governance-context.
- Facts already established:
  - user-entered Vietnamese values are source evidence;
  - form field chrome should switch with EN/VI;
  - English export needs readiness block;
  - UI PASS and exported risk warning must not contradict.
- Assumptions allowed: deterministic local tests are sufficient for this code
  tranche.
- Assumptions forbidden: hosted deploy is current; external agent will PASS.
- User/operator values that must not be overwritten: all source values entered
  in the form.

## 4. Role Assignment

| Role lane | Actor/provider/client | Scope | Required output | Forbidden actions |
| --- | --- | --- | --- | --- |
| Orchestrator | Codex | Sequence docs/code/tests/commit | Updated session and commits | Claim operator PASS |
| Implementer | Codex | Patch bounded web/export code | Source changes and tests | Provider/API changes |
| Reviewer | Codex simulated role | Check i18n/readiness/risk consistency | Findings in completion | Re-audit operator verdict |
| Auditor | Codex simulated role | Check governance/proof boundary | Claim boundary | Public push from private repo |
| Integrator | Codex | Merge outputs and prepare retest | Completion packet | Hide unresolved issues |

Conflict-control method: one Codex instance wears multiple roles; conflict is
controlled by MA1 section gates, focused tests, and explicit claim boundary.

## 5. Execution Instructions

- Allowed writes: bounded web/export files, tests, docs, session state.
- Allowed commands: focused vitest, `npm run check`, git status/diff/commit,
  public-sync remote verification.
- Required tests: template-i18n, governance-context, SpecExport, DynamicForm.
- Live API/provider proof requirement: not required unless claiming provider
  governance behavior.
- Secret handling: do not print or copy API keys.
- Commit expectation: commit private tranche; public-sync after local pass if
  public-safe.
- Public/provenance boundary: never push from provenance repo to public origin.

## 6. Role Output Schema

Each role returns:

- Role name:
- Work performed:
- Evidence:
- Files changed or reviewed:
- Findings:
- Risks:
- Recommended disposition:
- Open questions:

## 7. Dissent And Review Ledger

| Issue | Role position | Counter-position | Evidence | Integrator disposition |
| --- | --- | --- | --- | --- |
| User values language | Preserve Vietnamese values | Translate to English for agent readability | Surface Fidelity SF4 exempts source values | ACCEPT preserve |
| Risk gate | Use user values for risk detection | Use full control intent text | Control text caused false R2 via "database" mention | ACCEPT user values |
| Scope | app_builder_complete only | all templates | Operator blocker is this surface | ACCEPT bounded |

## 8. Integration Decision

- Accepted findings: fix bounded form i18n, readiness block, risk detection.
- Rejected findings: all-template i18n and live provider proof.
- Deferred findings: hosted deploy and operator external-agent acceptance.
- Final implementation decision: proceed.
- Next allowed move: implement, verify, commit, public-sync if appropriate.

## 9. Completion Evidence

- Tests run: focused Surface 1 tests PASS, 4 files / 104 tests.
- Receipts or traces: not required.
- Screenshots or exported samples: operator will provide after retest.
- Commit SHA: pending private commit.
- Active session update: prepared.
- Handoff update: prepared.

## 10. Claim Boundary

This packet does not claim live subagent runtime, provider independence, hosted
readiness, production readiness, public release readiness, or operator
acceptance.

## Claim Boundary

This transfer packet is an internal control artifact only. It does not claim
live subagent runtime, provider behavior, hosted readiness, production
readiness, public release readiness, or operator acceptance.
