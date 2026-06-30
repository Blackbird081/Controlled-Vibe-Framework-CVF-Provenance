# CVF GC-018 Baseline: ASCP-P1-P3 Runtime Package Skills Productionization

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: baseline

Batch ID: ASCP-P1-P3

dispatchBaseHead: 02e26d49

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | productionize the six ASCP runtime-eligible package skills with ACTIVE source state, receipt-backed execution, and CLI/MCP adapter envelope |
| Baseline | ASCP-T1 through ASCP-T5 proved package anatomy, runtime loading, policy semantics, CLI/MCP projection, and live use-proof |
| Proposed tranche | P1 ACTIVE lifecycle admission, P2 production execution/use-proof adapter, P3 CLI/MCP production envelope |
| Execution route | Codex direct implementation with reviewer-owned closure |
| Closure posture | CLOSED_PASS_BOUNDED after focused tests, generated-index checks, dry smoke, and one live provider proof |

## Purpose

ASCP-P1-P3 turns the first six runtime-eligible CVF package skills into
production-scoped runtime package skills. The scope is intentionally bounded:
the packages become `ACTIVE` only inside ASSF source-of-truth controls and can
be executed only through receipt-backed production adapters.

## Scope / Methodology

Allowed ASCP-P1-P3 scope:

- mark exactly six runtime-eligible package records `ACTIVE`;
- update six package roots, six registry entries, six truth packets, and the
  generated ASSF indexes;
- add the production package runtime standard;
- add the production package executor and CLI/MCP adapter wrapper;
- update certified-metadata and truth-packet guards for the new ACTIVE source
  contract;
- add focused unit tests and run one live provider proof.

Forbidden ASCP-P1-P3 scope:

- converting or activating the remaining 18 package roots;
- automatic skill invocation outside an explicit package execution command;
- full MCP server, daemon, hook, IDE bridge, or queue behavior;
- production Model Gateway or model router;
- provider registry mutation;
- public-sync or public catalog claims;
- filesystem, git, browser, merge, push, or action authority from package
  loading alone.

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
| ASSF package lifecycle vocabulary includes `ACTIVE` | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields | `ACTIVE` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Runtime loader emits package usage receipts after eligible package body reads | `governance/compat/run_assf_runtime_package_loader.py` | `_build_skill_usage_receipt`; `build_runtime_package_packet` | `CVF_ASSF_SKILL_USAGE_RECEIPT` | runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Activation policy resolver recognizes receipt-backed use | `governance/compat/run_assf_activation_policy_resolver.py` | `_state_for`; `build_activation_policy_packet` | `USED_WITH_RECEIPT` | activation policy resolver | RUNTIME_BEHAVIOR | ACCEPT |
| Package use-proof adapter emits live use-proof receipts | `governance/compat/run_assf_package_use_proof_adapter.py` | `_build_use_proof_receipt`; `build_package_use_proof_packet` | `CVF_ASSF_PACKAGE_USE_PROOF_RECEIPT` | package use-proof adapter | RUNTIME_BEHAVIOR | ACCEPT |
| Live provider/model selector chooses a source-backed free-quota model | `governance/compat/assf_live_model_selection.py` | `resolve_provider_model` | `AUTO_FROM_ASSF_LIVE_PROVIDER_CANDIDATES` | ASCP live provider/model selector | RUNTIME_BEHAVIOR | ACCEPT |
| Production executor is new in ASCP-P1-P3 | `governance/compat/run_assf_production_package_executor.py` | ASCP-P1-P3 new file | `build_production_package_execution_packet` | production package executor | DOC_ONLY_NEW | ACCEPT |
| CLI/MCP production wrapper is new in ASCP-P1-P3 | `governance/compat/run_assf_production_cli_mcp_adapter.py` | ASCP-P1-P3 new file | `build_cli_mcp_execution_envelope` | production CLI/MCP adapter | DOC_ONLY_NEW | ACCEPT |

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

Rollback boundary: revert ASCP-P1-P3 production runtime changes only; do not
revert ASCP-T1 through ASCP-T5 closures, package roots, source mirrors, truth
source-of-truth design, or previous session-sync commits.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASSF package contract, runtime package loader, activation policy resolver, use-proof adapter, live provider/model selector, generated ASSF index, truth index |
| Runtime behavior claimed | six ACTIVE packages can execute through production executor and CLI/MCP envelope with receipts |
| Live/provider proof claimed | YES - one Alibaba DashScope-compatible `deepseek-v4-flash` live call |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - current sources support bounded production package runtime for six packages only |

## Evidence / Verification

| Evidence | Required or observed result |
|---|---|
| Runtime eligibility audit | `runtimeEligibleCount=6`; `statusCounts.ACTIVE=6`; six package ids listed in `readyForBodyLoad` |
| Focused unit tests | `python -m unittest governance.compat.test_run_assf_production_package_executor governance.compat.test_check_assf_certified_metadata_admission governance.compat.test_check_skill_truth_packets` PASS, 19 tests |
| Py compile | production executor, CLI/MCP adapter, tests, and checker updates compile |
| Dry-run executor smoke | `DRY_RUN_PRODUCTION_PACKAGE_EXECUTION_READY`; package read emitted usage and policy receipts |
| Dry-run CLI/MCP smoke | `DRY_RUN_PRODUCTION_PACKAGE_EXECUTION_READY`; external envelope emitted source-truth trace |
| Live provider proof | `PRODUCTION_PACKAGE_EXECUTION_PASS`, provider `alibaba-dashscope`, model `deepseek-v4-flash`, HTTP 200, latency 12872 ms |
| Live execution receipt | `sha256:e60d0b3d9edb455b483b5f847b942d918ed5e6bdd1523cb1c60f59b9b16c59d5` |
| Live use-proof receipt | `sha256:bf0a7afa7fcb66a13f2949af1c68d0b4f7928c3047b894047ce529dae39dc803` |
| Live evidence file hash | `sha256:36e615e5fcff0b2dcdb27ed553f02292a42116bd9b7dce80309a4d3da5422e37` |

## Six Active Runtime Packages

| Skill id | Final lifecycle source state | Runtime disposition |
|---|---|---|
| `cvf-engineering-code-review-quality` | ACTIVE | production executor eligible |
| `cvf-engineering-debugging-error-recovery` | ACTIVE | production executor eligible |
| `cvf-engineering-planning-task-breakdown` | ACTIVE | production executor eligible |
| `cvf-engineering-security-hardening` | ACTIVE | production executor eligible |
| `cvf-engineering-spec-driven-development` | ACTIVE | production executor eligible; live proof representative |
| `cvf-engineering-test-driven-development` | ACTIVE | production executor eligible |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline references private ASSF runtime package and live-provider
proof surfaces. Public-safe export requires separate public-sync authorization.

## Claim Boundary

ASCP-P1-P3 makes six CVF-owned ASSF package skills production-scoped runtime
packages. It does not activate the remaining 18 packages, implement a full MCP
server or model router, mutate provider registry surfaces, public-sync, or
grant action authority beyond explicit receipt-backed package execution.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 baseline | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_P1_P3_RUNTIME_PACKAGE_SKILLS_PRODUCTIONIZATION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
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
