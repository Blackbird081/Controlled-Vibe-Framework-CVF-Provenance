# CVF GC-018 Baseline - TPGR-R2G Generalized Absorption Routing Feasibility Assessment

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Batch ID: TPGR-R2G

Dispatch base head: `9e0dba8fff772675c202204a865a0dbf43e45e95`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: CVF reviewer/orchestrator

Worker target: delegated assessment worker, role-based and provider-neutral

## Purpose

Authorize one non-implementation feasibility assessment of the generalized
CVF absorption-routing boundary. The worker must evaluate whether TPGR can
route the existing knowledge lifecycle across six source archetypes with less
irrelevant ceremony, without duplicating lifecycle evidence, weakening
semantic review, or promoting any outside source to CVF authority.

## Value / Cost Decision

This tranche is justified because the prior R2 design sampled only the
cheapest accepted-corpus case. One bounded comparative assessment is cheaper
than implementing a router whose maintenance cost or authority overlap is not
yet known. The assessment must separate unavoidable semantic-intake cost from
incremental TPGR cost and must stop at planning evidence.

## Decision / Baseline

`APPROVE_GENERALIZED_R2_FEASIBILITY_ASSESSMENT`

The approval authorizes the paired work order and its two worker outputs only.
R3-R9, rule/checker/registry/catalog edits, selective execution, T15, new
source intake, network access, runtime, provider/live, public, deployment, and
production actions remain unauthorized.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id TPGR-R2G --title "Generalized Absorption Routing Feasibility Assessment" --date 2026-08-17 --base 9e0dba8fff772675c202204a865a0dbf43e45e95 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced all placeholders with the approved R2G authority, six-archetype contract, exact paths, evidence boundaries, and commands |
| checkerReadAheadConfirmation | dispatch, routing, ADIF, structural, trace, public-disposition, and worker-return checker sources reviewed before authoring |
| docOnlyNewFields | archetype evidence map; Layer A cost; TPGR overhead; completion-claim token compatibility; authority-delta candidate manifest |
| claimBoundary | dispatch authoring provenance only; no behavior or selective-execution claim |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_core.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_work_order_dispatch_quality_artifacts.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | dispatch envelope placement; status and commit-mode tokens; source-verification columns; ADIF query and defect IDs; routing manifest shape; operation-trace labels; worker-return contract fields; exact public disposition |
| gateRunPurpose | confirm the source-reviewed baseline and paired work order satisfy current dispatch evidence shape |
| claimBoundary | checker conformance for dispatch artifacts only; no assessment result or implementation proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json`

Returned defects: 22, not truncated.

`ADIF-0001`, `ADIF-0002`, `ADIF-0014`, `ADIF-0015`, `ADIF-0020`,
`ADIF-0021`, `ADIF-0028`, `ADIF-0029`, `ADIF-0033`, `ADIF-0044`,
`ADIF-0045`, `ADIF-0051`, `ADIF-0052`, `ADIF-0007`, `ADIF-0016`,
`ADIF-0017`, `ADIF-0024`, `ADIF-0031`, `ADIF-0039`, `ADIF-0043`,
`ADIF-0049`, `ADIF-0006`.

Dispatch impact: use exact paths and source sections; treat the outside review
as advisory; avoid false applicability markers; bind the no-commit return
contract; keep protected paths forbidden; verify command help; prevent
aggregate claims from exceeding archetype evidence; and split material from
continuity commits.

## Authorization / Source

Operator approval is the `next` instruction following the committed R2G
reconciliation at `2e7f986095cf50a990344c443c47b3090df41095` and continuity
commit `9e0dba8fff772675c202204a865a0dbf43e45e95`.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| generalized R2G contract and six archetypes | planning authority | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_CRITIQUE_RECONCILIATION_AND_R2_RESCOPE_2026-08-17.md` | Generalized R2 Feasibility Assessment; R2 Deliverables And Exit | existing governed review path | R2G planning owner | ACCEPT |
| TPGR remains shadow-only | routing authority | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | TPGR-T0 Legacy Full-Gate Interlock | `selectiveExecutionAuthorized` | TPGR standard | ACCEPT |
| lifecycle already has a recorded router gap | authority boundary | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | Enforcement Gap | existing chain-map path | knowledge intake chain | ACCEPT |
| file processing and owner mapping remain existing-owner semantics | lifecycle authority | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | Central Core; Required Ledger Semantics | existing standard path | lifecycle core | ACCEPT |
| accepted derived packs reuse fresh evidence by cluster | evidence-reuse authority | `docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md` | Absorption Efficiency And Provenance Reuse | `semanticReviewUnit` | mixed-origin standard | ACCEPT |
| corpus registration applies to corpora and project corpora | registry authority | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | Mandatory Agent Rules; Rule 1; Rule 5 | existing standard path | GC-051 registry | ACCEPT |
| current generated registry contains 170 entries | machine evidence | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | `corpora` generated array | `corpora` | generated GC-051 aggregate | ACCEPT |
| worker may write only two outputs | dispatch decision | `docs/baselines/CVF_GC018_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md` | Decision / Baseline; Expected Worker Manifest | paired exact paths | TPGR-R2G | ACCEPT |

## Archetype Evidence Map

