# CVF ASSF Behavioral Evaluation Contract

Memory class: FULL_RECORD

Status: CANDIDATE

Date: 2026-09-16

docType: reference_contract

Batch ID: ACEL-G3-T2-BEHAVIORAL-EVALUATION-CONTRACT-IMPLEMENTATION

Rework: ACEL-G3-T2-R1-CONSOLIDATED-SEMANTIC-REWORK (R1-01, R1-02, R1-03,
R1-04, R1-06 applied; see `## R1 Rework Disposition` below)

Post-G7 refinement: ACEL-POST-G7-REFINEMENT-T0 applies source-verified Jev
decision-evidence boundaries without changing this contract's owner,
certification authority, capture modes, or runtime scope.

EPISTEMIC_PROCESS_NA_WITH_REASON: fixed-schema contract document; it defines
a normative evaluation model and vocabulary rather than testing an
evidence-comparison hypothesis.

## Purpose

Define the generic, ASSF-composed behavioral-evaluation contract identified
by the accepted G3 T1 owner-composition design
(`docs/audits/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_2026-09-16.md`,
`CLOSED_PASS_BOUNDED_DESIGN_READY`). This contract supplies real behavioral
evidence into the existing ASSF `uatState`/`acceptanceEvidence` package
fields; it does not redefine certification/UAT ordering, does not
self-certify, and does not implement a runtime, provider, or CLI/MCP
consumer.

## Source Authority

| Authority | Path |
|---|---|
| G3 T1 accepted design | `docs/audits/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_2026-09-16.md` |
| G3 T1 design manifest | `docs/audits/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json` |
| G3 T1 completion review | `docs/reviews/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-16.md` |
| ASSF-T7 lifecycle guard contract | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` |
| ASSF-T1 package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` |
| G3 T2 GC-018 baseline | `docs/baselines/CVF_GC018_ACEL_G3_T2_BEHAVIORAL_EVALUATION_CONTRACT_IMPLEMENTATION_2026-09-16.md` |
| G3 T2 work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G3_T2_BEHAVIORAL_EVALUATION_CONTRACT_IMPLEMENTATION_2026-09-16.md` |

## Scope / Applies To

Applies to a future package's `acceptanceEvidence` and `uatState` fields
when that package declares this contract as its behavioral evidence source.
Applies to pure, deterministic, offline fixture/trace/grader composition and
to read-only evidence admission checking.

Does not apply to executing a real skill, provider, or agent; mutating
`certificationState`; mutating the generated skill index or a registry
entry; implementing a CLI/MCP adapter; or any runtime/production wiring.
This contract is documentation-only normative reference plus its paired
pure TypeScript implementation and read-only Python evidence checker; it
grants no loader, resolver, or activation authority.

## Certification And UAT Relationship (Reused, Not Redefined)

`certificationState` and `uatState` remain owned by
`CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md`. This contract's
grader output may populate `acceptanceEvidence` and `uatState: PASSED` by
citing a governed review artifact path. The grader never writes
`certificationState: CERTIFIED`; that remains a reviewer/closer decision
under the existing lifecycle ordering rule (`uatState: PASSED` is a
precondition for `certificationState: CERTIFIED`, never a substitute for
reviewer decision).

## Evidence Flow

```text
1. fixture         : one input scenario + expected outcome/process assertions
                      + declared allowed-transition table (positive or negative)
2. invocation       : the skill's declared behavior is exercised (live for a
                      deterministic/simple skill; live-with-repeat for a
                      stochastic skill; or a provenance-tagged mock/replay)
3. trace            : the recorded sequence of tool/output events, independent
                      of any self-declared pass/fail
4. grader           : a pure function of (fixture, trace) -> {result, defects[]}
                      with pre-declared defect classes; never mutates the trace
                      or reads a runner self-grade
5. result           : PASS_WITH_EVIDENCE | FAIL_WITH_DEFECTS | INCOMPLETE_TRACE |
                      UNDECLARED_TOOL_USE | STALE_REPLAY_PROVENANCE |
                      NONEQUIVALENT_BASELINE_PAIR | INSUFFICIENT_REPEAT_EVIDENCE
6. UAT projection   : a governed review artifact cites the result and updates
                      only the package's uatState/acceptanceEvidence fields;
                      certificationState is never auto-set
