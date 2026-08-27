# CVF External-Agent Coding Quality And Forward-Value Absorption Roadmap

Memory class: FULL_RECORD

Status: PROPOSED_PENDING_EXTERNAL_ADVERSARIAL_REVIEW

docType: roadmap

Date: 2026-08-27

Roadmap ID: EACQ-FV

External absorption core: REQUIRED

Mixed-origin derived synthesis: REQUIRED

artifactClass: PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE

authorityStatus: NON_AUTHORITATIVE_UNTIL_REVIEWED

External knowledge intake routing: REQUIRED

## Purpose

Raise the quality and first-pass usefulness of code written for CVF by an
external agent, and repair the absorption review blind spot that can preserve
a source as `DEFERRED` while still overlooking its forward-looking design
value. The roadmap converts both concerns into governed, reviewable gates
without authorizing implementation yet.

## Target / Source

Two connected targets are in scope:

1. enrich the existing per-task external-agent capsule and return-review loop
   so coding work receives exact owners, symbols, invariants, tests, negative
   cases, boundaries, and prior reviewer corrections;
2. subject parked absorption value to an explicit forward-value assessment,
   then evaluate the eight deferred utility-under-attack files through three
   progressively more expensive gates.

Primary source surfaces:

- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json`
- `scripts/external_agent_packet.py`
- `scripts/Update-CVF-External-Agent-Packet.ps1`
- `docs/reference/external_agent_review/README.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md`
- `docs/audits/CVF_MPA_AI_T0_LOCAL_MEMORY_POISONING_ABSORPTION_AUDIT_2026-08-27.md`
- `docs/audits/CVF_MPA_AI_T0_LOCAL_MEMORY_POISONING_FILE_LEDGER_2026-08-27.json`
- `.private_reference/legacy/CVF 13.08/CVF_MEMORY_POISONING_ABSORPTION/04_UTILITY_UNDER_ATTACK/`

## Authorization / Decision

The operator authorizes this roadmap and asks that an operator-selected
external reviewer, currently Claude, challenge it before any implementation.
The normative role is `external reviewer`; the provider identity is not CVF
authority.

This roadmap is planning authority only. No schema change, generator change,
checker, benchmark, provider call, public sync, or runtime mutation may begin
until the external critique is returned, its findings are dispositioned, and
the operator explicitly accepts a revised roadmap or a bounded work order.

## Scope

In scope:

- reuse and enrich the existing task-capsule mechanism rather than create a
  competing external-agent context protocol;
- make prepared task capsules mandatory for coding modes if the design review
  accepts that rule;
- define a reusable reviewer-correction digest that is public-safe and does
  not leak private provenance;
- add a mandatory forward-value review after ordinary overlap classification;
- separate maturity and present authorization from potential value;
- preserve high-option-value deferred concepts in the conditional reopen
  index with concrete evidence triggers;
- normalize, then deterministically test, the eight-file utility-under-attack
  capability cluster before considering any model/provider evaluation;
- measure whether the upgraded external-agent packet reduces review repair,
  owner overlap, boundary violations, and missing negative-test coverage.

## Non-Goals

- no new capsule system parallel to `CVF_EXTERNAL_AGENT_TASK_CAPSULE`;
- no claim that more context always improves an external agent;
- no automatic acceptance of external code or prose as CVF authority;
- no use of provider identity as a normative worker or reviewer role;
- no benchmark threshold selected before a baseline exists;
- no provider/model run during the first two utility gates;
- no public export, deployment, production-readiness, or security-effectiveness
  claim from this roadmap;
- no reopening of the 34 already-owned files as implementation work merely
  because their independent rediscovery validates external-agent quality.

## Design Control Gate

`EACQ-FV-R0` is mandatory and blocking. The external reviewer must challenge:

- whether each proposed context field has a current owner and measurable use;
- whether task-capsule expansion creates context bloat or stale-authority risk;
- whether forward-value scoring can reward speculation or novelty theater;
- whether the three utility gates have observable stop conditions;
- whether any proposed checker would enforce shape without improving semantic
  review;
- whether private correction evidence can be summarized safely for a public
  external agent.

The reviewer return must classify every finding as `ACCEPT`, `REVISE`,
`REJECT`, or `SOURCE_GAP_WITH_SEARCH_EVIDENCE`, cite exact current CVF sources, and
state the smallest repair. Implementation remains closed until the operator
accepts the disposition packet.

## Forward-Value Review Control

Every future absorption closeout must retain the existing terminal ledger
status and add a second, orthogonal review for every `DEFERRED` item/group and
for representative plus high-risk `NO_NEW_VALUE` or `REJECTED` items.

Required questions:

| Dimension | Required question | Evidence expected |
|---|---|---|
| current-owner overlap | Is this already owned, and at what exact path/symbol? | source citation and overlap class |
| counterfactual acceleration | If available earlier, would this have avoided design, test, or review work CVF later performed? | later CVF artifact or correction showing the avoided work |
| directional novelty | Does it point to the next capability layer even when the present finding overlaps? | named uncovered evaluation, package, checker, or runtime seam |
| option value | Is the cost of losing the idea materially larger than the cost of parking it? | bounded preservation cost and loss scenario |
| cheap proof | What is the smallest provider-free test that could falsify its value? | command, fixture, output, and stop rule |
| maturity/value separation | Is the negative decision based only on build, review, or permission state? | independent maturity and value decisions |
| reopen accountability | Who owns the next decision and what observable evidence reopens it? | owner surface and conjunctive reopen condition |

Proposed secondary dispositions, subject to R0 critique:

- `DUPLICATE_CURRENT_OWNER`
- `FORWARD_DESIGN_SIGNAL`
- `EVALUATION_PRECURSOR`
- `OPTION_VALUE_PRESERVED`
- `NO_FORWARD_VALUE`

These labels do not replace `READ`, `ADAPTED`, `DEFERRED`, `REJECTED`,
`NO_NEW_VALUE`, or `BLOCKED_UNREADABLE`. They prevent phase and permission facts
from being mistaken for value findings.

The MPA utility cluster is provisionally
`DEFERRED_HIGH_POTENTIAL_FORWARD_SIGNAL`: its eight files form one evaluation
precursor, not eight independent implementation candidates.

## External-Agent Coding Context Contract

The current capsule already owns task identity, objective, mode, output root,
non-goals, pinned public commit, source repositories, source/owner-overlap Gate
A, design/code/test Gate B, and the authority envelope. The roadmap therefore
extends that owner rather than duplicating it.

Subject to R0 acceptance, build/extend coding tasks must use `PrepareTask` and
carry these additional bounded fields:

| Context group | Required content | Failure prevented |
|---|---|---|
| exact change envelope | allowed paths, protected paths, expected changed set | scope drift and authority-owner edits |
| owner map | current paths, symbols, versions, and competing owners checked | duplicate implementation |
| invariants | must-preserve behavior and explicit forbidden transitions | locally correct but CVF-invalid code |
| verification | exact focused tests, negative cases, deterministic checks, and required outputs | happy-path-only delivery |
| known-defect hints | source-backed prior misses relevant to this task | repeated reviewer corrections |
| return manifest | required code, tests, evidence, unresolved gaps, and manifest delta | ambiguous handback |
| claim/export boundary | public/private drift, credential, provider, commit, push, and publication limits | overclaim or data leakage |
| correction digest | public-safe recurring reviewer corrections with current owner citations | loss of learning between rounds |

Context must remain task-proportional. The generator should emit only fields
applicable to the selected mode, reject stale owner citations, and record a
reason when a context group is not applicable.

## Negative Search And Collision Discipline

This roadmap does not close future owner-search evidence. Each work order must
repeat collision checks against the then-current repository before adding a
capsule field, forward-value label, evaluation owner, metric, or checker.

| Field | Required value for future work orders |
|---|---|
| search roots | `docs governance CVF_SESSION EXTENSIONS scripts .github` plus the eight-file utility source cluster |
| search command or query | `rg -n --fixed-strings "<candidate-token>" docs governance CVF_SESSION EXTENSIONS scripts .github` followed by a targeted symbol search in the selected owner files |
| coverage | owner schemas, generators, validators, tests, roadmaps, registries, source, and return-review evidence |
| absent-versus-collision disposition | classify each result as absent, binding owner, same-token/different-meaning collision, non-authoritative occurrence, or stale owner |

Known collision controls:

- `task capsule` already binds to the existing schema/generator and cannot
  justify a parallel protocol;
- `DEFERRED` and `NO_NEW_VALUE` remain terminal-ledger vocabulary; proposed
  forward-value labels are orthogonal annotations;
- `utility under attack` must be checked against current Memory, Truth,
  retrieval, test, and evaluation owners before a new owner is created;
- any unavailable claimed owner/source receives
  `SOURCE_GAP_WITH_SEARCH_EVIDENCE` with the exact queries and roots searched;
- an absent exact phrase is not evidence that the underlying capability is
  absent under a different name.

## Utility-Under-Attack Three-Gate Route

### Gate UAA-G1 - Contract And Fixture Normalization

Provider use: forbidden.

Normalize the eight files into one CVF-native evaluation specification. Define
ground truth, scoring semantics, denominators, zero-baseline behavior, attack
budget/rate, deterministic seeds, repetitions, corpus/config/code hashes,
latency/token/quota fields, owner, and explicit stop conditions. Validate JSON
and JSONL shape and preserve the source packet as non-authoritative evidence.

Exit: a reviewer can reproduce expected metric calculations from fixtures
without a model call. Stop if the design only restates existing tests or if
the expected information value does not exceed implementation/review cost.

### Gate UAA-G2 - Deterministic Retrieval-Only Harness

Provider use: forbidden.

Bind the normalized scenarios to the actual current store/retrieval seams and
measure retrieval success separately from reader/model correctness. Cover
benign correct untrusted evidence, conflict, staleness, duplicate lineage,
cross-scope isolation, and action-time revalidation. Bounded occupancy remains
an experimental hypothesis, not an accepted defense.

Exit: deterministic evidence shows a material gap or a useful regression
signal not already covered by current owners. Stop on duplicate coverage,
non-reproducibility, or non-positive value after time/latency review.

### Gate UAA-G3 - Conditional Reader/Model/Provider Evaluation

Provider use: conditional and separately authorized.

Open only when UAA-G2 passes, a named owner accepts the result destination, a
fresh GC-018 and work order define budget/quota/latency limits, and the
operator authorizes the run. Retrieval metrics and reader/model accuracy must
remain separate. Any release-quality governance claim requires the real
provider proof mandated by current CVF authority.

Exit: source-backed comparative results with cost, uncertainty, and claim
boundary. No universal threshold or production-security claim follows from a
single run.

## Work Plan

| Tranche | Objective | Allowed output | Blocking exit |
|---|---|---|---|
| EACQ-FV-R0 | external adversarial critique | critique and finding-disposition packet only | operator accepts revised roadmap or stops it |
| EACQ-FV-R1 | formalize forward-value assessment | standard/template/index proposal and negative examples | no status conflation; deferred candidates retain owners and reopen conditions |
| EACQ-FV-R2 | enrich the existing task capsule | schema/generator/docs/tests under a fresh work order | coding modes receive proportional owner/invariant/test context |
| EACQ-FV-R3 | close the reviewer learning loop | correction-digest contract, validator, and return integration | repeated corrections are current, source-backed, and public-safe |
| EACQ-FV-R4 / UAA-G1 | normalize the utility evaluation contract | provider-free schema, fixtures, formulas, and validation | reproducible scoring and explicit stop decision |
| EACQ-FV-R5 / UAA-G2 | build deterministic retrieval evaluation | provider-free harness, tests, receipts, and value decision | distinct useful signal proven or lane stops |
| EACQ-FV-R6 | value/cost checkpoint | independent review and stop/proceed decision | serious, source-backed, non-duplicate value exceeds cost |
| EACQ-FV-R7 / UAA-G3 | optional model/provider evaluation | separately authorized results packet | fresh GC-018, budget, owner, real-provider evidence |
| EACQ-FV-R8 | reconcile and close | index, knowledge-map, session, and export disposition | no parked value or claim boundary is lost |

Each implementation tranche requires its own source verification, baseline,
work order, worker return, independent review, and closure evidence. R0 does
not authorize R1; acceptance of R1 does not authorize R2 or either utility
execution gate.

## Acceptance Criteria

The roadmap may advance beyond design only when:

1. the external critique is fully dispositioned and operator-accepted;
2. the task-capsule plan reuses the existing schema/generator owner;
3. every new context field has a consumer, freshness rule, and measurable
   failure mode;
4. a forward-value second pass is mandatory for all deferred groups and
   sampled/high-risk reject/no-new-value groups;
5. counterfactual acceleration and directional novelty are evaluated without
   promoting speculative ideas to authority;
6. all parked value is indexed or explicitly excluded with reason;
7. UAA-G1 and UAA-G2 remain deterministic and provider-free;
8. UAA-G3 cannot open without a separate value/cost decision and authority;
9. external-agent quality is evaluated against comparable tasks using repair
   count, owner-overlap defects, boundary violations, missing negative cases,
   reviewer time, and context size/latency;
10. no public, runtime, security-effectiveness, or production claim exceeds
    the evidence actually produced.

## Verification / Evidence Plan

External-agent quality comparison must record at least:

- first-return acceptance versus return-for-repair;
- number and severity of reviewer corrections;
- duplicate-owner and protected-path violations;
- required positive and negative tests delivered/passed;
- changed-set/manifest accuracy;
- context bytes or tokens and preparation/review latency;
- source-backed correction recurrence across later tasks.

The comparison is invalid if task difficulty, authority envelope, or expected
outputs differ materially without an explicit adjustment. No provider/model
superiority claim is in scope.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap tranche | Future work-order requirement | Reviewer evidence |
|---|---|---|
| R0 | design-only external critique packet | exact finding disposition and operator decision |
| R1 | governance-design work order | forward-value examples, counterexamples, reopen-index reconciliation |
| R2 | schema/generator implementation work order | fixture validation and backward compatibility |
| R3 | correction-loop implementation work order | leakage review, stale-citation tests, return validation |
| R4 | provider-free evaluation-contract work order | formula and fixture reproducibility |
| R5 | provider-free retrieval-harness work order | deterministic focused tests and cost decision |
| R6 | independent decision review | accepted stop/proceed evidence |
| R7 | fresh live/provider work order | GC-018, budget, secret-safe diagnostic, real-provider receipt |
| R8 | closure work order if needed | registry/session/public-disposition reconciliation |

## Dual Agent Surface Matrix

| Artifact | Worker source view | Reviewer evidence view | Cross-reference |
|---|---|---|---|
| external critique | roadmap plus named current owners | source-backed challenges and classifications | EACQ-FV-R0 |
| task capsule | task-proportional instructions and boundaries | generated capsule, freshness inputs, validation result | EACQ-FV-R2 |
| correction digest | relevant public-safe failure hints | original correction provenance and redaction decision | EACQ-FV-R3 |
| utility contract | normalized formulas and fixtures | source mapping, deterministic recomputation | UAA-G1 |
| retrieval harness | exact store/retrieval seams and scenarios | tests, receipts, distinct-value decision | UAA-G2 |
| provider evaluation | bounded prompt/run contract | live receipt, cost, uncertainty, claim boundary | UAA-G3 |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `## Purpose`; `## Target / Source`; `## Design Control Gate`; `## Work Plan`; `## Acceptance Criteria`; `External absorption core: REQUIRED`; `Mixed-origin derived synthesis: REQUIRED`; `External knowledge intake routing: REQUIRED`; `COMPLETE_VERIFIED`; `RECONCILED_VERIFIED`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | Checker execution is confirmation and durable evidence after direct source read-ahead, not first discovery of required fields or literals. |
| claimBoundary | Read-ahead proves only that applicable checker source and literal contracts were inspected for this roadmap; it does not prove semantic acceptance, implementation, runtime behavior, or closure. |

