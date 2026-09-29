# CVF Agent Work Order - LPCI1 Web Grounding And Clearance Conformance Design

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-08-08

Batch ID: LPCI1-WEB-D1

dispatchBaseHead: `68317891b`

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: documentation and source-verification design worker. The primary agent
is reviewer/closer.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN_2026-08-08.md`

Paired baseline: `docs/baselines/CVF_GC018_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN_2026-08-08.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: CURRENT_HEAD_AT_WORKER_START.

Current-time notes: operator released documentation-only DESIGN on 2026-08-08;
no live key, provider, network, runtime/test execution, or external action is
authorized.

Do-not-misread notes: design a bounded current-owner conformance boundary; do
not edit Web source/tests, invent an existing entitlement owner, pass a full
retrieval receipt, or open LPCI2/generic retrieval work.

Required first actions: complete startup acknowledgment; capture HEAD and clean
status; read the roadmap, baseline, T2/T3/T4, current source, guard orientation,
literal gotchas, and checker sources; run pre-implementation before writing.

Return contract: create exactly the design audit and worker return, leave both
unstaged and uncommitted, then return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON` with changed paths, captured base, gates, and status.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id LPCI1-WEB-D1 --title "LPCI1 Web Grounding And Clearance Conformance Design" --date 2026-08-08 --base 68317891b --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit and Web-boundary profiles |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact two-output design assignment, source verification, dependency release, design schema, threat/proof matrix, and lifecycle exclusions |
| checkerReadAheadConfirmation | dispatch-quality, prompt-envelope, structural, checker-read-ahead, ADIF, handoff, trace, worker-return, public-disposition, and file-size checkers |
| docOnlyNewFields | `modelEvidenceProjection`; `evidenceEligibilityRule`; `authorizationContext`; `authorizationDecision`; `grantEvidence`; `noProviderProjection`; `auditCorrelation`; `syntheticProofMatrix` |
| claimBoundary | dispatch authoring and documentation-only design execution; no runtime/test/provider/live/persistence/vector-RAG/public action |

## Purpose

Produce one independently source-verified design that either selects a safe,
owner-local LPCI1-Web conformance boundary or stops with an exact reason. The
design must jointly resolve grounding, sensitivity authorization, no-provider
minimization, audit correlation, and later synthetic proof requirements without
performing implementation.

## Authority Chain

- Operator authority: `LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN`,
  received 2026-08-08.
- Intake roadmap:
  `docs/roadmaps/CVF_LPCI_CURRENT_OWNER_GROUNDING_AND_CLEARANCE_DEFECT_INTAKE_ROADMAP_2026-08-08.md`.
- Accepted intake material commit: `38a3a21df`.
- Paired GC-018 baseline:
  `docs/baselines/CVF_GC018_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN_2026-08-08.md`.
- Active state and handoff remain authority pointers, not runtime fact sources.

Authority boundary: this work order releases design documentation only. Any
source contradiction or need for SPEC, BUILD, runtime/test change or execution,
provider/live action, persistence, vector/RAG, corpus mutation, public-sync,
push, or deployment stops the worker.

## Agent Roles

- Dispatcher: primary reviewer acting as dispatch author.
- Worker: delegated documentation and source-verification design worker.
- Reviewer/closer: primary reviewer, independent from worker output authorship.
- Session-sync steward: primary reviewer after accepted material commit.
- Commit owner: reviewer/closer only.

## Scope / Target / Owner Boundary

Allowed writes are exactly:

- `docs/audits/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN_2026-08-08.md`
- `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN_WORKER_RETURN_2026-08-08.md`

All route, library, test, UI, registry, corpus, canonical reference, baseline,
work-order, roadmap, session-state, handoff, provider, configuration, public,
and deployment paths are read-only to the worker.

Risk ceiling: R1 documentation and source-verification design evidence.

## Non-Goals

- no runtime implementation or test execution;
- no new grant store, database, persistence, provider, vector, embedding, RAG,
  graph, authentication, role taxonomy, UI, API, or registry implementation;
- no promotion of `contentSnippet` or any proposed field as existing authority
  without an explicit design decision and claim boundary;
- no sensitive fixture or production corpus use;
- no public, live, deployed, legal-answer-quality, or readiness claim.

## Dependency Release Evidence

| Dependency | Evidence | Commit/base | Disposition |
|---|---|---|---|
| defect intake accepted | intake roadmap and reviewer findings | `38a3a21df` | ACCEPT |
| design operator checkpoint | exact operator token received 2026-08-08 and recorded in roadmap Design Control Gate | dispatch base `68317891b` | ACCEPT |
| fresh source verification | paired GC-018 Source Verification Block and current searches | `68317891b` | ACCEPT |
| worker isolation | clean status before packet authoring; worker must recapture before execution | `68317891b` | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`design specification`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class "design specification" --role dispatcher --lifecycle-phase pre-dispatch --json`

