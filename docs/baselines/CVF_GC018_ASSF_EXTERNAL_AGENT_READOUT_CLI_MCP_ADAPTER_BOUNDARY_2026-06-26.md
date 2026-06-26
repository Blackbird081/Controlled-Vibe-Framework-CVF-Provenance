# CVF GC-018 ASSF External Agent Readout / CLI-MCP Adapter Boundary

Status: CLOSED_PASS_BOUNDED

Memory class: FULL_RECORD

Date: 2026-06-26

Baseline ID: GC-018-ASSF-EAR-CLI-MCP-T0-T4

## Purpose

Authorize a bounded decision-first documentation tranche for ASSF external-agent
readout and future CLI/MCP adapter boundaries.

## Decision / Baseline / Proposed Tranche

Decision: close a documentation-only T0-T4 boundary tranche now, and require a
fresh GC-018/work order before any adapter or runtime implementation.

Baseline: existing ASSF package, generated-index, Web projection, and
dual-agent standards already define enough authority to write a boundary
contract, but not enough authority to implement adapter behavior.

Proposed tranche: roadmap, GC-018 baseline, reference contract, and completion
review only.

## Scope

Allowed material paths:

- `docs/roadmaps/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_ROADMAP_2026-06-26.md`
- `docs/baselines/CVF_GC018_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_2026-06-26.md`
- `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md`
- `docs/reviews/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_COMPLETION_2026-06-26.md`

Forbidden material scope:

- adapter implementation;
- package instance creation;
- certification decision or lifecycle mutation;
- ASSF registry-source or generated-index source mutation;
- resolver mutation;
- provider/live proof;
- public-sync or push;
- package activation, package instruction execution, or package integration;
- session-sync in the material commit.

## Evidence / Verification

| Evidence | Source | Disposition |
|---|---|---|
| external adapter fields exist | ASSF package contract | PASS |
| Web projection is not adapter authority | Web projection contract | PASS |
| generated index denies runtime/adapter authorization | generated skill index claim boundary | PASS |
| checker requires adapter evidence before IMPLEMENTED | certified metadata admission checker | PASS |

## Current Runtime Freshness Verification

| Runtime claim | Verification command or source | Observed value | Disposition |
|---|---|---|---|
| No adapter implementation is authorized | this baseline scope | allowed paths are documentation-only | PASS |
| Generated index remains metadata-only | `docs/reference/agent_system_skills/generated/skill-index.json` | claim boundary denies adapter authorization | PASS |
| IMPLEMENTED adapter posture requires evidence | `governance/compat/check_assf_certified_metadata_admission.py` | checker validates `adapterEvidence` for IMPLEMENTED | PASS |

## Source Inventory

| File | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V23_2026-06-26.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | SOURCE_VERIFIED |
| `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | SOURCE_VERIFIED |
| `docs/reference/agent_system_skills/generated/skill-index.json` | SOURCE_VERIFIED |
| `governance/compat/check_assf_certified_metadata_admission.py` | SOURCE_VERIFIED |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | SOURCE_VERIFIED |
| `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | SOURCE_VERIFIED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| External adapter disposition fields are canonical ASSF package fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | lines 75 and 138-141 | `externalCliMcpDisposition` | ASSF package contract | EXISTS | ACCEPT |
| Adapter behavior needs separate authorization | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Provider Adapter Boundary | `adapterEvidence` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Web projection is not an external adapter | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | Adapter-Separation Invariant | `EXTERNAL_AGENT_CLI_MCP` | Web projection contract | LITERAL_INVARIANT | ACCEPT |
| Generated index is metadata-only | `docs/reference/agent_system_skills/generated/skill-index.json` | root `claimBoundary` | `claimBoundary` | generated ASSF skill index | LITERAL_INVARIANT | ACCEPT |
| IMPLEMENTED external adapter requires evidence | `governance/compat/check_assf_certified_metadata_admission.py` | lines 145-157 | `adapterEvidence` | certified metadata admission checker | RUNTIME_BEHAVIOR | ACCEPT |
| Web Skill type has display-only adapter fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | lines 34-40 | `adapterContract` | Web Skill type | EXISTS | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001
- ADIF-0002
- ADIF-0007
- ADIF-0006

