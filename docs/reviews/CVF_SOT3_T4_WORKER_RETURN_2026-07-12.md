# CVF SOT3-T4 Worker Return

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

docType: review_context

Date: 2026-07-12

Return ID: SOT3-T4-RETURN

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_T4_TRUTH_KERNEL_HARDENING_2026-07-12.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_T4_TRUTH_KERNEL_HARDENING_2026-07-12.md`

executionBaseHead: `08f103b38`

## Purpose

Worker return for the SOT3-T4 bounded no-commit implementation tranche.
Confirms exact scope executed, evidence coverage, gate results, actual
changed set, and no-commit state for the new
`EXTENSIONS/CVF_TRUTH_KERNEL/` package, per the paired work order's Worker
Return Packet Shape Contract.

## Target / Source

Accepted T2 contract chain
(`docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md`)
sections 3-6, invariants/negative-cases file
(`docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md`),
truth-foundation doctrine owner
(`docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md`),
the paired GC-018 baseline
(`docs/baselines/CVF_GC018_SOT3_T4_TRUTH_KERNEL_HARDENING_2026-07-12.md`),
the accepted T1 owner/novelty map CAP-04/CAP-05 rows, the accepted T3
completion review, and the retained legacy Kernel source at
`.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch/EXTENSIONS/CVF_TRUTH_KERNEL/`
(read for adaptable concepts only; no direct import).

## Scope / Methodology

Captured executionBaseHead `08f103b38` with a clean worktree. Re-read the
work order, GC-018 baseline, T2 contract chain sections 3-6, T2
invariants/negative-cases file, truth-foundation doctrine owner (Source
Conversion Matrix line rejecting the retained strict-mode package
directly), T1 owner map CAP-04 (`ENRICH_EXISTING_OWNER`) and CAP-05
(`NEW_OWNER_CANDIDATE`), and the retained legacy `strict-mode.ts`,
`verification-gate.ts`, `truth-receipt.ts`, and `hash-chain.ts` files
named in the baseline's Source Verification Block. Created a new package
at `EXTENSIONS/CVF_TRUTH_KERNEL/` with strict TypeScript types for
`KernelEvaluationRequest`, `KernelDecision`, `TruthReceipt`,
`TruthReference`, `EvidenceRecord`, `ObligationRecord`, and
`VerificationResult`, each matching the T2 canonical field/status
vocabulary exactly; a deterministic dependency boundary; immutable local
stores; a request-admission resolver binding packet hash, `READY_FOR_KERNEL`
status, evidence/obligation packet-lineage, and policy/rule version; a
deterministic evaluator that is the sole producer of verification
results; a canonical receipt-hash module implementing the T2
`cvf.sotThreeLayer.receiptHash.v1` profile exactly, reproducing the
published 522-byte preimage and its SHA-256 digest byte-for-byte; a
receipt issuer emitting a receipt for every decision outcome with replay
rejection; a revocation mechanism; and a reference issuer implementing
the complete Decision-Resolution Model and Eligible-Acceptance-Only
Issuance Rule. Ran typecheck, build, and test after fixing one real
defect the negative-matrix tests caught (see Findings / Position), then
the file-size guard and the forbidden-dependency `rg` scan. Did not stage
or commit.

## Findings / Position

- The retained prototype's `strictAllows` (`.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch/EXTENSIONS/CVF_TRUTH_KERNEL/src/gates/strict-mode.ts`)
  only filters for `status === 'fail'` and returns `allowed: true` on an
  empty `results` array, confirming the baseline's cited fail-open defect.
  The new admission and evaluation chain in `src/engine/admission.ts` and
  `src/engine/evaluator.ts` rejects an empty `evidence_refs` before
  evaluation and never reaches `ACCEPT_EVIDENCE_CANDIDATE` when the
  Kernel-produced `verification_result_refs` collection is empty,
  regardless of whether that emptiness comes from a caller supplying no
  evidence or from every supplied evidence reference failing to resolve.
- The retained prototype's `createTruthReceipt`
  (`.../src/receipts/truth-receipt.ts`) calls `new Date().toISOString()`
  directly and hashes only `{ previousHash, current }` where `current` is
  receipt metadata (project/phase/status fields), not the full
  authority-bearing field set the T2 profile requires. The new
  `src/receipt/receipt-hash.ts` module takes every field as an explicit
  parameter (no global clock read) and implements the exact
  `cvf.sotThreeLayer.receiptHash.v1` canonical preimage: fixed field
  order, RFC 8785 JCS string escaping, lexicographically sorted
  reference-identifier arrays, and `receipt_hash` excluded from its own
  preimage. `tests/receipt-hash-vector.test.ts` reproduces the contract
  chain's published 522-byte illustrative preimage and its SHA-256 digest
  (`bc32424380bd483ca208edd8ee18bcaaa874b109584341e8febc01b5e46ab5a3`)
  exactly, including a reordered-array case that produces the same
  digest (proving the sort step is order-independent) and two
  field-mutation cases that each produce a different digest (proving no
  authority-bearing field, including `receipt_id`, can be substituted
  without detection).
- One real defect was caught by the negative-matrix tests during this
  execution, not merely a documentation gap: the first
  `produceVerificationResults` draft only produced a verification result
  per bound obligation, so a clean request with evidence but zero
  obligations produced zero verification results and was incorrectly
  rejected as `REQUIRE_ADDITIONAL_EVIDENCE` even though its one evidence
  item was fully valid. The fix adds one verification result per bound
  evidence item (a provenance-label check) in addition to the existing
  per-obligation check, so an evidence-only request can reach
  `ACCEPT_EVIDENCE_CANDIDATE` while a request whose evidence reference
  does not resolve to any registered record still correctly produces zero
  verification results and is rejected. `tests/positive-path.test.ts`'s
  clean-input case and `tests/negative-matrix.test.ts`'s
  empty-verification-results case (now pointed at an unregistered
  evidence ID to genuinely exercise the empty-result path) both pass
  after the fix.
- `src/engine/reference-issuer.ts` implements the T2 contract chain's
  complete Decision-Resolution Model: it resolves the immutable
  `KernelDecision` via `TruthReceipt.decision_id`, then the immutable
  `KernelEvaluationRequest` via `KernelDecision.request_id`, and verifies
  `decision` token equality, `verification_result_refs` equality against
  the decision, `evidence_refs`/`obligation_refs` equality against the
  request (not the decision, which does not define those fields),
  `evaluated_content_hash`/`policy_version`/`rule_version` equality
  across all three records, `decision === "ACCEPT_EVIDENCE_CANDIDATE"`,
  empty `failed_obligations`, no blocking verification result, the
  receipt not revoked, and a valid (`from < until`) validity interval,
  in that order, before minting a `TruthReference`. Every missing record
  or mismatch returns a typed rejection reason instead of a reference.
- Reviewer recomputation now passes 33 of 33 focused tests across six suites
  (6 receipt-hash-vector
  cases, 15 negative-matrix cases covering every row in the work order's
  Negative Test Matrix, 6 positive-path/immutability cases, 3
  dependency-boundary cases). `npm run typecheck` and `npm run build`
  both complete with zero errors. The forbidden-dependency `rg` scan over
  `EXTENSIONS/CVF_TRUTH_KERNEL/src` returns zero matches.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| a future evaluator change reintroduces the retained prototype's vacuous-pass-on-empty-results defect | `computeDecision` in `src/engine/evaluator.ts` checks `request.evidence_refs.length === 0 \|\| verificationResults.length === 0` before any other condition and returns `REQUIRE_ADDITIONAL_EVIDENCE`, not `ACCEPT_EVIDENCE_CANDIDATE`; `tests/negative-matrix.test.ts` exercises both the empty-evidence-refs and the resolves-to-zero-results cases separately |
| a receipt hash is narrowed to a partial-field subset or a different encoding, allowing evidence/obligation/verification-result substitution | `tests/receipt-hash-vector.test.ts` pins the exact published 522-byte preimage and digest as a literal test vector, so any change to field order, escaping, or included fields fails the test immediately rather than silently drifting |
| a `TruthReference` is minted from a non-eligible receipt in a future change | every one of the Eligible-Acceptance-Only Issuance Rule's conditions is a separate `if` block in `src/engine/reference-issuer.ts` returning a distinct typed rejection reason, and `tests/negative-matrix.test.ts` exercises the non-acceptance-receipt, missing-record, and revoked-receipt cases independently |
| a caller-supplied boolean or fabricated verification-result object is read anywhere in the evaluation path | `produceVerificationResults` and `computeDecision` only read `request.evidence_refs`/`request.obligation_refs` (string IDs) and resolve them against locally registered records; `tests/negative-matrix.test.ts`'s caller-supplied-boolean case adds extra fields to the input object and asserts the resulting verification-result count matches only the genuinely registered evidence, not the fabricated caller data |
| replay (reusing a `receipt_id`/`decision_id` pair) silently overwrites prior receipt state | `stores.receipts` is an `ImmutableStore` that throws on key collision, and `issueReceipt` additionally checks for an existing receipt against the same `decision_id` before generating a new ID, returning `DUPLICATE_RECEIPT_IDENTITY` rather than silently succeeding |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | `Self-declared worker-return artifact: yes`; `Responds to work order:`; `dispatchWorkOrder:`; `Status: COMPLETE_PENDING_REVIEW`; required heading list in `check_worker_return_quality_gate.py`; `WORKER_MUST_NOT_COMMIT honored`; `operator-provided external comparison, critique, or recommendation`; full disposition/ledger-status taxonomy tokens for external absorption sections |
| gateRunPurpose | confirm this return's own shape matches the worker-return quality gate's structural requirements, informed directly by the correction rounds recorded in the SOT3-T3 worker return for the same gate family |
| claimBoundary | checker-shape conformance does not prove Truth Kernel correctness; that is proven separately by the typecheck/build/test/receipt-vector/scan evidence in Command Evidence below |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude no-commit TypeScript package worker |
| Provider or surface | local authorized private provenance workspace |
| Session or invocation | SOT3-T4 Truth Kernel hardening implementation execution, 2026-07-12 |
| Working directory | repository root |
| Command or tool surface | Read, Write, Edit, Bash (npm install/typecheck/build/test, rg, python governance checks, node vector verification, git status/diff read-only) |
| Target paths | new `EXTENSIONS/CVF_TRUTH_KERNEL/` package tree; this worker return |
| Allowed scope source | SOT3-T4 work order Allowed Scope section |
| Before status evidence | executionBaseHead `08f103b38`; clean worktree at worker start |
| After status evidence | `EXTENSIONS/CVF_TRUTH_KERNEL/` package created (26 tracked source/config/test files); this worker return created; no other path touched; no commit made |
| Diff evidence | `git status --short --untracked-files=all` and `git diff --name-status` both list only the new `EXTENSIONS/CVF_TRUTH_KERNEL/` files and this return as untracked additions |
| Approval boundary | bounded T4 no-commit package implementation and worker-return authoring only |
| Claim boundary | no reviewer acceptance, T5-T7, Flow, provider/live proof, or public-sync claim |
| Agent type | no-commit TypeScript package worker |
| Invocation ID | `sot3-t4-truth-kernel-hardening-execution-2026-07-12` |
| Expected manifest | `EXTENSIONS/CVF_TRUTH_KERNEL/README.md`; `EXTENSIONS/CVF_TRUTH_KERNEL/package.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/tsconfig.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/schemas/kernel-evaluation-request.schema.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/schemas/kernel-decision.schema.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/schemas/truth-receipt.schema.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/schemas/truth-reference.schema.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/schemas/evidence-record.schema.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/schemas/obligation-record.schema.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/schemas/verification-result.schema.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/deps.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/admission.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/deps-context.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/evaluator.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/receipt-issuer.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/revocation.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/receipt/receipt-hash.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/immutable-store.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/kernel-stores.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/evidence.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/kernel-decision.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/kernel-evaluation-request.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/obligation.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/refinery-packet.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-receipt.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-reference.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/verification-result.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/tests/dependency-boundary.test.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/tests/fixtures.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/tests/negative-matrix.test.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/tests/positive-path.test.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/tests/receipt-hash-vector.test.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/tests/reference-integrity.test.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/tests/schema-surfaces.test.ts`; `docs/reviews/CVF_SOT3_T4_WORKER_RETURN_2026-07-12.md` |
| Actual changed set | `EXTENSIONS/CVF_TRUTH_KERNEL/README.md`; `EXTENSIONS/CVF_TRUTH_KERNEL/package.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/tsconfig.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/schemas/kernel-evaluation-request.schema.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/schemas/kernel-decision.schema.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/schemas/truth-receipt.schema.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/schemas/truth-reference.schema.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/schemas/evidence-record.schema.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/schemas/obligation-record.schema.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/schemas/verification-result.schema.json`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/deps.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/admission.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/deps-context.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/evaluator.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/receipt-issuer.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/revocation.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/receipt/receipt-hash.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/immutable-store.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/kernel-stores.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/evidence.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/kernel-decision.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/kernel-evaluation-request.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/obligation.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/refinery-packet.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-receipt.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-reference.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/verification-result.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/tests/dependency-boundary.test.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/tests/fixtures.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/tests/negative-matrix.test.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/tests/positive-path.test.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/tests/receipt-hash-vector.test.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/tests/reference-integrity.test.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/tests/schema-surfaces.test.ts`; `docs/reviews/CVF_SOT3_T4_WORKER_RETURN_2026-07-12.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: create-only worker output; no source or governed artifact deleted or renamed |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | SOT3-T4 bounded no-commit deterministic Truth Kernel package implementation only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - typecheck/build/test output, the published receipt-hash test vector reproduction, the forbidden-dependency `rg` scan result, and the file-size guard result are recorded verbatim in Command Evidence below |
| actionEvidence | ACTION_EVIDENCE_PRESENT - the new `EXTENSIONS/CVF_TRUTH_KERNEL/` package and this return are the tranche's actions |
| invocationBoundary | local read/write source authoring plus local npm/rg/python/node command execution; no network call |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or runtime interception behavior claimed |
| claimLanguage | bounded no-commit deterministic package implementation |
| forbiddenExpansion | Truth Flow, direct retained-tree import, package registry activation, provider/live proof, public-sync, commit, release, readiness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation tranche; no public-sync
authorization; reviewer acceptance has not yet occurred.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | retained SOT3 corpus -> accepted T0-T3 evidence/contracts -> bounded T4 CVF-native Kernel rewrite |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing truth-foundation doctrine owner plus new `EXTENSIONS/CVF_TRUTH_KERNEL/` runtime candidate |
| Disposition | ADAPT contract-aligned value and REJECT_DIRECT_IMPORT retained prototype runtime |
| Claim boundary | T4 rewrite only; no Flow, provider/live, public-sync, or production claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch` plus accepted T1-T3 CVF authority |
| Enumeration command | `rg --files --hidden --no-ignore ".private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch"` followed by direct source reads |
| Manifest artifact or inline manifest | accepted `docs/evidence/sot/sot3-t0-source-manifest.json`; this return's own Changed Files section is the tranche output manifest |
| Processing ledger artifact or inline ledger | this return's Findings / Position section |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE - only READ, ADAPTED, and REJECTED were exercised this execution; DEFERRED, NO_NEW_VALUE, and BLOCKED_UNREADABLE apply to no source item in this bounded run |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE - only ADAPT and REJECT were exercised this execution; ABSORB, DEFER, BLOCK, and NO_NEW_VALUE apply to no source item in this bounded run |
| Owner-surface map | `docs/reviews/CVF_SOT3_T1_OWNER_NOVELTY_MAP_2026-07-12.md` CAP-04/CAP-05; new owner `EXTENSIONS/CVF_TRUTH_KERNEL/` |
| Unresolved items | 0; every adapted or rejected retained concept is named in Findings / Position |
| Completion claim boundary | bounded T4 Kernel package only; no whole-corpus, Flow, provider/live, public, or production claim |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| source/provenance/evidence/obligation doctrine | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | ENRICH_EXISTING | T2 adds concrete runtime bindings and receipt/reference contracts | Implemented against T2 without duplicating doctrine. |
| Kernel request/decision/receipt/reference runtime | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | no current general runtime owner existed before this tranche | Created `EXTENSIONS/CVF_TRUTH_KERNEL/` as the new owner. |
| retained strict gate and receipt code | OWNER_SURFACE_NOT_FOUND | REJECT_DIRECT_IMPORT | empty arrays passed, clock was global, receipt hash covered only metadata | Rewrote fully; added negative and receipt-vector tests. |
| retained verifier/registry concepts | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | NEW_FINDING | useful deterministic concepts required packet-bound CVF rewrite | Adapted only contract-aligned concepts (evidence/obligation packet binding). |
| monitors, adapters, database/SOT-index service | OWNER_SURFACE_NOT_FOUND | NO_NEW_VALUE | outside bounded T4 value | Excluded entirely from the package. |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| truth-foundation doctrine | provenance/evidence/obligation/verification minimums | DOCTRINE_ADAPTED | existing truth-foundation owner and T4 package contracts | CVF reviewer accepts, revises, or rejects the implementation | No duplicate doctrine owner. |
| independent Kernel identity | exclusive decision/receipt/reference producer | PACKAGE_CANDIDATE | `EXTENSIONS/CVF_TRUTH_KERNEL/` | Package metadata and exports created, subject to reviewer acceptance. | No activation. |
| evaluation and issuance engine | deterministic packet-bound trust evaluation | RUNTIME_CANDIDATE | new package source | Implemented bounded local runtime. | No provider/network/database. |
| future static overclaim checks | possible repeated-defect enforcement | CHECKER_CANDIDATE | future governance packet only | No checker implementation in T4. | No hook mutation. |
| retained strict gate/receipt/adapters | fail-open or incompatible implementation | REJECT_DIRECT_IMPORT | CVF-native rewrite only | Rejected direct copy; wrote a full CVF-native replacement. | No compatibility layer. |
| monitor/database/Flow implementation | outside T4 | NO_PACKAGE_OR_RUNTIME_VALUE | later explicit lane only | Kept excluded. | No monitor, SOT index, or Flow. |

