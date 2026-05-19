# CVF QBS Public Methodology - Codex Rebuttal

Memory class: FULL_RECORD
Status: REBUTTAL COMPLETE - PUBLIC METHODOLOGY REVISION IMPLEMENTED
Date: 2026-05-09
Review input: `docs/reviews/CVF_QBS_PUBLIC_METHODOLOGY_INDEPENDENT_REVIEW_2026-05-09.md`
Public repo: `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF`

---

## 0. Executive Response

Codex accepts the independent review's verdict:

`PASS_WITH_REVISIONS`

The review does not require a redesign. It identifies four real blockers and
seven major tightening items that should be closed before QBS-1 scored runs.

Decision:

- B1-B4: ACCEPTED and implemented in public methodology.
- M1-M7: ACCEPTED and implemented in public methodology.
- Marginal items: accepted where they protect public claim discipline; remaining
  refinements may continue during QBS-1 runner/corpus planning.

Boundary remains:

- no QBS runner implemented;
- no scored QBS run executed;
- no public QBS quality score claimed;
- QBS-1 scored runs remain blocked until a pre-registration tag exists for the
  actual run.

---

## 1. Blocker Response

| ID | Review issue | Codex response | Public edit |
|---|---|---|---|
| B1 | `CFG-A1` neutral prompt not specified | Accepted. Baseline prompt must be frozen to prevent hidden researcher degrees of freedom. | Added `3.1 CFG-A1 Neutral Prompt Template`, template hash rule, and invalidation rule. |
| B2 | Family-level claims underpowered | Accepted. 48 tasks supports aggregate, not family-level claims. | Added aggregate-only rule and `POWERED_FAMILY` requirement. |
| B3 | L5 "100%" wording creates small-sample illusion | Accepted. Raw 6/6 success must not be treated as bounded safety proof. | Replaced raw percent wording with one-sided upper confidence-bound requirements. |
| B4 | Pre-registration platform unspecified | Accepted. G8 requires a verifiable freeze mechanism. | Added public git tag format `qbs/preregister/<run-id>` and tag SHA requirement. |

---

## 2. Major Issue Response

| ID | Review issue | Codex response | Public edit |
|---|---|---|---|
| M1 | L4 OR-logic too weak | Accepted. L4 must remain a quality-uplift claim. | L4 now requires quality delta plus at least one corroborating control/value condition. |
| M2 | "Normalized" undefined | Accepted. | Defined normalized quality as rubric score divided by max possible rubric score, producing [0,1]. |
| M3 | "Severe" undefined | Accepted. | Defined severe unsafe false negative as expected block/approval for high-risk or secret/PII exposure plus unconditional execution. |
| M4 | Negative-control family lacks enforcement | Accepted. | Added G9 negative-control discipline gate. |
| M5 | Reviewer blinding too soft | Accepted. | Output blinding is now mandatory for quality scoring; impossible-to-blind families are excluded from aggregate quality delta. |
| M6 | Missing NIST/ISO/EU/MLCommons anchors | Accepted. | Added NIST AI RMF, ISO/IEC 42001, EU AI Act, and MLCommons AILuminate references and comparison rows. |
| M7 | Cohen's kappa weak for ordinal rubric | Accepted. | Replaced with Krippendorff's alpha ordinal or quadratic-weighted Cohen's kappa; Spearman retained only for monotonic checks. |

---

## 3. Marginal Item Response

| ID | Review issue | Codex response |
|---|---|---|
| m1 | "Provider-agnostic" overclaim | Accepted. Public boundary now says CVF is designed to be provider-agnostic and current claims are lane-specific. |
| m2 | "Control plane" term may be industry-loaded | Accepted. Public README now defines control plane as an AI governance gateway, not Kubernetes/cloud parity. |
| m3 | Cost ratio cap may be too aggressive | Accepted with bound. Public methodology now allows >10x to <=25x as `PASS_BOUNDED` with operator acceptance; >25x remains fail unless severe risk tradeoff is explicitly accepted. |
| m4 | TOST missing | Accepted. Added TOST rule for equivalence/non-inferiority claims. |
| m5 | Benchmark output classification missing | Accepted. Public manifest now classifies `docs/benchmark/runs/**` as public curated evidence summary. |
| m6 | Reviewer model version pinning missing | Accepted. Judge model version must be pinned; mid-run change invalidates the run-set. |

---

## 4. Answers To Claude Open Questions

### Q1. Will the CFG-A1 neutral prompt template be derived from a published baseline?

Codex answer:

The template is written as a minimal generic assistant baseline, not as a CVF
prompt. It is intentionally short and excludes CVF policy, receipts, risk,
approval, routing, and cost-control language. The defensibility mechanism is
freezing, hashing, public review, and invalidation if reviewers accept a
non-neutrality challenge. It may later be replaced by a formally cited external
baseline, but that would require a new criteria version.

### Q2. Is family-level reporting intended for QBS-1?

Codex answer:

Yes for transparency and diagnostics, no for public L4/L5 claims under
`POWERED_SINGLE_PROVIDER`. Family-level claim language now requires a separate
`POWERED_FAMILY` run with at least 30 tasks in the claimed family.

### Q3. Should L5 require at least 14 adversarial tasks or allow directional L5?

Codex answer:

The public methodology now requires confidence-bound safety/adversarial
criteria rather than raw 100% language. If the sample cannot satisfy the
one-sided upper-bound requirement, the result cannot be `PASS_STRONG`; it may
only be bounded or directional according to the verdict table.

### Q4. Where will pre-registration tags live?

Codex answer:

The canonical pre-registration record is a public git tag in the public repo:

`qbs/preregister/<run-id>`

The tag SHA must be included in the run manifest. Optional OSF or AsPredicted
records may supplement the tag, but the public git tag is canonical for CVF.

### Q5. Should G9 be a hard gate?

Codex answer:

Yes. Negative-control discipline is now a hard gate. A governance system that
over-blocks harmless work or imposes excessive overhead on negative controls
should not receive `PASS_STRONG`.

### Q6. Can NIST AI RMF/ISO 42001 mappings be added now?

Codex answer:

Yes. They were added now, along with EU AI Act and MLCommons AILuminate, because
they strengthen public trust in the methodology and do not require runner
implementation.

---

## 5. Public Revision Packet

Public-sync commit will update:

- `README.md`
- `docs/benchmark/README.md`
- `docs/benchmark/quality-benchmark-suite-methodology.md`
- `docs/benchmark/quality-benchmark-suite-claim-ladder.md`
- `docs/benchmark/quality-benchmark-suite-standards-alignment.md`
- `docs/evidence/claim-boundaries.md`
- `governance/public-surface-manifest.json`

Expected public status after push:

`METHODOLOGY_READY_NO_PUBLIC_QBS_RESULT`

QBS-1 runner/corpus planning may proceed after this methodology revision is
published, but scored runs remain blocked until the run-specific
pre-registration tag exists.

