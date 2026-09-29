# CVF GC-018 Baseline: ASCP-T4 Package Lifecycle Source-State Decision

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: baseline

Batch ID: ASCP-T4

dispatchBaseHead: 566cde63

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | keep ASSF package lifecycle sources unchanged; no package source moves to `ACTIVE` in ASCP-T4 |
| Baseline | ASCP-T1 through ASCP-T3 prove bounded readiness, policy classification, and external projection only |
| Proposed tranche | add a read-only package lifecycle decision helper, focused tests, roadmap update, work order, and completion evidence |
| Execution route | Codex direct implementation with reviewer-owned closure |
| Closure posture | CLOSED_PASS_BOUNDED after focused tests and local lifecycle decision smoke |

## Purpose

ASCP-T4 decides whether current package lifecycle sources should be promoted to
`ACTIVE`. The decision is bounded: 6 packages are runtime eligible and
activation ready, but `ACTIVATION_READY` is a body-read gate, not lifecycle
promotion. No registry entry, generated index, truth packet, or package root is
mutated by this tranche.

## Scope / Methodology

Allowed ASCP-T4 scope:

- add `governance/compat/run_assf_package_lifecycle_decision.py`;
- add `governance/compat/test_run_assf_package_lifecycle_decision.py`;
- update the ASCP roadmap row from T4 ready to T4 closed bounded;
- file baseline, work order, and completion evidence.

Forbidden ASCP-T4 scope:

- package lifecycle mutation to `ACTIVE`;
- ASSF registry entry edits or generated skill-index regeneration;
- package instruction body reads;
- emitting or consuming skill usage receipts;
- provider calls or live governance proof;
- package execution adapter, MCP server runtime, daemon, hook, or IDE bridge behavior;
- public-sync or production-readiness claims;
- remaining package conversion.

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
| ASCP roadmap requires T4 package lifecycle source decision after T3 closure | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | Work Plan | `ASCP-T4` | ASCP roadmap | VALUE_SET | ACCEPT |
| ASSF contract defines `ACTIVE` as lifecycle state selected for governed resolver/index use | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields | `ACTIVE` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Activation policy standard says `ACTIVATION_READY` permits explicit runtime loader body-read command and is not a package body read or usage receipt | `docs/reference/agent_system_skills/CVF_ASSF_ACTIVATION_POLICY_SEMANTICS_STANDARD.md` | State Semantics | `ACTIVATION_READY` | activation policy semantics standard | LITERAL_INVARIANT | ACCEPT |
| CLI/MCP projection denies external body reads and output use | `governance/compat/run_assf_cli_mcp_adapter_projection.py` | constants and `build_cli_mcp_adapter_projection` | `DENIED_EXTERNAL_BODY_READ_NOT_IMPLEMENTED` | CLI/MCP projection helper | RUNTIME_BEHAVIOR | ACCEPT |
| Runtime loader does not activate packages or mutate ASSF sources | `governance/compat/run_assf_runtime_package_loader.py` | `CLAIM_BOUNDARY`; `build_runtime_package_packet` | `include_instruction_bodies` | runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Provider registry surfaces are out of scope and untouched by ASCP-T4 | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | runtime source files | `ProviderRegistry`; `PROVIDER_CAPABILITY_REGISTRY` | Model Gateway provider registry surfaces | BOUNDARY_REFERENCE | ACCEPT |
| Package lifecycle decision helper is new in ASCP-T4 | `governance/compat/run_assf_package_lifecycle_decision.py` | ASCP-T4 new file | `build_package_lifecycle_decision` | package lifecycle decision helper | DOC_ONLY_NEW | ACCEPT |

## Provider Registry Boundary

