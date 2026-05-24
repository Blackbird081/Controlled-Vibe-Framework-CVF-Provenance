# CVF Value-Screened Next Tranche Roadmap

Memory class: SUMMARY_RECORD

Status: V1_V2_V3_CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-05-24

---

## Purpose

Select the next tranche by product value rather than by open-ended proof
extension. The S2 superseding soak now proves a bounded `15/15` live
tri-provider window. More broad provider soaking has diminishing marginal value
unless a specific product claim or customer workflow depends on it.

## Scope / Target / Owner Boundary

Scope: next-tranche selection only. This roadmap screens candidate directions
and recommends the next work package.

Target: roadmap/work-order planning surface, not product runtime.

Owner: operator selects; Codex implements only after fresh authorization and
the required GC-018/work order.

Out of scope: direct implementation, UI changes, route changes, provider
adapter changes, memory reinjection, graph authority, hosted readiness claims,
production readiness claims, or freeze release.

## Scope

In scope:

- rank next-value candidates by product usefulness and evidence need
- identify low-value continuation traps
- recommend the next tranche shape
- preserve S2 bounded provider claim without expanding it

Out of scope:

- committing to V1/V2 implementation before V3
- broad provider soaking
- model-specific retry loops
- F-1 parity tuning
- public-sync update except S3 metric-clarity wording

## Decision Principle

Prioritize work that moves CVF closer to a usable non-coder/small-team product
surface with governed evidence users can understand and reuse.

Deprioritize work that mostly increases benchmark counts, model variants,
token tuning, or provider retry loops without changing the user-visible value
proposition.

## Candidate Screen

| Candidate | Value | Risk | Recommendation |
| --- | --- | --- | --- |
| V1 Non-coder first-value journey hardening | High | Medium | Next after V3 |
| V2 Evidence-to-action product packaging | High | Low/Medium | Strong alternate or V1 companion after V3 |
| V3 Execution diagnostic contract | Critical | Medium | Selected mandatory next tranche |
| V4 Graph/memory productization through real tasks | Medium/High | Medium/High | Worth doing only with a concrete user workflow |
| V5 More provider soak windows | Low now | Low | Hold unless tied to a specific public claim |
| V6 More Qwen/model-specific proof loops | Low now | Medium | Hold unless operator has a concrete model need |
| V7 F-1 output-quality parity tuning | Rejected by rule | High | Do not reopen |

## Selected Next Tranche

V3: Execution Diagnostic Contract.

Authority:

- Standard:
  `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
- GC-018:
  `docs/baselines/CVF_GC018_V3_EXECUTION_DIAGNOSTIC_CONTRACT_2026-05-24.md`
- Work order:
  `docs/work_orders/CVF_WO_V3_EXECUTION_DIAGNOSTIC_CONTRACT_2026-05-24.md`

Bounded goal:

- Every failed, partial, empty-output, or rerun-triggering live run must record
  a secret-safe diagnostic with stable stage/class/retryability/userAction.
- Future CLI/MCP/API-key users must not receive only `success=false` or "no
  output" without a classified cause.

Why V3 moves ahead of V1/V2:

- V1/V2 rely on users understanding what happened when execution fails.
- Repeated live reruns without classified causes waste token budget and
  provider quota.
- V3 makes future product journeys debuggable and supportable.

## Next Product Tranche After V3

V1: Non-coder first-value journey hardening.

Bounded goal:

- A non-coder can enter a business request, receive a governed result,
  understand the receipt/evidence, export the deliverable pack, and continue
  one follow-up without needing to know CVF internals.

Likely scope:

- Use existing routed forms, result viewer, evidence receipt, deliverable pack,
  and continuity features.
- Add or repair only the smallest UI/workflow gaps discovered by a fresh
  browser proof.
- Measure time-to-first-value, evidence export, pack export, and follow-up
  continuity from one realistic journey.

Required guardrails:

- Read root `DESIGN.md` before UI work.
- Use live provider proof for any governance behavior claim.
- No new governance semantics.
- No new provider behavior.
- No memory reinjection or graph authority claim.
- No production/hosted readiness claim.

## Strong Alternate

V2: Evidence-to-action product packaging.

Bounded goal:

- Turn the existing receipt, benchmark, and deliverable-pack evidence into a
  clear user-facing "what happened / why it was allowed / what to do next"
  artifact.

This is attractive if the operator wants near-term demo clarity rather than new
runtime depth.

## Closure Update - 2026-05-24

Operator authorized Codex to process V1, V2, and V3 under the multi-role
workflow.

Disposition:

- V3 `CLOSED_PASS_BOUNDED`:
  `docs/reviews/CVF_V3_EXECUTION_DIAGNOSTIC_CONTRACT_COMPLETION_2026-05-24.md`
- V1 `CLOSED_PASS_BOUNDED`:
  `docs/reviews/CVF_V1_NONCODER_FIRST_VALUE_JOURNEY_HARDENING_COMPLETION_2026-05-24.md`
- V2 `CLOSED_PASS_BOUNDED`:
  `docs/reviews/CVF_V2_EVIDENCE_TO_ACTION_PACKAGING_COMPLETION_2026-05-24.md`

V3 delivered `cvf.executionDiagnostic.v1`, provider/route diagnostic mapping,
script rendering, and a live diagnostic proof with receipt
`rcpt-env-mpjiqzqg-v3k25r`, trace `env-mpjiqzqg-v3k25r`, diagnostic class
`model_unavailable`, and `userAction=change_model`.

V1 delivered non-coder first-value recovery hardening: classified live
execution failures now render an execution diagnostic panel and do not fall
back to mock output.

V2 delivered evidence-to-action packaging: copied/exported evidence receipts
now include "What happened", "Why this can be used", and "What to do next"
while preserving raw receipt fields and secret hygiene.

## Holds

Hold broad provider proof expansion. S2 is now clean enough for a bounded
claim. Additional runs should require a specific product or public claim that
the current `15/15` window does not support.

Hold model-specific proof loops. Qwen3 and provider-specific branches have
already produced useful boundary evidence; more work there should be
demand-triggered.

Hold F-1 tuning. The F-1 diminishing-returns stop rule remains binding.

## Non-Goals

- No broad provider stability expansion.
- No new provider or model proof loop.
- No governance-kernel semantic change.
- No new receipt envelope.
- No memory reinjection or graph authority claim.
- No public production-readiness claim.
- No public-sync change.

## Work Plan

1. Operator chooses V1, V2, or another screened candidate.
2. File fresh GC-018 and work order for the selected tranche.
3. If V1 is selected, read `DESIGN.md` before any UI/frontend change.
4. Execute the smallest product change that the selected proof requires.
5. Run targeted tests plus mandatory live governance proof for any governance
   behavior claim.
6. Close with bounded evidence and update session routing.

## Acceptance Criteria

- [ ] Operator-selected tranche has fresh GC-018 when required.
- [ ] Work order names exact target files and forbidden claims.
- [ ] Product value hypothesis is explicit before implementation.
- [ ] Evidence plan measures a user-visible outcome, not only internal proof
      count.
- [ ] Claim boundary blocks broad provider stability, hosted readiness,
      production readiness, memory reinjection, graph authority, and freeze
      release unless separately authorized.

## Verification / Evidence

This screening roadmap is verified by:

- S2 superseding completion:
  `docs/reviews/CVF_S2_PROVIDER_SOAK_HARDENING_COMPLETION_2026-05-24.md`
- active session state update:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- session memory update:
  `CVF_SESSION_MEMORY.md`

Future selected tranche must add its own completion evidence.

## Proposed Workflow

1. File fresh GC-018 for V1 or V2 after operator selection.
2. Create one work order with explicit pass/fail evidence.
3. Implement only gaps discovered by the journey proof.
4. Run targeted browser proof and mandatory live governance proof.
5. Close with claim boundary and update public-sync only if a public-safe claim
   changes.

## Current Recommendation

V1, V2, and V3 are closed for the bounded implementation scope above. The next
move should be a fresh value screen, not broad provider soaking, model-specific
proof loops, or F-1 tuning.

## Claim / Final / Verification Boundary

This roadmap claims bounded closure for V1, V2, and V3. It does not claim
universal provider stability, hosted readiness, production readiness, memory
reinjection, graph authority, public benchmark certification, or freeze
release.
