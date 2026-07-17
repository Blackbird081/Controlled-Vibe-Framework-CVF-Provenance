# CVF Agent Work Order - MAO-OA-T4 Operational Review Convergence And Commit Session Interlock

Memory class: FULL_RECORD

Date: 2026-07-17

Status: DISPATCH_READY

Work Order ID: MAO-OA-T4

Risk class: R2

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `baaabd064`

Paired baseline:
`docs/baselines/CVF_GC018_MAO_OA_T4_OPERATIONAL_REVIEW_CONVERGENCE_AND_COMMIT_SESSION_INTERLOCK_2026-07-17.md`

## Dispatch Prompt Envelope

Role: delegated implementation worker for MAO-OA-T4.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T4_OPERATIONAL_REVIEW_CONVERGENCE_AND_COMMIT_SESSION_INTERLOCK_2026-07-17.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture `git rev-parse --short HEAD` before any write.

Current-time notes: MAO-OA-T3 is independently accepted at material commit
`eead77edf`; operator standing authority releases this exact T4 packet after
the committed dispatch and continuity sync exist.

Do-not-misread notes: build a deterministic local composition around existing
reviewer/dissent/closer contracts. Do not run a provider, agent subprocess,
git, commit steward, or session generator. A typed authorization/projection is
not proof that the action occurred.

Required first actions: read startup surfaces, paired baseline, this packet,
all Source Verification files, and checker sources; confirm clean status and
capture `executionBaseHead`.

Return contract: create exactly six allowed paths, leave them uncommitted and
unstaged, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement one bounded `MaoOperationalReviewConvergence` owner that composes
existing independent-evidence, dissent/revision, closer-integration,
commit-authorization, and session-sync-projection contracts. Prove source
isolation, self-approval rejection, bounded repair, exactly-one-closer,
non-terminal convergence blocking, and material/session separation without
performing any external action.

## Authority Chain

1. operator standing instruction to continue the roadmap tranche sequence;
2. MAO-OA roadmap T4 row;
3. accepted T3 completion review and material commit `eead77edf`;
4. paired T4 GC-018 baseline;
5. current MAO reviewer/dissent/closer source contracts;
6. this exact no-commit work order.

## Agent Roles

- operator: owns standing sequence authority and future real-provider/live/public checkpoints;
- dispatcher: owns this source-verified packet and dispatch commit;
- worker: implements only the six allowed paths and must not commit;
- independent reviewer/closer: recomputes evidence, repairs only authorized paths, authors completion review, and owns material commit;
- session-sync steward: updates protected continuity only after accepted material closure.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. active handoff named by the state registry
4. `docs/reference/guard_orientation/README.md`
5. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
6. paired T4 baseline and this work order
7. every source file cited in the Source Verification Block

## Pre-Flight Checks

Before writing, record clean `git status --short`, capture
`executionBaseHead`, confirm all six planned paths are owned as specified, and
confirm the four new paths do not already exist.

## Write Ownership

Worker owns only the exact six Allowed Scope paths. Roadmap, baseline, work
order, completion review, protected session state, active handoff, existing MAO
owners, and every unrelated path are forbidden.

## Evidence Requirements

Evidence must include exact source imports, isolated-source exclusion,
self-approval and taint negatives, deterministic receipt replay, revision
ceiling, exactly-one-closer and wrong-closer negatives, integration decisions,
commit authorization, material/session disjointness, GC-051 generation and
coverage, focused/package tests, typecheck, and a complete worker return.

## Operator Checkpoint

