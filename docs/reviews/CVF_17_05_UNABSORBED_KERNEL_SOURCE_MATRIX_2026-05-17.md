# CVF 17.05 Unabsorbed Kernel Source Matrix

Date: 2026-05-17

Memory class: FULL_RECORD

Status: PHASE 1.0 EXTENDED SCOPE ARTIFACT. Absorption status matrix for all
private source files from the 17.05 review folder and the Agent Harnesses /
Claude Kit material.

This file does not authorize implementation, does not modify runtime code,
does not change public claims, and does not change release gates.

Authorized by:
`.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`

## Purpose

List every significant private source artifact from the 17.05 review chain
and the Agent Harnesses / Claude Kit material. For each source, record:

- absorption status (absorbed / partially\_absorbed / doc\_only\_absorbed /
  not\_absorbed / deferred / rejected)
- which root artifact received the absorption (if any)
- the blocking reason if not absorbed
- whether it touches a freeze-blocked kernel surface

This matrix prevents future agents from claiming "absorbed" when the true state
is doc-only or partial. It is the fourth required artifact from the Governance
Kernel Freeze recommendation, added specifically because of the ORCHESTRATOR
finding.

## Target

Private review folder:
`.private_reference/legacy/CVF 17.05/REVIEW FOLDER/`

Private agent harness material referenced in orchestrator gap audit:
`.private_reference/` (CVF ADD Human System Harness, CVF 16.5 Claude Kit)

## Scope / Target / Owner Boundary

In scope:

- All `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/` files
- Private Agent Harnesses / Claude Kit source files cited in the orchestrator
  gap audit
- The `Review CVF.md` source document itself

Out of scope:

- Private files not cited in any review packet (unknown unknowns)
- Archived handoffs in `CVF_SESSION/handoffs/archive/` (session artifacts, not
  knowledge sources)
- Public repo files (they are absorption targets, not sources)

Owner: CVF Phase 1.0 reconvergence surface. This matrix must be consulted
before any future agent claims that a private source concept has been absorbed.

## Active Boundary

Absorption status entries reflect the state as of 2026-05-17. Any future
absorption work that changes the status of a row must update this matrix as
part of its commit.

## Absorption Status Taxonomy

| Status | Meaning |
|---|---|
| `absorbed` | Core concept, contract, and implementation fully present in root working tree |
| `partially_absorbed` | Concept present in root; key sub-concepts or contracts missing |
| `doc_only_absorbed` | Concept documented in governance/docs; no runtime contract or implementation |
| `not_absorbed` | Concept cited in private source; not found anywhere in root working tree |
| `deferred` | Operator decision: absorption postponed to a named future phase |
| `rejected` | Operator decision: concept not appropriate for CVF canon |

---

## Section A — 17.05 Review Folder: Process and Governance Packets

These are the session-level governance artifacts from the 17.05 review chain.
They are not knowledge sources to absorb — they are process records. Listed
here for completeness and to confirm they are correctly classified as private.