## Rescan Intelligence Hardening

- Original source artifact: `docs/baselines/CVF_GC018_SOT3_T4_TRUTH_KERNEL_HARDENING_2026-07-12.md`
- Predecessor intake artifact: `docs/reviews/CVF_SOT3_T1_OWNER_NOVELTY_MAP_2026-07-12.md`
- Delta ledger status: NOT_APPLICABLE_WITH_REASON
- Routing matrix status: NOT_APPLICABLE_WITH_REASON
- Semantic sampling status: NOT_APPLICABLE_WITH_REASON
- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

N/A with reason: this tranche is a bounded implementation from
already-accepted T0-T3 evidence, not a corpus rehash or file-level
re-intake of the retained three-folder source. The baseline's Source
Verification Block named the retained strict-mode and receipt sources
plus the accepted doctrine and contract files; this execution re-opened
each one directly rather than performing a fresh full-corpus enumeration,
consistent with the baseline's Corpus Completeness And Report Integrity
disposition that final per-file reconciliation remains a later T7 lane.

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| SS-01 | GC-018 baseline, retained strict-mode row | retained strict mode passes empty results | confirmed present in `.../src/gates/strict-mode.ts`: `strictAllows` filters for failures only and returns `allowed: true` on an empty array | could the new evaluator still accept on a resolves-to-empty verification-result set through an indirect path | no; `computeDecision` checks `verificationResults.length === 0` unconditionally before any acceptance branch, and this exact case is covered by a dedicated negative-matrix test |
| SS-02 | GC-018 baseline, retained receipt row | retained receipt is nondeterministic and hashes a different shape | confirmed present in `.../src/receipts/truth-receipt.ts`: `new Date().toISOString()` and a `{previousHash, current}` metadata-only hash via `chainHash` | could an injected clock still leave a narrower hash payload than the full T2 profile | no; `computeReceiptHash` takes all thirteen T2-named fields as explicit parameters and the published test vector proves the exact preimage byte sequence is reproduced |
| SS-03 | T2 contract chain, Eligible-Acceptance-Only Issuance Rule | a non-accepting or unresolved receipt can never mint a TruthReference | new `issueReference` function checked line-by-line against the rule's four numbered conditions | could a receipt with `decision: "REJECT"` and a coincidentally-matching decision/request still pass by having no other mismatch | no; `receipt.decision !== "ACCEPT_EVIDENCE_CANDIDATE"` is checked as an explicit, separate condition after all binding-equality checks pass, and `tests/negative-matrix.test.ts`'s non-acceptance-receipt case confirms this |

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: T4 implements the bounded Kernel capability subset
from the already-enumerated and accepted SOT3-T0 corpus. It does not claim a new
full-source scan; the remaining per-file reverse reconciliation stays T7-owned.

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON: the retained `.private_reference/legacy/` folder is
already governed by the accepted SOT3-T0 intake. T4 performs bounded CVF-native
implementation from accepted T0-T3 evidence and does not open a new external
repository or copied-folder absorption entry.

