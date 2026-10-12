# CVF GC-018 Baseline - NCR History Recovery

Memory class: governed-dispatch-baseline
docType: baseline
Status: CLOSED_PASS_BOUNDED
Date: 2026-10-12
Batch ID: CVF-NCR-HISTORY-RECOVERY-20261012
Dispatch base head: 58efa8c43b70ace270dcb10ab03ecc92319f575b
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN

## Purpose

Make the existing saved-result journey usable: History click must reopen the selected completed result after persistence/reload, independent of ambient currentExecution. User can review, copy/download and start a bound follow-up without rerunning the saved job. Deliver existing Home/History code and meaningful offline composition regressions, preserving accepted continuation and fresh-run behavior.

Paired work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HISTORY_RECOVERY_2026-10-12.md`.

## Scope / Target / Owner Boundary

Exact five worker paths and Local release/review ownership are in the paired order. Store/type/receipt/ResultViewer/HistoryList/ProcessingScreen/wizards/routes/dependencies/continuity are read-only to worker. Requested Sonnet 5.5 high is assignment metadata; no worker launches during authoring.

## Source / Predecessor Evidence

Prior Home binding and ProcessingScreen closures remain bounded acceptance, with their disclosed procedure limits. Current named sources and actual History/Home/store probe are pinned in `docs/reviews/evidence/ncr-history-recovery-dispatch-20261012.json`. No prior implementation reopened and no broad duplicate suite.

## Decision / Proposed Tranche

Selected: History -> explicit saved-result identity -> existing Home/ResultViewer -> review/export/follow-up. Actual page/store probe at 58efa8c43b70ace270dcb10ab03ecc92319f575b has one accepted-continue positive PASS and two desired History-click assertions FAIL (accepted and unreviewed completed A both return to browse). docs/reviews/evidence/ncr-history-recovery-dispatch-20261012.json retains first configuration/mock harness failures separately. This is a concrete NCR R1 recovery/output-use contribution; full offline job journey and R3/R4 exits remain open. Do not extend into dormant hooks, durable cancellation/restart, global pin gates, provider/media/scoring or parked projects.

## Design Control Gate

Explicit result query selected-run restoration is distinct from accepted-only continue. Two existing consumer edits and actual offline composition proof; no new state owner, full-receipt invention, provider/runtime or whole NCR exit. The source-derived conditions and observable acceptance are supplied by orchestrator in the paired order.

## Evidence / Verification

One source positive PASS/two desired failures retained, first harness configuration/mock failures separate. Worker independently demonstrates red-green actual pages/real ResultViewer copy and Markdown output, persisted cold start, invalid query/identity/review/follow-up controls. Consume existing focused evidence; Local distinct bounded semantic challenge later. Customer Care learning informs proportional fixture/publication/claim-layer preparation, no new gate.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| RUNTIME_BEHAVIOR: History selects then pushes /home without selected ID | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/history/page.tsx` | onSelect inside HistoryPage | HistoryPage | existing UI consumer | ACCEPT |
| RUNTIME_BEHAVIOR: Home starts browse and restores only continue | `docs/reviews/evidence/ncr-history-recovery-local-20261012.json` | canonicalSourceVerificationWrapper; execution preimage sourcePinsVerifiedAgainstExecutionBase and originalWorkerArtifacts | HomePage | existing UI consumer | ACCEPT |
| RUNTIME_BEHAVIOR: persist includes execution state | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/store.ts` | persist options and execution actions | useExecutionStore | existing UI consumer | ACCEPT |
| RUNTIME_BEHAVIOR: History row triggers selection | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HistoryList.tsx` | row click and Continue button | HistoryList | existing UI consumer | ACCEPT |
| RUNTIME_BEHAVIOR: Markdown/copy use execution/output props | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ResultViewer.tsx` | props and copy/download handlers | ResultViewer | existing UI consumer | ACCEPT |
| EXISTS: actual one positive and two expected-result failures | `docs/reviews/evidence/ncr-history-recovery-dispatch-20261012.json` | reproduction | reproduction | Local UI source probe | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | released for bounded worker execution; WORKER_MUST_NOT_COMMIT; INTERNAL_AGENT; REQUIRED_FIELDS; TRACE_REQUIRED_LABELS; SECTION_GROUPS; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | confirmation/evidence of selected packet structure; not a dispatch or implementation proof |
| claimBoundary | targeted current checker constants/required sections and ready-state predicates read; not an all-lines reading claim |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-HISTORY-RECOVERY-20261012 --title "NCR History Recovery" --date 2026-10-12 --base 58efa8c43b70ace270dcb10ab03ecc92319f575b --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_COMPLETION_2026-10-12.md --include-worker-return-skeleton --no-evidence-readiness-applicable --scec-problem-key ncr-history-recovery --scec-successor-scope NO_SUCCESSOR --stdout |
| generatedProfile | web-ui-dashboard; internal no-commit |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: selected Home/History result-use outcome, exact five worker paths, fixed source/acceptance map; initial prior role-contract layout reused, historical closure not copied |
| checkerReadAheadConfirmation | applicable constants/required section, role/shape and source-pin predicates read before declarations |
| docOnlyNewFields | dispatch evidence and scoped result query contract; no new storage schema |
| claimBoundary | packet preparation only; no implementation outcome |

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
| Session or invocation | ncr-history-recovery-dispatch-20261012 |
| Working directory | repo root and existing Web package |
| Command or tool surface | targeted source/probe/checker reads; actual scaffold; packet/projection generation; gates/commits |
| Target paths | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HISTORY_RECOVERY_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_HISTORY_RECOVERY_2026-10-12.md`; `docs/reviews/evidence/ncr-history-recovery-dispatch-20261012.json`; `docs/roadmaps/README.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Allowed scope source | standing continuation/audit-and-choose/useful coding and manually selected Sonnet configuration |
| Before status evidence | clean worktree at HEAD 58efa8c43b70ace270dcb10ab03ecc92319f575b; git status --short (empty); staged empty |
| After status evidence | exact7 material then exact6 dedicated release continuity |
| Diff evidence | git diff --check; exact material/continuity source manifests |
| Approval boundary | packet authoring/release only; no worker launched, push or provider effect |
| Claim boundary | source/UI contradiction and ready packet, not repaired product |
| Agent type | INTERNAL_AGENT Local orchestrator |
| Invocation ID | ncr-history-recovery-dispatch-20261012 |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HISTORY_RECOVERY_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_HISTORY_RECOVERY_2026-10-12.md`; `docs/reviews/evidence/ncr-history-recovery-dispatch-20261012.json`; `docs/roadmaps/README.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HISTORY_RECOVERY_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_HISTORY_RECOVERY_2026-10-12.md`; `docs/reviews/evidence/ncr-history-recovery-dispatch-20261012.json`; `docs/roadmaps/README.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Manifest delta | MATCH required; no product edit in dispatch batch |
| Deletion or rename disposition | N/A with reason: none |

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST
Atomicity reason: dispatch packet and raw currentAuthority projections must be committed together; subsequent exact6 continuity binds real material SHA/batch.
Rollback boundary: exact seven material paths below, with no product source edits.
Exact changed manifest:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HISTORY_RECOVERY_2026-10-12.md`
- `docs/baselines/CVF_GC018_NCR_HISTORY_RECOVERY_2026-10-12.md`
- `docs/reviews/evidence/ncr-history-recovery-dispatch-20261012.json`
- `docs/roadmaps/README.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Expected Artifact Existence: baseline/order/dispatch proof are created by Local before commit; existing index/projection files are resolved from tracked source. No worker result or fabricated completion is included.

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
Rollback boundary: exact dispatch material and continuity; preserve17 historical worker rows and prior accepted closures.

## Epistemic Process Block

Expected Result / Prediction: explicit selected ID lets the existing saved result be reopened without execution.
Evidence Comparison: accepted continue control passes; actual History click fails to render saved A in both completed review states. First harness failures are not product evidence.
Contradiction Or Gap Disposition: sender does not carry ID and receiver does not restore basic viewing; scoped contract fixed before worker dispatch.
Claim Update: meaningful source/UI gap selected; repaired composition/export outcome not yet proven.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: private packet only, no public-sync or push grant.

## Claim Boundary

Source-selected offline maintenance and ready packet only; no full provider/governance, backend recovery, whole roadmap or production claim.

## Local Closure Disposition - 2026-10-12

Technical acceptance CLOSED_PASS_BOUNDED after one Local query-presence repair. `docs/reviews/CVF_NCR_HISTORY_RECOVERY_COMPLETION_2026-10-12.md` / `docs/reviews/evidence/ncr-history-recovery-local-20261012.json` (sha256:7450ea01bcb5ebf2a470491b126ad3feec30068159f16300b28fc17177e074a1); original worker return/proof unchanged. Continue completed guard retained by Local clarification: valid accepted completed continue remains supported; noncompleted accepted record is rejected. Explicit empty continue governs rather than falling through; empty result clears prior output. Original source pins are execution preimage at eb50152fae407533784f160a06d2c1faea683478, not a new dispatch pin or authority to run again. No worker restart, provider, public or push effect. Preparation limits and first failures retained.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HISTORY_RECOVERY_2026-10-12.md` | CLOSED_PASS_BOUNDED; useful selected recovery slice | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_NCR_HISTORY_RECOVERY_COMPLETION_2026-10-12.md` | original4 PASS/4 FAIL then repaired8/8; worker originals retained | PASS |
| Roadmap state | `docs/roadmaps/README.md` | finite History slice accepted; full NCR R1/R3/R4 stays open | PASS |
| Registry JSON | `docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json` |18 reviewed tasks:10 Haiku-family,4 Sonnet,4 Luna | PASS |
| Registry Markdown | `docs/reviews/CVF_WORKER_MODEL_SELECTION_PRELIMINARY_REPORT_2026-10-10.md` | current18, old dated counts retained | PASS |
| External evidence digest | `docs/reviews/evidence/ncr-history-recovery-local-20261012.json` | sha256:7450ea01bcb5ebf2a470491b126ad3feec30068159f16300b28fc17177e074a1; internal distinct Local proof | PASS |
| System loop interlock | parked checkpoints | no new loop or automatic successor | N/A with reason: bounded product maintenance |
| Session continuity | six current continuity surfaces | closed authority projections plus subsequent exact6 actual-material sync | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Evidence | Status |
|---|---|---|
| REQ-RESTORE | original22 cases consume actual History URL/store; Local empty-id repair and status/precedence controls | PASS |
| REQ-IDENTITY | worker review/follow-up parent/root/thread assertions; Local A export despite B with records unchanged | PASS |
| REQ-EXPORT | worker real clipboard/Markdown/pack bytes; independent poisoned snapshot excluded from A clipboard; fetch not called | PASS |
| REQ-RETURN | exact5 submitted paths; pins/logs/final gate verified; original metadata retained and Local repairs separate | PASS bounded; preparation limits retained |
