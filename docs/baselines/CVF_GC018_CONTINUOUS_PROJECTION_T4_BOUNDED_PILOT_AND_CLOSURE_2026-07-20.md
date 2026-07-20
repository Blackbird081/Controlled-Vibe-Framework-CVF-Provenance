# CVF GC-018 Baseline - Continuous Projection T4 Bounded Pilot And Closure

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: CVF-CONTINUOUS-PROJECTION-T4

Dispatch base head: `5f5c28b85`

Dependency release commit: `e21199dfa`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer/closer: Codex reviewer/closer

Worker route: manual copy/paste only

## Purpose

Freeze the final Continuous Projection bounded-pilot contract: rerun all three
disposable-fixture proof suites, perform exactly one read-only receipt scan
against the real provenance, public-sync, and cvf-web roots, create a governed
T2 draft from that receipt, and return evidence for independent reviewer
audience assessment and roadmap closure.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-CONTINUOUS-PROJECTION-T4 --title "Continuous Projection T4 Bounded Pilot And Closure" --date 2026-07-20 --base 5f5c28b85 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "T3 closure commit e21199dfa REVIEWER_ACCEPTED_WITH_REPAIRS" --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker-return profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | Replaced generic fields with bounded pilot contract, exact roots, one-scan stop rule, measurements, and reviewer-owned audience boundary. |
| checkerReadAheadConfirmation | dispatch, scaffold, handoff, ADIF, structural, and public-disposition checkers |
| docOnlyNewFields | measurement fields are documentation-only and owned by the ledger |
| claimBoundary | GC-018 dispatch baseline only; no execution or mutation claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`continuous projection T4 bounded pilot and closure`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Target / Source

The accepted T1, T2, and T3 scripts are the execution sources. The T3 closure
at `e21199dfa` releases T4 packet authoring and records 144/144 fixture proof.
The continuous-projection roadmap requires one disposable pilot followed by
one reviewer-authorized real-root read-only scan and measurement of false
positives, missed drift, reviewer effort, and packet usefulness.

## Source / Predecessor Evidence

T3 completion commit `e21199dfa` is the dependency release. Current T1/T2/T3
scripts and the projection policy are the direct execution sources.

## Decision / Baseline / Proposed Tranche

Release one manual copy/paste no-commit T4 evidence worker under the one-scan
and no-reviewer-impersonation boundary frozen here.

## Scope / Methodology

The worker must start from clean provenance and public-sync roots. Before
creating any governed output, it reruns the three existing fixture suites.
It then invokes T1 exactly once against:

