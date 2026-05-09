# CVF Public GitHub Renewal Baseline Measurement — 2026-05-09

Memory class: FULL_RECORD
Status: BASELINE FOR ROADMAP V2
Related roadmap: `docs/roadmaps/CVF_PUBLIC_GITHUB_RENEWAL_AND_PROVENANCE_SPLIT_ROADMAP_2026-05-09.md`

## Purpose

Claude's rebuttal correctly noted that the roadmap called the proposed `public-release` guard profile "fast" without a measurement baseline.

This artifact records the first local timing check before a dedicated Pre-R hygiene phase.

## Environment

- Date: 2026-05-09
- Workspace: current full CVF provenance/development repo
- Shell: PowerShell
- Measurement tool: `Measure-Command`

## Measurements

### Pre-Commit Profile

Command:

```powershell
Measure-Command { python governance/compat/run_local_governance_hook_chain.py --hook pre-commit }
```

Result:

| Metric | Value |
|---|---:|
| TotalSeconds | `1.21` |
| TotalMilliseconds | `1205.25` |
| Exit status | PASS |

### Pre-Push Profile

Command:

```powershell
Measure-Command { python governance/compat/run_local_governance_hook_chain.py --hook pre-push }
```

Result:

| Metric | Value |
|---|---:|
| TotalSeconds | `3.99` |
| TotalMilliseconds | `3992.69` |
| Exit status | FAIL early |
| Failure point | `memory governance compatibility` |

## Interpretation

The current pre-push number is not a valid full-chain duration because the chain failed early. It does confirm that the full provenance guard chain is active and that a clean timing baseline still needs to be captured during Pre-R after the working state is prepared.

## Public-Release Target

Proposed target for the renewed public repo:

| Profile | Target |
|---|---:|
| `public-release` local default | `< 10s` |
| `release-live-proof` | no short timing target; live provider proof may take minutes |

## Follow-Up Required

Pre-R must produce a cleaner measurement artifact after:

- public-surface scanner warning-mode is drafted
- provenance-only files are excluded from the renewed repo candidate
- public-release profile is implemented or simulated

This baseline does not authorize cutover.
