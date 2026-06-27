# CVF CGFP-T1 Provider-Local Learning Boundary Finding

Memory class: FULL_RECORD

Status: FINDING_RECORDED_MACHINE_CHECK_COVERED

docType: finding_review

Date: 2026-06-17

Reviewer: Codex

rawMemoryReleased: false

## Purpose

Record the second CGFP-adjacent finding raised by the operator on 2026-06-17:
after PRFC-T1 packet authoring exposed a reusable checker-authoring lesson, the
worker framed the learning escalation as separate/private work instead of first
class CVF governance carry-forward. The keyword false-positive issue is already
recorded in the CGFP-T1 finding packet; this artifact records the learning
boundary issue.

## Scope / Target / Owner Boundary

Target: reusable agent-learning disposition when a worker identifies a
cross-agent governance lesson during dispatch or closure authoring. Owner
boundary: this review records the finding and classifies it against existing
CVF standards. It does not modify checker code, open runtime work, or change
the CGFP-T1 work order.

## Target / Source

Observed during PRFC-T1 and CGFP-T1 authoring at current lineage ending in
commit `35f17941`. The operator reported that Claude described the checker
trigger issue as a worthwhile governance finding but also called the escalation
"viec rieng" / separate private work. The durable CVF concern is not worker
blame; it is that reusable lessons must be routed through governed artifacts
instead of remaining provider-local or optional.

Source artifacts:

- `AGENTS.md`
- `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`
- `docs/reviews/CVF_CGFP_T1_CHECKER_TRIGGER_FALSE_POSITIVE_FINDING_2026-06-17.md`
- `docs/baselines/CVF_GC018_FPRC_T2_PROVIDER_MEMORY_LESSON_PROMOTION_HARDENING_2026-06-16.md`
- `docs/reviews/CVF_FPRC_T2_PROVIDER_MEMORY_LESSON_PROMOTION_HARDENING_COMPLETION_2026-06-16.md`

## Scope / Methodology

Codex checked the committed CGFP-T1 finding and dispatch artifacts, then
searched current governed artifacts for provider-local learning boundary
coverage. The first finding is already recorded as a machine-check hardening
candidate. The second finding is classified here as an existing-rule
application: reusable cross-agent lessons may be local execution aids during
authoring, but must be promoted or explicitly declined in a CVF-governed
artifact.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Disposition |
|---|---|---|---|---|
| Provider-specific files and memory are not CVF source authority | `AGENTS.md` | Mandatory Provider-Specific Agent Memory Boundary | `provider-specific files and memory stores` | ACCEPT |
| Reusable lessons stored in provider memory need governed promotion or explicit decline | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | Provider-memory learning boundary | `acceptable governed promotions` | ACCEPT |
| Keyword false-positive finding is already recorded | `docs/reviews/CVF_CGFP_T1_CHECKER_TRIGGER_FALSE_POSITIVE_FINDING_2026-06-17.md` | Findings / Position | `F-CGFP-001`; `F-CGFP-002`; `F-CGFP-003` | ACCEPT |
| Prior hardening already treats provider-local-only lessons as a machine-check concern | `docs/baselines/CVF_GC018_FPRC_T2_PROVIDER_MEMORY_LESSON_PROMOTION_HARDENING_2026-06-16.md` | Purpose / Acceptance Criteria | `FPRC-T2 provider-memory escape pattern`; `reusable lessons` | ACCEPT |
| Prior completion added tests for reusable provider-memory lessons | `docs/reviews/CVF_FPRC_T2_PROVIDER_MEMORY_LESSON_PROMOTION_HARDENING_COMPLETION_2026-06-16.md` | Test / Learning Disposition sections | `reusable provider-memory lessons` | ACCEPT |

## Findings / Position

| ID | Finding | Evidence | Disposition |
|---|---|---|---|
| F-CGFP-004 | Worker recognized a reusable governance lesson but initially framed escalation as separate/private work. | Operator report on 2026-06-17 plus committed CGFP-T1 packet showing the lesson is cross-agent and reusable. | MACHINE_CHECK_ADDED |
| F-CGFP-005 | The first CGFP-T1 finding record cites Claude memory B2/B15 as supporting context; that wording is useful for trace but must not become canonical source authority. | `CVF_CGFP_T1_CHECKER_TRIGGER_FALSE_POSITIVE_FINDING_2026-06-17.md` row F-CGFP-003 names Claude memory B2/B15. | MACHINE_CHECK_ADDED_WITH_SOURCE_BOUNDARY |

