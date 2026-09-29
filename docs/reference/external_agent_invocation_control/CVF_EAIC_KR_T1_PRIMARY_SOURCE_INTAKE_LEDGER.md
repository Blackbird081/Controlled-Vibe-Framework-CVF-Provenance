# CVF EAIC-KR T1 Primary Source Intake Ledger

Status: ACTIVE_REFERENCE

Memory class: FULL_RECORD

docType: reference

Date: 2026-07-22

Batch ID: CVF-EAIC-KR-T1

executionBaseHead: `d000aa35b`

External absorption core: REQUIRED

Source intake decision packet: REQUIRED

## Purpose

Retrieve and reconcile operator-approved official public sources for the four
CRITICAL external-agent invocation-control knowledge gaps identified by
CVF-EAIC-KR-T0: launch admission, process identity, cumulative budget, and
unknown usage. Produce a source-backed evidence ledger that separates
host-specific, protocol, runtime, OS, API-key, and opaque-subscription
semantics and recommends either a T2 decision packet or continued parking.

## Scope / Applies-To

Applies to public pages retrieved 2026-07-22 from the six operator-approved
official root families in
`docs/baselines/CVF_GC018_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_2026-07-22.md`.
Retrieval used the parent session's internal WebFetch/WebSearch surfaces only
(no agent CLI, MCP tool, provider API, authenticated account, or separate
external session). Third-party blogs, GitHub issue trackers, forum posts, and
generated-answer aggregations that appeared in search results were not used
as accepted evidence; they are recorded in the Query Ledger only where a
search result surfaced them, with a `REJECTED_NON_PRIMARY` disposition.

Does not apply to architecture ratification, fail-closed policy ratification,
implementation, or T2 release; those remain gated behind a later
operator-authorized decision packet.

## Target / Source

Target: `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md`
(this file) plus the paired worker return.

Source: the six allowlisted official root families named in the paired
GC-018 baseline, cross-referenced against the T0 knowledge gap and source
acquisition map's Authority Ledger and Knowledge Gap And Source Acquisition
Map tables.

## Redirect Disposition Record

Two of the six approved root families redirected to a different literal
hostname during retrieval. Both redirects were confirmed, during this
worker's execution, by the operator as remaining inside the same
organization-owned root family for the purpose of this intake:

| Original approved root | Redirect target | Redirect type | Operator disposition |
| --- | --- | --- | --- |
| `https://docs.anthropic.com/` | `https://platform.claude.com/docs/` | HTTP 301 | CONFIRMED_SAME_ORGANIZATION_ROOT_FAMILY; provider-specific public documentation |
| `https://support.anthropic.com/` | `https://support.claude.com/` | HTTP 301 | CONFIRMED_SAME_ORGANIZATION_ROOT_FAMILY; provider-specific public documentation |
| `https://developers.openai.com/codex/` | `https://learn.chatgpt.com/docs` | HTTP 308 | CONFIRMED_SAME_ORGANIZATION_ROOT_FAMILY |

A fourth domain, `https://code.claude.com/`, was surfaced only through a
public search result (not a direct redirect from an approved root) and was
also confirmed by the operator during execution as an in-scope Anthropic/
Claude-owned documentation host for this intake, since it hosts the most
directly relevant Claude Code session-management documentation. This
confirmation is recorded here as evidence of an in-session scope decision,
not as a new standing approval for future tranches; a later tranche citing
`code.claude.com` or `learn.chatgpt.com` again should re-confirm with the
operator or cite this record.

`https://help.openai.com/` returned HTTP 403 Forbidden on direct root fetch;
individual article pages under the same host were reachable and used where
found (see Query Ledger).

## Source Manifest

