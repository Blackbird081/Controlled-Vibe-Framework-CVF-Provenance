# CVF MFRP-P3-R1 Actual-Seam Replay And Committed-Oracle Redesign

Memory class: governed-planning-assessment

docType: assessment

Status: DESIGN_REVIEW_READY_IMPLEMENTATION_CLOSED

Date: 2026-09-01

Batch ID: MFRP-P3-R1

Design base head: `c87390b118de46c86eaa5e6b5e5f9b0a1e681415`

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Replace the rejected self-referential P3 replay with an actual-seam design
that measures observable P2 receipt validation and reviewer-readout behavior
against a committed, independently ratified safety oracle. Preserve machine
efficiency while preventing the replay worker from authoring both expected
truth and the code that confirms it.

## Target / Source

| Source | Design authority |
|---|---|
| independent rejection | `docs/reviews/CVF_MFRP_P3_INDEPENDENT_REVIEW_RETURN_TO_DESIGN_2026-09-01.md`; P3-RV-1 through P3-RV-5 |
| original P3 work order | freeze/coverage intent and zero-tolerance categories; rejected execution shape is not inherited |
| P2 receipt owner | `governance/compat/agent_autorun_machine_verification.py`; `_machine_verification_object`, `_machine_verification_digest`, `_validate_receipt_integrity` |
| P2 readout owner | `governance/compat/agent_automation_machine_verification_readout.py`; `build_machine_verification_readout`, `machine_readout_to_dict` |
| accepted P2 result | `docs/reviews/CVF_MFRP_P2_RECEIPT_AND_REVIEWER_READOUT_COMPOSITION_WORKER_RETURN_2026-09-01.md` |
| MFRP roadmap | historical families, zero-tolerance classes, reviewer boundary and P4 stop |

## Scope / Methodology

This is design-only. No rejected worker artifact is modified, deleted, staged
or accepted. No oracle JSON, runner, test, result ledger, work order, hook,
catalog, standard or session surface is created by this assessment.

The redesign follows four separations:

1. normative safety expectation is committed before runner implementation;
2. test input/mutation is distinct from observed P2 output;
3. machine evidence completeness is distinct from safety disposition;
4. worker result production is distinct from reviewer acceptance.

## Root-Cause Model

The rejected helper used fixture-authored `expectedReceiptResult` as both the
oracle and the observed result. Membership in a fixed allowlist counted as
detection. The fixture's source, locator, mutation and surfaced-gap fields did
not cause owner behavior and were not evidence-bound. Current tests asserted
the chosen fixture but did not enforce fail-closed behavior on arbitrary
admissible input.

The redesign must therefore make the control flow causal:

```text
committed oracle case
  -> resolve source + locator/excerpt digest
  -> construct deterministic valid P2 base receipt
  -> apply declared mutation operator
  -> invoke actual P2 receipt validator
  -> invoke actual P2 readout builder/serializer
  -> classify observed output against precommitted safety predicate
  -> emit evidence-complete result + candidate safety disposition
  -> independent reviewer evaluates exceptions and decides
```

## Tranche Split And Authority Boundary

### MFRP-P3-R1A - Committed Oracle Ratification

R1A is a dispatcher/reviewer-owned documentary and machine-data tranche. It
creates and independently reviews one machine-readable oracle manifest plus
its ratification packet. It contains no replay helper and executes no case.

R1A exit: `ORACLE_RATIFIED_BOUNDED` or `RETURN_TO_DESIGN`.

The accepted oracle manifest is committed before R1B. Its repository blob and
SHA-256 become immutable predecessor evidence in the R1B work order. The R1B
worker cannot edit it.

### MFRP-P3-R1B - Actual-Seam Runner

R1B is a separate exact-manifest, no-commit implementation tranche. It may
create a runner, focused tests, post-run result ledger and worker return. It
consumes the exact committed R1A oracle and existing P2 owners read-only.

R1B exit:

