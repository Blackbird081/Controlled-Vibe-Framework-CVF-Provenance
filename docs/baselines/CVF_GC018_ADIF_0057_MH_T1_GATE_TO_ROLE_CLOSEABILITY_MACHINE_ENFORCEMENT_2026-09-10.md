# CVF GC-018 Baseline - ADIF-0057-MH-T1 Gate-To-Role Closeability Machine Enforcement

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Batch ID: ADIF-0057-MH-T1

Dispatch base head: fe62894f861c34a25a16c6267f557bf771ea9e2c

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: independent reviewer

Worker target: implementation worker

## Purpose

Authorize one bounded Core tranche that turns ADIF-0057 from written and
partial review-cost guidance into repository machine enforcement. The guard
must reject declared responsibility topologies that have cycles, late-only
repair authority, missing mutation owners, or missing post-review commit
ownership, while preserving agent freedom over ordinary implementation
decomposition inside authorized surfaces.

## Scope / Target / Owner Boundary

The worker may add one undated standard, one checker and its focused tests; wire the
checker into common autorun, reviewer-fast, and pre-commit catalogs; update the
work-order template, AGENTS router, and ADIF-0057 enforcement claim; and write
the worker return. No runtime interception, provider call, project repair,
public sync, deployment, or automatic authority expansion is authorized.

## Decision / Baseline

`ADIF-0057-MH-T1` is `DISPATCH_READY`. Machine enforcement is declaration-
based and fail-closed: new or amended executable work orders declare a
gate-to-role graph, while changed worker returns and completion reviews declare
the return-time closeability result before repair. The checker validates
structure and reachability, not code architecture or semantic design quality.

## Acceptance Matrix

| ID | Required outcome | Negative proof |
|---|---|---|
| C1 | Every changed executable work order carries the versioned closeability contract. | Missing or malformed contract fails. |
| C2 | Every mutating gate has an authorized repair owner and commit owner. | `NONE` owner on a mutating row fails. |
| C3 | Repair phase is not later than the phase by which the gate must pass. | closer-only catalog repair required before reviewer acceptance fails. |
| C4 | Gate dependencies form a directed acyclic graph, name real rows, and include post-dispatch GC-020 continuity before implementation. | unknown dependency, cycle, or missing dispatch continuity fails. |
| C5 | Implementation topology policy either covers foreseeable splits or truthfully fixes a no-split size budget. | exact-only plus foreseeable split fails. |
| C6 | Changed worker returns and completion reviews classify return-time closeability before repair. | packet contradiction plus worker redispatch `YES` fails. |
| C7 | Common autorun, reviewer-fast, and pre-commit catalogs invoke the checker. | missing catalog binding fails focused wiring tests. |
| C8 | ADIF-0057 becomes `MACHINE_CHECKED` only after executable proof passes. | dangling or partial binding fails integrity check. |

## Evidence / Verification

Required evidence: focused positive, malformed, cycle, late-writer, missing-
owner, exact-path/split, and return-time fail-stop tests; catalog wiring tests;
ADIF integrity; pre-implementation gate; reviewer-fast; pre-commit; clean
staging on worker return.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| ADIF-0057 requests pre-dispatch declared closeability | defect remediation | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0057.md` | Remediation 1 and 6 | gate-to-role closeability | ADIF-0057 | ACCEPT |
| Return-time reviewer classification is binding prose | standard authority | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | Return-Time Closeability And Agent-Intelligence Preservation | fail-stop routes | Review Cost standard | ACCEPT |
| Common autorun commands execute across phases | executable owner fact | `governance/compat/agent_autorun_command_catalog.py` | `_common_commands` | GateCommand list | autorun command catalog | ACCEPT |
| Pre-commit catalog is the local commit binding | executable owner fact | `governance/compat/local_governance_hook_catalog_pre_commit.py` | `PRE_COMMIT_CHECKS` | command list | pre-commit catalog | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`,
lifecyclePhase=`pre-dispatch`, risk ceiling=`HIGH`.

Returned bounded readout: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015,
ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044; readout was
truncated at 10 of 24. Source-directed ADIF-0057 was read in full and controls
this tranche. Impact: exact evidence, checker read-ahead, protected-path
authorization, and non-prescriptive machine semantics are explicit.

## Task Governance Routing Manifest

Routing mode: `HEAVY_GOVERNANCE_WITH_REASON` - this tranche changes Core
checkers and hook catalogs. Execution is internal-agent only; independent
completion review remains required.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ADIF-0057-MH-T1 --title "Gate-To-Role Closeability Machine Enforcement" --date 2026-09-10 --base fe62894f861c34a25a16c6267f557bf771ea9e2c --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced all placeholders with the bounded machine-enforcement contract and exact manifest. |
| checkerReadAheadConfirmation | Dispatch, structural, read-ahead, self-protection, review-cost, ADIF and catalog owners were read before authoring. |
| docOnlyNewFields | Gate-to-role closeability fields are executable checker inputs, not advisory metadata. |
| claimBoundary | Dispatch authoring provenance only. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_docs_governance_compat.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | `docType: baseline`; `Status: DISPATCH_READY`; Source Verification Block; Checker Source Read-Ahead Block; Core Guard Self-Protection Authorization; Public Export Disposition |
| gateRunPurpose | Confirmation and evidence after authoring, not first discovery of required shape. |
| claimBoundary | Read-ahead covers the governed dispatch artifacts only; implementation checkers must carry their own tests. |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add and wire the ADIF-0057 closeability
checker, its standard/tests, template/router binding, truthful ADIF promotion,
and bounded work/review artifacts.

Protected paths:

- `AGENTS.md`
- `governance/compat/check_gate_to_role_closeability.py`
- `governance/compat/test_check_gate_to_role_closeability.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/test_run_local_governance_hook_chain.py`

Operator authorization: on 2026-09-10 the operator explicitly ordered a
separate Core tranche to raise ADIF-0057 from `PARTIAL_CHECK` to machine-
enforced for every governed agent path, after P4-E was parked.

Rollback boundary: revert only ADIF-0057-MH-T1 material and continuity. Preserve
P4-E learning commits `3fcd426dc` and `fe62894f8` and every unrelated tranche.

Not authorized: direct process interception, hidden-memory transfer,
automatic path widening, runtime/provider/live use, public sync, push,
deployment, or production claims.

## Risk / Corrective Action

False precision could suppress agent judgment. Therefore the guard accepts
bounded path families and validates declared responsibility reachability only.
Malformed or contradictory declarations fail closed with path-local messages.

## Current Runtime Freshness Verification

Runtime/provider freshness: `NOT_APPLICABLE_WITH_REASON` - repository static
governance only; no provider or live behavior is claimed.

## Machine Closure Package

Closure requires a dispatch-control commit containing the independently
accepted authorization review, then focused tests, catalog wiring proof, ADIF
integrity, full applicable governance gates, and independent completion review
inside one material commit. Committed-range closure follows; any failure uses
one declared corrective-material route before separate continuity.

## Claim Boundary

This baseline authorizes repository machine checks on declared packet topology.
It does not prove agent comprehension, semantic correctness, or interception
of tools that bypass CVF gates and Git hooks.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening; no public-sync action is in
scope.
