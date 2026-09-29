# CVF GC-018 Baseline - ODVR-T1 Deterministic Local Composer

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-07-12

Batch ID: ODVR-T1-DISPATCH

dispatchBaseHead: `ef8702226`

executionBaseHead: `f3a9a7699`

closureBaseHead: `f3a9a7699`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer/closer: independent reviewer

Worker target: delegated worker

## Purpose

Authorize one deterministic read-only Python composer and local CLI-readable
JSON projection implementing the accepted ODVR-T0 contract. The tranche may
read canonical files and git metadata but may not mutate state, select work,
dispatch agents, build UI, or become a source of truth.

## Scope / Target / Owner Boundary

Worker owns exactly one helper, one focused test file, one ODVR front-door
update, and one worker return named in the paired work order. Existing active
session state, MAO-T7, MLW-NRD1, and Web Workspace owners remain authoritative.

## Decision / Baseline / Proposed Tranche

Release only T1 local read-only implementation. T2, UI, provider, public, and
outside-source lanes remain separately authorized work.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| ODVR-T0 closure | `docs/reviews/CVF_ODVR_T0_SOURCE_OVERLAP_AND_READOUT_CONTRACT_COMPLETION_2026-07-12.md`; material commit `2af788683` | T0 accepted after reviewer repair | SATISFIED |
| ODVR contract/schema | `docs/reference/operator_decision_value_readout/`; material commit `2af788683` | ACTIVE_REFERENCE and valid Draft-07 schema | SATISFIED |
| Session routing | session-sync commit `ef8702226` | next move names T1 packet authoring only | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind mcp-cli-adapter --batch-id ODVR-T1 --title "Operator Decision And Value Readout Deterministic Local Composer" --date 2026-07-12 --base ef8702226 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SATISFIED: ODVR-T0 REVIEWER_ACCEPTED_AFTER_REPAIR at material commit 2af788683" --include-worker-return-skeleton --stdout` |
| generatedProfile | mcp-cli-adapter plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with T0-backed local composer, CLI, test, and no-mutation controls |
| checkerReadAheadConfirmation | dispatch-quality, ADIF, AHB, operation-trace, CLI boundary, runtime-freshness, and public-disposition checkers read |
| docOnlyNewFields | none; T1 implements only fields ratified in the T0 schema |
| claimBoundary | dispatch authorship only; no implemented behavior claim |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| bootstrap field vocabulary exists | EXISTS | `governance/compat/generate_active_session_state.py` | `BOOTSTRAP_FIELDS` | `currentMode`; `activeHandoff`; `nextAllowedMove` | active session generator | ACCEPT |
| generated active state source exists | EXISTS | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | top-level object and ordered entries | `currentMode`; `nextAllowedMove`; state-entry objects | generated active state | ACCEPT |
| T0 composition and deterministic-selection contract exists | DOC_ONLY_NEW | `docs/reference/operator_decision_value_readout/CVF_ODVR_T0_SOURCE_OVERLAP_AND_READOUT_CONTRACT.md` | Freshness Rules and New Doc-Only Fields table | `CVF_ODVR_T0_SOURCE_OVERLAP_AND_READOUT_CONTRACT` | ODVR-T0 contract | ACCEPT |
| output schema exists with conditional freshness invariants | EXISTS | `docs/reference/operator_decision_value_readout/CVF_ODVR_T0_READOUT_SCHEMA.json` | `properties`; `allOf` | `aggregateFreshness`; `contradictions`; `staleSourceAnchors`; `missingSourceAnchor` | ODVR-T0 JSON Schema | ACCEPT |
| generated state drift checker exists | EXISTS | `governance/compat/generate_active_session_state.py` | CLI mode | `--check` | active session state generator | ACCEPT |
| MAO readout is a narrower owner | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | deterministic read-model section | `MaoEvidenceReadout` | MAO-T7 | ACCEPT |
| MLW decision readout is a narrower owner | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw-next-runtime-decision-readout.ts` | exports | `MlwNextRuntimeDecisionReadout` | MLW-NRD1 | ACCEPT |
| workspace lane summary is a narrower owner | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts` | read-model interface | `laneSummaries`; `parkedCheckpoints` | Web Workspace read model | ACCEPT |

## Current Runtime Freshness Verification

Verified at `ef8702226`: every accepted path and symbol exists; no
`run_odvr_readout.py` or `test_run_odvr_readout.py` path exists. T0 is accepted
at `2af788683`, and generated active state matches its split sources. The worker
must refresh all checks from its execution HEAD.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime-read-model`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class runtime-read-model --role dispatcher --lifecycle-phase pre-dispatch --surface-selector governance/compat --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: none returned |
| Dispatch impact | T0 reviewer corrections remain mandatory despite the empty resolver packet |

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `DISPATCH_READY`; source verification; AHB route; operation trace; CLI boundary; reviewer conversion |
| gateRunPurpose | confirmatory evidence after source-backed authoring |
| claimBoundary | packet compatibility only |

## Intake Role Routing Decision

Selected route: `MULTI_AGENT_MULTI_ROLE`

rolePattern: `worker-no-commit split`

The delegated worker implements without subagents. The identity-distinct
reviewer is designated closer and only commit owner.

## Evidence / Verification

Pre-dispatch requires source/collision searches, focused tests, JSON Schema
validation, diff hygiene, governed-file-size, reviewer-fast, and autorun gates.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private local foundation dispatch; no public artifact is authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ODVR_T1_DETERMINISTIC_LOCAL_COMPOSER_2026-07-12.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ODVR_T1_DETERMINISTIC_LOCAL_COMPOSER_COMPLETION_2026-07-12.md` | `Status: REVIEWER_ACCEPTED_AFTER_REPAIR` | PASS |
| Roadmap state | `docs/roadmaps/CVF_OPERATOR_DECISION_AND_VALUE_READOUT_ROADMAP_2026-07-12.md` | `PROPOSED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no mutation; aggregate drift check passes | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no mutation required | PASS |
| External evidence digest | N/A with reason: internal local implementation | no external evidence | N/A with reason |
| System loop interlock | current ODVR contract and schema | deterministic read-only boundary retained | PASS |
| Session continuity | separate session-sync after material commit | not part of material batch | N/A with reason |

## Claim Boundary

This baseline authorizes the bounded T1 local helper, CLI JSON output, tests,
front-door update, and worker return only. No UI, Web route, provider/live
proof, state write, autonomous selection, dispatch, public-sync, T2 value
claim, outside-source intake, or production readiness is authorized.
