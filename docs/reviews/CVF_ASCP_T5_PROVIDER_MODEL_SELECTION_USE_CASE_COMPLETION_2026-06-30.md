# CVF ASCP-T5 Provider Model Selection Use Case Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: completion_review

Batch ID: ASCP-T5-PROVIDER-MODEL-USE-CASE

## Purpose

Close the operator-authorized small Model Gateway use case for ASCP-T5:
upgrade the bounded package use-proof adapter from model-only selection to
provider-and-model selection without opening a production Model Gateway or
model router roadmap.

## Scope / Methodology

Changed scope:

- ASCP-T5 live provider/model selector;
- ASCP-T5 package use-proof adapter provider/model output fields;
- focused tests for auto provider, provider alias normalization, unsupported
  provider denial, and Windows-safe JSON output;
- ASCP-T5 package use-proof adapter standard.

Out of scope:

- production Model Gateway or model router implementation;
- multi-provider fallback;
- provider registry mutation;
- new credential source mutation;
- package lifecycle promotion to `ACTIVE`;
- public-sync.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: operator authorized a narrow ASCP-T5 Model
Gateway use case for provider/model auto-selection while keeping the production
Model Gateway and model router roadmap separate.

Protected paths:

- `governance/compat/assf_live_model_selection.py`
- `governance/compat/run_assf_package_use_proof_adapter.py`
- `governance/compat/test_run_assf_package_use_proof_adapter.py`

Operator authorization: operator approved upgrading the selector as a small
Model Gateway use case, not a full Model Gateway/model-router roadmap.

Rollback boundary: revert only this ASCP-T5 provider/model use-case patch if
rejected; do not revert ASCP-T5 corrective commit `09656d16`, session sync
`d9e6467d`, package roots, truth packets, generated ASSF index, or unrelated
session history.

## Findings / Position

| Finding | Disposition |
|---|---|
| ASCP-T5 selector could choose model but provider remained an implicit constant | PASS: selector now resolves provider and model together |
| Full Model Gateway/model router would be too broad for this tranche | PASS: output includes ASCP-T5 use-case boundary and denies unsupported providers before package read |
| Windows stdout could fail on non-ASCII provider output | PASS: CLI JSON and receipt files now use ASCII-safe JSON serialization |
| Live proof should prove auto provider plus auto model | PASS: live proof selected `alibaba-dashscope` plus `deepseek-v4-flash` and returned HTTP 200 |

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| ASCP-T5 use-case selector mistaken for production router | packet emits `selectionBoundary` stating it is not a production model router |
| Unsupported provider falls through to wrong credential path | unsupported provider returns `PROVIDER_NOT_SOURCE_BACKED_FOR_ASSF_USE_CASE` before package body read or provider call |
| Model choice drifts back to stale default | auto model selection remains ledger-backed and rejects absent or expired models |
| CLI live proof fails after successful provider call because of Windows encoding | JSON output now uses `ensure_ascii=True` and test encodes result with cp1252 |

## Finding-To-Governance Learning Disposition

Defect class: `RUNTIME_SIGNAL_GAP`

Learning lane: `RUNTIME_BEHAVIOR_LEARNING`

Disposition: `STANDARD_UPDATED`

Next action: keep this ASCP-T5 use case as a bounded consumer pattern for the
future independent Model Gateway/model router roadmap.

runtime/provider/cost learning lane: `RUNTIME_BEHAVIOR_LEARNING`

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Provider was implicit while model was explicit | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | STANDARD_UPDATED | selector now returns provider/model selection metadata | handled |
| Full router scope must remain separate | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_UPDATED | ASCP-T5 standard states use-case boundary only | handled |
| Windows stdout can fail on non-ASCII provider output | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | STANDARD_UPDATED | ASCII-safe JSON output and regression test | handled |

