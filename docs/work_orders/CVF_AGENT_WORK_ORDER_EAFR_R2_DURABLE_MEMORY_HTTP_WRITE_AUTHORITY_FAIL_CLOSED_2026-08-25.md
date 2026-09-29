# CVF Agent Work Order - EAFR-R2 Durable Memory HTTP Write Authority Fail Closed

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Work order ID: EAFR-R2

Date: 2026-08-25

dispatchBaseHead: `8036abf5609e3e87d6de98153cbad3c724f97475`

executionBaseHead: worker must record actual HEAD and require it to include this committed packet

closureBaseHead: reviewer captures the committed dispatch head

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through explicit EAFR authority

Reviewer/closer: current independent orchestrator/reviewer

Worker: implementation worker role

## Dispatch Prompt Envelope

Batch ID: EAFR-R2-DURABLE-WRITE

Role: no-commit R2 implementation worker.

Canonical packet: this committed work order and its paired baseline.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: R1 waiver closure is committed; R1C remains debt before R6.

Do-not-misread notes: R1 waiver does not apply to R2; no live/provider/public effect.

Required first actions: read startup surfaces, guard orientation, this work order,
paired baseline, every cited source, and applicable worker-output checkers.

Return contract: exact three paths, no stage/commit, pending-review or blocked status.

Worker return path: `docs/reviews/CVF_EAFR_R2_DURABLE_MEMORY_HTTP_WRITE_AUTHORITY_FAIL_CLOSED_WORKER_RETURN_2026-08-25.md`

## Purpose

Fail close incomplete or self-attested durable-memory HTTP writes.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R2 --title "Durable Memory HTTP Write Authority Fail Closed" --date 2026-08-25 --base ee268fa5b --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, exact runtime manifest and proof contract |
| checkerReadAheadConfirmation | applicable dispatch and worker-return checker sources read |
| docOnlyNewFields | none |
| claimBoundary | dispatch authoring only |

## Mission

Repair the durable-memory HTTP write route so incomplete provenance and caller-
self-attested identity/authority fail closed before persistence, with adversarial
tests proving zero store mutation.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R1 bounded closure | explicit waiver material commit `ee268fa5b`; R1C debt preserved before R6 | ACCEPT |
| R1A | closed at `ef142bfb2` | ACCEPT |
| R1B | adjudication accepted at `fc10c8e65` | ACCEPT |

## Authority And Scope

Governing baseline:
`docs/baselines/CVF_GC018_EAFR_R2_DURABLE_MEMORY_HTTP_WRITE_AUTHORITY_FAIL_CLOSED_2026-08-25.md`.

The worker may edit exactly:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.test.ts`
3. `docs/reviews/CVF_EAFR_R2_DURABLE_MEMORY_HTTP_WRITE_AUTHORITY_FAIL_CLOSED_WORKER_RETURN_2026-08-25.md`

No other path is writable. The worker must not stage or commit.

## Authority Chain

Operator waiver closure -> EAFR roadmap -> paired baseline -> this work order
-> no-commit worker -> independent reviewer/closer.

## Agent Roles

Operator owns scope; dispatcher owns the packet; worker implements without
commit; reviewer independently tests, repairs, closes, and commits.

## Required First Reads

Read startup surfaces, guard orientation, literal gotchas, paired baseline,
this work order, five pinned sources, and worker-return checker sources.

## Pre-Flight Checks

Confirm clean worktree, empty staging, actual HEAD, pinned hashes, Node/npm,
exact writable paths, and no live-test selection.

## Write Ownership

Exactly the three named paths. No deletion, rename, generated state,
environment, auth-owner, store-owner, or package edit.

## Execution Plan

Inspect, add adversarial tests, implement the smallest repair, run focused and
package evidence, author the return, run its fast gate, and stop.

## Evidence Requirements

Record commands, counts, failures, zero-mutation proof, hashes, manifest,
staging, HEAD, external-effect inventory, and no-commit statement.

## Pinned Input Hashes

| Path | SHA-256 |
| --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.ts` | `6d956ccabd2cbfc6c0ae2a2182ea666b2fc558ec5f024bd6772369007b35ec13` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.test.ts` | `bbdbf647da150d19ff97bb643f96564c4b8f5dd4adb2851d985e5fd8332e24bf` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | `e2fa4b495a688becb3e5d550679d852d0f9e49d939846a4832c07b5552cad599` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts` | `c2ab4845445439727060f1d8c9bcd7d2b9c5dc8fabd7edbe1057941878751f9f` |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | `531b03c9002d3dc1a2e48afc29aae583966a2db7c0d9d0f569dbef71958e75e2` |

