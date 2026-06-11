# CVF Agent Work Order: LPCI2 EX-T1 Dependency Source Audit

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Date: 2026-06-11

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `8b6bd04d`

executionBaseHead: worker must capture

closureBaseHead: reviewer-owned after return

---

## Purpose

Produce a source-backed dependency and local feasibility audit for the reusable
CVF scan/extraction foundation. Success means Codex receives enough evidence to
choose or reject the EX-T2 extraction implementation path without asking the
worker to build extraction code.

## Authority Chain

- Operator instruction: 2026-06-11, create the next work order under the new
  design-control foundation.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Roadmap:
  `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`
- Roadmap design-control gate: roadmap `## Dispatch Boundary`,
  `## Acceptance Criteria`, and `## Verification And Evidence`
- Spec / contract / machine-readable semantics: N/A with reason: EX-T1 is an
  audit-only dependency/source task and must not create runtime semantics.
- GC-018:
  `docs/baselines/CVF_GC018_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_2026-06-11.md`
- Active handoff: `AGENT_HANDOFF_V17_2026-06-07.md`

Authority boundary:

- This work order does not authorize work outside the cited authority chain.
- If any authority artifact conflicts with this work order, stop and return to
  Codex for reconciliation before implementation.

## Agent Roles

| Role | Agent | Responsibility |
|---|---|---|
| Orchestrator / dispatcher | Codex | Author dispatch packet and review return |
| Worker | Claude | Execute EX-T1 audit only; do not commit |
| Reviewer | Codex | Review artifacts, run gates, commit if bounded PASS |
| Operator | Human | Required for EX-T2 implementation, EC-T1 decision, public-sync, provider/key use, OCR model download, or repo dependency addition |

## Scope / Target / Owner Boundary

Allowed worker scope:

- Create `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md`.
- Create `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_SUMMARY_2026-06-11.json`.
- Create `docs/reviews/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_WORKER_RETURN_2026-06-11.md`.
- Read official or primary sources for candidate packages and system
  dependencies.
- Run bounded local install/import probes in a temporary environment outside
  the repo when safe, with no repo dependency or lockfile changes.
- Use `rg`, `Test-Path`, package metadata commands, and temporary probe logs to
  verify source facts.

Forbidden worker scope:

- Do not implement extractor source code.
- Do not modify runtime/source modules, package manifests, lockfiles, corpus
  data, generated chunks, retrieval code, EC-02 contracts, DSCP profiles, T12
  artifacts, public-sync files, or session continuity files.
- Do not download OCR model weights, run OCR over corpus documents, ingest
  corpus files, create vector indexes, call providers, load API keys, or make
  legal/current-law/readiness claims.

Risk ceiling:

R1 audit-only local feasibility work.

## Reviewer Closure Conversion

completionReviewPath:

`docs/reviews/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_COMPLETION_2026-06-11.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_COMPLETION_2026-06-11.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_FOR_CLAUDE_2026-06-11.md`
- `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V17_2026-06-07.md`

Reviewer conversion rule: Claude must not create or edit the completion review
unless a later operator instruction changes ownership. Codex owns closure
conversion, final gate reruns, commit, and continuity sync after worker return.

## Required First Reads

| File | Purpose |
|---|---|
| `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | Confirm EX/EC split and EX-T1 acceptance |
| `docs/baselines/CVF_GC018_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_2026-06-11.md` | Confirm authorization and claim boundary |
| `docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md` | Preserve design-control discipline |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Confirm work-order evidence requirements |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | Confirm `DscpDomainProfile.languageCodes` owner |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Confirm active mode and parked lanes |
| `AGENT_HANDOFF_V17_2026-06-07.md` | Confirm next allowed move and boundary |

## Pre-Flight Checks

| Check | Command | Required result |
|---|---|---|
| Base HEAD captured | `git rev-parse --short HEAD` | record as `executionBaseHead` |
| Audit report absent before worker edits | `Test-Path -LiteralPath docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md` | False |
| Machine summary absent before worker edits | `Test-Path -LiteralPath docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_SUMMARY_2026-06-11.json` | False |
| Worker return absent before worker edits | `Test-Path -LiteralPath docs/reviews/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_WORKER_RETURN_2026-06-11.md` | False |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 8b6bd04d --head HEAD` | PASS before worker edits |

