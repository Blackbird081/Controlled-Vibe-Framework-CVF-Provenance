# CVF Active Continuity Read Cost T2B Source Binding Matrix

Memory class: governed-source-map

Status: SOURCE_MAP_ACCEPTED_FOR_DISPATCH

Date: 2026-08-11

Batch ID: ACRC-T2B

Source base head: `178c5e7e169c936e285f484de5abd8dae2e06c07`

## Purpose

Map every current root instruction heading and every machine reader of
`AGENTS.md` or `CLAUDE.md` before T2B rewrites any carrier. This is a bounded
source review, not implementation authorization.

## Scope

The reviewed carriers are root `AGENTS.md`, provider-local `CLAUDE.md`, and
`governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`. Existing
downstream repositories, public-sync clones, runtime/provider behavior, and
session history are outside this map.

## Current Source Facts

| Carrier | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `AGENTS.md` | 1119 | 53604 | `24395f0fbab0e68ca416f500ab76118e01d368d506016c58c0a2ec1e31daf73a` |
| `CLAUDE.md` (`NOT_CVF_SOURCE`) | 465 | 24398 | `5d918333045b248beb1d3acbe9fb984da45298cf5348abe0a107593ee0c8c7c1` |
| downstream template | 262 | 12374 | `7f545fa243754cd3066f3b4264959f4b7f9bd3fa2f348bd1b99cc21483e34a74` |

## Guard Behavior Discussion

Discussion-only disposition: META_DISCUSSION_ONLY

### AGENTS Heading Binding Matrix

Every current level-two heading is accounted for below. `ROUTE` means the
compact carrier may point to the canonical owner. `RETAIN_LITERAL` means a
machine reader requires the named marker directly in `AGENTS.md`. The new
routing index must retain a concise binding summary for every row.

| Current heading | Canonical owner or retained literal | Disposition |
|---|---|---|
| Session Memory Front Door | active-continuity standard, bootstrap, front door, active-state checker | ROUTE_AND_RETAIN_LITERAL |
| Mandatory Startup Acknowledgment | front door plus `AGENTS.md` startup contract | ROUTE_AND_RETAIN_LITERAL |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ROUTE |
| Mandatory Provider-Specific Agent Memory Boundary | compact routing index plus packet-authority checker | ROUTE |
| Mandatory F-1 Diminishing Returns Stop Rule | canonical F-1 stop/closure/value/roadmap packet | ROUTE |
| Mandatory Public Export Disposition Guard | public-export standard and checker | ROUTE_AND_RETAIN_LITERAL |
| Critical Repository Boundary | critical repository-boundary reference | ROUTE |
| UI / Web Design Contract | root `DESIGN.md` | ROUTE |
| Mandatory Live Governance Proof | compact routing index plus release-gate command | ROUTE |
| Mandatory Live Run Diagnostics | live-run diagnostic standard | ROUTE |
| Mandatory ADIF Defect Registry Disclosure | ADIF registry, resolver, checker, template | ROUTE |
| Mandatory Value-Parked Lane Reopen Discipline | value-parked reopen standard | ROUTE |
| Mandatory Work Order Source Verification | canonical Work Order template and MA1 standard | ROUTE |
| Governed Artifact Literal-Format Gotchas | literal-format gotchas reference | ROUTE |
| Mandatory Work Order Closure Quality Gate | closure-quality standard | ROUTE |
| Mandatory Roadmap Closure Freshness Guard | roadmap-closure front door, standard, checker | ROUTE |
| Mandatory Work Order Dependency Release Evidence | dependency-release standard and dispatch checker | ROUTE |
| Mandatory Governed File Maintainability Planning | governed file-size guard | ROUTE |
| Mandatory Text Encoding And Symbol Discipline | text-encoding standard | ROUTE |
| Mandatory JSON Generated Aggregate Discipline | generated-aggregate standard and generators | ROUTE |
| Mandatory Agent Autorun Workflow Control | autorun and commit-steward standards/checkers | ROUTE |
| Mandatory Agent Handoff Boundary Contract Guard | handoff front door, contract, checker | ROUTE |
| Mandatory Agent Interaction Workspace Design Boundary | agent-workspace front door, contracts, checker | ROUTE |
| Mandatory Agent Workspace State Generated Aggregate Guard | state aggregate, taxonomy, item template, checker | RETAIN_LITERAL |
| Mandatory Agent Workspace Skeleton Guard | workspace skeleton README and checker | RETAIN_LITERAL |
| Mandatory Agent Workspace Runtime Boundary Guard | runtime contract, queue README, operator plan, checker | RETAIN_LITERAL |
| Mandatory IDE Extension Multi-Provider Execution Log Guard | execution-log standard and checker | ROUTE |
| Mandatory Finding-To-Governance Learning Trigger Guard | learning-trigger standard and checker | ROUTE |
| Mandatory Learning Signal Intake Bridge | learning-signal standard | ROUTE |
| Mandatory External Repository Absorption Entry Rule | absorption checker, source-reconciliation matrix, mirror index | ROUTE |
| Mandatory Knowledge Absorption Blind-Spot Prevention | knowledge-absorption standard | ROUTE |
| Mandatory Corpus Completeness And Report Integrity | corpus completeness standard and checker | ROUTE_AND_RETAIN_LITERAL |
| Mandatory Corpus-To-Knowledge-Map Reconciliation | knowledge method, reconciliation standard and checker | ROUTE_AND_RETAIN_LITERAL |
| Mandatory Corpus Intelligence Classification | corpus classification standard and checker | ROUTE |
| Mandatory Corpus Search And Filter Readiness | corpus search/filter standard | ROUTE |
| Mandatory Corpus Scan Registry Consultation | scan standard, registry, guard and checker | ROUTE |
| Mandatory System Loop Interlock | interlock standard, registry and checker | ROUTE |
| Latest Closed Continuation Roadmap | compact routing index; no historical narrative in root carrier | ROUTE |

