# CVF Agent CLI/MCP Invocation-Control System-Chain Reassessment

Memory class: FULL_RECORD

docType: audit

Status: ACTIVE_AUDIT_ONLY_GLOBAL_ROADMAP_EXECUTION_MORATORIUM

Date: 2026-07-20

Operator authority: direct operator instruction to park every roadmap and
reassess all system-chain, workflow, and plane surfaces related to calling
another agent through CLI or MCP.

EPISTEMIC_PROCESS_NA_WITH_REASON: this opening audit records direct source
inspection and an operator stop decision. It does not close an implementation
tranche or claim live effectiveness proof.

## Purpose

Establish a repository-wide execution moratorium while CVF reassesses whether
it can effectively control the cost, quota, retries, duration, and termination
of another agent invoked through CLI or MCP. The immediate incident showed
that one shell-level Claude command expanded into 147 model responses and
47856327 cache-read tokens. A command invocation is therefore not a bounded
provider-call unit.

## Target / Source

The target is the private-provenance control path for delegated agent
execution: operator approval, orchestration, MCP/CLI launch, Model Gateway,
Execution Plane, timeout/cancellation, retry/fallback, telemetry, receipt, and
system-chain proof. Source authority comes only from CVF-governed repository
files and direct local git/source inspection. Claude JSONL and operator UI
screenshots remain incident inputs, not canonical CVF authority.

## Scope / Methodology

This opening pass used read-only source inspection across the system-chain map,
gap index, Control Plane orchestration contract, Execution Plane MAO launcher,
MCP invocation contracts, MCP server command launcher, Model Gateway quota and
fallback owners, review-cost standard, and the committed T0 incident evidence.

No agent CLI was launched. No MCP tool was invoked. No provider request, API
key, account subscription, retry, fallback, browser action, public-sync,
deployment, or production mutation was used. The only repository mutation in
the material batch is this audit and the status/authorization correction in
the current provider/model roadmap.

The moratorium applies globally to execution authority. It does not rewrite
historical status lines across every roadmap, because those lines are part of
the historical record and a mechanical bulk rewrite could falsely reclassify
closed or superseded work. If any roadmap-local status appears executable, the
operator moratorium in this audit and canonical active-session state takes
precedence until the operator explicitly lifts it.

## Findings / Position

Position: `CONTROL_NOT_EFFECTIVE_FOR_EXTERNAL_AGENT_CLI`

CVF currently has useful artifact governance, dispatch evidence, deterministic
contracts, and provider-request controls. It does not currently own or enforce
the end-to-end lifecycle of an external agent CLI process. Its existing
surfaces cannot prove that they can prevent the observed class of runaway
multi-response agent loop or its equivalent billed through operator API keys.

### Terminology collision

Several CVF proofs use `CLI` to mean CVF's own checker, hook, or operator
readout command. That is not evidence that CVF governs an external Claude,
Codex, or other agent CLI process. These two meanings must remain distinct:

| Term | Meaning | Current posture |
|---|---|---|
| CVF governance CLI | Local checker, hook, doctor, or static governed command | Implemented in bounded areas |
| External agent CLI | A provider agent process that may perform many internal model turns and tool calls | No effective lifecycle owner found |
| MCP invocation contract | Deterministic wrapper around caller-supplied invocation status and payload | Evidence contract, not an MCP process governor |
| Model Gateway request | One request through an injected provider adapter | Request-level control, not an agent-loop control |

### Source ownership map

