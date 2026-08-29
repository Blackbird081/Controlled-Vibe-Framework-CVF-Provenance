# CVF Agent Work Order - EARTR-ESC-R1 Round-Trip 1.2 Candidate Contract Implementation

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED

Work order ID: EARTR-ESC-R1

Batch ID: EARTR-ESC-R1

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: delegated no-commit implementation worker for EARTR-ESC-R1.

Canonical packet: this work order, paired GC-018 baseline, and paired JSON task capsule.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

providerExecutionAuthority: FORBIDDEN.

Current-time notes: design review is closed `ACCEPT`; this tranche implements
only the four accepted private owners. Protocol 1.2.0 is not released by this
worker return.

Do-not-misread notes: the worker may modify four material paths and create one
evidence-only return. Public/portable projections, `EXTERNAL_AGENT_READ`,
session state, work orders, baselines, design/review evidence, schemas, hooks,
registries, and every other path are read-only.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, baseline, this work order, capsule, accepted design and closure, then
capture execution HEAD, verify all pins, ancestry, clean worktree, empty
staging, and owner collisions before edits.

Return contract: return `COMPLETE_PENDING_REVIEW` with exactly five unstaged
paths and full evidence, or `BLOCKED_WITH_REASON` when a required correction
would touch a forbidden path or change the accepted contract.

## Dispatch Metadata

Dispatch base head: `590cf8ab71805abb947a2c49b8dcc33335aadc1e`

dispatchBaseHead: `590cf8ab71805abb947a2c49b8dcc33335aadc1e`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `ab964a2764956d65000f17057033bd604f407332`

Worker: delegated implementation worker

Reviewer/closer: designated internal orchestrator/reviewer

Worker return path: `docs/reviews/CVF_EARTR_ESC_R1_ROUND_TRIP_1_2_CANDIDATE_CONTRACT_IMPLEMENTATION_WORKER_RETURN_2026-08-29.md`

workerHandoffPath: `docs/reviews/CVF_EARTR_ESC_R1_ROUND_TRIP_1_2_CANDIDATE_CONTRACT_IMPLEMENTATION_WORKER_RETURN_2026-08-29.md`

completionReviewPath: `docs/reviews/CVF_EARTR_ESC_R1_ROUND_TRIP_1_2_CANDIDATE_CONTRACT_IMPLEMENTATION_COMPLETION_2026-08-29.md`

Task capsule: `docs/work_orders/CVF_EARTR_ESC_R1_ROUND_TRIP_1_2_CANDIDATE_CONTRACT_IMPLEMENTATION_TASK_CAPSULE_2026-08-29.json`

rawMemoryReleased=false

## Purpose

Implement the accepted existing-owner enrichment for typed external absorption
candidates, provenance-lane separation, 1.1 legacy dual reading, deterministic
Local reconciliation binding, and candidate-aware validation receipts.

## Authority Chain

Operator instruction to proceed on 2026-08-29 -> externally accepted design
SHA-256 `ff3ca9815a52bcd2383f7da3f063fade6f53c02fc0d2da94972925c6c13c06c1`
-> RB-01 closure `ACCEPT` -> paired GC-018 baseline -> paired task capsule ->
this Work Order -> independent designated reviewer closure.

This chain authorizes worker implementation only inside Write Ownership. Work
Order existence does not authorize staging, commit, public/portable refresh,
push, provider use, deployment, or production claims.

## Agent Roles

- Orchestrator/dispatcher: designated internal dispatcher owns scope, source pins, and dispatch quality.
- Worker: delegated implementation worker implements/tests exactly the five no-commit output paths.
- Reviewer/closer: designated internal reviewer independently probes and accepts, repairs within the
  same boundary, or rejects the return; only the reviewer controls commits.
- Operator: reserves scope expansion, protocol design changes, new paths,
  release/public sync, provider/live work, deployment, and waivers.

## Worker Autonomy / No-Question Rule

