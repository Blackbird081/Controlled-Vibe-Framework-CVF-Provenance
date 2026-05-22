# CVF GC-018 G1 Execution Identity Runtime Gate

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_G1_EXECUTION_IDENTITY_RUNTIME_GATE

Date: 2026-05-22

## Source or Predecessor Evidence

- `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`
- `docs/roadmaps/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINT_ROADMAP_2026-05-22.md`
- `docs/reviews/CVF_REVIEW_CVF_POST_BC_ROADMAP_MULTI_ROLE_REBUTTAL_2026-05-22.md`
- `.private_reference/legacy/CVF 17.05/Review CVF.md`

## Purpose / Decision / Baseline

Authorize G1, the first post-B/C remaining pain-point implementation phase:
execution identity runtime minimum viable gate.

Decision: proceed with a bounded implementation that uses existing `CVFRole`
values and existing governed pack `allowedActorRoles` policy. No new role
taxonomy or auth model is authorized.

## Decision / Baseline / Proposed Tranche

Baseline: existing `/api/execute` already resolves app RBAC role to `CVFRole`,
checks governed-pack `allowedActorRoles`, and denies disallowed actors before
provider dispatch.

Proposed tranche: add a minimum viable execution identity readout that binds
the existing role and policy facts into one deterministic decision without
widening authority.

## Scope / Proposed Tranche

In scope:

- add a runtime execution identity contract;
- bind session actor, resolved CVF role, actor-role gate, output permission,
  context scope, execution boundary, and receipt ownership into one decision;
- expose execution identity decision through `/api/execute` response payload
  and audit payloads;
- keep denial before provider dispatch;
- test allowed, denied, and unknown actor cases.

Out of scope:

- new role taxonomy;
- planner/worker/reviewer/auditor job queues;
- auth/RBAC redesign;
- provider behavior changes;
- route ownership changes beyond the existing `/api/execute` owner;
- `GovernanceEvidenceReceipt` envelope changes;
- durable state, memory hierarchy expansion, public-sync, hosted readiness, or
  freeze release.

## Evidence / Required Evidence / Verification

Required evidence:

- execution identity unit tests covering allowed, denied, and unknown actor
  cases;
- route actor-gate test proving provider dispatch is not called on denied
  actor;
- targeted route tests still pass;
- `npm run check` for `cvf-web`;
- local governance hook chain before final commit.

Live provider proof:

- Not required for this phase because the claim is deterministic pre-provider
  identity gating and audit readout.
- If a later G phase asserts live governance behavior, use
  `python scripts/run_cvf_release_gate_bundle.py --json`.

## Claim Boundary / Approval Gate

This GC-018 authorizes only G1's minimum viable runtime identity decision on
the existing `/api/execute` path. It does not close full multi-agent identity,
background worker identity, planner/reviewer orchestration, auth model
redesign, receipt-envelope mutation, or public release readiness.

Blocked-work override: not required because this phase stays within existing
`CVFRole` values and does not introduce new role taxonomy or new governance
actor semantics.
