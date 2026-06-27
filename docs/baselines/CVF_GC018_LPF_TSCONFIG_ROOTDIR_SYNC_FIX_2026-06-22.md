# CVF GC-018 - LPF Tsconfig RootDir Sync Fix

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-22

docType: baseline

EPISTEMIC_PROCESS_NA_WITH_REASON: focused TypeScript configuration fix; package
check output is the direct evidence comparison.

## Purpose

Record the focused Learning Plane TypeScript configuration fix needed before
session sync after AAF-T7C. The package check failed when the local config set
`rootDir` to the Learning Plane package directory while the package imports
contract types from sibling extension packages.

## Scope / Target / Owner Boundary

Allowed scope: the Learning Plane TypeScript config file and this baseline.

Forbidden scope: source/runtime behavior, generated aggregates, public-sync,
provider/live proof, broad extension refactors, package dependency changes, and
changes outside the focused TypeScript config boundary.

## Decision / Baseline / Proposed Tranche

Decision: CLOSED_PASS_BOUNDED.

Baseline: Learning Plane package check must allow the existing cross-extension
contract imports that are part of the current source graph.

Proposed tranche: LPF TypeScript config rootDir sync fix.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Learning Plane package check runs TypeScript with its package config | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/package.json` | `scripts.check` | `tsc -p tsconfig.json --noEmit` | npm package script | ACCEPT |
| Learning Plane source imports sibling Control Plane contracts | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/evaluation.engine.consumer.pipeline.contract.ts` | import declarations | sibling Control Plane contract imports | TypeScript source graph | ACCEPT |
| Config sets an explicit root for the Learning Plane package check | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tsconfig.json` | `compilerOptions` | `rootDir` | TypeScript compiler config | ACCEPT |

## Evidence / Verification

| Evidence item | Result |
|---|---|
| Before correction | `npm run check` failed with TS6059 because sibling extension files were outside `rootDir` |
| After correction | `npm run check` passed |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance configuration fix. No public-sync batch is
authorized.

## Required Artifact Manifest

| Artifact path | Required? | Final disposition |
|---|---|---|
| Learning Plane TypeScript config | yes | `rootDir` covers sibling extension imports |
| `docs/baselines/CVF_GC018_LPF_TSCONFIG_ROOTDIR_SYNC_FIX_2026-06-22.md` | yes | baseline/update evidence |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: operator-authorized focused config sync fix, not a delegated work order. | N/A with reason | N/A with reason |
| Completion or reviewer artifact | N/A with reason: this baseline is the focused update evidence artifact. | N/A with reason | N/A with reason |
| Roadmap state | N/A with reason: not roadmap-derived. | N/A with reason | N/A with reason |
| Registry JSON | N/A with reason: no generated aggregate edit. | N/A with reason | N/A with reason |
| Registry Markdown | N/A with reason: no markdown registry edit. | N/A with reason | N/A with reason |
| External evidence digest | N/A with reason: no external evidence. | N/A with reason | N/A with reason |
| System loop interlock | Learning Plane package check | PASS | PASS |
| Session continuity | follow-up session-sync after material commit | handoff/front-door/state evidence | PASS |

## Claim Boundary

This packet claims only that the Learning Plane TypeScript package check passes
with the explicit config root set high enough to include existing sibling
extension contract imports. It makes no runtime, provider, public, or product
behavior claim.
