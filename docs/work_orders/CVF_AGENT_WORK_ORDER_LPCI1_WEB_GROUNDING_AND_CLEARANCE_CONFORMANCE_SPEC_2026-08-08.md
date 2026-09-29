# CVF Agent Work Order - LPCI1 Web Grounding And Clearance Conformance Specification

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED

Batch ID: LPCI1-WEB-S1

Date: 2026-08-08

dispatchBaseHead: `d68653ed9`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated documentation specification worker

Reviewer/closer: primary reviewer/closer

## Dispatch Prompt Envelope

Role: no-commit documentation specification worker for LPCI1-WEB-S1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact and authority date are 2026-08-08; source facts
must be refreshed at worker start.

Do-not-misread notes: this is SPEC documentation only. It does not authorize
BUILD, runtime/test mutation or execution, provider/live, persistence,
vector/RAG, corpus mutation, public-sync, deployment, or readiness claims.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, this work order, paired GC-018, accepted D1 design, canonical T2/T3/T4
contracts, and every checker source in the read-ahead block. Capture current
HEAD and status, rerun the exact worker ADIF query and pre-implementation gate,
then write only the two manifest outputs.

Return contract: create both outputs, run the required documentation gates,
leave changes unstaged and uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id LPCI1-WEB-S1 --title "LPCI1 Web Grounding And Clearance Conformance Specification" --date 2026-08-08 --base d68653ed9 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled exact authority, dependency, source, two-output, handoff, specification, runtime-audit, and stop-boundary requirements |
| checkerReadAheadConfirmation | applicable dispatch, structural, handoff, trace, ADIF, Delta, encoding, public-disposition, scaffold-provenance, worker-return, and file-size checker sources were read before authoring |
| docOnlyNewFields | normalized batch token and the fields listed under New Doc-Only Fields |
| claimBoundary | Dispatch authoring provenance only; no runtime, provider, live, public, Web implementation, or model-router behavior claim. |

## Purpose

Produce one normative LPCI1-Web conformance SPEC that converts the accepted D1
design into bounded documentation contracts. Reconcile T3 display-hint
semantics with T4 full-receipt context wording, preserve public-only fail-close,
and define exact projection, validation, response, audit, and synthetic later
proof requirements without implementing them.

## Authority Chain

1. Verbatim operator authority:
   `AUTHORIZE_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_DOCUMENTATION_ONLY`.
2. Defect intake roadmap at `38a3a21df`.
3. Accepted D1 design at `e0ee8a000`.
4. Paired GC-018 at dispatch base `d68653ed9`.
5. This source-verified work order.

Normalized token `LPCI1-WEB-S1` is new dispatch vocabulary introduced by this
packet and is not a prior source fact.

Authority boundary: SPEC documentation, current source reads, documentation
gates, and exact no-commit handoff only.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| dispatcher/reviewer | primary agent | author and commit packet, review worker output |
| specification worker | delegated worker | create exact reference SPEC and worker return, no commit |
| reviewer/closer | primary independent reviewer | semantic review, bounded repairs, closure conversion, material commit |
| session-sync steward | primary agent | separate continuity update only after accepted material commit |

## Scope / Target / Owner Boundary

Allowed analysis targets are current LPCI query route/library/types/audit/auth/UI
source, current focused tests as read-only evidence, the public synthetic pilot,
accepted D1 artifacts, roadmap, and T2/T3/T4 canonical contracts.

Allowed writes are exactly the two paths in the fulfillment manifest. Existing
LPCI1-Web remains owner. The SPEC may introduce normative doc-only vocabulary
but cannot claim that vocabulary exists in runtime.

## Non-Goals

- no runtime, source, test, UI, API, auth, registry, corpus, or generated-state edit;
- no runtime, unit, route, E2E, provider, live, or benchmark execution;
- no provider/model/key, persistence, vector, embedding, RAG, or graph decision;
- no grant store, non-public entitlement owner, general role taxonomy, or production corpus;
- no public-sync, push, deployment, security-readiness, or answer-quality claim.

## Dependency Release Evidence

