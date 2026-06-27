# CVF GC-018 - AAF-T2 Agent Automation Assist Early Gap Diagnostics

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-20

docType: baseline

dispatchBaseHead: 31b7ef35

Batch ID: AAF-T2

## Purpose

Authorize AAF-T2 as a bounded governance-tooling follow-up to AAF-T1. AAF-T1
proved useful but exposed one remaining latency source: a worker-return packet
can pass reviewer-fast and still fail a later full pre-commit/pre-closure gate
because a changed active Markdown artifact has an incomplete Corpus Completeness
And Report Integrity block. AAF-T2 moves that known late failure class into the
read-only helper's early local diagnostics and adds drift tests so helper
mirrors do not silently diverge from canonical machine gates.

## Operator Authorization

The operator approved continuing with AAF-T2 on 2026-06-20 after observing that
the AAF-T1 helper improved CVF workflow guidance but that additional automation
is needed to prevent repeat noncoder/external-agent latency loops.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-20 AAF-T2 selection | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| AAF-T1 closure | `docs/reviews/CVF_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_COMPLETION_2026-06-20.md` | ACCEPT |
| AAF-T1 helper | `governance/compat/run_agent_automation_assist.py` | ACCEPT |
| AAF-T1 focused tests | `governance/compat/test_run_agent_automation_assist.py` | ACCEPT |
| Corpus completeness checker | `governance/compat/check_corpus_completeness_report_integrity.py` | ACCEPT |
| Work-order dispatch-quality checker | `governance/compat/check_work_order_dispatch_quality.py` | ACCEPT |
| Worker-return fast gate | `governance/compat/run_worker_return_fast_gate.py` | ACCEPT |
| Commit steward protocol | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | ACCEPT |

## Scope / Owner Boundary

Allowed scope:

- modify the existing AAF helper under `governance/compat/run_agent_automation_assist.py`;
- modify the focused AAF helper tests under
  `governance/compat/test_run_agent_automation_assist.py`;
- create one AAF-T2 worker-return packet under `docs/reviews/`;
- add early read-only diagnostics for changed active Markdown artifacts that
  would fail the Corpus Completeness And Report Integrity output gate;
- add focused drift tests that compare the helper's worker-return packet-shape
  mirror to canonical constants in `check_work_order_dispatch_quality.py`;
- keep output concise for noncoder operators and structured for future
  external-agent CLI/MCP callers.

Forbidden scope:

- no new helper files, runtime source, product UI, MCP wiring, provider/live
  proof, dependency install, public-sync, CodeGraph install/init, queue, watcher,
  daemon, or background service;
- no automatic file edits, staging, committing, pushing, deleting, moving, or
  arbitrary shell execution by the helper;
- no direct IDE/shell/git/filesystem interception claim;
- no changes to canonical corpus checker behavior unless Codex issues a fresh
  work order;
- no readiness, public release, production, universal speed, or universal
  governed-coding-control claim.

Risk ceiling: R1 governance tooling, read-only assistance.

## Required Deliverables

Claude must return uncommitted `COMPLETE_PENDING_REVIEW` with exactly these
owned artifacts changed or created:

- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`
- `docs/reviews/CVF_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_WORKER_RETURN_2026-06-20.md`

No other files are authorized for the worker.

## Decision / Baseline / Proposed Tranche

Baseline decision: AAF-T2 is ready for Claude dispatch as a bounded helper
hardening tranche.

Proposed tranche: `AAF-T2 Agent Automation Assist Early Gap Diagnostics`.

Tranche owner split: Claude implements helper/test changes and the worker-return
artifact without committing. Codex reviews, repairs only within allowed scope if
needed, commits accepted material, and session-syncs if the current mode or next
allowed move changes.

Baseline evidence:

- Current HEAD is `31b7ef35`.
- AAF-T1 closed at material commit `3b26e23a` and session-sync commit
  `31b7ef35`.
- During AAF-T1 review, a worker-return packet passed reviewer-fast but the
  full pre-commit hook later caught missing Corpus Completeness fields.
- AAF-T1 helper already classifies dispatch and worker-return lanes, emits JSON,
  and fails `--enforce` on local helper-detectable defects.

## Source / Predecessor Evidence

| Source | Evidence | Disposition |
|---|---|---|
| AAF-T1 helper closure | `docs/reviews/CVF_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_COMPLETION_2026-06-20.md` | ACCEPT |
| AAF-T1 helper source | `governance/compat/run_agent_automation_assist.py` | ACCEPT |
| AAF-T1 tests | `governance/compat/test_run_agent_automation_assist.py` | ACCEPT |
| Corpus checker | `governance/compat/check_corpus_completeness_report_integrity.py` | ACCEPT |
| Dispatch-quality checker | `governance/compat/check_work_order_dispatch_quality.py` | ACCEPT |

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `31b7ef35`.
- `git status --short` was clean except the recurring Windows global git-ignore
  permission warning.
- Source verification used direct file reads and line anchors from the current
  workspace.

Required pre-dispatch verification before commit:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 31b7ef35 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 31b7ef35 --head HEAD --enforce
```

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason - this is a GC-018 dispatch baseline, not a
  corpus inventory, folder-tree scan, or extraction report.
