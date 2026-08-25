# CVF Agent Work Order - RFR-R7C Truthful Role Composition Proof

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-08-25

Batch ID: RFR-R7C-TRUTHFUL-ROLE-COMPOSITION-PROOF

Dispatch base head: `365d411ee`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: one delegated test-only implementation worker

Reviewer/closer: current independent orchestrator/reviewer/closer

Worker return path: `docs/reviews/CVF_RFR_R7C_TRUTHFUL_ROLE_COMPOSITION_PROOF_WORKER_RETURN_2026-08-25.md`

## Dispatch Prompt Envelope

Role: delegated test-only worker for RFR-R7C.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_RFR_R7C_TRUTHFUL_ROLE_COMPOSITION_PROOF_2026-08-25.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: authored 2026-08-25 from clean HEAD `365d411ee`;
capture the committed dispatch HEAD before edits.

Do-not-misread notes: this is not authority-matrix repair. Do not add
`execute` to AI-agent authority, relabel the runtime action, edit production
source, or weaken any BLOCK expectation.

Required first actions: read bootstrap/front door/handoff, guard orientation,
literal gotchas, paired baseline, this packet and cited sources/checkers;
capture HEAD/status/staging; verify hashes; run pre-implementation and
reproduce exact 6/7 focused plus 779/780 package baseline.