Remediation applied:

- No exhaustive directory claim is made.
- Provider-local memory is not used as source authority.
- Source Verification symbol cells contain bare symbols only.
- Boundary prose avoids using machine-trigger phrases as proof.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | GC-018 baseline and boundary contract | Planning/readout contract authority only; no execution authority | source verification table | N/A with reason: no internal adapter is implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | Future adapter/readout owner to be named by a later work order | no external mutation, certification, activation, execution, or public claim | ASSF package contract and dual-agent standard | deferred; separate GC-018/work order/test/review required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator approved the next ASSF external-agent readout / CLI-MCP adapter boundary lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline |
| Disposition | no external artifact absorbed; operator direction used as lane authorization only |
| Claim boundary | repo-local governed sources remain source authority |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | GC-018 baseline for ASSF external-agent readout and CLI/MCP adapter boundary |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no runtime/provider/adapter receipt exists |
| actionEvidence | ACTION_EVIDENCE_PRESENT: Source Inventory and Source Verification Block |
| invocationBoundary | governed local repository documentation only |
| interceptionBoundary | no provider, CLI, MCP, Web runtime, package execution, public-sync, or adapter interception claim |
| claimLanguage | authorizes contract/readiness decision artifacts only |
| forbiddenExpansion | no adapter implementation, package instance, certification decision, lifecycle mutation, ASSF registry-source mutation, generated-index source mutation, resolver mutation, provider/live proof, public-sync, push, activation, package instruction execution, or package integration |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: no delegated worker work order in this decision tranche | no work order created | N/A with reason |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_COMPLETION_2026-06-26.md` | completion review status `CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_ROADMAP_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason: no registry mutation authorized or required | no registry path in changed set | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown mutation authorized or required | no registry Markdown path in changed set | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence artifact absorbed | repo-local source evidence only | N/A with reason |
| System loop interlock | N/A with reason: no runtime loop, provider route, adapter, or package execution changed | documentation-only tranche | N/A with reason |
| Session continuity | N/A with reason: material closure first; session-sync must be separate | no session path in material changed set | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Acceptance criterion | Receipt evidence | Disposition |
|---|---|---|
| AC1 Allowed scope is documentation-only | Scope and Delta boundary | PASS |
| AC2 Source facts are verified | Source Verification Block | PASS |
| AC3 External adapter remains deferred | Dual Agent Surface Matrix | PASS |
| AC4 Completion review exists | completion review path | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | ASSF-EAR-CLI-MCP GC-018 baseline, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, Python, apply_patch, git |
| Target paths | baseline, roadmap, contract, completion review |
| Allowed scope source | active session next allowed move after commit `b46add61` |
| Before status evidence | HEAD `b46add61` and clean worktree |
| After status evidence | pending material closure changed set |
| Diff evidence | `git diff --name-status` before commit |
| Approval boundary | GC-018 decision baseline only |
| Claim boundary | no adapter/runtime/provider/package/public/session mutation |
| Agent type | single-agent multi-role closer |
| Invocation ID | GC018-ASSF-EAR-CLI-MCP-2026-06-26 |
| Expected manifest | `docs/roadmaps/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_ROADMAP_2026-06-26.md`; `docs/baselines/CVF_GC018_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_2026-06-26.md`; `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md`; `docs/reviews/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_COMPLETION_2026-06-26.md` |
| Actual changed set | `docs/roadmaps/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_ROADMAP_2026-06-26.md`; `docs/baselines/CVF_GC018_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_2026-06-26.md`; `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md`; `docs/reviews/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_COMPLETION_2026-06-26.md` |
| Manifest delta | MATCH |

## Claim Boundary

This baseline authorizes only the T0-T4 decision-first artifacts listed above.
It does not implement or expose external-agent adapter behavior.