| Surface | Direct source observation | Reassessment disposition |
|---|---|---|
| System-chain map | The `EVIDENCE_TO_OPERATOR_SURFACE` lane proves CLI checker/readout visibility | `NOT_EXTERNAL_AGENT_CLI_PROOF` |
| System-chain GAP index | GC-009/GC-010 already record no non-test production caller for MandatoryGateway and AgentExecutionRuntime | `NO_PRODUCTION_CALLER` |
| Control Plane orchestration contract | Assignment, dependency, and hash contract; no process identity, hard cost ceiling, spawn, streaming monitor, or kill owner | `CONTRACT_ONLY` |
| MAO operational worker launcher | File states there is no CLI/MCP/UI/runtime caller; execution is through an injected adapter | `NO_EXTERNAL_AGENT_CALLER` |
| MAO launcher timeout | Timeout is recorded from durable state after launch; it does not terminate a live external process | `POST_HOC_STATE_ONLY` |
| MCP invocation contract | `invoke()` hashes request plus caller-supplied status and payload | `EVIDENCE_WRAPPER_ONLY` |
| MCP consumer pipeline | Composes the invocation receipt with caller-supplied results | `CONTRACT_ONLY` |
| MCP generic-agent adapter | Source explicitly states advisory-only behavior and `runtimeAdapterAuthorized: false` | `ADVISORY_ONLY` |
| Governed command launcher | Real `spawn()` owner, limited to static profiles including git status, git diff check, and approval marker behavior | `REAL_RUNTIME_NOT_AGENT_CLI` |
| Governed command timeout | Calls `child.kill()` with `detached: false`; no descendant-tree termination proof | `PROCESS_TREE_CONTROL_NOT_PROVEN` |
| Model Gateway quota ledger | In-memory daily request/estimated-token/actual-token counters; permits when no limit is configured | `PROVIDER_REQUEST_LEDGER_ONLY` |
| Provider execution bridge | Checks quota before adapter use, then records usage after successful adapter completion | `NO_IN_FLIGHT_AGENT_LOOP_STOP` |
| Fallback policy | Defaults to as many as three attempts when not overridden | `NO_GLOBAL_OPERATOR_ENVELOPE` |
| Review-cost control standard | Defines evidence shape and diminishing-return review behavior but excludes live provider/quota accounting | `POST_HOC_EVIDENCE_ONLY` |

### Missing end-to-end control chain

| Required control point | Current evidence | Disposition |
|---|---|---|
| Operator-approved provider/model/account envelope | Documentation packet exists | `DOCUMENTED_NOT_RUNTIME_BOUND` |
| Admission check before external agent launch | No production external-agent launcher owner found | `MISSING_OWNER` |
| Exact process and descendant identity | No canonical receipt binding process tree to assignment | `MISSING_OWNER` |
| Streaming turn/response/tool telemetry | No cross-provider agent-loop collector found | `MISSING_OWNER` |
| Input, output, cache, quota, time, and money ceilings | Partial provider-request counters only | `NOT_EFFECTIVE_FOR_AGENT_CLI` |
| In-flight hard stop | No evidence of an external agent-loop interrupt owner | `MISSING_OWNER` |
| Complete process-tree termination | Static launcher uses child-only kill semantics | `NOT_PROVEN` |
| Retry and fallback budget shared across callers | Local fallback attempt limit exists, not a global assignment envelope | `NOT_EFFECTIVE_FOR_AGENT_CLI` |
| Secret-safe failure diagnostic | Diagnostic standard exists | `DOCUMENTED_PARTIAL` |
| Assigned-versus-actual provider/model reconciliation | T0 documentation design exists | `DOCUMENTED_NOT_IMPLEMENTED` |
| Subscription quota reconciliation | Provider UI snapshots and local JSONL remain different evidence classes | `NO_MACHINE_RECONCILIATION` |
| API-key spend reconciliation | No live spend owner connected to external agent CLI | `MISSING_OWNER` |

## Quality Findings

