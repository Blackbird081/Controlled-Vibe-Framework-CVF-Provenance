# CVF Central Core Local View Governance Refactor Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_IN_PROGRESS_T2_DISPATCHED

docType: roadmap

Date: 2026-06-16

rawMemoryReleased: false

Roadmap class: governance-foundation-data-shape-refactor

## Purpose

Reduce CVF governance drift by moving repeated shared facts into one central
core packet while preserving local artifact views for roadmaps, work orders,
worker returns, completion reviews, session state, and registries.

This roadmap responds to a repeated pattern: a single batch fact is copied into
many files, then a reviewer repair or closure commit changes the fact and
multiple artifacts fail separately. The target is not weaker evidence. The
target is one source of truth for shared batch facts and smaller local views
that link to it.

## Authorization / Decision

Decision: open a forward-only foundation roadmap. The operator explicitly
identified the pattern as a CVF-wide governance refactor: central core plus
local views.

No old closed artifact rewrite is authorized by this roadmap. No runtime,
provider/API, public-sync, broad legacy scan, co-work product development, or
production/public readiness work is authorized.

## Scope

In scope:

- define the CVF-wide central core/local view standard;
- design central facts packet fields for closure and finding evidence;
- add a narrow advisory validation path for new batches;
- pilot the pattern on one future small governance workflow;
- record migration rules that keep old artifacts untouched unless already in
  scope.

Out of scope:

- rewriting historical closed roadmaps, work orders, reviews, or handoffs;
- replacing local artifact sections entirely;
- removing required evidence;
- runtime/provider behavior;
- live API calls, credentials, public-sync, or production/public readiness.

## Non-Goals

- Do not migrate old closed artifacts in bulk.
- Do not replace local reviewer judgment with a central facts packet.
- Do not make central packets mandatory for small single-file batches.
- Do not remove Agent Operation Trace, closure quality, public export, or
  finding-learning requirements.
- Do not authorize runtime, provider, public-sync, or legacy broad-scan work.

## Design Rule

When a fact is shared by more than one artifact in a governed batch, prefer a
central core packet plus local references over repeated copy/paste evidence.
Each local artifact keeps its role-specific judgment and links to the central
facts.

## Design Control Gate

| Control | Decision |
|---|---|
| Foundation value | High: reduces repeated agent errors, reviewer latency, and cross-file drift |
| Scope size | Medium if rolled out broadly; must start with standard plus one pilot |
| Runtime risk | None authorized |
| Latency posture | Reduces closure and reviewer latency by avoiding repeated fact edits |
| Legacy posture | Not applicable; no legacy content is read or absorbed |
| Claim boundary | Governance data-shape refactor only |

## Tranche Plan

| Tranche | Status | Purpose | Owner |
|---|---|---|---|
| CCLV-T0 | COMPLETED_IN_ROADMAP_PACKET | Publish common standard and roadmap selection | Codex |
| CCLV-T1 | CLOSED_PASS_BOUNDED | Define a closure central facts packet template and local reference rules | Claude (combined role) |
| CCLV-T1A | CLOSED_PASS_BOUNDED | Apply CCLV pattern to the work order template (pointer refactor, 1200->994 lines) | Claude/Codex |
| CCLV-T2 | DISPATCHED_TO_CLAUDE | Add advisory checker for central facts references on changed new batches | Claude worker; Codex reviewer |
| CCLV-T3 | CANDIDATE_AFTER_T2 | Pilot on one small governance closure workflow | Future worker |
| CCLV-T4 | CANDIDATE_AFTER_PILOT | Decide whether selected workflows can replace duplicated AOT/closure facts with references | Codex reviewer |

## Work Plan

1. CCLV-T0 records the standard:
   `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md`.
2. CCLV-T1 should author a small template under `docs/reference/` for central
   closure facts and local references.
3. CCLV-T2 should add a narrow checker only after the template exists.
4. CCLV-T3 should pilot on a new governance batch, not on historical material.
5. CCLV-T4 should review latency, false positives, and operator readability.

## CCLV-T1 Closure Record (2026-06-16)

CCLV-T1 is `CLOSED_PASS_BOUNDED`. Delivered the closure central facts packet
template and the local reference block rules the standard specified.