## Corpus Completeness And Report Integrity

- Corpus task class: bounded implementation from a previously accepted
  retained three-folder absorption corpus.
- Corpus root: `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch`.
- Snapshot time: 2026-07-12, T4 execution.
- Enumeration command: `rg --files --hidden --no-ignore ".private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch"`; selected sources were then read directly and reconciled against the accepted 305-record `docs/evidence/sot/sot3-t0-source-manifest.json`.
- Manifest artifact or inline manifest: accepted 305-record SOT3-T0
  manifest; this tranche's own planned artifact manifest is the
  baseline's Planned Artifact Manifest table.
- Manifest hash: retained from accepted T0 evidence; no new whole-corpus
  hash claim.
- Processing ledger artifact or inline ledger: this return's Findings /
  Position and Semantic Sampling / Adversarial Review sections.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=305; ledger_terminal=0; exclusions=305; unresolved=0.
  T4 does not reopen corpus-wide terminal classification;
  final per-file reconciliation remains T7-owned, per the baseline's
  disposition.
- Unresolved files: 0 within the bounded T4 selected source facts.
- Declared exclusions: Truth Flow, retained monitors, adapters, database/
  SOT-index service, and all retained files not named in the baseline's
  Source Verification Block.
- Unreadable or unsupported files: none encountered.
- Aggregation check: 7 required public contracts planned
  (`KernelEvaluationRequest`, `KernelDecision`, `TruthReceipt`,
  `TruthReference`, `EvidenceRecord`, `ObligationRecord`,
  `VerificationResult`), 7 implemented and exported, 0 missing, 0 extra.
