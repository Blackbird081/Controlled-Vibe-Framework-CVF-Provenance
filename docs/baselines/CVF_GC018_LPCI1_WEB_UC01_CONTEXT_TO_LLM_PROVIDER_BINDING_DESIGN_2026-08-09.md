# CVF GC-018 Baseline - LPCI1 Web UC-01 Context-To-LLM Provider Binding Design

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-09

Batch ID: LPCI1-WEB-UC01-D1

Dispatch base head: `db24c5266`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: primary reviewer/closer

Worker target: delegated documentation-design worker

## Purpose

Authorize one documentation-only DESIGN tranche for roadmap candidate UC-01.
The DESIGN must choose a source-backed reuse-or-composition boundary with the
existing Model Gateway owner and define the paired LPCI configuration contract.

## Authorization / Decision

Operator authority: `AUTHORIZE_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_ONLY`.

Authority evidence: after the reviewer reported that the next checkpoint was a
fresh DESIGN-only authority for UC-01 including UC-04, the operator replied
the continuation response. This baseline records it as authority for exactly
this DESIGN tranche. It grants no SPEC, BUILD, runtime mutation, test execution,
provider/API-key/network/live action, persistence, vector/RAG, non-public grant,
public-sync, deployment, or readiness authority.

Decision: dispatch one no-commit worker to create exactly a DESIGN audit and a
worker return. Independent reviewer acceptance is mandatory before any later
authority can be considered.

## Proposed Tranche / Baseline Decision

`LPCI1-WEB-UC01-D1` is the single proposed DESIGN-only tranche. Baseline
decision: `DISPATCH_READY` for the exact two-output no-commit manifest.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id LPCI1-WEB-UC01-D1 --title "LPCI1 Web UC-01 Context-To-LLM Provider Binding Design" --date 2026-08-09 --base db24c5266 --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | web-ui-dashboard plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced all placeholders with source-verified UC-01/UC-04 authority, scope, manifest, evidence, and lifecycle controls |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py` |
| docOnlyNewFields | DESIGN-only decision vocabulary defined inside the worker output, not asserted as current runtime fields |
| claimBoundary | dispatch-authoring provenance only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `DISPATCH_READY`; Source Verification Block; ADIF Defect Registry Disclosure; Agent Operation Trace Block; Public Export Disposition |
| gateRunPurpose | confirmation evidence after checker-source and scaffold read-ahead; not first discovery |
| claimBoundary | packet structure only; no DESIGN acceptance or runtime proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`documentation-design`, role=`worker`, lifecyclePhase=`pre-implementation`

Resolver query executed: `python governance/compat/run_adif_defect_resolver.py --task-class documentation-design --role worker --lifecycle-phase pre-implementation --surface-selector LPCI --max-results 50 --json`

Returned defect count: 0. Disclosed defectIds: none.

Returned defects: NONE_RETURNED

The empty resolver result is recorded only as dispatch evidence; it does not
prove that the worker read or understood the registry.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| UC-01 DESIGN-only eligibility | LITERAL_INVARIANT | `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md` | Recommended Next Tranche | `UC-01` | roadmap lifecycle chain | ACCEPT |
| UC-04 AND requirement | LITERAL_INVARIANT | `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md` | Reopen Conditions | `UC-04` | roadmap dependency contract | ACCEPT |
| current LPCI credential input | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | line 263 | `LPCI_LLM_API_KEY` | `POST` | ACCEPT |
| current LPCI endpoint input | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | line 286 | `LPCI_LLM_ENDPOINT` | `POST` | ACCEPT |
| current LPCI model input | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | line 287 | `LPCI_LLM_MODEL` | `POST` | ACCEPT |
| current direct provider call | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 291-306 | `fetch` | `POST` | ACCEPT |
| existing provider capability owner | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | lines 49-123 | `PROVIDER_CAPABILITY_REGISTRY` | provider capability registry | ACCEPT |
| existing provider execution owner | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | lines 27-78 | `ProviderExecutionBridge` | provider execution bridge | ACCEPT |
| existing credential owner | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | lines 3-33 | `CredentialBoundary` | credential boundary | ACCEPT |
| current cvf-web Model Gateway package binding | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependencies; corrected fact: no dependency exists | `cvf-model-gateway` | package dependency graph | REJECT |
| current LPCI config documentation | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.example` | entire file; corrected fact: all three LPCI variables are absent | `LPCI_LLM_API_KEY` | cvf-web environment contract | REJECT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| packet path existence before authoring | both exact baseline/work-order paths returned `False` | PASS |
| batch/token collision | `rg -n 'LPCI1-WEB-UC01-D1\|AUTHORIZE_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_ONLY' docs CVF_SESSION` returned no match before authoring | PASS |
| Model Gateway dependency collision | no `cvf-model-gateway` dependency found in current cvf-web package or TypeScript config | SOURCE_GAP_FOR_DESIGN |
| LPCI config-doc collision | no LPCI provider variables found in current `.env.example`; source occurrences are limited to route/test code | SOURCE_GAP_FOR_DESIGN |

