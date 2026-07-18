# CVF Agent Work Order - MAO Durable Run Discovery Prerequisite

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: CVF-WEB-INHERITANCE-T3P1

Dispatch base head: `0e7904349`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated implementation worker

Reviewer/closer: CVF independent reviewer/closer

Worker return path:
`docs/reviews/CVF_WEB_INHERITANCE_T3P1_WORKER_RETURN_2026-07-18.md`

## Dispatch Prompt Envelope

Role: execute only CVF-WEB-INHERITANCE-T3P1 as a no-commit implementation
worker.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_INHERITANCE_T3P1_MAO_DURABLE_RUN_DISCOVERY_PREREQUISITE_2026-07-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: use the dispatcher-provided post-dispatch session HEAD and
verify it before any edit.

Current-time notes: source verification and packet date are 2026-07-18.

Do-not-misread notes: this is an execution-plane read-discovery prerequisite,
not a cvf-web page, MAO execution route, evidence store, heartbeat store,
configuration convention, or provider proof.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, paired baseline, roadmap, accepted T3A review, every source in Source
Verification, and checker source before implementation.

Return contract: leave exactly five allowed paths unstaged and uncommitted and
return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement a deterministic, read-only, fail-closed discovery seam over the
existing `MaoFileRunStore` root so a later prerequisite can enumerate valid
run identities without guessing them or weakening replay validation.

## Agent Roles

- Worker: bounded source/test implementation and no-commit return evidence.
- Reviewer/closer: independent code/test review, repairs, material commit, and
  closure conversion.
- Session-sync steward: protected continuity update in a separate commit.

## Authority Chain

Operator standing continuation authority -> CVF Web inheritance roadmap ->
accepted T3A review at `c0d88ff34` -> this T3P1 packet -> no-commit worker ->
independent reviewer/closer -> session-sync steward.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
4. `AGENT_HANDOFF_V47_2026-07-18.md`
5. `docs/reference/guard_orientation/README.md`
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
7. paired T3P1 baseline, roadmap, accepted T3A review, and every source in
   Source Verification

## Pre-Flight Checks

- verify instructed execution HEAD and a clean starting worktree;
- run pre-implementation autorun on the real execution base;
- confirm all five allowed paths and no collision with a pre-existing return;
- run current focused durable-store tests before editing; and
- stop before editing on a base mismatch or forbidden-scope requirement.

## Worker Autonomy / No-Question Rule

Repair source, test, or return-gate failures inside Allowed Scope and rerun.
Return to the orchestrator only for a base mismatch, source contradiction,
required sixth path, or a product decision beyond the specified contract.

## Intake Role Routing Decision

routeMode: SINGLE_AGENT_SINGLE_ROLE selected route

Intake summary: repository-local TypeScript store extension and focused tests.

Scope classification: one pure read method, one exported success type, tests,
and worker return.

Risk sensitivity: MEDIUM because corrupt-file handling and accidental writes
could produce misleading discovery evidence.

Role separation: worker cannot accept or commit its own implementation.

