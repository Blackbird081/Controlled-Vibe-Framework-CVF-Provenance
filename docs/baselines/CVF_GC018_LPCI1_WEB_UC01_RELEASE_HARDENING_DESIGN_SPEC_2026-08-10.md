# CVF GC-018 Baseline - LPCI1 Web UC-01 Release Hardening Design Spec

Memory class: governed-dispatch-baseline

Status: CLOSED_PASS_BOUNDED

Date: 2026-08-10

Batch ID: LPCI1-WEB-UC01-RELEASE-HARDENING-DESIGN-SPEC

Dispatch base head: `f391ec180`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: primary reviewer/closer

Worker target: delegated documentation-design worker

## Purpose

Authorize a source-backed DESIGN/SPEC-only tranche for the accepted UC-01
release-readiness gaps. The tranche defines owners, interfaces, failure
semantics, and acceptance contracts before any BUILD or hosted action.

## Operator Authority

The operator wrote `dong y, lam di` immediately after the primary agent named
the exact proposed token
`AUTHORIZE_LPCI1_WEB_UC01_RELEASE_HARDENING_DESIGN_SPEC_ONLY`. The dispatcher
records the original phrase and canonical token together. Authority is limited
to repository-local DESIGN/SPEC documentation.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id LPCI1-WEB-UC01-RELEASE-HARDENING-DESIGN-SPEC --title "LPCI1 Web UC-01 Release Hardening Design Spec" --date 2026-08-10 --base f391ec180 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "UC-01 release-readiness discovery accepted at 944fdfc56" --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit Web documentation profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with accepted readiness evidence, exact source facts, three-path manifest, role routing, and bounded design questions |
| checkerReadAheadConfirmation | dispatch-quality, ADIF disclosure, handoff boundary, worker-return quality, markdown structure, file size, and public disposition |
| docOnlyNewFields | `releaseRolePolicy`; `hostedConfigLifecycle`; `queryQuotaPolicy`; `durableAuditProjection`; `providerAttemptTimeout`; `releaseHealthContract`; `promotionRollbackContract` |
| claimBoundary | authoring provenance only; no implementation or operational claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| readiness discovery | `docs/reviews/CVF_LPCI1_WEB_UC01_RELEASE_READINESS_DISCOVERY_COMPLETION_2026-08-10.md` at material commit `944fdfc56`; verdict `UC01_RELEASE_READINESS_GAPS_REQUIRE_REMEDIATION` | accepted completion must name DESIGN/SPEC as minimum safe next tranche | SATISFIED |
| operator checkpoint | original approval phrase plus canonical token recorded above | explicit approval after exact proposed token | SATISFIED |
| clean dispatch base | `git status --short` empty at `f391ec180` | no cross-batch changes | SATISFIED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`LPCI web UC-01 release hardening design spec`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver query executed: `python governance/compat/run_adif_defect_resolver.py --task-class "LPCI web UC-01 release hardening design spec" --role dispatcher --lifecycle-phase pre-dispatch --json`

Returned defect count: 0. Disclosed defectIds: none.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch status, Source Verification Block, Dependency Release Evidence, handoff route, return shape, external-input disposition, corpus reconciliation, and public disposition |
| gateRunPurpose | confirmation evidence after source discovery |
| claimBoundary | checker conformance is not design acceptance or release evidence |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| accepted next tranche | VALUE_SET | `docs/reviews/CVF_LPCI1_WEB_UC01_RELEASE_READINESS_DISCOVERY_COMPLETION_2026-08-10.md` | header and Findings | `minimumSafeNextTranche` | reviewer completion | ACCEPT |
| route authorization before parsing | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 115 onward | `authorizeRouteGovernanceProof` | `POST` | ACCEPT |
| signed service token or valid session | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | `authorizeRouteGovernanceProof` | `authorizeRouteGovernanceProof` | route governance proof | ACCEPT |
| direct query limiter missing | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | imports and POST | `getRateLimiter` | `POST` | REJECT |
| generic limiter owner exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | line 210 | `getRateLimiter` | rate limiter factory | ACCEPT |
| exact LPCI config binding exists | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts` | binding construction | `LPCI_LLM_API_KEY` | LPCI provider binding | ACCEPT |
| response-local audit receipts exist | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | response branches | `auditReceipt` | `POST` | ACCEPT |
| direct provider-attempt timeout exists | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts` | provider execution path | `AbortSignal` | LPCI provider binding | REJECT |

