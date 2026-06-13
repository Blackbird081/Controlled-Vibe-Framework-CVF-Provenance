# CVF Agent Work Order - FPC-T2 System-Loop Interlock Expansion Decision

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Date: 2026-06-13

Owner: Codex (orchestrator)

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `3f57bf18`

executionBaseHead: `3f57bf18`

closureBaseHead: Codex reviewer-owned closure anchor

sourceAuthority:
`docs/baselines/CVF_GC018_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_2026-06-13.md`

rawMemoryReleased=false

completionReviewPath:
Codex reviewer-owned closure artifact

GC-018:
`docs/baselines/CVF_GC018_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_2026-06-13.md`

Parent roadmap:
`docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md`

FPC-T1 matrix:
`docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md`

## Purpose

Produce a source-backed FPC-T2 decision matrix that evaluates the five FPC-T2
system-loop interlock candidates from FPC-T1 and decides what should happen
next for each candidate.

This work order is decision-only. It does not authorize interlock registry
edits, checker/template implementation, runtime/source/test mutation, downstream
use-case work, live/provider/OCR proof, public-sync, readiness/cost/quality
claims, memory reinjection, high-risk promotion, or autonomous mutation.

## Authority Chain

| Authority | Path / evidence | Disposition |
| --- | --- | --- |
| Operator request | operator asked Codex to continue with work order for FPC-T2 | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V18_2026-06-12.md` | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | ACCEPT |
| FPC-T1 matrix | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | ACCEPT |
| FPC-T1 completion | `docs/reviews/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_COMPLETION_2026-06-13.md` | ACCEPT |
| System-loop interlock standard | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md` | ACCEPT |
| System-loop interlock registry | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | ACCEPT |
| FPC-T2 GC-018 | `docs/baselines/CVF_GC018_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_2026-06-13.md` | ACCEPT |

## Agent Roles

| Role | Agent | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | dispatches GC-018 and this work order |
| Worker | Claude | authors allowed-scope decision matrix and worker-return packet only |
| Reviewer / closer | Codex | reviews worker return, runs gates, commits, and decides any separate registry-edit or FPC-T3 packet |

## Intake Role Routing Decision

Intake summary: FPC-T1 is closed and produced five source-backed FPC-T2
candidates. The operator directed Codex to continue with FPC-T2.

Scope classification: read-only governed decision packet with bounded output
artifacts.

Risk sensitivity: medium-high governance risk because FPC-T2 decisions may
shape future registry edits, but this dispatch does not authorize those edits.

Selected route mode: MULTI_AGENT_MULTI_ROLE.

Role separation basis: Claude executes under `WORKER_MUST_NOT_COMMIT`; Codex
reviews, closes, and commits.

Escalation condition: return `BLOCKED_SCOPE_EXPANSION` if Claude needs registry
edits, runtime/source/test mutation, checker implementation, generated aggregate
mutation, session-state mutation, external app source access, provider/OCR/API
proof, public-sync, claim expansion, destructive action, or a new operator
decision.

## Required First Reads

Claude must read:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V18_2026-06-12.md`
4. `AGENTS.md`
5. `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md`
6. `docs/baselines/CVF_GC018_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_2026-06-13.md`
7. `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md`
8. `docs/reviews/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_COMPLETION_2026-06-13.md`
9. `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md`
10. `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`
11. `docs/reference/CVF_MLW3_EVIDENCE_TO_TRUTH_LEARNING_SIGNAL_PIPELINE_2026-06-05.md`
12. `docs/reviews/CVF_MLW3_RT1_EVIDENCE_TO_LEARNING_RUNTIME_PROOF_COMPLETION_2026-06-05.md`
13. this work order

Claude may read other CVF-governed roadmap, completion, reference, source, or
checker files only as needed to verify candidate evidence. Claude must not read
external Document Translator or Policy_Local source trees. Claude must not cite
provider-specific agent memory or guidance files as CVF source authority.

## Startup Acknowledgment Required

Claude must begin with:

`Startup acknowledged: current mode=fpc_t2_system_loop_interlock_expansion_decision_dispatched; active handoff=AGENT_HANDOFF_V18_2026-06-12.md; work order=FPC-T2; next allowed move=Claude produces FPC-T2 decision matrix and worker-return packet under WORKER_MUST_NOT_COMMIT; parked checkpoint=FPC-T3 execution, registry edits, DT-CVF-T0, Policy_Local PL-S1, external Document Translator source, OCR/provider/live proof, retrieval, public-sync, T12, readiness/cost/quality claims remain parked.`

## Pre-Flight Checks

Claude must complete these checks before authoring artifacts:

1. Read every Required First Reads file.
2. Record `git rev-parse --short HEAD`.
3. Record `git status --short`.
4. Stop with `BLOCKED_UNEXPECTED_FILESYSTEM_STATE` if unrelated staged or
   uncommitted files are present before work.
5. Confirm `WORKER_MUST_NOT_COMMIT`.
6. Confirm allowed artifacts are limited to the two deliverables in this work
   order, plus this work order only if adding worker-return evidence is
   necessary.

## Write Ownership

Claude owns only worker-authored FPC-T2 decision artifacts under
`WORKER_MUST_NOT_COMMIT`.

Codex owns dispatch packet edits, completion review, session-state sync,
roadmap closure conversion, final gates, commit, and any separate registry-edit
authorization.

Claude must not edit `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, active handoff
files, generated aggregates, runtime/source/test trees, interlock registries,
checker scripts, public-sync files, external app clones, provider/live-proof
surfaces, or provider-specific agent memory files.

