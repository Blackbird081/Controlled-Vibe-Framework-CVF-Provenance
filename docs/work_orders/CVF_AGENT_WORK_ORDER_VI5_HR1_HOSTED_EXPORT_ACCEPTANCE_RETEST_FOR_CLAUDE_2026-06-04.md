# CVF Agent Work Order - VI5-HR1 Hosted Export Acceptance Retest For Claude

Memory class: POINTER_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-06-04

Worker: Claude

dispatchBaseHead: `7c082836`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `NOT_EXECUTED_YET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Execute the bounded VI5-HR1 hosted export acceptance retest. Success means
Claude verifies whether the hosted Surface 1 web UI currently exposes the
VI5-T5 portable handoff improvements for `app_builder_complete` English full
export, then evaluates that fresh exported packet as an external receiving
agent. The result must be a private review artifact, not a public readiness
claim.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator authorization | 2026-06-04 request to create Claude work order after Codex recommended hosted/public-facing freshness retest | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |
| Fresh GC-018 | `docs/baselines/CVF_GC018_VI5_T4_T5_HOSTED_EXPORT_ACCEPTANCE_RETEST_2026-06-04.md` | ACCEPT |
| VI5 predecessor completion | `docs/reviews/archive/CVF_VI5_T4_T5_SURFACE1_EXPORT_ACCEPTANCE_AND_PORTABLE_HANDOFF_COMPLETION_2026-05-26.md` | ACCEPT |
| ERH cleanup boundary | `docs/reviews/CVF_ERH_INITIAL_PRIVATE_TRANCHES_COMPLETION_2026-06-04.md` | ACCEPT |

Authority boundary:

- This work order does not authorize DEP2, dependency migration, auth runtime
  edits, route live proof, public-sync, push, hosted production certification,
  or public readiness.
- If the hosted UI is stale, inaccessible, or does not expose the expected
  export, return a blocked/hold review packet instead of editing source.

## Agent Roles

| Role | Assignee | Boundary |
| --- | --- | --- |
| Orchestrator / dispatcher | Codex | authored fresh GC-018 and work order |
| Implementer / external-agent evaluator | Claude | browser-hosted retest and private review artifact only |
| Reviewer / committer | Codex or operator | review Claude artifact, decide commit/closure |
| Operator approval required for | source edits, public-sync, push, secrets/quota, route live proof, public readiness claim | not granted here |

## Scope / Target / Owner Boundary

Allowed scope:

- inspect `https://vibcode.netlify.app/home`;
- use the hosted UI to generate or copy an `app_builder_complete` English Full
  / CVF Guided Agent export;
- evaluate the fresh export using the VI5 operator/external-agent review gate;
- create or update only the review artifact:
  `docs/reviews/CVF_VI5_HR1_HOSTED_EXPORT_ACCEPTANCE_RETEST_CLAUDE_REVIEW_2026-06-04.md`;
- record safe diagnostics for hosted/browser failure.

Forbidden scope:

- edit runtime source, tests, package manifests, lockfiles, workflows, or
  public-sync clone files;
- use API keys, service tokens, provider credits, or hosted `/api/execute`
  governance proof;
- claim production readiness, hosted SaaS readiness, public readiness, all-route
  proof, all-template portability, or dependency/security clearance;
- commit or push.

Risk ceiling: R1 hosted/browser evidence review only.

## Required First Reads

| Path | Why it matters |
| --- | --- |
| `docs/baselines/CVF_GC018_VI5_T4_T5_HOSTED_EXPORT_ACCEPTANCE_RETEST_2026-06-04.md` | current authorization |
| `docs/reviews/archive/CVF_VI5_T4_T5_SURFACE1_EXPORT_ACCEPTANCE_AND_PORTABLE_HANDOFF_COMPLETION_2026-05-26.md` | acceptance packet and external-agent prompt |
| `docs/work_orders/archive/CVF_WO_VI5_T4_T5_SURFACE1_EXPORT_ACCEPTANCE_AND_PORTABLE_HANDOFF_2026-05-26.md` | original operator checkpoint and scope |
| `docs/concepts/archive/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md` | hosted Surface 1 target and surface fidelity boundary |
| `docs/reviews/CVF_ERH_INITIAL_PRIVATE_TRANCHES_COMPLETION_2026-06-04.md` | current ERH boundary and remaining hosted-readiness gap |

## Write Ownership

Owned path:

- `docs/reviews/CVF_VI5_HR1_HOSTED_EXPORT_ACCEPTANCE_RETEST_CLAUDE_REVIEW_2026-06-04.md`

Read-only evidence inputs:

- `docs/baselines/CVF_GC018_VI5_T4_T5_HOSTED_EXPORT_ACCEPTANCE_RETEST_2026-06-04.md`
- `docs/reviews/archive/CVF_VI5_T4_T5_SURFACE1_EXPORT_ACCEPTANCE_AND_PORTABLE_HANDOFF_COMPLETION_2026-05-26.md`
- `docs/work_orders/archive/CVF_WO_VI5_T4_T5_SURFACE1_EXPORT_ACCEPTANCE_AND_PORTABLE_HANDOFF_2026-05-26.md`
- `docs/concepts/archive/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md`

Forbidden write paths:

- `EXTENSIONS/**`
- `.github/**`
- `docs/roadmaps/**`
- `docs/reference/**`
- `docs/baselines/**`
- sibling public-sync clone

Write mode: create/update the single owned review artifact only.

## Pre-Flight Checks

Claude must run before hosted retest:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path docs/baselines/CVF_GC018_VI5_T4_T5_HOSTED_EXPORT_ACCEPTANCE_RETEST_2026-06-04.md
Test-Path docs/reviews/archive/CVF_VI5_T4_T5_SURFACE1_EXPORT_ACCEPTANCE_AND_PORTABLE_HANDOFF_COMPLETION_2026-05-26.md
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 7c082836 --head HEAD
```

Expected results:

- current execution head captured and recorded in the review artifact;
- worktree state recorded;
- required paths exist;
- pre-implementation gate passes or any failure is classified before retest.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: current GC-018 baseline for HR1 | `docs/baselines/CVF_GC018_VI5_T4_T5_HOSTED_EXPORT_ACCEPTANCE_RETEST_2026-06-04.md` | file source | `CVF_GC018_VI5_T4_T5_HOSTED_EXPORT_ACCEPTANCE_RETEST_2026-06-04.md` | HR1 baseline | ACCEPT |
| EXISTS: hosted Surface 1 URL | `docs/concepts/archive/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md` | Source / Predecessor Evidence | `vibcode.netlify.app/home` | Surface Fidelity evidence | ACCEPT |
| EXISTS: web product surface URL | `docs/concepts/archive/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md` | Web product surface | `vibcode.netlify.app/home` | Surface Fidelity evidence | ACCEPT |
| EXISTS: VI5-T4/T5 completion packet | `docs/reviews/archive/CVF_VI5_T4_T5_SURFACE1_EXPORT_ACCEPTANCE_AND_PORTABLE_HANDOFF_COMPLETION_2026-05-26.md` | file source | `CVF_VI5_T4_T5_SURFACE1_EXPORT_ACCEPTANCE_AND_PORTABLE_HANDOFF_COMPLETION_2026-05-26.md` | VI5 completion | ACCEPT |
| VALUE_SET: external-agent verdict values | `docs/reviews/archive/CVF_VI5_T4_T5_SURFACE1_EXPORT_ACCEPTANCE_AND_PORTABLE_HANDOFF_COMPLETION_2026-05-26.md` | Operator Acceptance Packet | `PASS`, `PASS_WITH_MINOR_FIX`, `HOLD` | VI5 operator review gate | ACCEPT |
| EXISTS: expected export section literal | `docs/reviews/archive/CVF_VI5_T4_T5_SURFACE1_EXPORT_ACCEPTANCE_AND_PORTABLE_HANDOFF_COMPLETION_2026-05-26.md` | Scope / Target / Owner Boundary | `Portable Agent Handoff Readiness` | VI5 export completion | ACCEPT |
| EXISTS: original operator checkpoint | `docs/work_orders/archive/CVF_WO_VI5_T4_T5_SURFACE1_EXPORT_ACCEPTANCE_AND_PORTABLE_HANDOFF_2026-05-26.md` | Operator Checkpoint | `Operator Checkpoint` | VI5 work order | ACCEPT |
| EXISTS: hosted retest remains open after ERH cleanup | `docs/reviews/CVF_ERH_INITIAL_PRIVATE_TRANCHES_COMPLETION_2026-06-04.md` | Remaining Work That Is Not Closed Here | `Hosted public readiness` | ERH initial closure | ACCEPT |

## New Doc-Only Fields

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
| --- | --- | --- | --- | --- |
| `HOSTED_FRESH_PASS` | Claude found expected hosted export section and external-agent verdict is PASS | Yes | Yes | review artifact only |
| `HOSTED_FRESH_PASS_WITH_MINOR_FIX` | Claude found expected hosted export section but minor wording/action issue remains | Yes | Yes | review artifact only |
| `HOSTED_STALE_HOLD` | hosted export lacks expected VI5-T5 section or appears stale | Yes | Yes | review artifact with evidence |
| `BLOCKED_HOSTED_UNAVAILABLE` | hosted UI/export path cannot be reached or completed | Yes | Yes | live run diagnostic required |
| `BLOCKED_BROWSER_OR_TOOLING` | Claude cannot perform the browser/export interaction | Yes | Yes | diagnostic and return-to-orchestrator action |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or predecessor requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| VI5-T4 operator manual export and external-agent review remains pending | Purpose, Scope, Execution Plan | Claude review artifact | hosted export evidence plus verdict | PASS |
| VI5-T5 portable handoff block must appear in fresh export | Acceptance Criteria | `Portable Agent Handoff Readiness` evidence | fresh hosted export inspection | PASS |
| ERH cleanup says hosted readiness remains separate | Authority Chain, Claim Boundary | no public/production claim | public export disposition and claim boundary | PASS |
| Worker must not commit | Commit mode, Review Gate | pending review artifact | `git status --short` in worker handoff | PASS |

## Worker Autonomy / No-Question Rule

Claude proceeds autonomously for reading required files, browsing the hosted
target, generating/copying the export, writing the allowed review artifact,
adding required evidence sections, and rerunning allowed docs/gate checks.

Escalation is reserved for source edits, public-sync, push, secrets/quota,
provider/API calls, hosted `/api/execute` proof, destructive actions, claim
boundary expansion, or any work outside the allowed review artifact.

## Execution Plan

| Step | Input | Output | Validation / Stop condition |
| --- | --- | --- | --- |
| 1 | required first reads | execution anchor and worktree state | stop if required source path missing |
| 2 | `https://vibcode.netlify.app/home` | hosted reachability result | if unreachable, record `BLOCKED_HOSTED_UNAVAILABLE` diagnostic |
| 3 | hosted UI | fresh `app_builder_complete` English Full / CVF Guided Agent export | if export cannot be produced, record `BLOCKED_BROWSER_OR_TOOLING` or hosted diagnostic |
| 4 | exported markdown | section and chrome check | if `Portable Agent Handoff Readiness` absent, return `HOSTED_STALE_HOLD` |
| 5 | exported markdown | external-agent readiness evaluation | return `PASS`, `PASS_WITH_MINOR_FIX`, or `HOLD` with reasons |
| 6 | all evidence | allowed review artifact | run component docs/gates and leave pending review, no commit |

