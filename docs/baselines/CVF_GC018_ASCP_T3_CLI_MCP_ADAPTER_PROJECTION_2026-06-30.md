# CVF GC-018 Baseline: ASCP-T3 CLI/MCP Adapter Projection

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: baseline

Batch ID: ASCP-T3

dispatchBaseHead: fe2f6205

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | add a bounded external CLI/MCP adapter projection readout |
| Baseline | ASCP-T2 activation policy semantics are closed; external consumers still need a safe metadata/policy view |
| Proposed tranche | projection standard, helper, focused tests, roadmap update, work order, and completion evidence |
| Execution route | Codex direct implementation with reviewer-owned closure |
| Closure posture | CLOSED_PASS_BOUNDED after focused tests and local projection smoke |

## Purpose

ASCP-T3 implements the first bounded external projection surface for ASSF. The
projection exposes allowlisted package metadata and activation policy state to
`EXTERNAL_AGENT_CLI_MCP` while denying external package body reads, output use,
provider calls, lifecycle mutation, and public claims.

## Scope / Methodology

Allowed ASCP-T3 scope:

- add `docs/reference/agent_system_skills/CVF_ASSF_CLI_MCP_ADAPTER_PROJECTION_STANDARD.md`;
- add `governance/compat/run_assf_cli_mcp_adapter_projection.py`;
- add `governance/compat/test_run_assf_cli_mcp_adapter_projection.py`;
- update the ASCP roadmap row from T3 ready to T3 closed and T4 ready;
- file baseline, work order, and completion evidence.

Forbidden ASCP-T3 scope:

- package lifecycle mutation to `ACTIVE`;
- package instruction body reads;
- emitting or consuming skill usage receipts;
- provider calls or live governance proof;
- MCP server runtime, daemon, hook, or IDE bridge behavior;
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
| ASCP roadmap requires T3 CLI/MCP adapter projection after T2 closure | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | Work Plan | `ASCP-T3` | ASCP roadmap | VALUE_SET | ACCEPT |
| External metadata readout allowlist defines permitted metadata fields | `governance/compat/run_assf_external_agent_metadata_readout.py` | `ALLOWED_SKILL_FIELDS` | `ALLOWED_SKILL_FIELDS` | external metadata readout helper | RUNTIME_BEHAVIOR | ACCEPT |
| External adapter execution remains bounded by the boundary contract | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | Adapter Admission Boundary | `EXTERNAL_AGENT_CLI_MCP` | external readout boundary contract | LITERAL_INVARIANT | ACCEPT |
| Activation policy resolver classifies readiness without body reads | `governance/compat/run_assf_activation_policy_resolver.py` | `build_activation_policy_packet` | `body_read_requested` | activation policy resolver | RUNTIME_BEHAVIOR | ACCEPT |
| CLI/MCP projection helper is new in ASCP-T3 | `governance/compat/run_assf_cli_mcp_adapter_projection.py` | ASCP-T3 new file | `build_cli_mcp_adapter_projection` | CLI/MCP adapter projection helper | DOC_ONLY_NEW | ACCEPT |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one bounded CLI/MCP projection helper
and focused tests under `governance/compat`.

Protected paths:

- `governance/compat/run_assf_cli_mcp_adapter_projection.py`
- `governance/compat/test_run_assf_cli_mcp_adapter_projection.py`

Operator authorization: active next move authorizes ASCP-T3 CLI/MCP adapter
projection after ASCP-T2 closure.

Rollback boundary: if ASCP-T3 is rejected, remove only the projection helper,
its tests, the projection standard, ASCP-T3 artifacts, and the ASCP roadmap row
update. Do not revert ASCP-T1, ASCP-T2, SKUSE-T1, truth packets, or package
promotion commits.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASCP roadmap, external readout helper, activation policy resolver, external adapter boundary, generated skill index, truth index |
| Runtime behavior claimed | local external metadata/policy projection only |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - current sources support bounded projection, not execution adapter behavior |

## Evidence / Verification