| Checker | Why it must be read before implementation |
|---|---|
| `governance/compat/check_markdown_structural_completeness.py` | required roadmap/work-order sections and literal headings |
| `governance/compat/check_roadmap_closure_freshness.py` | roadmap authority and closure freshness |
| `governance/compat/check_governed_artifact_checker_read_ahead.py` | checker read-ahead evidence |
| `governance/compat/check_external_absorption_core.py` | manifest/ledger/semantic-review obligations |
| `governance/compat/check_external_absorption_value_conversion.py` | value-conversion lanes and boundaries |
| `governance/compat/check_external_absorption_overlap_discipline.py` | overlap and novelty classification |
| `governance/compat/check_mixed_origin_derived_synthesis_absorption.py` | mixed-origin provenance and authority separation |
| `governance/compat/check_external_knowledge_intake_routing.py` | operator/external critique routing |
| `governance/compat/check_corpus_completeness_report_integrity.py` | corpus completeness claims |
| `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` | mapped/deferred/unmapped reconciliation |
| `governance/compat/check_agent_operation_trace.py` | exact actor, target, changed set, and boundary evidence |
| `governance/compat/check_public_export_disposition.py` | public-export disposition requirements |

## Source Verification Block

| Claim | Source verified | Result |
|---|---|---|
| task capsule already exists | schema, generator `create_capsule`, PowerShell `PrepareTask`, and review README | confirmed; enrichment must reuse current owner |
| current capsule lacks task-specific code context | `CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json` fields | confirmed for protected paths, owner symbols, invariants, test commands, defect digest, and expected changed set |
| deferred candidates require index handling | `CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` Conditional Reopen Index Rule | confirmed |
| semantic review already requires inspection of deferred and high-risk rejected/no-new-value groups | same standard, Reviewer Semantic Value Audit | confirmed; execution did not preserve the MPA candidate in the central index |
| MPA packet contains one eight-file utility cluster | MPA audit and per-file ledger | confirmed: 8 `DEFERRED` files |
| utility cluster has no current CVF result | MPA audit and source packet | confirmed; evaluation value remains unproved |

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | operator-supplied mixed-origin local folder plus current CVF external-agent packet/tooling; no new GitHub source repository |
| Upstream or source-mirror disposition | no mirror required; preserve the local packet as non-authoritative provenance |
| Enumeration or manifest plan | reuse the accepted 50-file MPA manifest and ledger; scope this roadmap to the one eight-file deferred capability cluster |
| Per-file terminal-ledger plan | retain original terminal statuses and add cluster-level forward-value disposition; do not rewrite history |
| Owner or overlap route | existing task capsule/generator, absorption core standard, conditional reopen index, current Memory/Truth/evaluation owners |
| Value-disposition route | task-context enrichment; forward-value doctrine/checker candidate; utility evaluation precursor behind UAA-G1/G2/G3 |
| Claim boundary | design and conditional-reopen preservation only; no implementation, runtime, provider, public, deploy, or production action |

