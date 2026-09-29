# CVF GC-018 Baseline - DSH Code Review Enforcement Path Guidance

Memory class: governed-dispatch-baseline

docType: baseline

Status: APPROVED_FOR_EXECUTION

Date: 2026-09-14

Batch ID: DSH-CODE-REVIEW-QUALITY-T1

Dispatch base head: 177c00f336b700c06d740315265b3993c95817c6

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: Local orchestrator/reviewer

Worker target: internal implementation worker

## Purpose

Authorize one existing-owner amendment to make the loaded
`cvf-engineering-code-review-quality` body fulfill its declared five-axis
review output and add DeepSeek Harness's bounded enforcement-path check. The
worker implements documentation and provenance only and returns pending
evidence without committing.

## Scope / Target / Owner Boundary

The existing ASSF package is the sole owner. The current body declares
five-axis guidance in its outputs but contains lifecycle and metadata prose
rather than an executable advisory review procedure. The Addy source supplies
the five axes and review flow. The DeepSeek source adds one material delta:
follow every denial path to the operation it protects and exercise direct and
alternate callers that may bypass schemas, prompts, facades, wrappers, or
listener ordering.

This is not a new skill, lifecycle promotion, receipt rotation, runtime
activation, automatic invocation, merge decision, or checker tranche.

## Proposed Guidance

Add a concise bounded procedure to the existing package body:

1. Establish intent, exact base/head, allowed scope, and project conventions.
2. Inspect tests and enough surrounding implementation to understand behavior.
3. Review correctness, readability/simplicity, architecture, security, and
   performance; lead with correctness, security, lifecycle, and broken required
   behavior.
4. For authorization or enforcement changes, trace every denial branch to the
   operation that executes it and test direct and alternate callers that might
   bypass declarative or wrapper layers. A passing facade-level test is not
   sufficient when another caller reaches the protected operation.
5. Classify findings as Critical, Required, Optional/Consider, Nit, or FYI;
   support each blocking finding with a path/symbol and failure consequence.
6. Verify the verification story and return a bounded verdict. Package loading
   grants no edit, merge, commit, provider, public, or production authority.

The worker may paraphrase and organize this guidance, but must preserve these
semantics and the existing CVF authority ceiling.

## Acceptance Scenarios

| ID | Scenario | Required result |
|---|---|---|
| CR1 | A route facade denies an action but a direct service caller bypasses it | Required or Critical finding with the alternate path named |
| CR2 | All callers converge on one enforcement point and denial prevents the operation | Record the traced path; do not invent a blocker |
| CR3 | Tests pass but omit an error path or lifecycle transition | Review remains incomplete until the missing behavior is assessed |
| CR4 | Code is stylistically imperfect but improves health without a correctness or security defect | Do not block on preference; classify optional feedback accurately |
| CR5 | A change adds coupling or relocates complexity without reducing it | Name the structural risk and propose a concrete remedy |
| CR6 | Package guidance is loaded without an active work order authorizing edits | Advisory review only; no mutation, merge, commit, provider, or public action |
| CR7 | DeepSeek source contains repository-specific commands or policies | Exclude them; import only the source-independent enforcement-path concept |

These are static semantic scenarios, not runtime or efficacy measurements.

## Decision / Baseline / Proposed Tranche

Decision: `APPROVED_BOUNDED_EXISTING_OWNER_AMENDMENT`. Baseline: the current
loader-eligible package remains lifecycle-unchanged, while its body/output
contract mismatch is the defect to repair. Proposed tranche:
`DSH-CODE-REVIEW-QUALITY-T1`, limited to the exact five-path manifest.

## Evidence / Verification

Dispatch evidence consists of the four selected raw-byte hashes, the package
loader receipt `sha256:1c50b864577052203b184e414b75f1ed21b8868caab05624f81291e74a2439e4`,
direct owner/source comparison, CR1-CR7, generated-index drift checking, truth
packet checking and the worker-return fast gate. These prove bounded document
and provenance consistency only.

## Source Identity And License Boundary