## CLAUDE Heading Disposition

`CLAUDE.md` is `NOT_CVF_SOURCE`. Its startup, diagnostics, corpus, ADIF,
source-verification and literal-format sections route to canonical CVF owners.
Its commands, architecture, CI/CD, workspace isolation, public-sync, catalog,
and key-reference sections become short provider-operating pointers rather
than duplicated governance authority. The historical full file is archived
byte-identically and is never cited as canonical authority.

Direct literals that must remain in compact `CLAUDE.md` are
`CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`,
`governance/compat/check_corpus_completeness_report_integrity.py`, and
`governance/compat/check_corpus_to_knowledge_map_reconciliation.py`.

## Downstream Template Heading Disposition

| Current heading | Compact owner/disposition |
|---|---|
| Mandatory Governance Proof | retain bounded live-proof rule |
| First-Request Protocol (MANDATORY) | retain progressive bootstrap-first sequence and fallback |
| Mandatory Continuity Rehydration | retain required doctor tokens and targeted-read semantics |
| Phase Model | retain exact seven-step literal |
| Provider-Neutral Role Contract | retain all seven role tokens |
| Live Governance Evidence Rule | retain no-mock governance claim boundary |
| Workspace Isolation Rule | retain workspace/core boundary pointer |
| Risk Classification | retain R0-R3 routing and approval boundary |
| Governance Latency and Approval Continuity | retain heading once and all golden-harness phrases |
| Required First-Read Documents | reduce to at most 12 progressive current paths |
| Handoff and Tranche Closure Protocol | retain current-state/handoff/closure sync rule |
| Workspace-To-Web Evidence Bridge | retain evidence-only bridge boundary |
| Override Refusal | retain refusal and escalation rule |

## Machine Reader Matrix

| Reader | Read behavior | Required T2B handling |
|---|---|---|
| `check_active_session_state.py` | reads both carriers for front-door/state markers, stale handoff references, and full-read wording | retain direct markers and progressive wording |
| `check_agent_workspace_state.py` | requires exact AGENTS heading plus aggregate/checker/taxonomy/template tokens | retain literals |
| `check_agent_workspace_skeleton.py` | requires exact AGENTS heading plus README/checker tokens | retain literals |
| `check_agent_workspace_runtime_boundary.py` | requires exact AGENTS heading plus contract/queue/plan/checker tokens | retain literals |
| `check_public_export_disposition.py` | requires its checker path in AGENTS | retain literal |
| `check_corpus_completeness_report_integrity.py` | requires its checker path in both root carriers | retain literal in both |
| `check_corpus_to_knowledge_map_reconciliation.py` | requires its checker path in both root carriers | retain literal in both |
| `check_agent_packet_authority_and_encoding.py` | classifies both paths and rejects provider-local authority use | preserve path and `NOT_CVF_SOURCE` boundary |
| `check_index_classification.py` | classifies `CLAUDE.md` as provider-private | preserve `NOT_CVF_SOURCE` boundary |
| `check_core_guard_self_protection.py` | treats both root carriers as protected | authorize exact paths |
| `check_closure_packaging_preflight.py` | treats both root carriers as protected | provide complete Core authorization |
| `check_agent_operation_trace.py` | treats AGENTS as protected path | exact manifest and trace required |
| `run_agent_commit_steward_preflight.py` | classifies AGENTS routing-only versus material edits | T2B AGENTS rewrite is material, not pointer-only sync |
| workspace path checkers | use AGENTS path as a protected/binding surface | keep required literals above |
| packet/scaffold/dispatch-quality helpers | refer to AGENTS as canonical agent guidance | do not reclassify AGENTS as provider-specific |
| catalog advisory/foundational surface checks | name `CLAUDE.md` as an existing/provider carrier | retain `NOT_CVF_SOURCE` file role |
| `scripts/check_cvf_workspace_agent_enforcement.ps1` | reads generated downstream AGENTS for seven roles, phase chain, rehydration tokens | retain every exact token |
| `scripts/test_cvf_golden_downstream_bootstrap.ps1` | requires one governance-latency heading and five literal phrases | retain heading and phrases exactly once |
| `scripts/new-cvf-workspace.ps1` | copies/replaces template tokens and merge block | preserve substitution tokens and merge compatibility |

## Approved T2B Design Boundary

