# CVF GC-018 - FPC-T2 System-Loop Interlock Expansion Decision

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-13

Owner: Codex

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `3f57bf18`

sourceAuthority:
`docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md`

rawMemoryReleased=false

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_FOR_CLAUDE_2026-06-13.md`

parentRoadmap:
`docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md`

fpcT1Matrix:
`docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md`

## Purpose

Authorize FPC-T2 as a bounded foundation decision tranche. Claude must evaluate
the FPC-T2 candidates produced by FPC-T1 and decide whether each candidate
should become a formal system-loop interlock entry later, remain structural,
wait for a machine check, defer because owner evidence is missing, or be
rejected with reason.

FPC-T2 is a decision tranche only. It does not authorize interlock registry
edits, checker implementation, runtime/source/test mutation, downstream
Document Translator or Policy_Local work, provider/OCR/live proof, public-sync,
readiness/cost/quality claims, memory reinjection, high-risk promotion, or
autonomous mutation.

## Scope / Target / Owner Boundary

Target: one FPC-T2 decision matrix and one worker-return packet.

Owner boundary: Codex owns orchestration, dispatch, review, commit, closure
conversion, any future session-state sync, and any later registry-edit work
order. Claude owns only the allowed FPC-T2 decision artifacts under
`WORKER_MUST_NOT_COMMIT`.

## Decision / Baseline / Proposed Tranche

Decision: open FPC-T2 after FPC-T1 closed with a source-backed candidate list.

Baseline:

- current dispatch base: `3f57bf18`;
- FPC-T1 material closure commit: `91e8f10f`;
- FPC-T1 provider-source hygiene commit: `d6c31c6d`;
- parent roadmap status after this dispatch:
  `FPC_T2_DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT`;
- active mode before this dispatch:
  `fpc_t1_foundation_planes_workflow_chain_system_audit_closed_pass_bounded`.

Proposed tranche:

- evaluate FPC-T2-C01 through FPC-T2-C05 from the FPC-T1 matrix;
- reconcile each candidate against existing interlock registry entries and
  existing governed owner surfaces;
- produce a per-candidate disposition using the roadmap-approved disposition
  vocabulary;
- include proposed registry-entry shape only for candidates whose disposition
  is `ADD_INTERLOCK_ENTRY`;
- return uncommitted artifacts for Codex review.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| FPC-T1 closed | FPC-T1 completion review and matrix; material commit `91e8f10f` | ACCEPT |
| Provider-specific authority cleanup complete | `d6c31c6d` replaced provider-specific source citations and added guard coverage | ACCEPT |
| Active state permits FPC-T2 | `CVF_SESSION/ACTIVE_SESSION_STATE.json` `nextAllowedMove` says FPC-T2 may open through fresh GC-018 and source-verified work order | ACCEPT |
| Fresh FPC-T2 baseline exists | this file | ACCEPT |
| Paired FPC-T2 work order exists | `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_FOR_CLAUDE_2026-06-13.md` | ACCEPT |

## Knowledge Absorption Blind-Spot Control Block

| Control item | Evidence | Disposition |
| --- | --- | --- |
| Prior absorption evidence resolved | FPC roadmap, FPC-T1 matrix, FPC-T1 completion, and system-loop interlock standard are governing input | COMPLETE |
| Detailed source files required | paired work order lists required first reads and source-authority files | COMPLETE |
| Current owner surfaces checked | FPC-T2 must source-verify each candidate against the current registry and owner artifacts before assigning disposition | COMPLETE |
| Accept/defer/reject dispositions recorded | FPC-T2 decision matrix must use only approved disposition tokens | COMPLETE |
| Adversarial role review applied | worker return must include duplicate-interlock, use-case drift, provider-source drift, and premature-implementation checks | COMPLETE |
| Blind-spot delta | registry edits, checker implementation, runtime mutation, use-case work, live proof, public-sync, and provider-specific memory-as-source are excluded | COMPLETE |

Verdict: `COMPLETE_WITH_DECLARED_BOUNDARIES`.

## Rescan Intelligence Hardening

Original source artifact: FPC-T1 audit matrix and current CVF governed
interlock artifacts, not provider-specific agent memory.

Predecessor intake artifact:

- `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md`;
- `docs/reviews/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_COMPLETION_2026-06-13.md`;
- `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md`;
- `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`.

- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

Delta ledger status: COMPLETE

Routing matrix status: COMPLETE

Semantic sampling status: COMPLETE

### Original-Intake Delta Ledger

| sampleId | Delta category | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| FPC-T2-GC018-D1 | UNCHANGED_FROM_INTAKE | FPC roadmap FPC-T2 | candidates are evaluated, not pre-accepted | decision-only work order | Could this dispatch registry edits early? | PASS |
| FPC-T2-GC018-D2 | CHANGED_DISPOSITION | FPC-T1 matrix | five candidates exist | require per-candidate disposition | Could candidate wording be treated as approval? | PASS |
| FPC-T2-GC018-D3 | NEW_FINDING | provider-source hygiene cleanup | provider files are not CVF authority | require CVF-governed sources only | Could Claude cite provider memory as evidence? | PASS |
| FPC-T2-GC018-D4 | REMOVED_OR_REJECTED | use-case pressure | downstream adapters are tempting | keep DT/Policy_Local/OCR/provider out of scope | Could worker inspect use-case repos? | PASS |

### Follow-Up Routing Matrix

| Route lane | Target | Disposition | Evidence | Next action |
| --- | --- | --- | --- | --- |
| DO_NOW | FPC-T2 decision matrix and worker return | ACCEPT | this GC-018 and paired work order | Claude executes allowed artifacts |
| SEPARATE_RUNTIME_TRANCHE | runtime/source/test edits, provider/OCR/API, retrieval, live proof, or app route wiring | DEFER | runtime authorization boundary | fresh operator authorization required |
| SEPARATE_REGISTRY_TRANCHE | registry edits for accepted interlocks | DEFER | roadmap requires explicit registry-edit authorization | Codex decides after worker return |
| SEPARATE_CHECKER_TRANCHE | FPC-T3 checker/template planning or implementation | DEFER | FPC-T3 remains parked until FPC-T2 closes | later fresh GC-018 |
| STRATEGIC_OPERATOR_DECISION | downstream use cases, live proof, public-sync, readiness/cost/quality | DEFER | active parked checkpoints | operator decision later |
| OUT_OF_SCOPE | external app source, provider-specific memory authority, runtime mutation | REJECT | forbidden scope | no access or action |
| RESOLVED_BY_DESIGN | worker commits and direct registry mutation | REJECT | `WORKER_MUST_NOT_COMMIT`; this GC-018 claim boundary | Codex reviews and commits; registry mutation requires a separate work order |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- |
| FPC-T2-GC018-S1 | FPC roadmap FPC-T2 | decide for each candidate | work order requires decision table | Could worker omit rejected/deferred candidates? | PASS |
| FPC-T2-GC018-S2 | FPC roadmap FPC-T2 registry boundary | no registry edit unless explicitly authorized | this baseline forbids registry mutation | Could decision matrix edit registry? | PASS |
| FPC-T2-GC018-S3 | FPC-T1 matrix constraints | C05 needs MLW3 reconciliation | work order requires C05 reconciliation section | Could C05 duplicate MLW3? | PASS |
| FPC-T2-GC018-S4 | provider-source boundary | provider memory is not authority | work order forbids provider-memory source citations | Could provider files become source truth again? | PASS |

## Current Runtime Freshness Verification

| Source fact | Verification command or evidence | Disposition |
| --- | --- | --- |
| No runtime/source/test edit is authorized | paired work order Forbidden Scope; `git diff --name-status` must contain no runtime/source/test path | ACCEPT |
| No interlock registry edit is authorized | paired work order Forbidden Scope; `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` is read-only input | ACCEPT |
| Existing registry reconciliation must use current registry | Required First Reads include `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`; worker must cite current entries or mark source gap | ACCEPT |
| Provider-specific memory/guidance is not source authority | `AGENTS.md` provider-specific boundary; `check_agent_packet_authority_and_encoding.py` gate | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: FPC roadmap records FPC-T2 dispatch | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | Status | `FPC_T2_DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT` | FPC roadmap | ACCEPT |
| EXISTS: FPC-T2 requires fresh GC-018/work order | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `Accepted next-route result` | fresh GC-018 and source-verified work order | FPC roadmap | ACCEPT |
| EXISTS: FPC-T2 purpose is interlock expansion decision | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `## FPC-T2 - System-Loop Interlock Expansion Decision` | system-loop interlock expansion decision | FPC roadmap | ACCEPT |
| EXISTS: FPC-T2 candidate disposition vocabulary | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `FPC-T2 must decide for each candidate` | `ADD_INTERLOCK_ENTRY`; `KEEP_STRUCTURAL_ONLY`; `MACHINE_CHECK_FIRST`; `DEFER_RUNTIME_OWNER_MISSING`; `REJECT_WITH_REASON`; `SOURCE_GAP_BLOCKS_DISPATCH` | FPC roadmap | ACCEPT |
| EXISTS: FPC-T2 registry edit boundary | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `FPC-T2 must not edit the registry unless...` | interlock registry | FPC roadmap | ACCEPT |
| EXISTS: FPC-T1 accepted five FPC-T2 candidates | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | `## FPC-T2 Candidate List` | `FPC-T2-C01` through `FPC-T2-C05` | FPC-T1 matrix | ACCEPT |
| EXISTS: FPC-T2-C05 MLW3 reconciliation constraint | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | `## FPC-T2 / FPC-T3 Decision Constraints` | `FPC-T2-C05` | FPC-T1 matrix | ACCEPT |
| EXISTS: system-loop interlock registry owner | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md` | `## Registry` | `CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | system-loop interlock standard | ACCEPT |
| EXISTS: registry field vocabulary includes automation and claim boundary | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md` | field table | `automationLevel`; `claimBoundary` | system-loop interlock standard | ACCEPT |
| EXISTS: existing scan-to-learning interlock for reconciliation | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | connection id | `scan-loop-to-learning-loop` | system-loop interlock registry | ACCEPT |
| EXISTS: provider-specific agent files are not CVF authority | `AGENTS.md` | `Mandatory Provider-Specific Agent Memory Boundary` | `NOT_CVF_SOURCE` | agent front-door instructions | ACCEPT |

## Authorized Artifact Set

Claude may create or update only:

- `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md`;
- `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_WORKER_RETURN_2026-06-13.md`;
- the paired work order only if adding worker-return evidence is necessary.

## Forbidden Scope

FPC-T2 authorizes no interlock registry edit, runtime/source/test
implementation, checker/template implementation, generated aggregate edit,
session-state edit, external Document Translator source inspection, Policy_Local
source inspection, OCR/provider/API/live proof, retrieval route wiring, corpus
ingestion, public-sync, readiness claim, cost claim, quality claim,
provider-specific memory-as-source claim, memory reinjection, high-risk
promotion, or autonomous mutation.

## Evidence / Verification

Required dispatch verification:

- reviewer-fast gate passes on this dispatch package;
- pre-dispatch autorun gate passes on the real changed range;
- pre-commit governance chain passes before Codex commits the dispatch package.

Required worker verification is defined in the paired work order.

Closure verification:

- worker-return artifacts accepted by Codex after review;
- reviewer-fast PASS;
- `git diff --check` PASS;
- FPC-T2 remains decision-only and does not mutate the registry.

Closure artifacts:

- decision matrix:
  `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md`;
- worker return:
  `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_WORKER_RETURN_2026-06-13.md`;
- completion review:
  `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_COMPLETION_2026-06-13.md`.

Closure result: FPC-T2-C01 through FPC-T2-C04 are accepted as proposal-only
`ADD_INTERLOCK_ENTRY` decisions requiring a later registry-edit work order.
FPC-T2-C05 is accepted as `MACHINE_CHECK_FIRST` pending FPC-T3-C01.

## Claim Boundary

This GC-018 authorizes a source-backed FPC-T2 decision matrix only. It does not
authorize interlock registry mutation, FPC-T3 checker/template planning or
implementation, runtime behavior changes, provider/OCR/live proof, external app
source work, public-sync, production/public/readiness/cost/quality claims,
memory reinjection, high-risk promotion, or autonomous mutation.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance FPC-T2 dispatch baseline. Public-sync is not
authorized.