Inside the exact five-path scope, the worker reads, implements, tests, writes
the return, and repairs routine allowed-scope failures without asking the
operator. Escalate only for source/hash mismatch, required forbidden-path
mutation, owner/design contradiction, authority expansion, external effect,
destructive action, or claim widening.

## Operator Checkpoint

Operator checkpoint: SATISFIED for this bounded worker dispatch by the
2026-08-29 instruction to proceed after external RB-01 closure
returned `ACCEPT`. A new checkpoint is required only for scope/path expansion,
new owner/schema/runtime, public/portable release, provider use, commit/push,
or a changed design invariant.

## Roadmap-To-Work-Order Trace Matrix

This work order derives from the externally accepted design decision rather
than a separate roadmap.

| Accepted design requirement | Work order section | Output | Verification | Status |
| --- | --- | --- | --- | --- |
| reuse existing protocol owner | Write Ownership; Required Implementation Contract | four existing material owners | exact changed-set and owner search | READY |
| discriminated provenance lanes | Candidate Contract | workflow, validator, tests | positive and contamination matrix | READY |
| deterministic parent-return join | Receipt And Local Binding Contract | workflow, validator, tests | manifest/receipt equality cases | READY |
| 1.2 minor plus 1.1 dual reader | Compatibility Contract | representation contract, validator, tests | legacy/strict/unsupported cases | READY |
| no parallel owner/schema/registry/runtime | Forbidden Scope | all outputs | changed-set and semantic review | READY |
| implementation remains no-commit | Return Contract | worker return | empty staging and unchanged HEAD | READY |

## Required First Reads

1. `AGENTS.md`, `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`,
   `CVF_SESSION_MEMORY.md`, and active handoff.
2. `docs/reference/guard_orientation/README.md` and
   `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
3. Paired GC-018 baseline, this work order, and paired task capsule.
4. `docs/reviews/archive/external_agent_handbacks/eartr_esc_r0_2026-08-29/CVF_EARTR_ESC_R0_SOURCE_COLLABORATION_ENRICHMENT_DESIGN_DECISION_2026-08-29.md.preserved`.
5. `docs/reviews/archive/external_agent_handbacks/eartr_esc_r0_2026-08-29/CVF_EARTR_ESC_R0_RB01_CLOSURE_CONFIRMATION_2026-08-29.md.preserved`.
6. All four material owner paths and applicable worker-return/checker sources.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| Initial external review | archived exact handback SHA-256 `b7dba25ed90931a3f6d9e52411334a8e2ac53b6c386dc7438e87f7e2b4be8d92` | ACCEPT |
| Final external review | archived exact handback SHA-256 `e466de1b97239fefb3c492d959bf49ce4e7c6c08a0d5d03f656c8d1cc732eee2` | ACCEPT_WITH_RB01_REPAIR |
| RB-01 closure | archived exact handback SHA-256 `b3b734d1ccd36a4c5dd22912bbfc0a9516a23e64b60ae1c7c8f6aca3b0dbbdda`; remaining blockers `NONE` | ACCEPT |
| Operator disposition | explicit 2026-08-29 instruction to proceed | ACCEPT_FOR_IMPLEMENTATION_DISPATCH |
| Public/portable 1.2 release | not included in worker scope | PARKED_REVIEWER_OPERATOR_CONTROLLED |

## Scaffold Provenance Block

| Field | Evidence |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EARTR_ESC_R1 --title "EARTR-ESC-R1 Round-Trip 1.2 Candidate Contract Implementation" --date 2026-08-29 --base 590cf8ab71805abb947a2c49b8dcc33335aadc1e --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added exact design/closure pins, four-owner contract, dual-reader and receipt binding matrix, five-path scope, capsule binding, and release boundary. |
| checkerReadAheadConfirmation | Dispatch, envelope, structural, operation-trace, return-quality, and task-capsule owner surfaces were read. |
| docOnlyNewFields | Candidate/receipt fields are protocol data fields implemented in existing owners; no new artifact class is introduced. |
| claimBoundary | Dispatch-authoring provenance only. |

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `Dispatch Prompt Envelope`; `Worker Return Packet Shape Contract`; `WORKER_RETURN_FULL_GATE_V1`; `Agent Handoff Contract Control Block`; `Delta Execution Claim Boundary Control Block`; `Foundation Storage Layout Block` |
| gateRunPurpose | Confirm dispatch and future worker-return shapes before implementation; gates are confirmation rather than first discovery. |
| claimBoundary | Read-ahead proves only that required checker shapes were inspected. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class "work-order-authoring" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector docs --risk-ceiling MEDIUM --json`.

