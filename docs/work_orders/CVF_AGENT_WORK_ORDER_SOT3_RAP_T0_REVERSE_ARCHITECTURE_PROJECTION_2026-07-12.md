# CVF Agent Work Order - SOT3-RAP-T0 Reverse Architecture Projection

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-12

Work Order ID: SOT3-RAP-T0-WO

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `73326a907`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_MUST_CAPTURE_AT_CLOSURE`

## Dispatch Prompt Envelope

Role: no-commit Catalog/GAP projection worker.

Canonical packet: this work order and paired baseline.

Commit mode: WORKER_MUST_NOT_COMMIT

Base: capture HEAD/status before edits.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

Current-time notes: T2 is accepted at `9c7b05b40`; ADIF-0026/0027 are
committed; T0 projection is the only released work.

Do-not-misread notes: project accepted documentation/candidate facts only; do not
implement SOT3 runtime or modify checkers/generators.

Required first actions: read startup surfaces, roadmap, baseline, work order,
accepted T2, ADIF-0026/0027, Catalog/GAP schema/examples/generator/checker;
capture HEAD and status.

Return contract: one worker return with `COMPLETE_PENDING_REVIEW`, exact
changed set, command evidence, and unchanged HEAD.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-RAP-T0 --title "Reverse Architecture Projection" --date 2026-07-12 --base 73326a907 --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | no-commit documentation projection worker |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Added source verification, projection rows, generated-source rules, handoff, evidence, and closure controls. |
| checkerReadAheadConfirmation | dispatch-quality, structural, ADIF disclosure, handoff, scaffold provenance, worker-return, and Catalog drift checkers |
| docOnlyNewFields | SOT3 projection claim class |
| claimBoundary | Dispatch only; no projection execution proof. |

## Purpose

Execute the bounded reverse projection authorized by the matching GC-018.

## Target / Source

Roadmap: `docs/roadmaps/CVF_SOT3_REVERSE_ARCHITECTURE_PROJECTION_AND_REVIEW_COST_SYSTEMIZATION_ROADMAP_2026-07-12.md`.

Baseline: `docs/baselines/CVF_GC018_SOT3_RAP_T0_REVERSE_ARCHITECTURE_PROJECTION_2026-07-12.md`.

## Scope / Methodology

Read the accepted SOT3 contract family, inspect current Catalog/GAP schema and
examples, author compact source entries, regenerate aggregates, refresh human
front doors, and return without committing.

## Role Assignment

| Role | Owner |
|---|---|
| dispatcher | Codex/operator-controlled packet author |
| worker | one no-commit evidence and JSON projection worker |
| reviewer/closer | Codex reviewer owns semantic acceptance and commits |

## Authority Chain

- operator request to create the fresh roadmap/work order;
- accepted T2 material `9c7b05b40`;
- learning material `b054829a7`;
- this roadmap, baseline, and work order.

## Agent Roles

Operator authorizes scope; dispatcher owns packet fidelity; worker authors
projection without commit; reviewer/closer owns acceptance and commits.

## Worker Autonomy / No-Question Rule

Proceed autonomously within allowed paths. Repair owned-output gate failures.
Return blocked only for source drift, unresolved ownership conflict, forbidden
path need, or operator-level scope choice.

## Required First Reads

1. startup/session state and active handoff;
2. Guard Orientation and literal-format gotchas;
3. roadmap, baseline, and this work order;
4. accepted T2 review and three SOT reference outputs;
5. ADIF-0026 and ADIF-0027;
6. Catalog/GAP schema, front doors, compact examples, generator, and checker.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/generate_active_session_state.py --check
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | reviewer-accepted SOT3 evidence and current Catalog/GAP sources |
| Scope classification | INTERNAL_ARCHITECTURE_PROJECTION |
| Intake role | no-commit projection worker |
| Risk sensitivity | HIGH: prevents as-built overclaim and owner duplication |
| Provider surface | operator-selected local worker; no provider authority |
| Reviewer role | CVF reviewer validates projection semantics and commits |
| Routing decision | WORKER_MUST_NOT_COMMIT |
| Escalation condition | source drift, new schema field, ambiguous owner, forbidden path, or runtime claim |
| Public route | DEFERRED_PRIVATE_ONLY |
| canonical route mode | MULTI_AGENT_MULTI_ROLE |
| selected role route | dispatcher -> projection worker -> reviewer/closer |

## Allowed Scope

Only the seven artifact classes in the baseline Planned Artifact Manifest.
The exact count of compact entries is determined by semantic grouping, but it
must remain the minimum set that covers the roadmap's six projection rows.

## Forbidden Scope

Runtime, SOT3 schemas/tests/packages, generator/checker/hook changes, provider
or live work, Web/UI, public-sync, and session/handoff edits are forbidden.

## Source Verification Block

The baseline Source Verification Block is incorporated by exact path and commit
context. The worker must re-open every cited source and must stop with
`BLOCKED_SOURCE_NOT_FOUND` if any accepted path/symbol is absent or materially
changed.

| Claimed item | Fact class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Catalog source layout | EXISTS | `docs/reference/system_architecture_catalog/README.md` | Family Contents | `entries/` | Catalog family | ACCEPT |
| GAP source layout | EXISTS | `docs/reference/system_chain/gaps/README.md` | Canonical Source | `entries/` | GAP family | ACCEPT |
| Catalog generator function | EXISTS | `governance/compat/generate_as_built_system_catalog.py` | builder definitions | `build_catalog_aggregate` | generator | ACCEPT |
| GAP generator function | EXISTS | `governance/compat/generate_as_built_system_catalog.py` | builder definitions | `build_gap_index` | generator | ACCEPT |
| Drift checker entry point | EXISTS | `governance/compat/check_as_built_system_catalog_drift.py` | main definition | `main` | checker | ACCEPT |
| T2 accepted disposition | VALUE_SET | `docs/reviews/CVF_SOT3_T2_COMPLETION_REVIEW_2026-07-12.md` | Disposition | `REVIEWER_ACCEPTED_BOUNDED` | completion review | ACCEPT |

## ADIF Defect Registry Disclosure

Query:
`python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector "architecture catalog" --json`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0014, ADIF-0015,
ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024.

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Direct mandatory entries: `ADIF-0026`, `ADIF-0027`.

## Negative Search And Collision Discipline

| Field | Evidence |
|---|---|
| Search command | `rg -n -i "sot|refinery|truth.kernel|truth.flow|TruthReceipt|cvf.asc.(module|interface|gap).sot" docs/reference/system_architecture_catalog/entries docs/reference/system_chain/gaps/entries docs/reference EXTENSIONS governance .private_reference/legacy` |
| Search roots | Catalog/GAP compact JSON sources; current docs; runtime/extensions; governance source/tests; retained external evidence |
| Coverage | source, tests, docs, JSON, and external/legacy evidence |
| Absent versus collision disposition | classify every hit as `MATCH_EXISTING_OWNER`, `COLLISION_NON_AUTHORITATIVE`, or `ABSENT_WITH_COMMAND_EVIDENCE` |
| Required action | reuse matching owners and attach command evidence to every new candidate/gap decision |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> no-commit projection worker -> reviewer/closer |
| phase | SOT3-RAP-T0 reverse architecture projection |
| contractSource | canonical archive-qualified contract citation immediately above |
| baseHeadFor(phase) | dispatch=`73326a907`; execution=worker-captured HEAD; closure=reviewer-captured base |
| changedSetScope(phase) | planned Catalog/GAP source, generated, front-door, and worker-return paths only |
| traceScope(phase, actor) | worker source reads/schema/generator/diff evidence; reviewer semantic and closure evidence |
| commitOwner(phase) | worker=WORKER_MUST_NOT_COMMIT; reviewer owns commits |
| crossBatchIsolation | no T1 checker, runtime, session, provider, or public paths |
| nextMoveSurfaces | reviewer/session-sync steward only after acceptance |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_SOT3_RAP_T0_COMPLETION_REVIEW_2026-07-12.md`