- `AGENTS.md`: maximum 220 lines and 20,480 bytes.
- `CLAUDE.md`: maximum 160 lines and 16,384 bytes.
- downstream template: maximum 180 lines and 20,480 bytes.
- routing index: maximum 300 lines and 32,768 bytes.
- three dated archives must equal the preimage hashes above byte-for-byte.
- a new checker must enforce budgets, hashes, required literals, routing-index
  coverage, and hook/autorun/CI bindings.
- existing downstream workspaces are not changed; only future/generated
  instructions are affected.

## Findings / Position

The rewrite is feasible only with a compact canonical routing index and direct
retention of the machine literals identified above. Archive-only ownership is
rejected because archives are historical evidence, not active authority.

## Risk / Corrective Action

Primary risk is silent loss of a literal binding while prose still appears
semantically similar. Corrective action is exact heading/token checking,
byte-identical archives, N/N+1 budget proof, and the downstream golden harness.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | governed Work Order dispatch only; no external material promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T2B Work Order and independent review |
| Disposition | NOT_APPLICABLE_WITH_REASON: this is a local source-binding map, not external intake |
| Claim boundary | repository-local source mapping only |

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: no legacy or external repository is absorbed.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no corpus enumeration or completeness claim exists.

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON: no external repository absorption is in scope.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| T2B scope and stop rule | `docs/roadmaps/CVF_ACTIVE_CONTINUITY_READ_COST_REDUCTION_ROADMAP_2026-08-10.md` | T2B and Stop Conditions | `T2B` | active-continuity roadmap | ACCEPT |
| Core carrier current headings | `AGENTS.md` | lines 3-1113 | level-two headings | root agent instruction carrier | ACCEPT |
| provider carrier current headings | `CLAUDE.md` (`NOT_CVF_SOURCE`; measured carrier only) | lines 5-454 | level-two/three headings | provider-local guidance carrier | ACCEPT |
| downstream headings and substitution tokens | `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | lines 10-247 | template headings and `{{...}}` tokens | downstream bootstrap template | ACCEPT |
| direct Core routing markers | `governance/compat/check_active_session_state.py` | constants and lines 656-704 | `AGENT_ROUTER_MARKERS`; `_classify` | active-session checker | ACCEPT |
| workspace state marker bindings | `governance/compat/check_agent_workspace_state.py` | marker map | `AGENTS_PATH` marker tuple | workspace state checker | ACCEPT |
| workspace skeleton marker bindings | `governance/compat/check_agent_workspace_skeleton.py` | marker map | `AGENTS_PATH` marker tuple | workspace skeleton checker | ACCEPT |
| workspace runtime marker bindings | `governance/compat/check_agent_workspace_runtime_boundary.py` | marker map | `AGENTS_PATH` marker tuple | workspace runtime checker | ACCEPT |
| downstream doctor literals | `scripts/check_cvf_workspace_agent_enforcement.ps1` | lines 407-440 | `requiredRoleTokens`; `rehydrationTokens` | workspace doctor | ACCEPT |
| golden carrier literals | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | lines 63-69 | `Test-CvfCarrierContent` | downstream bootstrap harness | ACCEPT |
| template consumer | `scripts/new-cvf-workspace.ps1` | lines 343-413 | `$agentsTemplatePath` | downstream bootstrap writer | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_active_session_state.py`; `governance/compat/check_agent_workspace_state.py`; `governance/compat/check_agent_workspace_skeleton.py`; `governance/compat/check_agent_workspace_runtime_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` |
| literalTokensReviewed | `AGENT_ROUTER_MARKERS`; `AGENTS_PATH`; `CLAUDE_PATH`; direct marker tuples; `Test-CvfCarrierContent` |
| gateRunPurpose | confirm the source map before any carrier rewrite |
| claimBoundary | current reader bindings and T2B design only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | source mapper/reviewer |
| Provider or surface | local private CVF Core workspace |
| Session or invocation | ACRC-T2B source mapping, 2026-08-11 |
| Working directory | repository root at `178c5e7e1` |
| Command or tool surface | targeted source reads, heading extraction, token search, hashes and sizes |
| Target paths | three current carriers and all repository readers named above |
| Allowed scope source | operator T2B selection and active-continuity roadmap |
| Before status evidence | clean HEAD `178c5e7e1`; staged zero |
| After status evidence | this source map only before packet authoring |
| Diff evidence | source hashes, heading map, reader-token search |
| Approval boundary | source mapping and dispatch design only |
| Claim boundary | no carrier rewrite, downstream mutation, external call, commit, or push |
| Agent type | source mapper/reviewer |
| Invocation ID | `active-continuity-read-cost-t2b-source-map-2026-08-11` |
| Expected manifest | this source-map artifact during mapping phase |
| Actual changed set | this source-map artifact during mapping phase |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: mapping deletes or renames nothing |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance source map. Public projection requires a
separate public-sync batch after accepted implementation.

## Claim Boundary

This matrix accepts only the source map and bounded T2B design. It does not
assert that compact carriers already exist or authorize T3, provider/live,
runtime, downstream mutation, deployment, public sync, push, or production.
