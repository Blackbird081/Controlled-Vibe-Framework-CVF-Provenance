# CVF Mixed EOL Committed Evidence Correction

Memory class: FULL_RECORD

Status: REVIEWED_BOUNDED

docType: review

Date: 2026-09-27

## Purpose

Correct the incomplete receipt diagnosis in the earlier reviewer-route repair.
That material commit passed pre-commit but its pre-closure receipt omitted
`committedEvidence`. This review records the reproduced cause and the bounded
contract, implementation, and test correction.

## Target / Source

- Earlier repair: `docs/reviews/CVF_REVIEW_ROUTE_AND_RECEIPT_DIAGNOSTIC_REPAIR_2026-09-27.md`, material commit `baa40286c23e12dc900b315e837eee67e850e892`.
- Canonical contract: `docs/reference/review_cost_control/CVF_COMMITTED_EVIDENCE_FINGERPRINT_CONTRACT.md`, historical-target admission guard.
- Implementation: `governance/compat/committed_evidence_fingerprint.py`, `verify_worktree_matches_committed_target`.
- Producer and map: `governance/compat/run_agent_autorun_workflow_gate.py`; `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`.

## Scope / Methodology

The actual committed standard file had 922 CRLF pairs and 19 LF-only lines in
the worktree; the Git blob had LF only. Replacing CRLF pairs in the worktree
with LF reproduced the committed bytes exactly, and the index retained the
committed blob. `git status` was clean. The previous helper allowed only a
complete LF-to-CRLF expansion, so it wrongly rejected this mixed-line-ending
representation. Pre-closure printed `No committedEvidence binding produced`
while returning `COMPLIANT`; the earlier review's claim that CRLF alone could
not reproduce the failure is superseded by this direct evidence.

The contract now admits a narrow worktree-only CRLF-to-LF comparison when the
target blob is LF text, the index still points to the target, and checkout
metadata authorizes CRLF. Lone CR, binary/control bytes, unrecognized
transforms, and actual content drift remain rejected. The raw worktree
fingerprint and during-run stability check remain byte-sensitive. The helper
does not invoke Git clean filters or `git hash-object`.

## Findings / Position

| Finding | Evidence | Disposition |
| --- | --- | --- |
| Mixed EOL false rejection | Real material pre-closure range `608c8365513783590f09017890d2be24b7af7d97..baa40286c23e12dc900b315e837eee67e850e892` omitted the binding at the mixed-EOL standard file | Corrected the single admitted representation class; no generic text normalization |
| Earlier diagnosis incomplete | The earlier review tested uniform CRLF, not the actual mixed-EOL worktree | This record supersedes only its "no admission broadening" and unreproduced-cause claims; reviewer-route machine interlock remains valid |
| Multi-file regression | Real producer, validator and collector exercised three Markdown paths with one mixed-EOL worktree file and a clean index | Binding and reconstructed fingerprint agree |

## Risk / Corrective Action

