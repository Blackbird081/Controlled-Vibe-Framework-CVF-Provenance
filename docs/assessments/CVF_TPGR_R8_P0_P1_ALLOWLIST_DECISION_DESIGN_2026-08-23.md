# CVF TPGR-R8 P0/P1 Allowlist Decision Design

Memory class: governed-planning-assessment

docType: baseline

Status: COMPLETE_PENDING_REVIEW

Batch ID: TPGR-R8

Date: 2026-08-23

executionBaseHead: `1a149b3a62d92d7b7805b0098fab52bd36720193`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R8_P0_P1_ALLOWLIST_DECISION_DESIGN_2026-08-23.md`

Paired baseline authority:
`docs/baselines/CVF_GC018_TPGR_R8_P0_P1_ALLOWLIST_DECISION_DESIGN_2026-08-23.md`

## Purpose

Define a deterministic, evidence-bound P0/P1 allowlist decision model for the
six accepted R7 documentary cases. `P0` means only a candidate for a future
lighter route under separate authority. `P1` means the full legacy bundle is
required. Because R8 activates nothing, both classes continue to execute the
unchanged full legacy bundle and `selectiveExecutionAuthorized` remains
`false`.

## Source / Predecessor Evidence

| Source | Identity | Authority use |
|---|---|---|
| paired R8 baseline | `docs/baselines/CVF_GC018_TPGR_R8_P0_P1_ALLOWLIST_DECISION_DESIGN_2026-08-23.md`; SHA-256 `4dd26d44651f891bea561feb499666d97725fa2b43ece136be0a38b3de61313d` | R8 design boundary and acceptance thresholds |
| paired R8 work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R8_P0_P1_ALLOWLIST_DECISION_DESIGN_2026-08-23.md`; SHA-256 `0a35879278264821c5699f25238e6748348f24f9b1953cdfeb79971320f8c533` | exact worker contract and two-path manifest |
| accepted R7 assessment | `docs/assessments/CVF_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_2026-08-18.md`; accepted material commit `723382cfc373f8da8971326733f0ed4c074066f1` | C1-C6 documentary comparator cases, mismatch and rollback design |
| accepted R7 worker return | `docs/reviews/CVF_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_WORKER_RETURN_2026-08-18.md`; accepted material commit `723382cfc373f8da8971326733f0ed4c074066f1` | bounded worker evidence and independent acceptance context |
| accepted R6 assessment | `docs/assessments/CVF_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_2026-08-18.md` | H1-H6 historical bounded evidence |
| R6 reviewer binding | `docs/reviews/CVF_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_WORKER_RETURN_2026-08-18.md`, Independent Reviewer Addendum | H3 stays strict until current identity is freshly proven |
| TPGR routing standard | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | T0 legacy full-gate interlock and no selective execution |
| canonical command catalog | `governance/compat/agent_autorun_command_catalog.py` | sole legacy command-universe identity owner |

## Scope / Methodology

The worker captured a clean `executionBaseHead`, read every Required First
Read and applicable checker source, and ran both required preflight commands
before authoring. Each C1-C6 case was evaluated by a conjunction of admission
predicates rather than by confidence, cost, or file count. Evidence-state
labels are kept separate: `OBSERVED_CURRENT`, `HISTORICAL_BOUNDED`,
`DESIGN_TIME_EXPECTATION`, `PROJECTED`, and `UNKNOWN` are never interchangeable.
No current R7 dual-run observation exists, so design expectations are not
promoted into observations. An empty P0 candidate set is a valid result.

## Closed P0/P1 Vocabulary

| Class | Documentary meaning in R8 | Execution behavior in R8 | Fail-closed rule |
|---|---|---|---|
| `P0_CANDIDATE_ONLY` | exact identity has met every future-light-route admission predicate | unchanged full legacy bundle | absence of separate activation authority prevents all suppression, reorder, skip, or shortening |
| `P1_FULL_LEGACY_REQUIRED` | one or more predicates are unmet, unknown, stale, partial, contradictory, expired, or ineligible | unchanged full legacy bundle | missing or ambiguous facts select P1 |

P0 is not an active route, exemption, waiver, command list, or permission.
P1 is the only current decision for C1-C6. R8 creates no executable allowlist.

## Exact Eligibility Identity

An eligibility identity is valid only when all components below are present,
exact, current, immutable in the decision record, and independently confirmed.

