# CVF Agent Work Order - CADP-AI-T2A Repository-Owned Capability Evidence Binding

Memory class: governed-worker-dispatch
Status: DISPATCH_READY
docType: work-order
Date: 2026-08-13
Batch ID: CADP-AI-T2A
## Dispatch Prompt Envelope

Role: implementation worker for CADP-AI-T2A.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T2A_REPOSITORY_OWNER_BINDING_CONTINUATION_2026-08-13.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`.

Current-time notes: packet and operator authorization are dated 2026-08-13.

Do-not-misread notes: the committed T2 fail-closed checkpoint is accepted but
does not close F11. This continuation must create a source-verified owner; it
must not restore a caller-data mint or treat green gates as independent review.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, paired baseline, this work order, current owner/CADP source, committed
grant and all applicable checker source; capture execution base before edits.

Return contract: implement exact scope, create the worker return, run all
proof, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

dispatchBaseHead: `86e06ab84896e3433f0484551facc2c6a08bb480`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `NOT_EXECUTED_YET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: implementation worker

Reviewer/closer: independent reviewer/closer

Worker return path:
`docs/reviews/CVF_CADP_AI_T2A_REPOSITORY_OWNER_BINDING_CONTINUATION_WORKER_RETURN_2026-08-13.md`

## Purpose

Close the missing T2 owner-binding implementation by deriving authority only
from the current private provenance repository's committed Git objects and by
persisting replay/retry consumption in SQLite.

## Worker Autonomy / No-Question Rule

Repair all allowed-scope code, test and checker failures directly. Stop only
for a source contradiction, forbidden-path requirement, missing committed
grant, or authority design that would again permit caller self-attestation.

## Required First Reads

- `AGENTS.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- active handoff named there
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- paired T2A baseline and this work order
- T2 worker return and independent review
- all source files in the Source Verification Block

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| operator release | explicit 2026-08-13 instruction to complete T2 | ACCEPT |
| T2 checkpoint | material commit `f4b99100e8d5f84313ebe9b41d410dcbb8df831c` | ACCEPT |
| T2A baseline | paired GC-018 baseline | ACCEPT |
| committed grant | private-provenance grant path named below | ACCEPT |

## Agent Roles

| Role | Responsibility |
|---|---|
| operator | owns scope release and any secret/live checkpoint |
| dispatcher | owns this packet and committed grant authority |
| implementation worker | implements exact allowed scope and returns uncommitted evidence |
| independent reviewer/closer | authors adversarial probes, disposition and commits accepted material |

## Pre-Flight Checks

1. Capture `executionBaseHead` and confirm it equals the committed dispatch
   head supplied after this packet is materialized.
2. Confirm staging is empty and no unrelated working-tree changes exist.
3. Run the exact pre-implementation autorun command.
4. Confirm the committed grant is visible through `git show HEAD:<grantRef>`.
5. Stop before implementation if any check fails outside Allowed Scope.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | convert the accepted T2 blocked checkpoint and F11 residual into a source-owned implementation |
| scope classification | SECURITY_SENSITIVE_LOCAL_RUNTIME_AND_DURABLE_STATE |
| risk sensitivity | high: authority minting, persistent replay state and trusted-evidence claims; no public sync, provider/live, secret use, deployment or production action |
| selected role route | SINGLE_AGENT_SINGLE_ROLE |
| role separation basis | one implementation worker owns only code/tests/return; an independent reviewer/closer owns adversarial acceptance and commit |
| escalation condition | stop on caller-mint reachability, alternate-repository acceptance, replay reset, missing committed hash, forbidden path, secret need or claim-boundary expansion |

## Allowed Scope

Allowed paths:

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.test.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/repository-capability-owner.source.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/repository-capability-owner.source.test.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.test.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/package.boundary.test.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/package.json`
- the exact worker return path named above

Forbidden paths:

- provider adapters, Web routes, MCP/CLI, public-sync clone and deployment
  configuration;
- API-key or raw-secret values in code, fixtures, logs or artifacts;
- the committed T2/T2A dispatch packet, grant, checkpoint receipt and prior
  independent review during worker execution;
- session state, handoff, governance checker and hook files.

Operator authorization: explicit instruction on 2026-08-13 to complete T2 and
use API keys only if live proof is actually required.

Rollback boundary: revert only the T2A implementation batch if rejected; do
not revert checkpoint commit `f4b99100e` or this dispatch authority.

## Write Ownership

