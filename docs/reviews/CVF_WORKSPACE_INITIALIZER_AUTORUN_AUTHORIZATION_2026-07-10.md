# CVF Workspace Initializer Autorun Authorization

Status: REVIEWER_ACCEPTED_BOUNDED

Date: 2026-07-10

Memory class: FULL_RECORD

## Purpose

Authorize one narrow startup-pointer change so a fresh provenance clone can
route an explicit operator workspace create or refresh request to the new
interactive initializer.

## Scope / Target / Owner Boundary

Applies only to `AGENTS.md`, the provenance-only initializer, its agent
workflow, root exposure classification, and the public-safe root-rules fix.
It does not authorize unrelated startup, session, runtime, provider, or
downstream project changes.

## Target / Source

Target: provenance fresh-clone workspace setup experience.

Source: the existing public installer, public-safe wrapper installer,
rule-pack materializer, profile catalog, distribution manifest, and workspace
enforcement gate.

## Findings / Position

The underlying components were complete but lacked one discoverable,
options-driven provenance entrypoint. The bounded initializer is accepted
because it composes existing commands and keeps operator profile choice
explicit.

## Risk / Corrective Action

Primary risks are dirty-core overwrite, wrong remote, accidental private-to-
public profile conversion, and setup inside a non-empty unrelated folder. The
initializer fails closed on each condition and requires a separate clean
workspace for public or paid use after `operator-local`.

## Evidence

- Interactive menu plan: PASS.
- Three-step Windows GUI render and selection smoke test: PASS.
- Double-click CMD launcher routes to the GUI with STA and execution-policy bypass.
- Non-interactive existing `operator-local` refresh and enforcement: PASS.
- Disposable clean `public-free` install and enforcement: PASS.
- Disposable clean `operator-local` install, 28-artifact materialization, and
  enforcement: PASS.
- In-place downgrade from `operator-local` to a public profile: BLOCKED.
- Non-empty new target without hidden core: BLOCKED.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one autorun pointer for explicit
workspace create or refresh requests.

Protected paths:

| Path | Purpose |
|---|---|
| `AGENTS.md` | Route the request to `Initialize-CVF-Operator-Workspace.ps1` while preserving operator profile selection. |

Operator authorization: provide agent autorun plus one options-driven file so
the operator can create a complete workspace conveniently on another machine.

Rollback boundary: revert only the pointer, initializer, workflow, exposure
entry, and root-rules installation fix in this batch.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_prepublic_p3_readiness.py` |
| literalTokensReviewed | `Core Guard Self-Protection Authorization`; `Protected paths`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `INTERNAL_ONLY` |
| gateRunPurpose | Confirmation evidence after source review, not first discovery of checker requirements. |
| claimBoundary | Read-ahead covers protected startup authorization, review shape, and root exposure only. |

## Verification

The initializer must preserve a non-git workspace root, approved public-core
remote, clean-core fast-forward rule, profile boundary, required root files,
and enforcement gate. Any failed invariant returns non-zero.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the interactive operator entrypoint is provenance-only. The separate
public-safe root-rules fix may be exported through the bounded workspace kit.

## Related Artifacts

- `Initialize-CVF-Operator-Workspace.ps1`
- `START_CVF_WORKSPACE_SETUP.cmd`
- `.agents/workflows/cvf-workspace-setup.md`
- `scripts/install_cvf_workspace_root_wrappers_public.ps1`
- `docs/reference/workspace_distribution/CVF_WORKSPACE_DISTRIBUTION_MANIFEST.json`

## Claim Boundary

This review proves Windows PowerShell fresh-install and refresh orchestration
for the three named profiles. It does not claim cross-platform, hosted,
provider-live, or downstream application readiness.
