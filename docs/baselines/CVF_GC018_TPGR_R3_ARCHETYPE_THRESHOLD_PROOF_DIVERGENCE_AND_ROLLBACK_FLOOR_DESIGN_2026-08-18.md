# CVF GC-018 Baseline - TPGR-R3 Archetype Threshold, Proof, Divergence, And Rollback Floor Design

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Batch ID: TPGR-R3

Dispatch base head: `e6f6f4916b8eec27e0a4877e98b325f993b4552e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: CVF reviewer/orchestrator

Worker target: delegated design worker, role-based and provider-neutral

## Purpose

Authorize one documentation-only R3 design pass that pre-registers proof,
cost, divergence, and rollback floors for each R2G archetype. The design must
make route selection fail closed, prevent worker self-downgrade, and keep TPGR
as a thin router over existing Layer A owners.

## Value / Cost Decision

R2G found bounded feasibility but left TPGR-specific overhead, long-term
maintenance, selective-command equivalence, and live router behavior projected
or unknown. R3 is the minimum design step needed before implementation
planning: it sets measurable entry and stop thresholds without changing any
standard, checker, registry, catalog, hook, or runtime surface.

## Decision / Baseline

`AUTHORIZE_FRESH_R3_THRESHOLD_DESIGN_DISPATCH`

The approval authorizes only the paired work order and exact two worker output
files. It does not authorize R4-R9, implementation, selective execution,
standard/checker/registry/catalog/hook edits, T15, new source intake, network,
runtime, provider/live, public, deployment, or production action.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id TPGR-R3 --title "Archetype Threshold Proof Divergence And Rollback Floor Design" --date 2026-08-18 --base accd005c1786f1e5e3d1950c706ba5f117424f32 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with R3 authorization, six-archetype threshold contract, anti-self-downgrade controls, exact manifests, evidence boundaries, and commands |
| checkerReadAheadConfirmation | dispatch, routing, ADIF, structural, trace, public-disposition, and worker-return checker sources reviewed before authoring |
| docOnlyNewFields | route outcome; proof floor; cost ceiling; divergence tolerance; freshness invalidator; rollback trigger; self-downgrade resistance |
| claimBoundary | dispatch provenance only; no implementation or selective-execution claim |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_core.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_work_order_dispatch_quality_artifacts.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | dispatch envelope placement; status and commit-mode tokens; source-verification columns; ADIF query and IDs; routing manifest; operation-trace labels; worker-return contract; exact public disposition |
| gateRunPurpose | confirm source-reviewed dispatch shape before worker execution |
| claimBoundary | checker conformance only; no R3 design result or runtime proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json`

Returned defects: 22, not truncated.

`ADIF-0001`, `ADIF-0002`, `ADIF-0014`, `ADIF-0015`, `ADIF-0020`,
`ADIF-0021`, `ADIF-0028`, `ADIF-0029`, `ADIF-0033`, `ADIF-0044`,
`ADIF-0045`, `ADIF-0051`, `ADIF-0052`, `ADIF-0007`, `ADIF-0016`,
`ADIF-0017`, `ADIF-0024`, `ADIF-0031`, `ADIF-0039`, `ADIF-0043`,
`ADIF-0049`, `ADIF-0006`.

Dispatch impact: keep authority source-bound; prevent aggregated conclusions
from exceeding per-archetype evidence; bind exact output paths; expose unknowns
instead of self-downgrading; verify command shapes; and split material from
continuity commits.

## Authorization / Source

