# CVF Guard Orientation Index

Memory class: POINTER_RECORD

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-06-20

**Applies to:** all roles before material governed CVF work.

EPISTEMIC_PROCESS_NA_WITH_REASON: orientation index - no evidence claims or source-backed assertions are made or updated by this document.

## Purpose

Provide a task-first guard map that any new or resumed role can read before
authoring governed CVF artifacts. This index names which guard surfaces to read,
what blocks or outputs are required, what failure patterns to avoid, and which
fast command applies for each common task class.

This is an orientation layer only. Canonical standards, work orders, machine
checkers, and current session state still control. This index does not change
checker semantics, runtime behavior, provider behavior, or public-sync state.

## Read This First

1. Complete the startup acknowledgment from `AGENTS.md` (current mode, active
   handoff, next allowed move, parked checkpoint) before any material governed
   work.
2. Confirm `git rev-parse --short HEAD` and `git status --short`. Record both
   in any worker return or closure packet.
3. Identify the active work order or task class.
4. Look up the task class row in the Task Class Guard Map below.
5. Read the guard surfaces named in the "Read first" column before editing.

## Role-Neutrality Rule

Normative instructions in CVF governed artifacts must name roles and required
work, not a specific agent, provider, or model.

Allowed role terms:

- operator, dispatcher, dispatch author
- worker
- reviewer, closer, reviewer/closer
- session-sync steward
- external reviewer

Forbidden normative patterns:

- naming a specific provider, model, or agent as the required worker;
- citing a provider-specific memory file as CVF source authority;
- binding future work to one provider surface when the route is role-based.

## Role Glossary

| Role | Responsibility |
|---|---|
| Operator | Authorizes scope, approves checkpoints, owns configuration keys. |
| Dispatcher / dispatch author | Authors GC-018 baseline and work order; runs pre-dispatch gate. |
| Worker | Executes work order; returns `COMPLETE_PENDING_REVIEW`; must not commit. |
| Reviewer | Reviews worker return; may repair allowed-scope defects; closes if accepted. |
| Closer | Commits closure artifacts; updates session-sync surfaces. |
| Reviewer/closer | Combined reviewer and closer in single-role tranches. |
| Session-sync steward | Updates active handoff, session state, and next-move after closure. |
| External reviewer | Reviews CVF from outside the repository; absorbed as input, not authority. |

## Task Class Guard Map

