# CVF Agent Work Order - LPCI1 Web Grounding And Clearance Conformance Build

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED

Batch ID: LPCI1-WEB-B1

Date: 2026-08-09

dispatchBaseHead: `dbd5645a3`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: one delegated implementation worker

Reviewer/closer: independent primary reviewer/closer

Worker return path: `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_WORKER_RETURN_2026-08-09.md`

## Dispatch Prompt Envelope

Role: no-commit implementation worker for LPCI1-WEB-B1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_2026-08-09.md`

Paired baseline: `docs/baselines/CVF_GC018_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_2026-08-09.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: date is 2026-08-09; dispatch source base is `dbd5645a3`;
the worker must start from the committed dispatch HEAD and refresh all source
facts before editing.

Do-not-misread notes: BUILD authority is limited to the exact fourteen-path writable
manifest and deterministic local verification. It does not authorize a real
provider call, network/live/release bundle, provider configuration, corpus
mutation, persistence, grant or entitlement work, vector/RAG, public-sync,
deployment, push, or production-readiness claim.

Required first actions: read this packet and baseline completely; read the
accepted S1 specification and completion; read `DESIGN.md`; capture execution
base and clean status; rerun the worker ADIF query; run pre-implementation; then
edit only the writable manifest.

Return contract: create or update exactly the thirteen runtime/test paths and
the one worker return listed in Required Artifact Manifest; leave all changes
unstaged and uncommitted; return `COMPLETE_PENDING_REVIEW` or one exact blocked
terminal disposition.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id LPCI1-WEB-B1 --title "LPCI1 Web Grounding And Clearance Conformance Build" --date 2026-08-09 --base dbd5645a3 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "LPCI1-WEB-S1 closure 3733cedd0" --include-worker-return-skeleton --stdout` |
| generatedProfile | Web runtime implementation, deterministic non-live tests, no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact source/proof manifests, S1 normative matrix, helper split, no-live boundary, AHB/AOT and reviewer closure |
| checkerReadAheadConfirmation | applicable dispatch, handoff, trace, worker-return, closure, authority, and file-size checkers reviewed |
| docOnlyNewFields | new helper, tests, response and projection vocabulary isolated below |
| claimBoundary | scaffold provenance only |

## Purpose

Implement the accepted LPCI1-WEB-S1 public-only grounding and clearance
conformance contract in the existing cvf-web query route. Preserve canonical
retrieval precedence and AuditReceipt fields, validate all projection-driving
data, construct one bounded allowlisted evidence object, minimize route
responses, and prove all accepted cases through deterministic local tests.

## Authority Chain

1. Verbatim operator authority:
   `AUTHORIZE_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD`.
2. Paired B1 GC-018 at current source base `dbd5645a3`.
3. Accepted LPCI1-WEB-S1 specification and closure at `3733cedd0`.
4. Accepted D1 design at `docs/audits/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN_2026-08-08.md`, commit `e0ee8a000`, status `DESIGN_ACCEPTED_BOUNDED_CONDITIONAL_ON_SPEC_RECONCILIATION`, Findings / Position `exitRecommendation`, as reconciled by S1.
5. Current LPCI source and tests refreshed at the worker execution base.
6. `DESIGN.md` for the changed dashboard consumer.

Normalized token `LPCI1-WEB-B1` is new dispatch vocabulary. It is not an
existing runtime field or prior authority source.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| packet author/dispatcher | primary reviewer | source verification, packet gates, dispatch material commit |
| implementation worker | one delegated worker | exact manifest implementation, deterministic tests, worker return, no commit |
| reviewer/closer | independent primary reviewer/closer | full diff and semantic review, recomputation, allowed repair, closure decision and material commit |
| session-sync steward | reviewer-designated steward | continuity update only when a future accepted B1 material commit exists |

## Scope / Target / Owner Boundary

The target is the existing `/api/lpci/query` Web path and its current LPCI
types, filter, audit, response, dashboard, and tests. The new pure helper owns
request/index validation, public-only admission, evidence eligibility,
deterministic projection/serialization, finite limits, and response correlation
helpers. The unchanged retrieval owner continues to supply the canonical
most-restrictive answer-class primitive.

This tranche does not create a new API, provider adapter, authorization owner,
store, registry, corpus, or retrieval technology.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition | Status |
|---|---|---|---|---|
| D1 design | `docs/audits/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN_2026-08-08.md` | `e0ee8a000` | `DESIGN_ACCEPTED_BOUNDED_CONDITIONAL_ON_SPEC_RECONCILIATION` at Findings / Position, `exitRecommendation` | PASS |
| S1 dispatch | `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md` | `9fe39992c` | source-verified SPEC dispatch | PASS |
| S1 closure | `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_COMPLETION_2026-08-08.md` | `3733cedd0` | `CLOSED_PASS_BOUNDED`; later BUILD input accepted | PASS |
| current packet base | repository HEAD | `dbd5645a3` | clean base verified before authoring | PASS |
| operator checkpoint | current operator instruction | N/A with reason: recorded verbatim in this work order | exact B1 implementation and deterministic tests authorized | PASS |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | bounded LPCI1-Web contract-to-runtime conformance BUILD |
| scopeClassification | TypeScript runtime, deterministic tests, existing dashboard consumer |
| riskSensitivity | R2 because response minimization and public-only sensitivity admission are security-relevant |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | dispatcher; one no-commit implementation worker; independent reviewer/closer; later session-sync steward |
| escalationCondition | stale source, extra path, provider/live/config, new auth/grant/store/corpus owner, test failure outside scope, or accepted-SPEC contradiction |

## Required First Reads

Read completely before editing:

1. this work order;
2. the paired B1 GC-018 baseline;
3. `docs/reference/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md`;
4. `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_COMPLETION_2026-08-08.md`;
5. `DESIGN.md`;
6. `docs/reference/guard_orientation/README.md`;
7. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`;
8. `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`;
9. `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`;
10. `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`;
11. the canonical AHB contract cited with the archive-qualified checker
    exception in the Agent Handoff Contract Control Block;
