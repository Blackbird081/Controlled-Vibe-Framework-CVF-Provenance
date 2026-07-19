# CVF Web Task-First UX And Audience Clarity Remediation Roadmap

Memory class: governed-roadmap

Status: CLOSED_PASS_BOUNDED

Date: 2026-07-19

Text Encoding Exception: Vietnamese labels are permitted only in user-facing
copy contracts and browser evidence.

## Purpose

Turn the accepted CVF Web UX audit into a staged remediation that makes the Web
surface understandable within one short scan while preserving deeper technical
truth for developers, agents, reviewers, and operators.

## Authorization / Decision

The operator authorized continued UX remediation after the localhost browser
audit. CVF-WEB-UX-T0 is closed bounded at completion commit `93c2663a6` with
final session sync `b9717a7f7`. T1 closed bounded at `d4e6e48a0`. T1P closed
bounded at `45d505836`, confirming visible hosted/current output drift while
leaving exact build identity and packaging mechanism unresolved. T2 closed
bounded at `bb1418554`. T3 is closed bounded by its reviewer completion; T4
browser-acceptance packet authoring is now authorized.

## Scope / Target / Owner Boundary

Target: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`.

Product owner: operator. Dispatch and closure owner: CVF orchestrator/reviewer.
Worker owns only the paths named by the current tranche work order.

The roadmap preserves current routes, APIs, stores, parsers, governance logic,
and evidence. It changes information hierarchy, audience routing, language,
and visual scanning cost in bounded tranches.

## Scope

- task-first navigation with fewer peer concepts;
- ordinary-user versus advanced reviewer/operator presentation;
- Vietnamese-first plain language on user routes;
- progressive disclosure of SOT3, MAO, handoff, commit, and receipt detail;
- shorter onboarding and faster access to primary actions;
- responsive, theme, accent, and keyboard verification through localhost;
- hosted-freshness diagnosis kept separate from UI source acceptance.

## Non-Goals

- no API, provider, database, policy, role, or evidence-contract redesign;
- no removal of governed technical truth;
- no fake readiness state when source data is unavailable;
- no deployment, public-sync, or production mutation inside implementation
  tranches;
- no new UI framework or broad design-system replacement;
- no claim that local browser proof equals hosted deployment freshness.

## Design Control Gate

`DESIGN.md` is canonical. Every tranche must preserve the app-shell contract,
task hierarchy, compact operational typography, token-first styling,
responsive priority, visible focus, natural Vietnamese, and progressive
disclosure. Current screenshots are defect evidence, not a design template.

### Audience Layers

| Layer | Default content | Deeper content route |
|---|---|---|
| End user | goal, current status, primary action, plain-language recovery | optional details |
| Developer | setup, architecture, extension seams, linked source | technical documentation |
| External agent | logic, catalog, authority, evidence locators | machine-readable technical context |
| Reviewer/operator | exact state, handoff, receipts, commits, drift | advanced operations |

## Audit-To-Roadmap Trace Matrix

| Audit finding | Roadmap control | Tranche |
|---|---|---|
| dense sidebar with mixed peer concepts | five task-oriented navigation groups and advanced disclosure | T1 |
| `/workspace` exposes continuity internals by default | ordinary summary plus advanced exact-state view | T1 |
| hosted `/workspace` differs from current source | independent packaging/freshness diagnosis | T1P |
| help and knowledge routes use internal names | outcome-first copy and terminology contract | T2 |
| intake, artifact, and transfer routes feel disconnected | one knowledge-to-review-to-handoff journey | T2 |
| onboarding obscures the outcome-first home | short state-aware onboarding | T3 |
| global chrome and repeated cards dominate | compact chrome and reduced prose/card density | T3 |
| visual acceptance previously relied on hosted screenshots | localhost multi-viewport/browser acceptance | T4 |

## Work Plan

### T1 - Navigation And Workspace Audience Separation

Disposition: `CLOSED_PASS_BOUNDED` at material commit `d4e6e48a0`.

Reorganize the sidebar around user jobs while preserving all existing routes.
Make `/workspace` default to plain-language operational summaries and place raw
mode, handoff, dispatch, commit, path, and lane detail under an explicit
advanced section. Add focused component tests. No deployment work.

### T1P - Hosted Packaging And Freshness Diagnosis

Disposition: `CLOSED_PASS_BOUNDED` at material commit `45d505836`. Visible
hosted/current output drift is accepted; exact hosted build identity and
packaging mechanism remain `INSUFFICIENT_EVIDENCE`. Deployment remains a
separate parked lane.

After T1 source closure, compare current-source build artifacts with hosted
state loading. Identify build inclusion, repository-root resolution, and
deployment cache/freshness causes. Keep UI presentation and deployment repair
as separate claims and commits.

### T2 - Language And Guided Knowledge Journey

Disposition: `CLOSED_PASS_BOUNDED` at material commit `bb1418554` after
reviewer scope, localization, evidence, and test repairs.

Rewrite `/help`, `/governance/knowledge`, `/knowledge/intake`, `/artifacts`, and
`/work-transfer` around outcomes. Use Vietnamese-first labels on Vietnamese
surfaces, retain technical terms secondarily, and show the sequence from source
to review to handoff.

### T3 - Home, Onboarding, Chrome, And Density

Disposition: `CLOSED_PASS_BOUNDED` through
`docs/baselines/CVF_GC018_CVF_WEB_UX_T3_HOME_ONBOARDING_CHROME_AND_DENSITY_2026-07-19.md`
and
`docs/reviews/CVF_WEB_UX_T3_COMPLETION_2026-07-19.md`.

Shorten first-run onboarding, expose the home value proposition immediately,
move settings/version controls out of primary attention, and reduce repeated
explanatory cards while retaining warnings at the point of action.

### T4 - Browser Acceptance And Roadmap Closure

Disposition: `CLOSED_PASS_BOUNDED`. The first audit, R1, and R2
preserve useful render/width evidence but cannot close. R2 correctly captured
820px persistent-sidebar behavior and a 767px drawer pair, but its claimed
preferences-open image contains no open panel, its own anchor is `NOT_FOUND`,
and named focus scenarios do not identify or reach the required targets. R3
adds valid Preferences, accent, drawer, and partial Home evidence, but its Home
anchor belongs to onboarding, Workspace omits the closing transition, Knowledge
targets a step tab, and command evidence remains non-terminal. R4 is
dispatch-ready through
`docs/baselines/CVF_GC018_CVF_WEB_UX_T4_BROWSER_ACCEPTANCE_AND_ROADMAP_CLOSURE_2026-07-19.md`
and
`docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T4_R4_FINAL_INTERACTION_AND_COMMAND_PROOF_2026-07-20.md`.
R4 supplies terminal JSON and command records, but all three submitted terminal
PNGs visibly retain the onboarding overlay and therefore contradict their
claimed result anchors. The narrow screenshot-state binding repair is released
through
`docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T4_R5_SCREENSHOT_STATE_BINDING_REPAIR_2026-07-20.md`.
R5 closes the final visual contradiction with three reviewer-opened,
overlay-free PNGs whose post-write SHA256 values recompute exactly. Final T4
acceptance and the cross-tranche closure diff are recorded in
`docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-20.md`.

Run current source on localhost and inspect desktop, tablet, and mobile in dark,
light, and a non-default accent. Check navigation, focus, overflow, primary
actions, loading/empty/error states, and audience disclosure. Hosted deploy and
public export remain separate later batches.

## Acceptance Criteria

- [x] A first-time user can identify the product value and next action without
  understanding SOT3, MAO, handoff, or commit vocabulary.
- [x] All current routes remain reachable.
- [x] Exact governance and continuity detail remains available to the advanced
  audience without dominating ordinary-user views.
- [x] Vietnamese surfaces avoid unexplained English fragments.
- [x] Primary actions appear before repeated explanatory prose.
- [x] Local browser evidence covers desktop, tablet, mobile, dark, light, and a
  non-default accent.
- [x] Focus and navigation are keyboard-usable.
- [x] Hosted freshness is not inferred from local UI success.
- [x] No runtime/provider/public/deployment claim is made without its own packet.

## Verification / Evidence

- focused tests for every changed component or page;
- `npm run typecheck` or the package-equivalent TypeScript command;
- production build from the cvf-web package;
- governed file-size guard;
- browser screenshots from `http://localhost:3000` using current source;
- reviewer recomputation of visible labels, primary actions, responsive
  behavior, and advanced-detail access;
