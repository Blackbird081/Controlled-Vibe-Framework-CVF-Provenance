# CVF Agent Work Order - EACQ-FV MV-1 Conditional Reopen Index Enforcement

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Work order ID: EACQ-FV-MV1

Batch ID: EACQ-FV-MV1

Dispatch base head: `f10c3e4188c22b72797651bd1cac5b1e4b5726f9`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated bounded implementation worker

Reviewer/closer: designated internal orchestrator/reviewer

Worker return path: `docs/reviews/CVF_EACQ_FV_MV1_CONDITIONAL_REOPEN_INDEX_ENFORCEMENT_WORKER_RETURN_2026-08-27.md`

## Dispatch Prompt Envelope

Role: delegated no-commit implementation worker for EACQ-FV-MV1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_EACQ_FV_MV1_CONDITIONAL_REOPEN_INDEX_ENFORCEMENT_2026-08-27.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

providerExecutionAuthority: FORBIDDEN.

Current-time notes: private provenance repository, 2026-08-27; operator has
approved only MV-1 and assigned an internal orchestrator/reviewer.

Do-not-misread notes: enforce the existing rule only; no doctrine, index,
hook, catalog, roadmap, session, provider, network, public-sync, deployment,
push, stage, or commit change is authorized.

Required first actions: read startup surfaces and every Required First Read;
then prove ancestry, pinned hashes, clean worktree, empty staging, absent
output paths, and run the pre-implementation route/autorun checks.

Return contract: create exactly the checker, focused test module, and worker
return; run all required verification after the final edit; leave changes
unstaged and uncommitted; return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Implement one deterministic compatibility checker that prevents a changed
absorption closeout from silently dropping a conditional forward-value
candidate from the central reopen index. Preserve the current rule, candidate
vocabulary, index owner, archive boundary, and authority hierarchy.

## Scope / Target / Owner Boundary

Allowed: three exact new paths in Write Ownership. Forbidden: every existing
file, including the core standard and conditional index; any hook/catalog
wiring; staging/commit; session state; provider/network/environment/credential
access; public sync; deployment; and push.

## Worker Autonomy / No-Question Rule

Within the exact three-path scope, implementation, tests, fixture design,
literal-shape repair, and required-gate repair are mandatory. Escalate only if
the task requires an existing-file edit, wider authority, live/provider work,
secrets/quota, public action, destructive action, or a rule change.

## Authority Chain

Existing absorption core standard -> revised EACQ-FV roadmap -> explicit
operator authorization -> committed GC-018/work order -> no-commit worker ->
independent reviewer/closer. Worker success is not closure or successor
authority.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R0 review | all 14 findings dispositioned; four blocking defects repaired | ACCEPT |
| Operator decision | explicit approval and role split, 2026-08-27 | ACCEPT |
| Existing rule | core-standard Conditional Reopen Index Rule | ACCEPT_AND_PRESERVE |
| Existing owner | central conditional reopen index | ACCEPT_AND_PRESERVE |
| Checker gap | R0 `MACHINE_GATE_GAP`, with FPC/KIOD precedents | ACCEPT_FOR_MV1 |
| MV-2/MV-3/UAA | separate value gates not opened | NOT_AUTHORIZED |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap control | MV-1 handling | Proof |
| --- | --- | --- |
| existing rule only | parse the three existing semantic outcomes | no new doctrine token |
| precedent reuse | adapt FPC/KIOD range and index patterns | source read-ahead plus tests |
| negative MPA case | candidate disappears without disposition | focused fixture must fail for that reason |
| no hook wiring | checker stays standalone | exact changed set |
| bounded cost | local deterministic tests only | no provider/network use |

## Required First Reads

1. `AGENTS.md`, `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`,
   `CVF_SESSION_MEMORY.md`, and the active handoff they name.
