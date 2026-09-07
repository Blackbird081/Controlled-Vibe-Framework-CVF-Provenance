# CVF GC-018 Baseline - DARA T2 Architecture Readiness Admission Implementation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: DARA-T2-IMPLEMENTATION

Dispatch base head: e1a5e3abc45f836c2b35b3580b42e5199c2b18c8

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator; dispatch author and reviewer: Codex role; worker target: delegated implementation worker.

providerExecutionAuthority: FORBIDDEN

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id DARA-T2 --title "DARA T2 Architecture Readiness Admission Foundation Implementation" --date 2026-09-06 --base e1a5e3abc45f836c2b35b3580b42e5199c2b18c8 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 2 --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with frozen T1 dependencies, exact owner manifest, MFRP boundary, and evidence-measurement contract |
| checkerReadAheadConfirmation | dispatch, route, convergence, cost, source, protected-path, return, trace, and public guards |
| docOnlyNewFields | evidence measurement narrative only; no new machine owner |
| claimBoundary | scaffold provenance only; no implementation or readiness proof |

## Purpose

Authorize the bounded DARA-T2 implementation that turns the accepted
architecture-readiness design into existing work-order, scaffold, worker-return,
and dispatch-quality owner surfaces. The worker must also return real execution
and defect-attribution evidence so CVF can measure dispatch quality without
duplicating worker work during review.

## Decision / Baseline / Proposed Tranche

DARA-T1 is accepted bounded at material commit
`e7c559d5f5396b86cdedbc7ab4f4f35a5745d3d2`. The accepted design freezes the
schema, closed-chain invariants, immutable digest preimage, role attribution,
quota admission ordering, MFRP composition boundary, ten implementation owner
paths, and sixteen hostile-test families. T2 may implement only that frozen
delta and its one worker return.

## Authorized Scope

- Implement `cvf.dara.architectureBindingMatrix.v1` on the ten exact existing
  owner paths in the paired work order.
- Add fail-closed applicability, identity/digest, review binding, quota, echo,
  and fault-attribution validation.
- Keep both worker-return generator routes aligned.
- Add focused positive and hostile regression tests for all sixteen T1 test
  families.
- Record first-run/final-run evidence, defect attribution, effort/friction, and
  external-invocation accounting in the exact worker return.
- Compose evidence through existing MFRP P4-C1 observation fields only.

## Forbidden Scope

No MFRP receipt-v3, collector, readout, eligibility, checkpoint, safety marker,
runtime/provider/live, source package, public-sync, session-state, active-handoff,
roadmap, ADIF, WP-ARCH-003, deployment, credential, commit, or push change is
authorized. No new DARA collector, receipt, readout, reviewer packet, evidence
ledger, checkpoint, runtime interceptor, or parallel owner may be created.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| DARA-T1 design | `docs/assessments/CVF_DARA_T1_ARCHITECTURE_READINESS_CONTRACT_DESIGN_2026-09-06.md`; SHA-256 `9E43B223F0D0BFA3DC4CC7A3806F5CFACA0E8096E5D548618F03CD5EEC2CEC32` | frozen schema, owner map, and hostile tests exist | ACCEPT |
| DARA-T1 design review | `docs/reviews/CVF_DARA_T1_ARCHITECTURE_READINESS_CONTRACT_DESIGN_REVIEW_2026-09-06.md`; material commit `e7c559d5f5396b86cdedbc7ab4f4f35a5745d3d2` | bounded T2 packet authoring is released | ACCEPT |
| DARA roadmap | `docs/roadmaps/CVF_DISPATCHER_ARCHITECTURE_READINESS_AND_QUOTA_ADMISSION_ROADMAP_2026-09-06.md`, Work Plan | T2 is the next allowed foundation tranche | ACCEPT |
| MFRP P4-C1 ownership | `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION_2026-09-02.md`; activation `b9bdba712` | DARA composes without a second collector | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024,
ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json --max-results 50` |
| Returned defect count | 22 |
| Disclosed defectIds | all IDs listed above |
| Dispatch impact | exact owner paths; verified command signatures; checker read-ahead; no-commit split; causal defect counters; no completeness overclaim; MFRP reuse |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_absorption_blindspot_control_presence.py` |
| literalTokensReviewed | dispatch status, prompt-envelope fields, convergence scalars, route JSON, source rows, protected-path authorization, return profile, trace labels, private export disposition |
| gateRunPurpose | confirm the source-verified dispatch packet rather than discover required prose |
| claimBoundary | checker conformance proves dispatch shape only; it does not prove implementation correctness |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| accepted T2 change map | design authority | `docs/assessments/CVF_DARA_T1_ARCHITECTURE_READINESS_CONTRACT_DESIGN_2026-09-06.md` | DARA-T2 Exact Owner Change Map | `cvf.dara.architectureBindingMatrix.v1` | DARA-T1 contract | ACCEPT |
| bounded T2 release | review authority | `docs/reviews/CVF_DARA_T1_ARCHITECTURE_READINESS_CONTRACT_DESIGN_REVIEW_2026-09-06.md` | Decision / Disposition | `DESIGN_ACCEPTED_BOUNDED` | T1 reviewer | ACCEPT |
| existing dispatch validator owner | implementation source | `governance/compat/check_work_order_dispatch_quality.py` | module entrypoint | `main` | dispatch-quality gate | ACCEPT |
| existing range entrypoint | implementation source | `governance/compat/check_work_order_dispatch_quality_range.py` | work-order validator | `_validate_work_order` | range gate | ACCEPT |
| existing source verifier | implementation source | `governance/compat/check_work_order_dispatch_quality_source.py` | accepted-row validator | `_validate_accepted_source_rows` | source-fidelity gate | ACCEPT |
| existing dispatch scaffold | implementation source | `governance/compat/build_dispatch_packet_scaffold.py` | parser and renderers | `main` | dispatch scaffold | ACCEPT |
| existing return scaffold owners | implementation source | `governance/compat/build_worker_return_skeleton_scaffold.py` | P4 renderer | `render_p4_observation_block` | worker-return scaffold | ACCEPT |
| existing standalone return scaffold | implementation source | `governance/compat/run_worker_return_scaffold.py` | module entrypoint | `main` | worker-return scaffold | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| baseline, work order, and return target paths | exact `Test-Path -LiteralPath` before authoring returned false | ACCEPT_NO_COLLISION |
| DARA-T2 implementation token | `rg -n` over `docs` and `CVF_SESSION` returned no conflicting artifact | ACCEPT_NO_COLLISION |
| parallel collector or receipt | explicitly forbidden; existing P4-C1 owner retained | REJECT_PARALLEL_OWNER |
| extra implementation path | any path outside the exact manifest blocks return readiness | REJECT_SCOPE_EXPANSION |

