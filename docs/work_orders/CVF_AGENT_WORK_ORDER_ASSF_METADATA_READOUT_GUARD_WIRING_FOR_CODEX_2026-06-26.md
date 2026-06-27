# CVF Agent Work Order: ASSF Metadata Readout Guard Wiring

Memory class: FULL_RECORD
Status: CLOSED_PASS_BOUNDED
Date: 2026-06-26
docType: work_order
Batch ID: ASSF-MRGW-T0-T4
dispatchBaseHead: a9adf3cb
executionBaseHead: a9adf3cb
closureBaseHead: a9adf3cb
Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role worker/reviewer/closer for bounded ASSF
metadata-readout guard wiring.

executionBaseHead: `a9adf3cb`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Current-time notes: active handoff is `AGENT_HANDOFF_V23_2026-06-26.md`;
current HEAD before dispatch authoring is `a9adf3cb`; this packet authorizes
dispatch only until committed and then worker execution under this work order.

Required first actions: read the paired GC-018 baseline, read all Required
First Reads, run pre-implementation gates, and stop before any forbidden
adapter, provider, package, public-sync, registry, generated-index, resolver,
lifecycle, certification, or session mutation.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_METADATA_READOUT_GUARD_WIRING_FOR_CODEX_2026-06-26.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ASSF_METADATA_READOUT_GUARD_WIRING_2026-06-26.md`

Do-not-misread notes: this implements a read-only checker and catalog wiring.
It is not CLI/MCP adapter behavior, provider proof, package activation,
package execution, certification, registry/index/resolver mutation, public-sync,
push, or session-sync.

Return contract: produce worker return and completion review. Return
`BLOCKED_WITH_REASON` if the checker cannot be implemented without forbidden
mutation or scope expansion.

## Purpose

Implement and wire a read-only checker that verifies the existing ASSF
external-agent metadata readout helper preserves its field allowlist and
no-adapter claim boundary.

## Scope / Target / Owner Boundary

Allowed material scope is limited to the new checker, focused tests, command
catalog wiring, worker return, completion review, and this work order status
conversion during closure. Session-sync must be a separate commit after
material closure.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Active front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V23_2026-06-26.md` | ACCEPT |
| Paired roadmap | `docs/roadmaps/CVF_ASSF_METADATA_READOUT_GUARD_WIRING_ROADMAP_2026-06-26.md` | ACCEPT |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_METADATA_READOUT_GUARD_WIRING_2026-06-26.md` | ACCEPT |
| Boundary contract | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | ACCEPT |
| Existing readout helper | `governance/compat/run_assf_external_agent_metadata_readout.py` | ACCEPT |

## Agent Roles

| Role | Owner |
|---|---|
| Operator | approves lane and future scope expansion |
| Dispatcher | Codex |
| Worker | Codex, no commit during worker execution |
| Reviewer | Codex after worker return |
| Closer | Codex after reviewer acceptance |
| Session-sync steward | Codex in a dedicated session-sync commit paired to the material commit |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | active next allowed move recorded at session-sync commit `a9adf3cb` |
| Scope classification | bounded read-only checker and catalog wiring |
| Intake role | Codex dispatches; Codex worker executes without commit |
| Reviewer role | Codex reviewer/closer validates worker return, gates, changed paths, and boundaries |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; single-agent multi-role with reviewer closure conversion |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `SINGLE_AGENT_MULTI_ROLE` |
| selected role route | Codex dispatch author to Codex no-commit worker to Codex reviewer/closer |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if implementation requires adapter behavior, provider/live proof, package execution, public-sync, push, registry/index/resolver mutation, lifecycle mutation, certification decision, or session-sync |

## Required First Reads

| Source | Action | Reason |
|---|---|---|
| `CVF_SESSION_MEMORY.md` | READ | active front door |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ | compact startup facts |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ | active state registry |
| `AGENT_HANDOFF_V23_2026-06-26.md` | READ | active handoff |
| `docs/reference/guard_orientation/README.md` | READ | guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ | literal-format checklist |
| `docs/baselines/CVF_GC018_ASSF_METADATA_READOUT_GUARD_WIRING_2026-06-26.md` | READ | paired baseline |
| `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | SOURCE_VERIFIED | readout boundary |
| `governance/compat/run_assf_external_agent_metadata_readout.py` | SOURCE_VERIFIED | helper under guard |
| `governance/compat/agent_autorun_command_catalog.py` | SOURCE_VERIFIED | autorun wiring surface |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | SOURCE_VERIFIED | pre-commit wiring surface |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | SOURCE_VERIFIED | reviewer-fast wiring surface |

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

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex dispatches, executes no-commit worker implementation, reviews, and closes if evidence supports closure |
| phase | DISPATCH_AUTHORING; IMPLEMENTATION; REVIEWER_CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=a9adf3cb`; `executionBaseHead=a9adf3cb`; closure base recorded in completion review |
| changedSetScope(phase) | dispatch packet first; later implementation/review paths only; session-sync separate |
| traceScope(phase, actor) | worker return and completion review record Agent Operation Trace Block |
| commitOwner(phase) | Codex reviewer/closer owns material commit once worker return passes gates |
| crossBatchIsolation | no package, adapter, provider, public-sync, registry/index/resolver, lifecycle, certification, or session mutation in worker material commit |
| Before status evidence | dispatchBaseHead `a9adf3cb`; clean worktree before dispatch authoring |
| nextMoveSurfaces | updated only in a separate session-sync commit paired to the accepted material commit |
| Closer designation | Codex reviewer/closer |

## Single-Agent Multi-Role Control Block

| Field | Control |
|---|---|
| Role separation ledger | dispatch packet, worker return, completion review, material commit, and session-sync are separate steps |
| Evidence basis | source verification, focused checker tests, catalog diff, pre-closure gates, commit steward preflight |
| Self-review boundary | Codex may review its own worker return only against this work order and machine gates |
| Gate sequence | pre-dispatch for packet, pre-implementation for worker start, reviewer-fast/pre-closure for closure, session-sync gates only in the dedicated session-sync phase |
| Escalation conditions | any required adapter behavior, provider/live proof, package execution, public-sync, registry/index/resolver mutation, lifecycle mutation, certification decision, or session-sync |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| workerReturnPath | `docs/reviews/CVF_ASSF_METADATA_READOUT_GUARD_WIRING_WORKER_RETURN_2026-06-26.md` |
| completionReviewPath | `docs/reviews/CVF_ASSF_METADATA_READOUT_GUARD_WIRING_COMPLETION_2026-06-26.md` |
| reviewerOwnedClosurePaths | worker return, completion review, implementation paths, and this work order status conversion |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` expected |
| closer | Codex |

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
| Owner surface | this work order |
| Disposition | no external artifact absorbed |
| Claim boundary | repository-local source and command evidence only |

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Work-order instruction | Expected closure evidence | Disposition |
|---|---|---|---|
| Implement readout guard | Required Outputs and Execution Plan | checker and tests | PASS |
| Preserve no-adapter boundary | Acceptance Criteria and Claim Boundary | checker PASS and completion review | PASS |
| Wire standard gates | Required Outputs | catalog diff and hook PASS | PASS |
| Keep session-sync separate | Scope / Target / Owner Boundary | material commit excludes session paths | PASS |

