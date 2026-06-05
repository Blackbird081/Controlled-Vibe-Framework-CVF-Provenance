# CVF ERH-RS2 Rescan Intelligence Hardening Addendum

Memory class: governed assessment
Status: CLOSED_PASS_BOUNDED
Date: 2026-06-05
Owner: Codex / CVF Governance
Scope: external-review rescan intelligence foundation pilot

## Purpose

This addendum converts the ERH-RS1 lesson into a reusable CVF scan-layer
control. ERH-RS1 proved file coverage for the external review. ERH-RS2 adds
the missing intelligence controls that future rescans must carry:

- original-intake delta reconciliation;
- follow-up routing matrix;
- adversarial semantic sampling of high-risk sections.

This is not a new runtime-hardening tranche and does not modify the DUR1 worker
files currently under Claude implementation.

## Decision

RS2 is accepted as a scan-layer foundation pilot. Future rescan/intake outputs
should follow the new standard before claiming a closed or complete rescan
result.

## Source Anchors

| Source | Anchor | Use |
| --- | --- | --- |
| `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md` | `## Findings Ledger`, rows `ERH-F1` through `ERH-F11` | predecessor intake baseline |
| `docs/assessments/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md` | `## Finding Disposition Ledger`, rows `RS-01` through `RS-17` | full rescan disposition baseline |
| `docs/assessments/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md` | `## Section 4.4 Architectural Weaknesses` | architecture sampling source |
| `docs/assessments/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md` | Section Coverage Ledger rows for section 7 and section 10 | benchmark/recommendation sampling source |
| `docs/reference/CVF_RESCAN_INTELLIGENCE_HARDENING_STANDARD_2026-06-05.md` | `## Required Evidence Block` | reusable CVF control standard |

## Verification Evidence

| Evidence | Result |
| --- | --- |
| `python -m pytest governance/compat/test_check_rescan_intelligence_hardening.py` | PASS |
| `python governance/compat/check_rescan_intelligence_hardening.py --base 35c468b5 --head HEAD --enforce` | PASS |

## Rescan Intelligence Hardening

- Original source artifact: `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_SOURCE_2026-06-03.docx`
- Predecessor intake artifact: `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md`
- Delta ledger status: COMPLETE - predecessor findings and new RS1 findings reconciled below.
- Routing matrix status: COMPLETE - all follow-up lanes explicitly assigned below.
- Semantic sampling status: COMPLETE - section 4.4, section 7, and section 10 sampled adversarially below.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Current finding | Predecessor finding | Delta category | Current disposition | Reason |
| --- | --- | --- | --- | --- |
| RS-03 safety layer too thin | ERH-F6 | CHANGED_DISPOSITION | Runtime workflow chain opened after RS1; SAF1/SAF2 now closed bounded | Intake only calibrated the public claim. RS1 showed the safety layer had enough runtime foundation to become workflow-chain work. |
| RS-10 CI lacks lint/coverage/audit hardening | ERH-F4 | CHANGED_DISPOSITION | Partially closed by CI/AUD tranches; residual lint/coverage remains separate | Original finding remains valid but no longer maps to one undifferentiated CI gap. |
| RS-11 next-auth beta | ERH-F9 | UNCHANGED_FROM_INTAKE | ACCEPT_WITH_CAVEAT | No stable v5 migration target exists; residual is API-stability risk, not immediate CVE remediation. |
| RS-12 output-quality parity not proven | ERH-F10 | UNCHANGED_FROM_INTAKE | CLOSED_BOUNDED claim boundary | CVF must keep the bounded value claim and not claim output-quality superiority. |
| RS-13 public evaluation boundary | ERH-F11 | CHANGED_DISPOSITION | Public-sync summary exported with bounded claim | Original concern was valid; public-facing guidance has been improved but remains bounded. |
| RS-14 documentation bloat/version inflation | N/A | NEW_FINDING | DOCUMENTED_OPEN | Strategic documentation cleanup concern found during full rescan; not an ERH runtime tranche. |
| RS-15 license blocks commercial use | N/A | NEW_FINDING | OUT_OF_SCOPE | Legal/license strategy is operator decision, not a technical hardening task. |
| RS-16 QBS scoring never passed and reviewer k threshold not met | ERH-F10 partial | NEW_FINDING | DOCUMENTED_OPEN | Benchmark-method gap is separate from public claim calibration and belongs to benchmark roadmap work. |
| RS-17 handoff visibility concern | N/A | NEW_FINDING | RESOLVED_BY_DESIGN | Concern came from private/provenance context; public-sync `.gitignore` and public-boundary rules cover it. |
| Broad "no durable audit" wording | ERH-F2 | REMOVED_OR_REJECTED | Split into narrower runtime findings | The broad formulation was too coarse after RS1; durable evidence, policy snapshot, signing, and backend choices must be tracked separately. |

