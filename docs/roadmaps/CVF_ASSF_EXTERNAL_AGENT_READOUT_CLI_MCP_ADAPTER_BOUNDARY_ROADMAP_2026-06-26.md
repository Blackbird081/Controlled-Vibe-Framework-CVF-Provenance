# CVF ASSF External Agent Readout / CLI-MCP Adapter Boundary Roadmap

Status: CLOSED_PASS_BOUNDED

Memory class: FULL_RECORD

Date: 2026-06-26

Roadmap ID: ASSF-EAR-CLI-MCP-T0-T4

## Purpose

Define the next ASSF value lane after Web projection closure: a decision-first
boundary for external-agent readout and future CLI/MCP adapter work. This
roadmap closes T0-T4 as a contract/readiness tranche only. It does not
implement an adapter, expose a runtime endpoint, run a provider, or execute any
package instruction body.

## Authorization / Decision

Operator authorized continuing from the active session next allowed move after
ASSF Web projection closure. Decision: close T0-T4 as a source-verified
roadmap/contract boundary tranche before any runtime or adapter work.

## Scope / Methodology

The tranche reads current ASSF package, generated-index, certified-admission,
Web projection, and dual-agent standards, then records a bounded contract for:

- external-agent readout field allowlist;
- future CLI/MCP adapter admission prerequisites;
- authority, mutation, provider, public-sync, and package-execution denials;
- closure evidence for leaving adapter behavior unimplemented.

## Non-Goals

- No CLI/MCP adapter implementation.
- No Web runtime route or API implementation.
- No provider/live proof.
- No package instance, activation, or instruction execution.
- No ASSF registry-source, generated-index source, or resolver mutation.
- No public-sync, push, or session-sync in the material range.

## Design Control Gate

| Gate | Disposition |
|---|---|
| Decision-first before implementation | PASS |
| Source verification before adapter claim | PASS |
| Separate external-agent boundary | PASS |
| Runtime/provider/public/package execution blocked | PASS |

## Work Plan

| Step | Work | Status |
|---|---|---|
| T0 | Source inventory and authority baseline | CLOSED |
| T1 | External-agent readout schema decision | CLOSED |
| T2 | CLI/MCP adapter boundary decision | CLOSED |
| T3 | Future implementation readiness criteria | CLOSED |
| T4 | Closure and next-move decision | CLOSED |

## T0-T4 Plan And Result

| Tranche | Objective | Result |
|---|---|---|
| T0 | Source inventory and authority baseline | CLOSED: source inventory recorded in GC-018 baseline and completion review |
| T1 | External-agent readout schema decision | CLOSED: contract defines metadata-only allowlist and denied fields |
| T2 | CLI/MCP adapter boundary decision | CLOSED: adapter remains `DEFERRED_WITH_REASON` until separate work order |
| T3 | Future implementation readiness criteria | CLOSED: contract lists minimum prerequisites for any adapter tranche |
| T4 | Closure and next-move decision | CLOSED: recommend future adapter-readout implementation only after fresh GC-018/work order |

## Acceptance Criteria

| Criterion | Evidence | Disposition |
|---|---|---|
| Roadmap closes T0-T4 bounded | T0-T4 Plan And Result | PASS |
| Contract defines readout allowlist | boundary contract | PASS |
| Adapter remains deferred | Dual Agent Surface Matrix | PASS |
| Runtime/public/provider/package execution excluded | Non-Goals and Delta boundary | PASS |

## Verification / Evidence

| Verification | Evidence | Disposition |
|---|---|---|
| Source facts verified | Source Verification Block | PASS |
| ASSF generated index still metadata-only | generated index claim boundary | PASS |
| Adapter implementation not claimed | Machine Closure Package and Delta boundary | PASS |

## Current Runtime Freshness Verification

| Runtime claim | Verification command or source | Observed value | Disposition |
|---|---|---|---|
| No adapter implementation is part of this roadmap | changed-set boundary | no runtime path in expected manifest | PASS |
| ASSF generated index remains metadata-only | `docs/reference/agent_system_skills/generated/skill-index.json` | claim boundary denies adapter authorization | PASS |
| Certified-admission checker still requires adapter evidence before IMPLEMENTED | `governance/compat/check_assf_certified_metadata_admission.py` | `adapterEvidence` checked for IMPLEMENTED posture | PASS |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF package schema has external adapter disposition fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | lines 75 and 138-141 | `externalCliMcpDisposition` | ASSF package contract | EXISTS | ACCEPT |
| Adapter behavior requires a separate GC-018/work order/tests/review | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Provider Adapter Boundary | `adapterEvidence` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Web projection contract separates external adapter from Web display | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | Principle 5 and Adapter-Separation Invariant | `EXTERNAL_AGENT_CLI_MCP` | ASSF Web projection contract | LITERAL_INVARIANT | ACCEPT |
| Generated ASSF index is metadata-only and not adapter authorization | `docs/reference/agent_system_skills/generated/skill-index.json` | root `claimBoundary` | `claimBoundary` | generated ASSF skill index | LITERAL_INVARIANT | ACCEPT |
| Certified-admission checker requires adapter evidence before IMPLEMENTED claim | `governance/compat/check_assf_certified_metadata_admission.py` | lines 145-157 | `adapterEvidence` | certified metadata admission checker | RUNTIME_BEHAVIOR | ACCEPT |
| Web type already carries display-only adapter fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | lines 34-40 | `adapterContract` | Web Skill type | EXISTS | ACCEPT |
| Dual-agent standard requires explicit external CLI/MCP row | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Mandatory Dual Agent Surface Matrix | `EXTERNAL_AGENT_CLI_MCP` | dual-agent standard | VALUE_SET | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001
- ADIF-0002
- ADIF-0007
- ADIF-0006

