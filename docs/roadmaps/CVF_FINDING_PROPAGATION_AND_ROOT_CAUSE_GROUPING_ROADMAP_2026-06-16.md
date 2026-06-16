# CVF Finding Propagation And Root Cause Grouping Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_ACTIVE_AFTER_FPRC_T2

docType: roadmap

Date: 2026-06-16

rawMemoryReleased: false

Roadmap class: governance-foundation-finding-root-cause-grouping

## Purpose

Improve CVF audit readability by grouping repeated artifact-local failures under
their root cause. Even with better authoring patterns, novel errors will still
occur. When they do, CVF should distinguish one root defect from propagated
symptoms, evidence replication, stale sync fallout, and reviewer-repair side
effects.

This roadmap complements the central core/local view roadmap. Central facts
reduce duplicate authoring errors before they occur. Root-cause grouping helps
CVF explain and triage remaining failures after they occur.

## Authorization / Decision

Decision: open a forward-only roadmap candidate for future GC-018. The operator
explicitly requested a continued error-catching roadmap after the central
core/local view refactor direction.

No implementation, checker wiring, public-sync, runtime/provider work, live
API call, credential use, broad legacy scan, or production/public readiness
claim is authorized by this roadmap alone.

## Scope

In scope:

- define a root finding and propagated symptom vocabulary;
- design a small `Root Cause To Propagated Findings` table for completion
  reviews and finding-bearing audits;
- design a checker or reporter that can group finding rows without blocking
  unrelated work too early;
- pilot the grouping on one future finding-bearing governance batch.

Out of scope:

- replacing existing finding-to-governance learning disposition;
- deleting artifact-local guard output;
- claiming semantic truth of the grouping without reviewer judgment;
- runtime/provider/live/public scope;
- retrofitting all historical findings.

## Non-Goals

- Do not suppress artifact-local guard output.
- Do not claim that grouping proves semantic correctness.
- Do not replace reviewer judgment with automatic clustering.
- Do not retrofit all historical findings.
- Do not authorize runtime, provider, public-sync, or broad legacy scan work.

## Design Rule

A batch can have many file-level failures but fewer root defects. CVF evidence
should say which finding is the root cause and which findings are symptoms or
replicated evidence.

Recommended taxonomy:

| Field | Example values |
|---|---|
| `rootFindingId` | `RF-2026-06-16-001` |
| `symptomFindingId` | `SF-2026-06-16-001-A` |
| `defectRole` | `ROOT_CAUSE`, `PROPAGATED_SYMPTOM`, `EVIDENCE_REPLICATION`, `STALE_SYNC`, `REVIEWER_REPAIR_SIDE_EFFECT` |
| `owningArtifact` | roadmap, work order, worker return, completion review, session state, checker output |
| `upstreamCause` | path or root finding ID |
| `blockingLevel` | `BLOCKING`, `REPAIR_REQUIRED`, `ADVISORY`, `N/A_WITH_REASON` |

## Design Control Gate

| Control | Decision |
|---|---|
| Foundation value | High: reduces operator confusion and reviewer triage latency |
| Scope size | Medium; begin with a documentation/table standard before machine grouping |
| Runtime risk | None authorized |
| Latency posture | Root-cause grouping should shorten review, not add broad scans |
| Legacy posture | Not applicable; no legacy content is read or absorbed |
| Claim boundary | Finding grouping aid only; reviewer still owns final judgment |

## Tranche Plan

| Tranche | Status | Purpose | Owner |
|---|---|---|---|
| FPRC-T1 | CLOSED_PASS_BOUNDED | Add root-cause grouping standard, provider-memory learning escape guard, and boundary-prose trigger discipline | Claude worker; Codex reviewer |
| FPRC-T2 | CLOSED_PASS_BOUNDED | Harden provider-memory lesson promotion so reusable lessons in Claude memory or `MEMORY.md` (`NOT_CVF_SOURCE`) require CVF-governed promotion | Codex |
| FPRC-T3 | CANDIDATE_AFTER_T2 | Pilot on one future finding-bearing closure and compare operator readability | Codex reviewer |