| Dependency | Evidence | Commit/base | Final disposition |
|---|---|---|---|
| defect intake | current-owner intake roadmap | `38a3a21df` | ACCEPT |
| D1 dispatch | D1 baseline and work order | `bd22ca0a4` | ACCEPT |
| D1 acceptance | accepted design audit and corrected return | `e0ee8a000` | ACCEPT |
| current continuity | active state, handoff, front door | `d68653ed9` | ACCEPT |
| SPEC authority | exact operator token in Authority Chain | `d68653ed9` | ACCEPT |
| clean dispatch base | `git status --short --untracked-files=all` empty before authoring | `d68653ed9` | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`design specification`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "design specification" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional ADIF-specific instruction; standing governance remains binding |

Worker pre-implementation query:

`python governance/compat/run_adif_defect_resolver.py --task-class specification --role worker --lifecycle-phase pre-implementation --json`

Current result is NONE_RETURNED. Rerun at worker start and disclose all returned
IDs if current state differs.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`, active state, and active handoff.
2. `docs/reference/guard_orientation/README.md` and literal gotchas.
3. Paired GC-018 and this work order.
4. Intake roadmap and accepted D1 design/worker return.
5. LPCI T2, T3, and T4 canonical specifications.
6. Current LPCI route, types, retrieval, filter, audit, route auth, session auth,
   service-token auth, UI, tests, and public synthetic index.
7. Checker sources in the read-ahead block.

`DESIGN.md` was read by the dispatcher because the owner is Web. Visual/UI rules
are N/A with reason: no UI or visual design/change is authorized.

## Pre-Flight Checks

```powershell
$lpciS1ExecutionBase = git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/run_adif_defect_resolver.py --task-class specification --role worker --lifecycle-phase pre-implementation --json
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $lpciS1ExecutionBase --head HEAD --serial
```

Run before any worker edit. HEAD must equal the captured execution base and
status must be clean. Repair allowed-scope documentation failures; return
`BLOCKED_WITH_REASON` for source, authority, path, risk, or lifecycle expansion.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| accepted design is conditional on SPEC reconciliation | VALUE_SET | `docs/audits/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN_2026-08-08.md` | Selected Model Evidence Projection; Findings / Position | `exitRecommendation` | D1 design decision | ACCEPT |
| roadmap holds before SPEC | VALUE_SET | `docs/roadmaps/CVF_LPCI_CURRENT_OWNER_GROUNDING_AND_CLEARANCE_DEFECT_INTAKE_ROADMAP_2026-08-08.md` | Design Control Gate | `Gate status` | current-owner roadmap | ACCEPT |
| current evidence and sensitivity fields | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 33-50 | `contentSnippet`; `sensitivityLevel` | `LpciIndexRecord` | ACCEPT |
| client clearance input | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 52-58 | `sensitivityClearance` | `FilterParams` | ACCEPT |
| receipt retains full records | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/retrieval.ts` | lines 108-122 | `matched_records` | `runRetrievalPipeline` | ACCEPT |
| client boolean controls current filter | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.ts` | lines 14-28 and 109-120 | `applySensitivityFilter` | `runFilterPipeline` | ACCEPT |
| current model prompt contains metadata but no evidence text | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 40-72 and 219-242 | `buildAnswerBoundaryPrompt` | LPCI query route | ACCEPT |
| no-provider response returns full receipt | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 189-216 | `retrievalReceipt` | LPCI query no-provider response | ACCEPT |
| provider error currently returns derived provider error text | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 245-268 | `POST` | LPCI query provider-error branch | ACCEPT |
| authenticated identity evidence exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 64-85 and 118-208 | `actorId`; `authMode`; `session` | route governance proof contracts | ACCEPT |
| session and impersonation facts exist | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | lines 19-30 and 118-155 | `SessionCookie`; `verifySessionCookie` | middleware authentication | ACCEPT |
| service identity exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | lines 23-25 | `deriveServiceTokenIdentity` | service-token authentication | ACCEPT |
| audit receipt retains filters and response hash | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 94-109 | `applied_filters`; `model_response_hash` | `AuditReceipt` | ACCEPT |
| audit builder copies the supplied filter shape | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/audit-receipt.ts` | lines 32-74 | `buildAuditReceipt` | LPCI audit receipt builder | ACCEPT |
| canonical sensitivity values and rules | VALUE_SET | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | Sensitivity Classification (NR-06) | `sensitivityLevel` | LPCI1 T2 contract | ACCEPT |
| T3 display hint and operator sensitivity rules | VALUE_SET | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | Searchable Fields; Stage 1 - Sensitivity Pre-Filter | `contentSnippet`; `classification_access`; `confidential_access` | LPCI1 T3 contract | ACCEPT |
| T4 full-receipt context and answer grounding | VALUE_SET | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | RetrievalReceipt Schema; Answer Boundary Rules | `RetrievalReceipt` | LPCI1 T4 contract | ACCEPT |
| public synthetic pilot values | VALUE_SET | `docs/corpus-intelligence/GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json` | records array | `sensitivityLevel` | pilot index | ACCEPT |

