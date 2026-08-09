# CVF GC-018 Baseline - LPCI1 Web UC-02 Reopen Discovery

Memory class: governed-dispatch-baseline

Status: DISPATCHED

Batch ID: LPCI1-WEB-UC02-REOPEN-DISCOVERY

Dispatch base head: `24a0d6dbd`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: primary reviewer/dispatcher

Worker target: delegated worker

## Authorization / Decision

The operator supplied the exact token
`AUTHORIZE_LPCI1_WEB_UC02_REOPEN_DISCOVERY_ONLY` on 2026-08-09. It authorizes
one source-verified, documentation-only audit of the three recorded UC-02
reopen conditions. It does not authorize satisfying those conditions through
new implementation.

## Purpose

Determine whether current governed source already contains all three facts
required to reopen UC-02: a named non-test consumer, a public route-compatible
index, and verified selection/binding of that consumer to `/api/lpci/query`.
The worker must return a source-backed satisfied, not-met, or contradiction
disposition without changing source, corpus, registry, roadmap, or runtime.

rawMemoryReleased=false.

## Baseline Decision

Proceed with one no-commit docs-only worker that may create exactly the audit
and worker return named by the paired work order. Discovery may inspect current
repository source and governed artifacts only. Missing evidence is a valid
bounded result and does not release DESIGN or BUILD.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| UC-01 bounded closure | material commit `b3f405b91`; full-route completion review | ACCEPT_BOUNDED |
| UC-02 parked condition | `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md`, Reopen Conditions | ACCEPT_FOR_DISCOVERY |
| operator checkpoint | exact token recorded above | ACCEPT_DISCOVERY_ONLY |
| clean dispatch base | HEAD `24a0d6dbd`; empty initial status | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id LPCI1-WEB-UC02-REOPEN-DISCOVERY --title "LPCI1 Web UC-02 Reopen Discovery" --date 2026-08-09 --base 24a0d6dbd --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit docs-only discovery profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact authority, three-condition decision contract, current source verification, dual-agent boundary, two-output manifest, and reviewer conversion |
| checkerReadAheadConfirmation | applicable dispatch, AHB, ADIF, prompt-envelope, Delta boundary, public export, and artifact-shape checker sources read before authoring |
| docOnlyNewFields | `uc02ReopenDisposition`; `consumerEvidenceStatus`; `routeCompatibleIndexStatus`; `consumerRouteBindingStatus` |
| claimBoundary | scaffold provenance is dispatch evidence only; no discovery result or runtime claim |

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | `DISPATCHED`; `WORKER_MUST_NOT_COMMIT`; `NONE_RETURNED`; `Source Verification Block`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirm packet shape after source verification and before dispatch |
| claimBoundary | read-ahead is not worker execution, UC-02 reopen, or implementation evidence |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`LPCI web UC-02 reopen discovery`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "LPCI web UC-02 reopen discovery" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | standard source-verification, no-commit, exact-manifest, and reviewer-isolation controls apply |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| UC-02 requires three simultaneous facts | VALUE_SET | `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md` | Reopen Conditions | `UC-02` | LPCI use-case roadmap | ACCEPT |
| current non-test route caller | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx` | `handleQuery` | `fetch('/api/lpci/query'` | LPCI dashboard page | ACCEPT |
| current page selects only pilot corpus by default | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx` | module constant and state initialization | `PILOT_CORPUS_ID` | LPCI dashboard page | ACCEPT |
| route-compatible index convention | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | `loadCorpusIndexText` | `${corpusId}-index.json` | LPCI query route | ACCEPT |
| only current matching index | EXISTS | `docs/corpus-intelligence/GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json` | full file | `GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json` | synthetic LPCI index | ACCEPT |
| PolicyLocal registry entry | EXISTS | `docs/corpus-intelligence/registry/entries/policylocal-production-corpus-dropzone.json` | root object | `policylocal-production-corpus-dropzone` | GC-051 registry entry | ACCEPT |
| PolicyLocal is LPCI2-owned and not an LPCI1 matching index | VALUE_SET | `docs/corpus-intelligence/registry/entries/policylocal-production-corpus-dropzone.json` | `scanWave` and `scopePaths` | `LPCI2-T9` | PolicyLocal registry entry | ACCEPT |
| accepted UC-01 full-route proof is bounded and stopped | VALUE_SET | `docs/reviews/CVF_LPCI1_WEB_UC01_FULL_ROUTE_LIVE_PROOF_COMPLETION_2026-08-09.md` | Next Allowed Move and Claim Boundary | `LPCI1_WEB_UC01_FULL_ROUTE_LIVE_PROOF_PASS` | reviewer completion | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| dispatch and output path collision | four planned paths returned `False` with `Test-Path` before authoring | ACCEPT_NO_COLLISION |
| non-test caller search | targeted `rg` under cvf-web source found the dashboard page plus route/registry owners; no second non-test consumer | ACCEPT_BOUNDED_NEGATIVE |
| route-compatible index enumeration | filesystem enumeration found only `GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json` | ACCEPT_BOUNDED_NEGATIVE |
| PolicyLocal matching-index search | registry entry exists; no `policylocal-production-corpus-dropzone-index.json` exists | ACCEPT_COUNTEREXAMPLE_ONLY |
| collision decision | artifact names are new and current facts support a discovery audit, not a reopen claim | ACCEPT |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | delegated repository discovery worker | read current governed source and write exactly two docs | paired packet and exact manifest | internal no-commit handoff only | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI/MCP consumer is selected | no ingress, auth, mutation, receipt, or public behavior is authorized | no source-verified external UC-02 caller found | any external adapter requires a separate packet | DEFERRED_WITH_REASON |

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | PASS; read because the discovery inspects the current dashboard consumer |
| UI claim boundary | read-only inspection only; no UI design, edit, hosted, production, or live-data claim |

## Allowed Scope

Worker may read current repository source and governed artifacts, run bounded
filesystem/token searches, and create exactly:

- `docs/reviews/CVF_LPCI1_WEB_UC02_REOPEN_DISCOVERY_AUDIT_2026-08-09.md`
- `docs/reviews/CVF_LPCI1_WEB_UC02_REOPEN_DISCOVERY_WORKER_RETURN_2026-08-09.md`

## Forbidden Scope

All source/test/config/package changes; corpus/index/registry creation or edit;
roadmap/session/handoff mutation; DESIGN, SPEC, BUILD; browser/server/runtime;
credential/environment inspection; provider/network/live calls; non-public
data reads; persistence/vector/RAG; CLI/MCP implementation; public sync;
deployment; stage; commit; push.

## Acceptance Criteria

- Exactly one canonical discovery disposition is selected.
- Each of the three reopen conditions has direct source evidence or a bounded
  missing-evidence result.
- PolicyLocal remains counterexample-only unless current source directly proves
  all three UC-02 conditions.
- No implementation or later-phase authority is inferred from discovery.
- Worker creates exactly two uncommitted outputs and leaves staging empty.

## Evidence / Verification

Dispatch evidence consists of the source-verification table, bounded negative
searches, exact two-path worker manifest, ADIF disclosure, pre-dispatch gate,
and later worker command evidence. No runtime or provider receipt is expected.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance discovery only; no public-safe projection is authorized.

## Claim Boundary

This baseline authorizes only a current-source UC-02 reopen-condition audit.
Even a satisfied discovery result would establish documentation eligibility
for reviewer disposition only; it would not authorize DESIGN, BUILD, corpus
creation, runtime behavior, provider/live proof, release, deployment, public
export, or production readiness.
