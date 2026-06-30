# CVF Agent Work Order - ASCP-P1-P3 Runtime Package Skills Productionization

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: work_order

Batch ID: ASCP-P1-P3

Commit mode: REVIEWER_MAY_COMMIT

dispatchBaseHead: 02e26d49

executionBaseHead: 02e26d49

closureBaseHead: 02e26d49

## Dispatch Prompt Envelope

Role: Codex direct dispatcher, implementer, reviewer, and closer for ASSF
runtime package skills productionization.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_P1_P3_RUNTIME_PACKAGE_SKILLS_PRODUCTIONIZATION_2026-06-30.md`.

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ASCP_P1_P3_RUNTIME_PACKAGE_SKILLS_PRODUCTIONIZATION_2026-06-30.md`.

Commit mode: `REVIEWER_MAY_COMMIT`.

Base: `02e26d49`.

Mission summary: complete P1 ACTIVE lifecycle admission, P2 production
execution adapter, and P3 CLI/MCP production envelope for the six current
runtime-eligible package skills.

Do-not-misread notes: this work order does not authorize remaining package
conversion, automatic invocation, full MCP server behavior, production Model
Gateway/model router, provider registry mutation, public-sync, or action
authority from package loading alone.

## Purpose

Close ASCP-P1-P3 with source-backed ACTIVE package records and receipt-backed
runtime execution for six CVF package skills.

## 1. Mission

Create and verify:

- P1 lifecycle source promotion for exactly six runtime-eligible packages;
- P2 production package executor requiring ACTIVE source state and use-proof
  receipts;
- P3 CLI/MCP-facing production envelope for external-agent consumption;
- guard updates so ACTIVE certified metadata remains evidence-bound;
- generated ASSF index and truth index refresh;
- dry-run and live provider proof.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat approval on 2026-06-30 for P1-P3 on the six packages | authorizes this tranche and live key use |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup and next-move source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generated session state |
| Active handoff | `AGENT_HANDOFF_V28_2026-06-30.md` | active handoff named by state registry |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ASCP_P1_P3_RUNTIME_PACKAGE_SKILLS_PRODUCTIONIZATION_2026-06-30.md` | scope and claim boundary |
| Production package runtime standard | `docs/reference/agent_system_skills/CVF_ASSF_PRODUCTION_PACKAGE_RUNTIME_STANDARD.md` | production adapter contract |
| ASSF package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | lifecycle and adapter boundary |
| Skill source-of-truth packet standard | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | truth packet obligations |

Authority boundary: ASCP-P1-P3 may make six packages ACTIVE inside ASSF source
control and execute them through receipt-backed adapters. It may not convert or
activate other packages, implement full MCP/model-router behavior, mutate
provider registry source, public-sync, or grant downstream action authority.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author baseline and work order |
| Implementer | Codex | update package sources, add adapters, update guards, regenerate indexes |
| Reviewer/closer | Codex | verify tests, dry smoke, live proof, changed set, and completion review |
| Operator approval required | operator | remaining package conversion, full MCP server, production Model Gateway/model router, public-sync |

## 4. Scope

Allowed paths:

- `docs/reference/agent_system_skills/CVF_ASSF_PRODUCTION_PACKAGE_RUNTIME_STANDARD.md`
- `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md`
- `docs/reference/agent_system_skills/generated/skill-index.json`
- `docs/reference/agent_system_skills/packages/cvf-engineering-*/README.md`
- `docs/reference/agent_system_skills/packages/cvf-engineering-*/skill.source.json`
- `docs/reference/agent_system_skills/registry/entries/cvf-engineering-*.json`
- `docs/reference/agent_system_skills/truth/packets/cvf-engineering-*.json`
- `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json`
- `governance/compat/run_assf_production_package_executor.py`
- `governance/compat/run_assf_production_cli_mcp_adapter.py`
- `governance/compat/test_run_assf_production_package_executor.py`
- `governance/compat/check_assf_certified_metadata_admission.py`
- `governance/compat/test_check_assf_certified_metadata_admission.py`
- `governance/compat/check_skill_truth_packets.py`
- `governance/compat/test_check_skill_truth_packets.py`
- this baseline, this work order, and paired completion review.

Forbidden paths:

- the 18 package roots that remain `PROPOSED`;
- provider registry or provider routing source mutation;
- full MCP server, daemon, queue, hook, or IDE bridge implementation;
- production Model Gateway/model router;
- session state files unless a later session-sync tranche is opened;
- public-sync repository files.

Risk ceiling: R2 internal governance control with one R2 live provider proof.

## Scope / Target / Owner Boundary

Target: bounded production runtime for the six existing runtime-eligible ASSF
package skills.

Owner boundary: Codex owns this direct implementation and reviewer closure.
The operator owns future remaining package conversion, full MCP server,
production Model Gateway/model router, provider registry mutation, and
public-sync decisions.

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
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_USE_PROOF_ADAPTER_STANDARD.md`
- `governance/compat/run_assf_runtime_package_loader.py`
- `governance/compat/run_assf_activation_policy_resolver.py`
- `governance/compat/run_assf_package_use_proof_adapter.py`
- `governance/compat/assf_live_model_selection.py`

