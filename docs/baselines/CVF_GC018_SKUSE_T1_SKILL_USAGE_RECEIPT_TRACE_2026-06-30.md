# CVF GC-018 Baseline: SKUSE-T1 Skill Usage Receipt Trace

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: baseline

Batch ID: SKUSE-T1

dispatchBaseHead: 6372ea64

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | add CVF-owned skill usage receipt traceability for bounded ASSF runtime package body reads |
| Baseline | SKSOT-T1 closed with six runtime-eligible package truth packets and no ACTIVE resolver |
| Proposed tranche | loader receipt emission, optional receipt bundle output, receipt trace standard, checker, tests, and hook wiring |
| Execution route | Codex direct implementation with reviewer-owned closure |
| Closure posture | CLOSED_PASS_BOUNDED after focused tests, receipt smoke, checker, and governance gates |

## Purpose

SKUSE-T1 closes the next evidence gap after SKSOT-T1. Truth packets record what
CVF knows about a skill package. Usage receipts record that a specific eligible
package body read happened through the bounded loader and left inspectable
evidence.

## Scope / Methodology

Allowed SKUSE-T1 scope:

- add `skillUsageReceipts` to the bounded ASSF runtime package loader only when
  an eligible instruction body is explicitly requested and loaded;
- add optional `--receipt-out` JSON bundle output;
- create a stable skill usage receipt trace standard;
- add a markdown checker and focused tests;
- wire the checker into reviewer-fast, pre-commit, and autorun catalogs;
- create baseline, work order, and completion review evidence.

Forbidden SKUSE-T1 scope:

- automatic package activation;
- ACTIVE resolver behavior;
- package lifecycle promotion;
- external CLI/MCP adapter implementation;
- provider runtime interception or live provider proof;
- public-sync or production-readiness claims.

## Findings / Position