The operator's standing sequence instruction releases T4 authoring, dispatch,
and bounded worker implementation after T3 closure. It does not release T5-T7,
actual git/session mutation by runtime code, real provider/live proof,
public-sync, or push.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | internal CVF current-source implementation request |
| scope classification | bounded exact six-path internal implementation |
| risk sensitivity | R2; no provider, live, public, git, or session mutation |
| Intake role | orchestrator authors and dispatches; one no-commit worker implements |
| Reviewer role | independent reviewer/closer recomputes evidence and owns closure conversion |
| canonical route mode | SINGLE_AGENT_SINGLE_ROLE |
| selected role route | worker return to independent reviewer/closer |
| escalation condition | return BLOCKED_WITH_REASON only for a listed Return-To-Orchestrator Condition |
| outside-source authority | NOT_APPLICABLE_WITH_REASON: no external source is consumed |
| claim boundary | no provider, agent subprocess, git/session mutation, live, or public action |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | N/A with reason: this is repository implementation dispatch, not external knowledge absorption |
| Matching local-view guard | N/A with reason: no external knowledge intake is admitted |
| Owner surface | canonical repository source and governed T4 packet |
| Disposition | N/A with reason: no outside-source fact is admitted by this work order |
| Claim boundary | internal implementation packet only |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-OA-T3 accepted closure | material commit `eead77edf`; `docs/reviews/CVF_MAO_OA_T3_COMPLETION_REVIEW_2026-07-17.md`; final disposition `REVIEWER_ACCEPTED_BOUNDED_WITH_REPAIR` | T3 local launcher must be accepted before review convergence | ACCEPT |
| operator continuation authority | explicit 2026-07-17 instruction to continue next work-order authoring until roadmap completion | authorizes the next source-verified packet, subject to fresh authority for live/public actions | ACCEPT |
| one-closer/session split authority | AHB ratification CF-07/C3 plus commit steward standard material/session split | runtime owner must emit typed plans only and preserve phase ownership | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-OA-T4 --title "MAO Operational Review Convergence And Commit Session Interlock" --date 2026-07-17 --base baaabd064 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MAO-OA-T3 accepted closure eead77edf" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced blanks with direct source verification, exact behavior, six-path manifest, negative tests, worker-return shape, and reviewer closure conversion |
| checkerReadAheadConfirmation | dispatch-quality, structural, ADIF, handoff, trace, delta-claim, worker-return, registry, file-size, and public-export checkers reviewed |
| docOnlyNewFields | T4 proposed symbols are isolated in New Doc-Only Fields |
| claimBoundary | scaffold provenance only; no runtime behavior claim |

## Worker Autonomy / No-Question Rule

Allowed-scope source, test, registry, worker-return, formatting, and checker
repairs are worker-owned. Return `BLOCKED_WITH_REASON` only when a listed
Return-To-Orchestrator Condition occurs; do not ask preference questions for
ordinary in-scope corrections.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-implementation`, surfaceSelector=`MAO`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-implementation --surface-selector MAO --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no prior MAO worker defect applies; standard no-commit and exact-scope controls remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_changed_corpus_registry_coverage.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/generate_corpus_scan_registry.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Dispatch Prompt Envelope; Role:; Canonical packet:; Commit mode:; executionBaseHead; Dependency Release Evidence; ADIF Defect Registry Disclosure; Source Verification Block; New Doc-Only Fields; Roadmap-To-Work-Order Trace Matrix; Required Artifact Manifest; Worker Return Packet Shape Contract; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Epistemic Process Block; Execution Plan; Verification Commands; Acceptance Criteria; Closure Diff Gate; Machine Closure Package; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm source-backed T4 packet shape before dispatch, not discover requirements after worker execution |
| claimBoundary | checker conformance does not prove implementation, actual agent independence, git/session action, or user value |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| isolated source packet excludes worker outputs | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/reviewer.isolation.contract.ts` | lines 80-113 | `buildIsolatedSourcePacket` | reviewer isolation contract | ACCEPT |
| recomputed evidence enforces identity and evidence independence | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/reviewer.isolation.contract.ts` | lines 133-207 | `buildRecomputedEvidence` | reviewer isolation contract | ACCEPT |
| deterministic defects and dissent exist | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/dissent.revision.contract.ts` | lines 166-218 | `buildDefectEntry`; `buildDissentRecord` | dissent/revision contract | ACCEPT |
| revision ledger and ceiling exist | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/dissent.revision.contract.ts` | lines 226-336 | `checkRevisionCeiling`; `recordReviewInLedger`; `terminalReviewDecision` | dissent/revision contract | ACCEPT |
| exactly-one closer identity check exists | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/closer.interlock.contract.ts` | lines 74-103 | `validateExactlyOneCloser`; `checkCloserIdentity` | closer interlock contract | ACCEPT |
| commit authorization is closer-only | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/closer.interlock.contract.ts` | lines 146-178 | `checkCommitAuthorization` | closer interlock contract | ACCEPT |
| session-sync projection is non-mutating | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/closer.interlock.contract.ts` | lines 184-214 | `buildSessionSyncProjection` | closer interlock contract | ACCEPT |
| non-terminal reviews block integration | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/closer.interlock.contract.ts` | lines 221-281 | `makeIntegrationDecision` | closer interlock contract | ACCEPT |
| material/session ownership is phase-separated | DOC_CONTRACT | archive-qualified canonical contract `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | CF-05; CF-07; C3 | `commitOwner(CLOSURE)` | Agent Handoff Contract | ACCEPT |
| session-sync uses a separate steward lane | DOC_CONTRACT | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | commit split and session-sync sections | `session-sync` | commit steward protocol | ACCEPT |

