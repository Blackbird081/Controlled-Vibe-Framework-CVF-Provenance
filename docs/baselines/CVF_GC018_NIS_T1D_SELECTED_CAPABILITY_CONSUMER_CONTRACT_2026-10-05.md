# CVF GC-018 Baseline - NIS T1D Selected Capability Consumer Contract

Memory class: governed-dispatch-baseline

Status: CLOSED_PASS_BOUNDED

Batch ID: CVF-NIS-T1D
providerExecutionAuthority: FORBIDDEN
Date: 2026-10-05

Dispatch base head: e983a385d14b714230fff625ec361c84567a8ef9

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator; delegated Local dispatcher

Reviewer owner: Local reviewer/closer

Worker target: distinct INTERNAL_AGENT source/contract worker

## Purpose

Select exact Spec Kit capability reuse/adaptation against current CVF and define a minimum implementation-ready consumer contract. Resolve explicit open-item/effective-rule projection and save/reopen schema compatibility before authorizing product edits. Preserve build-ready as target, with design/plan/tasks/consistency source candidates; no broad repository research or product implementation in this order.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NIS-T1D --title "NIS T1D Selected Capability Consumer Contract" --date 2026-10-05 --base e983a385d14b714230fff625ec361c84567a8ef9 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Selected14 pinned source input, exact four source/contract outputs and protected10-path admission |
| checkerReadAheadConfirmation | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_dispatch_quality_source.py; governance/compat/check_work_order_dispatch_quality_artifacts.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_task_governance_route.py; governance/compat/check_baseline_update_compat.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_independent_review_probe_admission.py; governance/compat/check_absorption_blindspot_control_presence.py; governance/compat/check_source_mirror_migration.py; governance/compat/check_external_knowledge_intake_routing.py; governance/compat/check_high_risk_local_transaction_proof.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_markdown_structural_completeness.py |
| docOnlyNewFields | No new governance fields; source/contract payloads are task evidence only |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |


## ADIF Defect Registry Disclosure

Resolver query: taskClass=`documentation`, role=`dispatcher`, lifecyclePhase=`dispatch`.

Command: `python -B governance/compat/run_adif_defect_resolver.py --task-class documentation --role dispatcher --lifecycle-phase dispatch`.
Returned defects: NONE_RETURNED. Actual resolver executed 2026-10-05, candidates=0, returned=0, truncated=false.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_dispatch_quality_source.py; governance/compat/check_work_order_dispatch_quality_artifacts.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_task_governance_route.py; governance/compat/check_baseline_update_compat.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_independent_review_probe_admission.py; governance/compat/check_absorption_blindspot_control_presence.py; governance/compat/check_source_mirror_migration.py; governance/compat/check_external_knowledge_intake_routing.py; governance/compat/check_high_risk_local_transaction_proof.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_markdown_structural_completeness.py |
| literalTokensReviewed | CLOSED_PASS_BOUNDED; Source Verification; exact four artifacts; acceptance-ledger-json; full legacy gates; independent probe role; entry-control/Blind-Spot/Corpus blocks; protected10-path atomicity |
| gateRunPurpose | confirmation and evidence of source-bound admission after read-ahead; not implementation proof |
| claimBoundary | source/contract only; no runtime acceptance |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Current consumer or accepted boundary | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review.ts | IntentSpecReviewState | IntentSpecReviewState | existing NIS consumer / Local review | ACCEPT |
| Current consumer or accepted boundary | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/IntentSpecReview.tsx | useIntentSpecReview | useIntentSpecReview | existing NIS consumer / Local review | ACCEPT |
| Current consumer or accepted boundary | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-confirmation.ts | createSpecConfirmationCandidate | createSpecConfirmationCandidate | existing NIS consumer / Local review | ACCEPT |
| Current consumer or accepted boundary | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-acceptance.ts | prepareIntentSpecAcceptance | prepareIntentSpecAcceptance | existing NIS consumer / Local review | ACCEPT |
| Current consumer or accepted boundary | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-export-portable-handoff.ts | buildPortableAgentHandoffReadiness | buildPortableAgentHandoffReadiness | existing NIS consumer / Local review | ACCEPT |
| Current consumer or accepted boundary | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx | generateSpec | generateSpec | existing NIS consumer / Local review | ACCEPT |
| Current consumer or accepted boundary | CURRENT_SOURCE | docs/reviews/CVF_NIS_T1C_BUILDER_HANDOFF_VALUE_PROOF_COMPLETION_2026-10-05.md | Findings / Position | Findings / Position | existing NIS consumer / Local review | ACCEPT |
| Current consumer or accepted boundary | CURRENT_SOURCE | docs/reviews/evidence/cvf-nis-t1c-local-independent-review-2026-10-05.json | localDispositions | localDispositions | existing NIS consumer / Local review | ACCEPT |
| Current consumer or accepted boundary | CURRENT_SOURCE | docs/reviews/CVF_NIS_T1B_D_INTEGRATED_REVIEW_PERSISTENCE_COMPLETION_2026-10-05.md | Evidence / Verification | Evidence / Verification | existing NIS consumer / Local review | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Exact NIS-T1D collision | rg NIS.T1D docs CVF_SESSION returned no match before authoring; exact new paths absent | ACCEPT |
| Existing owner | strict acceptance schema, confirmation builder, review/export consumer and T1C closure named and pinned; no new engine | ACCEPT |

