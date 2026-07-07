# CVF GC-018 Baseline: AGSK-R5 Runtime Eligibility Audit

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: baseline

Batch ID: AGSK-R5

dispatchBaseHead: 7e64e8bf

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | implement a bounded ASSF runtime eligibility audit helper |
| Baseline | AGSK-R4 added the runtime package loader at `416eb689`; session-sync closed at `7e64e8bf` |
| Proposed tranche | AGSK-R5 audit helper and focused tests |
| Execution route | Codex direct implementation with reviewer-owned commit |
| Closure posture | CLOSED_PASS_BOUNDED after focused tests, real-index audit, and governance gates |

## Purpose

AGSK-R5 adds a no-body audit layer over the AGSK-R4 runtime package loader. The
helper summarizes ASSF metadata, lifecycle states, package-root counts, runtime
eligibility counts, and denial reason buckets so future lifecycle promotion
work can start from machine-readable evidence instead of manually reading the
full package-loader packet.

This baseline does not certify, activate, approve, or implement any package
lifecycle state. It does not request or open package instruction bodies.

## Scope / Methodology

Allowed AGSK-R5 scope:

- add `governance/compat/run_assf_runtime_eligibility_audit.py`;
- add `governance/compat/test_run_assf_runtime_eligibility_audit.py`;
- reuse AGSK-R4 loader eligibility behavior;
- summarize generated-index metadata and denial reasons;
- support package-root-only filtering for AGSK-R3 package roots;
- run focused tests and real-index audit commands.

Forbidden AGSK-R5 scope:

- editing ASSF registry entries, package roots, generated index, resolver, hook
  catalogs, Web runtime, provider/live paths, public-sync paths, or session
  state;
- setting any package to `APPROVED`, `ACTIVE`, `PASSED`, `CERTIFIED`, or
  `IMPLEMENTED`;
- opening package instruction bodies;
- claiming CLI/MCP adapter behavior, provider proof, public export, production
  readiness, or action authority.

## Findings / Position

AGSK-R4 can answer one package request at a time. AGSK-R5 makes the next
operator question easier: how many ASSF records are runtime eligible, and why
are the AGSK-R3 package roots still blocked?

The current real-index audit shows 24 package roots, all `PROPOSED`, all
`uatState=NOT_STARTED`, all `certificationState=NOT_STARTED`, all
`internalAgentDisposition=CANDIDATE`, and zero runtime-eligible package roots.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| Audit could be mistaken for lifecycle promotion | Claim boundary denies certification, activation, lifecycle mutation, and authority grant |
| Audit could duplicate loader gate logic and drift | Helper reuses `build_runtime_package_packet` from AGSK-R4 |
| Package body could be opened during audit | Helper always calls the loader with instruction bodies disabled |
| All-package output could obscure AGSK-R3 package roots | Helper supports `--package-roots-only` |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one read-only governance helper and one
focused test under `governance/compat/` for ASSF runtime eligibility auditing.

Protected paths:

- `governance/compat/run_assf_runtime_eligibility_audit.py`
- `governance/compat/test_run_assf_runtime_eligibility_audit.py`

Operator authorization: operator requested continuing ASSF metadata and
runtime-condition evaluation on 2026-06-30.