## Mandatory Blind-Spot Control Block

Filename, current authorization, implementation maturity, and terminal status
must not decide forward value. The reviewer must inspect use-case content,
counterfactual acceleration, directional novelty, option value, and the
smallest falsifying proof. A second reviewer must challenge every high-option-
value `DEFERRED` group and a risk-based sample of `NO_NEW_VALUE`/`REJECTED`
groups. Any candidate retained without immediate action must enter the central
conditional reopen index or receive the exact governed no-entry reason.

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/legacy/CVF 13.08/CVF_MEMORY_POISONING_ABSORPTION/04_UTILITY_UNDER_ATTACK/` plus current CVF external-agent review owners |
| Enumeration command | reuse accepted recursive MPA manifest; filter ledger rows to `04_UTILITY_UNDER_ATTACK/` |
| Manifest artifact or inline manifest | `docs/audits/CVF_MPA_AI_T0_LOCAL_MEMORY_POISONING_MANIFEST_2026-08-27.json` |
| Processing ledger artifact or inline ledger | `docs/audits/CVF_MPA_AI_T0_LOCAL_MEMORY_POISONING_FILE_LEDGER_2026-08-27.json` |
| Ledger terminal statuses | allowed: READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE; source corpus actual: READ=8, DEFERRED=8, NO_NEW_VALUE=34; roadmap focus: 8 DEFERRED files as one capability cluster |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE; preserve source terminal status and add provisional `DEFERRED_HIGH_POTENTIAL_FORWARD_SIGNAL` cluster annotation |
| Owner-surface map | task capsule/generator; absorption core; conditional reopen index; future named evaluation owner |
| Unresolved items | no unreadable files; external critique and owner acceptance remain intentionally pending |
| Completion claim boundary | complete roadmap design and candidate preservation, not implementation or evaluation-effectiveness proof |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded reuse of the accepted MPA semantic intake.
- Corpus root: `.private_reference/legacy/CVF 13.08/CVF_MEMORY_POISONING_ABSORPTION/`.
- Snapshot time: 2026-08-27 local session.
- Enumeration command: recursive filesystem-backed `Get-ChildItem -LiteralPath <corpusRoot> -Recurse -Force -File`; reuse only after hash drift check.
- Manifest artifact or inline manifest: `docs/audits/CVF_MPA_AI_T0_LOCAL_MEMORY_POISONING_MANIFEST_2026-08-27.json`.
- Manifest hash: `7bcdc612aaf99e7323de9b1236474c1e9ebf8a6b326d3e19ada649a1b57f9e10`.
- Processing ledger artifact or inline ledger: `docs/audits/CVF_MPA_AI_T0_LOCAL_MEMORY_POISONING_FILE_LEDGER_2026-08-27.json`.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE; semantic dispositions additionally preserve READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE.
- Reconciliation: manifest=50 observed files; ledger_terminal=50 = 8 READ + 8 DEFERRED + 34 NO_NEW_VALUE; exclusions=0; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: none.
- Unreadable or unsupported files: none.
- Aggregation check: all 50 observed files reconcile; all 8 DEFERRED rows reconcile to one utility-under-attack capability cluster.
- Drift check: re-enumerate and compare hashes before any future UAA work order.
- Output traceability: roadmap claims map to the MPA audit, manifest, per-file ledger, and conditional reopen row.
- Adversarial verification: cluster-level aggregation was checked against all eight source files; present non-authorization was not accepted as no-value evidence.
- Corpus verdict: COMPLETE_VERIFIED

## Knowledge System Reconciliation

- Knowledge task class: bounded corpus-to-candidate and owner-map reconciliation.
- Source manifest: `docs/audits/CVF_MPA_AI_T0_LOCAL_MEMORY_POISONING_MANIFEST_2026-08-27.json`.
- Source manifest hash: `7bcdc612aaf99e7323de9b1236474c1e9ebf8a6b326d3e19ada649a1b57f9e10`.
- Enumeration safety: filesystem-backed `Get-ChildItem -LiteralPath <corpusRoot> -Recurse -Force -File` enumeration was accepted; repeat it before execution.
- Intake registry or ledger: `docs/audits/CVF_MPA_AI_T0_LOCAL_MEMORY_POISONING_FILE_LEDGER_2026-08-27.json` and the MPA conditional reopen index row.
- Authority assets: current task-capsule/generator, absorption core, Memory, Truth, and EAFR owners named in Source Verification.
- Derived views: this roadmap and the conditional reopen index are non-authoritative derived planning views until reviewed.
- Semantic region ledger: MPA audit groups 50 files into provenance/control, three existing-owner conceptual clusters, and one eight-file utility evaluation cluster.
- Region reconciliation: assets=50; mapped=42; deferred=8; unmapped=0.
- Orphan or unmapped assets: none.
- Cross-region links: the deferred utility cluster links Memory/Truth risk owners to the future evaluation owner without transferring runtime authority.
- Drift check: PASS
- Rebuildability check: reproducible from the manifest, per-file ledger, audit group IDs, and conditional reopen row.
- Retrieval boundary: roadmap and index improve discovery only; they are not runtime retrieval, truth, or evaluation evidence.
- Adversarial verification: the operator-raised counterfactual was tested against current standards and exposed a missing required index entry; the 34 overlap files remain closed as implementation candidates.
- Knowledge-map verdict: RECONCILED_WITH_DECLARED_GAPS

| Category | Count | Disposition |
|---|---:|---|
| mapped existing-owner files | 42 | 8 provenance/control READ plus 34 NO_NEW_VALUE remain mapped by the MPA audit |
| deferred files | 8 | one utility evaluation precursor, now indexed with three gated reopen stages |
| unmapped files | 0 | none |

Reconciliation: 42 mapped + 8 deferred + 0 unmapped = 50 manifest files.

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| missed forward-value review lesson | terminal disposition can hide counterfactual and directional value | `DOCTRINE_ADAPTED` | future absorption semantic-review control | R0 critique, then R1 design | no runtime |
| task-capsule enrichment | exact owner/invariant/test/correction context may reduce repair | `PACKAGE_CANDIDATE` | existing task-capsule schema/generator | R2 only after design acceptance | no competing package |
| utility-under-attack evaluation | provider-free normalization and retrieval evaluation | `RUNTIME_CANDIDATE` | future named evaluation owner | UAA-G1 then UAA-G2 | no provider in G1/G2 |
| forward-value enforcement | missing index/second-pass evidence can be checked deterministically | `CHECKER_CANDIDATE` | future `governance/compat` work order | R1 must first prove enforceable literals and negative cases | no checker wiring now |
| mixed-origin packet implementation/prose | useful evidence does not transfer authority | `REJECT_DIRECT_IMPORT` | CVF-native owners only | source-verify and rewrite only if authorized | no direct import |
| 34 already-owned files | independent convergence validates context quality but adds no current owner delta | `NO_PACKAGE_OR_RUNTIME_VALUE` | Memory/Truth/EAFR owners | use only as quality evidence; no duplicate work | no runtime/package |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| external task capsule | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json`; `scripts/external_agent_packet.py`; `scripts/Update-CVF-External-Agent-Packet.ps1` | ENRICH_EXISTING | task-specific code-owner, invariant, verification, and correction context is absent | extend current owner after R0 |
| ordinary semantic value audit | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | ENRICH_EXISTING | required review exists, but forward/counterfactual value and index evidence were missed in MPA closeout | formalize second pass and negative proof |
| MPA Memory/Truth concepts | `docs/audits/CVF_MPA_AI_T0_LOCAL_MEMORY_POISONING_ABSORPTION_AUDIT_2026-08-27.md`; Memory/Truth/EAFR owners cited there | CONFIRMED_EXISTING | independent rediscovery evidences external-agent alignment, not a new implementation need | retain as quality signal |
| utility-under-attack cluster | OWNER_SURFACE_NOT_FOUND; `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` previously had no MPA row | NEW_FINDING | coherent evaluation precursor separates utility preservation from blocking | preserve and apply UAA gates |
| direct packet code/prose | existing governed `AGENTS.md`; current authority hierarchy | REJECT_DIRECT_IMPORT | mixed-origin source cannot self-authorize | CVF-native design only |

