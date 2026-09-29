# CVF GC-018 Baseline - LPCI1 Web Grounding And Clearance Conformance Design

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-08

Batch ID: LPCI1-WEB-D1

dispatchBaseHead: `68317891b`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer/closer: primary reviewer

Worker target: documentation and source-verification design worker

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id LPCI1-WEB-D1 --title "LPCI1 Web Grounding And Clearance Conformance Design" --date 2026-08-08 --base 68317891b --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit and Web-boundary profiles |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with current LPCI source facts, canonical T2/T3/T4 requirements, exact design questions, two-output manifest, and lifecycle exclusions |
| checkerReadAheadConfirmation | dispatch-quality, structural, checker-read-ahead, ADIF, handoff, trace, worker-return, prompt-envelope, public-disposition, and file-size checkers |
| docOnlyNewFields | `modelEvidenceProjection`; `evidenceEligibilityRule`; `authorizationContext`; `authorizationDecision`; `grantEvidence`; `noProviderProjection`; `auditCorrelation`; `syntheticProofMatrix` |
| claimBoundary | dispatch baseline for documentation-only conformance design; no runtime, test, provider, persistence, vector/RAG, public, or deployment action |

## Purpose

Authorize one bounded, owner-local LPCI1-Web design analysis that selects or
rejects a safe model-bound evidence projection, server-derived sensitivity
authorization boundary, no-provider response projection, audit correlation,
and synthetic proof plan. The design must stop before implementation.

## Scope / Target / Owner Boundary

Target owner: the existing LPCI1-T5 cvf-web route/library/UI/test family.

Allowed design surface:

- `buildAnswerBoundaryPrompt()` and the current retrieval receipt boundary;
- route authentication identity and session/service-token context;
- T2/T3 sensitivity rules and T4 grounding/answer boundary;
- no-provider response minimization and audit evidence requirements;
- synthetic positive, deny, abstain, and disclosure-negative proof cases.

Owner boundary: no generic governed-retrieval, LPCI2 PolicyLocal, Control
Plane, Memory, provider, persistence, or vector/RAG owner is opened.

## Non-Goals

- no runtime, test, schema, route, UI, registry, corpus, or configuration edit;
- no choice or creation of a durable entitlement store;
- no provider/model selection, key use, network call, or live proof;
- no production, sensitive-release, exploit, legal-correctness, or readiness claim;
- no public-sync, push, deployment, or later-tranche dispatch.

## Authorization / Decision

Operator authority received on 2026-08-08:

`LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN`

This releases DESIGN documentation only. It does not release SPEC, BUILD,
runtime/test mutation or execution, provider/live action, persistence,
vector/RAG, public-sync, deployment, or readiness authority.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| current prompt builder narrows model context to metadata | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 40-72 | `buildAnswerBoundaryPrompt` | LPCI query route | ACCEPT |
| index rows may contain a display-hint snippet | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | line 49 | `contentSnippet` | `LpciIndexRecord` | ACCEPT |
| retrieval receipt retains complete matched index records | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/retrieval.ts` | lines 112-120 | `matched_records` | `runRetrievalPipeline` | ACCEPT |
| client request shape exposes boolean clearance | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | line 57 | `sensitivityClearance` | `FilterParams` | ACCEPT |
| filter uses client boolean and otherwise excludes only classified | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.ts` | lines 14-27 and 109-120 | `applySensitivityFilter` | `runFilterPipeline` | ACCEPT |
| route authorization exposes auth mode, actor ID, and optional session | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 64-85 | `RouteGovernanceAuthorization` | route governance proof contract | ACCEPT |
| session exposes role, org, team, and impersonation context | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | lines 19-30 | `SessionCookie` | middleware authentication | ACCEPT |
| T2 defines five sensitivity levels and restrictive unknown treatment | VALUE_SET | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | Sensitivity Level Assignment Rules | `sensitivityLevel` | LPCI1 T2 canonical contract | ACCEPT |
| T3 requires distinct classified, confidential, and restricted authorization | VALUE_SET | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | Stage 1 - Sensitivity Pre-Filter | `classification_access`; `confidential_access` | LPCI1 T3 canonical contract | ACCEPT |
| T3 classifies content snippet as a capped display hint | VALUE_SET | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | Searchable Fields | `contentSnippet` | LPCI1 T3 index contract | ACCEPT |
| T4 requires model context and answers grounded in retrieved text | VALUE_SET | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | RetrievalReceipt Schema; Answer Boundary Rules | `RetrievalReceipt` | LPCI1 T4 retrieval boundary | ACCEPT |
| no-provider response returns the full retrieval receipt | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 189-216 | `retrievalReceipt` | LPCI query no-provider branch | ACCEPT |
| current corpus is synthetic and all indexed rows are public | VALUE_SET | `docs/corpus-intelligence/GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json` | records array | `sensitivityLevel` | current LPCI pilot index | ACCEPT |