If any pinned hash differs at execution start, return `BLOCKED_WITH_REASON`.

## Required Implementation

1. Make provenance a mandatory finite number in the inclusive range `[0,1]`.
2. Reject blank `id`, `scope`, `summary`, and `actorId`; reject malformed
   optional `containsSecret`, lifecycle, sensitivity, tier and role values.
3. Reuse `resolveExecutionCVFRole` and `deriveServiceTokenIdentity`; do not
   duplicate their mappings or edit their owner files.
4. Bind a session caller to `session.userId` and the resolved session role.
5. Bind a verified service token to its derived identity and `SERVICE_AGENT`.
6. Reject caller actor-id or actor-role mismatches before store construction.
7. Treat request-body `actorAuthorized` and `policyDecision` as untrusted intent,
   never sufficient authority. Pass server-derived authorization to the store
   only after authentication, identity, role, provenance and payload validation.
8. Preserve raw payload rejection, summary-only receipts, no raw release, and
   existing valid writes for roles the durable store already authorizes.

## Required Adversarial Tests

Tests must prove both denial and file non-creation/non-mutation for:

- omitted provenance;
- zero, negative, above-one, and the valid `0.7` boundary;
- blank required strings;
- missing or false caller policy fields;
- unsupported session role;
- session actor-id mismatch and actor-role escalation;
- service-token actor-id mismatch and non-`SERVICE_AGENT` role claim;
- malformed `containsSecret`;
- raw content fields;
- valid bound session write and valid bound service-token write.

Use deterministic mocks only. Do not read `.env`, inspect keys, or call network,
provider, live, deployment, or external services.

## Acceptance Criteria

- focused route tests pass with all new negative cases;
- every rejected write proves zero persistence mutation;
- typecheck is run and reported exactly; pre-existing failures must be reported,
  not waived or relabeled;
- the safe non-live package command is run and reported exactly; R1's waiver
  does not apply to R2;
- no live-test file is selected and `test:live` is never invoked;
- exact three-path manifest, empty staging, unchanged worker HEAD;
- worker-return fast gate passes;
- no assertion is weakened and no compatibility bypass is added.

