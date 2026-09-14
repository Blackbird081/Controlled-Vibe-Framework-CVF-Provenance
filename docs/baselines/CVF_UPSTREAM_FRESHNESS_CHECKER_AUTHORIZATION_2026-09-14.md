# Upstream Freshness Receipt Checker Authorization

docType: baseline
Memory class: FULL_RECORD
Status: AUTHORIZED
Date: 2026-09-14

## Purpose

Record the operator's request for a lightweight offline checker supporting
the newly authorized pre-audit upstream observation rule.

## Source / Predecessor Evidence

The operator requested the upstream rule for other repositories, preserving
the active QM investigation, then explicitly requested a lightweight checker.
Rule owner: `.private_reference/source_mirrors/README.md`, Mandatory Upstream
Freshness Preflight. This is local guard maintenance, not a source intake run.

## Decision / Scope

Add one receipt validator and its negative tests. Document its exact
JSON fields and required pre-dispatch invocation in the existing rule owner.
Keep the domain-funnel method's pointer to that owner. The operator subsequently
requested enforcement without reminders: call the validator from the existing
intake-routing gate for changed source-audit work orders. No catalog edits,
live calls, source acquisition, pin changes or session changes.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: additive offline receipt validation and
focused tests, as explicitly requested by the operator on 2026-09-14.

Protected paths:

- `governance/compat/check_upstream_freshness_receipt.py`
- `governance/compat/test_check_upstream_freshness_receipt.py`
- `governance/compat/check_external_knowledge_intake_routing.py`

Operator authorization: the current instruction requests a lightweight checker
for the already authorized upstream freshness rule, then identified missing
automatic enforcement. Scope includes the existing routing-gate call site.

Rollback boundary: remove these two new files and the Lightweight Receipt Check
subsection and routing-gate call site if rejected; retain the previously
authorized procedural rule.

## Verification

Run `python -m pytest governance/compat/test_check_upstream_freshness_receipt.py -q`
and `python governance/compat/run_worker_return_fast_gate.py`.
Tests cover valid current/historical records, missing/duplicate fields, wrong
types, SHA and symbolic-HEAD mismatch, stale/reversed/future timestamps,
missing delta/selection reasons and missing-file CLI exit behavior.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | Core Guard Self-Protection Authorization; Authorized guard-maintenance scope; Protected paths; Operator authorization; Rollback boundary; baseline Source, Decision and Verification headings |
| gateRunPurpose | Confirm authorization packaging and regression evidence after the first fast gate exposed the missing authorization artifact |
| claimBoundary | Offline receipt consistency enforced by existing cooperative gates; no runtime interception |

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON - this change
maintains a local checker and does not investigate upstream source contents.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - local checker maintenance only; no source inventory claim.

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON -
the source-mirror README is a CVF rule owner; no repository is acquired or
absorbed in this change.

## Claim Boundary

No source freshness observation is performed by this checker. It cannot prove
receipt authenticity or semantic delta completeness. Existing frozen QM R2
authority stays intact. This artifact authorizes local maintenance and does
not claim commit, program closure, public export or runtime readiness.

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Operator-requested freshness receipt validation | `.private_reference/source_mirrors/README.md`; `governance/compat/check_external_knowledge_intake_routing.py` | `ENRICH_EXISTING` | Routing evidence needs observation timestamps and captured symbolic HEAD validation | Invoke the offline validator from the existing routing gate without another hook process |