12. every source and test path in the Source Verification Block and writable manifest.

## Pre-Flight Checks

Run before any edit:

```powershell
$lpciB1ExecutionBase = git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-implementation --json
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $lpciB1ExecutionBase --head HEAD --serial
```

HEAD must equal the committed dispatcher HEAD and status must be clean. Do not
use the historical `dbd5645a3` dispatch-author base as a substitute for the
worker execution base. Return `BLOCKED_STALE_EXECUTION_BASE` or
`BLOCKED_SOURCE_DRIFT` when applicable.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class implementation --role dispatcher --lifecycle-phase pre-dispatch --json`

Returned defects: NONE_RETURNED

Worker pre-implementation query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Worker resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-implementation --json`

Worker returned defects (0): NONE

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| accepted S1 is later-BUILD input | VALUE_SET | `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_COMPLETION_2026-08-08.md` | lines 45-55 | `CLOSED_PASS_BOUNDED` | S1 completion decision | ACCEPT |
| D1 status and exit recommendation are accepted conditional SPEC inputs | VALUE_SET | `docs/audits/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN_2026-08-08.md` | Status; Findings / Position, lines 228-232 | `exitRecommendation` | LPCI1-WEB-D1 design | ACCEPT |
| all MUST and synthetic cases are required | LITERAL_INVARIANT | `docs/reference/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md` | Requirements Summary, lines 504-509 | `syntheticProofMatrix` | LPCI1-WEB-S1 specification | ACCEPT |
| normative test matrix is P1-P8 and F1-F16 | VALUE_SET | `docs/reference/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md` | Synthetic Acceptance Cases, lines 453-482 | `syntheticProofMatrix` | LPCI1-WEB-S1 specification | ACCEPT |
| candidate-manifest subset P1-P5 and F1-F12 defines complete proof; corrected scope is P1-P8 and F1-F16 | VALUE_SET | `docs/reference/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md` | Later-Build Candidate Manifest, line 498 | `syntheticProofMatrix` | LPCI1-WEB-S1 specification | REJECT |
| existing answer, status, index, filter, retrieval, and audit contracts | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 3-109 | `AnswerClass`; `RecordStatus`; `LpciIndexRecord`; `FilterParams`; `RetrievalReceipt`; `AuditReceipt` | LPCI type contracts | ACCEPT |
| current client clearance affects classified admission | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.ts` | lines 15-28 and 109-120 | `applySensitivityFilter` | `runFilterPipeline` | ACCEPT |
| restrictive answer-class primitive is already correct and retained | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/retrieval.ts` | lines 15-31 and 108-122 | `mostRestrictiveAnswerClass` | `runRetrievalPipeline` | ACCEPT |
| index load uses unchecked cast and empty fallback | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 17-25 | `loadCorpusIndex` | LPCI query route | ACCEPT |
| route auth precedes JSON parse and required-field check | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 92-115 | `POST` | LPCI query route | ACCEPT |
| current prompt exposes metadata and no evidence snippet | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 40-90 and 219-242 | `buildAnswerBoundaryPrompt` | LPCI query route | ACCEPT |
| current no-provider response exposes full receipt | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 189-216 | `retrievalReceipt` | LPCI query route | ACCEPT |
| current provider error includes derived provider detail | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 245-268 | `POST` | LPCI query route | ACCEPT |
| canonical builder owns hash and supplied filters | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/audit-receipt.ts` | lines 32-74 | `buildAuditReceipt` | LPCI audit builder | ACCEPT |
| governance test directly invokes route POST | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.governance.test.ts` | lines 1-36 | `makeRequest` | LPCI query governance test | ACCEPT |
| existing route test simulates rather than invokes route | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.test.ts` | lines 1-167 | `simulateQueryRoute` | LPCI query route test | ACCEPT |
| package test runner excludes only TypeScript live-test suffix | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts, lines 14-18 | `scripts` | cvf-web package scripts | ACCEPT |
| a TSX live test exists outside that package exclusion | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx` | file path | `route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx` | cvf-web live test | ACCEPT |