- Corpus root: N/A with reason - no corpus root was authorized or enumerated.
- Snapshot time: 2026-06-20 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads and `rg -n` source
  lookups over named AAF-T2 authority files.
- Manifest artifact or inline manifest: Authority Chain and Source /
  Predecessor Evidence.
- Manifest hash: N/A with reason - no generated corpus manifest artifact was
  produced.
- Processing ledger artifact or inline ledger: inline in Evidence /
  Verification.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline; ledger_terminal=inline; exclusions=no-corpus-inventory-scope; unresolved=0.
- Unresolved files: 0
- Declared exclusions: full corpus inventory, folder-tree scan, extraction
  report, runtime/provider proof, public-sync.
- Unreadable or unsupported files: none.
- Aggregation check: N/A with reason - no corpus aggregate was produced.
- Drift check: N/A with reason - no corpus aggregate was produced.
- Output traceability: baseline source evidence cites current repo authority
  files and the AAF-T2 work order carries detailed line anchors.
- Adversarial verification: claim rejects any full-corpus, complete-inventory,
  full-hook equivalence, runtime, or public readiness assertion.
- Corpus verdict: PARTIAL

## Required Helper Behavior

The AAF-T2 helper update must:

- remain read-only by design and by implementation;
- keep the existing AAF-T1 CLI: `--base`, `--head`,
  `--mode auto|dispatch|implementation|reviewer-return|closure|session-sync|handoff-sync`,
  `--json`, and `--enforce`;
- preserve AAF-T1 lane recommendation behavior, including worker-return
  detection for changed review packets;
- inspect changed active Markdown artifacts under the same applicable path
  boundary used by the Corpus Completeness checker;
- report early local defects for missing or malformed
  `## Corpus Completeness And Report Integrity` blocks by reusing existing
  checker logic where practical;
- include the early corpus diagnostics in human output and JSON output;
- make `--enforce` return non-zero when the helper detects such corpus-shape
  defects;
- add tests for missing corpus section/fields, unsafe enumeration or missing
  reconciliation markers when applicable, clean N/A-with-reason corpus block,
  and JSON shape;
- add a drift test proving the helper's worker-return packet-shape mirror still
  matches the canonical constants in `check_work_order_dispatch_quality.py`.

## Claim Boundary

AAF-T2 may claim only earlier local detection for a known class of governance
packet shape defects and helper mirror drift coverage. It must not claim full
pre-commit/pre-closure equivalence, automatic governance decisioning, runtime
control, provider control, MCP execution, public sync readiness, direct
interception, production readiness, or universal latency elimination.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | `governance/compat/run_agent_automation_assist.py` |
| Disposition | ADAPT as CVF-owned governance helper hardening |
| Claim boundary | existing CVF helpers and standards remain source authority; no third-party code or claim is absorbed |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T2 read-only governance automation helper diagnostics only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | cooperating local user invokes the helper manually |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | early gap diagnostics helper, not execution-control enforcement |
| forbiddenExpansion | wrapper/proxy enforcement, direct interception, arbitrary commands, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, readiness, and universal control remain parked |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: AAF-T2 is private provenance governance tooling. Public export requires
separate public-sync authorization and a bounded public-facing summary if the
operator requests it later.