ASCP-T4 makes no provider registry absence, hardcoded-provider,
provider-selection, provider-routing, model-capability, or live-governance
claim. Current provider registry surfaces are accounted for and remain
untouched: `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` exports
`ProviderRegistry`, and `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
declares `PROVIDER_CAPABILITY_REGISTRY`.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one bounded read-only lifecycle
decision helper and focused tests under `governance/compat`.

Protected paths:

- `governance/compat/run_assf_package_lifecycle_decision.py`
- `governance/compat/test_run_assf_package_lifecycle_decision.py`

Operator authorization: active next move authorizes ASCP-T4 package lifecycle
source-state decision after ASCP-T3 closure.

Rollback boundary: if ASCP-T4 is rejected, remove only the lifecycle decision
helper, its tests, ASCP-T4 artifacts, and the ASCP roadmap row update. Do not
revert ASCP-T1, ASCP-T2, ASCP-T3, SKUSE-T1, truth packets, or package
promotion commits.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASCP roadmap, ASSF package contract, activation policy semantics standard, runtime package loader, active resolver, CLI/MCP projection helper |
| Runtime behavior claimed | local package lifecycle decision receipt only |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - current sources support a hold decision, not lifecycle source mutation |

## Evidence / Verification

| Evidence | Required or observed result |
|---|---|
| Focused unit tests | `python -m unittest governance.compat.test_run_assf_package_lifecycle_decision` PASS, 5 tests |
| Lifecycle decision smoke | `python governance/compat/run_assf_package_lifecycle_decision.py --json` returned 32 total candidates, 6 runtime eligible, 6 activation ready, 6 external projection ready, 0 active source records, and `HOLD_NO_ACTIVE_SOURCE_MUTATION` |
| Changed set review | no registry entry, generated index, truth packet, or package root mutation |
| Provider/live proof | NOT_RUN_WITH_REASON: no live provider behavior is claimed |

## Artifact Manifest

| Artifact | Status |
|---|---|
| `governance/compat/run_assf_package_lifecycle_decision.py` | CREATED |
| `governance/compat/test_run_assf_package_lifecycle_decision.py` | CREATED |
| `docs/baselines/CVF_GC018_ASCP_T4_PACKAGE_LIFECYCLE_SOURCE_STATE_DECISION_2026-06-30.md` | CREATED |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T4_PACKAGE_LIFECYCLE_SOURCE_STATE_DECISION_2026-06-30.md` | CREATED |
| `docs/reviews/CVF_ASCP_T4_PACKAGE_LIFECYCLE_SOURCE_STATE_DECISION_COMPLETION_2026-06-30.md` | CREATED |
| `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | UPDATED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | package lifecycle decision helper | summarizes readiness/projection evidence and source mutation decision only | ASCP-T4 tests and smoke | no external adapter | `IMPLEMENTED_BOUNDED_DECISION` |
| `INTERNAL_AGENT` | runtime package loader | may open package bodies only after explicit eligible body-read request | ASCP-T1/T2 evidence | no lifecycle promotion | `IMPLEMENTED_BOUNDED_BODY_READ` |
| `EXTERNAL_AGENT_CLI_MCP` | CLI/MCP projection helper | metadata and policy-state readout only | ASCP-T3 tests and smoke | body reads and output use denied | `IMPLEMENTED_BOUNDED_PROJECTION` |
| `EXTERNAL_AGENT_CLI_MCP` | package execution adapter | no package body read or output use authorized | N/A with reason: execution adapter not implemented | separate adapter/runtime work order required | `DEFERRED_WITH_REASON` |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Decision helper summarizes runtime eligible, activation ready, external projection ready, and active source records | unit tests and smoke PASS |
| AC2 | Decision emits `HOLD_NO_ACTIVE_SOURCE_MUTATION` | unit tests and smoke PASS |
| AC3 | Decision emits no recommended source mutations | unit tests PASS |
| AC4 | Helper does not open package instruction bodies or write files | unit tests PASS |
| AC5 | Roadmap records ASCP-T4 closure and keeps ASCP-T5 value-parked | roadmap update PASS |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| CVF skill id | N/A with reason: ASCP-T4 did not consume package instruction output as work evidence |
| Package root | N/A with reason: no package body was read by ASCP-T4 decision helper |
| Invocation context | ASCP-T4 decision tests and smoke |
| Receipt evidence | N/A with reason: no loader usage receipt output was consumed as evidence |
| Output consumed by CVF | local readiness/projection decision output only |
| Truth packet or source path | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Authority boundary | lifecycle decision receipt does not grant authority, activate packages, or bypass work-order scope |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed as CVF evidence |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | local file and helper work only |
| Output consumed by CVF | N/A with reason: no provider skill output consumed |
| CVF source-of-truth promotion path | N/A with reason: no provider skill output promoted |
| Evidence artifact | this baseline, work order, and completion review |
| Authority boundary | provider-owned skill output is not CVF canonical authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | local CVF skill-control implementation -> no external knowledge promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASCP-T4 baseline, work order, completion review, helper, tests, and roadmap |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local CVF source verification only |
| Claim boundary | no external source, provider output, or provider-local memory is promoted as CVF authority |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline references internal ASSF governance and private
provenance surfaces. Public-safe export requires separate public-sync
authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T4_PACKAGE_LIFECYCLE_SOURCE_STATE_DECISION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASCP_T4_PACKAGE_LIFECYCLE_SOURCE_STATE_DECISION_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | `Status: ACTIVE_ROADMAP` | PASS |
| Registry JSON | N/A with reason: no registry mutation authorized or performed | N/A with reason | PASS |
| Registry Markdown | N/A with reason: no registry markdown mutation | N/A with reason | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no provider route, execution adapter, or package execution changed | N/A with reason | PASS |
| Session continuity | session-sync may follow material closure | N/A with reason | PASS |
| Focused tests | lifecycle decision tests | PASS | PASS |
| Runtime smoke | lifecycle decision smoke | PASS | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Lifecycle decision | `HOLD_NO_ACTIVE_SOURCE_MUTATION` | helper emits required decision token | PASS |
| Source mutation disposition | `NO_SOURCE_MUTATIONS_AUTHORIZED` | helper emits required disposition | PASS |
| Runtime eligible count | 6 | lifecycle decision smoke observed 6 | PASS |
| Activation ready count | 6 | lifecycle decision smoke observed 6 | PASS |
| Active source count | 0 | lifecycle decision smoke observed 0 | PASS |
| Unit test status | PASS | `python -m unittest governance.compat.test_run_assf_package_lifecycle_decision` PASS | PASS |
| Provider/live claim | none | NOT_RUN_WITH_REASON | PASS |

## Claim Boundary

ASCP-T4 implements a bounded read-only lifecycle source-state decision only. It
does not activate skills, mutate package lifecycle state, read package
instruction bodies, emit or consume skill usage receipts, implement execution
adapters, call providers, public-sync, or grant action authority.