The worker owns only the eleven implementation/return paths listed under Allowed
Scope. The dispatcher owns the baseline, work order, grant, receipt, roadmap
and conditional reopen index. The reviewer owns completion/finality and commit.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| private provenance repository is canonical | authority | `AGENTS.md` | Critical Repository Boundary | private provenance repository | authority hierarchy | ACCEPT |
| current owner always rejects | runtime | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts` | owner front door | `isBoundCapabilityOwner` | owner-binding contract | ACCEPT |
| evidence validator consumes owner artifacts | contract | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts` | evidence validation | `validateCompatibilityEvidence` | CADP contract | ACCEPT |
| trace contains concrete receipt ID | contract | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/workflow-binding.contract.ts` | execution trace | `WorkflowStepExecutionTrace` | workflow contract | ACCEPT |
| receipt emission binds trace | contract | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts` | emission | `emitStepReceipt` | receipt contract | ACCEPT |
| SQLite package capability exists | implementation | `EXTENSIONS/CVF_GUARD_CONTRACT/src/audit/sqlite-db.ts` | database wrapper | `AuditDatabase` | audit package | ACCEPT |
| committed grant | governed input | `governance/capability-grants/cadp-ai-t2a-owner-binding-grant.v1.json` | complete JSON document | `cvf.cadp.repositoryGrant.v1` | private provenance repository | ACCEPT |

## Required Implementation

1. Add a repository source module whose only binding input is a normalized
   grant path under `governance/capability-grants/`.
2. Resolve repository root from the production module location, not caller
   cwd or a caller-supplied root.
3. Use `execFileSync`/argument arrays with Git; never construct a shell command.
4. Read grant and artifact bytes from committed `HEAD`, never working-tree
   files, and require plain blobs plus exact SHA-256 pins.
5. Strictly parse a closed JSON schema. Reject unknown keys, duplicate semantic
   IDs, unsafe paths, accessors/proxies after JSON parse N/A, raw-secret-shaped
   credential values, invalid times and invalid ceilings.
6. Store the verified frozen grant record in module-private `WeakSet`/`WeakMap`
   state. Public projections must be fresh frozen scalar copies.
7. Persist grant hash, invocation ID, retry ordinal and counters atomically in
   SQLite. Duplicate invocation and ceiling failures must survive reopening.
8. Reconcile every observation field exactly and require bound trace and
   receipt identities before recording consumption.
9. Keep the binder absent from package wildcard exports except the deliberate
   root API `bindCommittedCapabilityOwnerGrant(grantRef)`; prove this function
   cannot bind caller-created objects or alternate repositories.
10. Update CADP comments and error disposition only after positive and
    adversarial tests show the owner is reachable and F11 is no longer
    caller-self-attested.

## Execution Plan

1. Read and parse the committed grant through a new repository source module;
   validate path, schema, artifact types, times, IDs and hashes.
2. Replace the unconditional owner contract with module-private opaque handle
   state and immutable projections.
3. Add transactional SQLite replay/retry state and exact observation
   reconciliation.
4. Connect the CADP evidence validator to verified artifacts only.
5. Add positive and adversarial source/owner/CADP/package tests.
6. Run all required commands after the final code edit.
7. Create the exact worker return and stop uncommitted.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| owner contract | replace unconditional blocking with opaque consume/read/reconcile behavior |
| repository source | implement committed-blob verification and durable replay ownership |
| owner/source tests | positive binding plus direct-import, forgery, path, hash, replay, retry and hostile-input cases |
| CADP contract/tests | prove ranks 2-5 accept only correctly bound artifacts and reject wrong owner/type/ref |
| package boundary | prove no generic grant-data mint and deliberate export shape |
| worker return | disclose exact diff, commands, residuals and no-commit status |

## Acceptance Criteria

- [ ] committed grant binds and produces an opaque handle
- [ ] caller-created grant data has no accepted input position
- [ ] wrong/uncommitted/tampered/path-traversal grants fail closed
- [ ] copied, serialized, forged, proxy and cross-module values fail closed
- [ ] artifact bytes and SHA-256 pins are verified from `HEAD`
- [ ] versions and all constraint fields reconcile exactly
- [ ] trace and receipt linkage are concrete and owner-bound
- [ ] invocation/retry/duplicate ceilings persist across reopen
- [ ] raw secret material is rejected and never emitted
- [ ] focused/full tests, typecheck and governance gates pass
- [ ] independent reviewer accepts F11 closure before T2 is closed

Fail conditions:

- [ ] any API accepts a complete caller-authored grant or artifact index
- [ ] any test-only authority is imported by production or used as proof
- [ ] any green gate is described as independent acceptance
- [ ] any provider, deployment or production claim lacks its required proof

## Evidence Requirements

- exact `executionBaseHead`, final status and unstaged/staged evidence;
- committed grant and each artifact hash independently recomputed from `HEAD`;
- focused test identities and counts, full suite and TypeScript result;
- a fresh-process or reopened-store test proving duplicate/replay counters do
  not reset;