## 6. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF package lifecycle vocabulary includes `ACTIVE` | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields | `ACTIVE` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Runtime loader emits package usage receipts after eligible body reads | `governance/compat/run_assf_runtime_package_loader.py` | `_build_skill_usage_receipt`; `build_runtime_package_packet` | `CVF_ASSF_SKILL_USAGE_RECEIPT` | runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Activation policy resolver recognizes receipt-backed use | `governance/compat/run_assf_activation_policy_resolver.py` | `_state_for`; `build_activation_policy_packet` | `USED_WITH_RECEIPT` | activation policy resolver | RUNTIME_BEHAVIOR | ACCEPT |
| Package use-proof adapter emits live use-proof receipts | `governance/compat/run_assf_package_use_proof_adapter.py` | `_build_use_proof_receipt`; `build_package_use_proof_packet` | `CVF_ASSF_PACKAGE_USE_PROOF_RECEIPT` | package use-proof adapter | RUNTIME_BEHAVIOR | ACCEPT |
| Production executor is new in ASCP-P1-P3 | `governance/compat/run_assf_production_package_executor.py` | ASCP-P1-P3 new file | `build_production_package_execution_packet` | production package executor | DOC_ONLY_NEW | ACCEPT |
| CLI/MCP production wrapper is new in ASCP-P1-P3 | `governance/compat/run_assf_production_cli_mcp_adapter.py` | ASCP-P1-P3 new file | `build_cli_mcp_execution_envelope` | production CLI/MCP adapter | DOC_ONLY_NEW | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| P1 promote six runtime-eligible packages to ACTIVE | Mission; Scope | six registry entries and six package source files | runtime eligibility audit | PASS |
| P2 require production execution receipt path | Mission; Evidence Requirements | production executor and tests | unit tests and dry smoke | PASS |
| P3 expose CLI/MCP production envelope | Mission; Evidence Requirements | CLI/MCP adapter and live receipt | dry smoke and live proof | PASS |
| Preserve source-of-truth trace | Source-Fidelity Pass; Acceptance Criteria | truth packet updates and sourceTruthTrace | truth packet guard and live receipt | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> implementer -> reviewer/closer, all Codex in same governed turn |
| baseHeadFor(phase) | `dispatchBaseHead=02e26d49`; `executionBaseHead=02e26d49`; `closureBaseHead=02e26d49` |
| changedSetScope(phase) | ASCP-P1-P3 package source updates, runtime adapters, guard updates, generated indexes, baseline, work order, and completion review |
| traceScope(phase, actor) | work-order trace covers implementation; completion review trace covers closure |
| commitOwner(phase) | Codex reviewer/closer owns material commit if committed |
| crossBatchIsolation | no remaining package conversion, provider registry mutation, full MCP server, model router, public-sync, or session-sync mutation |
| nextMoveSurfaceHandling | session-sync follows material closure if current mode or next allowed move changes |
| nextMoveSurfaces | active session state, front door, and handoff |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: implement ASCP-P1-P3 production package
runtime controls, tests, and checker updates for the first six ACTIVE package
skills.

Protected paths:

- `governance/compat/run_assf_production_package_executor.py`
- `governance/compat/run_assf_production_cli_mcp_adapter.py`
- `governance/compat/test_run_assf_production_package_executor.py`
- `governance/compat/check_assf_certified_metadata_admission.py`
- `governance/compat/test_check_assf_certified_metadata_admission.py`
- `governance/compat/check_skill_truth_packets.py`
- `governance/compat/test_check_skill_truth_packets.py`

