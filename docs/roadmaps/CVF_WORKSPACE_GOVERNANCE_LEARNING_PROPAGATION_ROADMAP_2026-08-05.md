# CVF Workspace Governance Learning Propagation Roadmap

Memory class: FULL_RECORD

Status: GLP_T3_REVIEWER_ACCEPTED_PROPAGATION_PROVEN_BOUNDED

docType: roadmap

Date: 2026-08-05

Owner: CVF orchestrator

## Authorization / Decision

The operator accepted `CVF-WORKSPACE-GOVERNANCE-LEARNING-PROPAGATION-R0` as
the next roadmap after the governance-latency evidence lane reached its bounded
stop. This authority covers provenance-native planning and a documentation-only
T0 propagation audit. It does not authorize bootstrap implementation, generated
workspace mutation, application-project mutation, public synchronization,
provider use, network use, push, or deployment.

Decision: `OPEN_BOUNDED_PROPAGATION_AUDIT`

## Purpose

Ensure that minimum-effective-governance learning accepted in the private CVF
provenance can reach newly created or refreshed CVF workspaces through an
explicit, testable projection chain:

`provenance owner -> curated rule-pack catalog -> selected workspace profile -> workspace guidance -> project bootstrap/adoption`

The roadmap addresses a concrete distribution risk: provenance may contain a
valid learning owner while a generated workspace receives only a pointer to
that owner, omits the owner itself, or receives project guidance that preserves
safety controls without the matching latency and autonomy boundary.

## Scope

In scope:

- source-map the current provenance-to-workspace projection chain;
- distinguish canonical provenance ownership from curated workspace copies;
- verify whether same-scope authority continuity, avoidable operator wait,
  diminishing-return control, and minimum-effective-governance routing have a
  complete workspace carrier;
- select the smallest safe propagation remedy when a gap is proven;
- prove the selected remedy in a disposable workspace before any downstream
  adoption claim;
- retain project-level governance ownership in generated project artifacts.

## Non-Goals

- No reopening of governance-latency WS2, technical zero-network, DESIGN,
  specification, BUILD, or provider lanes.
- No copy or promotion of the downstream governed-plan runner.
- No wholesale export of private continuity, private session state, historical
  handoffs, or the complete provenance governance corpus.
- No weakening of public/private boundaries, source verification, independent
  review, no-commit discipline, or evidence-backed closure.
- No edit to the sibling workspace or any application project during T0.
- No assumption that an artifact present in provenance is automatically
  inherited by a workspace or project.

## Current Source Audit Result

| Claim | Current source evidence | Disposition |
|---|---|---|
| The provenance initializer is the workspace entrypoint | `Initialize-CVF-Operator-Workspace.ps1` lines 443-520 installs or refreshes the hidden public core, root wrappers, and a selected rule pack | SOURCE_VERIFIED |
| `operator-local` uses a curated profile chain | `workspace_overlay_profiles/operator-local.json` extends `paid-user-safe` and `provenance-local`; `provenance-local.json` extends `premium-workspace` and local continuity | SOURCE_VERIFIED |
| Artifact propagation is catalog-driven | `scripts/sync_cvf_workspace_rule_pack.ps1` lines 169-245 selects catalog artifacts by profile tags and copies only selected paths | SOURCE_VERIFIED |
| The rule-pack manifest records exact projected artifacts | `scripts/sync_cvf_workspace_rule_pack.ps1` lines 293-318 records source commit, tags, artifact count, and copied paths | SOURCE_VERIFIED |
| Guard orientation is projected to premium/operator-local workspaces | `workspace_overlay_catalog.json` entry `guard-orientation-index` carries `downstream-governance` and `operator-orientation` tags | SOURCE_VERIFIED |
| Three latency-learning owners are absent from the catalog | Exact catalog lookup returns zero entries for `CVF_ADIF-0026.md`, `CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md`, and the R72C Fast Lane case matrix | SOURCE_VERIFIED_GAP |
| Project guidance preserves high-risk review independence | `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` lines 132-170 requires independent review for high-risk work and defines risk levels | SOURCE_VERIFIED |
| Project guidance lacks the accepted same-scope wait classification | Exact search of the downstream agent template finds no same-scope authority, avoidable operator wait, review-cost, diminishing-return, or Fast Doc guidance | SOURCE_VERIFIED_GAP |

