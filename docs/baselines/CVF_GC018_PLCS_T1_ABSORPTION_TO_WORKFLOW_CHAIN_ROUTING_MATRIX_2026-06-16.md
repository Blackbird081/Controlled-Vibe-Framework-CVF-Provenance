# CVF GC-018 Authorization Baseline - PLCS-T1 Absorption To Workflow-Chain Routing Matrix

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: gc018

Date: 2026-06-16

Batch ID: PLCS-T1

rawMemoryReleased: false

## Purpose

Authorize a bounded, read-only PLCS-T1 worker task to map existing governed
knowledge-absorption evidence into plane/layer workflow-chain routing
dispositions.

The task is audit and matrix authoring only. It prevents accepted knowledge
from becoming another parallel plane/layer lane without owner, interlock,
checker/template, or rejection disposition.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| FPC roadmap closed T1/T2/T3 and left FPC-T4 held | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | Status and Tranche Plan | FPC-T4 | FPC roadmap | ACCEPT |
| FPC-T1 matrix lists planes, current chain posture, and next actions | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | FPC-T2/FPC-T3 Candidate List | FPC-T2 Candidate List | FPC-T1 audit matrix | ACCEPT |
| FPC-T2 C01-C04 are proposal-only ADD_INTERLOCK_ENTRY decisions | `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_COMPLETION_2026-06-13.md` | Decision Result | FPC-T2-C01 through FPC-T2-C04 | FPC-T2 completion review | ACCEPT |
| CCLV standard defines central facts plus local references | `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md` | Required Central Facts and Required Local References | Central Facts Reference | CCLV standard | ACCEPT |
| Knowledge absorption standard requires blind-spot control before absorption/implementation | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | Purpose and Mandatory Blind-Spot Control Block | Knowledge Absorption Blind-Spot Control Block | absorption standard | ACCEPT |
| CI1-T11 is existing governed memory/learning absorption evidence | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | Purpose and Work Plan | MLW1-MLW6 | CI1-T11 roadmap | ACCEPT |
| Current session permits fresh operator-selected foundation task | `CVF_SESSION/state/entries/nextAllowedMove.json` | value | nextAllowedMove | active session state source | ACCEPT |

## Baseline Decision

Decision: dispatch PLCS-T1 to Claude under `WORKER_MUST_NOT_COMMIT`.

This tranche must create:

- `docs/reference/CVF_PLCS_T1_ABSORPTION_TO_WORKFLOW_CHAIN_ROUTING_MATRIX_2026-06-16.md`;
- `docs/reviews/CVF_PLCS_T1_ABSORPTION_TO_WORKFLOW_CHAIN_ROUTING_MATRIX_WORKER_RETURN_2026-06-16.md`.

Codex owns review, allowed repairs, final commit, committed-range pre-closure,
and session sync.

## Authorized Scope

Authorized:

- read the source authority files named in this baseline and work order;
- create one routing matrix and one worker return;
- classify existing governed absorption lessons against plane/layer workflow
  owners and FPC/CCLV dispositions;
- use CCLV local reference/central facts pattern where it reduces repeated
  shared facts;
- report gaps with an explicit blocked-source, unmapped, or out-of-scope
  disposition plus reason.

Forbidden:

- scan new `.private_reference/legacy/` roots;
- rewrite historical closed artifacts;
- edit `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`;
- edit runtime/source/test files;
- mutate generated active session state;
- run provider/API/OCR/live proof;
- public-sync;
- claim production/public readiness;
- authorize Model Gateway, Policy_Local, Document Translator, retrieval, or
  downstream adapter implementation.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Matrix covers FPC-T1 target plane/layer rows and CI1-T11 governed absorption inputs. |
| AC2 | No matrix row accepts a knowledge unit without plane/layer owner and workflow-chain disposition. |
| AC3 | FPC-T2-C01 through C04 proposal-only decisions are preserved as proposal-only; no registry edit claim. |
| AC4 | FPC-T2-C05 remains machine-check-first unless the worker cites the existing FPC-T3-C01 checker as the concrete surface. |
| AC5 | CCLV usage is documented as central facts/local view or N/A with reason. |
| AC6 | Worktree return is uncommitted with exact changed paths, commands, and blocked decisions. |

