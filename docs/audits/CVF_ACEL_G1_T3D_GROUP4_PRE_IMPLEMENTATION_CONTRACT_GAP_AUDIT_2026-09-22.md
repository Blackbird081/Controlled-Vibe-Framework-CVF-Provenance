# CVF ACEL G1 T3D Group 4 Pre-Implementation Contract Gap Audit

Memory class: governed-audit

docType: audit

Status: REWORK_REQUIRED

Date: 2026-09-22

Batch ID: ACEL-G1-T3D-GROUP4-PRE-IMPLEMENTATION-CONTRACT-GAP

Decision base HEAD: `ed1cfa814`

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Decide whether the accepted T2E/T2F/T2H Group 4 contract is sufficiently
closed to dispatch issuer-registry and lookup-response tooling after Party C
principal verification.

## Target / Source

| Source | Authority used |
|---|---|
| `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md` | Contract 4 owner and cross-contract separation |
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 4 schema, closed preimages, lookup order, consumer binding and establishment checklist |
| `docs/reviews/CVF_ACEL_G1_T2H_PARTY_B_IMMUTABLE_OBSERVATION_RECONCILIATION_WORKER_RETURN_2026-09-18.md` | Party B immutable observation boundary and Party C separation |
| `docs/audits/CVF_ACEL_G1_T3D_PARTY_C_PRINCIPAL_LOCAL_VERIFICATION_2026-09-22.md` | concrete Party C principal is Local verified |

## Scope / Methodology

Local performed a field-to-preimage-to-writer-to-consumer reconciliation before
authoring any implementation work order. A read-only internal sub-agent mapped
candidate requirements; Local retained decision ownership and independently
checked the cited Group 4 and consumer-binding sections.

## Findings / Position

| ID | Contract gap | Why implementation cannot safely infer it | Disposition |
|---|---|---|---|
| G4-GAP-01 | `registrySnapshotHashHex` is mandatory in lookup responses, but no exact registry-envelope digest rule is declared | choosing parsed/JCS bytes versus exact published bytes changes identity and observation binding | AMEND_CONTRACT |
| G4-GAP-02 | `canonicalContentHashHex` names `issuer canonical content bytes` without declaring their exact source or byte preimage | the row stores no content bytes; hashing the full row would be circular because the digest field is itself in the row | AMEND_CONTRACT |
| G4-GAP-03 | the principal allowed to append `LOOKUP_RESPONSES.jsonl` and its DACL are unnamed | granting verifier consumers Party C registry-write authority would collapse least privilege; granting Party C sole append authority would make query evidence self-authored | AMEND_CONTRACT |
| G4-GAP-04 | T2F requires a real verifier consumer lookup for Group 4 establishment, while T3E is ordered only after T3D verification | tooling/source verification and consumer-binding completion need distinct bounded dispositions | AMEND_CONTRACT |

The contract is not implementation-closeable while these choices remain
implicit. Party C principal verification removes the identity blocker but does
not cure schema or authority ambiguity.

## Selected Route

Decision: `SELECT_ACEL_G1_T3D_C0_GROUP4_CONTRACT_COHERENCE_AMENDMENT`.

T3D-C0 must amend the existing T2F owner contract rather than invent a second
Group 4 contract. The amendment must make all four decisions explicit and add
positive/adversarial vectors proving that:

1. registry snapshot hashing binds exactly the bytes Party B observed;
2. issuer canonical-content hashing has a non-circular, reproducible preimage;
3. registry mutation and lookup-response append authorities remain distinct;
4. T3D may close only as
   `SOURCE_CREATED_LOCAL_VERIFIED_PENDING_CONSUMER_BINDING`, with T3E owning
   the real verifier call and final consumer-binding checklist row.

No T3D-C1 implementation dispatch is authorized until Local accepts T3D-C0.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| worker chooses a plausible but non-authoritative hash preimage | require exact byte construction and independently recomputable vectors in T3D-C0 |
| append writer gains registry mutation rights | require named separate ACL/write capability and negative access matrix |
| source creation is overclaimed as consumer binding | split T3D bounded source verification from T3E consumer execution |
| reviewer discovers contract choices only after code exists | block implementation now and resolve the full four-gap class in one amendment |

## Finding-To-Governance Learning Disposition

Defect class: `ORCHESTRATOR_PACKET_GAP`.

Learning lane: `GOVERNANCE_CONTROL_PLANE`.

Disposition: `DESIGN_REVIEW_REQUIRED`.

Next action: author one consolidated T3D-C0 contract-coherence work order that
closes all four gaps before any tooling path is created. Runtime behavior
learning, provider output learning and cost economics learning are each
`N/A_WITH_REASON`: this is pre-implementation contract analysis with no CVF
runtime execution, provider call, quota use or cost claim.

## Epistemic Process Block

### Expected Result / Prediction

The accepted Group 4 contract was expected to be sufficiently closed for a
five-path tooling dispatch once Party C became concrete.

### Evidence Comparison

Owner, lifecycle, row fields and lookup result order are present, but four
decision-changing joins remain unspecified: two byte identities, one append
authority/DACL and one T3D-to-T3E completion boundary.

### Contradiction Or Gap Disposition

The expected implementation readiness is contradicted. The gap is routed to a
single T3D-C0 amendment rather than distributed implementation guesses.

### Claim Update

Party C is Local verified, but Group 4 is `CONTRACT_REWORK_REQUIRED` and no
tooling or source-establishment claim is currently admissible.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | audit headings, finding class/lane/disposition/next action, epistemic comparison, contradiction, trace and private export disposition |
| gateRunPurpose | confirm the pre-implementation gap decision and bounded route; gates are confirmation evidence |
| claimBoundary | contract-gap audit only; no implementation or real source effect |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF Local orchestrator/reviewer |
| Provider or surface | local private provenance workspace |
| Session or invocation | ACEL G1 T3D Group 4 pre-implementation contract audit, 2026-09-22 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, read-only internal sub-agent mapping, Local source reconciliation, `apply_patch`, governance gates and Git |
| Target paths | this audit only |
| Allowed scope source | operator-directed G1-G6 continuation and standing Local reviewer/orchestrator authority |
| Before status evidence | Party C Local verified at `7a5d509f3`; Group 4 tooling absent |
| After status evidence | four contract gaps consolidated; T3D-C0 selected; implementation remains closed |
| Diff evidence | exact one-path material manifest before commit; thirteen parked paths excluded |
| Approval boundary | audit and route selection only |
| Claim boundary | no tooling, registry, lookup response, observation, T3E, admission, provider/live, public or deployment effect |
| Agent type | Local orchestrator/reviewer |
| Invocation ID | `acel-g1-t3d-group4-contract-gap-audit-20260922` |
| Expected manifest | this audit |
| Actual changed set | this audit |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: internal pre-implementation governance and private source-contract
analysis; no public-sync authority.

## Claim Boundary

This audit selects a contract-coherence amendment. It does not resolve the
four gaps itself, authorize T3D-C1 implementation, create Group 4 sources,
append a second observation, wire T3E, promote or admit a candidate, invoke a
provider, export publicly, deploy or claim production readiness.