| Component | Exact binding rule | Failure result |
|---|---|---|
| eight classification dimensions | exact values for `taskKind`, `authorityImpact`, `externalEffect`, `dataSensitivity`, `reversibility`, `sourceScale`, `delegation`, and `novelty` | P1 |
| path families | workspace-relative forward-slash paths, de-duplicated and sorted by ordinal code-point order; no prefix widening | P1 |
| claims | exact closed claim strings and their owners; no implied or aggregate claim | P1 |
| required proof | exact proof item set and evidence references | P1 |
| route receipt identity | schema version, exact manifest digest, base/head range, router/registry/schema identities, receipt status, selected profile, and legacy disposition | P1 |
| legacy command-catalog identity | phase, stable command-row keys, serialized arguments, and catalog blob identity from `agent_autorun_command_catalog.py` | P1 |
| checker semantic identities | every applicable checker path plus its semantic dependency closure identities, not filenames alone | P1 |
| confirming reviewer identity | reviewer role, artifact path, immutable artifact hash, reviewed evidence range, and disposition | P1 |
| evidence hashes | hashes for every admission input, including comparator and review artifacts | P1 |
| freshness and expiry | captured-at time, explicit expiry time, current source/owner/checker/catalog comparison, and no intervening invalidation | P1 |

Any missing field, additional path/claim, set-order ambiguity, identity drift,
stale dependency, hash mismatch, or widened scope deterministically creates a
different identity and selects P1. Identity equality is exact, not semantic
similarity.

## Deterministic Admission Predicates

`P0_CANDIDATE_ONLY` requires the conjunction `A1 && A2 && ... && A11`:

| ID | Predicate |
|---|---|
| A1 | the Exact Eligibility Identity is complete and matches current sources byte-for-byte/field-for-field |
| A2 | the H3/C3 identity binding is current and independently proven under the R6 reviewer repair |
| A3 | complete R7 comparator evidence exists for the exact case and identity |
| A4 | both comparator sides are labeled `OBSERVED_CURRENT`, not projected, expected, historical-only, or unknown |
| A5 | comparison disposition is exactly `EXACT_AGREEMENT` |
| A6 | mismatch, unknown, partial, timeout, malformed, contradiction, stale, and drift counts are all zero |
| A7 | no P3/P4 trigger, protected path, state, auth, persistence, dependency, network, live, public, destructive, or irreversible effect is present |
| A8 | legacy command universe and every checker semantic dependency remain unchanged |
| A9 | independent reviewer confirms exact identity, evidence, decision, expiry, and re-entry fields |
| A10 | evidence is unexpired and no revocation trigger has fired |
| A11 | the case scope is single-class and exactly bounded; no cross-class or authority contamination exists |

A separate future activation authority is deliberately not an admission
predicate: P0 is a candidate decision that must be computable before an
operator can decide whether activation design is justified. Even when A1-A11
all pass, P0 remains documentary and the full legacy bundle continues until a
separate fresh activation authority exists. A4 is unmet for every C1-C6 case
because R7 supplied design-time/projected comparisons rather than observed
current dual-run results. Thus no case can enter P0 now. A proposed threshold
unsupported by accepted evidence remains unmet; it is not waived.

## C1-C6 Decision Table

| Case | R7 posture | Accepted evidence state | Current observation state | Predicate result | allowlistClass | admissionReason | Execution |
|---|---|---|---|---|---|---|---|
| C1 / A1 new upstream corpus | full first-intake floor | `HISTORICAL_BOUNDED` for H1 legacy cost; `DESIGN_TIME_EXPECTATION` and `PROJECTED` for R7 comparator | `UNKNOWN` - no current dual-run receipt | A4 unmet | `P1_FULL_LEGACY_REQUIRED` | no observed exact agreement; first-intake and zero-divergence floors remain binding | full legacy bundle |
| C2 / A2 mixed-origin synthesis | dual-origin and semantic-reading controls | `HISTORICAL_BOUNDED` for H2; `DESIGN_TIME_EXPECTATION`/`PROJECTED` for comparator | `UNKNOWN` | A4 unmet | `P1_FULL_LEGACY_REQUIRED` | design agreement cannot prove current comparator agreement | full legacy bundle |
| C3 / A3 accepted-corpus cluster | `ESCALATE_FOR_REVIEW` until exact current H3 identity | `HISTORICAL_BOUNDED` reuse value; binding reviewer repair; `PROJECTED` comparator | `UNKNOWN`; current C0-C2 identity not proven by R8 | A2 and A4 unmet | `P1_FULL_LEGACY_REQUIRED` | stale H3 identity can never light-route; no copied receipt re-earns currency | full legacy bundle |
| C4 / A4 upstream delta | full verification from earliest affected node | `HISTORICAL_BOUNDED` H4 delta evidence; `DESIGN_TIME_EXPECTATION`/`PROJECTED` comparator | `UNKNOWN` | A4 unmet | `P1_FULL_LEGACY_REQUIRED` | no observed current exact agreement for the exact delta identity | full legacy bundle |
| C5 / A5 advisory item | ambiguity escalates; small size never downgrades | `HISTORICAL_BOUNDED` H5; `DESIGN_TIME_EXPECTATION`/`PROJECTED` comparator | `UNKNOWN` | A4 unmet | `P1_FULL_LEGACY_REQUIRED` | advisory evidence and projected agreement do not establish current authority identity | full legacy bundle |
| C6 / A6 downstream project source | registration never promotes CVF authority | `HISTORICAL_BOUNDED` H6; `DESIGN_TIME_EXPECTATION`/`PROJECTED` comparator | `UNKNOWN` | A4 unmet | `P1_FULL_LEGACY_REQUIRED` | no current dual-run observation and authority-promotion boundary remains absolute | full legacy bundle |