## Mixed-Origin Derived Synthesis Provenance

| Input or concept | Origin class | Evidence basis | Claim type | Validation method | Current CVF owner | Disposition |
|---|---|---|---|---|---|---|
| external coding-quality proposal | NOVEL_SYNTHESIS | current packet tooling and observed intake/review experience | roadmap design | R0 external critique and later controlled comparison | existing capsule/generator | REVIEW_REQUIRED |
| forward-value correction | OPERATOR_AGENT_CO_DESIGNED | operator identified the overlooked value; current standard/index prove the gap | governance correction | source verification and index repair | absorption core/index | ADAPT_PENDING_REVIEW |
| utility evaluation precursor | OPERATOR_AGENT_CO_DESIGNED | eight-file local packet cluster | evaluation design | G1 normalization and G2 deterministic proof | future named evaluation owner | DEFERRED_HIGH_POTENTIAL_FORWARD_SIGNAL |
| current CVF facts | MIXED_ORIGIN | exact current paths and source | current-state claim | direct repository inspection | named current owners | ACCEPT_WITH_BOUNDARY |

## Absorption Decision Vector

| Decision axis | Decision | Evidence | Cost boundary |
|---|---|---|---|
| Knowledge absorption | ADAPT_PENDING_REVIEW | forward-value miss and task-context gaps are source-backed | R0 first; no implementation |
| Direct import | REJECT | mixed-origin packet is non-authoritative | CVF-native rewrite only |
| Runtime activation | DEFER | utility value lacks CVF execution evidence | G1/G2 provider-free before G3 |
| Authority promotion | DEFER | roadmap awaits external critique and operator decision | no automatic promotion |