The worker must refresh each row against its execution base. The corrected
scope in the REJECT row is source-backed by the normative matrix and
Requirements Summary; the stale candidate-manifest subset is non-limiting.

## Current Runtime Freshness Verification

At dispatch author base `dbd5645a3`, current line counts are:

| Path owner | Lines | Disposition |
|---|---:|---|
| `types.ts` | 140 | below threshold |
| `filter-pipeline.ts` | 191 | below threshold |
| `retrieval.ts` | 127 | read/test only; modification forbidden |
| `audit-receipt.ts` | 75 | below threshold |
| query `route.ts` | 307 | below threshold; keep bounded through helper split |
| LPCI dashboard `page.tsx` | 219 | below threshold |

The new pure helper is required for validation/serialization test seams and to
avoid placing all conformance mechanics in the route. This is maintainability
planning, not authority for unrelated extraction.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| B1 packet paths before authoring | both absent at clean `dbd5645a3` | NO_COLLISION |
| new helper/test/page-test paths at dispatch | absent from current source | DOC_ONLY_NEW |
| normalized batch token | introduced by this packet under operator authority | DOC_ONLY_NEW |
| retrieval primitive owner | present and source-verified | RETAIN_UNCHANGED |
| grant/provider/storage/vector owners | excluded by accepted public-only scope | FORBIDDEN |

## New Doc-Only Fields

| Proposed item | Kind | Intended owner | Disposition before implementation |
|---|---|---|---|
| `LPCI1-WEB-B1` | batch token | this packet | DOC_ONLY_NEW |
| `query-conformance.ts` | pure runtime helper | LPCI query conformance | DOC_ONLY_NEW |
| `query-conformance.test.ts` | pure helper test | LPCI query conformance | DOC_ONLY_NEW |
| `page.test.tsx` | dashboard consumer test | LPCI dashboard | DOC_ONLY_NEW |
| `modelEvidenceProjection` | accepted contract concept | helper | DOC_ONLY_NEW |
| `evidenceEligibilityRule` | accepted contract concept | helper | DOC_ONLY_NEW |
| `effectiveServerFilters` | server-computed filter value | helper/route | DOC_ONLY_NEW |
| `routeResponseUnion`; `outcome` | discriminated response contract | types/route/page | DOC_ONLY_NEW |
| `evidenceOutcome`; top-level `auditId` | response correlation | types/route | DOC_ONLY_NEW |
| `GROUNDING_EVIDENCE_UNAVAILABLE` | route outcome | types/route | DOC_ONLY_NEW |
| `projectionLimits` | finite bounds | helper | DOC_ONLY_NEW |

Final TypeScript identifiers must be listed in the worker-return Source
Verification refresh. New names must not be claimed as pre-existing source.

## Protocol / Contract / Requirements

### Request And Index Validation

Implement every S1 request rule before corpus work: scalar-valid strings,
unpaired-surrogate rejection, trimmed nonempty query, exact byte limits,
corpus-ID grammar, exact unique status members, bounded facets, and effective
`sensitivityClearance:false`. Authentication denial and invalid JSON/body remain
outside LPCI AuditReceipt construction and include route governance proof only.

For a registered index, distinguish missing/read failure, invalid JSON,
non-array root, non-object rows, invalid sensitivity, excluded non-public rows,
and malformed admitted-public rows exactly as S1 requires. Never inspect or
expose non-sensitivity fields of a denied row before Stage 1 completes.

### Public-Only Filter And Restrictive Semantics

Admit exactly canonical `public` rows. Missing, unknown, restricted,
confidential, and classified rows cannot reach search, receipt, audit paths,
projection, or provider context. Client clearance, session, service-token,
impersonation, role, scope, or grant-shaped input cannot elevate admission.

Retain `mostRestrictiveAnswerClass` from the unchanged retrieval source.
Mixed direct plus `ESCALATE_OR_ABSTAIN` final matches abstain with zero provider
calls. Do not drop the restrictive record to obtain an answer.

### Evidence Projection And Limits

Every final non-escalate record must pass path, effective-date, status,
answer-class, authority-shape, and trimmed nonblank snippet validation. Build
one deterministic compact RFC 8259 JSON evidence object containing only the S1
top-level and per-record allowlists. All projected fields pass through the same
serializer. No raw interpolation or second prompt structure is allowed.

Enforce at most four records, at most 512 Unicode code points per snippet after
outer trim, and at most 16384 UTF-8 bytes over the final escaped serialized
object. A fifth record, 513th code point, 16385th byte, or unpaired surrogate
returns grounding unavailable with zero calls and no truncation or selective
answer.

### Route Response Union And Audit

Implement the required `outcome` discriminant for all nine S1 variants and the
exact additional-field allowlists. Never return `RetrievalReceipt`, matched
records, snippets, hashes, provider endpoint/model/status/body, stack, grant,
or diagnostics.

Here `hashes` means `sourceHash` and other source/evidence hashes outside the
canonical AuditReceipt. Retain `auditReceipt.model_response_hash` exactly as
required by S1; it is mandatory audit evidence, not a forbidden response leak.

