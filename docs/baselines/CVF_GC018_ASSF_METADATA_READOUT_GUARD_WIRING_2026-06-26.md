# CVF GC-018 Baseline: ASSF Metadata Readout Guard Wiring

Memory class: FULL_RECORD
Status: DISPATCH_READY
Date: 2026-06-26
docType: baseline
Batch ID: ASSF-MRGW-T0-T4
dispatchBaseHead: a9adf3cb

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | dispatch a source-verified work order for metadata-readout guard wiring |
| Baseline | ASSF metadata readout implementation closed bounded at `1f93ea33` and session-sync at `a9adf3cb` |
| Proposed tranche | `ASSF-MRGW-T0-T4` |
| Worker route | Codex single-agent multi-role, no worker commit |
| Closure posture | `DISPATCH_READY` |

## Purpose

Authorize a bounded implementation work order that turns the ASSF
external-agent metadata readout boundary into a standard read-only checker.

## Scope / Methodology

The worker may create a checker and focused tests, then wire that checker into
the same command catalogs that already carry ASSF certified metadata admission.
The worker must not mutate ASSF registry sources, generated index sources,
resolver source, package roots, Web runtime, provider routes, public-sync, or
session state in the material commit.

## Dependency Release Evidence

| Dependency | Status | Evidence |
|---|---|---|
| Active next move requires fresh governed lane | SATISFIED | `CVF_SESSION_MEMORY.md` at sync commit `a9adf3cb` |
| Metadata readout helper exists | SATISFIED | `governance/compat/run_assf_external_agent_metadata_readout.py` |
| Boundary contract exists | SATISFIED | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` |
| Standard catalog pattern exists | SATISFIED | ASSF certified metadata admission is catalog-wired |

## Evidence / Verification

| Evidence | Result |
|---|---|
| `git rev-parse --short HEAD` | `a9adf3cb` before dispatch authoring |
| `git status --short` | clean worktree before dispatch authoring |
| ADIF resolver API call for work-order authoring/dispatcher/pre-dispatch | returned ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0006 |
| ADIF resolver API call for checker implementation/worker/pre-implementation | returned no task-specific entries |

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

## New Implementation Surfaces

| Path | Purpose | Boundary |
|---|---|---|
| `governance/compat/check_assf_external_agent_metadata_readout.py` | read-only guard for helper output | no mutation, provider, adapter, or package execution |
| `governance/compat/test_check_assf_external_agent_metadata_readout.py` | focused regression tests | local unittest only |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | metadata-readout guard and command catalogs | internal gates may verify readout shape only | Source Verification Block and focused tests | no package activation or adapter behavior | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter/readout consumer | no external mutation, certification, activation, package execution, provider call, commit, push, or public claim | boundary contract and checker output | adapter remains deferred; this tranche wires a guard only | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator approved continuation from the active ASSF next-move lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline |
| Disposition | no external artifact absorbed |
| Claim boundary | repository-local source and command evidence only |

## Planned Artifact Manifest

| Artifact | Purpose | Status |
|---|---|---|
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_METADATA_READOUT_GUARD_WIRING_FOR_CODEX_2026-06-26.md` | paired work order | PRESENT |
| `governance/compat/check_assf_external_agent_metadata_readout.py` | future checker | PLANNED |
| `governance/compat/test_check_assf_external_agent_metadata_readout.py` | future tests | PLANNED |
| `docs/reviews/CVF_ASSF_METADATA_READOUT_GUARD_WIRING_WORKER_RETURN_2026-06-26.md` | future worker return | PLANNED |
| `docs/reviews/CVF_ASSF_METADATA_READOUT_GUARD_WIRING_COMPLETION_2026-06-26.md` | future completion review | PLANNED |

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| AC1 | checker passes current helper output |
| AC2 | checker fails non-allowlisted readout fields |
| AC3 | checker fails adapter implementation claims other than `NOT_IMPLEMENTED` |
| AC4 | checker is wired into autorun, pre-commit, and reviewer-fast catalogs |
| AC5 | focused tests and governance gates pass |

## Fail Conditions

Return `BLOCKED_WITH_REASON` if the guard requires adapter behavior, provider
proof, package execution, ASSF registry/index/resolver mutation, Web runtime
mutation, public-sync, or session-sync in the material commit.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF metadata readout guard wiring dispatch baseline |
| claimDisposition | N/A with reason: dispatch authorization only; no implementation claim |
| receiptEvidence | N/A with reason: no runtime receipt is created by this baseline |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source verification and dependency release evidence |
| invocationBoundary | governed local dispatch packet authoring only |
| interceptionBoundary | no provider, adapter, package execution, external MCP, or interception claim |
| claimLanguage | implementation work order authoring only |
| forbiddenExpansion | adapter behavior, package instance, certification decision, lifecycle mutation, registry/generated-index/resolver mutation, provider/live proof, public-sync, push, activation, package execution, and package integration remain out of scope |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: bounded creation and wiring of an ASSF
metadata-readout checker under `governance/compat/`.

Protected paths:

- read-only startup source `CVF_SESSION_MEMORY.md`;
- create `governance/compat/check_assf_external_agent_metadata_readout.py`;
- create `governance/compat/test_check_assf_external_agent_metadata_readout.py`;
- update `governance/compat/agent_autorun_command_catalog.py`;
- update `governance/compat/local_governance_hook_catalog_pre_commit.py`;
- update `governance/compat/local_governance_hook_catalog_reviewer_fast.py`.
- read-only source `governance/compat/generate_assf_skill_index.py`;
- read-only source `governance/compat/run_assf_skill_resolver.py`.

Operator authorization: operator instructed Codex to continue from the active
next allowed move and add useful checklist/guard learning before moving to a
new tranche.

Rollback boundary: remove the new checker/tests and catalog entries; do not
revert prior ASSF metadata readout or session-sync commits.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local repository tools |
| Session or invocation | ASSF-MRGW-T0-T4 GC-018 dispatch, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, Python source verification |
| Target paths | this GC-018 baseline and paired work order |
| Allowed scope source | active next allowed move at HEAD `a9adf3cb` |
| Before status evidence | baseHead `a9adf3cb`; clean worktree |
| After status evidence | pre-dispatch gates before dispatch commit |
| Diff evidence | `git diff --name-status` against baseHead `a9adf3cb` |
| Approval boundary | dispatch packet only |
| Claim boundary | no implementation, adapter behavior, provider/live proof, public-sync, package execution, registry/generated-index/resolver mutation, lifecycle mutation, certification decision, or session-sync |
| Agent type | dispatcher |
| Invocation ID | ASSF-MRGW-T0-T4-GC018-dispatch-2026-06-26 |
| Expected manifest | roadmap, GC-018 baseline, and work order |
| Actual changed set | pending dispatch changed set |
| Manifest delta | N/A with reason: pending pre-dispatch validation |

## Claim Boundary

This baseline authorizes only dispatch of the paired guard-wiring work order.
It does not implement adapter behavior, run providers, public-sync, push,
activate packages, execute package instruction bodies, or mutate ASSF
registry/generated-index/resolver state.
