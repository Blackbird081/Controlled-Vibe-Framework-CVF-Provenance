# CVF D2 Provider Capability Matrix Completion

Memory class: FULL_RECORD

Status: CLOSED_D2_PROVIDER_CAPABILITY_MATRIX

Date: 2026-05-22

## Purpose

Close D2 from the post-B/C Review-CVF remaining pain-point roadmap by turning
provider method support into a canonical Model Gateway capability registry and
deterministic unsupported-method gate.

## Scope / Target / Owner Boundary

Target: `EXTENSIONS/CVF_MODEL_GATEWAY` provider method contract, registry,
gate helpers, and focused tests.

Owner: Codex, acting as implementer, reviewer, and evidence owner under the
operator authorization to process the six remaining Review-CVF pain-point
phases in priority order.

Boundary: D2 does not add new live adapter behavior, route dispatch,
provider parity, receipt-envelope changes, retry/cost/risk ownership changes,
public-sync, hosted readiness, Maika proof, or freeze release.

## Target / Source

Target artifact:

- D2 provider capability matrix and deterministic unsupported-method behavior.

Source artifacts:

- `.private_reference/legacy/CVF 17.05/Review CVF.md`
- `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`
- `docs/roadmaps/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINT_ROADMAP_2026-05-22.md`
- `docs/baselines/CVF_GC018_D2_PROVIDER_CAPABILITY_MATRIX_2026-05-22.md`
- `docs/work_orders/CVF_WO_D2_PROVIDER_CAPABILITY_MATRIX_2026-05-22.md`

## Scope / Methodology

Methodology:

- inspect existing Model Gateway provider method contracts and adapter
  literals;
- expand `ProviderMethodName` to cover the Review-CVF method axis;
- preserve legacy `chat` compatibility as an alias of `complete`;
- add a machine-readable `cvf.providerCapability.v1` registry;
- keep `retry`, `cost`, and `risk` as owner references rather than provider
  methods;
- prove positive and negative registry behavior with focused tests.

## Authority Chain

- Original source oracle: `.private_reference/legacy/CVF 17.05/Review CVF.md`
- Assessment:
  `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`
- Roadmap:
  `docs/roadmaps/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINT_ROADMAP_2026-05-22.md`
- GC-018:
  `docs/baselines/CVF_GC018_D2_PROVIDER_CAPABILITY_MATRIX_2026-05-22.md`
- Work order:
  `docs/work_orders/CVF_WO_D2_PROVIDER_CAPABILITY_MATRIX_2026-05-22.md`

## Delivered

- Added canonical Review-CVF method axis:
  `complete`, `stream`, `tool_call`, `reasoning`, `json_mode`, `vision`,
  `embedding`, and `receipt`.
- Retained legacy `chat` as a compatibility alias for `complete`.
- Added `PROVIDER_CAPABILITY_REGISTRY` with bounded current support for:
  Alibaba `qwen-turbo`, Alibaba `qwen-vl-plus`, and DeepSeek
  `deepseek-chat`.
- Added owner references for `retry`, `cost`, and `risk`.
- Added registry-backed lookup, list, method contract, and assertion helpers.
- Updated existing Alibaba stream and DeepSeek JSON mode capability literals
  to include canonical `complete`.
- Added deterministic negative tests for unsupported methods and missing
  provider/model pairs.

## Findings / Position

Finding 1: the Review-CVF D pain point was still partially valid before this
tranche because method support existed, but it was split across adapter and
contract files without one canonical registry.

Finding 2: the current private baseline can now answer "what provider/model
supports which method?" through a single machine-readable surface.

Finding 3: unsupported method attempts now have one registry-backed failure
path using `UnsupportedMethodError`, which prevents ambiguous adapter calls.

Finding 4: D2 should not be overstated. Tool calling, reasoning, embedding, and
receipt methods are declared in the matrix axis but are not claimed as runtime
supported for current providers.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| D2 becomes all-provider parity claim | Registry records only bounded supported pairs |
| Legacy `chat` callers break | Added alias and retained `chat` in supported methods |
| Retry/cost/risk get misclassified as provider methods | Added owner refs and tests excluding them from method axis |
| Unsupported methods leak into adapter calls | Added registry-backed assertion helpers and negative tests |

## Evidence Trace Block

Commit:

```text
e918c690
```

Files changed:

```text
EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts
EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts
EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts
EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/stream-adapter.ts
EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/deepseek/json-mode-adapter.ts
EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts
EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-capability-registry.test.ts
EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-method-coverage.test.ts
```

Focused verification:

```text
npm test -- tests/provider-capability-registry.test.ts tests/provider-method-coverage.test.ts
-> PASS, 2 files / 11 tests

npm run check
-> PASS

npm test
-> PASS, 20 files / 80 tests
```

## Acceptance Criteria Result

| Criterion | Result |
| --- | --- |
| Registry exposes eight Review-CVF provider methods | PASS |
| `retry`, `cost`, and `risk` remain owner refs | PASS |
| Alibaba and DeepSeek have registry contracts | PASS |
| Unsupported methods throw deterministic `UnsupportedMethodError` | PASS |
| Existing adapter tests still pass | PASS |
| No new live provider behavior is claimed | PASS |

## Decision / Recommendation / Disposition

Disposition: `CLOSED_D2_PROVIDER_CAPABILITY_MATRIX`.

Recommendation: continue the post-B/C remaining pain-point roadmap with E2
operational benchmark suite next, using the D2 registry as the provider-method
axis for benchmark fairness.

## Public Catalog Disposition

Public catalog update: `N/A`.

Reason: D2 is a private provenance Model Gateway capability registry and gate
hardening tranche. It adds no public-facing setup, package distribution,
hosted-readiness, or public claim delta.

## Claim Boundary

D2 is closed for provider capability matrix and deterministic unsupported
method behavior in the current private baseline. It does not claim all-provider
parity, broad provider stability, runtime support for every declared method,
route behavior, public-sync, hosted readiness, Maika proof, or freeze release.

Live provider proof was not required or run for this phase because the closed
claim is contract/registry/gate behavior, not new runtime provider execution.