rawMemoryReleased=false

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "EAFR-R2",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": ["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/", "docs/reviews/", "docs/baselines/CVF_GC018_EAFR_R2_DURABLE_MEMORY_HTTP_WRITE_AUTHORITY_FAIL_CLOSED_2026-08-25.md", "docs/work_orders/CVF_AGENT_WORK_ORDER_EAFR_R2_DURABLE_MEMORY_HTTP_WRITE_AUTHORITY_FAIL_CLOSED_2026-08-25.md"],
  "claims": ["durable-memory HTTP write admission fails closed"],
  "requiredProof": ["focused tests", "zero mutation", "typecheck", "safe non-live suite", "worker-return fast gate", "independent review"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["live/provider/network call", "credential or environment-file access", "owner-file mutation", "worker stage or commit", "public/deploy/push"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| worker role | no-commit implementation worker |
| reviewer role | independent reviewer/closer |
| external intake | prior finding reverified; no new absorption |
| escalation condition | hash drift, scope expansion, unsafe evidence, or owner-file need |
| risk sensitivity | R2 authenticated persistence boundary |
| scope classification | exact three-path local runtime repair |

## Required Commands

Run from the cvf-web package unless noted:

1. focused Vitest for `src/app/api/memory/write/route.test.ts`;
2. `npm run check`;
3. `npm run test:run`;
4. from repository root, `python governance/compat/run_worker_return_fast_gate.py`;
5. `git diff --check`, `git diff --name-status`, `git status --short --untracked-files=all`, and `git diff --cached --name-only`.

Do not run `npm run build` in this tranche: R2 requires source/test/typecheck
proof and the known Auth.js environment condition is owned by R1C. Do not use
the R1 waiver as an R2 acceptance substitute.

## Verification Commands

Run every Required Commands item, including
`python governance/compat/run_worker_return_fast_gate.py`. Individual checker
substitution is forbidden.

## Fail Conditions

Return `BLOCKED_WITH_REASON` if a pinned hash drifts, an edit outside manifest is
needed, a rejected case mutates storage, authenticated identity cannot be bound
without editing an owner file, or a required command cannot be run safely.

## Worker Autonomy / No-Question Rule

Repair all allowed-scope defects and rerun focused evidence without asking the
operator. Do not expand scope. One consolidated repair round is preferred.

## Evidence Reuse And Encoding Plan

verificationMode: FRESH_RECOMPUTE

priorVerificationArtifact: N/A with reason: R2 changes runtime behavior

priorVerificationAnchor: N/A with reason: fresh focused proof required

freshRecomputeRequired: focused route tests, typecheck, safe non-live suite and worker-return gate

unicodePathHandling: use literal repository-relative paths and UTF-8-safe readers

extractedTextAuthority: source files and command output only

## Current Runtime Freshness Verification

Dispatch-author source inspection at `ee268fa5b` confirms optional provenance,
caller-supplied authority fields, existing server identity/role helpers, and the
test gap. Worker must recheck hashes before edits.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| optional provenance reaches store | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.ts` | validation and store call | `validateBody`; `provenanceScore` | route | ACCEPT |
| omitted provenance defaults to one | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | write path | `input.provenanceScore ?? 1` | durable store | ACCEPT |
| stable service identity helper | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | exported helper | `deriveServiceTokenIdentity` | service auth | ACCEPT |
| server role resolver | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts` | exported resolver | `resolveExecutionCVFRole` | role owner | ACCEPT |
| adversarial coverage missing | TEST_GAP | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.test.ts` | current suite | memory write route tests | test owner | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | dispatch status; Source Verification Block; worker-return shape; Evidence Reuse scalar fields; exact manifest |
| gateRunPurpose | confirm as evidence that this completed packet already matches checker shape |
| claimBoundary | checker compliance does not prove the worker implementation |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime implementation`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "runtime implementation" --role worker --lifecycle-phase implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | ordinary CVF controls apply |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | authenticated Web memory-write route | server-bound identity and role before store admission | focused route tests | Web route only | IMPLEMENT |
| EXTERNAL_AGENT_CLI_MCP | no CLI/MCP surface changed | no new external-agent adapter authority | exact manifest | N/A with reason: HTTP route repair only | N/A_WITH_REASON |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | no-commit implementation worker plus independent reviewer |
| phase | implementation pending worker return |
| baseHeadFor(phase) | dispatchBaseHead=8036abf56; executionBaseHead=worker captures; closureBaseHead=reviewer captures |
| changedSetScope(phase) | exact three-path worker manifest |
| traceScope(phase, actor) | local source/test implementation and deterministic proof |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | clean worktree required; R1C/R3-R6/RFR parked |
| nextMoveSurfaces | worker return then independent reviewer decision |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_EAFR_R2_DURABLE_MEMORY_HTTP_WRITE_AUTHORITY_FAIL_CLOSED_WORKER_RETURN_2026-08-25.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must include Purpose, Target / Source, Scope / Methodology, Findings
/ Position, Risk / Corrective Action, Checker Source Read-Ahead Block, Agent
Operation Trace Block, Delta Execution Claim Boundary Control Block, External
Knowledge Intake Routing, Rescan Intelligence Hardening, Corpus Completeness
And Report Integrity, Finding-To-Governance Learning Disposition, Epistemic
Process Block, Claim Boundary, git status, Changed Files, Command Evidence,
Public Export Disposition, and No-Commit Statement. It must self-declare as a
worker-return artifact and cite this work order.

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_EAFR_R2_DURABLE_MEMORY_HTTP_WRITE_AUTHORITY_FAIL_CLOSED_COMPLETION_2026-08-25.md` |
| reviewerOwnedClosurePaths | worker return, completion review, EAFR roadmap and continuity |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

The worker return is not closure. Reviewer must inspect source and tests,
challenge identity binding and zero-mutation behavior, rerun proportionate
evidence, own repairs, run reviewer/pre-commit gates, and commit material before
session sync. R3 remains held until accepted R2 closure.

## Review Gate

Independent reviewer must challenge every identity-binding and zero-mutation
case and run reviewer/closure gates before acceptance.

## Closure Checklist

- [ ] exact manifest and empty staging;
- [ ] focused tests and zero-mutation assertions pass;
- [ ] typecheck and safe non-live suite recorded without R1 waiver reuse;
- [ ] worker-return fast gate and independent reviewer gates pass;
- [ ] R3 remains held until committed acceptance.

## Operator Checkpoint

operator.checkpoint.waiver: none for R2. Standing authority covers bounded local
implementation and review only; live/provider/public/destructive expansion
requires fresh explicit approval.

## Return-To-Orchestrator Conditions

Return pending review on success or blocked with reason for hash drift, scope
expansion, unsafe verification, or inability to bind server authority.

## Commit Prompt Readiness

- worker commit: forbidden;
- reviewer material commit: allowed only after independent acceptance;
- session sync: separate commit;
- push/public sync: unauthorized.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/orchestrator |
| Provider or surface | private local repository |
| Session or invocation | EAFR-R2 dispatch authoring, 2026-08-25 |
| Working directory | repository root |
| Command or tool surface | source reads, hashes, governed packet authoring and gates |
| Target paths | R2 baseline and work order |
| Allowed scope source | EAFR roadmap and explicit R1 waiver closure |
| Before status evidence | clean worktree at HEAD `8036abf56`; R1 closure continuity was already committed; staging empty |
| After status evidence | two dispatch artifacts pending commit |
| Diff evidence | exact dispatch document set |
| Approval boundary | R2 dispatch only |
| Claim boundary | no implementation/live/provider/public effect |
| Agent type | dispatcher |
| Invocation ID | `eafr-r2-dispatch-2026-08-25` |
| Expected manifest | baseline and work order |
| Actual changed set | baseline and work order |
| Manifest delta | NONE |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R2 dispatch authority only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: source hashes and pre-dispatch gate |
| actionEvidence | ACTION_EVIDENCE_PRESENT: committed baseline/work order after gates |
| invocationBoundary | local documentation authoring |
| interceptionBoundary | no runtime/provider/CLI/MCP interception claim |
| forbiddenExpansion | paths and effects outside exact manifest |
| claimLanguage | packet authorizes worker execution only after commit |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | external finding reverified against current CVF-owned runtime source |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing Web route, auth helpers, role resolver and durable store |
| Disposition | ADAPT into bounded CVF-owned runtime repair |
| Claim boundary | external report remains input, not authority |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: named source verification, not corpus rescan.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no complete-corpus claim.

## Epistemic Process Block

- Epistemic Process Applicability: HIGH_EVIDENCE
- Expected Result / Prediction: current source would show optional provenance,
  caller authority claims, and reusable server identity owners.
- Evidence Comparison: all three were observed at the pinned HEAD.
- Contradiction or Gap Disposition: no source contradiction; test gap accepted.
- Claim Update: R2 is ready for exact three-path worker execution after commit.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation; no public-sync authority.

## Claim Boundary

This work order authorizes only the exact three-path local R2 implementation
and deterministic verification. It authorizes no live/provider/network call,
credential or environment-file access, installation, deployment, public sync,
push, production claim, R1 waiver reuse, R1C repair, or R3 execution.