Worker pre-implementation query:

`python governance/compat/run_adif_defect_resolver.py --task-class "design specification" --role worker --lifecycle-phase pre-implementation --json`

The current worker query also returns no entries. The worker must rerun it at
execution start and disclose every returned defect if current state differs.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`, generated active state, and active handoff.
2. `docs/reference/guard_orientation/README.md` and literal gotchas.
3. Intake roadmap and paired GC-018 baseline.
4. LPCI T2, T3, and T4 canonical contracts.
5. Current query route, LPCI types/retrieval/filter/audit modules,
   route-governance proof, middleware auth, service-token auth, current UI, and
   current synthetic pilot index.
6. Checker sources listed in the Checker Source Read-Ahead Block.

`DESIGN.md` was read by the dispatcher because this is a Web-owned design.
Visual/UI rules are N/A with reason: this tranche makes no UI or visual design.

## Pre-Flight Checks

```powershell
$lpciD1ExecutionBase = git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/run_adif_defect_resolver.py --task-class "design specification" --role worker --lifecycle-phase pre-implementation --json
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $lpciD1ExecutionBase --head HEAD --serial
```

Run before worker edits. HEAD must equal the captured execution base and status
must be clean. Allowed-scope gate failures are repaired without operator wait;
authority, source, path, risk, or external-effect expansion returns
`BLOCKED_WITH_REASON`.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| metadata-only model prompt | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 40-72 and 219-242 | `buildAnswerBoundaryPrompt` | LPCI query route | ACCEPT |
| full matched records retained in receipt | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/retrieval.ts` | lines 108-122 | `matched_records` | `runRetrievalPipeline` | ACCEPT |
| current record evidence and sensitivity fields | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 33-50 | `contentSnippet`; `sensitivityLevel` | `LpciIndexRecord` | ACCEPT |
| client clearance input | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 52-58 | `sensitivityClearance` | `FilterParams` | ACCEPT |
| client boolean controls current sensitivity filter | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.ts` | lines 14-28 and 109-120 | `applySensitivityFilter` | `runFilterPipeline` | ACCEPT |
| authenticated route identity input | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 64-85 and 118-208 | `actorId`; `authMode`; `session` | route governance proof contracts | ACCEPT |
| session actor and impersonation facts | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | lines 19-30 and 118-155 | `SessionCookie` | middleware authentication | ACCEPT |
| service-token identity has no corpus grant | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | lines 23-25 | `deriveServiceTokenIdentity` | service-token authentication | ACCEPT |
| no-provider branch returns full receipt | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 189-216 | `retrievalReceipt` | no-provider response | ACCEPT |
| successful route response already uses minimized source and audit shapes | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 286-306 | `matchedSources` | LPCI query success response | ACCEPT |
| canonical five-level sensitivity authorization | VALUE_SET | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | Sensitivity Classification (NR-06) | `sensitivityLevel` | LPCI1 T2 contract | ACCEPT |
| operator-controlled Stage 1 precedes client filters | VALUE_SET | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | Stage 1; Filter Execution Order | `classification_access`; `confidential_access` | LPCI1 T3 contract | ACCEPT |
| snippet is a capped display hint | VALUE_SET | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | Searchable Fields | `contentSnippet` | LPCI1 T3 contract | ACCEPT |
| model context and answer grounding requirement | VALUE_SET | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | RetrievalReceipt Schema; Answer Boundary Rules | `RetrievalReceipt` | LPCI1 T4 contract | ACCEPT |
| current pilot contains public synthetic records only | VALUE_SET | `docs/corpus-intelligence/GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json` | records array | `sensitivityLevel` | pilot index | ACCEPT |

The paired GC-018 table is incorporated by reference. The worker must repeat
decision-driving checks and correct stale facts in its outputs without editing
the dispatch packet.

## Current Runtime Freshness Verification

At dispatch base `68317891b`, exact searches confirm both defects and the full
no-provider receipt remain. Route authentication provides identity but no
current LPCI actor/corpus grant reader, grant store, grant expiry, revocation,
or service-to-corpus assignment owner was source-verified. Current runtime
`sensitivityLevel` handling is also narrower than the canonical five-level
contract. The worker must not convert absence into implementation authority.

## Negative Search And Collision Discipline

- Search roots: current cvf-web LPCI source/tests/UI/auth modules, LPCI T2/T3/T4
  references, corpus registry sources/aggregate, and current pilot index.
- Exact concepts: `classification_access`, `confidential_access`, corpus grant,
  retrieval authorization, `sensitivityClearance`, `contentSnippet`, full
  receipt response, route actor, impersonation, and service identity.
- Collisions: generic team permissions, Web knowledge-collection org/team
  scope, GC-051 scan metadata, and unrelated authorization owners are patterns
  only; none is accepted as LPCI sensitivity authority.
- Disposition: proposed entitlement/evidence interfaces must be listed as
  doc-only new. A missing source-backed owner must produce a stop or public-only
  fail-closed boundary, not an invented existing owner.

## New Doc-Only Fields

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
|---|---|---|---|---|
| `modelEvidenceProjection` | minimized provider-bound evidence records | Yes | Yes | design fields map only to source-verified existing values |
| `evidenceEligibilityRule` | public/sensitivity/content eligibility and fail-close | Yes | Yes | decision table plus negative cases |
| `authorizationContext` | server-derived actor/auth/corpus inputs | Yes | Yes | source mapping separates identity from entitlement |
| `authorizationDecision` | allow/deny, reason, sensitivity, corpus result | Yes | Yes | fail-closed threat matrix |
| `grantEvidence` | proposed active corpus-bound grant reference | Yes | Yes | owner/expiry/revocation must be resolved or stopped |
| `noProviderProjection` | minimized HTTP response without full records | Yes | Yes | existing UI needs mapped explicitly |
| `auditCorrelation` | actor/corpus/grant/evidence-path/outcome metadata | Yes | Yes | no raw evidence or secret release |
| `syntheticProofMatrix` | later deterministic positive/negative cases | Yes | Yes | no test execution in D1 |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | accepted current-owner conformance defects released to bounded DESIGN |
| scope classification | documentation-only, two worker paths, R1 |
| risk sensitivity | authorization and evidence disclosure require fail-closed design; no sensitive data used |
| selected role route | `MULTI_AGENT_MULTI_ROLE` |
| role separation basis | dispatcher authors packet; worker designs; independent reviewer/closer decides and commits |
| escalation condition | missing source owner, unsafe evidence projection, forbidden path, external effect, or later lifecycle need |

## Execution Plan

1. Capture execution base/clean status and run pre-implementation.
2. Reverify all current route, receipt, filter, auth, UI, and contract facts.
3. Compare at least these evidence choices: minimized eligible snippet
   projection, metadata-only abstention, and new approved-evidence contract.
4. Compare at least these authorization choices: dedicated LPCI resolver with
   injected read-only grant source, GC-051-owned grants, generic team/scope
   reuse, and current public-only fail-closed boundary.
5. Reject client clearance as authority and record migration disposition.
6. Select minimized provider and no-provider projections or stop.
7. Define actor/corpus/sensitivity/audit invariants and threat matrix.
8. Define deterministic synthetic later-build cases without running tests.
9. Create audit and worker return, then run the worker-return fast gate once
   after focused corrections.

## Required Design Schema

| Field | Required answer |
|---|---|
| `ownerBoundary` | exact LPCI1-Web current owner; LPCI2/generic retrieval excluded |
| `groundingOptionMatrix` | options, evidence for/against, disclosure risk, selected option or stop |
| `modelEvidenceProjection` | exact included/excluded existing fields and delimiter/injection boundary |
| `evidenceEligibilityRule` | blank, length, sensitivity, authorization, and missing-evidence behavior |
| `authorizationOptionMatrix` | options, source ownership, risk, selected option or stop |
| `authorizationContext` | session, service, impersonation, corpus and time facts |
| `authorizationDecision` | allow/deny reason classes and fail-closed invariants |
| `grantEvidence` | source-backed owner or explicit missing-owner/parked disposition |
| `clientClearanceDisposition` | ignore, reject, or later remove; never authority |
| `noProviderProjection` | exact allowed response fields and excluded full-record fields |
| `auditCorrelation` | exact metadata, minimization, and dropped-record disclosure boundary |
| `syntheticProofMatrix` | positive, negative, mixed, injection, and no-provider cases |
| `laterBuildCandidateManifest` | proposed bounded paths/tests only, clearly unauthorized |
| `exitRecommendation` | one exact design decision or stop token |

## Required Threat Matrix

Cover forged client `true`, public-only request, session without grant, exact
corpus grant, cross-corpus grant, confidential/classified override, restricted
and unknown, expired/revoked/malformed grant, grant-reader failure, valid
service token without grant, impersonated session, mixed public/non-public
matches, missing/blank/oversize evidence, evidence injection delimiter, and
no-provider response. Authorization must precede search, prompt, receipt, and
outward response for protected records.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/audits/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN_2026-08-08.md` | CREATE |
| `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN_WORKER_RETURN_2026-08-08.md` | CREATE |

