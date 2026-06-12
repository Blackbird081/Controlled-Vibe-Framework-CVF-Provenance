# CVF Reviewer-Fast Rescan Gate Placement Hardening Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-06-12

Owner: Codex

## Purpose

Close the EXA-T1 governance finding where the rescan intelligence checker ran
at pre-commit but not at `reviewer-fast`, causing a worker-return structural
defect to surface later than the review phase.

## Scope / Target / Owner Boundary

Target:

- add the existing rescan intelligence checker to the local `reviewer-fast`
  hook chain;
- add focused test coverage so the checker remains in that early review gate.

Owner boundary:

- this batch changes only local governance hook placement and its test;
- it does not change scan-layer runtime behavior, extraction semantics, OCR,
  provider routing, Policy_Local, EC activation, retrieval, or public-sync.

## Target / Source

Target source:

- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/test_run_local_governance_hook_chain.py`

Source finding:

- `docs/reviews/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_ABSORPTION_COMPLETION_2026-06-12.md`

## Findings / Position

Finding: EXA-T1 needed rescan intelligence evidence, but the missing section
was detected by pre-commit rather than the faster reviewer-return gate.

Position: the existing machine checker was correct; its phase placement was
too late for worker-return review. Moving the checker earlier reduces review
latency and prevents orchestrators from accepting incomplete packets.

## Risk / Corrective Action

| Risk | Corrective action | Residual boundary |
| --- | --- | --- |
| Reviewer accepts a worker packet missing rescan evidence | Add rescan intelligence hardening to `reviewer-fast` | Structural evidence only; semantic quality still needs review |
| Fast gate becomes slower | Add only the targeted existing checker, not the full pre-commit corpus suite | Bounded latency increase |
| Claim expands into scan runtime behavior | Keep this as hook-placement hardening only | No extraction/runtime behavior changed |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: promote the EXA-T1 phase-placement finding
into the earliest applicable reviewer gate.

Protected paths:

- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/test_run_local_governance_hook_chain.py`

Operator authorization: the operator directed Codex to focus on comprehensive
CVF foundation hardening before moving to Policy_Local use-case work.

Rollback boundary: revert only the reviewer-fast hook-chain placement and the
matching unit test if the added early checker is wrong. Do not revert EXA-T1
closure, handoff rotation, extraction foundation work, Policy_Local material,
or unrelated governance history.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| EXA-T1 rescan structural defect appeared at pre-commit instead of reviewer-fast | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_PHASE_MOVED_EARLIER | Add `check_rescan_intelligence_hardening.py` to `reviewer-fast` |
| No runtime/provider/cost behavior was exercised | N/A_WITH_REASON | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | Keep claim boundary limited to local governance hook placement |
| No provider output or provider-cost evidence was produced | N/A_WITH_REASON | PROVIDER_OUTPUT_LEARNING | N/A_WITH_REASON | Do not make provider-quality, provider-routing, or cost claims |

## Implementation Summary

Changed files:

- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/test_run_local_governance_hook_chain.py`

Implementation:

- added `rescan intelligence hardening` to `REVIEWER_FAST_CHECKS`;
- added focused test assertion that `reviewer-fast` contains the rescan
  checker label.

## Evidence Trace Block

| Evidence item | Command or source | Result |
| --- | --- | --- |
| Source finding | `docs/reviews/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_ABSORPTION_COMPLETION_2026-06-12.md` | phase-placement gap recorded |
| Focused unit test | `python -m unittest governance.compat.test_run_local_governance_hook_chain` | required before closure |
| Reviewer-fast gate | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | required before closure |
| Pre-closure gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <base> --head HEAD` | required after commit |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_ABSORPTION_COMPLETION_2026-06-12.md`
- Predecessor intake artifact: EXA-T1 worker-return review and closure range
  `e010c9d2..2b48b059`
- Delta ledger status: COMPLETE
- Routing matrix status: COMPLETE
- Semantic sampling status: COMPLETE
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Category | Current finding | Predecessor finding | New disposition | Reason |
| --- | --- | --- | --- | --- |
| NEW_FINDING | `reviewer-fast` lacked rescan intelligence checker | EXA-T1 pre-commit found missing rescan section after reviewer-fast PASS | MACHINE_CHECK_PHASE_MOVED_EARLIER | Move existing checker into earliest reviewer-return gate |
| CHANGED_DISPOSITION | rescan checker phase placement | Previously pre-commit/pre-push/autorun only | reviewer-fast also enforces it | Review packets should fail before closure/commit attempts |
| UNCHANGED_FROM_INTAKE | Rescan evidence remains required for rescan/intake outputs | Existing standard already enforced at pre-commit | PRESERVED | No standard change required |
| REMOVED_OR_REJECTED | Add full pre-commit corpus suite to reviewer-fast | Not in predecessor packet | REJECTED | Too broad for latency-sensitive worker-return review |

### Follow-Up Routing Matrix

| Lane | Item | Disposition |
| --- | --- | --- |
| DO_NOW | Add rescan intelligence checker to `reviewer-fast` | IMPLEMENTED |
| RESOLVED_BY_DESIGN | Preserve full pre-commit as deeper closure gate | PRESERVED |
| OUT_OF_SCOPE | Scan runtime behavior or Policy_Local behavior | NOT_AUTHORIZED |
| SEPARATE_RUNTIME_TRANCHE | `DocumentScanSignals` and `ScanRouteDecision` implementation | EXA-T2 |
| STRATEGIC_OPERATOR_DECISION | Future GitHub-link intake convention for broad external absorption | OPERATOR_CONFIRMED_DIRECTION |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| RF-RS-1 | EXA-T1 finding-to-governance row | rescan defect surfaced too late | MACHINE_CHECK_PHASE_MOVED_EARLIER | Is this worker quality only? | GOVERNANCE_PLACEMENT_GAP_CONFIRMED |
| RF-RS-2 | reviewer-fast hook chain | fast gate should catch reviewer packet defects | DO_NOW | Would adding the whole corpus suite be cleaner? | TARGETED_CHECK_ONLY |
| RF-RS-3 | claim boundary | no runtime scan behavior changed | OUT_OF_SCOPE | Could this be misread as scan-layer semantic improvement? | BOUNDED_TO_GOVERNANCE_GATE |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | N/A with reason: operator-authorized guard-maintenance micro-batch | no standalone work order required | N/A with reason |
| Completion or reviewer artifact | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | next move records reviewer-fast rescan hardening before EXA-T2 | PASS |
| Registry JSON | BLOCKED with reason: this batch adds no CVF corpus/search/classification source corpus eligible for GC-051 | no registry mutation authorized | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: this batch adds no CVF corpus/search/classification source corpus eligible for GC-051 | no registry mutation authorized | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence artifact is consumed by this hook-placement batch | local source and tests only | N/A with reason |
| System loop interlock | N/A with reason: no runtime/system loop mutation | no interlock update required | N/A with reason |
| Session continuity | active state/memory/handoff | session sync follows material commit | PASS |

## Claim Boundary

This closure proves only that the existing rescan intelligence checker is part
of `reviewer-fast` local governance review. It does not prove extraction
quality, semantic scan completeness, OCR readiness, provider behavior,
Policy_Local readiness, public readiness, production readiness, or autonomous
mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance-hook placement hardening; no public-sync batch or
public catalog claim is authorized.
