# CVF GC-018 Baseline - ODVR-T2 Representative Operator Value Proof

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-12

Batch ID: ODVR-T2-DISPATCH

dispatchBaseHead: `9fa305afd`

executionBaseHead: worker captures committed dispatch HEAD before editing

closureBaseHead: executionBaseHead captured by worker at start

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer/closer: independent reviewer

Worker target: delegated worker

## Purpose

Authorize one evidence-only comparison of manual canonical reconstruction and
the committed ODVR readout for the same operator questions across one closed
lane and one parked/reopen lane. This tranche measures value; it does not add
features or treat implementation success as operator-value proof.

## Scope / Target / Owner Boundary

The worker owns exactly one JSON measurement receipt, one review report, and
one worker return named in the paired work order. Canonical session, roadmap,
ODVR contract, and composer owners remain read-only authority.

## Decision / Baseline / Proposed Tranche

Release only ODVR-T2 representative value measurement. UI remains gated on a
positive result plus separate operator authorization. Provider, public-sync,
runtime edits, session mutation, and outside-source absorption remain parked.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| ODVR-T1 closure | `docs/reviews/CVF_ODVR_T1_DETERMINISTIC_LOCAL_COMPOSER_COMPLETION_2026-07-12.md`; material commit `16364f797` | accepted local composer exists | SATISFIED |
| ODVR contract/schema | `docs/reference/operator_decision_value_readout/`; material commits `2af788683` and `16364f797` | active deterministic contract and schema | SATISFIED |
| Session routing | session-sync commit `9fa305afd` | T2 packet authoring is current next move | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind evidence-only --batch-id ODVR-T2 --title "Representative Operator Value Proof" --date 2026-07-12 --base 9fa305afd --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SATISFIED: ODVR-T1 accepted at 16364f797" --include-worker-return-skeleton --stdout` |
| generatedProfile | evidence-only plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with source-backed two-scenario measurement protocol and exact evidence manifest |
| checkerReadAheadConfirmation | dispatch, ADIF, AHB, trace, evidence, and export checkers read |
| docOnlyNewFields | measurement receipt fields are isolated in New Doc-Only Fields |
| claimBoundary | packet authorship only; no value result claimed |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T2 requires closed and parked/reopen scenarios | LITERAL_INVARIANT | `docs/roadmaps/CVF_OPERATOR_DECISION_AND_VALUE_READOUT_ROADMAP_2026-07-12.md` | Work Plan ODVR-T2 row | `ODVR-T2` | ODVR roadmap | ACCEPT |
| T2 requires steps, files, time, and correctness | LITERAL_INVARIANT | `docs/roadmaps/CVF_OPERATOR_DECISION_AND_VALUE_READOUT_ROADMAP_2026-07-12.md` | Acceptance Criteria | `ODVR-T2 records operator steps` | ODVR roadmap | ACCEPT |
| continued use requires fewer files and steps with fact preservation | LITERAL_INVARIANT | `docs/roadmaps/CVF_OPERATOR_DECISION_AND_VALUE_READOUT_ROADMAP_2026-07-12.md` | Acceptance Criteria | `T2 may recommend continued use` | ODVR roadmap | ACCEPT |
| local composer entry point exists | EXISTS | `governance/compat/run_odvr_readout.py` | public callable and CLI | `build_odvr_readout`; `--json` | ODVR-T1 composer | ACCEPT |
| current output schema exists | EXISTS | `docs/reference/operator_decision_value_readout/CVF_ODVR_T0_READOUT_SCHEMA.json` | required properties and conditional states | `aggregateFreshness`; `sourceAnchors` | ODVR-T0 JSON Schema | ACCEPT |
| closed representative lane evidence exists | VALUE_SET | `CVF_SESSION/state/entries/odvrT1Closure20260712.json` | `value.status`; `value.materialCommit` | `odvrT1Closure20260712` | active session state entry | ACCEPT |
| parked/reopen representative lane evidence exists | VALUE_SET | `docs/roadmaps/CVF_MAO_LIVE_PROVIDER_ADAPTER_VALUE_PILOT_ROADMAP_2026-07-12.md` | Status and Concrete reopen condition | `Concrete reopen condition` | MAO-LIVE roadmap | ACCEPT |
| generated state drift check exists | RUNTIME_BEHAVIOR | `governance/compat/generate_active_session_state.py` | CLI parser and check path | `--check` | active session state generator | ACCEPT |

## New Doc-Only Fields

| Field | Artifact | Purpose | Runtime authority |
|---|---|---|---|
| `scenarioId` | T2 JSON receipt | distinguish closed and parked/reopen scenarios | none; evidence-only |
| `pathKind` | T2 JSON receipt | distinguish MANUAL and COMPOSED traces | none; evidence-only |
| `operatorQuestionSet` | T2 JSON receipt | bind both paths to identical questions | none; evidence-only |
| `stepCount`; `filesRead`; `elapsedMs` | T2 JSON receipt | recomputable friction measurements | none; evidence-only |
| `answers`; `canonicalExpectedAnswers` | T2 JSON receipt | compare fact preservation | none; evidence-only |
| `factComparison`; `valueVerdict` | T2 JSON receipt | terminal proof disposition | none; evidence-only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`evaluation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class evaluation --role dispatcher --lifecycle-phase pre-dispatch --surface-selector docs/reviews --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

Disclosed defectIds: N/A with reason: resolver returned zero defects.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | dispatch status, source table columns, ADIF query line, handoff route, trace labels, public-sync boundary |
| gateRunPurpose | confirmation and evidence after source-backed authoring |
| claimBoundary | T2 evidence packet only; no execution or product expansion |

## Intake Role Routing Decision

Selected route: `MULTI_AGENT_MULTI_ROLE`

rolePattern: `worker-no-commit split`

The delegated worker measures and reports without subagents or commit. The
identity-distinct reviewer is the closer and sole commit owner.

## Dual Agent Surface Matrix

| Surface | Disposition | Interface | Authority/risk boundary | Evidence | Adapter boundary |
|---|---|---|---|---|---|
| INTERNAL_AGENT | IMPLEMENTED | local files and Python CLI | read-only evidence collection | T2 receipt and report | no action adapter |
| EXTERNAL_AGENT_CLI_MCP | NOT_IMPLEMENTED | N/A with reason: no external CLI/MCP route | external execution is unauthorized | no external receipt | separate GC-018 required |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_CURRENT

priorVerificationArtifact: `docs/reviews/CVF_ODVR_T1_DETERMINISTIC_LOCAL_COMPOSER_COMPLETION_2026-07-12.md`

priorVerificationAnchor: material commit `16364f797`

freshRecomputeRequired: yes; both traces and all counts must be produced from execution HEAD

unicodePathHandling: use literal repository-relative paths and UTF-8-safe readers; author new governed text in ASCII

extractedTextAuthority: canonical source content and command receipts only

## Evidence / Verification

Pre-dispatch requires source searches, ADIF disclosure, roadmap trace coverage,
diff hygiene, file-size enforcement, commit steward, and pre-dispatch autorun.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private evidence dispatch. Public-sync boundary: no T2 artifact may be
copied or pushed by this tranche.

## Claim Boundary

This baseline authorizes T2 measurement artifacts only. It does not authorize
composer changes, UI/Web, provider/live proof, state mutation, autonomous
decision, public-sync, outside-source absorption, production readiness, or a
positive value conclusion before independent review.
