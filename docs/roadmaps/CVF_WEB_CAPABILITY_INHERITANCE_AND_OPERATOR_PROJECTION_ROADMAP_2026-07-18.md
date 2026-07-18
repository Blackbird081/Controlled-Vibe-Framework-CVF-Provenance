# CVF Web Capability Inheritance And Operator Projection Roadmap

Memory class: FULL_RECORD

Status: CVF_WEB_INHERITANCE_T3A_DISPATCH_READY

docType: roadmap

Date: 2026-07-18

Roadmap ID: CVF-WEB-INHERITANCE

## Authorization / Decision

The operator observed that CVF has gained SOT3, downstream SOT application,
MAO operational adoption, and Four-Surface control-boundary capability while
cvf-web appears not to inherit or expose much of that value. The operator
authorized a clean audit and continuation packet after SOT3-CVF-PROJ-T0.

T0 through T2 are independently closed. Direct T3 implementation is not
source-safe because the MAO operator projection has no persistent evidence
or Web caller seam. T3A is dispatch-ready to decide that seam; T3B and T4-T5
remain parked.

## Purpose

Determine, from current source, which accepted CVF capabilities are:

- package dependencies of cvf-web;
- wired into a Web/API runtime path;
- projected into the runtime-module registry;
- visible to an operator through a page or read model;
- present only in a sibling application; or
- absent from cvf-web with an explicit adoption decision still required.

Then upgrade cvf-web through bounded, dependency-ordered tranches without
copying sibling code blindly or claiming that a package dependency is an
operator-visible product capability.

## Scope / Target / Owner Boundary