The T0 audit must independently reproduce these observations. This roadmap does
not preselect whether the remedy is a catalog addition, a compact public-safe
carrier, a project-template amendment, or no change.

## Design Control Gate

The governing design principle is smallest safe carrier, not maximum document
replication.

The following controls must remain intact in every tranche:

| Protected control | Required preservation |
|---|---|
| provenance authority | workspace copies remain curated projections and never replace provenance source ownership |
| public/private boundary | private continuity and internal evidence are not copied into public or customer profiles |
| source verification | every claimed carrier, profile tag, copy path, and generated output is verified from current source |
| worker/reviewer separation | implementation workers do not approve their own propagation result |
| project ownership | generated project `AGENTS.md`, manifest, and policy remain project-level control surfaces |
| latency control | same-scope remediation continues without repeated operator confirmation unless a real boundary changes |

Dispatch must remain blocked if the proposed remedy requires exporting private
continuity, broadens a public profile without a public-safety classification,
or weakens a protected control.

## Work Plan

| Tranche | Objective | Bounded output | Exit decision |
|---|---|---|---|
| GLP-T0 | Reproduce the propagation chain and classify the gap | source audit, exact catalog/profile inventory, project-template comparison, governance-cost estimate, independent review | `PROCEED_BOOTSTRAP_ALIGNMENT`, `PROCEED_DOC_ONLY`, or `STOP_ALREADY_PROPAGATED` |
| GLP-T1 | Define the smallest safe carrier and ownership boundary | one source-verified design/spec packet; prefer an existing owner or compact public-safe carrier | `CARRIER_DESIGN_ACCEPTED` or `STOP_NO_SAFE_CARRIER` |
| GLP-T2 | Align provenance bootstrap/catalog/template surfaces | bounded implementation plus focused catalog/profile/template tests | `ALIGNMENT_IMPLEMENTED_BOUNDED` or `BLOCKED_IMPLEMENTATION_EVIDENCE` |
| GLP-T3 | Prove propagation in a disposable fresh workspace | generated manifest, expected-artifact assertions, negative private-leakage checks, project guidance readout | `PROPAGATION_PROVEN_BOUNDED` or `PROPAGATION_PROOF_FAILED` |
| GLP-T4 | Close and publish the adoption boundary | closure review, operator guide update if needed, public-export disposition | `CLOSED_PASS_BOUNDED`, `DEFERRED_PRIVATE_ONLY`, or `BLOCKED_MISSING_PUBLIC_ARTIFACTS` |

GLP-T1 is independently accepted with corrections and decision
`CARRIER_DESIGN_ACCEPTED`. GLP-T2 packet authoring is the next allowed move.
GLP-T2 execution and every later tranche remain held until a fresh
source-verified packet passes dispatch review and the implementation authority
required by that packet is explicit; no implementation authority is implied.

GLP-T2 returned `BLOCKED_IMPLEMENTATION_EVIDENCE` on 2026-08-05. The existing
CP1 hand-edited merge branch rewrites the complete `AGENTS.md` and failed the
required outside-block byte-identity proof. The partial template/harness diff
was rejected. GLP-T3 remains held. The next bounded planning move is a fresh
source-verified packet for CP1 byte-preserving merge repair; implementation of
that repair requires explicit operator authority.

GLP-T2R1 subsequently repaired the CP1 hand-edited merge path under fresh
operator authority. Independent review confirmed outside-block byte identity
on insertion and refresh, fail-closed zero-mutation behavior for duplicate,
reversed, and unterminated markers, one complete public-safe carrier, zero
private sentinel hits, cleanup PASS, and 79/79 focused assertions. Decision:
`ALIGNMENT_IMPLEMENTED_BOUNDED`. GLP-T3 remains held for a fresh proof packet.

