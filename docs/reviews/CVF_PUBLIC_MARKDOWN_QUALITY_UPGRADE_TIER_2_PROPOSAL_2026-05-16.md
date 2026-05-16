# CVF Public Markdown Quality Upgrade Tier 2 Proposal - 2026-05-16

Memory class: PROPOSAL_PACKET

Status: proposal awaiting GC-018 authorization; not yet executed.

## Purpose

Record the rationale, scope, candidate list, and exit criteria for a bounded
Tier 2 rewrite of the public CVF Markdown surface. This proposal is the
follow-on tranche after Tier 1 closure
(`docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_1_CLOSURE_2026-05-16.md`)
and the bilingual diacritics amendment applied directly on the public repo
(public commits `edd7d70`..`1e94439`).

## Scope

Tier 2 covers the next layer of public-facing Markdown after first-impression
files: evidence navigation, release-gate proof, provider lane summary, and
benchmark methodology entry points. These are the files an evaluator opens
*after* the front door to verify CVF's claims.

Tier 2 does **not** cover:

- audit-trail files (`docs/benchmark/runs/*/`, `docs/benchmark/qbs-1/r*-*`,
  preregistrations, reviewer plans);
- frozen baselines (`v1.0/`, `v1.1/`);
- FREEZE receipts;
- `AGENT_HANDOFF*.md`;
- `.private_reference/`;
- `docs/baselines/` except a Tier 2 authorization packet if approved;
- any runtime, code, test, or governance enforcement code.

## Source

Predecessor evidence:

- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_PROPOSAL_2026-05-16.md`
- `docs/baselines/CVF_GC018_PUBLIC_MARKDOWN_QUALITY_UPGRADE_AUTHORIZATION_2026-05-16.md`
- `docs/audits/CVF_PUBLIC_REPO_MARKDOWN_QUALITY_AUDIT_2026-05-16.md`
- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_1_CLOSURE_2026-05-16.md`
- Public commits `edd7d70`..`1e94439` (bilingual diacritics fix on Tier 1 set)

## Findings

Tier 1 met its measurable bar. Three findings carry forward into Tier 2 scope
decisions:

1. **First-impression value already captured.** Front-door files now expose
   GC-045 anchors. Further work on those files would be diminishing return.
2. **Evidence and benchmark entry points are the next bottleneck.** Audit
   classifies these as `agent context` with `medium evaluator impact` and
   names a 10-file Tier 2 candidate pool in the closure recommendation.
3. **Manual GC-045 rubric does not scale.** Public-sync workspace does not
   carry the GC-045 checker. Tier 1 used the canonical rubric manually for 15
   files. Tier 2 expands the surface, so an automated baseline is required to
   avoid drift between governance repo and public repo.

## Findings Caveat: Read-Test Coverage

Tier 1 closure noted no external human read-test was performed
(`audit line 323-326`). Tier 2 should not start without at least a minimal
read-test signal on Tier 1 output, because the qualitative claim
*"first useful information is now easier to locate"* is currently a self-claim
by Codex, not an external observation.

Recommended minimum: one non-coder Vietnamese reader spends 2 minutes on
`README.md` (public, post-bilingual-fix) and answers in writing:
*"trong 2 phút, bạn hiểu CVF là gì và làm được gì?"*. Capture the answer in
the audit. This is the read-test that should have closed Tier 1 and should
gate Tier 2.

## Requirements

Tier 2 execution must satisfy:

- Tier 2 ceiling: max 10 files.
- One commit per Tier 2 file in the public-sync workspace.
- Each rewritten file passes GC-045 structural rubric (automated, see below).
- Each rewritten file passes GC-023 size status (pass or documented inherited).
- No claim drift: original claim boundary wording preserved.
- Bilingual policy from Tier 1 audience routing is inherited. Files that fall
  into the first-impression audience class follow VN+EN; files in the
  agent/LLM class stay EN-only. Tier 2 candidate list is mostly evidence and
  benchmark, so default for Tier 2 is EN-only unless a specific file is
  explicitly retagged.
- Public-surface scanner passes (`python scripts/check_public_surface.py`).
- Measurement: representative before/after word count for three Tier 2 files
  using the same tool Tier 1 used (PowerShell `Measure-Object -Word`).
- External read-test note recorded if a non-coder reader is available, or an
  explicit *"no read-test performed"* note if not.

## Tier 2 Candidate Pool

Taken from Tier 1 closure recommendation:

| Candidate | Public path | Audience | Language |
| --- | --- | --- | --- |
| Latest release gate | `docs/evidence/latest-release-gate.md` | evaluator + LLM/agent | EN-only |
| Local-first release gate proof | `docs/evidence/local-first-release-gate-proof-2026-05-16.md` | evaluator | EN-only |
| Provider lanes | `docs/evidence/provider-lanes.md` | evaluator + coder/dev | EN-only |
| Redaction and key safety | `docs/evidence/redaction-and-key-safety.md` | security evaluator | EN-only |
| Web governance path | `docs/evidence/web-governance-path.md` | evaluator + coder/dev | EN-only |
| Release candidate truth packet | `docs/reference/CVF_RELEASE_CANDIDATE_TRUTH_PACKET_2026-04-21.md` | evaluator + LLM/agent | EN-only |
| Audit receipt integrity model | `docs/reference/CVF_AUDIT_RECEIPT_INTEGRITY_MODEL.md` | LLM/agent + coder/dev | EN-only |
| Benchmark entry | `docs/benchmark/README.md` | evaluator + coder/dev | EN-only |
| Benchmark methodology | `docs/benchmark/quality-benchmark-suite-methodology.md` | evaluator + LLM/agent | EN-only |
| QBS-1 entry | `docs/benchmark/qbs-1/README.md` | evaluator + LLM/agent | EN-only |

