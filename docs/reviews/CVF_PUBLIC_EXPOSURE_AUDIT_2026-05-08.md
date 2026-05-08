<!-- Memory class: FULL_RECORD -->
# CVF Public Exposure Audit

Date: 2026-05-08

Wave: WPR-3

Status: PASS WITH ACCEPTED BOUNDARIES

## Scope

This audit checks public-release exposure risks before RC tag binding. Commands
were chosen to report file names or counts only; no raw secret value was printed
or copied into this report.

## Summary

| Area | Result | Classification |
|---|---|---|
| Root license | `LICENSE` exists | RESOLVED |
| Extension package license fields | 51 package manifests scanned; 43 missing package-level `license` field | ACCEPTED_BOUNDARY |
| Raw provider key exposure | Broad pattern file scan found placeholders/env-var/test surfaces; release-gate secrets scan passed | ACCEPTED_BOUNDARY |
| `.private_reference/` tracking | `.gitignore` contains `.private_reference/`; no tracked `.private_reference/` files found | RESOLVED |
| `.env.local` tracking | No tracked `.env.local` files found | RESOLVED |
| Internal/handoff names | 22 tracked files contain internal/handoff-like names | ACCEPTED_BOUNDARY |
| TODO/FIXME/HACK with personal-info pattern | 1 hit, this audit roadmap text itself | ACCEPTED_BOUNDARY |
| Release gate | PASS 7/7 | RESOLVED |

## Findings

### F1 — Root License Present

State: RESOLVED

`LICENSE` exists at the repository root and is the governing license for the
repository.

### F2 — Package-Level License Fields Are Incomplete

State: ACCEPTED_BOUNDARY

The scan found 51 tracked `package.json` files under `EXTENSIONS/`; 43 do not
declare a package-level `license` field. This is not treated as an RC blocker
because the root repository license is present and applies to the repo. Several
matched files are historical or generated package manifests already present in
the repository.

Future packaging work may add package-level license fields, but WPR-3 does not
rewrite package manifests.

### F3 — Broad Key Pattern File-Name Scan

State: ACCEPTED_BOUNDARY

A broad file-name-only scan for provider-key-like patterns found 50 tracked
files outside `.env.example`, `docs/reference/*`, and the new deploy guide.
These hits are expected around placeholders, environment variable names,
provider adapters, and live-test harnesses. The release gate's secrets scan
passed with `No secret patterns detected`, so this is not treated as raw-key
exposure.

No raw key value is reproduced here.

### F4 — Private Reference And Env Files

State: RESOLVED

`.gitignore` contains `.private_reference/` and no tracked
`.private_reference/` path was found. No tracked `.env.local` file was found.

### F5 — Internal / Handoff-Like Tracked Paths

State: ACCEPTED_BOUNDARY

The scan found 22 tracked paths with `internal`, `handoff`, or related naming.
These are not automatically leaks in CVF. Several are canonical evidence,
internal-ledger module names, or governance history files intentionally kept in
the repository.

This audit does not delete or rewrite canonical evidence based on name alone.

### F6 — TODO/FIXME/HACK Personal-Info Pattern

State: ACCEPTED_BOUNDARY

One hit was found: the W153-W160 rebuttal packet's own audit checklist line that
mentions the search pattern. It is not personal information and does not require
code or doc remediation.

## Verification Commands

Commands run, summarized without raw secret output:

```powershell
Test-Path LICENSE
rg -n "^\\.private_reference/" .gitignore
git ls-files | rg "^\\.private_reference/"
git ls-files | rg "\\.env\\.local$"
git grep -I -l -E "<provider-key-patterns>" -- . <exclusions>
git grep -I -l -E "TODO.*@|FIXME.*@|// HACK" -- .
python scripts/run_cvf_release_gate_bundle.py --json
```

## Gate Result

`python scripts/run_cvf_release_gate_bundle.py --json` passed 7/7:

- Web build PASS
- TypeScript guard contract PASS
- Provider readiness PASS
- Secrets scan PASS
- Docs governance PASS
- UI mock Playwright PASS
- Live governance Playwright PASS

## WPR-4 Readiness

WPR-3 does not block WPR-4. All findings are `RESOLVED` or
`ACCEPTED_BOUNDARY`; none are `DEFERRED_TO_WPR_4`.