| Source file | Classification | Absorption status | Root artifact | Notes |
|---|---|---|---|---|
| `CVF_17_05_SYSTEM_RECONVERGENCE_STOP_DECISION_2026-05-17.md` | Session decision | `doc_only_absorbed` | `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V9_2026-05-18.md` | Operator decision recorded in session front door; posture active |
| `CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md` | Session recommendation | `doc_only_absorbed` | `AGENT_HANDOFF_V9_2026-05-18.md`, this artifact | Freeze recommendation recorded; not yet formally accepted by operator |
| `CVF_17_05_AGENT_HANDOFF_AND_MEMORY_GAP_CODEX_AUDIT_2026-05-17.md` | Gap audit | `absorbed` | `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION/handoffs/archive/` | Session front door and archive structure address all three competing-truth gaps identified |
| `CVF_17_05_SINGLE_SESSION_MEMORY_FRONT_DOOR_PROPOSAL_2026-05-17.md` | Infrastructure proposal | `absorbed` | `CVF_SESSION_MEMORY.md` | Front door implemented exactly as proposed |
| `CVF_17_05_AGENT_ORCHESTRATOR_ROLE_ABSORPTION_GAP_CODEX_AUDIT_2026-05-17.md` | Gap audit | `doc_only_absorbed` | `AGENT_HANDOFF_V9_2026-05-18.md`, this artifact | Gap documented; no runtime absorption yet — see Section C |
| `CVF_17_05_REVIEW_CVF_CLAUDE_PROBLEM_AND_PHASE_CROSS_CHECK_2026-05-17.md` | Review packet | `doc_only_absorbed` | `docs/reviews/CVF_17_05_REVIEW_CVF_CONVERGED_VERDICT_2026-05-17.md` | Problem A–H classification captured in converged verdict |
| `CVF_17_05_REVIEW_CVF_CONSENSUS_REMEDIATION_ROADMAP_DRAFT_2026-05-17.md` | Draft roadmap | `doc_only_absorbed` | Superseded by final converged roadmap | Draft only; not canonical |
| `CVF_17_05_REVIEW_CVF_CODEX_REVIEWER_REBUTTAL_TO_CONSENSUS_ROADMAP_DRAFT_2026-05-17.md` | Rebuttal packet | `doc_only_absorbed` | `docs/reviews/CVF_17_05_REVIEW_CVF_CONVERGED_VERDICT_2026-05-17.md` | 5 over-claims documented in GC-046 worked example |
| `CVF_17_05_REVIEW_CVF_CLAUDE_PROPOSER_RESPONSE_TO_REVIEWER_REBUTTAL_2026-05-17.md` | Response packet | `doc_only_absorbed` | `docs/reviews/CVF_17_05_REVIEW_CVF_CONVERGED_VERDICT_2026-05-17.md` | Converged into 10/10 ACCEPTED verdict |
| `CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md` | Final roadmap | `doc_only_absorbed` | `docs/reviews/CVF_17_05_REVIEW_CVF_CONVERGED_VERDICT_2026-05-17.md` | Roadmap recorded; implementation phases blocked pending Phase 1.0 closure |

**Kernel surface touched:** None — these are process artifacts.

---

## Section B — Review CVF.md Source Document

The primary source under 17.05 review: a structured system-integration audit
identifying Problems A–H and proposing a 4-phase remediation priority.

| Source concept | Problem | Absorption status | Root artifact | Kernel surface | Blocking reason |
|---|---|---|---|---|---|
| Internal coherence risk / kernel drift | A | `doc_only_absorbed` | `docs/reviews/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md`, this matrix | Surfaces 1–12 | Drift inventoried; 9 of 12 kernel surfaces remain `freeze_blocker` — consolidation requires Phase 1.P/1.I/1.R/1.M GC-018 |
| Skill system → product capability gap | B | `doc_only_absorbed` | `docs/reviews/CVF_17_05_REVIEW_CVF_CONVERGED_VERDICT_2026-05-17.md` | Surface 10 (Capability) | `CertifiedCapability`, `ProductWorkflow`, `Outcome` chain has no implementation; blocked until Phase 2.A GC-018 |
| CLI not unified runtime entry point | C | `not_absorbed` | None | Surface 6 (Execution lifecycle) | No unified CLI runtime work authorized; `doc_only_absorbed` classification premature — marking `not_absorbed` |
| Provider abstraction incomplete | D | `partially_absorbed` | `EXTENSIONS/CVF_MODEL_GATEWAY/` | Surface 11 (Provider execution) | Gateway owns provider execution; stream parsing exists; receipt shape not yet unified with canonical receipt (Surface 8) |
| Operational benchmark category incomplete | E | `not_absorbed` | None | (cross-cutting) | No benchmark category work authorized in current session posture |
| Noncoder UX not outcome-first | F | `not_absorbed` | None | Surface 10 (Capability) | F-1 output-quality parity explicitly excluded from scope; noncoder UX blocked on Phases 3–4 |
| Agent role / execution identity drift | G | `partially_absorbed` | `docs/reviews/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md` | Surface 2 (Agent roles), Surface 7 (Delegation) | Role drift inventoried (20 surfaces); ORCHESTRATOR role boundary not absorbed; worker-lane delegation not absorbed |
| Memory hierarchy not canonical | H | `not_absorbed` | `docs/reviews/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md` (1 surface found, false positive) | Surface 9 (Memory) | Memory tier model entirely unimplemented; no canonical memory home exists |

