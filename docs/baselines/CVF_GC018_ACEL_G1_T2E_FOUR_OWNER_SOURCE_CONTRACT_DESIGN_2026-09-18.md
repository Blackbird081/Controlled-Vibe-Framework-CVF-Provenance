# CVF GC-018 Baseline - ACEL G1 T2E Four-Owner Source Contract Design

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Date: 2026-09-18

Batch ID: ACEL-G1-T2E-FOUR-OWNER-SOURCE-CONTRACT-DESIGN

Dispatch base HEAD: `e47fad31191070bed9b57680118978e9a3973cce`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator for accountable-party appointment; Local orchestrator/reviewer for technical disposition

Worker target: one shared-workspace `INTERNAL_AGENT`

## Purpose

Authorize a documentation-only design of four separately accountable owner
contracts and their future evidence-admission requirements. The baseline does
not appoint actual owners, create source modules, or authorize G1 runtime work.

## Architecture Decision

Use four distinct responsibility contracts: verifier key and public-key
registry control; authority-specification and hash binding; snapshot identity
and append-only observation; issuer content and lookup semantics. Separation is
the default. Any later role combination requires an explicit operator decision
and conflict-of-duty review.

Every contract is `PROPOSED_OPERATOR_DECISION` until an exact accountable
party, governed source, authority interface, writer, consumer, lifecycle and
durable evidence are independently verified. Candidate admission remains
`UNVERIFIED`.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T2C consumer contract | `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md`, Owner Ledger | design input only | ACCEPT |
| T2D four-row analysis | `docs/audits/CVF_ACEL_G1_T2D_SOURCE_OWNER_OPTIONS_2026-09-18.md`, Owner-Option Matrix | bounded reviewed input | ACCEPT |
| Local T2D review | `docs/reviews/CVF_ACEL_G1_T2D_SOURCE_OWNER_ESTABLISHMENT_LOCAL_REVIEW_2026-09-18.md`, Decision | evidence-only acceptance; no operational owner | ACCEPT |
| Operator topology choice | `docs/reviews/CVF_ACEL_G1_T2E_FOUR_OWNER_RESPONSIBILITY_LOCAL_DECISION_2026-09-18.md`, Decision / Disposition | design dispatch only | ACCEPT |
| Actual owner appointment and runtime source release | not established | later exact appointment and independent Local review | BLOCKED_SOURCE_NOT_FOUND |

## Proposed Tranche

Worker creates exactly:

- `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md`;
- `docs/reviews/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_WORKER_RETURN_2026-09-18.md`.

The design artifact must contain four contracts with explicit responsibility,
decision rights, write authority, consumer, update/correction/revocation
lifecycle, independence rules, durable evidence, admission evidence, failure
behavior, and unresolved operator inputs. It must include a cross-contract
segregation-of-duties matrix and reject circular self-attestation.

No TypeScript, Python, checker, continuity, parked-evidence, key, secret,
configuration, provider, network, public-sync or deployment change is allowed.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | two T2E documentation outputs | worker designs contracts but cannot appoint, accept, stage, or commit | T2C/T2D reviewed sources and Local decision | no runtime adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no selected adapter owner | no external ingress, credentials, mutation, or public claim | explicit exclusion | future adapter remains separate | `DEFERRED_WITH_REASON` |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| four owner responsibilities are approved for contract design | CURRENT_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2E_FOUR_OWNER_RESPONSIBILITY_LOCAL_DECISION_2026-09-18.md` | Decision / Disposition | four-responsibility model | operator and Local | ACCEPT |
| four operational dependencies remain ownerless | REVIEWED_FINDING | `docs/audits/CVF_ACEL_G1_T2D_SOURCE_OWNER_OPTIONS_2026-09-18.md` | Owner-Option Matrix | rows 1-4 | T2D source analysis | ACCEPT |
| T2C requires owner/source boundaries | DESIGN_INPUT | `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | Owner Ledger | verifier trust-anchor dependencies | hypothetical G1 contract | ACCEPT |
| existing operational owner exists | OWNER_CLAIM | `docs/reviews/CVF_ACEL_G1_T2D_SOURCE_OWNER_ESTABLISHMENT_LOCAL_REVIEW_2026-09-18.md` | Decision | bounded documentation acceptance | Local reviewer | REJECT |

