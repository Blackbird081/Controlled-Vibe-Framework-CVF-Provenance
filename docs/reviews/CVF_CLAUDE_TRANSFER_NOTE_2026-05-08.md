# CVF Claude Transfer Note

> Date: 2026-05-08  
> Purpose: governed agent transfer note from Codex to Claude  
> Current canonical branch: `main`  
> Read this with: `AGENTS.md` and `AGENT_HANDOFF.md`

## Transfer Status

CVF is currently synchronized on `main` with the handoff state:

`UNIFIED ON MAIN / W114-W141 CLOSED`

The latest runtime-stability baseline is W141:

- Alibaba browser UI matrix: `12/12 accepted_with_receipt`
- `execute_request_not_sent`: `0`
- `wizard_routing_shadow`: `0`
- Latest release gate: `python scripts/run_cvf_release_gate_bundle.py --json` PASS

No active runtime-stability blocker remains from the W132-W141 sequence.

## Latest Commits To Know

- `ce12527c` - W140 diagnostic: classified residual UI failures as
  `execute_request_not_sent` caused by wizard routing shadow.
- `dd26fcc8` - W141 fix: trusted-form/wizard disambiguation and live proof.
- `ec9712f0` - Handoff sync: updated `AGENT_HANDOFF.md` through W141 closure.

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

No default continuation tranche is currently open after W141. The next move
should be operator-scoped rather than inferred from stale W132-W140 blockers.