**Summary for Review CVF.md:**
- `absorbed`: 0 concepts
- `partially_absorbed`: 2 concepts (D, G)
- `doc_only_absorbed`: 2 concepts (A, B)
- `not_absorbed`: 4 concepts (C, E, F, H)

---

## Section C — Agent Harnesses / Claude Kit Source Material

Source: private CVF ADD Human System Harness and CVF 16.5 Claude Kit files
cited in the orchestrator gap audit.

### C.1 — CVF ADD Human System Harness

| Source concept / file | Absorption status | Root artifact | Kernel surface | Blocking reason |
|---|---|---|---|---|
| Registered-agent action evaluation | `absorbed` | `CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts` | Surface 2 (Agent roles) | Fully implemented |
| Permission profile checks | `absorbed` | `CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts` | Surface 2 | Fully implemented |
| Structured handoff validation | `absorbed` | `CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts`, GC-020 | Surface 7 (Delegation) | Fully implemented |
| High-risk handoff approval stop | `absorbed` | `CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts` | Surface 7 | Fully implemented |
| Deterministic agent execution receipts | `absorbed` | `CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts` | Surface 8 (Receipt) | Fully implemented |
| Delegation ownership / write-boundary | `absorbed` | `CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` (ADD-C2) | Surface 7 | Fully implemented |
| `CVF_ORCHESTRATOR_DELEGATION_CONTRACT.md` — Orchestrator as CEO/dispatcher | `not_absorbed` | None | Surface 2, Surface 7 | Core invariant ("Orchestrator must not perform specialist work when a matching lane exists") not canonicalized; requires ORCHESTRATOR convergence roadmap GC-018 |
| `orchestrator_boundary.policy.json` — deny/require rules for `actor_role: orchestrator` | `not_absorbed` | None | Surface 2, Surface 3 (Policy) | Machine-readable policy for orchestrator actor role absent from root |
| `orchestrator_overreach.guard.ts` — overreach signal emission | `not_absorbed` | None | Surface 2, Surface 5 (Guard) | No root equivalent; overreach guard not implemented |
| `orchestrator_task_router.ts` — `delegate / fallback_execute / deny` | `not_absorbed` | None | Surface 6 (Execution lifecycle) | No task router contract in root |
| `phase_integrity.checker.ts` — lane-matched task missing delegation check | `not_absorbed` | None | Surface 7 (Delegation) | No lane-matching checker in root |
| Worker-lane / `delegation_required` field | `not_absorbed` | None | Surface 7 | Concept not found in root working tree |
| W7 delegation / overreach evidence fields | `not_absorbed` | None | Surface 8 (Receipt) | Receipt fields `delegationRequired`, `delegationRecorded`, `orchestratorOverreachSignal`, `fallbackAuthorized` not in any root receipt contract |

### C.2 — CVF 16.5 Claude Kit

