# CVF Phase 2.B Live Governance Proof Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_LIVE_GOVERNANCE_PROOF

docType: roadmap

Date: 2026-05-21

---

## Purpose

Define the separate live-provider proof needed after Phase 2.B runtime
coherence closes.

This roadmap exists so the live proof is not bundled into adapter/table
coverage or internal runtime-coherence work.

---

## Authority Chain

- Static Phase 2.B migration plan:
  `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- Final table-coverage completion:
  `docs/reviews/CVF_PHASE_2B_MEMORY_TAIL_ADAPTERS_MIGRATION_COMPLETION_2026-05-21.md`
- Runtime-coherence prerequisite roadmap:
  `docs/roadmaps/CVF_PHASE_2B_RUNTIME_COHERENCE_ROADMAP_2026-05-21.md`
- Mandatory live governance proof rule:
  `AGENTS.md`
- HN2.c freeze-release rule:
  `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`

---

## Authorization / Decision

Decision: propose live governance proof as a separate downstream tranche, not
as part of adapter/table coverage or internal runtime coherence.

Authorization posture: CLOSED_LIVE_GOVERNANCE_PROOF.
Runtime-coherence closure, downstream GC-018, and downstream work order are
filed and cited in the completion review.

---

## Prerequisite Gate

This prerequisite is satisfied by the runtime-coherence completion review.

Required prerequisite artifact:

- `docs/reviews/CVF_PHASE_2B_RUNTIME_COHERENCE_COMPLETION_2026-05-21.md`
  or a later dated equivalent completion review.

The live-proof work order executed after that artifact existed.

---

## Problem Statement

Phase 2.B will not be "really complete" for governance claims until a live
provider-backed path proves that CVF can produce, join, and audit governance
evidence under the migrated Phase 2.B adapter graph.

The proof must be narrow and honest: it proves one live governed route, not all
providers, all user tasks, all Maika workflows, or a global freeze lift.

---

## Scope

In scope:

- One narrow live governance proof path using the repository's mandatory
  release-quality proof command or a stricter successor.
- Loading operator-supplied live keys from allowed environment variables or
  the existing private `.env.local` path without printing raw secrets.
- Verifying receipt/audit evidence includes the Phase 2.B coherence graph
  reference.
- Verifying no direct provider fallback bypasses CVF governance.
- Completion review that records exact command, provider lane, decision,
  receipt id, trace id, redaction posture, and boundary.

---

## Non-Goals

- No broad provider benchmark.
- No multi-provider stability claim.
- No Maika child-data/photo/vision claim.
- No public catalog update unless the proof intentionally creates a public
  product capability claim through separate GC-024 handling.
- No provider runtime expansion.
- No new policy, risk, guard, receipt, or memory engine.
- No persistent memory store.
- No database schema migration.
- No new memory tier.
- No global freeze lift.

---

## Proposed Dependency Chain

Live proof should close as a single narrow chain after runtime coherence:

```text
LP-01 runtime-coherence completion cited
  -> LP-02 live key readiness and secret hygiene
  -> LP-03 live governed execution proof
  -> LP-04 receipt/coherence graph assertion
  -> LP-05 bypass/fallback rejection assertion
  -> LP-06 completion review and claim boundary
```

---

## Work Packages

| id | package | done criterion |
| --- | --- | --- |
| LP-01 | Prerequisite citation | Runtime-coherence completion is present and cited. |
| LP-02 | Live key readiness | Live key is loaded from allowed operator secret source; raw value is never printed or committed. |
| LP-03 | Live governed execution proof | Mandatory live proof command passes with a real provider call. |
| LP-04 | Receipt/coherence assertion | Live receipt includes traceable governance evidence linked to Phase 2.B coherence graph evidence. |
| LP-05 | Fallback rejection assertion | Proof fails if direct provider fallback or mock fallback is used. |
| LP-06 | Completion review | Review records provider lane, command, receipt, decision, and strict claim boundary. |

---

## Work Plan

1. Wait for Phase 2.B runtime-coherence completion review.
2. File reviewer rebuttal for this roadmap.
3. If accepted, file a bounded GC-018/work order for `LP-01 -> LP-06`.
4. Confirm live key readiness through allowed operator secret sources without
   printing raw values.
5. Run the mandatory live governance proof command or stricter successor.
6. Assert receipt/coherence graph linkage and bypass/fallback rejection.
7. File completion review with exact command, evidence, and claim boundary.

---

## Required Command

The default release-quality command is:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

The implementation may add a stricter Phase 2.B live-proof wrapper only if it
still runs the mandatory command or proves an equal-or-stricter live governed
path with no mock fallback.

---

## Acceptance Criteria

- Live proof fails when no DashScope-compatible live key is available.
- Live proof passes only with a real provider-backed governed route.
- Result includes a governance receipt with decision, receipt id, trace id,
  policy/risk evidence, and audit trail evidence.
- Result references the previously closed runtime-coherence artifact.
- No raw API key value is printed, copied into docs, or committed.
- Completion review does not claim broad provider stability, Maika vision,
  public capability readiness, or global freeze lift.

---

## Verification / Evidence

Required verification after implementation:

- prerequisite runtime-coherence completion review exists;
- mandatory live proof command result;
- fallback/bypass rejection evidence;
- docs governance compatibility check;
- markdown structural completeness check;
- completion review with Evidence Trace Block.

---

## Exit Condition

Live proof is closed only when a completion review records a passing
provider-backed governance proof and the exact bounded claim it supports.

If live provider keys are unavailable, this roadmap must remain blocked rather
than downgraded to mock proof.

---

## Claim Boundary

This roadmap may be cited only as proposed authorization for one narrow
provider-backed Phase 2.B live governance proof after runtime coherence closes.

It must not be cited as adapter coverage, runtime coherence, broad provider
stability, Maika product proof, child-data/photo/vision proof, public catalog
readiness, or global freeze release.
