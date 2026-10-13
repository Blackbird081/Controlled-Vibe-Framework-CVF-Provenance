# CVF GC-018 Baseline - NCR Brief Panel Reopen Continuity

Memory class: governed-dispatch-baseline
docType: baseline
Status: AUTHORIZED_BOUNDED
Date: 2026-10-13
Batch ID: CVF-NCR-BRIEF-REOPEN-20261013
Dispatch base head: 6de61d59ae39885b5e8544677966fae37d047d40
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN

## Purpose

A user who confirms and exports a Working Brief can close and reopen the form panel without losing the same-idea confirmation and generated packet or downloading again. Source edits while closed must invalidate the old confirmation, including A -> B -> A. This fixes panel presentation lifetime only; existing INTAKE handoff, permission owners and execution routes remain intact.

Retention applies only to voluntary close/toggle. Successful Send to Agent must reset/unmount the panel, preserving the existing draft-export send/reopen contract. Parent-owned wrapping of the existing successful send callback is admitted; child APIs and source stay read-only.

## Authority Chain

Operator 2026-10-13: continue CVF, primary worker requested Luna max; use Sol medium if returned quality is inadequate. Local selects one existing-consumer brief panel lifecycle repair from NCR. Paired `docs/baselines/CVF_GC018_NCR_BRIEF_REOPEN_2026-10-13.md` fixes exact4 outputs. Local owns source verification, quality disposition, independent review, commits and continuity. Parked checkpoints retain their authority.

## Scope / Target / Owner Boundary

Exactly4 owned paths: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/DynamicForm.tsx`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/DynamicForm.brief-lifecycle.test.tsx`, `docs/reviews/evidence/ncr-brief-reopen-worker-20261013.json`, `docs/reviews/CVF_NCR_BRIEF_REOPEN_WORKER_RETURN_2026-10-13.md`. DynamicForm <=450lines; new test <=650lines; return <=450lines/64000bytes; proof <=128000bytes. One primary BUILD <=60min including required reads, scaffolding, writes, tests and gates; earlier read-only intake separately timed. Ignored .cvf/runtime/ncr-brief-reopen-worker-20261013 logs and tool-owned autorun receipts allowed. Only voluntary panel lifetime/render visibility and successful existing send reset changes; SpecExport, hooks/helpers, Home, old tests, schema/store, checkers/hooks, continuity and model ledger read-only. No helper/split/dependency or provider/network/browser/server/public/real-data effects. Optional repair requires its own Local-issued bounded packet after quality rejection.

## Design Control Gate

Initial form renders no brief panel and does not eagerly start panel work. Once opened, closing hides the panel from the accessible UI without discarding the same-idea packet. Reopening exposes the current state. Let the existing SpecExport revision owner process source edits while hidden; old confirmation must not revive after A -> B -> A. Form/template unmount still resets session state. No global persistence, new store/service, new permission gate or execution CTA. Decisive DynamicForm and SpecExport must be real in regression observations. Synthetic settings/session, optional review/context leaves and OS download/clipboard adapters may be disclosed fixtures. Assertions are panel visibility, text identity/revision and adapter/callback counts only; no mocked AI governance efficacy, approval/risk/DLP/validation/audit/provider-routing or AI quality claim.

Do not retain confirmation after successful send. DynamicForm owns this reset through its existing onSendToAgent callback; no child API or source change is authorized. Caller failure must not be treated as a successful send. Do not add delivery-receipt or permission claims.

## Conditional Worker Quality Disposition

Local evaluates the first terminal return against every fixed requirement, source/proof identity, scope and mandatory final gates. QUALITY_ACCEPTED requires substantive criteria and usable proof; disclosed historical procedure limits remain separately attributed. QUALITY_REJECTED_WITH_CONSOLIDATED_FINDINGS applies to an unmet required UI behavior, invalid or missing required proof, required gate failure, prohibited mutation/effect, or a preparation omission that makes the return unusable. Preserve first-return bytes and final source/test snapshots before repair; no silent rewriting or cost ranking.

