# CVF GC-018 Baseline - MFRP-P2 Receipt And Reviewer Readout Composition

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MFRP-P2

Dispatch base head: `0e76be4b54cb6100813292fba3664a95bf665198`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: orchestrator/reviewer

successorTrancheOpened: NO

## Purpose

Authorize one bounded local composition of the existing autorun PASS receipt
and the existing AAF reviewer readout. P2 may add a canonical, tamper-evident
machine-verification payload and an exception-first L0 readout, while leaving
semantic judgment, closure, activation, replay, canary and downstream adoption
outside this tranche.

## Root Problem

H0 closed verifier/interpreter identity for reusable
`cvf.autorun.pass-receipt.v2` receipts, but the receipt still records gate
context and PASS checks rather than the P1 phase-return evidence boundary. AAF
has an L0 `ReviewerReadoutItem` seam, but it does not consume a verified machine
receipt, lead with not-checked scope/limitations, or surface every
`UNCLASSIFIED` item. P1 accepted the owner placement and left these two exact
owner-local deltas for P2.

## Accepted Authority

| Authority | Accepted fact |
|---|---|
| `docs/reviews/CVF_MFRP_P1_OWNER_AND_PHASE_RETURN_CONTRACT_RATIFICATION_PACKET_2026-09-01.md` | P1 is reviewer-accepted `CONTRACT_ACCEPTED_BOUNDED`; the P2 input contract names the autorun receipt and AAF readout owners, fixed-preimage boundary, ordering and hostile cases. |
| `governance/compat/run_agent_autorun_workflow_gate.py` | `RECEIPT_SCHEMA` is v2; `_receipt_context`, `_load_valid_receipt`, `_write_receipt`, `_verifier_identity_preimage` and `_jcs_bytes` are the current receipt/cache seams. |
| `governance/compat/test_run_agent_autorun_workflow_gate.py` | Focused tests already freeze v2 cache hit/migration and verifier-identity behavior; P2 extends this suite rather than creating a new runner suite. |
| `governance/compat/run_agent_automation_assist.py` | `ReviewerReadoutItem`, `AssistReport.to_dict`, `_build_reviewer_readout` and `_print_human` own the existing read-only reviewer readout. |
| `governance/compat/test_run_agent_automation_assist.py` | `ReviewerReadoutTests` prove L0 advisory behavior, JSON/human exposure, no closure decision and no filesystem mutation. |
| `docs/reference/sot_three_layer/README.md` | SOT3 owns RFC 8785 JCS/SHA-256 fixed-preimage mechanics and test-vector discipline; its TruthReceipt profile label and field set are not reusable here. |

## Decision / Baseline

P2 extends the existing autorun receipt owner; it does not create a sibling
runner, reference family, semantic checker or phase authority. The worker may
version-migrate the receipt to `cvf.autorun.pass-receipt.v3`. v2, partial,
unknown or digest-invalid receipts must be deterministic cache misses and must
never be upgraded in place.

The v3 receipt contains one nested machine-verification object under the
profile `cvf.autorun.machineVerification.v1` plus a top-level `receiptDigest`.
The canonical preimage excludes wall-clock duration, cache-hit timing and the
digest field itself. It includes only deterministic authority/evidence fields:
receipt schema/profile, local phase-return digest, predecessor availability,
changed-path-plan digest, verifier identity/set digest, conservatively
summarized dependency identity, interpreter identity, input digests,
deterministic results, hard-obligation-link availability/failures, manifest
reconciliation state, exceptions, all unclassified items, not-checked scope,
limitations and the produced cache disposition.

P2 has no external seven-phase envelope, predecessor contract, hard-obligation
map or expected artifact manifest input. It must not fabricate them. The local
composition records their absence explicitly as `UNCLASSIFIED` or not-checked
scope and must not emit a semantic-ready token from missing inputs. The
phase-return digest may bind the current deterministic local gate envelope
(phase, base/head identities, command manifest and changed-path plan), but its
limitation must state that this is not a complete seven-phase return envelope.

AAF may consume only a receipt whose schema, profile, fixed-preimage digest and
status validate through the autorun owner. Its readout is L0/read-only and
orders: receipt validity/status; `notCheckedScope`; limitations;
`UNCLASSIFIED`; exceptions; deterministic results; candidate reviewer probes;
claim boundary. `DETERMINISTIC_PREFLIGHT_COMPLETE` is permitted only as a
mechanical completion token for a valid PASS receipt. No text may advise that
no rerun is needed, decide materiality, accept a claim, close a tranche or
authorize a next phase.