Preserve canonical AuditReceipt fields. Supply `effectiveServerFilters`, exact
`sensitivity_pre_filter_applied`, canonical phase-one type where applicable,
and S1 response-boundary/evidence-outcome mapping. Top-level `auditId` equals
the nested audit ID. Authorization decision, actor/auth mode, corpus, outcome,
and matched paths satisfy every S1 correlation invariant.

Hash the exact safe emitted client payload input specified by S1. Provider
failure returns exactly `The answer provider is temporarily unavailable.` and
never exposes provider-derived detail. Provider attempt count is at most one.

### Dashboard Consumer

Replace the optional-field response bag with the discriminated union. Render
only fields allowed for the active outcome. For no-provider display, derive the
source count from `auditReceipt.matched_paths`, never a returned retrieval
receipt. Preserve accessible loading, empty, error, status, keyboard, and
non-color-only communication required by `DESIGN.md`. This is a response-state
conformance change, not a visual redesign.

## Aggregate Case-To-Test Ledger

All accepted cases are mandatory across the aggregate suite. The helper owns
only applicable pure validation/projection cases; it does not own the complete
matrix alone.

| Suite owner | Assigned cases | Required coverage |
|---|---|---|
| pure query-conformance helper | P1-P2 projection/byte portions; F1, F5-F7, F14-F16 pure validation portions | eligibility, deterministic serialization, limits, Unicode, invalid admitted rows |
| filter pipeline | P4-P5; F2-F3, F11 | clearance equivalence, sensitivity-first public admission, grant-shaped non-elevation |
| retrieval regression | F4 | retained most-restrictive class and mixed direct/escalate behavior |
| audit builder | P7-P8; F8 hash portion | canonical fields, exact safe-payload bytes, retained `model_response_hash` |
| direct POST route | P1-P3, P6-P8; F1-F16 integration portions | actual branch union, filesystem/provider mocks, exact zero/one fetch counts, response allowlists |
| governance route | F9-F10 and P7 auth/correlation portion | authentication and invalid-body audit boundary, route proof |
| dashboard UI | P3 and F8/F12 client portions | discriminated rendering, audit matched-path count, no forbidden-field dependency |

The worker return must provide an exhaustive ID-by-ID ledger for P1 through P8
and F1 through F16. Overlap is allowed; an unassigned ID is blocking.

The stale S1 candidate-manifest text P1-P5/F1-F12 does not limit the normative
matrix. Partial case coverage is a blocking defect.

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work-order instruction | Required evidence |
|---|---|---|
| public-only sensitivity | validation and filter sections | P4-P5, F2-F3, F11 |
| restrictive class | unchanged retrieval plus route abstention | F4; zero fetch; no retrieval diff |
| eligible evidence only | helper validation and whole-route fail-close | P1-P2, F1, F14 |
| deterministic safe projection | one serializer and finite bounds | P1-P2, F5-F7, F15-F16 |
| minimized discriminated responses | exact outcome union and allowlists | P3, P6-P8, F8-F13 |
| canonical audit | effective filters, hashes, path/correlation equality | P6-P8 and every audited branch |
| Web consumer | discriminated page and audit-path count | P3 UI test and error/outcome cases |
| bounded BUILD | exact changed set and package-owned runner with complementary TSX live-test exclusion | Git/gate/test evidence; no external effect |

## Worker Autonomy / No-Question Rule

Resolve in-scope TypeScript design details, mocks, test fixtures, lint, type,
and deterministic test defects directly. Preserve the accepted S1 outcomes,
allowlists, limits, and exact messages. Stop only for a return-to-orchestrator
condition; do not ask preference questions for ordinary in-scope repairs.

## Write Ownership

### Worker-Owned Writable Paths

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/query-conformance.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.ts`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/audit-receipt.ts`
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts`
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx`
7. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/query-conformance.test.ts`
8. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.test.ts`
9. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/retrieval.test.ts`
10. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/audit-receipt.test.ts`
11. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.test.ts`
12. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.governance.test.ts`
13. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.test.tsx`
14. `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_WORKER_RETURN_2026-08-09.md`

### Reviewer-Owned Closure Paths

- this work order;
- `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_COMPLETION_2026-08-09.md`;
- bounded intake-roadmap disposition if closure is accepted;
- canonical continuity surfaces only in a separate session-sync commit.

## Work-Order Fulfillment Manifest

Fulfillment requires every required writable artifact, no path outside the
manifest, every proof result, a complete worker return, zero staged paths, and
unchanged HEAD throughout worker execution.

## Required Artifact Manifest

| Artifact class | Required path | Owner | Required state |
|---|---|---|---|
| LPCI types | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | worker | modified |
| conformance helper | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/query-conformance.ts` | worker | new |
| public-only filter | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.ts` | worker | modified |
| canonical audit builder | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/audit-receipt.ts` | worker | modified |
| LPCI query route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | worker | modified |
| LPCI dashboard | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx` | worker | modified |
| helper tests | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/query-conformance.test.ts` | worker | new |
| filter tests | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.test.ts` | worker | modified |
| retrieval regression tests | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/retrieval.test.ts` | worker | modified |
| audit tests | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/audit-receipt.test.ts` | worker | modified |
| direct route tests | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.test.ts` | worker | modified |
| auth/body governance tests | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.governance.test.ts` | worker | modified |
| UI consumer tests | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.test.tsx` | worker | new |
| worker return | `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_WORKER_RETURN_2026-08-09.md` | worker | new |

