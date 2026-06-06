---
title: CVF Rescan Intelligence Hardening Standard
status: canonical and machine-enforced rescan intelligence standard
date: 2026-06-05
owner: CVF Governance / External Review Hardening
guard: governance/compat/check_rescan_intelligence_hardening.py
---

# CVF Rescan Intelligence Hardening Standard

Memory class: canonical governance standard
Status: canonical and machine-enforced rescan intelligence standard

## Purpose

This standard upgrades CVF rescan work from "read the corpus again" into a
reusable intelligence workflow:

1. rescan the bounded source;
2. reconcile against the original intake;
3. route follow-up work into the right lane;
4. sample high-risk interpretations adversarially before claiming confidence.

It applies to changed active CVF assessments, audits, reviews, reports,
baselines, roadmaps, and work orders that perform or depend on a rescan,
external-review intake refresh, corpus review refresh, or comparable
source-backed reassessment.

Machine enforcement proves structure and routing discipline. It does not prove
semantic correctness for every source paragraph; semantic correctness still
requires human or independent reviewer judgment on the sampled sections.

## Scope

Applies to changed active CVF assessments, audits, reviews, reports, baselines,
and work orders that perform or depend on a rescan, external-review intake
refresh, corpus review refresh, or comparable source-backed reassessment.

## Required Evidence Block

Applicable artifacts must include this heading exactly:

`## Rescan Intelligence Hardening`

The block must include these fields:

- `Original source artifact:`
- `Predecessor intake artifact:`
- `Delta ledger status:`
- `Routing matrix status:`
- `Semantic sampling status:`
- `Rescan intelligence verdict:`

Allowed verdicts:

- `COMPLETE_WITH_DELTA_ROUTING_SAMPLE`
- `COMPLETE_WITH_DECLARED_LIMITS`
- `PARTIAL`
- `BLOCKED`
- `NOT_APPLICABLE_WITH_REASON`

`NOT_APPLICABLE_WITH_REASON` is allowed only when the artifact is not itself a
rescan/intake output and includes a concrete reason.

## Original-Intake Delta Ledger

The block must include this subsection exactly:

`### Original-Intake Delta Ledger`

The ledger must distinguish every old and new finding class using this required
vocabulary:

- `UNCHANGED_FROM_INTAKE`
- `CHANGED_DISPOSITION`
- `NEW_FINDING`
- `REMOVED_OR_REJECTED`

Each row should identify the current finding, the predecessor finding when one
exists, the new disposition, and the reason. This prevents later agents from
losing findings like newly discovered low-severity issues, or from treating
operator decisions as runtime defects.

## Follow-Up Routing Matrix

The block must include this subsection exactly:

`### Follow-Up Routing Matrix`

The matrix must use these routing lanes:

- `DO_NOW`
- `SEPARATE_RUNTIME_TRANCHE`
- `STRATEGIC_OPERATOR_DECISION`
- `OUT_OF_SCOPE`
- `RESOLVED_BY_DESIGN`

The routing matrix is required even when no immediate engineering work is
opened. Its purpose is to keep real technical gaps visible while preventing
strategic, legal, public-claim, or already-resolved issues from becoming false
worker assignments.

## Semantic Sampling / Adversarial Review

The block must include this subsection exactly:

`### Semantic Sampling / Adversarial Review`

Sampling rows must include these field names:

- `sampleId`
- `source section`
- `source claim`
- `disposition checked`
- `adversarial challenge`
- `verdict`

For high-impact external-review or corpus-rescan work, sample the riskiest
sections rather than only the easiest ones. For the 2026-06-03 external CVF
review, the seed sampling set is section 4.4, section 7, and section 10 because
those sections mix architecture claims, benchmark interpretation, and
follow-up recommendations.

## Gate Binding

The machine guard is:

`governance/compat/check_rescan_intelligence_hardening.py`

The guard must be part of the local governance hook chain and the agent autorun
workflow gate. A changed applicable artifact missing the required block,
delta categories, routing lanes, or adversarial sampling fields must remain
`DRAFT`, `PARTIAL`, `BLOCKED`, or return to orchestrator. It must not be closed
as `CLOSED_PASS`, `CLOSED_PASS_BOUNDED`, `COMPLETE_VERIFIED`, or equivalent.

## Claim Boundary

This standard enforces rescan evidence shape, delta vocabulary, routing lanes,
and sampling-field presence. It does not prove semantic correctness for every
paragraph, runtime behavior, provider behavior, public readiness, or production
readiness.

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

This is a private provenance control standard. A public-facing summary may be
exported later only after the public-sync repository contains matching
non-provenance artifacts and the public export disposition guard passes.

## Finding-To-Governance Learning Disposition

- Defect class: `MACHINE_GATE_GAP` - rescan interpretation drift and follow-up routing loss.
- Learning lane: `GOVERNANCE_CONTROL_PLANE`.
- Escalation state: `MACHINE_CHECK_ADDED`.
- Next control action: enforce the rescan intelligence block through
  `governance/compat/check_rescan_intelligence_hardening.py` in autorun and
  local hook chains.
