# CVF GCLH-T1 Integrated Core Control Design

Memory class: governed-assessment

Status: REVIEWER_ACCEPTED_DESIGN_BOUNDED

docType: assessment

Date: 2026-09-01

Batch ID: GCLH-T1

Risk: R2

## Purpose

Define the smallest Core design that prevents phase-authorized work from
advancing on weak evidence across `INTAKE -> DESIGN -> SPEC -> WORK ORDER ->
BUILD -> REVIEW -> FREEZE`, without adding a new phase or a parallel repair-stop
owner.

## Source / Predecessor Evidence

- GCLH-T0 roadmap and accepted intake/review at material commit `0a4655cf`;
- SCEC standard as convergence and escalation owner;
- Review Cost standard as repair-round economics owner;
- governed work-order template as dispatch and frozen-scope owner;
- GLP roadmap as downstream projection owner;
- text encoding discipline as encoding owner.

## Governing Premise

Role switching is not control-loss. Review validity comes from the evidence
operation performed at the role boundary. A same-agent reviewer is valid when
the transition is disclosed and the reviewer reconstructs evidence from
governed sources, recomputes identity, tests frozen criteria, and does not use
the author conclusion or memory as proof. Such a review must not be labeled
independent multi-agent review.

## Decision / Baseline / Proposed Tranche

Decision: adopt this integrated evidence-envelope design as the bounded T2
basis. Current SCEC, Review Cost, work-order, encoding, and GLP owners remain
the baseline. The proposed tranche is additive owner enrichment and hostile
tests only, with no new lifecycle phase or parallel stop framework.

## Integrated Control Model

The seven phases remain unchanged. Each transition carries a typed evidence
envelope; SCEC and Review Cost consume the envelope when findings or repairs
occur.

| Transition | Required evidence | Fail-closed result |
|---|---|---|
| INTAKE -> DESIGN | capability facts, unknowns, negative feasibility probes, named authority/source | `HOLD_CAPABILITY_EVIDENCE` |
| DESIGN -> SPEC | semantic adversarial cases, invariant/constraint projection, unresolved contradictions | `HOLD_SEMANTIC_READINESS` |
| SPEC -> WORK ORDER | frozen acceptance criteria, exact manifest, parent-constraint digest | `HOLD_SPEC_BINDING` |
| WORK ORDER -> BUILD | authority, dependencies, rollback boundary, executable negative tests | `HOLD_DISPATCH_READINESS` |
| BUILD -> REVIEW | actual changed set, constraint-drift comparison, test/receipt evidence | `RETURN_EVIDENCE_INCOMPLETE` |
| REVIEW -> FREEZE | reviewer evidence reconstruction, findings/waivers, convergence/cost disposition | `BLOCK_FREEZE` |
| Core closure -> downstream adoption | projection-freshness receipt | `BLOCKED_PROJECTION_DRIFT` |

These results are readiness outcomes, not new lifecycle phases.

## Contract A: Capability Evidence

Required fields for elevated-risk design/spec work:

| Field | Meaning |
|---|---|
| `capabilityClaimId` | stable claim identity |
| `requiredCapability` | behavior needed for the proposed design |
| `authoritativeSource` | governed source or explicit external-evidence class |
| `positiveEvidence` | executable or inspectable support |
| `negativeProbe` | boundary/adversarial case and observed result |
| `unknowns` | unresolved facts; empty only with evidence |
| `disposition` | `SUPPORTED`, `BOUNDED`, or `UNSUPPORTED` |

Documentation assertions alone cannot produce `SUPPORTED` when executable
feasibility is available and material to the design.

## Contract B: Semantic Readiness And Parent Constraints

Before formal review, the author/orchestrator supplies named semantic-negative
cases. Before BUILD, immutable parent constraints are projected into a stable
ledger:

| Field | Meaning |
|---|---|
| `constraintId` | stable parent invariant identity |
| `sourcePath` and `locator` | governed origin |
| `expectedMeaning` | bounded semantic obligation |
| `allowedChange` | explicit variation boundary |
| `projectionDigest` | digest of canonical serialized projection |
| `repairDisposition` | unchanged, authorized change, or violation |

Every repair compares the new projection with the frozen parent projection.
An undeclared change is a new blocking finding even if the immediate failing
test passes. SCEC owns stable problem identity/escalation; Review Cost owns
aggregate rounds and cost. New finding labels never reset either counter.

## Contract C: Hash Identity Receipt

Every exact-hash claim names its byte domain. Allowed initial vocabulary:

- `FILESYSTEM_BYTES`: exact bytes read from the selected file;
- `UTF8_LF_NORMALIZED`: decode as UTF-8, normalize CRLF and CR to LF, then hash
  the resulting UTF-8 bytes.

The receipt binds `algorithm`, `byteDomain`, `normalizationRecipe`, `path`,
`digest`, and failure behavior. Bare `raw hash` is non-canonical. A digest from
one domain cannot prove equality in another domain. Decode failure, an unnamed
domain, or an unrecognized recipe fails closed.

## Contract D: Downstream Projection Freshness

Before a downstream profile may claim adoption of a Core control, one receipt
must bind:

| Field | Meaning |
|---|---|
| `coreControlId` | canonical control identity |
| `coreAuthorityPath` and `coreAuthorityDigest` | exact accepted Core source |
| `coreClosureCommit` | reviewed closure anchor |
| `projectionPath` and `projectionDigest` | consumed downstream carrier |
| `projectionGeneratorOrMethod` | reproducible projection method |
| `generatedFromDigest` | Core digest actually projected |
| `freshnessResult` | `CURRENT`, `STALE`, or `UNPROVEN` |

Only exact digest equality plus an accepted projection route yields `CURRENT`.
`STALE` and `UNPROVEN` block adoption but do not rewrite downstream evidence.

## Incident Replay

| Observed incident behavior | Earliest designed control | Existing owner composed | Expected effect |
|---|---|---|---|
| formal review first exposed semantic defects | DESIGN -> SPEC semantic negatives | work-order self-proof + Review Cost | discovery moves left; reviewer still reconstructs evidence |
| repairs changed parent interface | parent-constraint digest and drift comparison | work-order scope + SCEC identity | undeclared repair drift blocks before another narrow successor |
| new labels extended the loop | stable identity plus aggregate counters | SCEC + Review Cost | labels cannot reset convergence or cost |
| LF digest called raw | named byte-domain receipt | encoding discipline | cross-checkout identity claim becomes unambiguous |
| newer Core rule absent downstream | projection-freshness receipt | GLP | adoption claim blocks on stale carrier |

The replay does not show that actor count caused the incident. It shows that
required evidence was absent, ambiguous, or not reconciled at transitions.

## Implementation Ownership

| Design element | Existing owner to enrich | T2 candidate |
|---|---|---|
| capability and semantic readiness | work-order template / dispatch quality | additive packet fields and structural guard |
| parent constraints | work-order manifest + SCEC | projection block and drift-oriented hostile fixtures |
| convergence/economics | SCEC + Review Cost | composition wording and regression tests only |
| hash byte-domain | text encoding discipline | canonical vocabulary plus focused checker where exact hashes are claimed |
| projection freshness | GLP/downstream carrier | receipt schema and adoption gate |

No new top-level repair-stop standard is designed. L5/L6 schema capability and
universal agent-progress observation remain outside T1.

## Acceptance Criteria

- all seven transitions remain intact and no eighth phase is introduced;
- every control has a fail-closed outcome and an existing owner;
- same-agent multi-role review is explicitly valid under evidence
  reconstruction and makes no independence claim;
- hash domains are reproducible and non-interchangeable;
- downstream adoption is impossible from a stale or unproven projection;
- incident replay demonstrates earlier detection without claiming guaranteed
  semantic truth;
- T2 is limited to additive existing-owner changes and hostile tests.

## Evidence / Verification

Design verification consists of owner composition, seven-transition
reconciliation, explicit fail-closed outcomes, incident replay, and reviewer
evidence reconstruction. No runtime or provider proof is required because T1
makes no runtime behavior claim.

## Epistemic Process Block

### Expected Result / Prediction

The incident can be controlled by typed transition evidence plus existing SCEC
and Review Cost composition, with only hash-domain and projection-freshness
contracts materially new.

### Evidence Comparison

The replay maps every process defect to an earlier transition and preserves the
two existing stop/economics owners. Actor count does not explain any mapping;
missing or unreconciled evidence does.

### Contradiction Or Gap Disposition

No safe automatic semantic-truth scorer or universal progress observer is
established. Those ideas remain outside the implementation contract.

### Claim Update

The design is sufficient for bounded T2 planning, not implementation authority
or downstream adoption.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Core design derived from operator-provided downstream evidence;
public-sync is not authorized.

## Claim Boundary

This is a Core process-control design only. It does not mutate standards,
templates, checkers, schemas, runtime, or downstream workspace; it performs no
provider/live, public-sync, deployment, or production action.