- GC-018: `docs/baselines/CVF_GC018_CCLV_T1_CLOSURE_FACTS_PACKET_TEMPLATE_2026-06-16.md`
- Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T1_CLOSURE_FACTS_PACKET_TEMPLATE_2026-06-16.md`
- Markdown template: `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md`
- JSON companion: `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.json`
- Local reference rules: `docs/reference/CVF_CLOSURE_CENTRAL_FACTS_LOCAL_REFERENCE_RULES.md`
- Completion review: `docs/reviews/CVF_CCLV_T1_CLOSURE_FACTS_PACKET_TEMPLATE_COMPLETION_2026-06-16.md`

No checker was added (that is CCLV-T2). No workflow pilot was run (that is
CCLV-T3). Forward-only; no historical artifact was rewritten.

## CCLV-T2 Dispatch Record (2026-06-16)

CCLV-T2 is dispatched to Claude as a no-commit worker implementation packet.

- Codex audit and selection:
  `docs/reviews/CVF_CCLV_T1_T1A_CODEX_AUDIT_AND_CCLV_T2_SELECTION_2026-06-16.md`
- GC-018:
  `docs/baselines/CVF_GC018_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_2026-06-16.md`
- Work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_FOR_CLAUDE_2026-06-16.md`

Dispatch boundary: advisory checker only; no global hard-fail hook wiring, no
historical rewrite, no runtime/provider/live/public/legacy scope.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| CCLV-AC1 | New standard exists and says old closed artifacts are not reopened solely for migration. |
| CCLV-AC2 | T1 template distinguishes shared batch facts from local artifact view. |
| CCLV-AC3 | Any checker is additive/advisory or limited to changed new batches until pilot evidence exists. |
| CCLV-AC4 | Local artifacts retain local role judgment and do not become empty links. |
| CCLV-AC5 | No runtime/provider/live/public/legacy broad-scan scope is introduced. |

## Verification / Evidence

Required evidence for future tranches:

- template path and example central facts packet;
- local reference example;
- focused tests if a checker is added;
- reviewer-fast and diff hygiene;
- explicit claim boundary.

## Relationship To Finding Propagation

This roadmap prevents many duplicate-evidence errors by changing how shared
facts are authored. It does not replace a root-cause finding grouping roadmap.
Unknown or novel failures still need root-cause grouping after they occur.

## Non-Regression Boundary

The existing duplicated evidence pattern remains valid until a selected
workflow has a central facts template and guard support. Agents must not delete
local evidence from existing artifacts without a fresh work order and reviewer
approval.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `EVIDENCE_DUPLICATION_DRIFT` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `STANDARD_ADDED` |
| Next control action | CCLV-T2 advisory checker dispatched to Claude on 2026-06-16 |
| Worker blame | `N/A_WITH_REASON`: repeated facts across files create drift opportunities by design |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance roadmap. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 CCLV roadmap authoring and CCLV-T2 dispatch update |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch |
| Target paths | this roadmap; central core/local view standard |
| Allowed scope source | operator selected central core/local view as CVF-wide governance refactor |
| Before status evidence | base `28a72f45` for CCLV-T2 dispatch update |
| After status evidence | CCLV-T2 dispatched to Claude; pending dispatch commit |
| Diff evidence | `git diff --name-status`; `git status --short` |
| Approval boundary | roadmap update and dispatch packet only; no implementation by this commit |
| Claim boundary | governance planning and dispatch only |
| Expected manifest | `docs/reviews/CVF_CCLV_T1_T1A_CODEX_AUDIT_AND_CCLV_T2_SELECTION_2026-06-16.md`; `docs/baselines/CVF_GC018_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_FOR_CLAUDE_2026-06-16.md`; `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md` |
| Actual changed set | docs/reviews/CVF_CCLV_T1_T1A_CODEX_AUDIT_AND_CCLV_T2_SELECTION_2026-06-16.md; docs/baselines/CVF_GC018_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_2026-06-16.md; docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_FOR_CLAUDE_2026-06-16.md; docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This roadmap selects a governance data-shape refactor. It does not prove the
future checker, runtime behavior, provider behavior, public readiness,
production readiness, hosted freshness, or historical artifact migration.