- provenance: current repository root;
- public-sync: sibling `../Controlled-Vibe-Framework-CVF-public-sync`;
- cvf-web: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`;
- policy: `scripts/cvf_projection_policy.json`.

The receipt is first written outside all three roots in a unique temporary
directory. Only after the scan exits may the worker persist the receipt and T2
draft to the Allowed evidence paths. T3 is not run on real-root evidence by
the worker because the required audience input is reviewer-owned.

## Required Artifact Manifest

Exactly four worker outputs are allowed:

1. `docs/reviews/evidence/CVF_CONTINUOUS_PROJECTION_T4_REAL_ROOT_RECEIPT_2026-07-20.json`
2. `docs/reviews/evidence/CVF_CONTINUOUS_PROJECTION_T4_REAL_ROOT_REVIEW_DRAFT_2026-07-20.json`
3. `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_LEDGER_2026-07-20.md`
4. `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_WORKER_RETURN_2026-07-20.md`

All four remain untracked and unstaged. HEAD remains unchanged.

## Frozen Sequence And Stop Conditions

1. Capture `executionBaseHead`; require it to equal the committed dispatch
   HEAD supplied in the final prompt.
2. Require both Git roots clean and verify their remotes against policy.
3. Run T1, T2, and T3 fixture proof suites once each.
4. If a fixture suite fails, stop without real-root scan.
5. Create a unique temporary directory outside every target root.
6. Run T1 once with `ScanTimeoutSeconds=3600` and a temporary receipt path.
7. On timeout, nonzero exit, dirty-root refusal, or structured error, preserve
   the diagnostic in the ledger, create no success receipt/draft artifact, and
   return `BLOCKED_WITH_REASON`.
8. On success, copy only the receipt to the first Allowed evidence path, run T2
   against it, and write T2 stdout to the second Allowed evidence path.
9. Inspect the 16 rows read-only and record provisional measurement evidence.
10. Do not create reviewer-owned audience evidence and do not run the real T3
    gate; those actions belong to the independent reviewer.

## Measurement Contract

The ledger must record:

| Metric | Worker evidence | Reviewer ownership |
|---|---|---|
| fixture stability | exact totals for all three suites | reviewer recomputes |
| false positives | each receipt row suspected incorrect, with source locator | reviewer confirms/rejects |
| missed drift | bounded manual cross-check of frozen 16 surfaces, with evidence | reviewer confirms/rejects |
| reviewer effort | worker preparation minutes and review-ready item count | reviewer records final review minutes |
| packet usefulness | concrete decisions enabled/blocked by receipt and draft | reviewer gives final disposition |
| no mutation | before/after root status and exact T1 confirmation | reviewer recomputes |

Zero suspected rows is allowed only with an explicit per-row cross-check, not
a blanket assertion. The worker must not decide semantic correctness.

## CLI/MCP And Provider Prohibition

The operator explicitly forbids CLI/MCP agent invocation until a later direct
instruction. This T4 packet authorizes manual copy/paste handoff only. The
worker must not invoke another agent, Claude CLI, Codex CLI, MCP tool, provider
API, API key, account subscription, browser, or network service. Local Git,
PowerShell, Python governance checks, and repository scripts are allowed.

## Acceptance Criteria

- Exactly three fixture suites pass before the real-root scan.
- Exactly one real-root T1 invocation occurs.
- Both roots are clean at scan start and unchanged immediately after scan.
- Receipt schema is `1.0.0`, has 16 rows, reconciliation true, empty errors,
  and the exact no-target-write confirmation.
- T2 draft is `REVIEW_REQUIRED_UNCOMMITTED` and authorizes no decision.
- Ledger contains row-level false-positive and missed-drift evidence.
- No worker-authored reviewer-owned audience evidence exists.
- No apply, copy-to-target, commit, push, provider, CLI/MCP, browser, deploy,
  or production action occurs.
- Exactly four Allowed outputs remain unstaged; worker HEAD is unchanged.

## Evidence / Verification

Evidence is the three focused-suite totals, one-scan command or diagnostic,
receipt/draft hashes, row ledger, root status/remotes, zero-call counters, and
exact final manifest. The reviewer recomputes these facts.

## Reviewer Closure Boundary

The reviewer independently recomputes root status, receipt/draft integrity,
and focused proofs; authors the reviewer-owned audience evidence; runs T3 over
the real receipt/draft/evidence triplet; measures review effort and usefulness;
repairs allowed-scope defects; and decides T4 and roadmap closure. A T3 gate
PASS proves evidence completeness, not presentation quality by itself.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch status; dependency evidence; exact Allowed manifest; source verification; handoff route; public disposition; claim boundary |
| gateRunPurpose | confirm T4 dispatch shape as pre-handoff evidence, not discover requirements |
| claimBoundary | checker compliance proves packet shape only; current scripts and T3 closure support source facts |

## Epistemic Process Block

### Expected Result / Prediction

The accepted fixture mechanisms should remain deterministic, while the single
real-root receipt should either finish with bounded review-ready evidence or
fail closed with one diagnostic and no freshness claim.

### Evidence Comparison

T0 could not finish the live recursive mapper inside its worker window. T1 now
owns a 3600-second bounded child process and timeout diagnostic. T3 closes the
complete source-boundary validation gap but deliberately leaves real audience
judgment to the reviewer.

### Contradiction Or Gap Disposition

Any timeout, dirty root, remote mismatch, malformed receipt, or missing
reviewer evidence blocks closure. It must not be converted to CURRENT or PASS.

### Claim Update

T4 may close only from one successful read-only scan plus independent reviewer
assessment. It never authorizes automatic semantic mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T4 is private provenance evidence and authorizes no public-sync write.

## Claim Boundary

This baseline authorizes one manual-worker bounded pilot and one real-root
read-only scan. It does not authorize automated agent CLI/MCP invocation,
provider/API use, reviewer impersonation, mutation, commit by the worker,
public-sync, push, deployment, production action, or unattended execution.
