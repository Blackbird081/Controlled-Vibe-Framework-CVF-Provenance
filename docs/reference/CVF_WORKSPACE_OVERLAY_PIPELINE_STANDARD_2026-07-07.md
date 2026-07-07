# CVF Workspace Overlay Pipeline Standard

Date: 2026-07-07

## Purpose

Define a local-first pipeline that lets a workspace inherit selected
high-value CVF provenance assets without turning the workspace into a direct
clone of the private provenance repository.

## Base Model

The hidden workspace core stays anchored to the public repository:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Overlay is a second step that copies reviewed files from the provenance repo on
top of that fresh public clone.

This keeps three layers separate:

1. `public-core`
2. `premium-workspace`
3. `provenance-local`

## Layer Meanings

### 1. `public-core`

- Source: public GitHub repo only
- Use when the workspace should stay public-safe
- No private continuity state is copied

### 2. `premium-workspace`

- Source: provenance allowlist
- Adds curated rules, guards, and governance references that are useful for
  downstream project execution
- Excludes canonical private session continuity surfaces such as
  `CVF_SESSION/` and `CVF_SESSION_MEMORY.md`

### 3. `provenance-local`

- Extends `premium-workspace`
- Adds canonical internal continuity surfaces for the local operator machine,
  including `CVF_SESSION/`, `CVF_SESSION_MEMORY.md`, and the provenance
  `AGENTS.md`
- Intended for private/local use, not public export

## Source Of Truth

Overlay definitions live under:

`workspace_overlay_profiles/`

Each profile is a JSON allowlist. Directory entries are exported recursively.

## Commands

Export a reviewed overlay bundle:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\export_cvf_workspace_overlay.ps1 `
  -ProfileName premium-workspace `
  -OutputPath "D:\CVF-Workspace\_cvf-overlay-staging\premium-workspace" `
  -Force
```

Apply an overlay to a workspace hidden core:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\apply_cvf_workspace_overlay.ps1 `
  -WorkspaceRoot "D:\CVF-Workspace" `
  -ProfileName provenance-local `
  -UpdateProjectManifests
```

## Verification Behavior

The downstream doctor still expects the hidden core to:

- point at the public `origin`
- contain the public workspace kit
- match `origin/main` by commit

An applied overlay may leave the hidden core worktree dirty. That is acceptable
as a bounded note because the doctor reports pending overlay state as a warning,
not a hard failure.

## Boundary

This pipeline is local-first by default.

Running it does not publish anything to GitHub. A later provenance push is a
separate operator decision after review.
