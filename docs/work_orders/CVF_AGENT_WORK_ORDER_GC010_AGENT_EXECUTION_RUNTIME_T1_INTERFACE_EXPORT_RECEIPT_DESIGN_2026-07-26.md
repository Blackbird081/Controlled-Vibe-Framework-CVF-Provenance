# CVF Agent Work Order - GC010 AgentExecutionRuntime T1 Interface Export Receipt Design

Memory class: governed-worker-dispatch

Status: REVIEWER_ACCEPTED_DISPATCH_READY

Batch ID: GC010-AER-T1

Dispatch base head: `0b55e74d8`

dispatchBaseHead: `0b55e74d8`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_MUST_CAPTURE_AFTER_WORKER_RETURN

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: one Claude documentation worker

Reviewer/closer: Codex

Worker return path: `docs/reviews/CVF_GC010_AGENT_EXECUTION_RUNTIME_T1_INTERFACE_EXPORT_RECEIPT_DESIGN_WORKER_RETURN_2026-07-26.md`

## Dispatch Prompt Envelope

Role: Claude documentation worker for `GC010-AER-T1`.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_AGENT_EXECUTION_RUNTIME_T1_INTERFACE_EXPORT_RECEIPT_DESIGN_2026-07-26.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Current-time notes: GC010-AER-T0 closed at material commit `c9e246553` and
continuity commit `0b55e74d8`. It accepted only partial readiness and released
this documentation design prerequisite.

Do-not-misread notes: design exact future contracts on paper. Do not create or
edit runtime, tests, providers, package exports, CLI/MCP, Web, public, or
session surfaces. Do not claim a caller or durable receipt exists.

Required first actions: capture clean HEAD, read every required source, confirm
both outputs are absent, reproduce searches, and run pre-implementation before
writing.

Return contract: create exactly the two output files, run the full worker-return
fast gate, do not stage or commit, and return one allowed terminal disposition.

## Purpose

Remove the remaining design ambiguity before a fresh GC-010 implementation
packet: exact owner path/API, canonical engine and provider ownership, durable
receipt port, export manifest, deterministic tests, failure behavior, and
rollback.

## Authority Chain

- operator instruction to continue after GC010-AER-T0 acceptance;
- baseline:
  `docs/baselines/CVF_GC018_GC010_AGENT_EXECUTION_RUNTIME_T1_INTERFACE_EXPORT_RECEIPT_DESIGN_2026-07-26.md`;
- completion:
  `docs/reviews/CVF_GC010_AGENT_EXECUTION_RUNTIME_T0_OWNER_PROVIDER_RECEIPT_DECISION_COMPLETION_2026-07-26.md`;
- roadmap:
  `docs/roadmaps/CVF_GC009_GC010_PRODUCTION_CALLER_AND_BOUNDED_E2E_RUNTIME_ROADMAP_2026-07-25.md`.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition | Status |
|---|---|---|---|---|
| T0 independent closure | companion T0 completion | `c9e246553` | bounded partial-ready; design required before implementation | PASS |
| Continuity | active session state | `0b55e74d8` | this design packet is the exact next move | PASS |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | exact package-native owner, export, receipt, and proof design |
| scopeClassification | documentation-only interface and adapter contract |
| riskSensitivity | R2 because acceptance may release later implementation authoring |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | Codex dispatches; Claude designs; Codex independently reviews |
| escalationCondition | source contradiction or need beyond exact two-path scope |

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | authorizes continued value-seeking work |
| Codex dispatcher | source-verifies, gates, commits, and dispatches |
| Claude worker | creates exactly two documentation outputs; no commit |
| Codex reviewer/closer | recomputes evidence, repairs, decides, commits, and syncs |

## Scope

Allowed:

1. Read named current source and accepted T0 artifacts.
2. Define an exact future owner module and factory/lifecycle API.
3. Define canonical engine and provider/config/credential/model ownership.
4. Define a durable requestId-correlated receipt port and terminal writes.
5. Define exact barrel/package export additions.
6. Define exact implementation/test manifest and rollback boundary.
7. Select one design-readiness token.

Forbidden:

- any edit or execution under `EXTENSIONS/**`;
- tests, builds, providers, network, browser, CLI/MCP, benchmark, release bundle;
- package, export, roadmap, baseline, work-order, system-chain, session, public,
  push, deploy, or production change;
- inventing proposed fields as existing source facts;
- composing into the GC-009 Web execute route;
- staging or commit.

## Write Ownership

Worker-owned create-only paths:

1. `docs/audits/CVF_GC010_AGENT_EXECUTION_RUNTIME_T1_INTERFACE_EXPORT_RECEIPT_DESIGN_2026-07-26.md`
2. `docs/reviews/CVF_GC010_AGENT_EXECUTION_RUNTIME_T1_INTERFACE_EXPORT_RECEIPT_DESIGN_WORKER_RETURN_2026-07-26.md`

