# CVF ASCP-T2 Activation Policy Semantics Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: completion_review

Batch ID: ASCP-T2

dispatchBaseHead: 76f632ff

executionBaseHead: 76f632ff

closureBaseHead: 76f632ff

## Purpose

Close ASCP-T2 after defining activation policy semantics and adding a bounded
policy resolver that distinguishes selected, activation-ready, body-read
requested, and used-with-receipt states.

## Target / Source

| Field | Value |
|---|---|
| Target artifact | ASCP-T2 activation policy standard, helper, tests, and roadmap update |
| Source work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_2026-06-30.md` |
| Paired baseline | `docs/baselines/CVF_GC018_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_2026-06-30.md` |
| Roadmap source | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` |
| Review disposition | CLOSED_PASS_BOUNDED |

## Scope / Methodology

Changed material scope:

- activation policy semantics standard;
- activation policy resolver helper;
- focused tests;
- ASCP roadmap T2/T3 status update;
- GC-018 baseline, work order, and completion review.

Out of scope and not changed:

- ASSF registry lifecycle sources;
- ASSF package roots;
- external CLI/MCP adapter code;
- provider route code;
- public-sync files.

## Findings / Position

ASCP-T2 is closed bounded. The policy helper classifies the evidence chain
without opening package bodies:

- selected package rows remain selection only;
- `ACTIVATION_READY` means the caller may explicitly invoke the runtime loader;
- `BODY_READ_REQUESTED` means the policy allows a loader body-read request;
- `USED_WITH_RECEIPT` requires matching `CVF_ASSF_SKILL_USAGE_RECEIPT`;
- output consumption without a matching receipt returns
  `USED_WITHOUT_RECEIPT_DENIED`;
- body-read request before readiness returns `BODY_READ_DENIED`.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| Readiness confused with body loading | controlled by policy state and no body read in helper |
| Body loading confused with consumed output | controlled by required usage receipt matching |
| Adapter work started before policy closure | controlled by roadmap T3 dependency |
| Lifecycle activation implied by policy state | controlled by claim boundaries and changed set |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`,
lifecyclePhase=`implementation`, surfaceSelector=`docs/reference/agent_system_skills`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure command:

```text
python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase implementation --surface-selector docs/reference/agent_system_skills --risk-ceiling HIGH --max-results 20 --json
```

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Define selected, ready, body-read requested, and used-with-receipt | work order Purpose; Mission | standard and helper states | unit tests | PASS |
| Preserve receipt-backed use requirement | Source Verification; Acceptance Criteria | `USED_WITH_RECEIPT` and denial path | unit tests | PASS |
| Defer external CLI/MCP adapter | Scope; Dual Agent Surface Matrix | ASCP-T3 ready after T2 | roadmap update | PASS |
| Keep lifecycle activation separate | Claim Boundary | no package/registry mutation | changed set review | PASS |

## Closure Diff Gate

| Requirement | Evidence | Disposition |
|---|---|---|
| Policy standard exists | `docs/reference/agent_system_skills/CVF_ASSF_ACTIVATION_POLICY_SEMANTICS_STANDARD.md` | PASS |
| Policy helper exists | `governance/compat/run_assf_activation_policy_resolver.py` | PASS |
| Policy tests exist | `governance/compat/test_run_assf_activation_policy_resolver.py` | PASS |
| Helper does not open package bodies | source and tests | PASS |
| Used-with-receipt requires matching receipt | unit tests | PASS |
| No package lifecycle mutation | changed set excludes package roots and registry entries | PASS |

## Verification / Evidence

| Evidence | Observed result |
|---|---|
| `python -m unittest governance.compat.test_run_assf_activation_policy_resolver` | PASS, 7 tests |
| `python governance/compat/run_assf_activation_policy_resolver.py --skill-id cvf-engineering-spec-driven-development --json` | PASS, returned `ACTIVATION_READY` |
| `python governance/compat/run_assf_activation_policy_resolver.py --skill-id cvf-engineering-spec-driven-development --body-read-requested` | PASS, returned `BODY_READ_REQUESTED` |
| Live provider proof | NOT_RUN_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| CVF skill id | N/A with reason: ASCP-T2 did not consume package instruction output as work evidence |
| Package root | N/A with reason: no package body was read by ASCP-T2 policy helper |
| Invocation context | ASCP-T2 policy classification tests and smokes |
| Receipt evidence | N/A with reason: no loader usage receipt output was consumed as evidence |
| Output consumed by CVF | policy resolver output and test results only |
| Truth packet or source path | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Authority boundary | policy receipts do not grant authority, activate packages, or bypass work-order scope |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | local Python helper and repo metadata only |
| Output consumed by CVF | N/A with reason: no provider skill output consumed |
| CVF source-of-truth promotion path | N/A with reason: no provider skill output promoted |
| Evidence artifact | this completion review |
| Authority boundary | provider-owned skill output is not CVF canonical authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | local CVF skill-control implementation -> no external knowledge promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASCP-T2 roadmap, baseline, work order, completion review, policy standard, helper, and tests |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local CVF source verification only |
| Claim boundary | no external source, provider output, or provider-local memory is promoted as CVF authority |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | ASCP-T2 activation policy semantics on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | apply_patch; Python unittest; policy resolver smokes |
| Target paths | policy standard, helper, tests, roadmap, baseline, work order, completion review |
| Allowed scope source | active next move plus ASCP-T2 baseline and work order |
| Before status evidence | base commit `76f632ff`; clean worktree before ASCP-T2 edits |
| After status evidence | pending material closure changed set |
| Diff evidence | focused tests, policy smokes, and governance gates |
| Approval boundary | active next move authorized ASCP-T2; live API keys not needed because no live behavior claim is made |
| Claim boundary | bounded local policy classification only |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `cvf-ascp-t2-activation-policy-semantics-2026-06-30` |
| Expected manifest | standard, helper, tests, roadmap update, baseline, work order, completion review |
| Actual changed set | standard, helper, tests, roadmap update, baseline, work order, completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this completion review references internal ASSF governance and private
provenance surfaces. Public-safe export requires separate public-sync
authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
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

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASCP-T2 activation policy semantics |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - local policy classification helper implemented |
| receiptEvidence | N/A with reason: policy decision receipts are local helper evidence, not Delta receipt evidence |
| actionEvidence | ACTION_EVIDENCE_PRESENT - standard, helper, tests, roadmap update, baseline, work order, and completion review |
| invocationBoundary | local Python helper and governed Markdown sources only |
| interceptionBoundary | no IDE, shell hook, git hook, provider, CLI/MCP adapter, Web, public-sync, or external runtime interception claim |
| claimLanguage | classifies selected, ready, body-read requested, and used-with-receipt states |
| forbiddenExpansion | no package body read by policy helper, skill usage receipt emission, lifecycle mutation, automatic invocation, external adapter, provider/live proof, public-sync, commit authority, or production-readiness claim |

## Claim Boundary

ASCP-T2 creates bounded activation policy semantics and local classification
only. It does not activate skills, mutate package lifecycle state, read package
instruction bodies, implement adapters, call providers, public-sync, or grant
action authority.
