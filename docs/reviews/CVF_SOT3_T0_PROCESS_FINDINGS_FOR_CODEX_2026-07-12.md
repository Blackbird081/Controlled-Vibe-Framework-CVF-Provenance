# SOT3-T0 Process Findings Hand-off For Codex

Memory class: POINTER_RECORD

Status: ADVISORY_PROCESS_INPUT_TRIAGED

docType: review_context

Date: 2026-07-12

Author role: SOT3-T0 external-review worker (WORKER_MUST_NOT_COMMIT)

## Target / Source

Target: three process observations arising from the SOT3-T0 dispatch and
external-review execution. Sources are the committed dispatch artifacts,
current governance commands, local tooling source, and the uncommitted worker
return set. This note is not SOT architecture authority.

## Findings / Position

- P1 is accepted only in narrowed form: dirty-path authorship was asserted
  without canonical evidence; neither operator nor agent authorship is proven.
- P2 is confirmed after staging the complete return set: GC-051 reports 226
  uncovered retained-corpus path references. The closer owns the registry
  entry and generated aggregate repair.
- P3 remains a tooling candidate because child output is decoded as UTF-8 but
  Python stdout is cp1252 in the local shell and printing U+FFFD may still fail.

## Purpose

Route governance/dispatch **process** findings observed while executing the
SOT3-T0 external scan to the Codex dispatcher/closer role. These are distinct
from the SOT3 architecture findings, which stay `PENDING_CVF_REVIEWER` in
`docs/reviews/CVF_SOT3_T0_EXTERNAL_REVIEW_RETURN_2026-07-12.md` and are not
routed here. This note is an untracked hand-off draft: no ADIF entry was
created, no registry/session/handoff path was edited, and no commit was made,
per the operator instruction to stop at `COMPLETE_PENDING_REVIEW`.

## Scope Boundary

- These are candidate ADIF entries / a bug report, not accepted defects.
- Promotion into `docs/reference/agent_defect_intelligence/entries/` and any
  registry/handoff mutation is a Codex closer action, not a worker action.
- SOT3 architecture value (fail-open, topology, receipt binding) is out of scope
  here; it belongs to the CVF reviewer via the external-finding workflow.

## Finding P1 - Dispatch exempt-path premise was factually wrong

Candidate defectClass: `DISPATCH_PRECONDITION_MISSTATED`

What happened: the SOT3-T0 work order and GC-018 baseline both carried
`Status: HOLD_PENDING_CLEAN_DISPATCH_COMMIT` with a `Pre-Existing Dirty Path
Exemptions` row describing `CVF_SESSION_MEMORY.md` as a *pre-existing operator
modification* to be excluded. In fact the only uncommitted change to that file
was a one-line `Last updated: 2026-07-12` edit made by the agent earlier in the
same session (`git diff` showed exactly one added line vs HEAD `615304819`).

Impact: the first clean-dispatch commit attempt was blocked by the pre-commit
hook (`core guard self-protection` + `closure packaging preflight`) because the
protected `CVF_SESSION_MEMORY.md` was dirty in the worktree - a documentary
exemption does not satisfy the hook, which requires the protected path to be
clean, not merely unstaged. Resolution required reverting the agent's own line,
after which the 4 dispatch artifacts committed cleanly at `4937a610e` (82/82).

Lesson for Codex: a `Pre-Existing Dirty Path Exemptions` row must be verified
against `git diff <path>` at authoring time and must name the actual author of
the change. Do not assume a dirty protected path is a "pre-existing operator
change"; if the dirty content is an agent edit, revert or authorize it before
dispatch rather than exempting it in prose. The hook enforces worktree
cleanliness of protected paths, so a prose exemption never unblocks the commit.

Suggested remediation: extend the work-order dispatch-quality guidance (or a new
ADIF entry) so an exempt-path row requires a `git diff` fingerprint and an
explicit author attribution before `HOLD_PENDING_CLEAN_DISPATCH_COMMIT` can
clear.

## Finding P2 - Worker/closer deadlock on GC-051 corpus-scan-registry

Candidate defectClass: `ROLE_BOUNDARY_GATE_DEADLOCK`

What happened: the worker processing ledger lists each source file by its
retained-root-relative path (e.g. `EXTENSIONS/CVF_REFINERY/src/pipeline/
refinery-engine.ts`). The GC-051 checker
(`governance/compat/check_corpus_scan_registry.py`, corpus-path patterns at
lines 170-172 for retained private roots and extension-path aliases) matches
these substrings and demands a `CVF_CORPUS_SCAN_REGISTRY.json` entry for the
SOT3 scan (no such entry exists among the 228 current entries). But the work
order `crossBatchIsolation` (line 310) forbids the worker from touching the
registry, and prefixing the paths with the retained root does not help because
`.private_reference/legacy/...` also matches the detector.

