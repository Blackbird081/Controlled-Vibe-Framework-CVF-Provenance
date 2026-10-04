# CVF GC-018 - NIS T1A Intent Specification Review

Memory class: governed-maintenance-baseline
docType: gc018
Status: APPROVED_FOR_LOCAL_IMPLEMENTATION
Date: 2026-10-05
Batch ID: CVF-NIS-T1A
baseHead: 26dfe4d6a30fdccd3afe1e0669cfca4e9918bcc8
providerExecutionAuthority: FORBIDDEN

## Purpose

The operator accepted the selected NIS-T1A build on 2026-10-05: "dong y, tiep".
Implement a bounded local requirements-review consumer in the existing Web
app-builder export surface. Local authors, implements and verifies directly;
no delegated worker or independent reviewer identity is claimed. This new
operator authority supersedes the earlier review-only restriction for this
bounded implementation, not for previously parked projects or effects.

## Scope / Target / Owner Boundary

Existing CVF Web consumer; reversible source edits and focused structural UI
and typed-transformation tests. Reuse the app_builder_complete template and
generator. Preserve unknown/conflict decisions, current revision, review
acknowledgement invalidation and exact exported draft. No network or model
invocation. No durable content acceptance, build admission or semantic oracle.

Allowed source paths, prefix EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/:

- lib/intent-spec-review.ts
- lib/intent-spec-review.test.ts
- components/IntentSpecReview.tsx
- components/IntentSpecReview.test.tsx
- components/SpecExport.tsx
- components/SpecExport.test.tsx
- components/SpecExportQuickLinks.tsx

Scope delta before source edit: SpecExport currently has 1299 lines against its
approved maximum 1300. Its existing exception requires helper/panel extraction
before the next workflow change. Extract the current quick-paste link block to
SpecExportQuickLinks.tsx so this seam shrinks; preserve link behavior. This is
the sole additional implementation path, not a wider export refactor.

Allowed admission artifact: this baseline. Local ignored evidence and receipts
belong under .cvf/runtime/nis-t1a-20261005. A later result artifact may be
prepared after verification; this baseline does not assert a closed tranche.
Nine prior dirty paths are pinned in the entry snapshot and must be preserved.
No deletion, rename, dependency installation, API/store/gateway modification,
provider use, dispatch, push or deployment belongs to this scope.
The operator subsequently authorized the bounded material commit on 2026-10-05:
"commit. tiep". Commit only this baseline and the seven named source paths;
preserve the nine prior dirty paths. This does not authorize public export.
CCMA, S05/C1/send/B2, Q001/Q004 effects, P11 and FLAL T4/T5 retain their boundaries.

## Source / Predecessor Evidence

Operator-authorized priority: NIS-T1A guided requirements refinement and revision
review, followed conditionally by content-acceptance binding and build-ready
planning. Selected local proposals remain advisory inputs, not runtime authority.
Current governed owner is
docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md;
reuse direction is governed by
docs/reference/CVF_KNOWLEDGE_ABSORPTION_AND_EXTENSION_PRIORITY_STANDARD_2026-04-13.md.
Startup uses CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json,
CVF_SESSION_MEMORY.md and AGENT_HANDOFF_V63_2026-09-18.md. Current mode remains
cvf_ncr_p10_closed_p11_parked; the operator's new bounded implementation scope
does not revive FR2 or require its terminal work order to execute this consumer.

## Source Verification Block

| Claimed item | Source file | Verified section | Disposition |
|---|---|---|---|
| Non-coder brief and builder handoff already exist | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/development.ts | app_builder_complete | ACCEPT |
| Existing export integration seam | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx | SpecExport; generateSpec | ACCEPT |
| Form values reach export | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/DynamicForm.tsx | SpecExport render | ACCEPT |
| Field gate only validates required presence | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-gate.ts | evaluateSpecGate | ACCEPT |
| Routing clarification is not business quality proof | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-router-clarification.ts | clarification depth and phase/scope questions | ACCEPT |
| Design owner | DESIGN.md (canonical contract) | Form workflow; Accessibility and Language | ACCEPT |