## Write Ownership

The worker owns only the two manifest paths and leaves both unstaged and
uncommitted. The reviewer owns all accepted repairs, optional completion review,
material commit, roadmap status after decision, and session sync.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Closure evidence | Status |
|---|---|---|---|
| safe evidence projection | execution steps 3 and 6; design schema | option matrix and selected projection or stop | SATISFIED |
| actor/corpus authorization | execution steps 4-5; threat matrix | authorization owner/decision and client-input disposition | SATISFIED |
| no-provider minimization | design schema | exact included/excluded response fields | SATISFIED |
| deterministic proof | threat and proof matrices | synthetic later-build cases | SATISFIED |
| current-owner only | owner boundary and forbidden scope | path/owner ledger | SATISFIED |
| no implementation | exact write manifest and lifecycle exclusions | Git changed-set and no-commit evidence | SATISFIED |

## Worker Autonomy / No-Question Rule

Proceed without operator confirmation for all allowed read-only investigation,
option comparison, documentation corrections, checker-shape repairs, and gate
reruns. Escalate only when completion requires scope, path class, risk ceiling,
external effect, secret/quota, commit-owner, destructive action, or later
lifecycle authority to change.

## Agent Handoff Contract Control Block

Contract source archive-qualified checker exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher/reviewer -> no-commit design worker -> independent reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=68317891b; executionBaseHead=current HEAD captured before worker edits; closureBaseHead=reviewer captures worker-return base |
| changedSetScope(phase) | dispatch=roadmap release plus paired packets; execution=two worker outputs; closure=accepted outputs and one bounded reviewer repair; session sync=canonical continuity only |
| traceScope(phase, actor) | every actor records its phase-local trace and exact manifest |
| commitOwner(phase) | dispatcher commits packet; worker must not commit; reviewer commits accepted material; steward commits continuity |
| crossBatchIsolation | one LPCI1-WEB-D1 batch begins from a clean worktree |
| nextMoveSurfaces | reviewer updates only after accepted design decision |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN_COMPLETION_2026-08-08.md` (optional; create only if a separate completion artifact is required) |
| reviewerOwnedClosurePaths | design audit, worker return, optional completion review, and intake roadmap status |
| closureOwner | primary reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN_WORKER_RETURN_2026-08-08.md`