## Forbidden Path Manifest

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/retrieval.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`
- every package lockfile and dependency manifest
- corpus registry and corpus index artifacts
- auth, session, service-token, impersonation, role, grant, entitlement,
  persistence, database, migration, vector, embedding, or RAG owners
- provider adapters, provider/model/key/environment configuration, real keys,
  and configuration-file mutation; synthetic process-local test placeholders are allowed below
- live test files and release bundle scripts
- governance checkers and root agent instructions
- this baseline and work order during worker execution
- accepted SPEC, roadmap, completion review, session, and handoff surfaces
- public-sync clone and deployment surfaces
- every path not listed in Required Artifact Manifest

## Forbidden Filesystem State At Dispatch

- dirty or staged worker execution base;
- worker output already present;
- HEAD different from the committed dispatcher HEAD;
- any change outside the exact worker manifest;
- pre-existing mutation of the forbidden retrieval primitive;
- installed dependency or lockfile drift.

## Required Proof Manifest

| Proof | Path or command owner | Required literal/result | Required at handoff |
|---|---|---|---|
| direct POST branch coverage | route and governance tests | mocked filesystem/fetch; synthetic process-local key placeholder; exact zero/one fetch counts; zero network | Yes |
| aggregate conformance coverage | all seven suite owners in Aggregate Case-To-Test Ledger | P1-P8 and F1-F16 exhaustively assigned and passing | Yes |
| pure helper coverage | helper test | only applicable validation/projection/serialization cases | Yes |
| restrictive primitive | retrieval tests and Git diff | regression PASS; production retrieval source unchanged | Yes |
| public-only filtering | filter tests | clearance equivalence and denied-row noninspection | Yes |
| audit/hash correlation | audit and route tests | exact effective filters, paths, boundary, safe-payload hash | Yes |
| UI discrimination | page test | outcome-specific fields and audit matched-path count | Yes |
| focused tests | package non-live runner | PASS with exact test/file counts | Yes |
| static validation | package `check` and `lint` | PASS | Yes |
| full regression | package-owned `npm run test:run` with complementary TSX exclusion | PASS; package script excludes TypeScript live tests and command excludes TSX live tests | Yes |
| maintainability | GC-023 and before/after line counts | PASS | Yes |
| changed-set/no-commit | Git evidence | exact manifest, empty staging, unchanged HEAD | Yes |
| worker return | worker-fast gate | PASS | Yes |

## Execution Plan

1. Capture clean execution base and run ADIF/pre-implementation.
2. Refresh Source Verification and exact line counts.
3. Define discriminated response, projection, and validation types.
4. Implement the pure conformance helper and its applicable validation/projection tests.
5. Change Stage 1 to exact public-only admission without modifying retrieval.
6. Extend audit construction only as required by canonical S1 hash/correlation.
7. Integrate the helper into the route with mocked filesystem/provider seams.
8. Update direct POST and governance tests; prove exact fetch counts.
9. Update the dashboard union consumer and new UI test under `DESIGN.md`.
10. Run focused tests, check, lint, full non-live tests, GC-023, and diff checks.
11. Create the complete worker return, run worker-fast, and stop without staging
    or committing.

## Evidence Requirements

The worker return must record:

- execution base and actual clean-start status;
- refreshed source facts and final identifiers;
- exact changed-set and staged-set evidence;
- required-artifact and proof-manifest reconciliation;
- aggregate P1-P8/F1-F16 ID-by-ID case-to-test ledger across helper, filter,
  retrieval, audit, direct-POST, governance, and UI suites;
- direct POST mocked filesystem/fetch seams, synthetic process-local
  `LPCI_LLM_API_KEY` placeholder lifecycle, zero network, and exact fetch counts;
- exact serialization golden bytes, four/five-record and 16384/16385-byte edges;
- Unicode code-point and unpaired-surrogate cases;
- auth/invalid-body no-audit boundary;
- all response allowlists and forbidden-field negative assertions;
- audit ID/filter/hash/path correlation assertions;
- before/after line counts and helper-split evidence;
- focused test, check, lint, package-owned full non-live test with TSX exclusion, GC-023, worker-fast, and diff
  command results with counts;
- retrieval production source unchanged;
- no live/provider/network/release bundle/config/store/grant/vector-RAG/corpus/
  public/deployment action;
- no stage, no commit, and terminal disposition.

## Epistemic Process Block

### Expected Result / Prediction

The accepted S1 contract should be implementable inside the exact manifest by
adding one pure helper, retaining the existing restrictive primitive, and
changing only the current filter, audit, route, types, dashboard, and tests.

### Evidence Comparison

Compare the implemented response shapes, bytes, call counts, audit values,
source diff, and complete synthetic matrix against the accepted S1 literals.
Test PASS alone is insufficient when a field allowlist or claim differs.

### Contradiction Or Gap Disposition

Resolve in-scope implementation/test contradictions directly. Treat the stale
P1-P5/F1-F12 candidate subset as superseded by the normative P1-P8/F1-F16
matrix. Return blocked for any other accepted-SPEC contradiction or need for an
unlisted owner.

### Claim Update

The worker may claim only implementation complete pending independent review.
It may not claim accepted conformance, live/provider proof, release quality,
production readiness, public export, or deployment.

## Acceptance Criteria

- [x] Full S1 MUST/MUST NOT rules and P1-P8/F1-F16 are mapped and pass.
- [x] Aggregate case ledger assigns every ID to applicable suite owners; helper owns only applicable pure cases.
- [x] Query/filter strings reject unpaired surrogates before trim/byte count.
- [x] Index container/sensitivity/admitted-public validation follows exact order.
- [x] Only exact public rows reach search, audit paths, projection, or provider.
- [x] Client clearance, identity, role, or grant-shaped input never elevates.
- [x] Existing most-restrictive primitive is retained and production retrieval is unchanged.
- [x] Mixed direct/escalate abstains with zero fetch calls.
- [x] Every projection-driving value is validated and every field serialized safely.
- [x] Four-record/16384-byte limits pass and five-record/16385-byte cases fail closed without truncation.
- [x] All response variants use `outcome` and exact S1 field allowlists.
- [x] No-provider response contains no retrieval receipt and UI count uses audit paths.
- [x] Provider failure exposes only the exact fixed safe message.
- [x] AuditReceipt canonical fields, effective filters, hash, and correlation invariants hold.
- [x] `model_response_hash` is retained; only source/evidence hashes outside canonical AuditReceipt are forbidden.
- [x] Auth denial and invalid body have route proof, no LPCI audit, and zero fetch.
- [x] Direct POST, helper, filter, retrieval, audit, route-governance, and UI tests pass.
- [x] Synthetic process-local `LPCI_LLM_API_KEY` placeholder and mocked fetch use zero network and are restored after tests.
- [x] Check, lint, package-owned full non-live tests with TSX exclusion, GC-023, worker-fast, and diff checks pass.
- [x] Actual changed set is exact; retrieval source, package, lockfiles, and every forbidden path are unchanged.
- [x] Worker returned unstaged and uncommitted.

## Review Gate

The reviewer must inspect the entire diff, recompute source and line counts,
review every synthetic mapping and forbidden-field assertion, rerun all required
commands, confirm the retrieval production source is unchanged, and decide
closure. Worker PASS language and gate success are not semantic acceptance.

## Closure Diff Gate

Before closure, compare:

| Source | Comparison target | Required result |
|---|---|---|
| S1 every MUST/MUST NOT | runtime and tests | no omitted or weakened requirement |
| S1 P1-P8/F1-F16 | case-to-test ledger | every case has deterministic evidence |
| B1 writable manifest | actual changed set | exact match |
| forbidden manifest | Git diff/status | no mutation |
| work-order proofs | worker return and reviewer rerun | all resolved PASS, N/A with reason, or BLOCKED |
| worker claims | actual receipts | no live/release/production/public overclaim |

## Closure Checklist

- [x] Worker return admitted only after independent review.
- [x] Every acceptance item resolved PASS, N/A with reason, or BLOCKED.
- [x] Roadmap-to-work-order and SPEC-to-test matrices reconciled.
- [x] Exact changed set and forbidden-path evidence recorded.
- [x] Runtime/test results and no-live claims are command-backed.
- [x] Completion review records repairs and final bounded claim.
- [x] Material and continuity commits remain separate.
- [x] No open checkbox remains after conversion to closed status.

## Return-To-Orchestrator Conditions

Return the matching blocked disposition when:

- execution base is stale or dirty;
- a decision-driving symbol changed incompatibly;
- any path outside the writable manifest is required;
- accepted S1 requirements conflict beyond the recorded stale subset label;
- retrieval production source modification appears necessary;
- public-only admission cannot be proven before other row inspection;
- any fail-close branch can reach fetch;
- safe serialization or exact byte limits cannot be implemented in scope;
- check, lint, deterministic test, full non-live regression, GC-023, or
  worker-fast cannot pass in scope;
- provider/live/release bundle, key/config, persistence/grant/vector-RAG,
  corpus/registry, public-sync, deployment, or push is needed.

## Terminal Disposition Enum

Return exactly one:

- `COMPLETE_PENDING_REVIEW`
- `BLOCKED_STALE_EXECUTION_BASE`
- `BLOCKED_SOURCE_DRIFT`
- `BLOCKED_TEST_FAILURE`
- `BLOCKED_SCOPE_EXPANSION_REQUIRED`
- `BLOCKED_SPEC_CONTRADICTION`

Only `COMPLETE_PENDING_REVIEW` may accompany a closure recommendation.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_WORKER_RETURN_2026-08-09.md`

