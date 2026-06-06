# CVF GC-018 - MKG7-T7 Memory Live Proof Decision

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-01

## Purpose

Authorize MKG7-T7: file a decision packet that answers whether the Memory plane
now affects governed route behavior enough to require a live/provider proof
tranche. If yes, draft a fresh GC-018 for the live proof. If no, record the
reasoning and close MKG7 as a local-deterministic-evidence tranche.

T7 is documentation-only unless it authorizes a live proof, in which case a
separate GC-018 must be opened by the operator.

## Scope / Target / Owner Boundary

Target owner surfaces (NEW):

- `docs/reviews/CVF_MKG7_T7_MEMORY_LIVE_PROOF_DECISION_2026-06-01.md`

Boundary: decision packet only; no runtime/source edits; no live proof executed
by T7 itself; no public-sync. Live proof (if authorized) requires a separate
GC-018 and operator approval.

## Decision

Authorize T7 as a documentation-only decision packet. Worker evaluates the T1–T6
output set and answers the live-proof question. Worker must not run any live
provider call. Leave pending and uncommitted.

## Runtime Owner Surface

| Owner surface | Source path | Disposition |
| --- | --- | --- |
| T1–T6 completion reviews | `docs/reviews/CVF_MKG7_T*_*_COMPLETION_2026-06-01.md` | ACCEPT_AS_EVIDENCE_SET |
| T1 contract | `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | ACCEPT_AS_EVIDENCE |
| Live proof script (referenced only) | `scripts/run_cvf_release_gate_bundle.py` | ACCEPT_AS_REFERENCE — not executed in T7 |

## Source / Predecessor Evidence

T7 depends on T1–T6 being complete. The decision packet must cite the T1–T6
completion reviews and state whether the Memory advisory behavior in T3 now
constitutes a governance claim requiring live proof.

Current local evidence: all MKG7 tranches are local deterministic evidence only.
The Memory advisory field added in T3 is advisory-only; it does not change
provider routing, model selection, or enforcement outcomes.

## Knowledge Absorption Blind-Spot Control Block

### Gate 1 - Source Inventory

Decision packet only. No Legacy folder absorption. `N/A with reason`.

### Gate 2 - Prior Absorption Resolution

MKG1–MKG6 closed, T1–T6 complete.

### Gate 3 - File-Level Value Extraction

Decision must answer: does any T1–T6 output constitute a live-governance claim?
Based on current scope (advisory-only T3, readiness-only T5, doc-only T1/T4/T6,
new policy helper T2), the answer is expected to be NO — but worker must verify
against the actual T3 advisory wire-in behavior before filing.

### Gate 4 - Owner-Surface Normalization

Single decision review document. No owner-surface changes.

### Gate 5 - Accept / Defer / Reject Disposition

| Candidate | Disposition | Reason |
| --- | --- | --- |
| Decision packet filing | ACCEPT_NOW | required MKG7 closure artifact |
| Executing live proof in T7 | REJECT_DIRECT — requires operator + separate GC-018 | T7 decides, does not run |
| Extending T3 behavior to enforcement | REJECT_DIRECT — requires separate GC-018 | out of MKG7 scope |

### Gate 6 - Adversarial Role Review

Risk: worker concludes "no live proof needed" without citing the T3 advisory
behavior. Required: decision must explicitly reference what T3 added and confirm
it does not affect provider routing, enforcement, or model selection.

### Gate 7 - Thin Proof And Closure Delta

Decision review citing T1–T6 completion reviews, explicit YES/NO answer with
reasoning, and (if NO) a statement that MKG7 is closed as local-deterministic
evidence. Markdown structural completeness PASS, public-export PASS.

Blind-spot verdict: CLEAR_FOR_BOUNDED_IMPLEMENTATION.

## Required Evidence

- decision review citing T1–T6 completion reviews;
- explicit YES/NO live-proof answer with reasoning referencing T3 advisory behavior;
- if NO: MKG7 closure statement;
- if YES: draft GC-018 path for operator review (do not execute live proof);
- markdown structural completeness PASS;
- public-export PASS;
- pending completion review.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

T7 authorizes a decision packet only. Does not authorize executing live proof,
modifying route behavior, opening public-sync, or closing MKG7 without the
decision packet. Any YES decision requires a fresh operator-authorized GC-018
before live proof execution.