The worker must refresh every decision-driving row at its execution base. Stale
facts are corrected in worker outputs; dispatch files remain reviewer-owned.

## Current Runtime Freshness Verification

At `d68653ed9`, source still exhibits metadata-only prompting, full-record
receipts, client-controlled classified filtering, full no-provider receipt, and
raw-derived provider-error text. No LPCI grant reader or non-public authorization
owner was found. The accepted design remains `PUBLIC_ONLY`.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| planned path existence | all four planned dispatch/output paths returned `False` before authoring | NO_COLLISION |
| normalized token search | exact search over `docs`, `CVF_SESSION`, and active handoff returned no match | DOC_ONLY_NEW |
| entitlement-owner search | `classification_access`, `confidential_access`, corpus grant, expiry, revocation, service assignment | NO_CURRENT_LPCI_OWNER |
| nearby patterns | generic role permissions, GC-051 scan registry, knowledge collection scopes, route identity | PATTERN_ONLY_NOT_AUTHORITY |

Exact search command used before authoring:

`rg -n 'LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC|LPCI1-WEB-S1' docs CVF_SESSION AGENT_HANDOFF_V55_2026-08-05.md`

## New Doc-Only Fields

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
|---|---|---|---|---|
| `modelEvidenceProjection` | allowlisted provider-bound evidence | Yes | Yes | normative schema and validation table |
| `evidenceEligibilityRule` | public/content/answer-class admission | Yes | Yes | ordered fail-close decision table |
| `authorizationContext` | server-derived identity/corpus context | Yes | Yes | identity is not entitlement |
| `authorizationDecision` | fixed public-only decision for S1 | Yes | Yes | non-public always denied |
| `grantEvidence` | future exact-corpus grant concept | Yes | Yes | absent and parked in S1 |
| `noProviderProjection` | minimized client response | Yes | Yes | no full receipt or evidence text |
| `auditCorrelation` | response-local actor/corpus/outcome linkage | Yes | Yes | preserves canonical audit fields |
| `syntheticProofMatrix` | deterministic later-build cases | Yes | Yes | cases only; no execution |
| `GROUNDING_EVIDENCE_UNAVAILABLE` | bounded negative response discriminator | Yes | Yes | zero provider calls |
| `effectiveServerFilters` | server-computed filters retained for audit | Yes | Yes | client input cannot widen authority |
| `routeResponseUnion` | discriminated response variants | Yes | Yes | exhaustive variant table |
| `projectionLimits` | finite record and byte bounds | Yes | Yes | justified constants and overflow denial |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | accepted D1 design released to bounded normative SPEC reconciliation |
| scope classification | documentation-only, exact two worker outputs, R1 |
| risk sensitivity | evidence and authorization boundary; public synthetic data only |
| selected role route | `MULTI_AGENT_MULTI_ROLE` |
| role separation basis | dispatcher authors packet; no-commit worker specifies; independent reviewer closes |
| escalation condition | source contradiction, unsafe projection, missing finite bound, forbidden path, or later lifecycle need |

## Execution Plan