```

## Normative Rules

1. **Positive and negative invocation.** A fixture set for one skill must
   include at least one positive case (instructed behavior followed
   correctly) and at least one negative case (tool-order violation, missing
   required output field, or forbidden action attempt). A positive-only
   fixture set cannot reach `PASS_WITH_EVIDENCE`.
2. **Outcome and process assertions are both mandatory.** Outcome assertions
   check the final output shape/value. Process/tool assertions check the
   sequence and identity of tool/file/command invocations against the
   fixture's declared allowed-transition table. A correct outcome obtained
   through a forbidden process is a defect (`UNDECLARED_TOOL_USE`), not a
   pass; neither assertion class substitutes for the other.
3. **Explicit allowed-transition table.** Each fixture declares its own
   allowed-transition table. An event in the trace whose `(from, action, to)`
   triple is not in that table is fail-closed `UNDECLARED_TOOL_USE`
   regardless of the trace's final outcome.
4. **Repeat policy.** Deterministic fixtures (`repeatPolicy: "DETERMINISTIC"`)
   require exactly one passing repeat. Stochastic fixtures
   (`repeatPolicy: "STOCHASTIC"`) require three consecutive passing repeats
   before evidence reaches `PASS_WITH_EVIDENCE`; fewer than three consecutive
   passes is fail-closed `INSUFFICIENT_REPEAT_EVIDENCE`.
5. **WITH/WITHOUT baseline equivalence.** When a fixture pair declares a
   WITH run and a WITHOUT run, both runs must share byte-identical canonical
   input bytes (`canonicalInputBytes`). A WITH/WITHOUT pair built from
   unequal canonical input bytes is fail-closed `NONEQUIVALENT_BASELINE_PAIR`,
   never scored as a valid comparison.
6. **Mock/replay provenance and expiry.** Any trace whose `captureMode` is
   `MOCK_REPLAY` must carry a non-empty `provenanceSourceCommit` and a
   `provenanceExpiry` that, under strict ISO-8601 date-time parsing, is
   strictly after the fixture's declared `evaluationClockIso`. An expired,
   equal-to-clock, provenance-less, or malformed-date replay trace is
   fail-closed `STALE_REPLAY_PROVENANCE`. `MOCK_REPLAY` and
   `LIVE_REFERENCE_ONLY` are never live proof, and this contract's own
   tests and checker never execute a real live provider call.
7. **Source-hash invalidation.** Evidence is bound to the fixture's declared
   `sourceContentHash`. Whenever the trace's `sourceContentHash` does not
   match the fixture's `sourceContentHash`, prior evidence is invalidated
   and grading fails closed as `FAIL_WITH_DEFECTS` with a
   `SOURCE_HASH_MISMATCH` defect; passing evidence never carries forward
   across a source change without a fresh repeat.
8. **Runner/grader separation.** The trace producer (runner) and the grader
   are two independently invokable functions with no shared mutable state.
   The grader never trusts a runner-declared `selfReportedPass` field on the
   trace; any such field present on the trace is ignored by the grader and,
   if the trace's true condition would otherwise pass, the self-report is
   irrelevant, while a trace that declares `selfReportedPass: true` but is
   missing required evidence still fails as `INCOMPLETE_TRACE` or
   `UNDECLARED_TOOL_USE` per rules 2/3.
9. **Missing/incomplete trace.** A trace missing a fixture-required event or
   a fixture-required output observation is fail-closed `INCOMPLETE_TRACE`,
   never silently scored as a pass on partial evidence.
10. **Malformed and unknown input fails closed structurally, never throws.**
    Every field named in `## Cross-Language Evidence Schema` below is
    validated explicitly: `fixtureId`, `traceId`, `fixtureClass`,
    `repeatPolicy`, `baselineRole`, `captureMode`, `canonicalInputBytes`,
    `sourceContentHash`/`fixtureContentHash`, `allowedTransitions`,
    `requiredEvents`/`requiredOutputObservations`, `outcomeAssertions`/
    `outcomeValues`, `evaluationClockIso`/`provenanceExpiry`, and the trace
    array and each event's `{from, action, to}` shape. A missing, empty,
    wrong-typed, unknown-valued, or internally inconsistent value in any of
    these fields fails closed to `FAIL_WITH_DEFECTS` (or the more specific
    named result above when it applies) and never throws an uncaught
    exception or silently coerces the value. A field's absence is never
    treated the same as an explicit `false`/`0`/empty value passing a
    truthiness check; each is validated by its own explicit rule.
11. **No automatic certification and no input mutation.** The grader and the
    Python evidence checker never write `certificationState: CERTIFIED` and
    never mutate a fixture, trace, package entry, or generated index. Both
    are pure/read-only with respect to their inputs.