Escalation condition: required behavior conflicts with existing snapshot or
replay invariants.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition |
|---|---|---|---|
| T3A reviewer acceptance | `docs/reviews/CVF_WEB_INHERITANCE_T3A_COMPLETION_REVIEW_2026-07-18.md` | `c0d88ff34` | ACCEPT |
| T3A split decision | `docs/reviews/CVF_WEB_INHERITANCE_T3A_MAO_WEB_ADOPTION_AND_SOURCE_SEAM_DECISION_2026-07-18.md` | `c0d88ff34` | ACCEPT |
| current roadmap release | `docs/roadmaps/CVF_WEB_CAPABILITY_INHERITANCE_AND_OPERATOR_PROJECTION_ROADMAP_2026-07-18.md` | dispatcher material commit for this packet | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| snapshots use path-safe deterministic hashed filenames | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | `snapshotFileNameFor` | `snapshotFileNameFor` | durable run store | ACCEPT |
| full replay validation already owns snapshot trust | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | `loadAndReplay` | `loadAndReplay` | `MaoFileRunStore` | ACCEPT |
| existing failure union covers invalid JSON, schema, identity, authority, replay, and I/O | VALUE_SET | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | `MaoDurableRunStoreFailureReason` | `MaoDurableRunStoreFailureReason` | durable run store failure union | ACCEPT |
| existing atomic temporary files carry `.tmp-` after a canonical target path | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | `atomicWriteJson` | `tempPath` | durable filesystem helper | ACCEPT |
| durable-store types and class are exported by the local MAO barrel | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | durable run store export block | `MaoDurableRunResumeSuccess`; `MaoFileRunStore` | MAO local barrel | ACCEPT |
| package root forwards all local MAO exports | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | final export line | `./mao` | execution-plane package root | ACCEPT |
| durable-store test owns isolated real-filesystem behavior | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts` | `MaoFileRunStore` suite | `MaoFileRunStore` | focused vitest suite | ACCEPT |
| root-export test imports from the package root | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.package.root.exports.test.ts` | import and describe block | `execution package root MAO discoverability` | focused vitest suite | ACCEPT |
| package provides test and TypeScript commands | VALUE_SET | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/package.json` | `scripts` | `test`; `check` | npm manifest | ACCEPT |

## New Doc-Only Fields

| Field | Required value boundary |
|---|---|
| `discoveryReadContract` | exact method result and validation behavior |
| `canonicalSnapshotPolicy` | canonical snapshots versus ignored entries |
| `mutationProof` | filesystem evidence before and after reads |

## New Source Symbols

These are authorized new symbols and are not claims that they exist at
dispatch:

| Proposed symbol | Required shape | Owner |
|---|---|---|
| `MaoDurableRunListSuccess` | `{ ok: true; taskGraphIds: readonly string[] }` | `durable.run.store.ts` |
| `MaoFileRunStore.listRunIds` | `Promise<MaoDurableRunListSuccess \| MaoDurableRunStoreFailure>` | `MaoFileRunStore` |

## Scope / Target / Owner Boundary

Extend the existing durable-store owner only. Discovery must reuse the current
validation/replay authority. Tests may use real isolated temporary directories
but must remove them after each case.

## Allowed Scope

1. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts`
2. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts`
3. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts`
4. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.package.root.exports.test.ts`
5. `docs/reviews/CVF_WEB_INHERITANCE_T3P1_WORKER_RETURN_2026-07-18.md`

## Write Ownership

The worker owns only the five Allowed Scope paths. Reviewer closure conversion
also owns the paired baseline, this work order, roadmap, and T3P1 completion
review. Continuity is a separate protected sync.

## Forbidden Scope

- do not edit cvf-web, package manifests, lockfiles, configuration, evidence
  ledger, lifecycle controller, operational launcher, operator projection, or
  any other source/test path;
- do not call `createRun`, `appendEvent`, worker launch, provider, browser, or
  external network as discovery behavior;
- do not create the missing root, rewrite snapshots, delete entries, repair
  corrupt files, or silently omit a canonical invalid snapshot;
- do not add a second validation implementation when `loadAndReplay` can own
  full validation;
- do not edit registries, generated aggregates, session surfaces, public-sync,
  push, release, or production state; and
- do not stage, stash, or commit.

## Required Discovery Contract

1. Missing root: return successful empty list and perform no mkdir or write.
2. Candidate set: inspect regular files whose names match lowercase
   `[0-9a-f]{64}.json`; ignore atomic `.tmp-` files, subdirectories, and
   noncanonical unrelated entries.
3. Identity bootstrap: parse each canonical candidate only far enough to
   obtain a non-empty graph task ID; malformed canonical content fails closed.
4. Hash binding: recompute the canonical filename from the discovered task ID
   and require an exact filename match.
5. Trust: call the existing full replay-validation owner for every candidate;
   propagate its typed failure without partial success.
6. Result: return unique task IDs sorted by JavaScript lexicographic order.
7. Purity: repeated calls are deeply equal and do not change directory entry
   names, canonical bytes, or missing-root existence.

No partial-results field, warning list, path disclosure, repair mode, or
mutation option is authorized.

## Execution Plan

1. Run the pre-implementation gate and baseline focused tests.
2. Add the list success type and method using existing failure and replay
   owners.
3. Export the success type from the MAO local barrel.
4. Add focused cases for missing root, valid ordering, ignored entries,
   corrupt/mismatched canonical files, replay failure, repeated purity, and
   package-root availability.
5. Run focused tests, full package tests, TypeScript, file-size enforcement,
   and worker-return fast gate after the last edit.
6. Return exact five-path no-commit evidence.

## Required Artifact Manifest

| Required artifact | Expected result |
|---|---|
| durable store | one new read-only discovery method and success type |
| MAO barrel | success type exported |
| durable-store test | focused behavior and failure matrix |
| root-export test | method callable through package root |
| worker return | commands, results, exact path boundary, no-commit proof |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `durable.run.store.ts` | implement the specified pure discovery contract |
| `mao/index.ts` | export only the new success type |
| durable-store test | prove ordering, validation, failure, and purity |
| root-export test | prove package-root discoverability |
| worker return | record exact evidence after final edits |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Evidence |
|---|---|---|
| T3P1 read-only deterministic discovery | required discovery contract | focused store tests |
| no mutation or execution | missing-root and byte/entry purity proofs | focused negative tests |
| preserve validation authority | reuse `loadAndReplay` | corrupt and replay-invalid failures |
| package consumer availability | local-barrel type export and root call | TypeScript and root-export test |
| keep later dimensions parked | forbidden Web/evidence/liveness scope | exact changed set |

## Evidence Requirements

Evidence must show exact command lines and final results, real isolated
filesystem cases for every required discovery branch, before/after entry and
byte comparisons, package-root availability, exact changed set, empty cached
diff, unchanged execution HEAD, and no worker commit.

## Verification Commands

Run from `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION`:

```powershell
npx vitest run tests/mao.durable.run.store.test.ts tests/mao.package.root.exports.test.ts --config vitest.config.ts
npm test
npm run check
```

Run from repository root:

```powershell
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git diff --cached --name-status
git status --short --untracked-files=all
git rev-parse --short HEAD
```

## Acceptance Criteria

- AC-01: missing root succeeds empty without creating it.
- AC-02: valid snapshots return unique IDs in deterministic order after full
  validation.
- AC-03: unrelated entries are ignored and invalid canonical snapshots fail
  closed without partial results.
- AC-04: filename hash binding is checked.
- AC-05: repeated reads change no entry name or snapshot byte.
- AC-06: success type and method are available through package-root imports.
- AC-07: focused/full tests, TypeScript, worker-return gate, and file-size pass.
- AC-08: exact five-path no-commit boundary and unchanged execution HEAD hold.

Fail conditions:

- missing root is created or any discovery path writes;
- a canonical invalid snapshot is silently skipped;
- validation is weakened or duplicated inconsistently;
- result ordering or failure behavior is ambiguous;
- a forbidden path or Web/runtime claim enters the changed set; or
- any required final command fails.

## Review Gate

Independent reviewer must inspect the method for purity, race-safe fail-closed
behavior, canonical filename binding, reuse of replay validation, and test
coverage. Reviewer owns any material commit and closure claim.

## Closure Checklist

- [ ] execution HEAD matches dispatcher instruction;
- [ ] missing-root behavior is successful, empty, and non-creating;
- [ ] canonical candidate filtering and filename binding are tested;
- [ ] every canonical candidate receives full replay validation;
- [ ] ordering, uniqueness, and repeated-read purity are tested;
- [ ] local and package-root exports compile and pass;
- [ ] focused/full tests, TypeScript, file-size, and worker-return gate pass;
- [ ] exactly five paths change and nothing is staged;
- [ ] worker no-commit boundary is honored; and
- [ ] independent reviewer closure remains pending.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` before scope expansion if the existing failure
union cannot express a required failure safely, reuse of `loadAndReplay`
requires another source owner, execution HEAD mismatches, or a sixth path is
required.

