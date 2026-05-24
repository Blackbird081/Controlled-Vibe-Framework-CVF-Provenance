# CVF W1 Workflow State-Machine Enforcement Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-05-24

---

## Purpose

Close W1 by enforcing a bounded workflow state-machine projection for one
existing governed workflow so a downstream receipt-emission step is not
reported as completed after its upstream reviewer gate is deferred.

## Scope / Target / Owner Boundary

Target workflow:

- `workflow.product.create_product_brief.v1`

Target implementation:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/phase-e-workflow-binding.live.spec.ts`

Owner: Codex implementation under W1 work order.

Out of scope:

- route-level invalid-transition `BLOCK`;
- broad workflow engine;
- new receipt envelope;
- provider semantics;
- role taxonomy;
- auth/RBAC changes;
- memory reinjection;
- public-sync update;
- hosted/cloud persistence;
- production readiness;
- freeze release.

## Evidence Trace

Evidence Trace Block:

- Claim: the prior Product Brief projection could report step 5 as completed
  while step 4 reviewer gate was deferred.
- Command: `Get-Content` and focused test inspection of
  `workflow-resolver.ts`, `workflow-resolver.test.ts`, and
  `phase-e-workflow-binding.live.spec.ts`.
- Result: existing projection used active steps and excluded the deferred
  reviewer gate while still allowing receipt-emission obligations.
- Key path:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
- Verdict: EXISTS.
- Counter-evidence: none.

Evidence Trace Block:

- Claim: W1 now records the reachable workflow state and defers unreachable
  downstream steps.
- Command: `npm run test:run -- src/lib/workflows/workflow-resolver.test.ts src/app/api/execute/route.test.ts`
- Result: PASS, 2 files, 34 tests.
- Key path:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.test.ts`
- Verdict: EXISTS.
- Counter-evidence: no route-level pre-provider `BLOCK` was added by design.

Evidence Trace Block:

- Claim: live governance proof includes the bounded state-machine projection.
- Command:
  `npx playwright test --config playwright.config.ts tests/e2e/phase-e-workflow-binding.live.spec.ts --reporter=line`
- Result: PASS, 1 live test.
- Receipt: `rcpt-env-mpjx22ch-aee3y6`
- Workflow audit event: `c8d04faa-8474-4d02-beae-2c5519d179d2`
- Key path:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/phase-e-workflow-binding.live.spec.ts`
- Verdict: EXISTS.
- Counter-evidence: no trace/envelope id was present in the local
  `WORKFLOW_BINDING_EXECUTED` audit payload.

## Source / Predecessor Evidence

Authorization:

- `docs/baselines/CVF_GC018_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_2026-05-24.md`
- `docs/work_orders/CVF_WO_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_2026-05-24.md`

Predecessors:

- `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- `.private_reference/legacy/CVF Edit/CVF_EDIT_ANALYSIS.md`
- `.private_reference/legacy/CVF Edit/CVF AUDIT LOG_md`
- `.private_reference/legacy/CVF Edit/Failure Simulation cho CVF.md`
- `docs/reviews/CVF_WC1_WORKFLOW_CHAIN_PROOF_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_WC4_KNOWLEDGE_ABSORPTION_BLINDSPOT_STANDARD_COMPLETION_2026-05-24.md`

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - WC-3 map Candidate 1.
  - CVF Edit workflow/state-machine references.
  - Existing Product Brief workflow binding and route audit surfaces.
- Prior absorption evidence resolved:
  - WC-1 proved a live chain with existing surfaces.
  - WC-4 made source-level control mandatory before W-series work.
