# CVF GC-018 - RS2 Rescan Intelligence Hardening Foundation

Memory class: governed baseline
Status: CLOSED_PASS_BOUNDED
Date: 2026-06-05
Owner: Codex / CVF Governance
Base head: 35c468b5

## Purpose

Authorize and record a bounded CVF foundation upgrade for rescan intelligence:
future rescan/intake outputs must carry original-intake delta reconciliation,
follow-up routing, and adversarial semantic sampling before closure.

This baseline is guard/foundation work only. It does not alter Claude's active
ERH-DUR1 runtime implementation files.

## Decision

Decision: approve the RS2 scan-layer foundation as a bounded governance-control
upgrade and wire it into machine gates.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Original external-review intake has predecessor finding ledger | `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md` | `## Findings Ledger`, lines 57-71 | `ERH-F1` through `ERH-F11` | external-review intake artifact | ACCEPT |
| RS1 full rescan has all 17 finding dispositions | `docs/assessments/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md` | `## Finding Disposition Ledger`, lines 124-147 | `RS-01` through `RS-17` | ERH-RS1 rescan assessment | ACCEPT |
| RS1 surfaced new RS-14 through RS-17 findings | `docs/assessments/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md` | lines 144-147 | `RS-14`, `RS-15`, `RS-16`, `RS-17` | ERH-RS1 finding ledger | ACCEPT |
| RS1 sampled source sections include section 7 and section 10 coverage | `docs/assessments/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md` | lines 114 and 117 | section coverage ledger rows | ERH-RS1 section ledger | ACCEPT |
| RS1 workflow candidates include durable evidence, policy snapshot, and distributed rate limiter | `docs/assessments/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md` | lines 244-254 | `Workflow Chain Candidates` | ERH-RS1 workflow routing | ACCEPT |
| DUR1 is dispatched, not reviewed closed | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | row `ERH-DUR1` | `DISPATCH_READY` | ERH roadmap | ACCEPT |
| New machine guard path exists in this batch | `governance/compat/check_rescan_intelligence_hardening.py` | function definition | `main` | governance compat checker | ACCEPT |

## Verification Evidence

| Evidence | Result |
| --- | --- |
| Checker tests | PASS - `python -m pytest governance/compat/test_check_rescan_intelligence_hardening.py` |
| RS2 checker | PASS - `python governance/compat/check_rescan_intelligence_hardening.py --base 35c468b5 --head HEAD --enforce` |
| Public export disposition gate | PASS - private-only disposition accepted |

## Rescan Intelligence Hardening

- Original source artifact: `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_SOURCE_2026-06-03.docx`
- Predecessor intake artifact: `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md`
- Delta ledger status: COMPLETE - baseline authorizes the standard and pilot addendum.
- Routing matrix status: COMPLETE - required lanes are standardized and piloted.
- Semantic sampling status: COMPLETE - required sampling fields are standardized and piloted.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Current | Prior | Delta category | Basis |
| --- | --- | --- | --- |
| RS-11 next-auth beta | ERH-F9 | UNCHANGED_FROM_INTAKE | Accepted bounded residual remains. |
| RS-03 safety layer | ERH-F6 | CHANGED_DISPOSITION | Moved from claim calibration into SAF workflow-chain hardening. |
| RS-14 through RS-17 | N/A | NEW_FINDING | Found only in RS1 full rescan. |
| Broad ERH-F2 wording | ERH-F2 | REMOVED_OR_REJECTED | Replaced by narrower durable-evidence and policy-snapshot routing. |

### Follow-Up Routing Matrix

| Lane | Standardized use |
| --- | --- |
| DO_NOW | Work with enough source foundation and active operator authorization. |
| SEPARATE_RUNTIME_TRANCHE | Real runtime gap that needs its own design, proof, or dependency boundary. |
| STRATEGIC_OPERATOR_DECISION | Public, adoption, validation, documentation strategy, or operator policy choice. |
| OUT_OF_SCOPE | Not technical hardening for the current roadmap. |
| RESOLVED_BY_DESIGN | Already covered by source-verified design or repository boundary. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| RS2-GC018-SAMPLE-01 | section 4.4 | Architecture weaknesses require different routes. | Addendum routing matrix. | Could one workflow-chain tranche hide remaining architecture gaps? | PASS_WITH_FOLLOWUP |
| RS2-GC018-SAMPLE-02 | section 7 | Benchmark weakness must not become public superiority claim. | RS-12 and RS-16. | Could public docs overclaim after hardening? | PASS |
| RS2-GC018-SAMPLE-03 | section 10 | Recommendations mix technical and strategic concerns. | RS-14 through RS-17. | Could operator decisions become false worker tasks? | PASS |

## Allowed Scope

- Create the RS2 rescan intelligence hardening standard.
- Create a range-aware machine checker and focused tests.
- Wire the checker into agent autorun and local hook chains.
- Create a pilot addendum applying the standard to the external review rescan.
- Create a completion review for this foundation tranche.

## Out Of Scope

- Editing Claude's active DUR1 runtime files.
- Closing DUR1.
- Public-sync changes.
- Live provider proof.
- Production durability, Redis, database, license, or external validation work.

## Claim Boundary

This baseline authorizes scan-layer control-plane hardening only. It does not
claim completion of DUR1, production runtime behavior, live provider behavior,
or public repository readiness.

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: this is a private provenance control-plane foundation. Public-sync is
not opened in this batch.

## Finding-To-Governance Learning Disposition

- Defect class: `MACHINE_GATE_GAP` - rescan completeness can pass while delta/routing/semantic interpretation remains under-specified.
- Learning lane: `GOVERNANCE_CONTROL_PLANE`.
- Escalation state: `MACHINE_CHECK_ADDED`.
- Next control action: add and enforce `governance/compat/check_rescan_intelligence_hardening.py`.
