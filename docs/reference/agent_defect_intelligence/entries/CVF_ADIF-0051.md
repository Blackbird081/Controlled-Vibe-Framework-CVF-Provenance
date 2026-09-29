# ADIF-0051 - Byte-Exact Archive Scope Omits Dependent Guard Reconciliation

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0051
title: Byte-exact archive scope omits dependent guard reconciliation
defectCategory: SCOPE_AND_OWNERSHIP
defectClass: MACHINE_GATE_GAP
defectRole: dispatcher
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Work-order authoring / dispatch; Worker execution (WORKER_MUST_NOT_COMMIT); Reviewer-return review; Closure
roles: dispatcher; worker; reviewer; closer
lifecyclePhases: pre-dispatch; pre-implementation; pre-closure
surfaceSelectors: byte-exact governed archives, exact changed-set contracts, naming and encoding guards, source-fingerprint maps
detectionSignals: a work order mandates raw byte preservation or an exact nonstandard filename but omits the guard exception and dependent fingerprint-refresh paths needed for its own positive gate
enforcementLevel: PARTIAL_CHECK
checkerBindings: governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_docs_governance_compat.py; governance/compat/check_system_chain_map_freshness.py
promotionState: MACHINE_CHECK_ADDED
supersedes: NONE
lastVerifiedCommit: bc5be598e
roadmapSeedId: NONE
```

## Purpose

Prevent an exact-scope dispatch from requiring byte-identical evidence or an
exact filename while excluding the compatibility and fingerprint surfaces
that its own required gates must update.

## Scope / Applies To

Applies to work orders that create raw preimage archives, preserve historical
bytes that predate current encoding rules, require nonstandard governed
filenames, or edit a source tracked by a governed fingerprint map.

## Bad Example

Require a byte-for-byte archive with a pinned hash and an exact filename, but
authorize only the archive path. The worker then reaches closure with correct
bytes while encoding, naming, or source-freshness gates require forbidden-path
repairs.

## Good Example

Before dispatch, run the positive changed-set gate against a representative
archive. Source-read every applicable naming, encoding, and fingerprint
checker. Include exact compatibility exceptions, focused negative tests, and
dependent fingerprint refresh paths in the authorized manifest when needed.

## Canonical Sources

- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`, source
  verification and checker read-ahead requirements.
- `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`,
  encoding exception discipline.
- `docs/reference/system_chain/CVF_SYSTEM_CHAIN_FRESHNESS_STANDARD.md`, fresh
  human review requirement for source fingerprint refresh.
- `governance/compat/check_agent_packet_authority_and_encoding.py`.
- `governance/compat/check_docs_governance_compat.py`.
- `governance/compat/check_system_chain_map_freshness.py`.

## Remediation

Reconcile the proposed positive output against every applicable guard before
freezing the exact manifest. Prefer exact path exceptions with negative
regression tests over broad archive-directory exemptions. When an authorized
source edit invalidates a governed fingerprint, assign the map path to the
reviewer and require a fresh semantic confirmation of the affected chain.

## Epistemic Process Block

### Expected Result / Prediction

A source-verified exact scope should contain every path required for its own
positive closure gates.

### Evidence Comparison

ACRC-T2B produced all three pinned archives byte-for-byte and satisfied its
exact-15 contract, but reviewer-fast rejected the historical non-ASCII bytes,
two mandated filenames, and the intentionally changed documentation workflow
fingerprint. All required repairs were outside exact-15.

### Contradiction Or Gap Disposition

The worker output was correct under the dispatch contract, while the dispatch
contract was incomplete relative to already-binding guards. The reviewer used
fresh delegated authority for exact-path exceptions, focused negative tests,
and a bounded source-fingerprint refresh.

### Claim Update

Source-verifying output content is insufficient when the same output creates
new naming, encoding, or fingerprint obligations. Positive gate compatibility
must be source-verified before the exact changed set is frozen.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | independent reviewer/closer |
| Provider or surface | local private provenance workspace |
| Session or invocation | ACRC-T2B independent closure, 2026-08-11 |
| Working directory | repository root |
| Command or tool surface | checker source reads, focused pytest, reviewer-fast, Git diff inspection, and apply_patch |
| Target paths | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0051.md`; entries README row; exact-path guard repairs |
| Allowed scope source | mandatory ADIF learning capture and operator-delegated reviewer closure authority |
| Before status evidence | correct exact-15 output was blocked by three dependent guard obligations omitted from dispatch scope |
| After status evidence | reusable pattern is resolver-discoverable and the exact T2B paths have narrow machine-checked exceptions |
| Diff evidence | ACRC-T2B 24-path material closure changed set and focused negative tests |
| Approval boundary | governance learning and exact T2B compatibility repair only; no live, provider, runtime, public, deploy, push, or downstream mutation action |
| Claim boundary | partial checking for the exact T2B paths; no generalized dispatch-scope completeness claim |
| Agent type | reviewer/closer |
| Invocation ID | `active-continuity-t2b-adif-0051-20260811` |
| Expected manifest | ADIF-0051; entries README row; T2B reviewer-owned compatibility repairs |
| Actual changed set | ADIF-0051; entries README row; T2B reviewer-owned compatibility repairs |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance learning. No public-sync action is
authorized.

## Claim Boundary

This entry records one reusable dispatch-scope defect and its bounded T2B
repair. It does not prove generalized prevention, authorize broad archive
exceptions, or claim runtime, provider, external-agent, public, deployment,
or production behavior.
