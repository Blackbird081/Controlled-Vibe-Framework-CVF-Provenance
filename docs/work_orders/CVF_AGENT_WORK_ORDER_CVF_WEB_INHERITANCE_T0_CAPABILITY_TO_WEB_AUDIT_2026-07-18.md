# CVF Agent Work Order - CVF-WEB-INHERITANCE-T0 Capability-To-Web Audit

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-07-18

Batch ID: CVF-WEB-INHERITANCE-T0

## Dispatch Prompt Envelope

Role: execute one bounded, read-only capability-to-Web inheritance audit.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_INHERITANCE_T0_CAPABILITY_TO_WEB_AUDIT_2026-07-18.md`.

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `36041a985`.

executionBaseHead: capture the current committed dispatch/session-sync HEAD
before any edit and preserve it unchanged throughout worker execution.

closureBaseHead: equals executionBaseHead because the worker must not commit;
the independent reviewer refreshes this anchor before closure authoring.

Current-time notes: SOT3-CVF-PROJ-T0 is accepted at material commit
`9d8305942`; cvf-web has real SOT3 backend wiring but no audited operator
surface; T1-T5 are parked.

Do-not-misread notes: package dependency, backend wiring, registry projection,
operator visibility, and documentation freshness are separate dimensions. Do
not call a capability absent merely because no page exposes it. Do not call a
capability Web-inherited merely because its package exists elsewhere.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, `DESIGN.md`, this roadmap/baseline/work order, applicable checker
sources, then capture HEAD and clean status before authoring either output.

Return contract: return exactly `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`; do not stage or commit.

## Authority Chain

1. Operator instruction to assess cvf-web inheritance after recent CVF upgrades.
2. `DESIGN.md` for later UI boundaries.
3. `docs/roadmaps/CVF_WEB_CAPABILITY_INHERITANCE_AND_OPERATOR_PROJECTION_ROADMAP_2026-07-18.md`.
4. `docs/baselines/CVF_GC018_CVF_WEB_INHERITANCE_T0_CAPABILITY_TO_WEB_AUDIT_2026-07-18.md`.
5. This work order.
6. Current runtime/package source and accepted governed reviews.

Provider-specific memory and chat summaries are not factual authority.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake summary | operator request to audit inheritance of recent CVF capabilities into cvf-web |
| scope classification | bounded internal static audit with exactly two allowed worker outputs |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| dispatcher role | authors and commits the dispatch packet |
| worker role | reads current source and creates two uncommitted review outputs |
| reviewer role | independently recomputes, repairs within scope, and owns closure |
| session-sync role | protected continuity steward after material acceptance |
| risk sensitivity | Web/runtime/source mutation, browser, provider/live, public action, and sibling-source copy are prohibited |
| routing decision | `WORKER_MUST_NOT_COMMIT` |
| public route | `DEFERRED_PRIVATE_ONLY` |
| escalation condition | missing source, unclean worktree, non-enumerable page set, source contradiction, forbidden-path need, or scope expansion |

## Agent Roles

| Role | Owner | Authority |
|---|---|---|
| dispatcher | current dispatcher role | source verification, packet authoring, dispatch commit |
| worker | delegated worker role | read-only audit and exact two-output return |
| reviewer/closer | independent reviewer | recomputation, bounded repair, material commit |
| session-sync steward | designated steward role | protected continuity after accepted material closure |

## Required First Reads

1. `CVF_SESSION_MEMORY.md`.
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json` and active handoff.
3. `docs/reference/guard_orientation/README.md`.
4. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
5. `DESIGN.md`.
6. roadmap, GC-018 baseline, and this work order.
7. applicable worker-return and corpus checker sources.

## Pre-Flight Checks

- capture current `git rev-parse --short HEAD` as executionBaseHead;
- require clean `git status --short` before the first write;
- verify all Source Verification paths still exist;
- enumerate all current page files and record the command-backed denominator;
- run pre-implementation autorun before substantive authoring.

