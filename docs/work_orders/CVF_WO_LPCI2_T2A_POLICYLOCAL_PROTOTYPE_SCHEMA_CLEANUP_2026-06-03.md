# CVF Work Order - LPCI2-T2A PolicyLocal Prototype Schema Cleanup

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-03

executionBaseHead: `0c4c5ac8`

## Purpose

Repair the concrete schema blockers found in LPCI2-T2 for the local
PolicyLocal prototype before any real chatbot/product implementation begins.

Success means the prototype stores and displays CVF/LPCI canonical answer-class
values, carries the citation minimum in mock corpus and receipt examples, and
has a local validation script that catches regression.

## Scope / Target / Owner Boundary

Target: local external workspace
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local`.

Owner boundary: Codex holds orchestrator, worker, reviewer, and closer roles for
this bounded cleanup. This is a prototype schema cleanup, not a chatbot build.

## Authority Chain

| Authority | Path or note | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-03 chat request to finish groundwork before discussing real PolicyLocal chatbot | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |
| LPCI2 roadmap | `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` | ACCEPT |
| T2 readiness review | `docs/reviews/CVF_LPCI2_T2_POLICYLOCAL_FRONTEND_PROTOTYPE_READINESS_REVIEW_2026-06-03.md` | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| T2 found non-canonical answer classes | `docs/reviews/CVF_LPCI2_T2_POLICYLOCAL_FRONTEND_PROTOTYPE_READINESS_REVIEW_2026-06-03.md` | Findings F2 | DIRECT_CITED_ANSWER | LPCI2-T2 review | ACCEPT |
| Citation minimum requires path/hash/evidence fields | `docs/reference/CVF_LPCI2_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` | Citation Minimum | sourceHash | LPCI2 build-control packet | ACCEPT |
| T2A must not become chatbot runtime | `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` | Roadmap T4 hold | HOLD_UNTIL_T2A_T3_PASS | LPCI2 roadmap | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or review requirement | T2A action | Evidence |
| --- | --- | --- |
| Fix answer-class blocker before scaffold | Add `data/cvf-schema.js` and canonicalize prototype usages | Workspace diff and validator output |
| Fix citation/receipt evidence blocker | Expand mock corpus and sample receipt fields | Workspace diff and validator output |
| Keep chat blocked | Record prototype-only boundary and no provider/live proof | Completion review |

## Agent Roles

| Role | Owner |
| --- | --- |
| Orchestrator | Codex |
| Implementer | Codex |
| Reviewer | Codex |
| Closer | Codex |
| Stop-before-expansion boundary | Runtime scaffold, production corpus import, provider call, public-sync, or legal answer claim |

## Allowed Scope

- Edit static prototype files under `Policy_Local`.
- Add a small schema constants file.
- Add a local validation script.
- Update repo roadmap, review, work order, and session continuity.
- Run local validation and governance gates.

## Forbidden Scope

- Do not build the real PolicyLocal chatbot.
- Do not scaffold a Next.js runtime.
- Do not import production legal/policy corpus files.
- Do not call an LLM provider.
- Do not claim real source-hash proof, legal advice correctness, latest-law
  status, production readiness, hosted readiness, or public export.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`
- `docs/reviews/CVF_LPCI2_T2_POLICYLOCAL_FRONTEND_PROTOTYPE_READINESS_REVIEW_2026-06-03.md`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\CODEX_POLICYLOCAL_FRONTEND_PROTOTYPE_READINESS_REVIEW_2026-06-03.md`

## Pre-Flight Checks

| Check | Result |
| --- | --- |
| `git rev-parse --short HEAD` | `0c4c5ac8` |
| `git status --short --branch` | clean before repo T2A docs |
| PolicyLocal folder existence | PASS at `Policy_Local` |
| T2 blockers identified | PASS |

## Write Ownership

Owned external workspace paths:

- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\cvf-schema.js`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\mock.js`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\i18n.js`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\components\ui.jsx`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\components\screens2.jsx`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\components\screens_chat.jsx`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\app.html`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\landing.html`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\validate-cvf-prototype-schema.mjs`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\CODEX_POLICYLOCAL_SCHEMA_CLEANUP_COMPLETION_2026-06-03.md`

Owned repo paths:

- `docs/work_orders/CVF_WO_LPCI2_T2A_POLICYLOCAL_PROTOTYPE_SCHEMA_CLEANUP_2026-06-03.md`
- `docs/reviews/CVF_LPCI2_T2A_POLICYLOCAL_PROTOTYPE_SCHEMA_CLEANUP_COMPLETION_2026-06-03.md`
- `docs/reviews/CVF_LPCI2_T2A_SESSION_SYNC_AUTH_2026-06-03.md`
- `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`

## Execution Plan

1. Add prototype schema constants and answer-class aliases.
2. Canonicalize mock answer-class values and UI badge handling.
3. Add citation minimum fields and receipt proof-trail fields to mock data.
4. Add a local validation script.
5. Record completion evidence in repo and workspace.
6. Run local validation and governance gates.

## Evidence Requirements

Evidence must show:

- canonical answer classes in prototype runtime-facing data;
- citation minimum fields in mock corpus and receipt examples;
- provider boundary remains prototype-only and selected-excerpt-only;
- validator PASS;
- repo governance gates PASS.

## Acceptance Criteria

| Criterion | Status |
| --- | --- |
| Canonical answer classes used in mock runtime-facing values | PASS |
| Citation minimum represented in mock corpus and receipt | PASS |
| Receipt includes selected/rejected context and answer/provider boundary | PASS |
| Local validator added and PASS | PASS |
| No chatbot/runtime/provider claim made | PASS |

## Review Gate

Reviewer disposition: `CLOSED_PASS_BOUNDED`.

## Closure Checklist

| Item | Disposition |
| --- | --- |
| Workspace schema constants added | checked |
| Prototype mock/schema fixed | checked |
| Validator added | checked |
| Validator run | checked |
| Repo completion artifact created | checked |
| Session sync prepared | checked |

## Return-To-Orchestrator Conditions

Return to orchestrator if the next tranche attempts to reuse prototype
placeholder hashes as real file proof, skips the production corpus pilot, or
starts chat before import, search, citation, and receipt evidence is complete.

## Worker Autonomy / No-Question Rule

The assigned agent must resolve local prototype schema and documentation issues
inside Allowed Scope and rerun the relevant checks. The agent must stop before
runtime scaffold, provider calls, production corpus import, public-sync, secret
handling, or legal answer claims.

## operator.checkpoint.waiver

None parked for T2A. The next move remains production-corpus pilot planning or
a bounded scaffold-readiness decision.

## Claim Boundary

This work order claims only prototype schema cleanup and local validation.

It does not claim production corpus ingestion, real source-hash proof, runtime
chatbot implementation, provider proof, legal advice correctness, latest-law
status, production readiness, hosted readiness, or public export.
