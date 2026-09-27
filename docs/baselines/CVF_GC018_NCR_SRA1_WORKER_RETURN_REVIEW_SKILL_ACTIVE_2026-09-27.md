# CVF GC-018 NCR-SRA1 Worker-Return Review Skill Active Promotion

Memory class: gc-018-baseline

Status: CLOSED_PASS_BOUNDED

Date: 2026-09-27

Batch ID: NCR-SRA1

## Purpose

Promote only `cvf-governance-worker-return-review` from PROPOSED to the same
receipt-backed ACTIVE package runtime used by the existing CVF skills, after
controlled UAT, Local reviewer certification, truth-packet admission, and
package-specific dry and live proof.

## Baseline Facts

| Fact | Evidence |
| --- | --- |
| Dispatch base | `681ce92898ad26a5d318a4021f6f205dda2c3015` |
| Source state | Registry, package body, and `skill.source.json` say PROPOSED; UAT and certification not started |
| Prior source review | `docs/reviews/CVF_NCR_REVIEW_SKILL_PROPOSAL_2026-09-27.md` |
| Existing adapter | `docs/reference/agent_system_skills/CVF_ASSF_PRODUCTION_PACKAGE_RUNTIME_STANDARD.md` |

## Scope / Target / Owner Boundary

Allowed: one package source and registry entry; its new strict truth packet;
generated ASSF index, truth index, inventory, and two private CVF Web
projection read models; UAT and completion review;
this baseline and paired work order. Existing adapter source is unchanged.

Local is dispatcher, implementer, reviewer, and closer for this bounded
single-agent tranche, following the precedent in ASCP-P4-P6. The operator's
current request authorizes promotion through the existing ACTIVE procedure.
The operator still owns any new effect, data, or expense decision beyond the
existing bounded free-quota provider proof. No host/provider installation,
MCP server, automatic invocation, new resolver, public sync, or NCR roadmap
implementation is authorized here.

## Package Skill Productionization Control Block

- SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`
- Current phase: P5 through P10 for one previously PROPOSED package
- Target lifecycle state: `ACTIVE_PRODUCTION_RUNTIME`
- Prior phase evidence: `docs/reviews/CVF_NCR_REVIEW_SKILL_PROPOSAL_2026-09-27.md`
- Next forbidden skip: no status promotion before UAT, reviewer certification, truth packet, usage receipt, activation checks, adapter evidence, dry proof, and live proof
- Runtime/provider proof: package-specific production executor dry and live receipts required
- Claim boundary: bounded CVF-owned skill package runtime; no host deployment or independent agent action authority

## Evidence Requirements

| Stage | Required evidence |
| --- | --- |
| UAT | Four source-grounded scenarios covering reviewer repair, REWORK, uncloseable packet, and missing `committedEvidence`; negative routing and limitations disclosed |
| P5 | Local reviewer decision, `uatState=PASSED`, `certificationState=CERTIFIED`, internal disposition IMPLEMENTED |
| P6-P8 | Strict approved truth packet, generated index checks, explicit body-read usage receipt, resolver/projection evidence |
| P9-P10 | Package-specific dry-run and live provider receipt with safe diagnostic and source-truth trace |
| Closure | Focused guards, appropriate precommit and split-range preclosure, material and continuity commits |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| ACTIVE admission needs UAT/certification and truth | `governance/compat/check_package_skill_productionization_pipeline.py` | lifecycle snapshot | `_check_lifecycle_snapshot` | package pipeline checker | RUNTIME_BEHAVIOR | ACCEPT |
| Executor checks ACTIVE source and emits receipts | `governance/compat/run_assf_production_package_executor.py` | source | `_active_source_reasons`; `build_production_package_execution_packet` | production executor | RUNTIME_BEHAVIOR | ACCEPT |
| Truth index derives from packets | `governance/compat/check_skill_truth_packets.py` | source | `_expected_index` | SKSOT checker | RUNTIME_BEHAVIOR | ACCEPT |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private reviewer governance package and live proof stay in provenance.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_package_skill_productionization_pipeline.py`; `governance/compat/check_skill_truth_packets.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | `## Package Skill Productionization Control Block`; `## Source Verification Block`; `## Claim Boundary`; `## Public Export Disposition` |
| gateRunPurpose | Confirmation and evidence of source-reviewed scoped admission and packet structure, not first discovery |
| claimBoundary | baseline authority, not proof of ACTIVE use |

## Claim Boundary

This baseline scopes a single package promotion. Only the completion receipt
can establish the final dry/live behavior claim.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| GC-018 baseline | this file | `CLOSED_PASS_BOUNDED` | PASS |
| Work order status | paired NCR-SRA1 work order | `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | NCR-SRA1 ACTIVE completion | `ACCEPT_ACTIVE_PRODUCTION_RUNTIME_BOUNDED` | PASS |
| Roadmap state | N/A with reason: bounded skill promotion, no D013 edit | D013 remains next planned slice | N/A with reason |
| Registry JSON | one skill entry | ACTIVE, PASSED, CERTIFIED | PASS |
| Registry Markdown | package README and SKILL | ACTIVE | PASS |
| External evidence digest | ignored post-repair live receipt | SHA-256 `aabe5c2e1c6cd0643bb9b84d84a6f2b2f1776833d88147f0d5cf19aef94fc9ce` | PASS |
| System loop interlock | existing adapter gates | no new loop runtime | N/A with reason |
| Session continuity | active handoff | dedicated sync after material commit; verify in post-commit closure | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
| --- | --- | --- | --- |
| Skill | one named package | `cvf-governance-worker-return-review` | PASS |
| State | ACTIVE after UAT and certification | registry/source/truth agree | PASS |
| Runtime proof | production execution receipt and HTTP 200 | post-repair receipt `sha256:4ab934afdad0e198f21e072a114a466bef81541e0fa140bdff674f5029658ef3` | PASS |
| Action boundary | no package-granted mutation | `sourceMutations=[]` | PASS |
