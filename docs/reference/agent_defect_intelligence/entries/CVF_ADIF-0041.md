# ADIF-0041 - Dirty Sibling Install Masks File-Link Dependency Failure

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0041
title: Dirty sibling install masks file-link dependency failure
defectCategory: GATE_TRIGGER_FRICTION
defectClass: MACHINE_GATE_GAP
defectRole: worker
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Web UI/dashboard; Worker execution (`WORKER_MUST_NOT_COMMIT`); Public-sync
roles: dispatcher; worker; reviewer; closer; session-sync steward
lifecyclePhases: pre-implementation; pre-closure; pre-push
surfaceSelectors: Web packages that consume sibling TypeScript packages through package.json file dependencies
detectionSignals: local build passes while a clean deployment reports TS2307 from a sibling package import; sibling package has its own node_modules; package-lock entries use link true
enforcementLevel: GUIDANCE_ONLY
checkerBindings: NOT_APPLICABLE_WITH_REASON: the focused regression protects the repaired Truth Kernel mapping, but no generic governance checker yet validates every nested file-link dependency from a clean install
promotionState: MACHINE_CHECK_CANDIDATE
supersedes: NONE
lastVerifiedCommit: 365cdb372
roadmapSeedId: NONE
```

## Purpose

Prevent a warm developer workspace from being accepted as deployment proof
when nested local-package dependencies resolve only because a sibling package
retains an old `node_modules` directory.

## Scope / Applies To

Applies when a Web or deployment package consumes TypeScript source through a
`file:` dependency and that sibling source imports another package by package
name. It is especially relevant when npm installs the local package as a link
or junction and TypeScript resolves imports from the linked package's real
source path.

## Bad Example

Run typecheck and production build in the long-lived provenance workspace,
observe PASS, and push. The sibling package's existing dependency installation
silently satisfies an import that the deployment package's clean install
cannot resolve from the sibling real path.

## Good Example

Create a detached clean worktree from the exact public commit, install only
from the deployment base directory, and run TypeScript plus the production
build. For a required nested package import, provide a narrow source mapping or
another source-verified package boundary; do not enable global symlink
preservation without checking every linked package's relative imports.

## Canonical Sources

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tsconfig.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/truth-package-resolution-boundary.test.ts`
- `EXTENSIONS/CVF_TRUTH_FLOW/package.json`
- `EXTENSIONS/CVF_TRUTH_FLOW/src/kernel-reference/kernel-authority.ts`
- `EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts`
- `docs/reference/guard_orientation/README.md`

## Remediation

1. Inspect both the deployment package manifest and the nested sibling package
   manifest before claiming a dependency is missing.
2. Check whether local `node_modules` folders outside the deployment base can
   mask resolution.
3. Reproduce from the exact public commit in a clean detached worktree and run
   install only from the configured deployment base.
4. Prefer the narrowest source-verified mapping or bounded export. Do not move
   packages between dependency classes or externalize them without proving the
   actual import and runtime boundary.
5. Keep a focused regression for the repaired mapping and require clean-clone
   TypeScript plus production build evidence before public push.
6. Promote a generic nested file-link dependency checker if this pattern
   recurs on another package edge.

## Epistemic Process Block

### Expected Result / Prediction

A package declared in the deployment manifest and present in the public tree
should resolve after a clean install from the deployment base.

### Evidence Comparison

The warm provenance and public workspaces passed, but a detached public
worktree with only a cvf-web `npm ci` reproduced TS2307. The same clean
worktree passed TypeScript and the 121-page production build after adding the
narrow Truth Kernel source mapping.

### Contradiction Or Gap Disposition

The manifest was not missing. The contradiction came from different module
search roots between a warm multi-package workspace and the clean linked-source
deployment topology.

### Claim Update

A warm local build is not sufficient deployment evidence for nested `file:`
dependencies. Clean-base install and build evidence is required for this
topology.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | reviewer/closer and session-sync steward |
| Provider or surface | local private provenance workspace and detached public worktree |
| Session or invocation | Netlify Truth Kernel dependency repair learning capture, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | direct package/source reads, npm ci, TypeScript check, Next.js production build, apply_patch, ADIF integrity guard |
| Target paths | ADIF-0041 entry, entries README, and Guard Orientation README |
| Allowed scope source | operator instruction to record the cause as reusable learning |
| Before status evidence | the clean-install realpath resolution pattern existed only in repair evidence and session continuity |
| After status evidence | ADIF-0041 is resolver-discoverable and Guard Orientation exposes the pre-push prevention rule |
| Diff evidence | new entry plus two navigation/guidance rows in this material learning batch |
| Approval boundary | governance learning only; no new runtime, dependency, deployment, provider, or automatic mutation authority |
| Claim boundary | reusable guidance and machine-check candidate; current focused regression covers only the repaired Truth Kernel edge |
| Agent type | reviewer/closer |
| Invocation ID | `netlify-file-link-adif-0041-2026-07-18` |
| Expected manifest | ADIF-0041 entry, entries README row, Guard Orientation common-failure row |
| Actual changed set | ADIF-0041 entry, entries README row, Guard Orientation common-failure row |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance defect intelligence and operator guidance; no new
public-sync artifact is required for this learning record.

## Claim Boundary

This entry records the clean-install file-link resolution defect, the accepted
diagnostic sequence, and a bounded prevention rule. It does not claim a generic
machine checker exists, does not prove the current external Netlify deploy has
completed, and does not authorize dependency or deployment changes.
