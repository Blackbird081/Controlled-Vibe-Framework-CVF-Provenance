# CVF MSEA-R72C1 Rescan Guard Self-Reference False-Positive Repair

Memory class: governed-completion-review
Status: CLOSED_PASS_BOUNDED
Date: 2026-07-08

## Purpose

Close the bounded R72C1 micro-tranche that repairs one repeated
checker-maintenance false-positive observed during R72C closure work.

## Scope / Methodology

Method: read the active startup surfaces, guard orientation, literal-format
gotchas, the target checker, and its focused tests; add the smallest source
filter needed for negated explanatory clauses; add regression tests; verify
with focused tests and governance gates.

## Findings / Position

Finding: the target checker already excluded several non-signal discussion
phrases, but it still treated ordinary negated explanatory clauses as
applicability evidence when they mentioned the output class the checker owns.

Position: R72C1 is a narrow false-positive repair. It does not weaken the
required evidence path for real applicable outputs, work orders, or source
refresh packets.

## Risk / Corrective Action

Risk: an over-broad exclusion could hide a true applicable artifact.

Corrective action: the new filter is bounded to short negated clauses and the
existing positive regression still prevents an applicable sample from using a
compact not-applicable verdict.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | `APPLICABILITY_PATTERNS`; `_has_real_rescan_signal_outside_section`; `RESCAN_SELF_REFERENCE_COMPOUND_RE`; `Core Guard Self-Protection Authorization`; `Protected paths`; `Authorized guard-maintenance scope`; `Operator authorization`; `Rollback boundary`; `Rescan intelligence verdict:`; `NOT_APPLICABLE_WITH_REASON`; `N/A with reason` |
| gateRunPurpose | confirmation/evidence before material commit |
| claimBoundary | checker-maintenance false-positive repair only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Applicability keywords are centralized in the target checker | EXISTS | `governance/compat/check_rescan_intelligence_hardening.py` | `APPLICABILITY_PATTERNS` | `APPLICABILITY_PATTERNS` | target checker | ACCEPT |
| Real-signal detection for compact not-applicable sections is owned by one helper | EXISTS | `governance/compat/check_rescan_intelligence_hardening.py` | `_has_real_rescan_signal_outside_section` | `_has_real_rescan_signal_outside_section` | target checker | ACCEPT |
| Existing compound self-reference exclusion exists before this repair | EXISTS | `governance/compat/check_rescan_intelligence_hardening.py` | `RESCAN_SELF_REFERENCE_COMPOUND_RE` | `RESCAN_SELF_REFERENCE_COMPOUND_RE` | target checker | ACCEPT |
| Existing compact not-applicable regression tests cover checker-maintenance prose | EXISTS | `governance/compat/test_check_rescan_intelligence_hardening.py` | compact not-applicable tests | `test_compact_not_applicable_can_discuss_rescan_checker_scope`; `test_compact_not_applicable_can_discuss_rescan_hardening_compound_phrasing` | target checker tests | ACCEPT |
| Literal gotcha documents this checker's self-reference trap | EXISTS | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | gotcha 22 | self-reference keyword trap | literal-format checklist | ACCEPT |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: repair the target checker's false-positive
handling for short negated explanatory clauses and add focused regression
tests.

Protected paths:
- `governance/compat/check_rescan_intelligence_hardening.py`
- `governance/compat/test_check_rescan_intelligence_hardening.py`

Operator authorization: operator instructed Codex to handle this separate
tranche before the later Claude-owned R72D step.

Rollback boundary: revert this review plus the two target checker/test edits
together if the repair is rejected.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=checker-maintenance; role=reviewer;
lifecyclePhase=pre-implementation.

Resolved defects:
- `NONE_RETURNED`

Disposition: no existing ADIF entry was returned for this exact query. The
repair is source-backed by the changed checker tests and the documented
literal-format gotcha.

## Accepted Changed Set

| Path | Disposition |
| --- | --- |
| `governance/compat/check_rescan_intelligence_hardening.py` | add bounded negated-context filter |
| `governance/compat/test_check_rescan_intelligence_hardening.py` | add two regression tests |
| `docs/reviews/CVF_MSEA_R72C1_RESCAN_GUARD_SELF_REFERENCE_FALSE_POSITIVE_REPAIR_2026-07-08.md` | closure record and core-guard authorization |

## Command Evidence

