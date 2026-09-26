# CVF GC-018 Baseline - CVF-NCR-R1-W01 HTML UX Copy Implementation

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Batch ID: CVF-NCR-R1-W01

Dispatch base head: `cfc1cbb6d0fc18a523f6d2369fb15a7e5553ae14`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator for pilot data/effect/expense; Local for source and design disposition

Reviewer owner: Local orchestrator/reviewer, distinct from worker

Worker target: shared-workspace `INTERNAL_AGENT` Web UI implementation role

## Purpose

Authorize one bounded R1 copy implementation in the existing HTML export panel.
Use the accepted R1/W00 copy candidate to expose the uncertain receipt effect
before Build HTML and provide honest refusal recovery. The worker may edit the
component, its focused tests and one return; no browser, route call, raw
configuration read or pilot occurs.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-R1-W01 --title "HTML UX Copy Implementation" --date 2026-09-26 --base cfc1cbb6d0fc18a523f6d2369fb15a7e5553ae14 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit internal worker profile; Web UI scope narrowed manually |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | bounded R1 existing-component UI copy edit, inherited W00-W02 and R1/W00 evidence, exact three-path worker manifest |
| checkerReadAheadConfirmation | dispatch-quality, envelope, gate-to-role, ADIF, active-state and governed read-ahead sources inspected before authoring |
| docOnlyNewFields | implementation scope, copy source binding, effect boundary and focused offline test proof |
| claimBoundary | scaffold/dispatch shape only; no UI-interaction, runtime or usability proof |

## Authorization / Decision

The operator instructed Local to continue to the next roadmap tranche and stop
at a work order for manual relay. The selected HTML consumer was accepted in
R0/W00; R0/W01 profiled the first receipt hop and R0/W02 mapped downstream
source effects. The accepted R1/W00 return at `97532f703` supplies a repaired
copy candidate. The operator's relay of this work order permits the bounded
UI text change, while Q001 data/effect/expense and any effect-bearing pilot
remain open.

## Scope

Allowed: read the accepted R0/W00-W02 and R1/W00 packets, selected roadmap R1,
`DESIGN.md`, current `ArtifactExportPanel.tsx` and its existing focused test.
Edit only those two source/test paths to add bilingual pre-submit disclosure,
absent-receipt explanation, and accurate existing-error recovery. Return one
pending source/evidence review with exact changed set and offline test result.

Forbidden: UI/browser interaction, form submission, API/network/provider call,
raw configuration or ledger data, route/helper/server/config/dependency edit,
new dashboard/chooser/approval/storage owner, guide/video, public/deploy,
worker commit, and changes to the 52-deferred lane.

Maximum worker write set: `ArtifactExportPanel.tsx`, its existing
`ArtifactExportPanel.test.tsx`, and
`docs/reviews/CVF_CVF_NCR_R1_W01_HTML_UX_COPY_WORKER_RETURN_2026-09-26.md`.
Local owns review, correction, commit and continuity.

## Baseline Invariants

1. Use the already-wired `ArtifactExportPanel` in Work Transfer; do not claim
   the UI form is missing or reselect a pilot candidate.
2. Keep source/test execution separate from actual agent UI interaction
   (`NOT_RUN`) and real-user usability (`NOT_EVALUATED`).
3. The HTML route can conditionally send source content via the receipt
   helper. The downstream client fallback `8000` differs from the FastAPI
   server's documented `8100`. Actual URL, data, retention, latency and cost
   remain open; visible copy must disclose uncertainty, not invent safety.
4. P06/P08 stay `PARTIALLY_CONFIRMED_NEEDS_EVIDENCE`. This copy order does
   not change route validation or secret scanning.
5. No L1/L2/L3, R1 exit, pilot readiness, accessibility conformance or
   non-coder comprehension claim follows from a component/test change.
6. D010 overall CVF user guide and later video are separate scope; no media
   artifact is produced here.

## Verification / Evidence

The worker must bind each new visible line to the accepted R1/W00 copy and
confirm the warning appears before the submit action. Test the refusal
mapping with mocked fetch only; do not use a live route or claim pilot proof.
Record `UNKNOWN` where profile or runtime behavior is unmeasured.

## Dependency Release Evidence