GLP-T3 subsequently ran one existing local golden harness call through the
released no-commit worker route. Independent review accepted 79/79 assertions,
14/14 expected generated surfaces, the generated manifest contract, exactly
one complete five-semantic carrier, zero hits across 27 private-sentinel
checks, and zero cleanup residue. Decision: `PROPAGATION_PROVEN_BOUNDED`.
The proof-subject provider/network count was zero; the previously completed
Claude worker orchestration was separately disclosed as one session, 49 turns,
572.670 seconds, and USD 2.9589262. GLP-T4 packet authoring only is next;
adoption, public export, and GLP-T4 execution remain held.

## GLP-T0 Outcome - 2026-08-05

The independent reviewer reproduced 34 catalog artifacts and all 15 profile
files. `operator-local` resolves seven tags and selects 28 artifacts. Exact
membership remains zero for ADIF-0026, the review-cost standard, and the R72C
carrier; the downstream template also contains none of the enumerated
same-scope, avoidable-wait, review-cost, diminishing-return, or Fast Lane
vocabulary. The evidence therefore supports `PROCEED_DOC_ONLY`, not bootstrap
alignment and not no-change.

Reviewer corrections were bounded to profile/file counts, line citations, the
worker-return literal contract, and the historical execution-base defect. No
bootstrap, catalog, profile, template, generated workspace, downstream,
provider/network, public-sync, push, or deployment action occurred.

## GLP-T1 Outcome - 2026-08-05

Independent review accepts
`governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` as the
smallest safe carrier because `scripts/new-cvf-workspace.ps1` unconditionally
projects it into new and refreshed downstream project `AGENTS.md` files. The
first-pass guard-orientation recommendation remains preserved with the R1
consumer-chain disagreement.

The bounded GLP-T2 design manifest contains exactly the downstream template
and `scripts/test_cvf_golden_downstream_bootstrap.ps1`. The existing hermetic
harness must prove fresh delivery, refresh idempotency, hand-edited merge-block
delivery, byte preservation, and exact private-evidence exclusion. No template,
test, bootstrap, workspace, project, provider/network, public-sync, push, or
deployment action occurred in GLP-T1.

## Governance Cost Budget

GLP-T0 is documentation and local read-only evidence only. It should use one
audit, one worker return, and an independent review route. A separate completion
artifact is created only if the work-order contract requires it.

The audit must record:

- artifact count and profile count inspected;
- first-pass and final gate counts;
- repair round count;
- operator wait classification;
- whether any proposed control adds more recurring cost than the gap it fixes.

Repeated shape-only repair without new decision evidence triggers the existing
review-cost stop rule. Same-scope allowed repairs do not consume another
operator checkpoint.

## Acceptance Criteria

| ID | Criterion | Required evidence |
|---|---|---|
| AC1 | Provenance, public-core, workspace-root, rule-pack, and project authority classes are separated | source-backed chain map |
| AC2 | Every selected profile in scope has an exact artifact inventory | catalog/profile query output |
| AC3 | ADIF-0026, review-cost, R72C/R84, guard orientation, and downstream template coverage are classified separately | propagation coverage matrix |
| AC4 | Pointer-without-owner and owner-without-project-carrier gaps remain visible | disagreement/gap ledger |
| AC5 | The cheapest safe alternatives are compared before implementation | catalog-addition, compact-carrier, template-only, and no-change rows |
| AC6 | T0 returns exactly one exit decision | independent reviewer disposition |
| AC7 | No sibling workspace, application project, public-sync, runtime, provider, or network surface changes in T0 | Git changed-set and command evidence |
| AC8 | Governance cost of the roadmap itself is reported | review-cost telemetry |

Fail conditions:

- source paths or profile relationships cannot be reproduced;
- the audit treats a curated copy as canonical provenance authority;
- a proposed public carrier exposes private continuity or internal evidence;
- T0 edits bootstrap, catalog, template, generated workspace, or downstream
  project surfaces;
- the result infers propagation from provenance presence without checking the
  catalog, profile, manifest, and generated consumer chain.

## Verification / Evidence

