# CVF GC-018 Baseline: ASCP-T2 Activation Policy Semantics

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: baseline

Batch ID: ASCP-T2

dispatchBaseHead: 76f632ff

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | add a bounded activation policy semantics layer above the active resolver |
| Baseline | ASCP-T1 active resolver is closed; selected, ready, body-read, and used states need explicit separation before adapter work |
| Proposed tranche | reference standard, policy helper, focused tests, roadmap update, work order, and completion evidence |
| Execution route | Codex direct implementation with reviewer-owned closure |
| Closure posture | CLOSED_PASS_BOUNDED after focused tests and local smokes |

## Purpose

ASCP-T2 defines and implements the local policy distinction between metadata
selection, activation readiness, body-read request, and receipt-backed package
use. This prevents future CLI/MCP adapter work from treating a ready decision
as a body read or treating a body read as consumed package output without
receipt evidence.

## Scope / Methodology

Allowed ASCP-T2 scope:

- add `docs/reference/agent_system_skills/CVF_ASSF_ACTIVATION_POLICY_SEMANTICS_STANDARD.md`;
- add `governance/compat/run_assf_activation_policy_resolver.py`;
- add `governance/compat/test_run_assf_activation_policy_resolver.py`;
- update the ASCP roadmap row from T2 ready to T2 closed and T3 ready;
- file baseline, work order, and completion evidence.

Forbidden ASCP-T2 scope:

- package lifecycle mutation to `ACTIVE`;
- package instruction body reads outside the existing runtime loader;
- emitting `skillUsageReceipts` from the policy helper;
- external CLI/MCP adapter implementation;
- provider calls or live governance proof;
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
| Active resolver returns `ACTIVATION_READY` and requires package body receipt afterward | `governance/compat/run_assf_active_resolver.py` | `ActiveResolverItem.to_dict`; `_decision_for` | `activationDecision`; `packageBodyReceiptRequired` | active resolver helper | RUNTIME_BEHAVIOR | ACCEPT |
| Active resolver does not emit usage receipts | `governance/compat/run_assf_active_resolver.py` | `ActiveResolverPacket.to_dict` | `resolverDecisionReceipts` | active resolver packet schema | RUNTIME_BEHAVIOR | ACCEPT |
| Runtime loader owns body reads and usage receipts | `governance/compat/run_assf_runtime_package_loader.py` | `build_runtime_package_packet`; `_build_skill_usage_receipt` | `include_instruction_bodies`; `skillUsageReceipts` | runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Usage receipt standard limits receipt meaning to explicit eligible body reads | `docs/reference/agent_system_skills/CVF_SKILL_USAGE_RECEIPT_TRACE_STANDARD.md` | Receipt Source; Authority Boundary | `CVF_ASSF_SKILL_USAGE_RECEIPT` | skill usage receipt trace standard | LITERAL_INVARIANT | ACCEPT |
| External adapter implementation remains deferred | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | Adapter Admission Boundary | `EXTERNAL_AGENT_CLI_MCP` | external readout boundary contract | LITERAL_INVARIANT | ACCEPT |
| Activation policy resolver helper is new in ASCP-T2 | `governance/compat/run_assf_activation_policy_resolver.py` | ASCP-T2 new file | `build_activation_policy_packet` | activation policy resolver | DOC_ONLY_NEW | ACCEPT |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one bounded activation policy helper
and focused tests under `governance/compat`.

Protected paths:

- `governance/compat/run_assf_activation_policy_resolver.py`
- `governance/compat/test_run_assf_activation_policy_resolver.py`

Operator authorization: the active next move authorizes ASCP-T2 activation
policy semantics before CLI/MCP adapter implementation.

Rollback boundary: if ASCP-T2 is rejected, remove only the policy helper, its
tests, the policy standard, ASCP-T2 artifacts, and the ASCP roadmap row update.
Do not revert ASCP-T1, SKUSE-T1, truth packets, or package promotion commits.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASSF package contract, active resolver, runtime loader, usage receipt standard, external adapter boundary, ASCP roadmap |
| Runtime behavior claimed | local activation policy classification only |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - current sources support policy classification, not activation or adapter behavior |