## Worker Autonomy / No-Question Rule

Claude must repair allowed-scope gate failures without asking the operator.
Claude must return to Codex only when repair would require forbidden paths,
registry mutation, runtime/source/test mutation, checker implementation,
generated aggregate mutation, session-state mutation, external app source
access, live/provider/API proof, public-sync, claim expansion, destructive
action, or a new operator decision.

## Commit Mode And Base-Anchor Lifecycle

| Anchor | Value | Owner | Disposition |
| --- | --- | --- | --- |
| dispatchBaseHead | `3f57bf18` | Codex | ACCEPT |
| executionBaseHead | `3f57bf18` | Claude | ACCEPT |
| closureBaseHead | reviewer-owned closure anchor | Codex reviewer | ACCEPT |
| Commit mode | `WORKER_MUST_NOT_COMMIT` | Codex | ACCEPT |

Claude must not commit. Claude must record worker-return base/head and
`git status --short` output in the worker-return packet.

## Reviewer Closure Conversion Block

completionReviewPath:
Codex reviewer-owned closure artifact.

reviewerOwnedClosurePaths:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_FOR_CLAUDE_2026-06-13.md`
- `docs/baselines/CVF_GC018_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_2026-06-13.md`
- `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md`
- `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_WORKER_RETURN_2026-06-13.md`
- FPC-T2 completion review to be created by Codex
- `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md`

pendingStatusTokensAllowedBeforeReview: resolved by Codex reviewer before
closure.

forbiddenClosedEquivalentResidue: resolved by Codex reviewer before closure.

## Forbidden Filesystem State At Dispatch

Dispatch must begin from clean worktree state except for this committed dispatch
package. If Claude sees unrelated uncommitted or staged files before work,
Claude must stop and return `BLOCKED_UNEXPECTED_FILESYSTEM_STATE` with
`git status --short` evidence.

## Forbidden Path Manifest

| Path | Status |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | FORBIDDEN_TO_MODIFY |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | FORBIDDEN_TO_MODIFY |
| `AGENT_HANDOFF_V18_2026-06-12.md` | FORBIDDEN_TO_MODIFY |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | READ_ONLY_INPUT |
| `governance/compat/check_system_loop_interlock.py` | FORBIDDEN_TO_MODIFY |
| `governance/compat/check_agent_packet_authority_and_encoding.py` | FORBIDDEN_TO_MODIFY |
| external Document Translator source tree | FORBIDDEN_TO_ACCESS |
| external Policy_Local source tree | FORBIDDEN_TO_ACCESS |

## Dependency Release Evidence

| Dependency | Required evidence | Disposition |
| --- | --- | --- |
| FPC-T1 closure complete | `docs/reviews/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_COMPLETION_2026-06-13.md`; material commit `91e8f10f` | ACCEPT |
| FPC-T1 candidate matrix exists | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | ACCEPT |
| Provider-specific authority cleanup complete | commit `d6c31c6d`; `AGENTS.md` provider-specific boundary | ACCEPT |
| Active state permits FPC-T2 | `CVF_SESSION/ACTIVE_SESSION_STATE.json` `nextAllowedMove` | ACCEPT |
| Fresh FPC-T2 baseline | `docs/baselines/CVF_GC018_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_2026-06-13.md` | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: FPC roadmap records FPC-T2 dispatch | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | Status | `FPC_T2_DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT` | FPC roadmap | ACCEPT |
| EXISTS: FPC-T2 requires fresh GC-018/work order | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `Accepted next-route result` | fresh GC-018 and source-verified work order | FPC roadmap | ACCEPT |
| EXISTS: FPC-T2 purpose is system-loop interlock expansion decision | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `## FPC-T2 - System-Loop Interlock Expansion Decision` | system-loop interlock expansion decision | FPC roadmap | ACCEPT |
| EXISTS: FPC-T2 candidate families are evaluate-not-preaccept | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `Candidate families to evaluate, not pre-accept` | FPC-T2 candidate families | FPC roadmap | ACCEPT |
| EXISTS: FPC-T2 disposition vocabulary | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `FPC-T2 must decide for each candidate` | `ADD_INTERLOCK_ENTRY`; `KEEP_STRUCTURAL_ONLY`; `MACHINE_CHECK_FIRST`; `DEFER_RUNTIME_OWNER_MISSING`; `REJECT_WITH_REASON`; `SOURCE_GAP_BLOCKS_DISPATCH` | FPC roadmap | ACCEPT |
| EXISTS: FPC-T2 registry edit boundary | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `FPC-T2 must not edit the registry unless...` | interlock registry | FPC roadmap | ACCEPT |
| EXISTS: FPC-T1 matrix supplies five FPC-T2 candidates | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | `## FPC-T2 Candidate List` | `FPC-T2-C01` through `FPC-T2-C05` | FPC-T1 matrix | ACCEPT |
| EXISTS: FPC-T2-C05 has MLW3 reconciliation constraint | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | `## FPC-T2 / FPC-T3 Decision Constraints` | `FPC-T2-C05` | FPC-T1 matrix | ACCEPT |
| EXISTS: system-loop interlock registry owner | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md` | `## Registry` | `CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | system-loop interlock standard | ACCEPT |
| EXISTS: registry field vocabulary includes automation and claim boundary | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md` | field table | `automationLevel`; `claimBoundary` | system-loop interlock standard | ACCEPT |
| EXISTS: current registry has scan-loop-to-learning-loop for reconciliation | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | connection id | `scan-loop-to-learning-loop` | system-loop interlock registry | ACCEPT |
| EXISTS: provider-specific agent files are not CVF authority | `AGENTS.md` | `Mandatory Provider-Specific Agent Memory Boundary` | `NOT_CVF_SOURCE` | agent front-door instructions | ACCEPT |

## New Doc-Only Fields

The worker may introduce these doc-only fields in the FPC-T2 decision matrix:

| New doc-only field | Meaning |
| --- | --- |
| `Candidate ID` | FPC-T2 candidate identifier from FPC-T1 |
| `Candidate name` | candidate label from FPC-T1 |
| `Existing registry coverage` | current matching or adjacent registry entries |
| `Distinctness decision` | whether the candidate is distinct from existing registry entries |
| `Source confidence` | `SOURCE_BACKED`, `PARTIAL_SOURCE`, or `SOURCE_GAP` |
| `Disposition` | one approved FPC-T2 disposition token |
| `Proposed registry shape` | only for `ADD_INTERLOCK_ENTRY`; otherwise `N/A with reason` |
| `Registry edit authorization` | always `NOT_AUTHORIZED_BY_FPC_T2_WORK_ORDER` |
| `FPC-T3 dependency` | checker/template prerequisite if any |
| `Claim boundary` | what the decision does not prove |

These are doc-only decision fields. They must not be represented as existing
runtime fields or source symbols.

## Current Runtime Freshness Verification

| Source fact | Verification command or evidence | Disposition |
| --- | --- | --- |
| No runtime/source/test edit is authorized | Forbidden Scope and Allowed Artifact Set limit worker writes to governed markdown artifacts | ACCEPT |
| No interlock registry edit is authorized | Forbidden Path Manifest marks `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` as read-only input | ACCEPT |
| Existing registry reconciliation must use current registry | Required First Reads include the current registry; worker must cite registry entries or record source gap | ACCEPT |
| Provider-specific memory/guidance is not source authority | `AGENTS.md` provider-specific boundary and agent packet authority gate | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Roadmap evidence | Work-order section | Verification |
| --- | --- | --- | --- |
| FPC-T2 prerequisite is FPC-T1 closure plus fresh GC-018/work order | FPC roadmap Work Plan | Dependency Release Evidence | FPC-T1 closure and this dispatch baseline exist |
| Evaluate candidates, not pre-accept | FPC roadmap FPC-T2 | Purpose; Required Deliverables | matrix includes per-candidate dispositions |
| Use approved disposition vocabulary | FPC roadmap FPC-T2 | Candidate Disposition Rules | each candidate has one allowed token |
| Reconcile evidence-to-claim-update against MLW3 | FPC roadmap FPC-T2 and FPC-T1 matrix constraints | C05 Reconciliation Requirements | C05 section present |
| Do not edit registry unless explicitly authorized | FPC roadmap FPC-T2 | Forbidden Scope | registry remains unchanged |
| Keep FPC-T3 parked | FPC roadmap Work Plan | Claim Boundary | FPC-T3 only as dependency note |
| Keep use cases downstream | FPC roadmap Design Control Gate | Forbidden Scope | no external source inspection |
| Preserve provider-specific memory boundary | AGENTS.md provider boundary | Required First Reads; Source Verification | no provider-specific files as authority |

## Execution Plan

Claude must execute in this order:

1. Perform startup acknowledgment and pre-flight checks.
2. Read all required first-read files.
3. Build a candidate evidence ledger for FPC-T2-C01 through FPC-T2-C05.
4. Compare each candidate against the existing interlock registry and cited
   owner surfaces.
5. Assign exactly one approved disposition per candidate.
6. For any `ADD_INTERLOCK_ENTRY` candidate, draft proposed registry-entry shape
   in the decision matrix without editing the registry.
7. Record C05 MLW3 reconciliation separately.
8. Run worker-return gates and return uncommitted artifacts to Codex.

## Evidence Requirements

Claude must provide:

- source path and section/line evidence for every candidate decision;
- registry reconciliation evidence for each candidate;
- explicit `N/A with reason` when proposed registry shape is not applicable;
- `git rev-parse --short HEAD`, `git status --short`, and `git diff --check`
  outputs in the worker return;
- reviewer-fast or worker-return fast gate output when available;
- Finding-To-Governance Learning Disposition for any gap/finding;
- proof that no forbidden path was edited.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Decision matrix exists | `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md` created |
| Worker return exists | `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_WORKER_RETURN_2026-06-13.md` created |
| All five FPC-T2 candidates evaluated | FPC-T2-C01 through FPC-T2-C05 each have one approved disposition |
| MLW3 reconciliation completed | C05 has explicit comparison against MLW3 and existing `scan-loop-to-learning-loop` |
| Registry remains unchanged | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` not modified |
| FPC-T3 remains parked | any machine-check need is recorded as dependency only |
| Use-case lanes remain downstream | no external Document Translator or Policy_Local source inspected |
| Provider-specific source boundary preserved | no provider-specific memory/guidance file used as CVF authority |
| Commit mode honored | worker returns uncommitted artifacts only |