Default CLI behavior remains conservative. Any new receipt-input option is
explicit, read-only, repository-bounded and optional; an absent option must not
change existing AAF enforcement or output. P2 does not wire machine-first
routing into hooks or phase gates. P3 replay and P4 canary remain prerequisites
for any P5 activation.

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `governance/compat/run_agent_autorun_workflow_gate.py` | MODIFY only receipt v3 construction, validation, digest and fail-closed reuse/read seams. |
| `governance/compat/test_run_agent_autorun_workflow_gate.py` | MODIFY with fixed-vector, migration, tamper, omission, invalidation and rollback tests. |
| `governance/compat/run_agent_automation_assist.py` | MODIFY only L0 machine-verification receipt consumption and exception-first reviewer readout. |
| `governance/compat/test_run_agent_automation_assist.py` | MODIFY with ordering, unclassified, invalid-receipt, no-advice and no-mutation tests. |
| `docs/reviews/CVF_MFRP_P2_RECEIPT_AND_REVIEWER_READOUT_COMPOSITION_WORKER_RETURN_2026-09-01.md` | CREATE full no-commit implementation return and evidence ledger. |

No other path may change. In particular, do not edit the command catalog,
hooks, standards, templates, session state, roadmap or downstream workspace.

## Hostile Acceptance Matrix

| Case | Required observation |
|---|---|
| valid v3 exact state | reusable receipt validates; optional reuse remains exact-context only |
| v2/partial/unknown schema | deterministic miss and full bundle execution; no in-place upgrade |
| one canonical field or `receiptDigest` changed | validation rejects the receipt |
| duration-only change | authority-bearing digest remains unchanged |
| deterministic result/input/limitation change | digest changes |
| omitted or unavailable expected manifest | surfaced `UNCLASSIFIED`; never reported reconciled |
| absent predecessor/hard-obligation input | explicit not-checked/limitation; no semantic-ready claim |
| stale verifier/authority/path-plan boundary | cache miss through existing exact bindings |
| valid receipt with unclassified items | every item appears before completed results in AAF JSON and human output |
| invalid/tampered receipt | no `DETERMINISTIC_PREFLIGHT_COMPLETE`; fail-closed readout |
| exceptions present | none are filtered or silently downgraded |
| phrase/advice scan | no case variant of `no rerun needed`; no closure/acceptance/authorization advice |
| receipt input outside allowed local boundary | rejected without reading arbitrary external content |
| AAF default invocation | existing behavior and enforce exit semantics remain unchanged |
| reuse disabled | full autorun execution remains functional |
| implementation batch changes receipt/readout verifier paths | its own machine receipt is non-admissible as sole closure evidence; independent focused tests/gates remain required |

## Acceptance Strategy

The reviewer audits the four code/test paths as one graph, validates the fixed
preimage independently, reruns focused suites and samples hostile tamper,
ordering, unclassified preservation, default behavior and rollback. The
reviewer does not reproduce the worker's implementation. Gate PASS establishes
only deterministic local composition; it does not establish semantic truth or
authorize P3/P4/P5.

## Evidence / Verification

Worker must provide exact execution base/status, focused test counts, one
published fixed preimage/vector, v2-to-v3 miss evidence, receipt-tamper and
readout-order evidence, default-behavior compatibility, worker-return gates,
Core Guard authorization, SCEC successor binding and no-commit status. No
provider/live proof applies.

## Rollback Boundary