## Scope / Target / Owner Boundary

Target: the documentation-only architecture decision connecting the existing
LPCI1-T5 UC-01 call site to the existing Model Gateway provider capability,
credential, routing/execution, and receipt owners.

The DESIGN must preserve LPCI's accepted public-only evidence projection and
response/audit contracts. It must not create a parallel generic provider owner.

## Allowed Manifest

1. `docs/audits/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_2026-08-09.md`
2. `docs/reviews/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_WORKER_RETURN_2026-08-09.md`

## Forbidden Scope

- all runtime, source, test, package, config, and generated-state mutations;
- provider/API-key/network/live execution or secret-content reads;
- SPEC, BUILD, deployment, public-sync, catalog, registry, or session changes;
- persistence, vector/RAG, non-public grants, or a parallel provider owner;
- staging or commit by the worker.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES_BOUNDED_CURRENT_SOURCE_FACTS_ONLY |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | direct source read at `db24c5266` |
| reason | DESIGN must describe current direct-fetch and missing composition/config facts accurately without changing them |
| requiredFutureAction | independent DESIGN acceptance, then a separately authorized later lifecycle packet |

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | PASS before packet authoring |
| UI claim boundary | DESIGN may specify dashboard response-state implications but cannot change UI or claim hosted/live readiness |

## Evidence / Verification

Required dispatch evidence is the exact two-path manifest, direct source reads,
zero-result bounded ADIF query, dispatch-quality gate, pre-dispatch autorun,
file-size enforcement, diff hygiene, and clean staged/unstaged boundaries before
commit. Worker evidence requirements are controlled by the paired work order.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | primary reviewer/dispatcher |
| Provider or surface | private provenance repository |
| Session or invocation | `lpci1-web-uc01-d1-dispatch-2026-08-09` |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, scaffold preview, ADIF resolver, apply-patch authoring, gates, Git commit |
| Target paths | this baseline and paired work order |
| Allowed scope source | operator continuation after the explicit UC-01 DESIGN-only checkpoint |
| Before status evidence | clean HEAD `db24c5266` synchronized with provenance origin |
| After status evidence | exact two-path dispatch packet pending governed commit |
| Diff evidence | `git diff --name-status`; `git status --short` |
| Approval boundary | UC-01/UC-04 documentation-only DESIGN dispatch |
| Claim boundary | no DESIGN acceptance, runtime mutation, provider/live action, or public action |
| Agent type | primary reviewer/dispatcher |
| Invocation ID | `lpci1-web-uc01-d1-dispatch-2026-08-09` |
| Expected manifest | this baseline; paired work order |
| Actual changed set | same two dispatch paths before commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source/architecture dispatch with internal paths; no public
artifact or public-sync authority is included.

## Claim Boundary

This baseline authorizes only two documentation outputs under a no-commit
worker. It does not accept the future DESIGN or release any later lifecycle.