| Finding | Severity | Evidence | Consequence |
|---|---|---|---|
| F-01 No runtime owner governs an external agent CLI lifecycle | CRITICAL | MAO has no CLI/runtime caller; MCP adapter is advisory; static launcher has no agent profile | CVF cannot claim control of delegated agent execution |
| F-02 One shell command is not one model response | CRITICAL | T0 packet author expanded to 147 unique responses | Command-count caps do not bound quota or API cost |
| F-03 No preemptive or in-flight multi-dimensional budget | CRITICAL | Existing quota ledger is request-oriented and records successful use after adapter return | Runaway loops can consume the entire session or account budget before CVF reacts |
| F-04 Timeout semantics do not prove process-tree termination | HIGH | MAO records timeout state; static launcher calls child-only kill | Descendants may continue after caller timeout |
| F-05 MCP naming overstates runtime control | HIGH | Invocation contract accepts status/payload from caller and hashes them | Reviewers may mistake receipt construction for enforcement |
| F-06 Existing CLI proof is semantically narrower than agent CLI control | HIGH | System-chain evidence lane cites checker and hook readouts | A broad CLI claim can mask the missing external-agent edge |
| F-07 Retry/fallback ownership is fragmented | HIGH | Model Gateway fallback defaults locally to three attempts | One operator assignment has no shared cross-caller burn envelope |
| F-08 Governance overhead can amplify the agent loop | HIGH | Packet author used 73 Bash, 57 Read, and 21 Edit calls | CVF's many distributed requirements can increase context churn and quota burn |
| F-09 Subscription quota is opaque and API-key exposure can become financial | CRITICAL | UI percent, JSONL tokens, and billed cost are separate evidence classes | The same loop may exhaust a plan or produce uncontrolled charges |
| F-10 System-chain topology omits the external-agent invocation edge | HIGH | Current map has no admission-to-process-to-budget-to-kill chain | No owner, proof class, or fail-closed boundary is visible end to end |

## Risk / Corrective Action

Immediate corrective action is a global execution moratorium, not another
agent test. Every roadmap execution lane is parked. The previously released T0
R1 Claude rerun is revoked. No agent, provider, API-key, MCP live, fallback, or
subscription-backed invocation may be started from a roadmap while this
moratorium is active.

The audit may continue with local read-only source inspection and local
non-provider static checks. It must not create a work order, dispatch a worker,
run a live proof, or treat a smaller prompt as an adequate fix.

The minimum future control design must make one operator-approved assignment
the enforceable parent of all attempts and descendants. It must define hard
admission ceilings, streaming usage capture when the provider exposes it,
wall-clock and idle ceilings, cumulative retry/fallback ceilings, process-tree
termination, and explicit fail-closed behavior when usage cannot be measured.
Provider-neutrality is required; operator-supplied API keys and account
subscriptions are access modes, not hardcoded platform choices.

## Decision / Recommendation

Decision: `GLOBAL_ROADMAP_EXECUTION_MORATORIUM_ACTIVE`

The audit proceeds in four read-only questions, not implementation tranches:

1. Which component actually owns every possible external-agent CLI/MCP launch?
2. What exact sequence connects operator approval to process identity, usage
   telemetry, stop enforcement, diagnostic, and receipt reconciliation?
3. Which existing controls are runtime-effective, evidence-only, advisory,
   uncalled, or missing?
4. What is the smallest provider-neutral architecture that can fail closed
   before any further delegated-agent test is authorized?

The moratorium may be lifted only by a fresh explicit operator decision after
the audit produces an evidence-backed control architecture and bounded proof
plan. A roadmap status, old work order, subscription reset, available API key,
or model availability cannot lift it implicitly.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Lane | Disposition | Rationale / next owner |
|---|---|---|---|---|
| F-01, F-02, F-03 | RUNTIME_SIGNAL_GAP | COST_ECONOMICS_LEARNING | DESIGN_REVIEW_REQUIRED | Invocation admission and in-flight budget ownership require architecture review before implementation |
| F-04 | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | Process-tree termination semantics need a provider-neutral runtime owner and negative proof |
| F-05, F-06, F-10 | OPERATOR_SCOPE_CLARITY_GAP | DOCUMENTATION_ONLY_LEARNING | MACHINE_CHECK_CANDIDATE | Future system-chain claims must distinguish CVF command-line readout from external-agent CLI enforcement |
| F-07 | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | Retry and fallback require one cumulative operator envelope across launch surfaces |
| F-08 | ORCHESTRATOR_PACKET_GAP | COST_ECONOMICS_LEARNING | DESIGN_REVIEW_REQUIRED | Governance input size and gate loops need cost-aware compilation rather than discovery inside a paid agent loop |
| F-09 | RUNTIME_SIGNAL_GAP | COST_ECONOMICS_LEARNING | RUNTIME_LEARNING_CANDIDATE | Subscription quota, token telemetry, and API spend need distinct adapters and evidence classes |

