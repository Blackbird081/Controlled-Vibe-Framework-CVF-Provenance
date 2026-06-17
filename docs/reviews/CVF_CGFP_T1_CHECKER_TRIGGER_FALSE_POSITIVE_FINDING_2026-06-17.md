# CVF CGFP-T1 Checker Trigger False-Positive Finding

Memory class: FULL_RECORD

Status: FINDING_RECORDED_HARDENING_AUTHORIZED

docType: finding_review

Date: 2026-06-17

Reviewer: Claude (combined-role authoring under operator instruction 2026-06-17)

rawMemoryReleased: false

## Purpose

Record a repeating governance-control-plane finding: several dispatch and
closure machine checkers raise false-positive violations when their bare
trigger keywords appear inside cited filenames, inherited template row labels,
standard claim-boundary prose, or the very N/A lines that declare a section
non-applicable. This finding authorizes a bounded checker-hardening lane
(CGFP) so the gates judge real scope, not incidental words.

## Scope / Target / Owner Boundary

Target: the keyword-applicability logic of four governance checkers. Owner
boundary: this review records the finding and proposes the hardening lane; it
does not modify checker code. Implementation requires the CGFP-T1 GC-018 and
work order, reviewed and closed by Codex.

## Target / Source

Observed while authoring the PRFC-T1 dispatch packet (GC-018 +
work order) at base HEAD `2fc9114e`. The pre-dispatch autorun gate cycled
through 8 -> 6 -> 5 -> 3 -> 1 -> 0 failing gates across multiple authoring
rounds; most repairs were rewording incidental trigger words, not correcting
real scope.

Source checkers:

- `governance/compat/check_machine_closure_package.py` (`CORPUS_SIGNAL_RE`, line 59)
- `governance/compat/check_closure_packaging_preflight.py` (`STALE_CLOSED_PATTERNS`, line 50; `_is_closed_equivalent` scans first 80 lines)
- `governance/compat/check_foundation_storage_layout.py` (`FOUNDATION_WORK_MARKERS` line 34, `FOUNDATION_ACTION_MARKERS` line 46)
- `governance/compat/check_rescan_intelligence_hardening.py` (`APPLICABILITY_PATTERNS`, line 77)

Prior art for the fix (reusable, do not reinvent):

- `governance/compat/check_central_facts_reference.py` already has
  `_is_in_code_fence` (line 181) and `_is_placeholder` (line 193).

## Scope / Methodology

Each false trigger was located by `grep` against the authored packet and
cross-checked against the checker's trigger constant. Each candidate checker
was inspected for whether it strips code fences / inline code / citations
before keyword matching.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Disposition |
|---|---|---|---|---|
| Corpus signal is bare-keyword | `governance/compat/check_machine_closure_package.py` | line 59 | `CORPUS_SIGNAL_RE` | ACCEPT |
| Closed-equivalent scans first 80 lines for CLOSED_PASS | `governance/compat/check_closure_packaging_preflight.py` | `_is_closed_equivalent` | `CLOSED_PASS` substring | ACCEPT |
| Foundation markers are bare words refactor/split/relocate | `governance/compat/check_foundation_storage_layout.py` | lines 34, 46 | `FOUNDATION_WORK_MARKERS`; `FOUNDATION_ACTION_MARKERS` | ACCEPT |
| Rescan applicability is bare-keyword | `governance/compat/check_rescan_intelligence_hardening.py` | line 77 | `APPLICABILITY_PATTERNS` | ACCEPT |
| Reusable fence/placeholder helpers exist | `governance/compat/check_central_facts_reference.py` | lines 181, 193 | `_is_in_code_fence`; `_is_placeholder` | ACCEPT |
| Machine-closure candidate does no fence stripping | `governance/compat/check_machine_closure_package.py` | no fence/inline-code guard present | absence of `_is_in_code_fence` | ACCEPT |
| Foundation candidate does no fence stripping | `governance/compat/check_foundation_storage_layout.py` | no fence/inline-code guard present | absence of `_is_in_code_fence` | ACCEPT |
| Rescan candidate does no fence stripping | `governance/compat/check_rescan_intelligence_hardening.py` | no fence/inline-code guard present | absence of `_is_in_code_fence` | ACCEPT |

## Findings / Position

| ID | Finding | Evidence | Disposition |
|---|---|---|---|
| F-CGFP-001 | Bare-keyword applicability matches incidental words in cited filenames, template row labels, claim-boundary prose, and N/A declaration lines. | PRFC-T1 packet matched on "refactor" (filename), "Lane split"/"readiness" (template rows), "CLOSED_PASS_BOUNDED" (describing another tranche), "rescan"/"corpus"/"knowledge absorption" (N/A checklist lines). | MACHINE_GATE_GAP |
| F-CGFP-002 | The N/A escape spirals: adding an N/A block to satisfy one gate introduces new trigger words for another. | Adding a rescan N/A block re-triggered the rescan gate via its own heading and `NOT_APPLICABLE_WITH_REASON` token. | MACHINE_GATE_GAP |
| F-CGFP-003 | This is a repeat of recorded lessons B2 and B15; the rule exists but the gates still mis-fire, so the control must move from written rule to checker logic. | Claude memory B2 ("trigger words in N/A prose block machine-closure"); B15 ("literal role-mode tokens false-trigger"). | RULE_GAP_PROMOTE_TO_MACHINE |

