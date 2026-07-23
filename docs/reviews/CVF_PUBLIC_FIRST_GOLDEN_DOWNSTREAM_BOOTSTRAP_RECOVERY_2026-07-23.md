# CVF Public-First Golden Downstream Bootstrap Recovery

Memory class: EVIDENCE_RECORD

Status: CLOSED_PASS_BOUNDED

docType: audit

Date: 2026-07-23

## Purpose

Classify and repair the repository-boundary defect in which a downstream
bootstrap learning tranche was committed to the public repository before it
was absorbed, reviewed, and committed in private provenance.

## Scope / Methodology

Target public range:
`6ce1cf00c31a7f825d4c3fa3e66e8a3509e4a4b2..571cb21b7026f0cd925279ba698bf30a291a4644`.

Recovery scope is limited to importing the four public commits into
provenance, reconciling provenance-only mapped filenames, validating the
bootstrap implementation, removing private execution evidence from public,
and recording reusable governance learning.

No provider, API key, CLI/MCP agent invocation, runtime deployment, branch
history rewrite, or force push is authorized.

## Source Evidence

| Evidence | Observed result |
|---|---|
| Public event | direct push to public `main`; no matching new pull request |
| Public commits | `2c59f6ac1`, `869381c88`, `5ee560aac`, `571cb21b7` |
| Public changed set | 22 paths; 17 absent and 5 divergent in provenance before import |
| Public CI | 66 check runs: 28 success, 33 failure, 2 cancelled, 3 skipped |
| Secret-safe scan | no obvious raw credential or API key found in the imported range |
| Provenance import method | four sequential no-commit cherry-picks; no history rewrite |
| Initial provenance test | failed because a public-authored harness assumed the current checkout was public `main` |
| Corrected provenance test | golden downstream harness PASS, 69/69 assertions |

## Findings

### F1 - Repository authority order was reversed

The learning, design, implementation, review, and closure sequence landed on
public `main` before private provenance had absorbed or accepted it. Public is
a curated projection target, not the authority source for governed CVF work.

Disposition: `MATERIAL_REPAIR_REQUIRED`.

### F2 - Public-only mapped filenames were mistaken for provenance files

The imported harness expected root `AGENT_HANDOFF.md` and
`scripts/install_cvf_workspace_root_wrappers.ps1`. Those names are created by
`scripts/cvf-public-sync.ps1` from private sources and must not be added to
provenance as duplicate public aliases.

Disposition: `REPAIRED_IN_PROVENANCE`. The harness now anchors its clean clone
to the sibling public-sync repository when run from provenance and overlays
the canonical mapped sources deterministically.

### F3 - Internal execution evidence was published

The public range includes build evidence, work-order material, amendments, and
independent-review working records. They contain no detected secret, but they
are private execution-governance evidence and are not required for public use.

Disposition: `PUBLIC_CORRECTIVE_REMOVAL_REQUIRED`.

### F4 - Imported Markdown did not satisfy provenance structure

Nine new governed Markdown files lacked the structural metadata or headings
required by the current provenance gates.

Disposition: `REPAIRED_IN_PROVENANCE`. Imported execution records are marked
historical and non-dispatching; the durable references and guard now expose
purpose, scope, status, and claim boundaries.

### F5 - Canonical workspace mapper omitted the new kit

After the first provenance commit, a `WorkspaceKitOnly` dry run listed only
the pre-existing kit. It omitted the new catalog helpers, schemas, harness,
guard, learning intake, design, and specification. The direct public-first
push masked this gap because those files already existed in the public clone.

Disposition: `REPAIRED_IN_PROVENANCE`. The explicit workspace-kit allowlist
now includes every public-safe surface in the tranche, and BSL-R7 checks that
the mapper retains every new catalog/helper/schema/guard surface.

### F6 - Mapper regression crossed the public control-plane boundary

The first BSL-R7 mapper assertion assumed the private projection script also
existed in the public clone. That script is intentionally not exported.

Disposition: `REPAIRED_IN_PROVENANCE`. The assertion remains mandatory when
the mapper exists in provenance and records `N/A_WITH_REASON` on the
intentionally mapper-free public surface. The public harness still runs the
remaining bootstrap and completeness assertions.

### F7 - Provenance autorun has no bounded public-projection profile

Running the full provenance pre-implementation bundle inside the public clone
reported 24 failures dominated by intentionally absent private session,
review, corpus, and control-plane surfaces. This is not evidence that the
public bootstrap kit failed; its dedicated harness passed 69/69 in that clone.

Disposition: `PARKED_KNOWLEDGE_GAP`. A future governance tranche may define a
public-projection gate profile. This recovery does not export private surfaces
or weaken provenance gates merely to make the full private bundle pass in the
public clone.

## Public Projection Classification