Decision totals: P0 = 0/6; P1 = 6/6. Unobserved cases selecting P1 =
6/6. Design-time/projected agreement promoted to observed = 0. Empty P0 is
accepted as the evidence-correct outcome, not treated as tranche failure.

## Immutable Decision Record

Each future decision is a documentary record, never a registry or store, with:
`decisionCaseId`, exact `eligibilityIdentity`, identity/evidence hashes,
`evidenceState`, `allowlistClass`, every predicate result, `admissionReason`,
reviewer identity, `decidedAt`, `expiresAt`, `expiryState`, `revocationTier`,
preserved prior evidence, and exact `reentryProof`. Serialization has no
execution semantics. Records are append-only evidence; revocation preserves
the prior record and adds a new decision rather than overwriting history.

## Expiry, Revocation, Rollback, And Re-entry

| Event | Detection | Tier and result | Preserved evidence | Re-entry proof |
|---|---|---|---|---|
| expiry reached or cannot be evaluated | current time is at/after `expiresAt`, or expiry field is missing/malformed | Tier 2 only for an exactly bounded single class; otherwise Tier 1; P1 immediately | expired record and hashes | fresh full identity and observed comparator proof plus independent review |
| exact dependency drift | owner, source, catalog, checker closure, reviewer, path, claim, or proof identity changes | Tier 2 only when exact closure is independently bounded; otherwise Tier 1 | pre-drift record plus drift fact | recompute from earliest affected node; no timestamp-only refresh |
| ambiguous or cross-class scope | class/dependency blast radius cannot be proven exact or touches multiple classes | `TIER_1_GLOBAL`: advisory-off and full legacy for all affected/in-flight cases | all records and contradictory evidence | fresh R6/R7-shaped proof for every affected identity and reviewer confirmation |
| protected/state/runtime/live/public/destructive trigger | classification or changed scope includes any P3/P4 trigger | `TIER_1_GLOBAL`; P0 candidacy revoked | triggering manifest/diff and prior decision | fresh higher-governance dispatch; R8 proof alone cannot re-enter |
| exact class-local defect | one class and its complete dependency closure are proven isolated before execution influence | `TIER_2_CLASS_SCOPED`; that class returns to P1 | class record and isolation proof | fresh exact proof for that class plus independent review |
| any command influence | P0 text suppresses, reorders, skips, shortens, or adds enforcement | `TIER_1_GLOBAL`; restore advisory-off/full legacy | attempted influence and full command evidence | fresh root-cause correction and full proof; separate operator authority |

Tier 1 is the default whenever Tier 2 eligibility is ambiguous. Re-entry never
accepts copied receipts, path equality, role labels, confidence, or a renewed
timestamp as freshness proof.

## Hostile Admission Cases

