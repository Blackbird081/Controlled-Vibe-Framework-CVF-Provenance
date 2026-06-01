# CVF Work Order - MKE1-E1 Memory Enforcement Gate Wire-In

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

docType: work_order

Date: 2026-06-01

## Purpose

Implement the bounded MKE1-E1 enforcement wire-in so the existing `/api/execute` enforcement gate blocks execution when Memory readout eligibility is `REVOKED` or `READOUT_DENIED`.

Success: `memoryEligibility` is available to `evaluateEnforcement`, `REVOKED` maps to `BLOCK` reason `memory_access_revoked`, `READOUT_DENIED` maps to `BLOCK` reason `memory_readout_denied`, advisory-only states remain non-blocking, route advisory output is preserved, required tests and gates pass, and all files remain pending/uncommitted.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-01 request to execute committed MKE1 roadmap | ACCEPT |
| MKE1 roadmap | `docs/roadmaps/CVF_MKE1_MEMORY_ENFORCEMENT_ROADMAP_2026-06-01.md` | ACCEPT |
| MKE1-E1 GC-018 | `docs/baselines/CVF_GC018_MKE1_E1_MEMORY_ENFORCEMENT_GATE_WIREIN_2026-06-01.md` | ACCEPT |
| MKG7 T7 decision | `docs/reviews/CVF_MKG7_T7_MEMORY_LIVE_PROOF_DECISION_2026-06-01.md` | ACCEPT |
| Memory contract | `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | ACCEPT |
| Worker autonomy standard | `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | Dispatch E1 after GC-018 exists and gates pass | no E2/E3 scope expansion |
| Worker | Implement bounded enforcement input + route wire-in + tests + completion review | no durable write route, live proof, public-sync, commit, or push |
| Reviewer | Verify exact block states, route ordering, safety invariants, and gates | reject accidental broader Memory enforcement |

## Scope

Allowed scope:

- modify `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts` additively;
- modify `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.test.ts` for focused Memory eligibility tests;
- modify `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` to compute Memory advisory/eligibility before `evaluateEnforcement`, pass `memoryEligibility`, and preserve ALLOW advisory response;
- modify `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.ts` only if needed for bounded testable eligibility injection;
- modify `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.test.ts` for focused route/advisory assertions;
- create `docs/reviews/CVF_MKE1_E1_MEMORY_ENFORCEMENT_GATE_WIREIN_COMPLETION_2026-06-01.md`;
- run listed gates and repair allowed-scope defects.

Forbidden scope:

- `POST /api/memory/write` or any durable write route work;
- live/provider proof execution;
- public-sync, push, or commit;
- raw Memory content release;
- prompt injection or Memory reinjection;
- graph persistence mutation;
- new role taxonomy;
- blocking `NO_AUTHORITY_SOURCE`, `OUT_OF_SCOPE_FOR_ACTOR`, or `STALE_NEEDS_REFRESH` in E1;
- modifying unrelated route/provider/routing/enforcement behavior outside Memory eligibility gating.

Risk ceiling: R2 local deterministic enforcement; E3 live proof remains separate.

## Required First Reads

