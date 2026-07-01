# CVF Agent Work Order - WOAS-R2 Source-Intake Scaffold Golden Fixture

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: WOAS-R2

Dispatch base head: b23a2792

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: Codex

Worker return path: `docs/reviews/CVF_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_WORKER_RETURN_2026-07-01.md`

Completion review path: `docs/reviews/CVF_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_COMPLETION_2026-07-01.md` (reviewer optional; prefer worker-return acceptance unless a separate closure artifact is needed)

## Dispatch Prompt Envelope

Role: delegated worker for WOAS-R2.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_2026-07-01.md`

Paired GC-018 baseline: `docs/baselines/CVF_GC018_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_2026-07-01.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-01. Dispatch base is `b23a2792`,
the session-sync commit that records WOAS-R1 material closure commit
`fb6a0ae9`.

Do-not-misread notes: this packet dogfoods the WOAS-R1 helper on a
source-intake profile. It does not authorize real external source intake,
source import, external repository classification, runtime/provider/live proof,
public-sync, Web/UI dashboard work, MCP/CLI adapter work, package lifecycle
mutation, model-router work, action authority, automatic invocation, or
production-readiness claims.

Required first actions: read startup files, guard orientation, literal gotchas,
this work order, the paired GC-018 baseline, WOAS-R1 standard, and all checker
source listed in the Checker Source Read-Ahead Block before writing any artifact.
Capture `executionBaseHead` and `git status --short`.

Return contract: create the worker return artifact, run required tests and
gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Use the WOAS-R1 scaffold helper on its source-intake profile and turn that
output into durable test evidence. The goal is to make future source-intake
dispatch packets start from a machine-shaped form that already includes
checker-read-ahead, source verification, negative-search, no-commit handoff,
and marker-overmatch prevention cues.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| WOAS-R1 helper closure | WOAS-R1 closed bounded at material commit `fb6a0ae9`; session-sync commit `b23a2792`; helper path `governance/compat/build_dispatch_packet_scaffold.py`; focused tests path `governance/compat/test_build_dispatch_packet_scaffold.py`; standard path `docs/reference/work_order_authoring/CVF_WOAS_R1_DISPATCH_PACKET_AUTHORING_SCAFFOLD_STANDARD.md`. | Dispatch WOAS-R2 only after WOAS-R1 helper exists and session-sync is committed. | SATISFIED |
| Operator lane selection | Operator approved creating the next work order using WOAS-R1 material closure commit `fb6a0ae9` and session-sync commit `b23a2792` as release evidence. | Work order may dispatch as a helper dogfood tranche, not as real source intake. | SATISFIED |

## 1. Authority Chain

| Authority | Path or value | Disposition |
| --- | --- | --- |
| Operator instruction | Create the next work order for the proposed source-intake scaffold dogfood tranche. | ACCEPT |
| Active front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V30_2026-07-01.md` | ACCEPT |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_2026-07-01.md` | ACCEPT |
| WOAS-R1 standard | `docs/reference/work_order_authoring/CVF_WOAS_R1_DISPATCH_PACKET_AUTHORING_SCAFFOLD_STANDARD.md` | ACCEPT |

Authority boundary: if any source contradicts this work order, stop and return
`BLOCKED_WITH_REASON`. Do not resolve contradictions by widening scope.

## 2. Agent Roles