## Review Gate

Codex reviewer must run at least:

```powershell
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
git diff --check
git status --short
```

Before closure, Codex must also run the applicable pre-closure/pre-commit gates
on a real changed range and decide whether any `ADD_INTERLOCK_ENTRY`
disposition requires a separate registry-edit work order.

## Return-To-Orchestrator Conditions

Claude must return to Codex with `WORKER_RETURN_SUBMITTED_UNCOMMITTED` when the
decision matrix and worker-return packet are complete and gates are recorded.

Claude must return `BLOCKED_SCOPE_EXPANSION` if any candidate decision requires
registry edits, checker implementation, runtime/source/test mutation, external
source access, live/provider proof, session-state mutation, public-sync, or
operator authorization.

Claude must return `SOURCE_GAP_BLOCKS_DISPATCH` for any candidate whose required
owner source cannot be verified from CVF-governed artifacts.

## Operator Checkpoint

No operator checkpoint is required for Claude to complete this decision-only
work order. Operator approval is required before any later registry edit,
FPC-T3 checker/template implementation, downstream use-case adapter work,
provider/OCR/live proof, public-sync, or readiness/cost/quality claim.

## Closure Checklist

- [x] GC-018 baseline exists for FPC-T2.
- [x] Source Verification Block is present.
- [x] Roadmap-To-Work-Order Trace Matrix is present.
- [x] Forbidden Filesystem State At Dispatch is present.
- [x] Forbidden Path Manifest is present.
- [x] Current Runtime Freshness Verification is present.
- [x] Provider-specific source authority boundary is carried forward.
- [ ] Worker return submitted.
- [ ] Codex reviewer accepted decision matrix.
- [ ] Final gates passed on real changed range.

