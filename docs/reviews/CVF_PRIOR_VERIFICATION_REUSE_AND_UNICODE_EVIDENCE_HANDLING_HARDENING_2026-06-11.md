# CVF Prior Verification Reuse And Unicode Evidence Handling Hardening

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-11

Owner: CVF governance control plane

---

## Purpose

Record and close the governance-control-plane learning promoted from the EC-T4
worker finding about redundant binary hash recomputation and Unicode path
handling friction.

---

## Scope / Target / Owner Boundary

Target scope:

- work-order authoring template pointer;
- work-order authoring hardening addendum;
- new prior verification reuse and Unicode evidence handling standard.

Out of scope:

- EC-T4 source metadata decisions;
- EC-T5 readiness;
- runtime parser, retriever, provider, or application changes;
- public-sync export.

---

## Target / Source

Target artifacts:

- `docs/reference/CVF_PRIOR_VERIFICATION_REUSE_AND_UNICODE_EVIDENCE_HANDLING_STANDARD_2026-06-11.md`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md`

Source signal:

- operator-reported EC-T4 worker postmortem about redundant SHA-256
  recomputation and Unicode path handling friction.

---

## Findings / Position

The EC-T4 worker reported two avoidable execution frictions:

- the work order wording was read as requiring fresh SHA-256 recomputation for
  six binary files even though T11B had already recorded `HASH_MATCH` and
  `sizeMatch: true`;
- PowerShell text reading on Unicode-heavy extracted-text paths failed and
  required a UTF-8-safe fallback reader.

These are not only worker mistakes. They are reusable authoring-control
findings because the dispatch packet did not force an explicit choice between
prior verification reuse and fresh recomputation, and did not spell out
Unicode-path handling before execution.

---

## Risk / Corrective Action

Risk:

- repeated worker latency from unnecessary binary hashing;
- inconsistent evidence strength when workers recompute despite valid prior
  verification;
- avoidable shell/path failures on Unicode evidence filenames;
- future orchestrators relying on prose interpretation instead of an explicit
  verification mode.

Corrective action:

Added canonical standard:

`docs/reference/CVF_PRIOR_VERIFICATION_REUSE_AND_UNICODE_EVIDENCE_HANDLING_STANDARD_2026-06-11.md`

Updated the canonical work-order template pointer without increasing template
line count:

`docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`

Updated the authoring hardening addendum with a reusable section that requires
an `Evidence Reuse And Encoding Plan` for applicable work orders:

`docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md`

---

## Guard / Template Effect

Future applicable work orders must choose one verification mode:

- `REUSE_PRIOR_VERIFICATION`
- `RECOMPUTE_REQUIRED`
- `REVIEWER_RECOMPUTE_ONLY`

Future applicable work orders must record:

- prior verification artifact and anchor when reusing evidence;
- recompute reason when fresh recomputation is required;
- literal-path and UTF-8-safe handling when non-ASCII evidence paths appear;
- extracted-text authority boundary.

---

## Maintainability Evidence

The canonical template was already at its 1200-line threshold before this
batch. The fix did not append detailed rules into the template. It moved the
new detailed rule into a separate reference standard and kept the template as a
compact pointer surface.

Required follow-up gate:

`python governance/compat/check_governed_file_size.py --enforce`

---

## Finding-To-Governance Learning Disposition

Defect class: GOVERNANCE_CONTROL_PLANE_AUTHORING_GAP

Learning lane: governance/control-plane learning

Escalation state: RULE_PROMOTED_TO_STANDARD

Reusable control action: STANDARD_ADDED, TEMPLATE_UPDATED

Machine-check state: MACHINE_CHECK_CANDIDATE

Machine-check candidate: dispatch-quality or markdown structural check should
flag applicable work orders that cite prior manifests, T11B verification,
external evidence digests, source bundles, or Unicode-path extracted text but
lack an `Evidence Reuse And Encoding Plan`.

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| EC-T4 dispatch wording allowed redundant binary hash recomputation and omitted Unicode-path handling instructions | `ORCHESTRATOR_PACKET_GAP` | `GOVERNANCE_CONTROL_PLANE` | `STANDARD_ADDED`; `TEMPLATE_UPDATED`; `MACHINE_CHECK_CANDIDATE` | Add a future dispatch-quality or markdown structural check for missing `Evidence Reuse And Encoding Plan` when prior verification, external evidence digest, source bundle, or Unicode-path extracted text is cited |

Worker blame closure: N/A_WITH_REASON - the worker made an execution choice,
but the reusable defect belongs in work-order authoring control because future
agents should not have to infer reuse versus recompute from prose.

---

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `N/A with reason` | bounded governance-hardening review, not a delegated worker order | N/A with reason |
| Completion or reviewer artifact | `docs/reviews/CVF_PRIOR_VERIFICATION_REUSE_AND_UNICODE_EVIDENCE_HANDLING_HARDENING_2026-06-11.md` | `Status: CLOSED_PASS_BOUNDED`, claim boundary, learning disposition, public export disposition | PASS |
| Roadmap state | `N/A with reason` | operator-authorized immediate hardening from EC-T4 finding | N/A with reason |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no registry mutation authorized in this governance authoring batch; blocked if treated as corpus/search/classification closure input | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no registry mutation authorized in this governance authoring batch; blocked if treated as corpus/search/classification closure input | BLOCKED with reason |
| External evidence digest | `N/A with reason` | no external evidence artifact introduced | N/A with reason |
| System loop interlock | `docs/reference/CVF_PRIOR_VERIFICATION_REUSE_AND_UNICODE_EVIDENCE_HANDLING_STANDARD_2026-06-11.md`; `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md` | standard added; template pointer updated; addendum section added | PASS |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V17_2026-06-07.md` | current mode and next allowed move updated while EC-T5 remains blocked | PASS |

---

## Claim Boundary

This closure claims only governance authoring hardening for prior verification
reuse and Unicode evidence handling. It does not claim runtime behavior,
provider behavior, extraction quality, legal/policy freshness, EC-T5 readiness,
production readiness, public readiness, or release readiness.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-hardening batch. Public export requires a
separate public-sync mapping and operator decision.
