# CVF VI5-T2 Spec English Freeze Completion

Memory class: SUMMARY_RECORD

docType: review

Status: CLOSED_PASS_BOUNDED

Date: 2026-05-25

---

## Scope

VI5-T2 implemented the bounded Spec English Freeze tranche authorized by:

- `docs/baselines/CVF_GC018_VI5_T2_SPEC_ENGLISH_FREEZE_2026-05-25.md`
- `docs/work_orders/CVF_WO_VI5_T2_SPEC_ENGLISH_FREEZE_2026-05-25.md`

## Purpose

Close VI5-T2 with evidence that `/api/execute` now emits a validator-backed
English Spec freeze artifact while preserving the original Vietnamese source
prompt as evidence.

## Target / Source

Target owner surface:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-english-freeze.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-english-freeze.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vi5-language-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vi5-language-readout.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.vi5-t1-language-state.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.vi5-t1-language-state.alibaba.live.test.ts`

Primary sources:

- VI5-T1 completion
- VI5-T2 roadmap and GC-018
- L1 `specFirstMediation`
- VI5 layered language architecture

## Evidence Trace Block

- Claim: VI5-T2 should not treat the mixed L1 Spec body as the product target.
- Source read:
  `docs/reviews/CVF_VI5_T1_LANGUAGE_STATE_AND_STRATEGY_GUIDED_CATALOG_COMPLETION_2026-05-25.md`
- Result: VI5-T1 recorded `observedSpecBodyLanguage=mixed` and
  `englishFreezeEnforced=false`.
- Verdict: EXISTS; T2 addresses that boundary.
- Counter-evidence: none.

- Claim: a frozen English Spec must preserve Vietnamese source prompt evidence
  without embedding raw Vietnamese source text inside the frozen body.
- Source read:
  `docs/roadmaps/CVF_VI5_T2_SPEC_ENGLISH_FREEZE_ROADMAP_2026-05-25.md`
- Result: implementation emits `englishSpecFreeze.sourceEvidenceRef` while
  the frozen body references `specFirstMediation.originalPrompt` and
  `request.inputs`.
- Verdict: IMPLEMENTED.
- Counter-evidence: semantic translation of every source value is not claimed.

- Claim: `specBoundary.englishFreezeEnforced=true` must be validator-backed.
- Source read:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-english-freeze.ts`
- Result: `status=frozen` requires English-only body, required sections,
  source evidence separation, and original prompt preservation.
- Verdict: IMPLEMENTED.
- Counter-evidence: this is response-level freeze artifact validation, not a
  broad governance freeze release.

## Delivered

- Added `cvf.englishSpecFreeze.vi5.t2.v1`.
- Added canonical English Spec freeze builder.
- Added validator for English-only body, required sections, source evidence
  separation, and source prompt preservation.
- Added `/api/execute` response field `englishSpecFreeze`.
- Updated `specBoundary.frozen`, `specBoundary.englishFreezeEnforced`, and
  `specBoundary.frozenAt` from the T2 validator-backed freeze state.
- Preserved `specBoundary.observedSpecBodyLanguage=mixed` for the L1 body
  audit signal.
- Updated deterministic and live proof tests.

## Findings / Position

PASS bounded.

The important product correction is separation of two facts:

```text
L1 normalizedExecutionSpec observed body: mixed
T2 frozen English Spec artifact: frozen
```

This means CVF no longer has to pretend the existing L1 body is fully English.
It can preserve that audit signal and still provide a copy-ready English
handoff contract for agents.

## Risk / Corrective Action

Residual risk: T2 does not semantically translate every Vietnamese source value
into English. It freezes an English control artifact and references source
evidence for user-specific facts. If non-coder review shows agents need every
source value translated into English inside the frozen body, that requires a
later bounded translation/confirmation tranche.

Corrective action: do not expand this into broad prompt tuning. Open a later
tranche only if operator/non-coder review proves the source-reference model is
insufficient.

## Evidence

Focused tests:

- `npm run test:run -- src/lib/spec-english-freeze.test.ts src/lib/vi5-language-readout.test.ts src/lib/spec-first-mediation.test.ts src/app/api/execute/route.vi5-t1-language-state.test.ts src/app/api/execute/route.test.ts`
- Result: PASS 5 files / 45 tests

TypeScript:

- `npm run check` PASS

Live proof:

- Command: `npm run test:run -- src/app/api/execute/route.vi5-t1-language-state.alibaba.live.test.ts`
- Result: PASS 1/1
- Provider/model: `alibaba/qwen-turbo`
- Receipt: `rcpt-env-mpl6equw-qdarbu`
- `englishSpecFreeze.status`: `frozen`
- `observedSpecBodyLanguage`: `mixed`
- `englishFreezeEnforced`: `true`
- `rawSecretPrinted`: `false`

Route/file-size posture:

- `/api/execute/route.ts`: 1000 lines

## Claim Boundary

VI5-T2 proves only response-level English Spec freeze artifact generation and
validation for the tested Strategy path.

It does not prove universal translation quality, all workflow packs, UI shell
i18n, provider/model stability, provider adapter changes, broad prompt tuning,
receipt envelope changes, workflow execution blocking, hosted readiness,
public readiness, production readiness, runtime multi-agent scheduling, live
subagent isolation, or broad governance freeze release.

## Decision / Recommendation / Disposition

Decision: close VI5-T2 as `CLOSED_PASS_BOUNDED`.

Recommendation: pause for operator/non-coder review of the T2 frozen Spec
artifact. Do not start full semantic translation unless the source-reference
model fails review.

Disposition: completed and ready for operator review.