## Write Ownership

The worker owns only the two review outputs named in Planned Worker Fulfillment
Manifest. Reviewer closure paths and protected session paths are not worker
write scope.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only after both outputs and all worker gates
pass with exact scope, unchanged HEAD, and nothing staged. Otherwise return
`BLOCKED_WITH_REASON` with the first source/authority/scope blocker and command
evidence.

## Operator Checkpoint

No operator checkpoint is needed for source-decidable T0 classification. Any
choice to link, adapt, port, or defer sibling Controlled Quotation belongs to
T4 after independent T0 closure.

## Purpose

Produce the terminal 12-row ledger required to decide what cvf-web actually
inherits, what it hides, what it misreports, and what needs a separate adoption
decision before any Web implementation tranche is released.

## Scope / Target / Owner Boundary

### Allowed reads

- all startup and guard surfaces;
- `DESIGN.md`;
- the roadmap, baseline, and this work order;
- current cvf-web source, tests, package metadata, pages, navigation, scripts,
  and README;
- current SOT3 and MAO package roots named in Source Verification;
- accepted SOT3-APP and FSCB-ADAPT completion reviews;
- applicable governance checker source.

### Allowed writes

- `docs/reviews/CVF_WEB_INHERITANCE_T0_CAPABILITY_TO_WEB_LEDGER_2026-07-18.md`
- `docs/reviews/CVF_WEB_INHERITANCE_T0_WORKER_RETURN_2026-07-18.md`

### Forbidden scope

Every other path. In particular: no cvf-web source/test/package/README edit;
no extension source edit; no registry or generated aggregate edit; no session
surface edit; no browser, build, typecheck, provider, live, network, public-sync,
push, production, queue, daemon, worker launch, or sibling application edit.

## Dependency Release Evidence

| Dependency | Artifact | Disposition |
|---|---|---|
| SOT3-CVF-PROJ-T0 acceptance | `docs/reviews/CVF_SOT3_CVF_PROJ_T0_COMPLETION_REVIEW_2026-07-18.md`; material commit `9d8305942` | SATISFIED |
| current roadmap T0 release | `docs/roadmaps/CVF_WEB_CAPABILITY_INHERITANCE_AND_OPERATOR_PROJECTION_ROADMAP_2026-07-18.md` | SATISFIED_FOR_T0_ONLY |
| T1-T5 implementation | independent T0 completion review does not yet exist | HELD |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| SOT3 package dependencies exist | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependency rows 27-29 | `cvf-refinery`; `cvf-truth-flow`; `cvf-truth-kernel` | npm dependency map | ACCEPT |
| SOT3 adapter composes real owners | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-knowledge-adapter.ts` | imports 14-18; lifecycle 543 onward | `evaluateSot3KnowledgeActivation` | SOT3 adapter | ACCEPT |
| execute route fails closed on rejected activation | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | activation block around 686-735 | `terminalOutcome` | execute route | ACCEPT |
| page inventory and main navigation have zero audited capability terms | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` | main navigation plus enumeration of 41 page files; zero matches at dispatch | `Sidebar` | main navigation plus enumerated app pages | ACCEPT |
| Execution Plane is registry-not-exposed | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts` | Execution Plane entry | `execution-plane-foundation`; `NOT_EXPOSED` | `MODULES` | ACCEPT |
| Control and Learning are partially inherited | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts` | Control and Learning entries | `PARTIAL_INHERITED` | `MODULES` | ACCEPT |
| execution-plane MAO root exists | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | root export near 1418 | `./mao` | execution-plane root | ACCEPT |
| control-plane MAO root exists | EXISTS | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/index.ts` | line 12 | `./control.plane.mao.barrel` | control-plane root | ACCEPT |
| execution-plane package is absent from cvf-web dependency map | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | complete dependency map | `dependencies` | npm dependency map whose current values exclude the execution-plane package | ACCEPT |
| sibling application proof is accepted | EXISTS | `docs/reviews/CVF_SOT3_APP_T5_COMPLETION_REVIEW_2026-07-18.md` | final disposition | `SOT3-APP-T5` | completion review | ACCEPT |
| Four-Surface adaptation is accepted | EXISTS | `docs/reviews/CVF_FSCB_ADAPT_T0_COMPLETION_2026-07-15.md` | final disposition | `FSCB-ADAPT-T0` | completion review | ACCEPT |
| cvf-web README is dated before current capability work | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/README.md` | badge, quality snapshot, changelog | `1.6.0`; `2026-02-22`; `2026-02-07` | README | ACCEPT |
| UI contract exists | LITERAL_INVARIANT | CANONICAL_CONTRACT: root `DESIGN.md` | sections 4, 8, 9, 14 | `DESIGN.md` | canonical UI/UX contract | ACCEPT |