- `docs/baselines/CVF_GC018_MKE1_E1_MEMORY_ENFORCEMENT_GATE_WIREIN_2026-06-01.md`
- `docs/roadmaps/CVF_MKE1_MEMORY_ENFORCEMENT_ROADMAP_2026-06-01.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-readout-eligibility-policy.ts`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base 6ca730da --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 6ca730da --head HEAD
python governance/compat/check_execute_route_step_sequence.py --enforce
python governance/compat/check_governed_file_size.py --enforce
```

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `EnforcementInput` exists and has no memory field yet | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts` | lines 34-61 | `EnforcementInput` | `EnforcementInput` | ACCEPT |
| `evaluateEnforcement` owns local enforcement status | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts` | lines 118-177 | `evaluateEnforcement` | `evaluateEnforcement` | ACCEPT |
| Execute route calls enforcement before provider execution | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 343-358 | `evaluateEnforcement` | execute route | ACCEPT |
| Existing BLOCK path returns status 400 with receipt | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 360-386 | `enforcement` | execute route | ACCEPT |
| Current advisory readout runs after execution | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 822-824 | `memoryAdvisoryReadout` | execute route | ACCEPT |
| `REVOKED` exists in eligibility policy | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-readout-eligibility-policy.ts` | line 11 | `REVOKED` | `MemoryReadoutEligibilityState` | ACCEPT |
| `READOUT_DENIED` exists in eligibility policy | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-readout-eligibility-policy.ts` | line 9 | `READOUT_DENIED` | `MemoryReadoutEligibilityState` | ACCEPT |
| Eligibility invariants exist | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-readout-eligibility-policy.ts` | lines 25-31 | `rawMemoryReleased`, `canReinject` | `MemoryReadoutEligibilityResult` | ACCEPT |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Add `memoryEligibility` to `EnforcementInput` | Scope + Execution Plan | `enforcement.ts` | focused tests + TypeScript | DISPATCHED |
| Move eligibility before enforcement | Scope + Execution Plan | `route.ts` | execute-route sequence guard + route test | DISPATCHED |
| Block `REVOKED` and `READOUT_DENIED` | Acceptance Criteria | `evaluateEnforcement` branch | focused tests | DISPATCHED |
| Preserve advisory states as non-blocking | Acceptance Criteria | `evaluateEnforcement` tests | focused tests | DISPATCHED |
| Preserve advisory readout in ALLOW response | Acceptance Criteria | route/advisory test | focused test | DISPATCHED |

## 6C. Worker Autonomy / No-Question Rule

Proceed autonomously with reading source files, implementing allowed-scope code/test changes, running gates, and repairing allowed-scope gate failures. Ask only for scope expansion, forbidden path edits, live/provider proof, public-sync, secrets/quota, push, commit, or destructive actions.

## 6D. Pending Artifact Evidence Finality

Do not commit. Record actual `git status --short`. Do not cite committed-only or empty ranges as proof for pending E1 files.

## 6F. Near-Threshold Owner Maintainability Plan

Active owner entrypoint: `route.ts`, current physical count 861 lines. Keep below hard threshold 1000 and avoid multi-statement compression. If route growth becomes material, extract same-owner Memory preflight logic to `route-memory-preflight.ts` before continuing.

## 6G. Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts` | Yes | enforcement input + block branch |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.test.ts` | Yes | focused Memory enforcement tests |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | Yes | pre-enforcement Memory advisory/eligibility wiring |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.test.ts` | Yes | focused route/advisory tests |
| `docs/reviews/CVF_MKE1_E1_MEMORY_ENFORCEMENT_GATE_WIREIN_COMPLETION_2026-06-01.md` | No (produced during execution) | completion review |

## Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/**` | E2 only |
| `scripts/run_cvf_release_gate_bundle.py` execution | E3 live proof only |
| public-sync clone | out of E1 scope |

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| REVOKED blocks | `enforcement.test.ts` | `memory_access_revoked` | Yes |
| READOUT_DENIED blocks | `enforcement.test.ts` | `memory_readout_denied` | Yes |
| Advisory-only state allowed | `enforcement.test.ts` | `NO_AUTHORITY_SOURCE` | Yes |
| ALLOW response advisory preserved | route/advisory test | `memoryAdvisoryReadout` | Yes |

## 7. Write Ownership

Owned: E1 files listed in Allowed scope and completion review.

Forbidden: durable write route, live proof, public-sync, unrelated route/provider/routing behavior, commits, pushes.

Write mode: bounded additive implementation and tests.

## 8. Execution Plan

1. Capture `baseHead` and current git status.
2. Run dispatch/pre-implementation gates after this work order exists.
3. Add optional `memoryEligibility` to `EnforcementInput` with the existing eligibility result type.
4. Add local `evaluateEnforcement` branch: `REVOKED` and `READOUT_DENIED` block with required reasons; advisory-only states remain non-blocking.
5. Move `buildMemoryAdvisoryReadout` before `evaluateEnforcement` in `route.ts`; pass `memoryAdvisoryReadout.eligibility` into enforcement and reuse the same advisory in ALLOW response.
6. If needed, add a bounded test seam to `route-memory-advisory.ts` so tests can construct revoked/denied eligibility without raw Memory release.
7. Add focused tests and run TypeScript/test/route/file-size gates.
8. File completion review and leave all changes pending/uncommitted.