## Cross-Lane Queued Follow-Up: AOT-T3 (B11/B12 Machine-Check Hardening)

The PLCS-T3 dispatch authoring session surfaced two repeatable cross-agent
dispatch-authoring traps, now governed as findings B11 and B12 in
`docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`:

- B11: provider-registry trigger phrases in N/A prose force runtime-freshness
  evidence (work-order dispatch quality gate).
- B12: dispatch trace manifests that list not-yet-created execution
  deliverables produce false MISSING_DELIVERABLE failures (agent operation
  trace gate).

Operator decision (2026-06-16): two-layer promotion ("Ca hai"). The
documentation layer is delivered now (this standard, the work-order authoring
addendum, and the PLCS-T3 batch). The machine-check layer for B12 is queued as
a separate AOT-lane tranche:

| Queued tranche | Status | Purpose | Owner | Sequencing |
|---|---|---|---|---|
| AOT-T3 | CLOSED_PASS_BOUNDED | Hardened `governance/compat/check_agent_operation_trace.py` to distinguish dispatch trace manifests from future execution ownership sections and fail `DISPATCH_SCOPE_VIOLATION` when a dispatch Expected manifest lists future execution paths | Codex | Shipped standalone after AHB-T1A cleanup by operator decision; AHB-T2 remains unopened |

B11 stays documentation-only guidance; no B11 code enforcement is queued.
AOT-T3 is additive and does not supersede AOT-T2 manifest enforcement.

## AOT-T3 Closure Evidence (2026-06-16)

Operator selected AOT-T3 as the faster cleanup before AHB-T2.

Status: CLOSED_PASS_BOUNDED.

Artifacts:

- GC-018:
  `docs/baselines/CVF_GC018_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_2026-06-16.md`
- Work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_FOR_CODEX_2026-06-16.md`
- Standard update:
  `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`
- Checker/test update:
  `governance/compat/check_agent_operation_trace.py`
  and
  `governance/compat/test_check_agent_operation_trace.py`
- Completion review:
  `docs/reviews/CVF_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_COMPLETION_2026-06-16.md`

Bounded result: future execution paths listed in work-order ownership sections
remain valid execution intent, but future paths placed in a dispatch trace
`Expected manifest` now fail with `DISPATCH_SCOPE_VIOLATION`.

## Work Plan

1. FPRC-T1 defines the table standard and example root/symptom grouping.
2. FPRC-T1 updates a completion-review template note or reference addendum.
3. FPRC-T2 adds a narrow advisory parser/checker only after T1 closes.
4. FPRC-T3 pilots the table on one future finding-bearing closure.
5. Codex reviews whether the table reduces operator confusion before any hard
   gate is considered.

## FPRC-T1 Superseding Dispatch Record (2026-06-16)

Operator changed the next-move priority before CCLV-T2 worker execution because
two reusable agent-error patterns could recur during CCLV-T2:

- reusable guard lessons recorded only in provider-specific memory instead of a
  CVF-governed learning artifact;
- boundary prose using scan, classification, corpus, receipt, or provider-call
  wording in N/A/out-of-scope explanations, causing keyword-based gates to
  infer the wrong evidence class.

FPRC-T1 is now dispatched before CCLV-T2 resumes.

- Codex priority override audit:
  `docs/reviews/CVF_FPRC_T1_PRIORITY_OVERRIDE_AND_CCLV_T2_PAUSE_AUDIT_2026-06-16.md`
- GC-018:
  `docs/baselines/CVF_GC018_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_2026-06-16.md`
- Work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_FOR_CLAUDE_2026-06-16.md`

Dispatch boundary: foundation guard hardening only. No runtime behavior,
public-sync, historical migration, legacy absorption, or live proof is
authorized.