12. **Fixture-set admission (positive-plus-negative).** A fixture set for
    one skill is admitted toward `PASS_WITH_EVIDENCE` only when it contains
    at least one structurally valid `POSITIVE` fixture and at least one
    structurally valid `NEGATIVE` fixture. A positive-only or negative-only
    set is rejected (`MISSING_NEGATIVE_CASE`/`MISSING_POSITIVE_CASE`)
    regardless of how many fixtures of the one present class exist.
13. **WITH/WITHOUT baseline pairing.** A fixture declaring `baselineRole:
    WITH` or `WITHOUT` mandates a complementary paired fixture with the
    opposite role and byte-identical `canonicalInputBytes`; a missing pair,
    a same-role pair, a malformed role, or unequal input bytes is rejected
    (`MISSING_PAIR`/`SAME_ROLE_PAIR`/`MALFORMED_ROLE`/
    `NONEQUIVALENT_INPUT_BYTES`). A fixture declaring `baselineRole: NONE`
    must never silently consume a comparison pair; an unexpected pair
    supplied for a `NONE`-role fixture is itself rejected
    (`UNEXPECTED_PAIR_FOR_NONE_ROLE`).
14. **Decision-context binding.** Any judgment-bearing fixture and trace must
    carry the same canonical `decisionContextHash`. A source-equivalent trace
    produced against different state is fail-closed
    `DECISION_CONTEXT_MISMATCH`; typed output does not make a decision portable
    across state changes.
15. **Candidate-space and no-match semantics.** A fixture declares either
    `candidateSpaceMode: COMPLETE` with an explicit null `noMatchOutcome`, or
    `candidateSpaceMode: INCOMPLETE_WITH_ESCAPE` with a non-empty escape
    outcome. An incomplete candidate set may never force the grader to select
    one of the supplied candidates as though the set were exhaustive.
16. **Judgment is evidence, not authority.** `judgmentAuthority` has the only
    admitted value `EVIDENCE_ONLY`. Probability, confidence, or a typed choice
    may inform routing, verification, or escalation, but never grants tool,
    side-effect, certification, or promotion authority.

## Cross-Language Evidence Schema

One documented evidence/admission projection is shared semantically by the
TypeScript fixture, trace, and `BehavioralEvaluation` shapes and the Python
checker's `check_evidence_admission`. The grader result alone is not the
complete persisted evidence document: the projection also carries fixture
and trace provenance plus a reviewer-supplied governed artifact path. An
evidence document under this schema must carry, when the corresponding
capture mode or baseline role applies:

| Field | Type | Required when | Fail-closed rule |
|---|---|---|---|
| `result` | one of the seven named results | always | missing/malformed/unknown fails closed |
| `fixtureId` | non-empty string | always | missing/empty fails closed |
| `fixtureContentHash` | 64-char lowercase hex SHA-256 | always | missing/malformed fails closed |
| `sourceContentHash` | 64-char lowercase hex SHA-256 | always | missing/malformed fails closed; mismatch against the package's own `sourceContentHash` fails closed as stale |
| `decisionContextHash` | 64-char lowercase hex SHA-256 | always | missing/malformed fails closed; trace/fixture mismatch is `DECISION_CONTEXT_MISMATCH` |
| `candidateSpaceMode` | `COMPLETE` \| `INCOMPLETE_WITH_ESCAPE` | always | missing/unknown fails closed |
| `noMatchOutcome` | null or non-empty string | always | must be explicit null for `COMPLETE`; must be non-empty for `INCOMPLETE_WITH_ESCAPE` |
| `judgmentAuthority` | `EVIDENCE_ONLY` | always | any other value fails closed; judgment evidence never grants action authority |
| `repeatPolicy` | `DETERMINISTIC` \| `STOCHASTIC` | always | missing/unknown fails closed |
| `repeatsObserved` | integer | always | missing/wrong-typed fails closed |
| `repeatsRequired` | integer | always | missing/wrong-typed fails closed; must equal exactly 1 for `DETERMINISTIC` or exactly 3 for `STOCHASTIC`, else fails closed as inconsistent |
| `captureMode` | `OFFLINE_SYNTHETIC` \| `MOCK_REPLAY` \| `LIVE_REFERENCE_ONLY` | always | missing/unknown fails closed; `LIVE` is never an accepted value |
| `provenanceSourceCommit` | non-empty string | `captureMode: MOCK_REPLAY` | missing/empty fails closed |
| `provenanceExpiry` | strict ISO-8601 date-time | `captureMode: MOCK_REPLAY` | missing/malformed fails closed; must be strictly after `evaluationClockIso`, else fails closed as stale/expired |
| `evaluationClockIso` | strict ISO-8601 date-time | `captureMode: MOCK_REPLAY` | missing/malformed fails closed |
| `citedAsLiveProof` | boolean | optional | `true` on any of the three offline-tranche capture modes fails closed as a live overclaim |
| `baselineRole` | `WITH` \| `WITHOUT` \| `NONE` | optional | unknown value fails closed |
| `baselineEquivalent` | boolean | `baselineRole: WITH` or `WITHOUT` | missing is never treated as success; only an explicit `true` admits the pair, else fails closed as `NONEQUIVALENT_BASELINE_PAIR` |
| `reviewArtifactPath` | non-empty string | always | missing/empty fails closed |
| `claimBoundary` | non-empty string | always | missing/empty fails closed |