## Candidate Disposition Rules

Claude must assign exactly one of these dispositions to every candidate:

- `ADD_INTERLOCK_ENTRY`;
- `KEEP_STRUCTURAL_ONLY`;
- `MACHINE_CHECK_FIRST`;
- `DEFER_RUNTIME_OWNER_MISSING`;
- `REJECT_WITH_REASON`;
- `SOURCE_GAP_BLOCKS_DISPATCH`.

Decision constraints:

1. `ADD_INTERLOCK_ENTRY` requires a distinct upstream loop, downstream loop,
   output signal, input artifact, routing rule, automation level, and claim
   boundary. It is still proposal-only in this tranche.
2. `KEEP_STRUCTURAL_ONLY` requires explanation of why existing standards,
   templates, or artifacts are enough without registry expansion.
3. `MACHINE_CHECK_FIRST` requires a concrete FPC-T3 checker/template
   prerequisite.
4. `DEFER_RUNTIME_OWNER_MISSING` requires the missing owner surface or source
   symbol.
5. `REJECT_WITH_REASON` requires direct source-backed reason.
6. `SOURCE_GAP_BLOCKS_DISPATCH` requires the source fact that could not be
   verified and the next orchestrator action.

## Required Deliverables

Claude must create:

1. `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md`
2. `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_WORKER_RETURN_2026-06-13.md`

