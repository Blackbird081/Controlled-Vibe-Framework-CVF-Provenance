# CVF RSPB-AI-T0 Mixed-Origin Corrective Reassessment

Memory class: FULL_RECORD

Status: CORRECTED_PROCEED_SELECTIVELY_RUNTIME_STAGED

docType: assessment

Date: 2026-08-16

Supersedes decision only: `STOP_COST_EXCEEDS_VALUE` in
`docs/audits/CVF_RSPB_AI_T0_DUAL_CORPUS_INTAKE_AUDIT_2026-08-15.md`.

The prior manifests, hashes, file counts, upstream safety rejection, and
no-execution evidence remain valid.

Mixed-origin derived synthesis: REQUIRED

## Purpose

Correct the semantic value decision while preserving verified corpus evidence.

## Scope / Target / Owner Boundary

Scope is the prior RSPB decision and local-ledger provenance/value fields.
Owners are the external absorption SOT and named current CVF surfaces. No
runtime owner is created here.

## Source / Predecessor Evidence

The predecessor audit, two manifests/ledgers, local master design, operator
provenance clarification, and current environment-blocker worker returns form
the evidence set.

## Corrective Finding

The previous intake made a category error. It treated the 205-file local pack
as a secondary proposal whose absence from current owner paths demonstrated
low value, then combined that result with 448 rejected upstream security files
and the cost of full runtime implementation. The operator has now established
that the pack was produced from the pinned upstream, public CVF input,
operator requirements, and operator-agent design. It is a provenance-backed
derived synthesis candidate, not upstream authority and not baseless output.

## Mixed-Origin Derived Synthesis Provenance

artifactClass: PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE

authorityStatus: NON_AUTHORITATIVE_UNTIL_REVIEWED

| Input or concept | Origin class | Evidence basis | Claim type | Validation method | Current CVF owner | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| upstream routing, tool inventory, and unsafe auto-bootstrap patterns | UPSTREAM_REPOSITORY_BACKED | pinned mirror `dd7c50dc38e778373cd037b3f47d5e132ef43a2f`; prior 559-file manifest | upstream facts | pinned source paths and prior ledger | external absorption core and ASSF | retain prior ADAPT/REJECT results |
| CVF authority, work-order, owner, and fail-closed constraints | CVF_PUBLIC_DERIVED | local README owner map and operator attestation that public CVF was supplied | design input | reconcile against current governed owners | Work Order, Guard Contract, ASSF, Execution Plane | REVIEW_PER_OWNER |
| controlled preflight/bootstrap outcome | OPERATOR_REQUIREMENT | operator clarification on 2026-08-16 plus local lifecycle definition | requirement | operator confirmation and owner review | Execution Plane and Work Order | ACCEPT_AS_REQUIREMENT |
| composed profile, contracts, policies, fixtures, and staged implementation | OPERATOR_AGENT_CO_DESIGNED | local README, contracts, schemas, policies, fixtures, roadmap/review scaffolds | derived design | rationale/invariant/system-chain review | mapped existing owners | PROCEED_SELECTIVELY |
| capability environment snapshot and transaction semantics | MIXED_ORIGIN | upstream tool-index pattern plus CVF authority separation and new TTL/receipt design | synthesis | contract/schema/fixture review then tests | Execution Plane, ASSF, Guard Contract | HIGH_VALUE_CANDIDATE |

## Absorption Decision Vector

| Decision axis | Decision | Evidence | Cost boundary |
| --- | --- | --- | --- |
| Knowledge absorption | PROCEED_SELECTIVELY | coherent lifecycle, owner map, contracts, schemas, policies, positive/negative fixtures; known environment blockers | cost of owner reconciliation and CVF-native adaptation only |
| Direct import | REJECT_DIRECT_IMPORT | upstream contains domain-specific offensive-security and safety-bypass behavior; local paths are not current owner paths | no upstream or bulk local copy |
| Runtime activation | STAGED_NOT_YET_AUTHORIZED | candidate runtime is unproven; no selected minimal implementation work order exists | evaluate read-only snapshot separately from mutating acquisition |
| Authority promotion | REVIEW_REQUIRED_PER_OWNER | derived synthesis is non-authoritative until each selected artifact is reconciled | promotion cost only for selected owner surfaces |

The former whole-tranche stop is invalid. The corrected result is
`PROCEED_SELECTIVELY`: retain the upstream direct-import rejection, promote
the local knowledge/contract system selectively, and stage runtime by value
and risk.

## Baseline Decision / Proposed Tranche

`PROCEED_SELECTIVELY`. Next candidate is documentation/contract owner
reconciliation followed by a separately authorized read-only environment
snapshot value probe. Mutating acquisition remains parked.

## System-Chain Value Review