Generalizable finding promotion: `STANDARD_UPDATED`

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASCP-T5 selector resolves provider and model together | `governance/compat/assf_live_model_selection.py` | `resolve_provider_model` | `AUTO_FROM_ASSF_LIVE_PROVIDER_CANDIDATES`; `PROVIDER_NOT_SOURCE_BACKED_FOR_ASSF_USE_CASE` | ASCP live provider/model selector | RUNTIME_BEHAVIOR | ACCEPT |
| ASCP-T5 adapter emits provider/model selection metadata | `governance/compat/run_assf_package_use_proof_adapter.py` | `build_package_use_proof_packet` | `providerSelection`; `modelSelection` | package use-proof adapter | RUNTIME_BEHAVIOR | ACCEPT |
| ASCP-T5 adapter JSON output is ASCII-safe | `governance/compat/run_assf_package_use_proof_adapter.py` | `main` | `ensure_ascii` | package use-proof adapter CLI | RUNTIME_BEHAVIOR | ACCEPT |
| Alibaba free-quota model list remains the model source of truth for this use case | `docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.json` | `models` | `modelCode`; `expirationDate`; `freeQuotaRemaining` | Alibaba free-quota ledger | VALUE_SET | ACCEPT |
| ASCP-T5 standard records use-case boundary | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_USE_PROOF_ADAPTER_STANDARD.md` | `Live Model Selection Guard` | `AUTO_FROM_ASSF_LIVE_PROVIDER_CANDIDATES`; `selectionBoundary` | ASCP-T5 standard | LITERAL_INVARIANT | ACCEPT |

## Verification / Evidence

| Evidence | Observed result |
|---|---|
| `python -m unittest governance.compat.test_live_provider_bootstrap governance.compat.test_run_assf_package_use_proof_adapter` | PASS, 11 tests |
| `python -m py_compile governance/compat/assf_live_model_selection.py governance/compat/run_assf_package_use_proof_adapter.py governance/compat/test_run_assf_package_use_proof_adapter.py` | PASS |
| `python governance/compat/run_assf_package_use_proof_adapter.py --skill-id cvf-engineering-spec-driven-development --json` | PASS, auto-selected provider `alibaba-dashscope` and model `deepseek-v4-flash` |
| `python governance/compat/run_assf_package_use_proof_adapter.py --skill-id cvf-engineering-spec-driven-development --provider deepseek --live --json` | PASS expected denial, `PROVIDER_NOT_SOURCE_BACKED_FOR_ASSF_USE_CASE`, no package read |
| `python governance/compat/run_assf_package_use_proof_adapter.py --skill-id cvf-engineering-spec-driven-development --live --timeout-seconds 90 --json --receipt-out .cvf/runtime/assf-use-proof/ascp-t5-live-proof-auto-provider-model.json` | PASS, `LIVE_PROVIDER_USE_PROOF_PASS`, HTTP 200, latency 11031 ms |

## Live Run Diagnostic Record

| Field | Value |
|---|---|
| Stage | provider_response |
| Class | PASS |
| Retryable | false |
| User action | N/A with reason: live proof passed |
| Provider | alibaba-dashscope |
| Model | deepseek-v4-flash |
| Provider status | PROVIDER_USABLE |
| Model ledger status | MODEL_FREE_QUOTA_USABLE |
| HTTP status | 200 |
| Latency ms | 11031 |
| Credential source | DASHSCOPE_API_KEY |
| Env file loaded | repo-local cvf-web env file |
| Receipt id | `sha256:db51ca20b1967d95b5cc209185ffabd41b22adfbabe61b428cc6314ad1d3c0f1` |
| Trace id | `6a62e1fc-b6a6-978d-a961-fa2456f80e43` |
| Evidence file hash | `sha256:3a1b06ffd6d6366fe3bd471e7b160716ef553a6eb6fc69679bbf774de7ea5221` |
| Safe message | Auto provider/model use-proof passed; raw API key was not printed |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | USED_WITH_RECEIPT |
| CVF skill id | `cvf-engineering-spec-driven-development` |
| Package root | `docs/reference/agent_system_skills/packages/cvf-engineering-spec-driven-development/SKILL.md` |
| Invocation context | ASCP-T5 provider/model selection use-case live proof |
| Receipt evidence | `sha256:aa4e26d13ccd75475431e434ef1bd304f20d3b72d77f95a4726fdf6038f2455f` |
| Output consumed by CVF | package-use proof receipt and live output hash only |
| Truth packet or source path | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Authority boundary | skill usage receipt does not grant authority, activate package lifecycle state, or bypass work-order scope |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace plus Alibaba DashScope-compatible live model |
| Session or invocation | ASCP-T5 provider/model selection use case on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | apply_patch; Python unittest; dry-run smoke; denied-provider smoke; live provider proof |
| Target paths | `governance/compat/assf_live_model_selection.py`; `governance/compat/run_assf_package_use_proof_adapter.py`; `governance/compat/test_run_assf_package_use_proof_adapter.py`; `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_USE_PROOF_ADAPTER_STANDARD.md`; this completion review |
| Allowed scope source | operator instruction to treat provider/model auto-selection as a small ASCP-T5 Model Gateway use case |
| Before status evidence | base commit `d9e6467d`; clean worktree before use-case patch |
| After status evidence | provider/model use-case changed set only |
| Diff evidence | `git diff --name-status`; focused unit tests; dry-run smoke; denied-provider smoke; live proof |
| Approval boundary | operator authorized bounded use-case upgrade; raw keys were not printed |
| Claim boundary | bounded ASCP-T5 Model Gateway use case only |
| Agent type | implementer/reviewer/closer |
| Invocation ID | `cvf-ascp-t5-provider-model-selection-use-case-2026-06-30` |
| Expected manifest | selector, adapter, adapter tests, standard update, completion review |
| Actual changed set | selector, adapter, adapter tests, standard update, completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this completion review references private ASSF package runtime and
live-provider proof. Public-safe export requires separate public-sync
authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: operator-authorized small use-case patch without a separate work order | operator instruction in current session; this completion review records bounded closure | PASS |
| Completion or reviewer artifact | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | use-case patch does not close or reopen roadmap state | PASS |
| Registry JSON | no ASSF registry JSON mutation required for this use-case patch | source mutation list remains empty | PASS |
| Registry Markdown | no registry markdown mutation required for this use-case patch | source mutation list remains empty | PASS |
| External evidence digest | `.cvf/runtime/assf-use-proof/ascp-t5-live-proof-auto-provider-model.json` | `sha256:3a1b06ffd6d6366fe3bd471e7b160716ef553a6eb6fc69679bbf774de7ea5221` | PASS |
| System loop interlock | N/A with reason: no system-loop registry or runtime loop source changed | no interlock mutation | N/A with reason |
| Session continuity | active session front-door/state/handoff after material commit | session-sync may follow if mode or next move changes | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Provider selection | source-backed provider candidate | `alibaba-dashscope` | PASS |
| Model selection | unexpired ledger model | `deepseek-v4-flash` | PASS |
| Unsupported provider handling | deny before package read | `PROVIDER_NOT_SOURCE_BACKED_FOR_ASSF_USE_CASE` | PASS |
| Live proof disposition | `LIVE_PROVIDER_USE_PROOF_PASS` | `LIVE_PROVIDER_USE_PROOF_PASS` | PASS |
| Use-proof receipt | present | `sha256:db51ca20b1967d95b5cc209185ffabd41b22adfbabe61b428cc6314ad1d3c0f1` | PASS |
| Router boundary | no production model router claim | `selectionBoundary` states ASCP-T5 use case only | PASS |

## Claim Boundary

This patch upgrades ASCP-T5 package use-proof selection from model-only to
provider-and-model selection for a bounded Model Gateway use case. It does not
implement production Model Gateway routing, multi-provider fallback, provider
registry mutation, new credential management, package lifecycle activation,
external MCP runtime behavior, public-sync, or production readiness.