The runtime loader already gates package body reads by certification, UAT, and
internal-agent disposition. SKUSE-T1 keeps that gate intact and adds receipt
evidence for successful body reads. Denied packages and metadata-only readouts
produce no usage receipt.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`,
lifecyclePhase=`implementation`, surfaceSelector=`docs/reference/agent_system_skills`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: the read-only ADIF resolver returned no matching defects for
this implementation query.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF registry entries are authoritative per-skill sources | `docs/reference/agent_system_skills/registry/README.md` | Purpose | `entries/` | ASSF registry source family | LITERAL_INVARIANT | ACCEPT |
| ASSF package lifecycle fields include status, UAT, certification, and internal/external dispositions | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema; Internal-Agent And External-Agent CLI/MCP Disposition Fields | `status`; `uatState`; `certificationState`; `internalAgentDisposition`; `externalCliMcpDisposition` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Runtime loader opens package body only when explicitly requested and eligible | `governance/compat/run_assf_runtime_package_loader.py` | module docstring; `build_runtime_package_packet` | `include_instruction_bodies`; `packageBodyDisposition` | AGSK-R4 runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Runtime eligibility requires certified, UAT-passed, implemented internal disposition, and package root existence | `governance/compat/run_assf_runtime_package_loader.py` | `_runtime_ineligibility_reasons` | `certificationState`; `uatState`; `internalAgentDisposition`; `canonicalRoot` | AGSK-R4 runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Skill truth packets are source records for evidence, obligations, verification results, and truth receipts | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | Source Authority Boundary | `truth/packets/*.json` | SKSOT-T1 truth packet standard | LITERAL_INVARIANT | ACCEPT |
| CVF skill usage receipt trace checker is new in this tranche | `governance/compat/check_cvf_skill_usage_receipt_trace.py` | SKUSE-T1 new file | `check_text`; `validate_trace_section` | SKUSE-T1 checker | DOC_ONLY_NEW | ACCEPT |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update the bounded ASSF runtime package
loader to emit read receipts for eligible body reads, add one read-only receipt
trace checker, add focused tests, and wire the checker into governed local
workflow catalogs.

Protected paths:

- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/check_cvf_skill_usage_receipt_trace.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/run_assf_runtime_package_loader.py`
- `governance/compat/test_check_cvf_skill_usage_receipt_trace.py`
- `governance/compat/test_run_assf_runtime_package_loader.py`

Operator authorization: the operator agreed to make skill use leave traceable
evidence after SKSOT-T1 established skill truth packets.

Rollback boundary: if SKUSE-T1 is rejected, remove only the receipt changes,
new checker, tests, hook-catalog entries, SKUSE-T1 standard, and SKUSE-T1
artifacts. Do not revert prior SKSOT-T1, EPSOT-T1, AGSK-R7, or session-sync
commits unless a reviewer separately reopens those closures.

Scope boundary: this authorization does not extend to package lifecycle state,
ACTIVE resolver behavior, provider/live proof, external adapters, public-sync,
or production runtime.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation surface | `docs/reference/agent_system_skills/` |
| Storage decision | add stable receipt trace standard next to ASSF skill control-plane references |
| Stable filename disposition | `docs/reference/agent_system_skills/CVF_SKILL_USAGE_RECEIPT_TRACE_STANDARD.md` |
| Generated aggregate discipline | N/A with reason: no generated JSON aggregate is added |
| Authority boundary | loader receipts are evidence records; work orders, registry entries, and truth packets remain authority sources |
| Forbidden expansion | no ACTIVE resolver, adapter, package promotion, provider/live proof, or public export |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASSF registry README, ASSF package contract, runtime package loader, SKSOT-T1 truth packet standard, six runtime-eligible package roots |
| Runtime behavior claimed | read-only receipt emission for explicit eligible loader body reads |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - source supports receipt trace, not activation |

## Evidence / Verification

| Evidence | Required or observed result |
|---|---|
| Loader unit tests | receipt appears only for eligible loaded bodies |
| Checker unit tests | claim without trace fails; complete receipt trace passes |
| Real loader smoke | receipt emitted for `cvf-engineering-code-review-quality` |
| Provider/live proof | NOT_RUN_WITH_REASON: no live provider behavior is claimed |

## Artifact Manifest

| Artifact | Status |
|---|---|
| `docs/reference/agent_system_skills/CVF_SKILL_USAGE_RECEIPT_TRACE_STANDARD.md` | CREATED |
| `governance/compat/check_cvf_skill_usage_receipt_trace.py` | CREATED |
| `governance/compat/test_check_cvf_skill_usage_receipt_trace.py` | CREATED |
| `governance/compat/run_assf_runtime_package_loader.py` | UPDATED |
| `governance/compat/test_run_assf_runtime_package_loader.py` | UPDATED |
| governance hook catalogs | UPDATED |
| SKUSE-T1 work order and completion review | CREATED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | bounded loader JSON and governed markdown trace block | receipt proves explicit eligible body read only; no authority grant | focused tests and receipt smoke | no external adapter | `IMPLEMENTED_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter only | no external mutation, activation, provider call, public-sync, commit, or push | claim boundary | separate adapter contract required | `DEFERRED_WITH_REASON` |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Loader emits receipt for eligible loaded package bodies | unit tests and smoke PASS |
| AC2 | Loader emits no receipt for metadata-only or denied packages | unit tests PASS |
| AC3 | Stable receipt trace standard exists | standard created |
| AC4 | Markdown checker enforces trace block for CVF skill usage claims | checker tests PASS |
| AC5 | Checker is wired into governance catalogs | catalog diff PASS |
| AC6 | No ACTIVE, provider, external adapter, public-sync, or production claim is made | claim boundary PASS |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | USED_WITH_RECEIPT |
| CVF skill id | cvf-engineering-code-review-quality |
| Package root | docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/SKILL.md |
| Invocation context | SKUSE-T1 real loader smoke for receipt emission verification |
| Receipt evidence | skillUsageReceipt receiptId sha256:1c50b864577052203b184e414b75f1ed21b8868caab05624f81291e74a2439e4 |
| Output consumed by CVF | receipt metadata only; package instructions were not used as task authority |
| Truth packet or source path | docs/reference/agent_system_skills/truth/packets/cvf-engineering-code-review-quality.json |
| Authority boundary | receipt proves body read only and does not grant authority, activate a package, or bypass work-order scope |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed as CVF evidence |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | N/A with reason: local file and checker work only |
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
| Owner surface | SKUSE-T1 baseline, work order, completion review, receipt trace standard, loader, checker, and tests |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local CVF source verification only |
| Claim boundary | no external source, provider output, or provider-local memory is promoted as CVF authority in SKUSE-T1 |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_SKUSE_T1_SKILL_USAGE_RECEIPT_TRACE_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SKUSE_T1_SKILL_USAGE_RECEIPT_TRACE_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: operator-directed skill control-plane tranche, not a roadmap status edit | N/A with reason | PASS |
| Registry JSON | N/A with reason: SKUSE-T1 does not mutate ASSF registry lifecycle sources | N/A with reason | PASS |
| Registry Markdown | skill usage receipt trace standard | created | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no system-loop runtime change | N/A with reason | PASS |
| Session continuity | session-sync may follow material closure | N/A with reason | PASS |
| Focused tests | loader and receipt trace tests | PASS after execution | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Receipt type | `CVF_ASSF_SKILL_USAGE_RECEIPT` | real loader smoke emitted receipt | PASS |
| Receipt ID | `sha256:` value | `sha256:1c50b864577052203b184e414b75f1ed21b8868caab05624f81291e74a2439e4` | PASS |
| Checker status | PASS | `check_cvf_skill_usage_receipt_trace.py --base 6372ea64 --head HEAD --enforce` PASS | PASS |
| Unit test status | PASS | focused unittest PASS | PASS |
| Provider/live claim | none | NOT_RUN_WITH_REASON | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline references internal ASSF governance and private
provenance surfaces. Public-safe export requires separate redaction and
public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | SKUSE-T1 skill usage receipt trace |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - loader receipt emission and checker implemented |
| receiptEvidence | CVF_RECEIPT_PRESENT - loader receipt, focused tests, and governance gates |
| actionEvidence | ACTION_EVIDENCE_PRESENT - standard, loader, checker, tests, catalogs, and closure artifacts changed |
| invocationBoundary | local Python loader/checker and governed Markdown sources only |
| interceptionBoundary | no IDE, shell hook, git hook, provider, CLI/MCP, Web, public-sync, or external runtime interception claim |
| claimLanguage | creates receipt traceability for explicit eligible ASSF package body reads |
| forbiddenExpansion | no ACTIVE resolver, automatic invocation, external adapter, provider/live proof, public-sync, commit authority, or production-readiness claim |

## Claim Boundary

SKUSE-T1 creates bounded receipt traceability for explicit eligible ASSF runtime
package body reads through the internal loader. It does not change skill
package lifecycle state, activate package use, grant authority, expose
adapters, call providers, public-sync, or claim production readiness.
