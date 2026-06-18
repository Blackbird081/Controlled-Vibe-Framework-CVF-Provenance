# CVF External Agent Review Context Systemization Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_T1_CLOSED_T3_READY_FOR_GC018

docType: roadmap

Date: 2026-06-18

rawMemoryReleased: false

Roadmap class: external-agent-review-context-systemization

## Purpose

Turn the RTAD-T6 foundation into a practical workflow for asking external
agents to review CVF accurately, especially across workflow-chain, MCP,
runtime, and workspace surfaces.

This roadmap prevents external reviewers from treating public/simple lifecycle
language or copied external packages as CVF authority, while preserving the
private provenance/public-summary boundary.

## Authorization / Decision

The operator directed Codex to create a roadmap for execution after RTAD-T6
absorbed useful external-agent MCP/workspace reference patterns and classified
the copied external workspace-layer package root.

This roadmap authorizes planning and dispatch preparation only. It does not
authorize public-sync, MCP implementation, provider calls, workspace runtime
execution, production-readiness claims, or publication of private provenance
source.

## Scope

In scope:

- create reusable external-agent review packets and templates;
- make workflow-chain public/simple vocabulary easy to map back to governed CVF
  authority surfaces;
- define how external findings are absorbed as CVF-owned findings, questions,
  reusable patterns, or rejected assumptions;
- prepare public-safe context candidates without pushing public-sync unless a
  later authorization opens that tranche;
- prepare MCP/workspace implementation decisions without implementing runtime
  tools unless a later authorization opens that tranche.

Out of scope:

- pushing to the public repository;
- exposing private provenance files in full;
- importing the raw external workspace-layer package;
- implementing MCP tools or workspace runtime behavior;
- running provider/live proofs;
- claiming public, production, release, or external-facing readiness.

## Non-Goals

- Do not replace CVF internal workflow-chain authority with
  `INTAKE -> DESIGN -> SPEC -> WORK_ORDER -> BUILD -> REVIEW -> FREEZE`.
- Do not make external-agent output canonical without CVF-owned absorption.
- Do not let public README/catalog wording override active session state,
  handoff, roadmap, GC-018, work order, autorun, review, receipt, or
  session-sync surfaces.
- Do not move, delete, or commit the raw copied external package in this
  roadmap.

## Source Authority

| Source | Role |
|---|---|
| `CVF_SESSION/state/entries/nextAllowedMove.json` | Current next allowed move and parked boundaries |
| `docs/reference/external_agent_review/README.md` | Stable external-agent review front door |
| `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_STANDARD.md` | Context packet requirements and external review rules |
| `docs/reference/external_agent_review/CVF_WORKFLOW_CHAIN_PUBLIC_REVIEW_CONTEXT.md` | Public/simple workflow vocabulary boundary |
| `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | Governed absorption map for the copied external package |
| `docs/reference/mcp_gateway/README.md` | MCP local-view front door |
| `docs/reference/agent_workspace/README.md` | Agent workspace local-view front door |
| `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json` | Local copied package lifecycle classification |

## Design Rule

Every external-agent review request must carry a bounded CVF context packet
before asking for architectural critique. The packet must state what is CVF
authority, what is public simplification, what is private provenance context,
and what is external reference material.

## Design Control Gate

| Control | Decision |
|---|---|
| Foundation value | High: external reviewers need a governed context packet before critique |
| Scope size | Small first tranche: EARC-T1 only creates template/checklist/sample context |
| Runtime risk | None in T0/T1; MCP/runtime implementation remains parked until T4 authorization |
| Public risk | T2 is held until explicit public-sync authorization |
| Private provenance boundary | Preserve private source; publish only curated public-safe summaries after authorization |
| Central Core + Local View | Stable reference front doors are central core; review packet is local view |
| Claim boundary | Planning and context-shaping only |

## Central Core + Local View Rule

Central core:

- CVF remains source of truth;
- active session state and active handoff define current execution authority;
- stable reference front doors define current domain semantics.

Local views:

- external-agent review packets explain only the review surface;
- public/simple workflow labels are display vocabulary;
- copied packages and external repos are reference inputs, not authority.

## Tranche Plan

| Tranche | Status | Purpose | Owner | Dispatch rule |
|---|---|---|---|---|
| EARC-T0 | ROADMAP_READY_FOR_T1_DISPATCH | Create this roadmap and define execution sequence | Codex | This roadmap only |
| EARC-T1 | CLOSED_PASS_BOUNDED | Build reusable external-agent review packet template and authoring checklist | Codex | Closed by EARC-T1 material commit |
| EARC-T2 | HOLD_PUBLIC_SYNC_AUTHORIZATION | Prepare public-safe front-door/catalog reconciliation plan for external reviewers | Codex | Requires operator public-sync authorization before editing public-sync clone |
| EARC-T3 | READY_FOR_GC018 | Define external-finding absorption workflow: finding, question, useful pattern, rejected assumption | Codex or delegated worker | Requires fresh GC-018 |
| EARC-T4 | HOLD_RUNTIME_AUTHORIZATION | Decide first MCP/workspace implementation boundary after review-context stabilization | Codex | Requires explicit MCP/runtime implementation authorization |

## T1 Target Shape

EARC-T1 should produce stable reference material under:

`docs/reference/external_agent_review/`

Minimum expected outputs:

- `CVF_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE.md`
- `CVF_EXTERNAL_AGENT_REVIEW_AUTHORING_CHECKLIST.md`
- one bounded sample packet that uses CVF-owned source authority and marks
  public/simple workflow vocabulary as display vocabulary only.

EARC-T1 must not publish, public-sync, run providers, implement MCP, or import
the raw copied package.

## T2 Target Shape

EARC-T2 is only opened after explicit public-sync authorization. It should
compare the private provenance context against the sibling public-sync clone
and prepare the smallest public-facing update that helps external agents read
CVF correctly.

Candidate public-facing surfaces, if authorized later:

- public README/front door;
- public catalog;
- public governance overview;
- public MCP/workspace explanation.

T2 must not leak private provenance files or imply public readiness.

## T3 Target Shape

EARC-T3 should define how external-agent output is classified after review:

| External output | CVF disposition |
|---|---|
| Source-backed CVF defect | Governed finding candidate |
| Useful external pattern | Absorb/adapt/defer/reject map entry |
| Public-simple assumption | Question or hypothesis until source-verified |
| Runtime/readiness claim | Block unless CVF live proof exists |
| Raw private-source request | Reject or replace with public-safe summary |

## T4 Target Shape

EARC-T4 is parked until the operator explicitly authorizes MCP/runtime
implementation. If opened later, it must consume:

- RTAD-T5 MCP boundary;
- RTAD-T6 absorption map;
- Agent Handoff Contract;
- agent workspace state topology;
- current Model Gateway runtime source.

T4 must start with a decision packet before any implementation.

## Current Runtime Freshness Verification

| Runtime surface | Current disposition |
|---|---|
| Model Gateway deterministic/runtime checks | Last bounded checks are RTAD-T2 through RTAD-T4; this roadmap does not rerun them |
| Live provider calls | Not authorized in EARC-T0/T1 |
| MCP runtime tools | Not authorized in EARC-T0/T1; T4 requires explicit implementation authorization |
| Workspace runtime state mutation | Not authorized in EARC-T0/T1 |
| Public-sync clone | Not touched in EARC-T0/T1; T2 requires explicit public-sync authorization |
| Raw copied external package | Local ignored reference only; do not import as CVF runtime source |

## EARC-T1 Closure Note (2026-06-18)

EARC-T1 is `CLOSED_PASS_BOUNDED`. It added the stable external-agent review
packet template, authoring checklist, and bounded workflow/MCP/workspace sample
packet under `docs/reference/external_agent_review/`, updated the folder front
door, and added GC-051 registry coverage.

Delivered stable local views:

- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_AUTHORING_CHECKLIST.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_SAMPLE_PACKET_WORKFLOW_MCP_WORKSPACE.md`

