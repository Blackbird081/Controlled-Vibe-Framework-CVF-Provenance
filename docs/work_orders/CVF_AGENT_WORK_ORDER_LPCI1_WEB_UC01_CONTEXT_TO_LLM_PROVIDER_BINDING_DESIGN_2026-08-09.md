# CVF Agent Work Order - LPCI1 Web UC-01 Context-To-LLM Provider Binding Design

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Date: 2026-08-09

Batch ID: LPCI1-WEB-UC01-D1

Dispatch base head: `db24c5266`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated documentation-design worker

Reviewer/closer: primary reviewer/closer

Worker return path: `docs/reviews/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_WORKER_RETURN_2026-08-09.md`

## Dispatch Prompt Envelope

Role: independent documentation-design worker for `LPCI1-WEB-UC01-D1`.

Canonical packet: this work order and paired baseline
`docs/baselines/CVF_GC018_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_2026-08-09.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture current committed HEAD at start after packet/session
dispatch commits. Do not reuse `dispatchBaseHead` as execution evidence.

Current-time notes: LPCI intake R3 is independently closed and synchronized at
`db24c5266`. This tranche is the newly authorized UC-01 DESIGN-only checkpoint;
implementation and provider/live authority remain parked.

Do-not-misread notes: this is DESIGN-only. It does not authorize source/test,
package/config, provider/API-key/network/live, public, session, or deployment
mutation or execution.

Required first actions: read the session startup surfaces, guard orientation,
literal-format gotchas, `DESIGN.md`, this work order, the paired baseline, the
roadmap, the accepted S1 spec, and every source named in Source Verification;
then capture `executionBaseHead` and confirm `git status --short` is clean.

Return contract: create exactly the DESIGN audit and worker return, run required
gates, leave staging empty and HEAD unchanged, then return
`COMPLETE_PENDING_REVIEW` or an exact governed blocker.

## Purpose

Produce one source-backed UC-01 architecture DESIGN that removes the proposed
parallel generic provider ownership model. The DESIGN must specify how LPCI
reuses or composes the existing Model Gateway and must define the accompanying
documented configuration contract as one inseparable UC-04 decision.

## Authorization / Decision

Operator authority: `AUTHORIZE_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_ONLY`.

Authority evidence is the operator's continuation response after the reviewer
named this exact next checkpoint. The worker may design but may not implement,
test, invoke, stage, commit, or claim acceptance.

## Authority Chain

Operator continuation response -> this GC-018/work order -> no-commit worker
DESIGN -> independent reviewer acceptance. No later phase is inherited.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| operator | human operator | DESIGN-only authority and later checkpoints |
| dispatcher/reviewer/closer | primary agent | packet, independent review, commits, continuity |
| worker | delegated agent | exact two documentation outputs; no commit |

## Required First Reads

Read startup front doors, active handoff, guard orientation, literal gotchas,
`DESIGN.md`, this work order, paired baseline, intake roadmap, accepted S1 spec,
current LPCI route, Model Gateway capability/bridge/credential sources, and all
checker sources named in the read-ahead block.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id LPCI1-WEB-UC01-D1 --title "LPCI1 Web UC-01 Context-To-LLM Provider Binding Design" --date 2026-08-09 --base db24c5266 --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | web-ui-dashboard plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | completed source verification, lifecycle, exact manifest, no-commit handoff, DESIGN deliverables, and forbidden boundaries |
| checkerReadAheadConfirmation | dispatch-quality, structural, ADIF, handoff, trace, worker-return, public-export, and file-size checker sources |
| docOnlyNewFields | designDecision, compositionBoundary, configContract, providerSelectionInput, receiptCorrelation, failureMapping, laterBuildCandidateManifest |
| claimBoundary | packet authoring only; doc-only names are not current runtime fields |

## Worker Autonomy / No-Question Rule

Repair allowed-scope documentation or checker-shape failures directly. Return
to the reviewer only for a source contradiction, mandatory runtime/provider
action, forbidden-path need, or missing authority that makes the DESIGN
impossible.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `DISPATCH_READY`; Source Verification Block; Roadmap-to-Work-Order Trace Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Public Export Disposition |
| gateRunPurpose | confirmation evidence after checker-source/scaffold read-ahead; not first discovery |
| claimBoundary | dispatch and output-shape compliance only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`documentation-design`, role=`worker`, lifecyclePhase=`pre-implementation`

Resolver query executed: `python governance/compat/run_adif_defect_resolver.py --task-class documentation-design --role worker --lifecycle-phase pre-implementation --surface-selector LPCI --max-results 50 --json`

Returned defect count: 0. Disclosed defectIds: none.

Returned defects: NONE_RETURNED

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| UC-01 single lifecycle | LITERAL_INVARIANT | `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md` | Recommended Next Tranche | `UC-01` | roadmap lifecycle chain | ACCEPT |
| UC-04 composition plus config AND rule | LITERAL_INVARIANT | `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md` | Reopen Conditions | `UC-04` | roadmap dependency contract | ACCEPT |
| accepted evidence/response contract | EXISTS | `docs/reference/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md` | Model Evidence Projection and response variants | `modelEvidenceProjection` | accepted S1 contract | ACCEPT |
| current credential input | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | line 263 | `LPCI_LLM_API_KEY` | `POST` | ACCEPT |
| current endpoint input | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | line 286 | `LPCI_LLM_ENDPOINT` | `POST` | ACCEPT |
| current model input | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | line 287 | `LPCI_LLM_MODEL` | `POST` | ACCEPT |
| current direct call | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 291-306 | `fetch` | `POST` | ACCEPT |
| capability registry owner | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | lines 49-123 | `PROVIDER_CAPABILITY_REGISTRY` | capability registry | ACCEPT |
| execution bridge owner | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | lines 27-78 | `ProviderExecutionBridge` | provider execution bridge | ACCEPT |
| credential boundary owner | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | lines 3-33 | `CredentialReference` | `CredentialBoundary` | ACCEPT |
| public gateway exports | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | provider capability, credential, and bridge exports | `ProviderExecutionBridge` | Model Gateway package surface | ACCEPT |
| cvf-web Model Gateway dependency | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependencies; corrected fact: no dependency exists | `cvf-model-gateway` | package dependency graph | REJECT |
| documented LPCI config contract | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.example` | current file; corrected fact: all three variables are absent | `LPCI_LLM_API_KEY` | environment configuration contract | REJECT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact packet paths | both returned `False` before authoring | PASS |
| batch and authority token | repository search returned no match before authoring | PASS |
| current package binding | no Model Gateway dependency/import found in cvf-web package/config/source | GAP_TO_DESIGN |
| current config documentation | no LPCI provider variables found in `.env.example` | GAP_TO_DESIGN |
| duplicate owner decision | current LPCI direct fetch is a call-site implementation, not authority to create a second generic provider registry/credential/routing owner | REJECT_PARALLEL_OWNER |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| Intake source | operator continuation after the reviewer named the fresh UC-01 DESIGN-only checkpoint |
| intake summary | repository-local, source-backed provider-binding and config-contract DESIGN |
| scope classification | bounded documentation-design tranche; no implementation or live proof |
| risk sensitivity | governed product boundary with credential and provider-ownership implications |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| selected role route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | primary dispatcher/reviewer/closer plus one no-commit documentation-design worker |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| escalation condition | return to reviewer on source contradiction, scope expansion, runtime mutation need, secret-content need, or provider/live need |