## New Doc-Only Fields

| Field | Type | Intended owner | Current runtime status |
|---|---|---|---|
| `releaseRolePolicy` | DOC_ONLY_NEW | future UC-01 authorization composition | NOT_IMPLEMENTED |
| `hostedConfigLifecycle` | DOC_ONLY_NEW | future hosted configuration owner | NOT_IMPLEMENTED |
| `queryQuotaPolicy` | DOC_ONLY_NEW | future limiter composition | NOT_IMPLEMENTED |
| `durableAuditProjection` | DOC_ONLY_NEW | future minimized audit sink | NOT_IMPLEMENTED |
| `providerAttemptTimeout` | DOC_ONLY_NEW | future LPCI binding hardening | NOT_IMPLEMENTED |
| `releaseHealthContract` | DOC_ONLY_NEW | future system-health composition | NOT_IMPLEMENTED |
| `promotionRollbackContract` | DOC_ONLY_NEW | future release operations owner | NOT_IMPLEMENTED |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| five planned artifact paths | `Test-Path` returned False for all before authoring | PASS |
| exact batch token | no preexisting artifact collision at dispatch base | PASS |
| runtime names | direct `rg` reads distinguished existing symbols from new document-only names | PASS |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| Route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | primary dispatcher/reviewer/closer/commit/session steward plus one no-commit documentation worker |
| worker boundary | author exactly three fulfillment artifacts and return pending review |
| reviewer boundary | independent semantic review, repairs, closure, commits, and continuity |

## Required Decision Surface

The design and specification must resolve all eight accepted dimensions without
implementation: route authorization preservation; UC-01 role policy; hosted
secret/config lifecycle; direct distributed query limiting and provider quota;
durable minimized audit/observability; provider timeout and release health;
promotion/smoke/rollback; and deferred private-only public disposition.

## Proposed Tranche

One no-commit documentation worker authors exactly the DESIGN, normative SPEC,
and worker return named by the paired work order. The primary agent performs
independent review and closure conversion.

## Evidence / Verification

Dispatch evidence consists of the accepted readiness completion, direct source
reads, collision checks, ADIF result, range-aware pre-dispatch gate, exact
manifest, empty staging, and governed commit-steward evidence. These prove
packet quality only, not release readiness.

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | confirmed by dispatcher; worker must re-read before authoring |
| UI claim boundary | information-flow and error-state contracts only; no component, styling, runtime, hosted, or live-data mutation |

## Claim Boundary

This baseline releases only three repository-local documentation outputs. It
does not authorize BUILD, source/test/config/UI mutation, secret/private reads,
browser/server/provider/network/live/cloud action, deployment, rollback
execution, public-sync, push, production, or readiness claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this private architecture packet contains repository-specific evidence;
no public artifact or public-sync authority exists.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_UC01_RELEASE_HARDENING_DESIGN_SPEC_2026-08-10.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI1_WEB_UC01_RELEASE_HARDENING_DESIGN_SPEC_COMPLETION_2026-08-10.md` | reviewer accepted with R1 corrections | PASS |
| Roadmap state | `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md` | accepted hold before fresh BUILD authority | PASS |
| Registry JSON | N/A with reason: no classification work | no mutation authorized | BLOCKED with reason: outside design/spec scope |
| Registry Markdown | N/A with reason: no classification work | no mutation authorized | BLOCKED with reason: outside design/spec scope |
| External evidence digest | N/A with reason: repository-local sources only | no intake | N/A with reason |
| System loop interlock | completion and roadmap | fresh BUILD authority required | PASS |
| Session continuity | protected session surfaces | separate reviewer sync after material commit | N/A with reason |
