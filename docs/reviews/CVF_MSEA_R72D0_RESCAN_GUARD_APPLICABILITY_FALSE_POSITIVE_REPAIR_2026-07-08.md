# CVF MSEA-R72D0 Rescan Guard Applicability False-Positive Repair

Memory class: governed-completion-review
Status: CLOSED_PASS_BOUNDED
Date: 2026-07-08

## Purpose

Close a bounded R72D0 micro-tranche that repairs one remaining applicability
false-positive class in the local checker before R72D worker execution resumes.

## Target / Source

Target paths:

- `governance/compat/check_rescan_intelligence_hardening.py`
- `governance/compat/test_check_rescan_intelligence_hardening.py`

Source authority is the current repository source and focused test behavior.
The operator-provided Claude note is advisory input only and is not promoted as
CVF source authority.

## Scope / Methodology

Method: read the active startup surfaces, guard orientation, literal-format
gotchas, the target checker, and its focused tests; confirm the reported
failure class against source; make the smallest checker change; add regression
tests for the observed variants; verify with focused tests and governance
gates.

## Findings / Position

Finding: the checker had two related but separate signal paths. The compact
not-applicable validator used `_has_real_rescan_signal_outside_section`, while
the file-applicability gate used a shorter path that did not share every
self-reference filter.

Position: R72D0 is a narrow false-positive repair. It reuses the already tested
real-signal helper for ordinary active Markdown applicability and expands the
compound self-reference regex to cover the `re-scan` spelling. It does not
weaken evidence requirements for real applicable outputs.

## Risk / Corrective Action

Risk: an over-broad exclusion could hide a true applicable artifact.