Operator authorization is the exact instruction
`AUTHORIZE_FRESH_R3_THRESHOLD_DESIGN_DISPATCH` after R2G bounded closure at
material commit `6dae3bc20ed9f6b6ab809e7b05f2847e9e1a2629` and continuity
commit `accd005c1786f1e5e3d1950c706ba5f117424f32`.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R3 must pre-register per-archetype proof, cost, divergence, and rollback floors | planning authority | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_CRITIQUE_RECONCILIATION_AND_R2_RESCOPE_2026-08-17.md` | Revised Delivery Sequence | `R3` | generalized TPGR plan | ACCEPT |
| R2G final disposition is proceed to threshold design | closure authority | `docs/assessments/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md` | Decision; Final Disposition | `PROCEED_TO_THRESHOLD_DESIGN` | R2G assessment | ACCEPT |
| R2G provides A1-A6 worksheets and unresolved evidence classes | predecessor evidence | `docs/assessments/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md` | A1-A6 Worksheets; Observed / Projected / Unknown Evidence Summary | `A1-A6` | R2G evidence model | ACCEPT |
| TPGR remains shadow-only and full legacy gates remain active | routing authority | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | TPGR-T0 Legacy Full-Gate Interlock | `selectiveExecutionAuthorized` | TPGR standard | ACCEPT |
| Layer A remains the owner of absorption semantics | lifecycle authority | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_CRITIQUE_RECONCILIATION_AND_R2_RESCOPE_2026-08-17.md` | Generalized Architecture Boundary | existing lifecycle owners | TPGR/absorption boundary | ACCEPT |
| stale receipts must be bounded when source/checker authority changes | risk evidence | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_EXTERNAL_CRITIQUE_2026-08-17.md` | strongest failure modes; receipt freshness | existing critique path | reconciled advisory input | ACCEPT |

## Threshold Design Contract

For each A1-A6 archetype, the worker must define:

1. objective input facts and their canonical owners;
2. one of `LIGHT_ROUTE_ALLOWED`, `FULL_LAYER_A_REQUIRED`, or
   `ESCALATE_FOR_REVIEW` as the candidate route outcome;
3. minimum proof floor before that outcome is eligible;
4. maximum TPGR metadata and review-cost ceiling;
5. divergence tolerance and mandatory escalation boundary;
6. freshness invalidators, including relevant checker/catalog hardening;
7. rollback trigger and restored safe route;
8. who may assert each fact and which facts a worker may not self-declare;
9. observed, projected, and unknown evidence labels;
10. a seeded hostile example showing fail-closed behavior.

## Anti-Self-Downgrade Invariants

- `decisionUncertainty`, authority impact, evidence freshness, and source scale
  cannot be accepted solely from the executing worker's declaration.
- Missing, malformed, contradictory, or owner-unverified facts route to
  `ESCALATE_FOR_REVIEW` or `FULL_LAYER_A_REQUIRED`, never the light route.
- A small file count cannot override material authority impact.
- A prior receipt remains historical evidence but loses current eligibility
  from the earliest affected node when a relevant source, schema, checker, or
  command-catalog dependency changes.
- No threshold may omit an always-on or effect-triggered Layer A control.

## Expected Worker Manifest

- `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md`
- `docs/reviews/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_WORKER_RETURN_2026-08-18.md`

No other path is worker-owned.

## Evidence / Verification

The worker must use existing governed evidence only, distinguish observed
facts from design proposals, and record exact source sections. Thresholds
must be testable and expressed without claiming implementation. Reviewer
acceptance remains independent.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | previously reconciled critique -> accepted R2G evidence -> bounded R3 threshold design |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | TPGR standard and existing Layer A owners |
| Disposition | RECONCILED_DESIGN_INPUT_ONLY |
| Claim boundary | no direct import, new source intake, or outside authority promotion |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: R3 designs thresholds from committed evidence and opens no
  source refresh, repeat scan, or completeness update.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - A1-A6 are governed design
  fixtures; R3 makes no new corpus completeness claim.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE_PLANNING.

Expected Result / Prediction: archetype-specific floors can block unsafe
self-downgrade while preserving cheap routes for genuinely bounded work.

Evidence Comparison: compare each proposed threshold to R2G evidence,
existing TPGR classification, Layer A owners, and stale-receipt risks.

Contradiction Or Gap Disposition: ambiguous or unowned inputs, negative net
value, stale eligibility, or untestable thresholds force revision or stop.

Claim Update: one bounded R3 design disposition only; no authority or runtime
state changes.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | CVF reviewer/orchestrator as dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | TPGR-R3 dispatch authoring, 2026-08-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, ADIF resolver, scaffold preview, collision queries, apply patch, gates, Git |
| Target paths | paired GC-018 baseline and work order |
| Allowed scope source | operator exact R3 authorization |
| Before status evidence | clean HEAD `e6f6f4916b8eec27e0a4877e98b325f993b4552e` with only this planned dispatch pair created afterward |
| After status evidence | two dispatch artifacts only before material commit |
| Diff evidence | exact two-path reconciliation before commit |
| Approval boundary | R3 documentation design dispatch only |
| Claim boundary | no implementation, source intake, selective execution, T15, runtime/live/public/deploy/production |
| Agent type | dispatcher/reviewer |
| Invocation ID | `tpgr-r3-dispatch-20260818` |
| Expected manifest | this baseline and paired work order |
| Actual changed set | required to equal expected manifest before material commit |
| Manifest delta | zero required |
| Deletion or rename disposition | N/A with reason: none authorized |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | documentation-only R3 threshold design |
| claimDisposition | CLAIM_REJECTED_NO_EXECUTION: no execution-control or selective enforcement claim |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: existing receipts are design inputs only; no runtime receipt is created |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime or outside-system action is authorized or observed |
| invocationBoundary | local governed reads and exact two-file worker authoring |
| interceptionBoundary | no wrapper, proxy, hook, runtime gate, or agent-control interception |
| claimLanguage | observed, projected, unknown, proposed, or blocked remain distinct |
| forbiddenExpansion | R4-R9, implementation, protected governance edits, new intake, runtime/provider/live/public/deploy/production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design dispatch; public-sync is not authorized.

## Claim Boundary

This baseline authorizes only the paired no-commit R3 design work order. It
does not authorize implementation or modification of any standard, checker,
registry, catalog, hook, session surface, source corpus, runtime, provider,
public-sync, deployment, destructive operation, or production system.
