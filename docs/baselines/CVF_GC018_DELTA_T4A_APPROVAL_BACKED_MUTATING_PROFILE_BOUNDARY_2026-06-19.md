# CVF GC-018 - Delta-T4A Approval-Backed Mutating Profile Boundary

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-19

Owner: Codex

Execution route: SINGLE_AGENT_MULTI_ROLE

Base head: `5c718d46`

## Purpose

Authorize one bounded Delta-T4A dispatch after Delta-T1, Delta-T2, Delta-T3,
MCP-to-Model-Gateway Composition Proof, and EKA-R1 closed bounded.

Delta-T4A is the first approval-backed mutating execution boundary. It must not
open arbitrary commands, EDIT/COMMIT execution, direct IDE or shell
interception, provider/live calls, public-sync, queues, daemons, or universal
governed-coding claims.

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
| --- | --- |
| Decision | Closed one bounded local mutating-profile boundary implementation |
| Proposed tranche | Delta-T4A Approval-Backed Mutating Profile Boundary |
| Base head | `5c718d46` |
| Material commit | `d2fc4f5b` |
| Accepted-material session sync | `136b9095` |
| Worker / reviewer / closer | Codex across phase-separated roles |
| Route | `SINGLE_AGENT_MULTI_ROLE` |
| Upstream evidence | Delta-T1/T2/T3 closures, MCP-Gateway Composition Proof, EKA-R1 guard, workspace runtime contract |
| Later tranche | EDIT/COMMIT profiles, arbitrary mutating commands, IDE/shell interception, and mandatory governed-coding control remain separate authorization |

## Scope / Target / Owner Boundary

Allowed scope:

- extend the existing `cvf-governed-exec` launcher with one static mutating
  profile named `approval-marker-write`;
- keep the command shape CVF-owned and static, with no caller-supplied
  executable, shell text, environment override, interpreter eval, or arbitrary
  argument passthrough;
- add a deterministic approval policy record for the profile, including required
  approval role, approval token shape, target-file allowlist, mutation budget,
  and expiration window;
- require a Delta-T1 preflight `RUN` receipt, Delta-T2 one-time consumption,
  Delta-T3 execution intent, and Delta-T4A approval evidence before the runner
  can start;
- write only a bounded approval marker file inside the resolved workspace root
  at a fixed profile-owned target path;
- persist secret-safe approval and execution evidence without raw output or
  credential-bearing values;
- add focused tests, completion review, and evidence JSON.

Forbidden scope:

- no arbitrary executable, caller-supplied command args, shell/interpreter eval,
  npm script profile, provider/live call, network call, queue, daemon, CVF Web
  action, public-sync, registry mutation, or external repo mutation;
- no EDIT or COMMIT execution profile;
- no direct IDE, shell, git, filesystem, or non-wrapper interception;
- no claim that every coding action is governed;
- no provider/live, production, release, public, or external-facing readiness
  claim.

