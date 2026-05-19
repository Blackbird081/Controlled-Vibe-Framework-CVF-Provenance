# CVF Claude Transfer Note

> Date: 2026-05-08
> Purpose: governed agent transfer note from Codex to Claude
> Current canonical branch: `main`
> W152 sync: current through W151
> Read this with: `AGENTS.md` and `AGENT_HANDOFF.md`

## Transfer Status

CVF is currently synchronized on `main` with the handoff state:

`UNIFIED ON MAIN / W114-W151 CLOSED`

The latest runtime-stability baseline remains W141 for the original
runtime-stability sequence:

- Alibaba browser UI matrix: `12/12 accepted_with_receipt`
- `execute_request_not_sent`: `0`
- `wizard_routing_shadow`: `0`
- Latest release gate: `python scripts/run_cvf_release_gate_bundle.py --json` PASS

No active runtime-stability blocker remains from the W132-W141 sequence.

The latest trusted-form product baseline is W149-W151:

- W149 live value gate: Alibaba direct API `40/40`, Alibaba browser UI `40/40`
  with governed receipts, DeepSeek confirmatory `12/12`.
- W150 maintainability: trusted-form router API remains in
  `src/lib/form-routing.ts`; 40-form corpus data lives in
  `src/lib/trusted-form-corpus.ts`.
- W151 maintainability: activation coverage lives in
  `src/lib/trusted-form-corpus.test.ts`; `form-routing.test.ts` is router and
  integration focused.
- Latest release gate: `python scripts/run_cvf_release_gate_bundle.py --json`
  PASS.

## Latest Commits To Know

- `ce12527c` - W140 diagnostic: classified residual UI failures as
  `execute_request_not_sent` caused by wizard routing shadow.
- `dd26fcc8` - W141 fix: trusted-form/wizard disambiguation and live proof.
- `ec9712f0` - Handoff sync: updated `AGENT_HANDOFF.md` through W141 closure.
- `f9a592f8` - W149 live value gate: 40-form Alibaba direct/UI proof and
  DeepSeek confirmatory subset.
- `c5b72401` - W150 refactor: split trusted-form corpus from router API.
- `dae6356c` - W151 test split: data-driven activation matrix.

Use live `git log --oneline -n 10` for the exact current HEAD before making any
new change.

## W134-W141 Runtime Stability Chain

The stability investigation should not be restarted from W132 assumptions.

- W134 closed the pre-AI HTTP 400 blocker by capturing response bodies and
  normalizing trusted-form guard action before Guard Runtime. Alibaba reached
  `9/12`; DeepSeek reached `6/6`.
- W135 closed the `competitor_review` HTTP 422 false positive by fixing
  competitor-analysis language that collided with unsafe-term output validation.
- W136 hardened trusted-form token and retry budgets; targeted live proof for
  `documentation` and `strategy_analysis` passed under the browser deadline.
- W137 and W138 showed Alibaba still at `10/12`, while DeepSeek stayed `6/6`;
  cooldown was not the controlling variable.
- W139 direct `/api/execute` diagnostic passed Alibaba `12/12` and DeepSeek
  `6/6`, proving the remaining residual was not a general provider or route
  failure.
- W140 proved the remaining UI failures never fired `/api/execute` and instead
  landed in wizard flows: `System Design Wizard` and `Business Strategy Wizard`.
- W141 tightened audited trusted-form activation patterns and closed the
  residual with Alibaba UI `12/12`.

Primary evidence files:

- `docs/reviews/CVF_W134_CONTINUATION_DECISION_2026-05-07.md`
- `docs/reviews/CVF_W135_ROOT_CAUSE_FINDING_2026-05-07.md`
- `docs/reviews/CVF_W136_CLOSURE_RESULT_2026-05-07.md`
- `docs/reviews/CVF_W137_CONTINUATION_DECISION_2026-05-07.md`
- `docs/reviews/CVF_W138_CONTINUATION_DECISION_2026-05-07.md`
- `docs/reviews/CVF_W139_CONTINUATION_DECISION_2026-05-07.md`
- `docs/reviews/CVF_W140_CONTINUATION_DECISION_2026-05-08.md`
- `docs/reviews/CVF_W141_CLOSURE_DECISION_2026-05-08.md`

