# CVF Legacy Spec Absorption Blindspot Codex Review

Memory class: FULL_RECORD

Status: REVIEW_FILED_WITH_CORRECTIVE_ACTIONS

docType: review

Date: 2026-05-23

Reviewer: Codex

---

## Purpose

Review Claude's audit at
`docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md`
after operator reported a serious recurring pain point: legacy CVF
knowledge existed in `.private_reference/legacy/`, but later agents scoped
Review-CVF closure work without using it.

This review confirms the real defect and corrects one overbroad claim in the
audit so the fix does not preserve a new false memory.

---

## Target / Source

Target under review:

- `docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md`
- the active Review-CVF pain-point closure chain from 2026-05-22
- current legacy-source routing controls

Sources checked:

- `.private_reference/legacy/CVF 16.5/agentmemory/`
- `.private_reference/legacy/CVF ADD/code-review-graph/`
- `.private_reference/legacy/CVF Edit/`
- `docs/baselines/archive/CVF_CONTROLLED_MEMORY_SOURCE_ADOPTION_MATRIX_2026-05-16.md`
- `docs/reviews/archive/CVF_CONTROLLED_MEMORY_RUNTIME_ADOPTION_CLOSURE_2026-05-16.md`
- `docs/reviews/archive/CVF_UNABSORBED_KNOWLEDGE_INVENTORY_2026-05-16.md`
- `docs/roadmaps/archive/CVF_ADD_E1_SCOPED_KNOWLEDGE_RUNTIME_ADOPTION_ROADMAP_2026-05-17.md`
- `docs/reviews/archive/CVF_LEGACY_SCOPE_ABSORPTION_AUDIT_MATRIX_2026-05-18.md`

---

## Scope / Methodology

Scope:

- confirm whether Claude's process finding is valid;
- identify any counter-evidence from archived absorption records;
- file process-level corrective actions only.

Methodology:

- read the active session front door and active state registry;
- read Claude's audit;
- grep active and archived docs for `agentmemory`, `code-review-graph`,
  `ScopedKnowledgeProvider`, and `ControlledMemoryGatewayContract`;
- inspect the existing controlled-memory and scoped-knowledge owner surfaces;
- update only governance/documentation routing artifacts.

Out of scope:

- runtime memory implementation;
- graph engine implementation;
- provider, receipt, route, database, public-sync, or freeze-release changes.

---

## Scope / Target / Owner Boundary

Owner boundary:

- Codex owns this correction review and the process artifacts filed with it.
- Claude's audit remains a valid predecessor audit but is corrected by this
  review where the two disagree.
- Future tranche owners must use the registry and GC-018 Legacy Spec Scan
  Block before scoping legacy-adjacent implementation.

This review does not authorize implementation.

---

## Finding 1 - The blindspot is real

Severity: SYSTEMIC.

The 2026-05-22 Review-CVF pain-point closure chain did not require a legacy
spec scan before scoping T1-T5. The active V2 roadmap cited active reviews and
`.private_reference/legacy/CVF 17.05/Review CVF.md`, but it did not require
reading the relevant legacy source folders:

- `.private_reference/legacy/CVF 16.5/agentmemory/`
- `.private_reference/legacy/CVF ADD/code-review-graph/`
- `.private_reference/legacy/CVF Edit/`

That is enough to explain how T5 could close a bounded ephemeral task-memory
slice without reconciling the richer memory gateway/retrieval/reinjection
contracts already present elsewhere in the repo.

Verdict: Claude's core process finding is valid.

---

## Finding 2 - Claude's "never referenced" claim is overbroad

Severity: CORRECTION REQUIRED.

The audit says the two folders were never referenced in any audit, roadmap, or
tranche. That is not fully true.

Counter-evidence found by Codex:

- `docs/baselines/archive/CVF_CONTROLLED_MEMORY_SOURCE_ADOPTION_MATRIX_2026-05-16.md`
  maps all 10 `agentmemory` files into `ControlledMemoryGatewayContract`.
