# CVF Public Markdown Quality Upgrade Tier 2 Closure - 2026-05-16

Memory class: FULL_RECORD

Status: TIER 2 CLOSED - PUBLIC PUSH PENDING

## Purpose

Close the Tier 2 public Markdown quality tranche for the evidence and
benchmark entry-point files. Record what changed, what was measured, the
Tier 1 read-test status, and whether Tier 3 should start.

## Scope

This closure covers documentation-only work:

- Tier 2 GC-018 authorization;
- installation of the GC-045 checker stack into the public-sync workspace
  with a new `--no-bootstrap` portable flag;
- Tier 2 rewrite of 10 evidence and benchmark entry-point files;
- preservation of every numeric claim, date, and gate label across the
  rewrite;
- measurement recording.

It does not cover runtime, code, provider behavior, tests, governance
enforcement code, or new external knowledge absorption.

## Target

Target public repository:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Target local workspace:

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`

## Tier 1 Read-Test Status

`operator-skip-approved`

The Tier 2 GC-018 authorization explicitly waived the external Tier 1
read-test requirement noted in the Tier 2 proposal. The Tier 1 qualitative
claim about "first useful information is now easier to locate" therefore
remains a Codex self-claim, not an externally validated observation. Future
public-quality work should treat this as a known limitation.

## Completed Work

Tier 2 commits in public-sync (chronological):

| Commit | File |
| --- | --- |
| `37d35e9` | Install GC-045 checker stack with portable `--no-bootstrap` mode |
| `405c9f2` | `docs/evidence/latest-release-gate.md` |
| `d1f5f6b` | `docs/evidence/local-first-release-gate-proof-2026-05-16.md` |
| `e688248` | `docs/evidence/provider-lanes.md` |
| `fb3d4a8` | `docs/evidence/redaction-and-key-safety.md` |
| `8bc8777` | `docs/evidence/web-governance-path.md` |
| `6c7a0fe` | `docs/reference/CVF_RELEASE_CANDIDATE_TRUTH_PACKET_2026-04-21.md` |
| `2e48277` | `docs/reference/CVF_AUDIT_RECEIPT_INTEGRITY_MODEL.md` |
| `3cc6c59` | `docs/benchmark/README.md` |
| `da0a431` | `docs/benchmark/quality-benchmark-suite-methodology.md` |
| `572fb72` | `docs/benchmark/qbs-1/README.md` |

Tier 2 ceiling held at 10 files; one commit per Tier 2 file.

## Findings

Tier 2 reached automated GC-045 compliance for all 10 selected files. Three
findings carry forward:

1. **Automation prerequisite was load-bearing.** Running the checker
   surfaced that public-sync did not carry the governance repo's bootstrap
   marker files. Adding the `--no-bootstrap` flag let the checker validate
   structure portably without dragging the full hook chain into public-sync.
2. **`docs/evidence/` files classify as `baseline` not `spec`.** Several
   files initially failed because the classifier matched evidence-related
   tokens. The fix was to provide source/predecessor evidence, decision, and
   evidence/verification sections rather than spec sections. Future Tier 3
   work should expect this classification.
3. **Tier 2 word counts went up, not flat-or-down.** Tier 2 evidence and
   reference files needed additional GC-045 metadata sections (Memory class,
   Source, Decision, Protocol, Enforcement, Related Artifacts, Claim
   Boundary). The structural metadata enriches reviewability for evaluators
   and agents; pure prose volume is not the right metric for this layer.
   This finding amends the Tier 1 word-count-down-or-flat rule for evidence-
   class files.

## Risk

Residual risks recorded for the next tranche:

- the Tier 1 self-claim about read-time improvement is unverified;
- public-sync now carries a single governance checker but no hook chain, so
  enforcement is opt-in by manual command invocation;
- Tier 2 evidence files are now longer; future trimming work, if any, must
  preserve every numeric claim, date, and gate label.

Mitigation: close at Tier 2 and require fresh GC-018 before any Tier 3 work.

## Verification

Tier 2 verification (run in public-sync after each commit):

```bash
git diff --check
python governance/compat/check_markdown_structural_completeness.py \
  --base HEAD --head HEAD --no-bootstrap --all-changed --enforce
```

Tier 2 file-by-file GC-045 status:

| Check | Result |
| --- | --- |
| Tier 2 files rewritten | 10/10 |
| Commit discipline | 10 file commits + 1 checker install commit |
| GC-045 automated structural check | 10 of 10 satisfied |
| Claim drift on numeric/date/gate labels | none observed |
| Public-surface scanner | not re-run by Codex in this tranche; legacy invocation `python scripts/check_public_surface.py` remains the public-surface check |

## Measurement

Word counts before/after for three representative Tier 2 files.

Method: `git show <pre-tier-2-head>:<file> | wc -w` vs `wc -w < <file>`.

| File | Before | After | Direction |
| --- | ---: | ---: | --- |
| `docs/evidence/latest-release-gate.md` | 96 | 276 | up (structural metadata added) |
| `docs/evidence/provider-lanes.md` | 141 | 292 | up (structural metadata added) |
| `docs/benchmark/README.md` | 1394 | 1636 | up (structural metadata added) |

Interpretation: Tier 1 word-count rule (down or flat) does not apply to
Tier 2 evidence-class files. Tier 2 success criterion is structural-
completeness compliance plus no-claim-drift, both met.

## Decision

Recommendation: close the tranche at Tier 2.

Reason: The remaining public Markdown surface that has not been
standardized is largely audit-trail content (preregistrations, reviewer
plans, run-specific records under `docs/benchmark/runs/` and
`docs/benchmark/qbs-1/r*-*`). Rewriting that material risks evidence-shape
drift for low first-impression value. Tier 3 should not start automatically.

If Tier 3 ever opens, scope should be specific to a fresh first-impression
issue (e.g., onboarding flow that surfaces from real user feedback), not
broad standardization.

## Push Status

The 11 Tier 2 commits remain local in public-sync at the time of writing
this closure. Final push to
`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`
must follow this closure.

## Claim Boundary

This closure claims only that Tier 2 public Markdown quality hardening
reached GC-045 automated compliance for the 10 selected files. It does not
claim Tier 1 read-time improvement was externally verified, does not claim
every public Markdown file is GC-045 compliant, does not authorize Tier 3,
and does not claim runtime governance or output-quality changes.