## Execution Plan

1. Run pre-implementation gates using `a9adf3cb` as base.
2. Add `check_assf_external_agent_metadata_readout.py` with a read-only `check`
   function and CLI.
3. Add focused unittest coverage for current PASS, disallowed item field,
   adapter implementation widening, and weak claim boundary.
4. Add the checker to autorun, pre-commit, and reviewer-fast catalogs.
5. Run focused tests, direct checker, ASSF drift/admission checks, worker-return
   fast gate, and diff hygiene.
6. Author worker return and completion review; reviewer/closer commits material
   only after gates pass.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_assf_skill_index_drift.py
python governance/compat/check_assf_certified_metadata_admission.py --require-certified
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base a9adf3cb --head HEAD
```

## Worker Return Packet Shape Contract

The worker return must include these sections or explicit `N/A with reason`
dispositions where applicable:

- `Status`
- `dispatchWorkOrder`
- `Purpose`
- `Source Inventory`
- `Scope / Methodology`
- `Findings / Position`
- `Risk / Corrective Action`
- `Decision / Recommendation`
- `Claim Boundary`
- `Source Verification Block`
- `Agent Operation Trace Block`
- `Delta Execution Claim Boundary Control Block`
- `Public Export Disposition`
- `External Knowledge Intake Routing`
- `Rescan Intelligence Hardening`
- `Corpus Completeness And Report Integrity`
- `Finding-To-Governance Learning Disposition`
- `Epistemic Process Block`
- `Machine Closure Package`
- `Acceptance Receipt Assertion Matrix`
- actual `executionBaseHead`
- actual `git status --short`
- actual changed set as path list
- `receiptEvidence: CVF_RECEIPT_PRESENT - ...`

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker must repair machine-check, source-inventory,
packet-shape, focused-test, catalog-wiring, and worker-return fast-gate defects
and rerun the required checks without asking the operator. Ask only if repair
requires forbidden scope or a separate governed batch.

## Required Outputs

| Output | Required path | Disposition |
|---|---|---|
| Readout guard | `governance/compat/check_assf_external_agent_metadata_readout.py` | CREATE |
| Focused tests | `governance/compat/test_check_assf_external_agent_metadata_readout.py` | CREATE |
| Autorun catalog wiring | `governance/compat/agent_autorun_command_catalog.py` | MODIFY |
| Pre-commit catalog wiring | `governance/compat/local_governance_hook_catalog_pre_commit.py` | MODIFY |
| Reviewer-fast catalog wiring | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | MODIFY |
| Worker return | `docs/reviews/CVF_ASSF_METADATA_READOUT_GUARD_WIRING_WORKER_RETURN_2026-06-26.md` | CREATE |
| Completion review | `docs/reviews/CVF_ASSF_METADATA_READOUT_GUARD_WIRING_COMPLETION_2026-06-26.md` | CREATE |

## Required Artifact Manifest

| Artifact | Required status | Evidence |
|---|---|---|
| `governance/compat/check_assf_external_agent_metadata_readout.py` | PRESENT | checker created in closure changed set |
| `governance/compat/test_check_assf_external_agent_metadata_readout.py` | PRESENT | focused tests created in closure changed set |
| `docs/reviews/CVF_ASSF_METADATA_READOUT_GUARD_WIRING_WORKER_RETURN_2026-06-26.md` | PRESENT | worker return status `COMPLETE_PENDING_REVIEW` |
| `docs/reviews/CVF_ASSF_METADATA_READOUT_GUARD_WIRING_COMPLETION_2026-06-26.md` | PRESENT | completion review status `CLOSED_PASS_BOUNDED` |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Dispatch-state evidence | Closure disposition |
|---|---|---|
| `CVF_SESSION/**` | session-sync is separate | unchanged in material closure |
| `CVF_SESSION_MEMORY.md` | read-only startup source only | unchanged in material closure |
| `AGENT_HANDOFF_*.md` | session-sync is separate | unchanged in material closure |
| `docs/reference/agent_system_skills/registry/entries/**` | forbidden by work order | unchanged in material closure |
| `docs/reference/agent_system_skills/generated/skill-index.json` | forbidden by work order | unchanged in material closure |
| `governance/compat/generate_assf_skill_index.py` | source-verified read only | unchanged in material closure |
| `governance/compat/run_assf_skill_resolver.py` | source-verified read only | unchanged in material closure |

## Write Ownership

Allowed paths:

- `governance/compat/check_assf_external_agent_metadata_readout.py`
- `governance/compat/test_check_assf_external_agent_metadata_readout.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `docs/reviews/CVF_ASSF_METADATA_READOUT_GUARD_WIRING_WORKER_RETURN_2026-06-26.md`
- `docs/reviews/CVF_ASSF_METADATA_READOUT_GUARD_WIRING_COMPLETION_2026-06-26.md`
- this work order status conversion during closure

Forbidden paths:

- `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, and `AGENT_HANDOFF_*.md` during material execution;
- `docs/reference/agent_system_skills/registry/entries/**`;
- `docs/reference/agent_system_skills/generated/skill-index.json`;
- `governance/compat/generate_assf_skill_index.py`;
- `governance/compat/run_assf_skill_resolver.py`;
- Web runtime/source paths;
- public-sync repository or push surfaces.

## Verification Commands

Required before worker return:

```powershell
python -m unittest governance.compat.test_check_assf_external_agent_metadata_readout
python governance/compat/check_assf_external_agent_metadata_readout.py --enforce
python governance/compat/check_assf_skill_index_drift.py
python governance/compat/check_assf_certified_metadata_admission.py --require-certified
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
```

Required before material closure commit:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base a9adf3cb --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base a9adf3cb --head HEAD --enforce
git diff --check
```

## Evidence Requirements

| Evidence item | Required form | Owner |
|---|---|---|
| Checker proof | direct checker PASS and focused unittest PASS | worker then reviewer |
| Negative fixture proof | tests for non-allowlisted fields, widened adapter claim, and weak boundary | worker then reviewer |
| Catalog wiring proof | diff and hook/autorun gates show checker command present | reviewer |
| No forbidden mutation proof | `git diff --name-status` excludes forbidden paths | reviewer |

## Current Runtime Freshness Verification

| Runtime claim | Verification command or source | Observed value | Disposition |
|---|---|---|---|
| Checker does not implement adapter behavior | `governance/compat/check_assf_external_agent_metadata_readout.py` | validates readout metadata only | PASS |
| Readout helper still marks adapter as not implemented | `python governance/compat/check_assf_external_agent_metadata_readout.py --enforce` | PASS | PASS |
| ASSF generated index remains metadata-only | `python governance/compat/check_assf_skill_index_drift.py` | PASS | PASS |

## Review Gate

Reviewer must reject closure unless all changed paths are inside Write
Ownership, focused tests pass, direct checker passes, catalog wiring is present,
worker-return fast gate passes, and the material changed set excludes forbidden
ASSF registry/index/resolver, Web runtime, package, public-sync, and session
paths.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only after all Required Outputs exist, focused
tests pass, direct checker passes, and worker-return fast gate is compliant.
Return `BLOCKED_WITH_REASON` if the work requires forbidden mutation or cannot
preserve the no-adapter boundary.

## Operator Checkpoint

Operator checkpoint is required before any expansion into CLI/MCP adapter
availability, provider/live proof, public-sync, package activation, package
execution, package instance creation, certification decision, lifecycle
mutation, ASSF registry/generated-index source mutation, or resolver mutation.

## Closure Checklist

| Item | Required disposition |
|---|---|
| Write Ownership respected | PASS |
| Direct checker passes | PASS |
| Focused tests pass | PASS |
| Catalog wiring complete | PASS |
| Worker return fast gate passes | PASS |
| Pre-closure gates pass | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_METADATA_READOUT_GUARD_WIRING_COMPLETION_2026-06-26.md` | completion review status `CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_METADATA_READOUT_GUARD_WIRING_ROADMAP_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason: no registry JSON mutation authorized or required | no registry path in changed set | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown mutation authorized or required | no registry Markdown path in changed set | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence artifact absorbed | local command evidence only | N/A with reason |
| System loop interlock | N/A with reason: no runtime loop, provider route, adapter, or package execution changed | checker-only tranche | N/A with reason |
| Session continuity | N/A with reason: material closure first; session-sync must be separate | no session path in material changed set | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Acceptance criterion | Receipt evidence | Disposition |
|---|---|---|
| AC1 checker passes current helper output | direct checker PASS | PASS |
| AC2 checker fails non-allowlisted fields | focused unittest PASS | PASS |
| AC3 checker fails widened adapter implementation | focused unittest PASS | PASS |
| AC4 checker fails weak claim boundary | focused unittest PASS | PASS |
| AC5 catalog wiring complete | source diff and pre-commit hook PASS | PASS |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable governance foundation file change | CREATE one bounded checker, one focused test, and catalog wiring under `governance/compat/` |
| Source layout | checker and focused test live beside existing ASSF guard/checker files |
| Index/layout mutation | N/A with reason: no ASSF registry source, generated index, resolver, package root, or Web runtime mutation |
| Split/refactor posture | N/A with reason: this is an additive guard wiring tranche |
| Storage claim boundary | local governance compatibility checker only; not package storage, adapter storage, queue, runtime state, or public surface |

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| AC1 | checker passes current helper output |
| AC2 | checker fails non-allowlisted readout fields |
| AC3 | checker fails adapter implementation claims other than `NOT_IMPLEMENTED` |
| AC4 | checker fails if claim boundary no longer denies adapter behavior and package execution |
| AC5 | checker is wired into autorun, pre-commit, and reviewer-fast catalogs |

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

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF metadata readout guard wiring work-order dispatch |
| claimDisposition | N/A with reason: dispatch authorization only; no implementation claim |
| receiptEvidence | N/A with reason: no runtime receipt is created by this work order |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source verification, write ownership, and verification commands |
| invocationBoundary | governed local dispatch packet authoring only |
| interceptionBoundary | no provider, adapter, package execution, external MCP, or interception claim |
| claimLanguage | implementation instructions only |
| forbiddenExpansion | adapter behavior, package instance, certification decision, lifecycle mutation, registry/generated-index/resolver mutation, provider/live proof, public-sync, push, activation, package execution, and package integration remain out of scope |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local repository tools |
| Session or invocation | ASSF-MRGW-T0-T4 work-order dispatch, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, Python source verification |
| Target paths | paired roadmap, GC-018 baseline, and this work order |
| Allowed scope source | active next allowed move at HEAD `a9adf3cb` |
| Before status evidence | baseHead `a9adf3cb`; clean worktree |
| After status evidence | pre-dispatch gates before dispatch commit |
| Diff evidence | `git diff --name-status` against baseHead `a9adf3cb` |
| Approval boundary | dispatch packet only |
| Claim boundary | no implementation, adapter behavior, provider/live proof, public-sync, package execution, registry/generated-index/resolver mutation, lifecycle mutation, certification decision, or session-sync |
| Agent type | dispatcher |
| Invocation ID | ASSF-MRGW-T0-T4-work-order-dispatch-2026-06-26 |
| Expected manifest | roadmap, GC-018 baseline, and work order |
| Actual changed set | pending dispatch changed set |
| Manifest delta | N/A with reason: pending pre-dispatch validation |

## Claim Boundary

This work order dispatches only bounded metadata-readout guard wiring. It does
not authorize adapter behavior, provider/live proof, public-sync, push, package
activation, package execution, package integration, certification decision,
lifecycle mutation, ASSF registry-source mutation, ASSF generated-index source
mutation, resolver mutation, or session-sync.
