# CVF Agent Work Order - ASCP-T5 Package Execution Use-Proof Adapter

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: work_order

Batch ID: ASCP-T5

Commit mode: REVIEWER_MAY_COMMIT

dispatchBaseHead: 52d0787b

executionBaseHead: 52d0787b

closureBaseHead: 52d0787b

## Dispatch Prompt Envelope

Role: Codex direct implementer and reviewer for ASSF package execution
use-proof adapter.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T5_PACKAGE_EXECUTION_USE_PROOF_ADAPTER_2026-06-30.md`.

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ASCP_T5_PACKAGE_EXECUTION_USE_PROOF_ADAPTER_2026-06-30.md`.

Commit mode: `REVIEWER_MAY_COMMIT`.

Base: `52d0787b`.

Mission summary: implement a bounded internal package use-proof adapter before
any package lifecycle source is considered for `ACTIVE` promotion.

Do-not-misread notes: this work order does not authorize lifecycle mutation,
remaining package conversion, automatic invocation, external MCP package
execution, provider registry mutation, public-sync, or production readiness.

## Purpose

Close ASCP-T5 with a source-backed and live-tested package execution/use-proof
adapter.

## 1. Mission

Create and verify:

- package use-proof adapter standard;
- package use-proof adapter helper;
- focused helper tests;
- live provider proof with secret-safe evidence;
- roadmap update from ASCP-T5 value-parked to closed bounded;
- baseline, work order, and completion evidence.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat approval on 2026-06-30 for ASCP-T5 package execution/use-proof before ACTIVE promotion | authorizes ASCP-T5 execution and live key use |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup and next-move source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generated session state |
| Active handoff | `AGENT_HANDOFF_V28_2026-06-30.md` | active handoff named by state registry |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ASCP_T5_PACKAGE_EXECUTION_USE_PROOF_ADAPTER_2026-06-30.md` | scope and claim boundary |
| ASCP roadmap | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | T5 reopened lane and closure |
| Package use-proof standard | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_USE_PROOF_ADAPTER_STANDARD.md` | adapter contract |
| ASSF package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | lifecycle and adapter separation |
| Skill usage receipt standard | `docs/reference/agent_system_skills/CVF_SKILL_USAGE_RECEIPT_TRACE_STANDARD.md` | receipt trace source |

Authority boundary: ASCP-T5 may emit a package use-proof receipt after a
receipt-backed package read and live provider call. It may not mutate lifecycle
sources, regenerate indexes, convert remaining packages, implement MCP runtime
behavior, or public-sync.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author baseline and work order |
| Implementer | Codex | add standard, helper, tests, and roadmap update |
| Reviewer/closer | Codex | verify focused tests, live proof, changed set, and completion review |
| Operator approval required | operator | later ACTIVE promotion, remaining package conversion, external MCP execution runtime, or public-sync |

## 4. Scope

Allowed paths:

- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_USE_PROOF_ADAPTER_STANDARD.md`
- `governance/compat/run_assf_package_use_proof_adapter.py`
- `governance/compat/test_run_assf_package_use_proof_adapter.py`
- `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md`
- `docs/baselines/CVF_GC018_ASCP_T5_PACKAGE_EXECUTION_USE_PROOF_ADAPTER_2026-06-30.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T5_PACKAGE_EXECUTION_USE_PROOF_ADAPTER_2026-06-30.md`
- `docs/reviews/CVF_ASCP_T5_PACKAGE_EXECUTION_USE_PROOF_ADAPTER_COMPLETION_2026-06-30.md`

Forbidden paths:

- ASSF registry lifecycle sources;
- generated ASSF skill index;
- ASSF truth packets;
- ASSF package roots;
- provider registry or provider routing source mutation;
- MCP server, daemon, hook, or IDE bridge implementation;
- session state files unless a later session-sync tranche is opened;
- public-sync repository files.

Risk ceiling: R2 internal governance control with one R2 live provider proof.

## Scope / Target / Owner Boundary

Target: bounded internal package use-proof adapter for ASSF package control.

Owner boundary: Codex owns implementation and reviewer closure in this direct
tranche; operator owns future ACTIVE promotion, package conversion, external
runtime execution, and public-sync decisions.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`,
lifecyclePhase=`implementation`, surfaceSelector=`docs/reference/agent_system_skills`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure command:

```text
python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase implementation --surface-selector docs/reference/agent_system_skills --risk-ceiling HIGH --max-results 20 --json
```

## 5. Required First Reads