## Decision / Baseline / Proposed Tranche

Proceed with a thin in-browser drafting and review layer. Questions are visible
review prompts, not AI deductions. User-entered answers have explicit source
and disposition. Conflicts and unanswered prompts stay in the record. Scope
changes retain prior text but invalidate affected decisions for reconfirmation.
Packet-mode/language/context changes invalidate review acknowledgement. The
exact current draft is used for preview/copy/download and the existing send
callback; a pending draft is not mislabeled as reviewed or build-ready.
Preserve existing modes and behavior for unrelated templates. Spec Kit runtime
selection stays conditional; no upstream files or payloads are copied here.

## Implementation Contract

1. A bounded bilingual review panel appears only for app_builder_complete.
2. Six business-review dimensions have stable IDs, explicit answers, optional
   not-applicable reasons, conflict/open dispositions and source dependencies.
   Showing a few prompts per view never discards the remaining queue.
3. Draft revision identity binds exact inputs, decisions and generated packet.
   Acknowledgement is ephemeral review evidence, not signed actor acceptance.
4. Material source corrections preserve older answers visibly and require
   affected decisions to be reviewed again. No silently accepted stale answer.
5. Packet includes a plain-language decision/provenance/blocker readout and
   spec-only next-step limit. Future builder directions remain conditional.
6. Local UI/transformation tests check fidelity and revision mechanics only.
   They assert no AI governance, provider behavior or production readiness.

## Risk / Corrective Action

Prompt coverage is bounded and cannot prove complete business understanding.
Session state disappears on reload; label that limit. Empty text, conflicting
rules or stale acknowledgement cannot become complete specification claims.
Do not use raw user text as executable instructions or parse it as authority.
Do not change existing backend approvals to imitate durable acceptance.

## Evidence / Verification Requirements

Pre-implementation autorun gate must pass before source mutation. Record exact
initial dirty paths and hashes. Run focused tests for revision invalidation,
unknown retention, conflict and not-applicable reason handling, current export,
bilingual UI and unrelated-template regressions. Run typecheck without a
generated-output build step. Preserve all failures and distinguish baseline
diagnostics from introduced regressions. Hash the changed source and final diff.
No full framework build, mock AI proof or real provider call is required for
this structural UI/transformation claim. Real AI governance/value proof remains
a separately admitted action before any such claim.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON - named local consumer implementation, not a corpus
scan or external repository absorption. No repository-wide absence claim.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION - prior upstream comparisons inform the optional
future choice; this implementation copies no upstream source/template payload,
performs no acquisition and makes no runtime integration claim.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named seven-file consumer scope; no complete repository scan or source-ingestion claim

## Epistemic Process Block

Expected Result / Prediction: visible decisions and exported draft stay aligned
with edits; stale review never appears current; unknown/conflict items persist.
Evidence Comparison: recorded after the planned checks, not asserted here.
Contradiction Or Gap Disposition: semantic completeness, durable acceptance,
provider behavior and novice UX remain unproved by structural test success.
Claim Update: authorized implementation only; no test or closure PASS yet.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_baseline_update_compat.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_gc018_stop_boundary_semantics.py; governance/compat/check_agent_operation_trace.py |
| literalTokensReviewed | baseline source/decision/evidence headings; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; claimBoundary; Resolver query; Returned defects: NONE_RETURNED; COMPARISON_ONLY_NO_ABSORPTION |
| gateRunPurpose | confirmation of bounded source authority and admission before edits; not first discovery of checker requirements |
| claimBoundary | local UI and typed transformation only; no AI governance or durable acceptance proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`reviewer`, role=`reviewer`, lifecyclePhase=`review`.
Command: `python -B governance/compat/run_adif_defect_resolver.py --task-class reviewer --role reviewer --lifecycle-phase review --json`.
Returned defects: NONE_RETURNED.
The actual resolver returned zero candidates on 2026-10-05 before authoring.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

Bounded NIS-T1A admission under the operator's new instruction. One Local actor
implements and verifies. No independent review, dispatch-ready work order,
committed closure, provider/live, content acceptance or production claim.
