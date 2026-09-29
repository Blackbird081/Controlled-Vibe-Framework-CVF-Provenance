# CVF GC-018 Baseline - LPCI1 Web Grounding And Clearance Conformance Specification

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: LPCI1-WEB-S1

Date: 2026-08-08

dispatchBaseHead: `d68653ed9`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: primary reviewer/closer

Worker target: delegated documentation specification worker

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id LPCI1-WEB-S1 --title "LPCI1 Web Grounding And Clearance Conformance Specification" --date 2026-08-08 --base d68653ed9 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with current authority, source verification, dependency evidence, exact two-output scope, specification requirements, and claim boundaries |
| checkerReadAheadConfirmation | applicable dispatch, structural, handoff, trace, ADIF, Delta, encoding, public-disposition, scaffold-provenance, and file-size checker sources were read before authoring |
| docOnlyNewFields | normalized batch token; specification vocabulary listed in New Doc-Only Fields of the paired work order |
| claimBoundary | Dispatch authoring provenance only; no runtime, provider, live, public, Web implementation, or model-router behavior claim. |

## Purpose

Authorize one no-commit documentation worker to convert the accepted bounded
LPCI1-Web D1 design into a normative conformance specification. The
specification must reconcile the T3 display-hint boundary with T4 full-receipt
context wording and define a fail-closed public-only contract without changing
runtime or tests.

## Scope / Target / Owner Boundary

Scope is one new private reference specification and one worker return. Target
is the current LPCI1-Web query route, library, audit, authentication, UI, and
canonical T2/T3/T4 contract family. The existing LPCI1-Web owner remains the
only product owner; this packet creates no cross-owner or persistence owner.

The worker specifies contracts only. The independent reviewer owns acceptance,
repairs, closure conversion, roadmap status, and any material commit.

## Non-Goals

- no BUILD, runtime, source, test, UI, API, authentication, corpus, or registry edit;
- no unit, route, E2E, provider, live, or benchmark execution;
- no provider/model choice, key use, persistence, vector, embedding, RAG, or graph decision;
- no grant store, non-public authorization owner, general RBAC mapping, or durable audit claim;
- no sensitive fixture, production corpus, public-sync, push, deployment, or readiness claim.

## Authorization / Decision

Verbatim operator authority:

`AUTHORIZE_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_DOCUMENTATION_ONLY`

Normalized batch token `LPCI1-WEB-S1` is new dispatch vocabulary introduced by
this packet. It is not claimed as a prior runtime symbol, contract token, or
historical tranche name.

This authority releases documentation-only SPEC authoring and no later
lifecycle phase.

## Dependency Release Evidence

| Dependency | Evidence | Commit/base | Disposition |
|---|---|---|---|
| defect intake accepted | `docs/roadmaps/CVF_LPCI_CURRENT_OWNER_GROUNDING_AND_CLEARANCE_DEFECT_INTAKE_ROADMAP_2026-08-08.md` | `38a3a21df` | ACCEPT |
| D1 design packet released | paired D1 baseline and work order | `bd22ca0a4` | ACCEPT |
| D1 design accepted with bounded condition | `docs/audits/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN_2026-08-08.md` and corrected worker return | `e0ee8a000` | ACCEPT |
| continuity held before SPEC | active state, handoff, and front door | `d68653ed9` | ACCEPT |
| SPEC authorization | verbatim operator authority recorded above | dispatch base `d68653ed9` | ACCEPT |
| worker isolation | clean status at packet start; worker must recapture current HEAD and status | `d68653ed9` | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| accepted design requires SPEC reconciliation | VALUE_SET | `docs/audits/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN_2026-08-08.md` | Selected Model Evidence Projection; Findings / Position | `exitRecommendation` | D1 design decision | ACCEPT |
| current record evidence and sensitivity fields | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 33-50 | `contentSnippet`; `sensitivityLevel` | `LpciIndexRecord` | ACCEPT |
| client clearance input | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 52-58 | `sensitivityClearance` | `FilterParams` | ACCEPT |
| full matched records retained in receipt | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/retrieval.ts` | lines 108-122 | `matched_records` | `runRetrievalPipeline` | ACCEPT |
| client boolean controls current sensitivity filter | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.ts` | lines 14-28 and 109-120 | `applySensitivityFilter` | `runFilterPipeline` | ACCEPT |
| metadata-only model prompt | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 40-72 and 219-242 | `buildAnswerBoundaryPrompt` | LPCI query route | ACCEPT |
| no-provider branch returns full receipt | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 189-216 | `retrievalReceipt` | LPCI query no-provider response | ACCEPT |
| route provides authenticated identity evidence | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 64-85 and 118-208 | `actorId`; `authMode`; `session` | route governance proof contracts | ACCEPT |
| session and impersonation facts exist | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | lines 19-30 and 118-155 | `SessionCookie`; `verifySessionCookie` | middleware authentication | ACCEPT |
| service identity exists without LPCI grant semantics | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | lines 23-25 | `deriveServiceTokenIdentity` | service-token authentication | ACCEPT |
| canonical five-level sensitivity policy | VALUE_SET | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | Sensitivity Classification (NR-06) | `sensitivityLevel` | LPCI1 T2 contract | ACCEPT |
| T3 snippet and operator-controlled sensitivity rules | VALUE_SET | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | Searchable Fields; Stage 1 - Sensitivity Pre-Filter | `contentSnippet`; `classification_access`; `confidential_access` | LPCI1 T3 contract | ACCEPT |
| T4 full-receipt context and grounding requirements | VALUE_SET | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | RetrievalReceipt Schema; Answer Boundary Rules | `RetrievalReceipt` | LPCI1 T4 contract | ACCEPT |
| current pilot is public synthetic data | VALUE_SET | `docs/corpus-intelligence/GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json` | records array | `sensitivityLevel` | pilot index | ACCEPT |

