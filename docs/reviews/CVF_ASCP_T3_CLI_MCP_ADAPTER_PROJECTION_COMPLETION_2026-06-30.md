# CVF ASCP-T3 CLI/MCP Adapter Projection Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: completion_review

Batch ID: ASCP-T3

dispatchBaseHead: fe2f6205

executionBaseHead: fe2f6205

closureBaseHead: fe2f6205

## Purpose

Close ASCP-T3 after adding a bounded external CLI/MCP adapter projection that
exposes allowlisted ASSF metadata and activation policy state while denying
external package body reads and output use.

## Target / Source

| Field | Value |
|---|---|
| Target artifact | ASCP-T3 CLI/MCP adapter projection standard, helper, tests, and roadmap update |
| Source work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_2026-06-30.md` |
| Paired baseline | `docs/baselines/CVF_GC018_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_2026-06-30.md` |
| Roadmap source | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` |
| Review disposition | CLOSED_PASS_BOUNDED |

## Scope / Methodology

Changed material scope:

- CLI/MCP adapter projection standard;
- projection helper;
- focused tests;
- ASCP roadmap T3/T4 status update;
- GC-018 baseline, work order, and completion review.

Out of scope and not changed:

- ASSF registry lifecycle sources;
- ASSF package roots;
- provider route code;
- MCP server, daemon, hook, or IDE bridge behavior;
- public-sync files.

## Findings / Position

ASCP-T3 is closed bounded. The projection helper creates an
`EXTERNAL_AGENT_CLI_MCP` readout that:

- uses the external metadata readout allowlist;
- merges activation policy state from the ASCP-T2 resolver;
- emits `IMPLEMENTED_BOUNDED_PROJECTION`, not package execution authority;
- denies external package body reads with
  `DENIED_EXTERNAL_BODY_READ_NOT_IMPLEMENTED`;
- denies external output use with
  `DENIED_EXTERNAL_OUTPUT_USE_NOT_IMPLEMENTED`;
- does not emit package bodies, loader commands, truth objects, resolver
  receipts, policy receipts, matched usage receipt IDs, or skill usage
  receipts.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| Projection confused with package execution adapter | controlled by projection token, claim boundary, and denied external dispositions |
| Readiness confused with external body-read authority | controlled by `externalBodyReadDisposition` denial |
| Internal receipts leaked to external consumer | controlled by projection filter and focused tests |
| Lifecycle activation implied by projection | controlled by changed set and roadmap T4 dependency |

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
| Implement CLI/MCP adapter projection after T2 | work order Purpose; Mission | projection standard and helper | unit tests | PASS |
| Use external readout allowlist | Source Verification; Acceptance Criteria | allowlisted metadata fields | unit tests | PASS |
| Use resolver output without body reads | Evidence Requirements | `activationPolicyState` | smoke and unit tests | PASS |
| Keep lifecycle activation separate | Claim Boundary | no package or registry mutation | changed set review | PASS |

## Closure Diff Gate

| Requirement | Evidence | Disposition |
|---|---|---|
| Projection standard exists | `docs/reference/agent_system_skills/CVF_ASSF_CLI_MCP_ADAPTER_PROJECTION_STANDARD.md` | PASS |
| Projection helper exists | `governance/compat/run_assf_cli_mcp_adapter_projection.py` | PASS |
| Projection tests exist | `governance/compat/test_run_assf_cli_mcp_adapter_projection.py` | PASS |
| Helper does not open package bodies | source and tests | PASS |
| External body/read output remains denied | unit tests and smoke | PASS |
| No package lifecycle mutation | changed set excludes package roots and registry entries | PASS |

## Verification / Evidence

| Evidence | Observed result |
|---|---|
| `python -m unittest governance.compat.test_run_assf_cli_mcp_adapter_projection` | PASS, 6 tests |
| `python governance/compat/run_assf_cli_mcp_adapter_projection.py --skill-id cvf-engineering-spec-driven-development --json` | PASS, returned `ACTIVATION_READY` with external body/read output denied |
| Live provider proof | NOT_RUN_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |

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
| Owner surface | ASCP-T3 roadmap, baseline, work order, completion review, projection standard, helper, and tests |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local CVF source verification only |
| Claim boundary | no external source, provider output, or provider-local memory is promoted as CVF authority |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | ASCP-T3 CLI/MCP adapter projection on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | apply_patch; Python unittest; projection smoke |
| Target paths | projection standard, helper, tests, roadmap, baseline, work order, completion review |
| Allowed scope source | active next move plus ASCP-T3 baseline and work order |
| Before status evidence | base commit `fe2f6205`; clean worktree before ASCP-T3 edits |
| After status evidence | pending material closure changed set |
| Diff evidence | focused tests, projection smoke, and governance gates |
| Approval boundary | active next move authorized ASCP-T3; live API keys not needed because no live behavior claim is made |
| Claim boundary | bounded external metadata and policy readout only |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `cvf-ascp-t3-cli-mcp-adapter-projection-2026-06-30` |
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
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
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

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASCP-T3 CLI/MCP adapter projection |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - local external metadata/policy projection implemented |
| receiptEvidence | N/A with reason: no package usage receipts are emitted or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT - standard, helper, tests, roadmap update, baseline, work order, and completion review |
| invocationBoundary | local Python helper and governed repository sources only |
| interceptionBoundary | no IDE, shell hook, git hook, provider, MCP server, Web, public-sync, or external runtime interception claim |
| claimLanguage | projects allowlisted metadata and activation policy state to an external readout |
| forbiddenExpansion | no package body read, skill usage receipt emission or consumption, lifecycle mutation, automatic invocation, provider/live proof, public-sync, package execution adapter, commit authority expansion, or production-readiness claim |

## Claim Boundary

ASCP-T3 creates bounded external CLI/MCP adapter projection only. It does not
activate skills, mutate package lifecycle state, read package instruction
bodies, emit or consume skill usage receipts, implement package execution
adapters, call providers, public-sync, or grant action authority.