2. `docs/reference/guard_orientation/README.md` and
   `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
3. The paired roadmap, GC-018 baseline, and this work order.
4. `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`.
5. `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md`.
6. `governance/compat/check_fpc_parked_reopen_inventory.py` and
   `governance/compat/check_kiod_runtime_candidate_reopen_inventory.py`.
7. `governance/compat/check_external_absorption_core.py`.
8. Applicable dispatch, worker-return, task-route, AOT, read-ahead, and
   self-protection checker sources named below.

## Agent Roles

- The worker authors and tests exactly three uncommitted paths.
- The reviewer independently reviews semantics and negative cases, performs bounded
  repair if justified, owns commit/closure, and updates continuity state.
- The operator owns any successor tranche, public action, or expanded scope.

## Pre-Flight Checks

1. Capture `executionBaseHead`; prove dispatch-base ancestry.
2. Confirm a clean worktree and empty staging before edits.
3. Confirm all three writable paths are absent.
4. Recompute all pinned input hashes and stop on drift.
5. Complete required reads and run pre-implementation route/autorun gates.

## Pinned Input Hashes

| Path | SHA-256 |
| --- | --- |
| `docs/roadmaps/CVF_EXTERNAL_AGENT_CODING_QUALITY_AND_FORWARD_VALUE_ABSORPTION_ROADMAP_2026-08-27.md` | `aa1133380ba5b355577a4398d9dfaa8afc8ed23ae2a6d1eac92a903054ee127b` |
| `docs/reviews/CVF_EACQ_FV_R0_EXTERNAL_ADVERSARIAL_REVIEW_DISPOSITION_2026-08-27.md` | `dea56bbe89fb177ba160dbb27816b3134f28331b6145c4d2fdb12242fc1b63cc` |
| `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | `8f9ca8cb509b6ebdfe2dda5922d319e5803d856c8972c48ac0dbb73a715d2988` |
| `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | `c1b5cab4b3f8e5805e2d3fb221fdb11a3cecf4e63958b4dadc62f97e2a8b6a30` |
| `governance/compat/check_fpc_parked_reopen_inventory.py` | `5fe1083492864a680395298ac91e315629431a5872d17e0c02f9d410d70ce0b1` |
| `governance/compat/check_kiod_runtime_candidate_reopen_inventory.py` | `9755024250fbfe405fd3fccd32628d1d23e04a7e04e765e598ac09ad63d77d9d` |

The roadmap hash includes the orchestrator-owned approval/dispatch-status
update in this packet. The worker must verify the committed dispatch packet
and treat any semantic drift as blocking.

## Write Ownership

Create only:

- `governance/compat/check_external_absorption_conditional_reopen_index.py`
- `governance/compat/test_check_external_absorption_conditional_reopen_index.py`
- `docs/reviews/CVF_EACQ_FV_MV1_CONDITIONAL_REOPEN_INDEX_ENFORCEMENT_WORKER_RETURN_2026-08-27.md`

Every other path is read-only. The worker must not stage or commit.

## Required Implementation Contract

### Applicability And Changed-Set Semantics

Inspect relevant current, non-archive absorption closeout/audit/review documents
changed in `base..head` plus staged, unstaged, and untracked state. Behavior
must be deterministic, path-normalized, archive-safe, and callable as both a
module and CLI. Follow existing compatibility-checker conventions without
editing a shared helper.

### Existing Candidate Vocabulary

Use only the candidate categories already enumerated in the core-standard
Conditional Reopen Index Rule. Do not broaden them, infer a new forward-value
taxonomy, or make heuristic prose normative.

### Three Existing Semantic Outcomes

For each governed candidate in a changed closeout, require exactly one
machine-verifiable outcome:

1. a matching central-index row is added or updated in the same changed set;
2. the closeout cites a specific existing matching index row and explicitly
   states why that row remains current; or
3. the closeout contains exact
   `NO_CONDITIONAL_REOPEN_INDEX_ENTRY_WITH_REASON` with a non-empty reason
   aligned to the existing rule: fully adapted, rejected with no remaining
   value, or already owned by another governed index.

A bare path to the index, a row-like label without a resolvable matching row,
or generic "already covered" prose must fail. Existing-row proof must validate
the cited row identifier/path against the current central index.

### Mandatory MPA Regression

Create a negative fixture modeled on the MPA deferred closeout: it contains a
recognized conditional candidate but neither changes a matching index row,
cites a current matching row with rationale, nor supplies the exact no-entry
reason marker. Assert that the checker fails specifically because that
candidate disappeared from the reopen index. This is the primary regression,
not an incidental malformed-file test.

### Focused Case Matrix

Tests must cover at least:

- positive matching row add/update;
- positive cited existing matching row plus current rationale;
- positive exact no-entry marker with each allowed reason class or a
  parameterized equivalent;
- negative MPA omission;
- negative bare index-path citation;
- negative missing/non-matching row identifier;
- negative empty or unsupported no-entry reason;
- archive-only non-applicability;
- committed-range plus staged, unstaged, and untracked discovery;
- deterministic repeated output and CLI exit status.

Use temporary Git repositories or isolated fixtures; do not mutate governed
repository evidence during tests.

## Execution Plan

1. Complete pre-flight evidence and source reads without editing.
2. Implement the standalone checker inside the exact new checker path.
3. Build isolated positive and negative fixtures, with the MPA omission first.
4. Run focused tests and remediate every allowed-scope failure before
   proceeding.
5. Populate the worker return after the final code/test edit; rerun every
   verification command and leave staging empty.

## Evidence Requirements

The return must identify parser entrypoints, changed-set discovery, the three
outcome validators, MPA regression test, focused case names, command exit
codes, exact changed paths, and zero staged paths. Self-reported PASS is
evidence for review, not acceptance.

## Acceptance Criteria

All clauses in Required Implementation Contract and Focused Case Matrix are
mandatory. The worker changed set is exactly three paths, every final
verification command is recorded, and no existing governed file is edited.

## Verification Commands

Run after the final edit and record exit codes plus concise output:

```powershell
git merge-base --is-ancestor f10c3e4188c22b72797651bd1cac5b1e4b5726f9 HEAD
python governance/compat/run_adif_defect_resolver.py --task-class "checker implementation" --role worker --lifecycle-phase pre-implementation --surface-selector governance/compat --risk-ceiling HIGH --json
python -m pytest governance/compat/test_check_external_absorption_conditional_reopen_index.py -q
python governance/compat/check_external_absorption_conditional_reopen_index.py --base f10c3e4188c22b72797651bd1cac5b1e4b5726f9 --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_external_absorption_conditional_reopen_index.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-review --base f10c3e4188c22b72797651bd1cac5b1e4b5726f9 --head HEAD
git diff --check
git diff --name-only
git diff --cached --name-only
git status --short
```

If a repository-wide gate fails solely because the checker is intentionally
not hook-wired, record that exact result; do not widen scope to repair it.

## Work-Order Fulfillment Manifest

| Requirement | Required evidence in worker return |
| --- | --- |
| exact changed set | three paths only; empty staged set |
| semantic outcomes | implementation location and tests for all three |
| MPA regression | named test and observed failure reason |
| range/worktree behavior | tests for committed, staged, unstaged, untracked |
| archive safety | named focused test |
| deterministic CLI | repeated result and exit-code tests |
| final verification | commands, exit codes, concise outputs |
| claim boundary | no closure, hook, provider, public, or production claim |

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "EACQ-FV-MV1",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "CREATES_OR_CHANGES_AUTHORITY",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": [
    "governance/compat",
    "docs/reviews",
    "docs/baselines",
    "docs/roadmaps",
    "docs/work_orders"
  ],
  "claims": [
    "deterministic local checker",
    "existing-rule enforcement only"
  ],
  "requiredProof": [
    "focused positive and negative tests",
    "negative MPA regression fixture",
    "exact changed-set and no-commit evidence"
  ],
  "operatorCheckpoints": [
    "independent reviewer check before commit",
    "operator value gate before any successor tranche"
  ],
  "forbiddenEffects": [
    "provider or network execution",
    "hook or catalog wiring",
    "public sync, deployment, push, or worker commit"
  ],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: bounded named owner/checker cluster; no corpus completeness claim",
    "completenessClaimChanged": false
  }
}
```

