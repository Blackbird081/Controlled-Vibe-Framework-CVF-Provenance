# CVF GC-051 Corpus Scan Registry Establishment Review

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-06-02

## Purpose

Governance review for the establishment of GC-051 — the Corpus Scan Registry.
This review authorizes changes to protected guard/control files required to
create and wire the new corpus scan registry system.

## Scope / Target / Owner Boundary

Target: operator and future agents — establishes a new CVF governance layer
that applies to all corpus scanning, regardless of corpus type.

## Target / Source

Target: new `docs/corpus-intelligence/` folder, standard, guard, checker, and
autorun wiring.
Source: operator direction 2026-06-02 to create a corpus registry as a CVF-wide
rule.

## Scope / Methodology

New artifacts created and wired in one batch:

- `docs/corpus-intelligence/` folder with README, JSON registry, MD companion,
  findings subfolder
- `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`
- `governance/toolkit/05_OPERATION/CVF_GC051_CORPUS_SCAN_REGISTRY_GUARD.md`
- `governance/compat/check_corpus_scan_registry.py`
- Wired into `governance/compat/run_agent_autorun_workflow_gate.py`
- Wired into `governance/compat/run_local_governance_hook_chain.py`
- `CLAUDE.md` updated with GC-051 pointer

Checker verified locally: `python governance/compat/check_corpus_scan_registry.py --enforce` → COMPLIANT.

## Findings / Position

Position: ACCEPT. GC-051 addresses a real multi-session blind spot: agents
re-scan corpora and lose findings across session boundaries. The registry
backfills all 8 known legacy corpus entries and the CI1-T2 Graphify findings.

## Risk / Corrective Action

| Risk | Control |
| --- | --- |
| Registry becomes stale | Standard Rule 2 requires update after every scan; checker validates |
| New checker causes false positives on non-corpus audits | Checker only checks docs/audits/*.md files; scoped to corpus path mentions |
| Autorun gate number increases | Gate count increased from 19 to 20 — advisories only, same enforcement pattern |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: establish GC-051 Corpus Scan Registry as a
new CVF governance control (initial batch), and apply 5 post-review findings
(F1–F5) to the checker, AGENTS.md, registry, and standard.

Batch 1 (initial establishment):
- new checker, new guard file, new standard, autorun/hook wiring
- CLAUDE.md GC-051 pointer
- check_docs_governance_compat.py taxonomy extension

Batch 2 (F1–F5 fix):
- AGENTS.md: add Mandatory Corpus Scan Registry Consultation section
- governance/compat/check_corpus_scan_registry.py: hash format enforcement (F3) + docs/reviews coverage (F4)
- docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json: hash standardization (F5)
- docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md: hashAlgorithm + hashInput docs (F5)
- AGENT_HANDOFF_V15_2026-05-29.md: HEAD → 1add199b (F1 follow-up)

Batch 3 (action-evidence hardening):
- governance/compat/check_corpus_scan_registry.py: `PENDING` / `not yet`
  placeholders no longer count as action evidence for deferred or blocked
  findings unless another real artifact ref exists.
- docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json:
  `RESCAN-C-code-review-graph` now cites the existing CI1 roadmap instead of a
  not-yet-opened placeholder as its roadmap evidence.
- AGENT_HANDOFF_V15_2026-05-29.md: HEAD → 05bdc544.

Batch 4 (Graphify F1-F4 closure normalization):
- CI1-T2 F1 KGR1 partial absorption is normalized to `ACCEPT_NO_ACTION` with
  `defectClass=N/A` and `learningLane=N/A`.
- CI1-T2 F2 G-GM-01 through G-GM-08 now cites
  `docs/roadmaps/CVF_GRAPHIFY_GUARD_ENFORCEMENT_ROADMAP_2026-06-02.md`.
- CI1-T2 F3 `cvf graph` CLI absence now cites
  `docs/roadmaps/CVF_GRAPH_CLI_PHASED_BACKLOG_ROADMAP_2026-06-02.md`.
- CI1-T2 F4 71.5x token reduction remains `ACCEPT_WITH_BOUNDARY` and is routed
  as documentation-only learning unless a later live-proof benchmark is opened.

Protected paths:

- `AGENTS.md`
- `CLAUDE.md`
- `governance/compat/check_corpus_scan_registry.py`
- `governance/compat/check_docs_governance_compat.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/toolkit/05_OPERATION/CVF_GC051_CORPUS_SCAN_REGISTRY_GUARD.md`

Operator authorization: operator direction on 2026-06-02 to establish a
corpus scan registry as a CVF-wide rule for all agents and projects.

Rollback boundary: revert all files in this commit if the batch is unwound.
No runtime behavior changes — documentation, guard, checker, and wiring only.

## Finding-To-Governance Learning Disposition

Defect class: `RULE_GAP` — no registry existed; agents re-scanned and lost findings

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Disposition: `MACHINE_CHECK_IMPLEMENTED` — GC-051 + `check_corpus_scan_registry.py` now enforces pre-scan registry check

Next control action: `CLOSED` — checker is wired into autorun and pre-commit hook

Runtime/provider/cost learning: `N/A_WITH_REASON`

Reason: GC-051 is documentation and governance wiring only; no provider calls,
runtime behavior changes, or cost events.

## Claim Boundary

This review claims: GC-051 is established, checker passes, and autorun is wired.

This review does NOT claim: semantic correctness of all registry entries;
production or hosted readiness; full coverage of all possible corpora.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: internal governance control; registry contains `.private_reference/`
paths not for public-sync.