## New Doc-Only Fields

| Proposed symbol | Required shape | Disposition |
|---|---|---|
| `MaoOperationalReviewConvergence` | local class composing existing pure contract functions | DOC_ONLY_NEW |
| `MaoOperationalReviewRequest` | identities, source/evidence manifests, decision, defects, ledger, and time | DOC_ONLY_NEW |
| `MaoOperationalReviewResult` | typed receipt, terminal decision, ledger, dissent, or failure | DOC_ONLY_NEW |
| `MaoOperationalClosureRequest` | terminal reviews, designated closer list, changed sets, and optional material commit ref | DOC_ONLY_NEW |
| `MaoOperationalClosureResult` | integration receipt, commit authorization, and optional session projection | DOC_ONLY_NEW |
| T4-specific failure union | fail-closed reason vocabulary without changing existing enums | DOC_ONLY_NEW |

## Current Runtime Freshness Verification

Verified at clean dispatch base `baaabd064` on 2026-07-17.

| Check | Evidence | Disposition |
|---|---|---|
| four planned new paths | `Test-Path` returned `False` for source, focused test, GC-051 entry, and worker return | ACCEPT |
| existing owner symbols | direct `rg` found each cited function at current source lines | ACCEPT |
| T3 accepted closure | `git show --stat eead77edf` shows exact ten-path material closure | ACCEPT |
| current dispatch base | `git rev-parse --short HEAD`=`baaabd064`; worktree clean | ACCEPT |

## Negative Search And Collision Discipline

| Search | Result | Required disposition |
|---|---|---|
| `MaoOperationalReviewConvergence` | no current hit | safe new symbol |
| proposed four new paths | absent | safe new paths |
| second reviewer/dissent/closer/commit owner | prohibited | REJECT_DUPLICATE |
| git, child process, network, provider, session generator imports | prohibited in T4 source | focused negative source test |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_MAO_OA_T3_COMPLETION_REVIEW_2026-07-17.md`

priorVerificationAnchor: material commit `eead77edf`

recomputeReason: T3 proves dependency release only; T4 behavior and evidence must be recomputed from current source and tests.

freshRecomputeRequired: YES; the worker must reread all cited T4 source contracts and produce current command evidence.

unicodePathHandling: use literal paths and UTF-8-safe readers; author ASCII and perform no Unicode normalization.

extractedTextAuthority: N/A with reason: no extracted external text is used.

claimBoundary: prior receipts do not substitute for current implementation or test evidence.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap T4 requirement | Work-order instruction | Required evidence | Disposition |
|---|---|---|---|
| independent evidence collection | isolated packet and recomputation behavior | source inspection and negatives | RELEASED |
| review repair | revision ledger, repair owner, ceiling | focused tests | RELEASED |
| dissent | deterministic typed defect/dissent records | replay tests | RELEASED |
| closer convergence | terminal review collection and one closer | accept/reject/partial plus negative tests | RELEASED |
| commit/session interlock | closer-only authorization and disjoint post-commit projection | focused tests; no action claim | RELEASED |

## Design Control Carry-Forward

| Field | Disposition |
|---|---|
| reviewer owner | reuse existing contract |
| dissent/revision owner | reuse existing contract |
| closer owner | reuse existing contract |
| commit steward | no invocation; authorization signal only |
| session sync | no mutation; separate projection only after non-empty material commit ref |
| external agent execution | forbidden |
| T5 operator projection | parked |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| state owner | caller-supplied in-memory revision ledger plus immutable receipts |
| durable truth | existing T2 store remains launch-event truth; T4 adds no database or durable store |
| generated aggregate | GC-051 aggregate remains generator-owned |
| new dependency | forbidden |
| database/migration/retention/lock | forbidden |

## Allowed Scope

Worker may change exactly:

1. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.review.convergence.ts`
2. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts`
3. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.operational.review.convergence.test.ts`
4. `docs/corpus-intelligence/registry/entries/mao-oa-t4-operational-review-convergence-surfaces.json`
5. `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` through the existing generator
6. `docs/reviews/CVF_MAO_OA_T4_WORKER_RETURN_2026-07-17.md`

