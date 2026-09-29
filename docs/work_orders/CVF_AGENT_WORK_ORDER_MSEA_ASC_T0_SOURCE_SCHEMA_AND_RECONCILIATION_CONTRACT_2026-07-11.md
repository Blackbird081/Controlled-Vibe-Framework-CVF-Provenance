# CVF Agent Work Order MSEA-ASC-T0 Source Schema And Reconciliation Contract

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA-ASC-T0

Dispatch base head: `4c1abb6ff`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: delegated worker. Canonical packet: this work order. Commit mode:
`WORKER_MUST_NOT_COMMIT`. executionBaseHead: the dispatch-session HEAD provided
after reviewer commit/sync.

Current-time notes: 2026-07-11; use current governed sources at execution HEAD.

Do-not-misread notes: T0 designs schema and reconciliation contracts only. Do
not inventory/populate the catalog, create gap entries/index, implement a
generator/checker, edit R91 maps/checkers, or commit.

Required first actions: read startup sources, paired GC-018, roadmap, critique
classification, schema/freshness/generation authorities, then run the
pre-implementation gate from executionBaseHead.

Return contract: create exactly four reference/schema outputs plus one worker
return, run required gates, report `COMPLETE_PENDING_REVIEW`, and stop without
commit or session mutation.

## Purpose

Produce the ASC-T0 source schema and reconciliation contract needed to prevent
later inventory, edge graph, gap index, diagram, and freshness tranches from
encoding incompatible assumptions.

## Authority Chain

Operator authorization -> MSEA-ASC roadmap -> Claude critique -> Codex
classification/fold -> paired GC-018 -> this work order -> worker return ->
Codex reviewer/closer.

## Agent Roles

- Worker: authors exactly the allowed T0 outputs and evidence; no commit.
- Reviewer/closer: independently checks source fidelity, schema coherence,
  topology decisions, scope, gates, and commit conversion.
- Session-sync steward: updates continuity only after accepted material commit.

## Scope / Target / Owner Boundary

Allowed material outputs:

- `docs/reference/system_architecture_catalog/README.md`
- `docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_SCHEMA.json`
- `docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_RECONCILIATION_CONTRACT.md`
- `docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_TOPOLOGY_DECISIONS.md`
- `docs/reviews/CVF_MSEA_ASC_T0_SOURCE_SCHEMA_AND_RECONCILIATION_CONTRACT_WORKER_RETURN_2026-07-11.md`

Forbidden scope:

- no edits outside those five paths;
- no full-repository inventory or catalog records;
- no `gaps/` directory, entries, README, JSON index, or generator;
- no freshness checker, hook, workflow, registry, or tests;
- no R91 map/README/freshness edits;
- no architecture diagrams or front-door implementation;
- no doctrine, module inventory, control matrix, runtime, Web, provider,
  public-sync, legacy, session, or handoff mutation;
- no commit, push, live proof, destructive action, or secrets access.

## Write Ownership

Worker owns exactly the five uncommitted outputs above. Reviewer owns any
accepted closure conversion and later session sync.

## Dependency Release Evidence

| Dependency | Evidence | Commit | Disposition |
|---|---|---|---|
| roadmap proposed and critiqued | `docs/roadmaps/CVF_AS_BUILT_ARCHITECTURE_AND_SYSTEM_CATALOG_ROADMAP_2026-07-11.md` | `6485fc7ad` | SATISFIED |
| critique classified | `docs/reviews/CVF_MSEA_ASC_CLAUDE_REBUTTAL_CODEX_CLASSIFICATION_2026-07-11.md` | `6485fc7ad` | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-ASC-T0 --title "Source Schema And Reconciliation Contract" --date 2026-07-11 --base 4c1abb6ff --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | generic worker dispatch with worker-return skeleton |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | exact five-path T0 scope, topology decisions, and no-implementation boundary |
| checkerReadAheadConfirmation | dispatch, worker-return, trace, source verification, roadmap, external routing, public guards |
| docOnlyNewFields | catalog schema entity/field/enums and topology decision vocabulary |
| claimBoundary | scaffold provenance only |

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. active handoff named by state
4. paired MSEA-ASC-T0 GC-018
5. `docs/roadmaps/CVF_AS_BUILT_ARCHITECTURE_AND_SYSTEM_CATALOG_ROADMAP_2026-07-11.md`
6. `docs/reviews/CVF_MSEA_ASC_ARCHITECTURE_CATALOG_ROADMAP_CLAUDE_REBUTTAL_2026-07-11.md`
7. `docs/reviews/CVF_MSEA_ASC_CLAUDE_REBUTTAL_CODEX_CLASSIFICATION_2026-07-11.md`
8. `docs/reference/system_chain/CVF_SYSTEM_CHAIN_FRESHNESS_STANDARD.md`
9. `governance/compat/check_system_chain_map_freshness.py`
10. `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md`
11. `docs/reference/CVF_VALUE_PARKED_LANE_REOPEN_DISCIPLINE_STANDARD_2026-06-25.md`
12. R98 and R99 completion reviews named in the Source Verification Block.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: the legacy absorption coverage index is not corpus
authority for T0. The worker may read no legacy content; T0 designs current
CVF-owned schema contracts only.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | Claude critique -> Codex classification -> T0 requirements |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | MSEA-ASC roadmap and T0 contracts |
| Disposition | ADAPT only the internally verified findings recorded by Codex |
| Claim boundary | external critique is advisory and cannot define CVF authority |

