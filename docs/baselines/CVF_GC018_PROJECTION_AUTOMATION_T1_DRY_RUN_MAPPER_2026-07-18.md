# CVF GC-018 Projection Automation T1 Dry-Run Mapper Baseline

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-18

Batch ID: CVF-PROJECTION-AUTO-T1

Base head before packet authoring: `20ba27996`

## Purpose

Authorize one bounded implementation tranche for a parameterized, fail-closed,
dry-run-only projection mapper, its policy manifest, focused tests, receipt
schema, one test receipt, and a no-commit worker return.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-PROJECTION-AUTO-T1 --title "Projection Automation Dry-Run Mapper" --date 2026-07-18 --base 20ba27996 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | populated verified source, dry-run design, dependency, receipt, and closure controls |
| checkerReadAheadConfirmation | dispatch-quality, machine-closure, structural, public-disposition, and file-size checkers |
| docOnlyNewFields | mapper and receipt contract fields are new in T1 |
| claimBoundary | dispatch baseline provenance only |

## Proposed Tranche / Decision

Proceed with T1 as a six-path, dry-run-only implementation tranche. Keep T2
held until independent review accepts the mapper, tests, and receipt evidence.

## Target / Source

Target: the six paths listed in the paired T1 work order. Source authority:
the accepted T0 ledger and completion review, current public-sync script,
workspace updater path guard, and current cvf-web registry/package metadata.

## Scope / Target / Owner Boundary

T1 may implement read-only inventory, classification, root/remote/dirty checks,
path-containment checks, deterministic receipt creation, and focused disposable
tests. The only permitted filesystem write by the mapper is the explicitly
requested receipt output. No target copy/apply, stage, commit, push, Web repair,
provider call, deployment, or production action is authorized.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| T0 accepted closure | `docs/reviews/CVF_PROJECTION_AUTOMATION_T0_COMPLETION_REVIEW_2026-07-18.md` | `38ec816f9` | PASS |
| T0 registry evidence correction | ledger and completion review erratum | `20ba27996` | PASS |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| public-sync parameters distinguish dry-run, no-commit, and no-push | EXISTS | `scripts/cvf-public-sync.ps1` | lines 23-27 | `DryRun` | script parameter block | ACCEPT |
| public target remote is pinned | VALUE_SET | `scripts/cvf-public-sync.ps1` | lines 33-34 | `PUBLIC_REMOTE` | public-sync root validation | ACCEPT |
| allowlist groups exist | EXISTS | `scripts/cvf-public-sync.ps1` | lines 37-141 | `ALLOWED_TREES` | public export enumeration policy | ACCEPT |
| mapped exports exist | EXISTS | `scripts/cvf-public-sync.ps1` | lines 95-108 | `MAPPED_FILES` | mapped public exports | ACCEPT |
| deny patterns exist | EXISTS | `scripts/cvf-public-sync.ps1` | lines 144-167 | `DENY_PATTERNS` | defense-in-depth filter | ACCEPT |
| allowlist enumeration functions are embedded in sync script | EXISTS | `scripts/cvf-public-sync.ps1` | lines 171-224 | `Get-AllowedFiles` | public-sync script-local functions | ACCEPT |
| missing public root and wrong remote abort | RUNTIME_BEHAVIOR | `scripts/cvf-public-sync.ps1` | lines 234-247 | `PUBLIC_SYNC_ROOT` | public-sync preflight | ACCEPT |
| path-containment guard throws on escape | RUNTIME_BEHAVIOR | `scripts/update_cvf_workspace_public_core.ps1` | lines 59-66 | `Assert-PathInsideWorkspace` | workspace updater | ACCEPT |
| cvf-web registry read model exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts` | lines 60-271 | `getRuntimeModuleRegistry` | runtime module registry | ACCEPT |
| SOT3 registry entries currently exist | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts` | lines 162-188 | `cvf-refinery` | `MODULES` | ACCEPT |
| cvf-web dependency metadata exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependencies section | `dependencies` | package manifest | ACCEPT |

