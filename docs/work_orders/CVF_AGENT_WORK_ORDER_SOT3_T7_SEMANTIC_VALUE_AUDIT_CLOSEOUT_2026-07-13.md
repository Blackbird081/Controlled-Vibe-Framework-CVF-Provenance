# CVF Agent Work Order - SOT3-T7 Semantic Value Audit And Closeout

Memory class: FULL_RECORD

Status: HOLD_UNTIL_T6_PASS

Date: 2026-07-13

Work Order ID: SOT3-T7

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `BLOCKED_BY_T6_CLOSURE`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_MUST_CAPTURE_AT_CLOSURE`

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
| T6 vertical slice | reviewer completion review and material commit | HOLD_MISSING_T6_EVIDENCE |
| fresh T7 GC-018 | baseline authored after T6 acceptance | HOLD_MISSING_T7_BASELINE |
| refreshed base anchors | clean post-T6 dispatch base | HOLD_MISSING_BASE_ANCHORS |

This work order must remain `HOLD_UNTIL_T6_PASS`. After T6 acceptance, the
dispatcher must source-verify current T0-T6 artifacts, author a fresh T7
GC-018, replace all blocked dependency rows, capture dispatch anchors, and pass
pre-dispatch before assigning a worker.

## Allowed Scope

Documentation and evidence paths explicitly named by the future T7 GC-018.

## Forbidden Scope

Any package/runtime mutation; retained-root mutation; checker/hook mutation;
session state by worker; provider/live; public-sync; activation; adapters.

## Source Verification Block

Dispatch is blocked. Current roadmap facts are verified from
`docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md`, Tranche
Plan SOT3-T7. T6 closure facts do not yet exist in this packet and therefore
remain dependency-held; no worker may infer them from chat or memory.

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

Before status evidence: worker-captured full status

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
| phase | SOT3-T7 held semantic closeout |
| contractSource | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| baseHeadFor(phase) | dispatch blocked pending T6; execution and closure uncaptured |
| changedSetScope(phase) | future T7 docs/evidence only |
| traceScope(phase, actor) | manifest reads, semantic mapping, arithmetic, gates |
| commitOwner(phase) | worker=WORKER_MUST_NOT_COMMIT; reviewer owns accepted commit |
| crossBatchIsolation | package/runtime/session/provider/public excluded |
| nextMoveSurfaces | reviewer/session-sync steward only after acceptance |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_SOT3_T7_COMPLETION_REVIEW_2026-07-13.md`

reviewerOwnedClosurePaths: future T7 audit/evidence and completion review;
session continuity in a separate commit.

## Checker Source Read-Ahead Block

| Field | Disposition |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | HOLD_UNTIL_T6_PASS; Dependency Release Evidence; Source Verification Block; Roadmap-to-Work-Order Trace Matrix; Agent Handoff Contract Control Block |
| gateRunPurpose | confirm the pre-read machine-visible hold without fabricating dependency evidence |
| claimBoundary | this held packet is not dispatch authorization |

## Commit Prompt Readiness

NOT_READY_WITH_REASON: T6 closure and fresh T7 baseline are missing.

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
