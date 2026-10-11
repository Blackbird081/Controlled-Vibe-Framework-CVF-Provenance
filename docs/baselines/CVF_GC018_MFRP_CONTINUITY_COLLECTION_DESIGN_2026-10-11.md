# CVF GC-018 Baseline - MFRP Material Continuity Collection Design

Memory class: governed-dispatch-baseline
docType: baseline
Status: DISPATCH_READY
Date: 2026-10-11
Batch ID: CVF-MFRP-CONTINUITY-COLLECTION-DESIGN-20261011
Dispatch base head: 0e5de48d040c44a76cd729565d9780b8c50207d1
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN

## Purpose

Deliver one bounded design for the P2 producer -> P4-C1 collector -> material/continuity authority seam, using the real S2-R3 skipped case. Decide whether existing machinery can safely recover collection or needs a small explicitly scoped contract change. Correct fail-closed fingerprint behavior must remain. This is a useful MFRP design task, not another model benchmark or S5 implementation.

Paired work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_CONTINUITY_COLLECTION_DESIGN_2026-10-11.md`.

## Scope / Target / Owner Boundary

Dispatcher owns packet/admission; operator manually starts worker; worker owns three new documentation/evidence paths; distinct Local reviewer owns technical disposition/closure; steward owns continuity. Shared workspace is INTERNAL_AGENT. Requested Claude Haiku/ex high is operator metadata; native version/effort/tokens/bill remain unknown unless exposed. Local launches no agent. No product/helper/guard/profile/test/journal/receipt edits, historical replay, automatic retry or sample promotion.

## Source / Predecessor Evidence

Existing fingerprint contract, P2 producer/P4 collector, bounded retry and exact S2-R3 case `docs/reviews/evidence/mfrp-continuity-collection-design-dispatch-case-20261011.json`. Thirteen source pins in order; named three overlapping companion paths, actual correct target refusal, two valid split receipts and retained collection skip. Original receipts/journal/outcomes read-only.

## Decision / Proposed Tranche

Selected: bounded MFRP collection seam design. Actual case `docs/reviews/evidence/mfrp-continuity-collection-design-dispatch-case-20261011.json` freezes both canonical-valid PASS receipts and the SKIPPED_NO_COMMITTED_EVIDENCE attempt; exact three material/continuity overlaps verified. Actual historical-target owner rejects different bytes, current continuity target passes. This is correct enforcement and an unresolved producer/consumer composition question, not a proved algorithm bug.

Alternatives: another retrospective/model benchmark has no new task demand; O6 helper remains deferred because no new ineffective-mutation recurrence; broad fast-gate expansion has no admission/value case; S5/Expense/PLL/scoring/Gateway/provider/public/deploy remain parked. Old retry design already allows one bounded retry per trusted commit; preserve this and distinguish opportunity/attempt/sample counts. No second blind replay or historical promotion.

Consumer: Local maintainer chooses one design disposition with exact owner/acceptance/rollback. Stop after three outputs and Local review; implementation requires a separate future decision.

Worker exact outputs: `docs/reviews/CVF_MFRP_CONTINUITY_COLLECTION_DESIGN_2026-10-11.md`; `docs/reviews/evidence/mfrp-continuity-collection-design-worker-20261011.json`; `docs/reviews/CVF_MFRP_CONTINUITY_COLLECTION_DESIGN_WORKER_RETURN_2026-10-11.md`.45-minute invocation; design350/64000, return450/64000, proof128000. No stage/commit/push/nested agent.

## Evidence / Verification

Three actual isolated owner probes and canonical receipt integrity on copied raw frozen receipts; read-depth/source maps/clock scope/first-final failures retained. One selected safe recommendation or explicit deferral with bounded trigger. Distinct Local review owns final authority/design disposition; no collection sample promotion.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | DISPATCH_READY; WORKER_MUST_NOT_COMMIT; INTERNAL_AGENT; REQUIRED_FIELDS; TRACE_REQUIRED_LABELS; SECTION_GROUPS; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | confirmation/evidence of selected packet structure; not a dispatch or implementation proof |
| claimBoundary | checker constants and applicable predicates read before these packet files; added ready-state contracts were read before their declarations |

## Dual Agent Surface Matrix


| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | P2/P4/closure/continuity owners | three design/proof/return files; no commit/implementation | frozen case and existing contracts | shared workspace | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | no external consumer | zero external research/invocation | Local source design | no new adapter | N/A_WITH_REASON |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id CVF-MFRP-CONTINUITY-COLLECTION-DESIGN-20261011 --title "MFRP Material Continuity Collection Design" --date 2026-10-11 --base 0e5de48d040c44a76cd729565d9780b8c50207d1 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_MODEL_SELECTION_S2_R3_PROJECTION_COMPLETION_2026-10-11.md --include-worker-return-skeleton --no-evidence-readiness-applicable --scec-problem-key mfrp-material-continuity-collection-design --scec-successor-scope NO_SUCCESSOR --stdout` |
| generatedProfile | protected-governance-path; internal no-commit |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: exact collection seam consumer/paths/source joins; irrelevant corpus fields omitted |
| checkerReadAheadConfirmation | applicable constants/predicates read before declaration |
| docOnlyNewFields | source-derived design and proof/return; no new schema/store |
| claimBoundary | packet authoring only; no worker result |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| immutable range recipe and target admission | `docs/reference/review_cost_control/CVF_COMMITTED_EVIDENCE_FINGERPRINT_CONTRACT.md` | Producer Admission Condition; Continuity Case | committedEvidence | canonical fingerprint contract | ACCEPT |
| actual historical-target check | `governance/compat/committed_evidence_fingerprint.py` | verify_worktree_matches_committed_target body | verify_worktree_matches_committed_target | actual byte comparison and metadata owner | ACCEPT |
| producer refuses wrong target | `governance/compat/run_agent_autorun_workflow_gate.py` | _run_phase committedEvidence branch | _run_phase | P2 producer | ACCEPT |
| consumer exact trusted range/skip | `governance/compat/mfrp_shadow_canary_autocollect.py` | generate_current_receipt; validate_and_reconcile_receipt bodies | validate_and_reconcile_receipt | P4 collector | ACCEPT |
| prior retry limit | `docs/reviews/CVF_MFRP_P4_C1_BOUNDED_RETRY_RECOVERY_COMPLETION_2026-09-27.md` | Findings / Position; Risk / Corrective Action | retryOfTrustedCommit | existing bounded retry owner | ACCEPT |
| frozen current case | `docs/reviews/evidence/mfrp-continuity-collection-design-dispatch-case-20261011.json` | receipts; overlappingPaths; collectorAttemptsForThisMaterial | overlappingPaths | dispatcher evidence snapshot | ACCEPT |
| scaffold actual flags | `governance/compat/run_worker_return_scaffold.py` | main body | main | preparation owner | ACCEPT |