| Evidence | Required or observed result |
|---|---|
| Focused unit tests | `python -m unittest governance.compat.test_run_assf_cli_mcp_adapter_projection` PASS, 6 tests |
| Projection smoke | `python governance/compat/run_assf_cli_mcp_adapter_projection.py --skill-id cvf-engineering-spec-driven-development --json` returned `ACTIVATION_READY` with external body/read output denied |
| Provider/live proof | NOT_RUN_WITH_REASON: no live provider behavior is claimed |

## Artifact Manifest

| Artifact | Status |
|---|---|
| `docs/reference/agent_system_skills/CVF_ASSF_CLI_MCP_ADAPTER_PROJECTION_STANDARD.md` | CREATED |
| `governance/compat/run_assf_cli_mcp_adapter_projection.py` | CREATED |
| `governance/compat/test_run_assf_cli_mcp_adapter_projection.py` | CREATED |
| `docs/baselines/CVF_GC018_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_2026-06-30.md` | CREATED |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_2026-06-30.md` | CREATED |
| `docs/reviews/CVF_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_COMPLETION_2026-06-30.md` | CREATED |
| `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | UPDATED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | activation policy helper | selected/ready/body-read/use classification only | ASCP-T2 tests and smokes | no external adapter | `IMPLEMENTED_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | CLI/MCP projection helper | metadata and policy-state readout only | ASCP-T3 tests and smoke | body reads and output use denied | `IMPLEMENTED_BOUNDED_PROJECTION` |
| `EXTERNAL_AGENT_CLI_MCP` | package execution adapter | no package body read or output use authorized | N/A with reason: execution adapter not implemented | separate adapter/runtime work order required | `DEFERRED_WITH_REASON` |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Projection emits allowlisted metadata families | unit tests PASS |
| AC2 | Projection emits activation policy state for selected package rows | unit tests and smoke PASS |
| AC3 | Projection denies external package body reads and output use | unit tests and smoke PASS |
| AC4 | Projection does not emit body, loader command, truth, resolver receipt, policy receipt, or skill usage receipt fields | unit tests PASS |
| AC5 | ASCP-T4 becomes ready only after ASCP-T3 closure | roadmap update PASS |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| CVF skill id | N/A with reason: ASCP-T3 did not consume package instruction output as work evidence |
| Package root | N/A with reason: no package body was read by ASCP-T3 projection helper |
| Invocation context | ASCP-T3 projection tests and smoke |
| Receipt evidence | N/A with reason: no loader usage receipt output was consumed as evidence |
| Output consumed by CVF | local metadata/policy projection output only |
| Truth packet or source path | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Authority boundary | projection output does not grant authority, activate packages, or bypass work-order scope |

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
| Owner surface | ASCP-T3 baseline, work order, completion review, projection standard, helper, tests, and roadmap |
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
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | `Status: ACTIVE_ROADMAP` | PASS |
| Registry JSON | N/A with reason: no registry mutation authorized or performed | N/A with reason | PASS |
| Registry Markdown | N/A with reason: no registry markdown mutation | N/A with reason | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no provider route, execution adapter, or package execution changed | N/A with reason | PASS |
| Session continuity | session-sync may follow material closure | N/A with reason | PASS |
| Focused tests | projection tests | PASS | PASS |
| Runtime smoke | projection smoke | PASS | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Projection implementation | `IMPLEMENTED_BOUNDED_PROJECTION` | helper emits projection implementation token | PASS |
| External consumer | `EXTERNAL_AGENT_CLI_MCP` | helper emits external consumer token | PASS |
| Body-read disposition | `DENIED_EXTERNAL_BODY_READ_NOT_IMPLEMENTED` | unit tests and smoke observed denial | PASS |
| Output-use disposition | `DENIED_EXTERNAL_OUTPUT_USE_NOT_IMPLEMENTED` | unit tests observed denial | PASS |
| Unit test status | PASS | `python -m unittest governance.compat.test_run_assf_cli_mcp_adapter_projection` PASS | PASS |
| Provider/live claim | none | NOT_RUN_WITH_REASON | PASS |

## Claim Boundary

ASCP-T3 implements a bounded external metadata/policy projection only. It does
not activate skills, mutate package lifecycle state, read package instruction
bodies, emit or consume skill usage receipts, implement execution adapters,
call providers, public-sync, or grant action authority.
