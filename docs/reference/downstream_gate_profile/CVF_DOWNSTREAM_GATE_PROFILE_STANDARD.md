# CVF Downstream Gate Profile Standard

Memory class: FULL_RECORD

Status: ACTIVE_STANDARD

docType: reference

Date: 2026-10-03

Batch ID: CVF-DGIP-T1

## Purpose

Define the versioned portable control-plane gate profile
`cvf.downstreamGateProfile@1.1.0` that a generated downstream project inherits
from CVF Core: one framework-owned control source, an identity-pinned installed
copy, a phase-to-control applicability map, fail-closed outcomes, truthful
coverage states, a conditional reviewer-local repair route, and a bounded
project-to-parent finding intake. It extends the Golden Downstream Bootstrap
learning and the Workspace Governance Learning Propagation closure; it reopens
neither and creates no second automatic-learning framework.

## Scope / Applies To

Applies to projects bootstrapped by `scripts/new-cvf-workspace.ps1` (fresh
projects receive the profile), to the workspace doctor and new-project
aggregate, and to the portable runner in `scripts/lib/downstream_governance/`.
Pre-existing projects are inventoried and receive an explicit migration gap
(`docs/reference/downstream_gate_profile/CVF_DOWNSTREAM_GATE_PROFILE_MIGRATION.md`);
their history and project-owned content are never rewritten. Core
`check_session_mode_consistency.py` remains the Core-schema checker and is not
reused for the downstream schema.

## Owner Responsibility And Source Authority

| Responsibility | Owner |
|---|---|
| Profile, runner, modules, schemas, CI and hook templates | CVF Core: `scripts/lib/downstream_governance/` and this folder |
| Work-order status grammar and closeability contract | `governance/compat/check_gate_to_role_closeability.py`, installed into projects by content pin |
| Reviewer-local repair tokens and rule | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` |
| Finding-to-learning lanes, defect classes, dispositions | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` |
| Project-owned content (state, handoffs, work orders, reviews) | The project; the profile reads it and never rewrites it |

A project copy is never an independent definition: it is valid only while its
LF-normalised SHA-256 matches `.cvf/gate-profile.lock.json` and, under the Core
doctor (`--trusted`), the Core source.

## Reconciliation With Existing Learning

| Existing owner | Disposition | Reason |
|---|---|---|
| `CVF_GOLDEN_DOWNSTREAM_BOOTSTRAP_LEARNING_INTAKE_2026-07-23.md` (executable drift and golden proof) | EXTENDS_EXISTING | The catalog drift coverage there does not close continuity/dispatch inheritance; this profile adds those controls and keeps the golden-project method. |
| `docs/roadmaps/CVF_WORKSPACE_GOVERNANCE_LEARNING_PROPAGATION_ROADMAP_2026-08-05.md` | EXTENDS_EXISTING | Closed GLP propagation of carrier text; the reviewer-routing projection is added to the same template without reopening that closure. |
| ADIF-0026 (sequential reviewer finding cascade, review cost) | EXTENDS_EXISTING | The reviewer-local repair route is the parent rule being projected downstream. |
| ADIF-0052 (continuity pins and post-mode literal) | EXTENDS_EXISTING | Same continuity-pin class, applied to the generated project schema. |
| ADIF-0058 (authoring pass mistaken for worker-release readiness) | INDEPENDENT_REASON | It covers dispatch-release readiness in Core, not status-grammar applicability or inherited-gate invocation; no ADIF ID is assigned here. A new ID, if warranted, goes through the existing ADIF registry route. |
| ADIF-0050 (public repository used as authoring source) | NOT_A_DUPLICATE | Different defect; consulted for the private/public boundary, which stays `DEFERRED_PRIVATE_ONLY`. |

## Phase And Control Applicability Map

Profile1.1 extends the closed profile1.0 with a shared project learning home and
two pinned Core templates. See `CVF_PROJECT_LEARNING_LOOP_STANDARD.md` and
`CVF_BUILD_LEARNING_EVIDENCE_CHECKLIST.md`. `CVF-DG-INST-01` additionally requires
nonempty learning README/template inside the project. Project-authored records
remain editable and are preserved; learning quality/admission is a Local decision.

Phases: `bootstrap` (doctor and new-project aggregate), `pre-dispatch`,
`worker-return`, `reviewer-fast`, `pre-commit`, `pr-ci`. Controls are mandatory; a
project may only add `LOCAL-*` controls. `reviewer-fast` is implemented as a runner
phase with every review-relevant control (`run --phase reviewer-fast`), not a token.

