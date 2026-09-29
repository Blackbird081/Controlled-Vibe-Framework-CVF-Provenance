# CVF Agent Work Order - RFR-R1 Build Authority Closure Amendment 1

Memory class: governed-worker-dispatch

Status: APPROVED_FOR_EXECUTION

Date: 2026-08-24

Batch ID: RFR-R1-AMENDMENT-1

Base: `9df990f8b56d6fbc0e314aa3a84959104586f7de`

dispatchBaseHead: `9df990f8b56d6fbc0e314aa3a84959104586f7de`

executionBaseHead: capture the committed Amendment 1 authority HEAD.

closureBaseHead: capture the committed Amendment 1 authority HEAD before
restoring the worker stash.

Commit mode: REVIEWER_CLOSER_OWNS_COMMIT

## Dispatch Prompt Envelope

Role: current orchestrator/reviewer performing one consolidated repair after
an external no-commit worker return.

Canonical packet: parent RFR-R1 baseline/work order, blocked worker return,
and paired Amendment 1 baseline/work order.

Commit mode: `REVIEWER_CLOSER_OWNS_COMMIT`.

executionBaseHead: capture the committed Amendment 1 authority HEAD before
restoring the external worker diff.

Current-time notes: only RFR-R1 Amendment 1 is released. R2-R6 remain parked.

Do-not-misread notes: preserve mandatory shared-factory enforcement; do not
add a compatibility flag or fabricate authority evidence.

Required first actions: commit amendment authority, restore the named worker
stash, verify exact restoration, then perform one consolidated reviewer repair.

Return contract: full proof, completion review, reviewer-owned material commit,
then separate continuity sync.

## Purpose

