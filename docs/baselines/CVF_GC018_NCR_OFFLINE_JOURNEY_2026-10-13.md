# CVF GC-018 Baseline - NCR Offline UI Journey Composition

Memory class: governed-dispatch-baseline
docType: baseline
Status: CLOSED_PASS_BOUNDED
Date: 2026-10-13
Batch ID: CVF-NCR-OFFLINE-JOURNEY-20261013
Dispatch base head: 4cb80e5ac7f715089df89610ea696647f16e565e
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN

## Purpose

One new offline test joins real Home, DynamicForm, ProcessingScreen, ResultViewer and store through form submission, displayed parent result, follow-up submission and displayed child result. Existing draft-recovery and result-isolation evidence already cover cancel/error/history/export seams separately; do not recreate those tests. Synthetic transport is presentation data, not AI governance proof. No source defect or production repair selected.

## Scope / Target / Owner Boundary

Exactly3 new files: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.journey.test.tsx`, `docs/reviews/evidence/ncr-offline-journey-worker-20261013.json`, `docs/reviews/CVF_NCR_OFFLINE_JOURNEY_WORKER_RETURN_2026-10-13.md`. Test <=700 lines; return <=450 lines/64000 bytes; proof <=128000 bytes. One BUILD invocation <=60 minutes including reads/writes/tests/gates; preceding read-only intake recorded separately. Ignored `.cvf/runtime/ncr-offline-journey-worker-20261013/` logs and tool-owned autorun receipts allowed. Production source, old tests, configuration, store/schema/types, checkers/hooks/owners, continuity, model ledger and Customer Care read-only. No helper/split path, dependency, provider/network/browser/server/public/real-data effect. Out-of-scope repair needs a consolidated blocker, not a silent production patch.

## Design Control Gate

Preserve the existing UI and APIs. Home, DynamicForm, ProcessingScreen, ResultViewer and store must remain real at decisive assertions; no copying their implementation into the test. Mock transport/provider response, settings/navigation, analytics/enforcement recording and OS clipboard/file-generation boundaries explicitly; unrelated wizard/onboarding leaves may be stubs. Use synthetic local data only. Assertions are navigation, fields, displayed text, run/parent identity and captured UI payload. Do not assert governance decisions, risk/approval/DLP/validation/provider routing/audit efficacy or AI quality with mocks. Acceptance does not include real browser/OS export, backend cancellation or durable recovery.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: actual UI journey owners | `docs/reviews/evidence/ncr-offline-journey-dispatch-20261013.json` | sourcePins | sourcePins | Home/DynamicForm/ProcessingScreen/ResultViewer/store | ACCEPT |
| EXISTS: missing actual-component composition | `docs/reviews/evidence/ncr-offline-journey-dispatch-20261013.json` | selection | selection | observed existing Home callback stubs | ACCEPT |
| EXISTS: accepted result isolation | docs/reviews/CVF_NCR_RESULT_ISOLATION_COMPLETION_2026-10-12.md | Decision / Disposition | finite offline result acceptance | Local disposition | ACCEPT |

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
| scaffoldHelperCommand | python -B governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-OFFLINE-JOURNEY-20261013 --title "NCR Offline UI Journey Composition" --date 2026-10-13 --base 4cb80e5ac7f715089df89610ea696647f16e565e --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_NCR_RESULT_ISOLATION_COMPLETION_2026-10-12.md --include-worker-return-skeleton --no-evidence-readiness-applicable --scec-problem-key ncr-offline-ui-journey --scec-successor-scope NO_SUCCESSOR --stdout |
| generatedProfile | web-ui-dashboard; internal no-commit |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: reuse accepted role/trace/closeability shape; test-only actual-component requirements and three paths |
| checkerReadAheadConfirmation | applicable current constants and role/shape predicates read; not full checker reading |
| docOnlyNewFields | UI composition criteria and explicit intake/BUILD separation |
| claimBoundary | scoped packet preparation only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "work-order" --role dispatcher --lifecycle-phase pre-dispatch`
Returned defects: NONE_RETURNED
Actual result: 0 candidates, 0 returned, not truncated. This query does not prove absence of all applicable defects; refresh the final task class at release if classification changes.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local INTERNAL_AGENT orchestrator/dispatcher |
| Provider or surface | private shared workspace |
| Session or invocation | ncr-offline-journey-dispatch-20261013 |
| Working directory | repository root and installed Web package |
| Command or tool surface | targeted source/checker reads, actual scaffold/ADIF, pins, packet/gates/commits |
| Target paths | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_JOURNEY_2026-10-13.md`; `docs/baselines/CVF_GC018_NCR_OFFLINE_JOURNEY_2026-10-13.md`; `docs/reviews/evidence/ncr-offline-journey-dispatch-20261013.json`; `.gitattributes`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Allowed scope source | operator CVF Core continuation and Luna max worker authorization 2026-10-13 |
| Before status evidence | 4cb80e5ac7f715089df89610ea696647f16e565e;clean/staged empty |
| After status evidence | exact7 material then dedicated exact6 continuity;worker BUILD pending,23 prior observations retained |
| Diff evidence | git diff --check and exact manifest |
| Approval boundary | one internal subagent, offline UI tests only |
| Claim boundary | UI composition only;no provider/AI governance/full job/public/deploy |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-offline-journey-dispatch-20261013 |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_JOURNEY_2026-10-13.md`; `docs/baselines/CVF_GC018_NCR_OFFLINE_JOURNEY_2026-10-13.md`; `docs/reviews/evidence/ncr-offline-journey-dispatch-20261013.json`; `.gitattributes`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_JOURNEY_2026-10-13.md`; `docs/baselines/CVF_GC018_NCR_OFFLINE_JOURNEY_2026-10-13.md`; `docs/reviews/evidence/ncr-offline-journey-dispatch-20261013.json`; `.gitattributes`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Manifest delta | MATCH required before commit |
| Deletion or rename disposition | N/A with reason:none |

## Epistemic Process Block

Expected Result / Prediction: real form -> processing -> result -> follow-up -> child display preserves field/intent/parent/previous-output identity.
Evidence Comparison: accepted draft-recovery composes form/processing with a stub result; accepted result-isolation composes result/history with stub form/processing.
Contradiction Or Gap Disposition: one joint UI composition test is missing; no source defect or duplicate export/cancel suite selected.
Claim Update: test-only UI evidence selected; independent acceptance pending.

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
Rollback boundary: exact7 dispatch and exact6 continuity, prior accepted worker/evidence and23 observations retained; no guard/hook changes.

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST
Atomicity reason: packet/source pins and raw authority projection bind one finite dispatch; dedicated exact6 continuity binds actual material SHA.
Rollback boundary: exact7 dispatch material; accepted prior proof/source unchanged.
Exact changed manifest:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_JOURNEY_2026-10-13.md`
- `docs/baselines/CVF_GC018_NCR_OFFLINE_JOURNEY_2026-10-13.md`
- `docs/reviews/evidence/ncr-offline-journey-dispatch-20261013.json`
- `.gitattributes`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Expected Artifact Existence: packet/dispatch authored before commit; remaining material tracked; three future worker outputs absent.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/evidence/ncr-offline-journey-dispatch-20261013.json` |
| Chain map route | Local offline UI journey composition repair -> existing component -> independent Local review |
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
| INTERNAL_AGENT | actual existing UI components and store; internal worker | three new test/evidence/return paths, production read-only, no provider/effects/commit | source pins and selected gap; final review pending | N/A with reason: shared private workspace | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | no selected external consumer | no external execution authority | no external route | deferred; no adapter selected | DEFERRED_WITH_REASON |

## Claim Boundary

Finite offline jsdom UI form/processing/parent-result/follow-up/child-result composition only. Plain synthetic success responses are fixture display data. No AI governance, provider/live, real browser/OS effects, backend cancellation, durable recovery, full job/R3/R4, release/public/deployment or model ranking acceptance. Stop at this finite outcome.

## Evidence

Named source pins and selection in `docs/reviews/evidence/ncr-offline-journey-dispatch-20261013.json`; accepted component closures consumed. Implementation and independent acceptance pending.

## Decision / Proposed Tranche

One operator-authorized internal worker with exact3 new test/evidence/return outputs. Paired `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_JOURNEY_2026-10-13.md`; no production edit or automatic successor.23 prior model observations retained.

## Local Completion Disposition - 2026-10-13

Technical CLOSED_PASS_BOUNDED: finite test-only actual-component UI journey, worker1/1/type/lint/final-fast/ledger and distinct Local strategy/decoy1/1 PASS. Original3 byte receipts retained; test/proof MATCH, delivered return EOF normalized by Local with original base64 receipt. No production edit. Completion `docs/reviews/CVF_NCR_OFFLINE_JOURNEY_COMPLETION_2026-10-13.md`; Local proof `docs/reviews/evidence/ncr-offline-journey-local-20261013.json`, SHA256 `d9fa39ffcc487335dc6432339141b6287857413683721dfc198655160c2f9dbb`. Preparation PARTIAL_WITH_REASON: late clock, two metadata candidate failures and candidate2 digest typo retained. No full procedure, whole job/milestone/R3/R4, provider/public/deploy or model winner certification. Stop at this finite contribution; no automatic successor.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_JOURNEY_2026-10-13.md` | CLOSED_PASS_BOUNDED technical; procedure limits separate | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_NCR_OFFLINE_JOURNEY_COMPLETION_2026-10-13.md` | worker1/1 consumed; independent Local1/1; production unchanged | PASS |
| Roadmap state | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/roadmaps/README.md` | finite offline contribution; whole job/milestone/R3/R4 open | PASS |
| Registry JSON | `docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json` |24 tasks10 Haiku-family/9 Sonnet/5 Luna; previous23 preserved | PASS |
| Registry Markdown | `docs/reviews/CVF_WORKER_MODEL_SELECTION_PRELIMINARY_REPORT_2026-10-10.md` | current24; worker/Local attribution retained | PASS |
| External evidence digest | `docs/reviews/evidence/ncr-offline-journey-local-20261013.json` | sha256:d9fa39ffcc487335dc6432339141b6287857413683721dfc198655160c2f9dbb; internal Local proof/log/pin verification | PASS |
| System loop interlock | parked checkpoints | no automatic successor/new loop | N/A with reason: finite test-only UI contribution |
| Session continuity | current source/generated continuity surfaces | raw authority projection then dedicated actual material-SHA exact6 sync | PASS |

## Acceptance Receipt Assertion Matrix

| Requirement | Required value | Observed value | Status |
|---|---|---|---|
| REQ-JOURNEY | real form/process/result/store parent-child inputs/intent/output/id | worker1/1 and distinct Local strategy/decoy1/1; production unchanged | PASS_BOUNDED |
| REQ-BOUNDARY | synthetic UI data only, real five modules, no production/effect claim | exact3 original worker output; local URLs only; zero provider calls | PASS_BOUNDED |
| REQ-RETURN | exact3 honest evidence with ledger/fast/type/lint | final bound worker gates PASS consumed; clock/digest procedure limits retained | PASS_BOUNDED_EVIDENCE; PROCEDURE_PARTIAL_WITH_REASON |
