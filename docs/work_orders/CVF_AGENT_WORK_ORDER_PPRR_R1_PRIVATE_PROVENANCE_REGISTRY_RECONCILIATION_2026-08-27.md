# CVF Agent Work Order - PPRR-R1 Private Provenance Registry Reconciliation

Memory class: governed-worker-dispatch

Status: APPROVED_FOR_EXECUTION

Batch ID: PPRR-R1

Dispatch base head: `91fff28bb72235489aafe95883385efe761962de`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

Worker return path: `docs/reviews/CVF_PPRR_R1_PRIVATE_PROVENANCE_REGISTRY_RECONCILIATION_WORKER_RETURN_2026-08-27.md`

## Dispatch Prompt Envelope

Role: one no-commit private generated-registry reconciliation worker.

Canonical packet: PPRR roadmap, paired GC-018 baseline and this work order.

executionBaseHead: capture private and public exact HEADs before edits.

Do-not-misread: import one already accepted generated owner family; do not
reanalyze stale-record semantics, redesign the generator, mutate public or
open PPRR-R2.

Required first actions: read startup continuity, guard orientation, literal
gotchas, canonical packet, PSRR/AGTR reviewer evidence, both generators and
tests, unchanged validator, cleaner and applicable checker sources; prove both
repositories and staging areas clean.