## System-Chain Value Review

| Chain component | Evidence path | Existing CVF owner/gap | Value disposition | Readiness disposition | Next action |
|---|---|---|---|---|---|
| external-agent task preparation | task-capsule schema/generator/wrapper | owner exists; code-specific context gap | ENRICH_EXISTING | design unreviewed | R0 then R2 |
| external return/reviewer loop | external-agent return contract and reviews | correction learning is not task-capsule input | FORWARD_DESIGN_SIGNAL | owner decision needed | R0 then R3 |
| absorption semantic review | absorption core standard | rule exists; forward-value/index execution gap | DOCTRINE_ADAPTED | design proposal only | R1 |
| utility evaluation | eight deferred files | no named current evaluation result owner | EVALUATION_PRECURSOR | provider-free proof absent | G1 then G2 |
| live reader/model evaluation | future provider work order | deliberately unopened | OPTION_VALUE_PRESERVED | blocked by G2/value/budget | conditional G3 |

## Absorption Efficiency And Provenance Reuse

manifestLedgerReuse: REUSE_IF_FRESH

semanticReviewUnit: CAPABILITY_CLUSTER

defaultValuePosture: PRESERVE_UNTIL_CONTRADICTED

additionalValueProbe: SKIP_UNLESS_NAMED_GAP

