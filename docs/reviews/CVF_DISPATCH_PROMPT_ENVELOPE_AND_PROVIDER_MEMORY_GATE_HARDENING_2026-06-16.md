# CVF Dispatch Prompt Envelope And Provider Memory Gate Hardening

Memory class: POINTER_RECORD

Status: PASS_BOUNDED

Date: 2026-06-16

Owner: Codex

rawMemoryReleased: false

## Purpose

Close two small governance-foundation gaps found during RSF-T3 dispatch review:
dispatch prompt envelopes were standardized but not wired into the mandatory
dispatch path, and provider-memory-only learning escape detection did not cover
work-order authoring packets.

## Scope / Target / Owner Boundary

Target: mandatory authoring checks for delegated work orders and reusable
lessons.

Owner boundary: this batch changes only governance compatibility check wiring,
one focused checker scope, tests, and the current RSF-T3 work order prompt
placement. It does not authorize runtime, provider, public-sync, live proof,
legacy scan, Model Gateway implementation, or session-state mutation.

## Target / Source

- Prompt envelope standard:
  `docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md`
- Prompt envelope checker:
  `governance/compat/check_dispatch_prompt_envelope.py`
- FPRC-T1 standard:
  `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`
- FPRC-T1 checker:
  `governance/compat/check_finding_to_governance_learning.py`
- Current regression sample:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_FOR_CLAUDE_2026-06-16.md`

## Scope / Methodology

Codex compared the RSF-T3 work order against the prompt-envelope standard,
ran the prompt-envelope checker directly on the material dispatch range, and
confirmed the checker failed while mandatory pre-dispatch and steward lanes had
previously passed. Codex then wired the checker into the mandatory lanes and
extended the FPRC-T1 provider-memory escape guard to work-order authoring.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: wire the existing dispatch prompt envelope
checker into mandatory dispatch authoring paths, extend the existing
finding-to-governance checker to catch provider-memory-only learning escape in
work orders, add focused tests, and repair the current RSF-T3 work order prompt
envelope as the regression sample.

Protected paths:

- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/check_finding_to_governance_learning.py`
- `governance/compat/test_check_finding_to_governance_learning.py`

Operator authorization: operator directed Codex on 2026-06-16 to elevate the
finding as CVF foundation hardening so all agents comply when creating work
orders, and specifically cited the rule that lessons must not remain only in
provider-specific memory.

Rollback boundary: revert only this hardening batch if rejected. Do not revert
RSF-T3 dispatch `8450707a`, RSF-T3 session sync `32689562`, CCLV-T2 material
commit `bf938549`, or FPRC-T1 material commit `51f56133`.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Prompt envelope must be read-first before Mission and line 80 | `docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md` | `## Envelope Placement` | `Dispatch Prompt Envelope` | prompt envelope standard | ACCEPT |
| Prompt envelope checker exists and enforces placement/fields | `governance/compat/check_dispatch_prompt_envelope.py` | `READ_FIRST_MAX_LINE`; `_check_read_first_placement`; `REQUIRED_FIELDS` | `check_work_order` | dispatch prompt envelope checker | ACCEPT |
| Dispatch author fast gate already includes prompt-envelope checker | `governance/compat/run_dispatch_packet_author_fast_gate.py` | `GATE_COMMANDS` | `GATE_COMMANDS` | dispatch packet author fast gate | ACCEPT |
| Mandatory autorun pre-dispatch now includes prompt-envelope checker | `governance/compat/run_agent_autorun_workflow_gate.py` | `_common_commands` | `_common_commands` | autorun workflow gate | ACCEPT |
| Local reviewer-fast hook now includes prompt-envelope checker | `governance/compat/run_local_governance_hook_chain.py` | `REVIEWER_FAST_CHECKS` | `REVIEWER_FAST_CHECKS` | local governance hook chain | ACCEPT |
| Local pre-commit hook now includes prompt-envelope checker | `governance/compat/run_local_governance_hook_chain.py` | `HOOK_CHAINS` | `HOOK_CHAINS` | local governance hook chain | ACCEPT |
| FPRC-T1 provider-memory escape signals exist | `governance/compat/check_finding_to_governance_learning.py` | `PROVIDER_MEMORY_ONLY_SIGNALS` | `PROVIDER_MEMORY_ONLY_SIGNALS` | finding-to-governance checker | ACCEPT |
| FPRC-T1 rule says provider memory is not CVF-governed authority | `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md` | provider-memory learning escape section | `Provider Memory Learning Escape Guard` | FPRC-T1 standard | ACCEPT |