| Step | Worker action | Evidence |
|---|---|---|
| 1 | capture execution base/status, rerun ADIF and pre-implementation gate | worker return |
| 2 | refresh source verification and T2/T3/T4 contradiction | SPEC source map |
| 3 | define narrow authority/precedence and normative vocabulary | SPEC contract |
| 4 | define validation, eligibility, mixed-escalate ordering, escaping, and finite limits | normative matrices |
| 5 | define discriminated responses, provider/no-provider minimization, and audit boundaries | response/audit schemas |
| 6 | define synthetic allow/deny cases and later-build candidate manifest | proof matrix |
| 7 | write checker-safe return, run documentation gates, leave uncommitted | return and Git evidence |

## Required Specification Schema

The reference SPEC must include:

1. authority, applicability, and narrow precedence over conflicting T3/T4 text;
2. existing source symbols versus doc-only-new vocabulary;
3. normative terms `MUST`, `MUST NOT`, `SHOULD`, and `MAY`;
4. runtime validation for every projection-driving field;
5. public-only sensitivity normalization and effective server filters;
6. mixed direct plus escalate fail-close ordering;
7. allowlisted evidence projection and safe escaping/serialization;
8. justified finite per-record evidence, record-count, and aggregate serialized
   evidence byte bounds with fail-closed overflow;
9. discriminated route response union;
10. minimized no-provider and fixed safe provider-error client responses;
11. canonical AuditReceipt, effective filters, and `model_response_hash` retention;
12. auth-denial and invalid-body audit boundary;
13. response-local audit correlation only;
14. threat matrix, synthetic acceptance cases, rejection criteria, and later-build manifest.

## T3/T4 Reconciliation Matrix

| Prior contract | Conflict | S1 required resolution | Scope limit |
|---|---|---|---|
| T3 `contentSnippet` display hint | D1 needs evidence text for grounded provider output | ratify only validated, escaped, bounded public snippet as LPCI1-Web model evidence | no general corpus/evidence promotion |
| T4 full receipt as model context | full receipt violates minimization | replace provider input for this route with derived allowlisted projection | internal canonical receipt remains available for audit logic |
| T2/T3 non-public authorization | no grant owner exists | fix S1 to public-only; unknown and all non-public deny | no general authorization design |
| T4 AuditReceipt | audit fields remain required | retain canonical receipt, effective filters, and response hash | no durable storage claim |

The SPEC must state exact supplement/supersession language and must not claim
wholesale replacement of T2/T3/T4.

## Runtime Audit Requirements

Although BUILD is forbidden, the SPEC must define later-testable requirements:

- validate types, enum membership, finite lengths, required content, dates, and
  path/status/class fields before any projection-driving use;
- preserve most-restrictive/fail-closed behavior when direct and escalate rows
  coexist; no filtering step may silently downgrade escalation;
- escape every projected field against delimiter, markup, control-character,
  prompt-boundary, and serialization injection;
- select and justify one finite maximum record count, one per-record evidence
  limit, and one aggregate serialized-evidence byte limit; reject overflow before
  provider dispatch with zero calls;
- define a discriminant and exact field allowlist for each route response;
- retain canonical `AuditReceipt`, server-computed effective filters, and
  `model_response_hash` across applicable post-auth outcomes;
- return one fixed safe provider-error message to clients; raw provider status,
  body, stack, endpoint, model, and diagnostic text remain server-internal;
- clarify that authentication denial occurs before LPCI audit construction and
  is evidenced by route-governance proof; invalid JSON after successful auth
  must have an explicitly specified audit disposition rather than an implied one.

## Required Threat Matrix