| Chain component | Evidence path | Existing CVF owner/gap | Value disposition | Readiness disposition | Next action |
| --- | --- | --- | --- | --- | --- |
| profile and invariants | local `docs/reference/capability_preflight_bootstrap/README.md` | cross-owner profile gap | ADAPT_CANDIDATE_HIGH | coherent design, not canonical | create CVF-native profile reference |
| route/readiness contracts | local `contracts/` and `schemas/` | ASSF/Execution Plane seams | ADAPT_CANDIDATE_HIGH | schema review needed | reconcile fields with current owners |
| Capability Environment Snapshot | local snapshot contract/schema/policy/fixtures | Execution Plane freshness/readiness gap | RUNTIME_CANDIDATE_HIGH | read-only slice plausible | open smallest read-only value probe |
| controlled acquisition | local plan/approval/acquisition receipt contracts and policies | Work Order plus Execution Plane | RUNTIME_CANDIDATE_CONDITIONAL | mutating and supply-chain sensitive | keep separate from snapshot; require explicit operator authorization |
| repair, integrity, secret, and stale-state checks | local policies plus invalid fixtures | checker owners | CHECKER_CANDIDATE | depends partly on selected runtime contracts | adapt fixtures with owner-specific checker scope |
| CLI/MCP/Web projections | local adapter and interaction candidates | existing adapter/Web owners | DEFER_DEMAND_GATED | no direct import and no transport selected | revisit only after internal owner seam |
| review, freeze, learning | local review/freeze/learning contracts | existing governance owners | DOCTRINE_ADAPT_CANDIDATE | no runtime dependency | reuse current owners, avoid parallel authority |

## Current Consumer And Blocked-Workflow Evidence

The prior statement that no concrete blocked workflow existed was incomplete.
Repository evidence records recurring environment-readiness failures:

- `docs/reviews/CVF_CADP_AI_T6_LIVE_COMPATIBILITY_PROOF_WORKER_RETURN_2026-08-15.md`
  lines 74-105: `npm`/`npx`, node modules, and browser prerequisites blocked
  the release path before a provider call;
- its Finding-To-Governance section explicitly proposes dispatch-time
  environment preflight;
- T6-R2 later records a missing Playwright browser binary even after the
  Node/npm/npx prerequisite was repaired.

These are named blocked workflows and current operator-visible outcomes. They
do not prove that the 205-file implementation should be copied or that a full
acquisition runtime is justified. They do prove non-zero current value for a
bounded Capability Environment Snapshot/preflight seam.

## Corrected Ledger Semantics

The 205-row local ledger retains file-processing counts (`192 DEFERRED`, `10
REJECTED`, `3 READ`) because no bulk owner promotion occurs in this corrective
tranche. It now declares `MIXED_ORIGIN`, the non-authoritative artifact class,
separate value dispositions, owner surfaces, and readiness dispositions. Thus
`DEFERRED` means valuable conversion is parked or staged; it no longer means
the file lacks value because it is outside current paths.

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | pinned reverse-skill mirror plus local preflight derived synthesis |
| Enumeration command | prior `git ls-files -z` and `rg --files --hidden --no-ignore -g '!.git/**'` evidence reused |
| Manifest artifact or inline manifest | `docs/audits/CVF_RSPB_AI_T0_REVERSE_SKILL_UPSTREAM_MANIFEST_2026-08-15.json`; `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_MANIFEST_2026-08-15.json` |
| Processing ledger artifact or inline ledger | `docs/audits/CVF_RSPB_AI_T0_REVERSE_SKILL_UPSTREAM_FILE_LEDGER_2026-08-15.json`; corrected local proposal ledger |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline provenance and system-chain tables |
| Unresolved items | 0 file-processing rows; selected owner promotion remains future governed work |
| Completion claim boundary | semantic correction; no new full scan or runtime activation |

## Corpus Completeness And Report Integrity

- Corpus task class: corrective semantic review over prior dual-corpus intake.
- Corpus root: prior pinned upstream plus local preflight folder.
- Snapshot time: prior 2026-08-15 inventory, corrected 2026-08-16.
- Enumeration command: prior filesystem-backed `git ls-files -z` and `rg --files --hidden --no-ignore`.
- Manifest artifact or inline manifest: two JSON manifests cited above.
- Manifest hash: upstream `74ef4330d09afd04c52a8326a96132db490d62d06b823b2d97daf6fbabb6bbb4`; local `c51ed5055ee436a2f6fc20b03fd75b51bb23e3d180d40f5c482d15c36725feac`.
- Processing ledger artifact or inline ledger: two JSON ledgers cited above.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=764; ledger_terminal=764; exclusions=0; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: none.
- Unreadable or unsupported files: none.
- Aggregation check: 559 upstream plus 205 local equals 764.
- Drift check: no membership-freshness claim; correction changes semantic fields only.
- Output traceability: tables cite source paths and prior ledgers.
- Adversarial verification: preserved upstream safety rejection; challenged value/maturity, decision-axis, cost-scope, and system-chain errors.
- Corpus verdict: COMPLETE_VERIFIED

## Rescan Intelligence Hardening

