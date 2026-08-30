# CVF GC-018 Baseline - DEAR-LP P4 Representative Detached Transport Pilot

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Batch ID: DEAR-LP-P4-R1

Dispatch base head: c8483065c

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: orchestrator/reviewer

Worker target: detached external worker role

providerExecutionAuthority: FORBIDDEN_FOR_CVF_API_AND_CREDENTIALS

externalAgentInvocationAuthority: ONE_OPERATOR_MEDIATED_INVOCATION

## Purpose

Authorize one provider-neutral, operator-mediated P4 pilot that transports the
generated task capsule to a detached workspace, receives one non-authoritative
proposed changeset, and subjects it to the local P0-P3 validator. The pilot
tests transport and return-contract usability only.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id DEAR-LP-P4-R1 --title "Detached External-Agent Representative Transport Pilot" --date 2026-08-30 --base c8483065c --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface EXTERNAL_AGENT_CLI_MCP --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --stdout` |
| generatedProfile | generic worker dispatch plus no-commit and external-agent surface controls |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced all placeholders with P4 transport, capsule, authority, return-root, validation, invocation-budget, and stop controls. |
| checkerReadAheadConfirmation | Guard orientation, literal gotchas, work-order template, dispatch-quality, convergence, external-intake, operation-trace, and lifecycle checker sources were read before final dispatch. |
| docOnlyNewFields | `externalAgentInvocationAuthority` records the one operator-mediated interaction separately from forbidden CVF API/provider calls. |
| claimBoundary | Dispatch provenance only; no pilot outcome, provider API, promotion, public, runtime, or production claim. |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| DEAR-LP-R1 deterministic P0-P3 | `docs/reviews/CVF_DEAR_LP_R1_DETACHED_EXTERNAL_AGENT_IMPLEMENTATION_RETURN_AND_LOCAL_PROMOTION_COMPLETION_2026-08-30.md`; reviewer-accepted bounded with 211 focused tests and 66 reviewer-fast checks | P4 may open only after local validator acceptance and an operator value decision | RELEASED_BY_OPERATOR_NEXT_INSTRUCTION |
| Roadmap P4 checkpoint | `docs/roadmaps/CVF_DETACHED_AGENT_IMPLEMENTATION_RETURN_AND_LOCAL_PROMOTION_ROADMAP_2026-08-30.md` P4 row and reviewer update | exactly one representative detached transport; no automatic P5 | RELEASED_BOUNDED |
| Task capsule | `docs/work_orders/DEAR_LP_P4_R1_PACKET/CVF_EXTERNAL_AGENT_TASK_CAPSULE.json`; SHA-256 `31ef26fb63ae80b928174680b1aa8621c9067d5125cfbb572f36af9631d2b1e2` | strict schema, detached class, exact pins, four context groups | PASS |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py` |
| literalTokensReviewed | dispatch status; dependency release; source verification; negative collision evidence; review convergence fields; trace labels; external-intake route; public disposition |
| gateRunPurpose | Confirm dispatch evidence shape after source and value review. |
| claimBoundary | Read-ahead proves packet conformance only, not the future detached return. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external-agent pilot dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "external-agent pilot dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No additional ADIF control required. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| P4 requires a transported return and local verification | roadmap design | `docs/roadmaps/CVF_DETACHED_AGENT_IMPLEMENTATION_RETURN_AND_LOCAL_PROMOTION_ROADMAP_2026-08-30.md` | Work Plan P4 row | representative detached pilot | DEAR-LP roadmap | ACCEPT |
| Detached output remains non-authoritative | protocol contract | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_PROTOCOL_REPRESENTATION_CONTRACT.md` | detached implementation proposal semantics | `EXTERNAL_RETURN_READY_FOR_LOCAL_VERIFICATION` | protocol 1.3 representation | ACCEPT |
| Local validator requires exact capsule binding | executable source | `scripts/external_agent_return_contract.py` | dispatch-binding validation | `validate_dispatch_binding` | detached return validator | ACCEPT |
| CLI validates without promotion | executable source | `scripts/external_agent_packet.py` | command parser and command dispatch | `validate-detached-return` | packet helper CLI | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Dispatch artifact paths | `Test-Path` returned false for baseline, work order, context, capsule, and worker-return paths before authoring | NO_COLLISION |
| Batch token | `rg -n "DEAR-LP-P4-R1|DEAR_LP_P4_R1" docs CVF_SESSION scripts` returned no pre-existing batch owner outside the parent P4 roadmap/checkpoint | NO_PARALLEL_OWNER |
| Collision decision | extend the existing DEAR-LP roadmap, protocol, capsule, and validator; create only dispatch and evidence artifacts | PASS |

## Decision / Proposed Tranche

Decision: authorize exactly one DEAR-LP-P4-R1 detached transport pilot. The
operator transports only this packet and capsule; the local reviewer validates
returned bytes and no P5 or repair invocation opens automatically.

## Evidence / Verification

- Capsule schema generation completed offline with exact SHA-256.
- P0-P3 completion evidence releases the validator dependency.
- Pre-dispatch autorun must pass after all packet and continuity edits.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | operator-mediated packet dispatch, detached return, then local validator and reviewer |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` plus `scripts/external_agent_return_contract.py` |
| Owner surface | DEAR-LP protocol, capsule, validator, work order, and reviewer receipt |
| Disposition | ADAPT only after local validation; no automatic absorption or promotion |
| Claim boundary | external output remains input evidence and cannot become CVF authority by transport |

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: this is one task-capsule transport pilot, not a
legacy or external repository absorption task.

