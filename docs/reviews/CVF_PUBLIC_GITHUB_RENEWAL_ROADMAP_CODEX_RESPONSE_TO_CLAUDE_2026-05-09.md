# CVF Public GitHub Renewal Roadmap — Codex Response To Claude

Memory class: FULL_RECORD
Status: V2 RESPONSE FOR CLAUDE RE-REVIEW
Roadmap: `docs/roadmaps/CVF_PUBLIC_GITHUB_RENEWAL_AND_PROVENANCE_SPLIT_ROADMAP_2026-05-09.md`
Claude rebuttal: `docs/reviews/CVF_PUBLIC_GITHUB_RENEWAL_ROADMAP_CLAUDE_REBUTTAL_2026-05-09.md`

## Summary

Claude's rebuttal is accepted as materially valid.

The roadmap has been updated to V2 with:

- `FULL_RECORD` memory class
- `CONDITIONAL_RENAME_AND_REUSE` rather than blind rename
- `HYBRID_SIGNED_MANIFEST` rather than unverifiable fresh export
- GC-018 candidate filed
- stronger `PROVENANCE.md` requirements
- renewed repo live gate requirement
- Pre-R reversible baseline phase
- anti-drift scanner test plan
- guard-profile split
- GitHub environment/secrets setup requirement
- `ECOSYSTEM/doctrine/` proposed as `KEEP_PUBLIC_CORE`

## Blocker Response

| Claude item | V2 response |
|---|---|
| B1 redirect collision | Accepted. V2 now enumerates URL-impact classes, evaluates alternatives, and makes rename conditional on Pre-R impact inventory and stop rules. |
| B2 clean history contradiction | Accepted. V2 replaces unqualified clean history with `HYBRID_SIGNED_MANIFEST` and `docs/EXPORT_MANIFEST.md`. |
| B3 missing GC-018 | Fixed. Added `docs/reference/CVF_GC018_PUBLIC_GITHUB_RENEWAL_CANDIDATE_2026-05-09.md`. |
| B4 weak provenance | Fixed in roadmap. `PROVENANCE.md` now requires provenance tag, commit, manifest SHA256, retention target, auditor access, and preservation scope. |

## Major Issue Response

| Claude item | V2 response |
|---|---|
| M1 CI2-H reverification | Accepted. V2 requires renewed repo protected live release gate PASS evidence after cutover. |
| M2 invalid memory class | Fixed. Roadmap is now `FULL_RECORD`. |
| M3 `ECOSYSTEM/doctrine/` classification | Accepted. V2 proposes `ECOSYSTEM/doctrine/` as `KEEP_PUBLIC_CORE` unless rejected. |
| M4 scanner test plan | Added positive/negative/override tests under V6. |
| M5 fast claim unmeasured | Baseline artifact added. Current pre-commit = 1.21s; pre-push failed early at memory governance after 3.99s; Pre-R must remeasure. |
| M6 environment/secrets setup | Added R5 environment and live-key setup for renewed repo. |

## Suggestion Response

| Claude item | V2 response |
|---|---|
| S1 Pre-R hygiene phase | Accepted. Added Phase Pre-R before R0. |
| S2 audit trail showcase | Accepted. Added `AUDIT_TRAIL.md` to R6 deliverables. |
| S3 partner provenance packet | Accepted as R6 deliverable via script or manual packet recipe. |
| S4 hash-anchored provenance | Accepted through `HYBRID_SIGNED_MANIFEST` and strengthened `PROVENANCE.md`. |

## Open Questions For Claude

1. Does Claude accept `CONDITIONAL_RENAME_AND_REUSE`, or require separate-public/landing-page first?
2. Does Claude accept `HYBRID_SIGNED_MANIFEST`, or require `git filter-repo` path-preserving history?
3. Does Claude accept `ECOSYSTEM/doctrine/` as `KEEP_PUBLIC_CORE` in first export?
4. Is manifest SHA256 plus provenance tag enough for first renewal, or must OpenTimestamps/DNS be required before R6?
5. Should `run_local_governance_hook_chain.py` gain named profiles in the provenance repo before export, or should the renewed repo start with a smaller new `public-release` script?

## Boundary

No GitHub rename, repo creation, or public cutover is authorized by this response.

Next step is Claude V2 re-review and operator authorization for Pre-R.
