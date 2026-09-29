# CVF Agent Work Order - PSRR-R1 Public Skill Registry Atomic Reconciliation

Memory class: governed-worker-dispatch

Status: APPROVED_FOR_EXECUTION

Batch ID: PSRR-R1

Dispatch base head: `35be0dbe5`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

Worker return path: `docs/reviews/CVF_PSRR_R1_PUBLIC_SKILL_REGISTRY_ATOMIC_RECONCILIATION_WORKER_RETURN_2026-08-27.md`

## Dispatch Prompt Envelope

Role: one no-commit public generated-registry implementation worker.

Canonical packet: PSRR roadmap, paired GC-018 baseline and this work order.

executionBaseHead: capture private and public exact HEADs before edits.

Do-not-misread: this is one generated-owner reconciliation tranche, not
semantic skill review, arbitrary cleanup, validator weakening, merge or R2.

Required first actions: read startup continuity, guard orientation, literal
gotchas, canonical packet, generator/validator/cleaner, public workflow and
every named checker; prove both staging areas empty.

Return contract: author only the named private return plus allowlisted public
generator/test/generated-family changes, then return `COMPLETE_PENDING_REVIEW`
or `BLOCKED_WITH_REASON` without commit or staging.

## Purpose

Make the current generator safely reconcile its exact desired user-registry
manifest, prove failure atomicity and idempotence in temporary directories,
then regenerate the public registry to exact 62-source parity.

## Authority Chain

- Operator instruction selecting the next high-value roadmap.
- PCIT-R1-BD1 closure at private `8480ed51f` and public `86b1e728`.
- PSRR roadmap and paired PSRR-R1 GC-018 baseline.
- Active continuity at dispatch base `35be0dbe5`.

## Agent Roles

- Dispatcher: orchestrator/reviewer and scope owner.
- Worker: one no-commit implementation/evidence worker.
- Reviewer/closer: independently reviews, repairs within ownership and owns
  any later commit, push or hosted proof.
- Operator: any scope expansion, PR merge, deployment or successor.

## Required First Reads

Read `CVF_SESSION_MEMORY.md`, bootstrap model, active handoff, guard
orientation, literal gotchas, PSRR roadmap/baseline/order, the public generator,
cleaner, validator, workflow, generated index, two representative existing
records, two current source skills and applicable checker sources.

## Pre-Flight Checks

Require private HEAD descended from `35be0dbe5`, public branch
`pcit-r1-public-ci-truthfulness` at `86b1e728`, expected public remote, clean
worktrees and empty staging. Record current counts and read-only desired-name
manifest before edits. Stop on unrelated drift.

## Scope / Target / Owner Boundary

Allowed public writes:

- `governance/skill-library/registry/generate_user_skills.py`
- `governance/skill-library/registry/test_generate_user_skills.py`
- `governance/skill-library/registry/user-skills/INDEX.md`
- `governance/skill-library/registry/user-skills/USR-*.gov.md`

Allowed private write: the named PSRR-R1 worker return only.

Cleaner, validator, agent registry, source skills, workflow, mapping records,
quarantine, external sources, dependencies, package files and all unrelated
paths are read-only.

## Write Ownership

The generated-family wildcard authorizes only deterministic generator output.
Deletion is limited to existing `USR-*.gov.md` filenames absent from the fully
computed desired manifest. Preserve any unrelated file placed in the output
directory. Never call the legacy cleaner in mutating mode.

## Large-Scope Authorization

The expected public diff may include 329 generated deletions, 56 generated
additions, six generated replacements and one index replacement, plus the
generator and focused test. This count is authorized only as one generated
owner family and only after isolated atomicity tests pass. No archive cleanup,
source deletion or other path family is authorized.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| canonical generator | existing owner reads source library and writes record/index projections | add exact reconciliation contract | RELEASED_BOUNDED |
| destructive cleaner | all-record deletion loop | never invoke mutating mode | HELD_READ_ONLY |
| validator | exact record/source/link/index contract | must pass unchanged | RELEASED_READ_ONLY_PROOF |
| hosted CI | only registry family red at exact SHA | reviewer triggers after accepted commit | HELD_FOR_REVIEWER |

## Work Plan

