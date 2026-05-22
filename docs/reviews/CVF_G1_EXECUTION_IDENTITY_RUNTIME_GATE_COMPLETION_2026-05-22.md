# CVF G1 Execution Identity Runtime Gate Completion

Memory class: FULL_RECORD

Status: CLOSED_G1_EXECUTION_IDENTITY_RUNTIME_GATE

Date: 2026-05-22

## Purpose

Close G1 from the post-B/C Review-CVF remaining pain-point roadmap by adding a
minimum viable runtime execution identity decision to the governed `/api/execute`
path.

## Scope / Target / Owner Boundary

Target: the existing `cvf-web` `/api/execute` path and its focused helper/test
surface.

Owner: Codex, acting as implementer, reviewer, and evidence owner under the
operator authorization to process the six remaining Review-CVF pain-point
phases in priority order.

Boundary: G1 does not create a new role taxonomy, auth/RBAC model, receipt
envelope, durable identity store, provider behavior, public-sync delta, hosted
claim, Maika proof, or freeze-release claim.

## Target / Source

Target artifact:

- G1 execution identity runtime gate on `/api/execute`

Source artifacts:

- `.private_reference/legacy/CVF 17.05/Review CVF.md`
- `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`
- `docs/roadmaps/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINT_ROADMAP_2026-05-22.md`
- `docs/reviews/CVF_REVIEW_CVF_POST_BC_ROADMAP_MULTI_ROLE_REBUTTAL_2026-05-22.md`
- `docs/baselines/CVF_GC018_G1_EXECUTION_IDENTITY_RUNTIME_GATE_2026-05-22.md`

## Scope / Methodology

Methodology:

- inspect the existing role resolver and actor-role gate;
- add the smallest runtime identity helper that reuses existing `CVFRole`
  values and governed-pack policy;
- wire helper output into response and audit payloads;
- prove allowed, denied, and unknown actor decisions with focused unit tests;
- prove governed-pack denial remains pre-provider with route tests.

## Authority Chain

- Original source oracle: `.private_reference/legacy/CVF 17.05/Review CVF.md`
- Assessment:
  `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`
- Roadmap:
  `docs/roadmaps/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINT_ROADMAP_2026-05-22.md`
- Rebuttal:
  `docs/reviews/CVF_REVIEW_CVF_POST_BC_ROADMAP_MULTI_ROLE_REBUTTAL_2026-05-22.md`
- GC-018:
  `docs/baselines/CVF_GC018_G1_EXECUTION_IDENTITY_RUNTIME_GATE_2026-05-22.md`
- Work order:
  `docs/work_orders/CVF_WO_G1_EXECUTION_IDENTITY_RUNTIME_GATE_2026-05-22.md`

## Delivered

- Added `cvf.executionIdentity.v1` runtime decision helper.
- Bound actor id, session role, resolved `CVFRole`, actor-role gate,
  output permission, context scope, execution boundary, and receipt ownership
  into one deterministic identity readout.
- Added identity readout to allowed `/api/execute` responses.
- Added identity readout to actor-role rejection, role-permission denial, and
  output-class denial paths.
- Added identity readout to workflow-binding and audit-memory audit payloads.
- Preserved pre-provider denial ordering for disallowed governed-pack actors.

## Findings / Position

Finding 1: the Review-CVF G pain point was still valid before this tranche
because runtime execution lacked one canonical identity readout tying actor,
authority, boundary, and receipt ownership together.

Finding 2: existing `CVFRole` and governed-pack `allowedActorRoles` were
sufficient for a minimum viable G1 close; a new taxonomy would have widened
scope without evidence need.

Finding 3: the correct closure path was response/audit readout, not mutation of
`GovernanceEvidenceReceipt`, because the receipt envelope is a separate
governance evidence contract.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| G1 becomes a new role taxonomy | Reused existing `CVFRole` only |
| G1 weakens pre-provider denial | Added route test asserting provider dispatch is not called |
| G1 mutates receipt envelope | Kept identity top-level and audit-payload only |
| Unknown actor path becomes permissive | Added deterministic unknown-role denial unit test |

## Evidence Trace Block

Files changed:

```text
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-identity.ts
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-identity.test.ts
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-permission-gate.ts
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.actor-gate.test.ts
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts
```

Focused verification:

```text
npm run test:run -- src/lib/execution-identity.test.ts src/lib/execute-role-resolver.test.ts src/app/api/execute/route.actor-gate.test.ts src/app/api/execute/route.test.ts
-> PASS, 4 files / 44 tests

npm run check
-> PASS
```

Governance verification:

```text
python governance/compat/run_local_governance_hook_chain.py
-> PASS, 43/43 checks
```

## Acceptance Criteria Result

| Criterion | Result |
| --- | --- |
| Allowed actor path includes execution identity readout | PASS |
| Denied actor path includes execution identity readout | PASS |
| Denied governed-pack actor does not call provider dispatch | PASS |
| Unknown actor path remains denied with deterministic identity | PASS |
| Audit payload includes execution identity | PASS |
| `GovernanceEvidenceReceipt` envelope remains unchanged | PASS |

## Decision / Recommendation / Disposition

Disposition: `CLOSED_G1_EXECUTION_IDENTITY_RUNTIME_GATE`.

Recommendation: continue the post-B/C remaining pain-point roadmap with D2
provider capability/method contract hardening next, but only after fresh
GC-018/work order and any required blocked-work override.

## Claim Boundary

G1 is closed for the existing `/api/execute` path only. This does not implement
a new role taxonomy, auth/RBAC redesign, planner/worker/reviewer job queues,
background worker identity, durable state, provider behavior changes,
receipt-envelope mutation, public-sync update, hosted readiness, Maika proof,
or freeze release.

Live provider proof was not required or run for this phase because the closed
claim is deterministic pre-provider identity gating and audit readout, not a
release-quality live governance behavior claim.