## Pre-Flight Checks

Before edits, capture `executionBaseHead`, prove dispatch-base ancestry, require
a clean tracked/untracked worktree and empty staging, recompute every pin, run
the current 58-test focused suite, and validate the paired capsule. Stop on any
mismatch. Historical archived handbacks are read-only evidence.

## Execution Plan

1. Complete startup/first reads, capture `executionBaseHead`, and verify pins,
   ancestry, capsule, clean worktree, staging, and collision search.
2. Update the finding workflow and representation contract before code so the
   normative semantics are explicit.
3. Implement the smallest validator/receipt delta in
   `scripts/external_agent_packet.py`.
4. Add the complete positive/negative matrix in the existing focused test file.
5. Run focused verification, repair only allowed-scope failures, author the
   worker return last, rerun final gates, and leave all five paths unstaged.

## Source-Fidelity Pass

The worker must inspect current definitions before changing them. Do not infer
field names from review prose where current JSON uses camelCase. Documentation
and code must agree on exact names, enums, dual-reader results, receipt fields,
and claim boundaries.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| protocol version and projection synchronization owner | governed contract fact | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_PROTOCOL_REPRESENTATION_CONTRACT.md` | Protocol Identity; Update Rule | current version `1.1.0` | representation contract | ACCEPT |
| finding/local reconciliation owner | governed workflow fact | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | returned-output classification and absorption table | workflow sections | finding workflow | ACCEPT |
| current validator and receipt emitter | source fact | `scripts/external_agent_packet.py` | `validate_return` | `PROTOCOL_VERSION`; `_validate_source_rows`; receipt object | packet validator | ACCEPT |
| candidate rows currently unvalidated | source fact | `scripts/external_agent_packet.py` | `validate_return` | no semantic inspection of `suggestedAbsorptionCandidates` | packet validator | ACCEPT |
| focused fixture already uses `sources.id` | test fact | `scripts/test_external_agent_packet.py` | `_make_return` | `sources[0].id`; candidate array | focused packet tests | ACCEPT |
| accepted design | reviewed decision evidence | `docs/reviews/archive/external_agent_handbacks/eartr_esc_r0_2026-08-29/CVF_EARTR_ESC_R0_SOURCE_COLLABORATION_ENRICHMENT_DESIGN_DECISION_2026-08-29.md.preserved` | Candidate Contract; Compatibility And Dual-Reader Decision | reviewed design SHA | operator/reviewer authority chain | ACCEPT |
| RB-01 closure | reviewed closure evidence | `docs/reviews/archive/external_agent_handbacks/eartr_esc_r0_2026-08-29/CVF_EARTR_ESC_R0_RB01_CLOSURE_CONFIRMATION_2026-08-29.md.preserved` | Verdict; Remaining Blocking Findings | `ACCEPT`; `NONE` | preserved handback plus operator disposition | ACCEPT |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | external collaboration proposal -> Local current-owner reconciliation -> external adversarial closure -> operator-authorized bounded implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_PROTOCOL_REPRESENTATION_CONTRACT.md` |
| Disposition | ADAPT existing external-agent round-trip owners |
| Claim boundary | implementation dispatch only; no external-source absorption result, public release, runtime, provider, or production claim |

## Negative Search And Collision Discipline

Run:

```powershell
rg -n --hidden --no-ignore "suggestedAbsorptionCandidates|candidateContractVersion|validatedReturnManifestSha256|validatedCandidateContractVersion|EXTERNAL_SOURCE_VALUE_CANDIDATE|CVF_INTERNAL_DEFECT_CANDIDATE" docs scripts governance
```

