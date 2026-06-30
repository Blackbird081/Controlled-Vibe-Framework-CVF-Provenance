# CVF GC-018 Baseline: ADIF-CLI-T1 CLI Classification And Entrypoints

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: baseline

Batch ID: ADIF-CLI-T1

dispatchBaseHead: d2ce31e0

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | add direct CLI entrypoints for ADIF agent-facing helpers and add centralized CLI surface classification |
| Baseline | ADIF resolver, preflight readout, and finding intake were module-callable only |
| Proposed tranche | standard, registry, checker, tests, CLI entrypoints, baseline, work order, and completion evidence |
| Execution route | Codex direct implementation with reviewer-owned closure |
| Closure posture | CLOSED_PASS_BOUNDED after focused tests, CLI smokes, and classification checker |

## Purpose

ADIF-CLI-T1 removes the recurring ad hoc Python import requirement for ADIF
readouts and introduces a controlled classification registry for future helper
entrypoint decisions.

## Scope / Methodology

Allowed ADIF-CLI-T1 scope:

- add `main()` and `__main__` entrypoints to ADIF resolver, preflight readout,
  and finding-intake bridge helpers;
- preserve existing module APIs as the canonical implementation surface;
- add a CLI surface classification standard;
- add a machine-readable registry and checker;
- classify current ADIF helpers as `CLI_REQUIRED`;
- classify dispatch-quality split modules as `MODULE_ONLY`;
- add focused unit tests and command smoke evidence.

Forbidden ADIF-CLI-T1 scope:

- changing ADIF entry semantics or lifecycle;
- auto-promoting findings to ADIF entry files;
- wiring a new MCP adapter;
- changing ASSF runtime package activation policy;
- provider calls or live governance behavior claims;
- public-sync or production-readiness claims.

## Findings / Position

The correct control is not "every module gets CLI." The correct control is a
central registry with three classifications:

- `CLI_REQUIRED` for repeatable agent/operator evidence commands;
- `CLI_OPTIONAL` for low-risk convenience commands;
- `MODULE_ONLY` for split implementation modules owned by a parent command.

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
| ADIF resolver already exposes bounded packet data | `governance/compat/run_adif_defect_resolver.py` | `DefectPacket.to_dict`; `resolve_defect_packet` | `DefectPacket`; `resolve_defect_packet` | ADIF resolver | RUNTIME_BEHAVIOR | ACCEPT |
| ADIF preflight readout already exposes human and JSON-ready data | `governance/compat/run_adif_preflight_readout.py` | `PreflightReadout.to_human_text`; `PreflightReadout.to_dict`; `build_preflight_readout` | `PreflightReadout`; `build_preflight_readout` | ADIF preflight readout | RUNTIME_BEHAVIOR | ACCEPT |
| ADIF finding intake already returns a non-mutating classification outcome | `governance/compat/run_adif_finding_intake_bridge.py` | `FindingIntakeOutcome.to_dict`; `classify_finding` | `FindingIntakeOutcome`; `classify_finding` | ADIF finding intake bridge | RUNTIME_BEHAVIOR | ACCEPT |
| Dispatch-quality split modules are implementation details behind a parent checker | `governance/compat/check_work_order_dispatch_quality.py` | parent checker command surface | `check_work_order_dispatch_quality_*.py` | dispatch-quality checker | RUNTIME_BEHAVIOR | ACCEPT |
| CLI surface classification standard is new in ADIF-CLI-T1 | `docs/reference/CVF_CLI_SURFACE_CLASSIFICATION_STANDARD_2026-06-30.md` | ADIF-CLI-T1 new file | `CLI_REQUIRED`; `CLI_OPTIONAL`; `MODULE_ONLY` | CLI surface classification standard | DOC_ONLY_NEW | ACCEPT |
| CLI surface classification registry is new in ADIF-CLI-T1 | `governance/compat/CVF_CLI_SURFACE_CLASSIFICATION_REGISTRY.json` | ADIF-CLI-T1 new file | `entries` | CLI surface classification registry | DOC_ONLY_NEW | ACCEPT |
| CLI surface classification checker is new in ADIF-CLI-T1 | `governance/compat/check_cli_surface_classification.py` | ADIF-CLI-T1 new file | `build_report` | CLI surface classification checker | DOC_ONLY_NEW | ACCEPT |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add CLI entrypoints to existing ADIF helpers
and add one classification checker plus focused tests under `governance/compat`.