- `REPLAY_EVIDENCE_COMPLETE_PASS_CANDIDATE` only when execution is complete
  and every required predicate is satisfied;
- `REPLAY_EVIDENCE_COMPLETE_RETURN_TO_DESIGN_CANDIDATE` when execution is
  complete but at least one actual P2 safety predicate fails;
- `BLOCKED_EVIDENCE_INCOMPLETE` for oracle/source/seam/freeze/coverage drift.

Only the reviewer selects `REPLAY_PASS` or `RETURN_TO_DESIGN`. Neither R1A nor
R1B opens P4 automatically.

## Committed Oracle Manifest Contract

Proposed schema: `cvf.mfrp.actualSeamReplayOracle.v1`.

Top-level required fields:

| Field | Requirement |
|---|---|
| `schema` | exact schema token |
| `profile` | `MFRP_P3_R1_DISPATCHER_RATIFIED_ORACLE` |
| `sourceManifest` | exact seven paths and SHA-256 values |
| `requiredCaseIds` | exact unique ordered set; minimum eighteen |
| `requiredFamilies` | exact roadmap family set |
| `requiredZeroToleranceClasses` | exact seven-class set |
| `cases` | deterministic input/mutation and normative safety predicate only |
| `claimBoundary` | oracle is a safety expectation, not observed runtime evidence |

Every case carries:

| Field | Meaning |
|---|---|
| `caseId` | stable unique identifier |
| `family` | one required roadmap family |
| `sourceRef` | source ID, exact heading/locator and `sourceExcerptSha256` |
| `derivation` | `HISTORICAL_INPUT` or `SEEDED_DERIVATION` |
| `baseReceiptProfile` | deterministic valid P2 receipt factory profile |
| `mutation` | typed operator and exact JSON-pointer target; no prose-only mutation |
| `attackBindingMode` | `AFTER_BINDING`, `ATTACKER_REBOUND`, or `NO_MUTATION` |
| `requiredSafetyPredicate` | normative observable predicate, never a claimed observed token |
| `zeroToleranceClass` | one exact class or `NONE` |
| `prohibitedOutcome` | observation that constitutes escape/false negative |

The manifest must not contain `observed*`, `actual*`, pass/fail or helper
result fields. Those belong only to the R1B result ledger.

## Mutation Operator Contract

The runner supports a closed, code-owned operator set:

| Operator | Behavior |
|---|---|
| `DELETE_JSON_POINTER` | delete one exact field after validating pointer existence |
| `REPLACE_JSON_POINTER` | replace one exact field with a typed safe fixture value |
| `ADD_JSON_POINTER` | add only to an explicitly permitted object/list location |
| `ALTER_SOURCE_IDENTITY` | mutate bound phase/verifier/path identity |
| `ALTER_CHECK_SET` | add/remove/reorder named deterministic check evidence |
| `INJECT_SECRET_SENTINEL` | insert a non-secret fixed sentinel classified as secret-like |
| `NO_MUTATION` | positive control |

Unknown operator, pointer miss, type mismatch, ambiguous multiple target or
unconsumed mutation fails `BLOCKED_EVIDENCE_INCOMPLETE`. The runner records a
before/after mutation digest without writing the mutated receipt to disk.

## Actual P2 Seam Contract

For each case, the runner must:

1. build a valid deterministic P2 v3 receipt using the canonical P2 object and
   digest owners, not a copied schema implementation;
2. prove the unmutated control passes `_validate_receipt_integrity`;
3. apply the committed typed mutation in memory;
4. call `_validate_receipt_integrity` on the mutated payload;
5. call `build_machine_verification_readout(valid, payload, reason)` and
   `machine_readout_to_dict` on that exact observation;
6. store only secret-safe normalized observation fields in the result ledger;
7. evaluate the committed safety predicate against the observed fields.

The runner must import the existing P2 owners. A standalone comparison that
does not invoke both seams is a hard failure.

## Safety Predicate Vocabulary

Predicates are observable and closed:

| Predicate | Satisfaction rule |
|---|---|
| `RECEIPT_REJECTED` | validator returns false with non-empty reason |
| `GAP_SURFACED_UNCLASSIFIED` | named required gap is present in serialized `unclassified` or `notCheckedScope` |
| `NO_COMPLETION_TOKEN` | serialized status is not `DETERMINISTIC_PREFLIGHT_COMPLETE` |
| `SECRET_SENTINEL_NOT_EMITTED` | sentinel absent from every serialized output field; rejection/redaction reason remains secret-safe |
| `IDENTITY_DRIFT_REJECTED` | mutated bound identity produces validator false |
| `HARD_OBLIGATION_NOT_CLOSED` | hard-obligation scope remains explicit and no closure/authorization token is emitted |
| `POSITIVE_CONTROL_VALID` | unmutated canonical receipt validates and readout is mechanically complete with all limitations preserved |

No predicate may infer materiality, business value, semantic truth or
reviewer acceptance. A class not representable by current P2 fields must be
declared `NOT_REPRESENTABLE_BY_CURRENT_P2` during R1A and cannot count as
detected. R1B then returns a design candidate honestly.

## Source And Locator Binding

Before case execution, the runner recomputes all seven source hashes and
resolves each exact locator. It normalizes the selected UTF-8 excerpt under a
single published byte recipe and compares `sourceExcerptSha256`.

Missing/duplicate locator, source ID not present in `sourceManifest`, excerpt
digest drift or a case referencing the wrong source fails before execution.
Source binding establishes provenance only; it does not turn historical prose
into observed P2 behavior.

## Freeze And Immutability Contract

The only pre-execution frozen artifact is the R1A oracle manifest already
committed before R1B. The R1B work order pins:

- repository-relative oracle path;
- commit SHA containing it;
- file SHA-256;
- JCS content digest excluding no field;
- required case/family/class set digest.

R1B verifies all five identities before importing runner code. Any mismatch is
`BLOCKED_EVIDENCE_INCOMPLETE`; the worker cannot refresh the pins.

The result ledger is created after replay and is therefore not falsely called
pre-run frozen. It records oracle identity, actual observations, first run,
any runner-code-only repair, final run and all divergences. Oracle mutation is
never authorized in R1B.

## Runtime Coverage Invariants

The runner, not merely its tests, fails closed unless:

- case IDs exactly equal `requiredCaseIds`;
- case count is at least eighteen;
- family set exactly covers `requiredFamilies`;
- every seven zero-tolerance class has at least one case;
- every case source/locator/excerpt binding resolves;
- every mutation operator is consumed exactly once;
- every case produces one validator and one readout observation;
- observation totals reconcile exactly to admitted cases;
- no required predicate is unknown or unevaluated.

Zero-case totals are a hard failure, never N/A recall.

## Result Ledger Contract

Proposed schema: `cvf.mfrp.actualSeamReplayResult.v1`.

For each case the post-run ledger records:

- oracle case ID and oracle manifest digest;
- base receipt digest and mutated in-memory digest;
- mutation-applied proof;
- validator boolean and normalized reason code;
- serialized readout status, not-checked, limitations, unclassified and
  exception counts/content under secret-safe rules;
- required predicate, observed predicate outcome and pass/fail;
- false-negative/false-positive classification;
- limitation or `NOT_REPRESENTABLE_BY_CURRENT_P2` disposition.

Aggregate output separates:

- `executionCompleteness`: COMPLETE or INCOMPLETE;
- `safetyCandidate`: PASS_CANDIDATE or RETURN_TO_DESIGN_CANDIDATE;
- per-class numerator/denominator;
- exact missing/failed case IDs;
- claim boundary.

This prevents a complete run with findings from being confused with a safety
PASS.

## Mandatory Hostile Tests

R1B tests must prove at least:

1. one-case corpus cannot pass;
2. any missing family or zero-tolerance class cannot pass;
3. unknown source ID, missing locator and excerpt drift fail before replay;
4. changed committed oracle hash fails before replay;
5. unknown/unused mutation operator fails;
6. changing only expected/normative labels cannot manufacture observed output;
7. actual receipt digest tamper reaches P2 validator and is rejected;
8. attacker-rebound receipt tests structural gaps rather than only digest mismatch;
9. secret sentinel never appears in serialized evidence;
10. actual readout preserves every unclassified/not-checked/limitation field;
11. zero total for any required class is hard failure;
12. runner cannot emit reviewer `REPLAY_PASS`;
13. P2 owners remain byte-identical and focused regressions pass;
14. repeated runs are deterministic and write no receipt/cache/provider data;
15. a deliberately weakened local evaluator is caught by fixed oracle cases.

## Reviewer Minimal Sufficient Verification

The reviewer does not recreate R1B. It performs bounded independent checks:

1. recompute committed oracle identities and exact coverage sets;
2. inspect imports/call graph proving both P2 seams are invoked;
3. rerun the runner and focused suites;
4. mutate one coverage field, one source binding and one owner-observed field;
5. compare actual observations for all failed predicates, not all worker code;
6. decide PASS versus RETURN based on the result ledger and claim boundary.

This preserves machine-first cost savings while making the machine evidence
causal and independently challengeable.

## Evidence / Verification

Design verification requires the independent rejection's two hostile probes,
direct inspection of both current P2 owner seams and exact reconciliation of
each rejected control gap to one R1 boundary. Before any future dispatch, the
reviewer must confirm that the committed oracle is worker-read-only; the R1B
call graph invokes both actual P2 seams; runtime coverage/freeze/source checks
cannot be bypassed by a smaller fixture; and execution completeness remains
separate from safety disposition. No provider/live proof applies to R1A/R1B.

## Rejected Artifact Disposition

The five current P3 worker artifacts remain uncommitted rejected evidence
during this design review. Before any R1A commit or R1B clean-base execution,
the operator/reviewer must choose one explicit disposition:

- archive a hash-bound documentary snapshot and remove executable rejected
  paths from `governance/compat`; or
- discard the untracked paths after the rejection record is committed.

They must never be silently reused, overwritten as if they were a clean first
run, or committed as active helper/test owners. This assessment does not make
that destructive choice.

## Acceptance And Stop Conditions

R1 design is acceptable only if:

- R1A and R1B remain separate commits/checkpoints;
- oracle is committed and independently reviewed before runner authoring;
- runner invokes both actual P2 seams;
- runtime enforces coverage/source/freeze/mutation completeness;
- result distinguishes execution completion from safety outcome;
- actual misses remain visible and route to design;
- no provider/live call, P2 mutation, lifecycle activation or P4 opening.

Stop immediately for a need to modify P2 owners inside R1B. Any discovered P2
gap becomes a separately authorized P2-hardening successor after R1B review;
the replay worker cannot repair the measured system in the same tranche.

## Rollback Boundary

Rollback removes only unaccepted R1A/R1B new artifacts. It leaves accepted P2
unchanged, preserves the independent P3 rejection record and retains the full
trusted reviewer route. A failed actual-seam replay is evidence, not a reason
to weaken the oracle or exclude a safety class.

## Decision / Disposition

`DESIGN_REVIEW_READY_IMPLEMENTATION_CLOSED`.

Next eligible action is independent critique/review of this redesign, followed
by a separately authored R1A oracle-ratification baseline/work order only if
accepted. No R1A data, R1B implementation or P4 is authorized here.

## Epistemic Process Block

### Expected Result / Prediction

Separating a committed oracle from actual-seam execution should cause missing
coverage, provenance forgery and unrepresentable P2 safety behavior to appear
as explicit failures instead of `REPLAY_PASS_CANDIDATE`.

### Evidence Comparison

The rejected helper failed those exact probes because expected strings were
treated as observations and the freeze/coverage contract existed only in the
chosen fixture/tests. The redesign assigns each missing control to a distinct
committed or executable boundary.

