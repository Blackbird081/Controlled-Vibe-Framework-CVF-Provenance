# CVF GC-018 Baseline - NCR Result Viewer Run Isolation

Memory class: governed-dispatch-baseline
docType: baseline
Status: READY
Date: 2026-10-12
Batch ID: CVF-NCR-RESULT-ISOLATION-20261012
Dispatch base head: cd7314b0cbdab2e0a0b1f842ce6d1a6d4540ca29
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN

## Purpose

When navigating between saved runs, the result viewer must show the new run without carrying the previous run's unsent follow-up or export feedback. Same-run rerenders preserve the current draft and selected view. Late export/copy completion and old feedback timers must not mutate the replacement run. Two actual ResultViewer source assertions FAIL. Offline UI wiring only.

## Scope / Target / Owner Boundary

Exactly4: modify `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ResultViewer.tsx`; create `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ResultViewer.isolation.test.tsx`, `docs/reviews/evidence/ncr-result-isolation-worker-20261012.json`, `docs/reviews/CVF_NCR_RESULT_ISOLATION_WORKER_RETURN_2026-10-12.md`. Current source914 lines, final cap1100; new test<=700; return<=450 lines/64000B; proof<=128000B. One manual60min inclusive invocation. Ignored .cvf/runtime/ncr-result-isolation-worker-20261012 logs allowed. Home/store/types/receipt/schema/pack generation/old tests/history/AgentChat/checkers/hooks/owners/continuity/model ledger read-only. No extra helper path/global store/event bus, identity/schema redesign, dependencies, provider/browser/server/public/effects. Extra path/split => consolidated blocker.

## Design Control Gate

Use execution.id as existing run identity. Fix in ResultViewer only; no Home remount/key workaround. Same ID and changed object identity, current output refresh, language, ordinary rerender and StrictMode must not discard same-run unsent follow-up. Different ID, even identical output/template, starts empty follow-up, default view (pack with onFollowUp, result otherwise), closed menu, uncopied feedback and idle exporting. Preserve existing callback/export labels and source output/receipt pairing. Fixture receipts are presentation data, never AI governance proof.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: run changes without remount | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx` | result rendering and history restore | ResultViewer | execution={activeExecution} | ACCEPT |
| EXISTS: stale draft and late copy feedback | `docs/reviews/evidence/ncr-result-isolation-dispatch-20261012.json` | admissionWitness | admissionWitness | actual ResultViewer, same-run control, two original-source failures | ACCEPT |
| EXISTS: accepted prior history outcome | docs/reviews/CVF_NCR_CHAT_HISTORY_COMPLETION_2026-10-12.md | Claim Boundary | finite prior repair | Local disposition | ACCEPT |

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
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-RESULT-ISOLATION-20261012 --title "NCR Result Viewer Run Isolation" --date 2026-10-12 --base cd7314b0cbdab2e0a0b1f842ce6d1a6d4540ca29 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_NCR_CHAT_HISTORY_COMPLETION_2026-10-12.md --include-worker-return-skeleton --no-evidence-readiness-applicable --scec-problem-key ncr-result-run-isolation --scec-successor-scope NO_SUCCESSOR --stdout |
| generatedProfile | web-ui-dashboard; internal no-commit |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: prior verified ready role-contract shape, four paths and witnessed result state isolation contract; no copied closure |
| checkerReadAheadConfirmation | current dispatch/closeability/scaffold/read-ahead constants; retained verified role/trace/ledger/probe bindings, scoped read only |
| docOnlyNewFields | source witness and consumer repair contract; no new schema |
| claimBoundary | packet preparation and scoped source witness only |

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
| Session or invocation | ncr-result-isolation-dispatch-20261012 |
| Working directory | repository root and installed Web package |
| Command or tool surface | targeted source/owner/constants reads, actual scaffold/ADIF, two-case admission witness, raw/HEAD pins, dispatch/gates/commits |
| Target paths | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_RESULT_ISOLATION_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_RESULT_ISOLATION_2026-10-12.md`; `docs/reviews/evidence/ncr-result-isolation-dispatch-20261012.json`; `docs/roadmaps/README.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.csv`; `.gitattributes`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Allowed scope source | operator next under standing manual worker/Local orchestration; existing NCR result maintenance |
| Before status evidence | cd7314b0cbdab2e0a0b1f842ce6d1a6d4540ca29;clean/staged empty before temporary witness;production unchanged |
| After status evidence | exact11 dispatch material then exact6 continuity;worker pending,22 observations unchanged |
| Diff evidence | git diff --check and exact manifests |
| Approval boundary | one manual shared-workspace worker;offline synthetic UI only |
| Claim boundary | actual ResultViewer state only;no provider/AI governance/whole NCR acceptance |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-result-isolation-dispatch-20261012 |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_RESULT_ISOLATION_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_RESULT_ISOLATION_2026-10-12.md`; `docs/reviews/evidence/ncr-result-isolation-dispatch-20261012.json`; `docs/roadmaps/README.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.csv`; `.gitattributes`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_RESULT_ISOLATION_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_RESULT_ISOLATION_2026-10-12.md`; `docs/reviews/evidence/ncr-result-isolation-dispatch-20261012.json`; `docs/roadmaps/README.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.csv`; `.gitattributes`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Manifest delta | MATCH required before commit |
| Deletion or rename disposition | N/A with reason:none |