| Control | Meaning | Phases |
|---|---|---|
| CVF-DG-INST-01 | pinned profile/runner/bundle identity on actual bytes, lock integrity, unexpected files, override refusal | all six |
| CVF-DG-CONT-01 | state, handoff, memory and implementation-status consistency, active-handoff status, active work orders | all six |
| CVF-DG-RANGE-01 | candidate range resolution; refuses instead of emptying discovery | pre-dispatch, worker-return, reviewer-fast, pre-commit, pr-ci |
| CVF-DG-APPL-01 | strict work-order status applicability and closeability | pre-dispatch, worker-return, reviewer-fast, pre-commit, pr-ci |
| CVF-DG-ROUTE-01 | reviewer-local repair envelope before REWORK | pre-dispatch, reviewer-fast, pr-ci |
| CVF-DG-ROLE-01 | declared Risk grammar and R2/R3 reviewer independence | worker-return, reviewer-fast, pre-commit, pr-ci |
| CVF-DG-CLAIM-01 | gate claims limited to evidenced states, declarations collected before parsing | worker-return, reviewer-fast, pre-commit, pr-ci |

## Candidate Range

Discovery must never silently become empty. `pr-ci` requires a base (`--base` or
`--base-from-env CVF_DG_BASE`; the generated workflow binds it to the pull-request base or
the push `before` SHA with `fetch-depth: 0`). The range is the merge base to the checked-out
HEAD; an all-zero base (new branch) uses the empty tree so every file is a candidate. A
missing, unresolved, shallow-unavailable, unrelated-history or non-checked-out range is
refused (`RANGE_*`). Renames check the new path; deleted candidates are listed as not
checked. A resolved range with no candidates reports `RANGE_EMPTY_CHECKED`. Local phases
without a base use the worktree scope and say so (`WORKTREE_SCOPE`).

## Fail-Closed Outcomes

Outcomes are `PASS`, `FAIL`, `NOT_APPLICABLE_WITH_REASON`,
`BLOCKED_MIGRATION_REQUIRED` and `BLOCKED_INVALID_INPUT`. Only `PASS` and
`NOT_APPLICABLE_WITH_REASON` exit 0, and `NOT_APPLICABLE_WITH_REASON` is valid
only with a non-empty reason and the list of control IDs that were actually
checked. A missing, empty or tampered runner, profile, lock or inherited module,
an environment or local-profile override, an unparseable input, or any internal
runner error is non-zero. Exit codes: 0 pass, 2 gate failure, 3 blocked.

## Continuity Contract

`cvf.downstreamContinuityContract@1.0.0` pins the generated project schema
(state `schemaVersion 1.0`, implementation status `1.0`), not the Core state
layout. Compared fields: state `currentMode`/`activePhase`/`activeRole`/
`nextAllowedMove`/`activeHandoff`, handoff `## Current State` labels, memory
`## Current Truth` labels, and `IMPLEMENTATION_STATUS.currentPhase`. The mode to
phase map is the identity for the seven phases plus `REVIEW_PENDING` which maps to
phase `REVIEW`. Missing, duplicate, conflicting or unknown fields (outside the
`x-`/`x_` extension prefix), an active handoff that does not carry exactly one
unfenced `Status: ACTIVE` declaration (ACTIVE plus ARCHIVED, duplicates and a
malformed value refuse; a fenced example and an archived handoff are preserved), a second
ACTIVE handoff, active work orders before the WORK_ORDER phase, an incomplete
`activeTranche` triple, and any `activeWorkOrders` entry that is missing, duplicated,
not a `docs/work_orders/*.md` path or not an admitted active status under the shared
grammar (DRAFT, HOLD, closed and unknown refuse) are failures with field-specific locators. A state without `continuityContract` is
`BLOCKED_MIGRATION_REQUIRED`, never a pass and never rewritten.

## Applicability Grammar

`cvf.workOrderStatusGrammar@1.0.0`: a candidate work order declares exactly one
`Status: TOKEN` or `Status: TOKEN (annotation)` line. Blank, duplicate,
contradictory, lowercase, free-suffix and unknown values are rejected on a
candidate; explicit not-applicable families (closed, held, draft, reviewer
dispositions, dispatched) return a reason and the checked control IDs and are
never reported as a closeability PASS. Unchanged historical artifacts and
non-work-order files are not migrated.

## Install, Pin And Invocation

