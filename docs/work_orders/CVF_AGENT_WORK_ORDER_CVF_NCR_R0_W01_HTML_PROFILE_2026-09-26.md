# CVF Agent Work Order - CVF-NCR-R0-W01 HTML Pilot Profile Evidence

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

providerExecutionAuthority: FORBIDDEN

Batch ID: CVF-NCR-R0-W01

Dispatch base head: `11ba9eb46`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: shared-workspace `INTERNAL_AGENT` source-mapping role

Reviewer/closer: Local orchestrator/reviewer, distinct from worker

Worker return path: `docs/reviews/CVF_CVF_NCR_R0_W01_HTML_PROFILE_WORKER_RETURN_2026-09-26.md`

## Dispatch Prompt Envelope

Role: internal worker for bounded NCR-R0/W01 HTML profile evidence.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R0_W01_HTML_PROFILE_2026-09-26.md`

Paired baseline: `docs/baselines/CVF_GC018_CVF_NCR_R0_W01_HTML_PROFILE_2026-09-26.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture committed HEAD with `git rev-parse --short HEAD` before edits.

Current-time notes: operator relays this packet to Claude; worker checks exact HEAD/clean lane and does not touch the separate 52-deferred lane.

Do-not-misread notes: this is read-only source/profile analysis and one pending worker return. HTML candidate is already selected; overall guide/video is a later documentation tranche. No implementation, dependency install, render, provider/live call, credentials, public action, cross-lane edit, stage or commit.

Required first actions: read startup front door and active handoff; guard orientation and literal gotchas; paired baseline and this packet; source and checker paths below; capture HEAD/status; run pre-implementation gate with this exact work-order binding.

Return contract: leave only the exact W01 worker-return path uncommitted; report `COMPLETE_PENDING_REVIEW` with evidence and actual `git status --short`, or `BLOCKED_WITH_REASON` with a named contradiction. Local reviewer owns acceptance and commit.

## Purpose