## Epistemic Process Block

Expected Result / Prediction: result controls and async feedback belong to the displayed execution lifetime.
Evidence Comparison: same-run draft control PASS, two actual source assertions FAIL: A draft visible under B and late A copy marks B.
Contradiction Or Gap Disposition: existing local state lacks execution-lifetime binding; repair ResultViewer only.
Claim Update: offline UI isolation selected; worker implementation and independent Local acceptance pending.

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

Operator authorization: next under standing manual worker/Local orchestrator-reviewer roles,2026-10-12.
Rollback boundary: exact11 dispatch and exact6 continuity, prior accepted worker/evidence and22 observations retained; no guard/hook changes.

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST
Atomicity reason: packet/witness, roadmap/index/inventory and raw authority projection bind one finite dispatch. Dedicated continuity binds actual material SHA.
Rollback boundary: exact11 dispatch.
Exact changed manifest:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_RESULT_ISOLATION_2026-10-12.md`
- `docs/baselines/CVF_GC018_NCR_RESULT_ISOLATION_2026-10-12.md`
- `docs/reviews/evidence/ncr-result-isolation-dispatch-20261012.json`
- `docs/roadmaps/README.md`
- `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`
- `docs/roadmaps/CVF_ROADMAP_INVENTORY.md`
- `docs/roadmaps/CVF_ROADMAP_INVENTORY.csv`
- `.gitattributes`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Expected Artifact Existence: current packet/witness authored before commit;other material tracked;existing production source,three future outputs absent.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/evidence/ncr-result-isolation-dispatch-20261012.json` |
| Chain map route | Local result viewer run isolation repair -> existing component -> independent Local review |
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
| INTERNAL_AGENT | existing ResultViewer and Local worker | four paths, synthetic offline client repair, no commit/effects | dispatch witness and source pins; final review pending | N/A with reason: shared private workspace | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | no external consumer selected | no CLI/MCP/runtime effect authority | no external route in this finite outcome | deferred adapter; no implementation selected | DEFERRED_WITH_REASON |

## Claim Boundary

Finite offline jsdom result UI identity, draft and async feedback only. Synthetic receipt copy is presentation/payload wiring, not AI governance behavior. No live/full/provider/browser/backend/OS-side-effect cancellation/schema/public/deploy/whole NCR/model-ranking acceptance. Stop finite outcome.

## Evidence

Paired order fixes path/source/ledger/gate/clock scope. Local source witness in `docs/reviews/evidence/ncr-result-isolation-dispatch-20261012.json`; implementation/acceptance pending.

## Decision / Proposed Tranche

Four outputs, one manual60min offline worker only after bound committed release. Paired `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_RESULT_ISOLATION_2026-10-12.md`;22 observations unchanged;no automatic successor.
