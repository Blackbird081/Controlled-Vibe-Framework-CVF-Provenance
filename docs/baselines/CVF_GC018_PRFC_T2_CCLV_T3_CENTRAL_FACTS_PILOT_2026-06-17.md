# CVF GC-018 PRFC-T2 CCLV-T3 Central Facts Pilot

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_DISPATCH

docType: baseline

Date: 2026-06-17

Owner: Codex

rawMemoryReleased: false

GC-018 class: governance-foundation-pilot

## Purpose

Authorize PRFC-T2, the second tranche of the Pre-Runtime Foundation Cleanup And
Pilot roadmap. PRFC-T2 executes the CCLV-T3 pilot on one small governance
closure workflow to test whether a central facts packet plus local views reduces
duplicate shared-fact edits without weakening local reviewer judgment.

## Scope / Target / Owner Boundary

Target: one new governance closure workflow: PRFC-T2 itself. The worker creates
one central closure facts packet and at least two local views that reference it.

Owner boundary: this GC-018 authorizes dispatch only. It does not authorize
runtime queue execution, scheduler work, UI implementation, provider/live proof,
public-sync, registry edits, Model Gateway work, production release, or public
release.

## Authorization / Decision

Operator instruction (2026-06-17): continue after PRFC-T1 prerequisite
satisfaction. The active session now identifies PRFC-T2 as the next allowed
move with fresh GC-018 and a source-verified work order.

Decision: AUTHORIZE PRFC-T2 as a bounded Central Core + Local View pilot under
`WORKER_MUST_NOT_COMMIT` for Claude worker execution and Codex reviewer closure.
Runtime execution remains parked.

## Source Authority

- Parent roadmap:
  `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md`
- CCLV roadmap:
  `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md`
- CCLV standard:
  `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md`
- Local reference rules:
  `docs/reference/CVF_CLOSURE_CENTRAL_FACTS_LOCAL_REFERENCE_RULES.md`
- Central facts packet template:
  `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md`
- CCLV advisory checker:
  `governance/compat/check_central_facts_reference.py`
- PRFC-T1 completion:
  `docs/reviews/CVF_PRFC_T1_CCLV_T2_CURRENT_STATE_RECONCILIATION_COMPLETION_2026-06-17.md`

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| PRFC-T2 is the next tranche after PRFC-T1 prerequisite satisfaction | `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md` | `## Tranche Plan`; PRFC-T2 row | `READY_FOR_GC018` | PRFC roadmap | ACCEPT |
| PRFC-T2 purpose is CCLV-T3 pilot | `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md` | `## PRFC-T2 Acceptance Criteria` | T2-AC1..T2-AC5 | PRFC roadmap | ACCEPT |
| CCLV-T3 should pilot on a new governance batch | `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md` | `## Work Plan` | CCLV-T3 pilot | CCLV roadmap | ACCEPT |
| Central facts packet fields are defined | `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md` | `## Required Central Facts` | `batchId`; `baseHead`; `materialCommit`; `expectedChangedSet`; `claimBoundary` | CCLV standard | ACCEPT |
| Local reference block format is defined | `docs/reference/CVF_CLOSURE_CENTRAL_FACTS_LOCAL_REFERENCE_RULES.md` | `## Local Reference Block Format` | Central Facts Reference block | local reference rules | ACCEPT |
| Markdown central facts template exists | `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md` | `## Central Facts Packet` | required field table | closure facts template | ACCEPT |
| CCLV advisory checker validates central packets and local references | `governance/compat/check_central_facts_reference.py` | checker constants | `CENTRAL_FACTS_REQUIRED_FIELDS`; `LOCAL_REFERENCE_SUB_FIELDS` | checker | ACCEPT |
| PRFC-T1 prerequisite is satisfied before PRFC-T2 | `docs/reviews/CVF_PRFC_T1_CCLV_T2_CURRENT_STATE_RECONCILIATION_COMPLETION_2026-06-17.md` | `Status line and completion claim` | PRFC-T1 pass disposition | completion review | ACCEPT |

## Continuation Class And Depth Audit

GC-018 Continuation Candidate

- Candidate ID: PRFC-T2
- Date: 2026-06-17
- Parent roadmap / wave:
  `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md`