- Drift check: T0-T3 accepted evidence and the truth-foundation doctrine
  owner were re-read at execution start and found unchanged from the
  baseline's citations.
- Output traceability: every adapted concept in Findings / Position cites
  its retained source path and its converted CVF-native location.
- Adversarial verification: the Semantic Sampling / Adversarial Review
  table above independently re-checked the three highest-risk baseline
  claims (empty-results fail-open, nondeterministic/partial receipt hash,
  non-accepting receipt reference eligibility) against both the retained
  source and the new implementation.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS - matches the paired
  baseline's own corpus verdict; T4 is intentionally limited to the
  Kernel capability subset.

## Finding-To-Governance Learning Disposition

| Finding | defectClass | learningLane | disposition | nextAction |
|---|---|---|---|---|
| a first-draft evaluator implementation can pass typecheck and build cleanly while still containing a genuine logic gap (per-obligation-only verification-result production) that only the negative-matrix test suite caught | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RUNTIME_LEARNING_CANDIDATE | preserve the per-evidence-item plus per-obligation verification-result production pattern (`src/engine/evaluator.ts`) as a reference example; future Kernel-shaped evaluators should verify every bound input category independently, not only the category that happens to be present in the first test case written |
| the retained prototype's two highest-risk gaps (empty-results fail-open, receipt-hash payload narrowing) were both structural defects with source-cited line-level evidence, not merely doctrine gaps | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | CVF reviewer should confirm whether a published test vector (like the T2 receipt-hash 522-byte vector) should become a standard required artifact for every future canonical-hash-bearing contract, given how directly it constrained this implementation to the correct byte sequence on the first attempt |