If a pre-flight check fails inside allowed scope, repair and rerun it. If repair
requires forbidden scope, stop and return a blocked diagnostic.

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: parent roadmap dispatch boundary | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | line 163 | `Dispatch Boundary` | parent roadmap | ACCEPT |
| EXISTS: EX-T1 audit tranche | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | line 461 | `EX-T1` | parent roadmap work plan | ACCEPT |
| EXISTS: minimum EX-T1 source checks | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | line 252 | `Minimum EX-T1 source checks` | parent roadmap | ACCEPT |
| EXISTS: candidate dependency list source | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | lines 254-261 | `liteparse`, `pdfplumber`, `python-docx`, `pdf2image`, `EasyOCR`, `poppler` | parent roadmap candidate list | ACCEPT |
| EXISTS: DSCP domain profile | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 23 | `DscpDomainProfile` | `DscpDomainProfile` | ACCEPT |
| EXISTS: profile language codes | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 31 | `languageCodes` | `DscpDomainProfile` | ACCEPT |
| EXISTS: profile boundary rules | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 46 | `boundaryRules` | `DscpDomainProfile` | ACCEPT |
| EXISTS: design-control standard | `docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md` | line 93 | `Design Control Gate` | lifecycle standard | ACCEPT |
| EXISTS: work-order design carry-forward | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 965 | `Design Control Carry-Forward` | work-order template | ACCEPT |

## New Doc-Only Fields

These fields are report and JSON audit fields only. They are not runtime fields.

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
|---|---|---|---|---|
| `dependencyCandidateId` | stable audit key per candidate | Yes | Yes | present in report and JSON |
| `primarySourceUrl` | official or primary source locator | Yes | Yes | source-backed in report |
| `installProbeResult` | local feasibility result | Yes | Yes | command-backed |
| `importProbeResult` | import feasibility result | Yes | Yes | command-backed |
| `inputFormatFinding` | support finding for `.pdf`, `.docx`, images | Yes | Yes | source-backed |
| `ocrLanguageMappingFinding` | OCR code mapping evidence | Yes | Yes | source-backed |
| `ciFeasibilityVerdict` | bounded CI feasibility decision | Yes | Yes | evidence-backed |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| EX-T1 dependency audit only | Scope / Execution Plan | audit report and JSON summary | `git diff --name-status` forbidden path scan | ASSIGNED |
| Source verification for dependency install | Execution Plan / Evidence Requirements | `installProbeResult` | command output in report | ASSIGNED |
| Supported input formats | Execution Plan / Evidence Requirements | `inputFormatFinding` | primary-source citation table | ASSIGNED |
| OCR language-code mapping | Execution Plan / Evidence Requirements | `ocrLanguageMappingFinding` | source-backed mapping table | ASSIGNED |
| Local and CI feasibility | Evidence Requirements | `ciFeasibilityVerdict` | local probe ledger and CI constraint note | ASSIGNED |
| No runtime extraction claim beyond audit | Claim Boundary / Fail Conditions | claim boundary text | reviewer claim scan | ASSIGNED |
| Public Export Disposition remains private | Public Export Disposition | `DEFERRED_PRIVATE_ONLY` | reviewer packet check | ASSIGNED |

## Worker Autonomy / No-Question Rule

