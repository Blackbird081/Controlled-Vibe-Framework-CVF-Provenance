# CVF ASCP-T5 Package Use-Proof Adapter Corrective Review

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: completion_review

Batch ID: ASCP-T5-CORRECTIVE

## Purpose

Close the operator-requested corrective patch for two ASCP-T5 defects:

- nested live-run helpers could falsely report missing provider keys when they
  failed to import the repo-local env loader;
- ASCP-T5 defaulted to a legacy provider model instead of the current Alibaba
  free-quota model ledger.

## Scope / Methodology

Changed scope:

- shared live-provider env bootstrap helper;
- shared ASSF live model-selection helper;
- ASCP-T5 use-proof adapter model selection and diagnostics;
- focused unit tests for env bootstrap, auto model selection, and legacy-model
  denial;
- ASCP-T5 use-proof adapter standard.

Out of scope:

- package lifecycle promotion to `ACTIVE`;
- provider registry mutation;
- remaining package conversion;
- public-sync;
- MCP server runtime behavior;
- raw API-key disclosure.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: operator authorized a narrow corrective
patch for live-provider env bootstrap and package use-proof model selection;
scope is limited to ASCP-T5 helper behavior, its tests, and its standard.

Protected paths:

- `governance/compat/live_provider_bootstrap.py`
- `governance/compat/assf_live_model_selection.py`
- `governance/compat/test_live_provider_bootstrap.py`
- `governance/compat/run_assf_package_use_proof_adapter.py`
- `governance/compat/test_run_assf_package_use_proof_adapter.py`

Operator authorization: operator requested fixing the two findings and rerunning
live proof with a different model on 2026-06-30.

Rollback boundary: revert only this corrective patch if rejected; do not revert
ASCP-T1 through ASCP-T5 closures, package roots, generated ASSF index, truth
packets, or unrelated session-sync commits.

## Findings / Position

| Finding | Corrective disposition |
|---|---|
| False missing-key diagnostic from nested helper imports | PASS: `governance/compat/live_provider_bootstrap.py` inserts repo root before importing `scripts._local_env`; live smoke loaded the repo-local cvf-web env file |
| Legacy default model used for free-quota live proof | PASS: adapter default is now `AUTO_FROM_ALIBABA_FREE_QUOTA_LEDGER`; explicit `qwen-turbo` returns `MODEL_FREE_QUOTA_NOT_VERIFIED` before package body read or provider call |
| Need fresh live proof using a current ledger model | PASS: live rerun used `qwen3.6-flash-2026-04-16`, HTTP 200, receipt `sha256:435388ae0860a0a61f33dc4db7d7472990c0080be19d6e5158ed89a053f5aa9b` |

The prior ASCP-T5 `qwen-turbo` evidence remains a live provider-call record, but
this corrective review supersedes it as free-quota model-selection evidence for
future package use-proof claims.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| Future helpers again fail to import `scripts._local_env` from nested directories | shared helper inserts repo root before importing the canonical env bootstrap |
| Legacy provider capability entries are reused as current free-quota defaults | model selection reads the ledger `models` array and emits `MODEL_FREE_QUOTA_NOT_VERIFIED` for absent models |
| Slow model causes repeated unclassified live reruns | timeout result was captured as `provider_call` `TimeoutError`; retry used a different current ledger model |
| Corrective patch expands into lifecycle or provider registry mutation | changed set excludes package lifecycle sources and provider registry source |

## Finding-To-Governance Learning Disposition

Defect class: `RUNTIME_SIGNAL_GAP`

Learning lane: `RUNTIME_BEHAVIOR_LEARNING`

Disposition: `STANDARD_UPDATED`

Next action: retain the shared helpers, focused tests, and ASCP-T5 standard
guard as the governing regression for future package use-proof live runs.

runtime/provider/cost learning lane: `RUNTIME_BEHAVIOR_LEARNING`