| Task class | Active role | Read first | Required blocks or outputs | Common failure to avoid | Fast command or gate | Boundary |
|---|---|---|---|---|---|---|
| Startup / resume | Any | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; active handoff named by registry | Startup acknowledgment (mode, handoff, next-move, parked checkpoint) | Skipping acknowledgment; appending status to archived handoffs | `git rev-parse --short HEAD; git status --short` | Session memory and active handoff are the only sources of truth; provider memory files are not CVF authority |
| Work-order authoring / dispatch | Dispatcher | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`; `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md`; `AGENTS.md` Mandatory Work Order Source Verification section | Source Verification Block (ACCEPT/REJECT/BLOCKED_SOURCE_NOT_FOUND per item); Agent Handoff Contract Control Block; Dual Agent Surface Matrix with `INTERNAL_AGENT`, `EXTERNAL_AGENT_CLI_MCP`, and adapter boundary; Reviewer Closure Conversion; Commit Prompt Readiness | ACCEPT row cites no source file; work order dispatched without pre-dispatch gate; internal-only design omits external-agent disposition | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch` | Source facts require file and line/section before dispatch; doc-only fields must be separated from source facts; external CLI/MCP support requires separate source-verified authorization |
| Worker execution (`WORKER_MUST_NOT_COMMIT`) | Worker | This index; governing GC-018 baseline; the work order; source files named in Source Verification Block | Worker-return packet: Purpose, Scope / Methodology, Findings / Position, Risk / Corrective Action, Claim Boundary, Agent Operation Trace Block, Delta Execution Claim Boundary Control Block, Public Export Disposition, executionBaseHead, git status; N/A-with-reason for conditional sections (External Knowledge Intake Routing, Rescan Intelligence Hardening, Corpus Completeness And Report Integrity, Finding-To-Governance Learning Disposition, Epistemic Process Block, Machine Closure Package) | Committing before reviewer accepts; missing required packet shape sections; recording git status as clean when the worker-return file is untracked; ACCEPT rows using bare filename instead of full repo path | `python governance/compat/run_agent_automation_assist.py --base <base> --head HEAD --json --enforce`; `python governance/compat/run_worker_return_fast_gate.py` | Worker must not commit; all artifacts remain uncommitted until reviewer accepts |
| Reviewer-return review | Reviewer | Work order; worker-return packet; GC-018 baseline; `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Completion review (Target or Reviewed source, Scope / Methodology, Findings / Position, Risk / Corrective Action, decision/disposition); Dual Agent Surface Matrix if the reviewed artifact is agent-facing; reviewer-fast governance gate pass | Accepting a packet without running reviewer-fast gate; committing without verifying all required deliverables; treating internal helper evidence as external CLI/MCP support | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | Reviewer may repair only allowed-scope defects; scope expansion returns to operator; external-agent disposition must stay explicit |
| Closure | Closer | Completion review; active session state; `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`; `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Committed closure artifacts; Dual Agent Surface Matrix preserved for applicable roadmap/work-order/closure surfaces; session-sync surfaces updated if mode or next allowed move changes | Mixing closure commits with worker changes; updating generated state source files without a separate state-generator run; closing with no external-agent disposition or no adapter boundary | `python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <closureBase> --head HEAD --enforce` | Closer commits only reviewer-owned and closure-owned paths; closure does not convert `CONTRACT_ONLY` or deferred adapter rows into runtime support |
| Session-sync | Session-sync steward | Active handoff; `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Updated handoff, session state, and next-move surfaces; no change to archived handoffs | Appending new status to superseded handoffs; updating generated state without running the generator | `python governance/compat/generate_active_session_state.py` | Only the active handoff named by the registry receives new status |
| Push-readiness preview | Reviewer / closer / session-sync steward | `docs/reference/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARD_2026-06-27.md`; `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | Read-only preview readout before full pre-push gate; commit-shape split recommendation; final base/head range recorded | Discovering GC-020, front-door marker, active-window, review-retention, repository-lifecycle, pre-public P3, or knowledge-absorption marker defects one full pre-push rerun at a time | `python governance/compat/run_agent_push_readiness_preview.py --base <baseHead> --head HEAD --enforce` | Preview is diagnostic only; canonical pre-push autorun gate remains required before push |
| ADIF entry authoring | Worker / reviewer / closer | `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md`; `governance/compat/check_adif_entry_integrity.py`; this index | Entry field block; Canonical Sources; Remediation; complete Agent Operation Trace Block with `Diff evidence`; Public Export Disposition; Claim Boundary | Copying the template without all trace labels; adding an entry to record an entry-authoring error without a recurrence/latency threshold; mixing ADIF material entries with active handoff/session-sync paths | `python governance/compat/check_adif_entry_integrity.py --enforce` | ADIF entries are material learning records; session-sync surfaces must be committed separately by the session-sync steward |
| External knowledge absorption | Worker / dispatch author | `docs/reference/external_agent_review/README.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | External Knowledge Intake Routing table (chain map, input type, route, local guard, disposition, claim boundary); absorb / adapt / defer / reject classification per item | Treating external input as CVF authority without source verification; absorbing without classification | Classify each external item before authoring a CVF-owned reference | CVF remains source of truth; external material is reference input only |
| Public-sync | Session-sync steward / operator | `AGENTS.md` critical repository boundary section; `git remote -v` output | Confirmed `origin` points to public-sync clone, not provenance repository | Pushing provenance tree to the public repository; running public push from the provenance clone | `git remote -v` (confirm remote before push) | Never push provenance archive to the public repository; public-sync requires separate authorization |
| Runtime / provider / live proof | Dispatcher and operator checkpoint | `AGENTS.md` Mandatory Live Governance Proof section; governing GC-018 baseline authorizing live proof | Live governance proof command output with stage, class, retryability, HTTP status; API key loaded from `.env.local`; pass/fail evidence | Claiming live proof from mock mode; repeating unclear tests without a failure diagnostic; counting event ratios as execution pass rate | `python scripts/run_cvf_release_gate_bundle.py --json` | Live proof requires a real API call; mock mode is for UI-only structure checks only |
| Guard / checker maintenance | Worker | `governance/toolkit/05_OPERATION/CVF_GUARD_REGISTRY_GUARD.md`; `AGENTS.md`; this index | Core Guard Self-Protection Authorization block in the changed doc set listing every protected path, authorized scope, operator authorization, and rollback boundary | Editing `governance/compat/*.py` or `AGENTS.md` without an authorization block that lists every protected path | `python governance/compat/check_core_guard_self_protection.py` | Each protected path must be listed explicitly in the authorization block |
| Project role / provider-lane delegation setup | Operator and dispatch author | `docs/reference/project_role_provider_delegation/README.md`; `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md`; `docs/reference/CVF_AGENT_DELEGATION_AND_SUBAGENT_BOUNDARY_STANDARD_2026-05-19.md` | Operator-approved project profile: role lanes, allowed/forbidden tools, provider lane, cost/quota ceiling, evidence log, reapproval triggers | Letting an agent self-select a provider lane or self-widen scope; treating the public provider-routing guide as CVF source authority | review the delegation envelope before assigning roles | Documentation/reference envelope only; not an automated provider selector or runtime router; provider/live, runtime routing, and public-sync need fresh GC-018 |

## Common Failure Patterns

| Failure | Gate that catches it | Prevention |
|---|---|---|
| Worker commits before reviewer accepts | Core guard self-protection; tranche commit choreography | Check commit mode in work order; always use `WORKER_MUST_NOT_COMMIT` |
| Source Verification ACCEPT row uses bare filename, not full repo path | `check_work_order_dispatch_quality.py` | Use path starting from repo root (e.g., `governance/compat/foo.py`) |
| Worker-return records `git status --short` as clean when the packet itself is untracked | `check_work_order_dispatch_quality.py` | Record actual pending paths in the git status field at COMPLETE_PENDING_REVIEW |
| Rescan Intelligence Hardening section overbuilt for true non-rescan packets | `check_rescan_intelligence_hardening.py` | Use compact `NOT_APPLICABLE_WITH_REASON` plus a concrete reason for non-rescan worker-return/report packets; include the full delta / routing / sampling vocabulary only for real rescan or intake-refresh outputs |
| Evidence-heavy packet missing Epistemic Process required fields | `check_epistemic_process_packet.py` | Include Evidence Comparison (capital C on Comparison), Contradiction or Gap Disposition, and Claim Update; use EPISTEMIC_PROCESS_NA_WITH_REASON when truly not applicable |
| Corpus Completeness enumeration command is unsafe | `check_corpus_completeness_report_integrity.py` | Use `filesystem-backed direct file reads` or a fully qualified safe enumeration command; bare `rg --files` without `--hidden --no-ignore` is rejected |
| AGENTS.md or governance/compat files changed without authorization | `check_core_guard_self_protection.py` | Include Core Guard Self-Protection Authorization block in a docs/reviews/, docs/work_orders/, or AGENT_HANDOFF*.md file in the same changed set |
| Provider-specific memory file cited as CVF source authority | `check_work_order_dispatch_quality.py`; manual review | Use only CVF-governed surfaces; re-verify against runtime source before promoting any claim |
| INDEX artifact missing required metadata block | `governance/compat/check_index_classification.py` | Any artifact that declares `INDEX type:` must also include all seven required fields: `INDEX type:`, `Source authority:`, `Status:`, `Date:`, `Human-reviewable:`, `Claim boundary:`, `Public Export Disposition:` |
| Roadmap, work order, or closure omits external-agent disposition | machine-check candidate in `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Include a six-column Dual Agent Surface Matrix with `INTERNAL_AGENT`, `EXTERNAL_AGENT_CLI_MCP`, interface, authority/risk boundary, evidence, adapter boundary, and allowed disposition |
| ADIF entry trace table omits `Diff evidence` or another exact label | `check_adif_entry_integrity.py` | Copy the trace block from `CVF_ADIF_ENTRY_TEMPLATE.md`; run the ADIF integrity guard before commit |
| ADIF material entry is committed with active handoff/session state | commit steward preflight | Split into material entry commit first, then a dedicated session-sync or handoff-sync commit |
| Push readiness relies only on the full late pre-push gate | push-readiness preview helper; pre-push autorun gate | Run `python governance/compat/run_agent_push_readiness_preview.py --base <baseHead> --head HEAD --enforce` before the full pre-push gate, repair local marker/continuity findings first, and split material from protected session/handoff paths |

## Claim Boundary

This index is an orientation layer only. It does not claim enforcement authority,
replace canonical guards or standards, change checker semantics, authorize
runtime execution, prove live provider behavior, claim public-sync readiness,
or claim universal governed-coding control.

Canonical standards, work orders, machine checkers, and current session state
still control.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T3 guard-orientation index - documentation and routing only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made by this index |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | cooperating local role reads this index manually |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | orientation index and navigation layer only |
| forbiddenExpansion | enforcement wrapper, proxy enforcement, interception, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness claims, full-hook equivalence, and universal control remain out of scope |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer role |
| Provider or surface | local workspace |
| Session or invocation | push-readiness preview standardization, 2026-06-27 |
| Working directory | repository root |
| Command or tool surface | apply_patch, focused pytest, preview helper, governance gates |
| Target paths | `docs/reference/guard_orientation/README.md`; `docs/reference/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARD_2026-06-27.md`; `governance/compat/run_agent_push_readiness_preview.py`; `governance/compat/test_run_agent_push_readiness_preview.py`; `docs/reviews/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARDIZATION_COMPLETION_2026-06-27.md`; `governance/compat/CVF_REVIEW_RETENTION_REGISTRY.json` |
| Allowed scope source | operator instruction to standardize prevention of provenance pre-push cascade before returning to FPC-SCG next move |
| Before status evidence | baseHead `3e4b7266`; worktree clean before patch |
| After status evidence | push-readiness preview row and common-failure prevention note added |
| Diff evidence | `git diff --name-status 3e4b7266..HEAD` after material commit |
| Approval boundary | push-readiness preview standardization only |
| Claim boundary | orientation layer plus read-only preview routing; no runtime, provider/live, external adapter, public-sync, package instance, certification, push authorization, MPI-T6 work, or FPC implementation claim |
| Agent type | reviewer/closer |
| Invocation ID | `agent-push-readiness-preview-standardization-2026-06-27` |
| Expected manifest | `docs/reference/guard_orientation/README.md`; `docs/reference/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARD_2026-06-27.md`; `governance/compat/run_agent_push_readiness_preview.py`; `governance/compat/test_run_agent_push_readiness_preview.py`; `docs/reviews/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARDIZATION_COMPLETION_2026-06-27.md`; `governance/compat/CVF_REVIEW_RETENTION_REGISTRY.json` |
| Actual changed set | `docs/reference/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARD_2026-06-27.md`; `docs/reference/guard_orientation/README.md`; `docs/reviews/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARDIZATION_COMPLETION_2026-06-27.md`; `governance/compat/CVF_REVIEW_RETENTION_REGISTRY.json`; `governance/compat/run_agent_push_readiness_preview.py`; `governance/compat/test_run_agent_push_readiness_preview.py` |
| Manifest delta | MATCH |

## Related Surfaces

- `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md` - startup guard router
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` - task-trigger lookup table
- `AGENTS.md` - root agent instructions and mandatory acknowledgment
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` - work order template
- `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` - commit choreography
- `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` - internal/external agent surface accounting and matrix checker candidate
- `governance/compat/run_agent_automation_assist.py` - AAF helper smoke command
- `governance/compat/run_worker_return_fast_gate.py` - worker-return fast gate
- `governance/compat/run_agent_autorun_workflow_gate.py` - pre-dispatch gate
- `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` - external knowledge intake routing
- `governance/compat/check_index_classification.py` - INDEX classification gate (INDEX-T1)
- `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` - accepted forward-only INDEX classification standard