Read before editing:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V28_2026-06-30.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/agent_system_skills/CVF_SKILL_USAGE_RECEIPT_TRACE_STANDARD.md`
- `docs/reference/agent_system_skills/CVF_ASSF_ACTIVATION_POLICY_SEMANTICS_STANDARD.md`
- `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
- `governance/compat/run_assf_runtime_package_loader.py`
- `governance/compat/run_assf_activation_policy_resolver.py`
- `scripts/_local_env.py`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/alibaba-env.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`

## 6. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Runtime loader emits usage receipts only after explicit eligible body reads | `governance/compat/run_assf_runtime_package_loader.py` | `_build_skill_usage_receipt`; `build_runtime_package_packet` | `skillUsageReceipts` | runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Activation policy resolver requires matching usage receipt for consumed output | `governance/compat/run_assf_activation_policy_resolver.py` | `_state_for`; `build_activation_policy_packet` | `USED_WITH_RECEIPT` | activation policy resolver | RUNTIME_BEHAVIOR | ACCEPT |
| ASSF package contract keeps lifecycle activation separate from adapter behavior | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields; Provider Adapter Boundary | `ACTIVE`; `adapterContract` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Live key loader accepts repo env files without printing raw keys | `scripts/_local_env.py` | `DEFAULT_ENV_FILES`; `bootstrap_repo_env` | `DEFAULT_ENV_FILES` | repo env bootstrap | RUNTIME_BEHAVIOR | ACCEPT |
| Alibaba env source lists accepted DashScope-compatible aliases | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/alibaba-env.ts` | `keyCandidates` | `DASHSCOPE_API_KEY` | Alibaba env source | VALUE_SET | ACCEPT |
| Provider capability registry includes Alibaba `qwen-turbo` completion capability | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | `PROVIDER_CAPABILITY_REGISTRY` | `qwen-turbo` | Model Gateway provider capability registry | VALUE_SET | ACCEPT |
| Live run diagnostic standard requires secret-safe failure diagnostics | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | Required Diagnostic Record | `stage`; `class`; `retryable`; `safeMessage` | live run diagnostic standard | LITERAL_INVARIANT | ACCEPT |
| Package use-proof adapter is new in ASCP-T5 | `governance/compat/run_assf_package_use_proof_adapter.py` | ASCP-T5 new file | `build_package_use_proof_packet` | package use-proof adapter | DOC_ONLY_NEW | ACCEPT |

## Provider Registry Boundary

ASCP-T5 makes a single live provider call through the local helper. It does not
mutate provider registry source, claim provider ranking, or promote provider
model output into canonical source authority.

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Reopen ASCP-T5 for package execution/use-proof before ACTIVE promotion | Purpose; Mission | use-proof helper and roadmap update | live proof and roadmap review | PASS |
| Preserve lifecycle activation boundary | Source Verification; Claim Boundary | `lifecycleMutation=false`; `sourceMutations=[]` | unit tests and live proof | PASS |
| Require receipt-backed package use | Evidence Requirements | `CVF_ASSF_SKILL_USAGE_RECEIPT`; `USED_WITH_RECEIPT` | dry-run and live proof | PASS |
| Require live provider proof | Evidence Requirements | HTTP 200 and use-proof receipt | live proof | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> implementer -> reviewer/closer, all Codex in same governed turn |
| baseHeadFor(phase) | `dispatchBaseHead=52d0787b`; `executionBaseHead=52d0787b`; `closureBaseHead=52d0787b` |
| changedSetScope(phase) | ASCP-T5 standard, helper, tests, roadmap update, baseline, work order, and completion review |
| traceScope(phase, actor) | work-order trace covers implementation; completion review trace covers closure |
| commitOwner(phase) | Codex reviewer/closer owns material commit if committed |
| crossBatchIsolation | no ASSF lifecycle state, generated index, truth packet, package root, provider registry, MCP runtime, public-sync, or remaining conversion mutation |
| nextMoveSurfaceHandling | session-sync follows material closure |
| nextMoveSurfaces | active session state, front door, and handoff |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one bounded use-proof helper and
focused tests under `governance/compat`.

Protected paths:

- `governance/compat/run_assf_package_use_proof_adapter.py`
- `governance/compat/test_run_assf_package_use_proof_adapter.py`

Operator authorization: active instruction reopens ASCP-T5 for package
execution/use-proof before ACTIVE lifecycle promotion.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASCP roadmap, ASSF package contract, use-proof standard, runtime loader, activation policy resolver, provider env loader, provider capability registry, live diagnostic standard |
| Runtime behavior claimed | bounded package use-proof adapter with live proof |
| Live/provider proof claimed | YES - one Alibaba DashScope-compatible `qwen-turbo` live call |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - current sources support use-proof only, not lifecycle mutation |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation surface | `docs/reference/agent_system_skills/` and `governance/compat` |
| Storage decision | add local use-proof helper and standard, not a generated aggregate |
| Stable filename disposition | `governance/compat/run_assf_package_use_proof_adapter.py` |
| Generated aggregate discipline | N/A with reason: no generated JSON aggregate is added or edited |
| Authority boundary | use-proof receipt is evidence only; package sources and work orders remain authority |
| Forbidden expansion | no lifecycle mutation, package conversion, MCP runtime, provider registry mutation, public export, or production-readiness claim |

