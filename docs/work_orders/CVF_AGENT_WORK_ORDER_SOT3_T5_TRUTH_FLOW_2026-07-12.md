# CVF Agent Work Order - SOT3-T5 Post-Kernel Truth Flow

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-12

Work Order ID: SOT3-T5

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `646d37ed4`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_MUST_CAPTURE_AT_CLOSURE`

## Dispatch Prompt Envelope

Role: no-commit deterministic TypeScript Flow package worker.

Canonical packet: this work order and paired T5 GC-018.

Commit mode: WORKER_MUST_NOT_COMMIT

Base: capture HEAD and full status before edits.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

Current-time notes: T0-T4 and prerequisite T4R1 (`cda8fec64`) are accepted;
only T5 is released.

Do-not-misread notes: Flow calls the actual T4R1 `TruthKernel` instance for
current state before every action; it never accepts a substitute resolver,
evaluates trust, or mints, forges, or
restates `KernelDecision`/`TruthReceipt`/`TruthReference`; Flow never produces
a second `RefineryPacket`; retained Flow code is evidence, not import
authority; T2 overrides prototype shapes; T4's accepted Kernel package is
consumed by reference only, never reimplemented.

Required first actions: startup reads, roadmap, baseline, T1/T2/T4 reviews and
contracts, truth-foundation owner, accepted Kernel package exports, retained
README and cited sources.

Return contract: package implementation and `COMPLETE_PENDING_REVIEW`, no commit.

## Purpose

Implement the bounded deterministic Truth Flow package defined by the paired
baseline: routing, dose, distribution, consumption, feedback proposal,
recall, and retirement, strictly post-Kernel.

## Target / Source

Target root is `EXTENSIONS/CVF_TRUTH_FLOW/`; source precedence is the paired
baseline Source Verification Block.

## Scope / Methodology

Rewrite contract-first. Implement the smallest coherent local package proving
`DistributionPackage` creation and every delivery/consumption action gated on
a Kernel-owned effective-state resolver result of `ACTIVE`, recipient/dose/
lifecycle transitions, bounded pre-acknowledgement recall/retirement, and a proposal-only
`FeedbackProposal` path that never mutates Kernel or source-score state
directly.

## Authority Chain

Operator continuation -> main roadmap -> accepted T1 owner decision (CAP-06,
CAP-07) -> T2 contracts -> accepted T4 Truth Kernel -> paired GC-018 -> this
work order.

## Agent Roles

Dispatcher owns source fidelity; worker implements without commit;
reviewer/closer audits all contract dependencies in one first-pass matrix.

## Worker Autonomy / No-Question Rule

Repair in-scope package/test defects. Stop for a T2 contradiction, external
dependency, forbidden path, or scope expansion.

## Required First Reads

Startup front doors; guard orientation; literal gotchas; roadmap; baseline;
T1/T2/T4 completion reviews and contracts/negative cases; truth-foundation
owner; accepted `EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts` exports; retained
Flow README, `LIFECYCLE_SPEC.md`, `publish-gate.ts`, `source-score.ts`,
`lifecycle-engine.ts`, and their tests.

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
| Intake source | accepted CVF contracts plus retained Flow evidence |
| Scope classification | EXTERNAL_LEGACY_ADAPTIVE_IMPLEMENTATION |
| Intake role | no-commit package worker |
| Risk sensitivity | HIGH: distribution authority derived from Kernel truth references |
| Provider surface | local deterministic tools only |
| Reviewer role | contract, reference-resolution, dose/lifecycle, and negative-case audit |
| Routing decision | WORKER_MUST_NOT_COMMIT |
| Escalation condition | T2 contradiction, new dependency, or forbidden path |
| Public route | DEFERRED_PRIVATE_ONLY |
| canonical route mode | MULTI_AGENT_MULTI_ROLE |
| selected role route | dispatcher -> package worker -> reviewer/closer |

## Allowed Scope

Only `EXTENSIONS/CVF_TRUTH_FLOW/**` and
`docs/reviews/CVF_SOT3_T5_WORKER_RETURN_2026-07-12.md`.

## Forbidden Scope

`EXTENSIONS/CVF_TRUTH_KERNEL/**` mutation, `EXTENSIONS/CVF_REFINERY/**`
mutation, other extensions, governance checkers/hooks, session files, Web/UI,
provider/live, public-sync, package activation, database/SOT-index service,
monitors, adapters (Guard Contract, phase-governance, Truth Kernel adapter),
and direct retained-tree copying.

## Source Verification Block

Use and reopen every row in the paired baseline. T2 and the accepted T4
Kernel package are canonical; retained Flow sources have ADAPT or REJECT
authority only.

Prerequisite disposition: SATISFIED at T4R1 material commit `cda8fec64` and
completion review `docs/reviews/CVF_SOT3_T4R1_COMPLETION_REVIEW_2026-07-13.md`.
The worker must use the actual `TruthKernel.referenceState(referenceId,
nowUtcIso)` API and must not introduce a caller-controlled substitute resolver.

## Implementation Contract

- Public contracts: `DistributionPackage`, `FeedbackProposal`, per T2 contract
  chain sections 7-8.
- Flow type-consumes an already-issued `TruthReference`, but current authority
  comes only from the actual injected `TruthKernel` instance and its
  `referenceState(referenceId, nowUtcIso)` result. It never trusts the raw
  issuance snapshot as current state, computes revocation/supersession/expiry
  itself, or imports/duplicates Kernel evaluation logic.
- `DistributionPackage.routing_decision` is derived only from a resolved
  `ACTIVE` `TruthReference`; construction rejects empty `truth_references` or
  any non-`ACTIVE` reference.
- Every routing, delivery, acknowledgement, and consumption operation
  re-resolves all bound references at its injected action time and fails
  closed unless every effective state is `ACTIVE`. A creation-time result may
  not be cached as later action authority.
- Distribution package lifecycle uses exactly `PENDING_ACKNOWLEDGEMENT`,
  `ACKNOWLEDGED`, `EXPIRED`, `WITHDRAWN`; no Flow-local `VERIFIED`-equivalent
  token.
- Recall and retirement both use only the T2-valid
  `PENDING_ACKNOWLEDGEMENT -> WITHDRAWN` transition. `ACKNOWLEDGED`, `EXPIRED`,
  and `WITHDRAWN` are terminal. T5 adds no post-acknowledgement recall state
  and never retires or alters the underlying Kernel record.
- `FeedbackProposal` is proposal-only (`SUBMITTED -> UNDER_REVIEW ->
  ACCEPTED/REJECTED`); `no_direct_mutation_flag` is always true; no direct
  mutation function (`updateSourceScore()`-class) exists in this package.
- Inject clock and ID factory; no wall clock or random global.
- README records the strictly-post-Kernel boundary and no-AI/no-provider
  boundary.

## Negative Test Matrix

| Case | Required result |
|---|---|
| empty `truth_references` at package creation | rejected (NC-09/Invariant 8 class) |
| referenced `TruthReference.reference_state` is `EXPIRED` | package creation rejected |
| referenced `TruthReference.reference_state` is `REVOKED` or `SUPERSEDED` | package creation rejected (NC-10) |
| reference was ACTIVE at creation but resolver returns `REVOKED`, `SUPERSEDED`, or `EXPIRED` at delivery/acknowledgement/consumption time | action rejected; creation-time authority is not reused |
| raw reference snapshot says `ACTIVE` while effective resolver state is non-ACTIVE | resolver result wins and action is rejected |
| caller supplies `truthKernelAccepted: true` or an unverified string ID | `routing_decision` not derived from it; rejected until a real reference resolves (NC-11) |
| `FeedbackProposal` attempts a direct mutation path | rejected; only `ACCEPTED` review status may trigger a separate governed action (NC-12) |
| Flow-side code attempts to produce a second `RefineryPacket` | forbidden-dependency/boundary test fails the package |
| Flow-side code attempts to produce `KernelDecision`/`TruthReceipt`/`TruthReference` | forbidden-dependency/boundary test fails the package |
| same injected input twice | byte-equivalent outputs |
| AI/provider/network dependency | dependency proof fails |

## Dual Agent Surface Matrix

| Surface | Role | Interface | Authority/risk boundary | Evidence | Adapter boundary |
|---|---|---|---|---|---|
| INTERNAL_AGENT | worker/reviewer | local files and commands | worker cannot commit; Flow package only | tests and return | local process |
| EXTERNAL_AGENT_CLI_MCP | future worker | same packet | no provider authority or MCP support | locally revalidated return | NOT_IMPLEMENTED_WITH_REASON: separate adapter authorization required |

## ADIF Defect Registry Disclosure

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007,
ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024.

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> no-commit package worker -> reviewer/closer |
| phase | SOT3-T5 post-Kernel Truth Flow |
| contractSource | canonical contract citation immediately above |
| baseHeadFor(phase) | dispatch=`646d37ed4`; execution=worker-captured HEAD; closure=reviewer-captured base |
| changedSetScope(phase) | target package root plus one worker return |
| traceScope(phase, actor) | reads, manifest, code, schemas, tests, scans, gates, no-commit evidence |
| commitOwner(phase) | worker=WORKER_MUST_NOT_COMMIT; reviewer owns accepted commit |
| crossBatchIsolation | T6-T7, Kernel/Refinery mutation, other extensions, session, provider, public paths excluded |
| nextMoveSurfaces | reviewer/session-sync steward only after acceptance |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_SOT3_T5_COMPLETION_REVIEW_2026-07-12.md`

reviewerOwnedClosurePaths: completion review and accepted package material;
session continuity in a separate commit.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| routing, dose, distribution, consumption | Implementation Contract | `EXTENSIONS/CVF_TRUTH_FLOW/src/` routing/dose/distribution engines | package tests | PASS |
| feedback proposal, recall, retirement | Implementation Contract | feedback/lifecycle engines | negative test matrix (NC-12 row) | PASS |
| no embedded Refinery | Forbidden Scope; Negative Test Matrix | boundary test | dependency/forbidden-symbol scan | PASS |
| no direct VERIFIED transition without Kernel proof | Implementation Contract; Negative Test Matrix | `DistributionPackage` status vocabulary; NC-09/NC-10/NC-11 rows | negative tests | PASS |
| T6-T7 held | Forbidden Scope | no vertical-slice or closeout paths | exact status/diff | PASS |

## Execution Plan

1. Capture `executionBaseHead` and `git status --short --untracked-files=all`.
   Input: clean worktree. Output: recorded base. Validation: command output.
   Stop condition: worktree not clean at start.
2. Reopen T2 contract chain sections 6-8, invariants 6-9, and NC-04A/B,
   NC-09 through NC-12; reopen accepted `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-reference.ts`
   and `src/index.ts` exports. Input: cited sources. Output: confirmed field
   sets. Validation: source re-read. Stop condition: contract mismatch found.
3. Author package metadata, `tsconfig.json`, and strict TypeScript contract
   types for `DistributionPackage` and `FeedbackProposal`. Input: T2 field
   minimums. Output: `src/types/*.ts`. Validation: `tsc --noEmit`. Stop
   condition: field omitted from T2 minimum.
4. Implement a read-only Kernel authority boundary accepting the actual
   `TruthKernel` instance and calling its public ID-only `referenceState()` at
   the supplied action time; Flow neither accepts a substitute resolver, reads
   a raw snapshot as current authority, nor reimplements precedence. Input:
   accepted Kernel exports from `cda8fec64`. Output:
   `src/kernel-reference/*.ts`. Validation: integration tests with a real
   `TruthKernel` prove missing
   resolution fails closed, effective state overrides a stale ACTIVE snapshot,
   and no local revocation/supersession/expiry logic exists. Stop condition:
   boundary accepts caller state flags/substitute resolver or reimplements Kernel precedence.
5. Implement routing, dose, distribution, acknowledgement, and consumption
   engines gated on a fresh resolver call at every action.
   Input: step 4 output. Output: `src/routing/*.ts`, `src/distribution/*.ts`.
   Validation: positive-path test plus NC-09/NC-10/NC-11 tests. Stop
   condition: `routing_decision` derivable from an unverified boolean.
6. Implement lifecycle (`PENDING_ACKNOWLEDGEMENT`/`ACKNOWLEDGED`/`EXPIRED`/
   `WITHDRAWN`), with recall and retirement both bounded to the sole T2-valid
   withdrawal transition from `PENDING_ACKNOWLEDGEMENT`. Input: step 5 output.
   Output: `src/lifecycle/*.ts`. Validation: transition tests. Stop
   condition: any Flow-local `VERIFIED`-equivalent token, post-acknowledgement
   withdrawal, or fifth lifecycle state is reachable.
7. Implement the proposal-only feedback engine. Input: T2 `FeedbackProposal`
   contract. Output: `src/feedback/*.ts`. Validation: NC-12 test. Stop
   condition: any direct-mutation code path exists.
8. Author schemas, package exports (`src/index.ts`), README, and tests
   (positive path, full negative matrix, dependency-boundary,
   no-second-Refinery, no-second-Kernel-authority, determinism). Validation:
   `npm run typecheck`, `npm run build`, `npm test`. Stop condition: any
   negative case fails to fail closed.
9. Run forbidden-dependency scan, worker-return fast gate, file-size guard,
   and record exact manifest/status/diff. Return `COMPLETE_PENDING_REVIEW`
   without commit. Stop condition: any command fails without an in-scope
   repair.

## Write Ownership

Worker owns target package and worker return only. Reviewer owns closure/commit.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
npm --prefix EXTENSIONS/CVF_TRUTH_FLOW run typecheck
npm --prefix EXTENSIONS/CVF_TRUTH_FLOW run build
npm --prefix EXTENSIONS/CVF_TRUTH_FLOW test
rg -n -i "openai|anthropic|provider|prompt|agent|fetch\(|axios|randomUUID|Date\.now|new Date\(\)" EXTENSIONS/CVF_TRUTH_FLOW/src
rg -n "KernelDecision|TruthReceipt|TruthReference" EXTENSIONS/CVF_TRUTH_FLOW/src --glob "!**/kernel-reference/**"
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --check
git status --short --untracked-files=all
git rev-parse --short HEAD
```

The second `rg` command must return zero matches outside the read-only
Kernel-reference resolver module; any match elsewhere indicates Flow is
minting or restating Kernel authority and blocks closure.

## Review Gate

Reviewer builds one dependency-closure matrix before repair and recomputes
all negative cases, reference-resolution equality, dose/lifecycle
transitions, dependency scan, exact exports, status/diff, and committed
pre-closure range.

## Evidence Requirements

Exact manifest, test counts, typecheck/build output, reference-resolution
proof, determinism/dependency scans, no-copy disposition, status/diff and
unchanged HEAD.

## Acceptance Criteria

All baseline invariants and negative cases pass; no forbidden dependency,
no second Refinery/Kernel authority, and no out-of-scope path exists; worker
did not commit.

## Operator Checkpoint

No checkpoint for in-scope rewrite. Stop for contract change, dependency,
adapter/database/monitor integration, activation, or provider/live proof.

## Closure Checklist

- [ ] `DistributionPackage`/`FeedbackProposal` contract types and schemas complete;
- [ ] distribution creation with empty or non-`ACTIVE` references fails closed;
- [ ] caller-supplied approval boolean never substitutes for a resolved reference;
- [ ] lifecycle uses only the four `DistributionPackage` states, no local `VERIFIED`;
- [ ] feedback is proposal-only with no direct mutation path;
- [ ] no second Refinery/Kernel authority producer exists in the package;
- [ ] determinism and no-AI/no-provider proof pass;
- [ ] exact manifest and no-commit evidence returned.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`,
or `BLOCKED_WITH_REASON`; never a closed-equivalent worker status.

## Worker Return Conditions

Return after all commands pass or one source-backed blocker. Do not commit.

## Return / Escalation Conditions

Escalate only contract contradiction, dependency, forbidden path, or expansion.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| durable family | `EXTENSIONS/CVF_TRUTH_FLOW/` |
| stable front door | package README |
| canonical owner | new T5 runtime owner; T4 Kernel package remains upstream authority; truth-foundation remains doctrine owner |
| generated aggregate | NOT_APPLICABLE_WITH_REASON: direct package source authority |
| index/update route | package exports and later accepted Catalog projection |
| claim boundary | private package candidate until reviewer acceptance |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: T0 already established the 305-file manifest and
T0R-T4 accepted the semantic, owner, contract, and upstream package inputs.
T5 implements only the accepted Flow capability subset; T7 owns final
per-file terminal reconciliation.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | retained Flow evidence -> accepted T1/T2/T4 contracts/owners -> CVF-native T5 rewrite |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | new Flow package candidate only |
| Disposition | ADAPT and REJECT_DIRECT_IMPORT |
| Claim boundary | selective rewrite only; retained source is not runtime authority |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-T5 --title "Post-Kernel Truth Flow" --date 2026-07-12 --base 1bf21dcee --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | no-commit TypeScript package worker |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Hand-authored from the work-order template directly, following the T4 work order's proven section shape (T4 passed pre-dispatch with the same template). Added T2 Flow contracts, Kernel-reference-only resolver boundary, negative-case, handoff and storage controls. |
| checkerReadAheadConfirmation | dispatch, structural, handoff, external-intake, worker-return and file-size checkers |
| docOnlyNewFields | deterministic Flow resolver/engine interfaces |
| claimBoundary | dispatch only; no implementation proof |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Reviewer Closure Conversion; Roadmap-to-Work-Order Trace Matrix; Public Export Disposition |
| gateRunPurpose | confirm source-derived dispatch before implementation |
| claimBoundary | gates do not prove package semantics |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | SOT3-T5 packet authoring, 2026-07-12 |
| Working directory | repository root |
| Command or tool surface | governed reads, rg, source verification, file writes, dispatch gates |
| Target paths | paired T5 baseline and this work order |
| Allowed scope source | operator request to create the next work order |
| Before status evidence | clean worktree at refreshed dispatch base `646d37ed4`; T4R1 accepted at `cda8fec64`; target package absent |
| After status evidence | T5 packet authored; implementation awaits pre-dispatch |
| Diff evidence | exact two-path packet diff before commit |
| Approval boundary | T5 packet authoring and bounded no-commit dispatch |
| Claim boundary | no package behavior proof, T6-T7, provider/live or public claim |
| Agent type | dispatcher |
| Invocation ID | `sot3-t5-dispatch-authoring-2026-07-12` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation packet; no public-sync authorization.

## Claim Boundary

This work order authorizes one bounded no-commit T5 worker after pre-dispatch.
It does not authorize T6-T7, provider/live, public, activation, or Kernel/
Refinery mutation.
