# CVF GC-018 Baseline - MSEA-R92 Worker Return Scaffold Last-Mile Hardening

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA-R92

Dispatch base head: `668cecf7d`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: CVF operator

Reviewer owner: reviewer/closer role

Worker target: delegated worker role

## Purpose

Authorize one small, profile-neutral authoring-helper hardening tranche before
the next roadmap or advisory cleanup packet. Repair the direct worker-return
scaffold used in MSEA-R91 so it emits checker-required markers, exact evidence
headings, a complete checker-read-ahead table, and last-mile finalization
guidance without changing checker semantics or compact-profile eligibility.

## Baseline Decision

Decision: `DISPATCH_READY_BOUNDED_HELPER_HARDENING`.

The source-backed defect is local to `run_worker_return_scaffold.py`. The older
dispatch skeleton builder already emits the required markers and headings, so
its golden fixture is comparison evidence, not a change target.

## Evidence / Verification

| Evidence | Current result | Disposition |
|---|---|---|
| MSEA-R91 worker retrospective | nine manual repair cycles across two rounds, including worker-return structure and literal-shape repair | ACCEPT as bounded experience evidence |
| Direct scaffold helper | missing self-declaration, work-order response marker, exact status and changed-file headings, no-commit section, and checker-read-ahead field table | ACCEPT as the implementation target |
| Dispatch skeleton builder | already carries the required marker and heading shapes | ACCEPT as comparison source; no modification |
| R84 compact profile | backward-compatible and fail-closed, but not directly exercised by R91 | PRESERVE; no eligibility expansion |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MSEA-R91 closure | completion material commit `017ae9718`; session sync `668cecf7d` | R91 must be accepted before its worker experience can inform hardening | SATISFIED |
| Operator priority | operator directed this separate small tranche before roadmap continuation on 2026-07-10 | explicit order change must precede dispatch | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R92 --title "Worker Return Scaffold Last Mile Hardening" --date 2026-07-10 --base 668cecf7d --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SATISFIED: MSEA-R91 reviewer closure at 017ae9718 and operator priority on 2026-07-10." --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced scaffold fields with exact source rows, five-path worker scope, regression tests, protected-path authorization, and no-refactor boundaries. |
| checkerReadAheadConfirmation | `check_worker_return_quality_gate.py`; dispatch-quality, core-guard, trace, closure, and file-size checkers |
| docOnlyNewFields | none |
| claimBoundary | Dispatch authoring provenance only; no runtime, provider, public, Web, MCP, model-router, or semantic-enforcement claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`worker-return scaffold authoring hardening`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "worker-return scaffold authoring hardening" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | No ADIF-specific addition beyond ordinary governed dispatch controls. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_closure_packaging_preflight.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; required worker-return markers/headings; `gateRunPurpose`; `Core Guard Self-Protection Authorization`; `Agent Operation Trace Block`; `Public Export Disposition` |
| gateRunPurpose | Confirmation and evidence after checker-source read-ahead; gates are not used for first discovery. |
| claimBoundary | Baseline and planned five-path helper hardening only. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Direct scaffold section inventory | EXISTS | `governance/compat/run_worker_return_scaffold.py` | lines 25-47 | `WORKER_RETURN_SCAFFOLD_SECTIONS` | scaffold section tuple | ACCEPT |
| Direct scaffold renderer | RUNTIME_BEHAVIOR | `governance/compat/run_worker_return_scaffold.py` | lines 61-203 | `_section_body` | scaffold section body renderer | ACCEPT |
| Direct scaffold top-level output | RUNTIME_BEHAVIOR | `governance/compat/run_worker_return_scaffold.py` | lines 206-234 | `build_scaffold` | scaffold text builder | ACCEPT |
| Required worker-return markers | LITERAL_INVARIANT | `governance/compat/check_worker_return_quality_gate.py` | lines 35-36 | `SELF_DECLARE_MARKER`; `RESPONDS_MARKER` | worker-return quality checker | ACCEPT |
| Required headings | LITERAL_INVARIANT | `governance/compat/check_worker_return_quality_gate.py` | lines 54-78 | `REQUIRED_HEADINGS`; `FAST_DOC_REQUIRED_HEADINGS` | worker-return quality checker | ACCEPT |
| Confirmatory read-ahead purpose | LITERAL_INVARIANT | `governance/compat/check_worker_return_quality_gate.py` | lines 294-301 | `gateRunPurpose` first-discovery rejection | worker-return quality checker | ACCEPT |
| Existing direct-helper tests | EXISTS | `governance/compat/test_run_worker_return_scaffold.py` | lines 19-140 | `WorkerReturnScaffoldTests` | unittest suite | ACCEPT |
| Comparison scaffold already has correct shape | RUNTIME_BEHAVIOR | `governance/compat/build_worker_return_skeleton_scaffold.py` | lines 41-42, 60, 119-130 | `build_worker_return_skeleton` | dispatch worker-return skeleton builder | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Packet path collision | both planned paths returned `False` under `Test-Path` before authoring | CREATE planned packet paths |
| Batch/title collision | `rg -n "MSEA-R92|WORKER_RETURN_SCAFFOLD_LAST_MILE_HARDENING|Worker Return Scaffold Last Mile Hardening" docs CVF_SESSION governance .github --hidden --no-ignore` returned no prior artifact | NO_ACTIVE_COLLISION |
| Golden fixture ownership | direct read shows the comparison builder already emits required markers/headings | DO_NOT_MODIFY comparison helper or golden fixture |

## Allowed Scope

Worker may modify exactly:

- `governance/compat/run_worker_return_scaffold.py`;
- `governance/compat/test_run_worker_return_scaffold.py`;
- `docs/reference/work_order_authoring/CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md`;
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`;
- `docs/reviews/CVF_MSEA_R92_WORKER_RETURN_SCAFFOLD_LAST_MILE_HARDENING_WORKER_RETURN_2026-07-10.md`.

Every other path is forbidden, including worker-return checkers, compact
eligibility logic, hook/autorun catalogs, session state, public-sync, R91
artifacts, cleanup paths, and the comparison scaffold/golden fixture.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: bounded authoring-helper and regression
test improvement only; no checker or enforcement-severity change.

Protected paths:

| Path | Purpose |
|---|---|
| `governance/compat/run_worker_return_scaffold.py` | Emit checker-aligned full and compact worker-return starting shapes. |
| `governance/compat/test_run_worker_return_scaffold.py` | Prove marker, heading, read-ahead, finalization, profile, and write-safety invariants. |

Operator authorization: harden the worker-reported repeated friction before
continuing the roadmap, without opening a governance refactor.

Rollback boundary: revert only MSEA-R92 helper/docs/tests; do not revert R84,
R91, session continuity, or unrelated governance controls.

## Claim Boundary

This baseline authorizes a five-path authoring-helper maintenance tranche. It
does not authorize a new checker, checker weakening, new hook/catalog wiring,
automatic prose rewriting, compact-profile defaulting or expansion, runtime or
provider work, public export, advisory relocation, or roadmap implementation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MSEA-R92 is private provenance helper hardening with no public-sync
authorization.
