# CVF Work Order - LPCI2-T4S PolicyLocal Data Input Smoke Test

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-04

executionBaseHead: `e5c18554`

## Purpose

Rename the PolicyLocal local corpus drop-zone from `uploads` to `data_input`
and run a bounded import smoke test against the first real files supplied by
the operator.

Success means the local files are enumerated, normalized, SHA-256 hashed, and
recorded in a local manifest without claiming text extraction, legal
classification, search index readiness, provider proof, or chatbot behavior.

## Scope / Target / Owner Boundary

Target: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\`.

Owner boundary: Codex holds orchestrator, worker, reviewer, and closer roles for
this bounded smoke test. The rename reflects local-first product language for
private/internal data; it does not create a hosted upload surface.

## Authority Chain

| Authority | Path or note | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-04 chat request to test the newly added local file or files and rename `uploads` to `data_input` | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |
| LPCI2 roadmap | `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` | ACCEPT |
| T3 pilot plan | `docs/reference/CVF_LPCI2_T3_POLICYLOCAL_PRODUCTION_CORPUS_PILOT_PLAN_2026-06-03.md` | ACCEPT |
| GC-051 registry | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| T3 allowed import-first T4 when real files exist | `docs/reference/CVF_LPCI2_T3_POLICYLOCAL_PRODUCTION_CORPUS_PILOT_PLAN_2026-06-03.md` | T4 Release Conditions | Import-first T4 | LPCI2-T3 plan | ACCEPT |
| GC-051 entry exists | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | corpora entry | policylocal-production-corpus-dropzone | GC-051 registry | ACCEPT |
| Per-file sourceHash is required before runtime claims | `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` | Source Hash Policy | sourceHash | LPCI1 T1 intake | ACCEPT |
| Runtime answer boundary must not be upgraded from deferred records | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | Answer Assembly Rules | ESCALATE_OR_ABSTAIN | LPCI1 T4 retrieval | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | T4S action | Evidence |
| --- | --- | --- |
| Use local-first corpus folder | Rename `uploads` to `data_input` | External workspace listing |
| Test first real files | Hash and normalize two DOCX files | Local manifest |
| Preserve runtime boundary | Mark record `HASHED_ONLY` and answerClass `ESCALATE_OR_ABSTAIN` | Manifest + completion |
| Keep next tranche clear | Defer DOCX extraction/classification to bounded T4 | Registry finding |

## Agent Roles

| Role | Owner |
| --- | --- |
| Orchestrator | Codex |
| Implementer | Codex |
| Reviewer | Codex |
| Closer | Codex |
| Stop-before-expansion boundary | DOCX text extraction, legal classification, search index, provider call, chat runtime, public-sync |

## Allowed Scope

- Rename external folder `Policy_Local\uploads` to `Policy_Local\data_input`.
- Add a local smoke-test script under `Policy_Local\scripts`.
- Generate a local manifest under `Policy_Local\data\generated`.
- Update GC-051 registry, LPCI2 roadmap, completion review, and session
  continuity.
- Run local Node validation and governance gates.

## Forbidden Scope

- Do not extract legal text from DOCX in this tranche.
- Do not classify law/policy domain fields beyond `unknown`.
- Do not build search, retrieval, chat, vector, or provider runtime.
- Do not claim legal advice correctness, latest-law status, production
  readiness, hosted readiness, or public export.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`
- `docs/reference/CVF_LPCI2_T3_POLICYLOCAL_PRODUCTION_CORPUS_PILOT_PLAN_2026-06-03.md`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`

## Pre-Flight Checks

| Check | Result |
| --- | --- |
| `git rev-parse --short HEAD` | `e5c18554` |
| `git status --short --branch` | clean before T4S repo edits |
| `Policy_Local\uploads` | existed with one file before rename; final smoke run observed two DOCX files after local additions |
| `Policy_Local\data_input` | did not exist before rename |

## Write Ownership

Owned external workspace paths:

- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\policylocal-import-smoke.mjs`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-data-input-manifest.json`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\CODEX_POLICYLOCAL_DATA_INPUT_SMOKE_TEST_COMPLETION_2026-06-04.md`

Owned repo paths:

- `docs/work_orders/CVF_WO_LPCI2_T4S_POLICYLOCAL_DATA_INPUT_SMOKE_TEST_2026-06-04.md`
- `docs/reviews/CVF_LPCI2_T4S_POLICYLOCAL_DATA_INPUT_SMOKE_TEST_COMPLETION_2026-06-04.md`
- `docs/reviews/CVF_LPCI2_T4S_SESSION_SYNC_AUTH_2026-06-04.md`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md`
- `docs/reference/CVF_LPCI2_T3_POLICYLOCAL_PRODUCTION_CORPUS_PILOT_PLAN_2026-06-03.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`

## Execution Plan

1. Rename `uploads` to `data_input`.
2. Add `policylocal-import-smoke.mjs`.
3. Run `node --check` and smoke test.
4. Record manifest result and update GC-051.
5. Update roadmap and continuity.
6. Run governance gates.

## Evidence Requirements

Evidence must show:

- exact file paths under `data_input`;
- `normalizedPath`;
- SHA-256 source hash;
- `HASHED_ONLY` and `DEFERRED_DOCX_TEXT_EXTRACTION` boundaries;
- no runtime/provider/legal answer claims.

## Acceptance Criteria

| Criterion | Status |
| --- | --- |
| Folder renamed to `data_input` | PASS |
| Two DOCX files detected | PASS |
| Per-file SHA-256 produced for both files | PASS |
| Normalized path produced for both files | PASS |
| DOCX extraction deferred honestly | PASS |
| No runtime/chat/provider/legal answer claim made | PASS |

## Review Gate

Reviewer disposition: `CLOSED_PASS_BOUNDED`.

## Closure Checklist

| Item | Disposition |
| --- | --- |
| Folder rename completed | checked |
| Smoke script added | checked |
| Local manifest generated | checked |
| GC-051 registry updated | checked |
| Completion review created | checked |
| Session sync prepared | checked |

## Return-To-Orchestrator Conditions

Return to orchestrator if future work tries to use this hash-only manifest as
text extraction proof, upgrades `ESCALATE_OR_ABSTAIN` to `DIRECT_CITED_ANSWER`,
or starts chat runtime before DOCX extraction and domain classification pass.

## Worker Autonomy / No-Question Rule

The assigned agent must fix local smoke-test and documentation issues inside
Allowed Scope and rerun checks. The agent must stop before text extraction,
runtime scaffold, provider calls, public-sync, secret handling, or legal answer
claims.

## operator.checkpoint.waiver

None parked for T4S. The next move is a bounded T4 import/classification tranche
for DOCX text extraction and legal/policy field population.

## Claim Boundary

This work order claims only local folder rename and hash-only import smoke
testing.

It does not claim corpus text extraction, legal/policy classification, search
index readiness, retrieval behavior, provider proof, legal advice correctness,
latest-law status, production readiness, hosted readiness, or public export.