- negative proof for arbitrary grant data, path traversal, dirty-file drift,
  alternate repository, hash mismatch, forged handles and raw-secret input;
- no live receipt unless a provider call is actually introduced.

## Review Gate

Closure requires an independent reviewer to inspect the entire material diff,
author direct-import/alternate-repository/replay-reset probes, and accept F11
closure. Worker-authored tests and green governance gates are insufficient.

## Closure Checklist

- [ ] all acceptance criteria satisfied
- [ ] exact changed set is within manifest
- [ ] worker return fast gate passes after final edit
- [ ] independent reviewer disposition exists
- [ ] material commit is reviewer-owned
- [ ] committed-range pre-closure gate passes
- [ ] roadmap, reopen index and continuity state are reconciled

## Return-To-Orchestrator Conditions

Return without implementation if the production module cannot resolve the
canonical repository independently of caller input, the committed grant is
missing or hash-inconsistent, durable replay requires forbidden storage, or a
secure design requires provider/public/deployment scope.

## Operator Checkpoint

SATISFIED: the operator explicitly released T2 completion and allowed live API
use if required. No live call is currently required because the selected trust
root is the committed private provenance repository, not a provider response.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 86e06ab84896e3433f0484551facc2c6a08bb480 --head HEAD
pnpm --dir EXTENSIONS/CVF_GUARD_CONTRACT exec tsc --noEmit
pnpm --dir EXTENSIONS/CVF_GUARD_CONTRACT exec vitest run --pool forks src/contracts/repository-capability-owner.source.test.ts src/contracts/capability-owner-binding.contract.test.ts src/contracts/capability-admission-distribution-profile.contract.test.ts src/contracts/contracts.phaseE-workflow-binding.test.ts src/contracts/contracts.phaseE-receipt-binding.test.ts src/package.boundary.test.ts
pnpm --dir EXTENSIONS/CVF_GUARD_CONTRACT test
python governance/compat/check_governed_file_size.py --enforce
git diff --check
python governance/compat/run_worker_return_fast_gate.py
git status --short --untracked-files=all
git diff --cached --name-only
```

Live proof is `N/A with reason`: this tranche makes no provider behavior claim.
If implementation introduces such a claim, first follow the live diagnostic
standard and run `python scripts/run_cvf_release_gate_bundle.py --json` without
printing secrets.

## Worker Return Packet Shape Contract

workerReturnPath:
`docs/reviews/CVF_CADP_AI_T2A_REPOSITORY_OWNER_BINDING_CONTINUATION_WORKER_RETURN_2026-08-13.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections include Purpose, Target / Source, Scope / Methodology,
Findings / Position, Risk / Corrective Action, Decision / Disposition, Checker
Source Read-Ahead Block, Agent Operation Trace Block, Delta Execution Claim
Boundary Control Block, External Knowledge Intake Routing, Epistemic Process
Block, Public Export Disposition, Command Evidence, Changed Files, No-Commit
Statement and Claim Boundary.

The return must additionally carry these exact diagnostic surfaces:

- `Delta Execution Claim Boundary Control Block`
- `Epistemic Process Block`
- `Rescan Intelligence Hardening`
- `Corpus Completeness And Report Integrity`
- `Finding-To-Governance Learning Disposition`
- `Machine Closure Package`
- the actual `executionBaseHead`
- the actual `git status --short`
- a `WORKER_EXPERIENCE_RETRO` block or
  `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON`

