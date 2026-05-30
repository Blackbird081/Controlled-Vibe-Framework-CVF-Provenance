# CVF VI5-T2 Spec English Freeze Roadmap

Memory class: ROADMAP_RECORD

docType: roadmap

Date: 2026-05-25

Status: APPROVED_FOR_GC018_DISPATCH

## Purpose

Define the bounded VI5-T2 tranche after VI5-T1 proved that CVF can report
language state honestly but still observes a mixed-language Spec body for the
Vietnamese Strategy path.

VI5-T2 targets the product boundary the operator identified: the final agent
handoff Spec should be a governed English contract. Vietnamese source input
must remain preserved as evidence, but the implementation handoff should not
depend on mixed-language body text.

## Authorization Or Decision

Authority chain:

- Operator instruction on 2026-05-25: proceed with Spec English Freeze after
  confirming mixed Spec body is not the target product state.
- VI5-T1 completion:
  `docs/reviews/CVF_VI5_T1_LANGUAGE_STATE_AND_STRATEGY_GUIDED_CATALOG_COMPLETION_2026-05-25.md`
- VI5-T0 baseline:
  `docs/reviews/CVF_VI5_T0_L1_BASELINE_AUDIT_2026-05-25.md`
- Layered language architecture:
  `docs/concepts/CVF_LAYERED_PRODUCT_ARCHITECTURE_AND_VIBE_DIALOG_PATTERN_2026-05-25.md`

Implementation requires fresh GC-018 and work order before code changes.

## Scope / Target / Owner Boundary

Owner surface: `cvf-web` additive `/api/execute` response readout and
Spec-freeze helper.

Allowed scope:

- add deterministic `englishSpecFreeze` readout;
- create a canonical English Spec freeze artifact from existing L1 readout,
  selected template metadata, request metadata, and provider output when
  available;
- validate whether the frozen artifact is English-only enough to be declared
  agent-handoff-ready;
- update `specBoundary` to report freeze status from the T2 validator;
- add unit, route, and one live Vietnamese Strategy proof;
- update completion/session/handoff docs.

Forbidden scope:

- broad provider prompt tuning;
- new provider adapter, routing, model registry, or retry behavior;
- receipt envelope changes;
- workflow execution blocking;
- UI shell i18n;
- all-pack guided catalog expansion;
- external skill import;
- tool, MCP, browser, database, payment, or spend execution;
- hosted/public/production readiness claims;
- freeze release outside this response-level Spec artifact.

## Non-Goals

VI5-T2 does not:

- translate every provider output into English;
- guarantee universal English quality across all domains;
- change provider prompts as the primary mechanism;
- add a second provider call;
- change provider routing, adapters, models, or retry behavior;
- alter the receipt envelope;
- block workflow execution;
- implement UI shell i18n;
- migrate all certified packs;
- import external skills;
- claim hosted, public, or production readiness.

## Product Rule

Mixed Spec body is acceptable evidence of current state, not the product goal.

The product goal is:

```text
Vietnamese source prompt preserved as evidence
-> English canonical Spec block frozen for agents
-> Vietnamese user-facing explanation/readout remains allowed
```

VI5-T2 must not fake translation quality. If the freeze artifact still contains
Vietnamese body content or loses required context, the readout must report a
blocked or review-needed freeze state rather than claim success.

## Required Contract

Add `englishSpecFreeze`.

Contract version: `cvf.englishSpecFreeze.vi5.t2.v1`

Required fields:

- `contractVersion`
- `status`: `frozen` | `blocked`
- `frozenSpecLanguage`: `en`
- `sourcePromptLanguage`
- `sourcePromptPreserved`
- `frozenSpec`
- `standardSections`
- `validation`
- `sourceEvidenceRef`
- `agentHandoffReady`
- `userReviewRequired`
- `boundaries`

Validation fields:

- `englishOnlyBody`
- `requiredSectionsPresent`
- `sourceEvidenceSeparated`
- `missingSections`
- `blockedReasons`

Update `specBoundary` posture:

- `frozen=true` only when `englishSpecFreeze.status=frozen`.
- `englishFreezeEnforced=true` only when the T2 artifact validates.
- `observedSpecBodyLanguage` remains the L1 observed body language for audit.
- `specBlockLanguage=en` remains the intended block language.

## Work Plan

1. File VI5-T2 GC-018 with a blind-spot control block.
2. File VI5-T2 work order.
3. Add `spec-english-freeze.ts` with canonical freeze builder and validator.
4. Extend `vi5-language-readout.ts` to accept a T2 freeze result and update
   `specBoundary` without hiding the original L1 observation.
5. Wire the freeze readout into `/api/execute` response after
   `specFirstMediation` is built.
6. Add focused unit tests for frozen and blocked cases.
7. Add route test for Vietnamese Strategy path.
8. Run one live Vietnamese Strategy proof and classify any failure before
   rerun.
9. File completion packet and sync active state/front door/handoff.

## Acceptance Criteria

1. `/api/execute` emits `englishSpecFreeze`.
2. `englishSpecFreeze.contractVersion=cvf.englishSpecFreeze.vi5.t2.v1`.
3. Frozen status requires English-only body validation and required sections.
4. Vietnamese source prompt is preserved as evidence but excluded from the
   frozen English Spec body.
5. `specBoundary.englishFreezeEnforced=true` only when validation passes.
6. If validation fails, the route reports `englishSpecFreeze.status=blocked`
   and does not claim freeze.
7. Existing L1 `specFirstMediation.originalPromptPreserved` remains true for
   Vietnamese requests.
8. No provider adapter, provider routing, receipt envelope, broad prompt
   tuning, workflow blocking, or UI shell i18n change.

## Verification Or Evidence

Required deterministic verification:

```powershell
npm run test:run -- src/lib/spec-english-freeze.test.ts src/lib/vi5-language-readout.test.ts src/lib/spec-first-mediation.test.ts src/app/api/execute/route.vi5-t1-language-state.test.ts src/app/api/execute/route.test.ts
npm run check
```

Required live proof:

- one Vietnamese Strategy `/api/execute` request;
- live provider receipt recorded;
- `englishSpecFreeze` emitted;
- `specBoundary.englishFreezeEnforced` matches freeze validation;
- raw secret not printed.

Live failures must follow:

`docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`

## Claim Boundary

VI5-T2 may claim only response-level English Spec freeze artifact generation
and validation for the tested Strategy path.

It does not claim universal translation quality, all workflow packs, UI shell
i18n, provider stability, prompt parity, hosted readiness, public readiness,
production readiness, runtime multi-agent scheduling, or broad governance
freeze release.
