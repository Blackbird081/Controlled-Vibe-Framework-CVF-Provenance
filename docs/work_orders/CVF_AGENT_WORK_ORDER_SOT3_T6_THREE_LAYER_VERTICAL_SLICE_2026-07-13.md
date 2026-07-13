# CVF Agent Work Order - SOT3-T6 Three-Layer Vertical Slice

Memory class: FULL_RECORD

Status: PROPOSED_PRE_DISPATCH

Date: 2026-07-13

Work Order ID: SOT3-T6

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `TO_BE_CAPTURED_AT_DISPATCH`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_MUST_CAPTURE_AT_CLOSURE`

## Purpose

Implement three deterministic end-to-end scenarios through the actual accepted
Refinery, Truth Kernel, and Truth Flow public APIs.

## Target / Source

Target `EXTENSIONS/CVF_SOT_THREE_LAYER_SLICE/` plus
`docs/reviews/CVF_SOT3_T6_WORKER_RETURN_2026-07-13.md`. Source authority is the
paired T6 GC-018 and its Source Verification Block.

## Scope / Methodology

Create a thin integration orchestrator, fixtures, canonical evidence serializer,
and tests. Use real layer instances; do not reproduce their business logic.

## Authority Chain

Operator continuation -> SOT3 roadmap -> accepted T2 contracts -> accepted
T3/T4/T4R1/T5 packages -> paired T6 GC-018 -> this work order.

## Agent Roles

Dispatcher owns source fidelity; worker implements without commit; reviewer/
closer audits dependencies and evidence preservation.

## Write Ownership

Worker owns only Allowed Scope while uncommitted. Reviewer owns accepted
material; session-sync steward owns continuity files.

## Required First Reads

Startup front doors; guard orientation; literal gotchas; SOT3 roadmap; paired
baseline; T2 contract chain and negative cases; T3, T4R1, and T5 completion
reviews; all three package READMEs and public `src/index.ts` exports.

## Allowed Scope

Only `EXTENSIONS/CVF_SOT_THREE_LAYER_SLICE/**` and
`docs/reviews/CVF_SOT3_T6_WORKER_RETURN_2026-07-13.md`.

## Forbidden Scope

The three owning package roots; legacy retained roots; other extensions;
governance checkers/hooks; session state; activation; adapters; Web/UI;
provider/live/network/database; public-sync; T7 artifacts.

## Source Verification Block

The worker must reopen every ACCEPT row in
`docs/baselines/CVF_GC018_SOT3_T6_THREE_LAYER_VERTICAL_SLICE_2026-07-13.md`.
Any mismatch stops execution and returns the packet to the dispatcher with
direct source evidence.

## Dependency Release Evidence

T5 is reviewer-accepted at material commit `8a653370a`; completion evidence is
`docs/reviews/CVF_SOT3_T5_COMPLETION_REVIEW_2026-07-13.md`. T6 may dispatch only
after this packet and baseline pass pre-dispatch. T7 remains held.

## Implementation Contract

- Create scenario IDs `INTERNAL`, `PROJECT`, and `MARKET_SOURCE`.
- Each positive scenario must call the actual `RefineryEngine.run`, pass its
  released packet identity into actual `TruthKernel.evaluate`, then use the
  actual Kernel-issued reference with `DistributionEngine`.
- The integration package may map types and serialize evidence but may not
  implement normalization, conflict resolution, trust evaluation, receipt
  hashing, reference-state resolution, routing, dose, or lifecycle transitions.
- Produce one canonical evidence record per scenario containing source/scope,
  Refinery conflicts and status, Kernel decision/receipt/reference, Flow route,
  dose, and terminal acknowledgement state.
- Inject all clocks and ID factories. Identical input must produce
  byte-equivalent canonical JSON.
- Add boundary scans proving no AI, agent, prompt, provider, network, database,
  retained-root import, or copied layer implementation.

## Negative Test Matrix

| Case | Required result |
|---|---|
| Refinery result is not released | Kernel call is not made; fail closed |
| Kernel does not issue an active reference | Flow package is not created |
| reference becomes expired, revoked, or superseded before action | action rejected by real Flow/Kernel authority path |
| integration tries to mint receipt/reference or set Flow lifecycle directly | boundary test fails |
| evidence serializer omits source, scope, conflict, receipt, route, or lifecycle | schema/test fails |
| same injected input repeated | byte-equivalent evidence |

## Execution Plan

1. Capture HEAD and full status; stop if the start tree is not clean.
2. Reopen source verification rows and record exact public APIs in the return.
3. Scaffold a strict local TypeScript package using local file dependencies.
4. Implement the thin orchestrator and canonical evidence schema.
5. Add three positive scenarios and the full negative matrix.
6. Run package tests, typecheck, forbidden-import scan, and governance gates.
7. Return `COMPLETE_PENDING_REVIEW` with actual status; do not commit.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/generate_active_session_state.py --check
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

## Acceptance Evidence

Worker return must include commands and exact results for tests, typecheck,
forbidden dependency scan, deterministic evidence comparison, changed paths,
and `git status --short --untracked-files=all`.

## Evidence Requirements

Provide command-backed tests, typecheck, scans, deterministic comparison,
changed paths, and no-commit status.

## Acceptance Criteria

All baseline criteria and negative-test rows pass using real public layer
instances, with no forbidden path changes.

## Review Gate

Reviewer runs one dependency matrix, reviewer-fast, pre-closure, and
commit-steward preflight before acceptance.

## Closure Checklist

- [ ] Three positive scenarios pass.
- [ ] Every negative case passes.
- [ ] Typecheck and dependency scans pass.
- [ ] Changed set is within Allowed Scope.
- [ ] Worker made no commit.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW`, or an exact blocked disposition; never commit.

## Operator Checkpoint

Stop only for scope expansion, provider/live work, owner-package mutation, or
T2 contradiction.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output | Verification | Status |
|---|---|---|---|---|
| three scenario classes | Implementation Contract | fixtures/tests | test names and results | REQUIRED |
| traverse all contracts | Implementation Contract | orchestrator | real-instance integration tests | REQUIRED |
| preserve source through lifecycle | evidence schema | canonical records | schema and snapshots | REQUIRED |
| fail closed at layer boundaries | Negative Test Matrix | negative tests | exact failures | REQUIRED |
| T7 held | Forbidden Scope | no T7 path | diff/status | REQUIRED |

## Dual Agent Surface Matrix

| Surface | Role | Interface | Authority/risk boundary | Evidence | Adapter boundary |
|---|---|---|---|---|---|
| INTERNAL_AGENT | worker/reviewer | local files and commands | worker cannot commit | tests and return | local process |
| EXTERNAL_AGENT_CLI_MCP | future worker | same packet | no provider authority | locally revalidated return | NOT_IMPLEMENTED_WITH_REASON: separate authorization required |

## ADIF Defect Registry Disclosure

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 30 --json`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007,
ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021,
ADIF-0024.

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

## Agent Operation Trace Block

Actor: future no-commit T6 worker

Provider or surface: role-neutral local execution surface

Session or invocation: worker records at start

Working directory: repository root

Command or tool surface: filesystem, package manager, compiler, tests, gates

Target paths: Allowed Scope only

Allowed scope source: this work order

Before status evidence: worker-captured full status

After status evidence: worker-return full status

Diff evidence: worker-return name-status and diff summary

Approval boundary: no owner-package, provider, public, or T7 work

Claim boundary: worker return is pending reviewer acceptance

Agent type: no-commit implementation worker

Invocation ID: worker-assigned

Expected manifest: integration package plus one worker return

Actual changed set: worker records at return

Manifest delta: worker reconciles expected versus actual

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> no-commit integration worker -> reviewer/closer |
| phase | SOT3-T6 three-layer vertical slice |
| contractSource | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| baseHeadFor(phase) | dispatch=captured after packet commit; execution=worker-captured HEAD; closure=reviewer-captured base |
| changedSetScope(phase) | integration package plus one worker return |
| traceScope(phase, actor) | reads, code, fixtures, tests, scans, gates, no-commit evidence |
| commitOwner(phase) | worker=WORKER_MUST_NOT_COMMIT; reviewer owns accepted commit |
| crossBatchIsolation | owning packages, T7, session, provider, public excluded |
| nextMoveSurfaces | reviewer/session-sync steward only after acceptance |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_SOT3_T6_COMPLETION_REVIEW_2026-07-13.md`

reviewerOwnedClosurePaths: completion review and accepted T6 package material;
session continuity must be a separate commit.

## Checker Source Read-Ahead Block

| Field | Disposition |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Source Verification Block; Dependency Release Evidence; Roadmap-to-Work-Order Trace Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Commit Prompt Readiness |
| gateRunPurpose | confirm pre-read source-fidelity and dispatch-shape evidence before worker execution |
| claimBoundary | gate success does not prove the future implementation |

## Commit Prompt Readiness

Reviewer only: commit accepted material after reviewer-fast and commit-steward
preflight pass. Worker must not commit.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Legacy source family |
| Chain map route | accepted owner packages -> deterministic integration proof |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired T6 packet |
| Disposition | NOT_APPLICABLE_WITH_REASON: no new external intake |
| Claim boundary | T6 does not re-absorb retained sources |

## Finding-To-Governance Learning Disposition

NOT_APPLICABLE_WITH_REASON: dispatch makes no new repeated-defect claim.

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: implementation claims require worker evidence.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

No implementation, integration behavior, runtime activation, provider/live,
public, release, or production claim exists until reviewer acceptance.