Expected disposition: the four allowed material paths are the only current
owners requiring implementation. Public/portable representations may contain
the old collection shape but are forbidden worker paths and remain a later
release obligation, not a competing private owner.

## Pinned Input Hashes

| Path | SHA-256 |
| --- | --- |
| `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | `02c34b958dddc583295b5a7e74075b11d2de62293227e5188b66ba92e46efad5` |
| `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_PROTOCOL_REPRESENTATION_CONTRACT.md` | `40fdc125b315bf81210615e601c949a1037092dcd1ea2f24d481731ae9215bae` |
| `scripts/external_agent_packet.py` | `e0db19880a7260bb3850e87b8efd396813759fea176e3eee05683f2513b7c232` |
| `scripts/test_external_agent_packet.py` | `02c1a21e6ee53113278fc370282241d3cdb7efa0e524c898ca7b2a8cebf9db43` |
| accepted design decision | `ff3ca9815a52bcd2383f7da3f063fade6f53c02fc0d2da94972925c6c13c06c1` |
| archived RB-01 closure confirmation | `b3b734d1ccd36a4c5dd22912bbfc0a9516a23e64b60ae1c7c8f6aca3b0dbbdda` |
| paired task capsule | `4a825597f996a94ed4f7b3048bf7f358b309025c57f4db34654b11016792f529` |

## Write Ownership

Modify exactly these four material paths:

- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_PROTOCOL_REPRESENTATION_CONTRACT.md`
- `scripts/external_agent_packet.py`
- `scripts/test_external_agent_packet.py`

Create exactly this evidence-only path:

- `docs/reviews/CVF_EARTR_ESC_R1_ROUND_TRIP_1_2_CANDIDATE_CONTRACT_IMPLEMENTATION_WORKER_RETURN_2026-08-29.md`

Every other path is read-only. Do not stage or commit.

## Forbidden Scope

- No new file beyond the worker return.
- No new schema, registry, protocol/profile, runtime, truth, receipt, authority,
  lifecycle, or state-machine owner.
- No edit to public guides, portable packet files, `EXTERNAL_AGENT_READ`, task
  capsule, baseline, Work Order, design/review evidence, session state, handoff,
  hooks, autorun, CI, or public-sync clone.
- No network/provider/credential access, publication, push, deploy, destructive
  action, or release/readiness claim.
- No refactor unrelated to candidate validation and Local receipt binding.

## Candidate Contract

Use exact camelCase JSON fields and top-level
`candidateContractVersion: 1`. Under strict v1, validate every non-empty row
as exactly one variant.

`EXTERNAL_SOURCE_VALUE_CANDIDATE` requires candidate ID, source refs, source
locations bound to source refs, neutral summary, claimed value, public owner
search, bounded public overlap, preliminary value disposition, and Local
questions. Enforce unique return-local IDs, source-ID existence, safe paths,
nonblank symbols/text, bounded enums, and exact set equality between
`sourceRefs` and `sourceLocations[].sourceRef`.

`CVF_INTERNAL_DEFECT_CANDIDATE` requires candidate ID, `cvfPublicLocations`,
neutral defect hypothesis, public owner search, and Local questions. Optional
`triggerContextSourceRefs` are non-evidentiary and must resolve when present.
Prohibit `sourceLocations`, `claimedValue`, `publicOverlap`, and
`preliminaryValueDisposition` in this lane. Bind CVF paths to top-level
`cvfPublicSource`; do not synthesize a CVF row in external `sources`.

Parent `authorityStatus` governs all rows. Do not add per-row authority status.
Free-text `sourceEvidence`, if retained, is summary-only and never substitutes
for normalized source identity/locations.

## Compatibility Contract

- Bump protocol owner and validator `PROTOCOL_VERSION` to `1.2.0`.
- Retain `cvf.externalAgentReturn.v1`.
- Every new 1.2 producer emits `candidateContractVersion: 1`, including an
  empty candidate array.