## External Absorption Core

This packet transports one first-party CVF task capsule and expects one
proposal-only return. It does not enumerate or absorb an external repository.

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | one operator-transported task capsule and later detached return root |
| Enumeration command | exact Required Artifact Manifest plus local filesystem walk during validation |
| Manifest artifact or inline manifest | `docs/work_orders/DEAR_LP_P4_R1_PACKET/CVF_EXTERNAL_AGENT_TASK_CAPSULE.json` plus inline Required Artifact Manifest |
| Processing ledger artifact or inline ledger | inline Required Artifact Manifest and future `docs/reviews/evidence/CVF_DEAR_LP_P4_R1_LOCAL_VALIDATION_RECEIPT_2026-08-30.json` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/reference/external_agent_review/`; `scripts/external_agent_return_contract.py`; reviewer intake |
| Unresolved items | 1 before return: detached transport outcome |
| Absorption maturity | NO_RUNTIME_VALUE_WITH_REASON |
| Named runtime consumer | N/A_NO_RUNTIME_VALUE_WITH_REASON: documentation-only transport pilot |
| Integration evidence | N/A_NO_RUNTIME_VALUE_WITH_REASON: promotion and P5 are forbidden |
| Use proof | pending P4 transport receipt only; not runtime use proof |
| Operator checkpoint | exactly one external interaction |
| Absorption completion status | NO_RUNTIME_VALUE_WITH_REASON |
| Completion claim boundary | a valid return proves transport and local-verification eligibility only |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| one detached checklist proposal | evidence that the 1.3 return contract survives operator transport | `NO_PACKAGE_OR_RUNTIME_VALUE`; `DOCTRINE_ADAPTED`, `PACKAGE_CANDIDATE`, `RUNTIME_CANDIDATE`, `CHECKER_CANDIDATE`, and `REJECT_DIRECT_IMPORT` remain reviewer dispositions | DEAR-LP reviewer intake and local receipt | validate, then accept/reject/defer proposal value without promotion | documentation proposal only; no runtime or package activation |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| detached operator-checklist proposal | `docs/guides/CVF_EXTERNAL_AGENT_ROUND_TRIP_KIT.md`; `docs/reference/external_agent_review/README.md` | `ENRICH_EXISTING` candidate, subject to local review | representative transport evidence is new; checklist content may duplicate existing owners | validate transport first; reviewer later rejects, defers, or adapts content |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded four-artifact dispatch packet plus one future manifested return.
- Corpus root: paired baseline, work order, context JSON, and capsule JSON.
- Snapshot time: 2026-08-30 dispatch authoring.
- Enumeration command: filesystem-backed direct reads of the four named dispatch artifacts.
- Manifest artifact or inline manifest: Agent Operation Trace Expected manifest.
- Manifest hash: `31ef26fb63ae80b928174680b1aa8621c9067d5125cfbb572f36af9631d2b1e2` for the immutable task capsule.
- Processing ledger artifact or inline ledger: Source Verification and Required Artifact Manifest; returned bytes are pending.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=4; ledger_terminal=4; exclusions=0; unresolved=0 for dispatch artifacts.
- Unresolved files: 0 in dispatch packet; future return does not exist yet.
- Declared exclusions: private repository content and all paths outside the named packet.
- Unreadable or unsupported files: none among dispatch artifacts.
- Aggregation check: four named dispatch artifacts equal four dispositioned artifacts.
- Drift check: exact capsule SHA-256 and pinned commits recorded.
- Output traceability: capsule creation receipt, work order, and future local validation receipt.
- Adversarial verification: pin mismatch, missing artifact, extra file, symlink, secret, authority, path, and digest failures are fail-closed.
- Corpus verdict: PARTIAL - dispatch packet is reconciled; future detached return and any wider repository are outside this verdict.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: the public repository URL is an immutable task
pin only. The worker receives no authority to enumerate or absorb it.

## Claim Boundary

This baseline authorizes one external-agent interaction and one returned
folder for local validation. It does not authorize private-repository access,
CVF provider/API calls, credentials, network retrieval, subagents, local
promotion, P5 integration, commit, push, public sync, deployment, or a claim
that the workflow has passed before the reviewer validates the returned bytes.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private pilot dispatch with an offline operator-pinned public commit;
no public-sync action or public artifact mutation is authorized.
