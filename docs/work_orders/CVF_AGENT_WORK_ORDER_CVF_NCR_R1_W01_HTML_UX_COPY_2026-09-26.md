# CVF Agent Work Order - CVF-NCR-R1-W01 HTML UX Copy Implementation

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

providerExecutionAuthority: FORBIDDEN

Batch ID: CVF-NCR-R1-W01

Dispatch base head: `cfc1cbb6d0fc18a523f6d2369fb15a7e5553ae14`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: shared-workspace `INTERNAL_AGENT` Web UI implementation role

Reviewer/closer: Local orchestrator/reviewer, distinct from worker

Worker return path: `docs/reviews/CVF_CVF_NCR_R1_W01_HTML_UX_COPY_WORKER_RETURN_2026-09-26.md`

## Dispatch Prompt Envelope

Role: internal worker for bounded NCR-R1/W01 HTML export UX copy implementation.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_W01_HTML_UX_COPY_2026-09-26.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture committed HEAD and clean status before edits.

Current-time notes: operator relays this exact committed packet after Local's bound pre-dispatch PASS; accepted R0/W00-W02 and R1/W00 are bounded evidence, not an invitation to rerun them.

Do-not-misread notes: edit only the existing HTML export component, its focused test and one return. No browser/UI interaction, export/evaluate request, raw config, dependency, route/helper/config, guide/video, provider/live or public action.

Required first actions: read session memory/bootstrap/handoff, guard orientation and literal gotchas, paired baseline, this work order, named current sources and applicable checker sources; capture HEAD/status and run bound pre-implementation before editing.

Return contract: leave exactly the component, its focused test and worker-return path uncommitted with `COMPLETE_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` naming the smallest contradiction; Local reviews and commits.

## Purpose