Expected route: `P3_ELEVATED`, `ROUTED_SHADOW`, full legacy bundle preserved.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_external_absorption_conditional_reopen_index.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must begin with `Status: COMPLETE_PENDING_REVIEW` or
`Status: BLOCKED_WITH_REASON`, declare `Self-declared worker-return artifact:
yes`, name this work order in both `Responds to work order:` and
`dispatchWorkOrder:`, and use level-two headings named: Purpose; Scope /
Methodology; Findings / Position; Risk / Corrective Action; Checker Source
Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary
Control Block; Public Export Disposition; External Knowledge Intake Routing;
Rescan Intelligence Hardening; Corpus Completeness And Report Integrity;
Finding-To-Governance Learning Disposition; Epistemic Process Block; Claim
Boundary; git status --short; Changed Files; Command Evidence; and No-Commit
Statement.

No placeholder such as `FILL_ME` or `WORKER_MUST_CAPTURE_AT_START` may remain.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `check_dispatch_prompt_envelope.py`; `check_worker_return_quality_gate.py`; `check_governed_artifact_checker_read_ahead.py`; `check_core_guard_self_protection.py`; `check_task_governance_route.py`; `check_agent_operation_trace.py`; implementation precedents `check_fpc_parked_reopen_inventory.py`, `check_kiod_runtime_candidate_reopen_inventory.py`, and `check_external_absorption_core.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `providerExecutionAuthority: FORBIDDEN`; `Core Guard Self-Protection Authorization`; `NO_CONDITIONAL_REOPEN_INDEX_ENTRY_WITH_REASON`; worker-return required headings |
| gateRunPurpose | Confirm as evidence that dispatch, route, protected-checker authorization, read-ahead, trace, and no-commit return contracts are known before implementation; gate runs are not first discovery. |
| claimBoundary | Source read-ahead is preparation evidence only and does not establish checker correctness or closure. |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create only the new conditional-reopen
compatibility checker and its focused test; no existing guard modification.

Protected paths:

- `governance/compat/check_external_absorption_conditional_reopen_index.py`
- `governance/compat/test_check_external_absorption_conditional_reopen_index.py`

Operator authorization: explicit EACQ-FV-MV1 opening and orchestrator/worker role
split on 2026-08-27.

Rollback boundary: if rejected, remove only the two new code/test files and
retain R0 review, disposition, roadmap, index, and provenance evidence. The
worker may not edit existing guards, runners, hook chains, catalogs,
standards, indexes, or policy.

## Commit Mode And Base-Anchor Lifecycle

Commit mode is `WORKER_MUST_NOT_COMMIT`. The dispatch base is the minimum
required ancestor, not permission to reset. The worker captures the actual
execution head at start, never rebases/resets, keeps staging empty, and reports
any base drift. The reviewer owns any accepted commit.

| Field | Value |
| --- | --- |
| baseHeadFor(phase) | dispatchBaseHead=`f10c3e4188c22b72797651bd1cac5b1e4b5726f9`; executionBaseHead=worker captures; closureBaseHead=reviewer sets |
| changedSetScope(phase) | worker exact three paths; reviewer repairs only there; continuity is separate |
| commitOwner(phase) | designated reviewer/closer only |

## Negative Search And Collision Discipline

Before implementation, run exact query
`rg -n --hidden --no-ignore "conditional reopen|NO_CONDITIONAL_REOPEN_INDEX_ENTRY_WITH_REASON|check_external_absorption_conditional_reopen_index" governance/compat docs/reference docs/reviews docs/audits`
across search roots `governance/compat`, `docs/reference`, `docs/reviews`, and
`docs/audits`. Current collision disposition: FPC and KIOD occurrences are
authoritative precedents with different bounded owners, while no same-path
general binding checker exists at dispatch. If a competing general binding
implementation appears later, stop with `BLOCKED_WITH_REASON` and report the
collision without writing.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | governed R0 finding -> revised roadmap -> bounded MV-1 enforcement order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing absorption core standard and conditional reopen index |
| Disposition | ADAPT only as enforcement of the existing rule |
| Claim boundary | no new external knowledge, doctrine, provider, or effectiveness claim |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: bounded implementation of an existing rule; no source reassessment is performed.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - bounded named-owner implementation; no corpus inventory or completeness claim.

## Intake Role Routing Decision

| Field | Assignment |
| --- | --- |
| selected role route | MULTI_AGENT_SINGLE_ROLE |
| intake summary | operator-authorized bounded checker implementation |
| scope classification | local three-path no-commit protected-governance implementation |
| worker role | delegated no-commit implementation worker |
| reviewer role | designated internal orchestrator/reviewer/closer |
| escalation condition | existing-file edit, authority expansion, provider/public effect, destructive action, or rule change |
| risk sensitivity | elevated because a new compatibility checker is created; external effect remains none |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: the legacy-derived R0 source has already been
absorbed into governed roadmap/index evidence. MV-1 changes no legacy coverage
claim and performs only local enforcement implementation.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`checker implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class "checker implementation" --role worker --lifecycle-phase pre-implementation --surface-selector governance/compat --risk-ceiling HIGH --json`.
Dispatch-time result was not truncated. Any later non-empty result is a
mandatory overlay and must be recorded in the worker return.

## Scaffold Provenance Block

| Field | Evidence |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id EACQ_FV_MV1_CONDITIONAL_REOPEN_INDEX_ENFORCEMENT --title "EACQ-FV MV-1 Conditional Reopen Index Enforcement" --date 2026-08-27 --base f10c3e418 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | protected-governance-path, no-commit |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled existing-rule semantics, ownership, MPA regression, routing, handoff, and return contract. |
| checkerReadAheadConfirmation | Applicable dispatch and implementation precedent sources were read before authoring. |
| docOnlyNewFields | N/A with reason: no new normative field is introduced. |
| claimBoundary | Scaffold provenance is authoring evidence, not implementation or closure proof. |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | external no-commit implementation worker followed by independent internal reviewer |
| phase | MV-1 worker implementation then reviewer closure |
| baseHeadFor(phase) | dispatchBaseHead=`f10c3e4188c22b72797651bd1cac5b1e4b5726f9`; executionBaseHead=worker captures; closureBaseHead=reviewer sets |
| changedSetScope(phase) | worker exact three paths; reviewer repairs only there; continuity separate |
| traceScope(phase, actor) | reads, decisions, commands, tests, manifest, and no-commit evidence |
| commitOwner(phase) | designated reviewer/closer only |
| crossBatchIsolation | no MV-2, MV-3, UAA, hook, public, provider, deployment, or push |
| nextMoveSurfaces | worker return, then reviewer completion and continuity only after acceptance |

## Foundation Storage Layout Block

N/A with reason: the tranche creates one standalone compatibility checker and
one colocated test under the existing `governance/compat` owner; it creates no
new reference family, folder, index, split, relocation, or durable-foundation
layout.

## Delta Execution Claim Boundary Control Block

Delta execution claim boundary: REQUIRED

| Field | Value |
| --- | --- |
| claimScope | local checker implementation and synthetic tests only |
| claimDisposition | N/A with reason: no agent-control or runtime-execution claim is made |
| receiptEvidence | N/A with reason: no provider/runtime receipt is required or claimed |
| actionEvidence | N/A with reason: local file/test evidence only |
| invocationBoundary | the work order does not assert mandatory invocation or wrapper coverage |
| interceptionBoundary | no interception, proxy, hook, or universal control is authorized |
| claimLanguage | implementation remains pending independent review |
| forbiddenExpansion | no universal governed-coding, runtime, provider, public, or production claim |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | internal orchestrator/dispatcher |
| Provider or surface | local private-provenance repository |
| Session or invocation | EACQ-FV-MV1 work-order authoring, 2026-08-27 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | governed reads, source search, Git, scaffold helper, ADIF resolver, `apply_patch` |
| Target paths | roadmap, GC-018 baseline, this work order |
| Allowed scope source | operator authorization and orchestrator/worker role split, 2026-08-27 |
| Before status evidence | clean worktree at base `f10c3e4188c22b72797651bd1cac5b1e4b5726f9` |
| After status evidence | dispatch-ready packet only; implementation absent |
| Diff evidence | expected dispatch-author manifest below |
| Approval boundary | MV-1 dispatch authoring only |
| Claim boundary | no implementation, commit by worker, provider, public, push, or production claim |
| Agent type | orchestrator/dispatcher/reviewer |
| Invocation ID | `eacq-fv-mv1-dispatch-2026-08-27` |
| Expected manifest | roadmap, baseline, work order |
| Actual changed set | roadmap, baseline, work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | NONE |

## Expected Output Manifest

Worker output must be exactly:

1. `governance/compat/check_external_absorption_conditional_reopen_index.py`
2. `governance/compat/test_check_external_absorption_conditional_reopen_index.py`
3. `docs/reviews/CVF_EACQ_FV_MV1_CONDITIONAL_REOPEN_INDEX_ENFORCEMENT_WORKER_RETURN_2026-08-27.md`

Any extra changed path is `BLOCKED_WITH_REASON` unless restored without
discarding pre-existing user work.

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_EACQ_FV_MV1_CONDITIONAL_REOPEN_INDEX_ENFORCEMENT_COMPLETION_2026-08-27.md`

