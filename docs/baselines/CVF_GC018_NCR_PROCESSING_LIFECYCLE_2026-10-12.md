# CVF GC-018 Baseline - NCR Processing Lifecycle

Memory class: governed-dispatch-baseline
docType: baseline
Status: DISPATCH_READY
Date: 2026-10-12
Batch ID: CVF-NCR-PROCESSING-LIFECYCLE-20261012
Dispatch base head: 07fbf32cf04a6f4fd53697e6d3bb2216911e2afd
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN

## Purpose

Make the existing task-processing UI safe to leave, cancel and render again: abandoned work must not deliver a result; one unchanged task must not be re-sent due to presentation/callback changes; manual and automatic result delivery must happen at most once. Deliver actual component code and offline regressions, preserving request payload and classified failure/approval behavior.

Paired work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_PROCESSING_LIFECYCLE_2026-10-12.md`.

## Scope / Target / Owner Boundary

sourceFinding/reproduction/limits

## Source / Predecessor Evidence

Prior Home closure at745502c1c and `docs/reviews/CVF_NCR_HOME_HISTORY_BINDING_COMPLETION_2026-10-11.md` remains accepted bounded with procedureFAIL. New source audit/actual5-case probe at07fbf32cf04a6f4fd53697e6d3bb2216911e2afd: four established ProcessingScreen lifecycle failures plus one uncancelled positive PASS, preserved in `docs/reviews/evidence/ncr-processing-lifecycle-dispatch-20261012.json`. No prior implementation reopened. Packet supplies six raw-file/HEAD-blob pins and orchestrator-owned scopes/conditions before worker execution.

## Decision / Proposed Tranche

Selected: existing ProcessingScreen client lifecycle. Actual component probe at `07fbf32cf04a6f4fd53697e6d3bb2216911e2afd` confirms four failures with one passing uncancelled positive control: delayed callback after unmount=1; late response after Cancel=1; callback-only rerender POST count=2; two manual clicks plus auto timer completion count=3. `docs/reviews/evidence/ncr-processing-lifecycle-dispatch-20261012.json` preserves source, config, raw results/digests and Local harness collection failures separately.

This serves Home and the existing wizard consumers without another dashboard or runtime. Dormant unused hook, global pin checker, retrospective model projections and S5 remain deferred; provider/media/real-data/public/deploy effects and full roadmap exits remain parked. No benchmark-only task. Stop after fixed component, meaningful regressions and complete pending return; no automatic successor.

## Design Control Gate

Actual existing consumer contradiction established offline. Locked outcome is task lifetime isolation, request stability and at-most-once completion. Preserve public component props, request/governance envelope fields, classified failure/approval/recovery behavior and mock-only demo route. Client abort is best effort, never confirmed server cancellation. No new state owner or full roadmap release claim.

## Evidence / Verification

Actual component red-green lifecycle controls; mocked deferred transport, fake timers, exact callbacks/POSTs/output/receipt. New lifecycle/existing ProcessingScreen/Home focused tests, tsc, owned lint and full return/ledger. Required scopes supplied by orchestrator; optional parent/O6 context is not worker read burden. One distinct Local lifetime challenge later; consume valid returned proof without broad duplication.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| fetch and no-badge timer lack abandonment guard | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx` | executeReal response and 300ms completion branches | ProcessingScreen | ProcessingScreenProps | ACCEPT |
| startup reruns on executeReal dependency changes | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx` | useCallback executeReal dependencies; startup useEffect | ProcessingScreen | existing lifecycle effects | ACCEPT |
| manual and auto completion separate | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx` | completedOutput effect; view-results-btn onClick | ProcessingScreen | existing result delivery | ACCEPT |
| mock interval cleanup unused; Cancel forwards only | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx` | runMockExecution; startup mock branch; Cancel button | ProcessingScreen | existing demo/cancel consumer | ACCEPT |
| actual failures with valid uncancelled control | `docs/reviews/evidence/ncr-processing-lifecycle-dispatch-20261012.json` | sourceFinding and reproduction | reproduction | Local offline actual-component probe | ACCEPT |
| Home consumes completion and removes processing on back | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx` | handleProcessingComplete; handleBack; ProcessingScreen render | HomePage | existing parent UI | ACCEPT |
| current behavior contract regression suite | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.test.tsx` | named describe groups in Required First Reads | ProcessingScreen | current offline component tests | ACCEPT |
| installed offline selection and provider denial | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts` | default non-live include/exclude/setupFiles | defineConfig | current Vitest configuration | ACCEPT |

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
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-PROCESSING-LIFECYCLE-20261012 --title "NCR Processing Lifecycle" --date 2026-10-12 --base 07fbf32cf04a6f4fd53697e6d3bb2216911e2afd --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_NCR_HOME_HISTORY_BINDING_COMPLETION_2026-10-11.md --include-worker-return-skeleton --no-evidence-readiness-applicable --scec-problem-key ncr-processing-lifecycle --scec-successor-scope NO_SUCCESSOR --stdout` |
| generatedProfile | web-ui-dashboard; internal no-commit |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: bounded ProcessingScreen consumer, exact four outputs, orchestrator-derived scopes/assertions and honest read/clock proof |
| checkerReadAheadConfirmation | applicable constants, section/trace tokens and role predicates read before declarations |
| docOnlyNewFields | dispatch evidence only; no new runtime schema/store |
| claimBoundary | packet preparation, no implementation or worker outcome |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "work-order" --role dispatcher --lifecycle-phase pre-dispatch`
Returned defects: NONE_RETURNED
Actual result: 0 candidates, 0 returned, not truncated. This query does not prove absence of all applicable defects; refresh the final task class at release if classification changes.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named contracts/source/case only; no repository/corpus scan.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/evidence/ncr-processing-lifecycle-dispatch-20261012.json` |
| Chain map route | Local ProcessingScreen lifecycle contradiction -> existing component -> independent Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing UI lifecycle/source-fidelity/closure owners |
| Disposition | internal existing product repair; no external research |
| Claim boundary | Local private source verification and final decision |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: dedicated exact six-path dispatch/closure continuity and currentAuthority only; no guard/checker/hook mutation.
Protected paths:

- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Operator authorization: 2026-10-12 continuation and Sonnet5.5 high manual worker switch, standing audit/select/useful work-order/collection direction. Local owns necessary private commits and continuity; no push.
Rollback boundary: exact new packet and matching continuity only; preserve Home closure and historical observations.
Dispatcher material exact manifest: `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_PROCESSING_LIFECYCLE_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_PROCESSING_LIFECYCLE_2026-10-12.md`; `docs/reviews/evidence/ncr-processing-lifecycle-dispatch-20261012.json`; `docs/reference/work_order_template/CVF_WORK_ORDER_SOURCE_VERIFICATION_ADDENDUM.md`; `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; `docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json`; `docs/reviews/CVF_WORKER_MODEL_SELECTION_PRELIMINARY_REPORT_2026-10-10.md`.
Dedicated continuity exact manifest: `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
Worker exact manifest: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.lifecycle.test.tsx`; `docs/reviews/evidence/ncr-processing-lifecycle-worker-20261012.json`; `docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_WORKER_RETURN_2026-10-12.md`.
Local reserves `docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_COMPLETION_2026-10-12.md` and `docs/reviews/evidence/ncr-processing-lifecycle-local-20261012.json`; collection admission only after review. Never hand-edit generated aggregates.

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: admission baseline; source-selected contradiction and expected outcome in paired order/case. No worker proof yet.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: private dispatch packet, no publication claim.

## Claim Boundary

Finite ProcessingScreen client-lifecycle repair packet and synthetic offline red. Product source unchanged at dispatch. No confirmed backend cancellation, durable approval, full roadmap/release/live/provider/production/model-rank or cost claim. Requested model is operator metadata; reviewed collection remains16 until actual review.