No field in this schema is validated by truthiness alone: an absent field,
an explicit `false`, and an explicit `0`/empty string are three distinct
conditions, and each is checked by its own explicit rule so that a missing
required field can never silently pass because Python or JavaScript would
otherwise treat it as falsy-equivalent to a deliberate negative value.

## Result And Defect Vocabulary

| Result | Meaning |
|---|---|
| `PASS_WITH_EVIDENCE` | all required repeats passed; no defect was found |
| `FAIL_WITH_DEFECTS` | at least one non-repeat-count defect was found |
| `INCOMPLETE_TRACE` | a required trace event or output observation is missing |
| `UNDECLARED_TOOL_USE` | the trace used a transition outside the fixture's allowed-transition table |
| `STALE_REPLAY_PROVENANCE` | a mock/replay trace is expired, provenance-less, or source-hash-mismatched |
| `NONEQUIVALENT_BASELINE_PAIR` | a WITH/WITHOUT pair does not share byte-identical canonical input bytes |
| `INSUFFICIENT_REPEAT_EVIDENCE` | a stochastic fixture has fewer than three consecutive passing repeats |

`DECISION_CONTEXT_MISMATCH` is a fail-closed defect class under
`FAIL_WITH_DEFECTS`: the trace and fixture describe the same source but not
the same decision state. It is deliberately not a separate top-level result,
so this refinement does not expand the established seven-result admission
vocabulary.

## Dependency Direction (Unchanged From G3 T1)

```text
this behavioral evaluation contract (NEW)
        |
        | supplies evidence into
        v
ASSF certificationState / uatState / acceptanceEvidence (EXISTING)
        |
        | may later be cited as one input by
        v
release-gate bundle (EXISTING) --- provider-lane matrix (EXISTING)
```

The arrow direction is one-way. This contract never reads
`certificationState` to decide its own grading (no self-certification
loop); release gate and provider canary never grant certification on this
contract's behalf.

## TypeScript Implementation Pointer

`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/assf.behavioral.evaluation.contract.ts`
implements this contract as pure, immutable TypeScript types and three pure
functions: `gradeBehavioralEvaluation` (accepts `unknown`-typed runtime
input and fails closed structurally, per rule 10, rather than trusting a
caller-supplied type annotation), `admitFixtureSet` (rule 12), and
`admitBaselinePair` (rule 13). It performs no network call, no credential
read, no provider invocation, and no file I/O; it operates only on
already-constructed fixture and trace objects passed to it in memory. Dates
are validated with a strict ISO-8601 pattern plus calendar-range
reconciliation; `Date.parse` alone is never treated as sufficient
validation, per rule 10.

## Python Evidence Checker Pointer

`governance/compat/check_assf_behavioral_evaluation_evidence.py` is a
read-only checker that validates a supplied package/evidence document pair
against the `## Cross-Language Evidence Schema` above: it fails when a
package declares `uatState: PASSED` under this contract but no cited
governed result proves `PASS_WITH_EVIDENCE`, or when any required
schema field is missing, malformed, unknown, or internally inconsistent
(source/fixture hash, repeat policy/count consistency, capture mode,
replay provenance/expiry under the same strict ISO-8601 rule the
TypeScript grader uses, or baseline equivalence). It does not require
every existing package to adopt this contract and does not mutate any
package entry, the generated index, or certification state.

## R1 Rework Disposition

This contract was reworked under ACEL-G3-T2-R1-CONSOLIDATED-SEMANTIC-REWORK
after the parent tranche's worker return was returned `REWORK_REQUIRED`.
The rework corrected: an unauthorized `LIVE` capture-mode value replaced by
the exact `OFFLINE_SYNTHETIC`/`MOCK_REPLAY`/`LIVE_REFERENCE_ONLY`
vocabulary (rule 6, R1-01); the grader's acceptance of `unknown`-typed
runtime input with explicit fail-closed structural validation for every
field rather than a compile-time-only type contract (rule 10, R1-02); two
new pure admission functions enforcing the positive-plus-negative
fixture-set rule and the WITH/WITHOUT baseline pairing rule, neither of
which the pre-rework grader enforced (rules 12-13, R1-03); and one
documented cross-language evidence schema now shared explicitly by the
TypeScript fixture/trace/result projection and the Python checker, replacing the pre-rework
checker's truthiness-based field checks with explicit presence/type/value
validation for every field (R1-04). The pre-rework implementation also
contained literal NUL control-character bytes in a string-template
delimiter, removed and replaced with an ASCII-safe length-prefixed encoding
(R1-05).

