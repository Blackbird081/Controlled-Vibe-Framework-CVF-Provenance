# CVF GC-018 Baseline: ASCP-T5 Package Execution Use-Proof Adapter

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: baseline

Batch ID: ASCP-T5

dispatchBaseHead: 52d0787b

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | implement a bounded package execution/use-proof adapter before any ACTIVE lifecycle promotion |
| Baseline | ASCP-T1 through ASCP-T4 prove readiness, policy semantics, external projection, and no lifecycle source mutation |
| Proposed tranche | add ASCP-T5 standard, helper, tests, live provider proof, roadmap update, work order, and completion review |
| Execution route | Codex direct implementation with reviewer-owned closure |
| Closure posture | CLOSED_PASS_BOUNDED after focused tests and one live provider proof |

## Purpose

ASCP-T5 proves that a CVF runtime package can be used with inspectable
evidence before any package source is promoted to `ACTIVE`.

The tranche implements `governance/compat/run_assf_package_use_proof_adapter.py`.
It loads one runtime-eligible package through the existing loader, captures the
`CVF_ASSF_SKILL_USAGE_RECEIPT`, confirms activation-policy
`USED_WITH_RECEIPT`, calls a live provider when `--live` is used, and emits
`CVF_ASSF_PACKAGE_USE_PROOF_RECEIPT`.

## Scope / Methodology

Allowed ASCP-T5 scope:

- add `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_USE_PROOF_ADAPTER_STANDARD.md`;
- add `governance/compat/run_assf_package_use_proof_adapter.py`;
- add `governance/compat/test_run_assf_package_use_proof_adapter.py`;
- update the ASCP roadmap row from value-parked to closed bounded because the
  operator explicitly reopened ASCP-T5 for package execution/use-proof;
- file baseline, work order, and completion evidence;
- run one live provider proof using existing secret-safe environment loading.

Forbidden ASCP-T5 scope:

- package lifecycle mutation to `ACTIVE`;
- ASSF registry entry edits or generated skill-index regeneration;
- remaining package conversion;
- automatic package invocation;
- MCP server, daemon, hook, IDE bridge, or public adapter runtime behavior;
- provider registry mutation;
- public-sync or production-readiness claims.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`,
lifecyclePhase=`implementation`, surfaceSelector=`docs/reference/agent_system_skills`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure command:

```text
python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase implementation --surface-selector docs/reference/agent_system_skills --risk-ceiling HIGH --max-results 20 --json
```

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Runtime loader reads package bodies only after explicit eligible body request and emits usage receipts | `governance/compat/run_assf_runtime_package_loader.py` | `_build_skill_usage_receipt`; `build_runtime_package_packet` | `skillUsageReceipts` | runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Activation policy resolver classifies consumed output with matching receipt as `USED_WITH_RECEIPT` | `governance/compat/run_assf_activation_policy_resolver.py` | `_state_for`; `build_activation_policy_packet` | `USED_WITH_RECEIPT` | activation policy resolver | RUNTIME_BEHAVIOR | ACCEPT |
| ASSF package contract keeps lifecycle activation separate from adapter behavior | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields; Provider Adapter Boundary | `ACTIVE`; `adapterContract` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Live key loader accepts repo env files without printing raw keys | `scripts/_local_env.py` | `DEFAULT_ENV_FILES`; `bootstrap_repo_env` | `DEFAULT_ENV_FILES` | repo env bootstrap | RUNTIME_BEHAVIOR | ACCEPT |
| Alibaba env source lists accepted DashScope-compatible aliases | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/alibaba-env.ts` | `keyCandidates` | `DASHSCOPE_API_KEY`; `ALIBABA_API_KEY`; `CVF_ALIBABA_API_KEY`; `CVF_BENCHMARK_ALIBABA_KEY` | Alibaba env source | VALUE_SET | ACCEPT |
| Provider capability registry includes Alibaba `qwen-turbo` completion capability | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | `PROVIDER_CAPABILITY_REGISTRY` | `qwen-turbo` | Model Gateway provider capability registry | VALUE_SET | ACCEPT |
| Live run diagnostic standard requires secret-safe failure diagnostics | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | Required Diagnostic Record | `stage`; `class`; `retryable`; `safeMessage` | live run diagnostic standard | LITERAL_INVARIANT | ACCEPT |
| Package use-proof adapter is new in ASCP-T5 | `governance/compat/run_assf_package_use_proof_adapter.py` | ASCP-T5 new file | `build_package_use_proof_packet` | package use-proof adapter | DOC_ONLY_NEW | ACCEPT |

## Provider Registry Boundary

