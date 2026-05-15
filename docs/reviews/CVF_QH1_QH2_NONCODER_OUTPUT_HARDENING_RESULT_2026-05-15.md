# CVF QH-1/QH-2 Non-Coder Output Hardening Result

Date: 2026-05-15

Status: IMPLEMENTED WITH MIXED EVT-4 REGRESSION

Parent review:

- `docs/reviews/CVF_GC018_QH1_QH2_NONCODER_OUTPUT_HARDENING_2026-05-15.md`

Parent roadmap:

- `docs/roadmaps/CVF_NONCODER_OUTPUT_QUALITY_HARDENING_ROADMAP_2026-05-15.md`

## 1. Implemented Product Change

QH-1:

- `feature_prioritization` and backlog/MVP-scope prompts now use a
  scope-first deliverable contract.
- The output leads with `Do now / MVP`, `Do next`, `Defer`, explicit non-goals,
  first validation/build step, owner/role, and acceptance check.
- The scoring matrix is supporting evidence after the scope decision.

QH-2:

- `pricing_strategy` and pricing-focused prompts now use a concrete pricing
  recommendation contract.
- The output includes pricing tiers/options, target user, included
  limits/features, price anchors or relative bands, first experiment, and
  risk/validation checks.
- Unsupported exact prices remain disallowed; useful assumptions must be
  labeled.

Files changed:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/product.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/marketing.ts`

## 2. Static Evidence

Targeted tests:

- `npx vitest run src/lib/execute-prompt-contract.test.ts src/lib/templates/index.test.ts src/lib/front-door-template-standard.test.ts src/lib/trusted-form-corpus.test.ts`
- Result: `4` files passed, `124/124` tests passed.

Type/lint:

- `npx tsc --noEmit`: PASS.
- `npm run lint`: PASS with one pre-existing warning in
  `src/app/api/system/jobs/route.test.ts` for unused `_request`.

## 3. Focused Live Evidence

Command:

```bash
EVT4_PROVIDER=deepseek EVT4_MODEL=deepseek-v4-pro EVT4_TASK_IDS=EVT4-09,EVT4-05 EVT4_LIMIT=2 node scripts/run_evt4_output_quality_ab.js
```

Evidence:

- `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_QH1_QH2_FOCUSED_EVIDENCE_2026-05-15.json`
- `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_QH1_QH2_FOCUSED_SUMMARY_2026-05-15.md`

Result:

- Completed `2/2`.
- CFG-B live receipts `2/2`.
- Safety failures `0`.
- Median delta `-0.12`; registered parity decision rule not met.

Focused lane comparison against final stop-rule baseline:

| Task | Baseline Delta | Current Delta | Baseline CFG-B | Current CFG-B | Receipt |
| --- | ---: | ---: | ---: | ---: | --- |
| EVT4-05 Pricing tiers | `-0.20` | `-0.12` | `0.72` | `0.76` | yes |
| EVT4-09 MVP scope | `-0.20` | `-0.12` | `0.72` | `0.84` | yes |

Interpretation:

- The focused product lanes produced live receipts and the requested operator
  artifacts.
- The focused check improved over the corresponding baseline task deltas, but
  still did not meet parity.

## 4. Full EVT-4 Regression Evidence

Command:

```bash
EVT4_PROVIDER=deepseek EVT4_MODEL=deepseek-v4-pro EVT4_LIMIT=20 node scripts/run_evt4_output_quality_ab.js
```

Evidence:

- `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_QH1_QH2_REGRESSION_EVIDENCE_2026-05-15.json`
- `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_QH1_QH2_REGRESSION_SUMMARY_2026-05-15.md`

Result:

- Completed `20/20`.
- CFG-B live receipts `20/20`.
- Safety failures `0`.
- Median normalized delta `-0.12`.
- Registered parity decision rule not met.

Baseline comparison:

| Metric | Final Stop-Rule Baseline | QH-1/QH-2 Regression |
| --- | ---: | ---: |
| Completed | `20/20` | `20/20` |
| CFG-B receipts | `20/20` | `20/20` |
| Safety failures | `0` | `0` |
| Median delta | `-0.08` | `-0.12` |
| CFG-B median duration ms | `82012` | `79211` |
| CFG-B median output tokens | `2813` | `2625` |

Target-lane notes:

- EVT4-05 pricing tiers improved strongly in the full run:
  - delta `-0.20 -> 0.20`;
  - CFG-B `0.72 -> 1.00`.
- EVT4-09 MVP scope improved modestly:
  - delta `-0.20 -> -0.16`;
  - CFG-B `0.72 -> 0.76`.
- EVT4-14 backlog triage improved:
  - delta `-0.28 -> -0.20`;
  - CFG-B `0.72 -> 0.80`.
- EVT4-11 pilot pricing remained the same on CFG-B score:
  - CFG-B `0.76 -> 0.76`.
- EVT4-18 freemium decision retained CFG-B `1.00`, with delta movement driven
  by CFG-A/reviewer comparison.

## 5. Closure Interpretation

QH-1/QH-2 implementation is complete as a bounded product deliverable change.

However, full EVT-4 regression is mixed:

- Governance receipts and safety remained stable.
- Several target lanes improved or stayed stable.
- The full-corpus median delta moved from `-0.08` to `-0.12`, so this tranche
  must not be claimed as full no-degrade or output-quality parity.

No further rerun should be performed merely to chase reviewer/provider
variance. Future work should continue through the roadmap as bounded
product-quality tracks, especially QH-3 SOP/handoff, QH-4 persona-to-action,
and QH-5 decision activation.