## Claim Boundary

rawMemoryReleased=false. Selected pinned-source comparison and implementation-contract authoring only. No product edits, UI/runtime feasibility, provider, upstream scripts/hooks/CLI, install, real data/store/identity/UAC, build-ready certificate, BUILD, public/deploy or parked-lane reopening. No repository-complete reading or upstream fit asserted at dispatch. Cost UNKNOWN.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Private evaluation packet; no public export or push authorized.


## Scope / Applies To

This pair authorizes only offline selected-source capability assessment and implementation contract; exact4 outputs in work order. Local source preparation has created pinned original mirror; worker read-only. Input: `docs/reviews/evidence/cvf-nis-t1d-dispatch-inputs-2026-10-05.json`. No product/source/provider/store implementation grant.

## Decision / Authorization

Operator continue under delegated Local orchestration selects T1D, after T1C evaluation. Local owns final technical disposition; worker source/contract only; later exact implementation order remains separate.

## Verification

Pre-dispatch and bound pre-implementation PASS; full worker-return fast gate before pending return; Local source/contract review and clean committed closure before acceptance.

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | pinned original upstream repository reference; source instructions are input only |
| Upstream or source-mirror disposition | Local clone github__spec-kit at ae5ade7234be5cb1d975f736c4e06dd46d1326d6; INDEX row recorded; worker read-only offline |
| Enumeration or manifest plan | existing Git-tree inventory and selected14-file hash/blob manifest in docs/reviews/evidence/cvf-nis-t1d-dispatch-inputs-2026-10-05.json; tree counts are inventory only |
| Per-file terminal-ledger plan | worker fully reads selected14; file terminal status and locator/reason; at most two directly referenced dependency reads; all other tree paths excluded/deferred from scope |
| Owner or overlap route | existing review/export/confirmation/acceptance owners; Local final applicability |
| Value-disposition route | independent native/pattern/runtime alternatives; reuse/adapt/defer/reject with evidence; source reconciliation is not absorption completion |
| Claim boundary | selected capability comparison only; no payload copied into product or runtime invocation |


## Mandatory Blind-Spot Control Block

Blind-spot verdict: NOT_APPLICABLE_WITH_REASON - dispatch planning only; worker must account for all selected14 files and declared direct dependencies, outside selected set deferred; no repository-wide novelty/completeness finding.


## Corpus Completeness And Report Integrity