Return contract: author only the named return plus allowlisted private owner
family changes, then return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON` without commit or staging.

## Purpose

Bring the accepted public generated user-skill registry owner into private
provenance, delete only manifest-stale generated records, and restore the
unchanged private registry validator to green.

## Authority Chain

- Operator instruction to continue with the highest-value parked defect.
- Closed PSRR-R1 accepted generated-owner evidence.
- Closed AGTR-R1 exact-SHA full registry proof.
- PPRR roadmap, GC-018 baseline and this order at dispatch base.

## Agent Roles

- Dispatcher: orchestrator/reviewer and scope owner.
- Worker: one no-commit implementation/evidence worker.
- Reviewer/closer: independently inspects manifests, semantics boundary and
  tests, then owns any private commit and closure.
- Operator: any scope expansion, public write, merge, deployment or successor.

## Required First Reads

Read the active startup surfaces, guard orientation, literal gotchas, PPRR
packet, PSRR worker-return reviewer addendum, AGTR completion, private and
public generator/test/index, representative desired and stale records, the
unchanged validator and relevant worker-return checkers.

## Pre-Flight Checks

Require private HEAD descended from dispatch base, public branch
`pcit-r1-public-ci-truthfulness` at exact HEAD
`af957e279a8118b152d957a29f5731c6304a86bf`, correct public remote, clean
worktrees and empty staging. Recompute counts and source-name manifest before
editing; stop on contradiction.

## Scope / Target / Owner Boundary

Allowed private writes:

- `governance/skill-library/registry/generate_user_skills.py`
- `governance/skill-library/registry/test_generate_user_skills.py`
- `governance/skill-library/registry/user-skills/INDEX.md`
- `governance/skill-library/registry/user-skills/USR-*.gov.md`
- the named private worker return

Public repository paths are read-only. Private source skills, agent records,
validator, cleaner, workflows, maps, product, dependencies, continuity and all
unrelated paths are read-only.

## Write Ownership

The wildcard covers one deterministic generated family only. Delete an
existing private `USR-*.gov.md` file only when its basename is absent from the
accepted public exact-commit manifest. Preserve unrelated files in the output
directory. Never invoke the cleaner in mutating mode.

## Large-Scope Authorization

The expected private diff may include 329 generated deletions, 56 additions,
six replacements, one index replacement, one generator replacement, one new
focused test and one worker return. This is one atomic owner family, not
authority for general cleanup or deletion.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| accepted public owner | exact clean public HEAD and PSRR review | all imported owner files must hash-match | RELEASED_BOUNDED |
| private/public source names | same 62-path digest | mismatch stops before mutation | RELEASED_READ_ONLY_PROOF |
| unchanged validator | public PASS, private user debt only | private full PASS required after import | RELEASED_READ_ONLY_PROOF |
| public write or hosted rerun | no new public bytes | never perform | HELD |

## Work Plan

1. Capture dual repository state, remotes, counts and source-name digest.
2. Enumerate from public exact HEAD the generator, test, index and 62 records;
   compute an expected 65-file SHA-256 manifest before private mutation.
3. Compute the exact private add/update/delete set and reconcile it against
   the expected 56 add, six replace and 329 stale-record delete baseline.
4. Copy exact accepted bytes into private and delete only named stale records.
5. Prove 65 of 65 hashes match the accepted public exact commit.
6. Run focused tests, generator check, unchanged full validator, one apply for
   idempotence, diff hygiene and worker-return fast gate.
7. Author the return and leave both HEADs unchanged and staging empty.

## Execution Plan

Execute one capped pass. Do not split manifest analysis, import, validation or
return authoring into additional tranches. If exact parity cannot be achieved
inside the allowlist, return blocked.

## Required Artifact Manifest

| Artifact | Required state |
| --- | --- |
| private generator | byte-identical to accepted public exact commit |
| private focused test | byte-identical to accepted public exact commit |
| private user registry | exact 62-record and index parity with accepted public exact commit |
| private worker return | full manifest, hash, command and no-commit evidence |

No additional artifact is authorized.

## Acceptance Criteria

- Source-name manifests remain identical and contain 62 paths.
- Expected 65 owner files match public exact-commit SHA-256 bytes.
- Private generated record count is 62 and no stale `USR` remains.
- Focused generator tests, check mode, idempotence and unchanged full validator
  pass.
- Public repository remains byte- and status-unchanged.
- No validator, cleaner, source, AGT, workflow, product or dependency changes.
- Both HEADs unchanged and both staging areas empty.

## Evidence Requirements

Record dual HEADs, branch, remotes, worktree and staging; exact source-name,
desired and stale manifests; expected/actual add-update-delete counts; 65 hash
pairs; focused test and validator totals; generator check and idempotence;
exact changed paths; diff hygiene; zero external effects and no-commit proof.

## Verification Commands

```powershell
git rev-parse HEAD
git status --short
git diff --cached --name-only
git -C "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" rev-parse HEAD
git -C "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" status --short
python governance/skill-library/registry/test_generate_user_skills.py
python governance/skill-library/registry/generate_user_skills.py --check
python governance/skill-library/registry/validate_registry.py
python governance/compat/run_worker_return_fast_gate.py
git diff --check
```

After the imported generator is present, one normal apply is permitted only
to prove zero add/update/delete and byte-equivalent idempotence.

## Stop Conditions

Stop on source-name mismatch, public HEAD or worktree drift, an expected hash
mismatch, any non-generated owner need, validator/cleaner/source/AGT/workflow
change, deletion outside the exact stale manifest, secret or provider need,
commit/push/merge/deploy request, or any second tranche. Do not propose R2.

## Review Gate

Reviewer must independently reconstruct the public exact-commit manifest,
inspect the deletion set, sample retained/add/delete boundaries, rerun all
checks and verify empty staging before committing private material.

## Closure Checklist

- [ ] dual repository preflight and exact anchors recorded
- [ ] 62-path source-name manifest MATCH
- [ ] exact 65-file accepted-owner hash manifest MATCH
- [ ] private full unchanged validator PASS
- [ ] focused tests, check and idempotence PASS
- [ ] exact changed/deleted manifest inside ownership
- [ ] worker return fast gate PASS
- [ ] no commit, staging, public mutation, provider, secret, merge or deploy

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every acceptance item passes.
Return `BLOCKED_WITH_REASON` at the first stop condition. No worker result
grants commit, public, merge, deploy or successor authority.

## Operator Checkpoint

No checkpoint inside exact ownership. Additional owner, public mutation,
semantic decision, PPRR-R2, merge or deployment requires fresh authorization.

## Worker Autonomy / No-Question Rule

Proceed without questions for exact manifest and byte-copy work inside scope.
Repair in-scope test or return-format defects and rerun. Stop instead of
guessing when evidence conflicts or ownership would widen.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| private validator owns exact user/source/link/index acceptance | code contract | `governance/skill-library/registry/validate_registry.py` | user validation, index validation and main count checks | `validate_user_skill`; `validate_index`; `main` | registry validator | ACCEPT |
| accepted generator lifecycle and exact public family | governed review evidence | `docs/reviews/CVF_PSRR_R1_PUBLIC_SKILL_REGISTRY_ATOMIC_RECONCILIATION_WORKER_RETURN_2026-08-27.md` | Independent Reviewer Addendum and Command Evidence | public reconciliation commits through `d27d3db2` | PSRR reviewer closure | ACCEPT |
| public full registry proof is green | governed completion evidence | `docs/reviews/CVF_AGTR_R1_AGENT_SKILL_REGISTRY_STRUCTURAL_RECONCILIATION_COMPLETION_2026-08-27.md` | Material And Hosted Evidence | public exact SHA `af957e27` | AGTR reviewer closure | ACCEPT |
| source library owner is unchanged and contains current inputs | repository source | `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md` | end-user skill-library root and current `*.skill.md` tree | 62-path manifest | end-user skill library | ACCEPT |

## Current Runtime Freshness Verification

N/A with reason: no runtime/provider claim. Repository freshness is fixed to
the captured private and public exact commits dated 2026-08-27.

## Negative Search And Collision Discipline

PPRR token and title were absent before dispatch. No second private registry
owner was found. The accepted public generator is the comparison owner; the
private legacy cleaner remains read-only and is not a fallback.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "PPRR-R1",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "STATEFUL_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": ["governance/skill-library/registry", "docs/reviews", "docs/roadmaps", "docs/baselines", "docs/work_orders", "AGENT_HANDOFF_V59_2026-08-11.md", "CVF_SESSION"],
  "claims": ["accepted public generated-owner bytes can restore private provenance parity without semantic or policy change"],
  "requiredProof": ["source-name manifest match", "65-file byte identity", "focused generator tests", "full unchanged validator pass", "idempotence", "independent review"],
  "operatorCheckpoints": ["source mismatch", "additional owner", "public mutation", "semantic decision", "merge", "deployment"],
  "forbiddenEffects": ["worker commit", "push", "merge", "deploy", "secret read", "provider call", "validator weakening", "source mutation", "arbitrary deletion", "automatic successor"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intakeClass | existing private generated-owner defect |
| selectedRole | no-commit reconciliation worker |
| reviewerRole | independent reviewer/closer |
| reason | exact accepted source family with large but deterministic Git-reversible diff |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order binding | Proof |
| --- | --- | --- |
| one tranche only | one atomic owner family and one return | exact changed manifest |
| reuse accepted evidence | public exact-commit 65-file manifest | pairwise hashes |
| restore private truth | unchanged validator read-only | full PASS |
| no public effect | public repository read-only | before/after status and HEAD |

## Legacy Absorption Coverage Index Disposition

| Field | Value |
| --- | --- |
| disposition | NOT_APPLICABLE_WITH_REASON |
| reason | no legacy absorption or workflow-chain change; deterministic registry owner synchronization only |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | private generated user registry | static provenance parity only | hashes, tests and validator | N/A with reason: no adapter behavior | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | unchanged public registry | no external surface mutation | public exact commit remains unchanged | no CLI/MCP activation | `DEFERRED_WITH_REASON` |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one no-commit worker, then independent reviewer/closer |
| phase | implementation |
| baseHeadFor(phase) | dispatchBaseHead=`91fff28bb`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | one private generated owner family plus named return; public read-only |
| traceScope(phase, actor) | dual state, source/desired/stale manifests, hashes, tests, validator and idempotence |
| commitOwner(phase) | reviewer only |
| crossBatchIsolation | clean repositories; no AGTR-R2, PPRR-R2 or unrelated lane |
| Before status evidence | private and public clean worktree evidence: `git status --short` empty; both staging areas empty; exact HEADs captured |
| nextMoveSurfaces | named worker return then independent review |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | optional; prefer reviewer addendum in the named worker return |
| reviewerOwnedClosurePaths | accepted private owner family, named return, roadmap closure and later continuity |
| closureOwner | independent orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing the return, read worker-return quality, epistemic process,
agent operation trace, delta claim boundary, corpus completeness, public
disposition, encoding and external-provider-skill trace checkers. Use actual
section names and literal labels.

## Work-Order Fulfillment Manifest

| Requirement | Evidence location |
| --- | --- |
| accepted owner import | 65-file hash ledger in return |
| exact deletion boundary | stale manifest and final changed-set reconciliation |
| private validation | focused tests, check, idempotence and full validator output |
| no external effect | public HEAD/status and zero provider/secret evidence |
| no-commit compliance | private/public HEAD and staging evidence |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_PPRR_R1_PRIVATE_PROVENANCE_REGISTRY_RECONCILIATION_WORKER_RETURN_2026-08-27.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required real sections and evidence terms: Purpose; Target / Source; Scope /
Methodology; Findings / Position; Risk / Corrective Action; Checker Source
Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary
Control Block; Public Export Disposition; Claim Boundary; status; memory class;
executionBaseHead; git status --short; Changed Files; Command Evidence;
No-Commit Statement; Evidence Comparison; Contradiction or Gap Disposition;
Claim Update; and Worker Experience Retrospective.

Conditional sections must be present with evidence or N/A with reason:
External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus
Completeness And Report Integrity; Finding-To-Governance Learning Disposition;
Epistemic Process Block; Machine Closure Package; and External Provider Skill
Usage Trace.

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: N/A with reason: generated registry parity only.

Target lifecycle state: unchanged.

Prior phase evidence: accepted PSRR owner.

Next forbidden skip: no promotion, activation, loading or eligibility.

Runtime/provider proof: N/A with reason: no runtime/provider behavior.

Claim boundary: private generated-owner parity only.

## Foundation Storage Layout Block

N/A with reason: no foundation storage, durable state, receipt store or adapter
surface changes. Existing registry paths remain their sole owner.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | public/simple cvf vocabulary |
| Chain map route | NOT_APPLICABLE_WITH_REASON: same-project exact-byte provenance reconciliation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; no external intake |
| Owner surface | generated user-skill registry |
| Disposition | LOCAL_ONLY_NO_EXTERNAL_INTAKE |
| Claim boundary | no outside material or upstream-equivalence claim |

## Rescan Intelligence Hardening

- N/A with reason: fixed exact manifests are compared, not rescanned or
  refreshed from an external corpus.
- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044.

Applicable controls: source verification, exact manifests, large-scope
authorization, no-commit mode, checker read-ahead and reviewer-owned closure.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_external_provider_skill_usage_trace.py` |
| literalTokensReviewed | worker status, evidence comparison, operation trace labels, no-commit statement, private-only public disposition and retrospective |
| gateRunPurpose | confirm with evidence that the large generated-family return will be independently reviewable; not first discovery |
| claimBoundary | packet conformance does not prove byte parity or safe deletion |