Return contract: edit one test file, create the named full-gate return, leave
all changes unstaged/uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Make the real-engine positive composition proof use a role that canonical R7A
semantics actually authorize for truthful Model Gateway `execute`, while
preserving all AI-agent/orchestrator and risk-gate BLOCK proofs unchanged.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "RFR-R7C",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [
    "EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-composition-proof.test.ts",
    "docs/reviews/",
    "docs/baselines/CVF_GC018_RFR_R7C_TRUTHFUL_ROLE_COMPOSITION_PROOF_2026-08-25.md",
    "docs/roadmaps/CVF_RUNTIME_FINDINGS_CLOSURE_ROADMAP_2026-08-24.md"
  ],
  "claims": ["composition positive-path fixture matches accepted truthful role authority"],
  "requiredProof": ["focused composition and execute tests", "full MCP package", "TypeScript build", "hash invariance", "worker-return fast gate", "independent review"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["worker stage or commit", "production source edit", "Guard Contract edit", "authority widening", "action relabeling", "dependency installation", "provider/live/network call", "credential access", "deployment", "public write"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

Expected route: `ROUTED_SHADOW`, profile `P3_ELEVATED`, selective execution
false, legacy disposition `RUN_FULL_LEGACY_BUNDLE`.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RFR-R7C-TRUTHFUL-ROLE-COMPOSITION-PROOF --title "CVF RFR-R7C Truthful Role Composition Proof" --date 2026-08-25 --base 365d411ee --commit-mode WORKER_MUST_NOT_COMMIT --dependency "RFR-R7B independently accepted and materially closed at 79ca7e542" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic test-only no-commit worker dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact-two manifest, pinned hashes, truthful role invariant and forbidden authority/runtime owner set |
| checkerReadAheadConfirmation | cited checkers routed before authoring |
| docOnlyNewFields | none |
| claimBoundary | dispatch provenance only |

## Required First Reads

- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V59_2026-08-11.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/baselines/CVF_GC018_RFR_R7C_TRUTHFUL_ROLE_COMPOSITION_PROOF_2026-08-25.md`
- this work order and cited source/checker paths

## Agent Roles

| Role | Owner | Authority |
| --- | --- | --- |
| operator | current operator | standing dependency-ordered roadmap continuation |
| dispatcher | current orchestrator | source verification and exact packet |
| worker | one delegated worker | one test edit plus return; no commit |
| reviewer/closer | current independent orchestrator | reproduce, accept/reject, commit and sync |

## Authority Chain

Operator roadmap authority -> R7A truthful-action closure -> R7B bounded
closure at `79ca7e542` -> runtime findings roadmap -> paired baseline -> this
work order.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| R7A role/action contract | R7A completion R7A-F3 | must remain unchanged | ACCEPT |
| R7B material closure | `79ca7e542` | validator repair committed first | ACCEPT |
| R7B continuity | `365d411ee` | R7C preparation active | ACCEPT |
| exact residual | independent 31/32 focused and 779/780 package | no other failure may appear | ACCEPT |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intake summary | reconcile one stale positive-path role fixture |
| scope classification | TEST_ONLY_CONTRACT_RECONCILIATION |
| primary task class | bounded local test implementation |
| risk sensitivity | MEDIUM |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| orchestration requirement | one no-commit worker plus independent reviewer |
| role separation basis | worker cannot accept its own cross-owner proof change |
| escalation condition | production/authority edit, second test file, changed negative semantics, new failure or external effect |

## Scope

Change only the real-engine positive composition case so its input explicitly
uses an already authorized positive-path role. The preferred bounded change is
an input override local to that one test, not a mutation of shared
`VALID_INPUT`, because other cases intentionally exercise AI-agent and risk
behavior. Add or adjust assertions only inside the same case if required to
make the role/action intent explicit.

## Write Ownership

Worker may edit only:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-composition-proof.test.ts`
- `docs/reviews/CVF_RFR_R7C_TRUTHFUL_ROLE_COMPOSITION_PROOF_WORKER_RETURN_2026-08-25.md` (new)

Every other path is forbidden, especially MCP production source, other tests,
Guard Contract, Model Gateway, request schemas, package/lockfiles, governance,
roadmap and continuity.

## Source Hash Manifest

| Path | SHA-256 required at worker start | Authority |
| --- | --- | --- |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-composition-proof.test.ts` | `52b00ddf27b0879cd523fe826eb0914482a374f65a7b6e92b3839dde98f7d994` | edit |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.test.ts` | `5a00e42bef507966928ff6f4b0fce862676ce611a7ee4e828d879db7320ae52d` | read/test only; MATCH required |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/authority-gate.guard.ts` | `901e3f25ed1f6a2ab4e9f9eeaa2fc98a7dcf985cb3474eb6245ad1b844fc537c` | read/hash only; MATCH required |

## Pre-Flight Checks

1. Capture HEAD, clean worktree and empty staging.
2. Verify committed dispatch packet and all three hashes.
3. Run pre-implementation autorun.
4. Reproduce focused 31/32 and package 779/780 with only the named case failing.
5. Stop on any hash drift or unrelated baseline failure.

## Execution Plan

1. Change only the positive real-engine case to pass an explicit OPERATOR role
   while leaving shared AI-agent input and negative cases intact.
2. Assert ALLOW, executor call and bridge call remain truthful.
3. Run composition plus execute tests, then full package and build.
4. Recompute both read-only hashes and inspect the exact diff.
5. Create the full-gate worker return and stop without staging or committing.

## Acceptance Criteria

- composition proof passes 7/7;
- execute suite passes 25/25, including real OPERATOR ALLOW and
  AI-agent/orchestrator BLOCK;
- focused total passes 32/32;
- MCP package passes 780/780;
- MCP build passes;
- production and Guard Contract hashes remain MATCH;
- diff changes only the one test plus return;
- no authority/action/runtime semantic changes;
- worker HEAD unchanged and staging empty.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap item | Implementation | Proof |
| --- | --- | --- |
| stale positive role fixture | test-local authorized role override | composition 7/7 |
| preserve R7A semantics | no shared fixture or runtime/authority edit | execute 25/25 and hash MATCH |
| close MCP package residual | no remaining failure | package 780/780 |

## Required Proof Manifest

| Proof | Required result |
| --- | --- |
| pre-edit hashes | all three MATCH |
| composition plus execute focused | 32/32 PASS |
| MCP package | 780/780 PASS |
| MCP build | PASS |
| read-only hashes after edit | both MATCH |
| worker return fast gate | PASS |
| diff/status/staging | exact-two worker manifest; staging empty; HEAD unchanged |

## Verification Commands

From `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER`:

```powershell
npx vitest run src/tools/model-gateway-composition-proof.test.ts src/tools/model-gateway-execute.test.ts --run
npm test -- --run
npm run build
```

From repository root:

```powershell
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
git diff --cached --name-only
git status --short
```

## Evidence Requirements

Record each command, working directory, atomic count/result and disposition.
Recompute read-only hashes after edits. A focused pass cannot substitute for
the full 780-test package.

## Required Proof Manifest Atomic Literal Discipline

Report each proof once with one exact result and no aggregate laundering.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| positive case inherits AI-agent role | TEST_SOURCE | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-composition-proof.test.ts` | `VALID_INPUT`; positive case | `VALID_INPUT` | MCP composition proof | ACCEPT |
| accepted positive role proof exists | TEST_SOURCE | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.test.ts` | registered tool tests | OPERATOR ALLOW test | MCP execute proof | ACCEPT |
| accepted negative role proof exists | TEST_SOURCE | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.test.ts` | registered tool tests | AI-agent BLOCK test | MCP execute proof | ACCEPT |
| matrix is read-only authority | CONTRACT_SOURCE | `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/authority-gate.guard.ts` | `AUTHORITY_MATRIX` | `AUTHORITY_MATRIX` | Guard Contract | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_corpus_scan_registry.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `COMPLETE_PENDING_REVIEW`; Source Verification columns; Actual changed set |
| gateRunPurpose | confirm packet conformance after source verification |
| claimBoundary | structure does not prove test correctness |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_RFR_R7C_TRUTHFUL_ROLE_COMPOSITION_PROOF_WORKER_RETURN_2026-08-25.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required real sections: Purpose; Scope / Methodology; Findings / Position; Risk
/ Corrective Action; Checker Source Read-Ahead Block; Agent Operation Trace
Block; Delta Execution Claim Boundary Control Block; Public Export Disposition;
External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus
Completeness And Report Integrity; Finding-To-Governance Learning Disposition;
Epistemic Process Block; Claim Boundary; git status --short; Changed Files;
Worker Experience Retrospective; Command Evidence; No-Commit Statement; Machine
Closure Package.

## Work-Order Fulfillment Manifest

Fulfillment must reconcile the required artifact and proof manifests exactly.

## Required Artifact Manifest

| Artifact | Required worker action | Final status |
| --- | --- | --- |
| composition proof test | one positive-case role reconciliation | PASS |
| execute and authority sources | read/test/hash only; byte-unchanged | PASS |
| worker return | create exact full-gate artifact | PASS |
| all other paths | byte-unchanged | PASS |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> one test-only worker -> independent reviewer/closer |
| phase | R7C implementation pending |
| baseHeadFor(phase) | dispatchBaseHead=`365d411ee`; executionBaseHead=worker captures committed dispatch HEAD; closureBaseHead=reviewer captures return HEAD |
| changedSetScope(phase) | exact two-path Write Ownership manifest |
| traceScope(phase, actor) | worker records every command/delta; reviewer independently reproduces role proofs |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer only |
| crossBatchIsolation | production, authority, Model Gateway, governance, session and external effects forbidden |
| nextMoveSurfaces | exact worker return then independent review |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_RFR_R7C_TRUTHFUL_ROLE_COMPOSITION_PROOF_COMPLETION_2026-08-25.md` if needed |
| reviewerOwnedClosurePaths | worker return, this work order, roadmap, optional completion review and separate continuity |
| closureOwner | current independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Review Gate

Reviewer must inspect the exact test diff, independently prove OPERATOR ALLOW,
AI-agent/orchestrator BLOCK, risk-gate BLOCK, 7/7 focused and 780/780 package,
verify hashes and run reviewer-fast before commit.

## Closure Checklist

- [x] exact-two worker manifest;
- [x] focused 32/32 and package 780/780;
- [x] build and hashes pass;
- [x] no production/authority change;
- [x] worker HEAD unchanged/staging empty;
- [x] independent reviewer decision recorded in
  `docs/reviews/CVF_RFR_R7C_TRUTHFUL_ROLE_COMPOSITION_PROOF_COMPLETION_2026-08-25.md`.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_RFR_R7C_TRUTHFUL_ROLE_COMPOSITION_PROOF_COMPLETION_2026-08-25.md` | reviewer verdict | PASS |
| Worker return | `docs/reviews/CVF_RFR_R7C_TRUTHFUL_ROLE_COMPOSITION_PROOF_WORKER_RETURN_2026-08-25.md` | reviewer accepted | PASS |
| Implementation | MCP composition proof test | case-local OPERATOR input | PASS |
| Deterministic proof | focused, package and build commands | 32/32; 780/780; build PASS | PASS |
| Roadmap state | runtime findings roadmap | R7C closed; final reconciliation remains active | PASS |
| Registry JSON | corpus registry aggregate | no registry mutation authorized for R7C | BLOCKED with reason |
| Registry Markdown | corpus registry human projection | no registry mutation authorized for R7C | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence consumed | no digest | N/A with reason |
| System loop interlock | R7B-to-R7C dependency | stale role residual closed | PASS |
| Session continuity | separate post-material sync | not part of worker or material closure | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
| --- | --- | --- |
| truthful authorized positive role | case-local OPERATOR with `execute` | PASS |
| negative role semantics retained | AI-agent and orchestrator BLOCK tests pass | PASS |
| deterministic package proof | 780/780 | PASS |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/orchestrator |
| Provider or surface | repository-local orchestration |
| Session or invocation | RFR-R7C dispatch, 2026-08-25 |
| Working directory | repository root |
| Command or tool surface | source reads, hashes, scaffold, governed patch and dispatch gates |
| Target paths | paired baseline, work order and roadmap |
| Allowed scope source | standing operator authority plus R7B closure |
| Before status evidence | clean worktree at HEAD `365d411ee`; `git status --short` empty |
| After status evidence | exact three dispatcher artifacts pending before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch only; test edit begins after committed handoff |
| Claim boundary | no implementation or external effect |
| Agent type | dispatcher/orchestrator |
| Invocation ID | `rfr-r7c-dispatch-2026-08-25` |
| Expected manifest | paired baseline, work order and roadmap |
| Actual changed set | paired baseline, work order and roadmap |
| Manifest delta | NONE |
| Deletion or rename disposition | N/A with reason: none authorized |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local test-only implementation and deterministic proof |
| claimDisposition | CLAIM_REJECTED: dispatch proves no runtime behavior |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime/provider action |
| invocationBoundary | local tests/build only |
| interceptionBoundary | no live interception or wrapper authority |
| claimLanguage | test-only after independent acceptance |
| forbiddenExpansion | production, authority, action label, install, provider/live/network, credentials, deployment, public sync, push and production |

## Epistemic Process Block

- Epistemic Process Applicability: BOUNDED_TEST_CONTRACT_RECONCILIATION
- Expected result / prediction: one test-local OPERATOR override restores the
  real-engine positive path without affecting negative proofs.
- Evidence Comparison: R7A/R7B evidence and current source support that exact
  role distinction.
- Contradiction or gap disposition: any production or authority edit rejects
  the prediction and returns blocked.
- Claim update: R7C is dispatchable test-only; no runtime claim follows.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no external knowledge intake |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | MCP composition test |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | first-party repository authority only |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: current first-party test repair, not legacy intake.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-execution`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-execution --json`

## Worker Autonomy / No-Question Rule

Proceed inside exact scope, repair only allowed test/return formatting, and
rerun proof. Return blocked for any other file, hash drift, unrelated failure,
semantic contradiction or external effect.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with all criteria, exact-two delta,
unchanged HEAD and empty staging. Otherwise return `BLOCKED_WITH_REASON`.

## Escalation Boundary

No mid-worker checkpoint. Production/authority changes require fresh explicit
authority and must not be attempted.

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | TEST_ONLY_CURRENT_LOCAL_BASELINE |
| runtimeMutationAuthorized | NO_PRODUCTION_MUTATION |
| freshnessVerificationMode | current source/hashes and independent R7B tests dated 2026-08-25 |
| reason | one current test expectation is stale |
| requiredFutureAction | worker/reviewer rerun hermetic proof |

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: no storage, registry, aggregate or relocation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance test tranche; no public-sync action authorized.

## Claim Boundary

This work order authorizes exactly one test edit and one uncommitted return. It
does not authorize production, Guard Contract, Model Gateway, authority/action,
dependency, provider/live/network, credential, deployment, public-sync, push,
production-readiness or worker closure changes.

## Operator Checkpoint

NOT_APPLICABLE_WITH_REASON: standing roadmap authority releases this bounded
test-only step; no mid-worker decision is scheduled.