## Findings / Position

| ID | Finding | Evidence | Disposition |
|---|---|---|---|
| DPE-001 | Prompt-envelope standard and checker existed, but mandatory pre-dispatch/steward lanes did not run the checker. | Direct checker failed RSF-T3 work order; prior pre-dispatch/steward passed. | `PHASE_GATE_PLACEMENT_GAP` |
| DPE-002 | RSF-T3 work order carried a prose worker prompt at the bottom rather than a read-first structured envelope. | Checker reported line 476, after Mission, missing required fields. | `TEMPLATE_APPLICATION_GAP` |
| B6-001 | Provider-memory learning escape guard covered finding-bearing review/audit paths but not work-order authoring packets. | Existing checker scoped finding docs; operator cited Claude memory-only lessons. | `MACHINE_GATE_GAP` |

## Risk / Corrective Action

Risk: without this hardening, a future agent could create a malformed delegated
work order or park reusable lessons in provider memory while mandatory gates
still report pass.

- Add `check_dispatch_prompt_envelope.py` to
  `run_agent_autorun_workflow_gate.py` so pre-dispatch/steward dispatch fails
  before a malformed delegated work order is committed.
- Add the same checker to reviewer-fast and pre-commit local hook chains for
  immediate authoring feedback.
- Extend `check_finding_to_governance_learning.py` so provider-memory-only
  learning escape signals are checked in `docs/work_orders/` as well as
  finding-bearing review/audit/log/assessment artifacts.
- Add focused tests for work-order provider-memory escape coverage.
- Move the current RSF-T3 work order prompt envelope to the top and use the
  standard required fields.

## Verification

Required commands:

- `python -m pytest governance/compat/test_check_dispatch_prompt_envelope.py governance/compat/test_check_finding_to_governance_learning.py`
- `python governance/compat/check_dispatch_prompt_envelope.py --base 32689562 --head HEAD --enforce`
- `python governance/compat/check_finding_to_governance_learning.py --base 32689562 --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 32689562 --head HEAD`
- `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base 32689562 --head HEAD --enforce`

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `PHASE_GATE_PLACEMENT_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `MACHINE_CHECK_ADDED` |
| Next control action | Mandatory pre-dispatch/steward/hook path now runs dispatch prompt envelope checker; provider-memory-only learning escape now covers work orders |
| Worker blame | `N/A_WITH_REASON`: standards and checkers existed, but mandatory phase placement and work-order scope coverage were incomplete |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex governance hardening |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 dispatch prompt and provider-memory gate hardening |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | rg, pytest, governance gates, apply_patch |
| Target paths | prompt-envelope gate wiring, finding-to-governance checker/test, RSF-T3 work order, this review |
| Allowed scope source | operator request on 2026-06-16 to harden CVF foundation rather than only fix one work order |
| Before status evidence | clean worktree at `32689562` |
| After status evidence | pending material hardening commit |
| Diff evidence | `git diff --name-status` on `32689562..HEAD` |
| Approval boundary | governance compatibility checker/wiring and current packet correction only |
| Claim boundary | no runtime/provider/public/live/legacy/session-state claim |
| Agent type | Codex orchestrator/implementer |
| Invocation ID | `dispatch-prompt-provider-memory-gate-hardening-2026-06-16` |
| Expected manifest | `docs/reviews/CVF_DISPATCH_PROMPT_ENVELOPE_AND_PROVIDER_MEMORY_GATE_HARDENING_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_FOR_CLAUDE_2026-06-16.md`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/test_check_finding_to_governance_learning.py` |
| Actual changed set | `docs/reviews/CVF_DISPATCH_PROMPT_ENVELOPE_AND_PROVIDER_MEMORY_GATE_HARDENING_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_FOR_CLAUDE_2026-06-16.md`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/test_check_finding_to_governance_learning.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening. No public-sync batch is
authorized.