Corrective action: keep path-name detection for work orders intact, reuse the
same helper that still preserves the positive real-output regression, and add
focused tests for the four newly reported drafting variants.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | `APPLICABILITY_PATTERNS`; `_is_applicable_output`; `_has_real_rescan_signal_outside_section`; `RESCAN_SELF_REFERENCE_COMPOUND_RE`; `Core Guard Self-Protection Authorization`; `Protected paths`; `Authorized guard-maintenance scope`; `Operator authorization`; `Rollback boundary`; `Rescan intelligence verdict:`; `NOT_APPLICABLE_WITH_REASON`; `N/A with reason` |
| gateRunPurpose | confirmation/evidence before material commit |
| claimBoundary | checker-maintenance false-positive repair only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Applicability path is owned by the target checker | EXISTS | `governance/compat/check_rescan_intelligence_hardening.py` | `_is_applicable_output` | `_is_applicable_output` | target checker | ACCEPT |
| Real-signal detection helper already exists | EXISTS | `governance/compat/check_rescan_intelligence_hardening.py` | `_has_real_rescan_signal_outside_section` | `_has_real_rescan_signal_outside_section` | target checker | ACCEPT |
| Existing self-reference compound filter exists | EXISTS | `governance/compat/check_rescan_intelligence_hardening.py` | `RESCAN_SELF_REFERENCE_COMPOUND_RE` | `RESCAN_SELF_REFERENCE_COMPOUND_RE` | target checker | ACCEPT |
| Literal gotcha documents this checker self-reference trap | EXISTS | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | gotcha 22 | self-reference keyword trap | literal-format checklist | ACCEPT |
| Existing ADIF entry covers broad applicability-marker false positives | EXISTS | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0021.md` | `surfaceSelectors` and `Remediation` | `CVF_ADIF-0021` | ADIF registry | ACCEPT |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: repair the target checker's remaining
file-applicability self-reference false positives and add focused regression
tests.

Protected paths:

- `governance/compat/check_rescan_intelligence_hardening.py`
- `governance/compat/test_check_rescan_intelligence_hardening.py`

Operator authorization: operator identified the Claude-reported finding as
needing handling and asked Codex to address it.

Rollback boundary: revert this review plus the two target checker/test edits
together if the repair is rejected.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=checker-maintenance; role=reviewer;
lifecyclePhase=pre-implementation.

Resolved defects:

- `NONE_RETURNED`

Disposition: no resolver-matched defect was returned for this exact query.
The broader applicability-marker class is already recorded in `CVF_ADIF-0021`,
so this tranche repairs the source instead of adding another duplicate ADIF
entry.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | local reviewer verification against current CVF source |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this completion review plus target checker tests |
| Disposition | ADAPTED_AS_LOCAL_CHECKER_REPAIR |
| Claim boundary | Claude report is advisory input only; accepted facts are source-verified against local checker code and tests |

## Accepted Changed Set

| Path | Disposition |
| --- | --- |
| `governance/compat/check_rescan_intelligence_hardening.py` | reuse real-signal helper for file applicability and extend compound token coverage |
| `governance/compat/test_check_rescan_intelligence_hardening.py` | add four regression tests for the reported drafting variants |
| `docs/reviews/CVF_MSEA_R72D0_RESCAN_GUARD_APPLICABILITY_FALSE_POSITIVE_REPAIR_2026-07-08.md` | closure record and core-guard authorization |

## Command Evidence

| Command | Result |
| --- | --- |
| `python -m pytest governance/compat/test_check_rescan_intelligence_hardening.py -q` | PASS: 20 tests |
| `python governance/compat/check_rescan_intelligence_hardening.py --base c75bbe75f --head HEAD --enforce` | PASS |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: N/A with reason: this is checker maintenance, not a rescan or intake refresh output.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no corpus report or corpus
  manifest is produced by this checker-maintenance micro-tranche.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| File-applicability path did not reuse the stronger real-signal filter | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_REPAIRED | Patch the target checker and retain focused regression tests |
| Runtime/provider/cost applicability | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime, provider, live, token, or cost behavior changed or claimed |

Runtime/provider/cost learning lane: N/A_WITH_REASON - this tranche changes
only local governance checker code, tests, and a completion review.

## Epistemic Process Block

### Expected Result / Prediction

Prediction: reusing `_has_real_rescan_signal_outside_section` inside
`_is_applicable_output` will stop self-reference drafting phrases from making
ordinary review notes applicable while preserving true positive behavior for
real applicable output text.

### Evidence Comparison

Observed evidence: focused pytest now passes 20 tests, including the prior 16
regressions plus four new self-reference applicability variants. The target
checker also passes on the current changed range.

### Contradiction Or Gap Disposition

Disposition: no contradiction remains in the tested scope. The repair is still
bounded to the target checker and does not claim to solve every possible
keyword-based false trigger in other guards.

### Claim Update

Claim update: R72C1's prior repair remains valid, and R72D0 adds one adjacent
file-applicability repair for the same checker before R72D worker execution.

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
| forbiddenExpansion | no public-sync, no runtime/product business logic, no Fast Lane standard change |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex |
| Provider or surface | local workspace tools |
| Session or invocation | R72D0 checker-maintenance micro-tranche, 2026-07-08 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `apply_patch`; pytest; target governance checker |
| Target paths | `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/test_check_rescan_intelligence_hardening.py`; this review |
| Allowed scope source | operator instruction that the Claude-reported finding needs handling |
| Before status evidence | `git status --short --branch`; `git rev-parse --short HEAD`; `git rev-parse --short '@{upstream}'` returned clean and both refs at `c75bbe75f` |
| After status evidence | `git status --short` before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | direct operator authorization for R72D0 micro-tranche |
| Claim boundary | checker-maintenance only |
| Agent type | reviewer/closer |
| Invocation ID | `msea-r72d0-rescan-guard-applicability-false-positive-repair-2026-07-08` |
| Expected manifest | `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/test_check_rescan_intelligence_hardening.py`; `docs/reviews/CVF_MSEA_R72D0_RESCAN_GUARD_APPLICABILITY_FALSE_POSITIVE_REPAIR_2026-07-08.md` |
| Actual changed set | `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/test_check_rescan_intelligence_hardening.py`; `docs/reviews/CVF_MSEA_R72D0_RESCAN_GUARD_APPLICABILITY_FALSE_POSITIVE_REPAIR_2026-07-08.md` |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: provenance checker-maintenance closure only; no public-sync mutation or
public export action is authorized in R72D0.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | N/A with reason: operator directly authorized this bounded checker-maintenance micro-tranche | this completion review | N/A with reason: no delegated work order |
| Completion or reviewer artifact | `docs/reviews/CVF_MSEA_R72D0_RESCAN_GUARD_APPLICABILITY_FALSE_POSITIVE_REPAIR_2026-07-08.md` | this file changed in `git status --short` | PASS |
| Roadmap state | N/A with reason: R72D worker execution remains the next planned tranche and no roadmap file is changed here | active session surfaces after material commit | N/A with reason: no roadmap file changed |
| Registry JSON | BLOCKED with reason: no GC-051 registry JSON surface applies to this checker-maintenance false-positive repair | `git status --short` before material commit | BLOCKED with reason: registry update intentionally out of scope |
| Registry Markdown | BLOCKED with reason: no GC-051 registry Markdown surface applies to this checker-maintenance false-positive repair | `git status --short` before material commit | BLOCKED with reason: registry update intentionally out of scope |
| External evidence digest | N/A with reason: external finding text is advisory only and not imported as evidence authority | this completion review and accepted changed set | N/A with reason: no external evidence import |
| System loop interlock | focused tests plus pre-implementation autorun gate | command evidence before material commit | PASS |
| Session continuity | active session surfaces after material commit | session-sync commit required after material commit | PASS |

## Claim Boundary

This artifact claims only that R72D0 repaired one local checker false-positive
class and preserved focused regression coverage. It does not execute R72D
worker tasks, ratify FAST_DOC_LANE, alter Fast Lane standards, mutate
public-sync, run provider/live proof, or change production/runtime behavior.
