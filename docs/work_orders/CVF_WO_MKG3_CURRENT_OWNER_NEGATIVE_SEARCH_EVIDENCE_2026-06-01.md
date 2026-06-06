# CVF Work Order - MKG3 Current Owner Negative Search Evidence

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

docType: work_order

Date: 2026-06-01

## Purpose

Dispatch a worker to harden MKG2's current-owner absence claims with
current-repo search evidence, while testing that the worker obeys both the
Worker Autonomy rule and the Pending Artifact Evidence Finality rule.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| MKG3 GC-018 | `docs/baselines/CVF_GC018_MKG3_CURRENT_OWNER_NEGATIVE_SEARCH_EVIDENCE_2026-06-01.md` | ACCEPT |
| MKG3 roadmap | `docs/roadmaps/CVF_MKG3_CURRENT_OWNER_NEGATIVE_SEARCH_EVIDENCE_ROADMAP_2026-06-01.md` | ACCEPT |
| MKG2 review | `docs/reviews/CVF_MKG2_DEFERRED_RUNTIME_CANDIDATE_TRIAGE_REVIEW_2026-06-01.md` | ACCEPT |
| MKG1 completion | `docs/reviews/CVF_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_COMPLETION_2026-06-01.md` | ACCEPT |
| RESCAN-C manifest | `docs/audits/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_MANIFEST_2026-06-01.json` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | provide this packet and review worker output | no silent runtime expansion |
| Worker | search current non-Legacy repo and file pending review | no commit, push, runtime edit, or live proof |
| Reviewer | verify evidence finality and owner-search quality | reject stale clean/range claims |

## Scope

Allowed scope:

- read MKG2 review, MKG1 completion, and RESCAN-C manifest;
- search current non-Legacy CVF files for owner candidates related to cortex,
  governed skill evolution, and graph runtime;
- create one pending review artifact:
  `docs/reviews/CVF_MKG3_CURRENT_OWNER_NEGATIVE_SEARCH_EVIDENCE_REVIEW_2026-06-01.md`;
- run working-tree-aware pending-artifact checks;
- fix documentation-format or evidence-block defects inside this work order's
  Allowed scope.

Forbidden scope:

- `.private_reference/legacy/**` edits;
- runtime/source code edits;
- live/provider proof;
- graph retrieval execution;
- Memory reinjection;
- skill mutation;
- public-sync, push, publish, or local commit by the worker;
- destructive action.

Risk ceiling: R1 planning and documentation.

## Required First Reads

- `docs/reviews/CVF_MKG2_DEFERRED_RUNTIME_CANDIDATE_TRIAGE_REVIEW_2026-06-01.md`
- `docs/reviews/CVF_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_COMPLETION_2026-06-01.md`
- `docs/audits/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_MANIFEST_2026-06-01.json`
- `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md`
- `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`

## Pre-Flight Checks

Required before worker search:

```powershell
git rev-parse --short HEAD
git status --short
python scripts/build_legacy_rescan_c_manifest.py --check-only --expected-manifest-hash ae7fe05e016b7079a81002de60de1e1209112de59c8bee793e15e11557cae0ff
```

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| MKG2 review records 21 deferred candidates by group | VALUE_SET | `docs/reviews/CVF_MKG2_DEFERRED_RUNTIME_CANDIDATE_TRIAGE_REVIEW_2026-06-01.md` | Candidate Enumeration | `21/21` | MKG2 review | ACCEPT |
| MKG1 deferred rows back MKG2 candidate groups | VALUE_SET | `docs/reviews/CVF_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_COMPLETION_2026-06-01.md` | File-Level Processing Ledger | `DEFER_RUNTIME_GC018` | MKG1 completion | ACCEPT |
| RESCAN-C manifest hash backs candidate enumeration: `ae7fe05e016b7079a81002de60de1e1209112de59c8bee793e15e11557cae0ff` | VALUE_SET | `docs/audits/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_MANIFEST_2026-06-01.json` | `manifestHash` | `manifestHash` | RESCAN-C manifest | ACCEPT |
| Worker autonomy standard exists | EXISTS | `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md` | Worker Autonomy Prompt | `Worker Autonomy / No-Question Rule` | worker autonomy standard | ACCEPT |
| Pending Artifact Evidence Finality standard exists | EXISTS | `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | Section 4C | `Pending Artifact Evidence Finality` | closure-quality standard | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| Re-read MKG2/MKG1 evidence | Required First Reads | authority summary | review source citations | DISPATCHED |
| Search cortex owner candidates | Execution Plan | cortex search evidence | `rg` command output summary | DISPATCHED |
| Search governed-skill owner candidates | Execution Plan | skill search evidence | `rg` command output summary | DISPATCHED |
| Search graph runtime owner candidates | Execution Plan | graph search evidence | `rg` command output summary | DISPATCHED |
| Preserve pending artifact finality | Pending Artifact Evidence Finality | finality-safe gate evidence | dispatch-quality gate | DISPATCHED |

## Worker Autonomy / No-Question Rule

The worker must not ask the operator before performing non-destructive actions
inside this work order's Allowed scope.

Proceed autonomously with reading named files, running git status/diff/rev-parse,
running manifest/hash checks, running `rg` search commands, running governance
gates, fixing documentation format defects inside Allowed scope, adding missing
required evidence blocks, and rerunning failed guards after allowed-scope
remediation.

Ask only if the next action would exceed Allowed scope, edit Legacy source,
edit runtime/source code, run live/provider proof, use secrets/quota,
public-sync, push/publish, commit, change claim boundary or risk, release a
`HOLD_*` prerequisite, touch forbidden paths, or perform destructive/
irreversible action.

## Pending Artifact Evidence Finality

The worker must not commit. Leave the MKG3 review pending for operator review.

Because the review artifact will be pending, it must not claim
`git status --short` is clean. Record the actual pending status line for the
MKG3 review artifact.

Do not cite `--base HEAD~1 --head HEAD` as proof for the pending MKG3 review.
Use working-tree-aware pending-artifact checks and label them as such. If a gate
fails inside Allowed scope, repair and rerun instead of asking whether to fix it.

## Worker Dispatch Prompt

Send this exact bounded prompt with the work order when assigning MKG3:

```text
You are assigned MKG3 Current Owner Negative Search Evidence.