## New Doc-Only Fields

| Field | Allowed values |
|---|---|
| `dependencyState` | `PRESENT`; `ABSENT`; `N/A_WITH_REASON` |
| `backendWiringState` | `WIRED`; `PARTIAL`; `ABSENT`; `SIBLING_ONLY`; `N/A_WITH_REASON` |
| `registryProjectionState` | `CURRENT`; `STALE`; `MISSING`; `N/A_WITH_REASON` |
| `operatorSurfaceState` | `VISIBLE`; `PARTIAL`; `ABSENT`; `N/A_WITH_REASON` |
| `documentationState` | `CURRENT`; `STALE`; `MISSING`; `N/A_WITH_REASON` |
| `inheritanceDisposition` | `INHERITED_RUNNABLE`; `INHERITED_HIDDEN`; `PARTIAL_INHERITANCE`; `NOT_INHERITED`; `SIBLING_ADOPTION_DECISION_REQUIRED`; `DEFER_WITH_REASON` |
| `targetTranche` | `T1`; `T2`; `T3`; `T4`; `T5`; `NONE_WITH_REASON` |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Evidence |
|---|---|---|
| T0 terminal inheritance audit | produce one row for WEB-01 through WEB-12 | ledger terminal table and reconciliation |
| separate five evidence dimensions | fill dependency, backend, registry, operator, and documentation fields | every terminal row |
| preserve SOT3 backend truth | read adapter, route, evidence store, and tests directly | source citations |
| do not overclaim MAO inheritance | compare package roots with cvf-web dependency/import/page facts | WEB-05 through WEB-07 |
| preserve sibling boundary | use accepted review as evidence, not cvf-web runtime source | WEB-08 and WEB-09 |
| no implementation in T0 | exact two-output allowed writes | git evidence and no-commit statement |

## Execution Plan

1. Capture `executionBaseHead` and clean `git status --short`.
2. Read all mandatory startup, design, dispatch, and checker surfaces.
3. Enumerate all current cvf-web pages and navigation owners.
4. Search current cvf-web dependency/import/source/page/test/README families for
   every seed capability and record exact hits and bounded zero-hit claims.
5. Read source owners for all non-absence runtime claims.
6. Build exactly 12 terminal ledger rows.
7. Reconcile every enum count to 12 and record recommended next tranche.
8. Write the worker return and run the required gates.

## Evidence Requirements

Each ledger row must include:

- capability ID and name;
- source owner and exact Web comparison paths;
- dependency, backend wiring, registry, operator, and documentation states;
- final inheritance disposition;
- risk of a false positive or false absence claim;
- target tranche and exact proposed boundary;
- source evidence path plus line, symbol, or section.

The ledger must separately report:

- total current page count and exact enumeration method;
- term-hit and zero-hit boundaries;
- SOT3 dependency and runtime integration facts;
- MAO dependency/import/page facts;
- sibling-only service-chain evidence boundary;
- runtime-module registry gaps;
- README/version drift;
- near-threshold files that a later tranche must split or avoid expanding.

## Planned Worker Fulfillment Manifest