## Pre-Flight Checks

- Confirm executionBaseHead and record initial `git status --short`.
- Confirm exactly zero pre-existing worker-owned output paths.
- Run pre-implementation with a real base/head context.
- Read checker literal requirements before authoring outputs.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T0 output requirements | VALUE_SET | `docs/roadmaps/CVF_AS_BUILT_ARCHITECTURE_AND_SYSTEM_CATALOG_ROADMAP_2026-07-11.md` | ASC-T0 | ASC-T0 - Source Schema And Reconciliation Contract | roadmap | ACCEPT |
| R91 fixed family | VALUE_SET | `governance/compat/check_system_chain_map_freshness.py` | module constants | MAP_PATH; EXPECTED_LANE_COUNT; CANONICAL_LANE_IDS | R91 freshness checker | ACCEPT |
| deterministic aggregate discipline | VALUE_SET | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | Protocol / Contract / Requirements | compact source layout; deterministic generator; drift check | generated aggregate discipline | ACCEPT |
| L1 current state | VALUE_SET | `docs/reviews/CVF_MSEA_R99_L1_SYSTEM_DEFINITION_OWNER_DESIGN_COMPLETION_2026-07-11.md` | Findings / Position | ACTIVE_OWNER_CREATED_WITH_BOUNDARY | R99 review | ACCEPT |
| L2 current state | VALUE_SET | `docs/reviews/CVF_MSEA_R98_L2_BUILD_PROTOCOL_OWNER_RATIFICATION_COMPLETION_2026-07-11.md` | Findings / Position | NAMED_DIFFERENTLY_ACTIVE_OWNER_WITH_BOUNDARY | R98 review | ACCEPT |

## Current Runtime Freshness Verification

N/A with reason: T0 defines documentation/schema contracts only.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`documentation`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class documentation --role dispatcher --lifecycle-phase dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | none |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_foundation_storage_layout.py` |
| literalTokensReviewed | DISPATCH_READY; WORKER_MUST_NOT_COMMIT; completion state; exact manifest; public disposition; foundation storage |
| gateRunPurpose | confirmation and evidence after source-backed packet authoring; not first discovery |
| claimBoundary | T0 worker dispatch only |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | Produce source schema and reconciliation/topology contracts only. |
| scopeClassification | DOCUMENTATION_AND_SCHEMA_ONLY |
| riskSensitivity | R1 |
| Selected role route | routeMode=`SINGLE_AGENT_SINGLE_ROLE`; one delegated worker executes, then reviewer/closer converts if accepted. |
| roleSeparationBasis | worker returns no-commit artifacts; Codex reviews source/semantic correctness |
| escalationCondition | implementation, source mutation, authority ambiguity, or scope expansion |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> delegated worker -> reviewer/closer -> session-sync steward |
| phase | DISPATCH, IMPLEMENTATION, REVIEW, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=4c1abb6ff; executionBaseHead=dispatch session commit; closureBaseHead=executionBaseHead |
| changedSetScope(phase) | two dispatch paths; five worker outputs; reviewer closure; separate protected sync |
| traceScope(phase, actor) | source reads, schema decisions, exact manifest, gates, diff |
| commitOwner(phase) | worker none; reviewer/closer material; steward session sync |
| crossBatchIsolation | initial clean worktree required; unrelated changes prohibited |
| nextMoveSurfaces | reviewer updates only after accepted material commit |

## Dual Agent Surface Matrix

| Agent surface | Role | Interface | Authority and risk boundary | Required evidence | Adapter boundary and disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | dispatcher/reviewer/closer | governed docs, source tree, gates | final CVF classification and commit authority | source verification, diff, gate receipts | ALLOWED |
| EXTERNAL_AGENT_CLI_MCP | delegated worker | local file and shell tools | no commit, no authority expansion | five outputs and worker return | ALLOWED_BOUNDED_NO_COMMIT |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_ASC_T0_SOURCE_SCHEMA_AND_RECONCILIATION_CONTRACT_COMPLETION_2026-07-11.md`

