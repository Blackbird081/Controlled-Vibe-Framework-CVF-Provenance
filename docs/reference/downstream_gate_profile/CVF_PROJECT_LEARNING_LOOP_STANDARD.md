# CVF Project Learning Loop Standard

Memory class: FULL_RECORD
Status: ACTIVE_STANDARD
docType: reference
Date: 2026-10-04
Batch ID: CVF-PLL-T1

EPISTEMIC_PROCESS_NA_WITH_REASON: normative learning-home/value/state contract;
implementation observations and contradictions belong to the PLL-T1 completion review.

## Purpose

Give each CVF-governed project a shared learning home and a value-filtered route
from use case to CVF and back to use case. Extend the existing Finding-To-Governance
Learning Trigger Standard (F2G); its classes, lanes and dispositions remain authoritative.

## Scope / Applies To

Local project discovery, parent intake and returned adoption. New projects using
`cvf.downstreamGateProfile@1.1.0` receive `docs/reviews/learnings/README.md` and
`LEARNING_RECORD_TEMPLATE.md`. Existing projects adopt through deliberate migration
or `install --upgrade`; historical profile1.0 acceptance is not rewritten.

## Shared Home And Discovery

- Keep reusable observations in Git-backed `docs/reviews/learnings/`. A README
  indexes records and gives read triggers. An empty inventory is valid.
- Bootstrap registers the home in a fresh artifact catalog after the installer
  creates it. Session memory and the generated agent carrier point to the README.
- Read relevant records when the trigger matches: repair, review, command cleanup,
  sync-coverage claim or parent intake. Startup does not require reading all history.
- Provider-private memory is an execution aid, never the sole durable record or
  canonical CVF evidence. Shared project records are advisory until source verification.
- Preserve existing project README, templates and records. The installed Core
  templates are pinned; editable learning contents are not pinned as Core authority.

## Value Admission

Before accepting a project lesson into CVF, Local records all five checks:

| Check | Required evidence |
|---|---|
| Source confidence | source path, revision or exact hash, observation versus attributed claim, unread or unreproduced evidence |
| Reusable mechanism | concrete failure/constraint and why it can recur in other projects |
| Existing coverage | canonical owner and applicable rule/checker; dedup match or reason no match |
| Incremental value | specific standard, template, machine check or earlier gate that changes behavior; no promotion based solely on novelty |
| Bounded proof | meaningful positive/negative evidence for that change, with explicit untested boundaries |

Possible parent decisions are accept, merge into an existing owner, defer or decline,
each with a reason and control link. A covered local execution mistake can be
`RULE_EXISTS`; promote only an evidenced application/discovery gap. Do not create
a parallel intake system for the same defect. Existing F2G disposition and portable
`docs/learning_intake/<id>.intake.json` generation remain unchanged.

## Loopback And Independent States

Track project resolution, parent decision, parent implementation, return delivery
and source-project application separately. Record this trace:

`source path + revision/hash -> parent admission -> control + proof -> returned receipt -> project verification`

Parent acceptance or a merged rule does not prove delivery or project application.
Use `NOT_RETURNED`/`NOT_APPLIED` until receipts exist. An operator-parked project
stays `PARKED_BY_OPERATOR`: keep the parent result available without editing,
testing or migrating that project. Apply future loopback only when unparked.

## Parent Evidence Design Binding

`CVF_PROJECT_LEARNING_PARENT_EVIDENCE_CONTRACT.md` specifies an opt-in typed
parent evidence extension under this standard and existing F2G owners. Its design
separates five value checks, implementation proof, delivery and application
receipts. Legacy entries remain untyped and are never backfilled. Offline structural
validation is implemented in the existing F2G checker through
`governance/compat/parent_learning_evidence.py` and
`parent_learning_evidence.schema.json`; it proves declarations and byte identity,
not semantic acceptance, delivery or project application.

## Machine Binding

### Forward Application Binding (2026-10-09)

New or content-changed Core records under `docs/reviews/learnings/` must declare
exactly one `parentFindingId` joined to typed `parentEvidence.source.evidence`
in the existing parent registry. README/templates/archives are excluded;
unchanged history is not silently backfilled or claimed APPLIED.

An accepted/merged typed finding may declare `learningRecordPath` and
`dispatchBindingRequired: true` as a parent-owned obligation. Its implemented
control must have exactly one `control:` reference. New/content-changed work
orders must bind every active obligation using one fenced
`learning-application-plan-json` block, schemaVersion
`cvf.learningApplicationPlan@1.0.0`, and `bindings` array. Each binding is exactly
`{findingId, control: {path, sha256}, action, verificationPlan}`. Exact registry
control identity and concrete action/verification text are required. A question
about delegation does not expand the invocation scope.

The existing F2G checker invokes `learning_application_binding.validate_changed`
at its already installed pre-dispatch/authoring gates. Missing, malformed,
duplicate, stale or incomplete bindings fail closed. Parent obligations are
governed decisions, not worker-selected requirements. Legacy unchanged orders
remain evidence, not permission to re-execute a spent attempt.

A valid plan is only a declared execution/verification contract. It never creates
an APPLICATION receipt or proves compliance, read comprehension or effectiveness.
The existing typed DELIVERY/APPLICATION receipt contracts still govern lifecycle
claims. F2G reports implementation, resolution, delivery and application counts
separately for valid typed records; invalid/legacy entries cannot inflate them.
Reviewer checks the concrete action and its actual result against the canonical
control, rather than trusting nonempty text. No arbitrary IDE/shell interception
or guarantee about agents outside these gates follows from this mechanism.

`cvf_dg_install.install_learning_home` validates all target boundaries and sources
before creating missing scaffolds. Missing, empty or conflicting existing content
refuses; no silent repair. `CVF-DG-INST-01` checks nonempty discovery/template files
inside the project. An existing lock is verified without implicit upgrade.

This checks structure only. It does not judge lesson quality, intercept arbitrary
shell commands, automatically accept intake or prove agents read the records.

## Evidence Practice

Use `CVF_BUILD_LEARNING_EVIDENCE_CHECKLIST.md` for cleanup, repair/mutation and
sync-coverage lessons. The existing cleanup, diagnostic, epistemic, review-cost,
continuity and claim owners control; this checklist makes their application discoverable.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

Parent standards and disposable file-control proof only. No real-project migration,
CCMA adoption, hosted CI, Linux, provider/runtime governance or public readiness claim.
