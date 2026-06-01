# CVF Work Order - MKE1-E3 Memory Live Governance Proof

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

docType: work_order

Date: 2026-06-01

## Purpose

Implement the bounded MKE1-E3 proof-only seam and live governance proof so that setting `request.memoryGovernanceProof.revoked === true` deterministically produces eligibility state `REVOKED`, which the E1 gate maps to `BLOCK` before provider execution.

Success: `buildMemoryAdvisoryReadout` accepts proof fixture parameter; when fixture is present, `evaluateReadoutEligibility` receives `revoked:true` and `authoritySourcePresent:true`; eligibility state is `REVOKED` with reason `memory_readout_access_revoked`; non-proof requests are unchanged; live Playwright spec passes HTTP 400 with `success:false`, `model:blocked`, `enforcement.status:BLOCK`, `enforcement.reasons` contains `memory_access_revoked`; release gate bundle PASS; all governance gates PASS; files remain pending/uncommitted.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-01 request to execute committed MKE1 roadmap | ACCEPT |
| MKE1 roadmap | `docs/roadmaps/CVF_MKE1_MEMORY_ENFORCEMENT_ROADMAP_2026-06-01.md` | ACCEPT |
| MKE1-E3 GC-018 | `docs/baselines/CVF_GC018_MKE1_E3_MEMORY_LIVE_GOVERNANCE_PROOF_2026-06-01.md` | ACCEPT |
| MKE1-E1 completion | `docs/reviews/CVF_MKE1_E1_MEMORY_ENFORCEMENT_GATE_WIREIN_COMPLETION_2026-06-01.md` | ACCEPT |
| MKE1-E2 completion | `docs/reviews/CVF_MKE1_E2_MEMORY_DURABLE_WRITE_ROUTE_COMPLETION_2026-06-01.md` | ACCEPT |
| Memory contract | `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | ACCEPT |
| Live diagnostic standard | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | ACCEPT |
| Worker autonomy standard | `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | Dispatch E3 after GC-018 exists and gates pass | no E1/E2 scope re-opening |
| Worker | Implement proof seam + focused tests + live spec + release bundle wire + completion review | no durable write route changes, no public-sync, no commit, no push |
| Reviewer | Verify REVOKED path, invariants, live spec correctness, and gates | reject any seam that can produce ALLOW from revoked state |

## Scope

Allowed scope:

- modify `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.ts` additively: add `MemoryGovernanceProofRequest` type, `hasRevokedProofFixture` function, modify `evaluateEligibility` signature, modify `buildMemoryAdvisoryReadout` to detect proof fixture;
- modify `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.test.ts` to add focused non-live proof test;
- create `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/mke1-memory-governance-live.spec.ts`;
- modify `scripts/run_cvf_release_gate_bundle.py` to add `mke1-memory-governance-live.spec.ts` to live governance spec list;
- create `docs/reviews/CVF_MKE1_E3_MEMORY_LIVE_GOVERNANCE_PROOF_COMPLETION_2026-06-01.md`;
- run listed gates and repair allowed-scope defects.

Forbidden scope:

- modifying `/api/execute/route.ts` unless a source-verified route defect blocks E3 proof;
- modifying `/api/memory/write` or any E2 route files;
- any seam that turns a denied or revoked state into ALLOW;
- live provider calls before focused non-live tests pass;
- public-sync, push, or commit;
- raw Memory content release;
- prompt injection or Memory reinjection;
- graph persistence mutation;
- production/hosted/public readiness claims.

Risk ceiling: R2 bounded proof-only seam with live E2E verification.

## Required First Reads

