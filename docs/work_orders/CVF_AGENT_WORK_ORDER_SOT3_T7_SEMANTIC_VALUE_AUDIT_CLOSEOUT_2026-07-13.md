# CVF Agent Work Order - SOT3-T7 Semantic Value Audit And Closeout

Memory class: FULL_RECORD

Status: PROPOSED_PRE_DISPATCH

Date: 2026-07-13

Work Order ID: SOT3-T7

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `2c4c498da`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_MUST_CAPTURE_AT_CLOSURE`

## Dispatch Prompt Envelope

Role: no-commit semantic audit worker.

Canonical packet: this work order and paired T7 GC-018.

Commit mode: WORKER_MUST_NOT_COMMIT

Base: capture HEAD and clean full status before edits.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

Current-time notes: T6 accepted at `2c4c498da`; T7 is the final semantic and GAP audit.

Do-not-misread notes: zero unresolved requires semantic evidence; do not implement the packet-hash GAP.

Required first actions: startup reads, T0 ledger, T1-T6 reviews, Catalog/GAP
owners, paired baseline.

Return contract: complete audit evidence and `COMPLETE_PENDING_REVIEW`, no commit.

## Purpose

Define the held final semantic audit: reconcile every one of the 305 retained
source items to a terminal conversion disposition and close the parked-value
index without silently discarding architectural value.

## Target / Source

Future outputs are a T7 semantic audit, terminal conversion ledger,
parked-value reconciliation, and worker return under `docs/reviews/` and
`docs/evidence/sot/`. Exact dependency anchors must be refreshed after T6.

## Scope / Methodology

Reopen the T0 manifest and processing ledger, then map every source item to an
accepted CVF owner, explicit adaptation, documented rejection, or parked item
with a concrete reopen condition. Reconcile arithmetic to 305 and unresolved
value to zero. This is documentation/evidence closeout only.

## Authority Chain

Operator continuation -> SOT3 roadmap -> accepted T0-T6 evidence -> future
fresh T7 GC-018 -> refreshed T7 work order.

## Agent Roles

Dispatcher refreshes dependencies; worker audits without commit; reviewer/
closer accepts evidence; session-sync steward closes continuity.

## Worker Autonomy / No-Question Rule

Resolve in-scope ledger, evidence, and documentation defects without asking the
operator. Stop only for missing canonical source, value requiring a new
runtime/owner tranche, forbidden paths, or scope expansion.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | accepted T0-T6 evidence and retained T0 manifest |
| Scope classification | SEMANTIC_AUDIT_AND_CLOSEOUT |
| Intake role | no-commit audit worker |
| Risk sensitivity | HIGH: false zero-unresolved claim |
| Provider surface | local deterministic tools only |
| Reviewer role | semantic sampling, owner/GAP and arithmetic audit |
| Routing decision | WORKER_MUST_NOT_COMMIT |
| Escalation condition | ownerless value, runtime need, or missing source |
| Public route | DEFERRED_PRIVATE_ONLY |
| canonical route mode | MULTI_AGENT_MULTI_ROLE |
| selected role route | dispatcher -> audit worker -> reviewer/closer |

## Required First Reads

Startup front doors, guard orientation, literal gotchas, roadmap, T0 manifest
and ledger, T1-T6 completion reviews, Catalog/GAP front doors, and fresh T7
GC-018.

## Pre-Flight Checks

After release, capture HEAD/full status and run generated-state plus
pre-implementation gates. Current packet is held, so do not execute.

## Write Ownership

Future worker owns only released T7 docs/evidence paths and must not commit.

## Dependency Release Evidence

| Dependency | Required evidence | Current disposition |
|---|---|---|
| T6 vertical slice | `docs/reviews/CVF_SOT3_T6_COMPLETION_REVIEW_2026-07-13.md`; `2c4c498da` | SATISFIED |
| fresh T7 GC-018 | `docs/baselines/CVF_GC018_SOT3_T7_SEMANTIC_VALUE_AUDIT_CLOSEOUT_2026-07-13.md` | SATISFIED |
| refreshed base anchors | clean material closure `2c4c498da` | SATISFIED |

T6 dependencies are released. Worker execution remains unauthorized until this
refreshed packet and baseline pass pre-dispatch and the reviewer explicitly
marks the packet dispatch-ready.

## Allowed Scope

Documentation and evidence paths explicitly named by the future T7 GC-018.

## Forbidden Scope

Any package/runtime mutation; retained-root mutation; checker/hook mutation;
session state by worker; provider/live; public-sync; activation; adapters.

## Source Verification Block

Roadmap facts are verified from
`docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md`, Tranche
Plan SOT3-T7. T6 closure is verified from
`docs/reviews/CVF_SOT3_T6_COMPLETION_REVIEW_2026-07-13.md` and material commit
`2c4c498da`. The paired fresh GC-018 controls remaining source verification.

## Acceptance Criteria

- Exactly 305 manifest items have terminal, evidence-backed dispositions.
- Unresolved items equal zero; exclusions and arithmetic reconcile explicitly.
- Every absorbed/adapted item names its current CVF owner and evidence.
- Every rejected/no-new-value item carries a body-read semantic reason.
- Every parked item has an owner, value statement, and checkable reopen trigger.
- Catalog/GAP reverse projection is reconciled; pending value is not presented
  as as-built architecture.
- Roadmap closure, public export disposition, and session sync occur only after
  reviewer acceptance.
- The Refinery-to-Kernel canonical packet-binding hash GAP is assigned an
  owner/disposition/next action without runtime implementation.

## Execution Plan

1. Refresh T6 and T0 anchors. 2. Reconcile ledger drift. 3. Classify 305 items.
4. Audit low-value/rejected/parked groups. 5. Reconcile Catalog/GAP. 6. Prove
terminal arithmetic and zero unresolved value. 7. Return without commit.

## Evidence Requirements

Require hashes, arithmetic, per-item owner/disposition evidence, parked reopen
conditions, reverse projection, changed paths, gates, and no-commit status.

## Review Gate

Reviewer performs semantic sampling after fast gates and runs pre-closure plus
commit-steward preflight.

## Closure Checklist

- [ ] Fresh T6 and T7 anchors exist.
- [ ] Exactly 305 terminal rows reconcile.
- [ ] Unresolved value equals zero.
- [ ] Parked items have checkable reopen conditions.
- [ ] Catalog/GAP projection is reconciled.
- [ ] Worker made no commit.

## Return-To-Orchestrator Conditions

After release only, return `COMPLETE_PENDING_REVIEW` or exact blocked evidence;
never commit.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Return `docs/reviews/CVF_SOT3_T7_WORKER_RETURN_2026-07-13.md` with Purpose,
Target / Source, Scope / Methodology, Findings / Position, Risk / Corrective
Action, Claim Boundary, checker read-ahead, source inventory, corpus and rescan
evidence, intake routing, learning disposition, epistemic block, operation
trace, delta claim boundary, public disposition, actual changed set, commands,
full git status, and no-commit statement.

## Verification Commands

```powershell
python governance/compat/generate_corpus_scan_registry.py --check
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git status --short --untracked-files=all
```

## Operator Checkpoint

Required if value demands a new owner/runtime tranche or scope change.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Future output | Verification | Status |
|---|---|---|---|---|
| complete conversion ledger | Acceptance Criteria | terminal ledger | count and hash reconciliation | HOLD |
| parked-value index reconciliation | Acceptance Criteria | parked-value review | owner/reopen audit | HOLD |
| 305 terminal items | Acceptance Criteria | ledger | arithmetic | HOLD |
| unresolved value zero | Acceptance Criteria | closeout review | semantic reviewer audit | HOLD |

## Dual Agent Surface Matrix

| Surface | Role | Interface | Authority/risk boundary | Evidence | Adapter boundary |
|---|---|---|---|---|---|
| INTERNAL_AGENT | future worker/reviewer | local evidence files | no-commit docs-only closeout | ledger and review | local process |
| EXTERNAL_AGENT_CLI_MCP | future worker | same released packet | no provider authority | locally revalidated evidence | NOT_IMPLEMENTED_WITH_REASON: separate adapter authorization required |

## ADIF Defect Registry Disclosure

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 30 --json`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007,
ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021,
ADIF-0024.

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

