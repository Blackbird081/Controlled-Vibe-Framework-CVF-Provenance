<!-- Memory class: FULL_RECORD -->
# CVF RC2 Install Reality Audit

Date: 2026-05-08

Status: CLOSED FINDINGS FOR A1/A2

## Scope

This is the RC2-A0 fresh Windows clone audit from the RC2 Foundation V3 track.
It classifies install friction only. It does not change runtime behavior and
does not claim guided setup is already present.

## Probe Environment

| Item | Result |
|---|---|
| Probe type | Local fresh clone from current repo HEAD |
| Probe path | `C:\Users\DELL\AppData\Local\Temp\cvf-rc2-a0-fresh-clone-20260508-133140` |
| Probe commit | `27307b88` |
| OS | Microsoft Windows 11 Home Single Language |
| Node | `v22.17.0` |
| npm | `10.9.2` |
| Python | `3.11.9` |
| Port 3000 | free |
| Port 3001 | free |

## Fresh Clone Readiness

| Check | Result | Classification |
|---|---|---|
| Root `package.json` exists | yes | `OPTIONAL` |
| `cvf-web/package.json` exists | yes | `OPTIONAL` |
| `cvf-web/package-lock.json` tracked | yes | `OPTIONAL` |
| `cvf-web/node_modules` exists in fresh clone | no | `WARNING` |
| `scripts/run_cvf_release_gate_bundle.py` exists | yes | `OPTIONAL` |
| `governance/` exists | yes | `OPTIONAL` |
| `EXTENSIONS/` exists | yes | `OPTIONAL` |
| `cvf-web/playwright.config.ts` exists | yes | `OPTIONAL` |
| `cvf-web/playwright.config.mock.ts` exists | yes | `OPTIONAL` |
| `cvf-web/.env.local` exists in fresh clone | no | `WARNING` |
| `cvf-web/.env.example` exists in fresh clone | no | `BLOCKER` |

## Dependency Probe

From the fresh clone:

```bash
cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm ci --dry-run --ignore-scripts
```

Result: PASS. npm resolved the package graph and reported `777` packages would
be added.

This means the dependency graph is not the first install blocker. The first
install blocker is guidance/config readiness.

## Provider / Env Readiness

| Check | Result | Classification |
|---|---|---|
| Process-level Alibaba/DashScope key detected | no | `WARNING` |
| Process-level DeepSeek key detected | no | `WARNING` |
| Fresh clone `.env.local` detected | no | `WARNING` |
| Fresh clone `.env.example` detected | no | `BLOCKER` |

No raw provider key values were printed or recorded.

Important finding: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.example`
exists in the operator's local working copy, but it is not tracked. It is
ignored by package-local `.gitignore` rule `.env*`. The deploy guide currently
points users to this path as the reference shape for `.env.local`, so a fresh
clone receives guidance that references a missing file.

## Scripts Currently Available

`cvf-web/package.json` exposes:

- `sync:risk-models`
- `predev`
- `prebuild`
- `dev`
- `build`
- `start`
- `lint`
- `test`
- `test:run`
- `test:coverage`
- `test:e2e`

There is no canonical root-level or script-level install doctor yet:

- no `scripts/cvf_doctor.py`
- no `scripts/cvf_provider_check.py`
- no `scripts/cvf_setup.py`

## Classified Findings

| ID | Finding | Classification | Follow-up |
|---|---|---|---|
| A0-F1 | `cvf-web/.env.example` is referenced by docs but missing from fresh clone because `.env*` ignores it | `BLOCKER` | A1/A2 must add a tracked env template or change the docs to a tracked template path |
| A0-F2 | No one-command clone readiness doctor exists | `BLOCKER` | A1 creates `scripts/cvf_doctor.py --json` |
| A0-F3 | No secret-safe provider readiness check exists | `BLOCKER` | A1 creates `scripts/cvf_provider_check.py --provider alibaba --json` |
| A0-F4 | No guided first-run setup orchestrator exists | `BLOCKER` | A2 creates `scripts/cvf_setup.py` or equivalent |
| A0-F5 | Fresh clone requires package install inside `cvf-web` before Web run | `WARNING` | A1 doctor should classify missing package install |
| A0-F6 | Provider keys are absent in a generic fresh shell | `WARNING` | A1 provider check should report `MISSING_KEY` without treating it as basic clone failure |
| A0-F7 | macOS/Linux fresh-clone behavior not verified | `DEFERRED_PLATFORM` | Keep Windows-only proof boundary until external verification |

## A1/A2 Guidance

A1 should not try to solve all onboarding. It should first create structured
diagnostics:

- missing Node/npm
- unsupported Node version
- missing Python
- missing `node_modules`
- port busy
- missing Playwright browsers
- missing provider key
- provider key present but live validation failed
- missing tracked env template

A2 should orchestrate the successful path only after A1 classifications exist.

## Claim Boundary

Allowed after A0:

> Install blockers are classified from a fresh Windows clone audit.

Not allowed after A0:

- CVF has guided setup.
- CVF is zero-friction.
- Web controls runtime modules.
- Web can trigger governance operations.
