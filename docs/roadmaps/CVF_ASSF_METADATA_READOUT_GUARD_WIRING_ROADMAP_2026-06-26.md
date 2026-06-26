# CVF ASSF Metadata Readout Guard Wiring Roadmap

Status: DISPATCH_READY

Memory class: FULL_RECORD

Date: 2026-06-26

Roadmap ID: ASSF-MRGW-T0-T4

## Purpose

Create a bounded guard lane for the ASSF external-agent metadata readout helper.
The prior implementation added the read-only helper and focused tests; this
roadmap authorizes a fresh GC-018/work order to make the allowlist and
no-adapter boundary machine-checked in normal governance gates.

## Authorization / Decision

Operator direction is to continue from the active next allowed move after ASSF
metadata readout closure. Decision: open a fresh source-verified guard-wiring
lane before any further adapter or package-facing work.

## Scope / Methodology

In scope:

- add a read-only checker for ASSF external-agent metadata readout output;
- add focused tests for allowed fields, claim-boundary language, and negative
  fixtures;
- wire the checker into autorun, pre-commit, and reviewer-fast command
  catalogs;
- close with worker return and completion review.

Out of scope:

- CLI/MCP adapter behavior implementation;
- Web runtime route or UI mutation;
- provider/live proof;
- package instance creation, activation, package instruction execution, or
  package integration;
- certification decision or lifecycle mutation;
- ASSF registry-source, generated-index source, or resolver mutation;
- public-sync, push, or session-sync in the material commit.

## Non-Goals

- No CLI/MCP adapter implementation.
- No Web runtime or API route implementation.
- No provider/live proof.
- No ASSF package state mutation.
- No public-sync or push.

## Design Control Gate

| Gate | Disposition |
|---|---|
| Decision-first before implementation | PASS |
| Source verification before guard wiring | PASS |
| Adapter behavior remains deferred | PASS |
| Runtime/provider/public/package execution blocked | PASS |

## Work Plan

| Step | Objective | Status |
|---|---|---|
| T0 | Source inventory and guard target decision | DISPATCH_READY |
| T1 | Implement metadata-readout guard | DISPATCH_READY |
| T2 | Add focused guard tests | DISPATCH_READY |
| T3 | Wire guard into standard command catalogs | DISPATCH_READY |
| T4 | Review, close, and sync next move separately | DISPATCH_READY |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Boundary contract defines external readout allowlist | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | line 26 | `Readout Field Allowlist` | ASSF external-agent boundary contract | VALUE_SET | ACCEPT |
| Boundary contract keeps adapter admission separate | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | line 47 | `Adapter Admission Boundary` | ASSF external-agent boundary contract | LITERAL_INVARIANT | ACCEPT |
| Current readout helper declares no adapter implementation | `governance/compat/run_assf_external_agent_metadata_readout.py` | line 37 | `ADAPTER_IMPLEMENTATION` | metadata readout helper | VALUE_SET | ACCEPT |
| Current readout helper declares allowlisted fields | `governance/compat/run_assf_external_agent_metadata_readout.py` | line 60 | `ALLOWED_SKILL_FIELDS` | metadata readout helper | VALUE_SET | ACCEPT |
| Current readout helper builds the metadata packet | `governance/compat/run_assf_external_agent_metadata_readout.py` | line 130 | `build_metadata_readout` | metadata readout helper | RUNTIME_BEHAVIOR | ACCEPT |
| Autorun catalog carries ASSF gate wiring pattern | `governance/compat/agent_autorun_command_catalog.py` | line 256 | `ASSF certified metadata admission` | autorun command catalog | EXISTS | ACCEPT |
| Pre-commit catalog carries ASSF gate wiring pattern | `governance/compat/local_governance_hook_catalog_pre_commit.py` | line 175 | `ASSF certified metadata admission` | pre-commit hook catalog | EXISTS | ACCEPT |
| Reviewer-fast catalog carries ASSF gate wiring pattern | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | line 120 | `ASSF certified metadata admission` | reviewer-fast hook catalog | EXISTS | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