| Role | Actor | Authority |
| --- | --- | --- |
| Dispatcher | Codex | Authored and gates this dispatch packet. |
| Worker | delegated worker | Implements only the Work-Order Fulfillment Manifest and returns no-commit evidence. |
| Reviewer/closer | Codex | Accepts, rejects, or repairs allowed-scope defects; owns material commit and session-sync if accepted. |
| Operator approval required | Operator | Required for real external source intake, runtime/provider/live proof, public-sync, Web/UI dashboard, MCP/CLI adapter, package lifecycle mutation, model-router work, or production claim. |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intakeRoute | DISPATCH_HELPER_DOGFOOD |
| selected role route | routeMode=MULTI_AGENT_SINGLE_ROLE |
| dispatcherRole | Codex dispatch author creates WOAS-R2 GC-018 and work order. |
| workerRole | delegated worker executes helper/test/fixture changes only and returns no-commit evidence. |
| reviewerRole | Codex reviewer/closer accepts or rejects the worker return and owns commits. |
| escalation condition | Escalate only for missing source authority, forbidden-scope need, destructive action, live/provider/public request, or real external source intake. |
| noQuestionBoundary | Worker repairs allowed-scope gate failures by reading checker source and matching literal shapes. |
| claimBoundary | Role routing only; no runtime/provider/live/public/package/Web/MCP/model-router behavior is authorized. |

## 3. Scope

Allowed scope:

- Run `governance/compat/build_dispatch_packet_scaffold.py` in source-intake generation mode with `--stdout`.
- Add or update focused tests in `governance/compat/test_build_dispatch_packet_scaffold.py`.
- Modify `governance/compat/build_dispatch_packet_scaffold.py` only if tests prove source-intake output lacks required scaffold shape.
- Create `governance/compat/fixtures/woas_r2_source_intake_scaffold_golden.md` only if fixture-backed testing is the cleanest implementation.
- Create the worker return at `docs/reviews/CVF_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_WORKER_RETURN_2026-07-01.md`.

Forbidden scope:

- Do not absorb, scan, classify, or import any real external repository or folder.
- Do not edit `.private_reference/source_mirrors/`, corpus registries, ASSF registries, package skill roots, Web data, runtime routes, provider registries, MCP/CLI adapters, public-sync files, secrets, or active session state as worker.
- Do not add hook catalog wiring or a new blocking checker.
- Do not claim runtime/provider/live/public/package/Web/MCP/model-router behavior.
- Do not commit as worker.

Risk ceiling: R1 documentation/helper-test hardening only.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007, ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 10 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0006; ADIF-0007; ADIF-0014; ADIF-0015; ADIF-0016; ADIF-0017; ADIF-0020; ADIF-0021 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0006; ADIF-0007; ADIF-0014; ADIF-0015; ADIF-0016; ADIF-0017; ADIF-0020; ADIF-0021 |
| Dispatch impact | Worker must read disclosed entries before editing. The work specifically targets ADIF-0020 and ADIF-0021 prevention. |

## 4. Required First Reads

| Read order | Required file or command |
| --- | --- |
| 1 | `CVF_SESSION_MEMORY.md` |
| 2 | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| 3 | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| 4 | `AGENT_HANDOFF_V30_2026-07-01.md` |
| 5 | `docs/reference/guard_orientation/README.md` |
| 6 | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` |
| 7 | `docs/reference/work_order_authoring/CVF_WOAS_R1_DISPATCH_PACKET_AUTHORING_SCAFFOLD_STANDARD.md` |
| 8 | `governance/compat/build_dispatch_packet_scaffold.py` |
| 9 | `governance/compat/test_build_dispatch_packet_scaffold.py` |
| 10 | All checkers named in the Checker Source Read-Ahead Block |

## 5. Pre-Flight Checks

At execution start, worker must run:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
Test-Path docs/reviews/CVF_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_WORKER_RETURN_2026-07-01.md
```

Expected `Test-Path` result before worker-return creation is `False`.

## Worker Autonomy / No-Question Rule

Worker proceeds without operator confirmation for non-destructive actions inside
Allowed scope, including test additions, fixture creation, helper-shape repair,
and repeated guard reruns after allowed-scope remediation.