Return a secret-safe, source-backed profile boundary for the operator-selected HTML review-packet pilot. Resolve what can be determined from current source and non-secret profile metadata about `NEXTAUTH_URL`, receipt payload/destination, retention, latency/cost, P06/P08 validation depth and an eventual UI walkthrough. Leave actual effects and unknown configuration for Local/operator disposition.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-R0-W01 --title "NCR R0 W01 HTML Pilot Profile Evidence" --date 2026-09-26 --base 11ba9eb46 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit internal worker profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | replaced generated skeleton with W01 authority, path manifest, profile axes and return contract |
| checkerReadAheadConfirmation | read dispatch quality, envelope, closeability, ADIF and governed read-ahead checker sources before authoring |
| docOnlyNewFields | actual-profile classification, receipt-egress boundary and UI walkthrough admission |
| claimBoundary | authoring provenance and static packet shape only; no implementation proof |

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-NCR-R0-W01","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"DOC_CHANGE","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/baselines/","docs/work_orders/","docs/reviews/","AGENT_HANDOFF_V63_2026-09-18.md","CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json","CVF_SESSION/ACTIVE_SESSION_STATE.json","CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json","CVF_SESSION/state/entries/nextAllowedMove.json","CVF_SESSION_MEMORY.md"],"claims":["bounded HTML profile assessment"],"requiredProof":["source/profile boundary matrix","P06/P08 evidence gap","receipt endpoint and payload boundary","UI walkthrough admission plan","exact changed set","worker-return full gate"],"operatorCheckpoints":["pilot effect/data/expense choice","provider/live/public/deployment action"],"forbiddenEffects":["worker commit","UI/route invocation","source-code change","dependency installation","provider/live invocation","public write","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":false,"corpusReceiptRef":"docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md","completenessClaimChanged":false}}
```

## Authority Chain

- Operator instruction: selected HTML review packet as first internal pilot candidate; later overall CVF user guide/video; requested Local to continue as orchestrator/reviewer and relay worker work to Claude.
- Active front door: `CVF_SESSION_MEMORY.md`; handoff: `AGENT_HANDOFF_V63_2026-09-18.md`.
- Selected roadmap: `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`, R0/R1, D009/D010, Q001.
- Accepted source packet: `docs/reviews/CVF_CVF_NCR_R0_W00_PILOT_SELECTION_WORKER_RETURN_2026-09-26.md`, Local Reviewer Disposition.
- Paired GC-018: `docs/baselines/CVF_GC018_CVF_NCR_R0_W01_HTML_PROFILE_2026-09-26.md`.
- Dispatch release owner: `docs/reference/CVF_DISPATCH_RELEASE_READINESS_MACHINE_STANDARD_2026-09-25.md`.

Claude is `INTERNAL_AGENT` in this shared private workspace. Local owns private source/technical disposition; operator owns effect, expense and publication decisions. The Web agent's brief is advisory and does not decide this scope.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| Candidate selection | roadmap D009, committed at `11ba9eb46` | no reselection | ACCEPT |
| W00 source trace | Local-accepted return at `c7b7a2c721a3388a738eb2b2633fc4414cf1dff3` | reuse consumer and known gaps, no row-by-row repeat | ACCEPT |
| Paired GC-018 | exact W01 baseline in material dispatch batch | commit, continuity binding, bound pre-dispatch gate | PENDING_GATE |
| Actual profile/effect | destination, retention, latency, cost and operator data/effect choice still open | W01 read-only, no route invocation | DEFER |

## Agent Roles And Intake Role Routing Decision

| Role | Responsibility |
|---|---|
| Operator | relays committed packet; later decides data/effect/expense and guide/video scope |
| Local dispatcher/reviewer | scope, dispatch admission, source/technical review, commit and continuity |
| Internal worker | bounded read-only source/profile investigation and one uncommitted return |

| Field | Value |
|---|---|
| intake summary | selected roadmap plus accepted W00 source review; no new upstream intake |
| scope classification | one current private cvf-web route/profile, documentation-only |
| risk sensitivity | private source/config metadata read; no secret value read or effect |
| selected role route | `SINGLE_AGENT_SINGLE_ROLE` worker phase with distinct Local reviewer |
| role separation basis | worker cannot accept or commit its own return |
| escalation condition | actual secret/config value needed, source contradiction, cross-lane conflict, route invocation or new authority |

## Scope And Maximum Worker Path Manifest

Allowed:

- read current Git status, source and tests along the existing Work Transfer HTML export route; reuse W00 consumer trace and Local disposition;
- inspect non-secret profile documentation and configuration *presence/shape* without printing or copying `NEXTAUTH_URL`, secrets, request bodies or tokens; if actual runtime value is unavailable, mark `UNKNOWN`;
- classify receipt helper invocation conditions, destination derivation, payload fields/maximum source excerpt, timeout/error path and measurable versus unmeasured latency, retention and expense;
- identify exact P06 schema/type/size-before-normalization and P08 secret-detection/exemption-fixture gaps from current code/tests; propose minimum later tests without editing them;
- prepare a UI walkthrough protocol using a harmless fixture and explicit no-egress/no-effect prerequisite; do not execute browser UI in W01;
- create and repair only `docs/reviews/CVF_CVF_NCR_R0_W01_HTML_PROFILE_WORKER_RETURN_2026-09-26.md` and run document/governance checks.

Forbidden:

- changing runtime/Web/source/tests/config, guide/roadmap, checkers/registries, prior W00 evidence, active handoff/state, external mirrors or the 52-deferred lane;
- opening a browser session to submit/export, invoking the API or receipt endpoint, network/egress, provider/live/credentials, dependency install, media work or public/deploy action;
- reading or emitting raw environment/secret values, staging, committing, pushing, resetting, stashing or cleaning;
- calling W00 source reading an actual UI walkthrough or source-visible code proof of actual profile cost/retention.

Risk ceiling: read-only source/profile classification and one pending document. An actual UI walkthrough or test/effect needs a later scoped order.

## Write Ownership

The worker owns only the exact pending W01 return path. Local owns reviewer disposition, material commit and continuity. The 52-deferred lane and all other workspace paths remain with their current owners.

## Required First Reads And Pre-Flight

Read `AGENTS.md`, `CVF_SESSION_MEMORY.md`, its bootstrap, active handoff, paired baseline, selected NCR roadmap, `DESIGN.md` for UI claims, guard orientation, governed literal gotchas, and checker sources applicable to the worker return. Then inspect only source paths needed by the bounded trace. The worker captures `executionBaseHead` and `git status --short` before changes; if another lane owns a touched path or the dispatch packet is dirty, stop and return the conflict.

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R0_W01_HTML_PROFILE_2026-09-26.md
```