- Absent discriminator plus empty array: `LEGACY_EMPTY` read compatibility.
- Absent discriminator plus non-empty array:
  `LEGACY_UNTYPED_NOT_PROMOTABLE`; preserve as historical evidence, do not
  treat as typed candidates.
- Discriminator 1: `STRICT_V1`; validate every row fail closed.
- Unsupported/malformed discriminator: `UNSUPPORTED_OR_MALFORMED` and
  `RETURN_FOR_REPAIR`; never downgrade to legacy.

Do not update or claim release of public/portable projections. The protocol
contract must state that 1.2 remains unreleased until reviewer-controlled
same-release projection refresh is completed.

## Receipt And Local Binding Contract

The validation receipt must bind the exact bytes of
`EXTERNAL_AGENT_RETURN_MANIFEST.json` and expose machine-visible fields
equivalent to:

```json
{
  "validatedReturnManifestSha256": "<64-lowercase-hex>",
  "validatedProtocolVersion": "1.2.0",
  "validatedCandidateContractVersion": 1,
  "status": "PASS"
}
```

For legacy/untyped input, record an explicit non-strict candidate status and
do not claim candidate contract v1 was enforced. A candidate-unaware or legacy
PASS cannot open typed Local reconciliation.

The finding workflow must require Local reconciliation to verify:

```text
externalReturnBinding.returnManifestSha256
  == receipt.validatedReturnManifestSha256
externalReturnBinding.candidateContractVersion
  == receipt.validatedCandidateContractVersion
receipt.status == PASS
receipt.validatedProtocolVersion == 1.2.0
receipt.validatedCandidateContractVersion == 1
```

The effective row key remains `(returnManifestSha256, candidateId)`. No global
candidate ID or registry is allowed. `implementationAuthorized: false` is an
artifact invariant; Operator selection, owner binding, and Work Order existence
remain distinct from implementation authority.

## Required Test Matrix

Add focused tests for at least:

- valid strict-v1 empty collection and both valid candidate variants;
- duplicate candidate IDs;
- mixed/forbidden lane fields;
- missing required fields, blank text, unsafe paths, invalid enum values;
- missing source ID, unresolved location ref, source-set mismatch;
- fake missing-owner path and unresolved owner search without Local question;
- legacy empty acceptance and legacy non-empty not-promotable behavior;
- malformed/unsupported discriminator;
- strict-v1 invalid row fail closed;
- receipt exact-manifest hash, protocol version, candidate version, and PASS;
- receipt for another manifest;
- receipt candidate-version mismatch;
- strict-v1 manifest paired with candidate-unaware legacy PASS;
- no semantic acceptance or authority widening from validation PASS;
- all existing 58 focused tests remain passing.

Use existing fixtures/helpers and the existing test module. Do not create a
second test owner.

## Evidence Requirements

