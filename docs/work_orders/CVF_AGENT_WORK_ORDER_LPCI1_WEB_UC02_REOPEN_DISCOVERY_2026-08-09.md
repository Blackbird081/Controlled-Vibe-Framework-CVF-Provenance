# CVF Agent Work Order - LPCI1 Web UC-02 Reopen Discovery

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED_DISCOVERY_NOT_MET

Batch ID: LPCI1-WEB-UC02-REOPEN-DISCOVERY

dispatchBaseHead: `24a0d6dbd`

executionBaseHead: `da0d139cb`

closureBaseHead: `da0d139cb`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: primary reviewer/dispatcher

workerReturnPath: `docs/reviews/CVF_LPCI1_WEB_UC02_REOPEN_DISCOVERY_WORKER_RETURN_2026-08-09.md`

## Dispatch Prompt Envelope

Role: delegated UC-02 source-discovery worker. The primary agent is independent reviewer/closer.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_UC02_REOPEN_DISCOVERY_2026-08-09.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture the clean committed HEAD immediately before worker actions.

Current-time notes: exact operator authority permits only one documentation-only
audit of the three UC-02 reopen conditions using current governed source.

Do-not-misread notes: the audit may conclude that evidence is missing. It may
not create a consumer, corpus/index, binding, design, implementation, or live
proof to make the conditions pass.

Required first actions: read startup/session surfaces, guard orientation,
literal gotchas, `DESIGN.md`, paired baseline and this packet; capture clean
HEAD/status; query ADIF and run pre-implementation before writing outputs.

Return contract: create exactly the audit and worker return, select one
canonical disposition, run required gates, leave staging empty and HEAD
unchanged, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Independently determine whether current source already satisfies all three
UC-02 reopen facts: a named source-verified non-test consumer, a public
route-compatible `<corpusId>-index.json`, and verified consumer selection/
binding to `/api/lpci/query`.

rawMemoryReleased=false.

## Authority Chain

1. Exact operator token `AUTHORIZE_LPCI1_WEB_UC02_REOPEN_DISCOVERY_ONLY`.
2. Accepted UC-01 bounded closure at material commit `b3f405b91`.
3. UC-02 reopen conditions in the current LPCI use-case roadmap.
4. Paired GC-018 baseline and this work order.

## Agent Roles

| Role | Responsibility |
|---|---|
| operator | authorizes discovery-only scope and owns any later checkpoint |
| dispatcher | source-verifies and commits the packet |
| worker | creates exactly two uncommitted discovery outputs |
| reviewer/closer | independently validates evidence, accepts or returns, and owns commits |
| session-sync steward | updates protected continuity only after reviewer acceptance |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V56_2026-08-09.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `DESIGN.md`
- paired GC-018 baseline and this work order
- every source path in Source Verification Block
- applicable output checker sources named below

## Mission

Create exactly:

1. `docs/reviews/CVF_LPCI1_WEB_UC02_REOPEN_DISCOVERY_AUDIT_2026-08-09.md`
2. `docs/reviews/CVF_LPCI1_WEB_UC02_REOPEN_DISCOVERY_WORKER_RETURN_2026-08-09.md`

The audit must select exactly one:

- `UC02_REOPEN_CONDITION_SATISFIED`
- `UC02_REOPEN_CONDITION_NOT_MET`
- `UC02_DISCOVERY_BLOCKED_CONTRADICTORY_SOURCE`

`UC02_REOPEN_CONDITION_SATISFIED` is permitted only if all three facts are
directly source-verified at execution base. Partial evidence is not satisfied.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id LPCI1-WEB-UC02-REOPEN-DISCOVERY --title "LPCI1 Web UC-02 Reopen Discovery" --date 2026-08-09 --base 24a0d6dbd --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit docs-only discovery profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact authority, three-condition decision contract, current source verification, dual-agent boundary, two-output manifest, verification commands, and reviewer conversion |
| checkerReadAheadConfirmation | applicable dispatch, AHB, ADIF, prompt-envelope, Delta boundary, public export, markdown, corpus, rescan, and worker-return checker sources read |
| docOnlyNewFields | `uc02ReopenDisposition`; `consumerEvidenceStatus`; `routeCompatibleIndexStatus`; `consumerRouteBindingStatus` |
| claimBoundary | scaffold provenance is dispatch evidence only; no discovery result or runtime claim |

