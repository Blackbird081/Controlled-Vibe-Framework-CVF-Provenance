# CVF NCR Worker-Return Review Skill Proposal

Memory class: FULL_RECORD

Status: PROPOSED_PENDING_UAT

docType: review

Date: 2026-09-27

## Purpose And Authority

The operator explicitly requested a CVF review skill after the NCR R1/S01
reviewer initially proposed avoidable worker re-dispatch and after a closure
receipt omitted `committedEvidence`. Local owns this internal package proposal
and technical source reconciliation. The operator retains data, effect, and
expense decisions. No remote research or new worker assignment is involved.

This proposal adds one CVF-owned worker-return reviewer skill. The existing
`cvf-engineering-code-review-quality` package covers implementation quality;
it does not own CVF reviewer-local repair routing or closure choreography.

## Scope / Methodology

Local compared the learning record against current review-cost, closeability,
commit, and committed-evidence owners. The changed set is one PROPOSED package
body and source, one registry entry, one selection profile, two generated read
models, and this review. No existing package, checker, hook, host, or runtime
implementation is changed.

## Source Verification And Decision

| Source | Checked rule | Package treatment |
| --- | --- | --- |
| `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | reviewer-local repair default, REWORK boundary, consume valid returned evidence | route findings before re-dispatch; avoid duplicate reruns |
| `docs/reference/CVF_GATE_TO_ROLE_CLOSEABILITY_MACHINE_STANDARD.md` | uncloseable return cannot be handed back unchanged | stop and select reviewer repair, amendment, or operator route |
| `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | material and continuity roles have distinct commit ordering | guide bounded closure only under current authority |
| `docs/reference/review_cost_control/CVF_COMMITTED_EVIDENCE_FINGERPRINT_CONTRACT.md` | committed evidence is a distinct binding with guarded checkout equivalence | inspect receipt binding directly |
| `docs/reviews/CVF_CVF_NCR_R1_S01_SKILL_LIFECYCLE_BODY_COMPLETION_2026-09-27.md` | original avoidable re-dispatch was a reviewer packet gap | source of the learning signal, not new authority |
| `docs/reviews/CVF_MIXED_EOL_COMMITTED_EVIDENCE_CORRECTION_2026-09-27.md` | mixed CRLF/LF checkout caused absent binding before helper correction | avoid treating gate exit alone as receipt proof |

The package body points to current canonical owners instead of copying their
schemas or claiming a rule change. Source is CVF-owned; no third-party skill
material or license is imported.

## Findings / Position

The missing behavior was reviewer routing, not code-quality analysis. A
dedicated reviewer skill gives agents the canonical pre-review and closure
route, while the existing REWORK machine gate remains the stronger check.
The source and metadata are coherent at PROPOSED state; behavior and invocation
are not yet evidenced.

## Risk / Corrective Action

The main risk is treating a discoverable proposal as an ACTIVE package. The
registry, source, and generated inventory therefore keep runtime eligibility
denied. A later UAT must test at least a localized reviewer repair, a true
worker-return boundary, an uncloseable packet, and a receipt with missing
`committedEvidence` before any approval or activation claim.

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: P4 proposed package-root authoring following source-backed
learning and metadata registration.

Target lifecycle state: `PROPOSED` in body, source, and registry;
`AWAITING_REVIEW`, `NOT_STARTED` UAT and certification.

Prior phase evidence: R1/S01 completion and mixed-EOL correction reviews;
the source-verification table above; registry and generated metadata index.

Next forbidden skip: no `APPROVED` or `ACTIVE` promotion without governed UAT,
reviewer decision, certification, truth and usage receipts, adapter proof, and
applicable runtime gates.

Runtime/provider proof: not run; no package body was loaded through the ACTIVE
executor, provider called, or host surface changed.

Claim boundary: a source-backed, discoverable proposal only. Deterministic
selection metadata does not authorize package invocation or prove behavior.

## Verification

The `skill-creator` syntax validator accepted the body. ASSF package anatomy,
index drift, certified metadata admission, and Skill Control Plane inventory
checks passed after regenerating the two derived indexes. A deterministic
selection probe ranked this skill first for worker-return review and marked its
runtime activation `DENIED_NOT_RUNTIME_ELIGIBLE`. These checks establish
structural consistency and honest lifecycle status; behavioral UAT is pending.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_package_skill_productionization_pipeline.py`; `governance/compat/check_assf_package_candidate_anatomy.py`; `governance/compat/generate_assf_skill_index.py`; `governance/compat/generate_skill_control_plane_inventory.py` |
| literalTokensReviewed | `## Package Skill Productionization Control Block`; `SOP source:`; `Current phase:`; `Target lifecycle state:`; `Prior phase evidence:`; `Next forbidden skip:`; `Runtime/provider proof:`; `Claim boundary:` |
| gateRunPurpose | Confirm source-reviewed package proposal, generated metadata alignment, and no false ACTIVE claim; gate results are evidence after source inspection |
| claimBoundary | Checker structure does not establish reviewer behavior or provider use |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
| --- | --- | --- | --- | --- |
| Reviewer did not proactively apply local-repair rule | ORCHESTRATOR_PACKET_GAP | COST_ECONOMICS_LEARNING | RULE_EXISTS | The REWORK gate already enforces the declared route; test this proposed skill against realistic review cases before promotion |
| Receipt gate result was mistaken for full binding | EVIDENCE_INTERPRETATION_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Check the actual receipt field in future closure reviews |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Local reviewer and package author |
| Provider or surface | private CVF workspace |
| Session or invocation | NCR reviewer skill proposal 2026-09-27 |
| Working directory | repository root |
| Command or tool surface | source reads, `apply_patch`, local generators and checkers |
| Target paths | proposed package body and source, registry entry, selection profile, two generated read models, this review |
| Allowed scope source | operator request to create the CVF review skill after the R1/S01 learning |
| Before status evidence | clean HEAD `5ec1f7f76` |
| After status evidence | proposed package and metadata pending material commit |
| Diff evidence | `git diff --name-status`; `git diff --check` |
| Approval boundary | source proposal only; lifecycle promotion remains separately governed |
| Claim boundary | no ACTIVE runtime, host, provider/live, public, or production claim |
| Agent type | INTERNAL_AGENT Local reviewer/author |
| Invocation ID | `cvf-ncr-worker-return-review-skill-proposal-20260927` |
| Expected manifest | package `SKILL.md`; `skill.source.json`; registry entry; selection profile; generated index; generated inventory; this review |
| Actual changed set | package `SKILL.md`; `skill.source.json`; registry entry; selection profile; generated index; generated inventory; this review |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Epistemic Process Block

Expected result: a source-backed package proposal appears in deterministic
selection while runtime remains denied. Observed: structural checks passed and
the selection probe reported `DENIED_NOT_RUNTIME_ELIGIBLE`. Behavioral reviewer
UAT and invocation evidence remain untested.

## Claim Boundary

The authored skill does not guarantee that every agent will call it or obey it.
The existing REWORK gate remains the enforceable packet check. No external
network or provider invocation was needed; cost and quota impact are N/A.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private CVF review and skill-source evidence; no public sync is in scope.