Allowed-scope gate or formatting failures are mandatory remediation. The worker
must repair and rerun them without asking the operator. Escalate only when the
repair requires forbidden paths, public-sync, provider/key use, OCR model
download, corpus ingestion, repo dependency addition, runtime implementation,
or a higher-risk claim.

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md` | Yes | Human-readable dependency audit |
| `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_SUMMARY_2026-06-11.json` | Yes | Machine-readable candidate summary |
| `docs/reviews/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_WORKER_RETURN_2026-06-11.md` | Yes | Worker evidence packet |

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| `EXTENSIONS/**/src/**` | No runtime/source implementation authorized |
| `EXTENSIONS/**/package.json` | No repo dependency addition authorized |
| `EXTENSIONS/**/package-lock.json` | No repo dependency lockfile update authorized |
| `CVF-Workspace/Policy_Local/**` | External product workspace out of scope |
| `docs/corpus-intelligence/**` | No corpus registry or generated corpus update authorized |
| `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | T11/T12 readiness must not reopen |
| `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync\**` | No public-sync authorized |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `EXTENSIONS/**/src/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Worker must not edit, stage, or claim runtime/source files |
| `EXTENSIONS/**/package.json` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Worker must not edit dependency manifests |
| `EXTENSIONS/**/package-lock.json` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Worker must not edit lockfiles |
| `CVF-Workspace/Policy_Local/**` | EXTERNAL_WORKSPACE_NOT_MODIFIED | EXTERNAL_WORKSPACE_NOT_MODIFIED | Stop if external workspace edits are needed |
| `docs/corpus-intelligence/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Worker must not edit corpus registries |
| `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync\**` | EXTERNAL_WORKSPACE_NOT_MODIFIED | EXTERNAL_WORKSPACE_NOT_MODIFIED | Stop if public-sync is needed |

## Write Ownership

Owned files or modules:

- `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md`
- `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_SUMMARY_2026-06-11.json`
- `docs/reviews/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_WORKER_RETURN_2026-06-11.md`

Write mode:

create-only for worker artifacts.

## Execution Plan

1. Capture `executionBaseHead` with `git rev-parse --short HEAD`.
2. Run required pre-flight checks.
3. Read required first-read artifacts.
4. Enumerate candidate stacks exactly from the roadmap candidate list:
   composed stack and LiteParse path.
5. For each candidate, collect primary-source evidence for package identity,
   license, supported input formats, OCR language parameter format, system
   dependencies, model/download behavior, Windows constraints, and CI
   constraints.
6. Run bounded local probes in a temporary environment when safe:
   package metadata lookup, install or dry-run install, and import probe. Do
   not edit repo manifests or lockfiles.
7. Build the OCR language-code mapping table for at least `en` and `vi` from
   DSCP `languageCodes` to each candidate OCR engine code.
8. Produce the report and JSON summary.
9. Run reviewer-fast.
10. Stage only the three owned worker artifacts and return without committing.

## Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| Scope boundary | roadmap `## Scope` | audit-only; no implementation | PASS |
| Non-goals | roadmap `## Non-Goals` | forbidden scope blocks runtime/public/readiness claims | PASS |
| Lane split | roadmap `## Dispatch Boundary` | executes EX lane only; EC lane remains pending | PASS |
| Dependency/source-verification plan | roadmap `## Source Verification And External Dependency Evidence Needed` | requires source-backed dependency matrix | PASS |
| Claim boundary | roadmap `## Claim Boundary` | inherited and repeated in this work order | PASS |
| Acceptance criteria | roadmap `## Acceptance Criteria` | mapped in trace matrix | PASS |
| Verification/evidence | roadmap `## Verification And Evidence` | report, JSON, probe ledger, reviewer-fast | PASS |
| Dispatch-readiness decision | roadmap `## Work Plan` and operator 2026-06-11 instruction | EX-T1 may dispatch; EX-T2 remains blocked | PASS |

## Evidence Requirements

Required evidence:

- `git rev-parse --short HEAD` result recorded as `executionBaseHead`.
- `git status --short` before return.
- `git diff --name-status` showing only owned worker files.
- For each dependency candidate: primary-source citation, observed package name,
  license, input-format support, OCR language handling, system dependency risk,
  Windows feasibility, CI feasibility, and local probe result.
- OCR language-code mapping table for `en` and `vi`.
- Explicit recommendation: `COMPOSED_STACK_PREFERRED`,
  `LITEPARSE_PREFERRED`, `BOTH_BLOCKED`, or `NEEDS_OPERATOR_DECISION`, with
  evidence reasons.
- Reviewer-fast command and result.

Evidence Trace Block requirements:

| Claim | Command | Result | Key path | Verdict |
|---|---|---|---|---|
| Worker must fill one row per significant dependency claim | command/source lookup | observed evidence | source URL or local command output path | EXISTS / ABSENT / PARTIAL / DRIFT |