## Current Runtime Freshness Verification

At dispatch base `d68653ed9`, direct reads confirm the design-driving source and
T2/T3/T4 contradiction remain current. No server-owned LPCI grant reader,
corpus entitlement owner, or general non-public authorization contract was
source-verified. The SPEC must retain the accepted `PUBLIC_ONLY` boundary.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| path existence | exact four planned packet/output paths returned `False` before authoring | NO_COLLISION |
| token search | `rg -n 'LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC|LPCI1-WEB-S1' docs CVF_SESSION AGENT_HANDOFF_V55_2026-08-05.md` returned no matches | DOC_ONLY_NEW |
| generic authorization collisions | team permissions, GC-051 registration, Web knowledge-collection scopes, and service-token identity were reviewed | PATTERN_ONLY_NOT_LPCI_AUTHORITY |
| proposed vocabulary | all new specification fields must be declared doc-only new | RUNTIME_CLAIM_BLOCKED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`design specification`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "design specification" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional ADIF-specific instruction; all standing guards remain binding |

Worker pre-implementation query:

`python governance/compat/run_adif_defect_resolver.py --task-class specification --role worker --lifecycle-phase pre-implementation --json`

Current worker-query result: NONE_RETURNED. The worker must rerun it at its
execution base and disclose any changed result.

## Specification Questions

1. What exact bounded evidence projection reconciles T3 and T4 for LPCI1-Web?
2. Which runtime fields require validation before they may drive projection,
   routing, audit, or outward response?
3. What ordering preserves mixed direct plus escalate fail-close semantics?
4. What finite per-record, record-count, and aggregate serialized-evidence
   bounds prevent unbounded provider context?
5. What discriminated response variants prevent shape ambiguity?
6. Which canonical AuditReceipt fields and effective server filters remain?
7. What fixed client-safe provider-error message replaces raw provider errors?
8. Where do auth denial and invalid-body paths enter the audit boundary?

## Decision / Baseline / Proposed Tranche

Decision: dispatch one documentation-only no-commit SPEC worker. Baseline is the
accepted public-only D1 design plus current T2/T3/T4 and runtime facts. Proposed
tranche is `LPCI1-WEB-S1`, limited to the exact reference SPEC and worker return;
no implementation or later lifecycle phase is released.

## Required Specification Decisions

The worker must define normative, testable contracts for:

- runtime validation of every projection-driving field before eligibility;
- public-only sensitivity normalization and server-owned effective filters;
- mixed direct plus escalate fail-close before projection or provider dispatch;
- escaping or safe serialization of every projected path, date, status, answer
  class, and evidence-text field;
- justified finite record-count and aggregate serialized-evidence byte bounds,
  plus per-record evidence bounds, with fail-closed overflow;
- a discriminated route response union for validation denial, authorization
  denial, grounding unavailable, no provider, provider error, abstention, and
  answer success;
- retention of canonical `AuditReceipt`, effective server filters, and
  `model_response_hash` without exposing the full receipt to provider/client;
- fixed safe client provider-error text and secret-safe internal diagnostics;
- explicit auth-denial and invalid-body audit boundaries;
- zero provider calls for every ineligible, malformed, mixed-escalate, or
  over-bound case.

## T3/T4 Reconciliation Matrix

The specification must state its narrow precedence scope. It may ratify a
validated, escaped, public-only bounded `contentSnippet` as LPCI1-Web model
evidence and replace T4 full-receipt provider context for this route with a
derived allowlisted projection. It must not supersede T2/T3/T4 wholesale or
claim runtime implementation.