Implement the accepted R1/W00 bilingual disclosure and refusal copy in the
existing `ArtifactExportPanel` without changing its request, route, validation
or receipt logic. Place the uncertainty warning before Build HTML; explain
absent receipts without claiming no send; give secret/missing-field recovery
without claiming nothing left the browser. Prove the visible states with
focused mocked tests, and keep actual UI interaction `NOT_RUN`.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-R1-W01 --title "HTML UX Copy Implementation" --date 2026-09-26 --base cfc1cbb6d0fc18a523f6d2369fb15a7e5553ae14 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit internal worker profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | exact existing-component/test/return manifest, accepted bilingual copy, no-call gate |
| checkerReadAheadConfirmation | dispatch quality, envelope, gate-to-role, ADIF, active-state and governed read-ahead checker source inspected |
| docOnlyNewFields | copy/error-state implementation, mock-only test evidence and effect boundary |
| claimBoundary | authoring provenance only; no UI-interaction or user-comprehension proof |

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-NCR-R1-W01","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx","docs/baselines/","docs/work_orders/","docs/reviews/","AGENT_HANDOFF_V63_2026-09-18.md","CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json","CVF_SESSION/ACTIVE_SESSION_STATE.json","CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json","CVF_SESSION/state/entries/nextAllowedMove.json","CVF_SESSION/state/entries/cvfNcrR1W00HtmlUxDispatch20260926.json","CVF_SESSION/state/entries/cvfNcrR1W01HtmlUxCopyDispatch20260926.json","CVF_SESSION_MEMORY.md"],"claims":["bounded HTML export UX copy implementation"],"requiredProof":["accepted-copy source binding","bilingual visible states","focused mocked tests","exact changed set","worker-return full gate"],"operatorCheckpoints":["pilot data/effect/expense choice","actual UI/route/provider/live/public/deployment action"],"forbiddenEffects":["worker commit","UI/route invocation","route or helper logic change","dependency installation","provider/live invocation","public write","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":false,"corpusReceiptRef":"docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md","completenessClaimChanged":false}}
```

## Authority Chain

- Operator: continue the selected roadmap to the next tranche's work order, then stop for manual relay.
- Active session memory/handoff: `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V63_2026-09-18.md`.
- Roadmap: NCR-R1, D008-D011, Q001/Q003 and A01-A03/A10/A12 in `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`.
- Accepted R0 packets: W00 at `c7b7a2c72`, W01 at `d9b43a6f6`, W02 at `c638f2ece`; accepted R1/W00 at `97532f703`.
- Paired baseline: `docs/baselines/CVF_GC018_CVF_NCR_R1_W01_HTML_UX_COPY_2026-09-26.md`.

The shared-workspace worker is `INTERNAL_AGENT` regardless of provider. Local
owns private technical/design disposition; operator owns data/effect/expense.
Prior external research is advisory and is not a worker source-of-truth lane.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| Selected consumer | roadmap D009 and accepted W00 | do not reselect or create parallel UI owner | ACCEPT |
| W01/W02 boundaries | accepted source-only returns | reuse; actual profile stays unknown | ACCEPT_BOUNDED |
| UI source | existing `ArtifactExportPanel` and focused test | reuse current component; no second owner | ACCEPT |
| R1/W00 copy | repaired bilingual proposal and Local disposition at `97532f703` | implement only the four lines and placement, with honest error matching | ACCEPT_BOUNDED |
| CI/remote | no fresh SHA/profile CI evidence in this packet | no release or CI PASS claim; focused local tests only | DEFER |
| Q001 effects and Q003 actual walkthrough | operator effect choice and UI interaction remain open | component/test changes do not run the pilot | DEFER |

## Agent Roles And Intake Role Routing Decision

| Role | Responsibility |
|---|---|
| Operator | relays committed packet; later decides pilot data/effect/expense and Human UX choices |
| Local dispatcher/reviewer | dispatch admission, source/design review, commit and continuity |
| Internal worker | bounded component/test edit and one return, no commit |

| Field | Value |
|---|---|
| intake summary | selected roadmap plus accepted W00-W02; no new upstream intake |
| scope classification | existing Web UI copy and focused offline tests |
| risk sensitivity | private source and unresolved pilot data/egress; no actual route call in this order |
| selected role route | `SINGLE_AGENT_SINGLE_ROLE` worker phase with distinct Local reviewer |
| escalation condition | actual UI/effect, raw configuration, cross-lane conflict or source contradiction |

## Scope And Maximum Worker Path Manifest

Allowed:

- read the accepted R0/W00-W02 and R1/W00 review packets, roadmap R1, `DESIGN.md`, existing Work Transfer embedding, `ArtifactExportPanel.tsx`, its test and the export route/helper only for error/effect source binding;
- edit `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` to add the accepted bilingual disclosure immediately before Build HTML, an absent-receipt explanation when a generated result lacks a receipt, and plain-language recovery for the two known 400 errors while retaining the raw server error as secondary detail;
- edit `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` for focused mocked English/Vietnamese warning, absent-receipt and error recovery states; ensure unrelated/network errors retain truthful generic handling;
- create/repair `docs/reviews/CVF_CVF_NCR_R1_W01_HTML_UX_COPY_WORKER_RETURN_2026-09-26.md` with source/diff/test evidence and exact changed set.

Forbidden:

- browser, screenshot, UI click, form submit, export/evaluate/API request, actual network/egress or performance measurement;
- read/emit raw `.env*` values, ledger content, credentials or sensitive form data;
- change route/helper/server/auth/config/dependency/other UI/roadmap/guide/video/checker/registry/session/52-deferred paths;
- add a chooser, approval/storage owner, consent toggle or generate-without-receipt option; alter request payload, validation, receipt invocation, error status or copy/download/print logic;
- install dependencies, stage, commit, push, stash, reset or clean.

Risk ceiling: source/test-only copy implementation. Actual UI walkthrough or
pilot with possible receipt egress needs separate authority and profile.
The dispatch routing manifest includes the R1/W01 continuity entry for Local
commit accounting; it does not add that path to the worker's three-path set.

## Write Ownership

Worker owns only the two exact component/test paths and pending return path.
Local owns reviewer disposition, material commit and session sync. Other
active lanes retain their own files.

## Required First Reads And Pre-Flight

Read `AGENTS.md`, `CVF_SESSION_MEMORY.md`, bootstrap and active handoff,
paired baseline, selected roadmap, `DESIGN.md`, guard orientation, literal
gotchas, and applicable worker-return checkers. Verify the exact committed
dispatch anchor and clean lane. Then run:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_W01_HTML_UX_COPY_2026-09-26.md
```