| Dependency | Current evidence | Disposition |
|---|---|---|
| Pilot consumer | roadmap D009 and accepted W00 return at `c7b7a2c721a3388a738eb2b2633fc4414cf1dff3` | ACCEPT: one HTML consumer selected |
| First-hop profile | accepted W01 at `d9b43a6f6deff7fb19710b5a9a4f50bf2a6015b6` | ACCEPT_BOUNDED: source only |
| Downstream effects | accepted W02 at `c638f2ece` | ACCEPT_BOUNDED: actual reachability/retention open |
| Accepted R1/W00 copy | reviewer-repaired return at `97532f703`, `ACCEPTED_BOUNDED_UX_CONTRACT_PACKET` | ACCEPT_BOUNDED: copy candidate, not effect permission |
| CI and release | current local HEAD and remote CI/profile must be rechecked before any release claim | DEFER: this order proves only focused offline component behavior |
| Dispatch continuity source | active session bootstrap and next-move sources | ACCEPT: bind this dispatch after material commit |
| Real UI/pilot profile | actual endpoint, data/effect/expense and UI walkthrough unresolved | DEFER: no effect authorized |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | shared private workspace and exact three-path return | existing-component copy/test edit only; no commit or route effect | roadmap and accepted R1/W00 | local Git/file handoff | BOUNDED_IMPLEMENTATION |
| `EXTERNAL_AGENT_CLI_MCP` | no new external adapter | no ingress, credentials, approval, receipt or mutation authority | prior Web research already reconciled | N/A with reason: out of scope | N/A_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no ADIF-specific addition; all ordinary guards remain applicable |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_active_session_state.py` |
| literalTokensReviewed | dispatch-ready status, first-section envelope, Source Verification columns, ADIF query, gate IDs and `WORKER_MUST_NOT_COMMIT` |
| gateRunPurpose | confirmation after source read-ahead; authoring and final release are distinct gates |
| claimBoundary | checker shape review does not prove a future worker read or complied |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R1 scope and HTML choice | roadmap decision | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | Work Plan R0/R1, D009-D011, Q001 | selected HTML and R1 contract | operator/Local | ACCEPT |
| existing UI form | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `DEFAULT_REQUEST`, `LABELS`, submit, preview/actions | `ArtifactExportPanel` | cvf-web component | ACCEPT |
| Work Transfer embedding | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx` | export action, lines 261-275 | `ArtifactExportPanel initialRequest` | cvf-web page | ACCEPT |
| source/effect boundary | accepted review | `docs/reviews/CVF_CVF_NCR_R0_W02_HTML_DOWNSTREAM_WORKER_RETURN_2026-09-26.md` | Local Reviewer Disposition | port and conditional file/log effects | Local reviewer | ACCEPT_BOUNDED |
| accepted copy candidate | accepted review | `docs/reviews/CVF_CVF_NCR_R1_W00_HTML_UX_CONTRACT_WORKER_RETURN_2026-09-26.md` | Effect/Unknown Disclosure And Refusal Design; Local Reviewer Disposition | four repaired bilingual lines; no pilot approval | Local reviewer | ACCEPT_BOUNDED |
| focused UI tests | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | `describe('ArtifactExportPanel')` | mocked fetch and language toggle | cvf-web test | ACCEPT |
| UI design owner | design standard | canonical UI contract `DESIGN.md` | form workflow, state and error guidance | design contract | CVF UI owner | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Exact packet names | `rg --files docs/baselines docs/work_orders docs/reviews` before authoring found no `CVF_NCR_R1_W01` packet | NEW_PATHS |
| Existing owner | current Work Transfer page embeds export panel; no new UI owner is requested | REUSE |
| Corpus completeness | only named files read; no complete Web/source inventory claimed | NOT_APPLICABLE_WITH_REASON |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/dispatch author |
| Provider or surface | private CVF workspace |
| Session or invocation | CVF-NCR-R1-W01 authoring, 2026-09-26 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, Git, ADIF resolver, scaffold and local gates |
| Target paths | this baseline and paired R1/W01 work order |
| Allowed scope source | operator next-tranche instruction and selected roadmap R1 |
| Before status evidence | clean worktree at `cfc1cbb6d` |
| After status evidence | new baseline and work order pending material commit |
| Diff evidence | exact two-path dispatch artifact set; continuity follows material commit |
| Approval boundary | Local authoring; operator retains effect, data and expense |
| Claim boundary | UI source/test copy dispatch, no UI interaction or pilot effect |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `cvf-ncr-r1-w01-dispatch-author-20260926` |
| Expected manifest | this baseline and paired work order |
| Actual changed set | verify before commit |
| Manifest delta | PENDING_FINAL_CHECK |
| Deletion or rename disposition | N/A with reason: none planned |

## Claim Boundary

This baseline authorizes one internal worker to implement the accepted UX copy
in the existing HTML export component and focused test. It does not authorize
an actual walkthrough, export/evaluate call, route/config/provider change,
pilot, publication or production claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet only.