Runtime/provider/cost learning lane: N/A_WITH_REASON - none of the
findings above are a runtime-behavior, provider-output, or cost/token/
latency-economics finding; both are governance-control-plane design
observations about evaluator design and hash-profile publication
practice, so `GOVERNANCE_CONTROL_PLANE` is the correct and complete
learning lane for this tranche.

Next action: route the new `EXTENSIONS/CVF_TRUTH_KERNEL/` package to the
CVF reviewer for acceptance, revision, or rejection before any T5 (Flow)
or later tranche is authorized.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a deterministic, no-AI rewrite of the
retained Kernel concepts can satisfy the complete T2 negative matrix,
including exact reproduction of the published canonical receipt-hash
test vector, without direct import, per the work order's stated
prediction.

Evidence Comparison Requirement: every resolver and issuer's behavior was
compared against the paired baseline's Required Invariants list and the
T2 invariants/negative-cases file's fourteen negative cases (the
fourteen rows in the work order's own Negative Test Matrix), and against
the retained prototype's actual runtime behavior re-confirmed this
execution.

Contradiction Or Gap Disposition: the prediction held after one bounded
in-execution repair. The published receipt-hash test vector reproduced
exactly on the first implementation attempt (see Findings / Position),
confirming the T2 contract-chain profile is fully and unambiguously
implementable as specified. One genuine implementation gap was found and
fixed during this execution, not merely a documentation contradiction:
the first `produceVerificationResults` draft under-covered the
evidence-only request case, which the negative-matrix and positive-path
test suites caught before any command-evidence claim was made. No
contradiction was found between the T2 contract chain and this
implementation once that gap was closed; the fix is recorded in Findings
/ Position rather than silently absorbed.

