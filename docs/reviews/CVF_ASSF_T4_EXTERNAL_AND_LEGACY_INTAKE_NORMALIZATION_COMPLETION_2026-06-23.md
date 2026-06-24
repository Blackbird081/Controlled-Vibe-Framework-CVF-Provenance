# CVF ASSF-T4 External And Legacy Intake Normalization - Completion Review

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-23

docType: review

Batch ID: ASSF-T4

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_FOR_WORKER_2026-06-23.md`

reviewBaseHead: 5a4f9591

## Purpose

Record the reviewer's independent verification and closure of the ASSF-T4
External And Legacy Intake Normalization contract, authored by the worker
against the frozen ASSF-T1 package contract, the ASSF-T3 promotion bridge
contract, the external skill screening matrix, and the ASSF-T0.1 legacy
absorption ledger, plus the reviewer-owned worker-return accuracy repairs
and the handoff HEAD-block update the worker correctly flagged as outside
its scope.

## Target / Source

- Target: the worker-return packet at
  `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_WORKER_RETURN_2026-06-23.md`
  and its deliverable, the normalization contract
  `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md`.
- Source: the dispatched GC-018
  (`docs/baselines/CVF_GC018_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_2026-06-23.md`)
  and work order
  (`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_FOR_WORKER_2026-06-23.md`),
  both authored at `dispatchBaseHead 050741bb` and committed at `5a4f9591`.

## Risk / Corrective Action

Risk: a normalization contract that invented disposition labels not present
in the cited screening matrix or legacy ledger, that weakened the
no-self-activation invariant, or that misdescribed which fields already
exist in ASSF-T1 would let a future normalizer implement an unsafe or
unbuildable intake path. Accepting the worker-return self-report without
independently re-deriving the disposition vocabularies and the field
coverage against source would let an inaccurate claim pass into the
canonical reference family.

Corrective action (reviewer-owned, all applied before this commit): the
reviewer independently re-derived both disposition vocabularies against
source (all real and complete), cross-checked every ASSF-T1 field the
contract maps to against the real T1 contract, found two worker-return
accuracy defects (Findings A and B below), corrected the worker return and
added a T1-alignment note to the contract, updated the active handoff HEAD
block per GC-020, and re-ran the gates.

## Scope / Methodology

The reviewer independently re-verified the worker's deliverable rather than
accepting the worker-return's self-report:

1. Read the normalization contract and the worker return in full.
2. Re-derived the external screening disposition vocabulary from
   `docs/reference/archive/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md`:
   confirmed `ACCEPT_AS_PATTERN`, `MERGE_AS_PATTERN`, `DEFER_RUNTIME_GATED`,
   `DEFER_EVOLUTION_GATED`, and `DEFER_CANDIDATE_SPECIFIC_SCREEN` all exist;
   the three DEFER tokens are the complete DEFER set in the matrix.
3. Re-derived the legacy ledger disposition vocabulary from
   `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md`
   Absorption Candidate Ledger: confirmed all seven labels the contract maps
   (`ABSORB_AS_CONTRACT_INPUT`, `ABSORB_AS_LIFECYCLE_INPUT`,
   `ABSORB_AS_PACKAGE_PATTERN`, `ABSORB_AS_TOOL_ADAPTER_INPUT`,
   `REFERENCE_ONLY`, `BLOCKED_UNVERIFIED_SOURCE`, `DUPLICATE`) exist with
   real ledger rows; confirmed six distinct ledger rows carry
   `BLOCKED_UNVERIFIED_SOURCE` (the worker's "six files" claim holds).
4. Cross-checked every ASSF-T1 field the contract references against the real
   `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`:
   confirmed the Provenance family (`originLane`, `sourceArtifacts`,
   `legacyRows`, `license`, `reviewArtifacts`) and the Risk-and-authority
   family (`riskProfile`, `authorityCeiling`, `sideEffects`, `permissions`,
   `rollback`, `safeStop`) exist; found two contract-required fields
   (`security_notes`, `sourceRevision`) that do NOT exist in T1 (Finding B).
5. Compared the contract's No-Self-Activation Invariant against the ASSF-T3
   bridge contract source: clauses 3-5 are verbatim; clauses 1-2 are adapted
   (Finding A) - clause 1 extends the actor list to include the normalizer,
   clause 2 drops the T3-specific "inherited from the LSC field" derivation
   that does not apply to external/legacy intake. The adaptation is correct
   engineering; the binding semantics are preserved.
6. Ran the pre-closure autorun range-shape preflight and the reviewer-fast
   hook chain.

## Findings / Fixes Applied

| # | Finding | Source | Fix |
|---|---|---|---|
| A | The worker return claimed the no-self-activation invariant was reused "5 clauses verbatim" in three places (Finding 5 body, Roadmap-To-Work-Order Trace, Acceptance Receipt matrix). Clauses 3-5 are verbatim; clauses 1-2 are correctly adapted (normalizer actor added; LSC-specific derivation dropped). The contract itself is correct; only the worker-return self-description was inaccurate. | reviewer independent diff against ASSF-T3 source | reviewer corrected all three worker-return mentions to "clauses 1-2 adapted, 3-5 verbatim; binding semantics preserved"; no contract change needed |
| B | Worker Finding 3 and the NEW_FINDING delta-ledger row claimed "no new mandatory field needs to be added to the T1 contract." The normalization contract's Provenance Preservation Requirement and Reverification Gate require `security_notes` and `sourceRevision`, which are NOT in ASSF-T1 (T1 carries the related `sideEffects` under Risk-and-authority but no `security_notes`, and no `sourceRevision`). Introducing required fields is allowed for a contract tranche, but the "no new field" wording would mislead a future implementer. | reviewer field-existence cross-check against ASSF-T1 | reviewer corrected Finding 3 and the delta-ledger row to name the two contract-introduced fields; added a "T1 alignment note" to the normalization contract requiring a future tranche to add them to T1 or remap `security_notes` onto T1 `sideEffects` before an executable normalizer is built; recorded the same requirement in the roadmap Finding-To-Governance Learning Disposition |
| C | Active handoff HEAD block recorded `050741bb` (the dispatch's base) but HEAD advanced to `5a4f9591`; the active-session-state gate failed | worker self-report (Finding 1), confirmed independently | reviewer updated the handoff HEAD block per GC-020 in the separate session-sync commit; worker correctly could not fix this under its Forbidden Scope |

The two disposition mapping tables passed independent source-grounding
verification with zero invented disposition labels. The worker's core
deliverable is sound; the only substantive defect was the inaccurate
"no new field" self-description (Finding B), which is corrected and routed
forward as an explicit T1-alignment requirement.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Disposition |
|---|---|---|
| Map external screening dispositions to ASSF-T1 candidate shape | External Screening Disposition Mapping | satisfied - 6 rows, all labels verified against the matrix |
| Map legacy ledger dispositions to ASSF-T1 candidate shape | Legacy Ledger Disposition Mapping | satisfied - 7 rows, all labels verified against the T0.1 ledger |
| Reverification gate rejecting unverifiable claims | Reverification Gate | satisfied - 5-step gate; provider-local and unverifiable sources route to REJECTED_BLOCKED_UNVERIFIED |
| Preserve provenance/license/security | Provenance, License, And Security Preservation Requirement | satisfied - with the contract-introduced `security_notes`/`sourceRevision` T1-alignment note added (Finding B) |
| Reuse ASSF-T3 no-self-activation invariant | No-Self-Activation Invariant | satisfied - clauses 1-2 adapted, 3-5 verbatim; binding semantics preserved (Finding A) |
| Account for internal and external agents | Dual Agent Surface Matrix | satisfied - `CONTRACT_ONLY` and `DEFERRED_WITH_REASON` |

## Dual Agent Surface Matrix

| Agent surface | Disposition |
|---|---|
| INTERNAL_AGENT | CONTRACT_ONLY - the contract defines the mapping, reverification gate, and invariants only; no normalizer is implemented and no authority to set a candidate APPROVED or ACTIVE is granted; verified by reading the contract and confirming no executable normalizer exists in the changed set |
| EXTERNAL_AGENT_CLI_MCP | DEFERRED_WITH_REASON - all normalized candidates carry `externalCliMcpDisposition: DEFERRED_WITH_REASON` as a fixed constant; no CLI/MCP adapter exists; a separate ASSF adapter work order is required |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external screening or legacy ledger disposition -> ASSF-T4 normalization mapping -> ASSF CANDIDATE or REJECTED -> reviewer decision -> UAT -> APPROVED/ACTIVE or REJECTED |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASSF-T4 normalization contract |
| Disposition | candidate intake only; normalization never activates a skill |
| Claim boundary | external and legacy skills remain candidate inputs, not CVF authority; unreverifiable claims are rejected |

## Finding-To-Governance Learning Disposition

| Field | Value |
|---|---|
| Finding | Two worker-return accuracy defects: an over-stated "verbatim" invariant-reuse claim (Finding A) and an inaccurate "no new field" claim that masked two contract-introduced fields (Finding B). Both are the same class the operator flagged earlier - a worker asserting "maps to existing fields / reused verbatim" without a literal line-level cross-check against source. |
| Defect class | `WORKER_EXECUTION_ERROR` - worker asserted "maps to existing fields" and "reused verbatim" without a literal line-level cross-check against source |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Runtime/provider/cost lane | N/A_WITH_REASON - documentation-accuracy finding, not a runtime, provider, or cost finding |
| Disposition | `MACHINE_CHECK_CANDIDATE` - the Mandatory Work Order Source Verification rule already requires literal token cross-checks, but this is the second consecutive ASSF tranche (T3 then T4) where a worker-return self-description of source equivalence ("verbatim", "no new field", "maps to existing") was wrong and was caught only by manual reviewer re-derivation, not by any machine gate. The written rule alone is not a sufficient control for this defect class; no existing checker reads the two cited source files and the worker's equivalence claim together to verify the claim. Escalated from an earlier `RULE_EXISTS` self-assessment in this same review after the operator challenged that classification as too lenient given the repeated occurrence and the real downstream risk (a wrong "no new field" claim conceals a schema gap that would otherwise surface only when an executable normalizer is built). |
| Next action | (1) a future executable-normalizer tranche must resolve the two contract-introduced fields (`security_notes`, `sourceRevision`) against ASSF-T1 before implementation, per the contract's new T1 alignment note and the roadmap Finding-To-Governance Learning Disposition; (2) propose a machine check - a worker-return/completion-review linter that flags equivalence language (`verbatim`, `identical`, `no new field`, `maps to existing`, `unchanged`, `same as`) used about a named source file and requires an adjacent literal grep/diff command-and-result pair in the same finding, with manual-reviewer-required status as the fallback when that pair is absent; this proposal is documentation-only in this review and requires a separate GC-018 to design and build. |

## Epistemic Process Block

| Field | Value |
|---|---|
| Information sources | the normalization contract; the worker-return packet; the external screening matrix; the ASSF-T0.1 legacy ledger; the real ASSF-T1 package contract; the ASSF-T3 bridge contract; the pre-closure range-shape preflight and reviewer-fast gate output |
| Claim basis | EXISTS and LITERAL_INVARIANT for all reviewer verification claims; every disposition label and every ASSF-T1 field re-derived independently against source rather than trusting the worker-return |
| Claim boundary | this review records reviewer verification, the worker-return accuracy repairs, the contract T1-alignment note, the handoff HEAD repair, and closure of the ASSF-T4 normalization contract; it does not claim a normalizer implementation, runtime activation, CLI/MCP adapter, real candidate entry, or any ASSF-T5/T6/T7 scope |
| Uncertainty | none remaining; all disposition labels verified real, both worker-return defects corrected, all gates pass after the repairs |
| Expected Result | the contract would be source-grounded against the screening matrix and legacy ledger, and the invariant would be present |
| Evidence Comparison | confirmed for disposition vocabularies (all real); contradicted for two worker self-descriptions (Findings A and B), both corrected |
| Contradiction Or Gap Disposition | Findings A and B were genuine contradictions between worker self-report and source; both fixed in the worker return and surfaced as a forward T1-alignment requirement |
| Claim Update | worker "5 clauses verbatim" -> "clauses 1-2 adapted, 3-5 verbatim"; worker "no new field" -> "two contract-introduced fields (`security_notes`, `sourceRevision`) require T1 alignment" |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | reviewer accuracy repairs to the ASSF-T4 worker return and a T1-alignment note to the normalization contract, plus this completion review, the roadmap status update, and the handoff HEAD repair |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - reviewer-owned document repair and closure; no normalizer or code changed |
| receiptEvidence | CVF_RECEIPT_PRESENT - pre-closure range-shape preflight and reviewer-fast autorun receipts |
| actionEvidence | ACTION_EVIDENCE_PRESENT - findings table with the two worker-return repairs, the contract note, and the independent verification evidence |
| invocationBoundary | governed local document editing and read-only gate execution only |
| interceptionBoundary | no provider/runtime/API/browser interception claim |
| claimLanguage | reviewed, independently re-verified, corrected, and closed the ASSF-T4 normalization contract |
| forbiddenExpansion | no normalizer code, resolver, generator, real candidate entry, skill activation, CLI/MCP adapter, migration, runtime/provider/live, or public-sync performed or claimed |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the normalization contract references private legacy provenance and
external screening evidence from `.private_reference/legacy/` source
families. Public-safe export requires separate redaction and public-sync
authorization, not sought for this tranche.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T4_CLOSED_PASS_BOUNDED_PENDING_T5_SELECTION` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_FOR_WORKER_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_WORKER_RETURN_2026-06-23.md` | `Status: COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, accepted after reviewer accuracy repairs and handoff repair | PASS |
| Completion or reviewer artifact | this document | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Normalization contract | `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md` | `Status: CANDIDATE` reference contract, source-grounded (all disposition labels verified; T1-alignment note added for the two contract-introduced fields) | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: ASSF-T4 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: ASSF-T4 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported; the external screening matrix and legacy ledger are existing governed sources, not a new import | N/A with reason |
| System loop interlock | this review | T1->T2->T3->T4 are closed in order and consumed; T4 is required before T5; no automatic package activation | PASS |
| Session continuity | active session sync after material commit | separate session-sync lane after material commit | PASS |
| Public export | this review | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Status |
|---|---|
| Contract defines the external screening side | PASS - External Screening Disposition Mapping, all labels verified against the matrix |
| Contract defines the legacy ledger side | PASS - Legacy Ledger Disposition Mapping, all labels verified against the T0.1 ledger |
| Reverification gate routes unverifiable claims to rejected/blocked | PASS - 5-step gate; provider-local sources excluded |
| Provenance/license/security preservation required | PASS - with T1-alignment note for the two contract-introduced fields (Finding B) |
| No-self-activation invariant present | PASS - clauses 1-2 adapted, 3-5 verbatim (Finding A); binding semantics preserved |
| Normalized output always CANDIDATE | PASS - fixed constant in both mapping tables |
| Every external/legacy disposition label exists in source | PASS - independently re-derived; zero invented labels |
| External CLI/MCP disposition present | PASS - `DEFERRED_WITH_REASON` fixed constant |
| No normalizer code, candidate entry, or activation created | PASS - changed set is contract + worker return only |
| No commit performed by worker | PASS - HEAD stayed `5a4f9591` until this reviewer commit |
| Worker-return accuracy defects corrected | PASS - Findings A and B fixed in the worker return |
| Handoff HEAD block repaired | PASS - updated in the separate session-sync commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude reviewer/closer |
| Provider or surface | local workspace |
| Session or invocation | ASSF-T4 completion review, 2026-06-24 |
| Working directory | repository root |
| Command or tool surface | source reads, disposition-label and field cross-check greps, file edits, pre-closure range-shape preflight, reviewer-fast gate, git status |
| Target paths | ASSF-T4 worker return; normalization contract; external screening matrix; T0.1 ledger; ASSF-T1 package contract; ASSF-T3 bridge contract; ASSF roadmap; this completion review |
| Allowed scope source | operator relay of the ASSF-T4 worker return assigning the reviewer role |
| Before status evidence | clean worktree at HEAD `5a4f9591` (`git status --short` showed only the two untracked worker artifacts) |
| After status evidence | ASSF-T4 closed bounded pending material commit; worker-return defects corrected; contract T1-alignment note added; roadmap status `ASSF_T4_CLOSED_PASS_BOUNDED_PENDING_T5_SELECTION` |
| Diff evidence | `git status --short`; `git diff --check`; reviewer-fast gate output |
| Approval boundary | reviewer-owned closure and accuracy repair only; no normalizer, code, or disposition-mapping change |
| Claim boundary | full normalization-contract closure; no ASSF-T5/T6/T7 scope |
| Agent type | reviewer/closer |
| Invocation ID | `cvf-assf-t4-completion-review-2026-06-24` |
| Expected manifest | normalization contract (T1-alignment note), worker return (accuracy repairs), this completion review, roadmap status update, GC-018/work-order status, handoff HEAD repair |
| Actual changed set | normalization contract, worker return, this completion review, roadmap, GC-018, work order, handoff HEAD block |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This review records reviewer verification, the two worker-return accuracy
repairs, the contract T1-alignment note, the handoff HEAD repair, and
closure of the ASSF-T4 External And Legacy Intake Normalization contract.
It does not implement a normalizer, resolver, generator, or any code; it
does not create a real skill candidate, activate any skill, run a corpus
scan or migration, implement a CLI/MCP adapter, run provider/live proof,
public-sync, or authorize ASSF-T5. ASSF-T5 (Composition, Dependency,
Conflict, And Capability Controls) requires a fresh, explicit operator
selection and a new source-verified GC-018/work order; any future
normalizer implementation must cite this normalization contract as
authority and must first resolve the two contract-introduced fields
(`security_notes`, `sourceRevision`) against ASSF-T1.
