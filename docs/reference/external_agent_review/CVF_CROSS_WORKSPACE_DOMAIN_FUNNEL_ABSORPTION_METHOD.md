# CVF Cross-Workspace Domain-Funnel Absorption Method

Memory class: governed-method

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-09-11

## Purpose

Define the CVF absorption method for a broad external-source program in which
remote Web research first groups many repositories by domain and filters them
through multiple evidence rounds. Remote filtering prioritizes Local work; it
does not define the Local source boundary. Every remotely researched repository
with a usable GitHub clone URL proceeds to Local source acquisition, freshness
resolution, and bounded use-case recovery before Local private-CVF final
reconciliation.

The method reduces repeated CVF comparison work and avoids absorbing the same
mechanism independently from several similar repositories.

## Scope / Owner Boundary

Method identifier: `cvf.cross-workspace-domain-funnel-absorption@1.2.0`

This method owns:

- multi-repository source intake grouped by domain;
- remote upstream identity, freshness, license, relevance, and duplication
  filtering;
- mechanism-level shortlist convergence before CVF comparison;
- mandatory Local source-mirror acquisition for remotely researched GitHub
  repositories, subject only to an explicit blocked disposition;
- Local observed-upstream pinning and external-to-Local freshness-delta
  accounting;
- Local use-case recovery and runtime-sufficiency reconciliation so a remote
  pattern shortlist cannot become an accidental corpus boundary;
- the boundary between remote public-CVF pre-mapping and Local private-CVF
  final disposition;
- corpus accounting from the umbrella source ledger to every child return.

It does not make the remote agent, a repository, a search result, or an
external handoff pack CVF authority. It does not authorize implementation,
provider use, publication, deployment, dependency installation, or destructive
effects.

## Two-Step Operating Agreement And Proportional Depth

Operator-ratified on 2026-09-11: Step 1 is external multi-repository domain
research; Step 2 is the existing Local repository absorption process governed
by `CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`. This method coordinates the two
steps and adds no competing Local absorption lifecycle. Any work order issued
for Local source inspection, recovery, or implementation uses internal agents.

Step 1 must return three separate views: shared mechanism families with all
supporting sources, repository-specific operational value, and unverified or
unread regions. A duplicate-pattern decision does not erase unique examples,
skills, integrations, evaluations, failure behavior, or source provenance.
Read supplied CVF orientation before research; perform detailed public-CVF
mapping after domain filtering. Local private-CVF absence remains a hypothesis
until Local source comparison.

Step 2 applies the following depth levels within existing authority:

| Level | Required work | Exit or escalation |
|---|---|---|
| Initial survey for every acquired repository | Pin source; record freshness and license; enumerate all paths; classify relevant source regions; read representative content from applicable use-case, example, test, skill and consumer regions | Record promising deltas, excluded regions and unknowns; never infer no value from filenames alone |
| Selected capability investigation | Fully read selected files; trace inputs, outputs, consumer, invocation and failure paths; compare with current CVF owner evidence | Stop when the named value/overlap decision is supported; expand only for a decision-changing evidence gap |
| Selected value conversion | Adapt accepted knowledge, recipe, fixture, evaluation, skill, contract or implementation into its CVF owner under the applicable work order | Prove the claimed maturity; integration and use proof remain distinct from source reconciliation |

Every surveyed region records its actual read depth. File enumeration is not
semantic reading. A bounded survey cannot justify repository-wide
`NO_NEW_VALUE` or complete use-case coverage. Missing evidence and exhausted
budget remain explicitly unresolved/deferred, never converted into no value.

## Shared Evidence, Value Selection And Stop Rules

Use one umbrella source ledger and linked capability/use-case records. Stable
sourceId, mechanismId and useCaseId preserve many-to-many provenance. Each
source keeps its own commit, freshness and license evidence. Compare a shared
mechanism with CVF once, then examine per-source application differences.

A capability record carries: user outcome; source pin and path/symbol evidence;
shared mechanism; distinct use case; read depth; current CVF owner or evidenced
owner gap; producer, verifier and consumer; failure behavior; missing CVF link;
value/disposition; evidence confidence; next action or explicit reopen trigger.
Tests, recipes, fixtures, adapters and usable skills count as material value
even when their architectural pattern already exists in CVF. Skill inspection
includes instructions, scripts, assets and tool composition where present.

Prioritize a current workflow gap first, then reliability or delivery-cost
improvement, then a new capability with a concrete use case. Preserve promising
future value with source evidence and the existing conditional reopen index.
Reserve a bounded exploration sample for plausible unique value outside the
external shortlist; novelty without a current consumer is not automatically
worthless. Each future dispatch states its exploration allowance and budget.