Claim Update Requirement: every one of the seven required public
contracts, the canonical receipt-hash profile with its published test
vector, and the full fourteen-row negative matrix carries a passing test
or a direct code-level guarantee (closed union type, immutable store, or
explicit rejection reason); none remain unclassified or asserted without
evidence.

## Claim Boundary

This return is advisory. It proves a complete, typechecked, built, and
tested `EXTENSIONS/CVF_TRUTH_KERNEL/` package satisfying the paired
baseline's Required Invariants and the work order's Negative Test
Matrix, including exact reproduction of the published canonical
receipt-hash test vector. It does not authorize reviewer acceptance,
package registry activation, Truth Flow implementation, provider/live
proof, public-sync, commit, push, release, or production readiness. The
package remains PENDING_CVF_REVIEWER.

## Command Evidence

Range: `08f103b38..worktree` (executionBaseHead to current uncommitted
worktree state; no commit was made).

```text
npm --prefix EXTENSIONS/CVF_TRUTH_KERNEL run typecheck
> cvf-truth-kernel@0.1.0 typecheck
> tsc --noEmit
(no errors, exit 0)

npm --prefix EXTENSIONS/CVF_TRUTH_KERNEL run build
> cvf-truth-kernel@0.1.0 build
> tsc
(no errors, exit 0)

npm --prefix EXTENSIONS/CVF_TRUTH_KERNEL test
> cvf-truth-kernel@0.1.0 test
> vitest run
 Test Files  6 passed (6)
      Tests  33 passed (33)

rg -n -i "openai|anthropic|provider|prompt|agent|fetch\(|axios|randomUUID|Date\.now|new Date\(\)" EXTENSIONS/CVF_TRUTH_KERNEL/src
zero matches in src/.

python governance/compat/check_governed_file_size.py --enforce
Governed files checked: includes new CVF_TRUTH_KERNEL files; Violations: 0

git diff --check
(no output, exit 0 - no whitespace errors)
```