## Required Specification Schema

At minimum, the reference output must contain normative sections for authority
and precedence, source mapping, existing versus doc-only vocabulary, field
validation, sensitivity admission, evidence eligibility, projection fields,
escaping, bounds, fail-close ordering, response union, no-provider and provider
error projections, audit correlation, client-clearance disposition, synthetic
acceptance cases, later-build candidate manifest, rejection criteria, and claim
boundary.

## Threat And Proof Minimum

Cover forged client clearance, missing/unknown/non-public sensitivity,
malformed projection fields, blank/oversize evidence, delimiter/control
characters, aggregate overflow, mixed direct and escalate results, cross-corpus
grant inference, service-token possession without grant, impersonation,
no-provider response, provider failure, auth denial, and invalid JSON.

## Acceptance Criteria

- exactly one reference SPEC and one worker return are created;
- T3/T4 conflict is reconciled with narrow precedence;
- public-only and zero-evidence fail-close rules are normative;
- finite count and serialized-byte bounds are selected and justified;
- every projected field is validated and escaped;
- mixed direct plus escalate behavior remains fail-closed;
- route response variants are discriminated and exhaustively bounded;
- canonical audit/effective-filter/hash obligations are retained;
- no BUILD or external-effect claim appears;
- worker returns no commit for independent review.

## Evidence / Verification

Verification is source/documentation only: current source reads, exact searches,
worker-return fast gate, documentation governance gates, Git status/diff, and
independent reviewer inspection. Runtime and test execution are forbidden.

## Reviewer Independence

The dispatcher does not accept its own packet output. A delegated worker authors
the two outputs without commit; the primary reviewer independently validates,
repairs if bounded, converts closure, and owns any material commit.

## Dual Agent Surface Matrix

| Surface | Role | Interface | Authority/risk boundary | Evidence | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | dispatcher/reviewer/closer | governed local repository | packet, review, repair, commit ownership | Git and gate evidence | ACTIVE |
| INTERNAL_AGENT | no-commit specification worker | exact two-output manifest | documentation only | worker return | ACTIVE |
| EXTERNAL_AGENT_CLI_MCP | none | none | provider/CLI/MCP invocation forbidden | N/A with reason: no delegated CLI surface | PARKED |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_tables.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | dispatch status; dependency evidence; Source Verification columns and claim types; New Doc-Only separation; exact ADIF query; no-commit route; trace labels; public disposition; ASCII encoding; stop tokens |
| gateRunPurpose | confirm complete source-backed authoring after checker-source discovery; gates are not first discovery |
| claimBoundary | LPCI1-WEB-S1 private documentation-only dispatch baseline |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: one narrow companion specification can reconcile
the accepted T3/T4 conflict while preserving a public-only fail-closed boundary.

Evidence Comparison: current source, canonical T2/T3/T4 contracts, and accepted
D1 design must be compared at the worker execution base. Prior conclusions are
leads, not substitutes for current verification.

Contradiction Or Gap Disposition: unresolved bounds, response variants,
escaping, mixed-escalate behavior, audit obligations, or authorization ownership
must stop the worker rather than become inferred runtime authority.

Claim Update: return one bounded normative SPEC or `BLOCKED_WITH_REASON`.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer |
| Provider or surface | local private provenance repository |
| Session or invocation | LPCI1-WEB-S1 baseline authoring, 2026-08-08 |
| Working directory | repository root |
| Command or tool surface | startup reads, source reads, exact searches, scaffold stdout, ADIF resolver, apply_patch, pre-dispatch gates |
| Target paths | paired LPCI1-WEB-S1 baseline and work order |
| Allowed scope source | operator authority `AUTHORIZE_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_DOCUMENTATION_ONLY` |
| Before status evidence | HEAD `d68653ed9`; clean worktree |
| After status evidence | exact two-path dispatch packet pending primary review and commit |
| Diff evidence | exact two-path `git status --short` and `git diff --name-status` |
| Approval boundary | documentation-only SPEC dispatch |
| Claim boundary | no BUILD, runtime/test/provider/live/persistence/vector-RAG/corpus/public/deployment action |
| Agent type | dispatcher/reviewer |
| Invocation ID | `lpci1-web-s1-baseline-authoring-2026-08-08` |
| Expected manifest | paired baseline and work order only |
| Actual changed set | paired baseline and work order only |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private security/conformance specification dispatch with no public-sync
authority or public-safe projection.

## Claim Boundary

This baseline authorizes one private documentation-only SPEC worker and exact
two-output return. It does not implement or prove runtime behavior, authorize
non-public retrieval, create an authorization or persistence owner, run tests or
providers, or authorize BUILD, public-sync, deployment, or readiness claims.