Before another research round or deep read, name the unresolved decision,
expected information gain and cost reason. Stop once evidence supports that
decision. At the agreed budget ceiling, return existing evidence and a concrete
gap; Local decides continuation. Do not automatically repeat the research loop.

Reuse immutable inventories, hashes and accepted owner comparisons. Freeze a
pin for the investigation and assess relevant upstream deltas at the next
decision boundary. Refresh Local owner evidence when its source changes.
Reviewer consumes valid evidence and investigates named contradictions rather
than repeating the worker's scan. Reports reference the shared ledger instead
of copying its rows into every packet. Required governance gates still apply;
this agreement does not activate selective gate execution or extend the TPGR
trancheValue machine schema to absorption.

## Pilot And Scale-Out Admission

Before broad rollout, nominate one domain and about three repositories: two
with overlapping mechanisms and one with a materially different use case.
Prefer the existing researched pool and reuse Agentgateway evidence when it
fits the selected domain. Do not force unrelated sources into the pilot or
invent missing historical research. External first returns method concerns and
pilot nominations; Local selects the scope and issues the next bounded packet.

Record external and Local discoveries separately, duplicate investigation
avoided, unresolved regions, evidence-supported value converted or preserved,
and research/reviewer/repair/integration effort. Separate measured values from
estimates; unavailable time, token or monetary cost is UNKNOWN, not zero.
File/repository/packet counts are coverage measures, not value measures.

Local reviews the pilot's recovered value, decision quality and total effort
before selecting the next batch size and depth budget. No numeric efficiency
threshold or cost saving is claimed before pilot evidence exists. Survey
completion, candidate reconciliation, implementation and proven use remain
separate milestones; broad rollout requires this explicit Local assessment.

## Canonical Funnel

```text
LOCAL_UMBRELLA_SCOPE_AND_SOURCE_LEDGER
-> OPERATOR_RELAY_OUT
-> REMOTE_CURRENT_SOURCE_IDENTITY_AND_FRESHNESS
-> REMOTE_DOMAIN_GROUPING
-> REMOTE_MULTI_ROUND_EVIDENCE_FILTERING
-> REMOTE_CROSS_REPOSITORY_MECHANISM_DEDUPLICATION
-> REMOTE_SHORTLIST
-> REMOTE_PUBLIC_CVF_PREMAP
-> OPERATOR_RELAY_IN
-> LOCAL_RETURN_VALIDATION
-> LOCAL_GITHUB_SOURCE_MIRROR_ACQUISITION
-> LOCAL_OBSERVED_UPSTREAM_PIN_AND_FRESHNESS_DELTA
-> LOCAL_USE_CASE_RECOVERY_PASS
-> LOCAL_SHORTLIST_REOPEN_IF_MISSED_VALUE
-> LOCAL_CURRENT_PRIVATE_CVF_RECONCILIATION
-> LOCAL_CROSS_RETURN_DEDUPLICATION
-> LOCAL_FINAL_TECHNICAL_DISPOSITION
-> UMBRELLA_LEDGER_RECONCILIATION
-> EXTERNAL_RESEARCH_PHASE_CLOSED
-> INTERNAL_WORK_ORDER_IF_SELECTED
-> INTERNAL_SHARED_WORKSPACE_EXECUTION_AND_REVIEW
```

The ordering is material. Broad repository discovery does not trigger a full
CVF comparison for every repository. Remote filtering determines priority and
initial semantic regions, while Local source acquisition verifies what source
actually exists at the observed upstream head. A bounded Local use-case pass
may reopen a remotely filtered repository when examples, tests, evaluations,
integrations, skills, or executable consumers expose material value omitted by
pattern-level research. Deep CVF comparison remains focused on retained or
reopened mechanisms.

The following invariants are normative:

```text
EXTERNAL_SHORTLIST_IS_PRIORITY_INPUT_NOT_LOCAL_CORPUS_BOUNDARY
LOCAL_CLONE_IS_SOURCE_ACQUISITION_NOT_ABSORPTION_COMPLETION
PATTERN_FIT_DOES_NOT_PROVE_RUNTIME_SUFFICIENCY
ARCHITECTURE_SHELL_WITHOUT_USE_CASE_AND_CONSUMER_EVIDENCE_IS_PARTIAL
```

## Hard Research-To-Execution Phase Boundary

External participation is limited to discovery, source research, mechanism
filtering, preliminary public-CVF mapping, contradiction testing, and advisory
convergence on what may be worth absorbing. The Local Agent remains the final
technical disposition owner.