Close the exact dependent graph discovered by the RFR-R1 blocked worker return
while preserving fail-closed mandatory BUILD authority.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "RFR-R1-AMENDMENT-1",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "CREATES_OR_CHANGES_AUTHORITY",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_WITH_COMMIT",
    "novelty": "NEW_INTERFACE"
  },
  "pathFamilies": [
    "EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts",
    "EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/",
    "EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/",
    "EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts",
    "EXTENSIONS/CVF_GUARD_CONTRACT/src/index.test.ts",
    "docs/reference/system_chain/",
    "docs/reviews/",
    "docs/roadmaps/",
    "docs/baselines/",
    "docs/work_orders/"
  ],
  "claims": ["mandatory BUILD authority prerequisite with explicit runtime propagation"],
  "requiredProof": ["focused adversarial tests", "full Guard Contract tests", "TypeScript typecheck", "reviewer-fast", "pre-commit"],
  "operatorCheckpoints": ["R2 remains gated on accepted R1 closure"],
  "forbiddenEffects": ["provider or live call", "credential use", "deployment", "public write", "push", "new subsystem"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

Expected route: `ROUTED_SHADOW`, profile `P3_ELEVATED`, selective execution
false, legacy disposition `RUN_FULL_LEGACY_BUNDLE`.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator | operator message `next`, 2026-08-24 | ACCEPT |
| Parent baseline | `docs/baselines/CVF_GC018_RFR_R1_BUILD_AUTHORITY_CLOSURE_2026-08-24.md` | ACCEPT |
| Parent work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_RFR_R1_BUILD_AUTHORITY_CLOSURE_2026-08-24.md` | ACCEPT |
| Blocked evidence | `docs/reviews/CVF_RFR_R1_BUILD_AUTHORITY_CLOSURE_WORKER_RETURN_2026-08-24.md` | ACCEPT_AS_BLOCKER_ONLY |
| Amendment baseline | `docs/baselines/CVF_GC018_RFR_R1_BUILD_AUTHORITY_CLOSURE_AMENDMENT_1_2026-08-24.md` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V59_2026-08-11.md` | ACCEPT |

## Agent Roles

| Role | Owner | Boundary |
| --- | --- | --- |
| Operator | repository operator | authorized Amendment 1 with `next` |
| Dispatcher | current orchestrator | amendment authority only |
| Implementation worker | prior external worker | existing five-path no-commit diff only |
| Reviewer/closer | current orchestrator/reviewer | consolidated exact-scope repair, proof, review, and material commit |
| Session-sync steward | current orchestrator | separate post-acceptance continuity commit |

## Scope / Target / Owner Boundary

Repair exactly the original five worker paths plus:

1. `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.test.ts`
2. `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts`
3. `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.test.ts`
4. `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`

Reviewer-owned closure paths are:

- `docs/reviews/CVF_RFR_R1_BUILD_AUTHORITY_CLOSURE_COMPLETION_2026-08-24.md`
- `docs/roadmaps/CVF_RUNTIME_FINDINGS_CLOSURE_ROADMAP_2026-08-24.md`

Every other source, test, reference, governance, session, public, and external
path is read-only until a separate continuity batch is opened.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| exact guard count and IDs are stale | TEST_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.test.ts` | lines 39-63 | `createGuardEngine` tests | Guard Contract tests | ACCEPT |
| runtime config lacks BUILD evidence | INTERFACE_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | `RuntimeConfig`, line 88 | `RuntimeConfig` | Agent Execution Runtime | ACCEPT |
| pre-check omits BUILD evidence | COMPOSITION_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | `preCheck`, line 192 | context construction | Agent Execution Runtime | ACCEPT |
| BUILD fixtures omit evidence/targets | TEST_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.test.ts` | helper and BUILD suites | `defaultConfig`; `createRuntime` | runtime tests | ACCEPT |
| factory hash is governed | FRESHNESS_DEPENDENCY | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` | `CONTRACT_TO_RUNTIME`, lines 59-116 | source fingerprint | system-chain map | ACCEPT |

## Required First Reads

Read the active bootstrap/front door/handoff; guard orientation; literal
gotchas; parent RFR-R1 baseline/work order; Amendment 1 baseline/work order;
the exact implementation/runtime/test/map paths; system-chain freshness
standard; review-cost standard; and applicable checker sources.

## Pre-Flight Checks

Require the paired amendment-only changed set, empty staging, parent HEAD
`9df990f8b`, direct task-routing/work-order/ADIF/read-ahead passes, then the full
pre-dispatch autorun gate. Do not restore the worker stash until authority is
committed.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_worker_experience_retrospective.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_system_chain_map_freshness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | exact Source Verification columns; current definition lines; retrospective enums; `git diff --name-status`; review-cost vocabulary |
| gateRunPurpose | confirm Amendment 1 evidence and prevent a second dependent finding cascade; not first discovery |
| claimBoundary | source and checker read-ahead does not prove implementation |

## Required Artifact Manifest

| Path | Required state |
| --- | --- |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | retain typed evidence and mandatory ID; ASCII repair |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/build-authority.guard.ts` | malformed-safe fail-closed guard; ASCII repair |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/build-authority.guard.test.ts` | expanded malformed/ref normalization proof |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | mandatory export and registration |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.test.ts` | nine-guard composition assertions |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | typed authority propagation |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.test.ts` | valid BUILD evidence/target fixtures and fail-closed negative case |
| `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` | reviewed current factory fingerprint only; no automatic posture promotion |
| `docs/reviews/CVF_RFR_R1_BUILD_AUTHORITY_CLOSURE_WORKER_RETURN_2026-08-24.md` | truthful repaired return evidence |
| completion review and R1 roadmap | reviewer closure disposition |

No further path is authorized.

## Execution Instructions

1. Restore and verify the exact named worker stash after amendment authority is committed.
2. Complete one dependency-closure matrix before the first repair.
3. Make malformed `buildAuthority`, `allowedScope`, `targetFiles`, reference,
   expiry, and phase inputs fail closed without exceptions or bypass.
4. Add a typed `buildAuthority` field to `RuntimeConfig` and copy it into the
   pre-check `GuardRequestContext`; do not infer it from metadata.
5. Give positive BUILD runtime fixtures explicit valid evidence and targets;
   preserve negative BUILD coverage.
6. Update exact shared-factory assertions to nine guards.
7. Re-read `CONTRACT_TO_RUNTIME`; refresh only the changed source fingerprint
   after concluding whether posture/verdict remain unchanged.
8. Repair the worker return to match actual tests, gates, paths, and enums.
9. Create an independent completion review and update only the R1 roadmap row.

## Write Ownership

Write only the Required Artifact Manifest, completion review, and R1-only
roadmap transition. The later continuity batch owns only active handoff/session
projection paths. Everything else is read-only.

## Execution Plan

Commit amendment authority; restore and verify worker evidence; perform one
consolidated semantic repair; run narrow then full proof; author completion
evidence; commit material; run exact-range closure; synchronize continuity.

## Evidence Requirements

Record exact base/HEAD, changed-set and staging evidence, malformed-input
results, focused/full/typecheck counts, system-chain semantic disposition and
hash, worker-return/reviewer/pre-commit results, provider-call count zero,
material range, and parked-lane boundary.

## Acceptance Criteria

- malformed runtime objects return deterministic `BLOCK` results;
- whitespace-only references are rejected;
- mandatory shared composition remains unconditional;
- positive runtime execution requires explicit evidence and targets;
- focused/full/typecheck and governance gates pass;
- system-chain posture is semantically reviewed, not hash-only auto-updated;
- material commit is reviewer-owned; continuity is separate;
- R2-R6 and every external-effect lane remain parked.

## Verification Commands

```powershell
Set-Location EXTENSIONS/CVF_GUARD_CONTRACT
npx vitest run src/guards/build-authority.guard.test.ts src/index.test.ts src/runtime/agent-execution-runtime.test.ts --pool forks
npm test
npm run check
Set-Location ../..
python governance/compat/check_system_chain_map_freshness.py --enforce
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
python governance/compat/check_governed_file_size.py --enforce
git diff --check
git status --short
```

## Worker Autonomy / No-Question Rule

The current reviewer proceeds autonomously inside this exact local reversible
scope. Escalate only for another path, changed phase model, new subsystem,
dependency/network need, secret/quota use, provider/live, public, deployment,
push, destructive action, or a new independent critical authority defect.

## Review Gate

Before repair, inspect contract/schema, authority, path, malformed-input, test,
system-chain, evidence-packet, range, and commit-plan dependencies together.
After repair, rerun the exact proof once and reject closure on any failure.

## Closure Checklist

- [ ] Amendment authority committed before repair.
- [ ] Worker stash restored with exact five-path status.
- [ ] Dependency matrix completed before repair.
- [ ] Focused, full, typecheck, freshness, worker-return and reviewer gates pass.
- [ ] Completion review accepts the exact material range.
- [ ] One material commit and at most one continuity commit.
- [ ] R2-R6 and all external-effect lanes remain parked.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for any further path, unowned subsystem, phase
model change, dependency/network requirement, failing mandatory proof, or new
critical authority contradiction. Otherwise close as reviewer-accepted bounded.

## Operator Checkpoint

No checkpoint is required inside this exact local reversible Amendment 1
scope. New operator authority is required for any additional path or external
effect and before any R2 dispatch.

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_RFR_R1_BUILD_AUTHORITY_CLOSURE_COMPLETION_2026-08-24.md`

reviewerOwnedClosurePaths: exact repair manifest, completion review, R1-only
roadmap transition, material commit, then separate continuity sync.

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: Amendment 1 extends existing Guard Contract types,
runtime propagation, tests, and one governed source fingerprint. It creates no
durable storage foundation, index family, persistence owner, relocation, split,
or storage migration.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH --max-results 50 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no added control beyond the amendment contract |

## Agent Handoff Contract Control Block

Canonical source: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | external worker followed by current reviewer/closer consolidated repair |
| phase | RFR-R1 Amendment 1 review repair |
| baseHeadFor(phase) | committed Amendment 1 authority HEAD captured before stash restoration |
| changedSetScope(phase) | exact Required Artifact Manifest plus completion and R1 roadmap paths |
| traceScope(phase, actor) | restore, inspect, repair, test, review, commit |
| commitOwner(phase) | current reviewer/closer |
| crossBatchIsolation | R2-R6 and external effects parked |
| nextMoveSurfaces | completion review, material commit, separate continuity sync |

## Dual Agent Surface Matrix

| Surface | Role | Interface | Authority / risk boundary | Evidence | Adapter boundary |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | current orchestrator/reviewer | private repository and local tools | amendment repair/review/commit only | independent reruns and completion review | repository local |
| `EXTERNAL_AGENT_CLI_MCP` | original implementation worker | existing pending diff and blocked return | no new turn, commit, or external action | preserved worker evidence | no runtime adapter invocation |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | orchestrator/dispatcher |
| Provider or surface | private provenance repository |
| Session or invocation | `rfr-r1-amendment-1-dispatch-20260824` |
| Working directory | repository root |
| Command or tool surface | governed reads, Git, checker source inspection, amendment authoring |
| Target paths | paired Amendment 1 baseline and work order |
| Allowed scope source | operator message `next` after reviewer recommendation |
| Before status evidence | clean worktree at HEAD `9df990f8b`; worker five-path diff then preserved in named stash before amendment authoring |
| After status evidence | two amendment authority paths pending dispatch commit |
| Diff evidence | `git diff --name-status` must show only the two amendment authority paths before commit |
| Approval boundary | dispatch authority only |
| Claim boundary | no implementation, runtime/provider/live, public, deploy, push, or production claim |
| Agent type | dispatcher |
| Invocation ID | `rfr-r1-amendment-1-dispatch-20260824` |
| Expected manifest | paired Amendment 1 baseline and work order |
| Actual changed set | paired Amendment 1 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: two new authority files only |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | exact local RFR-R1 dependent repair dispatch |
| claimDisposition | CLAIM_REJECTED until tests and independent review pass |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: reproduced focused/full/typecheck/fast-gate evidence |
| invocationBoundary | local repository and test processes only |
| interceptionBoundary | no provider, network, public, deploy, push, or production action |
| claimLanguage | approved local repair, not accepted closure |
| forbiddenExpansion | compatibility bypass, R2-R6, new subsystem, external effects |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance amendment; public sync remains forbidden.

## Claim Boundary

This work order authorizes only the exact RFR-R1 Amendment 1 repair. It does
not prove implementation, accept the worker return, close R1, release R2-R6,
or authorize provider/live, credentials, deployment, public sync, push, or
production.
