# CVF Work Order - LPCI2-T3 Production Corpus Pilot Planning

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-03

executionBaseHead: `6f1f6a95`

## Purpose

Define the first PolicyLocal production-corpus pilot boundary before any real
runtime chatbot implementation begins.

Success means PolicyLocal has a GC-051 registered production drop-zone, a
source-backed pilot plan, legal/policy domain fields, sampling gates, and a
clear stop condition that prevents T4 from treating prototype mock data as real
legal/policy corpus proof.

## Scope / Target / Owner Boundary

Target: PolicyLocal production corpus planning for
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\uploads\`.

Owner boundary: Codex holds orchestrator, worker, reviewer, and closer roles
for this bounded planning tranche. This is planning and registry preparation
only; it does not ingest, classify, index, query, or answer against real
documents.

## Authority Chain

| Authority | Path or note | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-03 chat request to continue PolicyLocal groundwork before real chatbot discussion | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |
| LPCI2 roadmap | `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` | ACCEPT |
| LPCI1 T7 packaging spec | `docs/reference/CVF_LPCI1_T7_TEMPLATE_PACKAGING_SPEC_2026-06-03.md` | ACCEPT |
| GC-051 registry | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| PolicyLocal T4 is held until T2A and T3 pass | `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` | Roadmap table | HOLD_UNTIL_T2A_T3_PASS | LPCI2 roadmap | ACCEPT |
| Downstream adoption begins with GC-051 registration | `docs/reference/CVF_LPCI1_T7_TEMPLATE_PACKAGING_SPEC_2026-06-03.md` | Downstream Workspace Adoption Guide | GC-051 corpus registration | LPCI1 T7 template | ACCEPT |
| Legal/policy corpus records must carry normalizedPath and sourceHash | `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` | Source Hash Policy; NR-05 normalizedPath Adoption | sourceHash | LPCI1 T1 intake spec | ACCEPT |
| Query index depends on normalizedPath/sourceHash/domain fields | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | Index Record Schema | normalizedPath | LPCI1 T3 index spec | ACCEPT |
| Retrieval answer boundary uses canonical answer classes | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | Answer Assembly Rules | DIRECT_CITED_ANSWER | LPCI1 T4 retrieval spec | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | T3 action | Evidence |
| --- | --- | --- |
| Define first real corpus | Register production drop-zone as GC-051 `POLICY_DOCUMENT` entry with `status=NOT_STARTED` | GC-051 registry diff |
| Define legal/policy fields | Create pilot plan with domain field schema and intake checklist | T3 pilot plan |
| Define sampling plan | Add pre-runtime sampling gate and fail conditions | T3 pilot plan and completion review |
| Keep runtime blocked | Keep T4 status held until import/hash/classification evidence exists | Roadmap update |

## Agent Roles

| Role | Owner |
| --- | --- |
| Orchestrator | Codex |
| Implementer | Codex |
| Reviewer | Codex |
| Closer | Codex |
| Stop-before-expansion boundary | Real file import, OCR/PDF extraction, vector index, LLM call, legal answer claim, or public-sync |

## Allowed Scope

- Update GC-051 registry with a `NOT_STARTED` production-corpus drop-zone entry.
- Create the LPCI2-T3 production-corpus pilot plan.
- Create a bounded completion review.
- Update LPCI2 roadmap and active session continuity.
- Run local validation and governance gates.

## Forbidden Scope

- Do not ingest real legal/policy documents.
- Do not compute fake per-file source hashes for absent production files.
- Do not build a vector store, database, API route, or chat runtime.
- Do not call an LLM provider.
- Do not claim legal advice correctness, latest-law status, production
  readiness, hosted readiness, or public export.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`
- `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md`
- `docs/reference/CVF_LPCI1_T7_TEMPLATE_PACKAGING_SPEC_2026-06-03.md`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`

## Pre-Flight Checks

| Check | Result |
| --- | --- |
| `git rev-parse --short HEAD` | `6f1f6a95` |
| `git status --short --branch` | clean before T3 edits |
| PolicyLocal upload folder | exists but contains zero production files |
| T2A validator | PASS before T3 planning |

## Write Ownership

Owned repo paths:

- `docs/work_orders/CVF_WO_LPCI2_T3_PRODUCTION_CORPUS_PILOT_PLANNING_2026-06-03.md`
- `docs/reference/CVF_LPCI2_T3_POLICYLOCAL_PRODUCTION_CORPUS_PILOT_PLAN_2026-06-03.md`
- `docs/reviews/CVF_LPCI2_T3_POLICYLOCAL_PRODUCTION_CORPUS_PILOT_PLANNING_COMPLETION_2026-06-03.md`
- `docs/reviews/CVF_LPCI2_T3_SESSION_SYNC_AUTH_2026-06-03.md`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`

## Execution Plan

1. Confirm the local PolicyLocal upload drop-zone exists.
2. Add a GC-051 registry entry for the production drop-zone with
   `status=NOT_STARTED`.
3. Create the pilot plan with corpus root, domain fields, import gates,
   sampling protocol, and T4 release conditions.
4. Update the LPCI2 roadmap to mark T3 closed and keep runtime held until real
   import evidence exists.
5. Record completion evidence and run governance gates.

## Evidence Requirements

Evidence must show:

- the drop-zone is registered in GC-051;
- fileCount is zero and no production corpus is falsely claimed;
- the pilot plan names per-file hash, normalizedPath, domain fields, answer
  boundary, sampling, and release gates;
- T4 remains blocked from broad chat runtime.

## Acceptance Criteria

| Criterion | Status |
| --- | --- |
| GC-051 production drop-zone entry added | PASS |
| Pilot plan created | PASS |
| Upload folder emptiness honestly recorded | PASS |
| T4 release conditions tightened | PASS |
| No runtime/provider/legal-answer claim made | PASS |

## Review Gate

Reviewer disposition: `CLOSED_PASS_BOUNDED`.

## Closure Checklist

| Item | Disposition |
| --- | --- |
| GC-051 entry added | checked |
| T3 pilot plan created | checked |
| Completion review created | checked |
| Roadmap updated | checked |
| Session sync prepared | checked |

## Return-To-Orchestrator Conditions

Return to orchestrator if future work tries to import files outside the
registered drop-zone, treats placeholder hashes as production evidence, skips
GC-047/GC-050, or starts chat runtime before search/filter and receipt evidence
exist.

## Worker Autonomy / No-Question Rule

The assigned agent must resolve T3 documentation, registry, and gate issues
inside Allowed Scope and rerun the relevant checks. The agent must stop before
real file import, runtime scaffold, provider calls, public-sync, secret
handling, or legal answer claims.

## operator.checkpoint.waiver

None parked for T3. The next move is a bounded T4 import/scaffold tranche only
after the operator supplies or selects real corpus files under the registered
drop-zone.

## Claim Boundary

This work order claims only production-corpus pilot planning and GC-051
drop-zone registration.

It does not claim corpus ingestion, per-file source-hash proof, search index
availability, runtime chatbot implementation, provider proof, legal advice
correctness, latest-law status, production readiness, hosted readiness, or
public export.