Cover at least: client clearance true, missing/unknown/non-public sensitivity,
malformed enum/type/date/path/class, blank and oversize evidence, control and
delimiter injection in every projected field, aggregate overflow, mixed direct
and escalate rows, service identity without grant, impersonation, cross-corpus
inference, no provider, provider error, auth denial, invalid JSON, and response
shape confusion.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reference/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md` | CREATE |
| `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_WORKER_RETURN_2026-08-08.md` | CREATE |

## Required Artifact Manifest

| Path | Required state at return | Owner |
|---|---|---|
| `docs/reference/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md` | untracked or modified, unstaged, uncommitted | worker |
| `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_WORKER_RETURN_2026-08-08.md` | untracked or modified, unstaged, uncommitted | worker |

## Forbidden Path Manifest

| Path family | Disposition |
|---|---|
| existing LPCI T2/T3/T4 references | READ_ONLY |
| `EXTENSIONS/` source and tests | READ_ONLY |
| roadmap, GC-018, work order, handoff, and session state | REVIEWER_OWNED_READ_ONLY |
| corpus registry, generated state, public-sync, environment files | FORBIDDEN |
| any path outside the two required artifacts | FORBIDDEN |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| reference SPEC output | ABSENT | ABSENT | return to reviewer before overwriting |
| worker return output | ABSENT | ABSENT | return to reviewer before overwriting |
| unrelated dirty path | ABSENT | ABSENT | stop and report exact collision |

## Required Proof Manifest

| Proof | Required evidence |
|---|---|
| execution anchor | worker-captured `executionBaseHead` |
| scope | initial/final `git status --short --untracked-files=all` and name-status diff |
| source freshness | repeated decision-driving source reads/searches |
| structural quality | worker-return fast gate and applicable documentation gates |
| no execution | N/A with reason: runtime/test/provider/live execution is forbidden |
| no commit | unstaged/uncommitted status and worker statement |

## Write Ownership

Worker owns only the two fulfillment-manifest outputs and must not stage or
commit. Reviewer owns packet changes, accepted repairs, optional completion
review, roadmap status, material commit, and session synchronization.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap/design requirement | Work-order instruction | Closure evidence | Status |
|---|---|---|---|
| reconcile T3/T4 grounding | Required Specification Schema and reconciliation matrix | normative precedence section | SATISFIED |
| public-only authorization | runtime audit and threat requirements | normative decision table | SATISFIED |
| no full receipt disclosure | response and projection requirements | exact field allowlists | SATISFIED |
| audit correlation | runtime audit requirements | audit matrix | SATISFIED |
| deterministic later proof | threat and synthetic case requirements | proof matrix | SATISFIED |
| no implementation | exact write/forbidden manifests | Git and no-execution evidence | SATISFIED |

## Worker Autonomy / No-Question Rule

Proceed without operator confirmation for allowed read-only investigation,
normative specification decisions inside D1, formatting repairs, and gate
reruns. Return only for source contradiction, missing authority, forbidden path,
unsafe finite-limit decision, risk expansion, external effect, or later
lifecycle need.

## Agent Handoff Contract Control Block

Contract source archive-qualified checker exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher/reviewer -> no-commit specification worker -> independent reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=d68653ed9; executionBaseHead=current HEAD captured before worker edits; closureBaseHead=reviewer captures worker-return base |
| changedSetScope(phase) | dispatch=paired packet; execution=two worker outputs; closure=accepted outputs and bounded reviewer repairs; session sync=canonical continuity only |
| traceScope(phase, actor) | every actor records phase-local trace and exact manifest |
| commitOwner(phase) | dispatcher commits packet; worker must not commit; reviewer commits accepted material; steward commits continuity |
| crossBatchIsolation | one LPCI1-WEB-S1 batch begins from a clean worktree |
| nextMoveSurfaces | reviewer updates only after accepted SPEC decision |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_COMPLETION_2026-08-08.md` (optional; create only if separate closure evidence is necessary) |
| reviewerOwnedClosurePaths | reference SPEC, worker return, optional completion review, and intake roadmap status |
| closureOwner | primary reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_WORKER_RETURN_2026-08-08.md`

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

Before writing either output, read checker source for that docType, path family,
and conditional content class. Derive exact reference and worker-return headings,
trace labels, Delta fields, public disposition, conditional controls, and
no-commit evidence shape.

The return must contain a real `## Conditional Controls Disposition` section and
the line `conditionalControlsDisposition: EKI_NA; RIH_NA; CCRI_NA` unless
evidence makes a full conditional control applicable.

## Evidence Reuse And Encoding Plan