Once the Local Agent issues a governed work order for a selected mechanism,
that task has crossed into `INTERNAL_AGENT` execution. From that point:

- the worker, orchestrator, reviewer, and closer operate against the same Local
  workspace and governed SOT;
- the work order uses the internal shared-workspace worker contract, not the
  detached external-return contract;
- worker evidence is returned through governed Local files and Git/worktree
  state, not through operator copy/paste relay;
- the external research agent has no implementation, worker, reviewer, or
  closure role in that work order;
- any later question sent back to a Web agent is a new bounded research loop,
  not continuation of the internal work order.

The boundary is based on workspace and lifecycle state, not model, provider,
agent name, or agent count. A Claude, Codex, or other worker running in the same
Local VS Code workspace is an internal agent for this lifecycle.

## Umbrella Ledger And Domain Groups

The Local Agent records one umbrella ledger before dispatch. Each source row
keeps a stable source identity and one domain such as `GENERAL`, `SKILL`,
`MEMORY`, `MCP`, or `ARCHITECTURE`, or another explicitly defined domain.

Every input source must reach one terminal funnel state:

- `SHORTLISTED_FOR_CVF_COMPARISON`;
- `FILTERED_IDENTITY_OR_FRESHNESS`;
- `FILTERED_LICENSE_OR_USAGE_BOUNDARY`;
- `FILTERED_LOW_RELEVANCE`;
- `FILTERED_DUPLICATE_MECHANISM`;
- `DEFERRED_WITH_REASON`;
- `BLOCKED_UNVERIFIED`.

Every GitHub-backed source must additionally reach one Local acquisition state:
`LOCAL_MIRROR_PINNED`, `LOCAL_MIRROR_REFRESHED`, or
`BLOCKED_SOURCE_MIRROR_WITH_REASON`. Every acquired source must reach
`LOCAL_USE_CASE_PASS_COMPLETE`, `LOCAL_REOPEN_MISSED_USE_CASE`, or
`LOCAL_USE_CASE_PASS_BLOCKED_WITH_REASON` before umbrella completion.

Grouping is a review optimization, not an authority merge. Repository pins,
license evidence, source locations, and claim boundaries remain source-specific.

## Remote Multi-Round Filtering

The remote Web stage performs bounded evidence filters in this order:

1. Resolve current repository identity, canonical upstream, immutable commit,
   and freshness evidence.
2. Resolve license and permitted use posture.
3. Test domain relevance and identify concrete source-backed mechanisms rather
   than repository-level marketing claims.
4. Compare mechanisms across repositories in the same domain and collapse
   duplicates into one mechanism family with all supporting sources retained.
5. Rank the remaining mechanism families by likely CVF value, evidence quality,
   operating conditions, and risk.
6. Create a shortlist with explicit retained and filtered-out reasons.

Filtering must not hide sources. A filtered source remains in the processing
ledger with its terminal reason. Search snippets, popularity, provider/model
identity, and agent consensus are not evidence of mechanism value.

Remote filter dispositions are advisory until Local acquisition accounting is
terminal. `FILTERED_LOW_RELEVANCE` and `FILTERED_DUPLICATE_MECHANISM` may reduce
deep-read priority, but they do not waive the Local mirror and bounded use-case
recovery rules below.

## Mandatory Local Source Acquisition And Freshness Pinning

Before each new Local repository audit or absorption batch, apply
`.private_reference/source_mirrors/README.md`, section
`Mandatory Upstream Freshness Preflight`. This also applies to reused mirrors:
observe live upstream before manifest freeze, acquire the selected current
source, and reconcile changed paths before dispatch. Preserve active worker
pins and record any explicit historical-target reason or acquisition blocker.

For every repository researched remotely, when a canonical GitHub clone URL is
available and reachable, the Local Agent must create or refresh a source mirror
under:

```text
.private_reference/source_mirrors/<owner>__<repo>/
```

The Local source tree used for analysis must be pinned to an exact commit and
indexed in `.private_reference/source_mirrors/INDEX.md`. A shallow or partial
Git transport is acceptable only when the complete source tree for the pinned
commit remains readable. Clone presence records source availability only;
semantic coverage and absorption require their separate governed evidence.

Each umbrella source row or linked acquisition receipt must record:

| Field | Required meaning |
|---|---|
| `externalResearchPin` | Exact commit declared by the remote return, or `EXTERNAL_PIN_UNKNOWN`. |
| `remoteDefaultBranch` | Canonical upstream default branch observed by Local. |
| `localObservedUpstreamHead` | Exact remote default-branch HEAD resolved at Local fetch time. |
| `localAbsorptionPin` | Exact immutable commit checked out and used for Local analysis. |
| `localFetchTime` | Timestamp of the Local remote observation. |
| `freshnessDeltaStatus` | `MATCH`, `LOCAL_UPSTREAM_ADVANCED`, `EXTERNAL_PIN_UNKNOWN`, or `REMOTE_REWRITTEN_OR_UNREACHABLE`. |
| `licenseAtLocalPin` | License path and disposition observed at the Local analysis pin. |

"Latest" is an observation, not a stable version. The Local Agent must never
silently replace the remote research pin with a moving branch name. When
`LOCAL_UPSTREAM_ADVANCED` applies, Local must inspect the source delta affecting
the retained mechanisms and use-case regions before relying on remote findings.
When the remote agent omitted its pin, Local records `EXTERNAL_PIN_UNKNOWN` and
does not represent the remote research as current-source proof.

If acquisition cannot be completed, the row must use
`BLOCKED_SOURCE_MIRROR_WITH_REASON` and record the concrete access, repository,
resource, legal, or security blocker. Missing source acquisition cannot be
converted into `NO_NEW_VALUE`.

Cloning grants read-only source authority. It does not authorize dependency
installation, build, test, execution, hook activation, credential use, network
behavior beyond Git acquisition, direct import, publication, or deployment.

## Local Use-Case Recovery Pass

After acquisition and before final Local disposition, perform a bounded pass
over every acquired repository to detect operational value that remote
pattern-level research may have omitted. At minimum, enumerate and classify
applicable source regions for:

- READMEs, documentation, tutorials, examples, demos, quickstarts, and recipes;
- templates, sample configuration, manifests, fixtures, and reference outputs;
- tests, evaluations, benchmarks, failure cases, retries, rollback, and recovery;
- integrations, adapters, plugins, commands, APIs, hooks, and orchestration;
- skills, prompts, tool bindings, capability composition, and end-to-end user
  workflows;
- state, memory, permission, lifecycle, observability, and consumer behavior.

For a skills repository, pattern names or skill metadata are insufficient. The
Local ledger must determine, where present, each material skill's entry point,
inputs, tool or dependency assumptions, produced outputs, failure behavior,
composition path, executable consumer, and test/evaluation/demo evidence.

The pass may use a repository-wide path manifest followed by selective semantic
reads. It must not claim complete use-case coverage unless manifest, terminal
processing ledger, exclusions, unreadable files, aggregation, and drift all
reconcile under the corpus-completeness standard. Previously filtered sources
remain eligible for `LOCAL_REOPEN_MISSED_USE_CASE` when this pass finds material
producer-to-consumer or operational evidence.

## Runtime Sufficiency Reconciliation

Each retained or reopened candidate must distinguish architectural fit from
operational completeness. Record at least:

| Evidence dimension | Required question |
|---|---|
| Current owner | Which existing CVF doctrine, contract, plane, system chain, or workflow owns the concern? |
| Producer | What source or runtime component produces the capability or evidence? |
| Verifier | What gate, invariant, evaluator, or fail-closed check verifies it? |
| Consumer | What real workflow or runtime path consumes the verified output? |
| Invocation path | How is the producer-to-verifier-to-consumer chain entered? |
| Use proof | Which example, test, evaluation, fixture, demo, or receipt proves intended use? |
| Failure behavior | What happens on invalid input, denied authority, unavailable dependency, retry, or rollback? |
| Missing link | Is CVF missing doctrine, contract, implementation, integration, consumer, or proof? |

Use one bounded sufficiency status per candidate:
`ARCHITECTURE_ONLY`, `CONTRACT_ONLY`, `IMPLEMENTATION_NO_CONSUMER`,
`CONSUMER_NO_USE_PROOF`, `USE_CASE_PROVEN`, or `BLOCKED_EVIDENCE_GAP`.
An `ABSORB` or `ADAPT` knowledge decision may still be architecture-only, but it
must not be represented as runtime-capable until the executable consumer and use
proof exist under separately authorized implementation evidence.

## Delayed CVF Comparison

Shortlisted mechanism families proceed first to CVF comparison. A repository
or mechanism reopened by the Local use-case recovery pass joins that queue with
its source-backed reopen reason:

1. The remote agent reads the supplied `EXTERNAL_AGENT_READ` context and the
   task-pinned public GitHub repository.