| Source ID | Exact URL | Publisher | Title | Version/date shown | Retrieved-at | `sourceAuthorityClass` | `accessModeClass` | `sourceVolatility` | Terminal status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | `https://modelcontextprotocol.io/specification/` | Model Context Protocol / Anthropic-stewarded open spec | Specification | schema `2025-11-25` | 2026-07-22 | PRIMARY_OFFICIAL | PROTOCOL | STABLE_SPEC | READ |
| S2 | `https://modelcontextprotocol.io/specification/2025-11-25/basic` | Model Context Protocol | Overview (Base Protocol) | `2025-11-25` | 2026-07-22 | PRIMARY_OFFICIAL | PROTOCOL | STABLE_SPEC | ADAPTED |
| S3 | `https://platform.claude.com/docs/` (redirect target of `docs.anthropic.com`) | Anthropic; provider-specific public documentation | Claude Platform Docs index | not dated on page | 2026-07-22 | PRIMARY_OFFICIAL | ACCOUNT_SUBSCRIPTION / API_KEY (mixed index) | CURRENT_PRODUCT_DOC | READ |
| S4 | `https://support.claude.com/en/collections/14445694-claude-code` (redirect target of `support.anthropic.com`) | Anthropic; provider-specific public documentation | Claude Code collection index | not dated on page | 2026-07-22 | PRIMARY_OFFICIAL | ACCOUNT_SUBSCRIPTION | CURRENT_SUPPORT_DOC | READ |
| S5 | `https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code` | Anthropic; provider-specific public documentation | Models, usage, and limits in Claude Code | 2026-04-15 | 2026-07-22 | PRIMARY_OFFICIAL | ACCOUNT_SUBSCRIPTION / API_KEY (both described) | CURRENT_SUPPORT_DOC | ADAPTED |
| S6 | `https://code.claude.com/docs/en/sessions` | Anthropic; provider-specific public documentation | Manage sessions | not dated on page (references CLI versions from 2.1.169 through 2.1.216) | 2026-07-22 | PRIMARY_OFFICIAL | LOCAL_PROCESS | CURRENT_PRODUCT_DOC | ADAPTED |
| S7 | `https://code.claude.com/docs/en/agent-sdk/hosting` | Anthropic; provider-specific public documentation | Hosting the Agent SDK | not dated on page | 2026-07-22, reviewer refreshed 2026-07-23 | SUPPORTING_OFFICIAL | LOCAL_PROCESS | CURRENT_PRODUCT_DOC | ADAPTED |
| S8 | `https://learn.microsoft.com/windows/win32/procthread/job-objects` | Microsoft | Job Objects - Win32 apps | page `ms.date: 2025-07-14` | 2026-07-22 | PRIMARY_OFFICIAL | OS_RUNTIME | STABLE_SPEC | ADAPTED |
| S9 | `https://nodejs.org/docs/latest/api/child_process.html` | OpenJS Foundation / Node.js | Child process | Node.js v26.5.0 (latest at retrieval) | 2026-07-22 | PRIMARY_OFFICIAL | OS_RUNTIME | VERSIONED_DOC | ADAPTED |
| S10 | `https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap11.html` | The Open Group | 11. General Terminal Interface | Issue 7, 2018 edition (IEEE Std 1003.1-2017) | 2026-07-22 | PRIMARY_OFFICIAL | PROTOCOL | STABLE_SPEC | READ |
| S11 | `https://pubs.opengroup.org/onlinepubs/007904875/functions/setpgid.html` | The Open Group | setpgid | IEEE Std 1003.1, 2004 Edition | 2026-07-22 | PRIMARY_OFFICIAL | PROTOCOL | STABLE_SPEC | ADAPTED |
| S12 | `https://learn.chatgpt.com/docs` (redirect target of `developers.openai.com/codex/`) | OpenAI | OpenAI Developers documentation portal | not dated on page | 2026-07-22 | PRIMARY_OFFICIAL | ACCOUNT_SUBSCRIPTION / API_KEY (mixed index) | CURRENT_PRODUCT_DOC | READ |
| S13 | `https://learn.chatgpt.com/docs/codex/cli` | OpenAI | Codex CLI \| ChatGPT Learn | version `0.143.0` referenced in one example | worker retrieval 2026-07-22, reviewer refreshed 2026-07-23 | PRIMARY_OFFICIAL | ACCOUNT_SUBSCRIPTION | CURRENT_PRODUCT_DOC | ADAPTED |
| S14 | `https://learn.chatgpt.com/docs/developer-commands?surface=cli` | OpenAI | Developer commands \| ChatGPT Learn | not dated on page | reviewer retrieval 2026-07-23 | PRIMARY_OFFICIAL | ACCOUNT_SUBSCRIPTION | CURRENT_PRODUCT_DOC | ADAPTED |
| S15 | `https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan` | OpenAI | Using Codex with your ChatGPT plan | page showed Updated 5 days ago at review | worker attempt 2026-07-22 blocked; reviewer retrieval 2026-07-23 | PRIMARY_OFFICIAL | ACCOUNT_SUBSCRIPTION | CURRENT_SUPPORT_DOC | ADAPTED |