## Agent Handoff Contract Control Block

Contract source; archive classification N/A:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | primary dispatcher/reviewer/closer plus one no-commit documentation worker |
| phase | DESIGN execution followed by independent reviewer closure conversion |
| baseHeadFor(phase) | dispatchBaseHead=`db24c5266`; executionBaseHead=worker capture after packet/session commits; closureBaseHead=reviewer capture before acceptance |
| changedSetScope(phase) | worker exactly two documentation outputs; reviewer owns packet/session/closure paths |
| traceScope(phase, actor) | worker trace covers only two outputs; reviewer trace covers dispatch, acceptance, commits, and continuity separately |
| commitOwner(phase) | primary reviewer/closer; worker commit forbidden |
| crossBatchIsolation | clean worktree required at worker start; no unrelated dirty path, prior stash, public clone, or other batch may enter the manifest |
| Before status evidence | dispatcher observed a clean worktree at `db24c5266` before authoring; worker must independently confirm a clean worktree at execution start |
| nextMoveSurfaces | reviewer updates protected session surfaces only after accepted material commit |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_COMPLETION_2026-08-09.md` |
| reviewerOwnedClosurePaths | work-order status, completion review, roadmap status if required, then separate protected session sync |
| closureOwner | primary reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Required evidence |
|---|---|---|
| UC-01 only | design named dashboard/synthetic-public-index use case | exact consumer/query/corpus boundary |
| UC-04 reuse or composition | compare bounded options and select existing Model Gateway owner path | source-backed decision and rejected parallel-owner option |
| documented config contract | define all three LPCI variables and their gateway meaning, validation, defaults, and failure state | exact config table plus secret-safe boundary |
| DESIGN acceptance before live | no provider execution; worker returns pending review | explicit lifecycle/interlock section |
| separate provider/live authority | keep live cases as future proof plan only | zero call evidence and claim boundary |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/audits/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_2026-08-09.md` | create complete source-backed DESIGN |
| `docs/reviews/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_WORKER_RETURN_2026-08-09.md` | create checker-safe evidence return |