Mixed line endings can conceal semantic edits if normalized without limits.
The admission still requires an exact normalized byte match to the committed
blob, target-index identity and metadata eligibility. Existing hostile
filter, binary, historical-target and dirty-worktree tests remain in the full
suite. No provider, runtime, host, public or production effect is claimed.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_system_chain_map_freshness.py` |
| literalTokensReviewed | `Core Guard Self-Protection Authorization`; `Protected paths`; `Authorized guard-maintenance scope`; `Operator authorization`; `Rollback boundary`; `Actual changed set`; `Public Export Disposition` |
| gateRunPurpose | Confirm the protected-path authorization, exact changed-set trace and refreshed source fingerprint after source review |
| claimBoundary | These gates validate artifact shape and source hash; focused and pre-closure tests establish the bounded behavior |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: admit only metadata-backed mixed LF/CRLF
worktree representation against an unchanged LF target blob; correct the
producer comment and real regression fixtures. No generic normalization,
filter execution, receipt schema change, or broader authority.

Protected paths:

- `governance/compat/committed_evidence_fingerprint.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/test_committed_evidence_fingerprint.py`
- `governance/compat/test_mfrp_shadow_canary_autocollect.py`

Operator authorization: the 2026-09-27 instruction to resolve the receipt
and reviewer-routing errors so they do not recur.

Rollback boundary: revert this contract/implementation/test correction as one
material batch; retain the earlier reviewer-route guard and its first review
as historical evidence.

## Verification / Evidence

- Real pre-closure before this correction: exit 0, `COMPLIANT`, but no `committedEvidence` binding; exact offending path and target blob were printed.
- `python -m unittest governance.compat.test_committed_evidence_fingerprint`: 43/43 passed after the correction.
- `python -m pytest governance/compat/test_mfrp_shadow_canary_autocollect.py -q`: 53/53 passed, including a mixed-EOL multi-file producer/validator/collector case.
- Final committed-range pre-closure and governance gate results are recorded after commit.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
| --- | --- | --- | --- | --- |
| Mixed-EOL false rejection | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | Keep narrow contract and regression at the committed-evidence owner |
| Incomplete initial diagnosis | ORCHESTRATOR_PACKET_GAP | DOCUMENTATION_ONLY_LEARNING | RULE_EXISTS | Treat pre-commit PASS without a bound pre-closure receipt as incomplete closure evidence |

Runtime/provider/cost learning lane: N/A_WITH_REASON: this correction uses
local Git and deterministic Python tests only; no provider call, quota,
runtime deployment or cost-bearing service was observed.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Local reviewer and governance maintainer |
| Provider or surface | local private CVF workspace |
| Session or invocation | post-commit mixed-EOL correction, 2026-09-27 |
| Working directory | repository root |
| Command or tool surface | direct raw-byte comparison, `git` plumbing, focused tests, `apply_patch`, local gates |
| Target paths | committed-evidence contract and helper, producer comment, system-chain map, focused tests, this review |
| Allowed scope source | operator instruction to resolve recurring receipt and reviewer errors |
| Before status evidence | clean HEAD `962250f34` after the first repair and handoff sync; its material pre-closure lacked binding |
| After status evidence | bounded correction pending material commit and pre-closure confirmation |
| Diff evidence | exact `git diff --name-status` and `git diff --check` |
| Approval boundary | local guard-maintenance correction only |
| Claim boundary | no automatic skill invocation, provider/live/public/production effect |
| Agent type | Local reviewer/closer |
| Invocation ID | `cvf-mixed-eol-committed-evidence-correction-20260927` |
| Expected manifest | `docs/reviews/CVF_MIXED_EOL_COMMITTED_EVIDENCE_CORRECTION_2026-09-27.md`; `docs/reference/review_cost_control/CVF_COMMITTED_EVIDENCE_FINGERPRINT_CONTRACT.md`; `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`; `governance/compat/committed_evidence_fingerprint.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/test_committed_evidence_fingerprint.py`; `governance/compat/test_mfrp_shadow_canary_autocollect.py` |
| Actual changed set | `docs/reviews/CVF_MIXED_EOL_COMMITTED_EVIDENCE_CORRECTION_2026-09-27.md`; `docs/reference/review_cost_control/CVF_COMMITTED_EVIDENCE_FINGERPRINT_CONTRACT.md`; `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`; `governance/compat/committed_evidence_fingerprint.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/test_committed_evidence_fingerprint.py`; `governance/compat/test_mfrp_shadow_canary_autocollect.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Epistemic Process Block

Expected result / prediction: after the correction, a clean mixed-EOL
worktree with qualifying metadata produces a committed-evidence binding;
binary, filtered, or drifted content still fails closed. Unit and chain
results above support the local behavior. Committed-range proof follows.

## Claim Boundary

The earlier re-dispatch machine interlock remains in force. This review
corrects only the mixed-EOL receipt admission and its evidence claim. It
does not prove automatic skill invocation or change the active NCR next move.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private guard correction; no public-sync authorization.
