# CVF GC-018 Authorization Baseline - AHB-T1A Finding Cleanup

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018

Date: 2026-06-16

Batch ID: AHB-T1A

rawMemoryReleased: false

## Purpose

Authorize a bounded cleanup for the two AHB-T1 meta-findings surfaced during
audit authoring:

1. `docs/audits/` artifacts with `HANDOFF` in the filename can be mis-typed by
   the Markdown structural checker as active session handoff documents.
2. Descriptive defect labels must map to the canonical defect-class vocabulary,
   with `RULE_GAP` used for the AHB seam finding.

This baseline exists because the AHB roadmap requires fresh GC-018 before any
audit finding becomes a machine check.

## Authorization Decision

Operator instruction on 2026-06-16: once a finding is seen, handle it, clean it
up, and only then continue to other work.

Decision: process AHB-T1A immediately as a Codex-owned micro-tranche under
`WORKER_MAY_COMMIT`.

## Baseline Decision

AHB-T1A may modify:

- `governance/compat/check_markdown_structural_completeness.py`;
- `governance/compat/test_check_markdown_structural_completeness.py`;
- `governance/compat/test_check_finding_to_governance_learning.py`;
- `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`;
- `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`;
- this GC-018 baseline;
- the matching work order;
- the matching completion review.

No runtime/provider/public-sync/registry/session-state mutation is authorized.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Structural checker classifies by `docType` before path and keyword heuristics | `governance/compat/check_markdown_structural_completeness.py` | `_classify` | `docType` | `_classify` | ACCEPT |
| Structural checker currently has a `handoff` artifact type | `governance/compat/check_markdown_structural_completeness.py` | `SECTION_GROUPS` | `handoff` | `SECTION_GROUPS` | ACCEPT |
| Structural checker applies to governed docs under `docs/` | `governance/compat/check_markdown_structural_completeness.py` | `_is_governed_markdown` | `docs/` | `_is_governed_markdown` | ACCEPT |
| Finding-learning checker defines canonical defect classes | `governance/compat/check_finding_to_governance_learning.py` | `DEFECT_CLASSES` | `RULE_GAP` | `DEFECT_CLASSES` | ACCEPT |
| AHB-T1 completion records the two meta-findings | `docs/reviews/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_COMPLETION_2026-06-16.md` | `## Findings / Position` | `HANDOFF`; `RULE_GAP` | AHB-T1 completion | ACCEPT |
| AHB roadmap requires fresh GC-018 before audit findings become machine checks | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | `## Non-Goals` | `fresh GC-018` | AHB roadmap | ACCEPT |

## Authorized Scope

Authorized:

- patch structural checker classification so explicit `docType` aliases and
  `docs/audits/` path classification win over subject keywords such as
  `HANDOFF`;
- add focused regression tests for the audit-handoff filename case;
- add focused regression test proving descriptive defect labels without a
  canonical class fail the finding-learning gate;
- update the structural standard to state classifier precedence;
- update the AHB roadmap to record AHB-T1A closure;
- create a completion review with evidence.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: patch one existing governance checker and
two focused checker test files to close AHB-T1A finding cleanup. No hook-chain
rewiring, broad guard refactor, or session-state mutation is authorized.

Protected paths:

- governance/compat/check_markdown_structural_completeness.py
- governance/compat/test_check_markdown_structural_completeness.py
- governance/compat/test_check_finding_to_governance_learning.py

Operator authorization: operator instructed Codex on 2026-06-16 that confirmed
findings must be handled and cleaned before continuing to other work.

Rollback boundary: if rejected, revert only AHB-T1A files and keep AHB-T1
closure commits intact.

Forbidden:

- open or ratify AHB-T2;
- implement the unified AHB contract checker;
- absorb or execute AOT-T3;
- mutate runtime/source outside the named checker/test paths;
- mutate session state in the material commit;
- edit interlock registries;
- run provider/API/live proof;
- public-sync;
- claim production or public readiness.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | `docs/audits/` files with `docType: audit` and `HANDOFF` in the filename classify as audit/review, not handoff. |
| AC2 | Structural standard records that explicit `docType` and governed path classification win over subject keywords. |
| AC3 | Focused structural checker test covers the AHB audit filename case. |
| AC4 | Finding-learning focused test proves descriptive noncanonical defect labels are insufficient without canonical vocabulary. |
| AC5 | AHB roadmap records AHB-T1A as a closed cleanup and keeps AHB-T2/AOT-T3 parked. |
| AC6 | Completion review records both findings as handled; no memory-only or chat-only finding remains. |
| AC7 | Focused tests and pre-closure autorun gate pass before closure claim. |

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: this tranche changes governance checker
and test code only. It does not change CVF product runtime, provider adapters,
model routing, registry data, public-sync content, or live governance behavior.

## Evidence / Verification

Required focused checks:

- `python -m pytest governance/compat/test_check_markdown_structural_completeness.py governance/compat/test_check_finding_to_governance_learning.py -q`
- `python governance/compat/check_markdown_structural_completeness.py --base 30076e1b --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 30076e1b --head HEAD`
- `python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base 30076e1b --head HEAD --enforce`

## Rescan Intelligence Hardening

- Original source artifact: AHB-T1 audit completion finding section.
- Predecessor intake artifact: AHB-T1 audit, worker return, Codex rebuttal, and
  completion review.
- Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS.
- Routing matrix status: DO_NOW for AHB-T1A cleanup only; AHB-T2 and AOT-T3
  remain separate decisions.
- Semantic sampling status: bounded regression samples in focused tests.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | AHB-T1A disposition |
|---|---|
| `UNCHANGED_FROM_INTAKE` | AHB-T1 audit remains accepted and closed. |
| `CHANGED_DISPOSITION` | Meta-findings move from follow-up evidence to resolved cleanup. |
| `NEW_FINDING` | None beyond the two AHB-T1 meta-findings. |
| `REMOVED_OR_REJECTED` | No AHB-T2/AOT-T3 work is opened in this tranche. |

### Follow-Up Routing Matrix

| Lane | Applies to | Rationale |
|---|---|---|
| RESOLVED_BY_DESIGN | Audit `HANDOFF` filename classification | handled by checker precedence patch and regression test |
| RESOLVED_BY_DESIGN | Descriptive defect label canonical mapping | handled by finding-learning regression test |
| SEPARATE_RUNTIME_TRANCHE | Unified AHB contract checker | still requires AHB-T2/AHB-T3 authorization |
| STRATEGIC_OPERATOR_DECISION | AHB-T2 contract ratification and AOT-T3 sequencing | not opened by AHB-T1A |
| OUT_OF_SCOPE | Provider/live/public-sync/runtime/product mutation | explicitly forbidden |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AHB-T1A-B1 | AHB-T1 completion Findings / Position | audit filename with `HANDOFF` can be mis-typed | structural checker classification | Could a subject keyword override `docType: audit`? | PASS |
| AHB-T1A-B2 | AHB-T1 completion Findings / Position | descriptive labels must map to `RULE_GAP` | finding-learning defect class validation | Could a descriptive noncanonical class pass alone? | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening. No public-sync batch is
authorized.

## Claim Boundary

AHB-T1A closes the two immediate AHB-T1 meta-findings only. It does not ratify
the Agent Handoff Contract, implement a unified handoff-boundary checker, absorb
AOT-T3, mutate runtime/provider behavior, or authorize public-sync.
