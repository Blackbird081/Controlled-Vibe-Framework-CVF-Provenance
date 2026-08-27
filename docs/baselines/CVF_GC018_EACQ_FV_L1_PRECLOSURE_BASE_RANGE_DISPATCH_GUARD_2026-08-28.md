# CVF GC-018 Baseline - EACQ-FV L1 Pre-Closure Base Range Dispatch Guard

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: EACQ-FV-L1

Date: 2026-08-28

Dispatch base head: `3a7d210bebdec728a10e708468fde3947da3581b`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Worker: delegated no-commit implementation worker

Orchestrator/reviewer/closer: designated internal reviewer

providerExecutionAuthority: FORBIDDEN

## Purpose

Promote a defect repeated in MV-1, MV-2, and EV-1 into the earliest applicable
dispatch gate: reject a pinned pre-closure command that reuses a stale dispatch
base with `HEAD`. Runtime enforcement already exists; L1 prevents the bad
instruction before it reaches the worker.

## Operator Authorization And Role Split

The operator instructed the orchestrator/reviewer to continue after EV-1
closed. The repeated finding passes seriousness, source, non-duplication, and
cost gates for one bounded governance-learning task. The worker leaves all changes unstaged and uncommitted; the
reviewer independently tests, repairs if bounded, commits accepted material,
and decides whether the evidence changes any later value gate.

## Baseline Decision / Proposed Tranche

| Field | Decision |
| --- | --- |
| Candidate | EACQ-FV-L1 pre-closure base range dispatch guard |
| Quality-first action | PROMOTE_REPEATED_FINDING_TO_EARLY_GATE |
| Source-backed defect | Three consecutive worker returns show the pinned dispatch-base-to-HEAD pre-closure command failing the existing mixed-range preflight. |
| Owner disposition | ENRICH_EXISTING dispatch-quality checker; preserve autorun as runtime owner. |
| Cost boundary | One existing checker module, one new focused test, one worker return; local only; zero provider/network quota. |
| Successor authority | Independent review only; MV-3 and UAA remain parked. |

## Acceptance Criteria

1. Dispatch-ready work orders reject literal or symbolic dispatch-base reuse in
   executable pre-closure commands whose head is `HEAD`.
2. Pre-implementation, distinct-material-base, prose-only, and absent-command
   cases remain accepted.
3. Runtime autorun behavior and governed standards are unchanged.
4. The exact three-path no-commit manifest and applicable guards pass.

## Verification Evidence

Dispatch verification requires schema-valid capsule JSON, clean work-order and
trace guards, exact three-artifact dispatch
manifest, and the full pre-dispatch autorun bundle. Worker and reviewer proof
is recomputed later and cannot be substituted by this baseline evidence.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| stale dispatch base is not closure proof | governed rule | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | base-anchor lifecycle | `dispatchBaseHead`; `closureBaseHead` | work-order template | ACCEPT |
| mixed committed ranges must split | governed rule | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | gotcha 12 | range-shape guidance | literal-format owner | ACCEPT |
| runtime owner already rejects mixed ranges | current source fact | `governance/compat/run_agent_autorun_workflow_gate.py` | committed-range shape preflight | pre-closure range | autorun owner | ACCEPT |
| first occurrence | execution evidence | `docs/reviews/CVF_EACQ_FV_MV1_CONDITIONAL_REOPEN_INDEX_ENFORCEMENT_WORKER_RETURN_2026-08-27.md` | learning disposition | pinned command | governed review | ACCEPT |
| second occurrence | execution evidence | `docs/reviews/CVF_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_WORKER_RETURN_2026-08-27.md` | Finding 4 | pinned command | governed review | ACCEPT |
| third occurrence | execution evidence | `docs/reviews/CVF_EACQ_FV_EV1_CAPSULE_ENHANCED_OWNER_MAP_EVIDENCE_WORKER_RETURN_2026-08-28.md` | Finding 4 | pinned command | governed review | ACCEPT |

## Scaffold Provenance Block

| Field | Evidence |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id EACQ_FV_L1_PRECLOSURE_BASE_RANGE_DISPATCH_GUARD --title "EACQ-FV L1 Pre-Closure Base Range Dispatch Guard" --date 2026-08-28 --base 3a7d210be --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | protected-governance-path plus WORKER_MUST_NOT_COMMIT profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added value-gate evidence, exact protected owner, safe command contract, focused cases, and capsule binding. |
| checkerReadAheadConfirmation | Dispatch-quality, envelope, checker-read-ahead, and operation-trace checker sources were read. |
| docOnlyNewFields | N/A with reason: no new runtime field is introduced by the baseline. |
| claimBoundary | Dispatch authoring provenance only. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order dispatch quality guard hardening`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

The real resolver command used governance/compat scope, `MEDIUM` risk, returned zero items,
and was not truncated.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_range.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_python_automation_size.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `providerExecutionAuthority: FORBIDDEN`; `Dispatch Prompt Envelope`; trace table field labels |
| gateRunPurpose | Confirm required dispatch shapes before materialization. |
| claimBoundary | Read-ahead is preparation evidence, not implementation proof. |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | internal orchestrator/dispatcher/reviewer |
| Provider or surface | local private-provenance repository |
| Session or invocation | EACQ-FV-L1 dispatch, 2026-08-28 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | governed reads, `rg`, Git, scaffold helper, ADIF resolver, `apply_patch` |
| Target paths | this baseline, paired work order, paired task capsule |
| Allowed scope source | operator continuation plus EV-1 repeated-finding value gate |
| Before status evidence | clean worktree at dispatch base head |
| After status evidence | three-path dispatch packet only; implementation absent |
| Diff evidence | exact dispatch-author manifest before commit |
| Approval boundary | L1 dispatch only; MV-3 and UAA parked |
| Claim boundary | no implementation, causal uplift, provider, public, push, or deployment claim |
| Agent type | orchestrator/dispatcher/reviewer |
| Invocation ID | `eacq-fv-l1-dispatch-2026-08-28` |
| Expected manifest | this baseline; paired work order; paired capsule |
| Actual changed set | this baseline; paired work order; paired capsule |
| Manifest delta | MATCH |
| Deletion or rename disposition | NONE |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | L1 dispatch baseline only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no runtime receipt is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | local worker/reviewer commands only |
| interceptionBoundary | no direct IDE, shell, Git, filesystem, or provider interception claim |
| claimLanguage | dispatch baseline and early document validation only |
| forbiddenExpansion | runtime wrapper, provider/live, public-sync, queue/daemon, watcher, and universal control remain forbidden |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This baseline opens one private, local, no-commit governance-learning task.
It does not prove quality improvement or authorize MV-3, UAA, provider access,
external packet mutation, public sync, push, deployment, or production use.
