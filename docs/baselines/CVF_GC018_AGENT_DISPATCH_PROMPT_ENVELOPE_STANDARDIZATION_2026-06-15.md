# GC-018 Agent Dispatch Prompt Envelope Standardization

Memory class: FULL_RECORD

rawMemoryReleased: false

Baseline ID: GC018-AGENT-DISPATCH-PROMPT-ENVELOPE-STANDARDIZATION-2026-06-15

Date: 2026-06-15

Status: AUTHORIZED_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION

dispatchBaseHead: 4895bca3

## Purpose

Authorize a bounded CVF foundation tranche that standardizes dispatch prompt
envelopes for multi-agent and single-agent multi-role work transfer.

## Decision

Proceed with T1 documentation plus machine-check foundation:

- canonical standard;
- work-order template pointer/update;
- dispatch prompt envelope checker and tests;
- fast-gate wiring;
- completion review.

## Source / Predecessor Evidence

P4B-B T2 demonstrated that a short prompt envelope is useful when the work
order is canonical but the handoff has current-time facts: role assignment,
commit mode, live-key authorization, negative-sample caveat, gate sequence, and
return contract.

Existing CVF control surfaces already support related pieces:

- work-order template includes Single-Agent Multi-Role Control Block;
- work-order template includes Worker Autonomy / No-Question Rule;
- work-order template includes Reviewer Closure Conversion guidance;
- dispatch author fast gate already runs four authoring checks;
- Agent Operation Trace checker enforces exact-manifest trace blocks;
- commit steward standard separates material and session-sync commits.

The missing piece is a standardized prompt envelope contract and an early gate
that tells orchestrators whether a dispatch-ready packet includes the runtime
cover note or explains why it is not applicable.

## Authorized Scope

Claude may create or modify:

- `docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md`;
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`;
- `governance/compat/check_dispatch_prompt_envelope.py`;
- `governance/compat/test_check_dispatch_prompt_envelope.py`;
- `governance/compat/run_dispatch_packet_author_fast_gate.py`;
- `docs/reviews/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_COMPLETION_2026-06-15.md`.

## Not Authorized

- Runtime/provider behavior;
- live API calls or credential use;
- public-sync;
- co-work product development;
- new provider/model routing;
- source edits outside the authorized paths;
- claims that prompts override work orders or governed standards;
- production readiness or public readiness claims.

## Guard Requirements

The checker must be bounded and authoring-time only. It should require a
dispatch-ready work order to include either:

- `## Dispatch Prompt Envelope` with role assignment, canonical packet,
  current-time overrides, do-not-misread notes, required first actions, and
  return contract; or
- explicit `N/A with reason` when no agent delegation/runtime prompt will be
issued.

## Evidence / Verification

Claude must return focused test output for the new checker, dispatch author
fast gate output, diff hygiene, and a completion review proving no runtime,
provider, live, public-sync, or production-readiness scope was touched.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-15 dispatch prompt envelope authorization |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | apply_patch, source inspection, governance gates |
| Target paths | roadmap, this GC-018, Claude work order |
| Allowed scope source | operator requested CVF foundation standardization for dispatch prompts |
| Before status evidence | P4B-B T2 closed; session-sync commit `4895bca3` |
| After status evidence | Claude implementation packet authorized |
| Diff evidence | dispatch authoring range from `4895bca3` |
| Approval boundary | authoring-time prompt envelope standardization only |
| Claim boundary | no runtime/provider/public/production claim |
| Agent type | Codex orchestrator |
| Invocation ID | `gc018-dispatch-prompt-envelope-2026-06-15` |
| Expected manifest | `docs/roadmaps/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_ROADMAP_2026-06-15.md`; `docs/baselines/CVF_GC018_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_FOR_CLAUDE_2026-06-15.md` |
| Actual changed set | `docs/roadmaps/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_ROADMAP_2026-06-15.md`; `docs/baselines/CVF_GC018_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_FOR_CLAUDE_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance baseline. No public-sync batch is
authorized.

## Claim Boundary

This baseline authorizes one bounded control-plane standardization tranche. It
does not authorize runtime behavior, provider calls, public-sync, co-work
product development, production readiness, or public readiness.