## Worker Autonomy / No-Question Rule

Repair allowed-scope documentation or checker-shape defects directly and
rerun the failing gate. Return only for contradictory source, forbidden-scope
need, missing authority, or a mandatory gate blocker that cannot be repaired
inside the two worker-owned paths. Do not ask the operator incremental choices.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py` |
| literalTokensReviewed | `DISPATCHED`; `WORKER_MUST_NOT_COMMIT`; `NONE_RETURNED`; `COMPLETE_PENDING_REVIEW`; `BLOCKED_WITH_REASON`; exact AHB/AOT/Delta fields; corpus reconciliation; public disposition |
| gateRunPurpose | confirm packet and required output shape before worker dispatch |
| claimBoundary | read-ahead is not execution, UC-02 reopen, or implementation evidence |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`LPCI web UC-02 reopen discovery`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "LPCI web UC-02 reopen discovery" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | worker must perform fresh source verification and return exact no-commit evidence |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| three simultaneous UC-02 reopen facts | VALUE_SET | `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md` | Reopen Conditions | `UC-02` | LPCI use-case roadmap | ACCEPT |
| current non-test query consumer | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx` | `handleQuery` | `fetch('/api/lpci/query'` | LPCI dashboard page | ACCEPT |
| current consumer selects synthetic pilot | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx` | module constant | `PILOT_CORPUS_ID` | LPCI dashboard page | ACCEPT |
| route index path convention | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | `loadCorpusIndexText` | `${corpusId}-index.json` | LPCI query route | ACCEPT |
| current matching index | EXISTS | `docs/corpus-intelligence/GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json` | full file | `GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json` | synthetic LPCI index | ACCEPT |
| PolicyLocal registry owner | EXISTS | `docs/corpus-intelligence/registry/entries/policylocal-production-corpus-dropzone.json` | root object | `policylocal-production-corpus-dropzone` | GC-051 registry entry | ACCEPT |
| PolicyLocal ownership marker | VALUE_SET | `docs/corpus-intelligence/registry/entries/policylocal-production-corpus-dropzone.json` | `scanWave` | `LPCI2-T9` | PolicyLocal registry entry | ACCEPT |
| prior full-route closure stops continuation | VALUE_SET | `docs/reviews/CVF_LPCI1_WEB_UC01_FULL_ROUTE_LIVE_PROOF_COMPLETION_2026-08-09.md` | Next Allowed Move | `LPCI1_WEB_UC01_FULL_ROUTE_LIVE_PROOF_PASS` | reviewer completion | ACCEPT |

## New Doc-Only Fields

| Field | Owner artifact | Meaning |
|---|---|---|
| `uc02ReopenDisposition` | discovery audit | one canonical discovery result |
| `consumerEvidenceStatus` | discovery audit | direct evidence status for condition A |
| `routeCompatibleIndexStatus` | discovery audit | direct evidence status for condition B |
| `consumerRouteBindingStatus` | discovery audit | direct evidence status for condition C |

These fields do not exist in runtime and must not be presented as source facts.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| artifact paths | baseline, work order, audit, and return did not exist before authoring | ACCEPT_NO_COLLISION |
| non-test caller roots | refreshed under cvf-web source excluding test/spec files; only dashboard caller | REFRESHED_PASS |
| index enumeration | filesystem refresh found exactly the synthetic pilot index | REFRESHED_PASS |
| registry/corpus distinction | registry and literal index existence refreshed independently | REFRESHED_PASS |
| collision decision | no artifact collision; worker must refresh source facts at execution base | ACCEPT |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| Intake source | exact operator UC-02 discovery-only token |
| scope classification | documentation-only current-source reopen discovery |
| risk sensitivity | R1; read-only source inspection and two documentation outputs |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| selected role route | worker source-discovery return to independent reviewer/closer conversion |
| Worker role | create exactly two no-commit outputs |
| Reviewer role | independent primary reviewer/closer |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Checkpoint disposition | discovery released; DESIGN, BUILD, live, deploy, and public remain parked |
| escalation condition | contradictory source, forbidden path/action need, provider/live, secret/private data, public sync, destructive action, or claim-boundary expansion |
| Claim boundary | repository source audit only |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order handling | Result |
|---|---|---|
| named non-test consumer | direct source search and evidence row | REQUIRED |
| public route-compatible index | filesystem enumeration plus row-level public check if candidate exists | REQUIRED |
| verified consumer-to-route selection/binding | direct caller/config/source evidence | REQUIRED |
| all three simultaneous | satisfied token forbidden unless all three pass | PRESERVED |
| PolicyLocal counterexample-only | registry membership cannot substitute for matching index/binding | PRESERVED |
| no automatic continuation | worker returns evidence; reviewer owns any later decision | PRESERVED |

## Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| Scope boundary | UC-02 row and Reopen Conditions | audit current facts only | PASS |
| Non-goals | Explicit Parked Lanes | no DESIGN/BUILD/corpus/runtime work | PASS |
| Lane split | UC-02 versus UC-03/04/05/06 | inspect UC-02 only | PASS |
| Dependency/source plan | three simultaneous facts | direct source verification | PASS |
| Claim boundary | current continuation and parked lanes | no authority inheritance | PASS |
| Acceptance criteria | three-condition decision | observable matrix | PASS |
| Verification/evidence | current-source negative searches | command-backed | PASS |
| Dispatch-readiness decision | exact operator token | docs-only discovery released | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | delegated repository discovery worker | read current governed source and write exact two-path manifest | this packet | internal no-commit handoff | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no source-verified external UC-02 caller | no ingress/auth/mutation/runtime/public support | bounded negative search required | any CLI/MCP adapter needs fresh authority | DEFERRED_WITH_REASON |

## Agent Handoff Contract Control Block

Contract source: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | primary dispatcher/reviewer/closer delegates one no-commit discovery worker; primary closer converts accepted return |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=24a0d6dbd; executionBaseHead=da0d139cb; closureBaseHead=da0d139cb |
| changedSetScope(phase) | worker owns only audit and return; reviewer owns closure/status/roadmap; session steward owns protected continuity |
| traceScope(phase, actor) | each actor records phase-local AOT evidence and exact manifest |
| commitOwner(phase) | worker commit forbidden; primary reviewer/closer owns material commit; session steward owns separate sync |
| crossBatchIsolation | clean worktree at dispatchBaseHead `24a0d6dbd`; unexpected changes block execution |
| nextMoveSurfaces | worker must not edit them; reviewer updates only upon accepted disposition |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_LPCI1_WEB_UC02_REOPEN_DISCOVERY_COMPLETION_2026-08-10.md` |
| reviewerOwnedClosurePaths | completion review; paired baseline/work order status; LPCI use-case roadmap if disposition changes; protected continuity in a separate commit |
| closureOwner | primary reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before drafting, read every checker applicable to `docs/reviews/` audit and
worker-return artifacts. The real artifacts must include target/source,
scope/methodology, findings/position, risk/corrective action, decision/
disposition, source inventory, epistemic, external routing, rescan, corpus
integrity, finding-to-learning, AOT, Delta boundary, public disposition,
machine closure, command evidence, and claim-boundary sections. Use explicit
N/A-with-reason where conditional content is not applicable.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reviews/CVF_LPCI1_WEB_UC02_REOPEN_DISCOVERY_AUDIT_2026-08-09.md` | create source-backed three-condition matrix and select exactly one canonical discovery disposition |
| `docs/reviews/CVF_LPCI1_WEB_UC02_REOPEN_DISCOVERY_WORKER_RETURN_2026-08-09.md` | create full-gate no-commit return with exact commands, manifest, and unchanged HEAD evidence |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_LPCI1_WEB_UC02_REOPEN_DISCOVERY_WORKER_RETURN_2026-08-09.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Discovery Method

1. Refresh roadmap, current dashboard, route loader, registry sources, and all
   matching `*-index.json` paths at execution base.
2. Search current source for non-test callers or consumers of the route.
3. Enumerate route-compatible index files using the filesystem, not registry
   inference; inspect sensitivity only for a real candidate.
4. Verify whether a named consumer selects/binds a candidate corpus to the
   route. A generic caller plus unrelated registry entry is not a binding.
5. Select one disposition and record missing facts precisely.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES; bounded current-source caller/index/binding claims only |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | worker and reviewer direct source reads, targeted non-test caller search, filesystem index enumeration, and exact path check |
| verifiedBase | `da0d139cb` |
| staleEvidenceRule | dispatch source rows cannot substitute for execution-base refresh and independent closure review |

## Pre-Flight Checks

Before writing worker outputs: confirm execution HEAD and clean status, verify
the two output paths do not exist, run the worker ADIF query, refresh all
decision-driving sources, and pass pre-implementation 77/77. Any failure before
material edits blocks execution unless repair is inside the two owned outputs.

## Write Ownership

Worker owns only the audit and worker-return paths in the fulfillment manifest.
Reviewer owns completion/status/roadmap conversion. Session-sync steward owns
protected continuity. No actor may mix these ownership classes in one commit.

## Execution Plan

| Step | Input | Output | Validation or stop condition |
|---|---|---|---|
| 1 | required first reads and clean execution base | refreshed source inventory | stop on drift, collision, or contradictory authority |
| 2 | current caller/index/registry/route sources | three-condition evidence matrix | stop if a condition cannot be classified truthfully |
| 3 | evidence matrix | one canonical discovery disposition | satisfied requires all three direct facts |
| 4 | audit and worker return | final command evidence | rerun gates after last edit |
| 5 | exact pending manifest | no-commit handoff | staging empty and HEAD unchanged |

## Allowed Scope

Read current repository source/governed artifacts; run bounded local searches;
create exactly the two fulfillment-manifest files; repair only those two files;
run non-mutating governance gates. WORKER_MUST_NOT_COMMIT.

## Forbidden Scope

Any other durable path; source/test/config/package/UI edit; corpus/index/
registry creation or mutation; roadmap/session/handoff change; DESIGN, SPEC,
BUILD; browser/server/runtime; credential/env inspection; provider/network/
live call; non-public data read; persistence/vector/RAG; external repo; CLI/MCP
implementation; public sync; deploy; stage; commit; push.

## Verification Commands

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/run_adif_defect_resolver.py --task-class "LPCI web UC-02 reopen discovery" --role worker --lifecycle-phase pre-implementation --json
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/generate_corpus_scan_registry.py --check
git diff --check
git status --short --untracked-files=all
git diff --cached --name-only
git rev-parse --short HEAD
```

