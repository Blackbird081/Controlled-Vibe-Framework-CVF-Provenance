# CVF Agent Carrier EARTR Task Route Authorization

Memory class: REVIEW_RECORD

Status: COMPLETE_REVIEWED

docType: review

Date: 2026-08-29

## Purpose

Authorize one bounded root-carrier routing correction so a local agent assigned
a repository-intake task reaches the existing EARTR 1.2 front door directly.
The change creates no protocol, owner, runtime behavior, or implementation
authority.

## Target / Source

- Target: the existing task-class routing row in `AGENTS.md`.
- Canonical destination: `docs/reference/external_agent_review/README.md`.
- Protocol identity: `cvf.external-agent-round-trip@1.2.0`.
- Operator source: explicit direction to close local-agent discoverability
  before the next repository use case.

## Scope / Methodology

Replace one existing row without adding a carrier line, retain all corpus and
task-proportional owners, add the existing EARTR front door, and verify carrier
budgets plus self-protection gates. Protocol documents, validators, schemas,
runtime code, public projections, and the dated compaction index are unchanged.

## Findings / Position

`ACCEPT_BOUNDED_ROUTE_REPAIR`

Canonical EARTR semantics and machine support already existed. The remaining
gap was only direct root-carrier discovery for this task class, so one routed
row is sufficient and no parallel protocol or new owner is justified.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope:

- Replace one existing task-class routing row with an equally bounded row that
  also points to the current EARTR front door and protocol version.

Protected paths:

- `AGENTS.md`

Operator authorization:

- The operator explicitly directed this discoverability repair before the next
  independent repository use case.

Rollback boundary:

- Revert the single carrier row if instruction-carrier, routing, or pre-commit
  governance checks fail. No provider, runtime, public-sync, deployment, or
  production action is authorized.

## Risk / Corrective Action

The only material risk is future route drift between the root carrier and the
EARTR front door. Existing instruction-carrier checks preserve carrier shape;
the next independent repository use case provides operational confirmation.
If the route becomes stale, correct the same row rather than introduce another
protocol surface.

## Epistemic Process Block

Epistemic Process Applicability: APPLICABLE: the prior audit found canonical
EARTR ownership but only partial root-carrier discoverability.

Expected Result / Prediction: adding the existing front door to the task-class
row makes the route explicit without increasing the carrier line count.

Evidence Comparison: the carrier remains at 220 lines, the canonical EARTR
front door remains unchanged, and instruction-carrier focused checks pass.

Contradiction Or Gap Disposition: no protocol semantic gap was found; only the
root discovery route required correction.

Claim Update: local agents following `AGENTS.md` now receive a direct EARTR 1.2
route for repository intake. This is routing evidence, not universal hidden
memory or runtime-enforcement proof.

## Claim Boundary

Verification covers deterministic route presence, carrier budgets,
self-protection authorization, documentation structure, and local governance
checks. It does not prove that an agent ignored its instructions cannot deviate,
nor does it authorize source import, implementation, provider use, or public
mutation.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external knowledge intake routing guard implementation |
| Chain map route | root task classification -> existing EARTR front door -> later source-specific return validation and Local reconciliation |
| Matching local-view guard | `governance/compat/check_agent_instruction_carriers.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `AGENTS.md`; existing EARTR front door and representation contract |
| Disposition | reuse the existing protocol through a direct local-agent discovery route |
| Claim boundary | this artifact routes future intake tasks only; it does not perform or approve an absorption decision |

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_closure_packaging_preflight.py`; `governance/compat/check_agent_instruction_carriers.py`; `governance/compat/check_active_archive_hygiene.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | `Core Guard Self-Protection Authorization`; `Protected paths`; `External Knowledge Intake Routing`; `Matching local-view guard`; `applicableCheckersRead`; `gateRunPurpose`; `claimBoundary` |
| gateRunPurpose | confirm the source-reviewed route and authorization shape; gates provide confirmation evidence rather than first discovery |
| claimBoundary | checker evidence covers the bounded carrier route and review artifact only; it makes no universal agent-compliance or runtime claim |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | EARTR discovery-route hardening, 2026-08-29 |
| Working directory | repository root |
| Command or tool surface | source reads, `rg`, `apply_patch`, focused checkers, Git commit |
| Target paths | `AGENTS.md`; this authorization review |
| Allowed scope source | operator direction to make the route available to other local agents |
| Before status evidence | EARTR canonical and machine-supported; root route generic |
| After status evidence | root task-class row points directly to EARTR 1.2 front door |
| Diff evidence | one replaced carrier row plus this authorization review |
| Approval boundary | bounded discoverability routing only |
| Claim boundary | no protocol, runtime, provider, implementation, public, deployment, or production expansion |
| Agent type | orchestrator/reviewer |
| Invocation ID | `eartr-local-agent-route-2026-08-29` |
| Expected manifest | `AGENTS.md`; this authorization review |
| Actual changed set | `AGENTS.md`; this authorization review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private root-carrier routing and authorization evidence. The
public EARTR 1.2 representation already exists and is unchanged.
