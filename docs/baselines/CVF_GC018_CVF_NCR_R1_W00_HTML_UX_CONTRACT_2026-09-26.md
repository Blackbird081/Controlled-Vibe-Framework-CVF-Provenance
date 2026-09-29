# CVF GC-018 Baseline - CVF-NCR-R1-W00 HTML Work Transfer UX Contract

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Batch ID: CVF-NCR-R1-W00

Dispatch base head: `c7da7e767a94ca8ef1e846edddc5515c4ee960a7`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator for pilot data/effect/expense; Local for source and design disposition

Reviewer owner: Local orchestrator/reviewer, distinct from worker

Worker target: shared-workspace `INTERNAL_AGENT` UX/contract-mapping role

## Purpose

Authorize one documentation-only R1 design slice for the selected HTML review
packet in the existing Work Transfer UI. The worker maps the current user flow
and proposes the smallest comprehensible, effect-aware UX contract. No UI
interaction, route call, implementation, configuration read, or pilot occurs.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-R1-W00 --title "HTML Work Transfer UX Contract" --date 2026-09-26 --base c7da7e767a94ca8ef1e846edddc5515c4ee960a7 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit internal worker profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | bounded R1 design authority, inherited W00-W02 evidence, exact one-file worker return |
| checkerReadAheadConfirmation | dispatch-quality, envelope, gate-to-role, ADIF, active-state and governed read-ahead sources inspected before authoring |
| docOnlyNewFields | existing-state flow, proposed UX copy/contract, effect disclosure and refusal, support/unknown matrix |
| claimBoundary | scaffold/dispatch shape only; no UI, runtime or usability proof |

## Authorization / Decision

The operator instructed Local to continue to the next roadmap tranche and stop
at a work order for manual relay. The selected HTML consumer was accepted in
R0/W00; W01 profiled the first receipt hop and W02 mapped the downstream
source effects. R1 can map and improve the user contract without resolving the
operator's open Q001 data/effect/expense choices or submitting the form.

## Scope

Allowed: read the accepted W00-W02 packets, selected roadmap R1/D008-D011,
`DESIGN.md`, existing Work Transfer page and HTML export panel, relevant
operating-model entry points, and only named supporting source needed to map
states and visible copy. Produce one pending design return containing an
existing-flow inventory, reuse/change/defer map, goal-to-evidence fields,
effect/unknown disclosure and refusal proposal, error/recovery copy, initial
support matrix, and a bounded implementation/walkthrough recommendation.

Forbidden: UI/browser interaction, form submission, API/network/provider call,
raw configuration or ledger data, Web/source/test edit, dependency install,
new dashboard/chooser/approval owner, guide or video production, public or
deployment action, worker commit, and changes to the 52-deferred lane.

Maximum worker write set:
`docs/reviews/CVF_CVF_NCR_R1_W00_HTML_UX_CONTRACT_WORKER_RETURN_2026-09-26.md`
only. Local owns review, correction, commit and continuity.

## Baseline Invariants

1. Use the already-wired `ArtifactExportPanel` in Work Transfer; do not claim
   the UI form is missing or reselect a pilot candidate.
2. Label source-reading/design simulation separately from an actual agent
   UI-interaction walkthrough. The latter is `NOT_RUN` here; real-user
   usability remains `NOT_EVALUATED`.
3. The HTML route can conditionally send source content via the receipt
   helper. The downstream client fallback `8000` differs from the FastAPI
   server's documented `8100`. Actual URL, data, retention, latency and cost
   remain open; proposed UI copy must disclose uncertainty, not invent safety.
4. P06/P08 stay `PARTIALLY_CONFIRMED_NEEDS_EVIDENCE`. This design order does
   not implement validation or secret-scanning tests.
5. No L1/L2/L3, R1 exit, pilot readiness, accessibility conformance or
   non-coder comprehension claim follows from a static design packet.
6. D010 overall CVF user guide and later video are separate scope; no media
   artifact is produced here.

## Verification / Evidence

The worker must provide exact source locators for the existing UI states and
route-related effects, then mark every proposal as proposal. Acceptance is a
reviewable design choice with one consumer and no duplicate owner, not proof
that the user journey was exercised. Record `UNKNOWN` where current profile or
runtime behavior is unmeasured.

## Dependency Release Evidence

| Dependency | Current evidence | Disposition |
|---|---|---|
| Pilot consumer | roadmap D009 and accepted W00 return at `c7b7a2c721a3388a738eb2b2633fc4414cf1dff3` | ACCEPT: one HTML consumer selected |
| First-hop profile | accepted W01 at `d9b43a6f6deff7fb19710b5a9a4f50bf2a6015b6` | ACCEPT_BOUNDED: source only |
| Downstream effects | accepted W02 at `c638f2ece` | ACCEPT_BOUNDED: actual reachability/retention open |
| CI and release | local HEAD is 25 commits ahead of `origin/main`; recent remote workflow failures are at `4567d750087d47f369939a0e9891ca6fcb596034`, not this local HEAD | DEFER: no CI/release claim in this design order |
| Dispatch continuity source | `CVF_SESSION/state/entries/cvfNcrR1W00HtmlUxDispatch20260926.json` was created in the dispatch continuity commit | ACCEPT: include this exact path in the work-order routing manifest |
| Real UI/pilot profile | actual endpoint, data/effect/expense and UI walkthrough unresolved | DEFER: no effect authorized |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | shared private workspace and exact return | source/design documentation only; no commit | selected roadmap and accepted W00-W02 | local Git/file handoff | CONTRACT_ONLY |
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
| UI design owner | design standard | canonical UI contract `DESIGN.md` | form workflow, state and error guidance | design contract | CVF UI owner | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Exact packet names | `rg --files docs/baselines docs/work_orders docs/reviews` before authoring found no `CVF_NCR_R1_W00` packet | NEW_PATHS |
| Existing owner | current Work Transfer page embeds export panel; no new UI owner is requested | REUSE |
| Corpus completeness | only named files read; no complete Web/source inventory claimed | NOT_APPLICABLE_WITH_REASON |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/dispatch author |
| Provider or surface | private CVF workspace |
| Session or invocation | CVF-NCR-R1-W00 authoring, 2026-09-26 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, Git, ADIF resolver, scaffold and local gates |
| Target paths | this baseline and paired R1/W00 work order |
| Allowed scope source | operator next-tranche instruction and selected roadmap R1 |
| Before status evidence | clean worktree at `c7da7e767` |
| After status evidence | new baseline and work order pending material commit |
| Diff evidence | exact two-path dispatch artifact set; continuity follows material commit |
| Approval boundary | Local authoring; operator retains effect, data and expense |
| Claim boundary | design-only dispatch, no UI/pilot effect |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `cvf-ncr-r1-w00-dispatch-author-20260926` |
| Expected manifest | this baseline and paired work order |
| Actual changed set | verify before commit |
| Manifest delta | PENDING_FINAL_CHECK |
| Deletion or rename disposition | N/A with reason: none planned |

## Claim Boundary

This baseline authorizes one internal worker to prepare a static UX contract
for the selected HTML flow. It does not authorize an actual walkthrough,
export/evaluate call, provider/live proof, source change, pilot, publication or
production claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet only.