Risk ceiling: R2 local deterministic runtime implementation. The shipped T4A
profile is mutating only inside a fixed workspace-local marker path and must be
approval-backed before execution.

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Delta-T3 currently ships only two static read-only Git profiles. | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 26-29 and 42-55 | `GOVERNED_COMMAND_PROFILE_IDS`; `getGovernedCommandProfile` | Delta-T3 launcher | ACCEPT |
| Delta-T3 profile shape contains id, executable, args, and risk level only. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 32-37 | `GovernedCommandProfile` | Delta-T3 launcher | ACCEPT |
| Delta-T3 runner uses direct child process execution with `shell:false`. | LITERAL_INVARIANT | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 88-104 | `shell` | Delta-T3 runner | ACCEPT |
| Delta-T3 launcher builds a canonical action and calls Delta-T1 preflight before consumption. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 255-278 | `buildGovernedCommandAction`; `preflightGovernanceAction` | `launchGovernedCommand` | ACCEPT |
| Delta-T3 launcher consumes the matching receipt before execution intent. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 278-331 | `consumeGovernanceActionReceipt`; `beginExecution` | `launchGovernedCommand` | ACCEPT |
| Delta-T3 launcher invokes the runner only after durable admission stages. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 333-339 | `run` | `launchGovernedCommand` | ACCEPT |
| Delta-T1 supports `RUN` as a preflight action class. | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts` | lines 30-34 | `PREFLIGHT_ACTION_CLASSES`; `RUN` | Delta-T1 preflight | ACCEPT |
| Guard context already supports target files, mutation count, mutation budget, scope, and metadata. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/types.ts` | lines 27-40 | `GuardRequestContext` | guard runtime types | ACCEPT |
| Delta-T2 consumption markers remain one-time and do not prove action execution. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-receipt-consumption.store.ts` | lines 24-39 and 73-91 | `ReceiptConsumptionMarker`; `claimReceipt` | receipt consumption store | ACCEPT |
| Delta-T3 execution receipt records status and keeps external interception false. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts` | lines 11-29 and 119-127 | `GovernedExecutionReceipt`; `finalizeExecution` | governed execution store | ACCEPT |
| MCP package publishes `cvf-governed-exec` through package bin metadata. | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json` | lines 7-10 | `cvf-governed-exec` | npm package manifest | ACCEPT |
| Runtime expansion requires fresh work order control blocks and does not authorize queues, providers, public-sync, UI, or readiness by default. | LITERAL_INVARIANT | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | lines 43-56 and 102-109 | `Runtime Expansion Boundary`; `Work Order Requirement` | runtime expansion readiness contract | ACCEPT |

## New Delta-T4A Fields

These are new authorized fields, not existing runtime facts.

| New item | Required value or shape | Purpose |
| --- | --- | --- |
| profile id | `approval-marker-write` | first bounded mutating profile |
| profile kind | `MUTATING_FIXED_WORKSPACE_FILE` | distinguish mutating from read-only T3 profiles |
| approval policy contract | `cvf.delta.mutatingProfileApprovalPolicy.v1` | stable local approval evidence |
| approval record | profile id, role, approval token id/hash, issued/expiry timestamps, target allowlist, mutation budget | prove approval before mutation |
| approval verdict | `APPROVED`, `BLOCKED`, or `EXPIRED` | fail closed before runner |
| mutation target | fixed workspace-relative marker path owned by profile | prevent arbitrary file mutation |
| mutation claim marker | bounded to wrapper-owned marker write only | avoid EDIT/COMMIT or universal claims |

## Delta-T4A Execution Control Block

| Field | Disposition |
| --- | --- |
| Action class | `RUN` only; no EDIT or COMMIT profile |
| Mutating profile | `approval-marker-write` only |
| Command authority | static CVF-owned profile registry and profile-owned target path |
| Approval sequence | T1 durable ALLOW receipt -> T2 atomic consumption -> T3 durable intent -> T4A approval verdict -> direct runner |
| Approval role | `OPERATOR` or source-compatible explicit approved test role in focused tests |
| Approval expiry | required; expired approval blocks execution |
| Target files | fixed allowlist; no caller-selected arbitrary path |
| Process API | injected runner; production adapter uses direct executable with `shell:false` |
| Output | bounded capture; known credential patterns redacted; raw output not persisted |
| Receipt persistence | execution receipt plus secret-safe T4A approval evidence |
| Failure posture | no runner call before all durable admission and approval stages pass |
| Execution claim | bounded to wrapper-owned marker write |
| Interception claim | always `externalInterceptionProved=false` |
| Provider boundary | no provider or Model Gateway execution |
| Public boundary | private provenance only |

## External Knowledge Intake Routing

| Required row | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | Runtime/MCP claim must cite current runtime proof, MCP boundary, and work-order source verification before implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; work-order dispatch-quality gate; agent workspace runtime boundary guard |
| Owner surface | Delta-T4A GC-018 and work order |
| Disposition | `BLOCKED_UNTIL_CVF_PROOF` for universal or external interception claims; `DO_NOW` only for bounded wrapper-owned marker mutation |
| Claim boundary | no universal governed-coding, external interception, provider/live, public, production, release, or readiness claim |

## Rescan Intelligence Hardening

- Original source artifact: Delta-T3 completion and active next allowed move.
- Predecessor intake artifact:
  `docs/reviews/CVF_DELTA_T3_GOVERNED_COMMAND_LAUNCHER_COMPLETION_2026-06-19.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because mutating execution moves
  from parked to a single bounded approval-backed profile.
- Routing matrix status: `DO_NOW` for one fixed marker-write profile;
  `SEPARATE_RUNTIME_TRANCHE` for EDIT/COMMIT, arbitrary commands, npm scripts,
  provider/live, public-sync, queue/daemon, and interception.
- Semantic sampling status: `PARTIAL_TARGETED`, covering missing approval,
  expired approval, wrong target, replay, cwd escape, runner failure, output
  redaction, and non-wrapper claim rejection.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE
- Machine guard: `governance/compat/check_rescan_intelligence_hardening.py`

### Original-Intake Delta Ledger