### Follow-Up Routing Matrix

| Finding or issue | Routing lane | Action boundary |
| --- | --- | --- |
| RS-01 durable evidence and RS-04 policy snapshot reconstructability | DO_NOW | ERH-DUR1 is already dispatched to Claude as bounded local durable evidence and policy snapshot workflow. |
| RS-02 distributed rate limiting | SEPARATE_RUNTIME_TRANCHE | Requires Redis or equivalent multi-instance adapter design; not part of DUR1. |
| RS-05 provider risk ceilings hardcoded | SEPARATE_RUNTIME_TRANCHE | Convert source-verified config gap into a provider-risk-config workflow if operator prioritizes it after DUR1. |
| RS-06 evidence signing/hash-chain durability | SEPARATE_RUNTIME_TRANCHE | Separate evidence-tamper-resistance tranche after local durable evidence stabilizes. |
| RS-09 independent validator | STRATEGIC_OPERATOR_DECISION | External validation is a trust/adoption choice, not a worker-default implementation. |
| RS-14 documentation bloat/version inflation | STRATEGIC_OPERATOR_DECISION | Operator decides public catalog/readme compression strategy. |
| RS-15 license/commercial-use concern | OUT_OF_SCOPE | License policy is outside technical hardening; route only if operator opens legal/public-governance work. |
| RS-17 private handoff listing concern | RESOLVED_BY_DESIGN | No work order; public-sync exclusion and boundary rules already cover the issue. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| RS2-SAMPLE-01 | section 4.4 Architectural Weaknesses | External review lists ephemeral audit, in-memory rate limiting, thin safety, policySnapshotId, and hardcoded provider risk ceilings. | RS1 dispositions plus this addendum's routing matrix. | Could Codex handle safety and DUR1 while burying provider-risk config or distributed rate limiting? | PASS_WITH_FOLLOWUP - provider risk and distributed rate limiting are explicit `SEPARATE_RUNTIME_TRANCHE` rows. |
| RS2-SAMPLE-02 | section 7 Benchmark QBS | External review says output-quality parity is not proven and QBS/reviewer threshold did not pass. | RS-12 and RS-16. | Could the public claim calibration accidentally imply benchmark superiority after CI/public-doc work? | PASS - RS-12 keeps bounded value only; RS-16 remains separate benchmark roadmap work. |
| RS2-SAMPLE-03 | section 10 Recommendations | External review mixes development recommendations, adoption concerns, and license concern. | RS-13 through RS-17 routing. | Could legal/operator concerns become false technical work orders, or real runtime concerns become "operator only"? | PASS - license and documentation strategy are separated from runtime tranches; durable evidence and policy snapshot stay DO_NOW through DUR1. |

## Claim Boundary

RS2 proves that the CVF scan layer now has a reusable control shape for
rescan-derived intelligence. It does not prove every paragraph interpretation
is semantically perfect, does not close DUR1, does not claim production
durability, and does not replace live governance proof for runtime behavior.

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: this is private provenance scan-layer hardening. Public-facing changes
must be authored from the public-sync clone and carry separate public export
evidence.

## Finding-To-Governance Learning Disposition

- Defect class: `MACHINE_GATE_GAP` - rescan follow-up routing could lose new findings or over-route operator decisions.
- Learning lane: `GOVERNANCE_CONTROL_PLANE`; runtime terms in this artifact are routing references only, not runtime proof, so runtime-learning lane is `N/A_WITH_REASON`.
- Escalation state: `MACHINE_CHECK_ADDED`.
- Next control action: enforce `docs/reference/CVF_RESCAN_INTELLIGENCE_HARDENING_STANDARD_2026-06-05.md` and `governance/compat/check_rescan_intelligence_hardening.py` in autorun/local hook chains.