All other paths are forbidden to the worker.

## Write Ownership

Worker owns only the two fulfillment-manifest paths. Reviewer owns all packet,
closure, status-conversion, commit, and protected continuity paths.

## Required DESIGN Decisions

The DESIGN audit must include:

1. current-state diagram in prose or a compact table: LPCI route directly reads
   three environment inputs and performs direct fetch;
2. at least two composition options, including status quo rejection, and one
   selected source-backed reuse/composition boundary;
3. explicit ownership mapping for capability selection, credentials,
   routing/execution, receipt/diagnostic, LPCI evidence projection, and route
   response/audit correlation;
4. a documented config contract covering `LPCI_LLM_API_KEY`,
   `LPCI_LLM_ENDPOINT`, and `LPCI_LLM_MODEL`, including which remain, which are
   translated, provider/model identity validation, endpoint override posture,
   missing/invalid behavior, and secret-safe logging;
5. exact future package/import/composition seam without claiming it exists;
6. provider request and response mapping from accepted LPCI S1 fields to
   Model Gateway request/result/receipt surfaces;
7. fail-closed mapping for absent config, unsupported provider/model,
   credential unavailable, policy denial, no candidate, adapter error, invalid
   output, and correlation failure;
8. UI implications bounded by `DESIGN.md`, without UI implementation;
9. later-build candidate manifest and deterministic synthetic proof matrix;
10. explicit rejection of a new parallel generic provider owner;
11. one lifecycle interlock: DESIGN completion -> independent acceptance ->
    separate fresh provider/live authority.

The worker must not invent current imports, dependencies, fields, or adapters.
New design-only names must be marked `DOC_ONLY_NEW`.

## Execution Plan

1. Capture execution HEAD and clean worktree; run pre-implementation gate.
2. Re-read current source and record any change from dispatch facts.
3. Compare composition options and author the complete DESIGN audit.
4. Author the full worker return and run required gates.
5. Leave staging empty, do not commit, and return for independent review.

## Acceptance Criteria

| ID | Criterion | Fail condition |
|---|---|---|
| AC-01 | exact two-path worker manifest | any other path changes |
| AC-02 | one selected Model Gateway reuse/composition design | parallel generic owner remains available |
| AC-03 | config contract covers all three LPCI variables with AND binding | `.env.example` naming alone is treated as sufficient |
| AC-04 | current source facts and future doc-only names are separated | future seam claimed implemented |
| AC-05 | accepted LPCI evidence/response/audit contract remains intact | projection or public-only boundary weakened |
| AC-06 | failure mapping is finite and fail-closed | raw provider error/secret/prompt leaks |
| AC-07 | no provider/live/test/runtime action | any such action occurs |
| AC-08 | worker return passes full fast gate | individual checker substitution |
| AC-09 | staged set empty and HEAD unchanged | worker stages or commits |

## Worker Output Checker Read-Ahead Mandate

