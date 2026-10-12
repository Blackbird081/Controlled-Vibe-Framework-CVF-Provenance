# CVF GC-018 Baseline - NCR Draft Export Composition

Memory class: governed-dispatch-baseline
docType: baseline
Status: READY
Date: 2026-10-12
Batch ID: CVF-NCR-DRAFT-EXPORT-20261012
Dispatch base head: 6c0b0d20922593283c067a638ea0a360e1a2372c
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN

## Purpose

Prove the missing visible Home -> restored editable draft -> Vietnamese idea confirmation -> current English Working Brief preview/copy/download/handoff composition. The user can recover and reuse the idea without retyping. This assignment implements bounded offline UI regressions, not product-source changes or AI governance proof.

## Scope / Target / Owner Boundary

Exactly three new files: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/draft-export.test.tsx`, `docs/reviews/evidence/ncr-draft-export-worker-20261012.json`, `docs/reviews/CVF_NCR_DRAFT_EXPORT_WORKER_RETURN_2026-10-12.md`. All production source, existing tests, baselines/orders, roadmap/index, collection and continuity are read-only to worker. Ignored runtime `.cvf/runtime/ncr-draft-export-worker-20261012/` may contain logs only. One manual invocation,60min total including startup/reads/tests/gates; new test<=600 lines, return<=450 lines/64000 bytes, proof<=128000 bytes. No foreseeable split under these budgets. No credentials, dependency installation, local server/browser, network effects, source edits, subagents or new helper/service/schema. A necessary extra file or production repair requires one consolidated blocked return.

## Design Control Gate

Exercise actual Home, DynamicForm and SpecExport at the decisive controls, existing persisted store and synthetic A/B identities. Accepted stop/retry primitives may be invoked through their existing callbacks; any unrelated ProcessingScreen/ResultViewer/browse leaf stubs must be disclosed. Do not stub SpecExport, DynamicForm, source brief builders or the handoff event. Keep provider-denial setup enabled. This is UI/source-binding proof only; no policy correctness, live provider, receiving-agent execution, real browser/Next routing, backend abort, durable restart or complete NCR claim.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: recovery test hides SpecExport | `docs/reviews/evidence/ncr-draft-export-dispatch-20261012.json` | sourceFacts / sourcePins | sourceFacts | pinned actual source inspection, not runtime acceptance | ACCEPT |
| EXISTS: visible form mounts exporter with current values | `docs/reviews/evidence/ncr-draft-export-dispatch-20261012.json` | sourceFacts / sourcePins | sourceFacts | actual Home/DynamicForm render and handoff callback | ACCEPT |
| EXISTS: standalone current export/revision controls | `docs/reviews/evidence/ncr-draft-export-dispatch-20261012.json` | sourceFacts / sourcePins | sourceFacts | SpecExport.test.tsx selected assertions; composed outcome still unproved | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | previous bounded dispatch; WORKER_MUST_NOT_COMMIT; INTERNAL_AGENT; REQUIRED_FIELDS; TRACE_REQUIRED_LABELS; SECTION_GROUPS; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | confirmation/evidence of selected packet structure; not a dispatch or implementation proof |
| claimBoundary | targeted current checker constants/required sections and ready-state predicates read; not an all-lines reading claim |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-DRAFT-EXPORT-20261012 --title "NCR Draft Export Composition" --date 2026-10-12 --base ae3e9813afc424f3b590ccf91c353aaadc35102b --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_NCR_DRAFT_RECOVERY_COMPLETION_2026-10-12.md --include-worker-return-skeleton --no-evidence-readiness-applicable --scec-problem-key ncr-draft-export-composition --scec-successor-scope NO_SUCCESSOR --stdout |
| generatedProfile | web-ui-dashboard; internal no-commit |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: previous ready role-contract layout; visible restored-draft export/revision conditions, exact3 test/proof/return paths and source map; no copied closure |
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
| Actor | Local orchestrator/dispatcher |
| Provider or surface | private Codex IDE shared workspace |
| Session or invocation | ncr-draft-export-dispatch-20261012 |
| Working directory | repository root |
| Command or tool surface | targeted reads, actual scaffold/ADIF, source pins, packet/gates/commits |
| Target paths | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_DRAFT_EXPORT_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_DRAFT_EXPORT_2026-10-12.md`; `docs/reviews/evidence/ncr-draft-export-dispatch-20261012.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Allowed scope source | explicit operator manual Sonnet worker assignment plus prior local selection |
| Before status evidence | 6c0b0d20922593283c067a638ea0a360e1a2372c; initial material and continuity clean; release FAIL retained in bound-release.log; source pins remain at original inspection commit |
| After status evidence | exact6 release correction then exact6 continuity rebind; worker not started |
| Diff evidence | git diff --check and exact manifests |
| Approval boundary | manual shared-workspace worker, no provider/live/public effects |
| Claim boundary | dispatch and declared source gap only; runtime proof pending |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-draft-export-dispatch-20261012 |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_DRAFT_EXPORT_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_DRAFT_EXPORT_2026-10-12.md`; `docs/reviews/evidence/ncr-draft-export-dispatch-20261012.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_DRAFT_EXPORT_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_DRAFT_EXPORT_2026-10-12.md`; `docs/reviews/evidence/ncr-draft-export-dispatch-20261012.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Manifest delta | MATCH required before commit |
| Deletion or rename disposition | N/A with reason: none |

## Epistemic Process Block

Expected Result / Prediction: accepted recovery and exporter compose through the visible controls with current source/revision and no saved-job contamination.
Evidence Comparison: source inspection exposes an unproved composition because prior recovery hides SpecExport; existing component assertions are consumed. No runtime probe run by dispatcher.
Contradiction Or Gap Disposition: bounded integration coverage gap, not a known product failure.
Claim Update: offline proof task admitted; composed outcome pending worker and distinct Local review.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: private dispatch and offline proof only; no publication grant.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Local dispatch currentAuthority/source regeneration then exact6 dedicated continuity. Worker cannot edit protected paths.
Protected paths:
- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Operator authorization: explicit continue/assign manual Sonnet worker,2026-10-12.
Rollback boundary: exact dispatch material and subsequent continuity; accepted prior worker bytes/closures and19 observations preserved. No checker/hook/guard change.

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST
Atomicity reason: paired baseline/order release reanchor and worker gate command, source evidence and raw authority projections repair orchestrator release; dedicated continuity binds new material SHA.
Rollback boundary: exact6 release correction; prior material/continuity and all failures retained.
Exact changed manifest:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_DRAFT_EXPORT_2026-10-12.md`
- `docs/baselines/CVF_GC018_NCR_DRAFT_EXPORT_2026-10-12.md`
- `docs/reviews/evidence/ncr-draft-export-dispatch-20261012.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Expected Artifact Existence: all six paths already tracked; worker outputs remain absent.

## Release Reanchor

Current dispatch base: 6c0b0d20922593283c067a638ea0a360e1a2372c. Source evidence remains pinned at original selection commit, with current production hashes checked unchanged. Correct worker pre-implementation uses the autorun wrapper current-HEAD default and active work-order binding. Prior release FAIL retained at C:/Users/DELL/AppData/Local/Temp/ncr-draft-export-bound-release.log; no worker effect occurred.
