# CVF VI5-T1 Language State And Strategy Guided Catalog Roadmap

Memory class: ROADMAP_RECORD

docType: roadmap

Date: 2026-05-25

Status: APPROVED_FOR_GC018_DISPATCH

Supersedes:

- `docs/roadmaps/CVF_VI5_LOCALIZED_NONCODER_READOUT_CONSOLIDATION_ROADMAP_2026-05-25.md`

## Purpose

Define the bounded VI5-T1 implementation tranche after the multilingual
architecture convergence and VI5-T0 baseline audit.

VI5-T1 turns the accepted 4-layer language architecture into additive
`/api/execute` readout fields without changing provider behavior, Spec
generation semantics, receipt envelopes, or workflow execution authority.

## Authorization Or Decision

Authority chain:

- Operator instruction on 2026-05-25: proceed after Claude accepted Codex's
  Multi-Role Orchestrated Convergence correction.
- Claude acceptance:
  `docs/reviews/CVF_VI5_MULTI_ROLE_CONVERGENCE_CLAUDE_ACCEPTANCE_2026-05-25.md`
- Codex correction:
  `docs/reviews/CVF_VI5_MULTI_ROLE_CONVERGENCE_CORRECTION_TO_CLAUDE_2026-05-25.md`
- VI5-T0 baseline:
  `docs/reviews/CVF_VI5_T0_L1_BASELINE_AUDIT_2026-05-25.md`

Implementation still requires fresh GC-018 and work order before code changes.

## Scope / Target / Owner Boundary

Owner surface: `cvf-web` additive `/api/execute` readout and workflow
presentation catalog loading.

Target: Strategy workflow only for guided catalog proof.

Allowed scope:

- add deterministic `languageState`;
- add deterministic `guidedStepState`;
- add deterministic `specBoundary`;
- add presentation loader for workflow catalog assets;
- add Strategy workflow `presentation/en.json` and `presentation/vi.json`;
- add `guided_mode_available` boolean marker to certified pack registry
  entries;
- add tests for catalog parity, readout generation, route emission, and live
  Strategy proof.

Forbidden scope:

- Spec English Freeze implementation;
- provider adapter/routing/model changes;
- receipt envelope changes;
- prompt tuning;
- workflow execution blocking;
- UI shell i18n;
- catalog expansion beyond Strategy;
- external skill import;
- hosted/public/production readiness claims;
- freeze posture changes.

## Non-Goals

VI5-T1 does not:

- enforce English-only Spec body content;
- translate existing L1 `normalizedExecutionSpec` content;
- change model prompts to force provider output language;
- implement UI shell i18n;
- implement runtime multi-agent scheduling or live subagent isolation;
- migrate all certified packs to guided mode;
- make a public/product readiness claim;
- reopen F-1 output-quality tuning.

## Predecessor Evidence

- Architecture:
  `docs/concepts/CVF_LAYERED_PRODUCT_ARCHITECTURE_AND_VIBE_DIALOG_PATTERN_2026-05-25.md`
- Vibe-to-Spec form:
  `docs/reference/CVF_VIBE_TO_SPEC_CONVERSATION_CAPTURE_FORM_2026-05-25.md`
- Multi-role convergence form:
  `docs/reference/CVF_MULTI_ROLE_ORCHESTRATED_CONVERGENCE_CAPTURE_FORM_2026-05-25.md`
- L1 implementation:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-first-mediation.ts`
- Route emission point:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`

## VI5-T0 Baseline Result

VI5-T0 live audit found:

```text
provider/model: alibaba/qwen-turbo
receipt: rcpt-env-mpl4ct9q-fdm2xr
specFirstContract: cvf.specFirstMediation.l1.v1
sourceLanguage: vi
workingLanguage: en
outputLanguage: vi
originalPromptPreserved: true
observedSpecBodyLanguage: mixed
normalizedExecutionSpecLength: 4309
```

Therefore VI5-T1 must report observed state and must not claim English freeze
enforcement.

## Required Fields

### `languageState`

Contract version: `cvf.languageState.vi5.t1.v1`

Required fields:

- `userInputLanguage`
- `userFacingResponseLanguage`
- `engineRoomLanguage`
- `specContractLanguage`
- `uiLayerLanguage`

Required invariant:

- `engineRoomLanguage === "en"`
- `specContractLanguage === "en"`

Non-claim:

- this does not assert current Spec body is English-only.

### `guidedStepState`

Contract version: `cvf.guidedStepState.vi5.t1.v1`

Required fields:

- `workflowId`
- `templateId`
- `guidedModeAvailable`
- `currentStep`
- `totalSteps`
- `stepIntent`
- `presentedQuestion`
- `presentedOptions`
- `allowFreeformAlternative`
- `userMustChoose`
- `capturedSpecFields`
- `transitionState`

### `specBoundary`

Contract version: `cvf.specBoundary.vi5.t1.v1`

Required fields:

- `frozen`
- `specBlockLanguage`
- `observedSpecBodyLanguage`
- `englishFreezeEnforced`
- `frozenAt`
- `editAfterFreezeWarning`
- `sourcePromptPreserved`
- `normalizedSpecAvailable`

Required VI5-T1 posture:

- `specBlockLanguage === "en"`
- `observedSpecBodyLanguage === "mixed"` for the current L1 baseline case
- `englishFreezeEnforced === false`

## Strategy Guided Catalog

Canonical runtime source:

```text
governance/workflows/strategy_analysis/presentation/en.json
governance/workflows/strategy_analysis/presentation/vi.json
```

Strategy guided sequence:

1. Intent confirmation:
   - captures `strategy.type`
   - options: `strategic_decision`, `market_entry`, `competitive_response`,
     `other`
2. Context bounding:
   - captures `strategy.constraints`
   - options: `budget_limited`, `time_constrained`, `regulatory_concern`,
     `no_major_constraint`, `other`
3. Output preference:
   - captures `strategy.outputFormat`
   - options: `scoring_matrix`, `decision_tree`,
     `recommendation_with_rationale`, `executive_summary`

Vietnamese and English catalogs must have key parity. Runtime must not use LLM
translation for guided step presentation.

## Work Plan

1. File VI5-T1 GC-018 with this roadmap, VI5-T0 baseline, and multi-role
   convergence packets as authority.
2. File VI5-T1 work order with source-fidelity checks for the route, L1
   readout, certified pack registry, and planned catalog paths.
3. Add Strategy presentation catalogs under
   `governance/workflows/strategy_analysis/presentation/`.
4. Add a runtime presentation loader with deterministic locale fallback and
   catalog key parity validation.
5. Add additive `languageState`, `guidedStepState`, and `specBoundary` readout
   module.
6. Wire the readout into `/api/execute` response without changing route gate,
   provider, prompt, receipt, or workflow execution semantics.
7. Add `guided_mode_available` markers to the ten certified pack registry
   entries.
8. Add focused unit and route tests.
9. Run one live Vietnamese Strategy proof after deterministic tests pass.
10. File completion packet and sync active handoff.

## Acceptance Criteria

1. `languageState.engineRoomLanguage === "en"`.
2. `languageState.specContractLanguage === "en"`.
3. `specBoundary.observedSpecBodyLanguage` is populated from deterministic
   observation and reflects the VI5-T0 baseline as `mixed` for Vietnamese L1
   Strategy output.
4. `specBoundary.englishFreezeEnforced === false`.
5. `languageState.userInputLanguage` is per-request, not profile-forced.
6. Strategy guided step presentation resolves English and Vietnamese catalog
   strings without runtime LLM translation.
7. `guidedStepState` exposes option IDs, localized labels, freeform fallback
   flag, captured Spec fields, and step transition state.
8. Original Vietnamese prompt remains preserved in existing L1
   `specFirstMediation.originalPrompt` evidence path.
9. Raw governance evidence remains available.
10. No provider adapter, receipt envelope, workflow engine, broad prompt
    tuning, or Spec English Freeze changes.
11. Strategy catalog `en.json` and `vi.json` have key parity enforced by tests.
12. Each certified pack registry entry carries `guided_mode_available`
    boolean marker so transition state is explicit.

## Verification Or Evidence

Required deterministic verification:

```powershell
npm run test:run -- src/lib/presentation-loader.test.ts src/lib/vi5-language-readout.test.ts src/lib/spec-first-mediation.test.ts src/app/api/execute/route.test.ts
npm run check
```

Required live proof:

- one Vietnamese Strategy `/api/execute` request;
- live provider receipt recorded;
- `languageState`, `guidedStepState`, and `specBoundary` present;
- `observedSpecBodyLanguage=mixed`;
- `englishFreezeEnforced=false`;
- raw secret not printed.

Live failures must follow:

`docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`

## Review / Role Workflow

Multi-role execution roles:

- Orchestrator: Codex, scope and gate control
- Implementer: Codex, additive code/docs only
- Reviewer: Codex reviewer role, checks false claims and boundaries
- Auditor: Codex auditor role, runs docs/tests/live proof and handoff sync
- Operator: final product review after VI5-T1, not internal audit

Use:

`docs/reference/CVF_MULTI_ROLE_ORCHESTRATED_CONVERGENCE_CAPTURE_FORM_2026-05-25.md`

## Decision / Recommendation / Disposition

Decision: APPROVED_FOR_GC018_DISPATCH.

Recommendation: open VI5-T1 GC-018 and work order, then implement exactly this
bounded scope.

Disposition: roadmap complete; implementation not authorized until GC-018 and
work order are filed.

## Claim Boundary

This roadmap does not claim VI5-T1 implementation, Spec English Freeze, Real
Non-Coder Usage Test PASS, UI shell i18n, multi-pack guided catalog coverage,
hosted readiness, public readiness, production readiness, runtime multi-agent
scheduling, live subagent isolation, or freeze posture changes.