```text
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: python governance/compat/run_worker_return_fast_gate.py
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED
requiredEvidenceTerms: executionBaseHead; git status --short
requiredSections: Purpose; Scope / Methodology; Findings / Position; Risk / Corrective Action; Delta Execution Claim Boundary Control Block; Machine Closure Package
conditionalDispositionRule: Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; and Epistemic Process Block must each contain evidence when applicable, otherwise record N/A with reason
```

The return must also contain Source Verification refresh, Work-Order
Fulfillment Manifest, Required Artifact Manifest reconciliation, proof table,
case-to-test matrix, line-count table, exact changed set, Epistemic Process
Block, External Knowledge Intake Routing, Corpus Completeness And Report
Integrity, Rescan Intelligence Hardening, Finding-To-Governance Learning
Disposition, Agent Operation Trace Block, Delta Execution Claim Boundary
Control Block, Machine Closure Package, Public Export Disposition, Claim
Boundary, and no-staging/no-commit evidence.

## Verification Commands

Run from repository root unless the command changes directory:

```powershell
git status --short --untracked-files=all
git diff --name-status
git diff --check
git diff -- EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/retrieval.ts
Push-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm run test:run -- --exclude "src/**/*.live.test.tsx" src/lib/lpci/query-conformance.test.ts src/lib/lpci/filter-pipeline.test.ts src/lib/lpci/retrieval.test.ts src/lib/lpci/audit-receipt.test.ts src/app/api/lpci/query/route.test.ts src/app/api/lpci/query/route.governance.test.ts "src/app/(dashboard)/lpci/page.test.tsx"
npm run check
npm run lint
npm run test:run -- --exclude "src/**/*.live.test.tsx"
Pop-Location
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
```