latencyBudget: SINGLE_PASS_BOUNDED

intakePriority: LOCAL_SYNTHESIZED_PACK_FIRST

localSemanticInspection: FILE_AND_USE_CASE_CONTENT_REQUIRED

mappingAction: DIRECT_WORK_ORDER_FOR_HIGH_FIT_CLUSTERS

deliverySequence: WORK_ORDER_THEN_WORKER_THEN_INDEPENDENT_REVIEWER

namePatternInference: FORBIDDEN_AS_VALUE_DISPOSITION

upstreamConsultation: TARGETED_FOR_PROVENANCE_OR_GAP

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator correction -> roadmap design -> external adversarial review -> operator disposition -> bounded work orders |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; external absorption guards |
| Owner surface | this roadmap plus the existing task-capsule and conditional-reopen owners |
| Disposition | ADAPT into a proposed context-quality contract and forward-value review gate |
| Claim boundary | design proposal only; no implementation, runtime, provider, public, or production authority |

## Finding-To-Governance Learning

| Finding | Defect class | Learning lane | Proposed disposition |
|---|---|---|---|
| MPA deferred cluster was not entered in the required central reopen index | RULE_GAP in execution evidence, despite an existing prose rule | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED for a deterministic closeout check after R0/R1 |
| maturity/authorization was allowed to dominate forward-value interpretation | REVIEW_REASONING_GAP | GOVERNANCE_CONTROL_PLANE | add explicit counterfactual, directional, and option-value questions |
| external coding context is generic where task-specific owner/test context is needed | CONTEXT_CONTRACT_GAP | AGENT_EXECUTION_PLANE | enrich the existing capsule and measure repair reduction |