1. Capture dual-repository HEAD, branch, status, staging, remotes and counts.
2. Refactor generator into import-safe functions that render every desired
   record and index in memory before target mutation.
3. Add `--output-dir`, `--dry-run` and `--check` interfaces. Dry-run/check must
   never write. Invalid output targets or source-render failures must fail
   before mutation.
4. Apply only exact add/update/delete operations. Stale deletion may match
   only `USR-*.gov.md`; unrelated files survive. Use temporary files and
   replacement so a partial record write is not exposed.
5. Add focused temporary-directory tests for fresh generation, stale cleanup,
   unrelated-file preservation, dry-run/check no-write behavior, render failure
   byte-equivalence, deterministic ordering and second-run idempotence.
6. Run focused tests before touching the real generated directory.
7. Run dry-run on the real public registry and reconcile its reported counts
   against the 6 retained / 329 stale / 56 new name baseline. Investigate any
   contradiction before apply.
8. Apply once, validate exactly 62 records plus index, rerun apply to prove no
   diff, run check mode, unchanged validator and public-sync preflight.
9. Author the worker return and leave both HEADs unchanged, staging empty.

## Execution Plan

Execute as one capped pass. Test the mutation boundary in temporary output
first; real generated outputs are the final local step. Do not split analysis,
tooling and generation into numbered successor tranches.

## Required Artifact Manifest

| Artifact | Required state |
| --- | --- |
| public generator | safe render-plan-apply lifecycle with output-dir, dry-run and check |
| public focused test | adversarial atomicity, boundary and idempotence proof |
| public user registry | exact deterministic 62-record projection plus index |
| private worker return | full before/after, deletion and command evidence |

No additional artifact is authorized.

## Acceptance Criteria

- Dry-run/check leave target bytes and names unchanged.
- Any pre-apply render failure leaves target byte-equivalent.
- Only manifest-stale user records are deleted; unrelated files survive.
- Exact 62/62 source-record parity, valid source links and correct index.
- Focused tests, unchanged validator and public-sync preflight pass.
- Second apply yields no Git diff; check mode exits zero.
- No validator/workflow/source-skill/dependency change or CI suppression.
- Worker leaves both HEADs unchanged and staging empty.

## Evidence Requirements

Record both execution HEADs, branches, remotes, worktree and staging status;
the exact desired/current/add/update/delete manifests; before/after hashes for
failure-atomicity cases; focused test totals; dry-run and check outputs;
validator result; first-apply and second-apply diffs; public-sync preflight;
exact changed/deleted paths; and zero external effects.

## Verification Commands

```powershell
git status --short
git -C "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 35be0dbe5 --head HEAD
python governance/skill-library/registry/test_generate_user_skills.py
python governance/skill-library/registry/generate_user_skills.py --dry-run
python governance/skill-library/registry/generate_user_skills.py --check
python governance/skill-library/registry/validate_registry.py
python scripts/check_cvf_public_sync_candidate.py --public-root "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" --authorized-paths-json <exact-authorized-path-file> --expected-remote https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git --baseline-ref origin/main --json
python governance/compat/run_worker_return_fast_gate.py
```

The worker may use the test runner selected by the focused test file. Run the
full unchanged Documentation & Testing command family locally where feasible;
hosted execution remains reviewer-owned.

## Stop Conditions

Return blocked on source-skill mutation, validator or workflow change,
arbitrary deletion, any non-user registry owner, dependency change, secret or
provider need, Netlify, commit/push/merge/deploy, hosted rerun or additional
tranche need.

## Review Gate

Reviewer independently inspects the deletion manifest, generator failure
ordering and tests; reruns focused proof, validator and idempotence; confirms
every changed public path matches ownership before commit. Exact-SHA hosted
proof is mandatory before any merge recommendation.

## Closure Checklist

Atomic generator contract; focused adversarial tests; exact 62-record output;
validator pass; idempotence; exact deletion manifest; no suppression; empty
staging; independent review pending.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only if all local criteria pass. Otherwise
return `BLOCKED_WITH_REASON` at the first named stop condition.

## Operator Checkpoint

No checkpoint inside exact ownership. PR merge, deployment, source-skill or
validator changes, additional owner or successor require a fresh decision.

## Worker Autonomy / No-Question Rule