## 7. Execution Instructions

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| use-proof standard, helper, and tests | Codex | create |
| ASCP roadmap | Codex | update T5 row and evidence only |
| ASCP-T5 artifacts | Codex | create |

## Pre-Flight Checks

| Check | Status |
|---|---|
| Startup front door and active handoff read | PASS |
| Guard orientation and literal-format gotchas read | PASS |
| ADIF resolver queried | PASS |
| Runtime loader, activation policy resolver, env loader, provider capability registry, and live diagnostic standard read | PASS |

## Execution Plan

1. Add package use-proof standard.
2. Add package use-proof helper.
3. Add focused tests.
4. Run focused tests and dry-run smoke.
5. Run live provider proof.
6. Update roadmap and file completion review.
7. Run governance gates and commit.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| Unit tests | `python -m unittest governance.compat.test_run_assf_package_use_proof_adapter` PASS |
| Regression tests | loader, activation policy, and use-proof adapter focused tests PASS |
| Dry-run smoke | `DRY_RUN_READY_FOR_LIVE_PROVIDER_USE_PROOF` and `USED_WITH_RECEIPT` |
| Live proof | `LIVE_PROVIDER_USE_PROOF_PASS`, HTTP 200, use-proof receipt |
| Changed set review | no registry, generated index, truth packet, package root, provider registry, MCP runtime, or public-sync mutation |

## Review Gate

Reviewer must confirm use-proof is not lifecycle activation, live provider
output is not canonical authority, and ASCP-T5 does not authorize ACTIVE
promotion or remaining package conversion.

## Closure Checklist

| Item | Status |
|---|---|
| Use-proof standard created | PASS |
| Use-proof helper created | PASS |
| Focused tests created | PASS |
| Unit tests pass | PASS |
| Dry-run smoke passes | PASS |
| Live proof passes | PASS |
| Roadmap update filed | PASS |
| Completion review filed | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` only after focused tests, dry-run smoke, live
proof, changed set review, and governance gates pass. Return `BLOCKED` if
use-proof semantics require lifecycle mutation, registry/index edits, package
root edits, provider registry mutation, MCP runtime behavior, public-sync, or
production readiness.

## Operator Checkpoint

No further operator checkpoint is required for ASCP-T5 closure. Future ACTIVE
promotion, remaining package conversion, external MCP package execution, or
public-sync requires fresh authorization.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Helper loads one eligible package through runtime loader | unit tests and dry-run smoke PASS |
| AC2 | Helper records matching skill usage receipt | dry-run and live proof PASS |
| AC3 | Helper classifies consumed output as `USED_WITH_RECEIPT` before provider use | unit tests, dry-run, and live proof PASS |
| AC4 | Helper emits live diagnostics on missing key or provider failure | unit tests PASS |
| AC5 | Live provider proof emits use-proof receipt | live proof PASS |
| AC6 | Helper emits no lifecycle or source mutation authorization | unit tests and output PASS |
| AC7 | Roadmap records ASCP-T5 closed bounded and blocks ACTIVE promotion | roadmap update PASS |

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
| Evidence artifact | this work order and paired completion review |
| Authority boundary | provider model output is proof evidence only; provider skill surface: none; not CVF canonical authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | local CVF skill-control implementation -> no external knowledge promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASCP-T5 roadmap, baseline, work order, completion review, standard, helper, and tests |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local CVF source verification and live proof hashes only |
| Claim boundary | provider model output is not promoted as CVF canonical authority |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace plus Alibaba DashScope-compatible live model |
| Session or invocation | ASCP-T5 package execution use-proof adapter on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | apply_patch; Python unittest; dry-run smoke; live provider proof |
| Target paths | standard, helper, tests, roadmap, baseline, work order, completion review |
| Allowed scope source | operator instruction plus ASCP-T5 baseline and work order |
| Before status evidence | base commit `52d0787b`; clean worktree before ASCP-T5 edits |
| After status evidence | pending material closure changed set |
| Diff evidence | focused tests, dry-run smoke, live proof, changed set review, and governance gates |
| Approval boundary | operator authorized live API-key use; raw keys were not printed |
| Claim boundary | bounded internal package use-proof only |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `cvf-ascp-t5-package-execution-use-proof-adapter-2026-06-30` |
| Expected manifest | standard, helper, tests, roadmap update, baseline, work order, completion review |
| Actual changed set | standard, helper, tests, roadmap update, baseline, work order, completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order references internal ASSF governance, private runtime
package surfaces, and live-provider proof. Public-safe export requires separate
public-sync authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
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

ASCP-T5 implements bounded package execution/use-proof only. It does not
activate skills, mutate package lifecycle state, convert remaining packages,
implement external MCP runtime execution, mutate provider registry surfaces,
public-sync, or grant action authority.