Before writing each output, read checker source for its path/docType and
conditional terms. The audit must use proper audit sections; the worker return
must satisfy the full worker-return quality gate. Do not place backticked
heading syntax before the real section headings.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_WORKER_RETURN_2026-08-09.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must record execution base, exact manifest, gate counts, staging and
HEAD evidence, zero provider/live/network actions, epistemic comparison,
finding-to-governance disposition, and `COMPLETE_PENDING_REVIEW`.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --check
git diff --name-status
git status --short
git diff --cached --name-only
```

No runtime test, provider call, network call, or secret read is required or
allowed. Source reading and governance scripts are allowed.

## Pre-Flight Checks

- confirm committed packet/session dispatch and capture execution HEAD;
- confirm `git status --short` is clean;
- run pre-implementation with the real execution base;
- confirm exact allowed paths do not already exist;
- confirm no provider/live credential action is attempted.

## Evidence Requirements

Record exact source citations, option comparison, selected design, config
contract, failure mapping, proof plan, command outputs, exact manifest, staged
set, HEAD preservation, and zero provider/live/network count.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES_BOUNDED_CURRENT_SOURCE_FACTS_ONLY |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | direct route, package, gateway, credential, and config-source reads at dispatch base |
| reason | the DESIGN must resolve a verified current ownership/config gap without executing it |
| requiredFutureAction | independent reviewer acceptance, then a new governed lifecycle packet |

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | required before authoring DESIGN and recorded in output |
| UI claim boundary | only response-state and dashboard information-flow implications; no component/style/runtime mutation or readiness claim |

## Review Gate

Worker status remains `COMPLETE_PENDING_REVIEW`. Reviewer must independently
verify current-source fidelity, the UC-04 AND rule, no parallel owner, finite
fail-closed behavior, exact manifest, and gate evidence before acceptance.

## Closure Checklist

- [ ] exact two worker outputs returned
- [ ] current/future source facts separated
- [ ] Model Gateway composition selected
- [ ] all three LPCI configuration inputs covered
- [ ] provider/live/network count is zero
- [ ] worker staging empty and HEAD unchanged
- [ ] worker-return fast gate passes
- [ ] independent reviewer disposition recorded

## Operator Checkpoint

The current operator checkpoint is satisfied for DESIGN-only execution. A new
checkpoint is mandatory for SPEC, BUILD, runtime/config/package mutation,
provider/live proof, public-sync, deployment, or scope expansion.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when every worker-owned criterion passes.
Return an exact blocker for source contradiction, forbidden-path need,
mandatory provider/runtime execution, packet drift, or gate failure that cannot
be repaired within the two-path scope.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | primary reviewer/dispatcher |
| Provider or surface | private provenance repository |
| Session or invocation | `lpci1-web-uc01-d1-dispatch-2026-08-09` |
| Working directory | repository root |
| Command or tool surface | startup/guard/source reads, scaffold preview, ADIF resolver, patch authoring, gates, Git commit |
| Target paths | paired baseline and this work order |
| Allowed scope source | `AUTHORIZE_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_ONLY` |
| Before status evidence | clean worktree at synchronized HEAD `db24c5266` |
| After status evidence | exact two-path dispatch packet pending commit |
| Diff evidence | `git diff --name-status`; `git status --short` |
| Approval boundary | UC-01/UC-04 documentation-only DESIGN dispatch |
| Claim boundary | no DESIGN acceptance, runtime/test/provider/live/public action |
| Agent type | primary reviewer/dispatcher |
| Invocation ID | `lpci1-web-uc01-d1-dispatch-2026-08-09` |
| Expected manifest | paired baseline; this work order |
| Actual changed set | same two dispatch paths before commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | documentation-only UC-01 provider-binding/configuration DESIGN |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement or provider behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime/live receipt is created |
| actionEvidence | ACTION_EVIDENCE_PRESENT only for repository reads, documentation authoring, and governance gates |
| invocationBoundary | local repository tools only |
| interceptionBoundary | no direct interception, wrapper enforcement, provider call, or runtime gate execution |
| claimLanguage | source-backed design proposal pending independent review |
| forbiddenExpansion | runtime/test/package/config/provider/live/public/session/deployment action |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private architecture packet with internal source paths and no public
artifact authority.

## Claim Boundary

This work order authorizes exactly two documentation outputs. It does not
accept the DESIGN or authorize SPEC, BUILD, runtime/test/config/package edits,
provider/API-key/network/live action, public-sync, deployment, or readiness.