## New Doc-Only Fields

The mapper and receipt fields below are new T1 contract fields, not claims that
they already exist: `schemaVersion`, `receiptId`, `sourceRoot`, `targetRoot`,
`cvfWebRoot`, `rootsValidated`, `policyParity`, `candidateAction`,
`matchedAllowlistRule`, `matchedDenyPattern`, `pathEscapeChecksRun`,
`deniedPathCount`, `semanticReviewFlagCount`, `noTargetWriteConfirmation`.

## Design Control Gate

- roots are explicit parameters or safely discovered, then canonicalized;
- provenance and public-sync origins are validated against distinct remotes;
- dirty provenance or public-sync roots fail before mapping;
- policy is read from the new JSON manifest and parity-tested against the
  existing script without invoking or dot-sourcing its mutating flow;
- candidate actions distinguish absent-target mechanical candidates, changed
  semantic-review flags, unchanged skips, denied skips, and not-allowlisted skips;
- output ordering and receipt hashing are deterministic;
- receipt output must remain outside both projected target trees unless it is
  the exact worker-owned test receipt path;
- no apply parameter or hidden write branch exists in T1.

## Acceptance Criteria

- AC-01: default and only mode performs no target mutation.
- AC-02: missing root, wrong remote, dirty root, and path escape fail closed.
- AC-03: policy parity test covers all allow, mapped, and deny groups.
- AC-04: changed content is flagged for semantic review, never auto-approved.
- AC-05: current SOT3 registry entries are observed, not falsely reported absent.
- AC-06: identical fixture inputs produce byte-identical JSON and receipt ID.
- AC-07: receipt is secret-free and reconciles action/count fields.

## Evidence / Verification

Evidence requires the focused PowerShell test matrix, policy-parity output,
deterministic receipt comparison, before/after disposable-root status, exact
six-path worktree evidence, worker-fast, reviewer-fast, autorun, and file-size
gates. Test output is implementation evidence, not live/public proof.

## Dual Agent Surface Matrix

| Surface | Interface | Authority/risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | local PowerShell CLI | read-only target audit plus explicit receipt output | focused tests and JSON receipt | filesystem/git command adapter | ACCEPT |
| EXTERNAL_AGENT_CLI_MCP | documented CLI invocation only | no MCP server, provider, or remote execution authority | CLI help text | same local CLI; no external adapter | DEFER_WITH_REASON |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; Machine Closure Package; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation and evidence for T1 dispatch completeness, not first discovery |
| claimBoundary | bounded dry-run mapper dispatch only |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this baseline | `Status: DISPATCH_READY` | PASS |
| Work order status | paired T1 work order | `Status: DISPATCH_READY` | PASS |
| Completion or reviewer artifact | future T1 review | dependency-held | N/A with reason |
| Worker return | future T1 return | worker-owned | N/A with reason |
| Roadmap state | automation roadmap | `Status: T0_PASS_BOUNDED_T1_DISPATCH_READY_T2_HELD` | PASS |
| Registry JSON | existing GC-051 coverage | aggregate drift checked | PASS |
| Registry Markdown | existing registry front door | no new family required | PASS |
| External evidence digest | repository-local evidence only | none | N/A with reason |
| System loop interlock | no loop owner changed | none | N/A with reason |
| Session continuity | protected surfaces | separate sync | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| target writes | zero | implementation dependency-held | N/A with reason |
| deterministic receipt | byte-identical repeated fixture output | implementation dependency-held | N/A with reason |
| fail-closed matrix | four negative classes | implementation dependency-held | N/A with reason |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`projection automation implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "projection automation implementation" --role dispatcher --lifecycle-phase pre-dispatch --json`

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T1 implements and tests private provenance tooling only.

## Claim Boundary

This baseline authorizes only the six-path T1 worker scope. It does not prove
the mapper until worker tests and independent review pass, and it authorizes no
apply, target mutation, public commit/push, provider/live call, or production use.