contractProfile: WORKER_RETURN_FAST_DOC_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

scopeClassification: DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT

publicSyncDisposition: FORBIDDEN

liveRuntimeDisposition: FORBIDDEN

checkerMutationDisposition: FORBIDDEN

workerSelfSelection: FORBIDDEN

## Worker Output Checker Read-Ahead Mandate

Before writing, read the structural, worker-return, operation-trace,
epistemic-process, finding-to-governance, Delta claim, public-disposition, and
file-size checkers. The worker return must use `## Conditional Controls
Disposition` with `conditionalControlsDisposition: EKI_NA; RIH_NA; CCRI_NA`
unless evidence makes a full conditional block applicable.

## Evidence Reuse And Encoding Plan

| Field | Value |
|---|---|
| verificationMode | RECOMPUTE_REQUIRED |
| priorEvidenceUse | intake and three pre-dispatch audits are leads only |
| currentSourceRequirement | re-read decision-driving source and contracts at execution base |
| encoding | ASCII for all new worker-authored prose and fields |
| rawEvidenceBoundary | no secrets, sensitive content, provider payload, or unbounded source copy |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| foundationChange | NONE |
| ownerSurface | existing LPCI1-Web route/library/UI/test family and documentation outputs |
| newDurableFoundation | N/A with reason: design cannot create or select persistence |
| indexOrRegistryChange | N/A with reason: no corpus/index/registry mutation is authorized |
| claimBoundary | no relocation, split, schema lock, store, service, or runtime owner creation |