The prior worker return's 29/29 TypeScript and 21/21 Python test counts are
historical pre-rework evidence only and are not evidence of this rework's
correctness; see the paired audit's `## Command Evidence` section for the
current 79/79 and 55/55 counts obtained after reviewer repair and closure.

## Negative Cases (Required, All Present In This Contract)

| Negative case | Contract requirement |
|---|---|
| Self-grading | Runner and grader are separately invokable; a runner-declared `selfReportedPass` field is never trusted by the grader (rule 8). |
| Missing trace | A trace missing a required event or output observation is fail-closed `INCOMPLETE_TRACE` (rule 9). |
| Unknown token/tool use | A trace event outside the fixture's allowed-transition table is fail-closed `UNDECLARED_TOOL_USE` regardless of outcome (rule 3). |
| Replay drift | An expired, equal-to-clock, provenance-less, or source-hash-mismatched mock/replay trace is fail-closed `STALE_REPLAY_PROVENANCE` (rule 6). |
| Unequal WITH/WITHOUT inputs | A WITH/WITHOUT pair with unequal canonical input bytes is fail-closed `NONEQUIVALENT_BASELINE_PAIR` (rule 5) or rejected at admission as `NONEQUIVALENT_INPUT_BYTES` (rule 13). |
| Stochastic under-sampling | Fewer than three consecutive passing repeats on a stochastic fixture is fail-closed `INSUFFICIENT_REPEAT_EVIDENCE` (rule 4); more than the required count is equally rejected under the exact-count rule. |
| Positive-only or negative-only fixture set | A fixture set missing either class is rejected at admission before any individual fixture is graded (rule 12). |
| Missing or same-role baseline pair | A `WITH`/`WITHOUT` fixture with no pair, a same-role pair, or a malformed role is rejected both by explicit admission and on the mandatory grading path (rule 13). |
| Judgment applied to changed state | A trace whose `decisionContextHash` differs from the fixture fails with `DECISION_CONTEXT_MISMATCH` (rule 14). |
| Incomplete candidates without escape | `INCOMPLETE_WITH_ESCAPE` without a non-empty `noMatchOutcome` is malformed and fails closed (rule 15). |
| Probability treated as authority | Any `judgmentAuthority` other than `EVIDENCE_ONLY` is malformed and fails closed (rule 16). |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | this contract, its paired TypeScript grader and Python evidence checker | internal agents may grade an already-produced fixture/trace pair and check evidence admission; this contract grants no loader, resolver, provider, runtime, or registry-mutation authority | this contract; the G3 T1 accepted design; the ASSF-T7 lifecycle guard contract; the ASSF-T1 package contract | no internal checker, loader, resolver, hook, or generated-index change is authorized by this tranche | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external-agent evidence readout | external agents cannot certify, mutate, activate, or execute a package through this contract | Dual Agent Surface Accounting Standard | any implemented CLI/MCP adapter requires a later source-verified adapter contract, tests, and public/private boundary review; this tranche implements none | `DEFERRED_WITH_REASON` |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ACEL G3 T2 behavioral evaluation normative contract authoring only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- contract-definition worker-return lane only |
| receiptEvidence | N/A with reason: no runtime execution, provider call, or adapter receipt exists for this tranche |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- G3 T1 accepted design and this contract's own normative rules |
| invocationBoundary | governed local documentation authoring only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | defines a documentation-only behavioral-evaluation contract composed under ASSF, plus pointers to its paired pure implementation and read-only checker |
| forbiddenExpansion | no certification/index mutation, provider/live call, runtime wiring, public-sync, deployment, or automatic successor tranche |

## Claim Boundary

This contract defines the generic behavioral-evaluation evidence model
only. It does not implement a runtime, provider, or CLI/MCP adapter; does
not mutate any skill, package, registry, or generated-index state; does not
execute any capability, provider, agent, or live path; and does not certify
or decertify any package. Reviewer/closer owns completion review authoring,
roadmap status update, session sync, and any material commit after
acceptance.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this contract references private ASSF provenance architecture and
repository source surfaces. Public-safe export requires a separate
redaction and public-sync authorization.