| Field | Value |
|---|---|
| Finding-bearing artifact | yes |
| Finding type | repeated live-provider env bootstrap and stale model-selection default |
| Governance learning disposition | STANDARD_UPDATED |
| Generalizable finding promotion | STANDARD_UPDATED |
| ADIF entry required | N/A_WITH_REASON: defect is fixed directly in the active helper, standard, and tests; recurrence threshold for a separate ADIF entry is not claimed in this corrective patch |
| Durable guardrail | shared helpers, focused tests, and ASCP-T5 standard model-selection guard |

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Nested helper could miss repo-local env keys | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | STANDARD_UPDATED | shared env bootstrap helper plus unit test retained | handled |
| Legacy provider model could be selected outside free-quota ledger authority | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | STANDARD_UPDATED | model selector helper plus standard guard retained | handled |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Repo-local env loader reads configured local env files | `scripts/_local_env.py` | `DEFAULT_ENV_FILES`; `bootstrap_repo_env` | `DEFAULT_ENV_FILES` | repo env bootstrap | RUNTIME_BEHAVIOR | ACCEPT |
| Alibaba free-quota live tests must use ledger expiration rules | `docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.md` | `Use-Before-Live-Test Rule` | `MODEL_FREE_QUOTA_NOT_VERIFIED` | Alibaba free-quota ledger | LITERAL_INVARIANT | ACCEPT |
| Machine-readable free-quota models are under the JSON `models` array | `docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.json` | `models` | `modelCode`; `expirationDate`; `freeQuotaRemaining` | Alibaba free-quota ledger JSON | VALUE_SET | ACCEPT |
| ASCP-T5 adapter is the corrected package use-proof surface | `governance/compat/run_assf_package_use_proof_adapter.py` | `build_package_use_proof_packet` | `modelSelection`; `safeLoadedEnvFiles`; `packageUseProofReceipt` | package use-proof adapter | RUNTIME_BEHAVIOR | ACCEPT |
| Shared helper controls repo-root import bootstrap for live-provider helpers | `governance/compat/live_provider_bootstrap.py` | `ensure_repo_root_on_sys_path`; `bootstrap_live_provider_env` | `sys.path`; `scripts._local_env` | live provider bootstrap helper | RUNTIME_BEHAVIOR | ACCEPT |
| Shared model selector controls free-quota model eligibility | `governance/compat/assf_live_model_selection.py` | `resolve_free_quota_model` | `AUTO_FROM_ALIBABA_FREE_QUOTA_LEDGER`; `MODEL_FREE_QUOTA_USABLE` | ASSF live model selection helper | RUNTIME_BEHAVIOR | ACCEPT |

## Verification / Evidence

| Evidence | Observed result |
|---|---|
| `python -m unittest governance.compat.test_live_provider_bootstrap governance.compat.test_run_assf_package_use_proof_adapter` | PASS, 8 tests |
| `python governance/compat/run_assf_package_use_proof_adapter.py --skill-id cvf-engineering-spec-driven-development --json` | PASS, auto-selected `qwen3.7-plus`, `MODEL_FREE_QUOTA_USABLE`, dry-run ready |
| `python governance/compat/run_assf_package_use_proof_adapter.py --skill-id cvf-engineering-spec-driven-development --model qwen-turbo --live --json` | PASS expected denial, `MODEL_FREE_QUOTA_NOT_VERIFIED`, repo-local env file loaded, no package read |
| `python governance/compat/run_assf_package_use_proof_adapter.py --skill-id cvf-engineering-spec-driven-development --live --json --receipt-out .cvf/runtime/assf-use-proof/ascp-t5-live-proof-qwen37plus.json` | Diagnostic captured, `provider_call` `TimeoutError`, retryable |
| `python governance/compat/run_assf_package_use_proof_adapter.py --skill-id cvf-engineering-spec-driven-development --model qwen3.6-flash-2026-04-16 --live --timeout-seconds 90 --json --receipt-out .cvf/runtime/assf-use-proof/ascp-t5-live-proof-qwen36flash.json` | PASS, `LIVE_PROVIDER_USE_PROOF_PASS`, HTTP 200, latency 14438 ms |

## Live Run Diagnostic Record