| Path class | Provenance disposition | Public disposition |
|---|---|---|
| implementation scripts, schemas, test, workspace docs | retain and validate | retain after corrected projection |
| learning intake, design, specification | retain as imported reference | retain after public-safe header refresh |
| downstream catalog guard | retain with self-protection authorization | retain after public-safe refresh |
| build evidence | retain as private historical evidence | remove |
| work order and amendment | retain as private historical evidence | remove |
| independent review and findings | retain as private historical evidence | remove |
| provenance recovery audit and ADIF learning | retain | do not export |

## Risk / Corrective Action

1. Import the four public commits into provenance without committing their
   public-only assumptions unchanged.
2. Repair the hermetic harness at the provenance/public mapping seam.
3. Run the dedicated 69-assertion bootstrap harness and governed gates.
4. Commit and push provenance first.
5. Apply a normal forward corrective commit in the sibling public-sync clone:
   remove the five private evidence files and copy only reviewed public-safe
   surfaces from provenance.
6. Run public pre-push checks and push without rewriting history.
7. Record the final provenance and public commit receipts before closure.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: absorb and structurally reconcile the new
downstream catalog guard that already landed in the incident public range.

Protected paths:

- `governance/toolkit/05_OPERATION/downstream_catalog/CVF_DOWNSTREAM_CATALOG_GUARD.md`

Operator authorization: on 2026-07-23 the operator explicitly instructed the
reviewer to classify and process this bootstrap learning so provenance and
public are synchronized according to CVF rules.

Rollback boundary: revert only the recovery material commit if the recovered
bootstrap tranche is rejected. Do not rewrite or delete the four published
public commits and do not revert unrelated provenance work.

Scope boundary: this authorization does not extend to other guards, active
runtime, provider/API behavior, CLI/MCP agent invocation, deployment, branch
protection configuration, or history rewriting.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_adif_entry_integrity.py` |
| literalTokensReviewed | `Core Guard Self-Protection Authorization`; `Protected paths`; `Scope / Methodology`; `Risk / Corrective Action`; `External Knowledge Intake Routing`; `Finding-To-Governance Learning Disposition`; `Agent Operation Trace Block`; `Public Export Disposition` |
| gateRunPurpose | confirm the final repaired artifact shape after bounded checker diagnostics; not first discovery for the final gate run |
| claimBoundary | checker-shape evidence only; no runtime, provider, CLI/MCP, deployment, or automatic prevention claim |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator incident report to source verification, governed recovery review, local tests, and public projection classification |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_core_guard_self_protection.py`; `scripts/cvf-public-sync.ps1` |
| Owner surface | private provenance repository |
| Disposition | ADAPT as CVF-owned recovery evidence and ADIF learning; do not treat the public clone as source authority |
| Claim boundary | operator report is verified against Git evidence; no external-agent output, provider claim, or third-party code is absorbed |

## Finding-To-Governance Learning Disposition

Next action: retain ADIF-0050 as the reusable authority-boundary learning and
use the sibling-aware harness repair as the regression for provenance/public
mapped filenames.

Runtime/provider/cost learning lane: `N/A_WITH_REASON` - the incident and
recovery use repository and local test evidence only; no provider or live
runtime call occurred.

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| Governed work landed on public before provenance | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | Keep ADIF-0050 active and require provenance-first recovery order |
| Public-authored harness assumed mapped aliases existed in provenance | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Retain sibling-aware hermetic bootstrap regression |
| Five internal execution-evidence files were published | RULE_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Remove them through a forward public corrective commit |
| Imported Markdown missed current structural literals | ORCHESTRATOR_PACKET_GAP | DOCUMENTATION_ONLY_LEARNING | RULE_EXISTS | Retain imported-history headers and use the existing literal-format checklist |
| `WorkspaceKitOnly` mapper omitted the new kit | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | Retain the BSL-R7 mapper-completeness regression |
| Mapper regression assumed a private control-plane file existed in public | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | Preserve provenance-only enforcement and explicit public N/A boundary |
| Full provenance gate bundle is not projection-aware | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | PARKED_KNOWLEDGE_GAP | Design a bounded public-projection gate profile in a separate authorized tranche |
| Runtime/provider/cost applicability | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | No runtime, provider, quota, token, or cost behavior was exercised |

## Verification

| Check | Result |
|---|---|
| `git diff --cached --check` | PASS |
| `scripts/test_cvf_golden_downstream_bootstrap.ps1` | PASS, 69/69 |
| governed file size | PASS |
| Markdown structural completeness | PASS after provenance repair |
| provenance committed-range pre-closure / pre-push | PASS for each material and continuity range |
| provenance remote receipt | `29346790b`, equal to `origin/main` after push |
| public dedicated harness | PASS, 69/69 |
| public full provenance autorun | `N/A_WITH_REASON`: 24 projection-profile failures from intentionally absent private surfaces |
| public diff hygiene | PASS |
| public corrective commit receipt | `27137db4d`, equal to public `origin/main` after push |

