# CVF Agent Work Order - SOT3-T3 Deterministic Refinery Core

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-12

Work Order ID: SOT3-T3

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `5510412e8`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_MUST_CAPTURE_AT_CLOSURE`

## Dispatch Prompt Envelope

Role: no-commit deterministic TypeScript package worker.

Canonical packet: this work order and paired T3 GC-018.

Commit mode: WORKER_MUST_NOT_COMMIT

Base: capture HEAD and full status before edits.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

Current-time notes: T0-T2 are accepted; only T3 is released.

Do-not-misread notes: retained code is evidence, not import authority; T2
contracts override conflicting prototype fields and lifecycle behavior.

Required first actions: read startup surfaces, roadmap, baseline, T1/T2
reviews, T2 contracts/negative cases, retained README/TREEVIEW and cited source;
capture HEAD/status and run pre-implementation.

Return contract: one no-commit package implementation and
`COMPLETE_PENDING_REVIEW` worker return.

## Purpose

Implement the bounded deterministic no-AI Refinery Core defined by the paired baseline.

## Target / Source

Target root: `EXTENSIONS/CVF_REFINERY/`. Sources and precedence are defined in
the paired baseline Source Verification Block.

## Scope / Methodology

Rewrite contract-first. Implement the smallest coherent package that proves
the full required stage chain and fail-closed invariants; do not copy the retained tree wholesale.

## Authority Chain

Operator continuation -> main SOT3 roadmap -> accepted T1 owner decision ->
accepted T2 contracts -> paired GC-018 -> this work order.

## Agent Roles

Dispatcher owns source fidelity; worker implements without commit;
reviewer/closer independently audits semantics, tests, dependency graph, and commit.

## Worker Autonomy / No-Question Rule

Repair in-scope package/test defects. Stop for a T2 contract contradiction,
new external dependency, forbidden path, or scope expansion.

## Required First Reads

Startup front doors; guard orientation; literal gotchas; main roadmap; paired
baseline; T1/T2 completion reviews; T2 contract chain and negative cases;
retained Refinery README, TREEVIEW, engine, types, normalization, duplicate,
conflict, integrity, lineage and tests.

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
| Intake source | retained Refinery folder plus accepted CVF contracts |
| Scope classification | EXTERNAL_LEGACY_ADAPTIVE_IMPLEMENTATION |
| Intake role | no-commit package worker |
| Risk sensitivity | HIGH: new foundation package and fail-closed boundary |
| Provider surface | local deterministic tools only |
| Reviewer role | semantic, dependency, determinism, and negative-case audit |
| Routing decision | WORKER_MUST_NOT_COMMIT |
| Escalation condition | contract conflict, new dependency, or forbidden path |
| Public route | DEFERRED_PRIVATE_ONLY |
| canonical route mode | MULTI_AGENT_MULTI_ROLE |
| selected role route | dispatcher -> package worker -> reviewer/closer |

## Allowed Scope

Only `EXTENSIONS/CVF_REFINERY/**` and
`docs/reviews/CVF_SOT3_T3_WORKER_RETURN_2026-07-12.md`.

## Forbidden Scope

Truth Kernel/Flow, other extensions, governance checkers/hooks, session files,
Web/UI, provider/live, public-sync, package registry/activation, and direct retained-tree copying.

## Source Verification Block

Use the paired baseline table. Re-open every cited source. T2 contract and
negative-case files are canonical; retained sources have `ADAPT` or
`REJECT_DIRECT_IMPORT` authority only.

## Implementation Contract

- Public exports: SourceEnvelope, RefineryPacket, RefineryEngine and deterministic dependency types.
- Required stages: intake, normalize, schema, duplicate, conflict, quality, integrity, lineage, packet.
- Engine accepts injected clock and ID factory; no global time/random source.
- Default run executes the required pipeline; callers cannot obtain
  `READY_FOR_KERNEL` by omitting stages.
- Every output is deeply detached from input references.
- Status/failure behavior exactly follows T2.
- `README.md` records no-AI and no-truth boundaries.

## Negative Test Matrix

| Case | Required result |
|---|---|
| zero configured/executed stages | BLOCKED plus REFINERY_NO_STAGES_EXECUTED |
| missing source identity | BLOCKED |
| schema failure | BLOCKED plus SCHEMA_VALIDATION_FAILED |
| unresolved quality/integrity finding | REVIEW_REQUIRED or BLOCKED, never READY_FOR_KERNEL |
| incomplete lineage/integrity | not READY_FOR_KERNEL |
| different scope with same value | not silently exact duplicate/conflict |
| same scope with conflicting value | conflict retained, no authoritative selection |
| same injected inputs twice | byte-equivalent output |
| forbidden truth status/token | rejected |
| AI/provider/network dependency | dependency proof fails |

## Dual Agent Surface Matrix

| Surface | Role | Interface | Authority/risk boundary | Evidence | Adapter boundary |
|---|---|---|---|---|---|
| INTERNAL_AGENT | worker/reviewer | local files and package commands | no worker commit; package root only | worker return/tests | direct local process |
| EXTERNAL_AGENT_CLI_MCP | future external worker | same packet and CLI commands | no provider authority or MCP support claim | locally revalidated return | NOT_IMPLEMENTED_WITH_REASON: separate adapter authorization required |

## ADIF Defect Registry Disclosure

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0014, ADIF-0015,
ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024.

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> no-commit package worker -> reviewer/closer |
| phase | SOT3-T3 Refinery Core |
| contractSource | canonical archive-qualified contract citation immediately above |
| baseHeadFor(phase) | dispatch=`5510412e8`; execution=worker-captured HEAD; closure=reviewer-captured base |
| changedSetScope(phase) | target package root plus one worker return |
| traceScope(phase, actor) | source reads, manifest, code, tests, scans, gates, no-commit evidence |
| commitOwner(phase) | worker=WORKER_MUST_NOT_COMMIT; reviewer owns accepted commit |
| crossBatchIsolation | T4-T7, other extensions, session, provider and public paths excluded |
| nextMoveSurfaces | reviewer/session-sync steward only after acceptance |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_SOT3_T3_COMPLETION_REVIEW_2026-07-12.md`

reviewerOwnedClosurePaths: completion review and accepted package material;
session continuity in a separate commit.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Instruction | Evidence |
|---|---|---|
| independent Refinery Core | create new package root | exact manifest |
| deterministic no-AI | injected dependencies and forbidden scan | tests/scans |
| default cannot bypass stages | required default pipeline | NC-01 tests |
| T4 held | no Kernel/Flow paths | status/diff |

## Execution Plan

Capture base; derive types from T2; implement package; run negative matrix;
run typecheck/build/test/determinism/dependency scans; return without commit.

## Write Ownership

Worker owns target package and worker return only. Reviewer owns closure and commits.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
npm --prefix EXTENSIONS/CVF_REFINERY run typecheck
npm --prefix EXTENSIONS/CVF_REFINERY run build
npm --prefix EXTENSIONS/CVF_REFINERY test
rg -n -i "openai|anthropic|provider|prompt|agent|fetch\(|axios|randomUUID|Date\.now" EXTENSIONS/CVF_REFINERY
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --check
git status --short --untracked-files=all
git rev-parse --short HEAD
```

## Review Gate

Reviewer recomputes the negative matrix, repeated-run determinism, dependency
tree, forbidden scan, exact exports, T2 field/status compatibility, and full committed pre-closure range.

## Evidence Requirements

Exact file manifest, test counts, typecheck/build output, determinism proof,
dependency/forbidden scan, no-copy disposition, status/diff and unchanged HEAD.

## Acceptance Criteria

All baseline invariants and negative tests pass; no forbidden dependency or
out-of-scope path exists; worker did not commit.

## Operator Checkpoint

No checkpoint for in-scope rewrite. Stop for new dependency, T2 contract
change, cross-package integration, Kernel/Flow work, or package activation.

## Closure Checklist

- [ ] package and exports complete;
- [ ] default required pipeline cannot be empty;
- [ ] T2 statuses/failure tokens preserved;
- [ ] determinism and immutability proven;
- [ ] no-AI/no-provider dependency proof passes;
- [ ] negative matrix passes;
- [ ] exact manifest and no-commit evidence returned.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`,
or `BLOCKED_WITH_REASON`; never a closed-equivalent worker status.

## Worker Return Conditions

Return after all commands pass or one explicit source-backed blocker. Do not commit.

## Return / Escalation Conditions

Escalate only a contract contradiction, new dependency, forbidden path, or scope expansion.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| durable family | `EXTENSIONS/CVF_REFINERY/` |
| stable front door | package `README.md` |
| canonical owner | new independent T3 package |
| generated aggregate | NOT_APPLICABLE_WITH_REASON: package source is direct authority |
| index/update route | package index exports and later accepted Catalog projection |
| claim boundary | private package candidate until reviewer acceptance |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: SOT3-T0 already established the complete 305-file
manifest and processing evidence; T0R, T1, and T2 accepted the semantic,
ownership, and contract inputs used by T3. This work order implements only the
accepted Refinery capability subset. SOT3-T7 retains final per-file terminal
reconciliation and whole-corpus closure.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | retained Refinery evidence -> accepted T2 contracts -> CVF-owned rewrite |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | new `EXTENSIONS/CVF_REFINERY/` package candidate |
| Disposition | ADAPT |
| Claim boundary | selective rewrite only; retained source is not runtime authority |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-T3 --title "Deterministic Refinery Core" --date 2026-07-12 --base 5510412e8 --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | no-commit TypeScript package worker |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Added T2 contract, retained-source, deterministic/no-AI, negative-test, handoff and storage controls. |
| checkerReadAheadConfirmation | dispatch-quality, structural, handoff, external-intake, worker-return and file-size checkers |
| docOnlyNewFields | deterministic dependency injection boundary |
| claimBoundary | dispatch only; no implementation proof |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Reviewer Closure Conversion; Roadmap-to-Work-Order Trace Matrix; Public Export Disposition |
| gateRunPurpose | confirm source-derived dispatch before implementation |
| claimBoundary | gates do not prove package semantics |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | SOT3-T3 packet authoring, 2026-07-12 |
| Working directory | repository root |
| Command or tool surface | governed reads, rg, source verification, apply_patch, dispatch gates |
| Target paths | paired T3 baseline and this work order |
| Allowed scope source | operator instruction to continue main SOT3 absorption |
| Before status evidence | HEAD `5510412e8`; clean worktree; target package absent |
| After status evidence | T3 packet authored; implementation awaits pre-dispatch |
| Diff evidence | exact two-path packet diff before commit |
| Approval boundary | T3 packet authoring and bounded no-commit package dispatch |
| Claim boundary | no package behavior proof, T4-T7, provider/live or public claim |
| Agent type | dispatcher |
| Invocation ID | `sot3-t3-dispatch-authoring-2026-07-12` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation packet; no public-sync authorization.

## Claim Boundary

This work order authorizes one bounded no-commit T3 worker after pre-dispatch.
It does not authorize T4-T7 or any live/public integration.