reviewerOwnedClosurePaths: completion review and accepted material; continuity
only in a separate session-sync commit.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Evidence |
|---|---|---|
| six T0 projection rows | cover every row with Catalog/GAP disposition | worker return projection matrix |
| compact sources control aggregates | edit source entries then run generator | generator command output and diff |
| no runtime claim | use bounded claim classes | entry claim boundaries and reviewer audit |
| T1 held | do not edit checker/generator/hook sources | changed-set evidence |

## Execution Plan

1. Capture `executionBaseHead` and exact starting status.
2. Read roadmap, baseline, this work order, ADIF-0026/0027, accepted T2, schema,
   current entries, generator, and drift checker.
3. Build a six-row projection decision matrix before editing.
4. Author the minimum compact entries and README updates.
5. Run `python governance/compat/generate_as_built_system_catalog.py --target all`.
6. Run schema/generator tests and
   `python governance/compat/check_as_built_system_catalog_drift.py --enforce`.
7. Run worker-return fast gate and `git diff --check`.
8. Return `COMPLETE_PENDING_REVIEW`; do not commit.

## Write Ownership

Worker owns only planned projection outputs and worker return. Reviewer owns
completion review, accepted commits, and later continuity sync.

## Worker Return Packet Shape Contract

Worker return must include Purpose; Target / Source; Scope / Methodology;
Findings / Position; Risk / Corrective Action; Source Inventory; Projection
Matrix; command evidence; Checker Source Read-Ahead Block; Agent Operation
Trace Block; Finding-To-Governance disposition; Public Export Disposition; and
Claim Boundary.

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
python governance/compat/generate_as_built_system_catalog.py --target all
python governance/compat/check_as_built_system_catalog_drift.py --enforce
python -m pytest governance/compat/test_generate_as_built_system_catalog.py governance/compat/test_check_as_built_system_catalog_drift.py -q
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
git rev-parse --short HEAD
```

## Review Gate

Reviewer must run worker-return fast gate, independent stable-ID/schema audit,
hash/diff/status verification, and pre-closure on a real committed range.

## Closure Checklist

- [ ] six roadmap rows resolved;
- [ ] compact entries schema-valid;
- [ ] aggregates regenerated;
- [ ] both front doors refreshed;
- [ ] no runtime overclaim;
- [ ] worker HEAD unchanged and no commit;
- [ ] reviewer decision recorded.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`,
or `BLOCKED_WITH_REASON`. Never return a closed-equivalent worker status.