| Path | Change type | Owner |
|---|---|---|
| `docs/reviews/CVF_WEB_INHERITANCE_T0_CAPABILITY_TO_WEB_LEDGER_2026-07-18.md` | new | worker |
| `docs/reviews/CVF_WEB_INHERITANCE_T0_WORKER_RETURN_2026-07-18.md` | new | worker |

No other changed path is allowed.

## Acceptance Criteria

- AC-01: WEB-01 through WEB-12 each have exactly one terminal row.
- AC-02: all five evidence dimensions are populated or use bounded N/A reason.
- AC-03: counts reconcile to 12 for every classification family.
- AC-04: SOT3 is classified from actual dependency/runtime source.
- AC-05: MAO absence is bounded to cvf-web dependency/import/page search.
- AC-06: sibling app facts are sourced from governed reviews and not promoted
  into cvf-web source authority.
- AC-07: T1-T5 recommendations are non-overlapping and source-backed.
- AC-08: exact two-output changed set, nothing staged, HEAD unchanged.
- AC-09: no build, browser, provider, live, public, push, or production action.

## Review Gate

An independent reviewer must re-enumerate pages, recompute all 12 rows, verify
current symbols and absence boundaries, repair allowed closure paths if needed,
and own the material commit. Worker completion is not dependency release.

## Closure Checklist

- [ ] 12 seed families independently reconciled;
- [ ] SOT3 backend inheritance independently confirmed;
- [ ] MAO Web absence boundary independently confirmed;
- [ ] sibling-app authority boundary preserved;
- [ ] runtime-module registry routing accepted or repaired;
- [ ] exact two-path worker changed set confirmed;
- [ ] worker no-commit boundary confirmed;
- [ ] session continuity synchronized separately after material closure.

## Stop Conditions

Return `BLOCKED_WITH_REASON` before edits if a named source path is missing, the
page denominator cannot be enumerated, a source fact conflicts with the packet,
the worktree is not clean at start, or the two-output scope cannot be preserved.

After edits, return blocked if a gate fails and cannot be repaired inside the
two allowed outputs. Do not expand scope to fix source, registry, or session
state.

## Worker Autonomy / No-Question Rule