Bootstrap installs `scripts/cvf_gates/`, `.cvf/gate-profile.lock.json`, the PR
workflow `.github/workflows/cvf-downstream-gates.yml` (preserved if
project-owned) and a pre-commit template. A YAML token or file presence is not
executed CI evidence.

Trust anchors, stated explicitly:

| Anchor | Controlled by | What it establishes | What it does not |
|---|---|---|---|
| INDEPENDENT_CORE: the Core checkout runs `run --trusted` (doctor, aggregate) | the workspace operator, outside the project repository | every project byte equals the Core source and no unexpected file exists, verified before any project module is imported (Core code only) | a replaced Core entrypoint or Core checkout |
| CI_BUNDLE_PIN: profile, runner and bundle digests in the generated PR command | the project repository writers, through the reviewed PR | the project's own runner compares them with the actual bytes of its directory (stage 0, stdlib only) before importing any sibling module, so a consistent module-plus-lock edit is refused; `pr-ci` without all three pins is refused | an independent trust root: a PR author can edit the workflow too; hosted execution is not observed here |

The lock is editable project metadata: expected pins are compared with actual bytes, never
with lock fields, and the lock's own per-file hashes bind nothing independently. The bundle
digest covers every file of `scripts/cvf_gates/` (name and LF-normalised SHA-256, ordinal
order), so extra, shadow or cache files change it. Fully replacing the trusted gate, editing
the pins together with a module while the Core doctor is not run, hosted-CI substitution of an
independent Core checkout (deferred) and out-of-band invocation are not intercepted.

## Reviewer-Local Repair Routing

Before REWORK the packet records `reviewerLocalRepairBoundary`,
`reviewerLocalRepairBasis` and the seven assessment fields. REWORK with every
assessment answered "unchanged" and evidence determined fails as
`REWORK_UNJUSTIFIED_REVIEWER_LOCAL_AVAILABLE`; a boundary token must be backed
by at least one matching "changed" answer. The machine validates the decision
envelope, not whether a repair is semantically small, and forces no provider or
commit role.

## Finding Intake And Parent Back-Links

`runner intake --finding <json>` writes one deterministic
`docs/learning_intake/<findingId>.intake.json` at the review boundary with
version, source project and SHA, observed and expected behavior, negative
evidence, chain joins, defect class, lane, proposed disposition, candidate
control, claim limits and dedup candidates. It is `NOT_ACCEPTED_GENERATION_ONLY`
with empty `parentLinks`; the parent owner records dedup, admission, accept or
decline and links the resulting work order, checker and golden proof in
`downstream_finding_intake_registry.json`. `validate-intake` checks the complete record:
exact key set, pinned `schemaVersion`/`profileId`/`parentOwner`/`sourceClaimStatus`, every
input field's type and vocabulary, `parentLinks` keys and types, acceptance/disposition
coherence (a pending record has no links; a parent decision needs an equal acceptance and an
`admissionRecord` link) and the content digest. A recomputed digest over deleted or altered
metadata is refused. There is no daemon, scanner, remote submission or silent ingestion.

## Coverage And Claims

Per phase and control the readout is `INSTALLED` (identity-verified files),
`INVOKED` (a receipt bound to the installed identity), `PROVEN_HERMETIC` (a Core
golden-proof receipt bound to the installed identity), `NOT_APPLICABLE_WITH_REASON`
or `BLOCKED`. Declarations are collected first and parsed second: `Risk` is exactly one of
`R0`-`R3` (a role-bearing review without it is refused), role and `Gate claim` labels are
case-exact, and a malformed, duplicated or trailing-text claim is refused instead of
disappearing; fenced examples are not declarations. Hosted CI is never inferred. Doctor and bridge output state their
scope instead of a blanket readiness claim. Real adoption of a downstream
project, a hosted PR run and public rollout are `DEFERRED_PRIVATE_ONLY` and need
separate admission.

## Hermetic Proof Requirements

The proof is an offline disposable project built from a local fresh clone plus a
declared staged candidate overlay with recorded raw and normalised identities,
bytecode disabled, bootstrap run twice with project-owned content preserved,
positive control, negative mutations (each truth surface, malformed status,
self-review, unsupported claim, unjustified REWORK, tampered or no-op gate),
LF and CRLF checkout variants, and failure propagation through the doctor,
aggregate and the PR command. Actual Linux or hosted execution that is not
available is recorded `NOT_EXECUTED_PLATFORM_UNAVAILABLE`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

Pure file-based control-plane checks and hermetic tests. No claim about live AI
governance, provider behavior, hosted CI, Linux execution, real-project adoption,
public rollout or production enforcement.