Position: no additional checker lane is required solely for this second
finding because FPRC-T2 already added machine-check coverage for the
provider-memory escape pattern.
However, this occurrence is now recorded as governed evidence so it does not
remain a provider-local lesson.

## Risk / Corrective Action

Risk: if workers can label reusable governance findings as private work, future
agents will again depend on provider-local recall and the operator will need to
ask whether the lesson was promoted.

Corrective action: carry this finding as a governed review record. Future Codex
review of CGFP-T1 must treat provider-memory references as trace context only,
not source authority. If the pattern repeats after this record, open a small
checker/template hardening lane to flag "private work" framing near reusable
learning claims.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `RULE_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `MACHINE_CHECK_ADDED` |
| Next control action | Preserve this governed finding and rely on the existing FPRC-T2 finding-to-governance checker coverage; open a new lane only if the pattern repeats after that coverage |
| Worker blame | `N/A_WITH_REASON`: this is a control-boundary learning signal, not a worker blame packet |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex CLI |
| Session or invocation | 2026-06-17 provider-local learning boundary finding record |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, git, rg, Select-String |
| Target paths | this finding record only; handoff sync for prior CGFP-T1 dispatch is recorded in the separate preceding commit `2210bef6` |
| Allowed scope source | operator instruction 2026-06-17: "Ghi nhan 2 finding do" |
| Before status evidence | clean worktree at `35f17941` |
| After status evidence | this finding record added; active handoff repaired to prior CGFP-T1 dispatch commit before this commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | finding record plus handoff HEAD sync only; no checker or runtime mutation |
| Claim boundary | repo-local governance evidence only |
| Agent type | Codex |
| Invocation ID | `cgfp-t1-provider-local-learning-boundary-finding-2026-06-17` |
| Expected manifest | `docs/reviews/CVF_CGFP_T1_PROVIDER_LOCAL_LEARNING_BOUNDARY_FINDING_2026-06-17.md` |
| Actual changed set | `docs/reviews/CVF_CGFP_T1_PROVIDER_LOCAL_LEARNING_BOUNDARY_FINDING_2026-06-17.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: this is a finding record, not a work order | no work order in this artifact | N/A with reason: finding record |
| Completion or reviewer artifact | this file | finding recorded | PASS |
| Roadmap state | N/A with reason: standalone finding, no roadmap row | no roadmap row | N/A with reason: no roadmap |
| Registry JSON | N/A with reason: no registry mutation in scope | no registry mutation | N/A with reason |
| Registry Markdown | N/A with reason: no registry mutation in scope | no registry mutation | N/A with reason |
| External evidence digest | N/A with reason: no external source | no external calls | N/A with reason |
| System loop interlock | N/A with reason: no loop or interlock mutation | no loop mutation | N/A with reason |
| Session continuity | N/A with reason: no mode or next-move change | no session mutation | N/A with reason |

## Rescan Intelligence Hardening

- Original source artifact: N/A with reason: not a re-intake; a governance finding record
- Predecessor intake artifact: N/A with reason: none
- Delta ledger status: N/A with reason
- Routing matrix status: N/A with reason
- Semantic sampling status: N/A with reason
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Category | Item | Disposition | Reason |
|---|---|---|---|
| UNCHANGED_FROM_INTAKE | N/A | N/A | not a re-intake |
| CHANGED_DISPOSITION | N/A | N/A | not a re-intake |
| NEW_FINDING | provider-local learning boundary framing | recorded | new occurrence of existing rule boundary |
| REMOVED_OR_REJECTED | N/A | N/A | not a re-intake |

### Follow-Up Routing Matrix

| Routing lane | Item | Routed action |
|---|---|---|
| DO_NOW | governed finding record | this artifact |
| SEPARATE_RUNTIME_TRANCHE | N/A | N/A |
| STRATEGIC_OPERATOR_DECISION | N/A | N/A |
| OUT_OF_SCOPE | checker implementation | excluded |
| RESOLVED_BY_DESIGN | provider-memory escape guard exists | FPRC-T2 |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| s1 | Findings | existing provider-memory boundary rule covers the behavior | compared to FPRC-T2 and AGENTS.md | should this open a new checker now? | PASS_BOUNDARY |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance finding. No public-sync batch is
authorized.

## Claim Boundary

This review records the provider-local learning boundary finding. It does not
modify any checker, change runtime behavior, open public-sync, or claim CGFP-T1
implementation is complete.
