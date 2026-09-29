# CVF GC-018 Baseline - ACEL AKOE-P2 Durable Intent And Projection Reconciliation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: ACEL-AKOE-P2

Dispatch base head: `81ad480b86074b0d8e40025cde8a95c9051e6a0e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local reviewer/closer

Reviewer owner: Local reviewer/closer distinct from the worker phase

Worker target: shared-workspace `INTERNAL_AGENT` runtime-reconciliation role

## Purpose

Authorize one bounded, audit-first comparison of the existing MAO operational
worker launcher and governed-command launcher. The worker must prove any gap
with a deterministic negative test before changing implementation, preserve
the durable-ledger truth boundary, and return all work uncommitted for Local
review.

## Authorization / Decision

The operator authorized the next roadmap move on 2026-09-25. The accepted
AKOE roadmap marks P2 `READY_PENDING_OPERATOR_CHECKPOINT`; that checkpoint is
satisfied only for this bounded P2 packet.

This baseline does not open P3 integration proof, P4 common Local closure,
optional Unreal source intake, a new runtime engine, or any public/provider/
deployment action.

## Scope

Allowed:

- compare the two exact existing launch paths and their tests;
- model durable admission, effect dispatch/acceptance, terminal checkpoint,
  replay, cancellation, recovery identity, and projection boundaries;
- create the required seven-class test matrix and run deterministic negative
  cases against current behavior;
- make the smallest change within the paired work order manifest only when a
  negative case proves a current-owner defect;
- record `CONFIRMED_EXISTING`, `ENRICH_EXISTING`, `DEFER_WITH_TRIGGER`, or
  `REJECT_DIRECT_IMPORT` for each P2 class.

Forbidden:

- presuming a defect from document similarity or from the handoff alone;
- creating a new runtime, scheduler, queue, execution ledger, projection
  authority, semantic-completion owner, or architecture family;
- reading or importing Unreal upstream code, using network access, or making
  a source-specific Unreal factual claim;
- editing governance checkers, hooks, catalogs, session continuity, roadmaps,
  dispatch artifacts, or files outside the exact worker manifest;
- provider/model calls, credentials, live release proof, public sync,
  deployment, production action, staging, or worker commit.

## Baseline Invariants

1. Durable owner evidence and executable tests, not the design handoff, decide
   whether a P2 gap exists.
2. A durable admission record before effect dispatch must bind enough identity
   to prevent ambiguous replay or recovery; ambiguity fails closed.
3. Effect acceptance and terminal checkpoint are distinct states. A process
   return or runtime completion is not semantic completion without required
   artifact and independent-verification evidence.
4. The MAO event/receipt ledger is execution truth. Conversation/workspace
   views are projections and must never overwrite or contradict that truth.
5. Same-identity replay must not duplicate the effect. Conflicting identity,
   authority, scope, or budget evidence must fail closed without settlement.
6. Cancellation and completion races must have one deterministic durable
   outcome and may not fabricate success or release unrelated capacity.
7. No implementation change is valid without a failing deterministic test
   that passes after the minimal correction.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| `docs/roadmaps/CVF_ACEL_APPLIED_KNOWLEDGE_OWNER_ENRICHMENT_ROADMAP_2026-09-25.md` | P2 names both existing launch paths, the seven required test classes, and the no-new-runtime boundary | paired packet preserves every P2 class and audit-first rule | SATISFIED |
| AKOE-P1 closure | P1 is `CLOSED_PASS_BOUNDED`; completion review commit `af0e9a199`, closure projection `3c8378b8b`, marker sync `81ad480b8` | P2 must not reopen P1 | SATISFIED |
| operator checkpoint | operator said `next` on 2026-09-25 after P1 closure | authority is limited to authoring and releasing this P2 packet | SATISFIED |
| dispatch continuity | active handoff still records P1 closure before this packet is committed | worker starts only after committed P2 material and later handoff material-SHA marker | REQUIRED_BEFORE_IMPLEMENTATION |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| MAO persists reservation and admission before adapter call | current implementation | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | launch sequence around lines 313-399 | `MaoOperationalWorkerLauncher`; `launch` | durable delegation port plus MAO event ledger | ACCEPT |
| MAO currently appends `INVOCATION_STARTED` after successful adapter invocation | crash-window candidate | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | launch sequence around lines 399-445 | `adapter.invoke`; `INVOCATION_STARTED` append | operational launcher | ACCEPT |
| MAO recovery verifies reservation-bound attempt identity | recovery boundary | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | `reconcileDelegation` around lines 500-663 | `reconcileDelegation` | durable reservation identity and event ledger | ACCEPT |
| governed-command launcher persists create-exclusive intent before runner | current implementation | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | execution sequence around lines 412-503 | `beginExecution`; `runner.run` | governed execution store | ACCEPT |
| MAO event ledger is truth and workspace is projection | contract boundary | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Workspace relationship and Second governance/state truth | MAO runtime truth model | MAO contract | ACCEPT |

Optional Unreal evidence is excluded from this dispatch: no source-specific
claim is admitted, and any future need triggers a separate pinned-source
intake decision.

## Exact Input Evidence

| Input | SHA-256 | Origin class | Authority disposition |
|---|---|---|---|
| `C:/Users/DELL/Downloads/ASYNC_RUNTIME_CANONICAL_HANDOFF.md` | `a85d8fd35495e94257df1d3a8bfa238d3e5661eaa04b52e156b4886987a4525b` | `OPERATOR_AGENT_CO_DESIGNED` | design input only; current CVF source and tests control |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Planned artifact paths | `Test-Path` returned `False` for paired baseline, work order, and worker return before authoring | CLEAR |
| Packet token collision | exact command `rg -n "ACEL-AKOE-P2|Durable Intent And Projection Reconciliation" docs CVF_SESSION AGENT_HANDOFF_V63_2026-09-18.md`; roots `docs`, `CVF_SESSION`, and active handoff; result before authoring: one same-token collision at roadmap line 213 | CLEAR_EXPECTED_ROADMAP_OWNER |
| Runtime-owner collision | both implementation paths and their existing tests were found; no new owner is needed for the bounded audit | REUSE_EXISTING_OWNERS |

## Required P2 Decision Matrix

The worker return must carry one row for every required class:

| Class | Required deterministic evidence | Allowed outcome |
|---|---|---|
| crash after durable admission before effect dispatch | injected interruption or exact seam proving replay/recovery behavior | P2 disposition token |
| crash after effect acceptance before terminal checkpoint | injected terminal-persistence failure after effect acceptance | P2 disposition token |
| same/conflicting duplicate launch | exact identity and mismatch cases | P2 disposition token |
| cancel/completion race | deterministic ordering cases and durable winner | P2 disposition token |
| stale/contradictory projection | projection compared with ledger truth | P2 disposition token |
| authority/scope/budget mismatch recovery | mismatch leaves effect/settlement closed | P2 disposition token |
| semantic completion without required evidence | completion withheld until artifact and independent verification evidence exist | P2 disposition token |

Each row must name the current owner, exact symbol/test, pre-change result,
disposition, change or no-change reason, post-change result when applicable,
and `PENDING_LOCAL_REVIEW`.

## Acceptance Criteria

- the handoff hash matches and no Unreal/upstream factual claim is used;
- all seven P2 classes have deterministic evidence or an exact
  `DEFER_WITH_TRIGGER` reason that does not weaken an existing claim;
- every code change is preceded by a failing test and is minimal within the
  exact manifest;
- admission/effect/terminal/semantic-completion states remain explicit;
- ambiguous identity, authority, scope, budget, or recovery fails closed;
- projection remains non-authoritative and contradiction is surfaced;
- focused tests and type/build checks pass for every changed package;
- worker return passes the full gate and remains uncommitted.

## Evidence / Verification

Dispatch evidence is the exact two-file diff from base `81ad480b8`, the
recomputed input hash, source-symbol inspection, collision search, dispatch
author fast gate, and full pre-dispatch gate. Worker evidence is defined by
the paired work order; this baseline makes no implementation-result claim.

## Stop Conditions

Return `BLOCKED_WITH_REASON` for input-hash drift, missing dispatch continuity,
a needed path outside the manifest, a new owner/runtime requirement, optional
Unreal intake need, network/provider/live/public need, or an unrepairable gate
failure. A no-gap result is complete when all seven classes have passing
deterministic evidence and exact locators.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | paired packet, exact source/tests, worker return | bounded local audit and conditional source/test repair; no commit or final acceptance | deterministic tests, exact diff, gates | existing in-process test seams only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no P2 external adapter | no ingress, invocation, authentication, mutation, or public authority | zero external invocation ceiling | N/A with reason: no external adapter is invoked or designed | N/A_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime-source-reconciliation`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "runtime-source-reconciliation" --role worker --lifecycle-phase implementation --max-results 12 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | preserve audit-first proof, exact path ceiling, no-commit separation, and deterministic negative cases |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_independent_review_probe_admission.py` |
| literalTokensReviewed | top-level status and commit mode; exact source-verification columns; no-question rule; closeability scalars and graph columns; convergence scalars; SCEC JSON; dual-surface matrix; worker-return full-gate terms; trace labels; source-not-found spelling |
| gateRunPurpose | machine confirmation after source inspection and packet completion; not first discovery or semantic acceptance |
| claimBoundary | dispatch admission only; no defect, implementation correctness, runtime readiness, or P2 closure is proved |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-AKOE-P2 --title "ACEL AKOE-P2 Durable Intent And Projection Reconciliation" --date 2026-09-25 --base 81ad480b86074b0d8e40025cde8a95c9051e6a0e --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/roadmaps/CVF_ACEL_APPLIED_KNOWLEDGE_OWNER_ENRICHMENT_ROADMAP_2026-09-25.md --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence NONE --scec-problem-key acel-akoe-p2-durable-intent-projection --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope EXECUTABLE_IMPLEMENTATION --stdout` |
| generatedProfile | generic worker initial dispatch with no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact P2 source, test-class, invariant, scope, and acceptance contracts |
| checkerReadAheadConfirmation | applicable dispatch, lifecycle, routing, handoff, convergence, trace, review-probe, and public-disposition checker sources were inspected |
| docOnlyNewFields | Required P2 Decision Matrix columns only |
| claimBoundary | scaffold provenance only; no runtime, provider, external, public, or closure claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private-provenance dispatch baseline with no public-sync
authority or public artifact evidence.

## Claim Boundary

This baseline authorizes only bounded P2 audit and conditional minimal repair
of the exact current source/test owners under the paired work order. It does
not establish that a gap exists, accept worker findings, authorize Unreal
intake, open P3/P4, or prove live, provider, public, deployment, certification,
or production behavior.