2. It performs preliminary public owner and overlap mapping.
3. It returns hypotheses and source evidence, not private-CVF absence claims.
4. The Local Agent validates the return, checks current private owners and
   implementation history, challenges novelty, and issues the final technical
   disposition.

Allowed Local dispositions remain `ABSORB`, `ADAPT`, `DEFER`, `REJECT`,
`BLOCK`, and `NO_NEW_VALUE`. Mechanisms supported by several repositories are
still mapped to one current CVF owner wherever possible.

## Task And Return Packaging

The umbrella program may use one remote research agent or several. It may use a
domain-batch discovery return, per-repository child returns, or a bounded mix,
provided every source and mechanism retains independent provenance.

```text
REMOTE_AGENT_COUNT != SOURCE_COUNT
SOURCE_COUNT != RETURN_COUNT
RETURN_COUNT != TRUST_LEVEL
```

If the active task-capsule schema binds one repository, the Local Agent issues
one child capsule per shortlisted repository under the umbrella ledger. It must
not compress a multi-repository program into a single-repository task and then
mistake the conforming single-repository return for program completion.

The Operator transports the exact packets and returns under
`cvf.cross-workspace-evidence-relay@1.0.0` and does not adjudicate their
content during transport. Operator relay ends for a selected task when the
Local Agent issues its internal work order; normal same-workspace dispatch and
review then apply.

## Local Aggregation And Completion

Local final reconciliation occurs at mechanism level across all validated
returns. It must detect:

- the same mechanism proposed by several repositories;
- a mechanism already owned or implemented by current private CVF;
- competing mechanisms with incompatible assumptions;
- a higher-quality source replacing a weaker source without losing lineage;
- domain-spanning mechanisms that still require one canonical CVF owner plus
  explicit dependencies.

No complete-corpus or complete-absorption claim is allowed until umbrella totals
reconcile: input sources equal shortlisted plus every terminal filter, defer,
and block state; GitHub-backed researched repositories equal Local pinned or
explicitly blocked mirrors; acquired repositories equal completed, reopened, or
blocked Local use-case passes; retained and reopened mechanisms equal locally
accepted, adapted, deferred, rejected, blocked, or no-new-value outcomes.

## Current EARA-AGW-T0 Scope Clarification

`EARA-AGW-T0` is a Local-issued single-repository child task bound to
`agentgateway/agentgateway`. A remote return containing only Agentgateway is
therefore contract-conforming. It is not evidence that a broader multi-source
absorption program contains only one repository, and it cannot supersede an
umbrella source ledger.

The Local Agent, not the remote agent, created this narrow return scope. Any
broader source program must remain separately visible and must be restored to
continuity before program-level completion is assessed.

## Research-Assisted Audit Application

For repository-absorption audits assisted by a Web/remote research agent, apply
the `cvf.research-assisted-repository-absorption@1.0.0` profile in
`CVF_CROSS_WORKSPACE_EVIDENCE_RELAY_METHOD.md` inside this funnel. This is an
extension of the existing two-step agreement, not a parallel workflow.

The Local dispatcher refreshes `EXTERNAL_AGENT_READ` before each dispatch and
binds one independently reviewable audit question per lane. The remote return
is advisory source evidence. Local performs integrity validation first, checks
the upstream mechanisms, and then reconciles them against current private-CVF
owners. Local repository authority wins every contradiction.

Use the audit outcomes as a narrow decision view over the existing funnel
taxonomy: `NO_CHANGE -> NO_NEW_VALUE`, `ADAPT -> ADAPT`, and `WATCH -> DEFER`
or `BLOCK` with a named trigger/reason. `ADOPT -> ABSORB` is permitted only
after the profile's `ADOPT_HIGH_BAR` proves that the architectural
responsibility is absent and cannot map to an existing owner. A returned
advisory contract is not the default design to absorb.

