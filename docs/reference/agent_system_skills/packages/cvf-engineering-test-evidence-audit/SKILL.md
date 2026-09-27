---
name: cvf-engineering-test-evidence-audit
description: Give an advisory KEEP/REPAIR/CONSOLIDATE/ADD/DEFER_WITH_REASON disposition for one asserted existing-proof claim tied to a named source file and a named test file, by reading the actual test assertions rather than trusting the claim sentence or a docstring. Use when a worker or reviewer needs to check "is this tested" before trusting or extending a coverage claim; not for authoring a new failing test (TDD) or reviewing a diff/PR for defects (code-review).
---

# CVF Engineering Test Evidence Audit

Memory class: FULL_RECORD

Status: APPROVED

docType: assf_package

skillId: cvf-engineering-test-evidence-audit

## Purpose

Give a worker or reviewer an advisory disposition for one asserted
existing-proof claim (a comment, commit message, docstring, or prior
review stating a source file "is tested" or "is covered"), tied to a
specific source file and a specific test file, by reading the actual test
assertions instead of trusting the claim sentence. This body is a compact
route to the accepted content candidate below, not a replacement for its
current text.

## Scope / Applies-To

Use only when the claim under audit names both a source file and a test
file (or test function), or explicitly states no test file is known. The
governing work order and canonical CVF authority always control whether
any edit, test execution, or deletion is authorized; this package never
grants that authority by itself.

## Invocation Boundary

| Field | Value |
| --- | --- |
| Task classes | test-evidence-disposition |
| Roles and phases | worker, reviewer, dispatcher; WORKER_EXECUTION and REVIEWER_CLOSURE |
| Inputs | one asserted existing-proof claim sentence; the named source file path; the named test file path (or an explicit statement that no test file is known, which forces `DEFER_WITH_REASON`) |
| Outputs | one advisory artifact row: target, label, cited evidence, reason, confidence/unknowns, next owner/action; never a test PASS, a deletion permission, or a runtime receipt |
| Risk ceiling | R0 advisory guidance; current CVF review/test authority always controls |
| Exclusions | authoring a new failing test before implementation exists (TDD's trigger); reviewing a diff or PR for correctness/simplification/efficiency defects (code-review's trigger); running, evaluating, or deleting the named test |

## Audit Procedure

1. **Input**: the consumer supplies the asserted claim in one sentence,
   the source file path, and the test file path (or states "no test file
   known," which forces `DEFER_WITH_REASON`).
2. **Locate**: open the source file and the test file, and identify the
   exact function/class the claim is about and the exact test
   function(s) that exercise it. If the named test file does not exist
   or does not reference the named source symbol, stop at
   `DEFER_WITH_REASON` with a no-match reason rather than guessing a
   substitute file.
3. **Read the assertion, not the docstring**: read the actual `assert*`
   calls and fixture setup in the test body. A docstring or comment
   describing intended behavior is not evidence; only executable
   assertions and their concrete fixture values count.
4. **Classify**: select exactly one of the five labels below based on
   what the assertions actually establish, not on what the claim
   sentence asserts they establish.
5. **Artifact**: emit one row -- target, label, cited evidence, reason,
   confidence/unknowns, next owner/action. The row is handed to the next
   owner named in `Next owner/action`; it is not self-executing and
   never becomes a test PASS or a deletion permission by itself.

### Five Advisory Labels

- **KEEP** -- the cited assertions already establish the claim at a
  defensible level of rigor for its stated purpose; no surplus test is
  proposed.
- **REPAIR** -- an existing, clearly relevant test exists, but there is a
  concrete weakness (a vacuous assertion, a missing negative case, a
  wrong-value check); name the exact weakness without deleting the test.
- **CONSOLIDATE** -- two or more existing tests assert overlapping or
  redundant claims; name one keeper and the redundant test(s) by exact
  function name; never delete them directly.
- **ADD** -- a positive confirmation of absence within a defensible,
  stated search boundary (cite what the read locations do cover instead
  of the claim); uncertain absence is `DEFER_WITH_REASON`, not `ADD`.
- **DEFER_WITH_REASON** -- the disposition cannot be reached confidently
  within the current read set or authority (missing test file, ambiguous
  assertion intent, or a file outside allowed scope); preserves
  uncertainty rather than a soft KEEP or REPAIR.

## Risk And Authority

This package grants no test execution, fixture creation, deletion, commit,
provider call, host installation, public sync, or production authority.
Reading or loading this metadata or its accepted content source never
authorizes running the named test or any Git mutation. If the named test
file is missing or the current work order forbids execution, stop at
`DEFER_WITH_REASON` and state the exact blocker; do not infer execution
authority from read access.

## Progressive Disclosure

The registry/index exposes metadata before this body. This body is
`APPROVED`: `uatState: PASSED` and `certificationState: CERTIFIED` per the
five-case source-based review at
`docs/reviews/CVF_CVF_NCR_R1_S06_TEST_EVIDENCE_AUDIT_UAT_CERTIFICATION_2026-09-27.md`,
and `internalAgentDisposition: IMPLEMENTED` grants explicit internal
runtime-loader body-read eligibility only. A P6 approved `STRICT` source
truth packet now exists at
`docs/reference/agent_system_skills/truth/packets/cvf-engineering-test-evidence-audit.json`;
this records source truth only and does not change lifecycle state.
Activation remains denied because this package is not `ACTIVE`. This is
not `ACTIVE` status, resolver activation, automatic invocation, or any
external/live/public/production effect. The accepted content candidate and
its Local completion remain the authoritative source for the five-label
semantics, the adversarial/boundary cases, and the paired-evaluation
design; this body compresses that source and does not add behavior
beyond it.

## Source Provenance

Compressed from the accepted content candidate
`docs/audits/CVF_NCR_R1_S02_TEST_EVIDENCE_AUDIT_CONTENT_CANDIDATE_2026-09-27.md`
and its Local completion
`docs/reviews/CVF_CVF_NCR_R1_S02_TEST_EVIDENCE_AUDIT_CONTENT_COMPLETION_2026-09-27.md`.
The completion's recorded worker scope violation (unauthorized fixture
and `pytest` execution) is excluded from this package's own evidence; it
does not certify or imply that this package may execute tests. P5 UAT and
certification evidence is recorded in
`docs/reviews/CVF_CVF_NCR_R1_S06_TEST_EVIDENCE_AUDIT_UAT_CERTIFICATION_2026-09-27.md`,
which independently re-derived each of the five case dispositions from this
same accepted content source without executing any audited test.

## Claim Boundary

This package root is `APPROVED` with `uatState: PASSED`,
`certificationState: CERTIFIED`, and `internalAgentDisposition: IMPLEMENTED`,
and now carries an approved `STRICT` P6 truth packet. It grants explicit
internal runtime-loader body-read eligibility only. It does not add new
behavior beyond the already-accepted advisory audit procedure, does not
certify repository-wide test coverage, and does not authorize `ACTIVE`
status, resolver activation, automatic invocation, test execution,
deletion, external adapter, host exposure, or provider/live/public/
production effect. It may be opened only through explicit, separately
authorized CVF review under active governed work-order authority.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this package root cites private provenance registry and review
surfaces. Public-safe publication requires separate redaction and
public-sync authorization.