- exact `git diff --name-status`, no staged residue, and unchanged worker HEAD.

## Current Runtime Freshness Verification

| Runtime fact | Source | Disposition |
|---|---|---|
| current-source Web rendered the accepted task-first routes | R1-R5 localhost evidence and T1-T3 focused test/build completions | source-visible and browser-observed bounded |
| Workspace advanced disclosure remains reachable | R5 Workspace PNG and current Workspace page source | source-visible and browser-observed bounded |
| Knowledge unauthenticated compile response remains visible | R5 Knowledge PNG and current compile route source | source-visible and browser-observed bounded |
| hosted build identity is not established by localhost proof | T1P completion and this roadmap claim boundary | separate hosted packet required |
| continuous projection runtime is outside this roadmap | continuous-projection roadmap and this roadmap Non-Goals | packet authoring only may resume after closure |

## Dual Agent Surface Matrix

| Surface class | Intended user | Interface | Authority/risk boundary | Required evidence | Adapter boundary |
|---|---|---|---|---|---|
| INTERNAL_AGENT | reviewer/operator | advanced Web details and governed repo sources | read-only technical truth; no hidden memory authority | source paths, state owners, receipts | existing Web read models |
| EXTERNAL_AGENT_CLI_MCP | external agent or developer tool | linked technical context and machine-readable catalogs | no direct production mutation or authority promotion | source verification and catalog/evidence locators | later source-verified CLI/MCP or documentation seam only |

