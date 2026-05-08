<!-- Memory class: FULL_RECORD -->
# CVF CI2 Hosted Live Gate Failure Run

**Date:** 2026-05-09
**Track:** CI2-H1a - Hosted Run Failure Path
**Status:** FAILED BEFORE RELEASE GATE
**Run ID:** `25573498275`
**Run URL:** `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF/actions/runs/25573498275`
**Head SHA:** `d6f52284c14c581ccc7473f85d265fef891492ca`

## Summary

| Field | Value |
|---|---|
| Workflow | `CVF Protected Live Release Gate` |
| Event | `workflow_dispatch` |
| Conclusion | `failure` |
| Failed step | `Install CVF Guard Contract dependencies` |
| Failure class | `hosted_dependency_install_contract_mismatch` |
| Release gate command reached | no |
| Release gate artifact uploaded | no |
| Provider call reached | no |

## Failure Detail

The hosted workflow reached the protected environment and confirmed that
`DASHSCOPE_API_KEY` was present as a masked environment value. It failed before
the release gate command because the workflow ran `npm ci` in
`EXTENSIONS/CVF_GUARD_CONTRACT`, while `EXTENSIONS/CVF_GUARD_CONTRACT/package-lock.json`
is not tracked by the repository. The runner reported:

```text
npm error The `npm ci` command can only install with an existing package-lock.json
or npm-shrinkwrap.json with lockfileVersion >= 1.
```

The upload step also failed because `cvf-protected-live-release-gate-result.json`
was never created.

## Secret Handling

- GitHub logs masked `DASHSCOPE_API_KEY` as `***`.
- No raw provider key value is included in this artifact.
- No provider call was made.

## Corrective Action

Patch `.github/workflows/cvf-protected-live-release-gate.yml` so the Guard
Contract package uses `npm install --no-audit --no-fund`, matching the fact that
its lockfile is not tracked. Keep `npm ci` for `cvf-web`, which has a tracked
lockfile.

## Boundary

This run does not prove hosted CI2-H PASS. It proves the protected hosted lane
can dispatch and reach the configured environment, then fail closed before live
provider usage when dependency installation is invalid.