The orchestrator must run final `pre-dispatch` with the same exact binding after material and continuity commits. A failed bound gate blocks relay; the worker does not infer release from the status label alone.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| HTML candidate and guide split | roadmap decision | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D009/D010/Q001 | selected HTML, later guide/video | operator scope | ACCEPT |
| accepted W00 | reviewer evidence | `docs/reviews/CVF_CVF_NCR_R0_W00_PILOT_SELECTION_WORKER_RETURN_2026-09-26.md` | Local Reviewer Disposition | accepted bounded source packet | Local reviewer | ACCEPT |
| UI consumer | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx` | ArtifactExportPanel embedding | Work Transfer page | cvf-web UI | ACCEPT |
| export form | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | handle export / fetch | ArtifactExportPanel | cvf-web UI | ACCEPT |
| export route | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | POST / awaited fetchGovernanceReceipt | artifact export route | cvf-web API | ACCEPT |
| receipt helper | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | NEXTAUTH_URL-conditioned fetch | fetchGovernanceReceipt | cvf-web receipt helper | ACCEPT |

Actual configured destination, retention and cost are `NEEDS_EVIDENCE`; this table verifies source wiring only.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| W01 packet names | exact new baseline/work-order paths absent before authoring | new packet, no overwrite |
| W00 source | accepted prior return exists at named path | reuse, no duplicate selection |
| New runtime name | none introduced | NOT_APPLICABLE_WITH_REASON: source/profile document only |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| D009/Q001 selected HTML | Scope / Source Verification | selected candidate retained | route + reviewer locator | PASS_FOR_DISPATCH |
| R1 pre-pilot profile | Required Worker Return | destination/payload/retention/latency/cost table | source and secret-safe profile evidence | PASS_FOR_DISPATCH |
| P06/P08 open depth | Required Worker Return | validation/fixture gap table | route/test locators | PASS_FOR_DISPATCH |
| Q003 internal simulation | Required Worker Return | later UI walkthrough protocol | no actual UI claim | PASS_FOR_DISPATCH |
| D010 guide/video | Forbidden scope | follow-on documentation note only | no guide/video file mutation | N/A with reason: separate tranche |
| R2/R3 effect | Forbidden scope | stop conditions | exact changed set and no invocation | N/A with reason: later authority |

## Design Control Carry-Forward

| Control | W01 handling | Evidence |
|---|---|---|
| I01 non-coder first | later UI walkthrough protocol with harmless data | plan only, no usability proof |
| I02-I04 source/control boundary | trace actual route and conditional receipt egress | current code/profile evidence |
| I05-I08 value/effect/review/portability | retain selected outcome, list data/effect choices | open-decision matrix |
| I09-I12 proportionality/maturity/direction | reuse W00 and avoid duplicate owners or video conflation | dependency and claim boundaries |

## Required Worker Return And Acceptance

The exact worker return must contain:

1. `executionBaseHead`, starting/ending `git status --short`, exact one-file changed set and no-commit statement;
2. source-to-effect trace from Work Transfer form through export route and receipt helper, citing current path/line or symbol;
3. secret-safe profile matrix: actual known/unknown `NEXTAUTH_URL` presence/shape, derived endpoint, conditional egress, payload excerpt, timeout/error handling, retention owner, latency and expense with `UNKNOWN` for unmeasured facts;
4. P06/P08 matrix separating source-visible partial behavior from missing schema/type/size and secret/exemption fixture depth, with minimal later tests and no false `CONFIRMED`;
5. UI-interaction walkthrough protocol, safe fixture and stop conditions; explicitly mark `NOT_RUN` for actual UI interaction and distinguish it from source reading;
6. Q001 decisions still open for Local/operator: data class, effect, endpoint/retention, cost ceiling, L-level and metric/profile; a bounded next work package only after these are dispositioned;
7. source verification, checker read-ahead, agent trace, claim boundary, epistemic process, public export disposition and Return-Time Closeability Recheck required by the worker-return checker;
8. `COMPLETE_PENDING_REVIEW` only for a complete evidence packet, otherwise `BLOCKED_WITH_REASON` naming the smallest blocker. Neither status approves a pilot run.

Stop on a needed raw secret/config value, route call, unexpected write, source contradiction or unresolved cross-lane collision. Return a bounded unknown instead of manufacturing actual-profile proof.

## Execution Plan

1. Capture HEAD/status; pass bound pre-implementation gate before editing.
2. Reuse the accepted W00 source trace, then inspect only named route/helper/tests and non-secret profile evidence.
3. Classify source-visible versus actual-profile facts; mark missing values `UNKNOWN`.
4. Write one W01 return with P06/P08 gaps, receipt boundary and later UI walkthrough protocol.
5. Run applicable return gates, repair the allowed document, return uncommitted.

## Evidence Requirements

Every positive assertion cites current source or an exact secret-safe profile observation. Do not print `NEXTAUTH_URL` value, source-content payload or credentials. Distinguish configured value `UNKNOWN` from helper code semantics. No provider/network/UI action is evidence in W01 because none is authorized.

## Acceptance Criteria

Local can review the packet when all eight return items are present, actual profile facts are measured or honestly `UNKNOWN`, P06/P08 are not overclaimed, the UI walkthrough is explicitly `NOT_RUN`, the exact changed set is one file and the worker-return gate passes. Runtime/pilot readiness is not a W01 acceptance criterion.

## Review Gate

Local reviewer checks source locators and decision-changing contradictions under MFRP, consuming valid W00 evidence without a row-by-row replay. A repair request is one consolidated set. W01 acceptance does not authorize browser execution, receipt egress or R1 implementation.

## Closure Checklist

- One pending W01 return and exact changed set.
- Profile, P06/P08, and UI evidence classes bounded.
- Required worker gates recorded with actual results.
- Local owns material review/commit and later continuity.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for missing source, required raw secret/config access, actual endpoint call, cross-lane collision or mandatory gate impossible to repair in the one-file scope. Do not widen worker authority.

## Worker Autonomy / No-Question Rule

Worker proceeds on allowed read-only source checks and return-document repairs. Repair allowed-scope gate failures directly. Escalate only contradictions or actions outside this exact scope; operator is reserved for later effect/expense decisions.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-R0-W01
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: INITIAL_DISPATCH
rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: WORKER_RETURN
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-r0-w01-html-profile","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | this packet and exact worker return | shared-workspace read-only source mapping; no commit/effect | current roadmap, source locators and Local review | shared-workspace file/Git return only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external adapter work | no ingress/auth/approval/receipt/raw-data/mutation/public authority | external advisory already reconciled in roadmap | N/A with reason: CLI/MCP implementation is outside this batch | N/A_WITH_REASON |

## Independent Review Probe Admission Contract

independentProbeRequired: NOT_APPLICABLE_WITH_REASON: this R0/W01 assignment produces documentation-only source and applicability analysis, with no executable behavior oracle; distinct Local source review remains required.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline and work order | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline and work order | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker and active session sources | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact worker return path | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return ADIF block | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact worker return path | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact worker return path | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker return and reviewer disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material paths | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker return reviewer disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity paths | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | material and continuity committed ranges | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one internal worker followed by distinct Local reviewer/closer |
| phase | dispatch, R0/W01 secret-safe profile mapping, pending review |
| baseHeadFor(phase) | dispatchBaseHead=`11ba9eb46`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exact one-file worker return only; separate orchestrator dispatch/continuity paths |
| traceScope(phase, actor) | worker return records exact reads, findings and changed set; Local review evaluates returned evidence |
| commitOwner(phase) | worker forbidden; Local closer after review |
| crossBatchIsolation | 52-deferred lane and all non-owned paths are excluded; no stash/reset/clean |
| nextMoveSurfaces | committed dispatch binding before worker; reviewer closure and later continuity |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: internal worker after bound pre-dispatch passes

laneOwnedPaths: exact worker return path only

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: terminal worker return, exact changed set, empty staged set and worker-return gate

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no-commit return, exact paths, current source trace and Local review |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | envelope first-section rule; `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification columns; no-question rule; dual-surface six columns; closeability scalars and nine columns; worker-return full-gate literals |
| gateRunPurpose | confirm authored packet against machine gates after source and literal read; not first discovery |
| claimBoundary | static dispatch shape only; no source-gap verdict, integration or runtime truth is supplied by this block |

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return, inspect checker source for its `docType`, path family and conditional content. Required section names are Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Decision / Disposition; Checker Source Read-Ahead Block; Epistemic Process Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; Return-Time Closeability Recheck. Do not put heading syntax in a shape-list. Conditional new-source, rescan, corpus, knowledge-map and closure blocks use explicit N/A-with-reason when inapplicable.