Impact: the no-commit worker cannot satisfy the reviewer-fast bundle, because
the only fix (a registry entry) is outside the worker's authorized changed set.
This is a structural deadlock: the corpus-scan artifact necessarily names corpus
paths, but the worker that produces it cannot register the scan.

Lesson for Codex: for external-review corpus scans, the GC-051 registry entry
for the scan should be authored by the dispatcher at dispatch time (or reserved
for the closer), and the work order should state explicitly that the corpus-scan
registry gate is a closer-owned closure gate, not a worker-return gate. Consider
whether the ledger path column should use a non-triggering notation (or whether
the detector should exempt paths under a declared external-review evidence
ledger) so that worker-phase content gates do not fail on a closer-owned
concern.

Suggested remediation: (a) add the SOT3 scan to `CVF_CORPUS_SCAN_REGISTRY.json`
during closure; and (b) a new ADIF entry recording that corpus-scan-registry and
session-state/handoff (GC-020) are closer-owned closure gates that must not be
counted against a no-commit worker return.

## Finding P3 - Environment bug: worker-return fast gate crashes on Windows cp1252

Candidate class: `TOOLING_BUG` (not an agent defect)

What happened: `governance/compat/run_worker_return_fast_gate.py` line 78 prints
subprocess stdout with the default Windows console encoding (cp1252). When the
`reviewer-fast` hook output contains a Unicode replacement character U+FFFD, the run
aborts with a `UnicodeEncodeError` instead of reporting the gate result. The underlying gate still runs;
only the runner's own stdout print crashes.

Impact: on Windows, the fast gate is unreliable as a single command; the
reviewer-fast hook had to be run directly with `PYTHONUTF8=1` to obtain the real
result. This can mask or misreport genuine pass/fail state.

Suggested remediation: make the runner decode/encode subprocess output as UTF-8
with `errors="replace"` (or set `encoding="utf-8"` on the subprocess and force
`sys.stdout.reconfigure(encoding="utf-8")`) so Windows consoles do not abort the
runner. This is a tooling fix, not an ADIF authoring-pattern entry.

## Not Routed Here

The SOT3 architecture findings (repeated empty-collection fail-open across all
three layers; triple-sourced Flow topology contradiction; assertion-based trust
transitions; open truth-packet schema) are recorded with source citations in the
external review return and remain `PENDING_CVF_REVIEWER`. They are semantic-value
findings for the CVF reviewer, not dispatch-process findings for Codex.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| unsupported author attribution becomes governance memory | retain only the rule that authorship requires evidence |
| a staged GC-051 failure blocks advisory evidence commit | closer adds one generated-source registry entry covering the retained path aliases |
| tooling candidate is fixed inside architecture review | park P3 for a separate source-verified checker-maintenance tranche |
| process note contaminates the three-output worker manifest | retain this note as separate advisory intake, not SOT3-T0 closure evidence |

## Decision / Disposition

Disposition: `ADVISORY_PROCESS_INPUT_TRIAGED`.

