# CVF Multi-Provider Execution Log - RW1

Memory class: EXECUTION_LOG_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-05-31

Commit range: `21458dab..0256d266` plus closure-sync follow-up.

## Purpose

Record the mixed execution surfaces observed while closing RW1. The RW1 proof
itself used Alibaba `qwen-turbo`; broad full-suite attempts also invoked
unrelated DeepSeek and OpenAI live lanes because live keys were available in
the environment.

## Scope / Target / Owner Boundary

Scope: RW1 closure execution attribution for private provenance work.

Target: `/api/execute` route wire-in, focused RW1 live proof, broad-suite
diagnostics, and closure verification commands.

Owner: CVF session/closure evidence surface.

Boundary: this log does not authorize provider routing, public release,
production readiness, cost optimization claims, or autonomous Learning Plane
mutation.

## Owner And Source

Owner surface: CVF active session evidence and mixed-provider attribution.

Sources: local command output, commit `0256d266`, RW1 focused live receipt
`rcpt-env-mptfzz68-ywcuvn`, completion packet, and full-suite diagnostics.
Evidence basis values: `GIT_VERIFIED`, `TEST_VERIFIED`, `RECEIPT_VERIFIED`,
and `DIFF_VERIFIED`.

## Protocol / Contract / Requirements

The log follows
`docs/reference/CVF_IDE_EXTENSION_MULTI_PROVIDER_EXECUTION_LOG_STANDARD_2026-05-29.md`.
It records provider/model, execution surface, evidence basis, commit range,
quality findings, direct-provider-proof boundary, and cost boundary.

## Enforcement / Verification

Enforcement command: `python governance/compat/check_multi_provider_execution_log.py --base 21458dab --head HEAD --enforce`.

Verification is bounded to the changed range and this session log.

## Related Artifacts

- `docs/baselines/CVF_GC018_RW1_ROUTE_FINDINGTOLEARNING_WIREIN_2026-05-31.md`
- `docs/reviews/CVF_RW1_ROUTE_FINDINGTOLEARNING_WIREIN_COMPLETION_2026-05-31.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.rw1-finding-to-learning.alibaba.live.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`

## Execution Surface Summary

| Lane | Provider/model | Tool surface / invocation surface | Role | Evidence basis | Boundary |
| --- | --- | --- | --- | --- | --- |
| RW1 focused proof | Alibaba `qwen-turbo` | `LOCAL_SHELL` + `VITEST_DIRECT_ROUTE_CALL` to `/api/execute` | Closure proof | `RECEIPT_VERIFIED` receipt `rcpt-env-mptfzz68-ywcuvn` | Authorized execution surface for RW1 only; advisory field proof |
| broad live regression attempt | Alibaba `qwen-turbo` | `LOCAL_SHELL` + `VITEST_FULL_SUITE` | Diagnostic | `TEST_VERIFIED` full-suite output | Mixed unrelated DLP/RT1 failures; not RW1 closure evidence |
| incidental broad live lane | DeepSeek `deepseek-chat` | `LOCAL_SHELL` + `VITEST_FULL_SUITE` | Diagnostic | `TEST_VERIFIED` full-suite output receipts | Not RW1 closure evidence |
| incidental broad live lane | OpenAI `gpt-4o` | `LOCAL_SHELL` + `VITEST_FULL_SUITE` | Diagnostic | `TEST_VERIFIED` full-suite output receipts | Not RW1 closure evidence |
| local non-live regression | N/A | `LOCAL_SHELL` + `VITEST_NON_LIVE_EXCLUDED_LIVE_FILES` | Regression suite | `TEST_VERIFIED` 233 files, 2890 passed, 2 skipped | Mock/non-live regression only |

## Execution Attribution Block

| Artifact or range | Roadmap/order author | Worker/executor | Reviewer/closer | Provider/model | Execution surface | Evidence basis | Attribution boundary |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21458dab..0256d266` RW1 implementation | Operator + RW1 GC-018 | Codex | Codex closure review | Alibaba `qwen-turbo` | `LOCAL_SHELL` / `VITEST_DIRECT_ROUTE_CALL` / `/api/execute` | `GIT_VERIFIED`, `DIFF_VERIFIED`, `RECEIPT_VERIFIED` receipt `rcpt-env-mptfzz68-ywcuvn` | Repo verifies route field and receipt, not provider output quality |
| broad full-suite attempts | N/A | Codex-triggered Vitest | Codex diagnostic classification | Alibaba, DeepSeek, OpenAI | `LOCAL_SHELL` / `VITEST_FULL_SUITE` | `TEST_VERIFIED` command output | Diagnostics only; not RW1 closure proof |
| non-live regression suite | N/A | Codex-triggered Vitest | Codex | N/A | `LOCAL_SHELL` / `VITEST_NON_LIVE_EXCLUDED_LIVE_FILES` | `TEST_VERIFIED` 233 files, 2890 passed, 2 skipped | Regression proof, not live governance proof |

## Commit Evidence

| Commit / range | Files changed | Evidence basis | Boundary |
| --- | --- | --- | --- |
| `0256d266` | route.ts, RW1 live test, RW1 GC-018 | `GIT_VERIFIED` committed diff + pre-commit hook PASS | Implementation only; closure sync follows separately |
| `21458dab..0256d266` | RW1 implementation range | `DIFF_VERIFIED` pre-closure committed range evidence | Does not include unrelated untracked CLI evidence file |

## Quality Findings

| Finding | Disposition | Next control action |
| --- | --- | --- |
| RW1 targeted rerun timed out at 30000ms | RETRY_RESOLVED | Timeout raised to 60000ms; rerun passed with receipt. |
| Broad live DLP test still sees raw PII in serialized response body | OUT_OF_SCOPE_FINDING_RECORDED | Separate DLP hardening tranche required before closure claim. |
| Broad live RT1 test returned `success=false` once | OUT_OF_SCOPE_PROVIDER_VARIANCE | Separate RT1 stability rerun if operator requests it. |
| `npm run check` fails on pre-existing live-test `Request` vs `NextRequest` typings | OUT_OF_SCOPE_TYPECHECK_DEBT | Separate test typing cleanup tranche required. |

## Finding-To-Governance Learning Disposition

| Finding group | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| `/api/execute` lacked finding-to-learning advisory field | RULE_GAP | GOVERNANCE_CONTROL_PLANE | RULE_ADDED | RW1 closed; future ledger write needs separate R2-R3 GC-018 |
| Broad live DLP assertion still sees raw PII in serialized response | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | RUNTIME_LEARNING_CANDIDATE | Separate DLP hardening tranche if operator authorizes |
| `npm run check` live-test type errors | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Separate test typing cleanup tranche |

## Direct-Provider-Proof Boundary

The RW1 direct route proof demonstrates that `/api/execute` returns
`findingToLearningReadout` with `autonomousMutationAuthorized=false` for one
live Alibaba `qwen-turbo` ALLOW response. It does not prove provider quality,
cost optimization, hosted readiness, production readiness, universal
multi-provider parity, or feedback-ledger mutation.

## Cost And ROI Boundary

Live quota was consumed by the focused RW1 proof and by broad full-suite live
tests that ran because provider keys were present. Token counts and exact costs
are unknown because this tranche did not produce a token/cost ledger. Cost
source is therefore `UNKNOWN_NOT_CLAIMED`.

Only the focused RW1 receipt is used as closure evidence. Broad provider outputs
are diagnostics and are not used to claim quality, cost efficiency, ROI, or
provider superiority.

## Claim Boundary

This log is an attribution record only. It does not authorize new provider
behavior, public release claims, or autonomous Learning Plane mutation.