## Work-Order Fulfillment Manifest

| Obligation | Owning artifact | Terminal worker evidence |
|---|---|---|
| selected HTML source path | worker return | reuse W00 plus fresh route/helper locators |
| secret-safe actual-profile classification | worker return | known/UNKNOWN matrix, no raw values |
| P06/P08 gap depth | worker return | source-visible behavior versus missing fixtures |
| receipt egress/latency/cost boundary | worker return | conditional source trace and profile unknowns |
| later UI walkthrough | worker return | protocol only, actual interaction NOT_RUN |
| no effect/cross-lane work | worker return | exact changed set and no-invocation evidence |
| pending Local review | worker return | COMPLETE_PENDING_REVIEW or named blocker |

## Required Artifact Manifest

| Path | Required at handoff | Worker action | Forbidden paths |
|---|---|---|---|
| `docs/reviews/CVF_CVF_NCR_R0_W01_HTML_PROFILE_WORKER_RETURN_2026-09-26.md` | YES | create one pending evidence-backed return | every other tracked or untracked path |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_CVF_NCR_R0_W01_HTML_PROFILE_WORKER_RETURN_2026-09-26.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker leaves the return pending and records actual source commands, evidence classes, `executionBaseHead`, `git status --short`, Changed Files and No-Commit Statement. Reviewer-fast and committed-range closure remain Local work.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_CVF_NCR_R0_W01_HTML_PROFILE_COMPLETION_2026-09-26.md` is reviewer-owned and created only if a separate completion review is needed |
| reviewerOwnedClosurePaths | optional completion review, worker return disposition and authorized continuity paths |
| closureOwner | Local reviewer/closer distinct from worker |
| workerCommitPermission | FORBIDDEN |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R0_W01_HTML_PROFILE_2026-09-26.md
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
```