- Proposed scope: CCLV-T3 pilot on one new governance closure workflow
- Continuation class: STRUCTURAL
- Quality-first decision: CONTINUE
- Remediation target if not expanding: N/A with reason: PRFC-T1 already removed
  the stale current-state ambiguity that blocked this pilot
- Why now: this tests the Central Core + Local View pattern before runtime
  creates more state and closure records
- Active-path impact: LIMITED
- Risk if deferred: closure packets keep repeating shared facts and remain
  vulnerable to cross-file drift
- Lateral alternative considered: YES
- Why not lateral shift: PRFC-T3 checker hardening depends on knowing whether
  the CCLV pilot improves or worsens authoring/review effort
- Real decision boundary improved: YES
- Expected enforcement class: GOVERNANCE_DECISION_GATE
- Required evidence if approved:
- one central facts packet under `docs/reviews/evidence/`
- at least two local views that reference the central packet
- advisory checker pass for central packet and local references
- worker return comparing duplicate fact edits before and after

Depth Audit

- Risk reduction: 1
- Decision value: 2
- Machine enforceability: 1
- Operational efficiency: 1
- Portfolio priority: 1
- Total: 6
- Decision: CONTINUE
- Reason: bounded governance pilot with clear acceptance criteria and no runtime
  or provider blast radius.

## Authorized Deliverables

Worker deliverables:

- `docs/reviews/evidence/CVF_PRFC_T2_CCLV_T3_CENTRAL_FACTS_PILOT_CLOSURE_FACTS_2026-06-17.md`
- `docs/reviews/CVF_PRFC_T2_CCLV_T3_CENTRAL_FACTS_PILOT_WORKER_RETURN_2026-06-17.md`
- updates to this PRFC roadmap and the CCLV roadmap to record T2/CCLV-T3
  closure disposition
- optional work-order closure conversion edits if required by gates

The worker return and roadmap update must be local views. They may repeat a
short summary for readability, but the central facts packet is the shared-fact
source of truth for the pilot worker-return package. Codex owns any final
completion review after accepting the worker return.

## Protected Boundary

No protected state or session front-door edit is authorized for the worker. If
PRFC-T2 closure changes next allowed move, Codex performs reviewer-owned
session-sync after accepting the worker return.

## Tranche Closure Checklist

- [ ] Central facts packet exists and includes all CCLV required fields
- [ ] At least two local views reference the central facts packet
- [ ] Local views retain role-specific judgment and local deltas
- [ ] `check_central_facts_reference.py --paths <changed-packets> --enforce`
  passes
- [ ] Worker-return evidence states whether duplicate fact edits were reduced
- [ ] No historical artifact is rewritten solely for the pilot
- [ ] No runtime/provider/live/public-sync/registry/Model Gateway scope is added

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `EVIDENCE_DUPLICATION_DRIFT` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `PILOT_AUTHORIZED` |
| Next control action | PRFC-T2 executes one CCLV-T3 pilot before PRFC-T3 checker work |
| Worker blame | `N/A_WITH_REASON`: this is a governance data-shape pilot, not a worker defect |

## Decision

AUTHORIZE PRFC-T2 as a bounded CCLV-T3 Central Core + Local View pilot under
`WORKER_MUST_NOT_COMMIT`. Codex owns review, acceptance, commit, closure, and
any later session-sync. Workspace runtime execution remains parked.

## Verification

Required pre-dispatch evidence:

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base c1da2af0 --head HEAD`
- `python governance/compat/check_work_order_dispatch_quality.py --base c1da2af0 --head HEAD --enforce`
- `git diff --check`

Required worker-return evidence:

- `python governance/compat/check_central_facts_reference.py --paths docs/reviews/evidence/CVF_PRFC_T2_CCLV_T3_CENTRAL_FACTS_PILOT_CLOSURE_FACTS_2026-06-17.md docs/reviews/CVF_PRFC_T2_CCLV_T3_CENTRAL_FACTS_PILOT_WORKER_RETURN_2026-06-17.md --enforce`
- `python governance/compat/run_worker_return_fast_gate.py`
- `git diff --check`

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance pilot. No public-sync batch is authorized.

## Claim Boundary

This GC-018 authorizes a documentation/governance pilot only. It does not
implement PRFC-T3, open runtime, run provider/live proof, edit registries,
perform public-sync, touch Model Gateway, or claim production or public
release.