## Worker Return Conditions

The worker returns only after all verification commands pass or with one
explicit blocked condition and no commit.

## Return / Escalation Conditions

Return pending review after all checks pass. Escalate only a source-backed
owner ambiguity, schema change need, forbidden-path dependency, or scope change.

## Return Protocol

Return the worker packet to the named reviewer/closer with exact HEAD, status,
changed-set, generator, schema, drift, and fast-gate evidence. Do not commit.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: T0 projects already accepted SOT3 decisions into
current Catalog/GAP owners; it does not rescan, reclassify, or close the
underlying legacy corpus coverage index.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | accepted retained SOT evidence -> CVF owner reconciliation -> Catalog/GAP reverse projection |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing as-built Catalog and system-chain GAP compact sources |
| Disposition | ADAPT |
| Claim boundary | projection of accepted evidence only; no new external absorption or runtime import |

## Operator Checkpoint

No checkpoint is needed for source-backed in-scope projection. Stop for a new
schema field, checker/generator change, runtime claim, or ambiguous owner choice
that materially changes architecture.

## Evidence Requirements

- exact stable IDs and source paths;
- command-backed generated aggregate evidence;
- schema and drift pass;
- `git diff --name-status` and `git status --short`;
- explicit no-runtime/no-checker/no-public boundary;
- review-cost telemetry for this worker/reviewer cycle when available.

## Acceptance Criteria

- every roadmap projection row resolved;
- minimum non-duplicative entry set;
- front doors and generated artifacts consistent;
- no as-built runtime overclaim;
- all gates pass;
- worker HEAD unchanged and no commit.

## Fail Conditions

Any baseline fail condition, missing source symbol, schema error, generated
drift, unexplained projection row, forbidden path, runtime overclaim, or worker
commit returns the packet to the reviewer.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_as_built_system_catalog_drift.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Reviewer Closure Conversion; Roadmap-to-Work-Order Trace Matrix; Public Export Disposition |
| gateRunPurpose | confirm author-derived source fidelity and provide dispatch evidence |
| claimBoundary | machine gates do not replace semantic reviewer audit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | SOT3-RAP-T0 packet authoring, 2026-07-12 |
| Working directory | repository root |
| Command or tool surface | governed reads, rg, ADIF resolver, apply_patch, dispatch gates |
| Target paths | roadmap; matching GC-018 baseline; this work order |
| Allowed scope source | operator request to create the fresh roadmap and work order after clean SOT3-T2 closure |
| Before status evidence | HEAD `73326a907`; clean worktree; T2 accepted; projection next move recorded |
| After status evidence | T0 packet authored; implementation remains undispatched until gates pass |
| Diff evidence | exact three-path packet diff before commit |
| Approval boundary | packet authoring and dispatch only; worker must not commit |
| Claim boundary | no projection execution, runtime, checker, provider/live, public, or readiness claim |
| Agent type | dispatcher |
| Invocation ID | `sot3-rap-t0-dispatch-authoring-2026-07-12` |
| Expected manifest | roadmap; matching GC-018 baseline; this work order |
| Actual changed set | roadmap; matching GC-018 baseline; this work order |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet.

## Claim Boundary

This work order authorizes one bounded no-commit worker after all pre-dispatch
gates pass. It does not authorize SOT3 runtime or T1 machine enforcement.