API invocation used: `resolve_defect_packet(task_class="Work-order authoring / dispatch", role="dispatcher", lifecycle_phase="pre-dispatch")`

Returned defects:

- ADIF-0001
- ADIF-0002
- ADIF-0007
- ADIF-0006

Task-specific resolver query: taskClass=`checker implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Task-specific returned defects:

- N/A with reason: resolver returned no task-specific entries.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | metadata-readout guard and command catalogs | internal governance gates may verify readout shape and no-adapter boundary only | Source Verification Block and focused tests | no package activation or adapter behavior | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter/readout consumer | no external mutation, certification, activation, package execution, provider call, commit, push, or public claim | boundary contract and checker output | adapter remains deferred; this roadmap wires a guard only | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator approved continuation from the active ASSF next-move lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this roadmap |
| Disposition | no external artifact absorbed |
| Claim boundary | repository-local source and command evidence only |

## Acceptance Criteria

| Criterion | Evidence |
|---|---|
| AC1 | checker fails if readout emits any non-allowlisted skill field |
| AC2 | checker fails if adapter implementation is not `NOT_IMPLEMENTED` |
| AC3 | checker fails if claim-boundary language stops denying adapter behavior and package execution |
| AC4 | focused tests pass |
| AC5 | checker is present in autorun, pre-commit, and reviewer-fast catalogs |

## Verification / Evidence

| Verification | Evidence | Disposition |
|---|---|---|
| Base commit identified | `git rev-parse --short HEAD` returned `a9adf3cb` before dispatch authoring | PASS |
| Worktree checked before dispatch authoring | `git status --short` empty before dispatch authoring | PASS |
| ADIF dispatch query run | API resolver returned ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0006 | PASS |
| Task-specific ADIF query run | API resolver returned no checker-implementation entries | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance checker lane; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF metadata readout guard wiring roadmap |
| claimDisposition | N/A with reason: dispatch roadmap only; no implementation claim |
| receiptEvidence | N/A with reason: no runtime receipt is created by this roadmap |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source verification and planned guard scope |
| invocationBoundary | governed local dispatch authoring only |
| interceptionBoundary | no provider, CLI/MCP adapter, Web runtime, package execution, public-sync, or external interception claim |
| claimLanguage | guard wiring for read-only metadata readout shape |
| forbiddenExpansion | adapter behavior, package instance, certification decision, lifecycle mutation, registry/generated-index/resolver mutation, provider/live proof, public-sync, push, activation, package execution, and package integration remain out of scope |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local repository tools |
| Session or invocation | ASSF-MRGW-T0-T4 roadmap dispatch, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, Python source verification |
| Target paths | this roadmap, paired GC-018 baseline, paired work order |
| Allowed scope source | active next allowed move at HEAD `a9adf3cb` |
| Before status evidence | baseHead `a9adf3cb`; clean worktree |
| After status evidence | pre-dispatch gates before dispatch commit |
| Diff evidence | `git diff --name-status` against baseHead `a9adf3cb` |
| Approval boundary | dispatch packet only |
| Claim boundary | no implementation, adapter behavior, provider/live proof, public-sync, package execution, registry/generated-index/resolver mutation, lifecycle mutation, certification decision, or session-sync |
| Agent type | dispatcher |
| Invocation ID | ASSF-MRGW-T0-T4-dispatch-2026-06-26 |
| Expected manifest | roadmap, GC-018 baseline, and work order |
| Actual changed set | pending dispatch changed set |
| Manifest delta | N/A with reason: pending pre-dispatch validation |

## Claim Boundary

This roadmap authorizes only a paired source-verified guard-wiring work order.
It does not implement adapter behavior, expose external runtime behavior, run a
provider, mutate ASSF package state, public-sync, push, activate, or execute
package instruction bodies.