Proceed without questions for safe actions inside exact ownership. Repair
allowed-scope test or packet-format failures and rerun them. Stop only when a
named boundary would be crossed.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| generator enumerates current source skills | source owner | `governance/skill-library/registry/generate_user_skills.py` | lines 12-14, 147-153 | `SKILL_LIBRARY_PATH`; `OUTPUT_PATH`; `rglob` | generator | ACCEPT |
| generator writes records and index but omits stale deletion | lifecycle gap | `governance/skill-library/registry/generate_user_skills.py` | lines 79-199 | `generate_gov_file`; index write | generator | ACCEPT |
| cleaner mutation deletes all records and index | destructive boundary | `governance/skill-library/registry/clean_user_registry.py` | lines 17-41 | `main`; `unlink` | legacy cleaner | ACCEPT |
| validator requires exact parity, sections, links and index | acceptance owner | `governance/skill-library/registry/validate_registry.py` | lines 42-176 | `validate_user_skill`; `validate_index`; `main` | validator | ACCEPT |
| required status includes registry validation | hosted release boundary | `.github/workflows/documentation-testing.yml` | registry-validate and status-check jobs | `Governance Registry Validation`; `needs` | public workflow | ACCEPT |

## Current Runtime Freshness Verification

N/A with reason: this is deterministic local generation and hosted-CI repair;
no runtime/provider capability or production readiness is claimed.

## Negative Search And Collision Discipline