## Negative Search And Collision Discipline

Search command used before authoring:

```powershell
rg -n "PLCS|Absorption To Workflow-Chain|plane layer workflow-chain" docs
```

Search roots: `docs/`.

Same-purpose collision result: this batch establishes the PLCS-T1 baseline for
the operator-selected absorption-to-workflow-chain routing scope. Related FPC,
CCLV, session, and interlock artifacts are accepted predecessor authority and
standard governance vocabulary for this baseline.

Collision disposition: PLCS-T1 owns only the read-only routing matrix
authorization described in this baseline. Predecessor artifacts remain source
authority and are not duplicated or superseded by this batch.

## Current Runtime Freshness Verification

This baseline makes no runtime/source/test/provider/live behavior claim.
Runtime freshness is `N/A with reason`: PLCS-T1 is a governed markdown matrix
dispatch only. Runtime/source/test, registry, provider, OCR, and public-sync
mutation are explicitly forbidden.

## Evidence / Verification

Required authoring checks before dispatch/commit:

- `python governance/compat/check_dispatch_prompt_envelope.py --base 9882de99 --head HEAD --enforce`
- `python governance/compat/check_work_order_dispatch_quality.py --base 9882de99 --head HEAD --enforce`
- `python governance/compat/check_markdown_structural_completeness.py --base 9882de99 --head HEAD --enforce`
- `python governance/compat/check_agent_operation_trace.py --base 9882de99 --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 9882de99 --head HEAD`

## Knowledge Absorption Blind-Spot Control Block

- Absorption target: existing governed absorption packets only.
- Prior absorption evidence resolved: CI1-T11 roadmap and scan-wave packet;
  FPC-T1 matrix; FPC-T2 decision matrix.
- Blind spot risk: accepted knowledge becomes a parallel plane/layer lane
  without workflow-chain owner, interlock, or checker route.
- Mitigation: PLCS-T1 matrix must give each accepted knowledge unit an owner
  and disposition or block it.
- Runtime/source authority boundary: no legacy symbol may become a current
  runtime/source fact without future source verification.

## Rescan Intelligence Hardening

- Original source artifact: NOT_APPLICABLE_WITH_REASON - this baseline does not
  reopen a corpus rescan or new intake replay.
- Predecessor intake artifact: CI1-T11, FPC-T1, FPC-T2, FPC-T3, and CCLV
  governed artifacts named in Source Authority.
- Delta ledger status: NOT_APPLICABLE_WITH_REASON - PLCS-T1 routes already
  governed inputs; it does not compute a new delta ledger.
- Routing matrix status: DO_NOW for the PLCS-T1 read-only routing matrix;
  runtime, registry, provider, public-sync, and legacy rescans are OUT_OF_SCOPE.
- Semantic sampling status: bounded adversarial boundary sample recorded below.
- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

### Original-Intake Delta Ledger

Delta category vocabulary retained for worker boundary:
`UNCHANGED_FROM_INTAKE`, `CHANGED_DISPOSITION`, `NEW_FINDING`, and
`REMOVED_OR_REJECTED`. PLCS-T1 may classify a routing row against governed
predecessor evidence, but must not claim a fresh rescan delta ledger.

### Follow-Up Routing Matrix

Routing lane vocabulary retained for worker boundary: `DO_NOW`,
`SEPARATE_RUNTIME_TRANCHE`, `STRATEGIC_OPERATOR_DECISION`, `OUT_OF_SCOPE`, and
`RESOLVED_BY_DESIGN`. PLCS-T1 itself is the DO_NOW documentation matrix;
runtime/source/test, registry, provider/live, public-sync, and new legacy
absorption belong outside this baseline.

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| PLCS-T1-S1 | Authorized Scope | Existing governed inputs may be routed into a workflow-chain matrix. | DO_NOW bounded documentation matrix | Could the matrix be misread as a new legacy rescan or runtime implementation? | PASS_BOUNDARY - forbidden scope and claim boundary prevent that interpretation. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch baseline. No public-sync batch is
authorized.

## Claim Boundary

This baseline authorizes PLCS-T1 matrix authoring only. It does not absorb new
knowledge, complete all planes, edit registries, implement runtime, run live
proof, or make public/production readiness claims.