No browser, server, provider, release-bundle, or live command is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | primary dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | `lpci1-web-uc02-reopen-discovery-dispatch-2026-08-09` |
| Working directory | repository root |
| Command or tool surface | startup/source reads, targeted `rg`, filesystem enumeration, ADIF, scaffold stdout, apply_patch, dispatch gates, Git |
| Target paths | paired GC-018 baseline and this work order |
| Allowed scope source | exact operator discovery-only token |
| Before status evidence | clean worktree at HEAD `24a0d6dbd`; empty `git status --short` |
| After status evidence | exactly two dispatch artifacts pending commit |
| Diff evidence | `git diff --name-status` and exact staged manifest before dispatch commit |
| Approval boundary | packet authoring and dispatch only; no worker result or implementation authority |
| Claim boundary | repo-local trace only; no OS/user, runtime, provider, or public claim |
| Agent type | dispatcher |
| Invocation ID | `lpci1-web-uc02-reopen-discovery-dispatch-2026-08-09` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | docs-only UC-02 reopen-condition source discovery |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, or direct-interception behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime or provider receipt is authorized |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source audit artifacts and governance command evidence only |
| invocationBoundary | local file reads/searches and two governed documentation outputs |
| interceptionBoundary | no wrapper/proxy, IDE, shell, filesystem, provider, or agent-coding interception claim |
| claimLanguage | discovery establishes current evidence state only |
| forbiddenExpansion | no DESIGN, BUILD, corpus mutation, runtime, provider/live, CLI/MCP, public, deploy, production, or release claim |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | no external intake route selected |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired packet and worker outputs |
| Disposition | NOT_APPLICABLE_WITH_REASON: only CVF-governed repository sources are in scope |
| Claim boundary | external evidence need blocks and returns; it is not absorbed here |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: current source probably does not satisfy all
three UC-02 conditions because the page selects the synthetic pilot and only
one route-compatible index was found at dispatch.

