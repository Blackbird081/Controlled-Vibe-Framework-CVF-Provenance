# CVF MSEA R81 Workspace Productization Release Candidate Roadmap

Memory class: FULL_RECORD

Status: RC_PASS_BOUNDED

docType: roadmap

Date: 2026-07-09

Owner: Codex

## Authorization / Decision

Operator decision on 2026-07-09: continue with the next CVF-value roadmap, but
do not go deep into a specific downstream use case.

Decision: open R81 as the CVF Workspace Productization Release Candidate lane.
The lane turns the current public-safe and operator-local workspace work into a
small, testable release-candidate surface for CVF itself.

This roadmap does not authorize Policy_Local app logic, legal workflow,
retrieval, Memory/RAG, vectorization, provider/live proof, hosted production
claims, checker retirement, or broad governance refactoring.

## Purpose

Make CVF Workspace usable as a product surface instead of another internal
governance lane.

R81 should answer a narrow product question:

Can a local workspace inherit the right CVF rules, guides, handoff/memory
habits, update flow, and doctor checks from the public-safe core while keeping
provenance-only data private?

## Scope

R81 is scoped to CVF Workspace release-candidate readiness.

In scope:

- define the three-lane product boundary: provenance, public core, and local
  workspace;
- verify that existing project adoption and fresh project bootstrap remain
  repeatable from the local workspace root;
- make rule-pack selection understandable for operator-local, paid-user-safe,
  and public-free modes;
- keep session memory and handoff practices available to workspaces without
  leaking provenance data into public output;
- define a disposable-project smoke proof that does not depend on Policy_Local
  application code;
- produce a small RC checklist that future agents can run before calling the
  workspace flow usable.

Out of scope:

- Policy_Local feature implementation or domain-specific behavior;
- public marketing copy, hosted service claim, or production launch claim;
- new provider/API proof;
- Memory/RAG, retrieval, OCR, vectorization, or corpus ingestion;
- checker deletion, hook severity changes, Fast Lane edits, or R72F retirement
  execution;
- broad historical rename/move sweeps.

## Non-Goals

R81 is not a use-case pilot, legal assistant, hosted platform release, or new
governance framework rewrite.

It does not try to make every workspace perfect. It creates a practical RC
surface with explicit smoke checks and clear stop lines.

## Design Control Gate

R81 keeps four protected controls intact:

| Protected control | R81 disposition |
|---|---|
| Public/private boundary | Provenance-only data stays private; public core exports only public-safe files. |
| Source verification | Any named script, profile, guide, or generated artifact must be verified from repo source before dispatch. |
| No-commit and reviewer separation | Worker-owned tranches may remain no-commit when dispatched that way; reviewer/closer handles closure. |
| Closure evidence | RC claims require command-backed smoke proof, changed-path evidence, and gate output. |

R81 may reduce ceremony only by choosing smaller deliverables and avoiding
unneeded artifacts. It may not weaken these protected controls.

## Product Boundary Model

| Lane | Role | Must contain | Must not contain |
|---|---|---|---|
| Provenance | Full CVF source of truth | complete governed records, private evidence, internal continuity, operator-only decisions | accidental public export by direct push |
| Public core | Public-safe CVF core | wrapper installer, safe guides, rule-pack profile surfaces, public docs and scripts | `CVF_SESSION`, private handoffs, provenance-only overlays, private source mirrors |
| Local workspace | Operator or future paid-user working area | selected rules/guards, workspace guide, workspace rules, agent onboarding, optional local continuity templates | hidden private provenance data unless explicitly operator-local and local-only |

## Roadmap Tranches

| Tranche | Objective | Output | Status |
|---|---|---|---|
| R81A | RC source map and boundary confirmation | source-verified map of workspace scripts, generated files, guides, profiles, and public/private boundaries | REVIEWER_ACCEPTED_BOUNDED |
| R81B | RC checklist definition | compact workspace RC checklist with required commands and pass/fail meanings | PASS |
| R81C | Disposable fresh-project smoke | prove fresh bootstrap plus selected rule-pack behavior in a temp workspace | PASS |
| R81D | Existing-project adoption smoke | prove adopt-existing flow without depending on Policy_Local app logic | PASS |
| R81E | Local workspace update proof | prove hidden public core update, wrapper refresh, guide refresh, and doctor check remain repeatable | PASS |
| R81F | RC closure decision | close or park the RC lane with exact blockers and next product action | RC_PASS_BOUNDED |