Execution evidence:

- `docs/baselines/CVF_GC018_EARC_T1_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE_2026-06-18.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T1_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE_FOR_CODEX_2026-06-18.md`
- `docs/reviews/CVF_EARC_T1_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE_COMPLETION_2026-06-18.md`

No public-sync, MCP implementation, provider/live call, workspace runtime
mutation, raw package import, production readiness, release readiness, public
readiness, or external-facing readiness was authorized or performed.

## Work Plan

1. Commit this roadmap as the EARC execution front door.
2. Sync active session state so the next allowed move points to EARC-T1.
3. If the operator asks to proceed, author fresh GC-018 plus work order for
   EARC-T1.
4. Keep T2 through T4 parked until their dispatch rules are satisfied.

## Acceptance Criteria

- Roadmap exists under `docs/roadmaps/`.
- Roadmap separates public-context work from public-sync execution.
- Roadmap separates MCP/workspace review-context work from runtime
  implementation.
- Roadmap names EARC-T1 as the first bounded dispatch candidate.
- Roadmap does not claim public readiness, production readiness, provider
  reliability, or MCP runtime readiness.

## Verification / Evidence

| Evidence | Expected result |
|---|---|
| `git diff --check` | Pass before material commit |
| `python governance/compat/run_worker_return_fast_gate.py` | Pass before material commit |
| `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base <baseHead> --head HEAD --enforce` | Pass or identify only expected pre-commit range limitations |
| Pre-commit hook | Pass before roadmap commit |
| Session-sync gate | Pass after roadmap commit if active next move is updated |

## Machine Closure Package

| Required row | Disposition |
|---|---|
| Roadmap state | `ROADMAP_T1_CLOSED_T3_READY_FOR_GC018` at `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md` |
| Work order trace | `docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T1_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE_FOR_CODEX_2026-06-18.md` |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` generated from source entry |
| Registry Markdown | `BLOCKED_WITH_REASON`: no separate markdown registry is required for this reference family |
| Public export disposition | `DEFERRED_PRIVATE_ONLY`: roadmap is private provenance planning; public-sync requires later authorization |
| Runtime proof | `BLOCKED_WITH_REASON`: no runtime/provider/MCP proof authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap prepares private provenance planning for future
external-agent review context. Public-sync is an explicit later tranche, not
part of this roadmap creation.

## Next Dispatch Candidate

EARC-T3: define the external-finding absorption workflow with fresh GC-018 and
a source-verified work order. EARC-T2 remains held for explicit public-sync
authorization, and EARC-T4 remains held for explicit MCP/runtime authorization.

## Claim Boundary

This roadmap is planning authority only. It does not publish, public-sync,
import raw external packages, implement MCP, run live providers, mutate runtime
behavior, or claim readiness.
