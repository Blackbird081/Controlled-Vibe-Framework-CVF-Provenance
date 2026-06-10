# CVF GC-018 DSCP-T10 Domain Profile And Scan Adapter Contract Baseline

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-10

---

## Authorization

Authorized by operator instruction on 2026-06-10: the local product
`Policy_Local` uses CVF scan and memory rules, but today the practical rules are
still tuned to Vietnamese policy/legal scanning; CVF must continue raising the
foundation so the scan and memory layer can serve multiple domains.

Active state:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

## Decision

Open DSCP-T10 as a bounded domain-profile contract tranche.

The next CVF foundation step is not to make Policy_Local a permanent special
case. The next step is to define and test a domain-agnostic profile layer that
lets a product or corpus declare its language, source family, facet schema,
domain gate keys, boundary rules, and escalation/freshness behavior before scan
and memory packaging.

## Purpose

DSCP-T1 through DSCP-T9 proved a domain-agnostic governed context pack surface,
artifact descriptor helper, ECO adapter, LPF adapter, receipt helper, and local
pipeline harness. DSCP-T10 adds the missing profile boundary so Policy_Local can
be one profile among many, not the implicit owner of the scan/memory method.

## Predecessor Evidence

| Predecessor | Closure evidence | Disposition |
|---|---|---|
| DSCP-T9 local pipeline harness | `docs/reviews/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_COMPLETION_2026-06-08.md`; material commit `5c90506a` | ACCEPT |
| DSCP-T6 descriptor helper | `docs/reviews/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_COMPLETION_2026-06-08.md`; closure commit `13cc1505` | ACCEPT |
| DSCP-T7 ECO adapter | `docs/reviews/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_COMPLETION_2026-06-08.md`; closure commit `958f8d2b` | ACCEPT |
| DSCP-T8 LPF adapter | `docs/reviews/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_COMPLETION_2026-06-08.md`; closure commit `e96aacaf` | ACCEPT |

## External Product Evidence Digest

External product path:

`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local`

This path is evidence input only. It is not source authority for CVF runtime
contracts, and it must not appear in Source Verification as a repo-owned source
file.

| External artifact | Observed role | sha256 | Evidence note |
|---|---|---|---|
| `scripts/policylocal-docx-extract-classify.py` | PolicyLocal extraction/classification script | `sha256:c1699f4bcb36eb4523605fb0e2f2baacfb83a5838f910100f9f3ca53ddecbbb8` | Uses legal/policy fields such as jurisdiction and authority level |
| `scripts/policylocal-docx-deep-scan.py` | PolicyLocal deep scan script | `sha256:ab2d0045f2e6e271a9060a86c3895e08ee5ff9a1361533bff3814f0279383100` | Carries PolicyLocal legal effective-date deep-scan logic |
| `scripts/policylocal-chunk-generator.py` | PolicyLocal chunking script | `sha256:77fd13ba3397b6fdaca32e4246a85598117891fa754f05f243884fd5a2699602` | Uses Vietnamese legal article-boundary chunking |
| `scripts/policylocal-search-runtime.py` | PolicyLocal local search runtime | `sha256:7b1ec0f74f8578a46dd4a7419fe1478cb5c490d38b60853d2e137728a5c11b78` | Uses `VN_NATIONAL` and EC-01 through EC-04 legal escalation gates |

## Scope / Target / Owner Boundary

In scope:

- Add a deterministic local DSCP domain-profile source contract.
- Add focused CPF tests for at least three profile families:
  - PolicyLocal/Vietnamese legal-policy;
  - internal company documentation;
  - technical/project documentation.
- Add a helper that applies a profile to `GovernedArtifactDescriptorInput`
  metadata and `customGates` without hard-coding legal/policy fields.
- Export the new source contract through the existing CPF barrel structure.
- Register the new source and test paths in GC-051 JSON and Markdown registry
  surfaces.
- Create a worker return packet.

Out of scope:

- No edits to the external `Policy_Local` workspace.
- No corpus ingestion, OCR, body extraction, vector retrieval, semantic search,
  provider calls, API keys, public-sync, T12 authoring, current-law claim,
  legal advice quality claim, hosted readiness, production readiness, or public
  readiness.

