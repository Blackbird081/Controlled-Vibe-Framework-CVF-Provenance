# CVF GC-018 Agent Operation Trace Foundation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018_baseline

Date: 2026-06-13

Owner: Codex

rawMemoryReleased=false

## Purpose

Authorize a bounded governance-control batch that turns the FPC-T3-C07
workspace-integrity design into a repo-local agent operation trace standard
and machine gate.

The batch responds to the operator's clarified direction: CVF does not develop
`codex_cowork` or `claude_cowork`; CVF supervises agent/provider work by
requiring enough trace evidence for review, scope validation, rollback, and
bounded repo-local attribution.

## Scope / Target / Owner Boundary

Allowed scope:

- create the canonical Agent Operation Trace and Workspace Integrity standard;
- update the work-order template with the required trace block;
- add a deterministic repo-local trace checker and focused tests;
- wire the checker into reviewer-fast, pre-commit, pre-push, and autorun common
  phase gates;
- create this GC-018, work order, and completion packet.

Forbidden scope:

- OS audit setup, Windows audit policy, Sysmon, EDR, file watcher services, or
  endpoint telemetry;
- destructive broker design;
- agent computer-control permission changes;
- provider platform feature development;
- external Document Translator or Policy_Local inspection/mutation;
- runtime/source behavior change outside governance checkers;
- public-sync;
- live provider/OCR proof;
- production, public, readiness, cost, or quality claims.

## Source Authority

| Source | Path | Role |
| --- | --- | --- |
| Operator instruction | current session | authorizes CVF traceability foundation, not co_work development |
| FPC-T3 coverage plan | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | C07 repo-local workspace-integrity design and OS-level boundary |
| FPC-T3 completion | `docs/reviews/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_COMPLETION_2026-06-13.md` | accepts C07 as design-only and requires separate work order for repo-local implementation |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | canonical agent execution packet surface |
| Autorun workflow control | `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | phase-gate owner standard |
| Hook chain | `governance/compat/run_local_governance_hook_chain.py` | local reviewer-fast/pre-commit/pre-push execution surface |
| Autorun wrapper | `governance/compat/run_agent_autorun_workflow_gate.py` | phase gate execution surface |

## Decision / Baseline / Proposed Tranche

Decision: authorize AOT-T1 as a bounded same-session governance-control
hardening tranche.

Baseline: before this batch, work orders required changed-file and evidence
records, but no canonical Agent Operation Trace Block existed and no dedicated
checker required trace evidence on changed execution artifacts.

Proposed tranche: add the standard, template section, checker, focused tests,
and hook/autorun placement described in this packet.

## Design Control Gate

Accepted design:

- implement repo-local trace and changed-path evidence only;
- require trace blocks in changed work orders, worker returns, and completion
  reviews;
- detect protected governed path deletion or rename in changed ranges;
- state that OS/user attribution is outside the repo-local claim boundary.

Rejected design:

- build co_work capability inside CVF;
- configure OS audit or endpoint monitoring in this tranche;
- claim identity attribution from git diff evidence;
- retroactively rewrite all historical packets.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex |
| Provider or surface | Codex CLI in the private provenance repo |
| Session or invocation | current session; base HEAD `f789498d` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `apply_patch`, `python -m unittest`, governance hook commands |
| Target paths | standard, template, checker, tests, hook chain, autorun wrapper, GC-018/work-order/completion |
| Allowed scope source | operator instruction plus FPC-T3-C07 closure boundary |
| Before status evidence | `git status --short` clean before edits |
| After status evidence | recorded in completion review and final `git status --short` |
| Diff evidence | `git diff --name-status` and committed-range pre-closure |
| Approval boundary | operator said "Chinh xac, tien hanh di" after trace-foundation recommendation |
| Claim boundary | repo-local trace/integrity evidence only; no OS/user attribution |
| Deletion or rename disposition | N/A with reason: no protected deletion or rename is authorized |

## Evidence / Verification

Required verification for closure:

- focused unittest for the new checker;
- direct checker run over the AOT-T1 changed range;
- reviewer-fast;
- pre-commit;
- committed-range pre-closure after material commit.

## Acceptance Criteria

| Criterion | Status |
| --- | --- |
| Standard exists and separates CVF control-plane trace from co_work platform development | PASS |
| Work-order template includes Agent Operation Trace Block | PASS |
| Checker enforces trace blocks on changed work orders/reviews and protected delete/rename disposition | PASS |
| Focused unit tests cover missing trace, valid trace, non-execution review exemption, and protected deletion/rename handling | PASS |
| Hook chain and autorun wrapper include the new checker | PASS |
| Claim boundary excludes OS-level attribution and endpoint monitoring | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-control hardening. Public-sync is not
authorized.

## Claim Boundary

This GC-018 authorizes repo-local governance trace hardening only. It does not
prove OS-level user attribution, endpoint telemetry, provider-internal logs,
co_work platform behavior, runtime governance behavior, public readiness, or
production readiness.

rawMemoryReleased=false