## Acceptance Criteria

- [ ] both current conflicts and no-provider disclosure are reverified;
- [ ] one rubric compares all required grounding options;
- [ ] one rubric compares all required authorization options;
- [ ] client clearance is never accepted as authority;
- [ ] every proposed absent symbol/field is doc-only new;
- [ ] public-only fallback and missing-owner stop behavior are explicit;
- [ ] provider/no-provider/audit projections are minimized;
- [ ] synthetic proof matrix covers every required threat case;
- [ ] exactly one exit recommendation is returned;
- [ ] only two worker paths change and worker makes no commit;
- [ ] worker-return fast gate passes.

## Review Gate

The reviewer performs one single-pass dependency review across contract/schema,
source authority, paths, threat coverage, minimization, proof adequacy, claim
boundary, range, and commit choreography before any repair. Gate PASS is not
semantic acceptance.

## Evidence Requirements

- current command/result/path evidence for every decision-driving source row;
- supporting and contradicting evidence for every option;
- exact provider, client-response, audit, actor, corpus, grant, and sensitivity
  inclusion/exclusion ledgers;
- exact threat and synthetic later-build proof matrices;
- actual pending Git status, execution base, gate result, and no-commit statement.

## Closure Checklist

- [ ] two required outputs exist and no other worker path changed;
- [ ] all acceptance criteria and stop conditions are resolved;
- [ ] every absent runtime-shaped proposal is labeled doc-only new;
- [ ] worker-return fast gate passes after final worker edit;
- [ ] independent reviewer disposition is recorded;
- [ ] material and continuity commits remain reviewer/steward owned.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for a missing decision-driving source, unsafe
projection, unresolved owner required for the selected design, forbidden path,
unexpected worktree mutation, external action, sensitive fixture need, or any
authority above documentation-only DESIGN.

