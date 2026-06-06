# CVF Work Order - LPCI2-T2 PolicyLocal Frontend Prototype Readiness

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-03

executionBaseHead: `e4bc4b23`

## Purpose

Review the newly added PolicyLocal frontend prototype files in the local
workspace and decide whether they can feed the LPCI2 productization path.

Success means the prototype is classified as visual/product reference,
runtime-ready implementation input, or blocked input with concrete corrective
conditions before scaffold work begins.

## Scope / Target / Owner Boundary

Target: PolicyLocal frontend prototype files under
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal`.

Owner boundary: Codex holds orchestrator, reviewer, worker, and closer roles for
this bounded review because the operator paused external worker delegation.

This work order is documentation and readiness review only. It does not
authorize editing the app into a production scaffold, importing a production
corpus, running provider calls, or claiming legal answer correctness.

## Authority Chain

| Authority | Path or note | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-03 chat request to continue the plan and evaluate new PolicyLocal files | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |
| LPCI2 roadmap | `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` | ACCEPT |
| LPCI2-T1 control packet | `docs/reference/CVF_LPCI2_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| LPCI2-T2 is the scaffold readiness decision tranche | `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` | Roadmap table | LPCI2-T2 | LPCI2 roadmap | ACCEPT |
| PolicyLocal must preserve canonical answer classes | `docs/reference/CVF_LPCI2_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` | Canonical Answer Classes | DIRECT_CITED_ANSWER | LPCI2 build-control packet | ACCEPT |
| PolicyLocal citation minimum includes source hash and normalized path | `docs/reference/CVF_LPCI2_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` | Citation Minimum | sourceHash | LPCI2 build-control packet | ACCEPT |
| Active handoff is the current continuity artifact | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | activeHandoff | AGENT_HANDOFF_V15_2026-05-29.md | Active session registry | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order action | Evidence |
| --- | --- | --- |
| Decide scaffold readiness | Review prototype files against LPCI2-T1 gates | `docs/reviews/CVF_LPCI2_T2_POLICYLOCAL_FRONTEND_PROTOTYPE_READINESS_REVIEW_2026-06-03.md` |
| Keep chat behind import/search/receipt gates | Classify direct app implementation as not yet authorized | Review verdict |
| Preserve PolicyLocal build gate order | Record next allowed move as schema cleanup or production-corpus pilot before broad runtime | Roadmap and session updates |

## Agent Roles

| Role | Owner |
| --- | --- |
| Orchestrator | Codex |
| Implementer | Codex |
| Reviewer | Codex |
| Closer | Codex |
| Operator checkpoint | Only if a runtime build, live provider proof, destructive action, public-sync, or broad scope change is requested |

## Allowed Scope

- Inspect the local `PolicyLocal` prototype files.
- Compare prototype schema, mock data, UI labels, and receipt concepts to the
  LPCI2-T1 build-control packet.
- Create a repo review artifact and a local workspace review copy.
- Update the LPCI2 roadmap and active session continuity.
- Run governance checks and commit the documentation batch.

## Forbidden Scope

- Do not implement or refactor the PolicyLocal runtime.
- Do not convert the static prototype into a Next.js app in this tranche.
- Do not import real legal, policy, notice, decision, SOP, or internal corpus
  files.
- Do not call an LLM provider.
- Do not claim legal advice quality, latest-law status, hosted readiness,
  production readiness, or public export.
- Do not touch public-sync.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`
- `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md`
- `docs/reference/CVF_LPCI2_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal\CLAUDE_BUILD_HANDOFF.md`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal\app.jsx`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal\data\mock.js`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal\components\ui.jsx`

## Pre-Flight Checks

| Check | Result |
| --- | --- |
| `git rev-parse --short HEAD` | `e4bc4b23` |
| `git status --short --branch` | clean before T2 edits |
| `rg` over PolicyLocal answer classes and citation fields | completed |
| PolicyLocal source inspection | completed for landing, app, chat, search, UI, mock data, and handoff files |

## Write Ownership

Owned repo paths:

- `docs/work_orders/CVF_WO_LPCI2_T2_POLICYLOCAL_FRONTEND_PROTOTYPE_READINESS_2026-06-03.md`
- `docs/reviews/CVF_LPCI2_T2_POLICYLOCAL_FRONTEND_PROTOTYPE_READINESS_REVIEW_2026-06-03.md`
- `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`
- `docs/reviews/CVF_LPCI2_T2_SESSION_SYNC_AUTH_2026-06-03.md`

Owned external workspace path:

- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal\CODEX_POLICYLOCAL_FRONTEND_PROTOTYPE_READINESS_REVIEW_2026-06-03.md`

## Execution Plan

1. Inspect the new PolicyLocal prototype files.
2. Compare the prototype with the LPCI2-T1 build-control packet.
3. Record readiness verdict, strengths, blockers, and next gate.
4. Copy the bounded review to the external workspace.
5. Update roadmap and session continuity.
6. Run governance gates and commit.

## Evidence Requirements

Evidence must include:

- PolicyLocal file inventory or searched symbols.
- Specific prototype paths for findings.
- Explicit readiness verdict.
- Runtime and legal-advice boundary.
- Git status and governance gate output.

## Acceptance Criteria

| Criterion | Status |
| --- | --- |
| Visual/product prototype value classified | PASS |
| Canonical schema blockers identified | PASS |
| Runtime implementation boundary preserved | PASS |
| Workspace review copy created | PASS |
| Roadmap/session continuity updated | PASS |

## Review Gate

Reviewer disposition: `CLOSED_PASS_BOUNDED`.

The prototype is accepted as a visual and product reference. It is not accepted
as runtime-ready scaffold input until answer class, receipt, citation, and local
dependency boundaries are normalized.

## Closure Checklist

| Item | Disposition |
| --- | --- |
| Work order created | checked |
| Review artifact created | checked |
| Workspace review copy created | checked |
| Roadmap updated | checked |
| Session sync prepared | checked |
| No runtime/provider/legal-answer claim made | checked |

## Return-To-Orchestrator Conditions

Return to orchestrator if a future task attempts to:

- scaffold chat before import, search, and receipt gates pass;
- store non-canonical answer classes in runtime API or database schema;
- ship remote CDN dependencies as local-first production behavior;
- run provider calls without live diagnostic and secret-safety controls;
- claim latest-law status without verified update-source proof.

## Worker Autonomy / No-Question Rule

The assigned agent may repair documentation and review evidence inside Allowed
Scope without asking the operator. The agent must stop and return to
orchestrator before runtime implementation, public-sync, live provider calls,
secret handling, broad code rewrite, or legal-answer correctness claims.

## Operator Checkpoint

No operator checkpoint remains parked for LPCI2-T2. The next move is a bounded
schema-cleanup/scaffold-readiness correction or the production-corpus pilot
planning tranche.

## Claim Boundary

This work order claims only a bounded review and readiness disposition for the
PolicyLocal frontend prototype.

It does not claim app implementation, Next.js scaffold completion, production
corpus ingestion, provider proof, legal advice quality, latest-law status,
public export, or production readiness.
