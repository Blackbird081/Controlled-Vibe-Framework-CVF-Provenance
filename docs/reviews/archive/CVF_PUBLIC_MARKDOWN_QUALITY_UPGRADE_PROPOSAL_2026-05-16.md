# CVF Public Markdown Quality Upgrade Proposal - 2026-05-16

Memory class: FULL_RECORD

Status: proposal awaiting GC-018 authorization; not yet executed.

## Purpose

Record the rationale, scope boundary, audience routing, and execution plan for
a public-facing Markdown quality upgrade of the CVF repository
(`github.com/Blackbird081/Controlled-Vibe-Framework-CVF`).

This document is preserved as historical evidence of the decision. It is open
to Codex rebuttal under the established `*_CODEX_RESPONSE_TO_CLAUDE_*` pattern.

## Target

Public Markdown surface of the CVF repository, defined by the Scope section
below. The target is the *quality* of those files as evaluated by three
audiences (non-coder user, coder/dev, LLM/agent), not the volume of files
edited.

## Findings

Operator and rebuttal-reviewer agree on three compounding benefits (see "Why
This Upgrade" below). The disagreement-of-record is *scope*: the rebuttal
reviewer flagged that "standardize all 3283 Markdown files" has no finishing
condition and risks the same over-broad failure mode that required amendment
in the CVF 16.5 absorption tranche. Both parties accept the tiered strategy
below as the resolution.

## Recommendation

Approve a fresh GC-018 candidate for **Phase 1 audit + Tier 1 rewrite only**
(max 15 first-impression files). Defer Tier 2 and Tier 3 behind explicit ROI
measurement after Tier 1. Audit chain files, frozen baselines, and agent
handoff files remain out of scope hard.

## Scope

Public repository Markdown content visible to:

- non-coder users browsing or cloning the repo to evaluate CVF;
- coder/dev users integrating CVF into their workflow;
- external LLM/agents reading CVF as governance context.

Scope **excludes**:

- `docs/baselines/` (audit chain — edit destroys evidence);
- `docs/reviews/CVF_GC018_*_AUTHORIZATION_*.md` (audit chain);
- `v1.0/`, `v1.1/` (frozen baselines per `CLAUDE.md`);
- FREEZE receipts;
- `AGENT_HANDOFF*.md` (agent internal context, not public concern);
- `.private_reference/` (already not committed).

## Why This Upgrade

Three compounding benefits identified by operator and rebuttal-reviewer:

1. **Public evaluation quality.** Users cloning the repo extrapolate from
   Markdown quality to overall framework quality. Inconsistent structure
   signals an immature product even when the engineering is mature.
2. **Agent token efficiency.** Structured documents with predictable
   `Memory class`, `Status`, `Purpose`, `Scope`, `Claim Boundary` sections let
   future agents parse by anchor instead of by full read. This is a real,
   measurable cost saving across every future session.
3. **LLM/MCP integration readability.** When external LLMs (Codex, Cursor,
   Gemini, etc.) consume CVF as tool/MCP context, consistent shape reduces
   per-LLM re-derivation cost.

GC-045 already provides the structural vocabulary. Without this upgrade, the
vocabulary stays mostly theoretical for legacy files.

## Risk

**Risk 1 — Scope creep.** The public repo contains 3283 Markdown files in
scope-eligible directories. A blanket "standardize everything" tranche has no
finishing condition and risks repeating the over-broad failure mode that
required amendment in the CVF 16.5 absorption tranche.

**Risk 2 — Audit chain damage.** Edits to baselines, authorizations, or FREEZE
receipts break evidence chains. Out-of-scope list above is hard.

**Risk 3 — Claim drift.** A "cleanup rewrite" can silently change claim
boundary wording. Rewrites must preserve original claims; only structure and
audience-tuning changes are allowed.

**Risk 4 — Audience mismatch.** GC-045 structure compliance is not the same as
audience fit. A file can be GC-045 compliant and still useless to a non-coder
user. Audience-aware rewrite is required in addition to structural compliance.

## Counter-Argument Considered

Could the upgrade be skipped entirely? Argument against the upgrade:

- 3283 files is a heavy investment.
- Most files are working artifacts, not user-facing.
- Public renewal roadmap V2 already exists
  (`docs/roadmaps/archive/CVF_PUBLIC_GITHUB_RENEWAL_AND_PROVENANCE_SPLIT_ROADMAP_V2_2026-05-09.md`)
  and may already cover this.

Rebuttal: the existing renewal roadmap covers exposure split and provenance,
not Markdown quality per se. The proposed tranche fills a different need:
*"after a user clones this repo, do they form a professional impression in the
first 5 minutes?"* — and this is currently not measured anywhere.

Phase 1 audit will verify whether the renewal roadmap already addresses this.
If yes, extend the existing roadmap rather than open a parallel tranche.

## Tiered Strategy

**Tier 1 — First-impression files (max 15 files).** Audience-aware rewrite of
the files a fresh user encounters first.

**Tier 2 — Reference files (conditional, decided after Tier 1 metrics).**
Reference and governance documents that users consult after initial impression.

**Tier 3 — Working files (likely never).** Reviews, logs, archives. Most should
remain grandfathered under GC-045 legacy clause; some may be moved to
`.private_reference/` if not publicly load-bearing.

The tier sequence is gated: Tier 2 starts only if Tier 1 metrics justify it.
This stops "endless standardization" and forces ROI proof.

## Audience Routing

| File class | Examples | Primary audience | Language |
| --- | --- | --- | --- |
| First-impression | `README.md`, `docs/GET_STARTED.md`, `docs/CHEAT_SHEET.md`, `docs/guides/CVF_QUICK_ORIENTATION.md` | Non-coder user | VN+EN bilingual |
| Coder onboarding | `CLAUDE.md`, `docs/CVF_CORE_KNOWLEDGE_BASE.md`, `docs/CVF_ARCHITECTURE_DECISIONS.md`, `docs/reference/CVF_MODULE_INVENTORY.md` | Coder/dev | EN-only |
| Agent/LLM context | `docs/INDEX.md`, `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`, `docs/reference/CVF_SESSION_GOVERNANCE_BOOTSTRAP.md` | LLM/agent + dev | EN-only, dense metadata, heavy cross-reference |

Bilingual is selective on purpose. Mandatory bilingual on every file would
double agent parsing cost and create translation drift. EN-only on
machine-facing files keeps LLM parsing stable. VN+EN on user-facing files
serves the primary operator audience.

## Hard Constraints On Rewrite

1. **No claim drift.** Each rewrite preserves original claim boundary wording.
   Style and structure change; meaning does not.
2. **No bulk commits.** Each Tier 1 file is its own commit. This allows
   selective rollback if any rewrite drifts.
3. **GC-045 + GC-023 must pass** on every commit. Pre-commit hook enforces both.
4. **Tier 1 ceiling = 15 files.** If Codex proposes more, push back to clarify
   which fall to Tier 2.
5. **Out-of-scope list is hard.** No exceptions without a fresh GC-018.

## Measurement Plan

Phase 1 audit captures baseline. Tier 1 execution captures delta:

| Metric | Before | After Tier 1 | Decision rule |
| --- | --- | --- | --- |
| Tier 1 GC-045 compliance | baseline % | target 100% | gate before Tier 2 |
| Token count to read one full Tier 1 file (3 samples) | baseline | after | direction must be down or flat |
| Time-to-first-useful-info qualitative test (1-2 readers) | baseline note | after note | direction must be improved |
| GitHub Files-view first-impression screenshot | before | after | side-by-side visual |

If the after-Tier-1 measurement does not show net improvement, Tier 2 is
**not** authorized and the tranche stops. This is the ROI gate.

## Workflow

1. **Authorization.** Codex opens GC-018 candidate. Operator approves.
2. **Phase 1 audit.** Codex creates
   `docs/audits/CVF_PUBLIC_REPO_MARKDOWN_QUALITY_AUDIT_2026-05-16.md`. No file
   edits in Phase 1.
3. **Operator review.** Operator locks Tier 1 file list.
4. **Tier 1 execution.** One commit per file, GC-045 + GC-023 enforced.
5. **Measurement.** Codex records before/after metrics.
6. **Decision.** Operator decides Tier 2 start or tranche close.

## Related Artifacts

- `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md` (GC-045)
- `governance/toolkit/05_OPERATION/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_GUARD.md`
- `docs/roadmaps/archive/CVF_PUBLIC_GITHUB_RENEWAL_AND_PROVENANCE_SPLIT_ROADMAP_V2_2026-05-09.md`
- `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` (GC-023)
- `docs/reviews/CVF_16_5_EXTERNAL_KNOWLEDGE_INTAKE_REVIEW_CLAUDE_REBUTTAL_2026-05-16.md` (precedent for over-broad tranche failure mode this proposal explicitly avoids)

## Claim Boundary

This proposal claims only that the upgrade is justified, scoped, and ready for
GC-018 authorization. It does not authorize the upgrade. It does not claim any
file has been rewritten. Execution requires operator approval of a GC-018
candidate, completion of Phase 1 audit, and operator lock of the Tier 1 list.

Codex may rebut this proposal via
`CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_PROPOSAL_CODEX_RESPONSE_TO_CLAUDE_2026-05-16.md`
following the established rebuttal/response pattern.
