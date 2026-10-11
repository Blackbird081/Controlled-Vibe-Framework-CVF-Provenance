# CVF GC-018 Baseline - NCR Home History Binding

Memory class: governed-dispatch-baseline
docType: baseline
Status: DISPATCH_READY
Date: 2026-10-11
Batch ID: CVF-NCR-HOME-HISTORY-BINDING-20261011
Dispatch base head: 8240cd0d65e205f028391d31f58ac1555bd5b233
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN

## Purpose

Restore historical work so displayed output, execution metadata, local accept/reject target and follow-up lineage all refer to the same selected execution. Consumer: user continuing an accepted result in the existing Home flow. Deliver a bounded product fix and meaningful offline Home regressions; no extra model benchmark or governance subsystem.

Paired work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HOME_HISTORY_BINDING_2026-10-11.md`.

## Scope / Target / Owner Boundary

Exactly four worker paths: two existing product/test files and two new return/evidence files. Home local result decisions are not durable artifact approval (send/B2 remains stopped). No global store/type/continuity helper edits, new dashboard, model selector, API route, dependency/config/lockfile change or new helper path. No real user ledger/localStorage reads outside isolated synthetic fixtures, account/provider/network invocation, native media, public/deploy or nested agents. Local alone stages/commits/updates continuity. Runtime diagnostics/fixtures may be written under .cvf/runtime/ncr-home-history-worker-20261011; mandatory gate helper-owned standard receipts are explicitly admitted, with actual paths recorded.

Worker45min, exact four outputs; return450/64000, proof128000, Home700/test550 lines. Local reviewer/closer owns final disposition; sourceR2/media/provider/public/deploy/P11 and stopped durable-approval lanes unchanged.

## Source / Predecessor Evidence

Actual Local Home/real-store red at 35b2f9f1cdb579a6078513dd74382f339f85dbd6: expected fixture_A|OUTPUT_A, observed fixture_B|OUTPUT_A. Source owners: Home restore/ResultViewer/actions, store methods, continuity helper and History route. `docs/reviews/evidence/ncr-home-history-binding-dispatch-20261011.json` preserves exact12 source pins, actual oracle/log and two Local harness failures; no worker burden attribution. Paired order contains exact sections and13 source pins plus fresh authority pins. Only display mismatch dynamically established; decisions/lineage/query scenarios are fixed worker proof obligations.

## Decision / Proposed Tranche

History onContinue currently selects A before warm navigation; the selected defect is independent Home resume binding on historical URL/null selection/ambient change. Existing iteration-memory flag remains unchanged.

Selected: existing NCR Home history identity repair. Local actual Home/real-store probe at 35b2f9f1cdb579a6078513dd74382f339f85dbd6 restored OUTPUT_A with fixture_B metadata instead of fixture_A. This changes what users review and which parent a follow-up uses. Existing source points to wrong-target local decisions; only the display mismatch has been dynamically observed before dispatch. Raw evidence and two Local harness failures are retained in `docs/reviews/evidence/ncr-home-history-binding-dispatch-20261011.json`. Worker must independently construct actual page tests, not import the Local oracle.

Alternatives: S5 automation has no admitted demand; MFRP structural collection and O6 helper remain deferred; further retrospective projections add no new product output. SourceR2/media, Expense, provider/public/deploy/P11 remain parked. This finite fix advances NCR R1/R4 version/continuation correctness under existing UI/store owners; it does not claim full R1/R3/R4 exit.
Stop after exact product fix, regression proof and complete pending return. No automatic successor or endpoint campaign.


## Design Control Gate

Existing consumer and source defect; exact Home/test ownership, synthetic-only verification, independent Local review and fixed ledger. No new store/schema/approval semantics. Release requires committed packet/currentAuthority plus six-surface actual-SHA continuity and bound gates; readiness is not claimed from these draft bytes alone.

## Evidence / Verification

Actual Home red-green; stored A/B independence and B preservation; accept/reject/follow-up lineage, A->C/invalid query/fresh run. Focused four test files plus TypeScript/lint; final full return gate and ledger. Semantic source reads, actual scaffold and complete clock intervals; native usage null when unexposed. Distinct Local source-derived challenge at review; no broad duplicate suite.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| restore A output without selecting A execution | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx` | W123-T1 restore effect; ResultViewer invocation; handleAccept/handleReject/handleFollowUp bodies | HomePage | existing Home workflow | ACCEPT |
| exact store selection available | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/store.ts` | execution store methods | setCurrentExecution; getExecutionById | existing execution store | ACCEPT |
| child lineage comes from supplied parent | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-continuity.ts` | buildContinuationExecution body | buildContinuationExecution | existing continuity helper | ACCEPT |
| History routes accepted work to Home | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/history/page.tsx` | onContinue prop body | HistoryPage | existing history consumer | ACCEPT |
| result metadata and callbacks supplied by Home | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ResultViewer.tsx` | ResultViewerProps; ResultViewer signature | ResultViewer | existing result consumer | ACCEPT |
| real Home regression currently browse-only | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.test.tsx` | HomePage describe block | HomePage | existing component-test home | ACCEPT |
| offline test selection uses current setup | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts` | default non-live include/exclude/setupFiles | defineConfig | existing Vitest configuration | ACCEPT |
| real contradictory render observed | `docs/reviews/evidence/ncr-home-history-binding-dispatch-20261011.json` | reproduction; sourceFinding; localHarnessFailures | sourceFinding | Local synthetic component evidence | ACCEPT |
| O6 subordinate checklist applied to new controls | `docs/reviews/CVF_ORACLE_O6_DESIGN_COMPLETION_2026-10-11.md` | Purpose; Decision / Disposition | manual P0-P7 | existing reviewer reference | ACCEPT |

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
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-HOME-HISTORY-BINDING-20261011 --title "NCR Home History Binding" --date 2026-10-11 --base 35b2f9f1cdb579a6078513dd74382f339f85dbd6 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_NCR_W05_SELECTED_CHAIN_READINESS_2026-10-07.md --include-worker-return-skeleton --no-evidence-readiness-applicable --scec-problem-key ncr-home-history-binding --scec-successor-scope NO_SUCCESSOR --stdout` |
| generatedProfile | web-ui-dashboard; internal no-commit |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: bounded Home consumer, exact four outputs, semantic regression matrix and honest read/clock proof |
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
| Internal source | `docs/reviews/evidence/ncr-home-history-binding-dispatch-20261011.json` |
| Chain map route | Local actual Home contradiction -> existing Home/store consumer -> independent Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing P2/P4/fingerprint/closure owners |
| Disposition | internal existing product repair; no external research |
| Claim boundary | Local private source verification and final decision |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Dispatch Pin Repair Disposition

Local reviewed the blocked first invocation at8240cd0d6: the13th dispatch-evidence pin was stale. Intended committed evidence is confirmed; working-file and HEAD-blob hashes are now explicit and checked together. Original blocked return/proof are preserved verbatim in `docs/reviews/evidence/ncr-home-history-binding-local-20261011.json` with digests. Prior invocation is not implementation acceptance; capture fresh clocks/HEAD and perform the required semantic reads in the new invocation. Worker outputs are absent after Local preservation. No helper/checker or product mutation is included in this repair.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: exact current-authority projections and dedicated six-path dispatch/closure continuity only; no guard/checker mutation.
Protected paths:

- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Operator authorization: 2026-10-11 continuation, explicit audit-and-choose response, standing manual worker/work-order and collection instruction. Local owns necessary private admission/commit/continuity; no push grant.
Rollback boundary: revert this exact dispatch/implementation and its matching authority/continuity; preserve historical accepted work and raw returned evidence.
Dispatcher material exact manifest: `docs/baselines/CVF_GC018_NCR_HOME_HISTORY_BINDING_2026-10-11.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HOME_HISTORY_BINDING_2026-10-11.md`; `docs/reviews/evidence/ncr-home-history-binding-local-20261011.json`; `docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json`; `docs/reviews/CVF_WORKER_MODEL_SELECTION_PRELIMINARY_REPORT_2026-10-10.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
Dedicated continuity exact manifest: `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
Worker exact manifest: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.test.tsx`; `docs/reviews/evidence/ncr-home-history-binding-worker-20261011.json`; `docs/reviews/CVF_NCR_HOME_HISTORY_BINDING_WORKER_RETURN_2026-10-11.md`.
Local reserves `docs/reviews/CVF_NCR_HOME_HISTORY_BINDING_COMPLETION_2026-10-11.md` and `docs/reviews/evidence/ncr-home-history-binding-local-20261011.json`; any later collection promotion is reviewer-owned. Generated aggregates regenerated only.

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: admission baseline; source-selected contradiction and expected outcome in paired order/case. No worker proof yet.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: private dispatch packet, no publication claim.

## Claim Boundary

Bounded local product repair selected; no provider governance, full NCR exit, durable approval, release, production or comparative model claim. Fifteen reviewed tasks remain historical collection; new worker observation only after Local review.
