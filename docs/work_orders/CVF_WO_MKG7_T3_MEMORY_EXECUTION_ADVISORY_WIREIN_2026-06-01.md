# CVF Work Order - MKG7-T3 Memory Execution Advisory Wire-In

Memory class: FULL_RECORD

Status: HOLD_UNTIL_T2_PASS

docType: work_order

Date: 2026-06-01

## Purpose

Wire a compact, advisory-only Memory readout field into the `/api/execute`
governed execution response. The advisory is built by a new helper module
`route-memory-advisory.ts`, is additive in the ALLOW response envelope, and
must not modify the existing durable-memory or AIF-memory-reinjection paths
(lines 637–646 @ `route.ts`). Route must stay at or below its current 858 lines.

Success: new helper module exists with tests, ALLOW response includes advisory
field, existing memory paths untouched, route ≤ 858 lines, TypeScript check
PASS, file-size guard PASS, execute-route step-sequence guard PASS, all files
left pending and uncommitted.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-01 dispatch MKG7 T2–T7 for worker execution | ACCEPT |
| MKG7-T3 GC-018 | `docs/baselines/CVF_GC018_MKG7_T3_MEMORY_EXECUTION_ADVISORY_WIREIN_2026-06-01.md` | ACCEPT |
| MKG7 roadmap | `docs/roadmaps/CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md` | ACCEPT |
| T1 contract | `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | ACCEPT |
| Worker autonomy standard | `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md` | ACCEPT |

Prerequisite: T2 must be complete before T3 is executed (T3 uses the T2
eligibility policy).

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch after T2 complete; review pending output | no silent scope expansion |
| Worker | implement advisory helper + route wire-in + tests | no modification to existing memory paths, no commit |
| Reviewer | verify existing paths untouched, advisory-only, route ≤ 858 lines | reject if durable/AIF paths modified |

## Scope

Allowed scope:

- create `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.ts`;
- create `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.test.ts`;
- modify `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` — additive advisory field only, must stay ≤ 858 lines; if growth needed, extract helper first (min 50-line shrink);
- create `docs/reviews/CVF_MKG7_T3_MEMORY_EXECUTION_ADVISORY_WIREIN_COMPLETION_2026-06-01.md`;
- run listed gates and fix allowed-scope defects.

Forbidden scope:

- any modification to existing memory paths in `route.ts` (lines 637–646: `evaluateDurableMemoryRoute`, `evaluateAifMemoryReinjection`, `buildAifMemoryReinjectionSystemPrompt`);
- growing `route.ts` beyond 858 lines without prior helper extraction;
- enforcement behavior (advisory → policy gate) — requires separate GC-018;
- raw Memory release; prompt injection; provider calls; persistence mutation;
- public-sync, push, or commit.

Risk ceiling: R2 — bounded local route integration.

## Required First Reads

- `docs/baselines/CVF_GC018_MKG7_T3_MEMORY_EXECUTION_ADVISORY_WIREIN_2026-06-01.md`
- `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` — understand existing memory paths at lines 637–646
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` — advisory projection helper
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-readout-eligibility-policy.ts` — T2 output (must exist)

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base 5e55714d --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 5e55714d --head HEAD
python governance/compat/check_execute_route_step_sequence.py --enforce
```

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Execute route line count | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | physical count | 858 lines | execute route | ACCEPT |
| Existing durable memory path (must not be modified) | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 637–638 | `evaluateDurableMemoryRoute` | execute route | ACCEPT |
| Existing AIF reinjection path (must not be modified) | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 639–646 | `evaluateAifMemoryReinjection` | execute route | ACCEPT |
| Advisory projection builder | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | `buildMemoryRuntimeReadout` | `buildMemoryRuntimeReadout` | readout projection | ACCEPT |
| Readout response invariants | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 202–203 | `rawMemoryReleased` | readout route | ACCEPT |
| T2 eligibility policy (prerequisite) | DOC_ONLY_NEW | canonical-contract: T2 work order output | T2 completion review | `evaluateReadoutEligibility` | T2 policy | ACCEPT |

New doc-only fields:

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
| --- | --- | --- | --- | --- |
| `memoryAdvisoryReadout` | advisory-only field in ALLOW response envelope | Yes | Yes | focused route test only |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Advisory Memory readout in execute response | Execution Plan step 3 | `memoryAdvisoryReadout` field in ALLOW response | focused route test | DISPATCHED |
| Helper-first, route stays under threshold | Scope + Near-Threshold Plan | route ≤ 858 lines | `wc -l route.ts` | DISPATCHED |
| Existing memory paths untouched | Forbidden scope | no diff on lines 637–646 | `git diff route.ts` | DISPATCHED |
| Advisory-only boundary | Claim Boundary | advisory field, no enforcement | reviewer diff check | DISPATCHED |

## 6C. Worker Autonomy / No-Question Rule

Proceed autonomously with reading files, creating helper + test, additive route
edit, running gates, and fixing allowed-scope defects. Ask only for scope
expansion, forbidden-path edits, live proof, secrets, push, commit, or
destructive actions.

## 6D. Pending Artifact Evidence Finality

Do not commit. Record actual `git status --short`. Do not cite a committed-only
or empty range as proof for pending files.

## 6F. Near-Threshold Owner Maintainability Plan

