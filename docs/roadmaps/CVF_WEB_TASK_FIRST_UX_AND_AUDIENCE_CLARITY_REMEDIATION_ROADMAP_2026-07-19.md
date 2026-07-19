# CVF Web Task-First UX And Audience Clarity Remediation Roadmap

Memory class: governed-roadmap

Status: ACTIVE_T3_PACKET_AUTHORIZED

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
leaving exact build identity and packaging mechanism unresolved. T2 packet
authoring is released.

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

Rewrite `/help`, `/governance/knowledge`, `/knowledge/intake`, `/artifacts`, and
`/work-transfer` around outcomes. Use Vietnamese-first labels on Vietnamese
surfaces, retain technical terms secondarily, and show the sequence from source
to review to handoff.

### T3 - Home, Onboarding, Chrome, And Density

Shorten first-run onboarding, expose the home value proposition immediately,
move settings/version controls out of primary attention, and reduce repeated
explanatory cards while retaining warnings at the point of action.

### T4 - Browser Acceptance And Roadmap Closure

Run current source on localhost and inspect desktop, tablet, and mobile in dark,
light, and a non-default accent. Check navigation, focus, overflow, primary
actions, loading/empty/error states, and audience disclosure. Hosted deploy and
public export remain separate later batches.

## Acceptance Criteria

- [ ] A first-time user can identify the product value and next action without
  understanding SOT3, MAO, handoff, or commit vocabulary.
- [ ] All current routes remain reachable.
- [ ] Exact governance and continuity detail remains available to the advanced
  audience without dominating ordinary-user views.
- [ ] Vietnamese surfaces avoid unexplained English fragments.
- [ ] Primary actions appear before repeated explanatory prose.
- [ ] Local browser evidence covers desktop, tablet, mobile, dark, light, and a
  non-default accent.
- [ ] Focus and navigation are keyboard-usable.
- [ ] Hosted freshness is not inferred from local UI success.
- [ ] No runtime/provider/public/deployment claim is made without its own packet.

## Verification / Evidence

- focused tests for every changed component or page;
- `npm run typecheck` or the package-equivalent TypeScript command;
- production build from the cvf-web package;
- governed file-size guard;
- browser screenshots from `http://localhost:3000` using current source;
- reviewer recomputation of visible labels, primary actions, responsive
  behavior, and advanced-detail access;
- exact `git diff --name-status`, no staged residue, and unchanged worker HEAD.

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
| gateRunPurpose | confirm roadmap structure and T2 packet authority before packet creation |
| claimBoundary | machine compliance confirms structure; the accepted UX audit supports remediation decisions |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: implementation, browser acceptance, hosted deployment, and public-sync
require separate reviewed batches. This roadmap is private planning authority.

## Claim Boundary

T1, T1P, and T2 are closed with bounded evidence. This roadmap now authorizes
T3 packet creation only. It does not itself implement T3 or authorize provider
calls, deployment, public export, production mutation, or continuous-projection
execution.