| Archetype | Primary governed evidence | Use boundary |
| --- | --- | --- |
| A1 new upstream corpus | `docs/audits/CVF_EAIC_KR_R1_CVF_23_07_EXTERNAL_REPOSITORY_INTAKE_AUDIT_2026-07-23.md` | historical first-intake evidence; no new fetch |
| A2 mixed-origin local synthesis | `docs/audits/CVF_RSPB_AI_T0_DUAL_CORPUS_INTAKE_AUDIT_2026-08-15.md` | accepted 559 plus 205 accounting evidence |
| A3 accepted-corpus cluster | `docs/reviews/CVF_RSPB_AI_T11_CAPABILITY_WORKSPACE_PROFILE_AND_BOOTSTRAP_POLICY_BUNDLE_VALIDATION_KERNEL_COMPLETION_2026-08-17.md` | selected-cluster regression only |
| A4 pinned-source delta | `docs/audits/CVF_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md` | historical delta route; no current source refresh |
| A5 small named advisory item | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_EXTERNAL_CRITIQUE_2026-08-17.md` | bounded review input, not corpus completion |
| A6 downstream project boundary | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` Rule 5 plus current `PROJECT_SOURCE` registry entries | authority-boundary assessment only |

## Assessment Contract

The worker must produce one evidence-backed assessment that:

1. maps existing Layer A owners without inventing a new lifecycle;
2. tests the conditional lifecycle graph across A1-A6;
3. separates required semantic work from TPGR metadata and gate cost;
4. reports observed values separately from projections and unknowns;
5. assesses command-universe mapping feasibility without editing the catalog;
6. evaluates scoped completion-claim tokens without global migration claims;
7. proposes an exact authority-delta manifest but changes none of those paths;
8. returns one allowed disposition from the R2G plan.

## Expected Worker Manifest

- `docs/assessments/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md`
- `docs/reviews/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_WORKER_RETURN_2026-08-17.md`

No other path is worker-owned.

## Evidence / Verification

Before dispatch, both artifacts must pass routing and dispatch gates. During
execution, the worker records source sections, command counts, elapsed times
when actually measured, projection assumptions, unknowns, exact status/diff,
and the no-commit boundary. Reviewer acceptance remains separate.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | accepted advisory critique -> CVF reconciliation -> approved feasibility assessment |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing TPGR and lifecycle owners |
| Disposition | COMPARISON_AND_COST_ASSESSMENT_ONLY |
| Claim boundary | no outside-source authority promotion and no new corpus intake |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: the worker compares existing governed receipts and artifacts;
  this tranche opens no repeat scan, source refresh, or completeness update.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - A1-A6 are existing evidence
  fixtures for a routing assessment; no corpus manifest, ledger, or completeness
  verdict is created or changed.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE_PLANNING.

Expected Result / Prediction: existing lifecycle owners plus a thin TPGR
interface should be cheaper and safer than a duplicate lifecycle.

Evidence Comparison: A1-A6 must expose where inheritance saves work, where
first-intake controls remain unavoidable, and where evidence is insufficient.

Contradiction Or Gap Disposition: unknown command closure, negative net value,
duplicate evidence, or authority ambiguity narrows or stops the proposal.

Claim Update: only the worker's bounded R2G disposition may update planning;
no rule or execution state changes.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | CVF reviewer/orchestrator as dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | TPGR-R2G dispatch authoring, 2026-08-17 |
| Working directory | repository root |
| Command or tool surface | governed reads, registry query, ADIF resolver, scaffold preview, apply patch, dispatch gates, Git |
| Target paths | paired GC-018 baseline and work order |
| Allowed scope source | operator `next` approving the recommended generalized R2G assessment |
| Before status evidence | clean HEAD `9e0dba8fff772675c202204a865a0dbf43e45e95` |
| After status evidence | two dispatch artifacts only before material commit |
| Diff evidence | exact two-path reconciliation before commit |
| Approval boundary | R2G assessment dispatch only |
| Claim boundary | no assessment result, implementation, source intake, selective execution, T15, runtime/live/public/deploy/production |
| Agent type | dispatcher/reviewer |
| Invocation ID | `tpgr-r2g-dispatch-20260817` |
| Expected manifest | this baseline and paired work order |
| Actual changed set | required to equal the expected manifest before material commit |
| Manifest delta | zero required |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | documentation-only feasibility assessment |
| claimDisposition | CLAIM_REJECTED_NO_EXECUTION: no execution-control or selective enforcement claim |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: existing governed receipts are comparison inputs only; no runtime receipt is created |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime or outside-system action is authorized or observed |
| invocationBoundary | local read-only commands and two governed output files |
| interceptionBoundary | no wrapper, proxy, hook, runtime gate, or agent-control interception |
| claimLanguage | measured, projected, unknown, or blocked must remain distinct |
| forbiddenExpansion | authority edits, source intake, runtime/provider/live/public/deploy/production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private planning dispatch; public-sync is not authorized.

## Claim Boundary

This baseline authorizes only the paired no-commit R2G assessment work order.
It does not authorize implementation, modification of any proposed authority
path, selective execution, T15, new source acquisition, network use, runtime,
provider/live proof, public sync, deployment, destructive action, or production.