If the bound gate, HEAD or lane ownership disagrees, return a named blocker
before editing. Local must pass final `pre-dispatch` after material and
continuity commits; `DISPATCH_READY` text alone is insufficient.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| selected HTML and R1 contract | roadmap decision | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | R0/R1, D009-D011, Q001 | existing consumer and bounded UX delta | Local/operator | ACCEPT |
| accepted source/effect boundary | bounded reviewer evidence | `docs/reviews/CVF_CVF_NCR_R0_W02_HTML_DOWNSTREAM_WORKER_RETURN_2026-09-26.md` | Local Reviewer Disposition | source-only downstream effects | Local reviewer | ACCEPT |
| repaired copy candidate | accepted reviewer evidence | `docs/reviews/CVF_CVF_NCR_R1_W00_HTML_UX_CONTRACT_WORKER_RETURN_2026-09-26.md` | Effect/Unknown Disclosure And Refusal Design; Local Reviewer Disposition | four bilingual lines, bounded to copy and no effect permission | Local reviewer | ACCEPT |
| HTML form and states | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `DEFAULT_REQUEST`, `LABELS`, submit/result/actions | `ArtifactExportPanel` | cvf-web component | ACCEPT |
| focused existing tests | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | `describe('ArtifactExportPanel')` | mocked fetch, English/Vietnamese labels | cvf-web test | ACCEPT |
| current error branches | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | lines 235-272 | missing fields and secret pattern | export route | ACCEPT |
| existing entry point | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx` | lines 261-275 | export action and embedded panel | cvf-web page | ACCEPT |
| UI design constraints | current design | canonical UI contract `DESIGN.md` | form workflow and state/error guidance | design contract | CVF UI owner | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| R1/W01 copy packet names | `rg --files docs/baselines docs/work_orders docs/reviews` found none before authoring | NEW_PATHS |
| Existing form | Work Transfer embeds `ArtifactExportPanel` | REUSE_OWNER |
| New runtime name | none requested | NOT_APPLICABLE_WITH_REASON |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output evidence | Status |
|---|---|---|---|
| R1 reuse before delta | Scope / Source Verification | existing panel and test, no new owner | PASS_FOR_DISPATCH |
| R1 effect/error/recovery | Required Worker Return | bilingual visible copy with focused mocked tests | PASS_FOR_DISPATCH |
| D011 installation versus invocation | Required Worker Return | invocation effect uncertainty; no setup claim | PASS_FOR_DISPATCH |
| Q003 internal simulation | Evidence Requirements | actual UI interaction and real user remain unmeasured | PASS_FOR_DISPATCH |
| A01-A03/A10/A12 | Acceptance Criteria | bounded source/test copy coverage and explicit unmeasured cells | PASS_FOR_DISPATCH |
| D010 guide/video | Forbidden scope | no media/guide action | N/A with reason: separate tranche |

## Required Worker Return

The exact return must contain:

1. `executionBaseHead`, starting/ending `git status --short`, exact three-path changed set and no-commit statement;
2. component/test diff summary binding each visible line to accepted R1/W00 copy, or explicitly explaining a small wording adjustment;
3. focused mocked English/Vietnamese assertions for pre-submit warning, absent receipt, secret refusal, missing-field refusal and an unrelated error that stays generic; typecheck/lint result for touched files when available;
4. evidence that disclosure precedes Build HTML in DOM order and no request/route/helper/validation/receipt logic changed;
5. actual UI interaction `NOT_RUN`, real-user comprehension `NOT_EVALUATED`, P06/P08 `PARTIALLY_CONFIRMED_NEEDS_EVIDENCE`, real profile/cost/retention `UNKNOWN`;
6. source verification, checker read-ahead, epistemic process, agent trace, public export disposition, claim boundary, and Return-Time Closeability Recheck required by gates.

Stop at a source contradiction, needed raw config, required UI/network effect,
unexpected write or cross-lane collision; return `BLOCKED_WITH_REASON` rather
than silently widening authority.

## Acceptance Criteria

Local can review the result when the four accepted copy cases are visible in
the existing panel in both languages, the warning precedes the action in DOM
order, known 400 errors have accurate recovery and unrelated errors are not
misclassified. Focused mocked tests and typecheck must pass or carry a named
blocker. The return does not claim actual usability, accessibility, P06/P08
closure, Q001 resolution or R1 exit.

## Execution Plan

1. Capture HEAD/status and pass bound pre-implementation before writing.
2. Reuse accepted R0 and R1/W00 evidence, inspect the named component/test and
   the exact route error strings needed for mapping.
3. Make only the bounded copy/error presentation change and focused mocked
   tests; draft one return at the exact owned path.
4. Run focused tests, TypeScript check, touched-file lint and applicable
   worker-return gates; repair only the three allowed paths and leave pending.

## Evidence Requirements

Every effect assertion needs a current source locator or accepted bounded
review. Mocked component tests prove only local rendering and error mapping,
not actual UI interaction or real-user comprehension. Use `UNKNOWN` for real
destination, retention, measured latency/cost and supported provider.

## Review Gate

Local consumes valid R0 and R1/W00 evidence and samples the new UI diff and
focused tests under MFRP. Repair requests form one consolidated set. A clean
document or mocked-test gate is not user or runtime proof.

## Closure Checklist

- Exactly three worker-owned changed paths, no staged change or worker commit.
- Four bilingual copy states and focused offline evidence.
- Required gate outputs and exact changed set recorded.
- Local owns reviewer acceptance, material commit and later continuity.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for a needed UI/API interaction, raw profile
value, unexpected write, source contradiction, or required change outside the
three-path manifest. Do not widen worker authority.

## Operator Checkpoint

Operator relay of this exact committed work order permits only the bounded
UI source/test edit. Operator later decides pilot data class, whether any
receipt/evaluate effect is permitted, retention/cost ceiling, and any Human
wording choice that materially changes disclosure. No pilot call follows.

## Worker Autonomy / No-Question Rule

Worker repairs allowed-scope component/test/return defects directly. Ask Local
only for missing authority, source contradiction or unavoidable out-of-scope
action. Do not ask operator to decide pilot effects inside this worker phase.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-R1-W01
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-r1-w01-html-ux-copy","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | this packet and exact three-path return | existing Web component/test copy edit, no commit/effect | roadmap and accepted R1/W00 | local file/Git handoff | BOUNDED_IMPLEMENTATION |
| `EXTERNAL_AGENT_CLI_MCP` | none | no new external effect authority | advisory research already reconciled | N/A with reason: no adapter scope | N/A_WITH_REASON |

## Independent Review Probe Admission Contract

independentProbeRequired: NOT_APPLICABLE_WITH_REASON: focused mocked component assertions and Local UI-diff review cover this copy-only change; no live governance oracle is claimed.

## Foundation Storage Layout Block

N/A with reason: this order edits one existing component/test and creates a pending return. It does not
create, split, relocate or refactor a durable governance foundation file or
storage/index layout.

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
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | component, focused test and exact return | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return ADIF block | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact three-path worker set | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact worker return | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | component, test, return and disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material paths | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker return disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity paths | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | material and continuity split ranges | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one internal worker followed by distinct Local reviewer/closer |
| phase | dispatch, R1/W01 existing-component UX copy implementation, pending review |
| baseHeadFor(phase) | dispatchBaseHead=`cfc1cbb6d0fc18a523f6d2369fb15a7e5553ae14`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exact component/test/return worker set; separate dispatch/continuity paths |
| traceScope(phase, actor) | worker return records reads, claims and changed set; Local evaluates |
| commitOwner(phase) | worker forbidden; Local closer after review |
| crossBatchIsolation | 52-deferred and all non-owned paths excluded; no stash/reset/clean |
| nextMoveSurfaces | committed dispatch binding before worker, then reviewer/continuity |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: internal worker after bound pre-dispatch PASS

laneOwnedPaths: exact component, existing test and worker return paths only

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
| Dispatch impact | exact no-commit three-path UI copy boundary without runtime call |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | first-section envelope, dispatch-ready status, no-commit token, Source Verification columns, gate-to-role scalars and nine columns, worker-return full-gate literals |
| gateRunPurpose | confirmation of completed packet shape after source read-ahead |
| claimBoundary | static checker shape does not prove worker compliance, actual UI behavior or UX quality |

## Worker Output Checker Read-Ahead Mandate

Before writing the return, inspect checkers for its docType and path family.
Use the required return headings for Purpose, Target / Source, Scope /
Methodology, Findings / Position, Risk / Corrective Action, Decision /
Disposition, Checker Source Read-Ahead Block, Epistemic Process Block, Agent
Operation Trace Block, Delta Execution Claim Boundary Control Block, Public
Export Disposition and Return-Time Closeability Recheck. Keep required
multi-word headings on one physical line in the artifact. Route inapplicable
corpus, external-intake or runtime classes with an explicit reason.

## Work-Order Fulfillment Manifest

| Obligation | Owning artifact | Terminal worker evidence |
|---|---|---|
| existing HTML flow | component | reuse existing form and submit handler |
| bounded copy delta | component and focused test | four bilingual visible states and mocked assertions |
| effect boundary | worker return | warning/refusal wording, actual destination unknown |
| evidence-class separation | worker return | mocked test, UI NOT_RUN, real user NOT_EVALUATED |
| no effect/cross-lane work | worker return | exact changed set and no-invocation evidence |
| pending Local review | worker return | COMPLETE_PENDING_REVIEW or named blocker |

## Required Artifact Manifest

| Path | Required at handoff | Worker action | Forbidden paths |
|---|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | YES | edit visible copy and error presentation only | all other Web source |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | YES | edit focused mocked assertions only | all other tests |
| `docs/reviews/CVF_CVF_NCR_R1_W01_HTML_UX_COPY_WORKER_RETURN_2026-09-26.md` | YES | create one pending implementation/evidence return | every other tracked or untracked path |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_CVF_NCR_R1_W01_HTML_UX_COPY_WORKER_RETURN_2026-09-26.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker leaves the return pending and records actual commands,
`executionBaseHead`, before/after `git status --short`, Changed Files and
No-Commit Statement. Reviewer-fast and committed-range closure are Local work.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_CVF_NCR_R1_W01_HTML_UX_COPY_COMPLETION_2026-09-26.md` is reviewer-owned and optional |
| reviewerOwnedClosurePaths | optional completion review, return disposition and authorized continuity |
| closureOwner | Local reviewer/closer distinct from worker |
| workerCommitPermission | FORBIDDEN |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_W01_HTML_UX_COPY_2026-09-26.md
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
```

The worker records actual gate results and leaves reviewer-owned gates pending.
No successful document or mocked-test gate is evidence of an actual UI walkthrough.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/dispatch author |
| Provider or surface | private CVF workspace |
| Session or invocation | CVF-NCR-R1-W01 authoring, 2026-09-26 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, Git, ADIF resolver, scaffold and local gates |
| Target paths | paired R1/W01 baseline and this work order |
| Allowed scope source | operator next-tranche instruction and selected NCR roadmap R1 |
| Before status evidence | clean worktree at `cfc1cbb6d` |
| After status evidence | two new dispatch paths pending material commit |
| Diff evidence | exact two-path material dispatch; continuity follows separately |
| Approval boundary | Local work-order authoring, operator relay for bounded UI edit and later pilot effect/data/expense |
| Claim boundary | existing-component UX copy order, no UI interaction or pilot effect |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `cvf-ncr-r1-w01-dispatch-author-20260926` |
| Expected manifest | paired baseline and this work order |
| Actual changed set | verify before material commit |
| Manifest delta | PENDING_FINAL_CHECK |
| Deletion or rename disposition | N/A with reason: none planned |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | R1/W01 existing-component copy dispatch |
| claimDisposition | CLAIM_REJECTED_NO_RECEIPT: no execution-control behavior claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatch creates no UI/route/network action |
| invocationBoundary | authored packet and read-only local checks only |
| interceptionBoundary | no interception or runtime gate claim |
| claimLanguage | source-backed copy implementation scope and explicit unknowns only |
| forbiddenExpansion | no route/helper/config/provider/live/public mutation from this order |

## Claim Boundary

This packet prepares one bounded internal-worker UI-copy edit for operator
relay. It does not authorize a UI interaction, HTML route call, provider/live
proof, P06/P08 closure, guide/video production, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet only.