No ADIF entry is promoted in this opening pass because the audit has not yet
completed cross-surface recurrence analysis. Any repeated or non-obvious defect
confirmed before audit closure must be promoted to the shared ADIF registry,
not retained only in provider-local memory.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator quota incident and effectiveness critique to a CVF-owned invocation-control system-chain reassessment |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this private audit and canonical active-session moratorium |
| Disposition | ADAPT as CVF-owned evidence input; do not treat provider UI or local JSONL as canonical authority |
| Claim boundary | operator evidence establishes the incident and stop decision; runtime-control claims require CVF source and later bounded proof |

## Epistemic Process Block

| Field | Evidence |
|---|---|
| Expected Result | Existing CVF planes might provide at least a partial runtime chain capable of bounding an external agent CLI |
| Evidence Comparison | Direct source inspection found contract, receipt, advisory, static-command, and provider-request controls, but no owner for an external agent process and its internal multi-response loop |
| Contradiction | The broad phrase `CLI proof` is true for local governance readouts but false if interpreted as external-agent lifecycle enforcement |
| Claim Update | The CVF control claim is narrowed to artifact governance and bounded provider-request controls; external-agent CLI control is not effective |
| Confidence | HIGH for the inspected canonical surfaces; audit remains open for exhaustive caller enumeration |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/orchestrator |
| Provider or surface | Local private provenance repository only |
| Session or invocation | agent-cli-mcp-control-reassessment-opening-2026-07-20 |
| Working directory | repository root |
| Command or tool surface | read-only PowerShell, rg, git inspection, and apply_patch |
| Target paths | this audit, the current provider/model roadmap status correction, and the GC-051 source/aggregate registration pair |
| Allowed scope source | direct operator instruction to park every roadmap and review all MCP/CLI-related system chains, workflows, and planes |
| Before status evidence | T0 R1 external Claude worker was waiting for subscription reset under interim caps |
| After status evidence | T0 R1 authorization revoked; all roadmap execution superseded by audit-only moratorium |
| Diff evidence | material changed-set evidence must be recomputed before commit |
| Approval boundary | audit and parking only; no implementation, work order, agent call, provider call, or public action |
| Claim boundary | source-backed opening verdict; no live effectiveness proof |
| Agent type | reviewer/orchestrator |
| Invocation ID | agent-cli-mcp-control-reassessment-opening-2026-07-20 |
| Expected manifest | this audit; current provider/model roadmap; GC-051 source entry; generated GC-051 aggregate |
| Actual changed set | this audit; current provider/model roadmap; GC-051 source entry; generated GC-051 aggregate |
| Manifest delta | MATCH |

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: this is a private control-gap audit and global execution stop. No public
artifact, public-sync change, catalog claim, push, or publication is authorized.

Next action: keep private until the operator accepts a control architecture and
separately authorizes any public treatment.

## Claim Boundary

This audit does not claim exhaustive caller enumeration yet, implementation,
runtime interception, process-tree termination, live quota measurement, API
cost measurement, provider-neutral parity, MCP enforcement, production
readiness, public readiness, or safe unattended orchestration. It establishes
an evidence-backed opening verdict and an operator-authorized stop boundary.