The worker return must record exact commands and exit codes, before/after
focused test counts, all pinned hashes, execution start/finish timestamps with
timezone, `executionBaseHead`, final HEAD, exact changed paths, empty staging,
`git diff --check`, candidate/receipt negative cases exercised, worker-found
corrections, collisions, escalations, and remaining limitations. Self-report
is pending evidence only until independent reviewer assessment.

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_EARTR_ESC_R1_ROUND_TRIP_1_2_CANDIDATE_CONTRACT_IMPLEMENTATION_COMPLETION_2026-08-29.md`

reviewerOwnedClosurePaths: exact five worker paths plus a separate reviewer-owned
completion review if accepted; any continuity or representation-release paths
require separate reviewer/operator authority.

Completion review ownership belongs only to the designated reviewer; the
delegated output is a worker handoff artifact. The reviewer captures a fresh
closure base, independently tests the
pending diff, repairs only within the same five-path boundary if necessary,
and owns acceptance, commit, session sync, and any later representation-release
decision.

## Review Gate

The designated reviewer must independently inspect all four material diffs, rerun focused tests,
probe both candidate lanes, every dual-reader state, receipt/manifest/version
mismatches, source-set equality, legacy non-promotion, and authority boundaries.
Any HIGH/CRITICAL semantic defect returns the tranche; bounded allowed-scope
repair must be disclosed. No protocol-release claim is accepted without later
public/portable synchronization evidence.

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return, read checker source as applied to that exact
review path, including `check_worker_return_quality_gate.py`,
`check_markdown_structural_completeness.py`,
`check_external_knowledge_intake_routing.py`,
`check_finding_to_governance_learning.py`, and
`check_agent_operation_trace.py`. Extract required headings and literal tokens
before authoring; do not rely on memory or leave placeholders.

## Required Artifact Manifest

| Artifact | Required worker action |
| --- | --- |
| finding absorption workflow | add discriminated provenance lanes, deterministic parent-return join, Local equality checks, and authority boundary |
| protocol representation contract | set target 1.2.0 semantics, dual-reader compatibility, candidate discriminator, receipt binding, and unreleased projection boundary |
| packet validator | implement strict/legacy candidate validation and exact candidate-aware receipt evidence |
| focused packet tests | implement positive and negative matrix in the existing test owner |
| worker return | record no-commit implementation evidence and exact changed set |

Forbidden paths: every path not listed in Write Ownership.

## Work-Order Fulfillment Manifest

The Required Artifact Manifest is complete: four modified existing owner paths
and one created evidence-only worker return. No substitute or additional path
is allowed. A required protected-path edit is a stop condition, not implied
scope expansion.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_EARTR_ESC_R1_ROUND_TRIP_1_2_CANDIDATE_CONTRACT_IMPLEMENTATION_WORKER_RETURN_2026-08-29.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --pytest-target scripts/test_external_agent_packet.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must be self-declared as a worker-return artifact, name this
Work Order, and include Purpose, Scope / Methodology, Findings / Position, Risk
/ Corrective Action, Checker Source Read-Ahead Block, Agent Operation Trace
Block, Delta Execution Claim Boundary Control Block, Public Export Disposition,
External Knowledge Intake Routing, Finding-To-Governance Learning Disposition,
Epistemic Process Block, Machine Closure Package, Claim Boundary,
`git status --short`, Changed Files, Worker Experience Retrospective, Command
Evidence, and No-Commit Statement. Use `N/A with reason` only where truthful.

Record start/finish timestamps, `executionBaseHead`, all first-run and final-run
results, exact changed paths, empty staging, current HEAD unchanged, any worker
corrections, collisions/escalations, and honest remaining limitations.

## Verification Commands

Pre-implementation, before edits:

```powershell
git rev-parse HEAD
git merge-base --is-ancestor 590cf8ab71805abb947a2c49b8dcc33335aadc1e HEAD
git status --short
git diff --cached --name-only
python -m pytest scripts/test_external_agent_packet.py -q
python -c "import json; from pathlib import Path; from scripts.external_agent_packet import _validate_capsule; p=Path(r'docs/work_orders/CVF_EARTR_ESC_R1_ROUND_TRIP_1_2_CANDIDATE_CONTRACT_IMPLEMENTATION_TASK_CAPSULE_2026-08-29.json'); _validate_capsule(json.loads(p.read_text(encoding='utf-8'))); print('CAPSULE_SCHEMA_PASS')"
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 590cf8ab71805abb947a2c49b8dcc33335aadc1e --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 590cf8ab71805abb947a2c49b8dcc33335aadc1e --head HEAD --enforce
```

After the last material edit and again after writing the worker return:

```powershell
python -m pytest scripts/test_external_agent_packet.py -q
python governance/compat/run_worker_return_fast_gate.py --pytest-target scripts/test_external_agent_packet.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <executionBaseHead> --head HEAD
git diff --check
git diff --name-only
git diff --cached --name-only
git status --short
git rev-parse HEAD
```

The worker must recompute the seven pinned SHA-256 inputs before editing and
stop on mismatch. Provider and network execution are forbidden.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "EARTR-ESC-R1",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "ENRICHES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": ["docs/baselines", "docs/work_orders", "docs/reference/external_agent_review", "scripts", "docs/reviews"],
  "claims": ["typed candidate validation and receipt binding in existing owners"],
  "requiredProof": ["focused positive/negative tests", "exact changed-set evidence", "independent reviewer probes"],
  "operatorCheckpoints": ["independent review before commit", "operator/reviewer authorization before representation release"],
  "forbiddenEffects": ["network/provider use", "packet/public mutation", "push/deploy", "worker commit"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: bounded named-owner implementation",
    "completenessClaimChanged": false
  }
}
```

