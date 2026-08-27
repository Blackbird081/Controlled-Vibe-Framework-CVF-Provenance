# CVF Agent Work Order - PCIT-R1-BD1 Consolidated Public Blocker Disposition

Memory class: governed-worker-dispatch

Status: APPROVED_FOR_EXECUTION

Batch ID: PCIT-R1-BD1

Dispatch base head: `47260a08d9`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

Worker return path: `docs/reviews/CVF_PCIT_R1_BD1_CONSOLIDATED_PUBLIC_BLOCKER_DISPOSITION_WORKER_RETURN_2026-08-27.md`

## Dispatch Prompt Envelope

Role: one no-commit public test-repair and blocker-disposition worker.

Canonical packet: PCIT roadmap, R1/SA1 review evidence, paired PCIT-R1-BD1
baseline and this work order.

executionBaseHead: capture private and public exact HEADs before edits.

Do-not-misread: this is one same-roadmap bounded packet, not R2, registry
cleanup, validator weakening, product work, commit, push, merge or deploy.

Required first actions: read startup front doors, guard orientation, literal
gotchas, canonical packet, exact hosted evidence and every named owner; prove
both staging areas empty.

Return contract: author only the named private return plus up to three
allowlisted public test changes, then return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Repair the two bounded test-drift families without changing product behavior,
and classify the registry failure using exact counts and owner evidence without
performing destructive or semantics-weakening changes.

## Authority Chain

- User authorization for one consolidated blocker-disposition packet.
- PCIT roadmap and R1/SA1 committed authority.
- R1-SA1 reviewer evidence at private commit `06643ac4b`.
- Continuity checkpoint `1e671171b`, exact-anchor repair `47260a08d9` and paired
  BD1 GC-018 baseline.

## Agent Roles

- Dispatcher: orchestrator/reviewer and scope owner.
- Worker: one no-commit implementation/evidence worker.
- Reviewer/closer: independently accepts changes and owns any later commit.
- Operator: any registry mutation, product repair, external write or successor.

## Required First Reads

Read startup continuity, guard orientation, literal gotchas, PCIT roadmap,
R1-SA1 return/reviewer addendum, paired baseline, this order, the three writable
test files, related product implementations, registry validator/generator/
cleaner and applicable checker sources.

## Pre-Flight Checks

Require private HEAD descended from `47260a08d9`, public branch candidate at
`bbea31745`, expected public remote, clean worktrees and empty staging areas.
Stop if either execution base differs materially or contains unrelated changes.

## Scope / Target / Owner Boundary

Allowed public writes only:

- `EXTENSIONS/CVF_v1.3_IMPLEMENTATION_TOOLKIT/sdk/tests/unit/test_skill_contract.py`
- `EXTENSIONS/CVF_v1.3_IMPLEMENTATION_TOOLKIT/sdk/tests/conftest.py`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/runtime/page.test.tsx`

Allowed private write only: the named PCIT-R1-BD1 worker return.

All product source, workflows, validator, generator, cleaner, registry records,
indexes, lockfiles, package manifests and generated outputs are read-only.

## Write Ownership

Write no more than the four exact paths above. The conftest path may change only
when fixture meaning and assertion disagree. When fixture semantics are already
valid, the worker must keep it unchanged and align the test with the real
contract. Read access does not expand ownership.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| hosted Python failures | run `33042997497`, four failures after 61 passes | exact test owners only | RELEASED_BOUNDED |
| hosted runtime failure | run `33042997505`; focused local file 3/3 passed; same product source previously hosted-green | test synchronization only | RELEASED_BOUNDED |
| registry debt | 335 user records, 62 source skills, 344 validator errors; cleaner deletes all user records | read-only classification with exact evidence | HELD_READ_ONLY |

## Work Plan

1. Capture dual-repository HEAD, branch, status, staging and remotes.
2. Replace the three empty exception pseudo-tests with assertions against the
   real `SkillContract` construction or parsing interface and exact expected
   validation behavior.
3. Resolve the rollback wording assertion/fixture mismatch without weakening
   the intended high-risk rollback guarantee.
4. Make the Vietnamese runtime test wait for snapshot-dependent content before
   synchronous boundary assertions; do not add sleeps, retries or longer global
   timeouts.
5. Reproduce the registry counts and categorize all validator errors by exact
   class. Inspect lifecycle tools but make no registry-side change.
6. Record exactly one registry disposition: `PARK_CANONICAL_OWNER_NOT_PROVEN`
   or `BLOCKED_SCOPE_EXPANSION_REQUIRED`, with the smallest source-backed next
   owner surface. Do not propose a numbered tranche or roadmap.
7. Run focused and package-wide local tests, public-sync preflight and the full
   worker-return gate, then return without commit or external action.

## Execution Plan

Execute the Work Plan as one capped pass. Small test fixes and registry analysis
must remain consolidated; registry write implementation is explicitly outside
this packet.

## Finding-Family Disposition Matrix

| Finding family | Allowed action | Required terminal evidence |
| --- | --- | --- |
| SDK unit tests | bounded test/fixture repair | four formerly failing tests plus package suite pass |
| runtime page test | async assertion repair | repeated focused pass and relevant Web suite result |
| skill registry | read-only reconciliation | exact counts, error categories, lifecycle-tool boundary and one allowed disposition |

## Evidence Requirements

Record exact dual HEAD/status/staging/remotes, before/after failing assertions,
real model interfaces used, focused and package-wide test totals, registry
counts/error categories, dry-run-only lifecycle evidence, public preflight,
exact changed manifest and zero external effects.

## Failure Classification Contract

Use `TEST_DRIFT`, `HOSTED_NONDETERMINISM_CANDIDATE`,
`REGISTRY_LIFECYCLE_AUTHORITY_GAP`, `GENUINE_PRODUCT_DEFECT`, or
`NOT_REPRODUCED_WITH_EVIDENCE`. A genuine product defect or registry write need
is blocking and must remain unchanged.

## Required Artifact Manifest

| Path | Required state |
| --- | --- |
| public SDK unit test | real validation assertions, no placeholder pass body |
| public SDK fixture | unchanged unless semantically necessary |
| public runtime page test | deterministic async synchronization |
| private named worker return | full evidence and registry disposition |

No additional artifact is authorized.

## Acceptance Criteria

- All four named Python failures are corrected through real interface tests.
- No broad exception expectation, empty assertion body or weakened guarantee.
- Runtime test waits on state it later asserts and uses no sleeps/retries.
- Product source and all registry/governance owners remain byte-unchanged.
- Registry output includes exact reconciled counts and no green claim.
- At most three public test paths plus one private return change.
- Both HEADs remain unchanged and both staging areas remain empty.

## Verification Commands

```powershell
git status --short
git -C "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 47260a08d9 --head HEAD
python scripts/check_cvf_public_sync_candidate.py --public-root "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" --authorized-paths-json <exact-authorized-path-file> --expected-remote https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git --baseline-ref origin/main --json
python governance/compat/run_worker_return_fast_gate.py
```

Run the exact focused Python test file and its package-wide unit suite. Run the
exact runtime page test repeatedly and the owning Web suite when locally
feasible. Registry commands must be read-only or dry-run only.

## Stop Conditions

Return blocked on product source, workflow, registry, validator, generator,
cleaner, package/lockfile, dependency, generated output, secret/provider,
Netlify, commit/push/merge/deploy, hosted rerun or additional owner need.

## Review Gate

Reviewer independently inspects assertion strength and async synchronization,
reruns relevant tests, verifies registry owners are unchanged and confirms the
four-path cap before any material commit. Hosted execution remains reviewer-
owned and is not implied by local success.

## Closure Checklist

Two test families complete; registry classified without mutation; no
suppression; no product change; exact manifest; empty staging; no external
effect; independent review pending.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only if all acceptance criteria pass locally.
Otherwise return `BLOCKED_WITH_REASON` at the first named stop condition.

## Operator Checkpoint

No checkpoint inside exact test ownership. Any registry or product mutation,
new owner, public write beyond the test candidates, or successor requires a
fresh operator decision.

## Worker Autonomy / No-Question Rule

Proceed without questions inside exact ownership. Conform packet-format output
to checker source. Stop only for a named authority or scope boundary.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| empty exception contexts cannot pass | pseudo-test defect | `EXTENSIONS/CVF_v1.3_IMPLEMENTATION_TOOLKIT/sdk/tests/unit/test_skill_contract.py` | lines 60, 70, 78 | three `pytest.raises` blocks | SDK unit tests | ACCEPT |
| real validation interface exists | source-backed test target | `EXTENSIONS/CVF_v1.3_IMPLEMENTATION_TOOLKIT/sdk/models/skill_contract.py` | dataclass initialization and `from_dict` | `SkillContract` | SDK model | ACCEPT |
| rollback fixture lacks asserted token | fixture/assertion mismatch | `EXTENSIONS/CVF_v1.3_IMPLEMENTATION_TOOLKIT/sdk/tests/conftest.py` | line 122 | high-risk fixture | SDK fixtures | ACCEPT |
| snapshot content is conditionally rendered | async test race | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/runtime/page.tsx` | lines 209-215 | loading and snapshot branches | runtime page | ACCEPT |
| cleanup deletes all user records | destructive boundary | `governance/skill-library/registry/clean_user_registry.py` | lines 26-40 | cleanup loop | registry lifecycle helper | ACCEPT |

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "PCIT-R1-BD1",
  "requestedProfile": "P4_CRITICAL",
  "classification": {
    "taskKind": "PUBLIC_RELEASE",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PUBLIC",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": ["EXTENSIONS/CVF_v1.3_IMPLEMENTATION_TOOLKIT/sdk/tests", "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/runtime", "docs/baselines", "docs/work_orders", "docs/reviews", "AGENT_HANDOFF_V59_2026-08-11.md"],
  "claims": ["two test-drift families can be repaired without product changes; registry remains read-only"],
  "requiredProof": ["focused tests", "package suites", "registry count reconciliation", "exact manifest", "independent review"],
  "operatorCheckpoints": ["registry mutation", "product defect", "additional owner", "public write"],
  "forbiddenEffects": ["worker commit", "push", "merge", "deploy", "secret read", "provider call", "registry mutation", "product edit"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one no-commit worker, then independent reviewer/closer |
| phase | implementation |
| baseHeadFor(phase) | dispatchBaseHead=`47260a08d9`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | at most three public test paths plus one private return |
| traceScope(phase, actor) | dual-repo state, assertion diffs, tests, registry read-only evidence |
| commitOwner(phase) | reviewer only |
| crossBatchIsolation | clean worktrees; no R2, product, registry or workflow mutation |
| Before status evidence | clean worktree in each repository; both staging areas empty at dispatch |
| nextMoveSurfaces | named worker return then independent review |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | optional; prefer reviewer addendum in the worker return |
| reviewerOwnedClosurePaths | named return, existing PR branch and continuity only after acceptance |
| closureOwner | independent orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_PCIT_R1_BD1_CONSOLIDATED_PUBLIC_BLOCKER_DISPOSITION_WORKER_RETURN_2026-08-27.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

executionBaseHead: worker must record both repositories at start.

Required sections: Purpose; Scope / Methodology; Findings / Position; Risk / Corrective Action; Finding-Family Disposition Matrix; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; Claim Boundary; git status --short; Changed Files; Command Evidence; No-Commit Statement.

Conditional sections must contain evidence or `N/A with reason`: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package.

## Foundation Storage Layout Block

N/A with reason: this packet creates no foundation, index, registry or generated
aggregate and explicitly keeps registry storage read-only.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | NOT_TRIGGERED with reason: no outside corpus is absorbed |
| Matching local-view guard | `governance/compat/check_public_export_disposition.py` |
| Owner surface | three named public test paths |
| Disposition | RECONCILED_DESIGN_INPUT_ONLY |
| Claim boundary | CI receipts inform the bounded repair but create no new authority |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| SDK unit test | repair real validation assertions |
| SDK fixture | preserve unless exact semantics require correction |
| runtime page test | repair async synchronization |
| named worker return | record full proof and registry disposition |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`public-sync`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_authoring.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | dispatch envelope, source columns, fulfillment manifest, handoff fields, return profile and public disposition |
| gateRunPurpose | confirm bounded authority before worker execution |
| claimBoundary | conformance does not prove tests, registry resolution or hosted success |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id PCIT-R1-BD1 --title "Consolidated Public Blocker Disposition" --date 2026-08-27 --base 47260a08d9 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | public-sync plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact test ownership, registry hold and proof requirements |
| checkerReadAheadConfirmation | sources listed in Checker Source Read-Ahead Block |
| docOnlyNewFields | finding-family disposition matrix; registry lifecycle hold |
| claimBoundary | dispatch authoring only |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/reviewer |
| Provider or surface | private provenance and sibling public-sync source |
| Session or invocation | PCIT-R1-BD1 dispatch, 2026-08-27 |
| Working directory | private root; public sibling read-only during dispatch |
| Command or tool surface | Git reads, source reads, scaffold and governed patch |
| Target paths | paired BD1 baseline and work order |
| Allowed scope source | user authorization after R1-SA1 review |
| Before status evidence | clean worktree at private HEAD `47260a08d9` and public HEAD `bbea31745`; both staging areas empty |
| After status evidence | paired authority pending dispatch commit only |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch only; no public implementation write |
| Claim boundary | one bounded same-roadmap packet |
| Agent type | dispatcher |
| Invocation ID | `pcit-r1-bd1-dispatch-2026-08-27` |
| Expected manifest | paired baseline and work order |
| Actual changed set | must match expected manifest before commit |
| Manifest delta | must be NONE |
| Deletion or rename disposition | N/A with reason: authority artifacts only |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | no-commit bounded test repair plus read-only registry disposition |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: runs `33042997497` and `33042997505` plus Git evidence |
| actionEvidence | ACTION_EVIDENCE_PRESENT: later local test-only diffs and command receipts |
| invocationBoundary | hosted receipts are read-only; worker actions remain local and reversible |
| interceptionBoundary | no runtime/provider/secret interception |
| claimLanguage | candidate pending independent review |
| forbiddenExpansion | product, registry, workflow, dependency, external effect or successor |

## Current Runtime Freshness Verification

N/A with reason: hosted runs are bounded failure receipts, not current runtime
readiness proof. The worker must not call providers, trigger hosted jobs or make
deployment claims.

## Public/Provenance Boundary

Worker changes remain local in the sibling public-sync clone. Reviewer alone
may commit/push the PR branch and request hosted proof. Public main and branch
protection must not be bypassed.

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: no accepted BD1 candidate or exact-SHA hosted proof exists, and the
registry finding must remain truthfully blocking until separately authorized.

## Claim Boundary

This work order authorizes at most three public test-file edits and one private
return. It authorizes no product, registry, governance, dependency or external
effect and makes no claim that public CI or PR `#4` is green.