| Source concept / file | Absorption status | Root artifact | Kernel surface | Blocking reason |
|---|---|---|---|---|
| `CVF_AGENT_ORCHESTRATION_RULES.md` — one governed orchestrator, many bounded workers, no bypass | `partially_absorbed` | `docs/baselines/archive/CVF_AGENT_BOUNDARY_DELEGATION_SOURCE_ADOPTION_MATRIX_2026-05-16.md` | Surface 2, Surface 7 | Adopted as "high-risk handoff stop and no free-form handoff boundary" only; mandatory worker-lane delegation rule not absorbed |
| `CVF_AGENT_ROLE_CATALOG.md` — planner, coder, reviewer, test, security, docs, refactor, database, frontend, backend, deployment agent templates | `deferred` | `docs/baselines/archive/CVF_AGENT_BOUNDARY_DELEGATION_SOURCE_ADOPTION_MATRIX_2026-05-16.md` | Surface 2 | Explicitly deferred to future catalog expansion in source adoption matrix; role templates not yet in `AgentRole` CPF union |
| Only CVF Orchestrator may: select agent, start agent, stop agent, route handoff, escalate risk, require approval, deny execution, finalize receipt | `not_absorbed` | None | Surface 2 | Orchestrator authority model is doctrine-level claim only; no runtime enforcement |
| Roles are templates, not autonomous runtime authorities | `doc_only_absorbed` | `governance/toolkit/05_OPERATION/CVF_AGENT_REVIEW_ANTI_COLLUSION_GUARD.md` (GC-046, adversarial role convention) | Surface 2 | Role-as-template principle captured in GC-046 role convention; no runtime enforcement of template vs. authority boundary |

---

## Section D — GC-046 Anti-Collusion Protocol Sources

The anti-collusion protocol itself was the primary deliverable of Phase 0.A.
These source concepts are now fully absorbed.

| Source concept | Absorption status | Root artifact | Notes |
|---|---|---|---|
| Evidence Trace Block per claim | `absorbed` | `governance/toolkit/05_OPERATION/CVF_AGENT_REVIEW_ANTI_COLLUSION_GUARD.md` (GC-046) | Fully implemented |
| Doctrine ≠ Evidence rule | `absorbed` | GC-046 Rule 2 | Fully implemented |
| Run the Trace rule | `absorbed` | GC-046 Rule 3 | Fully implemented |
| Count the Duplicates rule | `absorbed` | GC-046 Rule 4 | Fully implemented |
| Adversarial Role Assignment | `absorbed` | GC-046 Rule 5 | Fully implemented |
| Convergence algorithm (3-round, mechanical) | `absorbed` | GC-046 Convergence Algorithm section | Fully implemented |
| 17.05 role convention (Codex=REVIEWER odd, Claude=PROPOSER odd) | `absorbed` | GC-046 "17.05 Role Convention" section | Binding for 17.05 chain only |
| Evidence Trace Block template requirement in GC-018 packets | `absorbed` | `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md` | Updated in Phase 0.A commit |

---

## Absorption Summary

| Status | Section A (Process) | Section B (Review CVF.md) | Section C (Agent Harnesses) | Section D (GC-046) | Total |
|---|---:|---:|---:|---:|---:|
| `absorbed` | 3 | 0 | 6 | 8 | **17** |
| `partially_absorbed` | 0 | 2 | 2 | 0 | **4** |
| `doc_only_absorbed` | 7 | 2 | 1 | 0 | **10** |
| `not_absorbed` | 0 | 4 | 8 | 0 | **12** |
| `deferred` | 0 | 0 | 1 | 0 | **1** |
| `rejected` | 0 | 0 | 0 | 0 | **0** |
| **Total** | **10** | **8** | **18** | **8** | **44** |

**Key finding:** Of 44 tracked source concepts, 12 are `not_absorbed`. All 12
map to freeze-blocked kernel surfaces. The single largest not-absorbed cluster
is the ORCHESTRATOR role boundary system (8 concepts from Section C.1), which
requires a dedicated convergence roadmap GC-018.

---

## Findings

### Finding 1 — ORCHESTRATOR Gap Is the Dominant Not-Absorbed Cluster

8 of the 12 `not_absorbed` concepts are from the ORCHESTRATOR role boundary
system in the CVF ADD Human System Harness. These are not scattered pieces —
they form a coherent system that the private source fully specified. The reason
they were not absorbed is architectural:

> The previous absorption work took the narrower, safer slice (session governance,
> handoff validation, receipt generation, delegated write ownership) and flattened
> the richer ORCHESTRATOR doctrine into generic delegation and handoff behavior.

This is the exact failure mode Problem A identifies: "we have pieces" mistaken
for "we have the system."

### Finding 2 — Memory Model Has Zero Absorption

Problem H (memory hierarchy not canonical) has no absorption path. There is no
canonical memory tier implementation anywhere in the working tree. The single
surface found in the drift inventory was a third-party node\_modules false
positive. This is a clean `not_absorbed` / `not_owned` gap.

### Finding 3 — Capability Chain Is Doc-Only

Problem B (skill system → product capability gap) and Problem C (CLI not
unified runtime) have no runtime absorption. The missing chain
(`Outcome → Workflow → CertifiedCapability → Policy → Runtime → Validation →
Receipt → Noncoder Deliverable`) is entirely absent. The skill system is an
adapter-ready layer, but nothing to adapt to exists.

### Finding 4 — Phase 0.A and Session Infrastructure Are Fully Absorbed

GC-046 anti-collusion protocol (8 concepts), session front door (3 concepts),
and delegation/handoff contracts from ADD-C2 and GAP-AGENT-HANDOFF (6 concepts)
are all fully absorbed. These are the completed deliverables.

### Finding 5 — `doc_only_absorbed` Is The Largest Ambiguous Zone

10 concepts are `doc_only_absorbed` — they appear in governance docs or
session records but have no runtime contract. This is not a failure state, but
it is the category most vulnerable to over-claiming: a future agent can point
to these docs and say "covered" when the runtime is empty.

## Risk

**Immediate risk:** Future agents will read `CVF_17_05_REVIEW_CVF_CONVERGED_VERDICT_2026-05-17.md`
and see "10/10 ACCEPTED" and infer that Review CVF.md concepts are absorbed.
This matrix makes explicit that 4 of the 8 Review CVF.md problems remain
`not_absorbed` at the runtime level.

**Structural risk:** The 12 `not_absorbed` concepts all touch freeze-blocked
kernel surfaces. If any of them is introduced without this matrix being
consulted, the Governance Kernel Freeze will be breached.

**ORCHESTRATOR risk:** The private source has a complete, coherent
ORCHESTRATOR system that CVF partially references in architecture diagrams but
does not implement. If the architecture whitepaper continues to claim
"CEO / Orchestrator Surface [DONE]," that claim is false at the contract level.

## Decision

This matrix is the authoritative absorption state record as of 2026-05-17.
The following decisions are embedded:

1. The 12 `not_absorbed` concepts are **blocked** from implementation until
   the relevant kernel surface has an assigned owner (see owner map) and a
   separate GC-018 is filed.
2. The ORCHESTRATOR convergence roadmap (6-phase, separate GC-018) is the
   required vehicle for absorbing Section C.1 concepts.
3. `CVF_AGENT_ROLE_CATALOG.md` remains `deferred` — role templates require
   the ORCHESTRATOR convergence roadmap before promotion to CPF.
4. The architecture whitepaper claim "CEO / Orchestrator Surface [DONE]"
   should be amended to reflect `doc_only_absorbed` status (operator decision
   required before any public-facing change).
5. Any future GC-018 absorption packet must reference this matrix and declare
   which row it moves and to what status.

## Claim Boundary

This matrix:

- does not authorize implementation of any `not_absorbed` concept
- does not modify runtime code or architecture whitepaper claims
- does not change public claims or release gates
- does not promote any private review source into CVF canon
- does not claim live governance proof
- `absorbed` entries do not imply runtime completeness — they confirm the
  concept is present in the working tree in some form
- `doc_only_absorbed` entries are not implementation claims
- this matrix supersedes informal "absorbed" claims made in prior handoffs
  for any concept listed here