Additional contract/review queries:

- taskClass=`Contract authoring`, role=`dispatcher`, lifecyclePhase=`pre-closure` returned ADIF-0011.
- taskClass=`Completion review authoring`, role=`reviewer`, lifecyclePhase=`pre-closure` returned ADIF-0009, ADIF-0010, and ADIF-0011.

Remediation:

- Avoid exhaustive directory claims.
- Use only CVF-governed source authority.
- Keep Source Verification symbol cells as bare fields or symbols.
- Keep governed markdown ASCII-only.
- Use canonical External Knowledge Intake Routing enum rows in closure.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | Internal agents may use the contract as planning authority only; no execution or adapter authority is granted | ASSF package contract, Web projection contract, generated index claim boundary | N/A with reason: internal documentation only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | Future adapter/readout surface, not implemented in this roadmap | External consumers may not mutate, certify, activate, execute, or publicize packages through this decision packet | dual-agent standard and ASSF adapter fields | deferred adapter owner; separate source-verified GC-018/work order required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator approved the next ASSF external-agent readout / CLI-MCP adapter boundary lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this roadmap |
| Disposition | no external artifact absorbed; operator direction used as lane authorization only |
| Claim boundary | repo-local governed sources remain source authority |

## Closure Diff Gate

| Requirement | Evidence | Disposition |
|---|---|---|
| T0 source inventory exists | GC-018 baseline and completion review Source Inventory | PASS |
| T1 readout schema decision exists | boundary contract Readout Field Allowlist | PASS |
| T2 adapter boundary decision exists | boundary contract Adapter Admission Boundary | PASS |
| T3 implementation readiness criteria exists | boundary contract Future Adapter Prerequisites | PASS |
| T4 closure decision exists | completion review and this roadmap status | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance architecture decision; no public-sync or push is
authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF external-agent readout and CLI/MCP adapter boundary roadmap T0-T4 |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no runtime/provider/adapter receipt exists |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source verification, boundary contract, and completion review |
| invocationBoundary | governed local repository documentation only |
| interceptionBoundary | no provider, CLI, MCP, Web runtime, package execution, public-sync, or adapter interception claim |
| claimLanguage | decision-first boundary for future external readout and adapter admission |
| forbiddenExpansion | no adapter implementation, package instance, certification decision, lifecycle mutation, ASSF registry-source mutation, generated-index source mutation, resolver mutation, provider/live proof, public-sync, push, activation, package instruction execution, or package integration |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: self-contained roadmap/contract tranche, no delegated worker | no work order created | N/A with reason |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_COMPLETION_2026-06-26.md` | completion review status `CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | this roadmap | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason: no registry mutation authorized or required | no registry path in changed set | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown mutation authorized or required | no registry Markdown path in changed set | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence artifact absorbed | source evidence is repo-local | N/A with reason |
| System loop interlock | N/A with reason: no runtime loop, provider route, adapter, or package execution changed | documentation-only tranche | N/A with reason |
| Session continuity | N/A with reason: material closure first; session-sync must be a separate commit | no session path in material changed set | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Acceptance criterion | Receipt evidence | Disposition |
|---|---|---|
| AC1 T0-T4 roadmap closed bounded | this roadmap status and completion review | PASS |
| AC2 Contract created for external readout and adapter boundary | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | PASS |
| AC3 Adapter implementation remains deferred | Dual Agent Surface Matrix and Delta boundary | PASS |
| AC4 Source facts are repo-verified | Source Verification Block | PASS |
| AC5 No public/provider/runtime/package execution claim | Public Export and Delta boundary | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | ASSF-EAR-CLI-MCP-T0-T4 roadmap closure, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, Python, apply_patch, git |
| Target paths | roadmap, GC-018 baseline, boundary contract, completion review |
| Allowed scope source | active session next allowed move after commit `b46add61` |
| Before status evidence | HEAD `b46add61` and clean worktree |
| After status evidence | pending material closure changed set |
| Diff evidence | `git diff --name-status` before commit |
| Approval boundary | decision-first roadmap/contract only |
| Claim boundary | no adapter/runtime/provider/package/public/session mutation |
| Agent type | single-agent multi-role closer |
| Invocation ID | ASSF-EAR-CLI-MCP-T0-T4-2026-06-26 |
| Expected manifest | `docs/roadmaps/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_ROADMAP_2026-06-26.md`; `docs/baselines/CVF_GC018_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_2026-06-26.md`; `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md`; `docs/reviews/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_COMPLETION_2026-06-26.md` |
| Actual changed set | `docs/roadmaps/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_ROADMAP_2026-06-26.md`; `docs/baselines/CVF_GC018_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_2026-06-26.md`; `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md`; `docs/reviews/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_COMPLETION_2026-06-26.md` |
| Manifest delta | MATCH |

## Claim Boundary

This roadmap closes a decision-first boundary tranche only. It does not create
or execute an adapter, package instance, provider call, public-sync, lifecycle
mutation, resolver mutation, or generated-index source mutation.