| Source | Pin and raw-byte SHA-256 | Role |
|---|---|---|
| `.private_reference/source_mirrors/addyosmani__agent-skills/skills/code-review-and-quality/SKILL.md` | pin `aba7c4e9695c363e65cb59effe926c7f1d1abe3d`; `455bc5911935eee5d259a017bf31465e83ce727235fd1d0a9a9bd2eee15eda6f` | primary five-axis/process source |
| `.private_reference/source_mirrors/addyosmani__agent-skills/LICENSE` | `b88ef8718459d5b5aabb1943cb8f4fd57963422f2d98a801dac814fea53932c8` | primary MIT notice |
| `.private_reference/source_mirrors/deepseek-ai__deepseek-harness/.agents/skills/dsh-code-review/SKILL.md` | pin `cd5ef8148158c3a752a658978873241fdf8e2bbc`; `167f0915c64e735bdf675e285faeea4b2dd66c37c3d2169c33a82070f2f770f0` | supplemental enforcement-path guidance |
| `.private_reference/source_mirrors/deepseek-ai__deepseek-harness/LICENSE` | `ebb4f09972aee8608be255debaf78451a68e95c290f55c240dec2ecfa16ea6be` | supplemental MIT notice |

Preserve Addy as the primary upstream identity and add DeepSeek as a separately
attributed supplemental source. Include both full MIT notices in the package
attribution section. Do not relabel the whole package as DeepSeek-derived.

## Dependency Disposition

| Path | Disposition |
|---|---|
| `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/SKILL.md` | Required bounded guidance and attribution edit |
| `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/skill.source.json` | Required sourceArtifacts and narrow adaptation-boundary edit |
| `docs/reference/agent_system_skills/registry/entries/cvf-engineering-code-review-quality.json` | Required sourceArtifacts edit only |
| `docs/reference/agent_system_skills/generated/skill-index.json` | Required generator output |
| `docs/reviews/CVF_DSH-CODE-REVIEW-QUALITY-T1_WORKER_RETURN_2026-09-14.md` | Required worker return |
| truth packet, truth index, control-plane inventory, package README | No write; their projected lifecycle/receipt fields do not change; run checks |

If a generator or checker proves another path is required, stop and return one
consolidated dependency finding rather than widening scope.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind package-skill --batch-id DSH-CODE-REVIEW-QUALITY-T1 --title "DSH Code Review Enforcement Path Guidance" --date 2026-09-14 --base 177c00f336b700c06d740315265b3993c95817c6 --commit-mode WORKER_MUST_NOT_COMMIT --scec-problem-key dsh-code-review-quality-t1 --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --include-worker-return-skeleton --stdout` |
| generatedProfile | package-skill; no-commit internal worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced all placeholders with this bounded existing-owner source, dependency, scenario and authority contract |
| checkerReadAheadConfirmation | `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py` |
| docOnlyNewFields | none; existing canonical fields reused |
| claimBoundary | dispatch authorization only; no worker payload or runtime proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation-planning`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class implementation-planning --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defects | NONE_RETURNED |
| Dispatch impact | No returned defect changes this bounded no-commit packet |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_core.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_package_skill_productionization_pipeline.py` |
| literalTokensReviewed | `APPROVED_FOR_EXECUTION`; `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `ACCEPT`; `DEFERRED_PRIVATE_ONLY`; `CLOSEABLE` |
| gateRunPurpose | confirm as evidence that the bounded source and dispatch contract match checker-required structure after source read-ahead |
| claimBoundary | targeted read-ahead only; no claim that all repository checkers were read |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Loaded body lacks its declared detailed procedure | current-owner comparison | `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/SKILL.md` | Inputs And Outputs; full body | `Outputs` | existing package body | ACCEPT |
| Addy supplies five axes and process | source guidance | `.private_reference/source_mirrors/addyosmani__agent-skills/skills/code-review-and-quality/SKILL.md` | The Five-Axis Review; Review Process | five axes | primary pinned source | ACCEPT |
| DeepSeek supplies bypass-path tracing | source guidance | `.private_reference/source_mirrors/deepseek-ai__deepseek-harness/.agents/skills/dsh-code-review/SKILL.md` | What to inspect beyond the diff | Enforcement | supplemental pinned source | ACCEPT |
| Registry projects to generated index | dependency | `governance/compat/generate_assf_skill_index.py` | `aggregate_entry` | `aggregate_entry` | index generator | ACCEPT |
| Truth fields need no mutation | dependency | `governance/compat/check_skill_truth_packets.py` | packet/index projection | `_expected_index` | truth checker | ACCEPT |

