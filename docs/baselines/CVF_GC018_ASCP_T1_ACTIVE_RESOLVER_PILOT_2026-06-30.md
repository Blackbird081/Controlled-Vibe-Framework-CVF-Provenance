# CVF GC-018 Baseline: ASCP-T1 ACTIVE Resolver Pilot

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: baseline

Batch ID: ASCP-T1

dispatchBaseHead: c134346e

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | add a read-only ASSF activation-readiness resolver between metadata selection and package body loading |
| Baseline | SKSOT-T1 truth packets and SKUSE-T1 usage receipts are closed; no ACTIVE resolver existed |
| Proposed tranche | helper, focused tests, roadmap, baseline, work order, and completion evidence |
| Execution route | Codex direct implementation with reviewer-owned closure |
| Closure posture | CLOSED_PASS_BOUNDED after focused tests and resolver smoke |

## Purpose

ASCP-T1 closes the control-plane gap between metadata resolution and runtime
package body reads. It decides whether a package is activation-ready using
generated ASSF metadata, generated truth-packet index data, and the existing
runtime loader eligibility gate.

## Scope / Methodology

Allowed ASCP-T1 scope:

- create a read-only active resolver helper;
- reuse the runtime loader eligibility gate without body reads;
- require approved STRICT runtime-eligible truth index records before
  `ACTIVATION_READY`;
- emit deterministic resolver decision receipts;
- deny `EXTERNAL_AGENT_CLI_MCP` until a separate adapter tranche exists;
- add focused unit tests and local smoke evidence.

Forbidden ASCP-T1 scope:

- loading package instruction bodies;
- emitting skill usage receipts;
- lifecycle promotion to `ACTIVE`;
- external CLI/MCP adapter implementation;
- provider calls or live governance proof;
- public-sync or production-readiness claims.

## Findings / Position

ASCP-T1 should not mark packages `ACTIVE` in source. The helper returns
activation-readiness decisions for current source state. Lifecycle mutation and
automatic invocation remain future governed decisions.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`,
lifecyclePhase=`implementation`, surfaceSelector=`docs/reference/agent_system_skills`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: the ADIF resolver was called through Python import because the
module has no CLI `main()` output path.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF lifecycle includes `ACTIVE` but adapter loading must not imply activation | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields; Provider Adapter Boundary | `ACTIVE`; `adapterContract` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Runtime loader can compute eligibility without instruction bodies | `governance/compat/run_assf_runtime_package_loader.py` | `build_runtime_package_packet` | `include_instruction_bodies` | runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Runtime eligibility requires certification, UAT, internal implementation, and package root existence | `governance/compat/run_assf_runtime_package_loader.py` | `_runtime_ineligibility_reasons` | `certificationState`; `uatState`; `internalAgentDisposition`; `canonicalRoot` | runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Truth index exposes runtime eligibility and truth receipt hashes | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` | root `entries` | `runtimeEligibility`; `receiptHash` | generated skill truth index | VALUE_SET | ACCEPT |
| External adapter remains deferred until separate implementation evidence exists | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | Adapter Admission Boundary | `EXTERNAL_AGENT_CLI_MCP` | external readout boundary contract | LITERAL_INVARIANT | ACCEPT |
| ACTIVE resolver helper is new in ASCP-T1 | `governance/compat/run_assf_active_resolver.py` | ASCP-T1 new file | `build_active_resolver_packet` | active resolver helper | DOC_ONLY_NEW | ACCEPT |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one read-only ASSF active resolver
helper and focused tests under `governance/compat`.

Protected paths:

- `governance/compat/run_assf_active_resolver.py`
- `governance/compat/test_run_assf_active_resolver.py`

Operator authorization: the operator approved continuing into ACTIVE resolver,
CLI/MCP adapter, and package activation sequencing after source-of-truth and
usage receipt work.

Rollback boundary: if ASCP-T1 is rejected, remove only the active resolver
helper, its tests, and ASCP-T1 roadmap/baseline/work-order/review artifacts.
Do not revert SKSOT-T1, SKUSE-T1, or prior package promotion commits.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation surface | `docs/reference/agent_system_skills/` and `governance/compat` |
| Storage decision | add a local helper, not a generated aggregate |
| Stable filename disposition | `governance/compat/run_assf_active_resolver.py` |
| Generated aggregate discipline | N/A with reason: no generated JSON aggregate is added |
| Authority boundary | resolver decisions are evidence; package sources, truth packets, and work orders remain authority |
| Forbidden expansion | no package body read, lifecycle mutation, adapter, provider/live proof, or public export |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASSF package contract, runtime package loader, truth index, usage receipt standard, external adapter boundary contract |
| Runtime behavior claimed | read-only activation-readiness decision helper |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - current sources support resolver decision behavior, not activation or adapter behavior |

## Evidence / Verification