## W142-W151 Trusted Form Expansion And Maintainability Chain

Do not resume from the W126 8-form boundary as if it were current.

- W142-W147 expanded the trusted-form corpus to 40 non-wizard forms.
- W149 live-proved that expanded corpus under a bounded claim:
  - Alibaba direct API: `40/40` accepted with receipts.
  - Alibaba browser UI: `40/40` accepted with receipts.
  - DeepSeek confirmatory subset: `12/12` accepted.
- W150 split corpus data into `trusted-form-corpus.ts` while preserving
  imports from `form-routing.ts`.
- W151 split activation tests into `trusted-form-corpus.test.ts`.

Primary evidence files:

- `docs/reviews/CVF_W149_CLOSURE_DECISION_2026-05-08.md`
- `docs/reviews/archive/CVF_W149_TRUSTED_FORM_FULL_CORPUS_LOCK_2026-05-08.md`
- `docs/reviews/CVF_W150_CLOSURE_DECISION_2026-05-08.md`
- `docs/reviews/CVF_W151_CLOSURE_DECISION_2026-05-08.md`

Boundary:

- This proves W149's bounded live usability claim, not perfect reliability or
  full provider parity across the entire 40-form corpus.
- W150/W151 are maintainability-only and do not alter routing behavior.

## CVF ADD Absorption State

CVF ADD doctrine absorption is complete for the current bounded scope.

Official docs absorption:

- `docs/reference/CVF_GOVERNED_CAPABILITY_INTAKE_DOCTRINE_2026-05-07.md`
- `docs/reference/CVF_BOUNDARY_FIRST_GOVERNANCE_DOCTRINE_2026-05-07.md`
- `docs/reference/CVF_GOVERNED_CONTEXT_PROFILE_METADATA_DOCTRINE_2026-05-07.md`
- `docs/reference/CVF_AGENT_CONTINUITY_AND_DELEGATION_DOCTRINE_2026-05-07.md`
- `docs/reference/CVF_SCOPED_KNOWLEDGE_PROVIDER_BOUNDARY_DOCTRINE_2026-05-07.md`

Runtime activation:

- `docs/roadmaps/CVF_ADD_RUNTIME_ACTIVATION_ROADMAP_2026-05-07.md`
- RT0-RT8 delivered: doctrine metadata is runtime-readable, registry-persisted,
  visible in External Asset Governance UI, and queryable by metadata filters.

Boundary:

- Do not promote private CVF ADD review files directly.
- Do not duplicate private deliverables; they already exist in
  `.private_reference/legacy/CVF ADD/REVIEW FOLDER/`.
- Future work should use the official docs above as source of truth.
- Runtime activation does not execute external tools, widen provider behavior,
  or claim live governance proof by itself.

## Mandatory Proof Rule

Any claim about CVF governance behavior must use live provider proof.

Release-quality proof command:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

Never print or commit raw API keys. Use operator-supplied environment variables
such as `DASHSCOPE_API_KEY`, `ALIBABA_API_KEY`, `CVF_ALIBABA_API_KEY`,
`CVF_BENCHMARK_ALIBABA_KEY`, and `DEEPSEEK_API_KEY`.

Mock mode is only valid for pure UI structure checks.

## Recommended Claude Starting Point

1. Read `AGENTS.md`.
2. Read the top of `AGENT_HANDOFF.md`.
3. Verify current git state with `git status --short` and
   `git log --oneline -n 10`.
4. If opening a new tranche, issue fresh GC-018 and roadmap before implementation.
5. If claiming governance behavior, run the live release gate.

No default continuation tranche is currently open after W151. The next move
should be operator-scoped rather than inferred from stale W126 or W132-W140
blockers.