## Scaffold Provenance Block

| Field | Evidence |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind implementation --batch-id PPRR-R1 --title "Private Provenance Registry Reconciliation" --date 2026-08-27 --base 91fff28bb --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | private P3 generated-owner no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact 65-file public source manifest, private stale deletion boundary and one-tranche cap |
| checkerReadAheadConfirmation | sources listed in Checker Source Read-Ahead Block |
| docOnlyNewFields | accepted-owner import ledger and private-only parity proof |
| claimBoundary | dispatch authoring only; no implementation claim |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | no-commit reconciliation worker |
| Provider or surface | private local repository plus read-only public sibling |
| Session or invocation | PPRR-R1 worker execution |
| Working directory | private root and sibling public root captured by worker |
| Command or tool surface | local file comparison/editing, Git read-only checks, Python tests and validators |
| Target paths | private generator, test, generated USR family, index and named return |
| Allowed scope source | committed PPRR roadmap, baseline and work order |
| Before status evidence | private and public clean worktree evidence: `git status --short` empty; both staging areas empty; exact HEADs captured |
| After status evidence | exact private pending manifest; public unchanged; empty staging |
| Diff evidence | private `git diff --name-status`, public status, hashes and `git diff --check` |
| Approval boundary | worker must not commit, push, merge or deploy |
| Claim boundary | candidate pending independent review |
| Agent type | implementation worker |
| Invocation ID | worker-generated stable session identifier |
| Expected manifest | private 65 owner files plus named return, with manifest-stale USR deletions |
| Actual changed set | worker-recorded exact paths |
| Manifest delta | MATCH or explicit BLOCKED discrepancy |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | private no-commit generated-owner reconciliation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: PSRR and AGTR reviewer evidence plus exact public commit |
| actionEvidence | ACTION_EVIDENCE_PRESENT: worker hashes, diffs, tests, validator and idempotence |
| invocationBoundary | local Git-reversible file work; public comparison is read-only |
| interceptionBoundary | no runtime, provider, secret, network or credential interception |
| claimLanguage | private parity candidate pending independent review |
| forbiddenExpansion | semantic rewrite, arbitrary deletion, public mutation, validator/source/workflow change or successor |

rawMemoryReleased=false

## Public/Provenance Boundary

The public exact commit is a read-only accepted comparison source. PPRR-R1
changes private provenance only; worker performs no public or network action.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: all PPRR changes are private provenance synchronization. Public-sync
already contains the accepted bytes and must remain unchanged.

## Commit Mode And Base-Anchor Lifecycle

Worker mode is `WORKER_MUST_NOT_COMMIT`. Dispatch base is the exact private
SHA above; worker captures its execution base and returns pending changes.
Reviewer alone owns material commit and later session-sync commit.

## Claim Boundary

This work order authorizes one no-commit PPRR-R1 candidate only. It grants no
semantic, public, runtime, provider, merge, deployment or successor authority.