## Work Plan

1. Open R81A with a fresh GC-018 baseline and source-verified work order.
2. Inventory only current workspace product surfaces, not all historical CVF
   governance.
3. Convert the inventory into a short RC checklist.
4. Run smoke checks in disposable projects first.
5. Use Policy_Local only as an optional after-RC downstream candidate, not as
   the proof that CVF Workspace works.
6. Public-sync only when the changed files are public-safe and remote boundary
   evidence is refreshed.
7. Close R81 with either RC_PASS_BOUNDED or RC_BLOCKED_WITH_REASON.

## Acceptance Criteria

R81 can close only when all of these are true:

- the provenance, public core, and local workspace roles are explicitly
  documented and source-backed;
- a fresh workspace can be bootstrapped and pass the workspace doctor;
- an existing project can be adopted without depending on project-specific app
  code;
- rule-pack/profile selection is understandable from the workspace guide and
  workspace rules;
- generated guides and workspace files are public-safe in public-free and
  paid-user-safe modes;
- operator-local continuity templates remain local-only and do not leak into
  public output;
- every RC_PASS claim cites command output, commit or working tree evidence,
  and exact changed paths.

## Verification / Evidence

| Evidence | Required result |
|---|---|
| Provenance status before dispatch | clean or explicitly disclosed |
| Public-sync remote check | confirms public repo remote before any public push |
| Workspace doctor | PASS for disposable fresh project and adopted existing project |
| Rule-pack profile smoke | selected profile produces expected allowed artifact class |
| Public-safe leakage scan | no private continuity or provenance-only tokens in public-free or paid-user-safe generated output |
| Git changed-set proof | no use-case app changes in R81 workspace RC closure |
| Governance gate | matching autorun phase passes before dispatch, closure, commit, or push |

## Closure Decision

R81 is RC_PASS_BOUNDED. The source map, compact checklist, disposable fresh
bootstrap, existing-project adoption, local workspace update, and profile
boundary proof are recorded in
`docs/reviews/CVF_MSEA_R81B_WORKSPACE_RC_INTEGRATED_SMOKE_AND_CLOSURE_REVIEW_2026-07-10.md`.

The next product move is public-safe packaging and distribution design only
when a separately authorized public-sync packet refreshes repository-boundary
evidence. Do not infer public release readiness from this local RC decision.

## Machine Closure Package

| Closure item | Required artifact/path | Final status |
|---|---|---|
| R81A source map | R81A source map and completion review | REVIEWER_ACCEPTED_BOUNDED |
| R81B checklist | Workspace RC checklist | PASS |
| R81C-R81E smoke evidence | R81B integrated smoke and closure review | PASS |
| R81F decision | R81B integrated smoke and closure review | RC_PASS_BOUNDED |
| Public export | no public-sync batch | DEFERRED_PRIVATE_ONLY |

## Dispatch Boundary

The next authorized move from this roadmap is a separately authorized
public-safe packaging or distribution-design packet. R81 execution is closed.

Any later packet may read current workspace scripts, guides, profile manifests,
and public-sync boundary evidence, but must not infer a public claim from R81.
It needs fresh authority before it changes public-sync, runtime, tests,
checkers, hooks, `Policy_Local`, provider/live behavior, or production scope.

## Checker Source Read-Ahead Block

| Field | Disposition |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| literalTokensReviewed | `Status:`, `docType: roadmap`, `## Authorization / Decision`, `## Purpose`, `## Scope`, `## Non-Goals`, `## Design Control Gate`, `## Work Plan`, `## Acceptance Criteria`, `## Verification / Evidence`, `## Public Export Disposition` |
| gateRunPurpose | confirmation evidence for the new active roadmap shape, not first discovery |
| claimBoundary | checker read-ahead records source files and literal tokens reviewed before authoring this roadmap; it does not claim checker semantic changes |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R81 is private provenance roadmap planning. Any later public-sync export
must be separately authorized and must use the sibling public-sync lane.

## Claim Boundary

This roadmap opens the CVF Workspace Productization Release Candidate lane
only. It does not implement a use case, mutate Policy_Local app behavior,
change governance checker semantics, retire guards, prove provider/live
behavior, claim hosted or production readiness, or export public artifacts.