## Epistemic Process Block

Expected Result / Prediction: richer but proportional task context will reduce
first-return repair and owner/boundary defects; an explicit forward-value
second pass will preserve high-option-value ideas without inflating them into
implementation authority.

Evidence Comparison: not yet run. The MPA audit proves a concrete index and
review-execution miss, while the current capsule schema proves the proposed
task-specific fields are absent. Causal quality improvement remains unproved.

Contradiction Or Gap Disposition: R0 must identify context-bloat, stale-owner,
speculation, and non-enforceable-checker failure modes. Later comparison stops
or revises the design if repair cost, latency, or defect rate does not improve.

Claim Update: roadmap proposed; no external-agent quality uplift or utility-
under-attack effectiveness is claimed.

## Fail Conditions

Stop or return for redesign if:

- the external reviewer identifies an unresolved authority or owner conflict;
- capsule additions have no named consumer or freshness rule;
- forward-value labels collapse into novelty scoring without source evidence;
- a deferred candidate lacks an objective reopen condition;
- UAA-G1 cannot define reproducible formulas and ground truth;
- UAA-G2 cannot bind to current retrieval seams or adds only duplicate tests;
- the expected value no longer exceeds time, latency, review, or quota cost;
- any tranche requires provider, public, deployment, or production authority
  outside its explicit work order.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex roadmap-author role |