## Forbidden Scope

- every existing MAO source/test other than the local barrel;
- package roots, control-plane source/tests, provider router, manifests,
  dependencies, lockfiles, schemas, or canonical reference contracts;
- git, staging, commit, commit-steward invocation, session-state mutation,
  generator invocation for active session state, queue/process/thread/shell,
  provider SDK, credentials, network, CLI/MCP, Web/UI/workspace projection;
- reviewer/closer runtime agents, roadmap, baseline, work order, completion
  review, session, handoff, Catalog, GAP, ADIF, checker, hook, CI, public-sync,
  or push mutation; and
- T5-T7 implementation or evidence claims.

## Work-Order Fulfillment Manifest

| Requirement | Fulfillment owner | Required output | Dispatch state |
|---|---|---|---|
| source implementation | worker | review-convergence source plus local-barrel export | RELEASED |
| behavioral proof | worker | focused deterministic tests and package checks | RELEASED |
| corpus accountability | worker | per-entry GC-051 source plus generated aggregate | RELEASED |
| no-commit evidence | worker | full worker return at exact path | RELEASED |
| independent acceptance | reviewer/closer | completion review and material commit | PENDING_REVIEW |
| continuity | session-sync steward | separate protected sync after material decision | PENDING_REVIEW |

## Required Artifact Manifest

| Path | Required action | Owner |
|---|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.review.convergence.ts` | create bounded composition owner | worker |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | add local export only | worker |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.operational.review.convergence.test.ts` | create focused deterministic tests | worker |
| `docs/corpus-intelligence/registry/entries/mao-oa-t4-operational-review-convergence-surfaces.json` | cover all cited T4 source/test surfaces | worker |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | regenerate, never hand-edit | worker |
| `docs/reviews/CVF_MAO_OA_T4_WORKER_RETURN_2026-07-17.md` | create checker-complete no-commit return | worker |

Expected worker changed-set cardinality: exactly 6 paths.

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | capture clean `executionBaseHead` and read exact owners/checkers | worker return |
| 2 | implement typed review collection and bounded repair composition | source inspection |
| 3 | implement terminal closer convergence and commit/session interlock plan | source inspection |
| 4 | export from MAO local barrel only | barrel diff and import test |
| 5 | add focused accept/reject/repair/escalate/closer/session negatives | Vitest output |
| 6 | add GC-051 source, regenerate aggregate, create worker return, and confirm six unstaged paths | gate/status evidence |

## Required Review-Convergence Behavior

### Independent review collection

- build the isolated packet from caller source manifest and worker outputs;
- exclude worker outputs from reviewer source authority;
- call `buildRecomputedEvidence` with distinct non-empty identities;
- fail closed for self-approval, tainted evidence, empty evidence, or invalid
  review inputs;
- build defects and dissent through existing deterministic builders; and
- bind each review receipt to the isolated packet hash.

### Repair and revision

- accept a caller-owned existing `MaoRevisionLedger` or create one explicitly;
- record sequential revision numbers only;
- require a non-empty repair owner for `REQUEST_REPAIR`;
- allow the bounded first repair when below ceiling;
- convert a further repair at the ceiling into `ESCALATE`; and
- allow terminal ACCEPT or REJECT without inventing another repair cycle.

### Closer convergence

