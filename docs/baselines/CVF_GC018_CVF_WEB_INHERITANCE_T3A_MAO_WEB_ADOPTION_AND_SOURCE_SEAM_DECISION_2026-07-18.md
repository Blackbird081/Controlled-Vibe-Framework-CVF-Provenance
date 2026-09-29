# CVF GC-018 Baseline - MAO Web Adoption And Source Seam Decision

Memory class: governed-dispatch-baseline

Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS

Batch ID: CVF-WEB-INHERITANCE-T3A

Dispatch base head: `296029998`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: CVF independent reviewer/closer

Worker target: delegated source-audit worker

## Purpose

Resolve the missing source seam between current MAO owners and cvf-web before
any T3 operator page or dependency change. Produce one terminal, source-backed
decision for T3B without guessing persistent evidence, liveness, milestone,
configuration, privacy, or caller semantics.

## Scope / Target / Owner Boundary

This is a two-output documentation-only audit. The worker reads current
cvf-web, control-plane MAO, execution-plane MAO, package metadata, and accepted
T0/T2 evidence. It does not edit any package, runtime, source, test, page,
state, registry, or generated aggregate.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Disposition |
|---|---|---|---|
| T2 accepted | `docs/reviews/CVF_WEB_INHERITANCE_T2_COMPLETION_REVIEW_2026-07-18.md` | `609edffbe` | ACCEPT |
| roadmap T3A release | `docs/roadmaps/CVF_WEB_CAPABILITY_INHERITANCE_AND_OPERATOR_PROJECTION_ROADMAP_2026-07-18.md` | pending this dispatch commit | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| cvf-web depends on control plane but not execution plane | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependencies lines 20-35 | `dependencies` | npm package manifest | ACCEPT |
| current Web source has no execution-plane import and no MAO symbol consumer | RUNTIME_BEHAVIOR | `docs/reviews/CVF_WEB_INHERITANCE_T0_CAPABILITY_TO_WEB_LEDGER_2026-07-18.md` | WEB-05 through WEB-07 rows plus direct negative search refreshed at dispatch | `WEB-05`; `WEB-06`; `WEB-07` | accepted Web inheritance ledger | ACCEPT |
| control-plane package exports MAO resolver and pure composition | EXISTS | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.mao.barrel.ts` | lines 17 and 24 | `resolveRole`; `composeOrchestrationPlan` | control-plane MAO barrel | ACCEPT |
| operational operator projection exists in execution plane | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.operator.projection.ts` | lines 68-115 and 149-226 | `buildOperationalOperatorProjection` | MAO operational operator projection | ACCEPT |
| operational projection has only caller-supplied inputs and no runtime caller | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.operator.projection.ts` | lines 12-17 | `MaoOperationalOperatorProjectionInput` | MAO operational operator projection | ACCEPT |
| durable store resumes one named task graph | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | lines 98-159 | `resumeRun` | `MaoFileRunStore` | ACCEPT |
| MAO evidence ledger is in-memory and exposes records from its instance | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | lines 153-227 | `MaoEvidenceLedger` | evidence readout contract | ACCEPT |
| roadmap requires read-only run, evidence, milestone, and liveness projection | VALUE_SET | `docs/roadmaps/CVF_WEB_CAPABILITY_INHERITANCE_AND_OPERATOR_PROJECTION_ROADMAP_2026-07-18.md` | Tranche Plan | `CVF-WEB-INHERITANCE-T3` | roadmap | ACCEPT |

## New Doc-Only Fields

| Field | Purpose |
|---|---|
| `sourceSeamDisposition` | terminal T3A route token |
| `requiredOwnerChange` | exact prerequisite owner or N/A with reason |
| `t3bAllowedScopeCandidate` | proposed implementation paths only after reviewer acceptance |
| `claimableReadoutDimensions` | dimensions directly supported by existing source |

## Initial Contradiction

The current T3 goal cannot be dispatched as a page directly. The existing
operational readout owner requires an in-memory `MaoEvidenceLedger` and other
caller snapshots, but current source identifies no persistent reconstruction
or Web caller. The durable store replays graph events for one known graph ID;
it is not direct evidence that the separate evidence ledger can be listed or
reconstructed. T3A resolves this contradiction instead of asking a worker to
invent an adapter contract.

## Required Decision Vocabulary

Select exactly one terminal `sourceSeamDisposition`:

- `ADOPT_EXECUTION_PLANE_DEPENDENCY_WITH_VERIFIED_READ_SEAM`;
- `CONTROL_PLANE_ONLY_BOUNDED_PROJECTION`;
- `SPLIT_T3B_PREREQUISITE_OWNER_REQUIRED`; or
- `DEFER_WITH_REASON`.

The selected route must cite existing owners for every claimed readout
dimension. A missing owner must be explicit and cannot be converted into an
implementation assumption.

## Required Source-Seam Matrix

The decision artifact must resolve control-plane MAO consumption,
execution-plane dependency, run discovery, durable replay, evidence-ledger
persistence/reconstruction, task-state read model, liveness, milestones,
configuration, privacy projection, build/package impact, and Web caller
ownership. Each row must name its current source owner, observed contract,
gap, T3B implication, and terminal disposition.

## Baseline Decision

Dispatch one documentation-only source-seam audit before any T3B Web change.
The baseline does not preselect the terminal route; it requires the worker to
resolve the contradiction through direct current-source evidence.

## Verification / Evidence

Worker evidence must include refreshed source citations and negative searches,
13 terminal matrix rows, exactly one decision token, a T3B candidate boundary
or checkable defer condition, file-size enforcement, worker-return fast gate,
exact changed set, empty cached diff, unchanged execution HEAD, and no-commit
statement.

## Allowed Scope

1. `docs/reviews/CVF_WEB_INHERITANCE_T3A_MAO_WEB_ADOPTION_AND_SOURCE_SEAM_DECISION_2026-07-18.md`
2. `docs/reviews/CVF_WEB_INHERITANCE_T3A_WORKER_RETURN_2026-07-18.md`

## Forbidden Scope

- no package manifest, lockfile, source, test, page, route, API, config,
  environment, state, registry, or generated-aggregate edit;
- no new field or function claimed as existing source;
- no worker launch, durable write, queue, process, provider, network, live
  proof, browser automation, public-sync, push, or production action;
- no T3B, T4, or T5 implementation; and
- no worker staging, stash, commit, or session mutation.

## Acceptance Criteria

- AC-01: every required source-seam row is terminal and directly cited.
- AC-02: event-ledger and evidence-ledger ownership are not conflated.
- AC-03: package presence, symbol consumption, runtime caller, and operator
  visibility remain separate claims.
- AC-04: one decision token is selected with explicit value and risk rationale.
- AC-05: the decision either supplies an exact source-backed T3B prerequisite
  and candidate scope or records a bounded defer with a checkable reopen rule.
- AC-06: exactly two output paths change; nothing is staged; worker HEAD stays
  unchanged.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| two new output paths | `Test-Path` returned False before authoring | ACCEPT |
| execution-plane package token in cvf-web manifest and lock | direct search returned no execution-plane package row | ACCEPT |
| execution-plane and MAO symbol imports in cvf-web source | direct search returned no execution-plane import and no MAO consumer | ACCEPT |
| collision decision | no existing T3A decision or worker-return owner exists | ACCEPT |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | current package and MAO source owners | read and classify only | terminal seam matrix | no adapter implementation | `DOCUMENTATION_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no changed interface | no ingress, action, receipt, or mutation | no adapter output | parked | `N/A_WITH_REASON` |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class architecture --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Status; Scope / Target / Owner Boundary; Dependency Release Evidence; Source Verification Block; Acceptance Criteria; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation after direct source verification |
| claimBoundary | structural conformance does not select the T3A decision |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-INHERITANCE-T3A --title "MAO Web Adoption And Source Seam Decision" --date 2026-07-18 --base 296029998 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit and Web claim-boundary profiles |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled exact source contradiction, decision vocabulary, seam matrix, outputs, and no-implementation boundary |
| checkerReadAheadConfirmation | checker paths listed above |
| docOnlyNewFields | four fields listed in New Doc-Only Fields |
| claimBoundary | dispatch-authoring provenance only |