## Current Runtime Freshness Verification

At HEAD `68317891b`, the reviewer repeated exact source searches for
`buildAnswerBoundaryPrompt`, `contentSnippet`, `matched_records`,
`sensitivityClearance`, `routeAuth`, `actorId`, session scope fields,
`classification_access`, `confidential_access`, and the no-provider receipt.
The two intake conflicts remain present. No current LPCI owner for actor-to-
corpus grants or GC-051 retrieval authorization was found in the searched Web
source and corpus registry surfaces. Absence is a design constraint, not proof
that an entitlement system may be invented or implemented in this tranche.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| output paths | both proposed worker output paths returned `False` with `Test-Path` | safe to create after dispatch |
| authority token | `rg -n --fixed-strings "LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN" docs CVF_SESSION` returned only intake and session checkpoint surfaces before this packet | operator token accepted as phase authority, not runtime source |
| entitlement owner search | exact searches across current cvf-web source, corpus registry sources, and T2/T3/T4 docs returned canonical requirement text but no LPCI actor/corpus grant store or lookup symbol | design must mark proposed authorization fields `DOC_ONLY_NEW` or stop |
| term collisions | authorization terms occur in unrelated agent, package, route-auth, and governance owners | unrelated collisions do not establish LPCI entitlement ownership |