Primary target:
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`.

Current CVF capability owners used as comparison evidence include SOT3 runtime
packages, MAO execution/control packages, accepted SOT3 application reviews,
and the Four-Surface control-boundary adaptation closure.

T0 owns a read-only inheritance ledger and worker return. T1-T5 each require a
fresh GC-018, source verification, work order, independent review, and material
commit. Browser proof, live provider calls, public-sync, push, and production
remain separately governed.

## Design Control Gate

`DESIGN.md` is the canonical visual contract for any later UI work. T0 performs
no UI mutation. Later pages must use existing cvf-web components and tokens,
preserve current routes/auth/APIs/stores, avoid new UI libraries without
authorization, and verify desktop, tablet, mobile, keyboard, loading, empty,
and error states.

## Non-Goals

- no Web source, component, route, package, test, or README implementation in T0;
- no browser, provider, live, network, public-sync, push, or production action;
- no sibling application source copy;
- no MAO worker launch, queue, daemon, or autonomous execution;
- no claim that every accepted CVF capability should become a Web feature.

## Starting Evidence

| Surface | Current source fact | Initial implication |
|---|---|---|
| cvf-web package dependencies | `cvf-refinery`, `cvf-truth-kernel`, and `cvf-truth-flow` are file dependencies | SOT3 packages are inherited at build/runtime dependency level |
| SOT3 adapter and execute route | real Refinery, Kernel, and Flow owners are composed and the execute path fails closed before provider execution | SOT3 backend integration exists |
| page inventory | 41 current `page.tsx` files have zero SOT3, MAO, Controlled Quotation, freeze, or recall matches | operator visibility is absent for the audited new capabilities |
| runtime-module registry | Execution Plane is `NOT_EXPOSED`; Control and Learning are `PARTIAL_INHERITED`; SOT3 packages are not listed | registry projection is stale or incomplete relative to source |
| MAO package roots | execution and control package roots export MAO surfaces | MAO exists in current source but cvf-web has no dependency or operator surface |
| SOT application | accepted reviews prove a sibling service chain and Controlled Quotation flow | adoption must be a deliberate boundary decision, not an assumed in-repo Web feature |
| cvf-web README | version 1.6.0 and dated quality/changelog sections predate July SOT3 and MAO work | operator/developer documentation is stale |

## Tranche Plan

| Tranche | Objective | Output boundary | Release condition |
|---|---|---|---|
| CVF-WEB-INHERITANCE-T0 | capability-to-Web inheritance audit | terminal ledger covering dependencies, runtime wiring, registry, pages, docs, and sibling-only capabilities | independent review accepts every row and route |
| CVF-WEB-INHERITANCE-T1 | runtime-module and dependency truth correction | source-backed registry entries and tests for currently inherited capability families | registry matches real dependency/wiring state without runnable overclaim |
| CVF-WEB-INHERITANCE-T2 | SOT3 operator evidence projection | read-only status/evidence surface for activation mode, outcome, identifiers, and bounded diagnostics | no raw knowledge or secret leakage; focused tests and build pass |
| CVF-WEB-INHERITANCE-T3 | MAO operator readout projection | read-only run/evidence/milestone/liveness projection from existing MAO owners | no worker launch, provider call, queue, or autonomous mutation |
| CVF-WEB-INHERITANCE-T3A | MAO Web adoption and source-seam decision | terminal source matrix for dependency, persistence/replay, liveness, milestones, configuration, privacy, and caller ownership | one source-backed T3B route or bounded defer; no guessed adapter or duplicated semantics |
| CVF-WEB-INHERITANCE-T3B | MAO operator readout implementation | only the implementation boundary released by accepted T3A evidence | T3A accepted with exact source owners, dependency release, and allowed scope |
| CVF-WEB-INHERITANCE-T4 | Controlled Quotation and sibling-app adoption decision | explicit `LINK`, `ADAPT`, `PORT_BOUNDED`, or `DEFER_WITH_REASON` decision before implementation | source/provenance boundary and duplicate-logic risk resolved |
| CVF-WEB-INHERITANCE-T5 | Web information, QA, and roadmap closure | README/help/version projection plus typecheck, tests, build, and UI QA for implemented tranches | all accepted claims match tested routes and public disposition is explicit |

## Work Plan

1. Freeze the current cvf-web capability/dependency/page inventory in T0.
2. Separate dependency, backend wiring, registry projection, and operator UI as
   four independent evidence dimensions.
3. Correct the registry before adding new operator pages.
4. Expose SOT3 evidence read-only before considering broader workflow control.
5. Project MAO evidence without releasing worker launch or live execution.
6. Decide how the sibling Controlled Quotation application relates to cvf-web
   before copying or adapting any service chain.
7. Refresh Web-facing information and run full QA only after accepted source
   changes exist.

## Acceptance Criteria

- AC-01: T0 inventories every capability family in its frozen manifest.
- AC-02: each row distinguishes package dependency, backend runtime wiring,
  registry projection, operator surface, and documentation projection.
- AC-03: SOT3 is not classified as absent because its current backend path is
  source-proven.
- AC-04: MAO is not classified as Web-inherited merely because package owners
  exist outside cvf-web.
- AC-05: sibling SOT application evidence is not promoted into cvf-web source
  authority or copied without a T4 decision.
- AC-06: runtime-module registry claims match current package and caller facts.
- AC-07: later UI follows `DESIGN.md` and preserves protected runtime contracts.
- AC-08: no live-governance or public claim is made from mock or static UI proof.
- AC-09: every tranche closes independently before the next is released.

## Verification / Evidence

T0 requires direct reads and repository searches only. Later implementation
tranches require focused tests, cvf-web typecheck/build, governed file-size
enforcement, and relevant route/component tests. Browser QA is required only
for changed UI and remains separately dispatched. Any release-quality
governance claim requires the canonical live release gate and an available
operator-supplied key; T0 makes no such claim.

## Dependency And Sequence Control

- SOT3-CVF-PROJ-T0 closed at material commit `9d8305942`.
- CVF-WEB-INHERITANCE-T0 may now run as a no-commit audit.
- T0 is independently accepted with reviewer repairs. T1 is independently
  accepted at material commit `b186df669`. T2 is independently accepted with
  reviewer repairs at material commit `609edffbe`. T3A is dispatch-ready;
  T3B and T4-T5 remain parked.
- T3A is required because the existing MAO operational projection is a pure,
  caller-supplied in-memory owner with no CLI, MCP, UI, or runtime caller;
  the durable run store replays event-ledger state but does not persist or
  reconstruct the separate evidence ledger required by that projection.
- SOT3-CVF-PROJ-T1 through T4 remain parked while this cross-product audit
  determines overlap and ordering.
- MAO-OA-T6B and SCLP-X-T3 remain parked under their existing conditions.

## Current Runtime Freshness Verification

Current source was re-read on 2026-07-18. cvf-web directly depends on the three
SOT3 packages and composes them through its knowledge adapter and execute path.
The Execution Plane and its MAO root exist in current source but the execution
package is not a cvf-web dependency. These facts supersede older catalog or
README absence language. No provider registry, model selection, or provider
capability change is proposed by this roadmap.

## Reverse Architecture Projection Matrix

| Source capability | Web projection question | T0 evidence owner | Later owner |
|---|---|---|---|
| SOT3 Refinery/Kernel/Flow | backend-only, registry-visible, or operator-visible | cvf-web dependency, adapter, route, page inventory | T1/T2 |
| MAO operational adoption | dependency, read-only evidence, or no inheritance | MAO package roots plus cvf-web package/registry/page facts | T1/T3 |
| Controlled Quotation | sibling link, bounded adapter, port, or defer | accepted SOT3-APP reviews plus cvf-web absence search | T4 |
| Four-Surface control boundary | already represented, partially inherited, or missing | accepted adaptation review plus Web source inventory | T0 routing; later packet if valuable |
| Web documentation | current or stale relative to accepted capability | README/version/changelog direct read | T5 |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | cvf-web API, registry, pages, and accepted package owners | audit only in T0; no mutation or execution authority | source-backed ledger | fresh tranche required for each change | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no new Web adapter in T0 | no ingress, auth, approval, receipt, raw-data, mutation, or public behavior | zero adapter change | remains parked | `N/A_WITH_REASON` |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`frontend`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class frontend --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | Status; Authorization / Decision; Purpose; Scope / Target / Owner Boundary; Design Control Gate; Starting Evidence; Tranche Plan; Work Plan; Acceptance Criteria; Verification / Evidence; Dependency And Sequence Control; Reverse Architecture Projection Matrix; Dual Agent Surface Matrix; ADIF Defect Registry Disclosure; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation after direct source and checker read-ahead |
| claimBoundary | structural roadmap conformance does not prove Web inheritance or user value |

## Epistemic Process Block

### Expected Result / Prediction

cvf-web likely contains real SOT3 backend inheritance but lacks registry and
operator projection, while MAO and Controlled Quotation remain outside its
current dependency/runtime boundary.

### Evidence Comparison

Initial source reads support that mixed posture. T0 must replace the initial
view with a terminal capability-by-capability ledger.

### Contradiction Or Gap Disposition

Treat differences as inheritance/projection gaps. Do not reopen accepted SOT3
or MAO implementation and do not infer that every capability belongs in Web.

### Claim Update

T0 audit, the bounded T1 registry correction, and the bounded T2 SOT3 evidence
projection are accepted. T3A must resolve the current MAO caller and evidence
seam gap before T3B can be authored.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | CVF-WEB-INHERITANCE roadmap authoring, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | source reads, repository search, apply_patch, governance gates |
| Target paths | this roadmap and paired T0 dispatch packet |
| Allowed scope source | operator instruction to assess why cvf-web did not inherit recent CVF upgrades |
| Before status evidence | clean worktree at session-sync HEAD `36041a985` |
| After status evidence | exact three-path T0 dispatch set pending validation and commit |
| Diff evidence | material diff captured before commit |
| Approval boundary | roadmap and T0 read-only audit dispatch only |
| Claim boundary | no Web/source/test/runtime/provider/live/browser/public/push/production mutation |
| Agent type | dispatcher |
| Invocation ID | `cvf-web-inheritance-roadmap-dispatch-2026-07-18` |
| Expected manifest | roadmap; T0 GC-018; T0 work order |
| Actual changed set | exact three-path dispatch set before commit |
| Manifest delta | MATCH expected after verification |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap is private provenance planning. Public-safe export needs a
separate public-sync authorization and artifact set.

## Claim Boundary

This roadmap records accepted T0 inventory, T1 registry correction, and T2
read-only SOT3 evidence projection. It releases the documentation-only T3A
source-seam decision packet only. It does not authorize T3B implementation,
SOT3 or MAO execution, sibling-source copying, browser or live proof,
public-sync, push, production readiness, or universal inheritance claims.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | this roadmap | `Status: CVF_WEB_INHERITANCE_T3A_DISPATCH_READY` | PASS |
| Baseline status | T3A GC-018 baseline | `Status: DISPATCH_READY` | PASS |
| Work order status | T3A work order | `Status: DISPATCH_READY` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_WEB_INHERITANCE_T2_COMPLETION_REVIEW_2026-07-18.md` | T2 dependency accepted at `609edffbe` | PASS |
| Registry JSON | corpus registry generated aggregate | existing cvf-web `src/` scope coverage and aggregate drift check | PASS |
| Registry Markdown | corpus registry read model | existing cvf-web `src/` scope coverage | PASS |
| External evidence digest | N/A with reason: repository-local evidence only | none | N/A with reason |
| System loop interlock | N/A with reason: no loop owner changed | none | N/A with reason |
| Session continuity | protected session surfaces | separate session-sync commit | N/A with reason |