Position: the finding is real, repeating, and worker-blameless. The correct
control is to make the four checkers context-aware before keyword matching.

## Risk / Corrective Action

Risk: authors waste rounds rewording boilerplate, and may weaken legitimate
prose merely to dodge a keyword. Worse, a real future violation could be hidden
by an author who has learned to strip all trigger words reflexively.

Corrective action: open the CGFP hardening lane. CGFP-T1 makes the four
checkers ignore trigger keywords that appear only inside code fences, inline
code spans, cited file paths, or recognized template/N-A declaration lines,
reusing the existing fence/placeholder helpers. Each checker keeps a focused
test proving the false positive is gone and a true positive still fires.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `MACHINE_GATE_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `MACHINE_CHECK_CANDIDATE` |
| Next control action | CGFP-T1 checker trigger-context hardening (fresh GC-018 + work order) |
| Worker blame | `N/A_WITH_REASON`: bare-keyword applicability is a checker design gap, not a worker error |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Claude (finding author under operator instruction) |
| Provider or surface | Claude Code VSCode extension |
| Session or invocation | 2026-06-17 CGFP-T1 finding authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read, Grep, Bash (git) |
| Target paths | this finding record |
| Allowed scope source | operator instruction 2026-06-17 to open the checker-hardening lane |
| Before status evidence | clean worktree at `833501a6` (git status --short empty) |
| After status evidence | finding recorded; pending commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | finding record only; no checker modified by this authoring |
| Claim boundary | repo-local trace only |
| Agent type | Claude |
| Invocation ID | `cgfp-t1-finding-authoring-2026-06-17` |
| Expected manifest | `docs/reviews/CVF_CGFP_T1_CHECKER_TRIGGER_FALSE_POSITIVE_FINDING_2026-06-17.md`; `docs/baselines/CVF_GC018_CGFP_T1_CHECKER_TRIGGER_CONTEXT_HARDENING_2026-06-17.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CGFP_T1_CHECKER_TRIGGER_CONTEXT_HARDENING_FOR_CLAUDE_2026-06-17.md`; `AGENT_HANDOFF_V19_2026-06-15.md` |
| Actual changed set | `docs/reviews/CVF_CGFP_T1_CHECKER_TRIGGER_FALSE_POSITIVE_FINDING_2026-06-17.md`; `docs/baselines/CVF_GC018_CGFP_T1_CHECKER_TRIGGER_CONTEXT_HARDENING_2026-06-17.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CGFP_T1_CHECKER_TRIGGER_CONTEXT_HARDENING_FOR_CLAUDE_2026-06-17.md`; `AGENT_HANDOFF_V19_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Self-Demonstration Note

This finding artifact itself trips the very checkers it documents, because it
must quote the trigger tokens as evidence. The blocks above are added solely to
satisfy the current gates. That an honest bug report cannot pass without
dodging its own documented bug is direct corroboration of F-CGFP-001.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: this is a finding record, not a work order | no work order in this artifact | N/A with reason: finding record |
| Completion or reviewer artifact | this file | finding recorded; hardening authorized | PASS |
| Roadmap state | N/A with reason: standalone finding, no roadmap | no roadmap row | N/A with reason: no roadmap |
| Registry JSON | BLOCKED with reason: this finding records checker behavior; no GC-051 registry surface is in scope | no registry mutation | BLOCKED with reason: out of finding scope |
| Registry Markdown | BLOCKED with reason: this finding records checker behavior; no GC-051 registry surface is in scope | no registry mutation | BLOCKED with reason: out of finding scope |
| External evidence digest | N/A with reason: no external source | no external calls | N/A with reason: no external source |
| System loop interlock | N/A with reason: no loop trigger in scope | no loop scope | N/A with reason: no loop |
| Session continuity | N/A with reason: no session mutation by this finding | no session change | N/A with reason: no session mutation |

## Rescan Intelligence Hardening

- Original source artifact: N/A with reason: not a re-intake; a checker-behavior finding
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
| NEW_FINDING | checker trigger false positive | recorded | new behavior finding |
| REMOVED_OR_REJECTED | N/A | N/A | not a re-intake |

### Follow-Up Routing Matrix

| Routing lane | Item | Routed action |
| --- | --- | --- |
| DO_NOW | CGFP-T1 hardening | dispatch authorized |
| SEPARATE_RUNTIME_TRANCHE | N/A | N/A |
| STRATEGIC_OPERATOR_DECISION | N/A | N/A |
| OUT_OF_SCOPE | gate wiring | excluded |
| RESOLVED_BY_DESIGN | N/A | N/A |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| s1 | Findings | false positives are incidental-word matches | confirmed by grep evidence | could they be real scope? | PASS |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance finding. No public-sync batch is
authorized.

## Claim Boundary

This review records a finding and authorizes a hardening lane. It does not
modify any checker, change runtime behavior, or claim the false positives are
fixed. Fixes require CGFP-T1 implementation and Codex closure.