Multiple questions remain independent through Local disposition even when one
return package or operator relay carries them together. External research must
close before any selected change enters a separate internal work order; the
Local reviewer receives and adjudicates external returns and internal worker
returns as separate evidence lanes.

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | Multi-repository and mixed external-source umbrella corpus |
| Upstream/source-mirror disposition | Every remotely researched repository with a usable GitHub clone URL requires a Local pinned mirror or `BLOCKED_SOURCE_MIRROR_WITH_REASON`; remote pins remain separately recorded |
| Enumeration/manifest plan | Umbrella source ledger plus external research pin, Local observed upstream head, Local absorption pin, freshness delta, domain membership, and use-case source-region manifest |
| Per-file terminal-ledger plan | Repository-wide path enumeration plus selective semantic reads for the Local use-case recovery pass; any completeness claim requires full terminal reconciliation |
| Owner/overlap route | Remote public-CVF pre-map after shortlist, then Local current-private-CVF final reconciliation |
| Value-disposition route | Cross-repository mechanism family -> Local owner -> `ABSORB`/`ADAPT`/`DEFER`/`REJECT`/`BLOCK`/`NO_NEW_VALUE` |
| Claim boundary | Funnel completion is not absorption, implementation, verification, freeze, public release, or production readiness |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | Future work-order-bound umbrella source ledger; this method materializes no source corpus |
| Enumeration command | Filesystem-backed direct enumeration recorded by each future governed run |
| Manifest artifact or inline manifest | Inline manifest: method definition only; no executed source rows are claimed |
| Processing ledger artifact or inline ledger | Inline ledger: future umbrella ledger must terminally account for every source |
| Ledger terminal statuses | `READ`, `ADAPTED`, `DEFERRED`, `REJECTED`, `NO_NEW_VALUE`, `BLOCKED_UNREADABLE` |
| Disposition taxonomy | `ABSORB`, `ADAPT`, `DEFER`, `REJECT`, `BLOCK`, `NO_NEW_VALUE` |
| Owner-surface map | `docs/reference/external_agent_review/README.md` and the overlap table below |
| Unresolved items | No source corpus executed by this method artifact; future run unresolved items stay in its umbrella ledger |
| Absorption maturity | `NO_RUNTIME_VALUE_WITH_REASON` |
| Named runtime consumer | `METHOD_ONLY_NO_RUNTIME_CONSUMER` |
| Integration evidence | Method-only documentation; no runtime integration is claimed |
| Use proof | Method-only documentation; no runtime use proof is claimed |
| Operator checkpoint | `NOT_SATISFIED_METHOD_ONLY` |
| Absorption completion status | `NO_RUNTIME_VALUE_WITH_REASON` |
| Completion claim boundary | Defining the funnel does not complete any source absorption or authorize implementation |

## Corpus Completeness And Report Integrity

- Corpus task class: method definition, not an executed corpus run.
- Corpus root: future work-order-bound umbrella ledger.
- Snapshot time: not created by this method artifact.
- Enumeration command: filesystem-backed direct file reads in the future governed run.
- Manifest artifact or inline manifest: inline method-only declaration; zero executed source rows claimed.
- Manifest hash: `NOT_PRODUCED_METHOD_ONLY`.
- Processing ledger artifact or inline ledger: inline requirement for a future umbrella ledger.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`, `BLOCKED_UNREADABLE`.
- Reconciliation: method artifact input=0; processed=0; unresolved=0; future run totals are separate.
- Unresolved files: 0 in this method artifact; no external corpus was executed.
- Declared exclusions: all repository payloads and run-specific evidence.
- Unreadable or unsupported files: none assessed because no corpus run occurred.
- Aggregation check: not executed; the method defines the required future equality only.
- Drift check: not executed; every future run must resolve the Local observed
  upstream head, freeze an exact absorption pin, and compare it with the remote
  research pin rather than trusting an unverified "latest" claim.
- Output traceability: this method and active Local continuity only.
- Adversarial verification: machine guards must reject a future program-complete claim without ledger reconciliation.
- Corpus verdict: PARTIAL - method contract only; no source-corpus completeness claim.

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Multi-repository domain-funnel coordination | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`; `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_EVIDENCE_RELAY_METHOD.md` | `ENRICH_EXISTING` | Existing owners govern absorption evidence and cross-workspace transport but did not preserve domain-first filtering, delayed CVF comparison, or umbrella-versus-child cardinality | Add this method as the coordination owner without creating a second absorption core or relay protocol |
| Local source and use-case recovery | `.private_reference/source_mirrors/README.md`; `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | `ENRICH_EXISTING` | Existing source-mirror control establishes upstream authority, but the funnel did not require every GitHub-backed researched repo to be acquired or prevent a remote pattern shortlist from hiding operational use cases | Make Local acquisition, freshness delta, use-case recovery, and runtime-sufficiency classification mandatory before final umbrella completion |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| Domain-funnel coordination rule | Domain-first filtering and umbrella/child scope separation | `DOCTRINE_ADAPTED` | This method | Apply when authoring a multi-source umbrella run | Documentation only |
| Local mirror and freshness rule | Current source authority plus reproducible external-to-Local version delta | `DOCTRINE_ADAPTED` | This method and `.private_reference/source_mirrors/INDEX.md` | Require acquisition evidence for every GitHub-backed researched repository | Clone is read-only evidence, not activation |
| Local use-case recovery | Examples, tests, evals, integrations, skills, workflows, consumers, and failure behavior omitted by pattern research | `PACKAGE_CANDIDATE` | Current CVF owner selected after Local reconciliation | Reopen missed-value candidates and classify runtime sufficiency | No package or runtime promotion without separate authority |
| Future retained package mechanism | No package selected by this method | `PACKAGE_CANDIDATE` | Pending current-owner reconciliation | Require separate source evidence and work order | No install or package promotion authorized |
| Future retained runtime mechanism | No runtime selected by this method | `RUNTIME_CANDIDATE` | Pending current-owner reconciliation | Require separate implementation authority and use proof | No runtime activation authorized |
| Future reusable deterministic guard | No checker selected by this method | `CHECKER_CANDIDATE` | Pending applicable governance owner | Require recurrence evidence and separate checker scope | No checker mutation authorized |
| Direct foreign implementation | Source code is not imported by funnel survival | `REJECT_DIRECT_IMPORT` | Existing CVF owners | Adapt mechanism evidence only after Local review | No direct code import authorized |
| Filtered or duplicate source | Preserve terminal evidence without forced runtime conversion | `NO_PACKAGE_OR_RUNTIME_VALUE` | Umbrella processing ledger | Record reason and retain traceability | No package or runtime value claimed |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | `external repo or copied folder` |
| Chain map route | umbrella ledger -> domain grouping -> remote filtering and preliminary shortlist -> public-CVF pre-map -> Local mirror acquisition and exact pin -> freshness delta -> Local use-case recovery and possible reopen -> private-CVF reconciliation -> runtime-sufficiency classification -> umbrella reconciliation |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md` |
| Disposition | ADAPT the existing absorption and relay chain with a domain-funnel coordination owner |
| Claim boundary | The method governs ordering and evidence accounting only; no source is absorbed by entering or surviving the funnel |