Base-anchor evidence:

- `dispatchBaseHead`: `8b6bd04d`
- `executionBaseHead`: worker must capture before edits
- `closureBaseHead`: reviewer-owned after return
- Commit mode: `WORKER_MUST_NOT_COMMIT`
- Pending-artifact component gates: reviewer-fast required before return
- Committed-range `pre-closure`: N/A before Codex review

## Acceptance Criteria

| Criterion | Required result |
|---|---|
| Report exists and covers all candidate dependencies named in the roadmap | PASS |
| JSON summary exists and mirrors the report verdicts | PASS |
| Every dependency claim is backed by primary-source or command evidence | PASS |
| Local install/import probes are recorded or blocked with evidence-backed reason | PASS |
| OCR language-code mapping for `en` and `vi` is source-backed | PASS |
| CI and Windows feasibility risks are explicit | PASS |
| Recommendation is bounded to EX-T2 planning and does not claim runtime proof | PASS |
| No forbidden path is modified | PASS |

## Fail Conditions

| Condition | Action |
|---|---|
| Worker needs runtime/source edits to complete audit | STOP and return blocked diagnostic |
| Worker needs repo dependency or lockfile modification | STOP and return blocked diagnostic |
| Worker needs provider/API key use | STOP and return blocked diagnostic |
| Worker needs OCR model download or corpus OCR execution | STOP and return blocked diagnostic |
| Any dependency claim lacks primary-source or command evidence | Mark candidate `PARTIAL` or `BLOCKED`; do not upgrade recommendation |
| Any public/readiness/legal/current-law/runtime extraction claim appears | Remove claim or return blocked diagnostic |

## Review Gate

Implementation may proceed only after:

- this work order is dispatched;
- GC-018 exists;
- worker captures `executionBaseHead`;
- `pre-implementation` gate passes on the dispatch range.

Closure may proceed only after Codex confirms:

- report and JSON are internally consistent;
- forbidden paths are untouched;
- reviewer-fast passed or a bounded blocker is recorded;
- no runtime, public, provider, corpus, EC-02, T12, legal-quality, current-law,
  hosted, production, or public-readiness claim was introduced.

## Return Packet Requirements

Claude must return uncommitted artifacts with:

- `executionBaseHead`;
- `git status --short`;
- `git diff --name-status`;
- local probe commands and results;
- source citation list;
- candidate recommendation;
- reviewer-fast result;
- exact changed files;
- claim boundary.

## Closure Checklist

- [ ] Worker return reviewed by Codex
- [ ] Report and JSON consistency checked
- [ ] Forbidden path scan PASS
- [ ] Reviewer-fast PASS confirmed or bounded blocker recorded
- [ ] Codex commits accepted worker artifacts if PASS
- [ ] Session continuity synced after material commit
- [ ] Next roadmap decision recorded: EX-T2, alternate audit, or blocked

## Return-To-Orchestrator Conditions

Return to Codex without continuing if:

- pre-flight fails outside allowed remediation;
- a required source cannot be accessed through safe evidence collection;
- a local probe would require forbidden repo changes, provider/key use, OCR
  model download, or corpus processing;
- source evidence contradicts the roadmap candidate assumptions;
- any forbidden path changes.

## Operator Checkpoint

operator.checkpoint.waiver: operator authorized EX-T1 work-order creation on
2026-06-11. Operator approval remains required for EX-T2 implementation,
EC-T1 decision evidence, dependency addition, OCR model download, corpus
ingestion, public-sync, provider/key use, or readiness claims.

## Claim Boundary

This work order authorizes only dependency/source audit, temporary local
feasibility probes, report artifacts, and a worker return packet. It does not
prove extraction runtime, dependency fitness for production, OCR quality,
parser correctness, retrieval quality, corpus ingestion, EC-02 runtime
behavior, T12 eligibility, legal advice quality, current-law status, provider
behavior, hosted readiness, production readiness, public readiness, public-sync,
memory reinjection, high-risk promotion, Learning Orchestrator runtime
behavior, or autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; not public-synced.