reviewerOwnedClosurePaths: worker outputs plus optional completion review only
if needed for material reviewer corrections; separate session paths.

closureOwner: Codex reviewer/closer.

workerCommitPermission: FORBIDDEN

## Roadmap-to-Work-Order Trace Matrix

| ASC-T0 requirement | Required output/evidence |
|---|---|
| schema and field vocabulary | JSON Schema plus reconciliation contract |
| stable IDs and enums | JSON Schema definitions and examples |
| reconciliation rules | precedence/conflict/source-view matrix |
| generated source layout | topology decision with reserved paths and determinism contract |
| bounded migration plan | reconciliation contract migration table from current sources |
| freshness topology | explicit R91 widening versus scoped sibling decision |
| front-door topology | dedicated as-built front door versus delimited R91 README decision |

## Work-Order Fulfillment Manifest

| Artifact | Required action |
|---|---|
| catalog README | describe T0 contract family, boundaries, future routes |
| schema JSON | define entities, fields, enums, conditional requirements, ID grammar |
| reconciliation contract | define precedence, conflict, negative search, lineage, migration, admission |
| topology decisions | decide generated layout, determinism, freshness ownership, front-door boundary |
| worker return | exact evidence, limitations, status, no-commit handoff |

## Execution Plan

1. Capture executionBaseHead, clean initial status, and required source reads.
2. Draft schema JSON and validate parseability after each material revision.
3. Draft reconciliation contract from current authority/view boundaries.
4. Record terminal generated-layout, freshness, and front-door decisions with
   rejected alternatives and deferred implementation paths.
5. Cross-check all minimum requirements, exact five-path manifest, and claims.
6. Create worker return, run gates, report terminal no-commit status, and stop.

## Schema Minimum Requirements

The JSON Schema must cover:

- entity types: PLANE, MODULE, INTERFACE, EDGE, CONTROL, EVIDENCE_OWNER,
  OPERATOR_SURFACE, GAP, AUTHORITY_SOURCE;
- stable IDs, authority class, maturity, owner paths, plane membership,
  inbound/outbound edge IDs, citations, claim boundary, freshness inputs;
- `boundaryCaveat`, `rejectedCandidates`, `negativeSearchEvidence`,
  `priorDisposition`, `supersededBy`;
- edge proof classes, evidence recency, operator visibility;
- gap terminal statuses, structured close/reopen conditions, action owner;
- admission dispositions and generated-source metadata;
- conditional constraints preventing `OPERATOR_VISIBLE_EDGE` when visibility is
  CI_ONLY/RAW_EVIDENCE_ONLY/ABSENT;
- no claims that all records already exist.

## Reconciliation Precedence Requirements

The contract must distinguish authority and view ownership rather than choose
one file as universally superior. At minimum reconcile doctrine/layer route,
architecture view, system-chain map, module inventory, governance control
matrix, accepted reviews, runtime source, and future catalog/gap source views.
Conflicts require terminal disposition and source citation; recent review does
not override runtime source for runtime facts, and runtime source does not
override frozen doctrine authority.

## Freshness And Front-Door Decision Requirements

Choose one freshness topology with tradeoffs and rejected alternative:

1. keep R91 strictly five-lane and reserve a scoped sibling catalog freshness
   family with non-overlapping owner/inputs; or
2. formally version/widen R91 schema/checker later through a protected T5
   implementation packet.

Do not implement either. Also choose a dedicated as-built front door by
default unless source evidence justifies a later delimited R91 README change.

## Verification Commands

```powershell
python -m json.tool docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_SCHEMA.json
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast --parallel
git diff --check
git status --short
```

## Acceptance Criteria

- Exactly five worker-owned output paths exist and no other path changes.
- JSON parses and expresses every minimum schema requirement.
- Current R98/R99 dispositions are represented without reopening them.
- Freshness topology has one selected option, rejected alternative, owner
  boundary, reserved future paths, and implementation-deferred statement.
- Generated-layout contract defines compact sources, deterministic UTF-8/LF
  stable ordering, aggregate drift proof, and aggregate-only edit rejection.
- Front-door topology avoids silent expansion of the R91 README contract.
- Reconciliation contract has precedence/conflict/lineage/negative-search and
  external-absorption admission rules.
- No catalog population, checker, generator, gap index, diagram, runtime,
  public, provider, session, or commit mutation occurs.
- Worker return truthfully records `COMPLETE_PENDING_REVIEW` and dirty status.

## Evidence Requirements

Provide file/section or symbol citations, schema validation output, exact
changed-set evidence, targeted vocabulary searches, worker-return fast-gate
output, reviewer-fast output where applicable, and `git diff --check`.