### Decision Matrix Minimum Contents

The decision matrix must include:

- Purpose;
- Scope / Target / Owner Boundary;
- Source Authority;
- Corpus Completeness And Report Integrity block;
- per-candidate decision table for FPC-T2-C01 through FPC-T2-C05;
- explicit C05 MLW3 reconciliation section;
- proposed registry shape section only for `ADD_INTERLOCK_ENTRY` candidates;
- no-registry-edit statement;
- FPC-T3 dependency notes where a candidate needs machine checks first;
- Finding-To-Governance Learning Disposition;
- Claim Boundary;
- Public Export Disposition;
- `rawMemoryReleased=false`.

### Worker Return Minimum Contents

The worker return must include:

- Worker disposition: `WORKER_RETURN_SUBMITTED_UNCOMMITTED`;
- startup acknowledgment;
- base/head/status evidence;
- Required First Reads ledger;
- allowed-artifact list;
- forbidden-path evidence;
- command evidence, including `reviewer-fast` if available and `git diff --check`;
- finding summary;
- Finding-To-Governance Learning Disposition;
- claim boundary;
- `rawMemoryReleased=false`.

## Allowed Artifact Set

Claude may create or update only:

- `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md`;
- `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_WORKER_RETURN_2026-06-13.md`;
- this work order only if adding worker-return evidence is necessary.

## Forbidden Scope

Claude must not:

- edit `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`;
- edit any runtime/source/test file;
- create or modify any checker script;
- edit `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, active handoff files, or
  generated aggregates;
- inspect or mutate external Document Translator or Policy_Local source trees;
- run OCR/provider/API/live proof;
- perform retrieval route wiring or corpus ingestion;
- use provider-specific memory or guidance files as CVF source authority;
- perform public-sync;
- make readiness, cost, quality, production, or public claims;
- commit.

## Worker Return Fast Gate

If available, Claude should run:

```powershell
python governance/compat/run_worker_return_fast_gate.py --pytest-target none
```

If that command is unavailable or not appropriate, Claude must run at minimum:

```powershell
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
git diff --check
git status --short
```

Claude must record the exact commands and results. Gate failure inside allowed
scope must be repaired before return.

## Claim Boundary

FPC-T2 decides candidate interlock disposition only. It does not mutate the
registry, implement checkers, authorize FPC-T3, prove semantic truth, prove
runtime/provider behavior, authorize downstream use-case adapters, authorize
public-sync, or release raw memory.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance FPC-T2 dispatch work order. Public-sync is not
authorized.