If any candidate's rewrite materially overlaps audit-trail evidence shape
(e.g., would alter scored-run claim wording), drop it from Tier 2 and surface
to operator before continuing.

## Automation Prerequisite

Before Tier 2 rewrite starts, copy the GC-045 enforcement stack into
public-sync so the rubric runs automatically:

| Source (governance repo) | Destination (public-sync) |
| --- | --- |
| `governance/compat/check_markdown_structural_completeness.py` | same path |
| `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md` | same path |
| `governance/toolkit/05_OPERATION/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_GUARD.md` | same path |

Public-sync `governance/toolkit/05_OPERATION/` does not exist today. The
prerequisite creates it. Copying these three files is permitted under Tier 2
even though `governance/toolkit/` was not in Tier 1 scope, because they
enable verification, not new governance authority. The acceptance criterion
is that the checker can be invoked successfully:

```bash
python governance/compat/check_markdown_structural_completeness.py \
  --base origin/main --head HEAD --all-changed --enforce
```

If running the checker in public-sync exposes additional hook chain
dependencies that are not part of public-sync today, those dependencies must
be deferred — do not pull in the full hook chain. Tier 2 needs only the
single checker, not the whole governance stack.

## Acceptance Criteria

- A fresh GC-018 authorization packet exists at
  `docs/baselines/CVF_GC018_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_2_AUTHORIZATION_2026-05-??.md`.
- Read-test signal recorded for Tier 1 output (or explicit *"not performed"* note).
- GC-045 checker installed in public-sync and shown to run.
- Tier 2 rewrite list locked at no more than 10 files.
- One commit per file in public-sync.
- 10/10 PASS GC-045 automated check after rewrite.
- Measurement and closure note created.

## Verification

Verification commands required at each Tier 2 commit:

```bash
git remote -v
git diff --check
python governance/compat/check_markdown_structural_completeness.py \
  --base origin/main --head HEAD --all-changed --enforce
python scripts/check_public_surface.py
```

## Risk

**Risk 1 — Scope creep.** Tier 2 candidate pool sits adjacent to audit-trail
files. A loose interpretation of the candidate list could pull preregistration
and reviewer-plan files into rewrite, which would damage evidence shape.
Mitigation: hard out-of-scope list above; if a candidate's rewrite would alter
scored-run claim wording, drop it.

**Risk 2 — Checker portability.** Installing the GC-045 checker in public-sync
may surface missing hook-chain dependencies. Mitigation: install only the
three required files; do not pull the full hook chain.

**Risk 3 — Read-test substitute.** Self-audit was acceptable for Tier 1's
small front-door set but is weaker evidence for Tier 2's evidence-and-benchmark
set, where claim fidelity matters more. Mitigation: require either external
read-test or explicit *"not performed"* note before Tier 2 closure.

**Risk 4 — Claim drift in evidence files.** Evidence files contain quoted
metrics, dates, and gate results. Mitigation: rewrite must preserve every
numeric claim, every date, and every gate label verbatim; only structure and
prose around them can change.

## Recommendation

Proceed to Tier 2 only after three preconditions are met:

1. operator approves the Tier 2 GC-018 authorization packet referenced in
   acceptance criteria above;
2. the GC-045 checker is copied into public-sync and shown to run;
3. either an external Tier 1 read-test is captured, or a *"not performed"*
   note is recorded in the audit.

If any precondition fails, Tier 2 does not start. The tranche stops at Tier 1
and the public Markdown quality upgrade is considered closed.

## Boundaries

Tier 2 is documentation-only. It does not authorize:

- Tier 3 work;
- changes to runtime, code, tests, or governance enforcement code beyond the
  single GC-045 checker copy described above;
- new external knowledge absorption;
- edits to audit-trail files even when they appear in candidate path globs.

## Related Artifacts

- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_PROPOSAL_2026-05-16.md`
- `docs/baselines/CVF_GC018_PUBLIC_MARKDOWN_QUALITY_UPGRADE_AUTHORIZATION_2026-05-16.md`
- `docs/audits/CVF_PUBLIC_REPO_MARKDOWN_QUALITY_AUDIT_2026-05-16.md`
- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_1_CLOSURE_2026-05-16.md`
- `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`
- `governance/toolkit/05_OPERATION/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_GUARD.md`

## Claim Boundary

This proposal claims only that Tier 2 is justified, scoped, and ready for
GC-018 authorization. It does not authorize execution. It does not claim any
Tier 2 file has been rewritten. It does not commit to Tier 3 work. Execution
requires operator approval of a fresh GC-018 authorization packet, completion
of the automation prerequisite, and recording of the Tier 1 read-test note.