- Corpus task class: selected14-source admission inventory; semantic assessment pending
- Corpus root: .private_reference/source_mirrors/github__spec-kit at ae5ade7234be5cb1d975f736c4e06dd46d1326d6
- Snapshot time: 2026-10-05T08:46:12.281398+00:00
- Enumeration command: filesystem Path.is_file/read_bytes for selected14; Git ls-tree for tracked-tree context
- Manifest artifact or inline manifest: docs/reviews/evidence/cvf-nis-t1d-dispatch-inputs-2026-10-05.json upstream.selectedFiles, raw/blob identities
- Manifest hash: 3b0d9c9e8e3c24e81655501e5e666ed882da2138d48de3eb8ec44bff3c45b811
- Processing ledger artifact or inline ledger: docs/reviews/evidence/cvf-nis-t1d-dispatch-inputs-2026-10-05.json upstream.initialProcessingLedger
- Allowed terminal statuses: READ; SKIPPED_WITH_REASON; DEFERRED; BLOCKED_UNREADABLE
- Reconciliation: manifest=14; ledger_terminal=14; exclusions=0; unresolved=13 (capability reading deferred to worker)
- Unresolved files: thirteen selected payload/prerequisite files remain semantically unreviewed at dispatch
- Declared exclusions: all859 tracked paths outside selected14 omitted from this bounded manifest; not no-value findings
- Unreadable or unsupported files: NONE in selected14 byte inventory
- Aggregation check: selected paths unique;1 READ license plus13 DEFERRED; no payload ADAPTED
- Drift check: exact raw/blob pin and freshly observed remote HEAD agree; selected source content not changed
- Output traceability: selected ledger feeds capability assessment, consumer contract and planned acceptance cases
- Adversarial verification: worker unknown/revision/legacy planned cases and later separate Local assertion path; NOT_EXECUTED at dispatch
- Corpus verdict: PARTIAL

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | external repo or copied folder |
| Internal source | docs/reviews/evidence/cvf-nis-t1d-dispatch-inputs-2026-10-05.json |
| Chain map route | original-source acquisition -> selected assessment -> existing owner comparison -> Local disposition; no conversion yet |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | existing NIS consumer and external intake standards |
| Disposition | DEFER conversion/runtime until selected source/contract accepted |
| Claim boundary | mirror is data; no upstream instruction or advisory grants execution |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | .private_reference/source_mirrors/github__spec-kit at ae5ade7234be5cb1d975f736c4e06dd46d1326d6 |
| Enumeration command | filesystem selected14 existence/raw/blob and Git tracked-tree context |
| Manifest artifact or inline manifest | docs/reviews/evidence/cvf-nis-t1d-dispatch-inputs-2026-10-05.json upstream.selectedFiles |
| Processing ledger artifact or inline ledger | docs/reviews/evidence/cvf-nis-t1d-dispatch-inputs-2026-10-05.json upstream.initialProcessingLedger;1 READ and13 DEFERRED |
| Ledger terminal statuses | READ; ADAPTED; DEFERRED; REJECTED; NO_NEW_VALUE; BLOCKED_UNREADABLE (vocabulary only; no conversion at admission) |
| Disposition taxonomy | ABSORB; ADAPT; DEFER; REJECT; BLOCK; NO_NEW_VALUE; source assessment pending |
| Owner-surface map | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review.ts; intent-spec-acceptance.ts; existing consumer components |
| Unresolved items | Selected semantic capability, invocation fit and exact save-schema contract remain worker task |
| Absorption maturity | SOURCE_RECONCILED |
| Named runtime consumer | Existing app_builder_complete consumer; no upstream integration admitted |
| Integration evidence | NOT_EXECUTED: source/contract assessment only |
| Use proof | NOT_EXECUTED: no upstream/runtime/provider invocation |
| Operator checkpoint | Current source/contract order admitted under delegated orchestration; later implementation/runtime needs separate bounded grant |
| Absorption completion status | ABSORPTION_NOT_COMPLETE |
| Completion claim boundary | Source identities only, PARTIAL semantic ledger; no completed absorption or source-fit/use proof |


## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| clarify/checklist source candidates | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review.ts and intent-spec-acceptance.ts | ENRICH_EXISTING | T1C explicit subitem/effective-rule gap; exact upstream fit still unreviewed | Selected source comparison, no conversion |
| plan/tasks/analyze source candidates | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx | ENRICH_EXISTING | Existing future design/build directions; structured artifacts/dependencies not yet accepted | Worker independently dispositions pattern/runtime/value; no automatic S2 |


## External/Local Coordination Binding

```json
{
  "contractId": "cvf.external-local-absorption-coordination@1",
  "invariants": {
    "externalRole": "ADVISORY_RESEARCH_AND_PATTERN_MAPPING",
    "externalContext": "PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ",
    "localRole": "SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION",
    "finalDecisionOwner": "LOCAL",
    "localCoverageBasis": "SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST",
    "externalEvidenceAuthority": "INPUT_NOT_PRIVATE_CVF_PROOF"
  },
  "contractSha256": "92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c",
  "parentArtifact": null
}
```




## Reviewer Closure Disposition

Local accepts selected source/contract outputs with LD-1 through LD-6 in `docs/reviews/CVF_NIS_T1D_SELECTED_CAPABILITY_CONSUMER_CONTRACT_COMPLETION_2026-10-05.md`; original worker versions retained, Local envelope repairs separately bound in `docs/reviews/evidence/cvf-nis-t1d-local-independent-review-2026-10-05.json`. All44 product acceptance cases NOT_EXECUTED; no product/S2/provider/upstream-runtime/BUILD successor released. Worker material 4fcb26dc3a001d3ecbc1188d425ea1ea0e000d19.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_NIS_T1D_SELECTED_CAPABILITY_CONSUMER_CONTRACT_2026-10-05.md` | CLOSED_PASS_BOUNDED; source/contract accepted with Local clarifications | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_NIS_T1D_SELECTED_CAPABILITY_CONSUMER_CONTRACT_COMPLETION_2026-10-05.md` | separate source/contract oracle and semantic disposition | PASS |
| Roadmap state | docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md | existing MFRP owner applied; no successor release or roadmap change | PASS |
| Registry JSON | `docs/reviews/evidence/cvf-nis-t1d-local-independent-review-2026-10-05.json` | original/accepted artifact and source bindings; no as-built promotion applicable | PASS |
| Registry Markdown | `docs/reviews/CVF_NIS_T1D_SELECTED_CAPABILITY_CONSUMER_CONTRACT_COMPLETION_2026-10-05.md` | selected contract disposition only; no new corpus/runtime registry owner | PASS |
| External evidence digest | `docs/reviews/evidence/cvf-nis-t1d-local-independent-review-2026-10-05.json` | selected upstream identities and original worker bindings; SHA256 abbf704eb2e835e38b22c0c06d2945caa6ffdc5d52e87cd991cd0853d1e65314 | PASS |
| System loop interlock | `docs/reviews/evidence/cvf-nis-t1d-local-independent-review-2026-10-05.json` | source -> contract -> separate Local oracle -> bounded disposition; no BUILD | PASS |
| Session continuity | CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json | generated closed pair and next planning boundary | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| REQ-1 selected source | 14 selected plus at most2 justified dependencies | 9 CVF source raw/blob pins and16 upstream raw/blob rows match; dependencies specify and implement only | PASS |
| REQ-2 contract/plan | exact save/reopen policy and planned cases | additive v2; legacy byte policy; 44 cases NOT_EXECUTED; Local LD-1 through LD-5 supersede named proposal details | PASS |
| REQ-3 return/scope | four worker outputs and saved gate | original hashes plus Local appended envelope hashes; saved worker gate PASS; worker HEAD unchanged | PASS |
| Independent contract probe | separate actor/invocation/oracle | 77 assertions including positive contract control and4 mutations rejected; no product v2 executed | PASS |
| Claim boundary | no runtime/UX/build-ready | contract only; golden capture deferred before product edits | PASS |