If any listed section is not applicable, retain the section and record
`N/A with reason` or `NOT_APPLICABLE_WITH_REASON`; omission is forbidden.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CADP-AI-T2A --title "Repository-Owned Capability Evidence Binding" --date 2026-08-13 --base f4b99100e8d5f84313ebe9b41d410dcbb8df831c --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | authority, source, exact scope, implementation, proof and return contract |
| checkerReadAheadConfirmation | applicable dispatch/review/trace/public/file-size checkers inspected |
| docOnlyNewFields | none |
| claimBoundary | dispatch authoring provenance only |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | implementation worker followed by independent reviewer/closer |
| phase | T2A owner-specific continuation |
| baseHeadFor(phase) | dispatchBaseHead=`86e06ab84`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| changedSetScope(phase) | exact eleven-path maximum implementation manifest |
| traceScope(phase, actor) | local reads, patches, Git blob reads, SQLite temp state, compiler/tests, gates and diff evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer only |
| crossBatchIsolation | no T3/provider/public/deploy/session mixing |
| nextMoveSurfaces | worker return, independent adversarial review and reviewer disposition |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_CADP_AI_T2A_REPOSITORY_OWNER_BINDING_CONTINUATION_COMPLETION_2026-08-13.md` |
| reviewerOwnedClosurePaths | T2/T2A finality, roadmap, conditional reopen index, completion review and material commit |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |
| acceptanceRequirement | full changed-surface review plus independently authored direct-import, alternate-repo, replay-reset and tampered-blob probes |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `DISPATCH_READY`; exact Allowed paths/Forbidden paths/Operator authorization/Rollback boundary; Worker Return Packet Shape Contract; Public Export Disposition |
| gateRunPurpose | confirmation after source inspection and dispatch drafting |
| claimBoundary | packet shape is not owner-authenticity or runtime proof |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| packet/grant paths | exact path checks before authoring found no prior T2A artifacts | NEW_PATHS |
| generic owner mint search | current owner source contains no bind/mint/register/create path | SOURCE_GAP_CONFIRMED |
| repository source collision | no existing `repository-capability-owner.source.ts` path | NEW_IMPLEMENTATION_PATH |
| collision decision | preserve committed T2 blocked checkpoint; add an owner-specific continuation | ADDITIVE_CONTINUATION |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defect count: 0.

Returned defects: NONE_RETURNED

Dispatch impact: independently authored adversarial probes remain required.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | repository-local owner binding, committed-artifact verification and durable local replay state |
| claimDisposition | CLAIM_REJECTED until independent reviewer acceptance |
| receiptEvidence | CVF_RECEIPT_PRESENT: committed checkpoint receipt and exact bound artifact hashes; no provider receipt claim |
| actionEvidence | ACTION_EVIDENCE_PRESENT only after compiler/tests, SQLite reopen tests and independent probes execute |
| invocationBoundary | local Git object reads and private SQLite state only |
| interceptionBoundary | no external channel interception, mandatory wrapper or provider enforcement claim |
| claimLanguage | T2A implementation pending independent review |
| forbiddenExpansion | provider/live, T3 consumers, external CLI/MCP, public sync, deploy and production |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a binder that accepts only a grant path and
derives all authority from committed repository blobs can close the original
caller-self-attestation path while remaining directly importable.

Evidence Comparison Requirement: compare positive binding with direct-source
import, arbitrary data, alternate repository, tampered blob and replay-reset
attacks.

Contradiction Handling Requirement: any accepted caller-created authority or
resettable counter returns the work as blocked/repair-required and preserves
F11 as open.

Claim Update Requirement: worker return must state whether F11 is confirmed
closed, narrowed, or still open; only the independent reviewer may accept it.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | CADP-R1 -> T1 -> T2 fail-closed checkpoint -> T2A source-owned continuation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Guard Contract plus private provenance Git object database |
| Disposition | implement CVF-native owner seam; no external runtime import |
| Claim boundary | no new corpus scan or external source authority |

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - bounded implementation source
  verification only; no corpus completeness claim.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| owner | Guard Contract capability-owner source |
| durable source | committed grant under `governance/capability-grants/` |
| runtime state | private SQLite file under `logs/capability-owner/` by default |
| index impact | no generated aggregate or catalog is created |
| migration | N/A with reason: new owner-specific store; no existing durable records are moved |
| rollback | implementation commit may be reverted without deleting runtime data; stale state remains non-authoritative without matching committed grant hash |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/source reviewer |
| Provider or surface | local repository workspace |
| Session or invocation | CADP-AI-T2A dispatch, 2026-08-13 |
| Working directory | repository root |
| Command or tool surface | governed reads, source inspection, patching, hashing and dispatch gates |
| Target paths | paired T2A baseline/work order, committed grant/checkpoint receipt and roadmap routing |
| Allowed scope source | operator instruction to complete T2, including live proof if required |
| Before status evidence | clean worktree at checkpoint commit `f4b99100e` |
| After status evidence | T2A dispatch packet pending material commit |
| Diff evidence | `git status --short`; `git diff --name-status` |
| Approval boundary | packet and committed grant authority only; implementation remains no-commit worker scope |
| Claim boundary | no implementation success, F11 closure, provider, deployment or production claim |
| Agent type | dispatcher/source reviewer |
| Invocation ID | `cadp-ai-t2a-dispatch-2026-08-13` |
| Expected manifest | paired baseline/work order, grant, checkpoint receipt, roadmap and conditional reopen index |
| Actual changed set | reviewer records before dispatch commit |
| Manifest delta | must be zero before dispatch commit |
| Deletion or rename disposition | N/A with reason: no governed path is deleted or renamed |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance owner-binding continuation; no public-sync action.

## Claim Boundary

This work order authorizes repository-owned binding and local durable replay
state. It does not itself close F11 or T2, and it makes no provider/live,
deployment, public or production-readiness claim.