Worker-return gate must pass for applicable pending-document checks. The worker records any structural gate that legitimately requires reviewer commit as pending, without claiming closure. Local reviewer applies MFRP non-duplication and rechecks at return.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | CVF-NCR-R0-W01 dispatch authoring, 2026-09-26 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, Git, scaffold and local gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | operator instruction; NCR roadmap D009/D010 and R1 pre-pilot boundary |
| Before status evidence | clean worktree at HEAD `11ba9eb46` before packet authoring |
| After status evidence | material and continuity commits before worker relay |
| Diff evidence | exact two-file dispatch material set |
| Approval boundary | operator data/effect/budget; Local source/technical disposition |
| Claim boundary | docs-only dispatch; no implemented slice |
| Agent type | orchestrator/reviewer |
| Invocation ID | `cvf-ncr-r0-w01-dispatch-2026-09-26` |
| Expected manifest | paired baseline and work order |
| Actual changed set | verified at material commit |
| Manifest delta | pending material commit |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | W01 source/profile classification only |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement or execution-control behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: pending worker return with source locators only |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no worker execution or effect is authorized by this packet |
| invocationBoundary | read-only local commands only |
| interceptionBoundary | no direct interception, wrapper/proxy or runtime gate claim |
| claimLanguage | source-visible behavior, actual-profile unknowns and later prerequisites only |
| forbiddenExpansion | no runtime/provider/live/public/Web/MCP mutation without later authority |

## High-Risk Local Transaction Proof Applicability

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - this batch authorizes read-only analysis and one pending Markdown return; no high-risk local transaction.

## Foundation Storage Layout Block

- N/A with reason: this work order creates no foundation file or reference-family folder; it authorizes one pending review document only.

## Epistemic Process Block

### Expected Result / Prediction

The existing HTML UI and route should remain source-visible, while actual configured receipt destination, retention and cost may be unavailable from safe local evidence.

### Evidence Comparison

The worker compares route/helper/tests with non-secret profile metadata, keeping source semantics separate from actual environment behavior.

### Contradiction Or Gap Disposition

Any missing actual value remains `UNKNOWN`; a source contradiction or need for a live request yields a bounded blocker or next-authority proposal.

### Claim Update

Local can accept a profile-boundary packet without treating it as UI, network, provider, usability or runtime proof.

## Claim Boundary

This work order authorizes one uncommitted, secret-safe W01 source/profile return. It does not run the HTML pilot, inspect raw secrets, repair P06/P08, create the overall user guide or video, send data, approve cost, publish or deploy.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch and worker return only; no public artifact or sync is authorized.

## Operator Checkpoint

After Local review, operator decides whether to permit any HTML pilot effect, sample data, endpoint/retention and expense. The overall CVF guide/video remains a separate documentation tranche; this worker does not produce or approve it.