## Evidence Requirements

- `git rev-parse --short HEAD`
- `git status --short`
- `python governance/compat/check_work_order_dispatch_quality.py --base 6ca730da --head HEAD --enforce` PASS
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 6ca730da --head HEAD` PASS
- `npm run check` from `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` PASS
- focused enforcement tests PASS
- focused route/advisory tests PASS
- `python governance/compat/check_execute_route_step_sequence.py --enforce` PASS
- `python governance/compat/check_governed_file_size.py --enforce` PASS
- `python governance/compat/check_public_export_disposition.py --base 6ca730da --head HEAD --enforce` PASS
- `python governance/compat/check_finding_to_governance_learning.py --base 6ca730da --head HEAD --enforce` PASS

## 10. Acceptance Criteria

- [ ] `EnforcementInput` includes optional `memoryEligibility`
- [ ] `REVOKED` causes `status === 'BLOCK'` and includes `memory_access_revoked`
- [ ] `READOUT_DENIED` causes `status === 'BLOCK'` and includes `memory_readout_denied`
- [ ] `NO_AUTHORITY_SOURCE` remains non-blocking
- [ ] `OUT_OF_SCOPE_FOR_ACTOR` remains non-blocking
- [ ] `STALE_NEEDS_REFRESH` remains non-blocking
- [ ] route computes Memory advisory/eligibility before `evaluateEnforcement`
- [ ] ALLOW response still includes `memoryAdvisoryReadout`
- [ ] `rawMemoryReleased:false` and `canReinject:false` preserved
- [ ] cvf-web TypeScript check PASS
- [ ] focused tests PASS
- [ ] execute-route step-sequence guard PASS
- [ ] governed file-size guard PASS

Fail conditions:

- [ ] Any live provider call executed in E1
- [ ] Durable write route implemented in E1
- [ ] Raw Memory content released
- [ ] Prompt reinjection or Memory reinjection added
- [ ] Advisory-only states blocked without new authorization
- [ ] Worker commits or pushes

## 11. Review Gate

E1 may be returned for review after tests/gates pass and completion review is filed. E2 remains blocked until E1 completion evidence is available.

## 12. Closure Checklist

N/A: worker must not close or commit. Return pending implementation and review packet for orchestrator/reviewer.

## 13. Return-To-Orchestrator Conditions

Return if implementing E1 requires live proof, durable route work, public-sync, raw Memory release, prompt reinjection, blocking additional Memory states, or modifying unrelated provider/routing behavior.

## Operator Checkpoint

Operator requested execution of the committed MKE1 roadmap. E1 is the first tranche and is required before E2/E3.

## Worker Dispatch Prompt

```text
You are assigned MKE1-E1 Memory Enforcement Gate Wire-In.

Primary work order:
docs/work_orders/CVF_WO_MKE1_E1_MEMORY_ENFORCEMENT_GATE_WIREIN_2026-06-01.md

Critical rules:
- implement only E1;
- add optional memoryEligibility to EnforcementInput;
- block only REVOKED and READOUT_DENIED;
- keep NO_AUTHORITY_SOURCE, OUT_OF_SCOPE_FOR_ACTOR, and STALE_NEEDS_REFRESH non-blocking;
- move advisory/eligibility before evaluateEnforcement and preserve ALLOW memoryAdvisoryReadout;
- do not implement E2 durable write route;
- do not run live provider proof;
- do not commit or push.

Worker Autonomy Rule: repair allowed-scope doc/code gate failures without asking.
Pending Artifact Rule: record actual git status; leave changes pending.
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private bounded E1 implementation only; no public-sync remote, public repository commit, public artifact path, hosted proof, or public README claim is included.

## Claim Boundary

E1 authorizes deterministic local Memory eligibility enforcement only. It does not authorize live/provider proof, durable write route work, public-sync, raw Memory release, prompt injection, Memory reinjection, graph mutation, autonomous durable mutation, production readiness, hosted readiness, or public readiness.