| Provider or surface | local private-provenance workspace |
| Session or invocation | EACQ-FV roadmap design, 2026-08-27 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | direct governed-file reads, `rg`, `git`, and `apply_patch` |
| Target paths | this roadmap and the conditional reopen index |
| Allowed scope source | operator instruction to design both upgrades and request external critique before execution |
| Before status evidence | clean worktree at `19c223ce06d579cfe16fb7feb4ff8996363797ab` |
| After status evidence | roadmap proposed; MPA utility cluster preserved in the central index; implementation remains closed |
| Diff evidence | exact two-path material diff before commit |
| Approval boundary | roadmap and preservation repair only |
| Claim boundary | no code implementation, benchmark execution, provider call, public sync, deployment, or production claim |
| Agent type | dispatcher/source reviewer |
| Invocation ID | `eacq-fv-roadmap-design-2026-08-27` |
| Expected manifest | roadmap plus conditional reopen index |
| Actual changed set | roadmap plus conditional reopen index |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

The roadmap has not completed external critique or operator acceptance and is
not yet eligible for public export.

## Claim Boundary

This artifact proposes a review-first roadmap and preserves one deferred
candidate cluster. It does not prove improved external-agent coding quality,
authorize any implementation, execute the utility benchmark, establish a
security threshold, call a provider, modify public artifacts, deploy, or make
a production-readiness claim.
