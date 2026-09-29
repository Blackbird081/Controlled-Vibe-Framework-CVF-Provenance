# CVF Agent Work Order - EAFR-R1 AIF Reinjection Provenance Fail Closed

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Date: 2026-08-25

Batch ID: EAFR-R1-AIF-REINJECTION-PROVENANCE-FAIL-CLOSED

Dispatch base head: `80bf3e850`

Commit mode: `WORKER_MUST_NOT_COMMIT`

rawMemoryReleased=false

Worker: delegated implementation-and-test worker

Reviewer/closer: current independent orchestrator/reviewer

Worker return path: `docs/reviews/CVF_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_WORKER_RETURN_2026-08-25.md`

## Dispatch Prompt Envelope

Role: delegated worker for EAFR-R1-AIF-REINJECTION-PROVENANCE-FAIL-CLOSED.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_2026-08-25.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: packet date is 2026-08-25; verify HEAD and source hashes at start.

Do-not-misread notes: this is a two-code-path fail-closed repair, not authority
widening, threshold redesign, live proof, documentation reconciliation, or
permission to edit the execute route.

Required first actions: read `AGENTS.md`, continuity front doors, guard
orientation, literal gotchas, this work order, its baseline and roadmap, then
read checker sources named below before writing the worker return.

Return contract: implement and test only within ownership, create the worker
return, run every required gate, leave changes uncommitted, and return exactly
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

Completion review path: `docs/reviews/CVF_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_COMPLETION_2026-08-25.md`

## Purpose