## Current Runtime Freshness Verification

At dispatch base `296029998`, cvf-web has the control-plane dependency but no
MAO symbol consumer or execution-plane package row. The current execution-plane
operator projection is pure and caller-supplied; the evidence ledger is
in-memory; the durable store resumes one known graph. These current facts are
the reason for T3A.

## Web/UI Claim Boundary

`DESIGN.md` was read for roadmap continuity. T3A changes no UI. No hosted,
live-data, production-readiness, or operator-value claim is authorized.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance source-decision dispatch; no public-sync action.

## Claim Boundary

This baseline authorizes exactly two documentation outputs deciding the MAO
Web source seam. It does not authorize dependency, runtime, source, test, UI,
provider/live, public, push, release, production, or session mutation.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this file | `Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS` | PASS |
| Work order status | paired T3A work order | `Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS` | PASS |
| Completion or reviewer artifact | T3A completion review | `Status: REVIEWER_ACCEPTED_WITH_REPAIRS` | PASS |
| Worker return | T3A worker return | `Status: ACCEPTED_BY_REVIEWER_WITH_REPAIRS` | PASS |
| Roadmap state | CVF Web inheritance roadmap | `Status: CVF_WEB_INHERITANCE_T3A_PASS_T3P1_PACKET_AUTHORING_NEXT` | PASS |
| Registry JSON | corpus registry generated aggregate | existing governed docs scope coverage; aggregate drift check passed | PASS |
| Registry Markdown | corpus registry read model | existing governed docs scope coverage | PASS |
| External evidence digest | N/A with reason: repository-local source audit | none | N/A with reason |
| System loop interlock | N/A with reason: no loop owner changed | none | N/A with reason |
| Session continuity | protected session surfaces | separate session-sync commit follows material closure | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence | N/A with reason: documentation-only source decision | N/A_WITH_REASON |
| Query acceptance evidence | 13 terminal source-seam rows independently recomputed | PASS |
| Worker-return acceptance | exact two paths, unchanged HEAD, no staging, gates passed | PASS |
| Closure claim | split prerequisite owner required, with reviewer repairs | PASS |
