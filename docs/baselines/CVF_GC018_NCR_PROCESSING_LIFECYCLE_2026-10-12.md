# CVF GC-018 Baseline - NCR Processing Lifecycle

Memory class: governed-dispatch-baseline
docType: baseline
Status: CLOSED_PASS_BOUNDED
Date: 2026-10-12
Batch ID: CVF-NCR-PROCESSING-LIFECYCLE-20261012
Dispatch base head: 07fbf32cf04a6f4fd53697e6d3bb2216911e2afd
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN

## Purpose

Make the existing task-processing UI safe to leave, cancel and render again: abandoned work must not deliver a result; one unchanged task must not be re-sent due to presentation/callback changes; manual and automatic result delivery must happen at most once. Deliver actual component code and offline regressions, preserving request payload and classified failure/approval behavior.

Paired work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_PROCESSING_LIFECYCLE_2026-10-12.md`.

## Scope / Target / Owner Boundary

Exact worker4paths and Local closure/collection authority are defined in paired work order; ProcessingScreen client lifecycle only. Existing Home/tests/wizards/routes/provider/store remain read-only. Local corrected this baseline scope projection at closure; original work-order ownership remains the dispatch authority.

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
| Home consumes completion and removes processing on back | `docs/reviews/evidence/ncr-processing-lifecycle-local-20261012.json` | canonicalConsumerEvidence: unchanged Home path/hash/scopes376-411/606-629 | HomePage | existing parent UI | ACCEPT |
| current behavior contract regression suite | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.test.tsx` | named describe groups in Required First Reads | ProcessingScreen | current offline component tests | ACCEPT |
| installed offline selection and provider denial | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts` | default non-live include/exclude/setupFiles | defineConfig | current Vitest configuration | ACCEPT |

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

Authorized guard-maintenance scope: exact currentAuthority raw-pin projections in material and subsequent exact6 continuity; no guard/checker/hook edit.
Protected paths:

- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Operator authorization: standing useful continuation, Local review/repair/closure, and quality/time collection; operator manually requested Sonnet5.5 high. No push grant.
Rollback boundary: exact ProcessingScreen closure material/continuity; preserve16 historical rows and immutable worker submission.

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: admission baseline; source-selected contradiction and expected outcome in paired order/case. No worker proof yet.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: private dispatch packet, no publication claim.

## Claim Boundary

Finite ProcessingScreen client-lifecycle repair packet and synthetic offline red. Product source unchanged at dispatch. No confirmed backend cancellation, durable approval, full roadmap/release/live/provider/production/model-rank or cost claim. Requested model is operator metadata; reviewed collection remains16 until actual review.


## Local Terminal Review Disposition

Technical output accepted bounded after one Local dependent callback repair. Original worker return/proof unchanged; code/test pre-repair snapshots retained in Local JSON. Required-read timing procedureFAIL; optional roadmap/wizard omissions outside scope are not defects. Original Source Pin Contract is the execution preimage, not post-repair release; no fresh worker dispatch.

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST
Atomicity reason: accepted repaired product, closure/collection and matching raw authority projections must describe one package. Subsequent dedicated exact6 continuity records actual material SHA.
Rollback boundary: this exact material and projections only.
Exact changed manifest:
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.lifecycle.test.tsx`
- `docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_WORKER_RETURN_2026-10-12.md`
- `docs/reviews/evidence/ncr-processing-lifecycle-worker-20261012.json`
- `docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_COMPLETION_2026-10-12.md`
- `docs/reviews/evidence/ncr-processing-lifecycle-local-20261012.json`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_PROCESSING_LIFECYCLE_2026-10-12.md`
- `docs/baselines/CVF_GC018_NCR_PROCESSING_LIFECYCLE_2026-10-12.md`
- `docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json`
- `docs/reviews/CVF_WORKER_MODEL_SELECTION_PRELIMINARY_REPORT_2026-10-10.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_PROCESSING_LIFECYCLE_2026-10-12.md` | CLOSED_PASS_BOUNDED; repaired technical output, procedureFAIL | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_COMPLETION_2026-10-12.md` | distinct original fail and repaired PASS with immutable worker return/proof | PASS |
| Roadmap state | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | parent retained; finite component fix does not close full R1/R3/R4 | PASS |
| Registry JSON | `docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json` |17 task observations:10 Haiku-family,3 Sonnet,4 Luna | PASS |
| Registry Markdown | `docs/reviews/CVF_WORKER_MODEL_SELECTION_PRELIMINARY_REPORT_2026-10-10.md` | dated17-task quality/time/repair section | PASS |
| External evidence digest | `docs/reviews/evidence/ncr-processing-lifecycle-local-20261012.json` | sha256:6bb5ebe98e3997decf87307cbea7e617fd0f92061290f98569d271feee342dc7; internal Local independent evidence, preserved originals | PASS |
| System loop interlock | parked checkpoints | no new loop or automatic successor | N/A with reason: existing client repair only |
| Session continuity | six current continuity surfaces | raw authority projections then dedicated material-SHA continuity; verify before final report | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| old attempt receipt/report must not contaminate B | Local approval/report negatives fail original then pass repaired; B owns busy state | PASS |
| active approval remains usable | independent positive control observes its own id and event | PASS |
| technical acceptance distinct from procedural compliance | repaired bounded product, procedureFAIL | PASS truthful distinction |