Make AIF memory reinjection fail closed when an item provenance score is
missing or non-finite, and prove excluded items cannot reach selected memory or
the generated system prompt.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "EAFR-R1",
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
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts",
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.test.ts",
    "docs/reviews/",
    "docs/baselines/CVF_GC018_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_2026-08-25.md",
    "docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md"
  ],
  "claims": ["missing and non-finite provenance fails closed before memory selection and prompt composition"],
  "requiredProof": ["adversarial focused tests", "full non-live package tests", "TypeScript", "build", "unchanged consumer hash", "worker-return fast gate", "independent review"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["worker stage or commit", "route or schema edit", "policy redesign", "provider/live/network call", "credential access", "deployment", "public write"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

Expected route: `ROUTED_SHADOW`, profile `P3_ELEVATED`, selective execution
false, legacy disposition `RUN_FULL_LEGACY_BUNDLE`.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R1-AIF-REINJECTION-PROVENANCE-FAIL-CLOSED --title "CVF EAFR-R1 AIF Reinjection Provenance Fail Closed" --date 2026-08-25 --base 0fcc1dc20 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "archive hygiene closed at 0fcc1dc20" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker return profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact-two source/test ownership, adversarial matrix, hashes, commands, output contract and no-live boundary |
| checkerReadAheadConfirmation | dispatch, prompt-envelope, lifecycle, worker-return, structural, trace and finality sources routed before authoring |
| docOnlyNewFields | none |
| claimBoundary | dispatch authoring provenance only; no implementation or test PASS claim |

## Authority And Dependency

- Roadmap: `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md`.
- GC-018 baseline: `docs/baselines/CVF_GC018_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_2026-08-25.md`.
- Archive-hygiene parent: `0fcc1dc20`.

## Authority Chain

Supreme doctrine and operating model route through `AGENTS.md`, the EAFR
roadmap, paired GC-018 baseline, this committed work order, then the worker's
bounded execution. The independent reviewer alone may convert the return to
accepted closure.

## Agent Roles

| Role | Responsibility | Prohibited action |
| --- | --- | --- |
| operator | delegates roadmap authority | no routine worker intervention required |
| orchestrator/dispatcher | authors and commits authority packet | does not perform worker implementation in this tranche |
| worker | edits two owned files, tests, returns evidence | no review, closure, commit, push, live call or scope expansion |
| reviewer/closer | adversarially validates and owns accepted commit | cannot rely on worker self-attestation alone |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| roadmap R1 | roadmap row is `DISPATCH_READY` | R1 remains first executable tranche | ACCEPT |
| baseline | paired GC-018 is `DISPATCH_READY` | source facts, hashes and ownership agree | ACCEPT |
| clean parent | `git status --short` empty after `0fcc1dc20` | no pre-existing dirty worker-owned path | ACCEPT |

## Scope

Allowed paths:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.test.ts`
- `docs/reviews/CVF_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_WORKER_RETURN_2026-08-25.md`

Allowed actions: edit the helper, add focused adversarial tests, run local
deterministic package checks, create the worker return, and repair format/gate
issues inside the three allowed paths.

Forbidden scope:

- execute route, schemas, policy owner, thresholds and all other source/tests;
- roadmap, baseline, this work order, session state and governance checkers;
- provider/live/network calls, API keys, quota, deployment, public sync, push;
- commit, amend, reset, stash, cleanup of unrelated files, or broad formatting.

Risk ceiling: R2.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intake summary | source-verified AIF provenance omission repair |
| scope classification | BOUNDED_RUNTIME_SAFETY_IMPLEMENTATION |
| primary task class | implementation |
| risk sensitivity | HIGH |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| orchestration requirement | one no-commit worker plus independent reviewer/closer |
| role separation basis | worker cannot accept its own safety-boundary change |
| escalation condition | forbidden edit, wider policy change, live call, failed proof or source contradiction |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-execution`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-execution --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no defect-specific amendment required |

## Required First Reads

- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` and `CVF_SESSION_MEMORY.md` - startup continuity.
- active handoff named there - current checkpoint and parked work.
- `docs/reference/guard_orientation/README.md` - worker routing.
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` - checker-safe literals.
- paired roadmap and baseline - authority, acceptance, hashes and boundaries.
- both owned source/test files - full read before edits.
- `governance/compat/check_worker_return_quality_gate.py`, `governance/compat/check_markdown_structural_completeness.py`, `governance/compat/check_governed_artifact_checker_read_ahead.py`, `governance/compat/check_agent_operation_trace.py`, and `governance/compat/check_delta_execution_claim_boundary.py` - worker-return shape.

## Pre-Flight Checks

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
Get-FileHash -Algorithm SHA256 -LiteralPath 'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts','EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.test.ts'
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 80bf3e850 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 80bf3e850 --head HEAD --enforce
python governance/compat/check_adif_defect_registry_disclosure.py --base 80bf3e850 --head HEAD --enforce
```

Expected: current HEAD contains the committed dispatch packet, owned source
hashes match the baseline, status has no pre-existing owned changes, and every
gate passes. If not, stop and return the exact contradiction.

## Mandatory Gate-Failure Remediation Protocol

Repair failures inside allowed paths and rerun the failed command. Escalate
only for forbidden scope, changed authority/claim boundary, live credentials,
public sync, destructive action, or an unrecoverable source contradiction.

Stage nothing and commit nothing. Staged-index evidence is reviewer-owned.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| optional provenance boundary | RUNTIME_SOURCE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts` | line 7 | `provenanceScore` | `AifMemoryReinjectionItem` | ACCEPT |
| fail-open omission | RUNTIME_SOURCE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts` | line 99 | `item.provenanceScore ?? 1` | `evaluateAifMemoryReinjection` | ACCEPT |
| prompt selection seam | RUNTIME_SOURCE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts` | lines 80-136 | `eligible`, `selected`, `promptBlock` | `evaluateAifMemoryReinjection` | ACCEPT |
| existing focused suite | TEST_SOURCE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.test.ts` | lines 9-109 | four AIF tests | Vitest | ACCEPT |
| execute consumer is out of edit scope | RUNTIME_SOURCE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 746-790 | helper decision to `executeAI` | execute route | ACCEPT |

## Current Runtime Freshness Verification

Current source searches immediately before dispatch found the only omission
default at helper line 99 and no focused test for missing, undefined, `NaN`, or
infinite provenance. Worker must repeat the searches and report contradiction
if current HEAD differs.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| planned packet paths | all absent before authoring | ACCEPT |
| batch collision | `rg -n` over `docs CVF_SESSION` returned none | ACCEPT |
| wider edit need | route already consumes helper result; no route edit needed | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| omission fails closed | Acceptance Criteria | helper/test/return | focused Vitest | PASS at dispatch design level; implementation pending |
| non-finite fails closed | Acceptance Criteria | helper/test/return | focused Vitest | PASS at dispatch design level; implementation pending |
| excluded data absent from prompt | Acceptance Criteria | mixed-item test | focused Vitest | PASS at dispatch design level; implementation pending |
| independent closure | Review Gate | worker return | reviewer-return preflight | PASS |
| no live proof for R1 | Claim Boundary | command inventory | absence of network/live command | PASS |

## Worker Autonomy / No-Question Rule

Proceed autonomously for non-destructive work inside Allowed scope. Do not ask
the operator to choose routine test names, formatting repairs, or reruns.

## Commit Mode And Base-Anchor Lifecycle

- dispatchBaseHead: `80bf3e850`.
- executionBaseHead: capture current committed HEAD before any worker edit.
- closureBaseHead: reviewer captures after worker return.
- Commit mode: `WORKER_MUST_NOT_COMMIT`.
- Worker handoff is pending evidence, not closure.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this work order | reviewer converts only after accepted commit | PENDING_REVIEWER |
| Completion/reviewer artifact | named worker return | disposition, hashes, changed set, commands | REQUIRED |
| Roadmap state | EAFR roadmap | R1 row updated by reviewer only | PENDING_REVIEWER |
| Registry JSON | N/A with reason | no corpus scan or registry mutation | N/A with reason |
| Registry Markdown | N/A with reason | no corpus scan or registry mutation | N/A with reason |
| External evidence digest | N/A with reason | deterministic local proof only | N/A with reason |
| System loop interlock | N/A with reason | no scan/import loop | N/A with reason |
| Session continuity | front door, state and active handoff | reviewer-owned post-closure sync | PENDING_REVIEWER |

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts` | Yes | fail-closed validation |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.test.ts` | Yes | adversarial proof |
| `docs/reviews/CVF_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_WORKER_RETURN_2026-08-25.md` | Yes | no-commit evidence |

## Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | read/hash-only consumer |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/schema.ts` | schema change not required |
| `docs/roadmaps/`, `docs/baselines/`, `docs/work_orders/` | reviewer-owned authority |
| `CVF_SESSION/`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF*.md` | reviewer-owned continuity |
| `governance/compat/` | no checker maintenance authorized |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
| --- | --- | --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | read/hash only; do not edit/stage/claim |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | do not edit/stage/claim |

## Pre-Existing Dirty Path Exemptions

N/A with reason: dispatch parent was clean; no pre-existing dirty path is
exempted for the worker.

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| missing score exclusion | focused test | `missing_provenance_score` | Yes |
| non-finite exclusion | source and focused test | `invalid_provenance_score` | Yes |
| existing threshold behavior | focused test | `low_provenance_score` | Yes |
| no prompt-block leakage | focused test | excluded item absent from `promptBlock` | Yes |
| no receipt leakage | focused test | excluded item absent from `memoryIds` | Yes |

## Write Ownership

Owned files: the three exact paths in Required Artifact Manifest.

Forbidden paths: every other path.

Write mode: modify-listed for two existing files; create-only for worker return.

## Execution Plan

1. Capture execution base, status, hashes and required reads; stop on mismatch.
2. Add explicit missing/non-finite validation before the threshold comparison;
   preserve the optional boundary type and all existing policy behavior.
3. Add adversarial cases for omitted, explicit undefined, `NaN`, both
   infinities, zero, threshold boundary, and mixed valid/invalid selection.
4. Run focused suite, package check, full non-live suite and build after the
   last material edit; repair only inside Allowed scope.
5. Scaffold the return before long prose, fill all evidence, run its fast gate,
   record final status, and leave all work uncommitted.

## Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
| --- | --- | --- | --- |
| Scope boundary | Scope | exact three-path ownership | PASS |
| Non-goals | Design Controls | no threshold/schema/route/live work | PASS |
| Lane split | Proposed Tranches | executes R1 only | PASS |
| Dependency/source verification | Source Evidence | hashes and symbol checks | PASS |
| Claim boundary | Claim Boundary | local tested behavior only | PASS |
| Acceptance criteria | Acceptance Criteria | adversarial observable cases | PASS |
| Verification/evidence | Verification Commands | focused/full/check/build/gates | PASS |
| Dispatch readiness | R1 status | dependencies released | PASS |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Worker Return Packet Shape Contract; Agent Operation Trace Block; exact action tokens |
| gateRunPurpose | confirm and record evidence for the already source-verified packet; not first discovery |
| claimBoundary | read-ahead confirms artifact shape only, not implementation correctness |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | one worker executes; independent orchestrator reviews/closes |
| phase | implementation pending review |
| baseHeadFor(phase) | dispatchBaseHead=80bf3e850; executionBaseHead=worker captures; closureBaseHead=reviewer captures |
| changedSetScope(phase) | exact three-path manifest |
| traceScope(phase, actor) | worker local commands and diff; reviewer separate closure trace |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | parked RFR and later EAFR tranches remain untouched |
| nextMoveSurfaces | worker return, then reviewer closure packet/session sync |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | optional; prefer reviewer conversion in worker return when checker-safe |
| reviewerOwnedClosurePaths | roadmap, baseline, work order, worker return, continuity |
| closureOwner | independent orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_WORKER_RETURN_2026-08-25.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required real sections include Purpose, Scope / Methodology, Findings /
Position, Risk / Corrective Action, Decision / Disposition, External Knowledge
Intake Routing with N/A reason, Epistemic Process Block, Agent Operation Trace
Block, Delta Execution Claim Boundary Control Block, Finding-To-Governance
Learning Disposition, Command Evidence, actual git status and No-Commit Statement.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | orchestrator/dispatcher |
| Provider or surface | Codex local repository tools |
| Session or invocation | EAFR-R1 dispatch, 2026-08-25 |
| Working directory | repository root |
| Command or tool surface | read-only source searches, hashing, scaffold helper, governed file authoring and gates |
| Target paths | roadmap, baseline and this work order |
| Allowed scope source | explicit operator authority plus EAFR roadmap |
| Before status evidence | parent `80bf3e850` had a clean worktree; current `git status --short` lists the three untracked dispatch artifacts pending orchestrator commit |
| After status evidence | pending dispatch files until orchestrator commit |
| Diff evidence | `git diff --name-status` before dispatch commit |
| Approval boundary | operator delegated orchestrator authority; worker remains no-commit |
| Claim boundary | repo-local dispatch trace only; no OS/user or runtime interception attribution |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `eafr-r1-dispatch-2026-08-25` |
| Expected manifest | three dispatch authority files |
| Actual changed set | verified before dispatch commit |
| Manifest delta | NONE expected |
| Deletion or rename disposition | N/A with reason: no protected deletion or rename |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: explicit validation before the threshold check
will exclude missing/non-finite scores without changing valid-score behavior.

Evidence Comparison Requirement: worker compares focused and full results with
that prediction.

Contradiction Handling Requirement: any contrary behavior or wider edit need
requires a Contradiction Or Gap Disposition and `BLOCKED_WITH_REASON`.

Claim Update Requirement: worker marks the claim confirmed, narrowed, revised,
or invalidated; tests alone do not authorize closure.

## External Knowledge Intake Routing

Canonical chain map:
`docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`

| Field | Value |
| --- | --- |
| Chain map | CVF external knowledge absorption chain |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | advisory history is archive-only; this dispatch relies on independently verified current source |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | EAFR roadmap, paired baseline and this work order |
| Disposition | PROCEED_WITH_SOURCE_VERIFIED_LOCAL_REMEDIATION |
| Claim boundary | no archived prose is an ACCEPT authority row or runtime proof |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this is a bounded current first-party helper repair,
not legacy absorption, corpus intake, or owner-map reassessment.

## Verification Commands

```powershell
Push-Location 'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web'
npm run test:run -- src/lib/aif-memory-reinjection.test.ts
npm run check
npm run test:run
npm run build
Pop-Location
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_WORKER_RETURN_2026-08-25.md --title "CVF EAFR-R1 AIF Reinjection Provenance Fail Closed Worker Return"
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git status --short --untracked-files=all
```

Live/provider commands and API keys are forbidden in R1.

## Evidence Requirements

- exact command, cwd, exit status and test counts after the final edit;
- before/after source hashes and MATCH hash for execute route;
- receipt reason assertions and prompt/memory-id non-leak assertions;
- actual three-path changed manifest and no staged files;
- static diagnostic disposition and worker self-audit.

## Acceptance Criteria

- [ ] omitted and explicit-undefined provenance produce `missing_provenance_score`.
- [ ] `NaN`, positive infinity and negative infinity produce `invalid_provenance_score`.
- [ ] zero retains `low_provenance_score`; default-threshold `0.7` is eligible.
- [ ] mixed input selects only valid items and leaks no excluded id/summary into prompt or `memoryIds`.
- [ ] all pre-existing focused tests pass without weakened assertions.
- [ ] focused suite, typecheck, full non-live suite and build pass.
- [ ] only three owned paths changed; worker return fast gate passes.

Fail conditions: any forbidden path changes, boundary type made required instead
of receipt-producing validation, threshold/policy semantics changed, excluded
data reaches prompt, live/provider call occurs, tests/gates fail after allowed
repair, or worker commits.

## Review Gate

Implementation begins only after committed dispatch and passing
`pre-dispatch`/`pre-implementation`. Worker handoff is not closure. Reviewer
must run reviewer-return preflight, inspect source/test semantics, commit the
accepted material, run non-empty committed-range `pre-closure`, then own
roadmap and continuity conversion.

## Operator Checkpoint

operator.checkpoint.waiver: the operator delegated routine orchestrator and
reviewer decisions for this roadmap on 2026-08-25. This waiver does not permit
scope expansion, live/provider activity, credentials/quota consumption,
public sync, destructive action, or a changed claim boundary.

## Closure Checklist

- worker return status is `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`;
- all acceptance rows and command evidence are current;
- exact changed set is within ownership and unstaged;
- no live/provider/public/commit action occurred;
- reviewer independently verifies before any closed-equivalent transition.

## Return-To-Orchestrator Conditions

Return immediately for source/hash contradiction, required forbidden edit,
claim-boundary or risk change, live/provider need, irreparable gate failure,
unexpected dirty/staged state, or any inability to prove fail-closed behavior.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | local helper validation and deterministic tests only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT through exclusion reasons asserted by tests |
| actionEvidence | ACTION_EVIDENCE_PRESENT through deterministic selection and prompt assertions |
| invocationBoundary | manual local edit and test commands inside the named package |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or agent-runtime interception claim |
| claimLanguage | tested fail-closed behavior only after evidence; closure remains reviewer-owned |
| forbiddenExpansion | no threshold redesign, route/schema edit, live proof, deployment, public sync, push or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private runtime safety implementation; no public-sync action.

## Claim Boundary

This work order authorizes exactly two source/test edits, deterministic local
verification and one no-commit worker return. It does not authorize live API
use despite standing operator availability, because R1 acceptance does not
require external effect. It also does not authorize closure, commit, push,
deployment, public export, wider runtime edits, or production-readiness claims.
