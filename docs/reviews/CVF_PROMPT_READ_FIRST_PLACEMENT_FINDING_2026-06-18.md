# CVF Prompt Read-First Placement Finding

Memory class: FULL_RECORD

Status: COMPLETE_WITH_GOVERNANCE_REMEDIATION

docType: review

Date: 2026-06-18

Owner: Codex

## Purpose

Record and remediate the prompt placement finding discovered during GFC-T1
dispatch review.

## Scope / Target / Owner Boundary

Target: dispatch prompt envelope placement enforcement for future delegated or
role-switching dispatch-ready work orders.

Owner boundary: this packet records the finding and the local governance
remediation. It does not reopen the already-dispatched GFC-T1 work order and
does not review Claude's pending worker return artifacts.

## Target / Source

| Item | Source |
|---|---|
| Operator finding | 2026-06-18 operator correction that prompt must be first for agent reading |
| Standard | `docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md` |
| Template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` |
| Checker | `governance/compat/check_dispatch_prompt_envelope.py` |
| Focused test | `governance/compat/test_check_dispatch_prompt_envelope.py` |

## Scope / Methodology

1. Compare the operator-intended rule with the standard and checker behavior.
2. Identify why the GFC-T1 work order passed the gate despite prompt-not-first
   placement.
3. Promote the rule from author memory to standard, template, checker, and
   focused test enforcement.
4. Leave the Claude worker-return files untouched for later review.

## Findings / Position

The dispatch prompt envelope rule was not enforced at the level intended by
the operator. A work order could place `## Purpose` before
`## Dispatch Prompt Envelope` and still pass the dispatch prompt checker as
long as the envelope appeared before line 80 and before Mission.

## Root Cause

The standard and checker encoded a weak placement rule:

- the envelope had to appear near the top;
- the envelope had to appear before Mission;
- the checker did not require the envelope to be the first `##` section;
- the checker did not reject `## Purpose` before the envelope;
- the canonical template taught authors to read Purpose before the placement
  rule.

This made the rule depend on author memory rather than a hard gate.

## Risk / Corrective Action

Risk: future agents can comply with the literal gate while still burying the
worker-readable prompt behind purpose prose or other sections.

Corrective action: harden the standard, canonical template, template folder
index, checker, and focused tests so the envelope must be the first `##`
section for delegated dispatch-ready work orders.

## Governance Remediation

The rule is promoted from guidance to machine enforcement:

- standard now requires the envelope to be the first `##` section, before
  `## Purpose`, and no later than line 25;
- template now states the placement rule before its own Purpose section and
  places the envelope first in the copyable skeleton;
- checker now fails delegated dispatch-ready work orders when any other `##`
  section precedes the envelope;
- focused tests cover the `Purpose before envelope` failure case.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update the dispatch prompt envelope checker
and its focused test to enforce the operator-confirmed read-first placement
rule.

Protected paths:

- `governance/compat/check_dispatch_prompt_envelope.py`
- `governance/compat/test_check_dispatch_prompt_envelope.py`

Operator authorization: 2026-06-18 operator directed Codex to handle the
finding before continuing Claude worker-return review.

Rollback boundary: revert only the prompt read-first standard/template/checker
hardening commit if rejected. Do not alter GFC-T1 worker-return files,
session-sync commits, or prior dispatch artifacts.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled in this batch? |
|---|---|---|---|---|---|
| Prompt envelope could pass while `## Purpose` preceded the worker prompt | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | Keep `check_dispatch_prompt_envelope.py` in dispatch author fast gate and local hook chain; future delegated dispatch-ready work orders fail if envelope is not the first `##` section | yes |

Generalizable finding promotion: MACHINE_CHECK_ADDED; STANDARD_UPDATED;
TEMPLATE_UPDATED.

Runtime/provider/cost learning lane: N/A_WITH_REASON. The defect is an
authoring-time governance/control-plane gap, not runtime behavior, provider
output, or cost evidence.

Reason: the defect is a repeated future-agent authoring risk. Guidance alone
is insufficient because the previous checker allowed the non-read-first
placement to pass.

Governed artifact updates:

- `docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/work_order_template/README.md`
- `governance/compat/check_dispatch_prompt_envelope.py`
- `governance/compat/test_check_dispatch_prompt_envelope.py`

Provider-local memory disposition: NOT_USED_AS_AUTHORITY. This finding is
recorded in CVF-governed artifacts.

## Evidence Trace Block

| Field | Evidence |
|---|---|
| Finding source | Operator review on 2026-06-18 after GFC-T1 dispatch |
| Affected standard | `docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md` |
| Affected template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` |
| Affected checker | `governance/compat/check_dispatch_prompt_envelope.py` |
| Test surface | `governance/compat/test_check_dispatch_prompt_envelope.py` |
| Governance disposition | PROMOTED_TO_MACHINE_CHECK |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-18 prompt read-first placement finding |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch |
| Target paths | prompt-envelope standard, work-order template, template README, checker, checker tests, finding review |
| Allowed scope source | operator instructed Codex to handle this finding before Claude worker-return review |
| Before status evidence | checker accepted envelope before line 80 even when Purpose preceded it |
| After status evidence | checker rejects Purpose-before-envelope placement |
| Diff evidence | `git diff --name-status`; focused test command |
| Approval boundary | governance rule/checker/template hardening only |
| Claim boundary | repo-local governance enforcement; no runtime/provider/live/public claim |
| Agent type | Codex |
| Invocation ID | prompt-read-first-placement-finding-2026-06-18 |
| Expected manifest | standard; template; template README; checker; checker tests; finding review |
| Actual changed set | `docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md`; `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; `docs/reference/work_order_template/README.md`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/test_check_dispatch_prompt_envelope.py`; `docs/reviews/CVF_PROMPT_READ_FIRST_PLACEMENT_FINDING_2026-06-18.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening. No public-sync batch is
authorized.

## Claim Boundary

This finding records and remediates an authoring-time governance gap. It does
not prove runtime agent behavior, hidden provider memory transfer, live
governance behavior, production readiness, public readiness, or public export.