## Query Ledger

| Query/domain | Approved root | Exact query or navigation route | Result URL or no-result disposition |
| --- | --- | --- | --- |
| launch admission / process identity (Claude host) | `docs.anthropic.com` | direct fetch of root, redirect followed | S3 (`platform.claude.com/docs/`), provider-specific public documentation |
| cumulative budget / unknown usage (Claude host) | `support.anthropic.com` | direct fetch of root, redirect followed, then Claude Code collection page | S4, then S5 |
| process identity (Claude host session model) | `code.claude.com` (operator-confirmed in-session extension) | WebSearch `code.claude.com docs Claude Code process management subprocess` | S6, S7; provider-specific public documentation |
| MCP lifecycle/cancellation/identity | `modelcontextprotocol.io` | direct fetch of specification root, then base protocol page | S1, S2 |
| Windows process-tree termination | `learn.microsoft.com` | direct fetch of the exact allowlisted URL | S8 |
| Node.js child-process identity/termination | `nodejs.org` | direct fetch of the exact allowlisted URL | S9 |
| POSIX process groups/sessions | `pubs.opengroup.org` | WebSearch `site:pubs.opengroup.org process groups sessions signals POSIX`, then direct fetch of the terminal-interface chapter | S10 |
| POSIX `setpgid` process-group membership | `pubs.opengroup.org` | WebSearch `site:pubs.opengroup.org setsid process group session leader`, then direct fetch of `setpgid` page | S11 |
| launch admission / process identity (Codex host) | `developers.openai.com/codex/` | direct fetch of root, redirect followed | S12 |
| Codex CLI session/process model | `learn.chatgpt.com` (redirect target) | worker direct fetch followed by reviewer refresh of the current CLI and developer-command pages | S13 documents saved-chat resume; S14 documents session configuration, chat ID, and usage commands; neither documents OS descendant-process binding |
| cumulative budget / unknown usage (Codex host) | `help.openai.com` | worker direct fetch returned 403; reviewer reopened the exact allowlisted article URL on 2026-07-23 | S15 ADAPTED: plan usage pool, usage page/limit banner, credits or reset options; no programmatic hard-ceiling owner is documented |
| Codex CLI descendant-process kill semantics | `learn.chatgpt.com`, `help.openai.com` | both routes above | NO_RESULT: no page reachable within the allowlist documented this |

Third-party pages that appeared in search results but were not used as
accepted evidence (recorded for negative-search completeness only):
`github.com/anthropics/claude-code/issues/*` (multiple), `mcpmarket.com`,
`claudelog.com`, `en.wikipedia.org/wiki/Process_group`, `dev.to`,
`blakecrosley.com`, `cometapi.com`. Disposition for all: `REJECTED_NON_PRIMARY`.

## Per-Source Processing Ledger