Worker must return to orchestrator only for source contradiction, missing
authority, forbidden-scope need, live/provider/public request, destructive
action, or a required claim-boundary change.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_package_skill_productionization_pipeline.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_machine_closure_package.py` |
| literalTokensReviewed | `## ADIF Defect Registry Disclosure`; `Resolver query: taskClass=`; `## Checker Source Read-Ahead Block`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `WORKER_MUST_NOT_COMMIT`; `## Dispatch Prompt Envelope`; `## Source Verification Block`; `## Negative Search And Collision Discipline`; `## Agent Handoff Contract Control Block`; `## Reviewer Closure Conversion`; `## Work-Order Fulfillment Manifest`; `## Worker Return Packet Shape Contract`; `APPLICABILITY_MARKER`; `STANDALONE_MARKER_PATTERN`; `REQUIRED_SECTION`; `REQUIRED_FIELDS`; `External Knowledge Intake Routing`; `## Overlap And Novelty Classification`; `## Foundation Storage Layout Block`; `Package Skill control block fields`; `DEFERRED_PRIVATE_ONLY`; `ADIF-0020`; `ADIF-0021` |
| gateRunPurpose | Pre-write and pre-dispatch confirmation evidence, not first discovery. |
| claimBoundary | Dispatcher read-ahead only. Worker must repeat read-ahead and record it in the worker return before claiming completion. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| WOAS-R1 helper supports the `source-intake` packet kind. | VALUE_SET | `governance/compat/build_dispatch_packet_scaffold.py` | line 35 | `source-intake` | `PACKET_KINDS` | ACCEPT |
| WOAS-R1 trigger families include source-intake indicators and source-intake stub text. | VALUE_SET | `governance/compat/build_dispatch_packet_scaffold.py` | lines 47-64 | `TRIGGER_FAMILIES` | scaffold trigger map | ACCEPT |
| Helper has a dedicated source-intake stub builder. | EXISTS | `governance/compat/build_dispatch_packet_scaffold.py` | line 365 | `_source_intake_stub` | scaffold renderer | ACCEPT |
| Existing tests assert source-intake indicator activation and stub presence. | EXISTS | `governance/compat/test_build_dispatch_packet_scaffold.py` | lines 191-198 | `test_source_intake_indicator_activates_trigger_and_stub` | scaffold focused tests | ACCEPT |
| WOAS-R1 standard defines the source-intake packet kind. | VALUE_SET | `docs/reference/work_order_authoring/CVF_WOAS_R1_DISPATCH_PACKET_AUTHORING_SCAFFOLD_STANDARD.md` | line 38 | `source-intake` | WOAS-R1 scaffold standard | ACCEPT |
| WOAS-R1 standard maps source-intake trigger to decision fields and negative-search rows. | VALUE_SET | `docs/reference/work_order_authoring/CVF_WOAS_R1_DISPATCH_PACKET_AUTHORING_SCAFFOLD_STANDARD.md` | line 81 | `source-intake` | Trigger Map Requirements | ACCEPT |
| Work orders must place Dispatch Prompt Envelope before other `##` sections. | VALUE_SET | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 9 | `Dispatch Prompt Envelope Placement Rule` | work-order template | ACCEPT |
| Work-order template requires Worker Autonomy / No-Question Rule. | EXISTS | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 442 | `Worker Autonomy / No-Question Rule` | work-order template | ACCEPT |
| Work-order template requires Work-Order Fulfillment Manifest for delegated source work. | EXISTS | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 649 | `Work-Order Fulfillment Manifest` | work-order template | ACCEPT |
| Source-intake preflight checker applies only to standalone marker declaration lines. | VALUE_SET | `governance/compat/check_source_intake_decision_packet_preflight.py` | lines 37-75 | `STANDALONE_MARKER_PATTERN` | source-intake preflight checker | ACCEPT |
| External knowledge intake routing guard requires canonical fields and input types when applicable. | VALUE_SET | `governance/compat/check_external_knowledge_intake_routing.py` | lines 29-48 | `REQUIRED_FIELDS; ALLOWED_INPUT_TYPES` | external knowledge intake routing checker | ACCEPT |
| Core guard treats `governance/compat/*.py` files as protected paths. | VALUE_SET | `governance/compat/check_core_guard_self_protection.py` | lines 36-112 | `_is_protected` | core guard self-protection checker | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned baseline path | `Test-Path docs/baselines/CVF_GC018_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_2026-07-01.md` returned `False` before authoring. | ACCEPT |
| Planned work-order path | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_2026-07-01.md` returned `False` before authoring. | ACCEPT |
| Existing WOAS-R2 collision search | `rg -n "WOAS-R2|SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE|Source-Intake Scaffold Golden Fixture" docs governance CVF_SESSION AGENT_HANDOFF_V30_2026-07-01.md CVF_SESSION_MEMORY.md` returned no pre-existing WOAS-R2 dispatch artifact before authoring. | ACCEPT |
| Existing helper surface | `rg -n "source-intake|Source-Intake|_source_intake_stub" governance/compat/build_dispatch_packet_scaffold.py governance/compat/test_build_dispatch_packet_scaffold.py docs/reference/work_order_authoring/CVF_WOAS_R1_DISPATCH_PACKET_AUTHORING_SCAFFOLD_STANDARD.md` found the WOAS-R1 helper and tests, which are intended owner surfaces. | ACCEPT |
| Collision decision | No existing WOAS-R2 golden fixture or generated-example artifact was found. | ACCEPT |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | N/A with reason: WOAS-R2 dogfoods an authoring helper profile; it is not an external source intake or absorption execution packet. |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/work_order_authoring/`; `governance/compat/build_dispatch_packet_scaffold.py`; `governance/compat/test_build_dispatch_packet_scaffold.py` |
| Disposition | NOT_APPLICABLE_WITH_REASON: no external source content may be classified or absorbed. |
| Claim boundary | Routing section only; no external repo/folder intake, source import, source-mirror mutation, package absorption, runtime/provider/live proof, public-sync, Web/UI dashboard, MCP/CLI adapter, model-router, action-authority, automatic invocation, or production-readiness claim. |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| WOAS-R2 source-intake scaffold dogfood | `docs/reference/work_order_authoring/`; `governance/compat/build_dispatch_packet_scaffold.py`; `governance/compat/test_build_dispatch_packet_scaffold.py` | ENRICH_EXISTING | Adds fixture/test pressure to the existing WOAS-R1 helper owner surface; does not absorb any external source value. | Modify only helper/tests/optional fixture under this work order. |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher_creates_packet_then_worker_returns_no_commit_then_reviewer_closes |
| phase | pre-dispatch_to_worker_implementation_to_reviewer_closure |
| baseHeadFor(phase) | dispatchBaseHead=b23a2792; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | Worker may change only helper/test/optional fixture and worker return paths named in the Work-Order Fulfillment Manifest. |
| traceScope(phase, actor) | Worker return must include command evidence, actual changed set, and no-commit status; reviewer records accepted material range. |
| commitOwner(phase) | Worker must not commit; reviewer owns material commit and session-sync commit if needed. |
| crossBatchIsolation | Do not mix WOAS-R2 with real source intake, EverOS/CodeGraph absorption, runtime/provider/live proof, Web/dashboard, MCP/CLI, model gateway, package lifecycle, public-sync, or session-sync as worker. |
| nextMoveSurfaces | Worker must not edit active session state, front door, or active handoff. Reviewer/closer owns next-move updates after acceptance. |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_COMPLETION_2026-07-01.md` (optional; prefer repairing evidence in the worker return per gotcha 30) |
| reviewerOwnedClosurePaths | this work order; paired GC-018 baseline; worker-return artifact; optional reviewer completion review; optional session-sync surfaces if accepted |
| closureOwner | Codex reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: worker may modify only the existing WOAS-R1
helper and its focused test file, and may create one non-runtime fixture or
generated-example artifact if needed. No new checker, hook catalog wiring,
session state edit, or broader guard semantics are authorized for the worker.

Protected paths:

- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`