- `docs/reviews/archive/CVF_CONTROLLED_MEMORY_RUNTIME_ADOPTION_CLOSURE_2026-05-16.md`
  closes `agentmemory` as a bounded runtime-owned controlled-memory contract.
- `docs/reviews/archive/CVF_UNABSORBED_KNOWLEDGE_INVENTORY_2026-05-16.md`
  records `code-review-graph` under ADD-E1 Scoped Knowledge / Code Graph.
- `docs/roadmaps/archive/CVF_ADD_E1_SCOPED_KNOWLEDGE_RUNTIME_ADOPTION_ROADMAP_2026-05-17.md`
  closes the read-only scoped-knowledge provider boundary.
- `docs/reviews/archive/CVF_LEGACY_SCOPE_ABSORPTION_AUDIT_MATRIX_2026-05-18.md`
  records `agentmemory` as `partially_absorbed` and `code-review-graph` as
  `not_absorbed` for graph-context resolver implementation.

Corrected verdict:

The folders were not invisible to the entire repo history. They were invisible
to the active Review-CVF pain-point closure chain because prior absorption
evidence lived in archived or side-channel artifacts and was not promoted into
a current absorption registry, GC-018 template requirement, or V2 roadmap
successor list.

This distinction matters: the defect is not only "nobody read it"; it is also
"the system forgot what it had already read."

---

## Finding 3 - The actual product gap remains

Severity: MATERIAL.

Existing runtime surfaces prove bounded contracts, not full product behavior:

- `ControlledMemoryGatewayContract` exists and covers policy, privacy,
  lifecycle, retrieval, reinjection packaging, and deterministic receipts.
- T5 later added ephemeral task-memory wiring and retained `canReinject=false`.
- Neither closure proves a broad live memory hierarchy on the governed
  `/api/execute` path.
- `ScopedKnowledgeProvider` exists as a read-only boundary, but the
  `code-review-graph` AST/dependency/blast-radius engine is not implemented.

Therefore the correct status is:

- Pain H memory: `partially_absorbed`, with successor work demand-gated.
- Graph knowledge: `boundary_absorbed_but_engine_not_implemented`, with
  successor work demand-gated.

---

## Findings / Position

Position:

- Claude's audit is directionally correct and should remain in the evidence
  chain.
- The corrected defect statement is narrower and more useful: archived
  absorption evidence existed, but current pain-point scoping did not resolve
  it.
- The fix must be systemic: registry plus mandatory legacy scan block, not
  another one-off audit.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Future agents repeat active-review-only scoping | Add Legacy Spec Scan Block to GC-018 template. |
| Archived absorption evidence is forgotten again | Create active legacy spec absorption registry. |
| T5 closure is mistaken for full Pain H memory readiness | Add T-H2 as demand-gated successor, not authorized implementation. |
| ScopedKnowledgeProvider is mistaken for graph engine implementation | Add T-GRAPH as demand-gated successor with explicit boundary. |
| Claude overclaim becomes future false memory | File this Codex correction and route session memory through it. |

---

## Corrective Actions Filed

Codex filed the following process artifacts in this turn:

- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
- `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md`
- `docs/roadmaps/archive/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md`
- `CVF_SESSION_MEMORY.md`

---

## Decision

Disposition: `CLAUDE_AUDIT_SUBSTANTIALLY_VALID_WITH_CORRECTION`.

Do not discard Claude's audit. It captured the operator pain correctly.
But future agents must use this corrected formulation:

> Prior legacy absorption evidence existed, but the active pain-point closure
> methodology did not require resolving it before scoping. The missing control
> is an active legacy spec absorption registry plus a mandatory legacy scan in
> every future GC-018/tranche touching memory, graph, intelligence, or
> Review-CVF pain points.

---

## Claim Boundary

This review does not authorize implementation of memory or graph runtime work.
It does not reopen T1-T5. It does not change provider, receipt, memory,
database, route, or public-sync behavior. T-H2 and T-GRAPH remain
`DEMAND_GATED` and require fresh GC-018 plus any blocked-work override.