- Detailed source files used:
  - `.private_reference/legacy/CVF Edit/CVF_EDIT_ANALYSIS.md`
  - `.private_reference/legacy/CVF Edit/CVF AUDIT LOG_md`
  - `.private_reference/legacy/CVF Edit/Failure Simulation cho CVF.md`
  - `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
- Source families skipped:
  - memory/graph/tool/provider legacy families; reason: W1 is a workflow
    projection tranche only.
- File-level accepted value:
  - explicit transition replay;
  - defer downstream steps when an upstream state is unreachable;
  - expose workflow state in route audit payload.
- Owner-surface normalization:
  - normalized into workflow resolver projection, route audit metadata, tests,
    live proof, roadmap, session state, and handoff.
- Accept/defer/reject matrix:
  - `ACCEPT_NOW`: one Product Brief workflow state-machine projection.
  - `DEFER`: route-level invalid-transition `BLOCK`, reviewer runtime surface,
    recovery/rollback UX, and global workflow engine.
  - `REJECT_DIRECT`: copying legacy workflow architecture wholesale into CVF.
- Adversarial roles completed:
  - Legacy Source Extractor: Candidate 1 is the correct first W-series value.
  - Implementation Surface Scout: `workflow-resolver.ts` is the smallest
    owner surface.
  - Skeptic/Auditor: bounded projection is useful; broad engine claims must
    remain blocked.
- Thin proof target:
  - step 4 and step 5 are both deferred after reviewer gate deferral; only
    reachable completed steps emit receipts.
- Blind-spot verdict: CLEAR.

## Findings / Decisions

W1 adds `cvf.workflowStateMachineProjection.v1` to the existing workflow
execution projection. It records initial state, final state, completed step
ids, deferred step ids, waiting step ids, and per-step transition decisions.

For Product Brief execution, the reachable path now completes only:

- `step-1-intake-validation`
- `step-2-knowledge-retrieval`
- `step-3-provider-call`

The reviewer gate and receipt-emission step now remain deferred:

- `step-4-review-gate`
- `step-5-receipt-emit`

Receipts are emitted only for completed reachable steps. The route audit event
now includes `stateMachine` so live evidence readers can distinguish workflow
state from receipt obligations.

## Live Proof

Live Phase E workflow-binding proof:

- Command:
  `npx playwright test --config playwright.config.ts tests/e2e/phase-e-workflow-binding.live.spec.ts --reporter=line`
- Result: PASS, 1 passed.
- Receipt: `rcpt-env-mpjx22ch-aee3y6`
- Workflow audit event: `c8d04faa-8474-4d02-beae-2c5519d179d2`
- Final state: `review_pending`
- Completed steps:
  `step-1-intake-validation`, `step-2-knowledge-retrieval`,
  `step-3-provider-call`
- Deferred steps:
  `step-4-review-gate`, `step-5-receipt-emit`
- Waiting step: `step-5-receipt-emit`
- Raw secret printed: false.

Mandatory release gate:

- Command: `python scripts/run_cvf_release_gate_bundle.py --json`
- Result: PASS `7/7`.

## Verification

- Focused resolver and route tests:
  `npm run test:run -- src/lib/workflows/workflow-resolver.test.ts src/app/api/execute/route.test.ts`
  - PASS, 2 files, 34 tests.
- TypeScript check:
  `npm run check`
  - PASS.
- Live Phase E workflow-binding proof:
  `npx playwright test --config playwright.config.ts tests/e2e/phase-e-workflow-binding.live.spec.ts --reporter=line`
  - PASS, 1 passed.
- Mandatory release gate:
  `python scripts/run_cvf_release_gate_bundle.py --json`
  - PASS, 7/7.
- Docs/session guards before closure packet:
  - `python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce` PASS.
  - `python governance/compat/check_docs_governance_compat.py` PASS.
  - `python governance/compat/check_active_session_state.py` PASS.
  - `git diff --check` PASS.

## Blind Spots Closed / Open

Closed:

- step 5 no longer appears completed when step 4 reviewer gate is deferred;
- live workflow evidence now carries a state-machine projection;
- receipt emissions no longer imply completion of unreachable downstream
  steps.

Still open and demand-gated:

- route-level invalid-transition pre-provider `BLOCK`;
- full workflow engine;
- recovery/rollback UI;
- reviewer runtime surface;
- global workflow state enforcement;
- public product claim updates.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Reader mistakes receipt obligation for completed execution | Add state-machine projection and route audit metadata |
| Deferred reviewer gate is bypassed by downstream receipt emission | Defer unreachable downstream step 5 when step 4 is deferred |
| W1 is over-read as a broad workflow engine | Completion boundary limits claim to one Product Brief projection |
| Future memory/context work starts without source control | Next candidate remains demand-gated with WC-4 Control Block required |

## Decision / Recommendation / Disposition

Disposition: `CLOSED_PASS_BOUNDED`.

Recommendation: proceed next only by opening Candidate 2 from the WC-3 map with
a fresh GC-018/work order and a full Knowledge Absorption Blind-Spot Control
Block. Candidate 2 must preserve `canReinject=false` and avoid raw memory
prompt injection.

## Public Catalog

Public catalog update: N/A.

Reason: W1 is a private bounded runtime/evidence correction for one existing
workflow projection. It does not add a public capability or public-safe product
claim.

## Tranche Closure Checklist

- [x] Public catalog updated OR explicitly N/A: N/A, no public capability
      added.
- [x] All new catalog paths Test-Path verified in public-sync clone: N/A.
- [x] GC-020 handoff Current HEAD updated to this tranche's commit SHA: to be
      synced after commit.
- [x] Evidence Trace Block present for all significant claims (GC-046).
- [x] Legacy Spec Scan Block present OR explicitly N/A: covered by the
      Knowledge Absorption Blind-Spot Control Block.
- [x] Knowledge Absorption Blind-Spot Control Block present OR explicitly N/A:
      present.
- [x] Live-run diagnostics standard followed: no failed or unclear live rerun
      was repeated without classification; successful live proof recorded
      receipt and audit event.

## Claim Boundary

W1 claims only a bounded workflow state-machine projection for the selected
Product Brief workflow. It does not claim route-level invalid-transition
blocking, a broad workflow engine, recovery orchestration, reviewer UI, new
receipt-envelope semantics, provider behavior changes, auth/RBAC, memory
changes, public-sync updates, hosted readiness, production readiness, or freeze
release.