Evidence Comparison Requirement: worker must independently refresh and compare
each condition against current source rather than confirming the prediction by
default.

Contradiction Handling Requirement: contrary evidence must cite direct paths/
symbols and select satisfied only if all three facts hold simultaneously.

Claim Update Requirement: record confirmed, revised, narrowed, or invalidated
prediction and preserve the no-implementation boundary.

## Evidence Requirements

| Evidence | Required form |
|---|---|
| condition A | named consumer, source path/symbol, non-test status, intended UC-02 use |
| condition B | exact matching index path, registry identity, row sensitivity/public eligibility |
| condition C | direct source proving consumer selects candidate corpus and calls route |
| negative result | exact roots/commands and concrete missing fact; no exhaustive-repo overclaim |
| PolicyLocal | counterexample-only unless direct matching index and binding both exist |
| hygiene | exact two-path manifest, empty staging, unchanged HEAD, no stray file |

## Acceptance Criteria

- Exactly two worker-owned artifacts exist.
- Exactly one canonical discovery disposition is selected.
- All three conditions have direct evidence or bounded missing evidence.
- Satisfied is selected only when all three pass simultaneously.
- Audit distinguishes consumer existence, index existence, and binding.
- PolicyLocal registry membership is not promoted into LPCI1 compatibility.
- Final commands run after last edit and staging remains empty.