The package `test:run` script alone is not sufficient because it excludes
`.live.test.ts` but not the existing `.live.test.tsx` file. Do not run
`npm run test:live`, the release bundle, browser/live proof, or any command that
uses a real key, network, provider, public-sync, or deployment. Tests may set a
fixed fake `LPCI_LLM_API_KEY` only in process memory and mock fetch; they must
restore the environment, perform zero network, and never touch a config file.
Use only the package-owned local runner commands above. Do not invoke `npx`,
contact a package registry, or install/update any dependency.

## Near-Threshold Owner Maintainability Plan

No current writable production file is near its hard threshold at dispatch.
Still, keep validation/projection/serialization in the new pure helper and keep
the route as orchestration. Record before/after line counts. If a touched file
approaches a governed threshold, split within the same LPCI domain and only
inside the existing writable manifest; otherwise return scope expansion.

## Design Control Carry-Forward

The dashboard change must follow `DESIGN.md` and preserve existing route,
authentication, data-contract, loading, empty, error, keyboard, responsive,
contrast, and non-color-only status behavior. Do not introduce a visual
redesign, third-party identity, new navigation, or new page. Deterministic UI
tests and static checks are the authorized proof; browser/live/deployment proof
is forbidden.

## Dual Agent Surface Matrix

| Surface class | Intended actor | Interface | Authority/risk boundary | Required evidence | Adapter boundary disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | no-commit implementation worker | committed work order and local workspace | exact fourteen-path manifest; no commit | execution trace, tests, diff, worker return | ALLOWED_LOCAL_ONLY |
| EXTERNAL_AGENT_CLI_MCP | none | no CLI/MCP adapter | external execution is not authorized | zero invocation evidence | NOT_APPLICABLE_WITH_REASON |
| reviewer/closer | independent reviewer | worker return and uncommitted diff | may repair only exact worker manifest and reviewer-owned closure paths | independent rerun and closure diff | REVIEWER_OWNED |
| session-sync steward | reviewer-designated steward | canonical continuity surfaces | only when a future accepted B1 material commit exists, separate commit | generator/freshness evidence when applicable | SESSION_SYNC_ONLY |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | N/A with reason: no external knowledge input |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | no external source absorption or authority promotion |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: accepted S1 releases contract requirements, but the worker and
reviewer must recompute current source, exact bytes, fetch counts, changed set,
line counts, and deterministic test results.

unicodePathHandling: literal ASCII repository paths; protocol Unicode is tested
as data under the accepted serialization contract.

extractedTextAuthority: N/A with reason: no extracted document text is used.

Prior reviews are dependency authority only. They do not substitute for current
runtime/test verification. Agent-authored prose remains ASCII.

## Agent Handoff Contract Control Block

