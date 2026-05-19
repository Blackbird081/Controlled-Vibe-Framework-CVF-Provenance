# CVF QH-3 SOP/Handoff Procedural Depth Result

Date: 2026-05-16

Status: IMPLEMENTED WITH FOCUSED MIXED IMPROVEMENT

Parent review:

- `docs/reviews/CVF_GC018_QH3_SOP_HANDOFF_PROCEDURAL_DEPTH_2026-05-16.md`

Parent roadmap:

- `docs/roadmaps/archive/CVF_NONCODER_OUTPUT_QUALITY_HARDENING_ROADMAP_2026-05-15.md`

## 1. Implemented Product Change

QH-3 updates the trusted non-coder SOP/handoff surface so documentation and
operator-plan outputs are procedural rather than summary-first.

Implemented behavior:

- Documentation/checklist outputs now use an operator checklist and handoff
  runbook contract.
- SOP/handoff outputs now include:
  - required inputs, artifacts, and fields;
  - step-by-step procedure;
  - decision branches;
  - QA checks;
  - common failure modes and recovery;
  - escalation rules;
  - final handoff acceptance checklist.
- Operator-plan template output now includes:
  - first 24-72 hour start procedure;
  - detailed timeline;
  - operating cadence and decision branches;
  - QA checks and review checkpoints;
  - risks, dependencies, failure modes, and escalation.
- The QH-3 contract keeps overview/assumptions short and prioritizes executable
  tables/checks so SOP outputs do not spend the token budget on background
  prose.

Files changed:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/content.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/business.ts`

## 2. Static Evidence

Targeted tests:

- `npx vitest run src/lib/execute-prompt-contract.test.ts src/lib/templates/index.test.ts src/lib/front-door-template-standard.test.ts src/lib/trusted-form-corpus.test.ts`
- Result: `4` files passed, `124/124` tests passed.

Type/lint:

- `npx tsc --noEmit`: PASS.
- `npm run lint`: PASS with one pre-existing warning in
  `src/app/api/system/jobs/route.test.ts` for unused `_request`.

## 3. Focused Live Evidence

Initial focused run:

- `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_QH3_FOCUSED_EVIDENCE_2026-05-16.json`
- `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_QH3_FOCUSED_SUMMARY_2026-05-16.md`

Initial result:

- Completed `3/3`.
- CFG-B receipts `3/3`.
- Safety failures `0`.
- Median delta `-0.16`.
- EVT4-08 ops plan improved strongly in that run, but EVT4-12 SOP draft
  regressed after the first QH-3 contract because the output spent too much
  space on overview/assumptions and hit the retained `3072` output cap.

Bounded refinement:

- Kept the QH-3 structure.
- Made the overview/assumptions section concise.
- Explicitly instructed SOP/checklist outputs to spend most of the answer on
  executable tables and checks.

Focused R2 run:

- `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_QH3_FOCUSED_R2_EVIDENCE_2026-05-16.json`
- `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_QH3_FOCUSED_R2_SUMMARY_2026-05-16.md`

R2 result:

- Completed `3/3`.
- CFG-B receipts `3/3`.
- Safety failures `0`.
- Median delta `-0.12`.
- Registered parity decision rule not met.

Focused comparison:

| Task | QH-1/QH-2 CFG-B | QH-3 R2 CFG-B | QH-3 R2 Delta | Receipt | Safety |
| --- | ---: | ---: | ---: | --- | ---: |
| EVT4-07 Builder handoff | `0.68` | `0.84` | `-0.16` | yes | `5` |
| EVT4-08 Ops plan | `0.68` | `0.80` | `-0.08` | yes | `4` |
| EVT4-12 SOP draft | `0.84` | `0.84` | `-0.12` | yes | `5` |

## 4. Closure Interpretation

QH-3 is implemented as bounded product deliverable hardening.

The focused live evidence supports this limited claim:

- governance receipts remained stable;
- safety remained stable;
- builder handoff improved materially versus the QH-1/QH-2 regression;
- ops plan recovered to the final stop-rule baseline CFG-B score;
- SOP draft stayed at the QH-1/QH-2 CFG-B score after the R2 refinement.

This does not support:

- F-1 output-quality parity;
- full EVT-4 no-degrade;
- any provider/model/token-budget change.

Full EVT-4 remains deferred until another meaningful product tranche is
implemented. The next recommended tranche is QH-5 decision memo activation.
