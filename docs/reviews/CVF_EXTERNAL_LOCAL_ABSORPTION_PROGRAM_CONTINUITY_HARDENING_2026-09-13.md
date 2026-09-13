# External/Local Absorption Program Continuity Hardening

Memory class: FULL_RECORD
docType: review
Status: VERIFIED_BOUNDED_PENDING_COMMIT
Date: 2026-09-13

## Purpose

Repair the machine gap exposed after the three-repository external pattern
review: role ownership was enforced, but the active Local absorption batch and
its exit condition were not. This allowed continuity to nominate an unrelated
repository while all three pilot sources still had incomplete runtime-value
accounting.

## Target / Source

The canonical coordination method, its existing checker and focused tests, and
one generated-state source item for the active absorption program. Correct the
current continuity projection after the material guard change commits.

## Core Guard Self-Protection Authorization

Operator authorization: the operator identified that the newly hardened rule
still allowed SOT to leave the three-repository absorption batch and required
the governing machine constraint to prevent recurrence.

Authorized guard-maintenance scope: program-continuity and exit-condition
enforcement only.

Protected paths:

- governance/compat/check_external_knowledge_intake_routing.py
- governance/compat/test_check_external_knowledge_intake_routing.py
- docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md
- CVF_SESSION/state/entries/activeExternalAbsorptionProgram.json
- CVF_SESSION/state/entries/externalLocalAbsorptionCoordination.json
- CVF_SESSION/state/entries/nextAllowedMove.json
- CVF_SESSION/state/entries/domainPilotSelectedReviewDecision20260912.json
- CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json
- CVF_SESSION/ACTIVE_SESSION_STATE.json
- CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json
- CVF_SESSION_MEMORY.md
- AGENT_HANDOFF_V60_2026-09-08.md

Rollback boundary: revert only this continuity hardening and its state
projection. Preserve the accepted external return, three-repository evidence,
stopped repair chains, and prior coordination-role binding.

## Scope / Methodology

Extend the existing checker and hook placement. Read compact state sources only.
Require a structured active-program ledger, source membership for the next Local
step, and terminal accounting or a governed operator scope decision before exit.
No model invocation, source traversal, new hook or runtime implementation.

## Findings / Position

FINDING_CONFIRMED: the first hardening bound who decides and what evidence is
authoritative, but had no active program identity, source set, per-source state,
next-source membership or exit gate. Matching role declarations could therefore
coexist with a wrong cross-batch transition.

## Risk / Corrective Action

Machine structure cannot interpret arbitrary prose. The structured program item
is authoritative; compact next-move prose must project exact program and next
source markers. Tests must reject an unrelated next source, a missing program
item, a prose-marker mismatch, and an exit without terminal evidence or an
operator scope-decision artifact.

## Decision

APPROVED_FOR_EXECUTION by Local under the operator's direct defect report and
the standing error-to-governance rule. Current correction must retain the
three-repository program and return ARCH-ABS-009 to backlog.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | governance/compat/check_external_knowledge_intake_routing.py; governance/compat/check_core_guard_self_protection.py |
| literalTokensReviewed | Core Guard Self-Protection Authorization; Protected paths; External/Local Coordination Binding |
| gateRunPurpose | Confirmation evidence from negative regressions, normal pre-commit and split closure |
| claimBoundary | Structured continuity enforcement, not semantic runtime completeness |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | external knowledge intake routing guard implementation |
| Chain map route | Active Local absorption program to terminal accounting or operator-authorized scope exit |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md |
| Disposition | Repair missing cross-batch transition enforcement |
| Claim boundary | No repository is declared fully absorbed by this guard |

## External/Local Coordination Binding

```json
{
  "contractId": "cvf.external-local-absorption-coordination@1",
  "invariants": {
    "externalRole": "ADVISORY_RESEARCH_AND_PATTERN_MAPPING",
    "externalContext": "PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ",
    "localRole": "SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION",
    "finalDecisionOwner": "LOCAL",
    "localCoverageBasis": "SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST",
    "externalEvidenceAuthority": "INPUT_NOT_PRIVATE_CVF_PROOF"
  },
  "contractSha256": "92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c",
  "parentArtifact": "docs/reviews/CVF_THREE_REPO_PATTERN_COMPARISON_LOCAL_REVIEW_2026-09-13.md"
}
```

## Evidence / Verification

Focused regression: 32/32 PASS with
`python -m unittest discover -s governance/compat -p test_check_external_knowledge_intake_routing.py`.
The added negative cases reject an out-of-program next source, a missing active
program item, a mismatched next-move projection, expansion/exit while incomplete,
terminal exit without complete accounting/evidence, and scope exit without a
governed operator decision. Normal gates and separate material/continuity ranges
control finality.

## Epistemic Process Block

Expected Result / Prediction: a role-correct SOT that leaves an incomplete active
batch must fail. Evidence Comparison: all focused positive and negative tests pass.
Contradiction Or Gap Disposition: add program continuity without changing source
decisions. Claim Update: bounded structured program/exit enforcement verified.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local reviewer/implementer |
| Provider or surface | internal workspace |
| Session or invocation | absorption-program-continuity-20260913 |
| Working directory | private provenance root |
| Command or tool surface | Targeted checker/test/method edits; focused unittest; normal gates |
| Target paths | governance/compat/check_external_knowledge_intake_routing.py; governance/compat/test_check_external_knowledge_intake_routing.py; docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md; docs/reviews/CVF_EXTERNAL_LOCAL_ABSORPTION_PROGRAM_CONTINUITY_HARDENING_2026-09-13.md |
| Allowed scope source | Operator defect report and exact authorization above |
| Before status evidence | HEAD 4843b147f; clean |
| After status evidence | Four material paths; continuity follows separately |
| Diff evidence | git diff --check; focused 32/32 PASS |
| Approval boundary | Program continuity and exit gate only |
| Claim boundary | No source/runtime completion |
| Agent type | reviewer/implementer |
| Invocation ID | absorption-program-continuity-20260913 |
| Expected manifest | four Target paths above |
| Actual changed set | four Target paths above |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY: private continuity and guard repair.

## Claim Boundary

No source completion, external invocation, implementation, provider, live,
deployment or broader-repository admission claim.
