# CVF GC-018 - ERH-RS1 External Review Full Coverage Rescan

Memory class: FULL_RECORD

Status: AUTHORIZED_DISPATCH_PACKET

docType: gc018_baseline

Date: 2026-06-04

dispatchBaseHead: `b442085e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize a bounded rescan of the archived external public-repo review source.
The rescan exists because the first ERH roadmap was created before the later
corpus-completeness, scan-registry, and smart-scan hardening controls were in
place. The goal is to produce a section-level coverage ledger that shows which
external-review statements were captured, fixed, bounded, deferred, superseded,
or missed.

## Scope / Target / Owner Boundary

Target source:

`docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_SOURCE_2026-06-03.docx`

Authorized outputs:

- `docs/assessments/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md`
- optional private follow-up candidate rows inside the RS1 assessment for
  ERH-SAF1, provider-risk configuration, audit durability, policy snapshot
  reconstruction, and distributed rate limiting.

Out of scope:

- runtime/source code edits;
- safety workflow implementation;
- ML DLP or classifier implementation;
- Redis/database/storage migration;
- provider routing behavior change;
- public-sync, public push, hosted proof, production readiness, or public
  readiness;
- live provider/API proof.

Risk ceiling: R0 docs-only rescan and planning.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-04: rescan external review because the old roadmap predates smart-scan hardening; inspect why safety was only claim-calibrated and elevate to workflow chain/system when foundation exists | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |
| Original ERH GC-018 | `docs/baselines/CVF_GC018_ERH_EXTERNAL_REVIEW_HARDENING_2026-06-04.md` | ACCEPT_AS_PREDECESSOR |
| Original ERH roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT_AS_PREDECESSOR |
| Archived external source | `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_SOURCE_2026-06-03.docx` | ACCEPT_AS_SOURCE |

## Decision / Baseline

Decision: authorize Claude to execute ERH-RS1 as a fresh full-coverage rescan,
not as an edit to the closed initial ERH tranche set.

Baseline facts:

- prior ERH intake remains predecessor evidence, not completeness proof;
- the archived Word document is the source authority for this rescan;
- findings from section 4.4 must be explicitly covered, including audit
  durability, in-memory rate limiting, thin safety/jailbreak coverage,
  policySnapshotId reconstructability, and hardcoded provider risk ceilings;
- safety must be evaluated as a possible workflow-chain follow-up because the
  current web route already has DLP and safety entry points.

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| External review DOCX source path is recorded by predecessor intake | EXISTS | `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md` | lines 13-15 | `CVF_EXTERNAL_PUBLIC_REPO_REVIEW_SOURCE_2026-06-03.docx` | archived external review source pointer | ACCEPT |
| Prior intake exists but is not completeness proof | EXISTS | `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md` | file source | `CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md` | predecessor ERH intake | ACCEPT |
| Existing route runs DLP before safety | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 240-261 | `applyDLPFilter` then `applySafetyFilters` | `/api/execute` POST route | ACCEPT |
| DLP policy entry point uses active policy patterns | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/dlp-filter.ts` | lines 6-8 | `applyDLPFilter` | web DLP filter | ACCEPT |
| DLP preset and custom pattern engine exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/dlp-filter-core.ts` | lines 24-190 | `PRESET_PATTERNS`, `applyDLPPatterns` | DLP pattern engine | ACCEPT |
| Current safety filter is regex/pattern based | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety.ts` | lines 1-35 | `INJECTION_PATTERNS`, `PII_PATTERNS`, `applySafetyFilters` | web safety filter | ACCEPT |
| Richer safety-status logic exists but is not the execute-route safety chain | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety-status.ts` | lines 115-167 | `sanitizePrompt`, `isInputDangerous` | web safety status helper | ACCEPT |
| WEB_PROVIDER_DEFINITIONS declares static maxRiskLevel values: openai R2, claude R2, gemini R2, alibaba R1, openrouter R1, deepseek R1 | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/provider-router-adapter.ts` | lines 70-119 | `WEB_PROVIDER_DEFINITIONS` | provider router adapter | ACCEPT |

## Evidence / Verification

External source digest:

| Artifact | SHA256 |
| --- | --- |
| `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_SOURCE_2026-06-03.docx` | `1C52C011A2D11922C5A5712FF785435474AB772B6F9C0A42563D177B1F255A10` |

Dispatch verification before Claude starts:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base b442085e --head HEAD --all-changed --enforce
python governance/compat/check_work_order_dispatch_quality.py --base b442085e --head HEAD --enforce
python governance/compat/check_public_export_disposition.py --base b442085e --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base b442085e --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base b442085e --head HEAD
```

Claude verification before closure must use the base anchor recorded by Claude
at implementation start.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| First ERH intake did not prove full-document coverage under the newer corpus controls | CORPUS_COMPLETENESS_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | require GC-047-style coverage ledger in RS1 |
| Safety was claim-calibrated because prior tranche was docs-only, while runtime foundations now exist | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | ROADMAP_REQUIRED | RS1 must decide whether ERH-SAF1 should be dispatched |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ERH-RS1 is a private provenance rescan and planning authorization.

Next action: any public-facing summary requires a later public-sync work order
from the public-sync clone.

## Claim Boundary

This GC-018 authorizes only a source-backed rescan and follow-up planning
assessment. It does not claim that the external review has been fully remediated
and does not authorize runtime safety, provider, durability, policy, or
rate-limit implementation.