Contract source archive-qualified checker exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher/reviewer -> one no-commit implementation worker -> independent reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=dbd5645a3; executionBaseHead=worker captures committed dispatch HEAD; closureBaseHead=reviewer captures worker-return base |
| changedSetScope(phase) | dispatch=paired packet; execution=exact fourteen-path worker manifest; closure=accepted execution plus reviewer-owned closure paths; session sync=continuity only |
| traceScope(phase, actor) | every actor records its own phase, commands, expected/actual manifest, and delta |
| commitOwner(phase) | dispatcher owns packet commit; worker must not commit; reviewer owns material closure; steward owns separate continuity commit |
| crossBatchIsolation | Before status evidence: `git status --short` is clean; no unrelated change may share B1 execution or closure |
| nextMoveSurfaces | worker does not edit them; steward updates them only after accepted material commit |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_COMPLETION_2026-08-09.md` |
| reviewerOwnedClosurePaths | this work order; B1 completion review; bounded roadmap disposition; later continuity surfaces separately |
| workerReturnAdmission | evidence only; independent source/diff/test/claim review required |
| repairAuthority | reviewer may repair only exact worker-manifest defects without expanding scope |
| blockedConversion | missing case, stale source, extra path, permissive branch, response leak, test/gate failure, provider/live need |
| commitConversion | reviewer commits accepted material; continuity remains a separate steward commit |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_tables.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/run_agent_autorun_workflow_gate.py` |
| literalTokensReviewed | CLOSED_PASS_BOUNDED; WORKER_MUST_NOT_COMMIT; Source Verification columns; New Doc-Only Fields; Required Artifact Manifest; Forbidden Path Manifest; completionReviewPath; reviewerOwnedClosurePaths; exact AOT manifests; ASCII prose |
| gateRunPurpose | confirmation evidence after checker-source read-ahead and packet review; not first discovery |
| claimBoundary | gate compliance does not prove implementation or conformance |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author/reviewer |
| Provider or surface | local governed workspace |
| Session or invocation | LPCI1-WEB-B1 work-order authoring, 2026-08-09 |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, ADIF resolver, `apply_patch`, dispatch gates, Git evidence |
| Target paths | paired B1 baseline and work order |
| Allowed scope source | operator authority `AUTHORIZE_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD` |
| Before status evidence | HEAD `dbd5645a3`; worktree clean; packet paths absent |
| After status evidence | exact paired packet untracked, unstaged, and uncommitted |
| Diff evidence | `git status --short --untracked-files=all`; `git diff --check` |
| Approval boundary | dispatch authoring and release only |
| Claim boundary | no worker source/test mutation or execution yet |
| Agent type | dispatcher/reviewer |
| Invocation ID | `lpci1-web-b1-work-order-author-2026-08-09` |
| Expected manifest | `docs/baselines/CVF_GC018_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_2026-08-09.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_2026-08-09.md` |
| Actual changed set | `docs/baselines/CVF_GC018_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_2026-08-09.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_2026-08-09.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | bounded LPCI1-WEB-B1 implementation dispatch |
| claimDisposition | CLAIM_REJECTED - packet authoring is not runtime execution |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | ACTION_EVIDENCE_PRESENT - current source reads and packet gates |
| invocationBoundary | repository-local dispatch workflow |
| interceptionBoundary | no provider, live, network, browser, CLI/MCP, or runtime interception claim |
| claimLanguage | one no-commit worker is released only from the committed reviewed packet |
| forbiddenExpansion | no live/release proof, provider/config, persistence/grants/vector-RAG, corpus/public/deployment/readiness claim |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_COMPLETION_2026-08-09.md` | independent source review, exact manifest, and validation evidence | PASS |
| Roadmap state | `docs/roadmaps/CVF_LPCI_CURRENT_OWNER_GROUNDING_AND_CLEARANCE_DEFECT_INTAKE_ROADMAP_2026-08-08.md` | `Status: LPCI_CONFORMANCE_BUILD_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | corpus registry mutation is outside B1 authority | no registry state changed; any reconciliation requires separate authority | BLOCKED with reason |
| Registry Markdown | catalog mutation is outside B1 authority | no catalog state changed; follow-up remains parked | BLOCKED with reason |
| External evidence digest | repository-local source, Git, and command evidence only | no external artifact admitted | N/A with reason |
| System loop interlock | B1 and BR1 completions | both global drift gates remain `WAIVED_BOUNDED`, `NON-COMPLIANT`, and not PASS | BLOCKED with reason |
| Session continuity | separate session-sync after reviewer material commit | continuity paths excluded from this closure batch | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| exact B1 manifest | 10 modified and 4 new paths | PASS |
| focused conformance | 7 files, 99 tests | PASS |
| full non-live regression | 304 files; 3397 passed, 2 skipped | PASS |
| production retrieval source | unchanged | PASS |
| provider/live calls | zero; forbidden scope | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime dispatch; no public-sync authority.

## Operator Checkpoint

N/A with reason: the verbatim B1 authority defines the complete worker scope.
Any scope beyond the exact manifest remains outside this packet and returns to
the orchestrator under a distinct future authority decision.

## Claim Boundary

`CLOSED_PASS_BOUNDED` accepts the exact fourteen-path LPCI1-Web conformance
implementation after independent source review and combined validation at
HEAD `5072f553b`. The reviewer completion converts the historical worker
`BLOCKED_WITH_REASON` status after the separately governed BR1 repair removed
the unrelated package baseline failures; the historical return is not
rewritten. Production `retrieval.ts` remains unchanged. No provider/live/
release proof, real key or configuration, persistence, grants, vector/RAG,
corpus mutation, public export, deployment, push, production use, or readiness
claim is authorized.