## Negative Search And Collision Discipline

Search existing package, registry, truth, prior DSH reviews and current source
mirrors before writing. Reuse the existing package owner. Do not create a new
skill, duplicate review framework, checker, runtime adapter, or similarly named
artifact outside the exact manifest.

## Epistemic Process Block

Expected Result / Prediction: adding the missing procedure and the distinct
enforcement-path check will make the loaded advisory body match its declared
outputs without changing lifecycle or runtime authority.

Evidence Comparison: the loader successfully loads the package, but the loaded
body currently contains metadata/lifecycle prose only; Addy contains the five
axes and process, while DeepSeek uniquely names alternate-caller bypass tracing.

Contradiction Or Gap Disposition: the source delta is admitted only inside the
existing owner. DSH-UC-03 remains deferred until a named source-code prose or
comment-quality tranche exists and is forbidden for governed-document cleanup.

Claim Update: bounded implementation is authorized; no implementation or
measured improvement is claimed before the worker return is reviewed.

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: source-verified advisory amendment to an existing ACTIVE package.
Target lifecycle state: retain every current lifecycle, UAT, certification and
adapter field unchanged. Prior phase evidence: current package, registry,
truth packet, DSH WRA completion, DSH UC01 Track B completion and source terminal
review evidence. Next forbidden skip: treating prose enrichment as a fresh
runtime receipt, UAT, certification, provider proof or production readiness.
Runtime/provider proof: none released or claimed. Claim boundary: package body
and provenance only; no automatic invocation or action authority.

## External Repository Absorption Entry Control

BOUNDED_ADAPTATION_AUTHORIZED: one selected guidance concept from the fully
read pinned DeepSeek skill and license, composed into an existing CVF owner.
No direct upstream execution or whole-repository absorption claim.

| Field | Value |
|---|---|
| Source type | named pinned external skill and license files |
| Upstream or source-mirror disposition | reuse clean DeepSeek pin `cd5ef8148158c3a752a658978873241fdf8e2bbc` |
| Enumeration or manifest plan | four selected files listed in Source Identity And License Boundary |
| Per-file terminal-ledger plan | all four selected files FULL_READ for dispatch admission |
| Owner or overlap route | existing `cvf-engineering-code-review-quality` package |
| Value-disposition route | adapt five-axis body completeness and DeepSeek enforcement-path delta |
| Claim boundary | bounded advisory amendment only |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | accepted pinned source evidence to Local owner comparison to bounded package adaptation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/SKILL.md` |
| Disposition | `BOUNDED_ADAPTATION_AUTHORIZED` |
| Claim boundary | selected source-independent guidance only |

## External/Local Coordination Binding

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
  },
  "contractSha256": "92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c",
  "parentArtifact": "docs/reviews/CVF_THREE_REPO_PATTERN_COMPARISON_LOCAL_REVIEW_2026-09-13.md"
}
```

## Mandatory Blind-Spot Control Block

Applied. The decision compares actual loaded owner-body content with both full
selected source files, separates overlap from the DeepSeek delta, and retains
DSH-UC-03 as demand-gated. It makes no full-corpus claim.

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Addy five-axis/process guidance | `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/SKILL.md` | `CONFIRMED_EXISTING` | declared output lacks detailed loaded procedure | complete body inside existing owner |
| DeepSeek enforcement guidance | `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/SKILL.md` | `ENRICH_EXISTING` | trace denial to operation and exercise alternate bypass callers | bounded supplemental adaptation |
| DSH-UC-03 prose taxonomy | `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/SKILL.md` | `NO_NEW_VALUE` | no named source-code prose tranche | no write in this tranche; retain trigger in residual audit |

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no complete-corpus scan or
  coverage claim. The bounded dispatch admission fully reads and hash-binds
  exactly two selected skill files and their two license files.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private package provenance and dispatch packet; no public-sync authority.

## Claim Boundary

This baseline authorizes exactly the five-path worker manifest and seven static
semantic scenarios. It does not authorize lifecycle changes, new truth or
runtime receipts, provider/live calls, dependency installation, public sync,
deployment, merge, commit, or production action.