## Verification Commands

```powershell
git status --short --untracked-files=all
python governance/compat/run_worker_return_fast_gate.py
git diff --check
```

## Operator Checkpoint

No repeated operator checkpoint applies inside allowed D1 work. After reviewer
acceptance, any SPEC, BUILD, runtime/test implementation or execution,
provider/live, persistence, vector/RAG, public-sync, push, or deployment action
requires a fresh explicit operator checkpoint and new governance packet.

## Finding-To-Governance Learning Disposition

The grounding and clearance gaps are already owned by the intake roadmap. Add
an ADIF entry only if execution reveals a new repeated or non-obvious agent
defect pattern; do not duplicate the product conformance findings as ADIF.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | prompt-envelope ordering; dispatch status; dependency rows; Source Verification shape and claim types; ADIF query; Fast Doc literals; handoff fields; trace labels; conditional controls; stop tokens; public disposition |
| gateRunPurpose | confirm and record gate evidence after complete source-backed dispatch authoring; gates are not first discovery |
| claimBoundary | LPCI1-WEB-D1 no-commit documentation design work order |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a minimized public-only evidence projection may
restore bounded current value while all non-public access remains fail-closed;
a future general sensitivity design may stop because no grant owner exists.

Evidence Comparison Requirement: apply the same safety/value/ownership rubric
to every required grounding and authorization option and preserve evidence
against the recommendation.

Contradiction Or Gap Disposition: select a bounded design only when evidence,
authorization, response, and audit boundaries all fail closed. Otherwise stop.

Claim Update Requirement: return one accepted-design candidate or exact stop.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LPCI1-WEB-D1 documentation/source design only |
| claimDisposition | N/A with reason: no runtime execution-control claim is made |
| receiptEvidence | N/A with reason: no runtime receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local source reads, document writes, gate commands, and Git evidence only |
| invocationBoundary | governed local documentation analysis |
| interceptionBoundary | no provider, network, runtime, shell-interception, or agent-interception claim |
| claimLanguage | source-verified design recommendation only |
| forbiddenExpansion | SPEC, BUILD, source/test mutation or execution, provider/live, persistence, vector/RAG, corpus mutation, public-sync, deployment |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer |
| Provider or surface | local private provenance repository |
| Session or invocation | LPCI1-WEB-D1 work-order authoring, 2026-08-08 |
| Working directory | repository root |
| Command or tool surface | source reads, exact searches, scaffold stdout, ADIF resolver, apply_patch, pre-dispatch gates |
| Target paths | intake roadmap release plus paired LPCI1-WEB-D1 dispatch packets |
| Allowed scope source | operator token `LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN` |
| Before status evidence | HEAD `68317891b`; clean worktree |
| After status evidence | documentation-only design packet pending dispatcher commit |
| Diff evidence | exact three-path Git status and diff before commit |
| Approval boundary | DESIGN documentation and worker dispatch only |
| Claim boundary | no runtime/test/provider/live/persistence/vector-RAG/public/deployment action |
| Agent type | dispatcher/reviewer |
| Invocation ID | `lpci1-web-d1-work-order-authoring-2026-08-08` |
| Expected manifest | intake roadmap release plus paired LPCI1-WEB-D1 baseline and work order |
| Actual changed set | intake roadmap release plus paired LPCI1-WEB-D1 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source/security design and no public-safe packet. No public-sync
action or claim is authorized.

## Claim Boundary

This work order authorizes exactly two local no-commit documentation outputs.
It does not authorize SPEC, BUILD, source/test mutation or execution,
provider/model/live action, persistence, vector/embedding/RAG, corpus/index
mutation, LPCI2/generic retrieval work, public-sync, push, deployment,
production use, sensitive-release claims, or readiness claims.