- Original source artifact: pinned reverse-skill mirror plus local Capability Preflight & Bootstrap folder.
- Predecessor intake artifact: `docs/audits/CVF_RSPB_AI_T0_DUAL_CORPUS_INTAKE_AUDIT_2026-08-15.md`.
- Delta ledger status: COMPLETE; UNCHANGED_FROM_INTAKE=559; CHANGED_DISPOSITION=205; NEW_FINDING=0; REMOVED_OR_REJECTED=0.
- Routing matrix status: COMPLETE; DO_NOW=1; SEPARATE_RUNTIME_TRANCHE=2; STRATEGIC_OPERATOR_DECISION=1; OUT_OF_SCOPE=1; RESOLVED_BY_DESIGN=1.
- Semantic sampling status: COMPLETE; local design, environment blockers, and upstream rejection checked.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Count | Evidence disposition |
| --- | ---: | --- |
| UNCHANGED_FROM_INTAKE | 559 | upstream processing/value evidence retained |
| CHANGED_DISPOSITION | 205 | local rows gain origin, authority, value, owner, and readiness fields |
| NEW_FINDING | 0 | correction creates no new corpus file |
| REMOVED_OR_REJECTED | 0 | no file removed; prior direct-import rejection retained |

### Follow-Up Routing Matrix

| Routing lane | Count | Governed route |
| --- | ---: | --- |
| DO_NOW | 1 | SOT and semantic ledger correction in MODS-T0 |
| SEPARATE_RUNTIME_TRANCHE | 2 | read-only snapshot first; mutating acquisition remains separate |
| STRATEGIC_OPERATOR_DECISION | 1 | any acquisition authority expansion |
| OUT_OF_SCOPE | 1 | direct upstream or bulk-local import |
| RESOLVED_BY_DESIGN | 1 | split decisions replace whole-tranche verdict |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| R1 | local README lifecycle | coherent system chain has CVF value | CHANGED_DISPOSITION | evaluated composition rather than file maturity | PROCEED_SELECTIVELY |
| R2 | CADP T6 worker return | no blocked workflow exists | CHANGED_DISPOSITION | found npm/npx/browser prerequisite blockers | snapshot value supported |
| R3 | upstream safety chain | direct repository behavior is safe to import | UNCHANGED_FROM_INTAKE | reread retained high-risk evidence | REJECT_DIRECT_IMPORT |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| profile/lifecycle/owner map | cross-owner preflight doctrine | DOCTRINE_ADAPTED | new corrective assessment and future profile owner | materialize selected profile | docs first |
| contracts/schemas/policies | reusable package contract set | PACKAGE_CANDIDATE | ASSF, Guard Contract, Work Order, Execution Plane | owner reconciliation | no package activation |
| environment snapshot | read-only readiness evidence | RUNTIME_CANDIDATE | Execution Plane | bounded value probe | no scanner now |
| invalid fixtures | fail-closed test vocabulary | CHECKER_CANDIDATE | owner-specific guard | adapt after contract selection | no wiring now |
| upstream/local executable implementations | unsafe or noncanonical direct code | REJECT_DIRECT_IMPORT | CVF-native owners | rewrite selected behavior only | no execution/import |
| pure duplicate scaffolds | accounting/process evidence | NO_PACKAGE_OR_RUNTIME_VALUE | existing governance owners | retain only as provenance evidence | no runtime/package |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| two-stage routing | `docs/reference/agent_system_skills/README.md` | ENRICH_EXISTING | readiness-aware candidate evidence | reconcile, do not duplicate resolver |
| snapshot/readiness | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/` | NEW_FINDING | TTL/freshness-bound capability environment evidence | bounded read-only probe |
| acquisition approval | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | ENRICH_EXISTING | plan-digest, receipt, repair-stop transaction | park mutating slice |
| external adapters | `docs/reference/mcp_gateway/README.md` | REJECT_DIRECT_IMPORT | projections may later consume accepted contracts | demand-gated |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | pinned upstream plus mixed-origin synthesis -> claim-specific evidence -> split decisions -> system-chain review -> selective owner promotion |
| Matching local-view guard | `governance/compat/check_mixed_origin_derived_synthesis_absorption.py` plus external absorption guards |
| Owner surface | this assessment and named current owners |
| Disposition | PROCEED_SELECTIVELY |
| Claim boundary | no direct import or runtime activation |

## Epistemic Process Block

Expected Result / Prediction: applying the new SOT should preserve the valid
upstream safety rejection while recovering local system-chain value.

Evidence Comparison: the result does so and identifies current environment
blockers missed by the former consumer search.

Contradiction Or Gap Disposition: runtime effectiveness remains unproven;
therefore runtime is staged rather than accepted.

Claim Update: whole-tranche stop is superseded by selective absorption.

## Evidence / Verification

Evidence is the corrected 205-row ledger, source-backed decision/system-chain
matrices, passing new guard tests, and the MODS-T0 governance gates.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance correction; no public-sync action authorized.

## Claim Boundary

No source code was executed or imported. This assessment authorizes no
runtime, package activation, provider/live call, public sync, deployment, or
production use.