- require a designated-closer list of exactly one non-empty identity;
- require the acting closer to equal that identity;
- reject empty review collections and any `REQUEST_REPAIR`/`ESCALATE` receipt;
- preserve existing ACCEPT, REJECT, and PARTIAL_ACCEPT integration rules;
- check commit authorization through `checkCommitAuthorization`; and
- never execute a commit or claim that commit steward ran.

### Commit/session interlock

- integration success must state session sync is required;
- before a material commit reference exists, return a pending projection state
  rather than fabricating a SHA;
- after a non-empty caller-supplied material commit reference exists, build the
  existing `MaoSessionSyncProjection`;
- require material changed-set paths and session surface paths to be disjoint;
- do not import or call active-session generators; and
- treat projection as a plan, not evidence that session mutation occurred.

### Failure vocabulary

Worker may define a compact T4-specific failure union but must not change
existing enums. It must distinguish isolated-evidence rejection, invalid
review/repair input, revision-ledger rejection, closer-count/identity failure,
non-terminal review, commit-authorization rejection, and material/session
overlap.

## Focused Test Matrix

Required tests include:

- worker outputs are excluded from isolated reviewer sources;
- distinct reviewer recomputes evidence and receives a packet-bound receipt;
- self-approval, tainted evidence, and empty evidence fail closed;
- deterministic defect, dissent, and review receipt replay;
- repair request requires one repair owner;
- first bounded repair is allowed and second repair at ceiling escalates;
- repaired revision may terminate ACCEPT;
- zero, empty, or multiple designated closers fail closed;
- wrong acting closer and worker-as-closer fail closed;
- empty or non-terminal review collections block integration;
- all ACCEPT produces ACCEPT, all REJECT produces REJECT, mixed terminal reviews produce PARTIAL_ACCEPT;
- only designated closer receives commit authorization;
- no material commit ref produces session-sync-pending without a fabricated ref;
- valid post-commit projection preserves the caller ref and session surfaces;
- material/session path overlap fails closed;
- source imports no git/process/network/provider/session-generator owner; and
- local MAO barrel exports the new composition owner.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MAO_OA_T4_WORKER_RETURN_2026-07-17.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required section names: Purpose; Target / Source; Scope / Methodology; Findings
/ Position; Risk / Corrective Action; Checker Source Read-Ahead Block; Agent
Operation Trace Block; Delta Execution Claim Boundary Control Block; Public
Export Disposition; External Knowledge Intake Routing; Rescan Intelligence
Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance
Learning Disposition; Epistemic Process Block; Claim Boundary; git status
--short; Changed Files; Worker Experience Retrospective; Command Evidence;
No-Commit Statement.

Do not pass a Vitest TypeScript path to `--pytest-target`. Use the package npm
test command and run the worker-return fast gate without a pytest target.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | delegated implementation worker; independent reviewer/closer follows |
| phase | DISPATCH then EXECUTION then REVIEWER_CLOSURE |
| baseHeadFor(phase) | dispatchBaseHead=`baaabd064`; executionBaseHead=worker captures committed dispatch/sync HEAD; closureBaseHead=reviewer captures unchanged worker HEAD |
| changedSetScope(phase) | dispatch=roadmap plus baseline plus work order; execution=exact six worker paths; closure=worker paths plus reviewer-owned closure paths only |
| traceScope(phase, actor) | each actor records only paths changed in that actor phase |
| commitOwner(phase) | dispatcher commits packet; worker must not commit; reviewer/closer owns material closure; session-sync steward owns separate continuity commit |
| crossBatchIsolation | clean worktree required; T5-T7 and unrelated lanes parked |
| nextMoveSurfaces | worker forbidden; reviewer/closer updates roadmap and protected continuity only after accepted material closure |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MAO_OA_T4_COMPLETION_REVIEW_2026-07-17.md` |
| reviewerOwnedClosurePaths | governing roadmap; paired baseline; this work order; worker return; completion review; allowed source/test review repairs; narrow GC-051 source/aggregate repair if independently required |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Epistemic Process Block

Epistemic Process Applicability: BOUNDED_GOVERNANCE_IMPLEMENTATION

Expected Result / Prediction: existing reviewer-isolation, dissent/revision,
and closer-interlock owners can be composed behind one local convergence owner
without modifying those owners or performing external action.

Evidence Comparison Requirement: worker and reviewer compare source imports,
isolated packet contents, receipt hashes, revision decisions, closer identity,
integration result, commit authorization, session projection, focused/package
tests, and registry/gate evidence against the prediction.

Contradiction Or Gap Disposition: any need to modify an existing owner, run git
or session mutation, import provider/process/network code, or invent a second
reviewer/closer/commit mechanism blocks the worker.

Claim Update Requirement: closure states whether local convergence composition
is confirmed, narrowed, or rejected and must not promote typed plans into proof
that independent agents, commits, or session updates actually ran.

## Verification Commands

Run from repository root; npm commands use
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` as working directory.