## Agent Operation Trace Block

Actor: future no-commit T7 worker

Provider or surface: role-neutral local execution surface

Session or invocation: captured after release

Working directory: repository root

Command or tool surface: filesystem, ledger tooling, governance gates

Target paths: future T7 Allowed Scope

Allowed scope source: refreshed T7 packet

Before status evidence: clean worktree required and worker-captured full status

After status evidence: worker-return full status

Diff evidence: name-status and ledger diff

Approval boundary: docs/evidence closeout only

Claim boundary: no closure before reviewer acceptance

Agent type: no-commit audit worker

Invocation ID: captured after release

Expected manifest: refreshed T7 output manifest

Actual changed set: worker records at return

Manifest delta: worker reconciles expected versus actual

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> no-commit audit worker -> reviewer/closer |
| phase | SOT3-T7 semantic closeout |
| contractSource | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| baseHeadFor(phase) | dispatch=`2c4c498da`; execution and closure actor-captured |
| changedSetScope(phase) | future T7 docs/evidence only |
| traceScope(phase, actor) | manifest reads, semantic mapping, arithmetic, gates |
| commitOwner(phase) | worker=WORKER_MUST_NOT_COMMIT; reviewer owns accepted commit |
| crossBatchIsolation | package/runtime/session/provider/public excluded |
| nextMoveSurfaces | reviewer/session-sync steward only after acceptance |