Everything else is read-only or forbidden.

## Required First Reads

1. startup front doors and active handoff;
2. guard orientation and governed literal-format gotchas;
3. baseline, this work order, roadmap, T0 audit, T0 return, T0 completion;
4. `agent-execution-runtime.ts` and its isolated test;
5. both provider adapter source files and tests;
6. guard-contract barrel and package manifest;
7. canonical engine and `createGuardEngine`;
8. governed launcher plus JSON execution store as receipt references;
9. paired system-chain gap;
10. applicable checker sources below.

## Pre-Flight Checks

1. Capture clean `executionBaseHead`.
2. Confirm both outputs are absent.
3. Reproduce constructor and export searches.
4. Run pre-implementation with the captured execution base.
5. Stop on drift, collision, source contradiction, or forbidden-path need.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T0 releases design only | VALUE_SET | `docs/reviews/CVF_GC010_AGENT_EXECUTION_RUNTIME_T0_OWNER_PROVIDER_RECEIPT_DECISION_COMPLETION_2026-07-26.md` | Successor Boundary | `PARTIAL_READY_REQUIRES_EXPORT_OR_RECEIPT_DESIGN` | completion review | ACCEPT |
| Runtime pipeline exists | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | class; `run` | `AgentExecutionRuntime` | agent runtime | ACCEPT |
| Engine/provider/config constructor exists | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | constructor | `constructor` | agent runtime | ACCEPT |
| Provider interface exists | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | interface | `ExecutionProvider` | provider contract | ACCEPT |
| In-memory log is insufficient | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | field; getter | `executionLog` | agent runtime | ACCEPT |
| Package export is absent | VALUE_SET | `docs/reviews/CVF_GC010_AGENT_EXECUTION_RUNTIME_T0_OWNER_PROVIDER_RECEIPT_DECISION_COMPLETION_2026-07-26.md` | Findings / Position | `AgentExecutionRuntime` | accepted T0 source decision | ACCEPT |
| JSON durable store exists as reference | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts` | interface; class | `GovernedExecutionStore`; `JsonGovernedExecutionStore` | launcher persistence | ACCEPT |
| Gap remains open | VALUE_SET | `docs/reference/system_chain/gaps/entries/gc009_gc010_no_production_caller.json` | `actionOwner`; `closeCondition` | `currentStatus` | gap entry | ACCEPT |

## New Doc-Only Fields

| Proposed item | Meaning | Runtime/source status |
|---|---|---|
| `ownerModulePath` | exact future module path | DOC_ONLY_NEW |
| `ownerFactorySignature` | exact factory and lifecycle API | DOC_ONLY_NEW |
| `receiptPortContract` | terminal durable write contract | DOC_ONLY_NEW |
| `providerSelectionContract` | selection and secret-ownership boundary | DOC_ONLY_NEW |
| `exportManifest` | exact future package surface additions | DOC_ONLY_NEW |
| `deterministicProofManifest` | exact future tests and assertions | DOC_ONLY_NEW |

## Current Runtime Freshness Verification

At dispatch base `0b55e74d8`, direct searches still find six constructor calls
only in test files and no `AgentExecutionRuntime` export in the package barrel
or manifest. The runtime constructor still accepts engine, provider, and
config; `run` still performs one direct pre-check call; `executionLog` remains
in-memory. The worker must recompute these facts at its captured execution
base rather than relying on this dispatch-time record.

## Required Design Questions

1. What exact future module path owns construction and lifecycle?
2. What exact exported factory/type signatures are proposed?
3. Which canonical engine source is supplied and is it singleton or per-owner?
4. Who selects provider adapter, model, config, and credentials, without
   embedding secrets?
5. What exact receipt-port input/result schema persists every terminal outcome
   using `requestId`?
6. At what exact points are ALLOW, BLOCK, approval, provider failure,
   post-check invalidity, and thrown guard errors written durably?
7. Does standard-mode ESCALATE execute, block, or require approval in the
   proposed contract, and why?
8. Does invalid post-check become terminal or advisory, and why?
9. What exact `src/index.ts`, `package.json.exports`, and `package.json.files`
   additions are required?
10. What exact future source/test/package manifest is smallest and complete?
11. What deterministic tests prove one guard evaluation, ALLOW provider once,
    BLOCK/approval provider zero, durable writes, correlation, and failures?
12. What is the rollback boundary and which evidence becomes stale?
13. Does the complete design avoid the GC-009 Web route and MCP-local engine?
14. Which terminal design-readiness token is supported?

## Terminal Design-Readiness Enum

Record exactly one:

- `DESIGN_SPEC_READY_FOR_FRESH_GC010_IMPLEMENTATION_PACKET`
- `PARTIAL_DESIGN_REQUIRES_FURTHER_SOURCE_DECISION`
- `NOT_READY_DESIGN_CONTRADICTION`
- `NO_CURRENT_VALUE_WITH_REOPEN_CONDITION`

The first token releases only authoring of a fresh implementation packet. It
does not release implementation itself.

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `docs/audits/CVF_GC010_AGENT_EXECUTION_RUNTIME_T1_INTERFACE_EXPORT_RECEIPT_DESIGN_2026-07-26.md` | Yes | fourteen-question source-bounded design specification |
| `docs/reviews/CVF_GC010_AGENT_EXECUTION_RUNTIME_T1_INTERFACE_EXPORT_RECEIPT_DESIGN_WORKER_RETURN_2026-07-26.md` | Yes | full-profile no-commit return |

## Work-Order Fulfillment Manifest

The Required Artifact, Forbidden Path, Forbidden Filesystem State, and
Required Proof manifests together define the complete worker handoff.

## Forbidden Path Manifest

| Path or class | Required disposition |
|---|---|
| `EXTENSIONS/**` | no change |
| package, exports, source, tests | no change |
| governance, roadmap, baseline, work order | no worker change |
| system-chain and session surfaces | no worker change |
| public, provider, CLI/MCP, deployment | no action |

## Forbidden Filesystem State At Dispatch

| Canonical output | Required state | Observed state | Disposition |
|---|---|---|---|
| audit output | ABSENT | ABSENT at packet authoring | PASS |
| worker-return output | ABSENT | ABSENT at packet authoring | PASS |

## Required Proof Manifest

| Proof | Path | Atomic literal | Required |
|---|---|---|---|
| owner contract | audit | `ownerModulePath` | Yes |
| receipt contract | audit | `receiptPortContract` | Yes |
| export design | audit | `exportManifest` | Yes |
| proof design | audit | `deterministicProofManifest` | Yes |
| no-commit evidence | worker return | `WORKER_MUST_NOT_COMMIT honored` | Yes |

## Evidence Requirements

- direct current-source citations for every existing symbol;
- proposed symbols only in doc-only tables;
- exact field tables, signatures, manifests, and test assertions;
- explicit fact versus design decision versus inference classification;
- exact two-path status and no staging/commit;
- no live, runtime, provider, public, or production claim.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order section | Output | Verification | Status |
|---|---|---|---|---|
| design prerequisite | questions 1-14 | exact contract audit | reviewer semantic check | PASS pending worker |
| durable receipt | questions 5-6 | field and write-point tables | source/reference citations | PASS pending worker |
| export decision | question 9 | exact manifest | package source comparison | PASS pending worker |
| proof and rollback | questions 10-12 | manifest and assertions | reviewer diff gate | PASS pending worker |

## Agent Handoff Contract Control Block

Contract source:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> one documentation worker -> independent reviewer/closer |
| phaseDisposition | dispatch, worker return, reviewer closure |
| baseHeadFor(phase) | dispatch=`0b55e74d8`; implementation=worker-captured clean HEAD; closure=reviewer-captured worker return base |
| changedSetScope(phase) | dispatch=three packet paths; worker=exact two outputs; closure=reviewer-owned conversion paths |
| traceScope(phase, actor) | worker records exact two-path before/after trace; reviewer records closure trace |
| commitOwner(phase) | dispatch=Codex; worker=FORBIDDEN; closure=Codex reviewer/closer |
| crossBatchIsolation | no unrelated path may enter the worker set |
| nextMoveSurfaces | Codex updates only after independent acceptance |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_GC010_AGENT_EXECUTION_RUNTIME_T1_INTERFACE_EXPORT_RECEIPT_DESIGN_COMPLETION_2026-07-26.md` |
| reviewerOwnedClosurePaths | worker outputs, completion, work order, roadmap, applicable gap and continuity surfaces |
| closureOwner | Codex |
| workerCommitPermission | FORBIDDEN |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: owner/export/receipt source facts may drift and proposed
contracts require current-source comparison.

| Field | Value |
|---|---|
| prior evidence | T0 audit and completion orient the design |
| reuse | no current source fact may be accepted without recomputation |
| tests/live | test source read only; no execution |
| encoding | ASCII default |
| exception | N/A with reason: none |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_GC010_AGENT_EXECUTION_RUNTIME_T1_INTERFACE_EXPORT_RECEIPT_DESIGN_WORKER_RETURN_2026-07-26.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

requiredEvidenceTerms: executionBaseHead; git status --short; git diff
--name-status; git diff --cached --name-status; git diff --check; constructor
search; export search; source citations; governed file size; no live provider;
no commit.

requiredSections: Purpose; Scope / Methodology; Findings / Position; Risk / Corrective Action; Claim Boundary; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package; Changed Files; Worker Experience Retrospective; Command Evidence; No-Commit Statement

naInstruction: use `N/A with reason` only when genuinely not applicable.

## Verification Commands

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
rg -n "new AgentExecutionRuntime" EXTENSIONS --glob "!**/node_modules/**" --glob "!**/dist/**" --glob "!**/coverage/**"
rg -n "agent-execution-runtime|AgentExecutionRuntime" EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts EXTENSIONS/CVF_GUARD_CONTRACT/package.json
git diff --check
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git diff --cached --name-status
git status --short
git rev-parse --short HEAD
```

Do not execute application tests, providers, network, browser, CLI/MCP,
benchmarks, or release bundles.

## Acceptance Criteria

- [ ] exact two worker outputs;
- [ ] all fourteen questions answered;
- [ ] exact signatures, schemas, manifests, tests, and rollback;
- [ ] exactly one terminal token;
- [ ] no forbidden path or action;
- [ ] gates pass; worker HEAD unchanged; nothing staged.

## Execution Plan

1. Capture clean execution base and run pre-implementation.
2. Recompute source facts and negative searches.
3. Draft only the audit and worker return.
4. Run size, fast, diff, staging, and status checks.
5. Return one terminal worker disposition without committing.

## Review Gate

Codex independently checks source accuracy, design completeness,
non-duplication, durable evidence semantics, exact manifests, and gates.

## Closure Checklist

- [ ] worker started clean;
- [ ] exact two outputs;
- [ ] fourteen questions and one design token;
- [ ] no forbidden action;
- [ ] worker fast gate passes;
- [ ] no staging or worker commit.

## Return-To-Orchestrator Conditions

Return blocked only for stale base, source drift, required scope expansion, or
insufficient source evidence. Name the exact condition and stop.

## Operator Checkpoint

Worker execution proceeds under the committed packet without expanding scope.
Independent Codex acceptance is required before implementation packet
authoring.

## Worker Autonomy / No-Question Rule

Repair allowed two-path formatting and checker defects directly. Do not ask
the operator to select design details or the terminal token.

## Terminal Worker Disposition Enum

Return exactly one:

- `COMPLETE_PENDING_REVIEW`
- `BLOCKED_STALE_EXECUTION_BASE`
- `BLOCKED_SOURCE_DRIFT`
- `BLOCKED_SCOPE_EXPANSION_REQUIRED`
- `BLOCKED_DECISION_INSUFFICIENT_EVIDENCE`

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039,
ADIF-0043, ADIF-0049, ADIF-0006

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json --max-results 50` |
| Returned defect count | 20 |
| Disclosed defectIds | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006 |
| Dispatch impact | exact source verification, doc-only proposals, no-commit manifest, and proof terms are explicit |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | status, source table, ADIF query, manifests, no-commit route, full return contract, ASCII |
| gateRunPurpose | confirm work-order dispatch shape after direct source verification |
| claimBoundary | gate compliance does not prove design readiness |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude documentation worker |
| Provider or surface | Claude through operator copy/paste |
| Session or invocation | GC010-AER-T1, 2026-07-26 |
| Working directory | repository root |
| Command or tool surface | read-only source/git inspection, searches, two doc edits, governance gates |
| Target paths | exact two worker paths |
| Allowed scope source | committed work order |
| Before status evidence | clean captured execution base |
| After status evidence | two added unstaged docs |
| Diff evidence | git status and diff commands |
| Approval boundary | documentation design only |
| Claim boundary | no implementation, execution, receipt, export, or closure |
| Agent type | documentation worker |
| Invocation ID | `gc010-aer-t1-claude-2026-07-26` |
| Expected manifest | audit and return |
| Actual changed set | worker records |
| Manifest delta | none required |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | documentation-only interface/export/receipt design |
| claimDisposition | CLAIM_REJECTED: no runtime control is implemented |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION |
| invocationBoundary | local read-only inspection |
| interceptionBoundary | no provider, CLI/MCP, Web, or process invocation |
| claimLanguage | design recommendation pending reviewer acceptance |
| forbiddenExpansion | no source/test/package/export/live/public behavior |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance design packet only.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external artifact is an evidence source |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | repository source and accepted CVF artifacts only |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| applicability | N/A with reason: worker creates two one-off review artifacts, not a reusable governance foundation or index |
| canonicalRoot | N/A with reason: no foundation storage is created |
| sourceOfTruth | existing runtime source and accepted T0 completion |
| generatedAggregate | N/A with reason: no aggregate is created |
| indexUpdate | N/A with reason: no registry or index structure changes |
| claimBoundary | no foundation storage mutation |

## Machine Closure Package

NOT_APPLICABLE_WITH_REASON: dispatch-ready work order; reviewer owns closure.

## Claim Boundary

This work order authorizes exactly two documentation outputs. It does not
authorize implementation, exports, tests, provider use, GC-010 or paired-gap
closure, public-sync, push, deployment, or production readiness.
