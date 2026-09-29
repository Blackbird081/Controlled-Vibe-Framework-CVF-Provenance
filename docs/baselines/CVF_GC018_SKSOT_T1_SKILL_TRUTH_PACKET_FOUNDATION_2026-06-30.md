# CVF GC-018 Baseline: SKSOT-T1 Skill Truth Packet Foundation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: baseline

Batch ID: SKSOT-T1

dispatchBaseHead: 291788b6

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | create a CVF-governed skill source-of-truth packet foundation for existing runtime-eligible ASSF packages |
| Baseline | AGSK-R7 closed with six runtime-eligible package roots and no ACTIVE resolver or external adapter |
| Proposed tranche | standard, packet source layout, generated truth index, checker, tests, and hook wiring |
| Execution route | Codex direct implementation with reviewer-owned closure |
| Closure posture | CLOSED_PASS_BOUNDED after packet checker, unit tests, and governance gates |

## Purpose

SKSOT-T1 gives CVF a central truth-record layer for skill package governance.
It records provenance labels, evidence, obligations, verification results, and
receipt hashes for the six package roots that already satisfy ASSF runtime
eligibility.

This baseline absorbs useful private Truth Kernel reference patterns into
CVF-owned skill governance. The private reference input is not canonical CVF
authority.

## Scope / Methodology

Allowed SKSOT-T1 scope:

- create a skill truth packet standard;
- create `docs/reference/agent_system_skills/truth/` packet and generated-index layout;
- seed packets for the six already runtime-eligible ASSF package roots;
- add `governance/compat/check_skill_truth_packets.py` and tests;
- wire the checker into reviewer-fast, pre-commit, and autorun catalogs;
- create baseline, work order, and completion review evidence.

Forbidden SKSOT-T1 scope:

- setting any package to `ACTIVE`;
- modifying package lifecycle state;
- loading package instruction bodies as task guidance;
- implementing automatic resolver activation;
- implementing or claiming external CLI/MCP adapters;
- calling providers or asserting live governance behavior;
- public-sync or production-readiness claims.

## Findings / Position

The ASSF registry and runtime audit already identify six runtime-eligible
package roots. SKSOT-T1 does not change that eligibility. It creates a truth
packet for each eligible package so future agents can inspect which evidence,
obligations, and verification results back the package before scaling skill
governance further.

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
| Generated ASSF skill index is a derived read model | `docs/reference/agent_system_skills/registry/README.md` | Purpose; Adding A New Entry | `generated/skill-index.json` | ASSF registry source family | LITERAL_INVARIANT | ACCEPT |
| ASSF package lifecycle fields include status, UAT, certification, and internal/external dispositions | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema; Internal-Agent And External-Agent CLI/MCP Disposition Fields | `status`; `uatState`; `certificationState`; `internalAgentDisposition`; `externalCliMcpDisposition` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Runtime eligibility requires certified, UAT-passed, implemented internal disposition, and package root existence | `governance/compat/run_assf_runtime_package_loader.py` | `_runtime_ineligibility_reasons` | `certificationState`; `uatState`; `internalAgentDisposition`; `canonicalRoot` | AGSK-R4 runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Runtime eligibility audit reports six ready package roots before SKSOT-T1 | `governance/compat/run_assf_runtime_eligibility_audit.py` | `build_runtime_eligibility_audit` | `ready_for_body_load` | AGSK-R5 audit helper | RUNTIME_BEHAVIOR | ACCEPT |
| Provider-local files and memories are not source authority | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Provider Adapter Boundary | provider-local files and memories | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Truth packet checker is new in this tranche | `governance/compat/check_skill_truth_packets.py` | SKSOT-T1 new file | `check` | SKSOT-T1 checker | DOC_ONLY_NEW | ACCEPT |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one read-only skill truth packet
checker, its focused test, and the minimal hook-catalog entries needed to run
that checker in governed local workflows.

Protected paths (every changed guard/control path is listed):

- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/check_skill_truth_packets.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/test_check_skill_truth_packets.py`

Operator authorization: the operator instructed Codex to proceed building the
skill source-of-truth control mechanism after reviewing the Truth Kernel
reference input and agreeing to the skill control-plane direction.

Rollback boundary: if SKSOT-T1 is rejected, remove only the new checker, test,
hook-catalog entries, skill truth packet standard, truth packet layout, packet
sources, generated truth index, and SKSOT-T1 artifacts. Do not revert prior
AGSK package promotion, ASSF registry entries, package roots, or session-sync
commits.

Scope boundary: this authorization does not extend to unrelated guard behavior,
package lifecycle state, package bodies, resolver activation, external
adapters, provider/live proof, public-sync, or production runtime.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASSF registry README, ASSF package contract, runtime package loader, runtime eligibility audit, six registry entries, six package roots |
| Runtime behavior claimed | read-only truth packet verification and generated-index drift checking |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - source supports truth packet foundation, not activation |

## Evidence / Verification

| Evidence | Required or observed result |
|---|---|
| Packet sources | six runtime-eligible package truth packets |
| Generated truth index | derived from packet source fields |
| Checker | validates packet schema, evidence references, obligations, registry lifecycle match, and index drift |
| Unit tests | valid packet, provenance, strict evidence, hard obligation, index drift, registry mismatch |
| Provider/live proof | NOT_RUN_WITH_REASON: no live provider behavior is claimed |

## Artifact Manifest

| Artifact | Status |
|---|---|
| `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | CREATED |
| `docs/reference/agent_system_skills/truth/README.md` | CREATED |
| `docs/reference/agent_system_skills/truth/packets/*.json` | CREATED |
| `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` | CREATED |
| `governance/compat/check_skill_truth_packets.py` | CREATED |
| `governance/compat/test_check_skill_truth_packets.py` | CREATED |
| governance hook catalogs | UPDATED |
| SKSOT-T1 work order and completion review | CREATED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | skill truth packets and generated truth index | read-only truth inspection for six package roots; no activation or action authority | packet checker and tests | no external adapter | `IMPLEMENTED_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter only | no external mutation, activation, provider call, public-sync, commit, or push | claim boundary | separate adapter contract required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Legacy source family |
| Chain map route | external/private reference input -> CVF-governed reference standard -> packet checker and source records |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | SKSOT-T1 baseline, work order, completion review, standard, packets, generated truth index, checker, and tests |
| Disposition | absorb useful source-of-truth patterns into CVF-owned skill governance without treating private reference input as canonical authority |
| Claim boundary | no external source or provider-local memory is promoted as CVF authority in SKSOT-T1 |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Skill truth packet standard exists with source boundary and packet fields | standard created |
| AC2 | Six runtime-eligible packages have packet records | packet folder contains six JSON files |
| AC3 | Generated truth index matches packet sources | checker PASS |
| AC4 | Checker validates schema, references, lifecycle match, strict obligations, and index drift | unit tests PASS |
| AC5 | Checker is wired into governance catalogs | catalog diff PASS |
| AC6 | No ACTIVE, provider, external adapter, public-sync, or production claim is made | claim boundary PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_SKSOT_T1_SKILL_TRUTH_PACKET_FOUNDATION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SKSOT_T1_SKILL_TRUTH_PACKET_FOUNDATION_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: operator-directed skill control-plane foundation, not a roadmap status edit | N/A with reason | PASS |
| Registry JSON | N/A with reason: SKSOT-T1 does not mutate ASSF registry lifecycle sources | N/A with reason | PASS |
| Registry Markdown | skill truth standard and README | created | PASS |
| External evidence digest | N/A with reason: private reference input is not promoted as canonical evidence | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no system-loop runtime change | N/A with reason | PASS |
| Session continuity | session-sync may follow material closure | N/A with reason | PASS |
| Focused tests | new unit tests and checker | PASS after execution | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Packet count | `6` | `6` | PASS |
| Runtime eligibility claim | existing six runtime-eligible package roots only | six packet records match existing eligible roots | PASS |
| Checker status | PASS | `check_skill_truth_packets.py --base 291788b6 --head HEAD --enforce` PASS | PASS |
| Unit test status | PASS | `python -m unittest governance.compat.test_check_skill_truth_packets` PASS | PASS |
| Provider/live claim | none | NOT_RUN_WITH_REASON | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline references private ASSF provenance and internal governed
skill records. Public-safe export requires separate redaction and public-sync
authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | SKSOT-T1 skill truth packet foundation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - six packet records and checker implemented |
| receiptEvidence | CVF_RECEIPT_PRESENT - packet checker, unit tests, and governance gates |
| actionEvidence | ACTION_EVIDENCE_PRESENT - standard, packet sources, generated index, checker, tests, and catalogs changed |
| invocationBoundary | local Python checker and governed JSON/Markdown sources only |
| interceptionBoundary | no IDE, shell hook, git hook, provider, CLI/MCP, Web, public-sync, or external runtime interception claim |
| claimLanguage | creates source-of-truth packet control for existing runtime-eligible package roots |
| forbiddenExpansion | no ACTIVE resolver, automatic invocation, external adapter, provider/live proof, public-sync, commit authority, or production-readiness claim |

## Claim Boundary

SKSOT-T1 creates the first CVF skill truth packet control layer for the six
existing runtime-eligible ASSF package roots. It does not change skill package
lifecycle state, activate package use, grant authority, expose adapters, call
providers, public-sync, or claim production readiness.