Search roots were current LPCI Web source/tests, canonical LPCI T2/T3/T4
references, corpus-intelligence source entries and aggregate, and session
authority surfaces. Generated dependencies and Git internals were excluded.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`design specification`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class "design specification" --role dispatcher --lifecycle-phase pre-dispatch --json`

## Design Questions

1. What is the smallest approved evidence projection that permits grounded
   answers without sending the full retrieval receipt or treating a display
   hint as authoritative by default?
2. Which evidence classes are eligible, minimized, ordered, truncated,
   sensitivity-checked, and traceable to a path?
3. How must positive-answer execution fail closed when no eligible evidence
   remains after authorization and minimization?
4. Which server-derived actor, corpus, auth-mode, impersonation, sensitivity,
   and grant facts are required for one authorization decision?
5. Can current source own those facts, or must the design stop with an explicit
   missing-owner decision before any later SPEC or BUILD?
6. What minimized no-provider projection preserves current UI needs without
   returning full matched records?
7. Which audit fields correlate actor, corpus, grant source, sensitivity
   decision, evidence paths, answer class, and response outcome without raw
   evidence release?
8. Which synthetic cases prove allow, deny, unknown/restricted fail-close,
   impersonation, service-token, cross-corpus, no-evidence, and response
   minimization behavior in a later authorized build?

## Required Design Decisions

| Decision | Allowed disposition |
|---|---|
| evidence projection | select one bounded projection or `STOP_NO_SAFE_EVIDENCE_PROJECTION` |
| authorization owner | select a source-backed owner or `STOP_AUTHORIZATION_OWNER_NOT_FOUND` |
| client clearance boolean | reject as authority; retain only as ignored/deprecated request input candidate or remove in later SPEC |
| no-provider response | select minimized projection or stop |
| audit correlation | define metadata-only evidence shape or stop |
| later implementation | bounded candidate manifest only; no implementation authorization |

## Decision / Proposed Tranche

Release `LPCI1-WEB-D1` documentation design evidence only. The worker creates
one design audit and one worker return and recommends exactly one bounded
design or an exact stop token. The reviewer owns the acceptance decision.

## Threat And Proof Minimum

The design must cover forged client clearance, ordinary session, privileged
session with and without corpus grant, impersonated session, valid service
token with and without a scoped grant, cross-corpus access, restricted and
unknown records, no eligible evidence, no-provider response, and prevention of
raw/full-record disclosure. All fixtures must be synthetic.

## Acceptance Criteria

| ID | Required result |
|---|---|
| AC1 | current grounding, clearance, no-provider, and owner facts are independently reverified |
| AC2 | evidence projection options receive one decision rubric and one selection or stop token |
| AC3 | full receipt and bare display-hint promotion are not silently accepted |
| AC4 | client clearance is rejected as entitlement evidence |
| AC5 | session, impersonation, service-token, corpus, and sensitivity semantics are explicit |
| AC6 | missing entitlement ownership stops rather than invents a runtime owner |
| AC7 | minimized no-provider and audit projections are specified without raw evidence |
| AC8 | synthetic positive and fail-closed proof matrix is deterministic and bounded |
| AC9 | exactly two documentation outputs change and worker makes no commit |

## Evidence / Verification

Evidence must include command/path/result source checks, option matrices with
supporting and contradicting evidence, exact existing-versus-doc-only fields,
threat and synthetic proof matrices, final Git status, and no-commit evidence.
No provider output, sensitive content, runtime result, or implementation claim
is admissible in this tranche.

## Reviewer Independence

The worker cannot approve its own design. The reviewer independently checks
source ownership, challenges disclosure minimization, verifies that every
runtime-shaped proposal is labeled doc-only when absent, and decides whether
the design is accepted, repaired once, or stopped.

## Dual Agent Surface Matrix

| Surface class | Interface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | local provenance reads and two documentation outputs | design evidence only; no source/test mutation | exact paths, source table, decision and threat matrices | local filesystem | ALLOWED |
| `EXTERNAL_AGENT_CLI_MCP` | role-neutral worker handoff | no CLI/MCP adapter or provider action is required | N/A with reason: local governed worker route only | no adapter | CONTRACT_ONLY |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch status; Source Verification columns and claim types; ADIF query; prompt-envelope fields; no-commit handoff route; trace fields; worker-return profile; public disposition; stop tokens |
| gateRunPurpose | confirm and record gate evidence after source-backed design requirements were written; gates are not first discovery |
| claimBoundary | LPCI1-WEB-D1 documentation-only design dispatch baseline |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: an owner-local design may safely separate
authorization, eligible evidence, model-bound projection, client response,
and audit metadata, but current source may lack the entitlement owner needed
to release a later implementation.

Evidence Comparison Requirement: compare at least two evidence-projection and
two authorization-owner options, retaining evidence against the recommendation.

Contradiction Or Gap Disposition: stop when safety depends on an owner, field,
grant source, or evidence class that current authority cannot establish.

Claim Update Requirement: select a bounded design or return an exact stop token.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer |
| Provider or surface | local private provenance repository |
| Session or invocation | LPCI1-WEB-D1 dispatch authoring, 2026-08-08 |
| Working directory | repository root |
| Command or tool surface | startup reads, source searches, scaffold stdout, ADIF resolver, apply_patch, governance gates |
| Target paths | paired LPCI1-WEB-D1 baseline and work order |
| Allowed scope source | operator token `LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN` |
| Before status evidence | HEAD `68317891b`; clean worktree |
| After status evidence | paired documentation-only design dispatch pending commit |
| Diff evidence | exact paired-path Git status and diff before commit |
| Approval boundary | DESIGN documentation and worker dispatch only |
| Claim boundary | no runtime/test/provider/live/persistence/vector-RAG/public/deployment action |
| Agent type | dispatcher/reviewer |
| Invocation ID | `lpci1-web-d1-dispatch-authoring-2026-08-08` |
| Expected manifest | paired LPCI1-WEB-D1 baseline and work order |
| Actual changed set | paired LPCI1-WEB-D1 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance source and security-boundary design. No public-sync
action or public claim is authorized.

## Claim Boundary

This baseline authorizes one local, no-commit documentation design worker. It
does not authorize implementation, runtime/test changes or execution,
provider/model/live action, persistence, vector/RAG, corpus mutation,
public-sync, push, deployment, production use, or readiness claims.