Primary work order:
docs/work_orders/CVF_WO_MKG3_CURRENT_OWNER_NEGATIVE_SEARCH_EVIDENCE_2026-06-01.md

Deliverable:
- create docs/reviews/CVF_MKG3_CURRENT_OWNER_NEGATIVE_SEARCH_EVIDENCE_REVIEW_2026-06-01.md;
- account for the 21/21 MKG2 deferred candidates by group;
- run current non-Legacy repo searches for cortex, governed-skill, and graph
  runtime owner candidates;
- record commands and bounded output summaries;
- state ACCEPT/BLOCKED/AMBIGUOUS owner evidence per group;
- leave the review pending and uncommitted for operator review.

Worker Autonomy Rule:
Do not ask the operator before performing non-destructive actions inside the
work order's Allowed scope. If a machine gate fails inside Allowed scope, repair
it and rerun.

Pending Artifact Evidence Finality:
Do not claim git status is clean while the review is pending. Do not use
HEAD~1..HEAD as proof for the pending review. Record actual pending status and
working-tree-aware gate results.

Stop and ask only if the next action would exceed Allowed scope, edit Legacy
source, edit runtime/source code, run live/provider/API proof, use
secrets/quota, public-sync, push/publish, commit, change claim boundary or
risk, release a HOLD prerequisite, touch forbidden paths, or perform destructive
or irreversible action.
```

## Write Ownership

Owned future path:

- `docs/reviews/CVF_MKG3_CURRENT_OWNER_NEGATIVE_SEARCH_EVIDENCE_REVIEW_2026-06-01.md`

Forbidden paths are listed in Scope.

Write mode:

- create-only review artifact;
- no commit by worker.

## Execution Plan

1. Read MKG2 review, MKG1 completion, and manifest.
2. Confirm `21/21` candidates by group from MKG2.
3. Run current non-Legacy search commands for cortex/cortex-hub/CORTEX terms.
4. Run current non-Legacy search commands for Memento-Skills, skill evolution,
   skill mutation, and governed skill terms.
5. Run current non-Legacy search commands for code-review-graph and graph
   runtime owner terms.
6. Create the MKG3 review with Search Evidence, Source Verification, Pending
   Artifact Evidence Finality, Public Export Disposition, and Claim Boundary.
7. Run working-tree-aware pending-artifact gates.
8. Leave the review pending for operator review without committing.

## Evidence Requirements

- manifest JSON and hash citation;
- `21/21` continuity by group;
- command-backed current non-Legacy owner search evidence;
- explicit `ACCEPT`, `AMBIGUOUS`, or `BLOCKED_SOURCE_NOT_FOUND` disposition per
  owner group;
- pending artifact status that does not claim clean worktree;
- explicit no-runtime/no-live/no-public/no-commit boundary.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Candidate continuity | `21/21` accounted for by group |
| Current-owner evidence | search-backed disposition for cortex, governed skill, and graph groups |
| Pending finality | no false clean/staged/range evidence |
| Runtime boundary | no implementation, live proof, or public-sync |
| Worker autonomy | no routine allowed-scope questions |

## Review Gate

Reviewer must reject any MKG3 packet that:

- treats Legacy source family names as current CVF owners without current
  non-Legacy source evidence;
- claims clean git status while the review is pending;
- cites a committed-only range as proof for an uncommitted review artifact;
- asks the operator whether to fix allowed-scope guard failures.

## Closure Checklist

- N/A with reason: MKG3 worker must not close this tranche or commit the review;
  the worker returns a pending review artifact for operator/reviewer audit.

## Return-To-Orchestrator Conditions

Return if implementation becomes necessary, live proof is required, a search
result would require runtime/source edits to interpret, or the worker needs to
exceed Allowed scope.

## Operator Checkpoint

Operator explicitly requested MKG3 as the next guard-behavior test after MKG2.
The worker must leave the MKG3 review pending/uncommitted so the reviewer can
check Pending Artifact Evidence Finality before closure.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private dispatched work order only. No public-sync remote, public
repository commit, or public artifact path is included.

## Claim Boundary

MKG3 is dispatched as bounded evidence hardening only. It does not authorize
implementation, live proof, runtime behavior, public-sync, graph retrieval,
Memory reinjection, skill mutation, hosted readiness, production readiness,
public readiness, or local commit by the worker.