Operator authorization: operator approved creating this WOAS-R2 work order
using WOAS-R1 material closure commit `fb6a0ae9` and session-sync commit
`b23a2792` as release evidence, to strengthen helper-generated forms for future
source-intake packet authoring.

Rollback boundary: if rejected, revert only WOAS-R2 helper/test/fixture and
worker-return changes; do not revert WOAS-R1, KIOD-R8, or session history.

## Write Ownership

| Surface | Owner |
| --- | --- |
| `governance/compat/build_dispatch_packet_scaffold.py` | Worker may modify only for source-intake scaffold shape repair. |
| `governance/compat/test_build_dispatch_packet_scaffold.py` | Worker may add focused source-intake scaffold tests. |
| `governance/compat/fixtures/woas_r2_source_intake_scaffold_golden.md` | Worker may create only if fixture-backed tests are used. |
| `docs/reviews/CVF_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_WORKER_RETURN_2026-07-01.md` | Worker must create and leave uncommitted. |
| Material commit | Reviewer/closer only. |
| Active session state, front door, active handoff | Reviewer/closer only after accepted material commit, if continuity changes. |

Any file outside this table is forbidden unless a reviewer issues a fresh
source-verified work order or the operator explicitly changes scope.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `governance/compat/build_dispatch_packet_scaffold.py` | Modify only if current source-intake output lacks required golden-fixture shape. |
| `governance/compat/test_build_dispatch_packet_scaffold.py` | Add focused tests for source-intake golden output and marker-overmatch avoidance. |
| `governance/compat/fixtures/woas_r2_source_intake_scaffold_golden.md` | Optional fixture path; create only if fixture-backed testing is cleaner than inline expected-output assertions. |
| `docs/reviews/CVF_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_WORKER_RETURN_2026-07-01.md` | Required worker return with command evidence, changed files, no-commit statement, and required review-shape sections. |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Planned durable reference folder | N/A with reason: worker is not authorized to create a new `docs/reference/` folder or standard. |
| Planned front door/index | N/A with reason: no new durable reference family is created by this work order. |
| Date policy | N/A with reason: no new dated reference standard is authorized. |
| Owner surface | Existing helper/test owner surface under `governance/compat/` plus optional local fixture path. |
| Claim boundary | Storage block is present only because the work order discusses durable scaffold evidence; no foundation storage refactor, split, relocation, or new reference folder is authorized. |

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: N/A with reason: this work order mentions package-skill only as a forbidden expansion and helper trigger family, not as package productionization work.