Protected paths:

- `governance/compat/run_adif_defect_resolver.py`
- `governance/compat/run_adif_preflight_readout.py`
- `governance/compat/run_adif_finding_intake_bridge.py`
- `governance/compat/test_run_adif_defect_resolver.py`
- `governance/compat/test_run_adif_preflight_readout.py`
- `governance/compat/test_run_adif_finding_intake_bridge.py`
- `governance/compat/CVF_CLI_SURFACE_CLASSIFICATION_REGISTRY.json`
- `governance/compat/check_cli_surface_classification.py`
- `governance/compat/test_check_cli_surface_classification.py`

Operator authorization: the operator approved adding CLI and requested a
central classification mechanism for future CLI versus module-only decisions.

Rollback boundary: if ADIF-CLI-T1 is rejected, remove only the new CLI
classification standard, registry, checker, checker tests, and CLI/test deltas
from the ADIF helper files.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ADIF resolver, ADIF preflight readout, ADIF finding-intake bridge, dispatch-quality parent checker and split modules |
| Runtime behavior claimed | direct local CLI entrypoints and classification checker |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - current sources support bounded CLI entrypoints and classification control |

## Evidence / Verification

| Evidence | Required or observed result |
|---|---|
| Focused unit tests | `python -m unittest governance.compat.test_run_adif_defect_resolver governance.compat.test_run_adif_preflight_readout governance.compat.test_run_adif_finding_intake_bridge governance.compat.test_check_cli_surface_classification` PASS, 44 tests |
| Resolver CLI smoke | ADIF ASSF-context query returned empty `items` and `totalCandidates=0` |
| Preflight CLI smoke | returned 2 of 10 closure candidates with truncation claim boundary |
| Finding intake CLI smoke | returned `LINK_TO_EXISTING_ENTRY` for `ADIF-0001` |
| Classification checker | `python governance/compat/check_cli_surface_classification.py --enforce` PASS with 9 entries and 0 violations |
| Provider/live proof | NOT_RUN_WITH_REASON: no live provider behavior is claimed |

## Artifact Manifest

