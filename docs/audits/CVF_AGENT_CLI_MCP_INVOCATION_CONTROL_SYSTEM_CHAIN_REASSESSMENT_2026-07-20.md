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
| Chain map route | operator quota incident, effectiveness critique, and external MCP/CLI architecture proposal to a CVF-owned invocation-control system-chain reassessment |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this private audit and canonical active-session moratorium |
| Disposition | ADAPT_SELECTIVELY; retain useful architecture patterns, reject unsupported control claims, and do not promote the external proposal to CVF authority |
| Claim boundary | operator evidence establishes the incident and stop decision; the proposal contributes design hypotheses only; runtime-control claims require CVF source and later bounded proof |

## External Proposal Selective Absorption Record

Source input:
`.private_reference/legacy/CVF_MCP 20.07/De_xuat_xay_dung_CVF_MCP.md`

Source authority disposition: `NOT_CVF_SOURCE`

Absorption disposition: `ADAPT_SELECTIVELY`

The proposal is retained as external design input only. It is not sufficient
evidence for fixing the current invocation-control defect and does not lift the
global execution moratorium.

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/legacy/CVF_MCP 20.07/De_xuat_xay_dung_CVF_MCP.md` |
| Enumeration command | exact operator-named single-file lookup followed by complete UTF-8 file read |
| Manifest artifact or inline manifest | inline one-item source record in this audit: 13175 bytes; SHA-256 `3e15e6c47221acbde1c437b57d91e05e0f693f47c02cf73e8182b2be543aaff2` |
| Processing ledger artifact or inline ledger | inline Retained ideas and Rejected or unproven claims tables in this audit |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE; actual item status is READ with selective ADAPTED and REJECTED claims |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE; actual aggregate disposition is ADAPT_SELECTIVELY |
| Owner-surface map | inline Overlap And Novelty Classification table below |
| Unresolved items | 0 source files; authoritative knowledge gaps remain explicitly carried forward |
| Completion claim boundary | complete evaluation of one external proposal, not implementation readiness or runtime-control proof |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| layered transport/policy/execution concept | separation of responsibilities | DOCTRINE_ADAPTED | current system-chain reassessment | retain as a later architecture constraint | no runtime or package change |
| one core and two surfaces | shared truth with role-specific projections | PACKAGE_CANDIDATE | future control-state projection design | reconsider only after authoritative knowledge absorption | no package activation |
| external-agent lifecycle control | missing supervisor responsibilities exposed by comparison | RUNTIME_CANDIDATE | future provider-neutral invocation supervisor design | require threat model and authoritative runtime semantics first | no runtime implementation |
| CLI versus external-agent CLI terminology | claim-scope distinction | CHECKER_CANDIDATE | future system-chain claim-quality owner | consider only after audit confirms recurrence and smallest check | no checker edit or wiring |
| absolute MCP compliance and prompt-injection prevention | unsupported security claims | REJECT_DIRECT_IMPORT | none | retain explicit rejection | no direct import |
| TUI colors, seven-column board, and unmeasured token multiplier | presentation detail without current control value | NO_PACKAGE_OR_RUNTIME_VALUE | later product research only | revisit only after runtime control is proven | no package or runtime value now |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| layered MCP, policy, and CLI separation | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` | ENRICH_EXISTING | useful adapter responsibility framing | retain in this audit only |
| shared core with Dev and non-technical projections | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | CONFIRMED_EXISTING | concise product-surface expression | preserve for later design comparison |
| unrestricted shell avoidance | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | CONFIRMED_EXISTING | reinforces allowlisted profile posture | no implementation action |
| invocation supervisor and cumulative budget | `docs/audits/CVF_AGENT_CLI_MCP_INVOCATION_CONTROL_SYSTEM_CHAIN_REASSESSMENT_2026-07-20.md` | NEW_FINDING | proposal omits the critical runtime owner | continue authoritative knowledge absorption |
| MCP absolute compliance and immutable-log claims | OWNER_SURFACE_NOT_FOUND | REJECT_DIRECT_IMPORT | claims exceed protocol capability | retain rejection |
| precise dashboard cost for opaque access modes | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | NO_NEW_VALUE | contradicts known evidence-class boundaries | do not promote |

## Corpus Completeness And Report Integrity

