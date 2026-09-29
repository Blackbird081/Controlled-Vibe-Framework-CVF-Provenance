# CVF ACEL G1 T2F Operational Source Establishment Readiness Local Decision

Memory class: governed-local-decision

docType: review

Status: T2F_DOCUMENTATION_CONTRACT_DISPATCH_APPROVED

Date: 2026-09-18

Decision base HEAD: `f0b06d023bcf45feeb1981e4d940e1aa8ed40995`

Decision owner: Local orchestrator/reviewer

## Purpose

Determine whether the completed T2E authority appointments support a bounded
T2F worker dispatch and select the narrowest closeable tranche. The selected
tranche designs operational-source establishment contracts only; it does not
create, populate or operate any source.

## Target / Source

| Source | Verified locator | Use |
|---|---|---|
| `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md` | Contracts 1-4; Source-Admission Evidence Matrix | required source forms, lifecycle and evidence |
| `docs/reviews/CVF_ACEL_G1_T2E_PARTY_A_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party A Appointment Contract | Contracts 1+2 accountable identity and restrictions |
| `docs/reviews/CVF_ACEL_G1_T2E_PARTY_B_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party B Appointment Contract | two-registry observation boundary |
| `docs/reviews/CVF_ACEL_G1_T2E_PARTY_C_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party C Appointment Contract | issuer-registry authority boundary |
| `docs/reviews/CVF_ACEL_G1_T2E_CONTRACT_2_ACTIVATION_APPROVER_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Activation Approver Appointment Contract | independent exact-version/hash approval boundary |

## Scope / Methodology

Local evaluated dependency closure, source gaps, authority separation,
foreseeable output topology and worker closeability. Valid T2E evidence was
consumed under `EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION`.

The audit compared three options: direct source implementation; four separate
source-design tranches; and one integrated documentation-only source-
establishment contract. Direct implementation is rejected because exact paths,
schemas and evidence formats are not yet approved. Four independent designs
would duplicate shared identity, versioning, observation and admission rules.
The integrated documentation tranche is bounded and closeable.

## Findings / Position

All accountable identities are appointed, so worker design no longer needs to
invent owners. Four operational source groups remain absent:

1. verifier public-key registry and lifecycle evidence;
2. authority specification plus independent activation-decision record;
3. append-only registry observation log covering both registries;
4. issuer registry, lookup semantics and durable response evidence.

These groups share cross-source requirements: stable identities, monotonic
versions, canonicalization/hash rules, permission separation, correction and
revocation chaining, consumer bindings, fail-closed behavior and admission
evidence. One integrated contract can define those relationships without
creating the sources.

## Option Assessment

| Option | Disposition | Reason |
|---|---|---|
| implement sources now | REJECT | exact paths, schemas, approval records and consumer bindings are not established |
| four unrelated design tranches | REJECT | duplicates shared cross-source invariants and risks incompatible identities |
| integrated T2F source-establishment contract | SELECT | one bounded documentation artifact can define source inventory, interfaces, separation, lifecycle and phased implementation gates |

## Decision / Disposition

Decision: `DISPATCH_T2F_INTEGRATED_SOURCE_ESTABLISHMENT_CONTRACT_DESIGN`.

Authorize one `WORKER_MUST_NOT_COMMIT` internal worker to create exactly one
contract-design audit and one worker return. Required output must name proposed
exact future source paths, schema/field contracts, ownership and access matrix,
version identities, lifecycle transitions, durable receipts, consumer
bindings, validation rules, failure taxonomy and implementation tranche split.

The worker must preserve every source as `SOURCE_NOT_CREATED` and candidate
admission as `UNVERIFIED`. It may not create a registry/specification/log,
write code or schema files, provision an identity, generate/import keys, run a
live lookup, or open implementation automatically.

## Risk / Corrective Action

| Risk | Control |
|---|---|
| design prose is mistaken for source creation | require `SOURCE_NOT_CREATED` on every source row |
| one source silently trusts another's self-assertion | require cross-source evidence and circular-authority negative cases |
| worker chooses runtime technology prematurely | constrain output to implementation-neutral contracts and proposed paths |
| integrated scope becomes implementation | exact two-output ownership and explicit forbidden path families |
| accepted design auto-opens implementation | successor remains `NO`; Local review and operator checkpoint required |

## Negative Search And Collision Discipline

Exact path checks before authoring found all five T2F dispatch/output paths
absent. Targeted query:

```
rg -n --hidden --no-ignore -i "ACEL-G1-T2F|OPERATIONAL-SOURCE-ESTABLISHMENT-CONTRACT" docs governance EXTENSIONS ECOSYSTEM CVF_SESSION -g '*.md' -g '*.json' -g '*.py' -g '*.ts'
```

Absent-versus-collision disposition: query returned zero pre-existing T2F
matches before authoring. Matches introduced by this Local decision, paired
baseline and work order are planned-path collisions, not worker output or
operational-source evidence. Existing T2C-T2E source terms remain accepted
design-input collisions only.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | dispatch envelope placement; Source Verification dispositions; convergence scalars; closeability phases; trace labels; protected-path authorization labels |
| gateRunPurpose | confirm closeable dispatch shape after authority appointment |
| claimBoundary | checker conformity does not establish or implement a source |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: read-only changed-set accounting for the
two pre-existing parked protected checker paths while filing T2F dispatch
documents. No checker mutation is authorized.

Protected paths: `governance/compat/check_task_class_calibration_owner_evidence.py`;
`governance/compat/test_check_task_class_calibration_owner_evidence.py`.

Operator authorization: standing authority to continue after all T2E identity
decisions, with Local owning bounded readiness and dispatch. Rollback boundary:
revert only the T2F decision/baseline/work-order dispatch batch; preserve T2E
material and all thirteen parked paths.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer and dispatcher |
| Provider or surface | private CVF workspace |
| Session or invocation | ACEL G1 T2F readiness audit, 2026-09-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, path/token checks, scaffold preview, apply_patch and governance gates |
| Target paths | this decision, paired GC-018 baseline and T2F work order |
| Allowed scope source | completed T2E appointments and active next move |
| Before status evidence | HEAD `f0b06d023`; thirteen parked untracked paths; five planned paths absent |
| After status evidence | exact three dispatch artifacts pending; two worker outputs remain absent |
| Diff evidence | exact three-path dispatch manifest before commit |
| Approval boundary | documentation/evidence-only T2F dispatch |
| Claim boundary | no source creation, key, implementation, live/runtime/public effect |
| Agent type | Local dispatcher |
| Invocation ID | `acel-g1-t2f-readiness-dispatch-20260918` |
| Expected manifest | this decision, paired baseline and work order |
| Actual changed set | this decision, paired baseline and T2F work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | T2F documentation-contract dispatch readiness |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no runtime receipt is claimed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: Local readiness and dispatch decision only |
| invocationBoundary | local governed documentation workflow |
| interceptionBoundary | no provider, CLI/MCP, live or runtime interception claim |
| claimLanguage | ready for contract design; not ready for source creation or implementation |
| forbiddenExpansion | sources, keys, credentials, code/schema implementation, live lookup, admission, runtime, public sync, deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private readiness decision with no public-sync authorization.

## Claim Boundary

This decision authorizes a two-output documentation worker tranche only. It
does not establish any source, approve a source path for implementation,
activate a specification, admit a candidate or authorize runtime, provider,
public-sync or deployment work.
