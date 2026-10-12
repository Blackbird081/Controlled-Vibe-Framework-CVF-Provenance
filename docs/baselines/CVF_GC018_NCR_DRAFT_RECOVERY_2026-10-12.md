# CVF GC-018 Baseline - NCR Draft Recovery

Memory class: governed-dispatch-baseline
docType: baseline
Status: DISPATCH_READY
Date: 2026-10-12
Batch ID: CVF-NCR-DRAFT-RECOVERY-20261012
Dispatch base head: 1d8092788a1e515217ee001d267fe4b1d2939ec9
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN

## Purpose

Make the existing Home attempt recoverable without retyping: stop processing or leave its failure screen for the exact editable draft; retry/reject returns filled inputs; an explicit resubmit creates a distinct attempt while saved A and unrelated B stay intact. This finite client-only recovery slice reuses existing store/types/components.

Paired work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_DRAFT_RECOVERY_2026-10-12.md`.

## Scope / Target / Owner Boundary

Exact five worker paths/ownership are in the paired order. Existing store/types/processing/history/result/export/routes/wizards/provider/dependencies/continuity stay read-only to worker. Latest selected Sonnet 5.5 high is assignment metadata; no worker auto-start.

## Source / Predecessor Evidence

History recovery completion `docs/reviews/CVF_NCR_HISTORY_RECOVERY_COMPLETION_2026-10-12.md` remains accepted within disclosed scope. Current named sources and actual Home/form/store probe are pinned in `docs/reviews/evidence/ncr-draft-recovery-dispatch-20261012.json`. Consume accepted prior processing/result evidence; no broad duplicate suite.

## Decision / Proposed Tranche

Selected Home processing/result -> editable draft -> explicit distinct resubmit. Actual Home/DynamicForm/store probe at 1d8092788a1e515217ee001d267fe4b1d2939ec9: one fresh-submit/selected-completion control PASS, four desired stop/status/draft/retry/identity assertions FAIL. Evidence `docs/reviews/evidence/ncr-draft-recovery-dispatch-20261012.json` retains the zero-test mock-hoisting harness failure separately. This is a material NCR Current Delivery Checkpoint recovery gap; History viewing/export closure remains accepted. No full job/R1/R3/R4 exit, backend cancellation/restart, global gate or parked project.

## Design Control Gate

Existing failed means unsuccessful local attempt, not confirmed backend stop. Selected processing/failure-exit -> exact draft -> explicit unique new submit. Optional initial values preserve other form callers/defaults/validation. No new status/schema/durable writer, receipt manufacture or complete R1/R3/R4 exit.

## Evidence / Verification

1 positive/4 desired failures retained; first zero-test mock-hoisting harness error is Local. Worker independently composes actual Home/form/processing cancellation, storage, draft edit and distinct same-clock submit; Local bounded independent challenge later. Required source scopes/derived observable conditions are authored by orchestrator before dispatch, no quiz/gate additions.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| RUNTIME_BEHAVIOR: cancel calls handleBack without failed bookkeeping | `docs/reviews/evidence/ncr-draft-recovery-dispatch-20261012.json` | sourceFacts and sourcePins | sourceFacts | named existing consumer; canonical source path/raw/HEAD binding recorded in dispatch proof | ACCEPT |
| RUNTIME_BEHAVIOR: useForm has no initial values | `docs/reviews/evidence/ncr-draft-recovery-dispatch-20261012.json` | sourceFacts and sourcePins | sourceFacts | named existing consumer; canonical source path/raw/HEAD binding recorded in dispatch proof | ACCEPT |
| RUNTIME_BEHAVIOR: millisecond-only Home form/demo IDs | `docs/reviews/evidence/ncr-draft-recovery-dispatch-20261012.json` | sourceFacts and sourcePins | sourceFacts | named existing consumer; canonical source path/raw/HEAD binding recorded in dispatch proof | ACCEPT |
| RUNTIME_BEHAVIOR: store persists all execution state, update by ID | `docs/reviews/evidence/ncr-draft-recovery-dispatch-20261012.json` | sourceFacts and sourcePins | sourceFacts | named existing consumer; canonical source path/raw/HEAD binding recorded in dispatch proof | ACCEPT |
| RUNTIME_BEHAVIOR: ProcessingScreen only best-effort client stop; no parent error callback | `docs/reviews/evidence/ncr-draft-recovery-dispatch-20261012.json` | sourceFacts and sourcePins | sourceFacts | named existing consumer; canonical source path/raw/HEAD binding recorded in dispatch proof | ACCEPT |
| EXISTS: actual one positive and four desired failures | `docs/reviews/evidence/ncr-draft-recovery-dispatch-20261012.json` | reproduction | reproduction | Local bounded source UI probe | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | DISPATCH_READY; WORKER_MUST_NOT_COMMIT; INTERNAL_AGENT; REQUIRED_FIELDS; TRACE_REQUIRED_LABELS; SECTION_GROUPS; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | confirmation/evidence of selected packet structure; not a dispatch or implementation proof |
| claimBoundary | targeted current checker constants/required sections and ready-state predicates read; not an all-lines reading claim |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-DRAFT-RECOVERY-20261012 --title "NCR Draft Recovery" --date 2026-10-12 --base 1d8092788a1e515217ee001d267fe4b1d2939ec9 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_NCR_HISTORY_RECOVERY_COMPLETION_2026-10-12.md --include-worker-return-skeleton --no-evidence-readiness-applicable --scec-problem-key ncr-draft-recovery --scec-successor-scope NO_SUCCESSOR --stdout |
| generatedProfile | web-ui-dashboard; internal no-commit |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: previous ready role-contract layout; new finite stop/draft/new-ID conditions, exact5 paths and source map; no copied closure |
| checkerReadAheadConfirmation | dispatch source/core, acceptance ledger, core-protection constants plus prior verified role/shape owner bindings; no claim full checker bodies |
| docOnlyNewFields | dispatch evidence and client recovery contract; no schema/status |
| claimBoundary | packet preparation, implementation pending |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "work-order" --role dispatcher --lifecycle-phase pre-dispatch`
Returned defects: NONE_RETURNED
Actual result: 0 candidates, 0 returned, not truncated. This query does not prove absence of all applicable defects; refresh the final task class at release if classification changes.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher |
| Provider or surface | private Codex IDE shared workspace |
| Session or invocation | ncr-draft-recovery-dispatch-20261012 |
| Working directory | repo root and installed Web package |
| Command or tool surface | named source/probe/scaffold/ADIF/checker reads; packet generation; release gates/commits |
| Target paths | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_DRAFT_RECOVERY_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_DRAFT_RECOVERY_2026-10-12.md`; `docs/reviews/evidence/ncr-draft-recovery-dispatch-20261012.json`; `docs/roadmaps/README.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Allowed scope source | standing continue/audit-and-choose/useful coding with manually selected Sonnet worker |
| Before status evidence | clean worktree at HEAD 1d8092788a1e515217ee001d267fe4b1d2939ec9; git status --short empty; staged empty |
| After status evidence | exact7 material then exact6 continuity |
| Diff evidence | git diff --check; exact manifests |
| Approval boundary | packet/release only; worker/provider/push not started |
| Claim boundary | synthetic source gap and packet, fixed product pending |
| Agent type | INTERNAL_AGENT Local dispatcher |
| Invocation ID | ncr-draft-recovery-dispatch-20261012 |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_DRAFT_RECOVERY_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_DRAFT_RECOVERY_2026-10-12.md`; `docs/reviews/evidence/ncr-draft-recovery-dispatch-20261012.json`; `docs/roadmaps/README.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_DRAFT_RECOVERY_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_DRAFT_RECOVERY_2026-10-12.md`; `docs/reviews/evidence/ncr-draft-recovery-dispatch-20261012.json`; `docs/roadmaps/README.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Manifest delta | MATCH required |
| Deletion or rename disposition | N/A with reason: none |

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST
Atomicity reason: paired dispatch and currentAuthority raw-hash projections commit together; dedicated exact6 continuity binds material SHA/batch.
Rollback boundary: exact seven material paths, no product edits.
Exact changed manifest:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_DRAFT_RECOVERY_2026-10-12.md`
- `docs/baselines/CVF_GC018_NCR_DRAFT_RECOVERY_2026-10-12.md`
- `docs/reviews/evidence/ncr-draft-recovery-dispatch-20261012.json`
- `docs/roadmaps/README.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Expected Artifact Existence: Local creates baseline/order/dispatch proof before commit; index/projections existing. No worker output or fabricated completion.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: exact currentAuthority projections in material and subsequent six-path continuity; no checker/hook/guard edit.
Protected paths:

- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Operator authorization: standing continuation, audit-and-choose and manually started Sonnet 5.5 high useful coding; Local owns packet/continuity. No push grant.
Rollback boundary: exact dispatch material and continuity; preserve18 historical worker rows and prior accepted closures.

## Epistemic Process Block

Expected Result / Prediction: selected cancel/retry should return an editable draft, preserve correct unsuccessful state and allow a distinct new submit.
Evidence Comparison:1 fresh-submit/completion control PASS/4 desired assertions FAIL; initial zero-test mock-hoisting error separate.
Contradiction Or Gap Disposition: missing local stop bookkeeping, absent form initial values and millisecond-only IDs.
Claim Update: bounded useful client recovery selected; fixed/full user journey unproven.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: private dispatch only, no public-sync or push grant.

## Claim Boundary

Source-selected client recovery and packet only, no fixed/full journey, backend cancellation/provider/governance/production or ranking claim.