- Corpus task class: SINGLE_EXTERNAL_MCP_CLI_PROPOSAL_EVALUATION
- Corpus root: exact operator-named proposal file under the private legacy area
- Snapshot time: 2026-07-20 at base `f127f62c6`
- Enumeration command: `rg --files --hidden --no-ignore` followed by an exact `De_xuat_xay_dung_CVF_MCP.md` filename filter
- Manifest artifact or inline manifest: one source file, 13175 bytes, SHA-256 `3e15e6c47221acbde1c437b57d91e05e0f693f47c02cf73e8182b2be543aaff2`
- Manifest hash: `3e15e6c47221acbde1c437b57d91e05e0f693f47c02cf73e8182b2be543aaff2`
- Processing ledger artifact or inline ledger: the inline selective absorption, conversion, overlap, retained, and rejected tables in this audit
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE, ADAPTED, REJECTED, NO_NEW_VALUE
- Reconciliation: manifest=1; fully_read=1; ledger_terminal=1; exclusions=0; unresolved=0
- Unresolved files: 0
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: PASS - one named source reconciles to one terminal evaluation
- Drift check: PASS - hash and byte count were recomputed before recording
- Output traceability: retained and rejected claims map to explicit tables and future boundaries
- Adversarial verification: absolute compliance, prompt-injection prevention, immutable logging, fixed token savings, sandbox sufficiency, and precise cost claims were challenged
- Corpus verdict: COMPLETE_VERIFIED

## Rescan Intelligence Hardening

- Original source artifact: `.private_reference/legacy/CVF_MCP 20.07/De_xuat_xay_dung_CVF_MCP.md`
- Predecessor intake artifact: the opening audit at material commit `8b34ec5cb`; it did not yet classify this proposal
- Delta ledger status: complete inline classification across UNCHANGED_FROM_INTAKE, CHANGED_DISPOSITION, NEW_FINDING, and REMOVED_OR_REJECTED
- Routing matrix status: complete inline routing across DO_NOW, SEPARATE_RUNTIME_TRANCHE, STRATEGIC_OPERATOR_DECISION, OUT_OF_SCOPE, and RESOLVED_BY_DESIGN
- Semantic sampling status: representative security, cost, runtime-owner, adapter, and product-surface claims challenged below
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Proposal element | Disposition |
|---|---|---|
| UNCHANGED_FROM_INTAKE | global execution moratorium and missing external-agent lifecycle owner | retained |
| CHANGED_DISPOSITION | MCP/Extension/CLI layering | narrowed from complete control chain to useful adapter separation |
| NEW_FINDING | one-core/two-surface pattern and explicit separation of observability from approval mutation | selectively retained |
| REMOVED_OR_REJECTED | absolute compliance, prompt-injection prevention, immutable audit, fixed token multiplier, and immediate MCP build | rejected or blocked from authority promotion |

### Follow-Up Routing Matrix

| Routing lane | Routed subject | Reopen condition |
|---|---|---|
| DO_NOW | record selective absorption and claim rejections | fulfilled in this audit update |
| SEPARATE_RUNTIME_TRANCHE | invocation supervisor, process-tree control, and usage enforcement | only after authoritative knowledge readiness and operator approval |
| STRATEGIC_OPERATOR_DECISION | future Dev/TUI/Web product surface priority | after runtime control architecture is accepted |
| OUT_OF_SCOPE | immediate MCP server, UI, TUI, or runtime implementation | remains prohibited by the moratorium |
| RESOLVED_BY_DESIGN | reuse one canonical state/evidence source for multiple projections | retain as a later design constraint |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| SMP-01 | layered governance introduction | MCP plus guards plus CLI forms a closed control chain | ADAPT | internal model loops and bypass capabilities occur outside the proposed chain | NARROWED |
| SMP-02 | MCP gateway layer | MCP blocks prompt injection | REJECT | schema-valid input can still contain direct or indirect injection | REJECTED |
| SMP-03 | CLI execution layer | local CLI is thirty times more token-efficient | BLOCK | no denominator, benchmark, or comparable workload is supplied | BLOCKED_EVIDENCE |
| SMP-04 | one core and two surfaces | shared state can project to Dev and non-technical users | ADAPT | approval is mutating and must not be conflated with a read-only view | ACCEPTED_WITH_BOUNDARY |
| SMP-05 | suggested roadmap | MCP Server implementation should start immediately | REJECT | runtime-owner and authoritative knowledge gaps remain unresolved | REJECTED |

### Retained ideas

| Proposal idea | CVF adaptation | Future use boundary |
|---|---|---|
| Separate MCP transport, CVF policy logic, and CLI execution | Preserve separation of protocol adapter, policy decision, and execution adapter | MCP remains one adapter; it is not the invocation supervisor |
| One governed core with developer and non-technical surfaces | Reuse one canonical control-state and evidence source for multiple projections | Each surface must preserve the same authority, freshness, and receipt semantics |
| Reuse IDE/client interaction surfaces before building another UI | Treat existing client UI as an optional delivery surface during bounded pilots | Client approval behavior is not assumed consistent or enforcement-capable across products |
| Provide a compact CLI/TUI operator experience | Retain TUI as a projection of governed state and diagnostics | TUI presentation never substitutes for runtime enforcement |
| Provide a Web control tower for non-technical operators | Separate read-only observability from authenticated approval commands | Approval is a state mutation requiring authorization, idempotency, and a durable receipt |
| Avoid unrestricted agent shell access | Prefer allowlisted, assignment-bound execution profiles | Bypass analysis must cover filesystem, IDE, browser, plugin, provider-native, and subprocess capabilities |
| Recognize MCP schema/context overhead | Minimize exposed tool schemas and load capabilities according to task need | Any token-saving claim requires measured evidence; no fixed multiplier is accepted |
| Keep MCP as transport rather than policy intelligence | Bind MCP tools to CVF-owned policy and runtime owners | Schema validation alone is not semantic governance |