Rollback boundary: remove only the AGSK-R5 audit helper, focused test, paired
governance artifacts, and completion evidence. Do not revert AGSK-R4 loader,
AGSK-R3 package roots, registry entries, generated index, or session-sync
commit `7e64e8bf`.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`,
lifecyclePhase=`implementation`, surfaceSelector=`governance/compat`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: the read-only ADIF resolver returned no matching defects for
this implementation query.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Runtime loader already builds bounded metadata packets and exposes total candidate counts | `governance/compat/run_assf_runtime_package_loader.py` | `RuntimePackagePacket`; `build_runtime_package_packet` | `build_runtime_package_packet` | AGSK-R4 runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Runtime loader has explicit ineligibility reasons for certification, UAT, internal disposition, and package roots | `governance/compat/run_assf_runtime_package_loader.py` | `_runtime_ineligibility_reasons` | `_runtime_ineligibility_reasons` | AGSK-R4 runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| ASSF package contract requires lifecycle and internal disposition metadata fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `uatState`; `certificationState`; `internalAgentDisposition` | ASSF package contract | EXISTS | ACCEPT |
| Certification requires UAT before certification | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `certificationState`; `uatState` | ASSF certification lifecycle contract | LITERAL_INVARIANT | ACCEPT |
| Generated index remains metadata-only and denies runtime activation authority | `docs/reference/agent_system_skills/generated/skill-index.json` | `claimBoundary` | `claimBoundary` | ASSF generated index | LITERAL_INVARIANT | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | AGSK-R4 loader, ASSF package contract, certification lifecycle contract, generated skill index |
| Runtime behavior claimed | no-body audit summary only |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - source supports a no-body eligibility audit, not package activation |

## Evidence / Verification

| Evidence | Required or observed result |
|---|---|
| Focused unit tests | `python -m unittest governance.compat.test_run_assf_runtime_eligibility_audit` PASS, 3 tests |
| Loader regression tests | `python -m unittest governance.compat.test_run_assf_runtime_package_loader` PASS, 7 tests |
| Real-index package-root audit | 24 package roots, 0 runtime eligible, 24 blocked by certification, UAT, and internal disposition |
| Real-index all-record audit | 32 records, 0 runtime eligible |

## Artifact Manifest

| Artifact | Status |
|---|---|
| `governance/compat/run_assf_runtime_eligibility_audit.py` | IMPLEMENTED |
| `governance/compat/test_run_assf_runtime_eligibility_audit.py` | IMPLEMENTED |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_2026-06-30.md` | CLOSED_PASS_BOUNDED |
| `docs/reviews/CVF_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_COMPLETION_2026-06-30.md` | CLOSED_PASS_BOUNDED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | `run_assf_runtime_eligibility_audit.py` | internal agents may read metadata summary and denial buckets only; no instruction body or action authority is granted | focused tests and real-index audit | no external adapter | `IMPLEMENTED_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter only | external agents cannot use this helper to mutate, activate, execute, or publish packages | claim boundary | separate adapter work order required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | AGSK-R4 runtime package loader -> AGSK-R5 runtime eligibility audit |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | AGSK-R5 baseline, work order, completion review, audit helper, and focused tests |
| Disposition | IMPLEMENT bounded internal metadata audit; defer activation, certification, external adapter, provider/live, and public-sync |
| Claim boundary | No external source or provider-local memory is promoted as CVF authority in AGSK-R5 |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Audit summarizes runtime eligibility counts from generated metadata | focused tests PASS |
| AC2 | Audit reports ineligibility reason buckets | focused tests PASS |
| AC3 | Audit supports package-root-only filtering | focused tests PASS |
| AC4 | Audit does not request instruction bodies | claim boundary and focused tests PASS |
| AC5 | Real AGSK-R3 package roots are reported as 24 blocked package roots and 0 runtime eligible | real-index audit PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: AGSK-R5 is operator-directed follow-on audit helper, not a roadmap status edit | N/A with reason | PASS |
| Registry JSON | N/A with reason: no registry JSON or generated index edit in AGSK-R5 | no changed registry path | PASS |
| Registry Markdown | N/A with reason: no registry Markdown edit in AGSK-R5 | N/A with reason | PASS |
| External evidence digest | N/A with reason: no external evidence digest created; AGSK-R5 consumes existing governed ASSF metadata | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no system-loop interlock roadmap or runtime loop change in AGSK-R5 | N/A with reason | PASS |
| Session continuity | N/A with reason: material baseline does not update session state; session-sync may follow after material commit | N/A with reason | PASS |
| Focused tests | `governance/compat/test_run_assf_runtime_eligibility_audit.py` | 3 unittest cases PASS | PASS |
| Runtime audit smoke | `governance/compat/run_assf_runtime_eligibility_audit.py` | package-root audit reports 24 blocked, 0 eligible | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline references private provenance package roots and internal
governance helper implementation. Public-safe export requires separate
redaction and public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AGSK-R5 bounded ASSF runtime eligibility audit |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - helper summarizes metadata and denial reasons without opening instruction bodies |
| receiptEvidence | CVF_RECEIPT_PRESENT - focused tests and real-index audit commands |
| actionEvidence | ACTION_EVIDENCE_PRESENT - helper, test, and source verification |
| invocationBoundary | governed local Python helper and tests only |
| interceptionBoundary | no IDE, shell hook, git, provider, CLI/MCP, Web, public-sync, or external runtime interception claim |
| claimLanguage | summarizes current ASSF runtime eligibility metadata |
| forbiddenExpansion | no package promotion, certification, registry/index mutation, resolver activation, external adapter, provider/live proof, public-sync, or production-readiness claim |

## Claim Boundary

AGSK-R5 implements an internal metadata audit helper only. It does not activate
packages, certify packages, mutate lifecycle state, open instruction bodies,
grant authority, expose external adapters, call providers, public-sync, or
claim production readiness.