## Evidence / Verification

| Evidence | Required or observed result |
|---|---|
| Focused unit tests | `python -m unittest governance.compat.test_run_assf_activation_policy_resolver` PASS, 7 tests |
| Policy smoke | `python governance/compat/run_assf_activation_policy_resolver.py --skill-id cvf-engineering-spec-driven-development --json` returned `ACTIVATION_READY` |
| Body-read request smoke | `python governance/compat/run_assf_activation_policy_resolver.py --skill-id cvf-engineering-spec-driven-development --body-read-requested` returned `BODY_READ_REQUESTED` |
| Provider/live proof | NOT_RUN_WITH_REASON: no live provider behavior is claimed |

## Artifact Manifest

| Artifact | Status |
|---|---|
| `docs/reference/agent_system_skills/CVF_ASSF_ACTIVATION_POLICY_SEMANTICS_STANDARD.md` | CREATED |
| `governance/compat/run_assf_activation_policy_resolver.py` | CREATED |
| `governance/compat/test_run_assf_activation_policy_resolver.py` | CREATED |
| `docs/baselines/CVF_GC018_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_2026-06-30.md` | CREATED |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_2026-06-30.md` | CREATED |
| `docs/reviews/CVF_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_COMPLETION_2026-06-30.md` | CREATED |
| `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | UPDATED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | activation policy helper | selected/ready/body-read/use classification only | focused tests and local smokes | no external adapter | `IMPLEMENTED_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter only | may not receive adapter behavior before ASCP-T3 | boundary contract and policy standard | separate adapter contract required | `DEFERRED_WITH_REASON` |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Policy states distinguish selected, ready, body-read requested, and used-with-receipt | unit tests PASS |
| AC2 | Consumed output without matching receipt is denied | unit tests PASS |
| AC3 | Policy helper does not open package bodies or emit usage receipts | source and tests PASS |
| AC4 | External consumer remains not activation-ready until adapter work | unit tests PASS |
| AC5 | Roadmap advances ASCP-T3 only after T2 closure | roadmap update PASS |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| CVF skill id | N/A with reason: ASCP-T2 did not consume package instruction output as work evidence |
| Package root | N/A with reason: no package body was read by ASCP-T2 policy helper |
| Invocation context | ASCP-T2 policy classification tests and smokes |
| Receipt evidence | N/A with reason: no loader usage receipt output was consumed as evidence |
| Output consumed by CVF | local policy resolver output only |
| Truth packet or source path | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Authority boundary | policy receipts do not grant authority, activate packages, or bypass work-order scope |

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
| Owner surface | ASCP-T2 baseline, work order, completion review, policy standard, helper, tests, and roadmap |
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
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | `Status: ACTIVE_ROADMAP` | PASS |
| Registry JSON | N/A with reason: no registry mutation authorized or performed | N/A with reason | PASS |
| Registry Markdown | N/A with reason: no registry markdown mutation | N/A with reason | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no provider route, adapter, or package execution changed | N/A with reason | PASS |
| Session continuity | session-sync may follow material closure | N/A with reason | PASS |
| Focused tests | activation policy tests | PASS | PASS |
| Runtime smoke | activation policy resolver smokes | PASS | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Policy receipt type | `CVF_ASSF_ACTIVATION_POLICY_DECISION_RECEIPT` | helper emits policy decision receipts | PASS |
| Ready smoke state | `ACTIVATION_READY` | smoke returned `ACTIVATION_READY` | PASS |
| Body-read request state | `BODY_READ_REQUESTED` | smoke returned `BODY_READ_REQUESTED` | PASS |
| Unit test status | PASS | `python -m unittest governance.compat.test_run_assf_activation_policy_resolver` PASS | PASS |
| Provider/live claim | none | NOT_RUN_WITH_REASON | PASS |

## Claim Boundary

ASCP-T2 defines and implements bounded activation policy classification only.
It does not activate skills, mutate package lifecycle state, read package
instruction bodies, implement adapters, call providers, public-sync, or grant
action authority.