### Rejected or unproven claims

| Proposal claim | Disposition | Reason |
|---|---|---|
| MCP can force absolute agent compliance | `REJECT` | Only mediated capabilities are controlled; bypass paths and internal model loops remain |
| MCP blocks prompt injection | `REJECT` | Protocol and schema validation do not provide complete content or indirect-injection protection |
| MCP automatically creates immutable audit logs | `REJECT` | Immutability requires a durable append-only evidence design, identity, integrity, and retention controls |
| Local CLI is thirty times more token-efficient | `BLOCKED_SOURCE_NOT_FOUND` | No measurement method or comparable evidence accompanies the claim |
| A sandbox alone controls delegated-agent cost | `REJECT` | Filesystem/process isolation does not bound model turns, quota, retries, fallback, or billed spend |
| Building the MCP Server core is the immediate next step | `REJECT` | Knowledge absorption, threat modeling, runtime-owner selection, and control architecture must precede implementation |
| A precise cost value can always be shown in the dashboard | `REJECT` | Subscription quota, provider usage, estimates, and billed cost are distinct and may be unavailable |

### Carried-forward knowledge need

The useful proposal patterns belong to later product and adapter design. They
do not close the current knowledge gaps in process supervision, MCP
cancellation propagation, cross-provider usage telemetry, cumulative budget
enforcement, descendant termination, bypass analysis, or unknown-usage
fail-closed behavior. Those subjects require targeted authoritative absorption
before an implementation roadmap is considered.

## Epistemic Process Block

| Field | Evidence |
|---|---|
| Expected Result | Existing CVF planes might provide at least a partial runtime chain capable of bounding an external agent CLI |
| Evidence Comparison | Direct source inspection found contract, receipt, advisory, static-command, and provider-request controls, but no owner for an external agent process and its internal multi-response loop |
| Contradiction | The broad phrase `CLI proof` is true for local governance readouts but false if interpreted as external-agent lifecycle enforcement |
| Claim Update | The CVF control claim is narrowed to artifact governance and bounded provider-request controls; external-agent CLI control is not effective |
| Confidence | HIGH for the inspected canonical surfaces; audit remains open for exhaustive caller enumeration |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | read and selectively classify one external MCP/CLI architecture proposal |
| claimDisposition | CLAIM_REJECTED: no runtime execution-control claim is accepted from the proposal |
| receiptEvidence | CVF_RECEIPT_PRESENT: local file identity, hash, byte count, classification, and governance-gate evidence only |
| actionEvidence | ACTION_EVIDENCE_PRESENT: complete local file read, direct source comparison, and governed documentation update |
| invocationBoundary | zero agent CLI, MCP live tool, provider, API-key, account-subscription, retry, fallback, or live-proof invocation |
| interceptionBoundary | no shell, IDE, MCP host, provider, process, filesystem, or network interception claim |
| claimLanguage | external design hypotheses selectively retained for future authoritative knowledge work |
| forbiddenExpansion | implementation readiness, runtime effectiveness, immutable logging, prompt-injection prevention, fixed token savings, cost precision, public readiness, and moratorium lift |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/orchestrator |
| Provider or surface | Local private provenance repository only |
| Session or invocation | agent-cli-mcp-external-proposal-selective-absorption-2026-07-20 |
| Working directory | repository root |
| Command or tool surface | read-only PowerShell, rg, git inspection, and apply_patch |
| Target paths | this audit and its GC-051 source/aggregate registration pair |
| Allowed scope source | operator instruction to retain useful proposal ideas for later use without treating the proposal as sufficient fix authority |
| Before status evidence | external proposal inspected but not recorded in the governed audit |
| After status evidence | useful ideas selectively retained; unsupported claims rejected or blocked; moratorium unchanged |
| Diff evidence | exact three-path material batch shown by staged name-status evidence |
| Approval boundary | knowledge recording only; no implementation, work order, agent call, provider call, or public action |
| Claim boundary | selective external-input absorption; no runtime effectiveness or implementation-readiness proof |
| Agent type | reviewer/orchestrator |
| Invocation ID | agent-cli-mcp-external-proposal-selective-absorption-2026-07-20 |
| Expected manifest | this audit; GC-051 source entry; generated GC-051 aggregate |
| Actual changed set | this audit; GC-051 source entry; generated GC-051 aggregate |
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