## Epistemic Process Block

- Expected Result / Prediction: grouping repositories by domain and filtering
  source-native evidence before CVF comparison should reduce repeated owner
  searches and duplicate absorption candidates.
- Evidence Comparison: the operator clarified that the external Web workflow
  used multiple repositories and multiple filter rounds, while the Local-issued
  `EARA-AGW-T0` capsule requested only Agentgateway and therefore produced a
  correct one-repository return.
- Contradiction or Gap Disposition: the prior relay method described agent
  cardinality but did not distinguish umbrella source cardinality from child
  task cardinality or preserve the domain-first funnel. Version 1.0.0 also let
  the remote shortlist narrow Local attention without a mandatory Local mirror
  and operational-use-case recovery pass. Version 1.1.0 closes both gaps
  without treating remote pattern research as wrong or authoritative.
- Claim Update: `EARA-AGW-T0` is one child return; the broader absorption scope
  remains governed by its umbrella ledger, Local source acquisition, use-case
  recovery, runtime-sufficiency classification, and terminal accounting.

## Machine Enforcement Disposition

### Pilot Admission Safety Adjudication - 2026-09-11

Reviewer disposition: reject P4 observation attempt `ATTEMPT-d25f3c7dabca71e7`
as unusable measurement evidence. Trusted material was `d679c060871917c78bc83cf2f2c4eb51f8dcaf8e`;
disclosure was `dca44af2dfe38f91aab06a123d4ffc0429bce95a`. The pending journal
retains `UNSAFE_FINGERPRINT_MISMATCH`; no sample or checkpoint is promoted.

Read-only Git-blob reconstruction exactly reproduced the marker's fingerprint
`eaedcfd7875c759df0360fc17df693e74202a1e9f51330531ca434ac1ddc153c`.
The old receipt's declared fingerprint
`d8cce61338f2e66d92df297e7661127c877d3cee3d38b3240c1dbb93466064cd`
was not reproduced. The phase receipt has since been replaced by a different
range, so the original receipt bytes are unavailable for full reconstruction.

Source inspection of `governance/compat/run_agent_autorun_workflow_gate.py`
`_worktree_fingerprint` shows mutable disk bytes; source inspection of
`governance/compat/mfrp_shadow_canary_autocollect.py`
`_reconstruct_fingerprint_from_commit` shows committed Git blobs. Local
`core.autocrlf=true` and read-only byte comparisons establish LF/CRLF differences
on several material paths. This identifies a representation risk, not proof
that line endings alone explain the old failure. The collector's rejection is
retained as valid fail-closed behavior, not relabeled PASS or false positive.