P1=`ACCEPT_NARROWED`; P2=`ACCEPT_CLOSER_OWNED_REGISTRY_REPAIR`;
P3=`DEFER_SOURCE_VERIFIED_TOOLING_CANDIDATE`. No ADIF entry or checker change is
authorized by this note.

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | external worker process handoff derived from a retained legacy corpus review |
| Upstream or source-mirror disposition | COMPARISON_ONLY_NO_ABSORPTION |
| Enumeration or manifest plan | this three-finding note is the complete process-input set |
| Per-file terminal-ledger plan | N/A with reason: single governed note, not a repository corpus |
| Owner or overlap route | P1 process-learning owner candidate; P2 rejected; P3 checker-maintenance candidate |
| Value-disposition route | adapt, defer, or reject after CVF reviewer verification |
| Claim boundary | process triage only; no architecture, ADIF, or checker authority |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | this process handoff note |
| Enumeration command | filesystem-backed direct file reads of this note |
| Manifest artifact or inline manifest | inline P1, P2, and P3 finding sections |
| Processing ledger artifact or inline ledger | inline Decision / Disposition section |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline Overlap And Novelty Classification table |
| Unresolved items | P3 remains deferred to a future tooling decision |
| Completion claim boundary | triage complete; remediation and promotion not authorized |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | SOT3 retained-source process handoff |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | exactly three process findings P1, P2, and P3 |
| Blind-spot prevention action | reviewer checks committed dispatch, staged gates, and local tooling source |
| Residual gap | P3 tooling remediation remains separately authorization-gated |
| Blind-spot verdict | PARTIAL_PENDING_SEPARATE_TOOLING_DECISION |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| P1 evidence rule | do not attribute dirty paths without proof | DOCTRINE_ADAPTED | future process-learning decision | consider ADIF only if recurrence threshold is met | no runtime action |
| P3 stdout defect | Windows output-encoding failure candidate | CHECKER_CANDIDATE | future checker-maintenance work order | reproduce without UTF-8 environment override | no checker edit now |
| process-note shape | review artifact formatting only | NO_PACKAGE_OR_RUNTIME_VALUE | this note | retain as evidence | no package/runtime value |
| external review workflow | bounded advisory intake | PACKAGE_CANDIDATE | existing external-review workflow | reuse existing workflow only | no package activation |
| SOT architecture findings | routed elsewhere | RUNTIME_CANDIDATE | SOT3-T0R | keep outside this note | no runtime mutation |
| direct import or automatic ADIF promotion | unsafe expansion | REJECT_DIRECT_IMPORT | none | reject | no direct import |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| dirty-path evidence discipline | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | ENRICH_EXISTING | attribution evidence is narrower than existing dirty-path guidance | park as learning candidate |
| GC-051 deadlock claim | `governance/compat/check_corpus_scan_registry.py` | NEW_FINDING | staged reviewer-fast gate reproduced 226 uncovered path references | closer adds SOT3 registry entry; no ADIF promotion in this batch |
| stdout encoding candidate | `governance/compat/run_worker_return_fast_gate.py` | NEW_FINDING | stdout encoding remains environment-sensitive | defer P3 to separate tooling tranche |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | external process handoff -> CVF reviewer triage -> accept-narrow, reject, or defer -> separate authorization if action is selected |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py` |
| Owner surface | this note for triage only |
| Disposition | ADAPT P1, REJECT P2, DEFER P3 |
| Claim boundary | no external process claim becomes CVF authority directly |

## Corpus Completeness And Report Integrity

- Corpus task class: three-item external process handoff triage.
- Corpus root: this note.
- Snapshot time: 2026-07-12 reviewer triage.
- Enumeration command: filesystem-backed direct file reads.
- Manifest artifact or inline manifest: P1, P2, and P3 sections.
- Manifest hash: N/A with reason: single uncommitted note, content tracked by git diff.
- Processing ledger artifact or inline ledger: Decision / Disposition.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=3; ledger_terminal=3; exclusions=0; unresolved=0
- Unresolved files: 0
- Declared exclusions: SOT architecture findings route through the external return.
- Unreadable or unsupported files: none.
- Aggregation check: three process findings triaged.
- Drift check: reviewer used current HEAD and current gate output.
- Output traceability: each decision maps to P1, P2, or P3.
- Adversarial verification: current gate output contradicted P2 and narrowed P1.
- Corpus verdict: PARTIAL

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: process findings may reveal reusable dispatch or
tooling defects.

Evidence Comparison: P1 retained only a narrower evidence rule; P2 reproduced
only after the complete set was staged and is repaired by the closer-owned
registry entry; P3 reproduced as a cp1252 stdout crash during commit steward
preflight.

Contradiction Or Gap Disposition: staged evidence confirms P2 while removing
unsupported authorship from P1. P3 remains deferred to a separate tooling fix.

Claim Update: three proposed findings become one narrowed learning candidate,
one closer-owned registry repair, and one source-visible tooling candidate.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | Target / Source; Findings / Position; Risk / Corrective Action; Decision / Disposition; External Absorption Core; External Absorption Value Conversion Matrix; Overlap And Novelty Classification; External Knowledge Intake Routing; Corpus Completeness And Report Integrity; Epistemic Process Block; Agent Operation Trace Block |
| gateRunPurpose | confirm advisory process-note shape after reviewer triage |
| claimBoundary | checker conformance does not promote an ADIF entry or prove a tooling defect |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | local private provenance workspace |
| Session or invocation | SOT3-T0 process-handoff triage, 2026-07-12 |
| Working directory | repository root |
| Command or tool surface | full-file reads, rg, Python/PowerShell read-only diagnostics, governance gates, apply_patch |
| Target paths | this process note and companion SOT3-T0 advisory evidence |
| Allowed scope source | operator instruction to commit cleanly and create the next Claude tranche |
| Before status evidence | HEAD `4937a610e`; four untracked advisory files |
| After status evidence | process findings classified; no ADIF, checker, runtime, session, or handoff mutation in this material batch |
| Diff evidence | `git diff --no-index` or staged diff plus `git status --short` before commit |
| Approval boundary | advisory evidence repair and process triage only |
| Claim boundary | no architecture closure, ADIF promotion, checker fix, provider/live, or public action |
| Agent type | reviewer/closer |
| Invocation ID | `sot3-t0-process-findings-triage-2026-07-12` |
| Expected manifest | manifest JSON; processing ledger; external review return; this process note |
| Actual changed set | manifest JSON; processing ledger; external review return; this process note |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this note concerns private dispatch and local tooling evidence.

## Claim Boundary

This is an advisory, untracked hand-off draft. It creates no ADIF entry, edits
no registry/session/handoff/runtime path, and makes no commit. Promotion of P1
and P2 into the ADIF registry and the P3 tooling fix are Codex/closer actions
subject to their own authorization.