Expected route: `P3_ELEVATED`; the full existing governance bundle remains
authoritative.

## Intake Role Routing Decision

| Field | Assignment |
| --- | --- |
| selected role route | MULTI_AGENT_SINGLE_ROLE |
| intake summary | operator-authorized implementation of an externally reviewed existing-owner protocol enrichment |
| scope classification | local five-path no-commit contract/code/test implementation |
| worker role | delegated implementation worker |
| reviewer role | designated internal orchestrator/reviewer/closer |
| escalation condition | source mismatch, forbidden edit, owner/design contradiction, authority expansion, or external effect |
| risk sensitivity | strict protocol/receipt contract change; local reversible tests; no external effect |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: EARTR-ESC-R1 implements a reviewed current-owner
round-trip enrichment and makes no legacy-corpus, foundation-plane, or
workflow-chain coverage-index claim. Legacy 1.1 return compatibility is a
bounded protocol-reader behavior, not a corpus absorption assertion.

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Planned durable reference folder | NOT_APPLICABLE_WITH_REASON: no new durable folder; two current reference owners are modified in place |
| Planned front door/index | NOT_APPLICABLE_WITH_REASON: no new front door or index is created |
| Date policy | NOT_APPLICABLE_WITH_REASON: existing undated canonical owner filenames are retained |
| Owner surface | existing finding-workflow and protocol-representation contract paths in Write Ownership |
| Claim boundary | no foundation split, relocation, new index, or storage-owner change |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> delegated implementation worker -> independent reviewer/closer |
| phase | pre-dispatch; worker execution; reviewer closure |
| baseHeadFor(phase) | dispatchBaseHead=`590cf8ab71805abb947a2c49b8dcc33335aadc1e`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| changedSetScope(phase) | dispatch packet/evidence only before worker; exact five worker paths during execution; reviewer-owned completion path only after acceptance |
| traceScope(phase, actor) | dispatcher records dispatch evidence; worker records implementation/return evidence; reviewer records independent closure evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/committer owns any accepted commit |
| crossBatchIsolation | worker execution requires a clean worktree at start and must not absorb unrelated changes |
| nextMoveSurfaces | worker return -> reviewer completion decision -> separately authorized representation release or bounded park |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | designated internal orchestrator/dispatcher/reviewer |
| Provider or surface | local private-provenance repository |
| Session or invocation | EARTR-ESC-R1 worker dispatch, 2026-08-29 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | governed reads, `rg`, Git, ADIF resolver, scaffold inspection, capsule validation, focused pytest, `apply_patch` |
| Target paths | paired baseline, this Work Order, paired capsule; worker owns four material paths plus one return |
| Allowed scope source | operator instruction after externally accepted RB-01 closure |
| Before status evidence | dispatcher pending batch contains only intended dispatch/evidence paths; worker precondition requires a clean worktree after dispatch commit; source pins recorded at base `590cf8ab71805abb947a2c49b8dcc33335aadc1e`; focused tests 58/58 PASS |
| After status evidence | dispatch packet only; implementation not yet executed |
| Diff evidence | exact dispatch-author manifest and pre-dispatch gates |
| Approval boundary | no-commit private implementation only; public/portable release and every external effect remain closed |
| Claim boundary | dispatch readiness only, not implementation correctness or protocol release |
| Agent type | orchestrator/dispatcher/reviewer |
| Invocation ID | `eartr-esc-r1-worker-dispatch-2026-08-29` |
| Expected manifest | paired baseline; this Work Order; paired capsule; accepted design/review evidence |
| Actual changed set | paired baseline; this Work Order; paired capsule; accepted design/review evidence |
| Manifest delta | MATCH |
| Deletion or rename disposition | completed external handbacks/prompts archived byte-for-byte; no content deletion |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | pending local four-owner protocol/validator implementation and focused tests |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: implementation candidate pending independent review |
| receiptEvidence | CVF_RECEIPT_PRESENT at contract/test level only; no real external return is accepted by this tranche |
| actionEvidence | ACTION_EVIDENCE_PRESENT through exact pending diff, focused test output, worker return, empty staging, and unchanged HEAD |
| invocationBoundary | local Python/pytest/governance commands only; no provider, network, public, or portable invocation |
| interceptionBoundary | validator parses supplied local return folders only; no daemon, hook, runtime interception, or automatic admission |
| claimLanguage | use implemented/tested locally only when supported; never released, public-ready, production-ready, or semantically accepted |
| forbiddenExpansion | no candidate value acceptance, authority promotion, public/portable release, new owner/schema/registry/runtime, commit, push, or deploy |