## Negative Search And Collision Discipline

The T2D bounded search is accepted evidence and is not repeated. Same-token
roles, HMAC signing, generic credential stores, provider-key rotation, packet
issuer literals and T2C pseudocode are not operational owner proof. Proposed
contract paths and role labels must never be described as existing sources.

The two planned output paths were absent at dispatch authoring. A future match
found during execution is a contradiction requiring `BLOCKED_WITH_REASON`, not
authority to overwrite it.

Targeted dispatch query:
`rg -n --hidden --no-ignore -i 'ACEL-G1-T2E|VerifierKeyAndRegistryControlOwner|VerificationAuthoritySpecificationOwner|RegistryObservationOwner|IssuerRegistryAuthorityOwner' docs governance EXTENSIONS ECOSYSTEM CVF_SESSION -g '*.md' -g '*.json' -g '*.py' -g '*.ts'`.
Exact roots: `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM`, `CVF_SESSION`;
these cover docs, JSON evidence/state, Python checkers/tests and TypeScript
source/tests. Result before authoring: no proposed T2E output path or role-name
collision. Existing G1 trust terms in T2C/T2D are authoritative input
collisions, not operational-owner evidence. External evidence is not searched
because the packet declares internal-only intake.

Same-token collision `CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026` occurs in this baseline and the paired work order and is non-authoritative for completed output.
Same-token collision `CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_WORKER_RETURN_2026` occurs as a planned path and is non-authoritative pending worker execution. Same-token
collision `TY_LOCAL_DECISION_2026` is a parser fragment of the decision path
and is non-authoritative. Disposition: planned-path collisions are not binding
proof that a worker output or operational source exists.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | dispatch envelope fields; Source Verification columns and dispositions; closeability phases; review convergence scalars; review heading groups |
| gateRunPurpose | confirm packet shape before dispatch, not discover or prove an owner |
| claimBoundary | machine conformity does not appoint owners or authorize runtime |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class DOC_CHANGE --role dispatcher --lifecycle-phase pre-dispatch`

Returned defects: NONE_RETURNED

Returned defect count: 0

Dispatch impact: no matched ADIF entry; all normal dispatch controls still apply.

## Evidence / Verification Boundary

Required before release: exact-path status check, paired work-order consistency,
pre-dispatch autorun PASS, 13/13 frozen hash reconciliation, empty staging and
material commit followed by bounded continuity sync. Worker evidence is
pending-worktree evidence only; Local owns review and commits.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind held-dependency --batch-id ACEL-G1-T2E-FOUR-OWNER-SOURCE-CONTRACT-DESIGN --title "ACEL G1 T2E Four Owner Source Contract Design" --date 2026-09-18 --base e47fad31191070bed9b57680118978e9a3973cce --commit-mode WORKER_MUST_NOT_COMMIT --dependency ACEL-G1-T2D-OWNER-OPTIONS-REVIEWED --stdout` |
| generatedProfile | held-dependency plus no-commit worker profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | populated exact four-contract design scope, manifests, evidence and parked boundaries |
| checkerReadAheadConfirmation | applicable dispatch and artifact checkers read before authoring |
| docOnlyNewFields | contract responsibility, separation rule, admission evidence, circular-attestation rejection |
| claimBoundary | scaffold and baseline define dispatch shape only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design dispatch; no public-safe artifact or public-sync authority.

## Claim Boundary

This baseline authorizes only two documentation outputs. It does not appoint an
owner, implement a registry, generate or bind keys, perform issuer lookup,
admit a candidate, close T2D, or authorize runtime, provider, public-sync or
deployment work.