ASCP-T5 uses the existing Alibaba/DashScope live provider surface for one
bounded proof. It does not mutate provider registry code, add hardcoded routing
policy, claim provider parity, or promote provider output into canonical
source authority. Current provider registry surfaces remain accounted for:
`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` exports
`ProviderRegistry`, and `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
declares `PROVIDER_CAPABILITY_REGISTRY`.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one bounded use-proof helper and
focused tests under `governance/compat`.

Protected paths:

- `governance/compat/run_assf_package_use_proof_adapter.py`
- `governance/compat/test_run_assf_package_use_proof_adapter.py`

Operator authorization: active instruction reopens ASCP-T5 for package
execution/use-proof before any ACTIVE lifecycle promotion.

Rollback boundary: if ASCP-T5 is rejected, remove only the ASCP-T5 helper,
tests, standard, artifacts, and roadmap update. Do not revert ASCP-T1 through
ASCP-T4, SKUSE-T1, truth packets, package roots, or previous session-sync
commits.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASCP roadmap, ASSF package contract, use-proof standard, runtime loader, activation policy resolver, provider env loader, provider capability registry, live diagnostic standard |
| Runtime behavior claimed | bounded package use-proof adapter with receipt-backed live proof |
| Live/provider proof claimed | YES - one Alibaba DashScope-compatible `qwen-turbo` live call |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - current sources support use-proof adapter only, not lifecycle promotion |

## Evidence / Verification

| Evidence | Required or observed result |
|---|---|
| Focused unit tests | `python -m unittest governance.compat.test_run_assf_package_use_proof_adapter` PASS, 5 tests |
| Focused regression tests | `python -m unittest governance.compat.test_run_assf_runtime_package_loader governance.compat.test_run_assf_activation_policy_resolver governance.compat.test_run_assf_package_use_proof_adapter` PASS, 20 tests |
| Dry-run smoke | `python governance/compat/run_assf_package_use_proof_adapter.py --skill-id cvf-engineering-spec-driven-development --json` returned `DRY_RUN_READY_FOR_LIVE_PROVIDER_USE_PROOF` and `USED_WITH_RECEIPT` |
| Live provider proof | `python governance/compat/run_assf_package_use_proof_adapter.py --skill-id cvf-engineering-spec-driven-development --live --json --receipt-out .cvf/runtime/assf-use-proof/ascp-t5-live-proof.json` returned `LIVE_PROVIDER_USE_PROOF_PASS`, HTTP 200, latency 2162 ms |
| Live proof receipt | `sha256:f67bd3331f81e088c2f75f7287db0fce60508abbc89cd7099481e5e86aeaa7dc` |
| Skill usage receipt | `sha256:aa4e26d13ccd75475431e434ef1bd304f20d3b72d77f95a4726fdf6038f2455f` |
| Policy receipt | `sha256:e51e3a291282f0cfc700543ed120e4d7d778d85f1197e80b514db9a46e99ed5f` |
| Live response hash | `sha256:5994ea4c7a45664a6e6d35ff67f7e41f6f0b6bbd28bd61cd4b6855ccf7c295a6` |
| Live output hash | `sha256:d50c44e5dc269b11ad99002ced625a76c077c08dc309ad698385be0fcb535896` |
| Changed set review | no ASSF registry, generated index, truth packet, package root, provider registry, or public-sync mutation |

## Artifact Manifest

| Artifact | Status |
|---|---|
| `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_USE_PROOF_ADAPTER_STANDARD.md` | CREATED |
| `governance/compat/run_assf_package_use_proof_adapter.py` | CREATED |
| `governance/compat/test_run_assf_package_use_proof_adapter.py` | CREATED |
| `docs/baselines/CVF_GC018_ASCP_T5_PACKAGE_EXECUTION_USE_PROOF_ADAPTER_2026-06-30.md` | CREATED |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T5_PACKAGE_EXECUTION_USE_PROOF_ADAPTER_2026-06-30.md` | CREATED |
| `docs/reviews/CVF_ASCP_T5_PACKAGE_EXECUTION_USE_PROOF_ADAPTER_COMPLETION_2026-06-30.md` | CREATED |
| `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | UPDATED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | package use-proof adapter | may run one explicit receipt-backed package use proof | ASCP-T5 tests and live proof | no lifecycle mutation | `IMPLEMENTED_BOUNDED_USE_PROOF_ADAPTER` |
| `INTERNAL_AGENT` | runtime package loader | may open eligible package bodies only after explicit body-read request | ASCP-T1/T2/T5 evidence | no lifecycle promotion | `IMPLEMENTED_BOUNDED_BODY_READ` |
| `EXTERNAL_AGENT_CLI_MCP` | CLI/MCP projection helper | metadata and policy-state readout only | ASCP-T3 tests and smoke | external body reads and output use denied | `IMPLEMENTED_BOUNDED_PROJECTION` |
| `EXTERNAL_AGENT_CLI_MCP` | package execution adapter | no external MCP package execution authorized | N/A with reason: ASCP-T5 is internal local helper only | separate MCP runtime work order required | `DEFERRED_WITH_REASON` |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Helper loads exactly one eligible package through runtime loader | unit tests and dry-run smoke PASS |
| AC2 | Helper records matching `CVF_ASSF_SKILL_USAGE_RECEIPT` | dry-run and live proof PASS |
| AC3 | Helper classifies consumed output as `USED_WITH_RECEIPT` before provider use | unit tests, dry-run, and live proof PASS |
| AC4 | Helper emits live run diagnostic on missing key or provider failure | unit tests PASS |
| AC5 | Live provider proof emits `CVF_ASSF_PACKAGE_USE_PROOF_RECEIPT` | live proof PASS |
| AC6 | Helper does not authorize lifecycle mutation or source mutations | unit tests and output PASS |
| AC7 | Roadmap records ASCP-T5 closed bounded and still blocks ACTIVE promotion | roadmap update PASS |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | USED_WITH_RECEIPT |
| CVF skill id | `cvf-engineering-spec-driven-development` |
| Package root | `docs/reference/agent_system_skills/packages/cvf-engineering-spec-driven-development/SKILL.md` |
| Invocation context | ASCP-T5 live use-proof adapter smoke |
| Receipt evidence | `sha256:aa4e26d13ccd75475431e434ef1bd304f20d3b72d77f95a4726fdf6038f2455f` |
| Output consumed by CVF | package-use proof receipt and live output hash only |
| Truth packet or source path | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Authority boundary | skill usage receipt does not grant authority, activate package lifecycle state, or bypass work-order scope |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | ASCP-T5 model-completion proof; provider skill surface: none |
| Output consumed by CVF | N/A with reason: no provider skill output consumed |
| CVF source-of-truth promotion path | N/A with reason: no provider skill output promoted |
| Evidence artifact | this baseline, work order, and completion review |
| Authority boundary | provider model output is proof evidence only; provider skill surface: none; not CVF canonical authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | local CVF skill-control implementation -> no external knowledge promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASCP-T5 baseline, work order, completion review, helper, tests, standard, and roadmap |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local CVF source verification and live proof hashes only |
| Claim boundary | provider model output is not promoted as CVF canonical authority |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline references internal ASSF governance, private package
runtime, and live-provider proof surfaces. Public-safe export requires separate
public-sync authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T5_PACKAGE_EXECUTION_USE_PROOF_ADAPTER_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASCP_T5_PACKAGE_EXECUTION_USE_PROOF_ADAPTER_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | `Status: ACTIVE_ROADMAP` | PASS |
| Registry JSON | N/A with reason: no registry mutation authorized or performed | N/A with reason | PASS |
| Registry Markdown | N/A with reason: no registry markdown mutation | N/A with reason | PASS |
| External evidence digest | `.cvf/runtime/assf-use-proof/ascp-t5-live-proof.json` | `sha256:6fb08064c35dbfcdb1a7dbc3657edd345d57bbe78e186ca9267a60576d932c4a` | PASS |
| System loop interlock | no lifecycle mutation or external MCP execution adapter | output fields `lifecycleMutation=false`; `sourceMutations=[]` | PASS |
| Session continuity | session-sync may follow material closure | N/A with reason | PASS |
| Focused tests | package use-proof adapter tests | PASS | PASS |
| Runtime smoke | dry-run and live use-proof smokes | PASS | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | HTTP 200 and use-proof receipt | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Adapter implementation | `IMPLEMENTED_BOUNDED_USE_PROOF_ADAPTER` | helper emits required token | PASS |
| Live disposition | `LIVE_PROVIDER_USE_PROOF_PASS` | live proof observed required token | PASS |
| Activation policy state | `USED_WITH_RECEIPT` | live proof observed required token | PASS |
| Live HTTP status | 200 | live proof observed 200 | PASS |
| Skill usage receipt | `sha256:` id | `sha256:aa4e26d13ccd75475431e434ef1bd304f20d3b72d77f95a4726fdf6038f2455f` | PASS |
| Use-proof receipt | `sha256:` id | `sha256:f67bd3331f81e088c2f75f7287db0fce60508abbc89cd7099481e5e86aeaa7dc` | PASS |
| Lifecycle mutation | false | false | PASS |
| Source mutations | empty list | empty list | PASS |
| Unit test status | PASS | 5 focused tests and 20 focused regression tests PASS | PASS |

## Claim Boundary

ASCP-T5 implements a bounded package execution/use-proof adapter only. It does
not activate skills, mutate package lifecycle state, convert remaining
packages, implement external MCP runtime execution, mutate provider registry
surfaces, public-sync, or grant action authority.