## Required Review Artifact

Claude must create or update:

`docs/reviews/CVF_VI5_HR1_HOSTED_EXPORT_ACCEPTANCE_RETEST_CLAUDE_REVIEW_2026-06-04.md`

Required sections:

- `## Purpose`
- `## Target / Source`
- `## Scope / Target / Owner Boundary`
- `## Evidence Trace Block`
- `## Hosted Retest Result`
- `## External-Agent Evaluation`
- `## Findings / Position`
- `## Risk / Corrective Action`
- `## Live Run Diagnostics`
- `## Claim Integrity Scan`
- `## Finding-To-Governance Learning Disposition`
- `## Public Export Disposition`
- `## Claim Boundary`

## Evidence Requirements

Required evidence:

- hosted URL and timestamp;
- executionBaseHead captured by Claude;
- safe description of steps used to reach/export the packet;
- whether the exported packet contains `Portable Agent Handoff Readiness`;
- whether packet chrome is English while source values are preserved;
- external-agent verdict and short rationale;
- sanitized excerpt no longer than needed to prove the presence/absence of key
  section headings;
- `git status --short` showing pending artifact state;
- governance component gates run from the provenance repo.

Live run diagnostic requirement:

- If browser/hosted/export interaction fails, times out, returns unexpected
  content, or must be rerun, classify the failure before another retest attempt.
- Record stage, class, retryability, user action, target URL, HTTP/browser
  status when available, safe message, and whether the failure consumed any
  secret/quota.

## Acceptance Criteria

| Criterion | Required evidence | Worker status if met |
| --- | --- | --- |
| Hosted UI reached | URL/timestamp/browser evidence | continue |
| Correct template/language/mode selected | review artifact step log | continue |
| Fresh export obtained | safe excerpt/heading evidence | continue |
| `Portable Agent Handoff Readiness` present | heading evidence | `HOSTED_FRESH_PASS` or `HOSTED_FRESH_PASS_WITH_MINOR_FIX` depending on evaluation |
| External-agent evaluation complete | verdict `PASS`, `PASS_WITH_MINOR_FIX`, or `HOLD` | `COMPLETE_PENDING_REVIEW` |
| Hosted export stale or missing section | absence evidence | `HOSTED_STALE_HOLD` |
| Hosted/browser unavailable | diagnostic | `BLOCKED_HOSTED_UNAVAILABLE` or `BLOCKED_BROWSER_OR_TOOLING` |

Fail conditions:

| Condition | Disposition |
| --- | --- |
| Claude edits runtime/source/public-sync files | BLOCKS_REVIEW |
| Claude claims production/public readiness | BLOCKS_REVIEW |
| Claude claims provider/live governance behavior from UI export review | BLOCKS_REVIEW |
| Claude omits live diagnostic after failed hosted/browser run | BLOCKS_REVIEW |
| Claude commits or pushes | BLOCKS_REVIEW |

## Review Gate

Worker handoff may proceed when:

- review artifact exists;
- component gates pass or failure is classified as outside worker scope;
- actual pending files are listed;
- status remains pending/blocked, not closed-equivalent.

Reviewer/committer closure may proceed only after:

- Codex/operator reviews Claude artifact;
- approved artifact is committed;
- committed-range pre-closure gate passes on a non-empty range;
- active handoff is synced after commit.

## Return Conditions

Return to Orchestrator without source edits if:

- the hosted URL is unreachable or blocked;
- the export cannot be generated/copied through available browser tooling;
- the hosted export is stale or lacks `Portable Agent Handoff Readiness`;
- the external-agent verdict is `HOLD`;
- any required diagnostic cannot be captured safely;
- completing the task would require runtime/source edits, public-sync, push,
  secrets/quota, hosted `/api/execute` proof, or provider/API calls.

## Operator Checkpoint

Operator checkpoint after Claude handoff:

- Codex/operator reviews the Claude review artifact.
- If the result is `HOSTED_FRESH_PASS` or
  `HOSTED_FRESH_PASS_WITH_MINOR_FIX`, operator may decide whether to accept
  VI5-T4 or request a small public-sync summary.
- If the result is `HOSTED_STALE_HOLD`, operator decides whether to deploy the
  latest public-sync/web build before another retest.

## Closure Checklist For Worker Handoff

| Item | Required worker disposition |
| --- | --- |
| Required first reads completed | PASS or BLOCKED with reason |
| executionBaseHead captured | PASS |
| Hosted/browser result recorded | PASS or BLOCKED with diagnostic |
| External-agent verdict recorded | PASS or N/A with reason |
| Allowed file scope preserved | PASS |
| Public/provenance boundary preserved | PASS |
| Component gates run | PASS or BLOCKED with reason |
| Worker did not commit | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_VI5_HR1_HOSTED_EXPORT_ACCEPTANCE_RETEST_FOR_CLAUDE_2026-06-04.md` | `DISPATCH_READY`; worker returns pending review, not closed-equivalent | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_VI5_HR1_HOSTED_EXPORT_ACCEPTANCE_RETEST_CLAUDE_REVIEW_2026-06-04.md` | final worker verdict and evidence; reviewer closure later | PASS |
| Roadmap state | `N/A with reason` | HR1 uses fresh GC-018 plus predecessor VI5 roadmap; no active roadmap state changed by dispatch | N/A with reason |
| Corpus scan registry JSON | `N/A with reason` | not corpus/search/classification work | N/A with reason |
| Corpus scan registry MD | `N/A with reason` | not corpus/search/classification work | N/A with reason |
| External evidence digest | review artifact `Evidence Trace Block` and `Hosted Retest Result` | hosted target, timestamp, verdict, safe excerpt, no secrets | PASS |
| System loop interlock | `N/A with reason` | no new runtime workflow chain or registry connection in HR1 dispatch | N/A with reason |
| Session continuity | `AGENT_HANDOFF_V15_2026-05-29.md` | reviewer-owned continuity sync after accepted worker artifact commit | PASS |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| VI5-T4/T5 remained parked after deterministic implementation | OPERATOR_SCOPE_CLARITY_GAP | DOCUMENTATION_ONLY_LEARNING | DESIGN_REVIEW_REQUIRED | Claude hosted retest work order |
| Hosted stale or unavailable result would indicate deployment freshness gap | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | RUNTIME_LEARNING_CANDIDATE | return diagnostic and decide deploy/retest tranche |
| Runtime/provider/cost learning lane | N/A_WITH_REASON | N/A_WITH_REASON | N/A_WITH_REASON | no provider/API/secret/quota work authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order dispatches a private hosted retest. It does not update
the public repository and does not authorize a public readiness claim.

Next action: reviewer/committer decides from Claude's returned verdict whether
a separate public-sync summary is warranted.

## Claim Boundary

This work order may produce a bounded hosted freshness and external-agent
readiness review for one Surface 1 export path only:
`app_builder_complete`, English, Full / CVF Guided Agent mode, from
`https://vibcode.netlify.app/home`. It does not prove live governance behavior,
hosted SaaS readiness, production readiness, public readiness, full template
portability, dependency security clearance, or external-agent build success.