### Contradiction Or Gap Disposition

Current P2 may genuinely fail some R1A safety predicates, especially
secret-sentinel handling or classes outside its local receipt envelope. That
is not a redesign defect and must not be predicted away; R1B exists to expose
it and return to design honestly.

### Claim Update

The design is ready for critique, not implementation. Actual recall, latency,
quota reduction, safety improvement and P4 eligibility remain unproven.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| rejected replay defects | independent executable review | `docs/reviews/CVF_MFRP_P3_INDEPENDENT_REVIEW_RETURN_TO_DESIGN_2026-09-01.md` | Independent Hostile Probe Results; Findings | P3-RV-1 through P3-RV-5 | P3 reviewer disposition | ACCEPT |
| receipt validation seam | executable owner | `governance/compat/agent_autorun_machine_verification.py` | validation/digest functions | `_machine_verification_object`; `_machine_verification_digest`; `_validate_receipt_integrity` | P2 receipt owner | ACCEPT |
| readout seam | executable owner | `governance/compat/agent_automation_machine_verification_readout.py` | build/serialization functions | `build_machine_verification_readout`; `machine_readout_to_dict` | P2 readout owner | ACCEPT |
| replay families/classes | governed roadmap | `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | Historical Replay And Hostile Test Matrix | eighteen families; seven zero-tolerance classes | MFRP roadmap | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_truth_foundation_claim_guard.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | assessment structural headings; epistemic structure; source-verification seven columns; claim boundary; public disposition; trace fields; file-size limits |
| gateRunPurpose | ensure redesign evidence is structurally inspectable without predeclaring implementation success |
| claimBoundary | checker PASS cannot ratify the oracle, implement R1B or open P4 |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF dispatcher/designer |
| Provider or surface | local private provenance repository |
| Session or invocation | MFRP-P3-R1 redesign, 2026-09-01 |
| Working directory | repository root |
| Command or tool surface | current owner/source reads, `rg`, hashes, hostile review evidence and `apply_patch` |
| Target paths | this assessment; independent rejection review; MFRP roadmap |
| Allowed scope source | operator instruction to redesign after independent `RETURN_TO_DESIGN` |
| Before status evidence | five rejected P3 artifacts untracked and untouched; HEAD `c87390b118de46c86eaa5e6b5e5f9b0a1e681415` |
| After status evidence | design/review documentation added; rejected artifacts remain untouched; implementation closed |
| Diff evidence | exact design-document paths reconciled separately from the five rejected worker paths |
| Approval boundary | P3-R1 design only |
| Claim boundary | no oracle ratification, runner implementation, P2 repair or P4 |
| Agent type | dispatcher/designer |
| Invocation ID | `mfrp-p3-r1-actual-seam-redesign-2026-09-01` |
| Expected manifest | N/A with reason: exact archive changed-set is content-addressed in `docs/reviews/rejected_evidence/MFRP_P3_2026-09-01/ARCHIVE_MANIFEST.txt`; this assessment is design-only and dispatches no implementation manifest. |
| Actual changed set | N/A with reason: repository status and the content-addressed archive manifest are the authoritative changed-set evidence for this design checkpoint. |
| Manifest delta | N/A with reason: no implementation manifest is dispatched by this design-only assessment. |
| Deletion or rename disposition | Five rejected P3 additions moved byte-identically to `docs/reviews/rejected_evidence/MFRP_P3_2026-09-01/` and given `.rejected` suffixes under operator approval; hashes are recorded in the archive manifest. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Core design correction; no public artifact or claim.

## Claim Boundary

This assessment designs a causal, actual-seam replay and independent committed
oracle boundary. It does not ratify oracle cases, implement a runner, repair
P2, claim replay recall or cost improvement, activate lifecycle routing, open
P4-P6, modify downstream workspaces or authorize provider/live, public-sync,
deployment or production behavior.