| Current item | Delta category | Original disposition | Updated disposition | Rationale |
| --- | --- | --- | --- | --- |
| T1 preflight | `UNCHANGED_FROM_INTAKE` | closed bounded and reused by T3 | reused by T4A without contract mutation | prevents duplicate preflight authority |
| T2 consumption | `UNCHANGED_FROM_INTAKE` | closed bounded and reused by T3 | reused by T4A without contract mutation | preserves one-time receipt consumption |
| T3 execution intent | `UNCHANGED_FROM_INTAKE` | closed bounded for read-only profiles | reused before T4A approval gate | preserves admission-before-run evidence |
| T4A approval evidence | `NEW_FINDING` | absent from T3 | required before one bounded mutation | adds approval between intent and runner |
| Mutating profile | `CHANGED_DISPOSITION` | parked after T3 | opened only as fixed marker-write profile | bounded mutation gives next enforcement step |
| Arbitrary commands and EDIT/COMMIT | `REMOVED_OR_REJECTED` | parked after T3 | still rejected from T4A | exceeds approval-marker boundary |

### Follow-Up Routing Matrix

| Lane | Applies to | Rationale |
| --- | --- | --- |
| DO_NOW | `approval-marker-write` with fixed target and approval evidence | bounded T4A implementation |
| RESOLVED_BY_DESIGN | T1/T2/T3 durable admission chain | reuse existing owners instead of duplicating them |
| SEPARATE_RUNTIME_TRANCHE | EDIT/COMMIT, npm scripts, arbitrary commands, broader mutating profiles | materially higher execution risk |
| STRATEGIC_OPERATOR_DECISION | direct IDE/shell/git/filesystem interception | changes operator workflow and control reach |
| OUT_OF_SCOPE | provider/live, public-sync, queue, daemon, readiness | unnecessary for T4A proof |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | required verdict |
| --- | --- | --- | --- | --- | --- |
| DELTA-T4A-01 | T3 execution chain | runner starts only after durable admission | `UNCHANGED_FROM_INTAKE` | Can mutation run before T1/T2/T3 success? | No runner call before all T1/T2/T3 stages pass |
| DELTA-T4A-02 | T4A approval evidence | approval is required for mutation | `NEW_FINDING` | Can missing or expired approval still write? | No runner call before valid approval |
| DELTA-T4A-03 | fixed target boundary | profile owns the target path | `CHANGED_DISPOSITION` | Can caller choose arbitrary target file? | No caller-selected target path |
| DELTA-T4A-04 | claim boundary | wrapper mutation improves governed execution | `REMOVED_OR_REJECTED` | Does this prove direct IDE/shell interception? | No; external interception remains false |

## Acceptance Criteria

| ID | Criterion | Closure state |
| --- | --- | --- |
| AC1 | T4A adds exactly one mutating static profile and leaves T1/T2 contracts unchanged. | PASS |
| AC2 | Runner is unreachable unless T1 ALLOW, T2 consumption, T3 intent, and T4A approval all succeed. | PASS |
| AC3 | The mutating profile can write only the fixed marker target inside the resolved workspace root. | PASS |
| AC4 | Missing, expired, wrong-profile, or wrong-target approval blocks before runner. | PASS |
| AC5 | CLI remains strict and does not expose arbitrary executable, args, env, shell, EDIT, or COMMIT. | PASS |
| AC6 | Approval and execution evidence are secret-safe and do not persist stdout/stderr or raw credential values. | PASS |
| AC7 | Focused tests, full MCP tests, build, smoke proof, reviewer-fast, and governance gates pass. | PASS |
| AC8 | No provider/live, public-sync, queue, daemon, workspace-state, external interception, or universal enforcement claim occurs. | PASS |

## Evidence / Verification

Required evidence:

- focused Vitest for approval pass/block/expiry/target mismatch, admission
  ordering, fixed target mutation, cwd containment, durable evidence, runner
  failure, and output redaction;
- full MCP package test suite and TypeScript build;
- bounded local smoke using the single marker-write profile in a temporary
  workspace and secret-safe receipt directory;
- `git diff --check`, exact changed-set evidence, reviewer-fast, autorun phase
  gates, and commit-steward preflights;
- no provider/live receipt because provider behavior is outside this tranche.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Delta runtime tranche. No public-sync authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Baseline status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_FOR_CODEX_2026-06-19.md` | source-verified closure packet | PASS |
| Material implementation | MCP package source/tests and completion evidence | material commit `d2fc4f5b` | PASS |
| Provider/live proof | N/A with reason: no provider claim | no live provider command | N/A with reason |
| Public-sync | N/A with reason: not authorized | `DEFERRED_PRIVATE_ONLY` | N/A with reason |

## Claim Boundary

Delta-T4A may prove only that `cvf-governed-exec` can run one exact
approval-backed workspace-local marker-write profile after durable T1/T2/T3/T4A
controls. It does not prove direct IDE or shell actions are intercepted, make
the wrapper mandatory outside its own process path, execute arbitrary EDIT or
COMMIT actions, run providers, or establish universal governed coding.