## Decision

The implementation is accepted with bounded claims. Provenance is restored as
the authority, the public-safe kit is projected from it, and the five internal
evidence records are removed through a normal forward public commit. The
original public-first publication is rejected as a valid CVF synchronization
route. No public history was rewritten.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: operator-authorized incident recovery, not a dispatched work order | recovery scope and authority recorded in this review | N/A with reason |
| Worker return | N/A with reason: reviewer/closer performed the bounded repository recovery directly | Git and harness receipts recorded below | N/A with reason |
| Completion review | `docs/reviews/CVF_PUBLIC_FIRST_GOLDEN_DOWNSTREAM_BOOTSTRAP_RECOVERY_2026-07-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_PUBLIC_FIRST_GOLDEN_DOWNSTREAM_BOOTSTRAP_RECOVERY_2026-07-23.md` | reviewer/closer decision and receipts present | PASS |
| Provenance material | provenance commits through `d82127d76` | committed-range pre-closure and pre-push PASS | PASS |
| Provenance continuity | provenance commit `29346790b` | equals provenance `origin/main` after push | PASS |
| Public correction | public commit `27137db4d` | equals public `origin/main` after push | PASS |
| Public private-evidence removal | five named bootstrap execution-evidence files | deletion set in public commit `27137db4d` | PASS |
| Dedicated public validation | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | 69/69 assertions PASS in public clone | PASS |
| Full public governance bundle | N/A with reason: private provenance bundle has no bounded public-projection profile | 24 projection-profile failures classified as F7 | N/A with reason |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | unchanged generated aggregate; corpus registry gate PASS | PASS |
| Registry Markdown | `docs/reference/agent_defect_intelligence/README.md` | ADIF-0050 index row committed in initial recovery material | PASS |
| External evidence digest | N/A with reason: no external evidence digest was created or consumed | repository and local test evidence only | N/A with reason |
| System loop interlock | N/A with reason: no system loop interlock changed | repository projection recovery only | N/A with reason |
| Roadmap state | N/A with reason: no roadmap opened or closed | incident recovery only | N/A with reason |
| Session continuity | active session front door/state/handoff after this material closure | dedicated session-sync follows this closure commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Provenance acceptance | reviewed material and continuity at `29346790b` | PASS |
| Public projection acceptance | corrective public commit `27137db4d` | PASS |
| Bootstrap behavior | 69/69 assertions PASS in both provenance and public clones | PASS |
| Private evidence boundary | five internal records absent from public and retained in provenance | PASS |
| Runtime receipt evidence | N/A with reason: no provider or governed runtime was invoked | N/A_WITH_REASON |
| Query acceptance evidence | N/A with reason: no query contract was exercised | N/A_WITH_REASON |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | local private provenance workspace and sibling public-sync clone |
| Session or invocation | golden downstream public-first recovery, 2026-07-23 |
| Working directory | repository root |
| Command or tool surface | Git read/fetch/cherry-pick-no-commit, local PowerShell harness, Python governance gates, apply_patch |
| Target paths | imported 22-path tranche, this audit, ADIF-0050, and public corrective projection |
| Allowed scope source | operator instruction to classify and synchronize the misplaced public-first learning tranche |
| Before status evidence | provenance `e26253e25`; public `571cb21b7`; 17 missing and 5 divergent paths |
| After status evidence | provenance `29346790b`; public `27137db4d`; both matched their `origin/main` after push |
| Diff evidence | staged provenance changed set and later committed public correction |
| Approval boundary | recovery and synchronization only; no force push, provider, runtime, deployment, or external-agent invocation |
| Claim boundary | repository recovery and local bootstrap evidence only |
| Agent type | reviewer/closer and session-sync steward |
| Invocation ID | `public-first-bootstrap-recovery-20260723` |
| Expected manifest | imported tranche, recovery audit, ADIF entry/index, later continuity receipt |
| Actual changed set | provenance recovery/material/continuity commits `a47f3d71f`, `ede6633f1`, `af7a05c9c`, `8184e83ec`, `d82127d76`, `29346790b`; public 16-path corrective commit `27137db4d` |
| Manifest delta | five private evidence files removed only from public; public-safe durable references, guard, scripts, harness, and mapped front doors retained |
| Deletion or rename disposition | public-only deletion of five private evidence records; no provenance deletion |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is the private recovery and authority record. Public-safe product
surfaces are projected separately after provenance acceptance.

## Claim Boundary

This audit closes only the repository recovery and public projection boundary.
It does not prove hosted or provider behavior and does not authorize any
CLI/MCP agent invocation.