## Fail Conditions

- Missing/multiple disposition tokens or partial evidence labeled satisfied.
- Registry membership treated as route-compatible index proof.
- Synthetic dashboard consumer treated as a real UC-02 consumer without direct source evidence.
- Any forbidden file/action, raw secret/private data read, provider/live call, stage, or commit.
- Provider-local memory or chat history used as source authority.
- Required final gates omitted or stale.

## Review Gate

Worker handoff is not closure. The primary reviewer must inspect source and
negative-search evidence, run reviewer-fast and commit steward, accept or
return the bounded disposition, then own status/roadmap/continuity changes.

## Closure Checklist

- [x] Worker outputs reviewed against current source.
- [x] Exactly one disposition and three condition rows verified.
- [x] PolicyLocal counterexample boundary preserved.
- [x] Exact two-path worker manifest and empty staging verified.
- [x] Reviewer-return steward is required before material commit.
- [x] Material committed-range pre-closure is required and reviewer-owned.
- [x] Session continuity will be synchronized separately after material acceptance.
- [x] Public export remains deferred private-only.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for source contradiction, missing required source,
unexpected worktree change, mandatory gate failure outside worker scope,
forbidden-path need, private/secret access need, provider/live action, public
sync, or any request to implement a missing reopen condition.

## Operator Checkpoint

No incremental operator choice is needed for the discovery audit. Any DESIGN,
BUILD, consumer/corpus/index creation, registry mutation, provider/live call,
hosted/release proof, deployment, production, public sync, or claim-boundary
expansion requires another fresh explicit operator authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `CLOSED_PASS_BOUNDED_DISCOVERY_NOT_MET` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI1_WEB_UC02_REOPEN_DISCOVERY_COMPLETION_2026-08-10.md` | independent bounded acceptance | PASS |
| Worker return | named return | `COMPLETE_PENDING_REVIEW`; accepted by completion | PASS |
| Discovery audit | named audit | `UC02_REOPEN_CONDITION_NOT_MET`; A/B/C NOT_MET | PASS |
| Roadmap state | LPCI use-case roadmap | `LPCI1_WEB_UC02_REOPEN_DISCOVERY_NOT_MET_PARKED_NO_CONTINUATION` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated aggregate drift PASS | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no registry mutation | PASS |
| External evidence digest | N/A | N/A with reason: no external evidence artifact was used | N/A with reason |
| System loop interlock | UC-02 discovery -> not met -> park | no implementation release | PASS |
| Session continuity | active V57 and generated state | separate sync after material commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| one canonical discovery disposition | `UC02_REOPEN_CONDITION_NOT_MET` | PASS |
| condition A | no named real UC-02 consumer | NOT_MET |
| condition B | no real UC-02 route-compatible public index | NOT_MET |
| condition C | no real UC-02 consumer-to-corpus-to-route binding | NOT_MET |
| exact worker manifest | audit and worker return only | PASS |
| worker commit | forbidden; HEAD unchanged and staging empty | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance discovery only; no public-safe projection is authorized.

## Claim Boundary

This work order authorizes exactly one current-source UC-02 reopen-condition
audit and no-commit return. It does not authorize DESIGN, SPEC, BUILD, consumer
or corpus creation, registry/index mutation, UI/runtime work, credential or
private-data access, provider/live proof, persistence/vector/RAG, CLI/MCP,
release, deployment, production readiness, public sync, commit, or push.
