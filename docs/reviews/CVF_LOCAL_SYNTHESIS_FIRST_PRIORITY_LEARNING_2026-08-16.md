# CVF Local-Synthesis-First Priority Learning

Memory class: governed-learning-review

Status: REVIEWER_ACCEPTED_PENDING_CLOSER_COMMIT

Date: 2026-08-16

## Purpose

Make local synthesized folders the first value-bearing input for mixed-origin
absorption while preserving detailed file/use-case inspection, fast mapping,
worker/reviewer separation, and targeted upstream verification.

## Target / Source

The operator clarified that these local folders were produced through prior
operator/external-agent evaluation against public CVF plus new design work.
They therefore have high prior fit but remain non-authoritative until mapped,
implemented, and independently reviewed against current CVF owners.

## Scope / Methodology

Enrich the existing mixed-origin standard, forward checker, and focused tests.
The common work-order template already routes applicable work to this standard;
do not duplicate the six controls there or introduce a parallel workflow.

## Findings / Position

The prior rule preserved value and reduced repeated probes, but did not enforce
local-first inspection, content/use-case evidence, direct work-order routing
for high-fit clusters, or distinct worker and reviewer roles. That allowed both
name/pattern false negatives and same-agent closure after machine checks.

## Risk / Corrective Action

Local-first is a priority rule, not automatic acceptance. Contradictions,
safety-sensitive behavior, unclear provenance, and weak owner fit trigger
deeper current-CVF and upstream review. Runtime and authority promotion remain
separate decisions.

## Decision / Disposition

REVIEWER_ACCEPTED_EXISTING_OWNER_HARDENING

## Verification Evidence

- Focused mixed-origin guard tests: 16/16 PASS.
- Forward mixed-origin compatibility guard: PASS, zero violations.
- Core Guard Self-Protection gate: PASS, exact two protected paths authorized.
- Public Export Disposition gate: PASS.
- Reviewer-fast governance suite: 64/64 PASS.
- `git diff --check`: PASS.
- Independent semantic review: ACCEPTED for Target A in
  `docs/reviews/CVF_LOCAL_SYNTHESIS_FIRST_LEARNING_AND_RSPB_AI_T4_INDEPENDENT_REVIEW_2026-08-16.md`;
  the reviewer independently reproduced 16/16 focused tests and 64/64 fast
  governance checks. Target B remains separately rejected pending repair.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | mixed-origin marker; efficiency control key/value lines; protected paths; public disposition |
| gateRunPurpose | confirm the operator learning is machine-enforced in the existing owner before independent semantic review |
| claimBoundary | governance-process evidence only |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| local synthesized content could be undervalued from names or broad patterns | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | require substantive file/use-case inspection and local-first priority |
| worker machine checks were treated as independent review | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_UPDATED | require work order, no-commit worker, then distinct reviewer and test rerun |

runtimeProviderCostLearningLane: N/A_WITH_REASON - this change reduces local
governance latency and makes no provider or live call.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External knowledge intake routing guard implementation |
| Chain map route | local synthesized content first -> detailed file/use-case inspection -> CVF owner mapping -> bounded work order -> no-commit worker -> independent reviewer/test -> closer |
| Matching local-view guard | `governance/compat/check_mixed_origin_derived_synthesis_absorption.py` |
| Owner surface | `docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md` |
| Disposition | ENRICH_EXISTING |
| Claim boundary | process routing only; no automatic authority or runtime activation |

## Core Guard Self-Protection Authorization

Protected paths:

- `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`
- `governance/compat/test_check_mixed_origin_derived_synthesis_absorption.py`

Operator authorization: explicit instruction on 2026-08-16 to make local
folder value the first absorption priority, inspect detailed files/use cases,
map high-fit clusters directly through work order and worker, and preserve an
independent reviewer/test step.

Authorized guard-maintenance scope: add the six local-first routing controls
to the existing mixed-origin checker and its focused regression tests.

Rollback boundary: revert this bounded five-path learning batch as one unit if
independent review rejects it.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | governance worker role |
| Provider or surface | local private provenance repository |
| Session or invocation | local-synthesis-first absorption learning, 2026-08-16 |
| Working directory | repository root |
| Command or tool surface | governed reads, apply_patch, Python tests and compatibility gates |
| Target paths | exact five-path material closure batch |
| Allowed scope source | operator instruction in current session |
| Before status evidence | clean worktree at `c8bbd24d7` |
| After status evidence | four worker paths plus independent review; focused tests 16/16 and reviewer-fast 64/64 independently reproduced; Target A accepted pending closer commit |
| Diff evidence | `git diff --name-status` and focused guard output |
| Approval boundary | standard/template/checker/test/learning record only |
| Claim boundary | no absorption implementation, runtime/provider/live, public sync, deployment, or production |
| Agent type | worker |
| Invocation ID | `local-synthesis-first-learning-20260816` |
| Expected manifest | standard; checker; checker test; this learning record; independent review |
| Actual changed set | standard; checker; checker test; this learning record; independent review |
| Manifest delta | zero; the near-limit common template was restored before closure because its existing pointer already routes to this standard |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: future mixed-origin absorption starts from the
locally synthesized design value and reaches implementable clusters sooner
without allowing filenames or machine checks to replace semantic review.

Evidence Comparison: the prior standard already established provenance reuse
and bounded cluster review; the operator identified the remaining priority and
review-separation gap during RSPB T4 closure.

Contradiction Or Gap Disposition: independent review accepted Target A and
identified two bounded non-blocking drift notes; T4 remains separately rejected
and receives no closure authority from this learning batch.

Claim Update: local-first priority and independent-review sequencing are
independently accepted for closer commit; no T4 repair or closure is implied.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance learning; no public-sync action is authorized.

## Claim Boundary

This learning does not make local content canonical, authorize direct import,
execute candidate code, prove runtime behavior, commit material changes, or
authorize public/deployment/production activity.