## Evidence Measurement Contract

This tranche is a real measurement sample, not a new telemetry subsystem. The
worker return must state external invocation count before and after, observable
token/quota and elapsed time or an exact unavailability reason, first-run and
final-run results, gate-failure ledger, work-order ambiguity count, questions
needed, and the six DARA fault counters with evidence IDs. The reviewer consumes
that evidence and performs targeted checks only; reviewer implementation repair
and broad duplicate reruns are outside this baseline.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: implement the accepted DARA-T2 contract on
the ten existing protected owners listed in the paired work order.

Protected paths:

- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`
- `governance/compat/build_worker_return_skeleton_scaffold.py`
- `governance/compat/run_worker_return_scaffold.py`
- `governance/compat/test_run_worker_return_scaffold.py`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/check_work_order_dispatch_quality_range.py`
- `governance/compat/check_work_order_dispatch_quality_source.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`

Operator authorization: the operator directed foundation improvement first and
then explicitly delegated implementation to an external worker while retaining
Codex as reviewer, on 2026-09-06.

Rollback boundary: revert only the DARA-T2 material commit if rejected; preserve
T1 design/review, MFRP P4-C1, parked WP-ARCH-003 files, and continuity history.

Not authorized: no MFRP collector/receipt/readout modification, second evidence
system, session mutation, provider/live behavior, public sync, or worker commit.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation implementation dispatch; no public-sync authority.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatch author preparing evidence for later reviewer-only evaluation |
| Provider or surface | local private CVF workspace |
| Session or invocation | DARA-T2 implementation dispatch, 2026-09-06 |
| Working directory | repository root |
| Command or tool surface | startup reads, design/review reads, ADIF resolver, scaffold preview, exact path checks, apply_patch, pre-dispatch gate |
| Target paths | this baseline and paired work order |
| Allowed scope source | operator instruction to prompt the external worker and keep Codex as reviewer |
| Before status evidence | clean worktree for the DARA dispatch range at gate/commit time after exact isolation of two unrelated parked untracked files; HEAD `e1a5e3abc45f836c2b35b3580b42e5199c2b18c8` |
| After status evidence | exactly two dispatch artifacts added; worker implementation not executed |
| Diff evidence | `git diff --name-status`; `git status --short` |
| Approval boundary | DARA-T2 dispatch authoring only |
| Claim boundary | no implementation, reviewer acceptance, runtime/provider/live/public effect |
| Agent type | dispatcher for packet creation; future role reviewer |
| Invocation ID | `dara-t2-implementation-dispatch-2026-09-06` |
| Expected manifest | this baseline and paired work order |
| Actual changed set | same two paths, excluding pre-existing parked untracked files |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes only the exact DARA-T2 foundation implementation and
worker-return evidence contract. It does not claim the control is implemented,
effective, independently reviewed, integrated into MFRP runtime, or ready for
public or production use.
