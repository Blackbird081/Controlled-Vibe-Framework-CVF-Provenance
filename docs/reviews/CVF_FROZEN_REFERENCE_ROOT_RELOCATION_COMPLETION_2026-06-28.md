# CVF Frozen Reference Root Relocation Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: completion_review

Date: 2026-06-28

## Purpose

Record the bounded relocation of two low-value frozen reference roots out of
the visible repository root after their useful knowledge was already routed
through governed absorption artifacts.

## Target / Source

| Target | Source or evidence |
|---|---|
| Root lifecycle registry | `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json` |
| Ignore rules | `.gitignore` |
| Relocated CodeGraph source | `.private_reference/legacy/CodeGraph` |
| Relocated workspace-layer package | `.private_reference/legacy/CVF_WORKSPACE_LAYER_PRODUCTION_HANDOFF_PACKAGE` |
| Prior CodeGraph contract | `docs/reference/CVF_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_2026-06-20.md` |
| Prior CodeGraph root classification | `docs/reviews/CVF_PUSH_GATE_CODEGRAPH_ROOT_LIFECYCLE_REPAIR_COMPLETION_2026-06-27.md` |

## Scope / Methodology

The operator confirmed that `CVF_WORKSPACE_LAYER_PRODUCTION_HANDOFF_PACKAGE`
includes the same low-value frozen reference class as `CodeGraph` and asked to
move the material into legacy storage before changing roadmap focus.

The two local ignored folders were moved from repository root to
`.private_reference/legacy`. The root lifecycle registry entries were removed
because the folders are no longer visible root directories, and `.gitignore`
was simplified because `.private_reference/` already covers the relocated
legacy package contents.

## Findings / Position

Position: `ACCEPTED_CLOSED_PASS_BOUNDED`.

The relocation preserves prior governed absorption outcomes while reducing root
noise. `CodeGraph` remains usable as frozen internal reference material only.
The prior CGE-T1/CGE-T2 artifacts remain the governed evidence for absorbed
CodeGraph value; historical paths in those artifacts are not rewritten.

`CVF_WORKSPACE_LAYER_PRODUCTION_HANDOFF_PACKAGE` remains a local legacy
handoff package only. Its useful content must still be absorbed through fresh
CVF-governed reference, work-order, review, or roadmap artifacts before any
future canonical use.

## Risk / Corrective Action

| Risk | Corrective action | Result |
|---|---|---|
| Future agents treat `CodeGraph` as active root capability | Root directory removed from visible root and registry entry removed | PASS |
| Prior CGE historical evidence appears path-stale | This completion records relocation instead of rewriting historical artifacts | PASS |
| Raw packages are accidentally committed | `.private_reference/` ignore coverage remains active | PASS |
| Relocation is misread as runtime adoption | Claim boundary states no install, runtime, MCP, watcher, provider/live, or public-sync action | PASS |

## Decision / Disposition

Decision: `RELOCATE_TO_LEGACY_REFERENCE`.

Disposition: both folders are local legacy reference material under
`.private_reference/legacy`, not visible root surfaces. No roadmap, runtime,
provider/live, public-sync, checker, adapter, package activation, or
certification lane is opened by this relocation.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: operator-authorized lifecycle relocation, not a dispatched work order | no work order opened | PASS |
| Registry JSON | `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json` | root entries removed for relocated folders | PASS |
| Registry Markdown | BLOCKED with reason: no companion registry Markdown file is authorized or required for this JSON-only root lifecycle update | N/A | BLOCKED with reason |
| Ignore rules | `.gitignore` | explicit root ignores replaced by legacy-reference note | PASS |
| Completion review | `docs/reviews/CVF_FROZEN_REFERENCE_ROOT_RELOCATION_COMPLETION_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_FROZEN_REFERENCE_ROOT_RELOCATION_COMPLETION_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: no roadmap status or roadmap machine closure package is changed | no roadmap path changed | PASS |
| External evidence digest | N/A with reason: no new external artifact, source bundle, or live proof is consumed | no digest artifact required | N/A with reason |
| System loop interlock | N/A with reason: no system-loop interlock registry edit is authorized or required | no system-loop path changed | PASS |
| Runtime/source implementation | N/A with reason: relocation only | no runtime/source implementation authorized | PASS |
| Public export | N/A with reason: internal legacy relocation only | no public-sync remote, commit, or artifact path | PASS |
| Session continuity | N/A with reason: current mode and next allowed move are unchanged | no active-session surface update required | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the relocated folders are internal frozen reference material under
`.private_reference/legacy`. No public-sync mutation or public claim is made.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: remove the no-longer-visible root entries
for `CodeGraph` and `CVF_WORKSPACE_LAYER_PRODUCTION_HANDOFF_PACKAGE` after
operator-approved relocation to `.private_reference/legacy`.

Protected paths:

- `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json`
- `.gitignore`

Operator authorization: the operator stated that the remaining value is not
high enough to keep the packages at root and instructed relocation so work can
move to another roadmap.

Rollback boundary: if this relocation is rejected, restore only the two folders
to root, the two registry entries, the two explicit ignore rules, and this
completion note. Do not alter prior CGE-T1/CGE-T2 absorption artifacts or
current FPC-PRG roadmap/session state.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | 2026-06-28 frozen reference root relocation |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch, governance lifecycle checks |
| Target paths | `.gitignore`; `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json`; `docs/reviews/CVF_FROZEN_REFERENCE_ROOT_RELOCATION_COMPLETION_2026-06-28.md`; `.private_reference/legacy/CodeGraph`; `.private_reference/legacy/CVF_WORKSPACE_LAYER_PRODUCTION_HANDOFF_PACKAGE` |
| Allowed scope source | operator relocation instruction and prior frozen-reference classification |
| Before status evidence | baseHead `d749823c`; root folders existed and were ignored before relocation |
| After status evidence | root folders absent; legacy folders present under `.private_reference/legacy` |
| Diff evidence | `git diff --name-status d749823c` |
| Approval boundary | frozen reference root relocation only |
| Claim boundary | no runtime/source/test implementation, CodeGraph install/init, watcher/daemon, MCP wiring, benchmark, provider/live proof, public-sync, adapter implementation, package activation, certification, generated-state mutation, or roadmap selection |
| Agent type | single-agent relocation steward |
| Invocation ID | `frozen-reference-root-relocation-2026-06-28` |
| Expected manifest | `.gitignore`; `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json`; `docs/reviews/CVF_FROZEN_REFERENCE_ROOT_RELOCATION_COMPLETION_2026-06-28.md`; `.private_reference/legacy/CodeGraph`; `.private_reference/legacy/CVF_WORKSPACE_LAYER_PRODUCTION_HANDOFF_PACKAGE` |
| Actual changed set | `.gitignore`; `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json`; `docs/reviews/CVF_FROZEN_REFERENCE_ROOT_RELOCATION_COMPLETION_2026-06-28.md`; `.private_reference/legacy/CodeGraph`; `.private_reference/legacy/CVF_WORKSPACE_LAYER_PRODUCTION_HANDOFF_PACKAGE` |
| Manifest delta | MATCH |
| Deletion or rename disposition | root folders moved to ignored legacy reference storage |

## Claim Boundary

This completion records local frozen-reference relocation only. It does not
reopen CodeGraph absorption, workspace-layer absorption, FPC downstream
implementation, runtime/provider/live work, public-sync, MCP wiring, watcher or
daemon behavior, adapter implementation, package activation, certification, or
any new roadmap lane.
