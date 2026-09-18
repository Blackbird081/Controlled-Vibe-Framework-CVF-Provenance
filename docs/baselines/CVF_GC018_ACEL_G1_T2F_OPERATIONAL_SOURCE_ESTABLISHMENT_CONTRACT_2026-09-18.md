# CVF GC-018 Baseline - ACEL G1 T2F Operational Source Establishment Contract

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Date: 2026-09-18

Batch ID: ACEL-G1-T2F-OPERATIONAL-SOURCE-ESTABLISHMENT-CONTRACT

Dispatch base HEAD: `f0b06d023bcf45feeb1981e4d940e1aa8ed40995`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local orchestrator/reviewer for technical disposition; operator for later source-creation or implementation authorization

Worker target: one shared-workspace `INTERNAL_AGENT`

## Purpose

Authorize a documentation/evidence-only design of an integrated operational-
source establishment contract for the four T2E source groups. The baseline
does not create sources, schemas, code, keys, credentials or runtime behavior.

## Architecture Decision

Use one integrated contract-design tranche because the source groups share
identity, versioning, permission separation, correction chaining, durable
evidence, consumer binding and fail-closed admission rules. The design must
keep each source independently identifiable and separable for later
implementation work orders.

Every source row remains `SOURCE_NOT_CREATED`; candidate admission remains
`UNVERIFIED`. Proposed paths and schemas are design decisions pending Local
review, not operational artifacts.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T2E four-owner contract design | `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md` | accepted design input | ACCEPT |
| Party A appointment | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_A_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | bounded identity only | ACCEPT |
| Party B appointment | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_B_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | bounded identity only | ACCEPT |
| Party C appointment | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_C_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | bounded identity only | ACCEPT |
| activation approver appointment | `docs/reviews/CVF_ACEL_G1_T2E_CONTRACT_2_ACTIVATION_APPROVER_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | bounded identity only | ACCEPT |
| Local T2F readiness | `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_READINESS_LOCAL_DECISION_2026-09-18.md` | integrated documentation tranche selected | ACCEPT |
| operational sources | no verified implementation source | later separately authorized implementation | BLOCKED_SOURCE_NOT_FOUND |

## Proposed Tranche

Worker creates exactly:

- `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md`;
- `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_WORKER_RETURN_2026-09-18.md`.

The contract artifact must define the proposed exact path and contract for:

1. verifier public-key registry and lifecycle receipts;
2. authority specification and independent activation-decision record;
3. append-only observation log spanning both registries;
4. issuer registry, lookup semantics and durable response evidence.

For every group define format/schema fields, stable identity and version,
owner/writer/reader permissions, lifecycle, correction/revocation, integrity
or canonicalization rule, durable evidence, verifier consumer, fail-closed
behavior, negative cases and implementation prerequisite. Add a cross-source
access/separation matrix and a proposed successor-tranche split.

No implementation file, registry/specification/log instance, checker,
continuity file, parked evidence, key, credential, provider, network,
public-sync or deployment change is allowed.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | exact two T2F documentation outputs | contract design and return only; no acceptance or commit | T2E design and appointments | no runtime adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no selected adapter owner | no external ingress, credentials, mutation or public claim | explicit exclusion | adapter remains deferred | `DEFERRED_WITH_REASON` |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| four source groups and evidence requirements are defined | CURRENT_AUTHORITY | `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md` | Contracts 1-4; Source-Admission Evidence Matrix | source groups 1-4 | T2E design | ACCEPT |
| all accountable identities are appointed | CURRENT_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2E_CONTRACT_2_ACTIVATION_APPROVER_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Decision / Disposition | all accountable roles | operator decisions | ACCEPT |
| integrated documentation design is closeable | REVIEWED_DECISION | `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_READINESS_LOCAL_DECISION_2026-09-18.md` | Decision / Disposition | selected T2F option | Local reviewer | ACCEPT |
| operational sources already exist | SOURCE_EXISTENCE | `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md` | Existing/Proposed Owner Matrix | source rows | T2E evidence | REJECT |

## Negative Search And Collision Discipline

Before authoring, exact path checks returned false for the decision, baseline,
work order and both worker outputs. Targeted query returned zero pre-existing
T2F token matches:

```
rg -n --hidden --no-ignore -i "ACEL-G1-T2F|OPERATIONAL-SOURCE-ESTABLISHMENT-CONTRACT" docs governance EXTENSIONS ECOSYSTEM CVF_SESSION -g '*.md' -g '*.json' -g '*.py' -g '*.ts'
```

Absent-versus-collision disposition: matches now introduced by the dispatch
packet are planned-path collisions only. They do not prove worker output or an
operational source exists. T2E contract and appointment terminology is
accepted authoritative input, not T2F completion evidence.

Exact search roots: `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM` and
`CVF_SESSION`, with Markdown, JSON, Python and TypeScript globs shown above.
Same-token collision `CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026` occurs in the baseline/work-order planned paths and is non-authoritative.
Same-token collision `CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_WORKER_` occurs in the planned worker-return path and is non-authoritative.
Same-token collision `OURCE_ESTABLISHMENT_READINESS_LOCAL_DECISION_2026` is a parser fragment of the Local decision path and is non-authoritative.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | envelope fields; Source Verification dispositions; closeability phases; review convergence scalars; baseline headings |
| gateRunPurpose | confirm packet shape before dispatch, not discover or establish a source |
| claimBoundary | machine conformity does not authorize implementation |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class DOC_CHANGE --role dispatcher --lifecycle-phase pre-dispatch`

Returned defects: NONE_RETURNED

Returned defect count: 0

Dispatch impact: no matched ADIF entry; normal fail-closed controls remain.

## Evidence / Verification Boundary

Before release require exact three-path dispatch staging, output absence,
13/13 parked-path preservation, pre-dispatch PASS and a material commit followed
by continuity sync. Worker evidence remains pending-worktree evidence; Local
owns review and commits.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind held-dependency --batch-id ACEL-G1-T2F-OPERATIONAL-SOURCE-ESTABLISHMENT-CONTRACT --title "ACEL G1 T2F Operational Source Establishment Contract" --date 2026-09-18 --base f0b06d023bcf45feeb1981e4d940e1aa8ed40995 --commit-mode WORKER_MUST_NOT_COMMIT --dependency ACEL-G1-T2E-ALL-AUTHORITIES-APPOINTED --stdout` |
| generatedProfile | held-dependency plus no-commit worker profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | populated integrated source-contract scope, exact outputs, evidence and forbidden effects |
| checkerReadAheadConfirmation | dispatch, structure, closeability and review-cost checker sources read |
| docOnlyNewFields | source group identity, proposed path, schema, access matrix, lifecycle and implementation split |
| claimBoundary | scaffold and baseline define dispatch shape only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source-contract design dispatch with no public authorization.

## Claim Boundary

This baseline authorizes only two documentation outputs. It does not create or
approve implementation of a source, key, credential, schema/code module,
lookup, observation receipt, candidate admission, runtime, provider,
public-sync or deployment behavior.