| Artifact | Status |
|---|---|
| `docs/reference/CVF_CLI_SURFACE_CLASSIFICATION_STANDARD_2026-06-30.md` | CREATED |
| `governance/compat/CVF_CLI_SURFACE_CLASSIFICATION_REGISTRY.json` | CREATED |
| `governance/compat/check_cli_surface_classification.py` | CREATED |
| `governance/compat/test_check_cli_surface_classification.py` | CREATED |
| `governance/compat/run_adif_defect_resolver.py` | UPDATED |
| `governance/compat/run_adif_preflight_readout.py` | UPDATED |
| `governance/compat/run_adif_finding_intake_bridge.py` | UPDATED |
| ADIF helper tests | UPDATED |
| `docs/baselines/CVF_GC018_ADIF_CLI_T1_CLI_CLASSIFICATION_AND_ENTRYPOINTS_2026-06-30.md` | CREATED |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ADIF_CLI_T1_CLI_CLASSIFICATION_AND_ENTRYPOINTS_2026-06-30.md` | CREATED |
| `docs/reviews/CVF_ADIF_CLI_T1_CLI_CLASSIFICATION_AND_ENTRYPOINTS_COMPLETION_2026-06-30.md` | CREATED |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | ADIF resolver has a direct CLI without changing resolver API | unit tests and CLI smoke PASS |
| AC2 | ADIF preflight readout has a direct CLI without duplicating resolver logic | unit tests and CLI smoke PASS |
| AC3 | ADIF finding intake has a direct CLI that remains non-mutating | unit tests and CLI smoke PASS |
| AC4 | Central classification distinguishes CLI-required and module-only surfaces | registry and checker PASS |
| AC5 | No ASSF activation, MCP adapter, provider/live, public-sync, or ADIF entry mutation is claimed | claim boundary PASS |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| CVF skill id | N/A with reason: no CVF runtime skill package instruction body was consumed |
| Package root | N/A with reason: no package body was requested |
| Invocation context | local Python helper and governance checker work only |
| Receipt evidence | N/A with reason: no skill usage receipt is emitted for local ADIF helper CLI work |
| Output consumed by CVF | local command outputs and tests |
| Truth packet or source path | N/A with reason: no skill truth packet was consumed |
| Authority boundary | local CLI evidence does not activate skills or grant runtime package authority |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | N/A with reason: local Python and repo files only |
| Output consumed by CVF | N/A with reason: no provider skill output consumed |
| CVF source-of-truth promotion path | N/A with reason: no provider skill output promoted |
| Evidence artifact | this baseline, work order, and completion review |
| Authority boundary | provider-owned skill output is not CVF canonical authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | local CVF implementation -> no external knowledge promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ADIF-CLI-T1 baseline, work order, completion review, standard, registry, checker, and tests |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local CVF source verification only |
| Claim boundary | no external source, provider output, or provider-local memory is promoted as CVF authority |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ADIF_CLI_T1_CLI_CLASSIFICATION_AND_ENTRYPOINTS_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ADIF_CLI_T1_CLI_CLASSIFICATION_AND_ENTRYPOINTS_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: ADIF-CLI-T1 is a direct requested governance tranche, not a roadmap-derived tranche | N/A with reason | PASS |
| Registry JSON | `governance/compat/CVF_CLI_SURFACE_CLASSIFICATION_REGISTRY.json` | checker PASS | PASS |
| Registry Markdown | this standard | `Status: ACTIVE_STANDARD` | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no provider route, adapter, or package execution changed | N/A with reason | PASS |
| Session continuity | session-sync may follow material closure | N/A with reason | PASS |
| Focused tests | ADIF and CLI classification tests | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| ADIF resolver CLI | implemented | direct CLI smoke returned JSON | PASS |
| ADIF preflight CLI | implemented | direct CLI smoke returned bounded readout | PASS |
| ADIF finding intake CLI | implemented | direct CLI smoke returned `LINK_TO_EXISTING_ENTRY` | PASS |
| Classification checker | compliant | 9 entries, 0 violations | PASS |
| Unit test status | PASS | 44 tests PASS | PASS |
| Provider/live claim | none | NOT_RUN_WITH_REASON | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline references internal ADIF and governance helper surfaces.
Public-safe export requires separate public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ADIF-CLI-T1 CLI classification and entrypoints |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - local CLI entrypoints and classification checker implemented |
| receiptEvidence | N/A with reason: CLI smoke output and checker reports are local evidence, not Delta receipt evidence |
| actionEvidence | ACTION_EVIDENCE_PRESENT - standard, registry, checker, CLI entrypoints, tests, and closure docs |
| invocationBoundary | local Python CLI and governed Markdown/JSON sources only |
| interceptionBoundary | no IDE, shell hook, git hook, provider, MCP, Web, public-sync, or external runtime interception claim |
| claimLanguage | adds command entrypoints and centralized classification for helper surfaces |
| forbiddenExpansion | no ADIF entry mutation, ASSF activation, package body read, skill usage receipt emission, MCP adapter, provider/live proof, public-sync, or production-readiness claim |

## Claim Boundary

ADIF-CLI-T1 adds local CLI entrypoints and centralized classification only. It
does not activate skills, mutate ADIF entries, implement MCP adapters, call
providers, public-sync, or grant runtime authority.
