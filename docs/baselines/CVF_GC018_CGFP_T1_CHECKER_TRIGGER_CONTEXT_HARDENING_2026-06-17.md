# CVF GC-018 CGFP-T1 Checker Trigger-Context Hardening

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_DISPATCH

docType: baseline

Date: 2026-06-17

Owner: Codex

rawMemoryReleased: false

GC-018 class: governance-checker-hardening

## Purpose

Authorize CGFP-T1, a bounded checker-hardening tranche that makes four
governance checkers context-aware so they stop raising false-positive
violations on trigger keywords that appear only inside code fences, inline code
spans, cited file paths, or recognized N/A declaration lines. This closes the
repeating MACHINE_GATE_GAP recorded in the CGFP-T1 finding.

## Scope / Source / Owner Boundary

Target: the keyword-applicability logic of four named checkers and their
focused tests. Owner boundary: this GC-018 authorizes checker-logic and test
changes only. It does not authorize new gate wiring, runtime/product mutation,
provider/live proof, public-sync, registry edits, or any relaxation of a real
violation path.

## Authorization / Decision

Operator instruction (2026-06-17): after the PRFC-T1 packet authoring exposed
repeated checker false positives, the operator chose to open the checker-
hardening lane immediately. CGFP is a separate lane from PRFC; it does not
belong to the PRFC roadmap and carries its own authorization.

Commit mode: WORKER_MUST_NOT_COMMIT. Claude implements the checker and test
changes as pending; Codex reviews and commits/closes.

## Source Authority

- Finding record:
  `docs/reviews/CVF_CGFP_T1_CHECKER_TRIGGER_FALSE_POSITIVE_FINDING_2026-06-17.md`
- Candidate checkers:
  `governance/compat/check_machine_closure_package.py`
  `governance/compat/check_closure_packaging_preflight.py`
  `governance/compat/check_foundation_storage_layout.py`
  `governance/compat/check_rescan_intelligence_hardening.py`
- Reusable helpers (prior art):
  `governance/compat/check_central_facts_reference.py`