Disposition: PASS for typecheck, build, test, receipt-hash-vector
reproduction, dependency scan, file-size guard, and whitespace check.

`python governance/compat/run_worker_return_fast_gate.py` (62 checks) ran
clean except one pre-existing, out-of-scope finding: the active session
state compatibility gate reports that `AGENT_HANDOFF_V42_2026-07-12.md`
does not yet record current HEAD `08f103b38` in its HEAD SHA block. This
finding is reproducible against `executionBaseHead` `08f103b38` itself
with zero worker changes present (confirmed by running
`python governance/compat/check_active_session_state.py` in isolation
before any package file was written), so it is a pre-dispatch dispatcher-
session artifact gap, not a defect introduced by this tranche. Session
files are explicit Forbidden Scope for this worker (Forbidden Scope:
"session files"), and the work order's Agent Handoff Contract Control
Block names `nextMoveSurfaces: reviewer/session-sync steward only after
acceptance`, so this worker did not and must not repair it. Disposition:
NOT_APPLICABLE_TO_WORKER_SCOPE - reviewer/session-sync steward owns the
handoff HEAD update after this return is accepted.

## git status --short

```text
?? EXTENSIONS/CVF_TRUTH_KERNEL/README.md
?? EXTENSIONS/CVF_TRUTH_KERNEL/package.json
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/deps.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/admission.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/deps-context.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/evaluator.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/receipt-issuer.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/revocation.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/receipt/receipt-hash.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/immutable-store.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/kernel-stores.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/types/evidence.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/types/kernel-decision.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/types/kernel-evaluation-request.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/types/obligation.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/types/refinery-packet.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-receipt.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-reference.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/src/types/verification-result.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/tests/dependency-boundary.test.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/tests/fixtures.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/tests/negative-matrix.test.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/tests/positive-path.test.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/tests/receipt-hash-vector.test.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/tsconfig.json
?? docs/reviews/CVF_SOT3_T4_WORKER_RETURN_2026-07-12.md
```