Operator authorization: operator requested P1-P3 productionization for the six
existing runtime-eligible package skills.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation surface | `docs/reference/agent_system_skills/` and `governance/compat` |
| Storage decision | update existing package source layout and generated indexes; add two local runtime helpers |
| Stable filename disposition | production executor and CLI/MCP adapter under `governance/compat` |
| Generated aggregate discipline | generated ASSF skill index and truth index regenerated from source records |
| Authority boundary | package execution receipts are evidence only; work orders and source records remain authority |
| Forbidden expansion | no remaining package activation, full MCP server, provider router, public export, or action authority |

## 7. Execution Instructions

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| production package runtime standard | Codex | create |
| six package source records, registry entries, and truth packets | Codex | update |
| generated ASSF skill index and truth index | Codex | regenerate |
| production executor, CLI/MCP adapter, tests, and guard updates | Codex | create or update |
| ASCP-P1-P3 baseline, work order, and completion review | Codex | create |

## Pre-Flight Checks

| Check | Status |
|---|---|
| Startup front door and active handoff read | PASS |
| Guard orientation and literal-format gotchas read | PASS |
| ADIF resolver queried | PASS |
| ASSF package, SKSOT, loader, policy, use-proof, and live selector sources checked | PASS |
| Operator live-key authorization confirmed | PASS |

## Execution Plan

1. Promote exactly six runtime-eligible package source records to ACTIVE.
2. Regenerate ASSF generated indexes.
3. Add production package executor and CLI/MCP adapter.
4. Update certified metadata and truth packet guards.
5. Add focused tests.
6. Run dry-run and live provider proof.
7. File completion review and governance evidence.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| Runtime eligibility audit | exactly six ACTIVE runtime-eligible packages |
| Unit tests | production executor, certified metadata admission, and truth packet tests PASS |
| Generated index checks | generated skill index and truth index are in sync |
| Dry-run smoke | production executor and CLI/MCP adapter return `DRY_RUN_PRODUCTION_PACKAGE_EXECUTION_READY` |
| Live proof | CLI/MCP adapter returns `PRODUCTION_PACKAGE_EXECUTION_PASS`, HTTP 200, and receipt ids |
| Changed set review | no remaining package conversion, provider registry mutation, full MCP server, model router, public-sync, or session-sync mutation |

## Review Gate

Reviewer must confirm ACTIVE source state remains bounded by ASSF receipts,
external CLI/MCP use is envelope-only, provider output is proof evidence only,
and no action authority is granted by package loading.

## Closure Checklist