| Command | Result |
| --- | --- |
| `python -m pytest governance/compat/test_check_rescan_intelligence_hardening.py -q` | PASS: 16 tests |
| `python governance/compat/check_rescan_intelligence_hardening.py --base 6ec393a79 --head HEAD --enforce` | PASS |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: N/A with reason: this is checker maintenance, not a rescan or intake refresh output.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no corpus report or corpus
  manifest is produced by this checker-maintenance micro-tranche.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external knowledge intake routing guard implementation |
| Chain map route | local checker-maintenance artifact with no external artifact import |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this completion review |
| Disposition | local checker false-positive repair only |
| Claim boundary | CVF source authority remains repo-governed local source and tests |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| Negated explanatory clauses could still trigger the target checker | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | Patch the target checker and retain focused regression tests |
| Runtime/provider/cost applicability | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime, provider, live, token, or cost behavior changed or claimed |

Runtime/provider/cost learning lane: N/A_WITH_REASON - this tranche changes
only local governance checker code, tests, and a completion review.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | bounded checker false-positive repair |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: focused pytest and target checker command evidence above |
| actionEvidence | ACTION_EVIDENCE_PRESENT: changed set listed above |
| invocationBoundary | local shell and apply_patch only |
| interceptionBoundary | no runtime/provider/live interception |
| claimLanguage | no public, production, provider, or workflow-value claim |
| forbiddenExpansion | no public-sync, no runtime/source business logic, no Fast Lane standard change |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex |
| Provider or surface | local workspace tools |
| Session or invocation | R72C1 checker-maintenance micro-tranche, 2026-07-08 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `apply_patch`; pytest; target governance checker |
| Target paths | `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/test_check_rescan_intelligence_hardening.py`; this review |
| Allowed scope source | operator instruction to handle this separate tranche before the later Claude-owned R72D step |
| Before status evidence | `git status --short --branch`; `git rev-parse --short HEAD`; `git rev-parse --short '@{upstream}'` returned clean and both refs at `6ec393a79` |
| After status evidence | `git status --short` to be recorded before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | direct operator authorization for R72C1 micro-tranche |
| Claim boundary | checker-maintenance only |
| Agent type | reviewer/closer |
| Invocation ID | `msea-r72c1-rescan-guard-self-reference-false-positive-repair-2026-07-08` |
| Expected manifest | `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/test_check_rescan_intelligence_hardening.py`; `docs/reviews/CVF_MSEA_R72C1_RESCAN_GUARD_SELF_REFERENCE_FALSE_POSITIVE_REPAIR_2026-07-08.md` |
| Actual changed set | `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/test_check_rescan_intelligence_hardening.py`; `docs/reviews/CVF_MSEA_R72C1_RESCAN_GUARD_SELF_REFERENCE_FALSE_POSITIVE_REPAIR_2026-07-08.md` |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: provenance checker-maintenance closure only; no public-sync mutation or
public export action is authorized in R72C1.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | N/A with reason: operator directly authorized this bounded checker-maintenance micro-tranche | this completion review | N/A with reason: no delegated work order |
| Completion or reviewer artifact | `docs/reviews/CVF_MSEA_R72C1_RESCAN_GUARD_SELF_REFERENCE_FALSE_POSITIVE_REPAIR_2026-07-08.md` | this file changed in `git status --short` | PASS |
| Roadmap state | N/A with reason: R72D remains the next planned tranche and no roadmap file is changed here | active session surfaces after material commit | N/A with reason: no roadmap file changed |
| Registry JSON | BLOCKED with reason: no GC-051 registry JSON surface applies to this checker-maintenance false-positive repair | `git status --short` before material commit | BLOCKED with reason: registry update intentionally out of scope |
| Registry Markdown | BLOCKED with reason: no GC-051 registry Markdown surface applies to this checker-maintenance false-positive repair | `git status --short` before material commit | BLOCKED with reason: registry update intentionally out of scope |
| External evidence digest | N/A with reason: no external evidence artifact or out-of-repo path is used by this tranche | this completion review and accepted changed set | N/A with reason: no external evidence |
| System loop interlock | focused tests plus pre-implementation autorun gate | command evidence before material commit | PASS |
| Session continuity | active session surfaces after material commit | session-sync commit required after material commit | PASS |

## Claim Boundary

This artifact claims only that R72C1 repaired one local checker
false-positive class and preserved focused regression coverage. It does not
execute the later Claude-owned R72D step, ratify FAST_DOC_LANE, alter Fast Lane standards, mutate
public-sync, run provider/live proof, or change production/runtime behavior.