```powershell
git status --short --untracked-files=all
git rev-parse --short HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
npm test -- tests/mao.operational.review.convergence.test.ts
npm run check
npm test
python governance/compat/generate_corpus_scan_registry.py --generate
python governance/compat/generate_corpus_scan_registry.py --check
python governance/compat/check_changed_corpus_registry_coverage.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
git status --short --untracked-files=all
git rev-parse --short HEAD
```

## Acceptance Criteria

- exactly six allowed paths changed and none staged;
- HEAD equals captured `executionBaseHead`;
- no forbidden import, mutation, dependency, owner, or later-tranche behavior;
- source isolation and self-approval boundaries match existing contracts;
- repair ownership, sequential revision, and ceiling escalation are proven;
- exactly-one-closer and terminal-review convergence are proven;
- commit authorization and session projection remain non-mutating signals;
- material/session changed sets are disjoint;
- focused tests, typecheck, package tests, registry checks, file-size check,
  worker-return fast gate, and diff hygiene pass;
- every failure is disclosed rather than waived; and
- worker return is `COMPLETE_PENDING_REVIEW`, not a closure claim.

## Review Gate

Independent reviewer must inspect every changed line, recompute isolation,
receipt determinism, revision ceiling, closer identity, integration decisions,
commit authorization, and material/session disjointness; rerun focused,
typecheck, package, registry, and governance evidence; and confirm no action or
T5-T7 scope entered the worker batch.

## Closure Diff Gate

Reviewer compares roadmap T4 row, paired baseline, this work order, current MAO
owners, exact worker diff, tests, worker return, completion review, registry,
and final roadmap/session state. Every item ends PASS, N/A with reason, or
BLOCKED with return action.

## Closure Checklist

| Item | Required closure disposition |
|---|---|
| exact six-path worker set | reviewer recomputed |
| no-commit boundary | reviewer verified |
| existing-owner reuse | reviewer proven |
| source isolation and self-approval | reviewer rerun |
| dissent, repair owner, and revision ceiling | reviewer rerun |
| closer count/identity and terminal convergence | reviewer rerun |
| commit/session non-mutation and disjointness | reviewer rerun |
| focused, typecheck, and package tests | reviewer rerun |
| GC-051 source/aggregate alignment | reviewer rerun |
| roadmap/session continuity | reviewer/closer and session-sync steward only |
| public export | DEFERRED_PRIVATE_ONLY unless separately authorized |

## Reviewer Closure Decision

N/A with reason: pending worker implementation and independent review. This
dispatch packet makes no acceptance or closure decision.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: DISPATCH_READY` | PASS |
| Completion or reviewer artifact | planned T4 completion review | reviewer-owned following worker return | N/A with reason |
| Roadmap state | governing MAO-OA roadmap | T4 dispatched; T5-T7 held | PASS |
| Registry JSON | planned T4 source entry and generated aggregate | worker generator plus reviewer checks | N/A with reason |
| Registry Markdown | GC-051 JSON source and aggregate; no separate Markdown owner | dispatch has no closure registry mutation | PASS |
| External evidence digest | N/A with reason: no external evidence consumed | none | N/A with reason |
| System loop interlock | N/A with reason: no repository governance loop/process launcher mutation | none | N/A with reason |
| Session continuity | protected sync following dispatch material commit | worker forbidden | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Required evidence | Dispatch state |
|---|---|---|
| local review convergence | focused deterministic tests | PENDING_WORKER |
| actual commit/session action | N/A with reason: mutation forbidden | N/A_WITH_REASON |
| provider acceptance | N/A with reason: provider invocation forbidden | N/A_WITH_REASON |
| reviewer acceptance | independent completion review | PENDING_REVIEW |
| public acceptance | N/A with reason: public action forbidden | N/A_WITH_REASON |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` without scope expansion when:

- safe behavior requires modifying an existing MAO contract or enum;
- git, commit steward, session generator, provider/network/process/queue, or a
  new dependency becomes necessary;
- exactly-one-closer or independent-evidence semantics cannot be preserved;
- exact six-path manifest cannot be preserved;
- unrelated worktree changes appear;
- a repeated defect needs ADIF mutation outside worker scope; or
- worker commit/staging becomes necessary.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | MAO-OA-T4 dispatch authoring, 2026-07-17 |
| Working directory | repository root |
| Command or tool surface | governed reads, source searches, ADIF resolver, scaffold preview, apply_patch, governance gates, git |
| Target paths | governing roadmap; paired T4 baseline; this T4 work order |
| Allowed scope source | standing operator sequence authority, accepted T3 closure, governing roadmap, canonical MAO/AHB contracts |
| Before status evidence | clean worktree at `baaabd064`; planned T4 paths absent |
| After status evidence | exact three-path dispatch packet pending verification and material commit |
| Diff evidence | `git diff --name-status`; `git diff --check`; pre-dispatch range from `baaabd064` |
| Approval boundary | bounded T4 local review-convergence dispatch only |
| Claim boundary | no worker implementation, actual reviewer agents, git/session mutation, T5-T7, provider/live, public, or push action |
| Agent type | dispatcher |
| Invocation ID | `mao-oa-t4-dispatch-2026-07-17` |
| Expected manifest | `docs/roadmaps/CVF_MAO_OPERATIONAL_ADOPTION_AND_AGENT_EXECUTION_ASSURANCE_ROADMAP_2026-07-16.md`; `docs/baselines/CVF_GC018_MAO_OA_T4_OPERATIONAL_REVIEW_CONVERGENCE_AND_COMMIT_SESSION_INTERLOCK_2026-07-17.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T4_OPERATIONAL_REVIEW_CONVERGENCE_AND_COMMIT_SESSION_INTERLOCK_2026-07-17.md` |
| Actual changed set | `docs/roadmaps/CVF_MAO_OPERATIONAL_ADOPTION_AND_AGENT_EXECUTION_ASSURANCE_ROADMAP_2026-07-16.md`; `docs/baselines/CVF_GC018_MAO_OA_T4_OPERATIONAL_REVIEW_CONVERGENCE_AND_COMMIT_SESSION_INTERLOCK_2026-07-17.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T4_OPERATIONAL_REVIEW_CONVERGENCE_AND_COMMIT_SESSION_INTERLOCK_2026-07-17.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | local execution-plane review/dissent/closer convergence and commit/session interlock plan |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE after deterministic focused tests and independent review only |
| receiptEvidence | CVF_RECEIPT_PRESENT only as deterministic MAO review/integration receipts; no action/provider receipt |
| actionEvidence | N/A with reason: runtime mutation is forbidden; tests exercise pure/local composition only |
| invocationBoundary | package-local tests, typecheck, registry generation, and governance checks |
| interceptionBoundary | no IDE/shell/git/provider interception, wrapper/proxy enforcement, runtime gate, or agent coding-control claim |
| claimLanguage | bounded internal convergence component; not an autonomous reviewer/closer or commit executor |
| forbiddenExpansion | no git/session mutation, real provider/router/network/process/queue, T5-T7, live/public/push work |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch. No public artifact,
public-sync operation, or public claim is authorized.

## Claim Boundary

This work order authorizes exactly one local review-convergence composition
owner, one local-barrel export, focused tests, narrow GC-051 source/aggregate
coverage, and one no-commit worker return. It does not authorize or prove
actual independent reviewer-agent execution, automatic repair, git commit,
session mutation, real provider work, operator projection, public or production
readiness, distributed concurrency, scale, shipment, or user value.