Resolve ordinary audit details from current source and checker messages. Do not
ask the operator to choose classification values already decidable from source.
Stop only on a genuine source, authority, or scope blocker.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | current Web and package source | static audit only | terminal ledger | fresh tranche required | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | none changed | no ingress, auth, approval, receipt, raw-data, mutation, or public behavior | no adapter output | parked | `N/A_WITH_REASON` |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Disposition |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | worker-no-commit split: dispatcher -> worker -> independent reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`36041a985`; executionBaseHead captured from committed dispatch/session-sync HEAD; closureBaseHead equals executionBaseHead because worker does not commit |
| changedSetScope(phase) | dispatch=roadmap/baseline/work order; execution=exact two review outputs; closure=reviewer-owned closure paths; session=protected continuity only |
| traceScope(phase, actor) | each actor records only its own commands, changed set, manifest delta, and boundary |
| commitOwner(phase) | dispatch=dispatcher; execution=none; closure=independent reviewer/closer; session=session-sync steward |
| crossBatchIsolation | T1-T5, projection T1-T4, runtime/provider/live/public/push work remain parked |
| nextMoveSurfaces | worker must not edit; session-sync steward updates after accepted material closure |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_WEB_INHERITANCE_T0_COMPLETION_REVIEW_2026-07-18.md`

reviewerOwnedClosurePaths: the two worker outputs; this roadmap; paired GC-018
and work order; optional completion review when needed; protected continuity
only in a separate session-sync commit.

closureOwner: independent reviewer/closer.

workerCommitPermission: FORBIDDEN.

## Worker Return Packet Shape Contract

workerReturnPath:
`docs/reviews/CVF_WEB_INHERITANCE_T0_WORKER_RETURN_2026-07-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must contain Purpose, Target / Source, Scope / Methodology, Findings
/ Position, Risk / Corrective Action, Checker Source Read-Ahead Block, External
Knowledge Intake Routing, Corpus Completeness And Report Integrity, Finding-To-
Governance Learning Disposition, Epistemic Process Block, Agent Operation Trace
Block, Delta Execution Claim Boundary Control Block, Public Export Disposition,
Claim Boundary, git status evidence, Changed Files, Command Evidence, and a
No-Commit Statement.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $executionBaseHead --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --name-status
git diff --cached --name-status
git status --short
git rev-parse --short HEAD
```

## Current Runtime Freshness Verification

Current source was re-read during dispatch. SOT3 packages and their Web adapter
exist and are integrated with the execute path. Execution-plane and control-
plane MAO roots exist, but `cvf-execution-plane-foundation` is not a cvf-web
dependency and no current page exposes MAO. Provider/model selection is outside
this audit; the current provider registry remains
`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` with
`PROVIDER_CAPABILITY_REGISTRY`, and this packet makes no provider-registry
absence or hardcoding claim.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`frontend`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class frontend --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | Status; Dispatch Prompt Envelope; Role; Canonical packet; Commit mode; executionBaseHead; Current-time notes; Do-not-misread notes; Required first actions; Return contract; Authority Chain; Scope / Target / Owner Boundary; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; Roadmap-To-Work-Order Trace Matrix; Execution Plan; Evidence Requirements; Planned Worker Fulfillment Manifest; Acceptance Criteria; Review Gate; Closure Checklist; Stop Conditions; Worker Autonomy / No-Question Rule; Dual Agent Surface Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; COMPLETE_PENDING_REVIEW; BLOCKED_WITH_REASON; WORKER_MUST_NOT_COMMIT; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation after source and checker read-ahead |
| claimBoundary | structural dispatch conformance only; semantic acceptance remains reviewer-owned |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-INHERITANCE-T0 --title "Capability To Web Audit" --date 2026-07-18 --base 36041a985 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | completed exact source, seed, evidence, handoff, and return contracts |
| checkerReadAheadConfirmation | checker paths and literal families recorded above |
| docOnlyNewFields | inheritance ledger fields named above |
| claimBoundary | dispatch-authoring provenance only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | CVF-WEB-INHERITANCE-T0 dispatch, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | source reads, repository search, apply_patch, governance gates |
| Target paths | roadmap; GC-018 baseline; this work order |
| Allowed scope source | operator instruction to assess cvf-web inheritance |
| Before status evidence | clean worktree at `36041a985` |
| After status evidence | exact three-path dispatch set pending commit |
| Diff evidence | material diff captured before commit |
| Approval boundary | T0 read-only audit dispatch only |
| Claim boundary | no Web/source/test/runtime/provider/live/browser/public/push/production mutation |
| Agent type | dispatcher |
| Invocation ID | `cvf-web-inheritance-t0-dispatch-2026-07-18` |
| Expected manifest | roadmap; GC-018 baseline; work order |
| Actual changed set | exact three-path dispatch set before commit |
| Manifest delta | MATCH expected after verification |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | static capability-to-Web inheritance audit |
| claimDisposition | N/A with reason: no runtime execution-control behavior is implemented |
| receiptEvidence | N/A with reason: accepted reviews are read only and no runtime receipt is created |
| actionEvidence | N/A with reason: audit authoring is not runtime action evidence |
| invocationBoundary | exact T0 worker packet |
| interceptionBoundary | no IDE, shell, provider, filesystem, or agent-action interception claim |
| claimLanguage | inspect, classify, reconcile, and route only |
| forbiddenExpansion | Web/source/test/package mutation, browser, provider/live, public-sync, push, production, and universal inheritance claims |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance audit packet; no public-sync action authorized.

## Claim Boundary

This work order authorizes exactly one no-commit, two-output static audit. It
does not authorize cvf-web implementation, test/build/browser execution,
package or registry change, SOT3/MAO execution, sibling source copying,
provider/live work, public-sync, push, production, or universal inheritance
claims.