| ID | Hostile input and detection | P1 outcome and preserved evidence | Revocation / visibility | Exact re-entry proof |
|---|---|---|---|---|
| H-A1 identity drift | any of the eight dimensions or evidence hashes differs | P1; preserve old/new identities and diff | Tier 2 only if exact single class, else Tier 1; name changed component to operator | fresh complete identity, comparator evidence, and independent review |
| H-A2 semantic drift under stable filenames | checker dependency-closure hash or catalog serialized arguments change while path/key stays stable | P1; preserve both semantic closures | Tier 2 if closure exact, else Tier 1; explicitly flag misleading name stability | recompute affected proof from current source and review it |
| H-A3 stale reviewer binding | review hash/range/role no longer matches, or H3 current identity is unproven | P1; preserve stale review as historical only | Tier 1 for confirming-review ambiguity; operator sees exact stale leg | fresh identity-bound review of the exact evidence range |
| H-A4 partial receipt | missing/malformed/timeout field or one comparator side absent | P1; preserve partial bytes labeled partial | Tier 1 because completeness/blast radius is unknown | fresh complete receipt and diagnosed cause, independently confirmed |
| H-A5 widened task/path scope | added claim/path/prefix or classification value differs from recorded identity | P1; preserve original and widened manifests | Tier 1 if cross-class/ambiguous, otherwise Tier 2; operator sees added scope | fresh dispatch and full proof for exact widened identity |
| H-A6 protected-path contamination | changed scope touches standard, checker, hook, generator, state, auth, persistence, or other P3/P4 surface | P1; preserve diff and classification | Tier 1; explicit protected trigger shown | separately authorized elevated tranche; no R8 shortcut |
| H-A7 contradictory comparator state | summary says agreement while receipt says mismatch/unknown, or sides conflict | P1; preserve both records verbatim | Tier 1; contradiction displayed side by side | explicit source-authority reconciliation plus fresh full dual-run proof |
| H-A8 expiry | `expiresAt` passed, absent, malformed, or unverifiable | P1; preserve expired record | Tier 2 only when exact single class, else Tier 1; expiry visible | fresh evidence and review; timestamp-only renewal forbidden |

Hostile coverage: 8/8 fail closed to P1; 0/8 can activate or alter legacy
execution.

## Negative-Test Design

| ID | Test design | Expected outcome |
|---|---|---|
| N1 | serialize a P0 candidate beside the command catalog and attempt to omit one command | omission rejected; full legacy bundle unchanged |
| N2 | reorder or shorten legacy commands using a P0 label | rejected; P0 has no execution semantics |
| N3 | submit an ordinary P1 record | all phase-appropriate legacy commands remain required |
| N4 | submit unknown, partial, malformed, or timeout comparator evidence | deterministic P1, never agreement |
| N5 | submit C3/H3 with exact scope but stale reviewer/receipt identity | deterministic P1; binding H3 escalation retained |
| N6 | keep checker filenames stable while changing a semantic dependency | drift detected and P1 selected |
| N7 | include a protected path or P3/P4 trigger in an otherwise eligible identity | P1 plus Tier 1 revocation |
| N8 | advance beyond `expiresAt` and reuse the old hash set | P1; expired evidence cannot be refreshed by timestamp |
| N9 | provide ambiguous class-local isolation for revocation | promote to Tier 1 global reversion |
| N10 | feed a serialized decision record to a hypothetical executor | no action is produced; record is inert documentary data |
| N11 | quote the Zero-Edit R9 Candidate Manifest as activation authority | rejected; R9 text grants no implementation or activation authority |
| N12 | present R7 design-time expected agreement as `OBSERVED_CURRENT` | rejected as evidence-state promotion; P1 retained |

Negative-test coverage: 12/12 designs have fail-closed expected outcomes;
none is implemented or executed here.

## Cost And Value

| Cost/value category | Evidence state | R8 determination |
|---|---|---|
| unavoidable legacy execution | `OBSERVED` as current gate execution for this local governance workflow and `HISTORICAL_BOUNDED` for R6 archetype examples | still mandatory for P0 and P1 in R8; never counted as a saving |
| classification | `PROJECTED` per future decision record | one exact-identity evaluation; no measured recurring value claimed |
| identity verification | `UNKNOWN` / `PROJECTED` | current per-case dual-run identity cost is unmeasured |
| comparison | `UNKNOWN` / `PROJECTED` | no real C1-C6 dual run exists |
| independent review | `OBSERVED` only as an R8 workflow requirement; future per-decision cost is `PROJECTED` | reviewer confirmation remains mandatory |
| expiry maintenance | `PROJECTED` | periodic freshness work exists by design; no saving asserted |
| revocation and re-entry | `PROJECTED` | cost depends on earliest affected node and blast radius |
| future activation/implementation | `UNKNOWN` | no implementation is authorized, scoped, or costed as a current saving |
| value of empty P0 | `OBSERVED` documentary result | prevents unsupported evidence promotion; not an execution saving |

No projected value is presented as observed. No projected saving is an
admission or activation reason.

## Zero-Edit R9 Candidate Manifest

