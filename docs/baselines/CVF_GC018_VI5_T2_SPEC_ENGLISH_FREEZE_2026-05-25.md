# CVF GC-018 VI5-T2 Spec English Freeze

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_VI5_T2_SPEC_ENGLISH_FREEZE

docType: baseline

Date: 2026-05-25

---

## Purpose

Authorize VI5-T2 as a bounded implementation tranche that adds a validated
English Spec freeze artifact to `/api/execute` responses.

VI5-T1 correctly reported `observedSpecBodyLanguage=mixed` and
`englishFreezeEnforced=false`. VI5-T2 turns that diagnostic into a product
control: the final agent handoff Spec may be declared frozen only when CVF can
emit and validate an English canonical Spec block.

## Scope / Target / Owner Boundary

Owner surface:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- focused `cvf-web` tests
- VI5-T2 evidence/session/handoff docs

Allowed:

- add `cvf.englishSpecFreeze.vi5.t2.v1`;
- add English Spec freeze builder/validator;
- wire additive `englishSpecFreeze` into `/api/execute`;
- update `specBoundary` freeze booleans from the validator;
- preserve original Vietnamese prompt as source evidence;
- run one Vietnamese Strategy live proof after deterministic tests pass.

Forbidden:

- provider adapter, provider routing, model registry, or retry changes;
- receipt envelope changes;
- broad prompt tuning;
- workflow execution blocking;
- UI shell i18n;
- all-pack catalog expansion;
- external skill import;
- hosted/public/production readiness claims;
- broad governance freeze release.

## Decision / Baseline / Proposed Tranche

Decision: authorize VI5-T2 as a bounded response-level Spec English Freeze
implementation.

Baseline: VI5-T1 live evidence recorded `observedSpecBodyLanguage=mixed` and
`englishFreezeEnforced=false` for the Vietnamese Strategy path.

Proposed tranche: add a validator-backed `englishSpecFreeze` artifact and wire
`specBoundary` freeze booleans to that artifact. The tranche may claim English
freeze only when validation passes; otherwise it must report a blocked freeze
state.

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_VI5_T2_SPEC_ENGLISH_FREEZE_ROADMAP_2026-05-25.md`
- `docs/reviews/CVF_VI5_T1_LANGUAGE_STATE_AND_STRATEGY_GUIDED_CATALOG_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_VI5_T0_L1_BASELINE_AUDIT_2026-05-25.md`
- `docs/concepts/CVF_LAYERED_PRODUCT_ARCHITECTURE_AND_VIBE_DIALOG_PATTERN_2026-05-25.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-first-mediation.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vi5-language-readout.ts`

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - VI5-T0/T1 evidence family: 2 review packets
  - VI5 architecture family: 1 concept packet
  - L1/T1 runtime files: 2 code files
  - route response owner surface: 1 route file
- Prior absorption evidence resolved:
  - L1 is accepted as source preservation and normalized Spec baseline.
  - VI5-T1 is accepted as state reporting, not freeze.
  - VI5-T0 establishes the mixed-body problem that T2 addresses.
- Detailed source files used:
  - `docs/reviews/CVF_VI5_T1_LANGUAGE_STATE_AND_STRATEGY_GUIDED_CATALOG_COMPLETION_2026-05-25.md`
  - `docs/reviews/CVF_VI5_T0_L1_BASELINE_AUDIT_2026-05-25.md`
  - `docs/concepts/CVF_LAYERED_PRODUCT_ARCHITECTURE_AND_VIBE_DIALOG_PATTERN_2026-05-25.md`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-first-mediation.ts`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vi5-language-readout.ts`
- Source families skipped:
  - `.private_reference/legacy/`: skipped because this tranche does not
    absorb external/legacy skills; it implements an already accepted VI5
    product control.
  - provider/model docs: skipped because provider behavior changes are
    forbidden.
- File-level accepted value:
  - VI5 architecture -> Layer 4 agent handoff should be English.
  - VI5-T1 completion -> current mixed body must remain visible as audit
    evidence.
  - L1 implementation -> original prompt preservation must not be removed.
- Owner-surface normalization:
  - English freeze -> `cvf-web` response-level `englishSpecFreeze`.
  - Existing observation -> preserve `specBoundary.observedSpecBodyLanguage`.
  - Freeze claim -> only emitted through validator-backed booleans.
- Accept/defer/reject matrix:
  - ACCEPT_NOW: additive English Spec freeze artifact and validator.
  - ACCEPT_NOW: Strategy live proof.
  - DEFER_DEMAND_GATED: all-pack catalog/spec freeze UX.
  - DEFER_DEMAND_GATED: UI shell i18n.
  - REJECT_DIRECT: provider prompt tuning as the primary solution.
  - REJECT_DIRECT: claiming freeze when the body still contains Vietnamese.
- Adversarial roles completed:
  - Implementer: smallest viable proof is artifact + validation + route
    emission.
  - Skeptic/Auditor: main risk is fake English; validator must block.
  - Product/Operator Advocate: non-coder value is knowing the exact copy-ready
    English Spec for agents.
  - Safety/Boundary Owner: no provider/receipt/routing/workflow authority
    changes.
- Thin proof target:
  - deterministic tests plus one live Vietnamese Strategy proof.
- Blind-spot verdict: CLEAR.

## Required Evidence / Verification

Required deterministic verification:

```powershell
npm run test:run -- src/lib/spec-english-freeze.test.ts src/lib/vi5-language-readout.test.ts src/lib/spec-first-mediation.test.ts src/app/api/execute/route.vi5-t1-language-state.test.ts src/app/api/execute/route.test.ts
npm run check
```

Required live proof:

- one Vietnamese Strategy `/api/execute` request;
- provider receipt recorded without printing raw secrets;
- `englishSpecFreeze` present;
- `specBoundary.englishFreezeEnforced` matches validation state.

## Acceptance Criteria

1. `englishSpecFreeze.contractVersion=cvf.englishSpecFreeze.vi5.t2.v1`.
2. Frozen status requires English-only validation.
3. Source prompt is preserved as evidence but excluded from frozen Spec body.
4. `specBoundary.englishFreezeEnforced=true` only for validator PASS.
5. Validator BLOCK is explicit if English freeze cannot be safely claimed.
6. No forbidden owner surfaces are changed.

## Claim Boundary / Approval Gate

VI5-T2 may claim only a bounded response-level English Spec freeze artifact and
validation path. It does not claim universal translation quality, UI i18n,
provider stability, public readiness, production readiness, or broad freeze
release.
