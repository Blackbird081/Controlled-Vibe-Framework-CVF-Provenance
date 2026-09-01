# CVF MFRP-P3 Independent Review - Return To Design

Memory class: governed-review

docType: review

Status: REVIEWER_REJECTED_RETURN_TO_DESIGN

Date: 2026-09-01

Batch ID: MFRP-P3-REVIEW

Review base head: `c87390b118de46c86eaa5e6b5e5f9b0a1e681415`

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Record the independent disposition of the five-path MFRP-P3 worker return and
convert its reproduced control-loss defects into a bounded redesign input.
This review evaluates evidence and hostile behavior; it does not recreate or
repair the worker implementation.

## Target / Source

| Source | Identity / role |
|---|---|
| P3 work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P3_HISTORICAL_REPLAY_AND_FROZEN_DEFECT_LEDGER_2026-09-01.md`; freeze, actual replay and stop contract |
| rejected fixture | `governance/compat/fixtures/mfrp_p3_historical_replay.json`; SHA-256 `5b27701520f843ffcdbf4a05f7c1f9b9a76530f78b04c2f1ac6f79768d17dd5e` |
| rejected helper | `governance/compat/mfrp_historical_replay.py`; SHA-256 `497840c0d5c71c42fe05bca9d9e411d71ed8b8f9e609882628c25d5c513c84d6` |
| rejected tests | `governance/compat/test_mfrp_historical_replay.py`; SHA-256 `973a1b9f46f46f27d1e8cade660a0098f49b86ef4bf3d42de7aa78c5fa7265e7` |
| rejected ledger | Archive manifest `docs/reviews/rejected_evidence/MFRP_P3_2026-09-01/ARCHIVE_MANIFEST.txt`, entry `CVF_MFRP_P3_FROZEN_DEFECT_AND_FALSE_NEGATIVE_LEDGER_2026-09-01.md.rejected`; SHA-256 `51e56e080392bb4b396127ff72cb9d9e67ad4dcfe2c157caddcdc6cc35b3d935`; `NOT_ACTIVE_AUTHORITY` |
| worker return | Archive manifest `docs/reviews/rejected_evidence/MFRP_P3_2026-09-01/ARCHIVE_MANIFEST.txt`, entry `CVF_MFRP_P3_HISTORICAL_REPLAY_WORKER_RETURN_2026-09-01.md.rejected`; SHA-256 `a985f879d0239bf2d90844d38d87eb445673a3c95940efb3e20c79ef9aaf4347`; `NOT_ACTIVE_AUTHORITY` |

These identities describe the uncommitted worker return observed by the
reviewer. They do not promote any rejected Python or fixture path into an
accepted owner.

## Scope / Methodology

The reviewer confirmed the exact five untracked paths and no staged or
committed worker change. It read the helper, fixture, tests, ledger and return;
recomputed the seven historical source identities through the helper; reran
the replay, 32 P3 tests, 18 current P2 focused tests and reviewer-fast 67/67;
then ran two bounded provider-free hostile probes against the helper API using
temporary data outside the repository.

The probes changed only in-memory or temporary copies and removed them after
execution. The five worker artifacts remained byte-unchanged.

## Evidence Reconstruction

The ordinary worker proof reproduced:

| Proof | Result |
|---|---|
| current fixture replay | `REPLAY_PASS_CANDIDATE`; 20 cases; 18 families; source drift 0 |
| P3 focused tests | 32/32 PASS |
| P2 focused regression | 18/18 PASS |
| worker-return fast gate | 67/67 reviewer-fast PASS |
| changed set | exact five untracked additions; nothing staged/committed |

Those results prove current code/test agreement and document shape only. They
do not prove historical defect recall.

## Independent Hostile Probe Results

### Probe 1 - Coverage Removal And Provenance Forgery

A temporary copy retained the seven valid source-manifest hashes but reduced
`cases` to one clean case. The reviewer changed that case to a nonexistent
`sourceId`, nonexistent locator, arbitrary family/route, fabricated mutation
and empty surfaced gaps.

Observed output:

| Field | Observed |
|---|---|
| result | `REPLAY_PASS_CANDIDATE` |
| caseCount | 1 |
| familyCount | 1 |
| sourceDriftCount | 0 |
| required zero-tolerance totals | 0/0 in every one of seven classes |
| unclassifiedCases | empty |

This contradicts the work-order minimum of eighteen cases, every roadmap
family, all seven zero-tolerance classes and real case-to-source binding.

### Probe 2 - Safety Evidence Field Erasure

For a zero-tolerance predecessor-forgery case, the reviewer replaced
`sourceId`, locator, family, route class, mutation and surfaced gaps with
invalid or empty values while preserving the self-declared expected receipt
token. `_evaluate_case` continued to return `detected: true`.

The decision uses only `expectedReceiptResult`, `expectedReadoutResult` and
the class label. It does not execute the P2 receipt validator/readout, resolve
the source locator, apply the mutation or compare observed gaps.

## Findings / Position

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| P3-RV-1 | CRITICAL | the replay is a self-referential allowlist comparison over fixture-authored expected strings, not an actual P2 seam replay or independent oracle | BLOCKS_ACCEPTANCE |
| P3-RV-2 | CRITICAL | helper recomputes fixture digests but compares them to no committed freeze identity and never reads the ledger; changed corpus can pass | BLOCKS_ACCEPTANCE |
| P3-RV-3 | CRITICAL | minimum cases, required families/classes and case-to-source/locator bindings are tests of one current fixture, not fail-closed runtime invariants | BLOCKS_ACCEPTANCE |
| P3-RV-4 | HIGH | worker disclosed four ledger sections added after first replay, while the work order requires the whole corpus and ledger to remain unedited and mandates `RETURN_TO_DESIGN` on either mutation | BLOCKS_ACCEPTANCE |
| P3-RV-5 | HIGH | passing tests mirror helper assumptions and therefore do not detect the above false-positive acceptance route | REDESIGN_TEST_ORACLE |

## Finding-To-Governance Learning Disposition

PROMOTE_TO_REDESIGN_THEN_MACHINE_GUARD: a replay cannot measure its own
expected-output declarations. Freeze must be a committed dispatcher/reviewer
input, observed results must come from actual owner seams, and coverage/source
binding must be enforced by the runner rather than only by tests over one
fixture.

This is an existing-owner design correction. It does not justify a new
governance system, role taxonomy or semantic-scoring model.

## Risk / Corrective Action

| Risk | Required correction |
|---|---|
| self-authored oracle | commit the normative case manifest before runner implementation; worker cannot edit it |
| claimed rather than observed output | invoke P2 `_validate_receipt_integrity`, `build_machine_verification_readout` and `machine_readout_to_dict` on deterministic mutated receipt inputs |
| source label without binding | resolve exact source path/hash plus locator/excerpt digest before case admission |
| fixture mutation after freeze | pin committed blob SHA-256 in the implementation work order and reject any mismatch before replay |
| missing coverage accepted | fail closed on exact required case IDs, family set, zero-tolerance set and minimum counts |
| frozen ledger conflicts with later metadata | freeze only the committed oracle manifest; generate the result ledger after replay |

## Decision / Disposition

`RETURN_TO_DESIGN`.

The current P3 result is not accepted, no current rejected Python/fixture path
may be installed or committed as an active helper, and `REPLAY_PASS` is not
selected. A separately reviewed MFRP-P3-R1 design may split committed-oracle
ratification from actual-seam runner implementation. P4 remains closed.

## Epistemic Process Block

### Expected Result / Prediction

If the worker helper truly measured actual P2 safety behavior, removing all
required zero-tolerance cases or breaking source/locator/mutation bindings
would fail closed before a candidate result.

### Evidence Comparison

Both hostile probes instead returned or retained mechanical detection/pass.
The reproduced normal PASS therefore reflects fixture/helper agreement rather
than the required safety property.

### Contradiction Or Gap Disposition

The contradiction is executable and material. Passing worker tests do not
waive it. The ledger post-freeze edit independently activates the work-order
return-to-design condition.

### Claim Update

The evidence supports only `P3_REPLAY_DESIGN_INADEQUATE`. It makes no claim
about P2 being safe or unsafe across all seven categories; that is what the
actual-seam redesign must measure.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | governed review headings; Finding-To-Governance disposition; epistemic four-part structure; public disposition; trace manifest fields |
| gateRunPurpose | preserve an evidence-backed rejection without treating machine PASS as semantic acceptance |
| claimBoundary | checker PASS validates packet shape only, not the redesign or a future replay result |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF independent reviewer/orchestrator |
| Provider or surface | local private provenance repository |
| Session or invocation | MFRP-P3 independent review, 2026-09-01 |
| Working directory | repository root |
| Command or tool surface | governed reads, hashes, replay/test/gate commands and bounded temporary hostile probes |
| Target paths | five rejected worker artifacts read-only; this review document |
| Allowed scope source | operator returned `COMPLETE_PENDING_REVIEW`, then authorized redesign after reviewer rejection |
| Before status evidence | exact five untracked worker additions; nothing staged/committed |
| After status evidence | five worker artifacts byte-unchanged; review/design documentation only added separately |
| Diff evidence | reviewer did not modify, stage or commit the five worker paths |
| Approval boundary | independent P3 evaluation and redesign evidence only |
| Claim boundary | no P3 acceptance, implementation repair, P4 or external effect |
| Agent type | independent reviewer/orchestrator |
| Invocation ID | `mfrp-p3-independent-review-return-to-design-2026-09-01` |
| Expected manifest | N/A with reason: exact archive changed-set is content-addressed in `docs/reviews/rejected_evidence/MFRP_P3_2026-09-01/ARCHIVE_MANIFEST.txt`; this review evaluates the rejected execution and replacement design rather than dispatching an execution manifest. |
| Actual changed set | N/A with reason: repository status and the content-addressed archive manifest are the authoritative changed-set evidence for this design/review checkpoint. |
| Manifest delta | N/A with reason: no execution manifest is dispatched by this review checkpoint. |
| Deletion or rename disposition | Five rejected P3 additions moved byte-identically to `docs/reviews/rejected_evidence/MFRP_P3_2026-09-01/` and given `.rejected` suffixes under operator approval; hashes are recorded in the archive manifest. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Core governance redesign evidence; no public claim or export.

## Claim Boundary

This review rejects the current P3 replay design with reproducible local
evidence. It does not itself implement the replacement, decide actual P2
zero-tolerance recall, activate machine-first routing or authorize P4-P6,
downstream, provider/live, public-sync, deployment or production behavior.