## Acceptance Criteria

All Candidate, Compatibility, Receipt/Local Binding, and Required Test Matrix
requirements are satisfied; all focused tests pass; no forbidden path changes;
worker return is structurally complete; changed set is exactly five paths;
staging is empty; HEAD is unchanged from `executionBaseHead`; and claims remain
bounded to pending local implementation.

## Closure Checklist

- [x] Worker captured execution base and verified every pin before edits.
- [x] Exactly four original material owner paths and one worker return were produced; Amendment 1 added six authorized checker/test paths.
- [x] Focused tests and worker-return full gate pass after the last edit.
- [x] Staging was empty and HEAD equaled execution base at worker return.
- [x] Reviewer independently verified semantics and the exact amended changed set.
- [x] Reviewer-owned completion record was created after acceptance.
- [x] Public/portable release remains explicitly parked until opened later by
      separate authority and same-release synchronization evidence.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all worker-owned acceptance criteria
pass and the exact five paths are unstaged. Return `BLOCKED_WITH_REASON` for a
pin mismatch, owner/design contradiction, or required forbidden-path change.
Do not return a preference question for an allowed-scope formatting, test, or
machine-gate repair.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this Work Order | `Status: CLOSED_PASS_BOUNDED`; closure base and checklist finalized | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_EARTR_ESC_R1_ROUND_TRIP_1_2_CANDIDATE_CONTRACT_IMPLEMENTATION_COMPLETION_2026-08-29.md` | `REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED`; final tests and reviewer repair recorded | PASS |
| Roadmap state | N/A with reason: this bounded implementation was not assigned a new roadmap owner | no downstream roadmap dependency created | N/A with reason |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | aggregate drift check PASS; no source-entry mutation | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | unchanged projection remains aligned | PASS |
| External evidence digest | N/A with reason: no new external evidence was ingested during implementation | dispatch already pins preserved design/review hashes | N/A with reason |
| System loop interlock | N/A with reason: existing round-trip chain is enriched without a new loop edge | no interlock mutation required | N/A with reason |
| Session continuity | active handoff | reviewer-owned handoff-only sync follows material closure | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
| --- | --- | --- | --- |
| exact return binding | manifest binding equals receipt validated-manifest SHA-256 | exact manifest-byte digest is emitted and equality-tested | PASS |
| validator protocol | `1.2.0` | `validatedProtocolVersion: 1.2.0` | PASS |
| strict candidate contract | `1` | strict-v1 receipt records `validatedCandidateContractVersion: 1`; legacy records null | PASS |
| validation result | `PASS` | typed reconciliation opens only for `status: PASS` | PASS |

## Claim Boundary

This Work Order authorizes a bounded local no-commit implementation candidate.
It does not itself authorize implementation outside Write Ownership, protocol
release, public/portable refresh, `EXTERNAL_AGENT_READ` update, public sync,
commit, push, provider call, deployment, production use, or semantic
acceptance of any future external candidate.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private implementation dispatch. Public/portable projection
refresh remains a separately reviewed post-acceptance release obligation.