- `docs/baselines/CVF_GC018_MKE1_E3_MEMORY_LIVE_GOVERNANCE_PROOF_2026-06-01.md`
- `docs/roadmaps/CVF_MKE1_MEMORY_ENFORCEMENT_ROADMAP_2026-06-01.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-readout-eligibility-policy.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base 08c1b54f --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 08c1b54f --head HEAD
```

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `MemoryReadoutEligibilityInput.revoked` is a boolean field | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-readout-eligibility-policy.ts` | line 21 | `MemoryReadoutEligibilityInput.revoked` | `MemoryReadoutEligibilityInput` | ACCEPT |
| `REVOKED` is a valid eligibility state | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-readout-eligibility-policy.ts` | line 11 | `MemoryReadoutEligibilityState` | `MemoryReadoutEligibilityState` | ACCEPT |
| `evaluateEligibility` in route-memory-advisory.ts supplies the revoked parameter to the eligibility policy | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.ts` | line 109 | `evaluateEligibility` | `evaluateEligibility` | ACCEPT |
| `buildMemoryAdvisoryReadout` is the public export | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.ts` | line 114 | `buildMemoryAdvisoryReadout` | `buildMemoryAdvisoryReadout` | ACCEPT |
| Execute route passes eligibility to enforcement | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 352 | `buildMemoryAdvisoryReadout` | execute route | ACCEPT |
| BLOCK response returns HTTP 400 with enforcement and error | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts` | lines 65-67 | `EnforcementResult.status` | `EnforcementResult` | ACCEPT |
| `enforcement.reasons` appears in BLOCK response error field | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts` | line 67 | `EnforcementResult.reasons` | `EnforcementResult` | ACCEPT |
| `REVOKED` literal in advisory test file | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.test.ts` | No (produced during execution) | `buildMemoryAdvisoryReadout` | test assertion | ACCEPT |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Proof seam for REVOKED state | Scope (allowed) | `route-memory-advisory.ts` modified | non-live test PASS | Produced during execution |
| Focused non-live test for seam | Scope (allowed) | `route-memory-advisory.test.ts` modified | vitest PASS | Produced during execution |
| Live Playwright E2E spec | Scope (allowed) | `mke1-memory-governance-live.spec.ts` created | Playwright PASS | Produced during execution |
| Release bundle includes E3 spec | Scope (allowed) | `run_cvf_release_gate_bundle.py` modified | bundle PASS | Produced during execution |
| E3 completion review | Scope (allowed) | completion review created | governance gates PASS | Produced during execution |

## Worker Autonomy / No-Question Rule

Non-destructive read, check, and gate actions inside Allowed scope proceed without operator confirmation. This includes reading named files, running git status/diff/rev-parse, running markdown/dispatch/autorun/closure gates, fixing documentation format defects inside Allowed scope, and rerunning failed gates after allowed-scope remediation.

Escalation is required only if the next action would: edit runtime/source code outside Allowed scope; run live/provider/API proof; use secrets, quota, or paid external services; public-sync, push, or publish; change claim boundary, risk level, or release a HOLD prerequisite; touch forbidden paths; perform destructive or irreversible actions.

## 6D. Pending Artifact Evidence Finality

Do not commit. Record actual `git status --short`. Do not cite committed-only or empty ranges as proof for pending E3 files.

## 6F. Near-Threshold Owner Maintainability Plan

Active owner entrypoint: `route-memory-advisory.ts`. Current implementation is under 150 lines. Seam must remain additive; if advisory builder grows above 250 lines, extract proof-seam logic to `route-memory-advisory-proof.ts`.

## 6G. Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.ts` | Yes | proof seam implementation |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.test.ts` | Yes | focused non-live proof test |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/mke1-memory-governance-live.spec.ts` | No (produced during execution) | live Playwright spec |
| `scripts/run_cvf_release_gate_bundle.py` | Yes | live governance spec wired |
| `docs/reviews/CVF_MKE1_E3_MEMORY_LIVE_GOVERNANCE_PROOF_COMPLETION_2026-06-01.md` | No (produced during execution) | completion review |

## Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | no source-verified defect found; E1 already wires enforcement |
| public-sync clone | out of E3 scope |

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| REVOKED state produced by seam | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.test.ts` | `REVOKED` | No (produced during execution) |
| rawMemoryReleased invariant | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.test.ts` | `rawMemoryReleased` | Yes |
| Live BLOCK proof | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/mke1-memory-governance-live.spec.ts` | `memory_access_revoked` | No (produced during execution) |

## 7. Write Ownership

Owned: `route-memory-advisory.ts` (additive seam), `route-memory-advisory.test.ts` (additional test), `mke1-memory-governance-live.spec.ts` (new live spec), `run_cvf_release_gate_bundle.py` (additive wire), completion review.

Forbidden: `route.ts` enforcement changes, durable write route, live proof before non-live tests pass, public-sync, unrelated route/provider/routing behavior, commits, pushes.

Write mode: bounded additive proof seam and tests only.

## Execution Plan

1. Verify filesystem state: confirm GC-018 and WO exist and all missing files are identified.
2. Implement proof seam in `route-memory-advisory.ts`: add `MemoryGovernanceProofRequest` type, `hasRevokedProofFixture` function, update `evaluateEligibility` to accept `proofRevoked: boolean`, update `buildMemoryAdvisoryReadout` to pass `hasRevokedProofFixture(params.request)`.
3. Add focused non-live test in `route-memory-advisory.test.ts` asserting `state: REVOKED`, `rawMemoryReleased: false`, `canReinject: false`.
4. Create live Playwright spec `tests/e2e/mke1-memory-governance-live.spec.ts`.
5. Add spec to `scripts/run_cvf_release_gate_bundle.py` live governance spec list.
6. Run TypeScript check and focused non-live tests.
7. Verify files exist on filesystem before running live spec.
8. Run targeted live Playwright spec.
9. Run release gate bundle.
10. Run all final governance gates.
11. File completion review.

## Evidence Requirements

- `npm --prefix "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web" run check` output PASS
- `npm run test:run -- src/app/api/execute/route-memory-advisory.test.ts src/lib/enforcement.test.ts` output showing REVOKED assertion PASS
- `npx playwright test tests/e2e/mke1-memory-governance-live.spec.ts` output PASS
- `python scripts/run_cvf_release_gate_bundle.py --json` output with gate_result PASS
- All governance gate commands PASS

## Acceptance Criteria

- `buildMemoryAdvisoryReadout` with `memoryGovernanceProof: { revoked: true }` returns `eligibility.state === 'REVOKED'`.
- `rawMemoryReleased` and `canReinject` are both `false` in all proof and non-proof paths.
- Non-proof requests continue to produce non-REVOKED eligibility states.
- Live Playwright spec confirms HTTP 400, `success:false`, `model:blocked`, `enforcement.status:BLOCK`, `enforcement.reasons` contains `memory_access_revoked`, no provider output.
- Release gate bundle PASS with E3 spec in live governance suite.
- All governance gates PASS.
- No raw Memory sentinel in any output.
- Files confirmed to exist on filesystem before completion review is filed.

## Review Gate

E3 may be returned for review after all tests and gates pass and completion review is filed. No further MKE1 tranche work is pending after E3.

## Closure Checklist

Worker must not close or commit. Return pending implementation and review packet for orchestrator/reviewer.

## Return-To-Orchestrator Conditions

Return if implementing E3 requires modifying `/api/execute/route.ts` without source-verified defect, durable write route changes, live proof before non-live tests pass, public-sync, raw Memory release, prompt reinjection, or destructive actions.

## Operator Checkpoint

Operator requested execution of the committed MKE1 roadmap. E3 is the final tranche and depends on E1 enforcement gate. E2 durable write route may be reviewed in parallel.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private bounded proof-only seam and live governance proof artifact. No public-sync remote, public repository commit, public artifact path, hosted proof, or public README claim is included.

## Claim Boundary

E3 claims only: bounded proof-only seam exists in `route-memory-advisory.ts`; REVOKED state triggered by fixture produces BLOCK before provider execution; live E2E spec confirms this behavior; release gate bundle confirms release-quality evidence.

E3 does not claim: production Memory enforcement, durable write production stability, general Memory eligibility parity, public-sync, commit, push, hosted readiness, or public readiness.