| Field | Value |
|---|---|
| verificationMode | RECOMPUTE_REQUIRED |
| priorEvidenceUse | accepted D1 and dispatch audits are leads and authority inputs, not substitutes for current source reads |
| currentSourceRequirement | refresh every decision-driving source and contract at execution base |
| encoding | ASCII for new prose and fields |
| rawEvidenceBoundary | no secrets, sensitive corpus content, provider payload, or unbounded source copy |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| foundationChange | NONE |
| ownerSurface | existing LPCI1-Web source family plus new private reference SPEC |
| newDurableFoundation | N/A with reason: SPEC cannot create or select persistence |
| generatedAggregate | N/A with reason: no generated aggregate is edited |

## Acceptance Criteria

- exact two worker artifacts and no other write;
- narrow T3/T4 reconciliation with explicit precedence;
- all projection-driving fields receive runtime-validation requirements;
- mixed direct plus escalate remains fail-closed;
- every projected field is escaped;
- finite record-count, per-record, and aggregate serialized-byte bounds are
  selected with rationale and fail-closed overflow;
- discriminated response union is exhaustive and minimized;
- canonical AuditReceipt, effective server filters, and response hash remain;
- provider errors use fixed safe client text;
- auth and invalid-body audit boundary is explicit;
- all non-public/unknown records remain denied and client clearance is inert;
- no runtime, test, provider, persistence, vector/RAG, public, or readiness claim;
- worker returns unstaged and uncommitted.

## Review Gate

Primary reviewer must independently verify source facts, normative consistency,
finite limits, fail-close ordering, exact changed set, gate evidence, and claim
boundary. Worker completion is `COMPLETE_PENDING_REVIEW`, not closure.

## Evidence Requirements

- execution base and initial/final status;
- exact two-path name-status/diff evidence;
- refreshed source/contract verification;
- ADIF resolver result;
- worker-return fast gate and `git diff --check`;
- complete worker-return trace, epistemic, Delta, conditional, and public blocks;
- explicit N/A reason for every forbidden runtime/test/provider proof class.

## Closure Checklist