## External Knowledge Intake Routing


| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/evidence/mfrp-continuity-collection-design-dispatch-case-20261011.json` |
| Chain map route | frozen Local receipt case -> existing owner design -> distinct Local disposition |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing P2/P4/fingerprint/closure owners |
| Disposition | internal design; no external research |
| Claim boundary | Local private source verification and final decision |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: exact documentation/case packet, raw current-authority hashes and regenerated projections; dedicated six-surface dispatch continuity after material. Worker edits no protected source/receipt/journal/profile.
Protected paths: `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
Operator authorization: 2026-10-11 next; standing audit-and-choose/manual Haiku worker/model collection; necessary private packet/closure/continuity. No push/API/public/deploy grant.
Rollback boundary: revert exact new design packet/case/worker outputs and matching authority/continuity; preserve original receipts/journal/historical outcomes.
Dispatcher material exact manifest: `docs/baselines/CVF_GC018_MFRP_CONTINUITY_COLLECTION_DESIGN_2026-10-11.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_CONTINUITY_COLLECTION_DESIGN_2026-10-11.md`; `docs/reviews/evidence/mfrp-continuity-collection-design-dispatch-case-20261011.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
Dedicated continuity exact manifest: `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
Worker exact manifest: `docs/reviews/CVF_MFRP_CONTINUITY_COLLECTION_DESIGN_2026-10-11.md`; `docs/reviews/evidence/mfrp-continuity-collection-design-worker-20261011.json`; `docs/reviews/CVF_MFRP_CONTINUITY_COLLECTION_DESIGN_WORKER_RETURN_2026-10-11.md`. Local alone owns completion `docs/reviews/CVF_MFRP_CONTINUITY_COLLECTION_DESIGN_COMPLETION_2026-10-11.md` and `docs/reviews/evidence/mfrp-continuity-collection-design-local-20261011.json` plus necessary reviewed order/baseline/collection promotion after acceptance. Generated aggregates regenerated only.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "work-order" --role dispatcher --lifecycle-phase pre-dispatch`
Returned defects: NONE_RETURNED
Actual result: 0 candidates, 0 returned, not truncated. This query does not prove absence of all applicable defects; refresh the final task class at release if classification changes.

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: normative admission baseline; source/consumer audit in paired order, no worker result observed.

## Claim Boundary

Packet proposal under existing optional profiles; final committed bound pre-dispatch must PASS before manual worker start. No old-history quality upgrade, extra original Haiku/Opus sample, runtime effect or push authority.
