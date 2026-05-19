Memory class: FULL_RECORD
# CVF Public GitHub Renewal PRE_R.0 Hygiene Report — 2026-05-09

Status: PRE_R.0 HOOK FAILURE RESOLVED / BASELINE CAPTURED
Roadmap: `docs/roadmaps/CVF_PUBLIC_GITHUB_RENEWAL_AND_PROVENANCE_SPLIT_ROADMAP_V2_2026-05-09.md`

## Purpose

Record the first Pre-R.0 investigation after Gate A/B opened for local,
reversible public-renewal hygiene work.

## Hook Failure Investigation

Initial full pre-push rerun:

```powershell
python governance/compat/run_local_governance_hook_chain.py --hook pre-push
```

Result:

| Metric | Value |
|---|---:|
| Exit code | `2` |
| Elapsed seconds | `3.99` |
| Failure point | `memory governance compatibility` |
| Failure detail | V2 roadmap marker was `FULL_RECORD`, but `check_memory_governance_compat.py` expected `SUMMARY_RECORD` by default for `docs/roadmaps/`. |

Resolution:

- Kept V2 roadmap as `FULL_RECORD`, matching Claude/operator decision and the file's full-detail role.
- Added a path-specific memory-class expectation for `docs/roadmaps/CVF_PUBLIC_GITHUB_RENEWAL_AND_PROVENANCE_SPLIT_ROADMAP_V2_2026-05-09.md`.
- Did not weaken the default `docs/roadmaps/` expectation; ordinary roadmaps remain `SUMMARY_RECORD` unless explicitly exempted.

## Clean Timing Baseline

### Pre-Commit

Command:

```powershell
python governance/compat/run_local_governance_hook_chain.py --hook pre-commit
```

Result:

| Metric | Value |
|---|---:|
| Exit code | `0` |
| Elapsed seconds | `1.97` |
| Result | PASS |

### Pre-Push

Command:

```powershell
python governance/compat/run_local_governance_hook_chain.py --hook pre-push
```

Result:

| Metric | Value |
|---|---:|
| Exit code | `0` |
| Elapsed seconds | `309.14` |
| Result | PASS |

Note: the first retry used a shorter shell timeout and was interrupted at 304s
before the hook returned. A second run with a longer timeout completed cleanly.

## URL Inventory Snapshot

Local inventory command family:

```powershell
git grep -n "https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF"
git grep -n "releases/tag/v4.0.0-rc.1"
git grep -n "actions/runs/\|25575296660\|25573498275\|25574408974"
git ls-remote --tags origin
git ls-remote --heads origin
```

Snapshot:

| Inventory item | Count / result |
|---|---:|
| Hardcoded `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF` references | `79` |
| Unique files containing that GitHub URL | `47` |
| `v4.0.0-rc.1` release URL references | `5` |
| Actions run / hosted CI2 references | `28` |
| Remote heads | `main`, `cvf-next`, `restructuring/p3-cp2-retained-internal-root-relocation`, `restructuring/p3-layout-wave-2` |
| Remote tags include | `v4.0.0-rc.1`, `provenance-pre-renewal-2026-05-09`, historical `v1.x`/`v2.0.0` tags |

Important URL classes found:

- public clone/setup instructions in README, docs, Web content, and scripts
- GitHub Release references for `v4.0.0-rc.1`
- GitHub Issues links in user-facing docs and Web content
- GitHub Actions run evidence for CI2-H, including run `25575296660`
- historical compare links and old strategy/archive references
- package metadata repository URLs

## Interpretation

Pre-R.0 hook failure is resolved. The clean provenance `pre-push` baseline is
valid but slow, which reinforces the V2 decision to keep the full guard chain in
the provenance repo and create a smaller `public-release` profile for the
renewed public repo.

The URL inventory confirms that rename-and-reuse must not proceed blindly.
Public clone URLs are useful and should point to the renewed repo after cutover,
but release, Actions, and historical evidence links need curated replacement
summaries or provenance access.

## Boundary

This report does not authorize GitHub rename, renewed repo creation, history
export, or public cutover. Gate C remains blocked until the R1 manifest/export
verification is complete.