## Source Verification Summary

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: DSCP governance gate set has `customGates` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 13-25 | `customGates` | `GovernanceGateSet` | ACCEPT |
| EXISTS: DSCP artifact descriptor has open `metadata` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 31-50 | `metadata` | `GovernedArtifactDescriptor` | ACCEPT |
| EXISTS: artifact descriptor builder accepts `metadata` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts` | lines 11-18 | `metadata` | `GovernedArtifactDescriptorInput` | ACCEPT |
| RUNTIME_BEHAVIOR: descriptor builder preserves supplied metadata | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts` | lines 50-57 | `buildGovernedArtifactDescriptor` | `GovernedArtifactDescriptorResult` | ACCEPT |
| EXISTS: ECO adapter builds governed pack request from RAG result | `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/dscp.eco.adapter.ts` | lines 19-35 | `buildECOGovernedPackRequest` | `GovernedContextPackRequest` | ACCEPT |
| EXISTS: LPF adapter builds governed package from memory block | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.lpf.adapter.ts` | lines 42-61 | `buildLPFGovernedPackage` | `GovernedContextPackage` | ACCEPT |
| CANONICAL_CONTRACT: common search/filter facets permit project domain extensions | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | lines 73-115 | common facet schema and domain extension examples | corpus search/filter readiness standard | ACCEPT |
| CANONICAL_CONTRACT: classification vocabulary is not legal-only | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | lines 69-108 | knowledge regions, owner surfaces, answer classes | corpus intelligence classification standard | ACCEPT |
| CANONICAL_CONTRACT: knowledge method starts from source manifest and governed intake | `docs/reference/CVF_KNOWLEDGE_SYSTEM_METHOD_STANDARD_2026-06-01.md` | lines 23-66 | canonical method and authority model | knowledge-system method standard | ACCEPT |

## Current Runtime Freshness Verification

Repo search on 2026-06-10 found no existing DSCP `domainProfile`,
`DomainProfile`, `ScanDomainProfile`, or `domainProfileId` source contract in
active DSCP source. Existing `profileId` hits are unrelated governed-session or
release-grade profile fields, not scan-domain profiles.

This baseline therefore authorizes new DSCP source contract fields as new
runtime/source work, not as pre-existing source facts.

## New Source Contract Fields

| New field | Purpose | Runtime claim blocked before implementation? | Validation expectation |
|---|---|---|---|
| `domainProfileId` | Stable identifier for the scan/memory domain profile | Yes | focused CPF tests |
| `domainFamily` | Domain grouping such as legal_policy, company_docs, technical_project, governance_docs, mixed_corpus | Yes | focused CPF tests |
| `languageCodes` | Language tags used by the profile without hard-coding Vietnamese | Yes | focused CPF tests |
| `facetSchema` | Common and domain-specific filter fields required by the profile | Yes | focused CPF tests |
| `domainGateKeys` | Allowed domain-specific gate names to copy into `customGates` | Yes | focused CPF tests |
| `boundaryRules` | Profile-owned content boundary or chunking rule descriptors | Yes | focused CPF tests |

## Evidence / Verification

| Evidence | Required result |
|---|---|
| Source Verification Summary | all rows ACCEPT with existing repo source or canonical contract paths |
| Work-order dispatch quality | PASS before Claude execution |
| CPF package check | PASS during worker execution |
| Focused DSCP-T10 vitest | PASS during worker execution |
| GC-051 JSON and Markdown coverage | PASS after new source/test registration |

## Acceptance Criteria

| Criterion | Gate |
|---|---|
| New domain-profile source contract is deterministic and local | focused test PASS |
| PolicyLocal profile is represented as one profile, not a hard-coded global default | focused test PASS |
| Non-policy profiles can express their own facet and gate fields | focused test PASS |
| Profile application copies only allowed domain gate keys into `customGates` | focused test PASS |
| Profile application rejects or records unknown gate keys without leaking raw content | focused test PASS |
| No external `Policy_Local` files are modified | `git diff --name-status` |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_FOR_CLAUDE_2026-06-10.md` | `Status: DISPATCHED` before worker return | READY |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_COMPLETION_2026-06-10.md` | reviewer-authored after worker return | PENDING |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_ROADMAP_2026-06-10.md` | `Status: DISPATCHED` before worker return | READY |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | new source/test paths covered during worker execution | PENDING |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | human lookup updated during worker execution | PENDING |
| Session continuity | active handoff and state registry | reviewer sync after closure | PENDING |

## Claim Boundary

This baseline authorizes a local deterministic domain-profile contract and
tests. It does not authorize external product edits, provider calls, live
governance proof, API key use, corpus ingestion, OCR, vector retrieval, semantic
search, PolicyLocal T12, current-law claims, legal advice quality claims,
public-sync, hosted readiness, production readiness, public readiness, memory
reinjection, high-risk promotion, or autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; not public-synced.