Immediate rollback is to disable optional receipt reuse/receipt consumption
and retain full autorun execution plus the pre-P2 AAF readout. Revert only the
four protected Python paths and P2 worker return. Preserve failed receipts for
diagnosis; never erase evidence or weaken existing H0 identity checks.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| P2 mission and exit token | governed roadmap | `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | Work Plan / Proposed Delivery Tranches | `MFRP-P2`; `COMPOSED_LOCAL_PASS_BOUNDED` | MFRP roadmap | ACCEPT |
| accepted P2 input contract | accepted review evidence | `docs/reviews/CVF_MFRP_P1_OWNER_AND_PHASE_RETURN_CONTRACT_RATIFICATION_PACKET_2026-09-01.md` | P2 Input Contract; Independent Reviewer Addendum | owner-local paths, ordering, fixed preimage, hostile cases | P1 accepted decision | ACCEPT |
| current receipt v2 seams | executable source | `governance/compat/run_agent_autorun_workflow_gate.py` | constants and receipt functions | `RECEIPT_SCHEMA`; `_receipt_context`; `_load_valid_receipt`; `_write_receipt`; `_jcs_bytes` | autorun receipt owner | ACCEPT |
| current AAF L0 seam | executable source | `governance/compat/run_agent_automation_assist.py` | reviewer readout and report serialization | `ReviewerReadoutItem`; `_build_reviewer_readout`; `AssistReport.to_dict`; `_print_human` | AAF owner | ACCEPT |
| focused receipt tests exist | regression source | `governance/compat/test_run_agent_autorun_workflow_gate.py` | v2 and H0 tests | `test_v2_exact_state_reuse_hit_no_execution`; hostile drift tests | autorun focused suite | ACCEPT |
| focused L0 tests exist | regression source | `governance/compat/test_run_agent_automation_assist.py` | `ReviewerReadoutTests` | ordering/output/no-decision/no-write seams | AAF focused suite | ACCEPT |
| canonical mechanics owner | canonical reference | `docs/reference/sot_three_layer/README.md` | receipt hash profile description | RFC 8785 JCS, SHA-256 and published vector discipline | SOT3 mechanics | ACCEPT |

## Negative Search And Collision Discipline

- All three named P2 dispatch/return paths were absent before authoring.
- Exact search:
  `rg -n "MFRP-P2|MFRP_P2_RECEIPT_AND_REVIEWER_READOUT_COMPOSITION|receipt and reviewer readout composition" docs CVF_SESSION governance/compat`.
- Matches were roadmap/P1 planning and critique/reconciliation references only.
- Disposition: `NO_ACTIVE_P2_PACKET_OR_COMPETING_OWNER_FOUND`.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`machine-first receipt readout composition`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "machine-first receipt readout composition" --role dispatcher --lifecycle-phase dispatch --json`
- Returned defect count: 0
- Returned defects: `NONE_RETURNED`
- Disclosed defectIds: `NONE`
- Dispatch impact: apply existing evidence, no-self-attestation, review-cost and single-pass controls; no ADIF edit.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | dispatch-ready and no-commit markers; seven Source Verification columns; protected-path authorization labels; Review-Dispatch fields; SCEC fields; trace labels; delta-boundary labels; full worker-return terms |
| gateRunPurpose | confirm source-derived dispatch shape after direct owner/test inspection |
| claimBoundary | machine checks validate shape and bindings only; they cannot prove receipt semantics or open P2 execution |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-P2 --title "Receipt And Reviewer Readout Composition" --date 2026-09-01 --base 0e76be4b54cb6100813292fba3664a95bf665198 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --scec-problem-key mfrp-receipt-reviewer-readout-composition --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope EXECUTABLE_IMPLEMENTATION --stdout` |
| generatedProfile | protected-governance-path, internal no-commit implementation profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact P1 authority, four-path owner/test graph, receipt/readout contract, hostile matrix and rollback |
| checkerReadAheadConfirmation | COMPLETE |
| docOnlyNewFields | local composition profile, receipt digest domain, readout ordering and hostile case identifiers |
| claimBoundary | dispatch provenance only; no P2 implementation result is predeclared |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: compose only the existing local autorun
receipt and existing AAF L0 reviewer readout with focused hostile tests.

Protected paths:

- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/test_run_agent_autorun_workflow_gate.py`
- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`

Operator authorization: the operator explicitly instructed continuation to P2
after independently accepted P1 contract ratification.

Rollback boundary: revert the four P2 Python changes, disable receipt reuse or
receipt consumption, and retain full autorun plus the pre-P2 AAF route. Do not
weaken H0 verifier identity or edit command catalogs/hooks to force PASS.

## Claim Boundary

This baseline authorizes four protected Python modifications and one worker
return. It does not authorize a new owner/reference family, command catalog or
hook changes, semantic scoring, automatic closure, P3-P6, downstream workspace,
provider/live, public sync, deployment or production.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private CVF governance-foundation composition.
