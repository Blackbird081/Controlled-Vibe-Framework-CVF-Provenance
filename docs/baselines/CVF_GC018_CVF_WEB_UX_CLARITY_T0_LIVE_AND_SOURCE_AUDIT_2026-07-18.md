# CVF GC-018 Baseline - CVF Web UX Clarity T0 Live And Source Audit

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: CVF-WEB-UX-T0

Dispatch base head: `7051eb87d`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: Codex reviewer/closer

Worker target: delegated audit worker

## Purpose

Authorize one evidence-only audit of the public CVF Web information
architecture, Vietnamese/English language clarity, internal-governance leakage,
stale read models, and visual hierarchy. The audit must turn live observations
and direct source reads into a bounded redesign backlog; it must not implement
the redesign.

## Scope / Applies To

Applies to the public routes `/home`, `/workspace`, `/help`,
`/governance/knowledge`, `/knowledge/intake`, `/artifacts`, and
`/work-transfer`, plus the shared sidebar and compact header. Desktop evidence
is required; responsive behavior may be recorded only when the worker can
inspect it directly.

## Target / Source

- Live target: `https://cvfcoding.vn`.
- Canonical design contract: `DESIGN.md`.
- Current implementation: cvf-web route, navigation, language, and read-model
  sources verified in the paired work order.
- Operator screenshots are reference evidence, not CVF source authority.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-WEB-UX-T0 --title "CVF Web UX Clarity And Information Architecture Live Audit" --date 2026-07-18 --base 7051eb87d --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | web-ui-dashboard plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with source-verified audit scope, live routes, two-output manifest, role boundary, and no-mutation acceptance criteria. |
| checkerReadAheadConfirmation | Dispatch-quality, ADIF disclosure, operation-trace, handoff-boundary, lifecycle-hygiene, structural-completeness, and packet-authority checker sources were inspected before dispatch. |
| docOnlyNewFields | Audit matrix fields and redesign-disposition vocabulary are new documentation-only fields. |
| claimBoundary | Dispatch provenance only; no runtime, hosted-success, provider, redesign-completion, or public-readiness claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0014, ADIF-0015,
ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 10 |
| Returned defects | ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033 |
| Disclosed defectIds | ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033 |
| Dispatch impact | Use the canonical Web/UI task map, DESIGN contract, clean evidence boundary, and no-commit reviewer conversion. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | Purpose, Scope / Applies To, Target / Source, Source Verification Block, Agent Handoff Contract Control Block, Reviewer Closure Conversion, Public Export Disposition, and exact operation-trace labels |
| gateRunPurpose | Confirmation and dispatch evidence after source verification and packet authoring. |
| claimBoundary | Read-ahead covers the two dispatch artifacts only; worker outputs require their own checker-source read-ahead. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Vietnamese UI must be natural, short, and avoid technical jargon on non-coder surfaces. | LITERAL_INVARIANT | canonical-contract:DESIGN.md | Section 8, Accessibility & Language | Vietnamese UI language rules | CVF design contract | ACCEPT |
| Shared sidebar currently mixes Vietnamese and English product labels. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` | symbol definition line 48; navigation definitions lines 153-176 | `Sidebar` | shared dashboard navigation | ACCEPT |
| Workspace read model retains a V19 fallback and WWU-T2 source labels. | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts` | symbol definition line 261; fallback/source rows lines 267-278 | `getCvfWorkspaceReadModel` | workspace server read model | ACCEPT |
| Help content exposes Agent Chat, Self-UAT, Multi-Agent, SOT3, and MAO terminology. | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/help-content.ts` | symbol definition line 41 | `HELP_CONTENT` | help content model | ACCEPT |
| Artifact export panel owns Vietnamese review-package copy. | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | symbol definition line 208 | `ArtifactExportPanel` | artifact export panel | ACCEPT |
| Header owns the Tweaks, language, and theme controls. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/CompactHeader.tsx` | symbol definition line 65 | `CompactHeader` | shared compact header | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Target artifact existence | All four planned baseline, work-order, audit, and return paths returned `False` before authoring. | NEW_PATHS_CONFIRMED |
| Batch-token search | `rg -n "CVF-WEB-UX-T0|CVF Web UX Clarity" docs CVF_SESSION` returned no prior batch. | NO_COLLISION |
| Collision decision | Open a new T0 audit batch; do not reuse or overwrite prior CVF Web inheritance artifacts. | ACCEPT |

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | CONFIRMED by dispatcher; worker must reread before audit. |
| UI claim boundary | Audit and redesign backlog only. No code, data, route, runtime, deployment, provider, or public-readiness mutation is authorized. |

## Decision / Baseline / Proposed Tranche

Decision: dispatch one T0 audit-only tranche. Baseline: current public Web and
source at dispatch base `7051eb87d`. Proposed later work: reviewer must use the
accepted audit to decide whether a redesign roadmap is warranted; no T1
implementation is released here.

## Evidence / Verification

Evidence must include terminal route rows, visible-text or secret-safe
screenshot observations, source-owner citations, DESIGN comparisons, gate
output, exact changed set, unchanged HEAD, and nothing staged.

## Claim Boundary

This baseline authorizes live read-only observation, screenshots without
secrets, direct source inspection, and two private review outputs. It forbids
form submission, provider calls, credentials, production mutation, source
edits, dependency changes, public-sync edits, commits, pushes, and deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private UX audit dispatch. A later accepted redesign packet must decide
whether any public artifact or implementation tranche is authorized.