Target lifecycle state: N/A with reason: no package lifecycle state is changed.

Prior phase evidence: N/A with reason: no package-skill productionization work is authorized.

Next forbidden skip: Do not use WOAS-R2 to promote, activate, load, project, or claim runtime eligibility for any package skill.

Runtime/provider proof: N/A with reason: no runtime or provider behavior is claimed.

Claim boundary: Package-skill references are boundary examples only.

## Worker Return Packet Shape Contract

Worker return must include:

- `Status`
- `dispatchWorkOrder`
- `Purpose`
- `Scope / Methodology`
- `Findings / Position`
- `Risk / Corrective Action`
- `Claim Boundary`
- `Agent Operation Trace Block`
- `Delta Execution Claim Boundary Control Block`
- `Public Export Disposition`
- `executionBaseHead`
- `git status --short`
- changed files
- command evidence
- no-commit statement

Worker return must also include these conditional sections, each filled with
evidence or `N/A with reason` / `NOT_APPLICABLE_WITH_REASON`:

- `External Knowledge Intake Routing`
- `Rescan Intelligence Hardening`
- `Corpus Completeness And Report Integrity`
- `Finding-To-Governance Learning Disposition`
- `Epistemic Process Block`
- `Machine Closure Package`

Review-shape headings must include at least one target/source heading, one
scope/methodology heading, one findings/position heading, one risk/corrective
action heading, and one decision/recommendation/disposition heading.

## Source-Intake Scaffold Requirements

Worker must verify that source-intake scaffold output includes, at minimum:

| Requirement | Required evidence |
| --- | --- |
| Dispatch Prompt Envelope first | Focused test checks first `##` heading in generated work order. |
| No-commit handoff fields | Focused test checks Agent Handoff Contract Control Block and Reviewer Closure Conversion for `WORKER_MUST_NOT_COMMIT`. |
| Checker read-ahead fields | Focused test checks `applicableCheckersRead`, `literalTokensReviewed`, `gateRunPurpose`, and `claimBoundary`. |
| Source verification table shape | Focused test checks required source verification columns. |
| Negative-search rows | Focused test checks `## Negative Search And Collision Discipline` and search/collision rows. |
| Source-intake stub | Focused test checks the helper's source-intake trigger stub is present and does not declare a real source-intake packet. |
| Marker-overmatch avoidance | Focused test checks generated source-intake profile does not include the standalone declaration marker that would opt the artifact into the KIOD-R8 preflight checker unless the helper explicitly supports a real decision packet mode in a future work order. |
| Public export default | Focused test checks `DEFERRED_PRIVATE_ONLY`. |

## Execution Plan

Worker executes in this order:

1. Capture `executionBaseHead` and `git status --short`.
2. Read all required files and checker source.
3. Run the helper in source-intake mode and inspect the output.
4. Add focused tests and optional fixture for source-intake scaffold shape.
5. Patch helper output only if the tests expose a shape gap.
6. Run focused tests and smoke commands.
7. Run worker-return fast gate after writing the worker return.
8. Leave changes uncommitted and return `COMPLETE_PENDING_REVIEW`.

## Evidence Requirements

| Evidence item | Required evidence |
| --- | --- |
| Base anchor | `git rev-parse --short HEAD` captured at worker start. |
| Worktree status | `git status --short` before and after worker changes. |
| Changed files | `git diff --name-status <executionBaseHead>..HEAD` plus untracked path list if any. |
| Helper source-intake smoke | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id WOAS-R2-SMOKE --title "Source Intake Scaffold Golden Fixture" --date 2026-07-01 --base <executionBaseHead> --commit-mode WORKER_MUST_NOT_COMMIT --dependency "WOAS-R1 closed bounded at material commit fb6a0ae9" --stdout` |
| Focused tests | `python -m unittest governance.compat.test_build_dispatch_packet_scaffold` |
| Worker-return fast gate | `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_build_dispatch_packet_scaffold.py` |
| Pre-closure pending range | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <executionBaseHead> --head HEAD` with no-commit pending-finality limitations clearly classified if present. |
| No commit | Worker return states HEAD unchanged from `executionBaseHead`. |

## Review Gate

Reviewer/closer must reject or return the worker output if:

- worker absorbed or classified real external source content;
- worker edited outside the Work-Order Fulfillment Manifest;
- helper output omits required source-intake scaffold fields;
- source-intake output opts into a real decision-packet checker without all required real packet fields;
- tests or required gates fail without an allowed-scope repair;
- worker commits material;
- worker claims runtime, provider, public, package lifecycle, Web, MCP/CLI, model-router, action authority, automatic invocation, or production behavior.

## Operator Checkpoint

No operator checkpoint is required for allowed-scope helper/test/fixture
remediation. Operator checkpoint is required for real source intake, any live or
provider call, public-sync, runtime code, Web/UI dashboard work, MCP/CLI adapter
work, package lifecycle mutation, model-router work, hook catalog wiring, new
blocking checker semantics, or higher risk.

## Acceptance Criteria

| AC | Criteria | Evidence |
| --- | --- | --- |
| AC1 | Source-intake scaffold output is represented by focused tests or a deterministic fixture. | Test file and optional fixture. |
| AC2 | Generated work order keeps Dispatch Prompt Envelope as the first `##` section. | Focused unittest. |
| AC3 | Generated output contains no-commit handoff, reviewer conversion, checker read-ahead, source verification, negative-search, and public export default sections. | Focused unittest. |
| AC4 | Generated source-intake profile avoids false opt-in as a real decision packet unless a future packet explicitly authorizes real decision packet mode. | Focused unittest referencing source-intake preflight marker behavior. |
| AC5 | Worker return records read-ahead, evidence, no commit, and no forbidden claims. | Worker return plus fast gate. |