`node_modules/`, `package-lock.json`, and `dist/` under
`EXTENSIONS/CVF_TRUTH_KERNEL/` are all repository-gitignored and do not
appear in this status output.

## Changed Files

Comparing the clean executionBaseHead worktree to the current worktree;
the worker did not commit, so this reflects working-tree additions, not
a committed diff.

```text
A  EXTENSIONS/CVF_TRUTH_KERNEL/README.md
A  EXTENSIONS/CVF_TRUTH_KERNEL/package.json
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/deps.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/admission.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/deps-context.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/evaluator.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/receipt-issuer.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/revocation.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/receipt/receipt-hash.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/immutable-store.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/kernel-stores.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/types/evidence.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/types/kernel-decision.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/types/kernel-evaluation-request.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/types/obligation.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/types/refinery-packet.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-receipt.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-reference.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/src/types/verification-result.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/tests/dependency-boundary.test.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/tests/fixtures.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/tests/negative-matrix.test.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/tests/positive-path.test.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/tests/receipt-hash-vector.test.ts
A  EXTENSIONS/CVF_TRUTH_KERNEL/tsconfig.json
A  docs/reviews/CVF_SOT3_T4_WORKER_RETURN_2026-07-12.md
```

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. The no-commit package worker did not
commit. HEAD remains at executionBaseHead `08f103b38`. Only the
`EXTENSIONS/CVF_TRUTH_KERNEL/` package and this worker return are present
in the changed set. Any accepted material commit is owned by the CVF
reviewer/closer.