Disposition: `DOCUMENTATION_ONLY_WITH_REASON` for external CLI/MCP adaptation in
this roadmap. Web UI tranches do not create a new agent runtime adapter.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: operator requirements and accepted CVF audit are already governed inputs |
| Matching local-view guard | N/A with reason: no outside artifact is promoted to authority |
| Owner surface | this roadmap and current CVF Web source |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | audience design does not make an external agent or provider a CVF authority |

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| simplification hides truth | advanced disclosure must retain exact source-backed detail |
| navigation breaks routes | preserve hrefs and add reachability tests |
| Vietnamese becomes literal or verbose | test labels as user jobs and keep actions short |
| large pages worsen maintainability | split same-domain components when size guard advises |
| local success masks stale hosting | T1P owns hosted packaging separately |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | roadmap headings; status; work plan; acceptance criteria; dual-agent surface tokens; public disposition |
| gateRunPurpose | confirm roadmap structure, T3 closure, and T4 packet-authoring authority |
| claimBoundary | machine compliance confirms structure; the accepted UX audit supports remediation decisions |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the closed roadmap proves only private current-source localhost UX.
Hosted deployment, public-sync, and public presentation remain separate work.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | R5 canonical order | status CLOSED_PASS_BOUNDED | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-20.md` | reviewer decision CLOSED_PASS_BOUNDED | PASS |
| Roadmap state | this roadmap | top Status equals CLOSED_PASS_BOUNDED | PASS |
| T1 closure | `docs/reviews/CVF_WEB_UX_T1_COMPLETION_2026-07-19.md` | material commit `d4e6e48a0` | PASS |
| T1P closure | `docs/reviews/CVF_WEB_UX_T1P_COMPLETION_2026-07-19.md` | material commit `45d505836` | PASS_BOUNDED |
| T2 closure | `docs/reviews/CVF_WEB_UX_T2_COMPLETION_2026-07-19.md` | material commit `bb1418554` | PASS_BOUNDED |
| T3 closure | `docs/reviews/CVF_WEB_UX_T3_COMPLETION_2026-07-19.md` | accepted source, tests, build, and browser evidence | PASS_BOUNDED |
| T4 closure | `docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-20.md` | R1-R5 accepted evidence chain | PASS |
| Registry JSON | corpus registry aggregate | generated aggregate drift and changed-path coverage checks PASS | PASS |
| Registry Markdown | corpus registry source/front door | registry checks PASS; no source entry mutation required | PASS |
| External evidence digest | R5 evidence root | SHA256 `78b68c72d25edf2f69b59ea7160cd7991ca34eabf87b8c91a33cb7c2e9c77a54`; `9ea9972c8fc3adaaf97f1377df5d6a1864d390761e8fe06d3286fde56533e68a`; `3a7d9bf71d165c182542e37be168979ff417ef5a37f7d029f460ab07ef1bcfb5` | PASS |
| System loop interlock | no system-loop mutation | UX-only roadmap | N/A with reason |
| Session continuity | active session surfaces | separate session-sync follows material commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| T4-R5-HOME | `docs/reviews/evidence/CVF_WEB_UX_T4_R5_LOCALHOST_2026-07-20/captures.json` | `$[0].verdict` | `PASS` | `PASS` | PASS |
| T4-R5-WORKSPACE | `docs/reviews/evidence/CVF_WEB_UX_T4_R5_LOCALHOST_2026-07-20/captures.json` | `$[1].verdict` | `PASS` | `PASS` | PASS |
| T4-R5-KNOWLEDGE | `docs/reviews/evidence/CVF_WEB_UX_T4_R5_LOCALHOST_2026-07-20/captures.json` | `$[2].verdict` | `PASS` | `PASS` | PASS |

## Claim Boundary

T1, T1P, T2, T3, and T4 are closed with bounded current-source evidence. This
roadmap makes no hosted freshness, deployment, public export, provider/live,
production-readiness, or continuous-projection execution claim.