## Required Verification After Release

Worker must run and report:

```powershell
python -m unittest governance.compat.test_build_dispatch_packet_scaffold
python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id WOAS-R2-SMOKE --title "Source Intake Scaffold Golden Fixture" --date 2026-07-01 --base <executionBaseHead> --commit-mode WORKER_MUST_NOT_COMMIT --dependency "WOAS-R1 closed bounded at material commit fb6a0ae9" --stdout
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_build_dispatch_packet_scaffold.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <executionBaseHead> --head HEAD
```

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | WOAS-R2 work-order authoring, 2026-07-01 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, `rg`, `Get-Content`, `apply_patch`, WOAS-R1 scaffold helper |
| Target paths | `docs/baselines/CVF_GC018_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_2026-07-01.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_2026-07-01.md` |
| Allowed scope source | operator instruction to create this work order using WOAS-R1 material closure commit `fb6a0ae9` and session-sync commit `b23a2792` as release evidence |
| Before status evidence | HEAD `b23a2792`; clean worktree before WOAS-R2 authoring |
| After status evidence | WOAS-R2 dispatch packet pending commit |
| Diff evidence | `git diff --name-status b23a2792..HEAD` |
| Approval boundary | dispatch packet authoring only |
| Claim boundary | no real external source intake, runtime/provider/live proof, public-sync, Web/UI dashboard, MCP/CLI adapter, package lifecycle, model-router, action authority, automatic invocation, or production claim |
| Agent type | dispatcher |
| Invocation ID | `woas-r2-source-intake-scaffold-golden-fixture-2026-07-01` |
| Expected manifest | `docs/baselines/CVF_GC018_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_2026-07-01.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_2026-07-01.md` |
| Actual changed set | `docs/baselines/CVF_GC018_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_2026-07-01.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_WOAS_R2_SOURCE_INTAKE_SCAFFOLD_GOLDEN_FIXTURE_2026-07-01.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch authoring |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | WOAS-R2 helper/test dogfood dispatch packet only |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt evidence is needed because the runtime claim is rejected. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action evidence is needed because no runtime action is claimed. |
| invocationBoundary | Worker manually runs local helper/tests only. |
| interceptionBoundary | No IDE/shell/git/filesystem/provider interception claim. |
| claimLanguage | Source-intake scaffold dogfood and focused tests only. |
| forbiddenExpansion | Do not expand into real source intake, runtime/provider/live/public/package/Web/MCP/model-router behavior, action authority, automatic invocation, hook catalog wiring, or production readiness. |

## Claim Boundary

This work order authorizes only a bounded helper/test dogfood tranche under
`WORKER_MUST_NOT_COMMIT`. It does not authorize real outside-source intake,
source import, external repository classification, runtime/provider/live proof,
public-sync, Web/UI dashboard work, MCP/CLI adapter work, model-router work,
package lifecycle mutation, action authority, automatic invocation, or
production-readiness claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: WOAS-R2 is private provenance governance-helper work. Public-sync is
outside this packet.

## Closure Checklist

- [ ] Worker captured `executionBaseHead` and initial `git status --short`.
- [ ] Worker read all required files and checker source before editing.
- [ ] Worker stayed inside Write Ownership and Work-Order Fulfillment Manifest.
- [ ] Focused helper tests passed.
- [ ] Source-intake helper smoke command was run and recorded.
- [ ] Worker-return fast gate passed or remaining limitations are classified.
- [ ] Worker made no commit.
- [ ] Reviewer accepted or rejected the worker return.
- [ ] Reviewer/closer ran commit steward preflight before material commit.
- [ ] Pre-closure autorun passed on the accepted material range.
- [ ] Session-sync, if needed, was committed separately from material closure.
