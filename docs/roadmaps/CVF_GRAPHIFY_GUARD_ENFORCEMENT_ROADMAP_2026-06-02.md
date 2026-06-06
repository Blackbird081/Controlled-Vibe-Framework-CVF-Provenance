# CVF Graphify Guard Enforcement Roadmap

Memory class: FULL_RECORD

Status: PARKED_POST_CI1

docType: roadmap

Date: 2026-06-02

Related finding: `F2-guard-spec-absent`

Related registry: `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`

---

## Purpose

This roadmap parks the post-CI1 follow-up for Graphify guard policies
`G-GM-01` through `G-GM-08`.

CI1-T2 verified that `CVF_GRAPH_MEMORY_GUARD_SPEC.md` defines graph-memory guard
policies, but current CVF TypeScript runtime does not implement those guard IDs.
That is a valid deferred follow-up, not a CI1-T2 closure blocker.

---

## Authorization / Decision

Decision: `PARKED_POST_CI1`.

Authorization boundary: this document is a roadmap parking slot created to close
CI1-T2 finding disposition debt. It does not dispatch implementation. A later
operator-authorized GC/work order must be opened before any runtime, guard, or
agent-setting change.

---

## Scope Boundary

This roadmap does not authorize implementation by itself.

Before implementation, open a fresh governed GC/work order with source
verification against the current KGR/runtime/guard surfaces.

Out of scope for this parking roadmap:

- implementing `G-GM-*` checks;
- changing agent settings or PreToolUse hooks;
- modifying core guards without a guard-maintenance work order;
- claiming graph-first enforcement exists in CVF runtime.

---

## Non-Goals

- Do not implement Graphify `G-GM-*` guards in this batch.
- Do not change core guard behavior from this roadmap alone.
- Do not require every future corpus scan to use graph retrieval before a graph
  runtime enforcement point exists.
- Do not claim semantic correctness of legacy Graphify guard specs.

---

## Finding Disposition

| Finding | Disposition | Follow-up |
| --- | --- | --- |
| `F2-guard-spec-absent` | `DEFER_WITH_ROADMAP` | Use this roadmap as the parking reference before opening a bounded implementation tranche |

---

## Work Plan

The future implementation tranche should proceed in bounded phases:

1. Source-verify current KGR, retrieval, guard, CLI, and workflow owner surfaces.
2. Map each `G-GM-*` policy to accept/defer/reject disposition.
3. Select the smallest CVF-owned enforcement point for a first machine check.
4. Implement only the accepted subset with tests, guard docs, and explicit claim
   boundary.
5. Leave unsupported legacy-only hook behavior deferred with evidence.

---

## Candidate Phases

### Phase 1 — Source Verification

Verify current KGR surfaces, retrieval request flow, guard checker surfaces, and
any CLI/runtime call path that could enforce graph-first behavior.

Required outcome: source-verified implementation options and explicit reject
list for any legacy-only Graphify assumptions.

### Phase 2 — Advisory Guard Mapping

Map `G-GM-01` through `G-GM-08` to current CVF owner surfaces.

At minimum:

- `G-GM-01` Graph Priority Guard;
- `G-GM-02` No Bypass Guard;
- `G-GM-03` Provenance Guard;
- `G-GM-04` Integrity Guard;
- `G-GM-05` Access Control Guard;
- `G-GM-06` Confidentiality Guard;
- `G-GM-07` Drift Detection Guard;
- `G-GM-08` Compliance Guard.

Required outcome: accept/defer/reject matrix for each guard ID.

### Phase 3 — Machine Enforcement Candidate

Implement only the guard subset that has a current CVF-owned enforcement point.

Preferred first candidate: provenance-backed graph retrieval discipline, because
it can be checked without overclaiming a universal graph-first runtime.

Required outcome: machine tests and guard docs proving exactly what is enforced.

---

## Claim Boundary

This roadmap records a future enforcement lane. It does not prove that CVF
currently enforces Graphify `G-GM-*` policies.

---

## Acceptance Criteria

- A future work order cites this roadmap and the CI1-T2 finding packet.
- Every proposed `G-GM-*` implementation row has source verification.
- Unsupported guard IDs are explicitly deferred or rejected.
- The first implementation tranche proves a bounded enforcement claim only.
- Core guard edits, if any, are covered by guard-maintenance authorization.

---

## Verification / Evidence

Parking evidence for this roadmap:

- Registry finding: `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- Finding packet: `docs/corpus-intelligence/findings/legacy-cvf-important-graphify.md`
- CI1-T2 audit packet: `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md`
- CI1-T2 completion review: `docs/reviews/CVF_CI1_T2_GRAPHIFY_LEGACY_RESCAN_PILOT_COMPLETION_2026-06-02.md`

Future implementation evidence must include source verification, tests, and
the applicable autorun phase gates.