Before status evidence: clean worktree required at worker execution start.

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_SOT3_T7_COMPLETION_REVIEW_2026-07-13.md`

reviewerOwnedClosurePaths: future T7 audit/evidence and completion review;
session continuity in a separate commit.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| durable foundation change | N/A with reason: update existing Catalog/GAP owners only |
| source layout | existing canonical owner files control |
| aggregate discipline | use existing generators where applicable |
| index/front door | update existing discovery surfaces only after acceptance |
| claim boundary | no parallel foundation tree |

## Checker Source Read-Ahead Block

| Field | Disposition |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | HOLD_UNTIL_T6_PASS; Dependency Release Evidence; Source Verification Block; Roadmap-to-Work-Order Trace Matrix; Agent Handoff Contract Control Block |
| gateRunPurpose | confirm the pre-read machine-visible hold without fabricating dependency evidence |
| claimBoundary | dispatch authorization only; no completion claim |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-T7 --title "Semantic Value Audit And Closeout" --date 2026-07-13 --base 2c4c498da --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | no-commit docs/evidence audit worker |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Refreshed held packet using current T6 closure evidence and T7 audit requirements. |
| checkerReadAheadConfirmation | dispatch, corpus, rescan, handoff, worker-return guards |
| docOnlyNewFields | T7 audit outputs only |
| claimBoundary | dispatch only; no semantic closure proof |

## Commit Prompt Readiness

Pre-dispatch passed on the refreshed packet; worker must still capture its own
execution base and clean start status.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Corpus scan or extraction intake |
| Chain map route | T0 ledger -> T7 semantic audit -> owner reconciliation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | future T7 audit packet |
| Disposition | HOLD until T6 and fresh GC-018 |
| Claim boundary | retained input is evidence, not CVF authority |

## Future Release Requirements

The fresh post-T6 GC-018 must define delta scope, prior-ledger reuse, drift
handling, semantic sampling, direct file-backed ledger reads, terminal
arithmetic, exclusions, unsupported files, and unresolved count.

## Finding-To-Governance Learning Disposition

Required at closeout: reusable findings must update canonical owner, Catalog/GAP,
or ADIF surfaces rather than remain only in the one-off review.

## Epistemic Process Block

Evidence Comparison: T0 inventory and ledgers against accepted T1-T6 owners.

Contradiction or Gap Disposition: block closure for any ownerless or
semantically unresolved value.

Claim Update: roadmap closure is allowed only after the reviewer proves all 305
terminal dispositions and zero unresolved value.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This file is a dependency-held planning packet. It authorizes no T7 execution,
roadmap closure, runtime change, public export, release, or production claim.
