# CVF GC-018 Baseline - ODVR-T0 Source Overlap And Readout Contract

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-12

Batch ID: ODVR-T0-DISPATCH

dispatchBaseHead: `933f7a420`

executionBaseHead: worker captures committed dispatch HEAD before editing

closureBaseHead: reviewer assigns after worker return

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer/closer: independent reviewer

Worker target: delegated worker

## Purpose

Authorize a documentation/schema-only inventory that determines whether ODVR
has a real cross-owner composition gap. Define the field authority map,
freshness and contradiction semantics, JSON contract, and representative
fixtures without implementing a composer, CLI, UI, or new truth store.

## Scope / Target / Owner Boundary

The worker owns exactly three material reference/schema outputs and one worker
return named in the paired work order. Existing active-session, MAO-T7,
MLW-NRD1, and Web Workspace read models remain authoritative for their current
scopes. The independent reviewer is closer and commit owner.

## Decision / Baseline / Proposed Tranche

Release ODVR-T0 only. T1 remains dependency-held until T0 proves a non-duplicate
composition gap and the reviewer accepts the contract. If an existing canonical
surface already owns the full required result, the worker must return a stop
recommendation rather than manufacture a new owner.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| ODVR roadmap | `docs/roadmaps/CVF_OPERATOR_DECISION_AND_VALUE_READOUT_ROADMAP_2026-07-12.md`; material commit `7c6f13ab8` | roadmap is PROPOSED and authorizes T0 packet authoring | SATISFIED |
| Active session routing | generated bootstrap and state at session-sync commit `933f7a420` | next move names fresh ODVR-T0 packet | SATISFIED |
| Prior narrow owners | source files in the Source Verification Block | all must remain read-only and explicitly overlap-classified | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ODVR-T0 --title "Operator Decision And Value Readout Source Overlap And Contract" --date 2026-07-12 --base 933f7a420 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SATISFIED: ODVR roadmap PROPOSED at material commit 7c6f13ab8 and session routing current at 933f7a420" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced generated placeholders with ODVR-T0 source-backed scope, authority, evidence, and handoff controls |
| checkerReadAheadConfirmation | dispatch-quality, ADIF disclosure, AHB, workspace-design, runtime-freshness, scaffold-provenance, and public-disposition checkers read |
| docOnlyNewFields | all proposed ODVR result fields belong in the T0 New Doc-Only Fields table and JSON Schema, not the Source Verification table |
| claimBoundary | dispatch authorship only; no composer, CLI, UI, provider, public, or external-intake behavior claim |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| active session generator requires current mode and next move | EXISTS | `governance/compat/generate_active_session_state.py` | `REQUIRED_CORE_KEYS` | `currentMode`; `nextAllowedMove` | active session state generator | ACCEPT |
| bootstrap projection exposes mode, handoff, next move, and claim boundary | EXISTS | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | top-level object | `currentMode`; `activeHandoff`; `nextAllowedMove`; `claimBoundary` | bootstrap read model | ACCEPT |
| MAO task-graph evidence readout and freshness classifier exist | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | deterministic read-model and freshness sections | `MaoEvidenceReadout`; `buildEvidenceReadout`; `classifyReadoutFreshness` | MAO-T7 evidence/readout contract | ACCEPT |
| MLW route advisory decision readout exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw-next-runtime-decision-readout.ts` | exports | `MlwNextRuntimeDecisionReadout`; `buildMlwNextRuntimeDecisionReadout` | MLW-NRD1 readout | ACCEPT |
| Web Workspace server read model exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts` | module exports and consumers | `cvf-workspace-read-model` | Web Workspace server read model | ACCEPT |
| local workspace projection foundation is closed bounded | VALUE_SET | `CVF_SESSION/state/entries/localWorkspaceProjectionReadModelClosure20260627.json` | `value.status` | `localWorkspaceProjectionReadModelClosure20260627` | active session state entry | ACCEPT |
| MAO live value verdict and quantified reopen condition exist | VALUE_SET | `docs/roadmaps/CVF_MAO_LIVE_PROVIDER_ADAPTER_VALUE_PILOT_ROADMAP_2026-07-12.md` | `Status`; `Next Allowed Move` | `REVIEWER_ACCEPTED_VALUE_NOT_PROVEN`; `Concrete reopen condition` | MAO-LIVE roadmap | ACCEPT |
| ODVR roadmap requires overlap classification before implementation | LITERAL_INVARIANT | `docs/roadmaps/CVF_OPERATOR_DECISION_AND_VALUE_READOUT_ROADMAP_2026-07-12.md` | `Design Control Gate`; `Work Plan` | `ODVR-T0` | ODVR roadmap | ACCEPT |

## Current Runtime Freshness Verification

Verified at `933f7a420`: every accepted path and symbol above exists. Searches
for `ODVR` collide with the roadmap and current session-routing artifacts;
`Decision And Value Readout` has no exact same-token collision in the searched
roots, while semantic searches identify the narrower owners listed above. These
results do not prove absence of a semantic full owner; the worker must refresh
and classify overlap before authoring.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture-contract`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class architecture-contract --role dispatcher --lifecycle-phase pre-dispatch --surface-selector docs/reference --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: none returned |
| Dispatch impact | worker must still source-verify every owner and must not treat an empty resolver result as proof of comprehension |

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_workspace_design.py`; `governance/compat/check_agent_workspace_runtime_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; source verification columns; AHB block; workspace block; reviewer closure conversion; worker return contract |
| gateRunPurpose | confirmation and evidence after source-backed authoring; not first discovery |
| claimBoundary | packet compatibility only; no execution proof |

## Intake Role Routing Decision

Selected route: `MULTI_AGENT_MULTI_ROLE`

rolePattern: `worker-no-commit split`

The delegated worker performs T0 execution without subagents. The
identity-distinct independent reviewer is designated closer and only material
commit owner.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: ODVR-T0 compares internal CVF owner surfaces only;
it does not ingest, enumerate, map, or absorb an outside corpus.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no source corpus, mirror
  manifest, processing ledger, or completeness claim is created by this
  internal contract tranche.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION

ODVR-T0 does not select or consume an outside source target. Later source-mirror
work remains a separate operator decision after ODVR disposition.

## Evidence / Verification

Pre-dispatch requires refreshed source searches, JSON parsing, `git diff
--check`, dispatch-quality, AHB, workspace-design, governed-file-size, and
autorun gates on the real changed range.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance contract dispatch with no public-safe artifact.

Next action: retain the packet privately pending worker execution and review.

## Claim Boundary

This baseline authorizes ODVR-T0 documentation, JSON Schema, and representative
doc fixtures only. It does not authorize a composer, CLI, UI, provider/live
proof, mutable state, automatic decision, session mutation, public-sync,
outside-source intake, ODVR-T1, or production-readiness claim.