Required T0 evidence includes:

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
rg -n "Install-NewWorkspace|Apply-SelectedProfile|Refresh-ExistingWorkspace" Initialize-CVF-Operator-Workspace.ps1
rg -n "Resolve-ProfileTags|selectionTags|RULE_PACK_MANIFEST" scripts/sync_cvf_workspace_rule_pack.ps1
python -m json.tool workspace_overlay_catalog.json
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD
```

No live governance proof is required or authorized for T0 because T0 makes no
runtime or provider-behavior claim.

## Dual Agent Surface Matrix

| Surface class | Interface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | provenance files and local read-only commands | may audit and author T0 evidence; may not implement T1+ | committed provenance paths and Git evidence | local filesystem only | T0_ALLOWED |
| `EXTERNAL_AGENT_CLI_MCP` | future role-neutral worker handoff | may execute only a source-verified no-commit T0 packet | worker return and independent review | no provider, network, MCP write, or downstream adapter | CONTRACT_ONLY |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| provenance learning can be absent from the curated workspace carrier | `PHASE_GATE_PLACEMENT_GAP` | `GOVERNANCE_CONTROL_PLANE` | `DESIGN_REVIEW_REQUIRED` | GLP-T0 reproduces and classifies the propagation gap before any carrier edit |
| project safety guidance lacks the matching same-scope latency boundary | `RULE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `RULE_EXISTS` | compare project carrier needs against ADIF-0026 and the review-cost standard |

No new ADIF entry is opened by this roadmap. The observed latency behavior is
already owned by ADIF-0026; GLP-T0 tests distribution, not defect novelty.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the operator-local profile will prove a real but
bounded carrier gap, while public/customer profiles will require a smaller
public-safe learning projection rather than private-owner replication.

Evidence Comparison Requirement: GLP-T0 compares the prediction with exact
catalog membership, resolved profile tags, generated-manifest semantics, and
project-template coverage.

Contradiction Or Gap Disposition: contradictory evidence must remain visible;
if the current generated chain already carries equivalent guidance with a
source-backed owner, return `STOP_ALREADY_PROPAGATED`.

Claim Update Requirement: GLP-T0 must confirm, narrow, or invalidate the gap
claim and must not treat pointer presence as content propagation.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | roadmap authorization, purpose, scope, non-goals, design control, work plan, acceptance, verification, finding-learning, epistemic-process, trace, and public-export section labels; `ROADMAP_READY_FOR_T0_GC018_AUTHORING`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirm the roadmap shape and bounded authority after source audit, not discover requirements through repeated failures |
| claimBoundary | roadmap and T0 release only; no bootstrap implementation, generated workspace mutation, downstream edit, or public action |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | orchestrator and roadmap author |
| Provider or surface | local private provenance repository |
| Session or invocation | GLP-R0 roadmap authoring, 2026-08-05 |
| Working directory | repository root |
| Command or tool surface | canonical reads, source searches, JSON queries, Git inspection, apply_patch, governance gates |
| Target paths | `docs/roadmaps/CVF_WORKSPACE_GOVERNANCE_LEARNING_PROPAGATION_ROADMAP_2026-08-05.md` |
| Allowed scope source | operator acceptance of the recommended next roadmap on 2026-08-05 |
| Before status evidence | HEAD `c91cd52b3`; clean worktree; branch `main` |
| After status evidence | one new roadmap pending governed validation and commit |
| Diff evidence | `git diff --name-status --no-renames` before commit |
| Approval boundary | roadmap authoring and documentation-only T0 release |
| Claim boundary | local source audit and planning only; no implementation or external-effect claim |
| Agent type | orchestrator/roadmap author |
| Invocation ID | `cvf-workspace-governance-learning-propagation-r0-2026-08-05` |
| Expected manifest | this roadmap only |
| Actual changed set | this roadmap only |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap contains private provenance distribution analysis and does
not authorize public-sync mutation. A later public-safe carrier requires its own
classification, evidence, and repository-boundary verification.

## Claim Boundary

This roadmap proves only that current provenance source contains a bounded
workspace-learning propagation risk worth independent T0 audit. It releases
GLP-T0 documentation and local read-only evidence work only. It does not prove
that every generated workspace is stale, authorize a carrier implementation,
change any profile, mutate a workspace or project, publish artifacts, call a
provider, use the network, push, deploy, or claim production readiness.