After rejection, Local authors one bounded REWORK packet using the existing convergence/closeability owners and the single consolidated finding digest. Only then release one conditional repair worker with the configured fallback request. Original return/evidence remain immutable; correction evidence and repaired source identities stay distinct. Primary BUILD <=60min, optional repair BUILD <=45min; at most two BUILD assignments, zero nested agents. Root performs review/closure and permitted documentary corrections, not unrecorded fallback implementation. Further dependent scope or exhausted ceiling returns a consolidated blocker. No automatic selector, scheduler or runtime routing is added.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: parent conditional child mount | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/DynamicForm.tsx` | Spec Export Panel | showSpecExport | DynamicForm | ACCEPT |
| EXISTS: child revision and packet owner | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx` | SpecExport | confirmedRevision | SpecExport | ACCEPT |
| EXISTS: named source identities | `docs/reviews/evidence/ncr-brief-reopen-dispatch-20261013.json` | sourcePins | sourcePins | Local raw/Git pins | ACCEPT |

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
| scaffoldHelperCommand | python -B governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-BRIEF-REOPEN-20261013 --title "NCR Brief Panel Reopen Continuity" --date 2026-10-13 --base 6de61d59ae39885b5e8544677966fae37d047d40 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_NCR_OFFLINE_JOURNEY_COMPLETION_2026-10-13.md --include-worker-return-skeleton --no-evidence-readiness-applicable --scec-problem-key ncr-brief-panel-reopen --scec-successor-scope NO_SUCCESSOR --stdout |
| generatedProfile | web-ui-dashboard; internal no-commit |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: accepted role/trace/graph fields reused; new panel-lifetime criteria, exact4 paths, conditional quality boundary and raw archives |
| checkerReadAheadConfirmation | current relevant constants/required fields/ready predicates read; not all checker lines |
| docOnlyNewFields | fixed panel continuity criteria and operator conditional configuration metadata |
| claimBoundary | bounded packet authoring only; no runtime selector |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "work-order" --role dispatcher --lifecycle-phase pre-dispatch`
Returned defects: NONE_RETURNED
Actual result: 0 candidates, 0 returned, not truncated. This query does not prove absence of all applicable defects; refresh the final task class at release if classification changes.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local INTERNAL_AGENT dispatcher |
| Provider or surface | private shared workspace |
| Session or invocation | ncr-brief-reopen-dispatch-20261013 |
| Working directory | repository root and installed Web package |
| Command or tool surface | targeted reads, actual scaffold/ADIF, source pins/raw archive, packet/gates/commit |
| Target paths | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_BRIEF_REOPEN_2026-10-13.md`; `docs/baselines/CVF_GC018_NCR_BRIEF_REOPEN_2026-10-13.md`; `docs/reviews/evidence/ncr-brief-reopen-dispatch-20261013.json`; `.gitattributes`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/roadmaps/archive/CVF_NCR_PRE_BRIEF_REOPEN_2026-10-13.md`; `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V63_PRE_BRIEF_REOPEN_2026-10-13.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Allowed scope source | operator CVF continuation and primary/conditional worker instructions 2026-10-13 |
| Before status evidence | 6de61d59ae39885b5e8544677966fae37d047d40; clean worktree; staged empty |
| After status evidence | exact10 dispatch material then exact6 continuity; primary BUILD pending |
| Diff evidence | git diff --check and exact staged manifest |
| Approval boundary | one primary and at most one separately released conditional repair BUILD; no provider/effects |
| Claim boundary | offline UI presentation lifetime only; no AI governance/full-job/live/public/deploy |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-brief-reopen-dispatch-20261013 |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_BRIEF_REOPEN_2026-10-13.md`; `docs/baselines/CVF_GC018_NCR_BRIEF_REOPEN_2026-10-13.md`; `docs/reviews/evidence/ncr-brief-reopen-dispatch-20261013.json`; `.gitattributes`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/roadmaps/archive/CVF_NCR_PRE_BRIEF_REOPEN_2026-10-13.md`; `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V63_PRE_BRIEF_REOPEN_2026-10-13.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_BRIEF_REOPEN_2026-10-13.md`; `docs/baselines/CVF_GC018_NCR_BRIEF_REOPEN_2026-10-13.md`; `docs/reviews/evidence/ncr-brief-reopen-dispatch-20261013.json`; `.gitattributes`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/roadmaps/archive/CVF_NCR_PRE_BRIEF_REOPEN_2026-10-13.md`; `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V63_PRE_BRIEF_REOPEN_2026-10-13.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Manifest delta | MATCH required before commit |
| Deletion or rename disposition | N/A with reason: raw archive copies and historical owner extraction; no path deletion/rename |

