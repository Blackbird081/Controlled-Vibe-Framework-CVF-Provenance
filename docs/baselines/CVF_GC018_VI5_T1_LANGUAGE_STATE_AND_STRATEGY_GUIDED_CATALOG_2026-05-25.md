# CVF GC-018 VI5-T1 Language State And Strategy Guided Catalog

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_VI5_T1_LANGUAGE_STATE_AND_STRATEGY_GUIDED_CATALOG

docType: baseline

Date: 2026-05-25

---

## Purpose

Authorize VI5-T1 as a bounded implementation tranche after the VI5 layered
architecture discussion, Claude acceptance, and VI5-T0 live baseline audit.

The goal is to expose three deterministic `/api/execute` readouts:
`languageState`, `guidedStepState`, and `specBoundary`, plus one Strategy
workflow presentation catalog. This records what CVF actually knows about
language and guided-mode readiness without claiming Spec English Freeze.

## Scope / Target / Owner Boundary

Owner surface:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/`
- `governance/workflows/strategy_analysis/presentation/`
- `governance/registries/cvf-certified-skill-pack-registry.json`
- focused `cvf-web` tests and VI5-T1 evidence docs

Allowed:

- add additive response readouts only;
- add deterministic language/spec-boundary observation helpers;
- add deterministic workflow presentation catalog loader;
- add Strategy `en.json` and `vi.json` presentation catalogs;
- add `guided_mode_available` boolean markers to certified pack registry
  entries;
- run one Vietnamese Strategy live proof after deterministic tests pass.

Forbidden:

- Spec English Freeze;
- provider adapter, provider routing, or model changes;
- prompt tuning;
- receipt envelope changes;
- workflow execution blocking;
- UI shell i18n;
- catalog expansion beyond Strategy;
- external skill import;
- runtime multi-agent scheduling or subagent isolation;
- public-sync, hosted readiness, production readiness, or release claims.

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_VI5_T1_LANGUAGE_STATE_AND_STRATEGY_GUIDED_CATALOG_ROADMAP_2026-05-25.md`
- `docs/reviews/CVF_VI5_MULTI_ROLE_CONVERGENCE_CLAUDE_ACCEPTANCE_2026-05-25.md`
- `docs/reviews/CVF_VI5_MULTI_ROLE_CONVERGENCE_CORRECTION_TO_CLAUDE_2026-05-25.md`
- `docs/reference/CVF_MULTI_ROLE_ORCHESTRATED_CONVERGENCE_CAPTURE_FORM_2026-05-25.md`
- `docs/concepts/CVF_LAYERED_PRODUCT_ARCHITECTURE_AND_VIBE_DIALOG_PATTERN_2026-05-25.md`
- `docs/reviews/CVF_VI5_T0_L1_BASELINE_AUDIT_2026-05-25.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-first-mediation.ts`

## Baseline

VI5-T0 live audit proved the current L1 path preserves the Vietnamese source
prompt and emits an English Spec structure with mixed Vietnamese/English body
content:

```text
provider/model: alibaba/qwen-turbo
receipt: rcpt-env-mpl4ct9q-fdm2xr
sourceLanguage: vi
workingLanguage: en
outputLanguage: vi
observedSpecBodyLanguage: mixed
englishFreezeEnforced: false
```

VI5-T1 must report this boundary explicitly. It must not hide the mixed body or
claim English-only Spec enforcement.

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - VI5 architecture/review packet family: 5 files
  - L1 implementation/runtime family: 2 code files identified before dispatch
  - certified pack registry family: 1 registry file
  - Strategy workflow presentation target: new files only
- Prior absorption evidence resolved:
  - L1 multilingual mediation work is predecessor evidence, not reopened.
  - VI5-T0 live audit is accepted baseline.
  - Claude acceptance supersedes the earlier two-agent framing.
