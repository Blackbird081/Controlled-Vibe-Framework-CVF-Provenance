# CVF Work Order - MKG7-T7 Memory Live Proof Decision

Memory class: FULL_RECORD

Status: HOLD_UNTIL_T3_PASS

docType: work_order

Date: 2026-06-01

## Purpose

File a decision packet answering whether the Memory plane now affects governed
route behavior enough to require a live/provider proof tranche. T7 reviews the
T1–T6 output set and records a YES or NO decision with explicit reasoning. T7
itself does NOT execute any live proof.

- If NO: MKG7 is closed as local-deterministic-evidence-only.
- If YES: worker drafts a GC-018 path for a live proof tranche and returns it
  for operator authorization. No live call is made in T7.

Success: decision review exists citing T1–T6 completion reviews, explicit YES/NO
answer referencing T3 advisory behavior, MKG7 closure statement (if NO) or draft
GC-018 path (if YES), markdown-structural gate PASS, public-export gate PASS,
pending and uncommitted.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-01 dispatch MKG7 T2–T7 for worker execution | ACCEPT |
| MKG7-T7 GC-018 | `docs/baselines/CVF_GC018_MKG7_T7_MEMORY_LIVE_PROOF_DECISION_2026-06-01.md` | ACCEPT |
| MKG7 roadmap | `docs/roadmaps/CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md` | ACCEPT |
| T1 contract | `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | ACCEPT |
| Worker autonomy standard | `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md` | ACCEPT |

Prerequisite: T1–T6 must all be complete before T7 is executed.

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch after T1–T6 complete; review decision | no silent scope expansion |
| Worker | read T1–T6 reviews; file decision packet | no live proof execution, no `.ts` edits, no commit |
| Reviewer | verify decision explicitly cites T3 advisory behavior and does not authorize live proof in T7 | reject if live call attempted |

Live proof execution: requires a separate GC-018 authorized by the operator — T7 does not execute live proof.

## Scope

Allowed scope:

- read T1–T6 completion reviews and the T1 contract;
- create `docs/reviews/CVF_MKG7_T7_MEMORY_LIVE_PROOF_DECISION_2026-06-01.md`;
- if YES: draft a `docs/baselines/CVF_GC018_MKG7_T8_MEMORY_LIVE_PROOF_DRAFT_2026-06-01.md` for operator review (do not mark it AUTHORIZED);
- run listed gates.

Forbidden scope:

- executing any live provider call in T7;
- editing any `.ts` file;
- self-authorizing a live proof tranche;
- public-sync, push, or commit.

Risk ceiling: R0 — decision document only.

## Required First Reads

- `docs/baselines/CVF_GC018_MKG7_T7_MEMORY_LIVE_PROOF_DECISION_2026-06-01.md`
- `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md`
- `docs/reviews/CVF_MKG7_T1_MEMORY_PLANE_OPERATIONAL_CONTRACT_COMPLETION_2026-06-01.md`
- `docs/reviews/CVF_MKG7_T2_MEMORY_READOUT_ELIGIBILITY_LIFECYCLE_COMPLETION_2026-06-01.md`
- `docs/reviews/CVF_MKG7_T3_MEMORY_EXECUTION_ADVISORY_WIREIN_COMPLETION_2026-06-01.md`
- `docs/reviews/CVF_MKG7_T4_MEMORY_RETRIEVAL_ATTRIBUTION_COMPLETION_2026-06-01.md`
- `docs/reviews/CVF_MKG7_T5_MEMORY_DURABLE_WRITE_READINESS_COMPLETION_2026-06-01.md`
- `docs/reviews/CVF_MKG7_T6_MEMORY_DERIVED_GRAPH_BOUNDARY_COMPLETION_2026-06-01.md`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_markdown_structural_completeness.py --base 5e55714d --head HEAD --enforce
python governance/compat/check_public_export_disposition.py --base 5e55714d --head HEAD --enforce
```

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T3 advisory field (T3 output — read at dispatch) | DOC_ONLY_NEW | canonical-contract: T3 work order output | T3 completion review | `memoryAdvisoryReadout` | T3 advisory helper | ACCEPT |
| Live proof script exists | EXISTS | `scripts/run_cvf_release_gate_bundle.py` | top-level file | `run_cvf_release_gate_bundle` | release gate scripts | ACCEPT |
| T1 advisory-only boundary | EXISTS | `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | Advisory-Only Execution Boundary section | `Advisory-Only` | T1 contract | ACCEPT |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Decide whether live proof required | Execution Plan step 2 | YES/NO decision in review | reviewer check | DISPATCHED |
| Cite T3 advisory behavior explicitly | Execution Plan step 2 | reference to `memoryAdvisoryReadout` | reviewer check | DISPATCHED |
| If NO: MKG7 closure statement | Execution Plan step 2 | closure statement in review | reviewer check | DISPATCHED |
| If YES: draft GC-018 for operator (do not authorize) | Execution Plan step 3 | draft GC-018 file | reviewer check | DISPATCHED |

## 6C. Worker Autonomy / No-Question Rule

Machine-gate failures inside Allowed scope must be repaired and gates rerun
without escalation. Non-destructive actions inside Allowed scope (reading files,
writing the decision review, running listed gates, fixing documentation-format
defects) proceed without escalation.

Stop and escalate only when the next action would: exceed Allowed scope, edit
a `.ts` file, execute a live provider call, push, commit, trigger a live proof
tranche, or perform a destructive/irreversible action.

## 6D. Pending Artifact Evidence Finality

Do not commit. Record actual `git status --short`. Do not cite committed-only
or empty range as proof.

## 6G. Work-Order Fulfillment Manifest

### Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `docs/reviews/CVF_MKG7_T7_MEMORY_LIVE_PROOF_DECISION_2026-06-01.md` | Yes | decision packet |

### Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| Any `EXTENSIONS/**/*.ts` | T7 is documentation-only |
| `docs/baselines/CVF_GC018_MKG7_T8_*` (if YES) | must be DRAFT only, not AUTHORIZED — operator must authorize |

### Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| Explicit YES/NO decision | decision review | `YES` or `NO` | Yes |
| Reference to T3 advisory behavior | decision review | `memoryAdvisoryReadout` | Yes |
| MKG7 closure statement (if NO) | decision review | `MKG7` | Yes |

## 7. Write Ownership

Owned: T7 decision review, optionally draft T8 GC-018 (if YES, DRAFT only).
Forbidden: all `.ts` files.

## 8. Execution Plan

1. Capture `baseHead` and git status.
2. Read all T1–T6 completion reviews. For each tranche, confirm the boundary: T1 doc-only, T2 new policy helper (no route), T3 advisory field only (no enforcement, no provider routing change), T4 attribution helper (no raw content), T5 readiness layer (no new write path), T6 doc-only boundary.
3. Answer the decision question: does any T1–T6 output affect provider routing, model selection, enforcement outcomes, or governance claims in a way that requires live proof?
   - Expected answer based on current scope: NO — all outputs are local deterministic; T3 advisory field is additive and does not influence provider execution.
   - If the T3 completion review reveals enforcement behavior was added, answer YES.
4. Write decision review citing each tranche and recording the YES/NO verdict.
5. If NO: add MKG7 closure statement: "MKG7 is closed as local-deterministic-evidence-only. No live/provider proof required."
6. If YES: draft `docs/baselines/CVF_GC018_MKG7_T8_MEMORY_LIVE_PROOF_DRAFT_2026-06-01.md` with Status: DRAFT (not AUTHORIZED); return for operator.
7. Run markdown-structural and public-export gates.
8. Leave all files pending and uncommitted.

## Evidence Requirements

- `python governance/compat/check_markdown_structural_completeness.py --base 5e55714d --head HEAD --enforce` — PASS;
- `python governance/compat/check_public_export_disposition.py --base 5e55714d --head HEAD --enforce` — PASS;
- actual `git status --short`.

## 10. Acceptance Criteria

- [ ] Decision review exists citing all T1–T6 completion reviews
- [ ] Explicit YES or NO decision with reasoning
- [ ] T3 advisory behavior (`memoryAdvisoryReadout`) explicitly referenced
- [ ] If NO: MKG7 closure statement present
- [ ] If YES: draft GC-018 returned as DRAFT, not executed
- [ ] Markdown-structural gate PASS
- [ ] Public-export gate PASS

Fail conditions:

- [ ] Any live provider call executed in T7
- [ ] Any `.ts` file edited
- [ ] Live proof self-authorized without a separate GC-018
- [ ] Worker commits, or escalates a gate failure that is inside Allowed scope

## 11. Review Gate

T1–T6 must all be complete. Closure (by orchestrator) after reviewer no-blocking
objection. If YES decision: operator must authorize T8 GC-018 before any live
proof.

## 12. Closure Checklist

N/A: worker must not close or commit T7. Return pending decision review for
orchestrator. If YES: the operator reviews the draft T8 GC-018 and decides
whether to authorize a live proof tranche.

## 13. Return-To-Orchestrator Conditions

Return if: T1–T6 not all complete; T3 completion review reveals enforcement
behavior requiring operator decision; `.ts` edit required.

## Operator Checkpoint

Operator requested all MKG7 T2–T7 work orders dispatched for worker execution.
T7 requires T1–T6 all complete. T7 is the final MKG7 closing tranche.

## Worker Dispatch Prompt

```text
You are assigned MKG7-T7 Memory Live Proof Decision.
PREREQUISITE: T1-T6 must all be complete (all 6 completion reviews must exist).

Primary work order:
docs/work_orders/CVF_WO_MKG7_T7_MEMORY_LIVE_PROOF_DECISION_2026-06-01.md

Critical rules:
- read all T1-T6 completion reviews;
- answer: does any T1-T6 output affect provider routing, enforcement, or model
  selection in a way requiring live proof? Expected: NO (T3 is advisory-only);
- write the decision review with explicit YES/NO and reasoning citing T3's
  memoryAdvisoryReadout behavior;
- if NO: include MKG7 closure statement;
- if YES: draft a GC-018 as DRAFT only — do NOT execute live proof;
- do NOT edit any .ts file; do NOT run any live provider call.

Worker Autonomy Rule: repair allowed-scope doc gate failures without asking.
Pending Artifact Rule: do not commit; record actual git status.
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

T7 authorizes a decision packet only. No live proof execution, `.ts` edits,
self-authorization of a live proof tranche, public-sync, or push. Any YES
decision requires fresh operator-authorized GC-018 before execution.