| Field | Value |
|---|---|
| Stage | provider_response |
| Class | PASS |
| Retryable | false |
| User action | N/A with reason: live proof passed on retry with a current ledger model |
| Provider | alibaba-dashscope |
| Model | qwen3.6-flash-2026-04-16 |
| Model ledger status | MODEL_FREE_QUOTA_USABLE |
| Expiration date | 2026-07-16 |
| HTTP status | 200 |
| Latency ms | 14438 |
| Credential source | DASHSCOPE_API_KEY |
| Env file loaded | repo-local cvf-web env file |
| Receipt id | `sha256:435388ae0860a0a61f33dc4db7d7472990c0080be19d6e5158ed89a053f5aa9b` |
| Trace id | `c614e5ea-492d-924b-82d0-51b0bcddac89` |
| Evidence file hash | `sha256:c44baadc5cdf909712b0262f1d7deb0d05692598d360365cb0817bbe04a00348` |
| Safe message | Live provider use-proof passed; raw API key was not printed |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | USED_WITH_RECEIPT |
| CVF skill id | `cvf-engineering-spec-driven-development` |
| Package root | `docs/reference/agent_system_skills/packages/cvf-engineering-spec-driven-development/SKILL.md` |
| Invocation context | ASCP-T5 corrective live use-proof adapter smoke |
| Receipt evidence | `sha256:aa4e26d13ccd75475431e434ef1bd304f20d3b72d77f95a4726fdf6038f2455f` |
| Output consumed by CVF | package-use proof receipt and live output hash only |
| Truth packet or source path | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Authority boundary | skill usage receipt does not grant authority, activate package lifecycle state, or bypass work-order scope |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace plus Alibaba DashScope-compatible live model |
| Session or invocation | ASCP-T5 corrective patch on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | apply_patch; Python unittest; dry-run smoke; denied-model smoke; live provider proof |
| Target paths | `governance/compat/live_provider_bootstrap.py`; `governance/compat/assf_live_model_selection.py`; `governance/compat/test_live_provider_bootstrap.py`; `governance/compat/run_assf_package_use_proof_adapter.py`; `governance/compat/test_run_assf_package_use_proof_adapter.py`; `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_USE_PROOF_ADAPTER_STANDARD.md`; this corrective review |
| Allowed scope source | operator instruction to fix two findings and rerun live proof with a different model |
| Before status evidence | base commit `60b9b981`; clean worktree before corrective patch |
| After status evidence | corrective changed set only |
| Diff evidence | `git diff --name-status`; focused unit tests; dry-run smoke; denied-model smoke; live proof |
| Approval boundary | operator authorized live API-key use; raw keys were not printed |
| Claim boundary | bounded internal package use-proof correction only |
| Agent type | implementer/reviewer/closer |
| Invocation ID | `cvf-ascp-t5-package-use-proof-corrective-2026-06-30` |
| Expected manifest | env helper, model selector, helper test, adapter, adapter test, standard update, corrective review |
| Actual changed set | env helper, model selector, helper test, adapter, adapter test, standard update, corrective review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this corrective review references private ASSF package runtime and
live-provider proof. Public-safe export requires separate public-sync
authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: operator-authorized corrective patch without a separate work order | operator instruction in current session; this corrective review records bounded closure | PASS |
| Completion or reviewer artifact | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | `Status: ACTIVE_ROADMAP`; corrective patch does not close or reopen roadmap state | PASS |
| Registry JSON | no ASSF registry JSON mutation required for this corrective patch | source mutation list remains empty | PASS |
| Registry Markdown | no registry markdown mutation required for this corrective patch | source mutation list remains empty | PASS |
| External evidence digest | `.cvf/runtime/assf-use-proof/ascp-t5-live-proof-qwen36flash.json` | `sha256:c44baadc5cdf909712b0262f1d7deb0d05692598d360365cb0817bbe04a00348` | PASS |
| System loop interlock | N/A with reason: no system-loop registry or runtime loop source changed | no interlock mutation | N/A with reason |
| Session continuity | active session front-door/state/handoff after material commit | no next-move change claimed by material corrective patch; session-sync may follow if needed | N/A with reason |
| Env bootstrap helper | `governance/compat/live_provider_bootstrap.py` | unit test import bootstrap PASS | PASS |
| Model selection helper | `governance/compat/assf_live_model_selection.py` | adapter unit tests cover auto and denied model paths | PASS |
| Use-proof adapter | `governance/compat/run_assf_package_use_proof_adapter.py` | live proof returned `LIVE_PROVIDER_USE_PROOF_PASS` with current ledger model | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Live proof disposition | `LIVE_PROVIDER_USE_PROOF_PASS` | `LIVE_PROVIDER_USE_PROOF_PASS` | PASS |
| Live proof model | current ledger model, not `qwen-turbo` | `qwen3.6-flash-2026-04-16` | PASS |
| Model ledger status | `MODEL_FREE_QUOTA_USABLE` | `MODEL_FREE_QUOTA_USABLE` | PASS |
| Env file loading | repo-local env file loaded without printing key | cvf-web local env file | PASS |
| Use-proof receipt | present | `sha256:435388ae0860a0a61f33dc4db7d7472990c0080be19d6e5158ed89a053f5aa9b` | PASS |
| Legacy model denial | `MODEL_FREE_QUOTA_NOT_VERIFIED` | `MODEL_FREE_QUOTA_NOT_VERIFIED` | PASS |

## Claim Boundary

This corrective patch fixes ASCP-T5 live-provider env bootstrap and
free-quota model selection only. It does not activate package lifecycle state,
convert remaining packages, mutate provider registry source, implement MCP
runtime behavior, public-sync, or claim production readiness.