- Finding-learning standard:
  `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Disposition |
|---|---|---|---|---|
| Corpus signal regex is bare-keyword | `governance/compat/check_machine_closure_package.py` | line 59 | `CORPUS_SIGNAL_RE` | ACCEPT |
| Closed-equivalent scans first 80 lines | `governance/compat/check_closure_packaging_preflight.py` | `_is_closed_equivalent` | `CLOSED_PASS` substring | ACCEPT |
| Foundation markers are bare words | `governance/compat/check_foundation_storage_layout.py` | lines 34, 46 | `FOUNDATION_WORK_MARKERS`; `FOUNDATION_ACTION_MARKERS` | ACCEPT |
| Rescan applicability is bare-keyword | `governance/compat/check_rescan_intelligence_hardening.py` | line 77 | `APPLICABILITY_PATTERNS` | ACCEPT |
| Reusable fence/placeholder helpers exist | `governance/compat/check_central_facts_reference.py` | lines 181, 193 | `_is_in_code_fence`; `_is_placeholder` | ACCEPT |

## Continuation Class And Depth Audit

GC-018 Continuation Candidate

- Candidate ID: CGFP-T1
- Date: 2026-06-17
- Parent roadmap / wave: N/A with reason - new standalone hardening lane derived from the CGFP-T1 finding
- Proposed scope: context-aware keyword applicability for four checkers + focused tests
- Continuation class: STRUCTURAL
- Quality-first decision: REMEDIATE_FIRST
- Remediation target if not expanding: stop false positives that waste authoring rounds and risk hiding real violations
- Why now: the gap repeats (B2, B15) and was just hit again; fixing the checker logic is the durable control
- Active-path impact: LIMITED
- Risk if deferred: authors keep stripping legitimate prose to dodge keywords, eroding gate signal
- Lateral alternative considered: YES
- Why not lateral shift: the rule already exists in memory; the durable fix is in checker logic, not another written rule
- Real decision boundary improved: YES
- Expected enforcement class: CI_REPO_GATE
- Required evidence if approved:
  - each checker ignores trigger words inside code fences / inline code / cited paths / N/A lines
  - each checker still fires on a real in-scope violation (true-positive test)
  - focused tests pass for all four checkers

Depth Audit

- Risk reduction: 2
- Decision value: 1
- Machine enforceability: 2
- Operational efficiency: 2
- Portfolio priority: 1
- Total: 8
- Decision: CONTINUE
- Reason: durable machine improvement closing a repeating gate gap with reusable prior art.

Authorization Boundary

- Authorized now: YES
- If YES, next batch name: CGFP-T1 dispatch and execution (WORKER_MUST_NOT_COMMIT)
- Reopen trigger for any CGFP-T2: fresh GC-018 if more checkers need the same treatment

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: CGFP-T1 may modify the four named
governance checkers and their focused tests to add context-aware keyword
applicability. It must not relax any real violation path, add gate wiring, or
change any other checker.

Protected paths:

- governance/compat/check_machine_closure_package.py
- governance/compat/check_closure_packaging_preflight.py
- governance/compat/check_foundation_storage_layout.py
- governance/compat/check_rescan_intelligence_hardening.py
- governance/compat/test_check_machine_closure_package.py
- governance/compat/test_check_closure_packaging_preflight.py
- governance/compat/test_check_foundation_storage_layout.py
- governance/compat/test_check_rescan_intelligence_hardening.py
- AGENT_HANDOFF_V19_2026-06-15.md

Operator authorization: operator instruction 2026-06-17 to open the checker-
hardening lane immediately.

Rollback boundary: if rejected, revert only the CGFP-T1 checker and test
changes. Do not revert the CGFP-T1 finding, the PRFC-T1 packet, or any prior
closure.

## Tranche Closure Checklist

- [ ] Public catalog updated OR explicitly N/A: N/A - internal checker hardening, no public capability change
- [ ] All new catalog paths Test-Path verified in public-sync clone: N/A - no catalog change
- [ ] GC-020 handoff Current HEAD updated to this tranche's commit SHA
- [ ] Evidence Trace Block present for all significant claims (GC-046)
- [ ] Legacy Spec Scan Block present OR explicitly N/A: N/A - no legacy source read
- [ ] Blind-Spot Control block present OR explicitly N/A: N/A - no external/legacy source absorbed
- [ ] Corpus Completeness block present OR explicitly N/A: N/A - not a folder enumeration
- [ ] Intake-Hardening block present OR explicitly N/A: N/A - not a re-intake
- [ ] Knowledge System Reconciliation block present OR explicitly N/A: N/A - not a knowledge map
- [ ] Protected file changes have Core Guard Self-Protection Authorization
- [ ] New review/sync review artifacts include required structural review sections
- [ ] Finding-bearing artifacts include canonical Finding-To-Governance Learning Disposition
- [ ] Active session nextAllowedMove and latest closed LHW continuity remain aligned
- [ ] Pre-push autorun gate run on a committed non-empty range

## Decision

AUTHORIZE CGFP-T1 as a bounded checker-hardening tranche under
WORKER_MUST_NOT_COMMIT. Depth Audit total 8, decision CONTINUE.

## Verification

Required evidence before CGFP-T1 closure:

- for each of the four checkers, a focused test proving an incidental trigger
  word inside a code fence / inline code / cited path / N/A line no longer
  raises a violation;
- for each checker, a true-positive test proving a real in-scope violation
  still fires;
- all four focused test suites pass;
- a committed-range pre-closure gate run by the reviewer.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `MACHINE_GATE_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `MACHINE_CHECK_ADDED` |
| Next control action | CGFP-T1 implements context-aware keyword applicability in four checkers |
| Worker blame | `N/A_WITH_REASON`: bare-keyword applicability is a checker design gap |

## Rescan Intelligence Hardening

- Original source artifact: N/A with reason: not a re-intake; a checker-behavior hardening baseline
- Predecessor intake artifact: N/A with reason: none
- Delta ledger status: N/A with reason
- Routing matrix status: N/A with reason
- Semantic sampling status: N/A with reason
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Category | Item | Disposition | Reason |
| --- | --- | --- | --- |
| UNCHANGED_FROM_INTAKE | N/A | N/A | not a re-intake |
| CHANGED_DISPOSITION | N/A | N/A | not a re-intake |
| NEW_FINDING | checker trigger false positive | authorized for hardening | derived from finding |
| REMOVED_OR_REJECTED | N/A | N/A | not a re-intake |

### Follow-Up Routing Matrix

| Routing lane | Item | Routed action |
| --- | --- | --- |
| DO_NOW | CGFP-T1 hardening | authorized |
| SEPARATE_RUNTIME_TRANCHE | N/A | N/A |
| STRATEGIC_OPERATOR_DECISION | N/A | N/A |
| OUT_OF_SCOPE | gate wiring | excluded |
| RESOLVED_BY_DESIGN | N/A | N/A |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| s1 | Source Verification | trigger constants are bare-keyword | confirmed by line refs | could be intentional? | PASS |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance baseline. No public-sync batch is
authorized.

## Claim Boundary

This GC-018 authorizes a bounded checker-hardening dispatch. It does not add
gate wiring, mutate runtime or product behavior, run provider/live proof,
perform public-sync, edit registries, or claim production or public launch.