Active owner entrypoint: `route.ts`, current 858 lines, hard threshold 1000.
If adding the advisory field would push route.ts above 858 lines, extract 50+
lines of stable logic into a new helper under `src/app/api/execute/` first, then
add the advisory field. Command-backed post-change line count required.

## 6G. Work-Order Fulfillment Manifest

### Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.ts` | Yes | advisory builder helper |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.test.ts` | Yes | focused tests |
| `docs/reviews/CVF_MKG7_T3_MEMORY_EXECUTION_ADVISORY_WIREIN_COMPLETION_2026-06-01.md` | Yes | pending completion review |

### Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `route.ts` lines 637–646 | existing durable/AIF memory paths — must not be modified |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-response-readouts.ts` | explicitly forbidden |

### Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| Advisory field present in ALLOW response | test file | `memoryAdvisoryReadout` | Yes |
| `rawMemoryReleased=false` in advisory | test file | `rawMemoryReleased` | Yes |
| `canReinject=false` in advisory | test file | `canReinject` | Yes |

## 7. Write Ownership

Owned: `route-memory-advisory.ts`, test file, additive change to `route.ts`, completion review.
Forbidden: `route-response-readouts.ts`, `route.ts` lines 637–646, any other existing route file.
Write mode: create new helpers; additive field only in `route.ts`.

## 8. Execution Plan

1. Capture `baseHead` and git status. Run pre-flight gates.
2. Read `route.ts` lines 630–700 to understand existing memory path context.
3. Create `route-memory-advisory.ts` that builds a compact advisory object using `buildMemoryRuntimeReadout` and `evaluateReadoutEligibility`; output includes eligibility state, summary projection, `rawMemoryReleased:false`, `canReinject:false`.
4. Add `memoryAdvisoryReadout` field to ALLOW response envelope in `route.ts` (additive only). Verify route stays ≤ 858 lines.
5. Create focused tests: advisory present, invariants asserted, existing memory path receipts unaffected.
6. Run `npm run check` from cvf-web. Run execute-route step-sequence guard. Run file-size guard.
7. Create pending completion review.
8. Leave all files pending and uncommitted.

## Evidence Requirements

- `npm run check` from cvf-web — PASS;
- `python governance/compat/check_execute_route_step_sequence.py --enforce` — PASS;
- `python governance/compat/check_governed_file_size.py --enforce` — PASS;
- `wc -l route.ts` confirming ≤ 858 lines;
- `git diff --name-status` confirming no edits to forbidden paths;
- actual `git status --short`.

## 10. Acceptance Criteria

- [ ] `route-memory-advisory.ts` exists with advisory builder
- [ ] ALLOW response includes `memoryAdvisoryReadout` field
- [ ] Advisory field carries `rawMemoryReleased=false` and `canReinject=false`
- [ ] `route.ts` lines 637–646 unchanged (verified with `git diff`)
- [ ] `route.ts` ≤ 858 lines after change
- [ ] cvf-web `npm run check` PASS
- [ ] Execute-route step-sequence guard PASS
- [ ] File-size guard PASS

Fail conditions:

- [ ] Any modification to existing durable/AIF memory paths
- [ ] Route grows beyond 858 lines without prior helper extraction
- [ ] Advisory field changes provider routing or enforcement behavior
- [ ] Worker commits or asks whether to fix an allowed-scope gate failure

## 11. Review Gate

T2 must be complete. Pre-implementation autorun gate must pass. Closure by
orchestrator after reviewer no-blocking objection and `pre-closure` gate.

## 12. Closure Checklist

N/A: worker must not close or commit T3. Return pending files for orchestrator.

## 13. Return-To-Orchestrator Conditions

Return if: T2 eligibility policy does not exist; pre-flight fails outside
Allowed scope; forbidden path edit required; route growth cannot be controlled
within Allowed scope.

## Operator Checkpoint

Operator requested all MKG7 T2–T7 work orders dispatched for worker execution.
T3 requires T2 to be complete first. T3 is dispatch-ready once T2 output exists.

## Worker Dispatch Prompt

```text
You are assigned MKG7-T3 Memory Execution Advisory Wire-In.
PREREQUISITE: T2 memory-readout-eligibility-policy.ts must exist before starting.

Primary work order:
docs/work_orders/CVF_WO_MKG7_T3_MEMORY_EXECUTION_ADVISORY_WIREIN_2026-06-01.md

Critical rules:
- create route-memory-advisory.ts helper under src/app/api/execute/;
- add memoryAdvisoryReadout field to ALLOW response in route.ts (additive only);
- do NOT modify lines 637-646 of route.ts (evaluateDurableMemoryRoute,
  evaluateAifMemoryReinjection) — these are forbidden-touch paths;
- route.ts must stay at or below 858 lines; if growth needed, extract helper first;
- advisory must set rawMemoryReleased:false and canReinject:false;
- run npm run check, execute-route step-sequence guard, file-size guard.

Worker Autonomy Rule: repair allowed-scope gate failures and rerun without asking.
Pending Artifact Rule: do not commit; record actual git status.
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

T3 authorizes an advisory-only Memory field in the execute response. Does not
authorize modifying existing memory paths, enforcement behavior, provider calls,
raw Memory release, prompt injection, persistence mutation, public-sync, or push.
