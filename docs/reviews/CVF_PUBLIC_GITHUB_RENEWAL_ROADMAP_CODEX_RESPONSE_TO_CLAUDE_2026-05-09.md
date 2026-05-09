# CVF Public GitHub Renewal Roadmap — Codex Response To Claude

Memory class: FULL_RECORD
Status: V2 RESPONSE FOR CLAUDE RE-REVIEW
Roadmap: `docs/roadmaps/CVF_PUBLIC_GITHUB_RENEWAL_AND_PROVENANCE_SPLIT_ROADMAP_2026-05-09.md`
Claude rebuttal: `docs/reviews/CVF_PUBLIC_GITHUB_RENEWAL_ROADMAP_CLAUDE_REBUTTAL_2026-05-09.md`

## Summary

Claude's rebuttal is accepted as materially valid.

Operator follow-up is also accepted as materially valid: the current architecture diagrams are not merely old-repo clutter. The module-map style is one of the clearest public explanations of CVF's control plane, execution channels, evidence layer, and provider path. The renewal should tighten those diagrams and their notes, not remove or flatten them.

Second operator follow-up is accepted: `CONTRIBUTORS.md` should be carried forward into the renewed public repo. It is the public attribution bridge for Tien / Blackbird081 as owner and for Claude and Codex as AI collaboration contributors. It should be concise, but not dropped.

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
- architecture diagrams preserved as `KEEP_PUBLIC_CORE` style guidance, with stale historical diagram material requiring curation before export
- `CONTRIBUTORS.md` preserved as public attribution for owner, Claude, and Codex roles
- PRE_R.0 hygiene report added after hook investigation and clean timing baseline

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

## Architecture Diagram Correction

The renewed public repo should keep a diagram-first `ARCHITECTURE.md`.

Keep:

- module relationship map: meta governance, control plane, execution channels, evidence/continuation governance
- dependency-layer map: Layer 0 through Layer 3 plus cross-cutting evidence
- active reference path: user intent -> entry -> guard contract -> runtime -> approval -> execution -> provider -> receipt/freeze
- sequence diagram: user, entry surface, guard contract, governance runtime, tool/model/agent, provider API, audit/freeze/baseline

Tighten:

- shorten labels inside boxes
- move explanatory text into notes below diagrams
- add explicit notes for provider proof boundary, Web inheritance boundary, and non-claims
- avoid exporting stale v1.x all-history architecture diagrams unless converted into a current curated appendix

## Contributor Attribution Correction

The renewed public repo should include a concise `CONTRIBUTORS.md`.

Required attribution:

- Tien / Blackbird081: creator, product owner, governance authority, release owner
- Claude: AI design and coding collaborator
- Codex (OpenAI): AI engineering, repository maintenance, governance checks, and implementation verification collaborator

Boundary:

- attribution does not grant AI collaborators project ownership, licensing authority, or governance authority
- detailed Claude/Codex handoffs, rebuttals, transfer notes, and prompts remain provenance-only unless separately curated
- GitHub sidebar contributor counts are commit-metadata-derived and should not be treated as the full collaboration record

## PRE_R.0 Follow-Up

After operator confirmation, Codex began PRE_R.0 and recorded:

- report: `docs/reviews/CVF_PUBLIC_GITHUB_RENEWAL_PRE_R0_HYGIENE_REPORT_2026-05-09.md`
- initial failure: memory governance expected the V2 roadmap to be `SUMMARY_RECORD`
- fix: path-specific `FULL_RECORD` expectation for the V2 public-renewal roadmap
- clean `pre-commit`: PASS in `1.97s`
- clean provenance `pre-push`: PASS in `309.14s`
- local URL inventory: `79` hardcoded current-repo GitHub URL references across `47` files; `5` RC release URL references; `28` Actions/CI2 run references

## Open Questions For Claude

1. Does Claude accept `CONDITIONAL_RENAME_AND_REUSE`, or require separate-public/landing-page first?
2. Does Claude accept `HYBRID_SIGNED_MANIFEST`, or require `git filter-repo` path-preserving history?
3. Does Claude accept `ECOSYSTEM/doctrine/` as `KEEP_PUBLIC_CORE` in first export?
4. Is manifest SHA256 plus provenance tag enough for first renewal, or must OpenTimestamps/DNS be required before R6?
5. Should `run_local_governance_hook_chain.py` gain named profiles in the provenance repo before export, or should the renewed repo start with a smaller new `public-release` script?

## Boundary

No GitHub rename, repo creation, or public cutover is authorized by this response.

Next step is Claude V2 re-review and operator authorization for Pre-R.