| Source ID | Supported claim | Prohibited inference | T0 overlap | Disposition | Owner surface |
| --- | --- | --- | --- | --- | --- |
| S1, S2 | MCP defines JSON-RPC request/response/notification framing, lifecycle management, and a cancellation utility as protocol-level concepts; request IDs must be unique per session | Do not read this as proof CVF's own MCP invocation contract implements cancellation; it does not | ENRICH_EXISTING against T0's `MCP invocation contract` and `MCP consumer pipeline` rows | ADAPT | T0 `EAIC-KR` reference family; no CVF runtime owner selected |
| S3 | Claude Platform Docs links both the `ant` API CLI documentation and Claude Code/Agent SDK documentation | Do not conflate the `ant` API CLI with the Claude Code CLI; they are different products under the same publisher | NEW_FINDING: T0 did not previously distinguish these two CLIs | ADAPT | T1 ledger only; no CVF owner exists for this distinction yet |
| S4 | A "Claude Code" support collection with 20 articles exists, including one on usage/limits | none beyond index existence | ENRICH_EXISTING against T0 `usage telemetry` row | ADAPT | T1 ledger |
| S5 | Enterprise-seat Claude Code usage is a pooled quota on a rolling-window reset with a "limit reached, resets at _time_" message; API-key usage is pay-as-you-go per-token with no hard cap; `/cost` shows running session spend for API-key users; a live context-window indicator exists separately from account usage | Do not infer that a numeric percentage or token count is exposed for account-subscription (non-Enterprise) usage; the source does not describe Pro/Max plan visibility explicitly, only Enterprise and API-key | Directly narrows T0 `usage telemetry` row (`OPAQUE_BY_ACCESS_MODE`) and `unknown usage` row (`MISSING_PRIMARY_SOURCE`) | ADAPT | T1 ledger; later T2 fail-closed policy owner remains undecided |
| S6 | A Claude Code session is identified by a session ID; sessions are stored as local JSONL transcripts at a documented path; `--resume <session-id>` and `/branch`/`--fork-session` create distinct session IDs; background subagents and background Bash commands are named concepts with documented resume behavior | Do not infer that session ID alone constitutes a security-relevant process identity binding, or that resuming a session resumes descendant OS processes; the page describes conversation/transcript identity, not OS process-tree identity | Directly narrows T0 `process identity` row (`MISSING_PRIMARY_SOURCE`); still does not resolve OS-level process-tree binding | ADAPT | T1 ledger |
| S7 | The Agent SDK spawns and supervises one `claude` CLI subprocess per session; N concurrent sessions mean N subprocesses, each with its own process tree and transcript | Do not infer this describes every interactive Claude Code launch; do not infer a documented admission, kill, or cancel API from this page | ENRICH_EXISTING against T0's `process identity` row: the host-specific session-to-process relation is documented, but no CVF receipt binding exists | ADAPT | T1 ledger; RUNTIME_CANDIDATE flagged in Value Conversion Matrix, no implementation |
| S8 | A Windows Job Object groups processes so `TerminateJobObject` terminates all associated processes as a unit; child processes are associated with a job by default unless a breakaway limit is set; a process can escape (\"break away\") from job-based monitoring under documented conditions | Do not infer that Job Objects are already used by any CVF-governed launcher; T0 confirmed `governed-command-launcher.ts` uses only `child.kill()` with `detached: false`, not Job Objects | ENRICH_EXISTING against T0 `cancellation and termination` row (`PARTIAL`); identifies a concrete Windows-native mechanism CVF does not currently use | ADAPT | T1 ledger; RUNTIME_CANDIDATE flagged, no implementation |
| S9 | On Linux/POSIX, "child processes of child processes will not be terminated when attempting to kill their parent"; `options.detached` plus `unref()` lets a child outlive the parent on both Windows and POSIX, with different underlying mechanisms (new process group on POSIX) | Do not infer this documents Windows Job Object equivalent behavior; Node's own `child_process` docs explicitly describe a documented gap for descendant termination, not a solved problem | Directly confirms and sharpens T0's `cancellation and termination` `PARTIAL` disposition with an authoritative, explicit descendant-non-termination caveat | ADAPT | T1 ledger |
| S10, S11 | A process group permits signaling of related processes; `setpgid()` lets a process join or create a process group within its session; a session leader cannot change its own group; signals to a process group are described in the terminal-interface chapter in the context of foreground/background job control | Do not infer POSIX process groups are already used by any CVF launcher; do not infer this proves descendant-tree kill is automatic in POSIX shells generally (Node's own docs (S9) explicitly caveat this) | ENRICH_EXISTING against T0 `cancellation and termination` row; provides the portable (non-Windows) counterpart primitive to S8 | ADAPT | T1 ledger |
| S12 | The OpenAI Developers portal groups Codex CLI documentation under a "Codex" section with CLI, reference, and administration subsections | none beyond index existence | ENRICH_EXISTING (parallel structure to S3 for the Codex host) | ADAPT | T1 ledger |
| S13, S14 | Codex CLI supports reopening saved chats; current developer commands expose session configuration, chat ID, token usage, and daily, weekly, or cumulative account-usage views when service-account authentication is present | Do not infer that chat ID is an OS process-tree identity or that displayed usage is a CVF-enforced cumulative ceiling | ENRICH_EXISTING against T0 process-identity, usage-telemetry, and cumulative-budget rows | ADAPT | T1 ledger; no CVF binding or enforcement owner selected |
| S15 | Codex tasks draw from a plan-dependent agentic usage and credit pool; the usage page or limit banner exposes available options such as credits, reset, upgrade, or waiting | Do not infer a stable numeric plan allowance, programmatic telemetry API, or caller-enforced hard ceiling; availability varies by plan and task consumption varies by model, task size, and execution surface | ENRICH_EXISTING against T0 cumulative-budget and unknown-usage rows | ADAPT | T1 ledger; fail-closed policy and CVF envelope owner remain undecided |

## Domain Readiness Matrix

Four CRITICAL T0 domains, each resolved to exactly one `domainReadinessDisposition`.

| T0 domain | Source IDs | Remaining gap | `domainReadinessDisposition` | Operator policy need | Blocked next decision |
| --- | --- | --- | --- | --- | --- |
| Launch admission | S1, S2, S7, S12, S13, S14 | MCP lifecycle and host session/process descriptions exist, but no source names a CVF-equivalent pre-launch admission owner that approves or denies an external-agent launch | `PARTIAL_REMAINS` | operator must decide the required admission policy and later architecture owner | T3 owner-architecture selection for admission remains blocked pending T2 policy and a future owner decision |
| Process identity | S6, S7, S8, S9, S10, S11, S13, S14 | Claude and Codex conversation/session identifiers, the Agent SDK session-to-subprocess relation, Windows Job Objects, and POSIX process groups are documented; no source binds a CVF task assignment and receipt to both conversation and OS process-tree identity | `PARTIAL_REMAINS` | operator must approve which identity layers a future CVF binding must reconcile | T2 identity reconciliation fields cannot be ratified from evidence alone; a design choice is required |
| Cumulative budget | S5, S14, S15 | Both hosts expose usage concepts, but neither source defines a CVF-owned hard envelope that aggregates retry, resume, fallback, and internal-agent consumption across access modes | `PARTIAL_REMAINS` | operator must decide the provider-neutral envelope semantics and how display-only subscription usage constrains admission | T2 budget-ceiling fields remain a policy and ownership decision rather than a source fact |
| Unknown usage | S5, S14, S15 | Both hosts expose some interactive usage state, but availability depends on plan/authentication and no source guarantees a machine-readable value before every launch | `OPAQUE_REQUIRES_OPERATOR_POLICY` | operator must ratify the fail-closed default when reliable pre-launch usage is unavailable | T2 fail-closed disposition cannot be ratified by this ledger; it requires an explicit operator policy decision |

### Domain terminal-state summary

`READY_FOR_T2_DECISION`: 0. `PARTIAL_REMAINS`: 3 (launch admission; process identity; cumulative budget). `OPAQUE_REQUIRES_OPERATOR_POLICY`: 1 (unknown usage). `BLOCKED_MISSING_PRIMARY_SOURCE`: 0.

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | six operator-approved official public documentation root families named in `docs/baselines/CVF_GC018_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_2026-07-22.md`, plus two operator-confirmed same-organization redirect targets and one operator-confirmed provider-specific public documentation extension (`code.claude.com`) |
| Enumeration command | WebFetch/WebSearch retrieval log recorded inline in the Query Ledger above; no filesystem clone |
| Manifest artifact or inline manifest | inline Source Manifest table above (15 source rows) |
| Processing ledger artifact or inline ledger | inline Per-Source Processing Ledger table above |
| Ledger terminal statuses | READ, ADAPTED; no source remains DEFERRED, REJECTED, NO_NEW_VALUE, or BLOCKED_UNREADABLE after reviewer refresh |
| Disposition taxonomy | ADAPT for every semantic source row; READ for index-only rows |
| Owner-surface map | `docs/reference/external_agent_invocation_control/` family; no new implementation owner selected |
| Unresolved items | no source names a pre-launch CVF admission owner, binds task/receipt identity to an OS process tree, or defines a provider-neutral cumulative envelope; unknown-usage fail-closed behavior remains an operator policy decision |
| Completion claim boundary | bounded public-source evidence only; no runtime, provider, public, or production expansion |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| MCP lifecycle/cancellation/request-ID semantics (S1, S2) | protocol-level cancellation utility and per-session unique request ID requirement | DOCTRINE_ADAPTED | T1 ledger; future T2 identity-reconciliation design | reviewer decides whether MCP request-ID uniqueness informs a future CVF invocation-identity field | no adapter or protocol-conformance implementation |
| Claude Code session ID and transcript model (S6) | conversation/session identity is distinct from OS process identity; documented resume/fork/branch semantics | RUNTIME_CANDIDATE | future T2/T3 process-identity design | reviewer decides whether to route this to a future architecture decision packet | no implementation; no binding of this identity model into CVF source |
| Agent SDK session/subprocess model (S7) | one Agent SDK session maps to one subprocess with its own process tree and transcript | RUNTIME_CANDIDATE | future T2/T3 identity-reconciliation design | reviewer records this as a host-specific identity primitive, not launch admission | no implementation |
| Windows Job Objects (S8) | a native OS mechanism exists for whole-process-tree termination with an explicit escape/breakaway mechanism to guard against | RUNTIME_CANDIDATE | future T3 owner-architecture selection for cancellation/termination | reviewer decides whether Job Objects should be evaluated against the existing `governed-command-launcher.ts` child-only-kill gap T0 identified | no implementation; CVF's current launcher does not use Job Objects |
| Node child_process descendant-termination gap (S9) | authoritative confirmation that killing a direct child does not terminate grandchildren on POSIX by default | DOCTRINE_ADAPTED | T1 ledger; sharpens T0's existing `PARTIAL` cancellation/termination finding | no new action; this confirms rather than changes T0's prior disposition | no implementation |
| POSIX process groups and `setpgid` (S10, S11) | portable process-group primitive as the POSIX counterpart to Windows Job Objects | RUNTIME_CANDIDATE | future T3 owner-architecture selection for cancellation/termination | reviewer decides whether a portable process-group-based design should be compared against the Windows Job Object approach in a later architecture packet | no implementation |
| Claude host usage-metering distinction: Enterprise pooled quota vs. API-key pay-as-you-go (S5) | two genuinely distinct, non-interchangeable usage-tracking models exist even within one host | DOCTRINE_ADAPTED | T1 ledger; sharpens T0's `usage telemetry` and `unknown usage` findings | operator decision needed on fail-closed policy for the still-unmeasured Pro/Max case; not resolved by this ledger | no implementation |
| Codex session and usage surfaces (S13-S15) | saved-chat resume, session/chat status, account usage views, and plan-dependent usage/credit behavior are documented | DOCTRINE_ADAPTED | T1 ledger process-identity, cumulative-budget, and unknown-usage rows | preserve the distinction between observability and CVF enforcement ownership | no implementation |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| MCP lifecycle/cancellation/request-ID (S1, S2) | T0 `MCP invocation contract` and `MCP consumer pipeline` rows (`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/`) | ENRICH_EXISTING | protocol-level cancellation exists as a concept CVF's current contract does not yet implement | adapt evidence; do not select an owner; T0's `MISSING_PRIMARY_SOURCE`/`MISSING_OWNER` findings for launch admission and in-flight stop remain unresolved by protocol existence alone |
| Claude Code session/transcript identity and Agent SDK subprocess model (S6, S7) | T0 `process identity` row (`MISSING_PRIMARY_SOURCE`); no existing CVF process-identity binding owner | NEW_FINDING | host-specific session ID plus a documented one-session-to-one-subprocess/process-tree relation are concrete primitives not previously documented in a CVF-governed source | route to a future T2/T3 architecture decision packet; these source identifiers still lack a CVF task/receipt binding |
| Windows Job Objects and POSIX process groups (S8, S9, S10, S11) | T0 `governed command launcher` row (`EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts`), confirmed to use only `child.kill()` with `detached: false` | ENRICH_EXISTING | both a Windows-native and a POSIX-native whole-process-tree mechanism exist and are not currently used by the governed command launcher | adapt evidence; T0's `PROCESS_TREE_CONTROL_NOT_PROVEN` disposition is now paired with two concrete, named native mechanisms a future design could evaluate |
| Claude host usage-metering classes (S5) | T0 `usage telemetry` row (`OPAQUE_BY_ACCESS_MODE`) and `unknown usage` row (`MISSING_PRIMARY_SOURCE`) | ENRICH_EXISTING | Enterprise pooled-quota and API-key pay-as-you-go are now confirmed as officially documented, distinct classes; Pro/Max-tier visibility remains undocumented at the allowlisted sources | preserve opacity for the undocumented tier; operator-policy need remains as T0 already recorded |
| Codex host equivalents for all four CRITICAL domains | T0 knowledge map (all four rows currently `MISSING_PRIMARY_SOURCE` or `CRITICAL`) | ENRICH_EXISTING | current official pages expose session/chat identity and interactive usage state, but still no pre-launch admission owner, OS process-tree binding, or CVF-owned aggregate ceiling | retain the evidence for later policy design; do not convert interactive display or plan behavior into a provider-neutral enforcement guarantee |

## Contradiction / Gap Ledger

No two accepted sources directly contradicted each other. One apparent
tension was found and resolved without merging semantics: S5 (Claude host)
describes two distinct metering models (pooled Enterprise quota vs.
per-token API-key billing) that might look like they describe the same
"usage limit" concept but are explicitly documented as non-interchangeable;
this is recorded as two separate `accessModeClass` rows in the Source
Manifest rather than being averaged or generalized into one CVF-wide usage
model.

The most significant gap is control ownership rather than source absence.
Both host families now provide session and usage evidence, but neither source
family binds that evidence to a CVF assignment/receipt or names a
provider-neutral admission and aggregate-budget owner.

## Findings / Position

Position: `PARKED_KNOWLEDGE_GAP`.

Primary-source retrieval substantially enriched three of the four CRITICAL
T0 domains (launch admission, process identity, cumulative budget) from
`MISSING_PRIMARY_SOURCE` toward `PARTIAL_REMAINS`, and confirmed the fourth
(unknown usage) as `OPAQUE_REQUIRES_OPERATOR_POLICY` with sharper evidence
than T0 had. No domain reached `READY_FOR_T2_DECISION`. The binding
constraint is no longer broad primary-source absence. No accepted source
binds the documented identity, usage, or termination primitives to a
CVF-owned admission, receipt, and cumulative-budget control surface.

## Decision / Disposition

`PARKED_KNOWLEDGE_GAP`

No CRITICAL domain reached `READY_FOR_T2_DECISION`. A T2 decision packet is
not recommended at this time. The R84-style overall recommendation token
required by the work order is `PARKED_KNOWLEDGE_GAP`, not
`READY_FOR_T2_DECISION_PACKET`.

## Risk / Corrective Action

No corrective action is authorized or performed. No architecture,
fail-closed policy, or implementation decision is made by this ledger.

One process observation, not a corrective action: two allowlisted roots
required an in-session operator confirmation to follow a same-organization
redirect, and one additional domain (`code.claude.com`) required an
in-session operator confirmation to use at all. If a future T1-style
tranche is authorized, the paired GC-018/work order could reduce this
friction by naming the confirmed redirect targets and `code.claude.com`
directly in the allowlist rather than requiring a fresh in-session
confirmation each time; this ledger does not make that change itself.

## Epistemic Process Block

### Expected Result / Prediction

The paired GC-018 baseline predicted that official process and protocol
documents would clarify primitives, while agent-host subscription telemetry
and cumulative budget ownership might remain incomplete or opaque.

### Evidence Comparison

Protocol (MCP) and OS/runtime (Windows Job Objects, Node child_process,
POSIX process groups) primitives were confirmed and are now documented with
specific, citable mechanisms, matching the prediction's more optimistic
half. Subscription/usage evidence was partially clarified for both host
families, including plan-dependent usage views and account-level usage
commands. It still does not guarantee machine-readable pre-launch telemetry
or a provider-neutral cumulative enforcement owner.

### Contradiction Or Gap Disposition

No contradiction was found between sources. The main gap is the unresolved
binding and ownership boundary: host-specific session and usage surfaces do
not establish CVF task/receipt identity, launch admission, or cumulative
budget enforcement. The gap remains open rather than smoothed into a PASS.

### Claim Update

Each of the four CRITICAL domains is reclassified with a
`domainReadinessDisposition`: three `PARTIAL_REMAINS` (launch admission,
process identity, cumulative budget) and one `OPAQUE_REQUIRES_OPERATOR_POLICY`
(unknown usage). None reaches `READY_FOR_T2_DECISION`. The overall T1
recommendation is `PARKED_KNOWLEDGE_GAP`, not a T2 release.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Lane | Disposition | Rationale / next owner |
| --- | --- | --- | --- | --- |
| Two allowlisted roots (`docs.anthropic.com`, `support.anthropic.com`) and one implicit root (`developers.openai.com/codex/`) all redirect to a different literal hostname than the one named in the baseline allowlist | OPERATOR_SCOPE_CLARITY_GAP | DOCUMENTATION_ONLY_LEARNING | MACHINE_CHECK_CANDIDATE | future source-intake baselines that name a root family should consider naming both the historical and current hostname, or explicitly pre-authorizing same-organization redirects, so a worker does not need an in-session confirmation each time |
| A relevant, more specific provider-specific public documentation host (`code.claude.com`) existed outside the originally named allowlist but was discoverable only through public search, not through any named root | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | a future source-intake baseline template could ask the dispatcher to verify each named root is still the canonical current documentation host before dispatch, not only at worker execution time |

No ADIF entry is promoted from this single-instance observation; if this
redirect/rename pattern recurs across a second independent source-intake
tranche, it should be promoted per
`docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | official source retrieval -> authority classification -> T0 overlap comparison -> four-domain readiness ledger -> independent review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/external_agent_invocation_control/` family |
| Disposition | ADAPT primary-source knowledge; reject direct implementation import |
| Claim boundary | accepted sources inform a later decision packet but do not authorize architecture or runtime |

## Source Intake Decision Packet

| Field | Value |
| --- | --- |
| Decision packet standard | `docs/reference/external_agent_review/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_STANDARD.md` |
| Input root or repository | six official public root families listed in the paired baseline, plus two operator-confirmed same-organization redirect targets and one operator-confirmed provider-specific public documentation extension (`code.claude.com`) |
| Bounded scope | four CRITICAL T0 domains only: launch admission, process identity, cumulative budget, unknown usage |
| Enumeration authority | worker recorded every retrieved official page in the Source Manifest above |
| Owner-surface taxonomy | existing `docs/reference/external_agent_invocation_control/` reference family; new implementation owner is forbidden in this tranche |
| Pre-scan packet source | T0 knowledge gap and source acquisition map |
| Overlap routing matrix | see Overlap And Novelty Classification above; three `ENRICH_EXISTING`, one `NEW_FINDING`, one `OWNER_SURFACE_NOT_FOUND` |
| Negative-search evidence | worker retrieval misses are preserved in the Query Ledger; reviewer refresh found S13-S15, then confirmed that these pages still do not name a CVF binding or enforcement owner |
| Core disposition | ADAPT official-source evidence into the bounded T1 ledger |
| Value conversion requirement | see External Absorption Value Conversion Matrix above; five `RUNTIME_CANDIDATE`, three `DOCTRINE_ADAPTED`, one `NO_PACKAGE_OR_RUNTIME_VALUE` |
| Overlap classification requirement | see Overlap And Novelty Classification above |
| Worker output path | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md` |
| Forbidden scope | login, paid access, agent/provider execution, source import, runtime/checker build, policy ratification, or public release |
| Claim boundary | knowledge intake and readiness recommendation only |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated no-commit primary-source intake worker |
| Provider or surface | local private provenance repository plus the parent session's internal WebFetch/WebSearch surfaces; no external agent, CLI, MCP, or authenticated account |
| Session or invocation | CVF-EAIC-KR-T1 worker execution, 2026-07-22 |
| Working directory | repository root |
| Command or tool surface | local read-only file reads, `rg`/Grep, Git status/rev-parse, Python governance gates, and the parent session's internal WebFetch/WebSearch tools limited to the operator-approved (and in-session operator-confirmed) root families |
| Target paths | this ledger and the paired worker return |
| Allowed scope source | canonical work order Scope and Required Artifact Manifest; paired GC-018 baseline Operator-Approved Source Classes And Roots |
| Before status evidence | HEAD `d000aa35b`; `git status --short --untracked-files=all` empty; both Allowed output paths absent; pre-implementation autorun gate passed 0 failures |
| After status evidence | exactly two untracked files created; no existing path modified; HEAD unchanged at `d000aa35b` |
| Diff evidence | `git status --short --untracked-files=all` and `git diff --name-status`, recorded in the paired worker return |
| Approval boundary | worker execution for bounded public-source intake; no commit, push, agent CLI/MCP invocation, provider API call, authenticated account access, or implementation |
| Claim boundary | source-backed evidence intake and readiness classification only; no architecture, runtime, or fail-closed policy ratification |
| Agent type | worker |
| Invocation ID | `cvf-eaic-kr-t1-worker-execution-2026-07-22` |
| Expected manifest | this ledger; the paired worker return |
| Actual changed set | this ledger; the paired worker return |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred |

## Claim Boundary

This ledger authorizes no agent CLI/MCP invocation, provider/model
execution, API request, authenticated account access, secret, paid query,
executable test, source-repository clone, package install, download,
runtime/source/test/checker/hook/standard/roadmap/registry/session/handoff
mutation, public-sync, architecture ratification, fail-closed policy
ratification, implementation recommendation framed as authorization, or
moratorium lift. It is a bounded, source-backed public-documentation
evidence ledger only, current as of `executionBaseHead` `d000aa35b` and
retrieval timestamp 2026-07-22. `READY_FOR_T2_DECISION_PACKET` is not
claimed; the overall recommendation is `PARKED_KNOWLEDGE_GAP`.