| Item | Status |
|---|---|
| Production standard created | PASS |
| Six package sources marked ACTIVE | PASS |
| Production executor created | PASS |
| CLI/MCP wrapper created | PASS |
| Guard updates created | PASS |
| Generated indexes refreshed | PASS |
| Focused tests pass | PASS |
| Dry-run smoke passes | PASS |
| Live proof passes | PASS |
| Completion review filed | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` only after focused tests, dry-run smoke, live
proof, generated-index checks, truth/certification guards, changed set review,
and governance gates pass. Return `BLOCKED` if this tranche requires remaining
package conversion, provider registry mutation, full MCP server behavior,
production Model Gateway/model router behavior, public-sync, or action
authority from package loading alone.

## Operator Checkpoint

No further operator checkpoint is required for ASCP-P1-P3 closure. Future
remaining package conversion, full MCP server, production Model Gateway/model
router, or public-sync requires fresh authorization.

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | USED_WITH_RECEIPT |
| CVF skill id | `cvf-engineering-spec-driven-development` |
| Package root | `docs/reference/agent_system_skills/packages/cvf-engineering-spec-driven-development/SKILL.md` |
| Invocation context | ASCP-P1-P3 CLI/MCP production live proof |
| Receipt evidence | `sha256:aa4e26d13ccd75475431e434ef1bd304f20d3b72d77f95a4726fdf6038f2455f` |
| Output consumed by CVF | package-use proof receipt, production execution receipt, and live output hash only |
| Truth packet or source path | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Authority boundary | skill usage receipt does not grant authority, filesystem access, git access, browser access, provider access, public-sync, or downstream action authority |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | ASCP-P1-P3 model-completion proof; provider skill surface: none |
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
| Owner surface | ASCP-P1-P3 baseline, work order, completion review, standard, runtime helpers, package sources, generated indexes, guards, and tests |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local CVF source verification and live proof hashes only |
| Claim boundary | provider model output is not promoted as CVF canonical authority |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace plus Alibaba DashScope-compatible live model |
| Session or invocation | ASCP-P1-P3 runtime package skills productionization on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | apply_patch; Python unittest; generated index; dry-run smoke; live provider proof |
| Target paths | package sources, registry entries, truth packets, generated indexes, production standard, runtime helpers, guard updates, tests, baseline, work order, completion review |
| Allowed scope source | operator instruction plus ASCP-P1-P3 baseline and work order |
| Before status evidence | base commit `02e26d49`; clean worktree before ASCP-P1-P3 edits |
| After status evidence | six ACTIVE runtime-eligible packages with production executor and CLI/MCP adapter evidence |
| Diff evidence | `git diff --name-status`; focused tests; dry-run smoke; live proof; governance gates |
| Approval boundary | operator authorized live API-key use; raw keys were not printed |
| Claim boundary | bounded six-package production runtime only |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `cvf-ascp-p1-p3-runtime-package-skills-productionization-2026-06-30` |
| Expected manifest | baseline, work order, completion review, production standard, executor, CLI/MCP adapter, tests, checker updates, six registry entries, six package sources, six truth packets, generated indexes |
| Actual changed set | baseline, work order, completion review, production standard, executor, CLI/MCP adapter, tests, checker updates, six registry entries, six package sources, six truth packets, generated indexes |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order references internal ASSF governance, private runtime
package surfaces, and live-provider proof. Public-safe export requires separate
public-sync authorization.

## Claim Boundary

ASCP-P1-P3 implements bounded production runtime for six package skills only.
It does not convert remaining packages, implement full MCP runtime behavior,
mutate provider registry surfaces, public-sync, or grant action authority.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 baseline | `docs/baselines/CVF_GC018_ASCP_P1_P3_RUNTIME_PACKAGE_SKILLS_PRODUCTIONIZATION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASCP_P1_P3_RUNTIME_PACKAGE_SKILLS_PRODUCTIONIZATION_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: no roadmap file was changed in ASCP-P1-P3 | no roadmap closure state mutation | PASS |
| Registry JSON | six ASSF registry entries | `status=ACTIVE`; adapter evidence present | PASS |
| Registry Markdown | N/A with reason: no separate registry markdown exists for this package set | package README files updated instead | PASS |
| External evidence digest | `.cvf/runtime/assf-production/p1-p3-cli-mcp-live.json` | `sha256:36e615e5fcff0b2dcdb27ed553f02292a42116bd9b7dce80309a4d3da5422e37` | PASS |
| System loop interlock | no action authority from package loading | source mutations empty in runtime receipts | PASS |
| Session continuity | active session front-door/state/handoff after material commit | session-sync may follow material commit | N/A with reason |
| Focused tests | production executor and checker tests | PASS | PASS |
| Runtime smoke | dry-run and live CLI/MCP smokes | PASS | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Runtime eligible package count | 6 | 6 | PASS |
| ACTIVE package count | 6 | 6 | PASS |
| Production executor dry disposition | `DRY_RUN_PRODUCTION_PACKAGE_EXECUTION_READY` | observed | PASS |
| CLI/MCP live disposition | `PRODUCTION_PACKAGE_EXECUTION_PASS` | observed | PASS |
| Provider selection | source-backed provider candidate | `alibaba-dashscope` | PASS |
| Model selection | unexpired ledger model | `deepseek-v4-flash` | PASS |
| Live HTTP status | 200 | 200 | PASS |
| Production execution receipt | present | `sha256:e60d0b3d9edb455b483b5f847b942d918ed5e6bdd1523cb1c60f59b9b16c59d5` | PASS |
| Use-proof receipt | present | `sha256:bf0a7afa7fcb66a13f2949af1c68d0b4f7928c3047b894047ce529dae39dc803` | PASS |
| Provider skill output promotion | none | none | PASS |