PSRR artifact paths and token were absent at dispatch. Search across governed
artifact and continuity roots found no competing PSRR authority. Existing
generator/test names are treated as owner/collision inputs, not duplicates.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "PSRR-R1",
  "requestedProfile": "P4_CRITICAL",
  "classification": {
    "taskKind": "PUBLIC_RELEASE",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PUBLIC",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": ["governance/skill-library/registry", "docs/roadmaps", "docs/baselines", "docs/work_orders", "docs/reviews", "AGENT_HANDOFF_V59_2026-08-11.md"],
  "claims": ["one existing generator owner can reconcile its exact generated family without weakening validation"],
  "requiredProof": ["focused atomicity tests", "exact generated manifest", "validator pass", "idempotence", "public-sync preflight", "independent review"],
  "operatorCheckpoints": ["validator change", "source-skill mutation", "additional owner", "PR merge", "deployment"],
  "forbiddenEffects": ["worker commit", "push", "merge", "deploy", "secret read", "provider call", "workflow weakening", "arbitrary deletion", "automatic successor"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | generator and generated user records | local generated-output reconciliation only | focused tests and validator | N/A with reason: no agent adapter behavior | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | public Markdown records | read-only artifact consumption only | public paths after reviewer export | no CLI/MCP adapter in scope | `DEFERRED_WITH_REASON` |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one no-commit worker, then independent reviewer/closer |
| phase | implementation |
| baseHeadFor(phase) | dispatchBaseHead=`35be0dbe5`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | one public generator, one test, one generated family, one private return |
| traceScope(phase, actor) | dual state, planned/applied manifest, tests, validator and idempotence |
| commitOwner(phase) | reviewer only |
| crossBatchIsolation | clean worktrees; no PCIT-R2, PSRR-R2 or unrelated lane |
| Before status evidence | clean worktree in both repositories; `git status --short` empty and both staging areas empty at dispatch |
| nextMoveSurfaces | named worker return then independent review |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | optional; prefer reviewer addendum in the worker return |
| reviewerOwnedClosurePaths | named return, accepted public branch and continuity after acceptance |
| closureOwner | independent orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing the return, read checker sources for review quality, trace,
delta, rescan, generated-output, public disposition and no-commit evidence.
List real section names without duplicating heading syntax in prose.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| public generator | implement safe reconciliation and three no-write interfaces |
| public focused test | prove atomicity, boundaries, determinism and idempotence |
| generated user registry | reconcile to exact 62-record manifest plus index |
| named private worker return | record full evidence and exact changed/deleted manifest |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_PSRR_R1_PUBLIC_SKILL_REGISTRY_ATOMIC_RECONCILIATION_WORKER_RETURN_2026-08-27.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

executionBaseHead: worker records both repositories at start.

Required section names: Purpose; Scope / Methodology; Findings / Position; Risk
/ Corrective Action; Checker Source Read-Ahead Block; Agent Operation Trace
Block; Delta Execution Claim Boundary Control Block; Public Export
Disposition; Claim Boundary; git status --short; Changed Files; Command
Evidence; No-Commit Statement.

Conditional sections require evidence or N/A with reason: External Knowledge
Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report
Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block;
Machine Closure Package.

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: N/A with reason: no ASSF package lifecycle state changes.

Target lifecycle state: unchanged.

Prior phase evidence: legacy user projection registry only.

Next forbidden skip: no promotion, activation, loading or runtime eligibility.

Runtime/provider proof: N/A with reason: local generation only.

Claim boundary: exact user-registry projection parity only.

## Foundation Storage Layout Block

Existing storage owner remains `governance/skill-library/registry/user-skills`.
No new foundation, parallel index, archive or aggregate is created. Source
files remain under the current end-user skill library; the generated index
stays in its existing owner directory.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | NOT_TRIGGERED with reason: no outside repository or external knowledge intake |
| Matching local-view guard | `governance/compat/check_public_export_disposition.py` |
| Owner surface | public generator and generated user registry |
| Disposition | RECONCILED_DESIGN_INPUT_ONLY |
| Claim boundary | no external material is promoted into CVF authority |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`public-sync`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_authoring.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_package_skill_productionization_pipeline.py` |
| literalTokensReviewed | dispatch envelope, source columns, fulfillment manifest, handoff fields, return profile, package block and public disposition |
| gateRunPurpose | confirm exact authority before worker execution |
| claimBoundary | checker conformance does not prove safe reconciliation or hosted success |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id PSRR-R1 --title "Public Skill Registry Atomic Reconciliation" --date 2026-08-27 --base 35be0dbe5 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | public-sync, package-skill trigger and no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact generator lifecycle, deletion boundary and proof commands |
| checkerReadAheadConfirmation | sources listed in Checker Source Read-Ahead Block |
| docOnlyNewFields | atomic reconciliation and large generated-family authorization |
| claimBoundary | dispatch authoring only |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/reviewer |
| Provider or surface | private provenance and sibling public-sync source |
| Session or invocation | PSRR-R1 dispatch, 2026-08-27 |
| Working directory | private root; public sibling read-only during dispatch |
| Command or tool surface | Git reads, source reads, resolver, scaffold and governed patch |
| Target paths | PSRR roadmap, baseline and work order; PCIT terminal status correction |
| Allowed scope source | operator request for next roadmap plus standing high-value-finding authority |
| Before status evidence | clean worktree at private HEAD `35be0dbe5` and public HEAD `86b1e728`; `git status --short` empty and both staging areas empty |
| After status evidence | four private authority paths pending dispatch commit only |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch only; no public implementation write |
| Claim boundary | one bounded generated-owner packet |
| Agent type | dispatcher |
| Invocation ID | `psrr-r1-dispatch-2026-08-27` |
| Expected manifest | PCIT roadmap status correction plus PSRR roadmap, baseline and work order |
| Actual changed set | must match expected manifest before commit |
| Manifest delta | must be NONE |
| Deletion or rename disposition | N/A with reason: authority artifacts only |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | no-commit generated-registry reconciliation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: exact hosted run `33047367938` plus local manifest evidence |
| actionEvidence | ACTION_EVIDENCE_PRESENT: later local generator/test/generated diffs and command receipts |
| invocationBoundary | hosted receipt is read-only; worker actions local and Git-reversible |
| interceptionBoundary | no runtime/provider/secret interception |
| claimLanguage | candidate pending independent review |
| forbiddenExpansion | source skill, validator, workflow, other registry, dependency, external effect or successor |

## Public/Provenance Boundary

Worker changes remain local in the sibling public-sync clone. Reviewer alone
may commit/push the branch and request hosted proof. Public main and branch
protection must not be bypassed.

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: no accepted PSRR candidate or exact-SHA hosted proof exists.

## Claim Boundary

This order authorizes one public generator, one focused test, its exact
generated user-registry family and one private return. It authorizes no
validator weakening, source-skill mutation, arbitrary deletion, package
activation, commit, push, merge, deploy, secret/provider action or successor.
