# CVF Unabsorbed Knowledge Reporting Correction Roadmap - 2026-05-17

Memory class: ROADMAP

Status: proposed - not authorized for absorption.

## Purpose

Define the governed path for correcting the reporting failure discovered after
`docs/reviews/CVF_UNABSORBED_KNOWLEDGE_INVENTORY_2026-05-16.md`.

The failure was not that the inventory existed. The failure was that agents
completed absorption, release, and tranche closure work without producing a
clear operator-facing decision report about valuable knowledge that remained
unabsorbed.

This roadmap keeps that correction out of CVF policy until it has been reviewed
and explicitly accepted.

## Scope

In scope:

- classify the reporting failure;
- review whether the proposed operator report is sufficient;
- require a rebuttal before any durable reporting rule is adopted;
- define what an operator-facing unabsorbed-knowledge report must contain if
  the correction is accepted;
- preserve the status of the Claude inventory as an input, not an
  implementation authorization.

Out of scope:

- promoting ADD-A or ADD-D into governance doctrine;
- opening Observability Plane implementation;
- implementing Memory, Skill Evolution, Agent, or Provider runtime gaps;
- changing live release gates;
- changing public claims;
- treating the corrective report as an already adopted CVF rule.

## Non-Goals

This roadmap does not:

- validate every claim in the unabsorbed-knowledge inventory;
- implement any knowledge item;
- create a public-facing claim;
- authorize a runtime surface;
- require a live provider proof;
- make the proposed reporting rule binding without operator acceptance.

## Source

- `docs/reviews/CVF_UNABSORBED_KNOWLEDGE_INVENTORY_2026-05-16.md`
- `docs/reviews/CVF_OPERATOR_PROGRESS_AND_UNABSORBED_KNOWLEDGE_REPORT_2026-05-17.md`
- `CHANGELOG.md`
- `AGENT_HANDOFF_V7_2026-05-16.md`
- `docs/baselines/CVF_16_5_LIVING_INTEGRATION_CLASSIFICATION_SUMMARY_2026-05-16.md`

## Baseline

Current baseline:

- inventory exists and is open pending operator decision;
- operator-facing report exists but was created before this roadmap;
- the report must therefore be treated as a status brief and proposal, not as a
  binding CVF process rule;
- no implementation is authorized by either the inventory or the report.

## Work Plan

| Step | Action | Status |
|---|---|---|
| 1 | Reclassify the existing operator report as not absorption authorization | complete |
| 2 | Create this corrective roadmap | complete |
| 3 | Create a rebuttal review that tests the proposed correction | complete |
| 4 | Update active handoff to preserve the distinction between proposal and adopted rule | complete |
| 5 | Run docs governance and markdown structural guards | pending |
| 6 | Prepare Claude review packet before any unabsorbed-knowledge absorption | complete |
| 7 | Wait for Claude review before selecting the first absorption roadmap | pending |
| 8 | Wait for operator decision before promoting any durable reporting rule | pending |

## Acceptance Criteria

The correction is accepted only if all criteria are true:

- the operator report clearly says it does not authorize implementation,
  doctrine promotion, public claim changes, or process-rule absorption;
- the roadmap exists before any durable correction is claimed;
- the rebuttal review identifies at least one reason the correction could be
  overbroad or premature;
- a Claude review packet exists and clearly says Codex self-review is not
  sufficient for absorption;
- handoff language says the future reporting rule is proposed, not binding;
- docs governance and markdown structural checks pass;
- operator decision remains explicit for ADD-A, ADD-D, Observability Plane, and
  runtime gap roadmaps.

## Verification / Evidence

Required verification before committing this correction packet:

- docs governance compatibility passes;
- markdown structural completeness passes;
- governed file-size guard passes;
- git diff whitespace check passes;
- active handoff references the roadmap and rebuttal as proposed governance
  artifacts, not adopted policy.

Evidence files:

- this roadmap;
- `docs/reviews/CVF_UNABSORBED_KNOWLEDGE_CLAUDE_REVIEW_PACKET_2026-05-17.md`;
- `docs/reviews/CVF_UNABSORBED_KNOWLEDGE_REPORTING_CORRECTION_REBUTTAL_2026-05-17.md`;
- updated `docs/reviews/CVF_OPERATOR_PROGRESS_AND_UNABSORBED_KNOWLEDGE_REPORT_2026-05-17.md`;
- updated `AGENT_HANDOFF_V7_2026-05-16.md`.

## Proposed Corrective Rule

If accepted later, future external-knowledge absorption, GA release, or tranche
series closure should produce an operator-facing summary when either condition
is true:

1. reviewed knowledge remains valuable but unabsorbed;
2. a lane is marked `runtime-owned` while known sub-contracts remain missing.

The summary should state:

- what shipped;
- what did not ship;
- why it did not ship;
- what decision is needed next;
- whether implementation is authorized or only proposed.

## Risk

R0 for this roadmap: documentation only.

Main risk: overcorrecting a reporting miss into a broad process burden. The
rebuttal must therefore test whether this rule should be narrow, trigger-based,
and limited to external-knowledge absorption or release closures.

## Decision

Proposed only. Do not treat this roadmap as acceptance of the corrective rule.
The operator must decide whether the proposed reporting rule becomes binding.
No unabsorbed-knowledge absorption should begin before Claude completes the
review packet.

## Claim Boundary

This roadmap does not absorb the Claude inventory into CVF, does not implement
any inventory item, and does not authorize a new governance rule. It defines the
review path needed before a reporting correction can become binding.

## Related Artifacts

- `docs/reviews/CVF_UNABSORBED_KNOWLEDGE_INVENTORY_2026-05-16.md`
- `docs/reviews/CVF_UNABSORBED_KNOWLEDGE_CLAUDE_REVIEW_PACKET_2026-05-17.md`
- `docs/reviews/CVF_OPERATOR_PROGRESS_AND_UNABSORBED_KNOWLEDGE_REPORT_2026-05-17.md`
- `docs/reviews/CVF_UNABSORBED_KNOWLEDGE_REPORTING_CORRECTION_REBUTTAL_2026-05-17.md`