| Possible future path/surface | Candidate purpose | Prerequisite | Authority state |
|---|---|---|---|
| `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | potentially document a reviewed activation/rollback authority contract | independent R8 closure, non-empty observed evidence if P0 is proposed, fresh operator dispatch, P3 governance | NOT_AUTHORIZED |
| a future allowlist decision checker under `governance/compat/` | validate exact identity, expiry, and fail-closed P1 selection | exact implementation work order, checker tests, independent review, protected-path authority | NOT_AUTHORIZED |
| a future inert decision-record schema under `governance/compat/` | validate documentary record shape without executing it | owner decision, collision check, implementation design, tests | NOT_AUTHORIZED |
| a future dual-run comparison harness under `governance/compat/` | collect observed comparator evidence while legacy remains controlling | separately authorized harness design, safety proof, test plan, and operator checkpoint | NOT_AUTHORIZED |
| command catalog, registry, hook, config, store, runtime, or CI wiring | no R8 change proposed | new elevated work order and independent evidence | NOT_PROPOSED |

This manifest edits or creates none of those surfaces. R9 remains a fresh
operator decision after independent R8 closure; candidate text grants no
activation, selective execution, canary, or implementation authority.

## Acceptance Threshold Reconciliation

| Threshold | Result |
|---|---|
| C1-C6 decisions with evidence labels | PASS: 6/6 |
| unobserved/stale/unknown/partial/conflicting selects P1 | PASS: 100% |
| projected/design-time promoted to observed | PASS: 0 |
| protected/state/runtime/live/public/destructive enters P0 | PASS: 0 |
| hostile cases fail closed | PASS: 8/8 |
| negative-test designs with outcomes | PASS: 12/12 |
| ambiguous revocation scope selects Tier 1 | PASS: 100% |
| legacy suppression/reorder/skip or added enforcement | PASS: 0 |
| deterministic decision/expiry/revocation/rollback/re-entry fields | PASS |
| cost classes separated; projected saving presented as observed | PASS; 0 promotions |
| zero-edit activation-neutral R9 manifest | PASS |
| exact changed manifest and no commit | pending final command evidence in paired worker return; designed for exactly two untracked outputs |

## Evidence / Verification

Preflight route verification was `COMPLIANT`, reported selective execution
false, full legacy disposition, and zero violations. Pre-implementation
autorun passed 80/80 before the first edit. Final worker-return, route,
pre-implementation, whitespace, and status evidence is recorded in the paired
worker return and remains subject to independent reviewer reproduction.

## Findings / Position

R8 yields an empty P0 set and six P1 decisions. That is the only evidence-honest
result because accepted R7 evidence is documentary/projected rather than
observed current dual-run evidence, and H3 additionally lacks current exact
identity proof. The decision model is deterministic and activation-neutral;
all ambiguity, stale/partial evidence, semantic drift, protected scope, and
expiry fail closed to P1.

## Risk / Corrective Action

The main risk is treating accepted design quality as observed execution
equivalence. Corrective action: A4 requires both sides to be
`OBSERVED_CURRENT`, and every current case explicitly records `UNKNOWN` for
that observation. A second risk is treating empty P0 as pressure to weaken a
predicate. Corrective action: empty P0 is explicitly valid and selects the
hold disposition. A third risk is that future candidate-path prose could be
mistaken for authority. Corrective action: every R9 row is `NOT_AUTHORIZED` or
`NOT_PROPOSED`, and this artifact remains inert documentary evidence.

## Decision

`HOLD_EMPTY_P0_ALLOWLIST_PENDING_OBSERVED_DUAL_RUN_EVIDENCE`

## Final Disposition

`HOLD_EMPTY_P0_ALLOWLIST_PENDING_OBSERVED_DUAL_RUN_EVIDENCE`

Rationale: P0 = 0/6 and P1 = 6/6 because no C1-C6 case has accepted
`OBSERVED_CURRENT` dual-run exact-agreement evidence. The deterministic design
is complete, but proceeding to activation/rollback authority design would
misrepresent projected evidence as observed and violate the work order's
thresholds. A later tranche may revisit only after fresh governed observation,
exact identity proof, independent review, and explicit operator authority.

## Claim Boundary

This is a documentation-only P0/P1 decision design. It creates no allowlist,
registry, store, schema, checker, harness, test, fixture, receipt, config,
standard change, hook, CI wiring, or runtime plan. It performs no canary or
selective execution and authorizes no R9, P0/P1 activation, command
suppression/reorder/skip, source intake, provider/network/live action,
public-sync, deployment, production, or destructive effect. Both P0 and P1
continue to run the unchanged full legacy bundle.
