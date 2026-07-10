---
description: Create or refresh a CVF Workspace from a trusted provenance clone
---

# CVF Workspace Setup Workflow

When the operator asks to create, initialize, install, classify, or refresh a
CVF Workspace from this provenance repository, use the root entrypoint:

```powershell
.\Initialize-CVF-Operator-Workspace.ps1
```

Interactive use is the default and preserves the operator decision. Do not
preselect a profile for the operator.

After the operator has explicitly selected the path and profile, an agent may
run the same flow non-interactively:

```powershell
.\Initialize-CVF-Operator-Workspace.ps1 `
  -WorkspaceRoot "D:\CVF-Workspace" `
  -ProfileName "operator-local" `
  -NonInteractive
```

Use `-PlanOnly` first when the requested path or existing-workspace posture is
uncertain. Never select `operator-local` for a public, customer, or shared
workspace. Stop if the hidden public core is dirty or its remote is not the
approved public CVF repository.

Successful completion must leave the workspace root non-git, preserve sibling
project isolation, verify the active profile, and run the workspace enforcement
gate unless the operator explicitly requests `-SkipEnforcementGate`.