reviewerOwnedClosurePaths: the exact three worker paths; the completion review
and continuity updates are separately reviewer-owned.

The reviewer must independently inspect the implementation, run focused and
applicable governance gates, probe the MPA negative case and all three positive
outcomes, compare actual changed set to the manifest, and either reject/repair
or create the separate completion packet. Worker self-report is not closure.

Completion target:
`docs/reviews/CVF_EACQ_FV_MV1_CONDITIONAL_REOPEN_INDEX_ENFORCEMENT_COMPLETION_2026-08-27.md`.

## Review Gate

Review remains closed until the worker returns the exact no-commit manifest.
The reviewer then verifies rule fidelity, tests an independent missing-index case,
confirms no candidate-vocabulary expansion, runs all applicable gates, and
records ACCEPT, RETURN_FOR_REPAIR, or BLOCKED_WITH_REASON.

## Closure Checklist

- [ ] exact worker manifest and empty staging independently confirmed;
- [ ] all three outcome branches and negative MPA regression reviewed;
- [ ] focused tests and applicable governance gates pass after final edit;
- [ ] no hook/catalog/standard/index/session drift exists;
- [ ] completion evidence and continuity update are reviewer-owned;
- [ ] successor remains behind a fresh operator value gate.

## Return-To-Orchestrator Conditions

Return immediately after the final verification run with either
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`. Do not wait for permission
to repair failures inside the exact writable scope; remediate and rerun them.

operator.checkpoint.waiver: dispatch authorization is already recorded; the
next human decision is successor admission after independent MV-1 closure.
The worker must not self-select MV-2, MV-3, UAA work, public export, or any
external effect.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

No public artifact, remote, commit, or path is authorized or claimed by this
work order.

## Claim Boundary

This order authorizes only three-path, local, deterministic, no-commit MV-1
work. It does not change doctrine, close MV-1, authorize a successor tranche,
wire a hook, call a provider, publish, deploy, push, or prove production
effectiveness.