- Detailed source files used:
  - `docs/concepts/CVF_LAYERED_PRODUCT_ARCHITECTURE_AND_VIBE_DIALOG_PATTERN_2026-05-25.md`
  - `docs/reviews/CVF_VI5_MULTI_ROLE_CONVERGENCE_CLAUDE_ACCEPTANCE_2026-05-25.md`
  - `docs/reviews/CVF_VI5_T0_L1_BASELINE_AUDIT_2026-05-25.md`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-first-mediation.ts`
- Source families skipped:
  - `.private_reference/legacy/`: skipped because VI5-T1 is not importing a
    legacy capability; it only exposes state for already accepted L1/VI5
    architecture.
  - external skill sources: skipped because external skill absorption is
    explicitly forbidden in this tranche.
- File-level accepted value:
  - VI5 architecture -> four-layer language separation.
  - Claude acceptance -> no two-agent limit; use multi-role convergence.
  - VI5-T0 audit -> mixed Spec body must be visible.
  - L1 mediation module -> source/working/output language signal source.
- Owner-surface normalization:
  - language separation -> `cvf-web` `/api/execute` readout.
  - guided Strategy presentation -> `governance/workflows/strategy_analysis`
    catalog, loaded deterministically.
  - mixed Spec body observation -> `specBoundary`, not freeze enforcement.
- Accept/defer/reject matrix:
  - ACCEPT_NOW: additive `languageState`, `guidedStepState`, `specBoundary`.
  - ACCEPT_NOW: Strategy-only presentation catalog.
  - DEFER_DEMAND_GATED: Spec English Freeze.
  - DEFER_DEMAND_GATED: all-pack guided catalogs and UI shell i18n.
  - REJECT_DIRECT: two-agent-only convergence model.
  - REJECT_DIRECT: LLM runtime translation for catalog strings.
- Adversarial roles completed:
  - Implementer: smallest proof is route emission plus Strategy catalog.
  - Skeptic/Auditor: primary overclaim risk is implying English freeze; forbid
    that and expose `englishFreezeEnforced=false`.
  - Product/Operator Advocate: noncoder value is clarity about language,
    guided choices, and what remains unresolved.
  - Safety/Boundary Owner: keep provider, prompt, receipt, execution gate, and
    public claims unchanged.
- Thin proof target:
  - deterministic tests plus one Vietnamese Strategy live `/api/execute` proof.
- Blind-spot verdict: CLEAR.

## Required Evidence / Verification

Required deterministic verification:

```powershell
npm run test:run -- src/lib/presentation-loader.test.ts src/lib/vi5-language-readout.test.ts src/lib/spec-first-mediation.test.ts src/app/api/execute/route.test.ts
npm run check
```

Required live proof:

- one Vietnamese Strategy `/api/execute` request;
- provider receipt recorded without printing raw secrets;
- `languageState`, `guidedStepState`, and `specBoundary` present;
- `specBoundary.observedSpecBodyLanguage=mixed`;
- `specBoundary.englishFreezeEnforced=false`.

Live failures must follow
`docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`.

## Acceptance Criteria

1. `languageState.engineRoomLanguage === "en"`.
2. `languageState.specContractLanguage === "en"`.
3. `languageState.userInputLanguage` is request-derived.
4. `guidedStepState` resolves Strategy EN/VI catalogs without LLM translation.
5. `guidedStepState` includes option IDs, labels, freeform fallback, captured
   Spec fields, and transition state.
6. `specBoundary.observedSpecBodyLanguage` is deterministic and populated.
7. `specBoundary.englishFreezeEnforced === false`.
8. All ten certified registry entries have `guided_mode_available`.
9. Raw governance evidence and existing L1 prompt preservation remain present.
10. No forbidden owner surfaces are changed.

## Claim Boundary / Approval Gate

VI5-T1 may claim only additive deterministic readouts and Strategy guided
catalog availability. It does not claim Spec English Freeze, all-pack guided
coverage, UI shell i18n, provider/model changes, hosted readiness, public
readiness, production readiness, runtime multi-agent scheduling, or live
subagent isolation.