## Epistemic Process Block

Expected Result / Prediction: panel visibility can change without losing same-idea output, while source edits still invalidate revision identity.
Evidence Comparison: parent conditional mounting discards child state; existing child revision tests only rerender a still-mounted child; draft-export integration explicitly requires reset after successful send.
Contradiction Or Gap Disposition: retain existing revision owner and test actual parent-child mounting; do not add governance/execute behavior.
Claim Update: selected bounded repair; original-source and independent acceptance pending.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: private dispatch and offline proof only; no publication grant.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Local dispatch raw authority projection then exact6 continuity. Worker cannot edit protected paths.
Protected paths:
- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Operator authorization: next under standing subagent worker/Local orchestrator-reviewer roles,2026-10-13.
Rollback boundary: exact10 dispatch and exact6 continuity, prior accepted worker/evidence and24 observations retained; no guard/hook changes.

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST
Atomicity reason: paired packet/pins, immutable preimages, roadmap history extraction and raw authority bind one finite dispatch. Dedicated exact6 continuity binds actual material SHA and archives closed handoff history.
Rollback boundary: exact10 dispatch material; prior accepted production/evidence/model observations retained.
Exact changed manifest:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_BRIEF_REOPEN_2026-10-13.md`
- `docs/baselines/CVF_GC018_NCR_BRIEF_REOPEN_2026-10-13.md`
- `docs/reviews/evidence/ncr-brief-reopen-dispatch-20261013.json`
- `.gitattributes`
- `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`
- `docs/roadmaps/archive/CVF_NCR_PRE_BRIEF_REOPEN_2026-10-13.md`
- `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V63_PRE_BRIEF_REOPEN_2026-10-13.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Expected Artifact Existence: packet/dispatch/archives authored before commit; existing material tracked; future worker test/proof/return absent.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/evidence/ncr-brief-reopen-dispatch-20261013.json` |
| Chain map route | Local brief panel continuity repair -> existing component -> independent Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing UI lifecycle/source-fidelity/closure owners |
| Disposition | internal existing product composition proof; no external research |
| Claim boundary | Local private source verification and final decision |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named consumer/test evidence only; no repository/corpus scan.

## Knowledge System Applicability

NOT_APPLICABLE_WITH_REASON: named dashboard/chat source and fixture evidence only; no corpus rescan or semantic knowledge-map/retrieval production.

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: named UI composition proof, no rescan/intake.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | existing DynamicForm/SpecExport; private implementation worker | exact4 paths, only parent panel lifetime; no effects/commit | ten pins and selected gap; independent review pending | N/A with reason: shared private workspace | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | no selected external consumer | no external execution authority | no external route selected | deferred; no adapter selected | DEFERRED_WITH_REASON |

## Claim Boundary

Finite offline/jsdom parent/child brief-panel presentation continuity and source revision identity only. UI fixtures do not prove AI behavior, governance approval/risk/DLP/validation/audit/provider routing, actual browser/OS effects, backend/durable recovery, full job/R3/R4, release/public/deploy or model ranking. Conditional fallback is an operator instruction with Local judgment, not a runtime routing mechanism.

## Evidence

Ten raw/Git source pins and exact raw archive preimages in `docs/reviews/evidence/ncr-brief-reopen-dispatch-20261013.json`. Required source-red and independent acceptance pending.

## Decision / Proposed Tranche

One primary INTERNAL_AGENT worker with exact4 source/test/evidence/return files; conditional repair only after Local quality rejection and its own bounded packet. Paired `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_BRIEF_REOPEN_2026-10-13.md`.24 prior observations retained; no new provider/live/public authority.
