# CVF GC-018 Baseline - External Findings Intake Archive Hygiene

Memory class: SUMMARY_RECORD

Status: ACCEPTED

docType: baseline

Date: 2026-08-25

Batch ID: EXTERNAL-FINDINGS-INTAKE-ARCHIVE-HYGIENE

Decision owner: operator through explicit 2026-08-25 orchestrator authority

Reviewer owner: current independent orchestrator/reviewer

## Purpose

Preserve four external-findings intake documents byte-for-byte as historical
text while preventing them from being treated as active governed Markdown.
Also classify the existing ignored `logs` runtime root so the repository
lifecycle gate reflects the already-declared `.gitignore` boundary.

## Scope

Allowed paths:

- `docs/reviews/archive/CVF_EXTERNAL_AGENT_FINDINGS_INDEPENDENT_ADVERSARIAL_REVIEW_2026-08-25.md.txt`
- `docs/reviews/archive/CVF_EXTERNAL_AGENT_FINDINGS_REMEDIATION_PROPOSAL_2026-08-25.md.txt`
- `docs/reviews/archive/CVF_EXTERNAL_AGENT_FINDINGS_VERIFICATION_REPORT_2026-08-25.md.txt`
- `docs/reviews/archive/CVF_EXTERNAL_AGENT_FINDINGS_VERIFICATION_REPORT_CORRECTED_2026-08-25.md.txt`
- `docs/baselines/CVF_GC018_EXTERNAL_FINDINGS_INTAKE_ARCHIVE_HYGIENE_2026-08-25.md`
- `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json`

Forbidden paths:

- all runtime source and tests
- all session-continuity surfaces
- all other governance checkers and registries
- all public-sync surfaces

Operator authorization: the operator authorized the current orchestrator to
act fully on their behalf while preserving CVF rules and prioritizing these
findings before the parked roadmap.

Rollback boundary: revert only this archive-hygiene batch if rejected; do not
alter or revert any previously accepted RFR closure.

## Evidence

The four archived `.md.txt` files preserve the SHA-256 values measured before
the move. Their content remains advisory and `NOT_CVF_SOURCE`. The `logs` root
contains ignored capability-owner database runtime state and is already
covered by `.gitignore`; adding it to `ignoredRoots` makes the lifecycle
registry match that existing boundary without deleting runtime evidence.

## Source Evidence

| Source | Verification | Disposition |
| --- | --- | --- |
| `.gitignore` | lines 39-41 already ignore capability-owner database files under `logs/` | ACCEPT |
| `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json` | `logs` was absent from `ignoredRoots` before this batch | ACCEPT |
| four archived intake files | pre-move and post-move SHA-256 values match | ACCEPT_AS_HISTORY_ONLY |

## Baseline Decision

`ACCEPT_ARCHIVE_HYGIENE`: retain exact advisory bytes with `.md.txt` suffix and
classify `logs` as an ignored runtime root. No advisory claim is absorbed as
authority by this decision.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_repository_lifecycle_classification.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `Core Guard Self-Protection Authorization`; `ignoredRoots`; `External Knowledge Intake Routing`; baseline structural headings |
| gateRunPurpose | confirm and record evidence for the pre-authored archive and protected-registry repair shape; not first discovery |
| claimBoundary | checker conformance does not validate the archived external claims |

## External Knowledge Intake Routing

Canonical chain map:
`docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`

| Field | Value |
| --- | --- |
| Chain map | CVF external knowledge absorption chain |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | archive as historical input; derive governed remediation only from independently verified CVF sources |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | independent orchestrator/reviewer and subsequent governed roadmap/work orders |
| Disposition | NOT_CVF_SOURCE; HISTORY_ONLY |
| Claim boundary | archive retention is not factual acceptance, remediation closure, or runtime proof |

## Rescan Intelligence Hardening

- Original source artifact: four operator-provided external-findings files
- Predecessor intake artifact: N/A with reason - these files entered as untracked advisory material
- Delta ledger status: COMPLETE for archive/hygiene disposition only
- Routing matrix status: COMPLETE for the bounded remediation sequence
- Semantic sampling status: COMPLETE for the decisive provenance fail-open claim
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Category | Disposition |
| --- | --- |
| UNCHANGED_FROM_INTAKE | source bytes and hashes preserved |
| CHANGED_DISPOSITION | active review candidates reclassified as historical `NOT_CVF_SOURCE` text |
| NEW_FINDING | `logs` lifecycle registry drift found by the hook chain and repaired in this batch |
| REMOVED_OR_REJECTED | authority status of advisory prose rejected; no source evidence removed |

### Follow-Up Routing Matrix

| Lane | Routing |
| --- | --- |
| DO_NOW | archive hygiene and `logs` ignored-root alignment |
| SEPARATE_RUNTIME_TRANCHE | AIF provenance fail-closed remediation |
| STRATEGIC_OPERATOR_DECISION | any later live/provider proof or public export |
| OUT_OF_SCOPE | unrelated runtime and the parked RFR roadmap |
| RESOLVED_BY_DESIGN | archive suffix prevents active governed-Markdown admission |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| EAF-HYG-01 | corrected report AIF finding | omitted provenance can be admitted | compared against current AIF source and tests | advisory wording cannot substitute for current runtime evidence | route to separate source-verified runtime tranche |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add only `logs` to the existing
`ignoredRoots` array; no checker logic or lifecycle class changes are allowed.

Protected paths:

- `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json`

Operator authorization: explicit 2026-08-25 delegation of full orchestrator
authority, bounded by CVF rules and this exact hygiene repair.

Rollback boundary: revert only the `logs` ignored-root entry and this
authorization artifact if rejected; preserve the archived source bytes and all
prior accepted commits.

## Scope Firewall Authorization

Allowed paths:

- `docs/reviews/archive/CVF_EXTERNAL_AGENT_FINDINGS_*.md.txt`
- `docs/baselines/CVF_GC018_EXTERNAL_FINDINGS_INTAKE_ARCHIVE_HYGIENE_2026-08-25.md`
- `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json`

Forbidden paths:

- `EXTENSIONS/`
- `CVF_SESSION/`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF*.md`
- `public/`

Operator authorization: explicit operator delegation recorded on 2026-08-25.

Rollback boundary: this batch only; no rollback across the accepted parent
HEAD `416a38bf159cea0105234f307fffd94d8bf5ac0c`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance history and local runtime-root classification only.

## Claim Boundary

This baseline preserves advisory history and repairs repository classification.
It does not accept the archived claims as CVF authority, close any finding,
authorize runtime implementation, run provider/live proof, use credentials,
publish, push, or make a production-readiness claim.