| Evidence | Required or observed result |
|---|---|
| Focused unit tests | `python -m unittest governance.compat.test_run_assf_active_resolver` PASS |
| Resolver smoke | `python governance/compat/run_assf_active_resolver.py --json --max-results 100` observed 32 candidates and 6 `ACTIVATION_READY` items |
| Provider/live proof | NOT_RUN_WITH_REASON: no live provider behavior is claimed |

## Artifact Manifest

| Artifact | Status |
|---|---|
| `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | CREATED |
| `governance/compat/run_assf_active_resolver.py` | CREATED |
| `governance/compat/test_run_assf_active_resolver.py` | CREATED |
| `docs/baselines/CVF_GC018_ASCP_T1_ACTIVE_RESOLVER_PILOT_2026-06-30.md` | CREATED |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T1_ACTIVE_RESOLVER_PILOT_2026-06-30.md` | CREATED |
| `docs/reviews/CVF_ASCP_T1_ACTIVE_RESOLVER_PILOT_COMPLETION_2026-06-30.md` | CREATED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | active resolver helper | activation-readiness decision only; no body read or authority grant | focused tests and smoke | no external adapter | `IMPLEMENTED_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter only | denied until separate adapter implementation | boundary contract | separate adapter contract required | `DEFERRED_WITH_REASON` |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Resolver returns `ACTIVATION_READY` only when loader eligibility and truth requirements pass | unit tests PASS |
| AC2 | Resolver does not emit skill usage receipts or read package bodies | unit tests and code path PASS |
| AC3 | External CLI/MCP consumer is denied until adapter exists | unit tests PASS |
| AC4 | Real repo smoke observes 6 ready packages | resolver smoke PASS |
| AC5 | No lifecycle, provider, adapter, public-sync, or production claim is made | claim boundary PASS |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| CVF skill id | N/A with reason: ASCP-T1 did not consume package instruction output as work evidence |
| Package root | N/A with reason: no package body was requested |
| Invocation context | ASCP-T1 resolver smoke used metadata and truth index only |
| Receipt evidence | N/A with reason: no `skillUsageReceipt` is emitted until the runtime loader explicitly reads an eligible body |
| Output consumed by CVF | resolver decision receipt metadata only |
| Truth packet or source path | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Authority boundary | resolver decision receipt does not grant authority, activate a package, or bypass work-order scope |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed as CVF evidence |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | local file and checker work only |
| Output consumed by CVF | N/A with reason: no provider skill output consumed |
| CVF source-of-truth promotion path | N/A with reason: no provider skill output promoted |
| Evidence artifact | this baseline, work order, and completion review |
| Authority boundary | provider-owned skill output is not CVF canonical authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | local CVF skill-control implementation -> no external knowledge promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASCP-T1 baseline, work order, completion review, roadmap, helper, and tests |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local CVF source verification only |
| Claim boundary | no external source, provider output, or provider-local memory is promoted as CVF authority |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T1_ACTIVE_RESOLVER_PILOT_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASCP_T1_ACTIVE_RESOLVER_PILOT_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | `Status: ACTIVE_ROADMAP` | PASS |
| Registry JSON | N/A with reason: ASCP-T1 does not mutate ASSF registry lifecycle sources | N/A with reason | PASS |
| Registry Markdown | N/A with reason: no registry markdown mutation | N/A with reason | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no provider route, adapter, or package execution changed | N/A with reason | PASS |
| Session continuity | session-sync may follow material closure | N/A with reason | PASS |
| Focused tests | active resolver tests | PASS after execution | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Resolver receipt type | `CVF_ASSF_ACTIVE_RESOLVER_DECISION_RECEIPT` | unit test verified receipt type | PASS |
| Ready package count | 6 | smoke observed 6 `ACTIVATION_READY` items | PASS |
| Total generated candidates | 32 | smoke observed 32 total candidates | PASS |
| Provider/live claim | none | NOT_RUN_WITH_REASON | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline references internal ASSF governance and private
provenance surfaces. Public-safe export requires separate redaction and
public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASCP-T1 active resolver pilot |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - local resolver decision helper implemented |
| receiptEvidence | N/A with reason: resolver decision receipts are ASCP helper evidence, not Delta receipt evidence |
| actionEvidence | ACTION_EVIDENCE_PRESENT - helper, tests, roadmap, baseline, work order, and completion review |
| invocationBoundary | local Python helper and governed Markdown sources only |
| interceptionBoundary | no IDE, shell hook, git hook, provider, CLI/MCP, Web, public-sync, or external runtime interception claim |
| claimLanguage | creates activation-readiness decisions for current runtime-eligible packages |
| forbiddenExpansion | no package body read, skill usage receipt emission, lifecycle mutation, automatic invocation, external adapter, provider/live proof, public-sync, commit authority, or production-readiness claim |

## Claim Boundary

ASCP-T1 creates bounded local activation-readiness decisions. It does not
change package lifecycle state, read package instruction bodies, activate
packages, expose adapters, call providers, public-sync, or grant action
authority.