## FPRC-T1 Closure Evidence (2026-06-16)

Worker: Claude. Reviewer: Codex. executionBaseHead: `ba902737`.
Status: CLOSED_PASS_BOUNDED.

Artifacts delivered and accepted:

- Standard: `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`
- Addendum update: `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md` (FPRC-T1 sections added)
- Checker update: `governance/compat/check_finding_to_governance_learning.py` (provider-memory-only escape guard)
- Focused tests: `governance/compat/test_check_finding_to_governance_learning.py` (12/12 PASS)
- Completion review: `docs/reviews/CVF_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_COMPLETION_2026-06-16.md`

Gate results: focused pytest 12/12 PASS; checker self-run COMPLIANT;
worker-return fast gate PASS; `git diff --check` PASS.

Codex reviewer owns: commit accepted material range, run pre-closure on
committed range, and perform session sync.

## FPRC-T2 Closure Evidence (2026-06-16)

Operator identified a remaining control-loop gap after PLCS-T2: Claude stated
that B7/B8/B9 were written to Claude-only memory and future same-kind work
would be faster, but did not promote those reusable lessons into CVF governance
until prompted.

Status: CLOSED_PASS_BOUNDED.

Artifacts:

- GC-018:
  `docs/baselines/CVF_GC018_FPRC_T2_PROVIDER_MEMORY_LESSON_PROMOTION_HARDENING_2026-06-16.md`
- Standard update:
  `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`
- Addendum update:
  `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md`
- Checker/test update:
  `governance/compat/check_finding_to_governance_learning.py`
  and
  `governance/compat/test_check_finding_to_governance_learning.py`
- Completion review:
  `docs/reviews/CVF_FPRC_T2_PROVIDER_MEMORY_LESSON_PROMOTION_HARDENING_COMPLETION_2026-06-16.md`

Bounded result: `MEMORY.md` is now treated as a provider-local memory signal;
reusable lessons cannot be waived with generic `N/A_WITH_REASON`; B7/B8/B9
authoring traps are written into the standard/addendum.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| FPRC-AC1 | The standard distinguishes root cause from propagated symptoms and evidence replication. |
| FPRC-AC2 | The table does not replace finding-to-governance learning disposition. |
| FPRC-AC3 | Initial checker behavior is advisory or limited to artifacts that opt into the table. |
| FPRC-AC4 | No broad full-repository text scan is required. |
| FPRC-AC5 | No runtime/provider/live/public/legacy broad-scan scope is introduced. |

## Verification / Evidence

Future tranches should provide:

- example table with one root finding and multiple symptoms;
- focused parser/checker tests if machine support is added;
- reviewer-fast and diff hygiene;
- explicit claim boundary.

## Relationship To Central Core Local View

Central core/local view prevents many duplicated fact mismatches at authoring
time. This roadmap handles the residual class: unexpected failures that still
appear across multiple artifacts. If a central facts packet exists, root-cause
grouping should reference it instead of repeating the shared facts again.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `FINDING_PROPAGATION_NOISE` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `ROADMAP_READY_FOR_GC018` |
| Next control action | FPRC-T1 dispatched before CCLV-T2 resumes |
| Worker blame | `N/A_WITH_REASON`: repeated file-level failures can be symptoms of one root control-plane defect |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance roadmap. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 finding propagation roadmap authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch |
| Target paths | `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md` |
| Allowed scope source | operator requested a remaining roadmap for unexpected errors and root-cause grouping |
| Before status evidence | base `dedc97c4` |
| After status evidence | roadmap authored; pending material commit |
| Diff evidence | governed documentation add |
| Approval boundary | roadmap only; no checker implementation yet |
| Claim boundary | finding grouping planning only |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This roadmap selects a future governance/error-reporting improvement. It does
not prove implementation, runtime behavior, provider behavior, public readiness,
production readiness, hosted freshness, or historical finding migration.