## Worker Autonomy / No-Question Rule

Repair allowed-scope defects and gate failures without asking the operator.
Stop only when a required source fact is absent, two topology choices remain
materially undecidable after source review, or forbidden scope is required.

## Negative And Fail-Condition Scan

Fail for guessed existing fields, external-review-as-authority, universal
precedence, proof-class inflation, CI-only operator visibility, free-text-only
reopen conditions, aggregate-only editing, R91 semantic mutation, output path
expansion, commit, or false clean-worktree claim.

## Review Gate

Return `COMPLETE_PENDING_REVIEW` only after direct semantic self-check and all
worker-required gates pass. Codex must independently review topology decisions
and may return the packet for correction.

## Closure Checklist

- [ ] Five outputs only.
- [ ] Schema parses and covers minimum requirements.
- [ ] Reconciliation and topology decisions are terminal.
- [ ] R98/R99 lineage retained.
- [ ] No implementation or population.
- [ ] Worker did not commit.
- [ ] Exact dirty status reported.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if an existing source claim cannot be verified or
a topology decision needs new authority. Do not invent or implement around the
block.

## Negative Search And Collision Discipline

Before claiming a new field, enum, file family, generator path, or checker path,
search current governed sources for the exact token and likely owner family.
Record `DOC_ONLY_NEW` for proposed schema vocabulary and reserved future paths.
Reject duplicate owners and report any collision with an existing canonical
field, route, aggregate, or freshness family.

## Operator Checkpoint

No checkpoint during allowed-scope execution. Reviewer acceptance is required
before any ASC-T1 packet or implementation.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated worker |
| Provider or surface | external agent CLI/MCP or equivalent local worker surface |
| Session or invocation | MSEA-ASC-T0 worker execution |
| Working directory | repository root |
| Command or tool surface | read, search, apply_patch, JSON validation, gates, git status/diff |
| Target paths | exact five output paths |
| Allowed scope source | paired GC-018 and this work order |
| Before status evidence | clean worktree at executionBaseHead |
| After status evidence | exactly five uncommitted worker-owned paths |
| Diff evidence | `git diff --name-status`; `git status --short`; `git diff --check` |
| Approval boundary | no commit; reviewer owns acceptance |
| Claim boundary | T0 schema/reconciliation/topology contracts only |
| Agent type | delegated worker |
| Invocation ID | msea-asc-t0-worker-2026-07-11 |
| Expected manifest | five paths in Scope / Target / Owner Boundary |
| Actual changed set | worker must list all five exact paths |
| Manifest delta | must be MATCH |
| Deletion or rename disposition | N/A with reason: none authorized |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | T0 schema, reconciliation, migration, and topology decisions |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt applies |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source reads, schema validation, diff, gates |
| invocationBoundary | documentation/schema authoring only |
| interceptionBoundary | no provider runtime, Web, proxy, or execution interception |
| claimLanguage | contract design, not implemented/populated catalog |
| forbiddenExpansion | no inventory, gap index, generator, checker, diagram, runtime, public, provider, session, or commit |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance T0 design tranche.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| owner family | `docs/reference/system_architecture_catalog/` |
| schema | JSON Schema contract, not aggregate data |
| compact source layout | reserved future path and contract only |
| aggregate/generator/checker | implementation deferred to ASC-T3/T5 packets |
| duplicate owner prevention | README routes to existing R91/system-chain owners |

## Worker Return Packet Shape Contract

Worker return must be created at
`docs/reviews/CVF_MSEA_ASC_T0_SOURCE_SCHEMA_AND_RECONCILIATION_CONTRACT_WORKER_RETURN_2026-07-11.md`
with `Status: COMPLETE_PENDING_REVIEW` or `Status: BLOCKED_WITH_REASON` and include:

- `executionBaseHead`
- dispatch work-order path
- `Purpose`
- `Target / Source`
- `Scope / Methodology`
- `Findings / Position`
- `Risk / Corrective Action`
- `Checker Source Read-Ahead Block`
- `Agent Operation Trace Block`
- `Delta Execution Claim Boundary Control Block`
- `Public Export Disposition`
- `Claim Boundary`
- exact changed files, command evidence, `git status --short`, and no-commit statement.

Conditional sections must be present with evidence or exact N/A-with-reason:

- `External Knowledge Intake Routing`
- `Rescan Intelligence Hardening`
- `Corpus Completeness And Report Integrity`
- `Finding-To-Governance Learning Disposition`
- `Epistemic Process Block`
- `Machine Closure Package`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Claim Boundary

This work order authorizes T0 contracts only. It does not authorize catalog
records, gap management implementation, freshness code, diagrams, or ASC-T1+.
