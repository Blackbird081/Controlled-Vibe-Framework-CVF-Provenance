# CVF ACEL G1 T3B Group 2 Source Readiness Route

Memory class: governed-local-audit

docType: audit

Status: ROUTE_SELECTED_OPERATOR_CHECKPOINT_REQUIRED

Date: 2026-09-20

Decision base HEAD: `90218ca32`

Decision owner: Local orchestrator/reviewer for route selection; operator for
principal provisioning, policy values and authorization of actual source work.

successorTrancheOpened: NO

## Purpose

Audit whether ACEL G1 T3B can be dispatched after Group 1 became
`SOURCE_CREATED_LOCAL_VERIFIED`, select the safest Group 2 route, and expose
one consolidated operator checkpoint without inventing identity or policy.

## Target / Source

| Source | Decision-relevant authority |
|---|---|
| `docs/audits/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_LOCAL_VERIFICATION_2026-09-20.md` | Group 1 source is independently verified; no downstream tranche opened automatically. |
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Group 2 outer record, dual hashes, decision-event chain, unique-active invariant, proposed paths and explicit T3B operator checkpoint. |
| `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | `LookupProvenanceCheck` consumes `expectedAuthorityHash` and `freshnessThresholdSeconds`; admission requires `IDENTITY_CONFIRMED`. |
| `docs/reviews/CVF_ACEL_G1_T2E_CONTRACT_2_ACTIVATION_APPROVER_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | bounded role appointment only; concrete principal and operational proof remain pending. |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Local T3B readiness audit and route selection are the only open action. |

## Scope / Methodology

Local reused the accepted T2C/T2F evidence, checked both proposed Group 2
paths literally, searched the bounded governed roots for an existing Group 2
source or first-version content, and inspected enabled local Windows accounts
without changing them. No external research, credential access, account
mutation, source creation, activation event, provider call or worker execution
occurred.

## Readiness Evidence

| Check | Evidence | Result |
|---|---|---|
| Group 1 prerequisite | material commit `58281c2c6`; Local verification audit | PASS_BOUNDED |
| specification path | `governance/sources/verification_authority_spec/SPEC_v1.json` | ABSENT_EXPECTED |
| decision log path | `governance/sources/verification_authority_spec/ACTIVATION_DECISIONS.jsonl` | ABSENT_EXPECTED |
| path collision | bounded exact search found only T2F and current continuity prose | NO_COLLISION |
| concrete approver principal | no dedicated `cvf-g1-activation-approver` account or other operator-appointed exact principal exists | MISSING_OPERATOR_INPUT |
| canonical content contract | T2F defines the outer `canonicalBytesBase64` carrier and hashes but does not define the decoded content schema | ORCHESTRATOR_PACKET_GAP |
| freshness policy value | T2C requires `freshnessThresholdSeconds`; no exact governed value exists | MISSING_OPERATOR_POLICY |

Enabled local accounts are not silently eligible. `cvf-g1-party-a` is
forbidden because Party A cannot activate its own authored specification.
`Blackbird` and `DELL` are general operator identities, not the appointed
dedicated approval identity. `CodexSandboxOffline` and `CodexSandboxOnline`
are execution-support accounts and have no operator appointment as Contract 2
activation authority.

## Findings / Position

The outer Group 2 integrity model is sufficiently specified: immutable
`SPEC_v{n}.json`, direct content hash, record hash, append-only decision events,
independent recomputation and a unique-active invariant. The decoded bytes are
not sufficiently specified. In particular, the accepted contract does not pin
the content schema, canonical field vocabulary, or initial freshness value.

This is not an operator failure. Asking the operator to provide arbitrary
"first specification content" would transfer an orchestrator-owned contract
gap to the operator and would let two implementations produce different valid
hashes for semantically different policies.

## Route Selection

Decision: `SELECT_T3B_C0_CONTENT_CONTRACT_THEN_PRINCIPAL_BOUND_CREATION`.

The selected sequence is:

1. Local proposes and operator approves one exact compact JSON policy payload.
2. Operator provisions or appoints one exact non-admin dedicated principal,
   recommended local name `cvf-g1-activation-approver`, distinct from Party A
   and reserved from future Parties B/C.
3. Local files a fresh GC-018 baseline and bounded no-commit tooling work order.
4. The worker builds hermetic author/decision tooling only; it does not log on
   as either principal and creates no real Group 2 source.
5. After Local acceptance, Party A authors `SPEC_v1.json`; the activation
   approver independently approves then activates it; Local verifies both.

No implementation work order is dispatchable from this audit because steps 1
and 2 are operator checkpoints.

## Recommended First-Version Policy

Local recommends that the decoded `canonicalBytesBase64` bytes be exact UTF-8
compact JCS for this object, with no BOM and no trailing newline:

```json
{"admissionRequiredLookupResult":"IDENTITY_CONFIRMED","authorityId":"ACEL_G1_DECISION_OWNER","authoritySpecSchema":"cvf.acel.g1.verificationAuthoritySpec@1","freshnessThresholdSeconds":86400,"issuerVerificationRequirement":"VERIFIED_BY_LIVE_REGISTRY_LOOKUP","receiptDomain":"cvf.verifierReceipt","receiptProfileVersion":"v1"}
```

The recommended `86400` seconds is a conservative initial 24-hour policy
choice, not an already accepted fact. The operator may approve it or select a
different non-negative integer. Any change to any field creates different
canonical bytes and must be decided before the source/tooling work order.

## Consolidated Operator Checkpoint

To open the next packet, the operator must decide both items together:

1. approve creation/use of the dedicated standard local account
   `cvf-g1-activation-approver` as the exact activation principal; and
2. approve the recommended compact policy payload above, including
   `freshnessThresholdSeconds=86400`, or provide the exact replacement value.

Passwords remain operator-only and must never be pasted into chat, committed,
printed, or supplied to the worker.

## Risk / Corrective Action

| Risk | Control |
|---|---|
| Party A self-activates its own bytes | require exact different account name/SID before tooling dispatch and again at execution |
| general operator account is treated as dedicated authority | require explicit appointment of one exact principal; no inference from account existence |
| content hash binds an ambiguous policy | freeze exact compact JCS bytes before implementation; recompute independently |
| approval is confused with activation | require separate `APPROVED` then `ACTIVATED` events |
| T3B source is confused with candidate admission | keep T3C/T3D/T3E and candidate evaluation parked |

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `successorTrancheOpened: NO`; `## Findings / Position`; `## Finding-To-Governance Learning Disposition`; `## Agent Operation Trace Block`; `DEFERRED_PRIVATE_ONLY`; `## Claim Boundary` |
| gateRunPurpose | confirmation of a bounded Local route decision after source and collision checks |
| claimBoundary | no principal, policy approval, source, activation, consumer binding or admission is created |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: Group 1 would be ready, while the exact approver
principal and first policy bytes would remain unresolved.

Evidence Comparison: confirmed, with one additional design defect: the
accepted outer record does not define the decoded content schema or initial
freshness value.

Contradiction Or Gap Disposition: stop before dispatch, propose one exact
minimal content object, and consolidate the remaining identity/policy choices
into one operator checkpoint.

Claim Update: T3B is route-selected but not opened; Group 2 remains
`SOURCE_NOT_CREATED` and candidate evaluation remains `UNVERIFIED`.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Batch status |
|---|---|---|---|---|---|
| T2F defined the hash carrier but not the decoded policy schema/value | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | encode both envelope and hashed-payload schema in the next T3B packet before requesting operator content | HANDLED_IN_THIS_BATCH_BY_ROUTE_STOP |

This is a material tranche-local contract gap, not yet evidence of a repeated
cross-program failure requiring a new global checker.

Runtime/provider/cost learning: `N/A_WITH_REASON` because no runtime behavior,
provider output, token use, latency measurement or cost evidence was exercised;
their words appear only in forbidden-effect and claim-boundary statements.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | `acel-g1-t3b-group2-readiness-route-20260920` |
| Working directory | repository root |
| Command or tool surface | governed reads, literal path probes, bounded rg, read-only local-account inventory, apply_patch and governance gates |
| Target paths | T2C/T2F/T2E sources, Group 2 proposed paths, this audit |
| Allowed scope source | active next move at session commit `90218ca32` |
| Before status evidence | Group 1 verified; Group 2 paths absent; no exact approver principal or content payload accepted |
| After status evidence | route and exact consolidated operator checkpoint recorded; no source or account changed |
| Diff evidence | this audit is the only intended material path beyond unchanged parked files |
| Approval boundary | Local route selection and content recommendation only |
| Claim boundary | no T3B implementation, principal, source, approval, activation or admission |
| Agent type | Local reviewer/dispatcher |
| Invocation ID | `acel-g1-t3b-readiness-route-local-20260920` |
| Expected manifest | this audit only |
| Actual changed set | this audit only; thirteen pre-existing parked paths remain untracked and unchanged |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private readiness and operator-checkpoint decision; no public
artifact or public-sync authorization exists.

## Claim Boundary

This audit selects the next safe route and recommends exact initial policy
bytes. It does not appoint or provision a principal, approve the policy,
create Group 2 files, append a decision event, activate a specification, bind
a consumer, promote a key, admit a candidate, or authorize provider/live,
runtime, public-sync, deployment or production behavior.
