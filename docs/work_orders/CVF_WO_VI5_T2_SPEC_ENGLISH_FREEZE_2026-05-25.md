# CVF Work Order VI5-T2 Spec English Freeze

Memory class: SUMMARY_RECORD

Status: OPEN_AUTHORIZED

docType: work_order

Date: 2026-05-25

---

## Purpose

Implement the bounded VI5-T2 tranche authorized by:

`docs/baselines/CVF_GC018_VI5_T2_SPEC_ENGLISH_FREEZE_2026-05-25.md`

## Scope / Target / Owner Boundary

Allowed owner files:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-english-freeze.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-english-freeze.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vi5-language-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vi5-language-readout.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.vi5-t1-language-state.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.vi5-t1-language-state.alibaba.live.test.ts`
- VI5-T2 completion/session/handoff files

Forbidden:

- provider adapter/routing/model changes;
- broad prompt tuning;
- receipt envelope changes;
- workflow execution blocking;
- UI shell i18n;
- all-pack catalog expansion;
- external skill import;
- public-sync, hosted readiness, production readiness, or release claims.

## Authority Chain

- Human operator authorized proceeding on 2026-05-25 after accepting that mixed
  Spec body is not the product target.
- Roadmap:
  `docs/roadmaps/CVF_VI5_T2_SPEC_ENGLISH_FREEZE_ROADMAP_2026-05-25.md`
- GC-018:
  `docs/baselines/CVF_GC018_VI5_T2_SPEC_ENGLISH_FREEZE_2026-05-25.md`
- VI5-T1 completion:
  `docs/reviews/CVF_VI5_T1_LANGUAGE_STATE_AND_STRATEGY_GUIDED_CATALOG_COMPLETION_2026-05-25.md`

## Agent Roles

- Orchestrator: enforce T2 scope and commit checkpoints.
- Implementer: add additive freeze code/readout only.
- Reviewer: check fake-English claims and source evidence preservation.
- Auditor: run deterministic tests, live proof, docs gates, and handoff sync.
- Operator: reviews product meaning after closure.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/baselines/CVF_GC018_VI5_T2_SPEC_ENGLISH_FREEZE_2026-05-25.md`
- `docs/roadmaps/CVF_VI5_T2_SPEC_ENGLISH_FREEZE_ROADMAP_2026-05-25.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-first-mediation.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vi5-language-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`

## Pre-Flight Checks

- Confirm worktree status.
- Confirm VI5-T1 completion and current route readout location.
- Confirm route line-count guard posture before editing.
- Confirm live key loading path before any live proof.
- Confirm no provider adapter/routing/model file needs to change.

## Write Ownership

Implementation writes are limited to the listed `cvf-web` lib/route/test
surfaces and VI5-T2 continuity/evidence docs. No public-sync write is
authorized in this work order.

## Execution Plan

1. Add `spec-english-freeze.ts` with a canonical English Spec builder and
   validator.
2. Extend VI5 language readout so `specBoundary` reflects freeze validation.
3. Wire `englishSpecFreeze` into `/api/execute` response.
4. Add focused unit, route, and live proof assertions.
5. Run deterministic verification and one live proof.
6. File completion review and update active session/handoff.

## Evidence Requirements

Required evidence:

- focused unit/route tests PASS;
- `npm run check` PASS;
- one live Vietnamese Strategy proof PASS with receipt;
- docs gates PASS;
- active handoff updated after final commit.

## Acceptance Criteria

- `englishSpecFreeze` is emitted by `/api/execute`.
- Freeze PASS requires validator-backed English-only body.
- Freeze BLOCK is explicit when validation fails.
- Source Vietnamese prompt remains preserved as evidence.
- `specBoundary.englishFreezeEnforced` mirrors the validator state.
- no forbidden provider/receipt/routing/workflow/UI behavior changes.

## Review Gate

Before closure, verify:

- `englishSpecFreeze.status=frozen` is backed by validation;
- blocked validation never sets `specBoundary.englishFreezeEnforced=true`;
- original Vietnamese prompt remains available as source evidence;
- frozen Spec body excludes raw Vietnamese source text;
- route changes are additive and do not modify provider execution authority.

## Closure Checklist

- [ ] GC-018 filed
- [ ] work order filed
- [ ] implementation complete
- [ ] focused deterministic tests PASS
- [ ] live Strategy proof PASS or classified blocker filed
- [ ] docs gates PASS
- [ ] completion review filed
- [ ] active state/front door/handoff updated
- [ ] commits created

## Return-To-Orchestrator Conditions

Return blocked if implementation requires provider adapter changes, broad prompt
tuning, a second provider call, receipt changes, or hiding original Vietnamese
source evidence.

## Operator Checkpoint

No additional operator checkpoint is required before implementation because the
operator explicitly authorized proceeding with Spec English Freeze. Return to
the operator only if implementation requires a provider behavior change, second
live model call, or weaker claim boundary than the roadmap permits.

## Claim Boundary

VI5-T2 closes only the bounded English Spec freeze artifact and validation
surface. It does not claim universal translation quality, UI i18n, all-pack
coverage, hosted readiness, public readiness, production readiness, or broad
governance freeze release.