## Operator Checkpoint

N/A with reason: standing authorization releases this narrow prerequisite.
T3P2, T3B, Web changes, provider/live, public, push, and production remain
outside this packet.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | execution-plane package root | read-only run ID discovery only | focused tests and typed result | no Web or execution adapter | `BOUNDED_RUNTIME_CONTRACT` |
| `EXTERNAL_AGENT_CLI_MCP` | no changed interface | no ingress, action, auth, receipt, or mutation | no adapter output | parked | `N/A_WITH_REASON` |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `SINGLE_AGENT_SINGLE_ROLE` |
| rolePattern | one implementation worker followed by independent reviewer/closer |
| phase | dispatch then no-commit implementation then reviewer closure then session sync |
| baseHeadFor(phase) | dispatchBaseHead=`0e7904349`; executionBaseHead=dispatcher-provided post-dispatch session HEAD; closureBaseHead=executionBaseHead |
| changedSetScope(phase) | dispatch=roadmap/baseline/work order; execution=exact five allowed paths; closure=reviewer-owned paths; session=protected continuity only |
| traceScope(phase, actor) | each actor records only its own commands, changed set, and boundary |
| commitOwner(phase) | dispatcher; none for worker; reviewer/closer; session-sync steward |
| crossBatchIsolation | T3P2, T3B, T4-T5, Web, provider/live, public, and production lanes remain parked |
| nextMoveSurfaces | worker must not edit; session steward owns protected updates separately |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_WEB_INHERITANCE_T3P1_COMPLETION_REVIEW_2026-07-18.md`

reviewerOwnedClosurePaths: five worker-owned paths, paired baseline and work
order, roadmap, and completion review; continuity only in a separate commit.

closureOwner: CVF independent reviewer/closer.

workerCommitPermission: FORBIDDEN.

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return, read checker source for its path and
conditional content. Include the full review shape, with explicit
non-applicability reasons where a conditional section does not apply.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_WEB_INHERITANCE_T3P1_WORKER_RETURN_2026-07-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required review headings include `Target / Source`, `Scope / Methodology`,
`Findings / Position`, `Risk / Corrective Action`, `Disposition`, `External
Knowledge Intake Routing`, and `Epistemic Process Block`.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`backend`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class backend --role dispatcher --lifecycle-phase pre-dispatch --surface-selector execution-plane --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Dispatch Prompt Envelope; Scope / Target / Owner Boundary; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; New Source Symbols; Allowed Scope; Forbidden Scope; Roadmap-To-Work-Order Trace Matrix; Acceptance Criteria; Review Gate; Closure Checklist; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition; Claim Boundary |
| gateRunPurpose | dispatch confirmation after direct source verification |
| claimBoundary | structural conformance does not prove implementation behavior |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-INHERITANCE-T3P1 --title "MAO Durable Run Discovery Prerequisite" --date 2026-07-18 --base 0e7904349 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled exact API contract, five-path manifest, focused test matrix, handoff, and no-Web boundary |
| checkerReadAheadConfirmation | checker paths listed above |
| docOnlyNewFields | three fields listed in New Doc-Only Fields |
| claimBoundary | dispatch-authoring provenance only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | CVF-WEB-INHERITANCE-T3P1 dispatch, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | startup reads, source verification, repository search, scaffold helper, artifact authoring, governance gates |
| Target paths | roadmap; paired T3P1 baseline; this work order |
| Allowed scope source | accepted T3A review and roadmap T3P1 row |
| Before status evidence | clean worktree at `0e7904349` |
| After status evidence | exact three-path dispatch set pending commit |
| Diff evidence | material diff captured before commit |
| Approval boundary | narrow read-only run-discovery prerequisite dispatch |
| Claim boundary | no Web, evidence/heartbeat persistence, execution, provider/live, public, push, or production mutation |
| Agent type | dispatcher |
| Invocation ID | `cvf-web-inheritance-t3p1-dispatch-2026-07-18` |
| Expected manifest | roadmap; T3P1 baseline; T3P1 work order |
| Actual changed set | exact three-path dispatch set |
| Manifest delta | MATCH after verification |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | read-only durable run discovery contract and tests |
| claimDisposition | N/A with reason: dispatch packet itself implements no behavior |
| receiptEvidence | N/A with reason: discovery creates no runtime receipt |
| actionEvidence | N/A with reason: no action surface is released |
| invocationBoundary | exact five-path no-commit worker packet |
| interceptionBoundary | no IDE, shell, provider, filesystem-action, or agent-action interception claim |
| claimLanguage | enumerate, validate, sort, and return run identities without mutation |
| forbiddenExpansion | Web, evidence/heartbeat persistence, run/event mutation, worker launch, provider/live, public, push, production |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: canonical snapshots can be discovered safely by
binding filename hashes to embedded graph IDs and reusing full replay
validation.

Evidence Comparison Requirement: worker return compares valid, missing,
ignored, corrupt, mismatched, and replay-invalid cases against the prediction.

Contradiction Handling Requirement: contradictory source or test evidence
requires `BLOCKED_WITH_REASON` and a narrowed claim.

Claim Update Requirement: worker return records whether the read-only
discovery contract is confirmed, narrowed, or invalidated.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance prerequisite dispatch; no public-sync action.

## Claim Boundary

This work order authorizes only the specified read-only run-discovery method,
type export, focused tests, and no-commit worker return. It does not authorize
cvf-web changes, evidence or heartbeat persistence, execution, provider/live,
public, push, release, production, or session mutation.