- [x] execution base captured before worker edits
- [x] exact worker ADIF query rerun and disclosed
- [x] only two worker-manifest paths changed during worker execution
- [x] normative SPEC resolves every required decision
- [x] Source Verification and doc-only fields remain separated
- [x] worker-return fast gate passes
- [x] runtime/test/provider/live execution remains N/A with reason
- [x] worker did not stage or commit
- [x] independent reviewer records final acceptance

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_COMPLETION_2026-08-08.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_LPCI_CURRENT_OWNER_GROUNDING_AND_CLEARANCE_DEFECT_INTAKE_ROADMAP_2026-08-08.md` | `Status: LPCI_CONFORMANCE_SPEC_ACCEPTED_BOUNDED_HOLD_BEFORE_BUILD` | PASS |
| Reference SPEC | `docs/reference/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md` | accepted documentation contract | PASS |
| Worker return | required worker-return path | `COMPLETE_PENDING_REVIEW`; reviewer accepted after repair | PASS |
| Registry JSON | N/A path because registry mutation was forbidden | no registry authority | BLOCKED with reason |
| Registry Markdown | N/A path because registry mutation was forbidden | no registry authority | BLOCKED with reason |
| External evidence digest | N/A with reason: repository-local source packet only | no external artifact consumed | N/A with reason |
| System loop interlock | intake roadmap | BUILD remains parked | PASS |
| Session continuity | separate post-material session-sync | protected paths excluded | N/A with reason |
| Public export | private completion | `DEFERRED_PRIVATE_ONLY` | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| exact worker output count | 2 | PASS |
| execution base | `88a3e6b2a` | PASS |
| worker commit permission | `WORKER_MUST_NOT_COMMIT` | PASS |
| reviewer-fast checks | 62 PASS | PASS |
| independent verdict | `FINAL PASS` | PASS |
| runtime/provider calls | 0 | PASS |
| next lifecycle | HOLD_BEFORE_BUILD | PASS |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if a source fact is missing/contradicted; the SPEC
cannot choose justified finite limits; T3/T4 cannot be reconciled safely; any
required action touches forbidden paths, runtime/tests, secrets, provider/live,
persistence, vector/RAG, public-sync, or later lifecycle authority; or a gate
failure cannot be repaired inside the two output paths.

## Verification Commands

```powershell
git status --short --untracked-files=all
python governance/compat/run_worker_return_fast_gate.py
git diff --check
```

No runtime or product test command is authorized.

## Operator Checkpoint

No repeated operator question applies inside this bounded SPEC. Any BUILD,
runtime/test implementation or execution, provider/live, persistence,
vector/RAG, non-public authorization, corpus mutation, public-sync, push, or
deployment action requires a fresh explicit checkpoint and governance packet.

## Finding-To-Governance Learning Disposition

Grounding and clearance product gaps remain owned by the intake roadmap. Add an
ADIF entry only if work reveals a new repeated or non-obvious agent defect; do
not duplicate the LPCI product defects as agent-defect intelligence.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_tables.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | Dispatch Prompt Envelope ordering; closed lifecycle status; Dependency Release Evidence; Source Verification columns and claim types; New Doc-Only Fields; exact ADIF query; manifest sibling headings; Agent Handoff Contract Control Block; Reviewer Closure Conversion; WORKER_MUST_NOT_COMMIT; Fast Doc literals; trace fields; ASCII encoding; public disposition; stop tokens |
| gateRunPurpose | confirm complete source-backed packet after checker-source discovery; gates are not first discovery |
| claimBoundary | LPCI1-WEB-S1 no-commit private documentation SPEC work order |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a narrow public-only companion SPEC can reconcile
the accepted grounding conflict and define deterministic fail-close behavior
without inventing a non-public grant owner.

Evidence Comparison Requirement: compare current runtime, canonical T2/T3/T4,
D1 design, and every selected limit/response decision. Preserve contrary
evidence and explain each resolution.

Contradiction Or Gap Disposition: stop rather than infer authority when a
projection field, limit, response, audit obligation, or owner is unresolved.

Claim Update Requirement: return one reviewable normative SPEC or exact block.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LPCI1-WEB-S1 documentation/source specification only |
| claimDisposition | N/A with reason: no runtime execution-control claim is made |
| receiptEvidence | N/A with reason: no runtime receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local reads, two document writes, gate commands, and Git evidence only |
| invocationBoundary | governed local documentation analysis |
| interceptionBoundary | no provider, network, runtime, shell-interception, or agent-interception claim |
| claimLanguage | source-verified normative specification pending independent review |
| forbiddenExpansion | BUILD, runtime/test mutation or execution, provider/live, persistence, vector/RAG, corpus mutation, public-sync, deployment |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer |
| Provider or surface | local private provenance repository |
| Session or invocation | LPCI1-WEB-S1 work-order authoring, 2026-08-08 |
| Working directory | repository root |
| Command or tool surface | startup/source/checker reads, exact searches, scaffold stdout, ADIF resolver, apply_patch, pre-dispatch gates |
| Target paths | paired LPCI1-WEB-S1 baseline and work order |
| Allowed scope source | operator authority `AUTHORIZE_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_DOCUMENTATION_ONLY` |
| Before status evidence | HEAD `d68653ed9`; clean worktree |
| After status evidence | exact two-path dispatch packet pending primary review/commit |
| Diff evidence | exact two-path Git status and name-status diff |
| Approval boundary | documentation-only SPEC packet authoring |
| Claim boundary | no BUILD/runtime/test/provider/live/persistence/vector-RAG/corpus/public/deployment action |
| Agent type | dispatcher/reviewer |
| Invocation ID | `lpci1-web-s1-work-order-authoring-2026-08-08` |
| Expected manifest | paired baseline and work order only |
| Actual changed set | paired baseline and work order only |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private security/conformance specification packet with no public-sync
authority or public-safe projection.

## Claim Boundary

This work order authorizes exactly one private reference SPEC and one worker
return under no-commit review. It does not implement or prove runtime behavior,
authorize non-public retrieval, create a grant or persistence owner, execute
tests/providers, or authorize BUILD, public-sync, deployment, or readiness.