Under the P4-C1 work order's Write Ownership, the reviewer may archive the
marker after this explicit rejection adjudication. Preserve its original bytes
and journal; do not rerun the historical observation, modify receipts, relax
identity comparison, or claim a repaired collector. Further fingerprint-domain
hardening requires a separately governed maintenance packet. This permits
ordinary governed documentation/dispatch work, not retrospective sample use.

- Disposition: `CHECKER_CANDIDATE`.
- Required future enforcement: multi-repository absorption packets must account
  every remotely researched GitHub repository as a pinned/refreshed Local
  mirror or `BLOCKED_SOURCE_MIRROR_WITH_REASON`, record the external-to-Local
  freshness fields, and carry use-case recovery plus runtime-sufficiency
  dispositions before umbrella completion.
- Activation boundary: checker, test, hook, scaffold, or autorun changes require
  a separate governed hardening tranche. They must not be inserted by mutating
  an already-dispatched shared-workspace worker contract mid-execution.
- Interim enforcement: dispatcher and reviewer apply this active reference
  manually and reject any umbrella-complete claim missing these records.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this Local method records a private coordination correction. No
public-sync action or public artifact was authorized.

## Claim Boundary

This method does not claim that any source list is complete, any repository is
permanently "latest", any candidate is novel, or any absorption is complete. A
Local mirror proves only availability of an exact source snapshot. It does not
make an external return authoritative and does not authorize implementation.
Those claims require the applicable manifests, ledgers, freshness-delta and
use-case evidence, current Local owner evidence, machine checks, and separate
governed authority.

## Machine Coordination Contract

The existing external-knowledge intake checker enforces this contract at changed
roadmap, work-order, review and continuity boundaries. Structured declarations
must match this canonical owner, independently of SOT. No promise of semantic
understanding or source/runtime completeness is implied.

```json
{
  "contractId": "cvf.external-local-absorption-coordination@1",
  "invariants": {
    "externalRole": "ADVISORY_RESEARCH_AND_PATTERN_MAPPING",
    "externalContext": "PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ",
    "localRole": "SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION",
    "finalDecisionOwner": "LOCAL",
    "localCoverageBasis": "SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST",
    "externalEvidenceAuthority": "INPUT_NOT_PRIVATE_CVF_PROOF"
  }
}
```

Changed applicable governed artifacts carry one `External/Local Coordination Binding`
JSON block with this contractId/invariants, the SHA256 of compact sorted-key UTF-8
contract JSON, and parentArtifact (null for a directly authorized root, otherwise
a normalized repo-relative governed Markdown path). Parents must carry the same
valid contract, with cycle and depth bounds. Untouched historical artifacts are
not rechecked unless explicitly bound as a parent. A missing or contradictory
binding fails; agreement among artifacts cannot override this method.

Continuity changes during absorption carry the same binding under value in
CVF_SESSION/state/entries/externalLocalAbsorptionCoordination.json; parentArtifact
identifies the governed active coordination artifact. Existing state regeneration
projects that source item. The checker reads compact state sources, not the full
aggregate. Missing/deleted state bindings, malformed bindings and unsafe linked paths fail closed.
Deleted historical artifacts are not automatically reopened. The structured binding
constrains declarations; it does not interpret arbitrary free-form planning prose.

No model call, source corpus traversal or extra hook is added. The existing
pre-dispatch/reviewer/pre-commit integration invokes the extended checker.

## Active Program Continuity And Exit Gate

Role and evidence ownership do not by themselves prevent a Local SOT from
leaving an unfinished absorption batch. During a multi-repository Local
absorption program, the source item
`CVF_SESSION/state/entries/activeExternalAbsorptionProgram.json` is the
structured continuity authority. It records the program ID, exact source set,
per-source state, next in-program source, action class, expansion posture and
exit evidence.

While any source is `INCOMPLETE`, the program must remain
`LOCAL_RUNTIME_VALUE_RECOVERY`, set `expansionAllowed` to false, select an
incomplete `nextSourceId` from the same source set, and project the exact
program/next-source markers into `nextAllowedMove`. Work may use independent
per-source lanes when a prior repair chain is stopped; it must not disguise a
stopped-chain successor or leave the active repository set.

The program may exit only through one of two machine states:

- `TERMINAL_ACCOUNTED`: every source has an allowed terminal disposition and
  at least one governed exit-evidence path exists;
- `SCOPE_EXIT_AUTHORIZED`: a governed operator scope-decision artifact exists.

An external comparison ending, a method pilot succeeding, or Local retaining
final authority is not an absorption-program exit condition. This check reads
only compact continuity sources and explicitly cited governed evidence paths;
it adds no repository traversal or external/model call.
