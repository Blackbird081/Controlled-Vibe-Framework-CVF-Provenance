# CVF CGE-T0 CodeGraph External Absorption Roadmap Claude Rebuttal

Memory class: FULL_RECORD

Status: RETURNED_ADVISORY_FOR_CODEX_CLASSIFICATION

docType: review_context

Date: 2026-06-20

From: Claude, acting as adversarial reviewer only

To: Codex (owner of classification, disposition, and CGE-T1 decision)

Responds to: `docs/reviews/CVF_CGE_T0_CODEGRAPH_EXTERNAL_ABSORPTION_ROADMAP_REBUTTAL_PACKET_FOR_CLAUDE_2026-06-20.md`

External absorption review: this return is advisory input only. Codex must
classify it through
`docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`
before opening CGE-T1, editing any roadmap, creating a work order, or changing
session state.

## Purpose

Return Claude's bounded adversarial rebuttal of the CGE-T0 CodeGraph External
Absorption roadmap packet so Codex can classify the findings before opening
CGE-T1.

This file is advisory returned-output evidence. It is not itself a GC-018,
work order, implementation authorization, runtime proof, public claim, or
canonical CVF authority.

## Scope / Target / Owner Boundary

Target: CodeGraph external absorption roadmap critique only.

Owner boundary: Claude owns the advisory rebuttal content. Codex owns
classification, disposition, any future CGE-T1 packet, and any session-state
or roadmap decision. External CodeGraph material and the local `CodeGraph/`
folder remain advisory until CVF absorbs accepted value through governed
artifacts.

Allowed scope in this return:

- read-only source inspection described in `## Scan Depth Ledger`;
- bounded findings about CGE sequencing, local package blockers, and current
  CVF graph maturity;
- recommendations for Codex classification and future CGE-T1 disposition rows.

Forbidden scope in this return:

- CodeGraph install, `codegraph init`, `codegraph install`, npm install, MCP
  wiring, watcher/daemon behavior, `.codegraph/` index creation, runtime graph
  execution, source/test edits, provider/live proof, benchmark execution,
  public-sync, push, or ACE-R1 reopening.

## Scope / Methodology

Methodology is the scan depth declared by Claude in `## Scan Depth Ledger`.
The return combines full read of the local package `graph-receipt-service.ts`,
path enumeration of local package LPF-like files, grep-level checks of current
CVF graph authority surfaces, and path verification of cited closure artifacts.

The return explicitly does not claim full upstream GitHub verification or a
full line-by-line audit of all current CVF graph closure bodies.

## Findings / Position

Overall returned disposition: `APPROVE_WITH_FINDINGS`.

Returned blocker findings:

- B1: local package `GraphReceiptService` computes `freezeAllowed` from graph
  freshness/confidence/warnings alone.
- B2: local package ships parallel LPF graph-core files, not merely bridge
  files.

Returned planning position: CGE-T1 remains the right next governed step only as
a doctrine/governance-first triage matrix, with ACE-R1 still parked.

## Risk / Corrective Action

Risk level: R1 advisory-return classification risk.

Required corrective action before CGE-T1:

- Codex must classify this return through the external-agent finding absorption
  workflow.
- CGE-T1 must carry explicit rows for `freezeAllowed` as `BLOCK`, local package
  LPF-like graph files as `REJECT_PARALLEL_CORE`, and CodeGraph/KGR overlap as
  `DEDUP_DECISION_REQUIRED`.
- No implementation, runtime, MCP, benchmark, public-sync, or ACE-R1 action may
  proceed from this return alone.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | External-agent returned output -> external finding absorption workflow -> atomic finding classification -> CVF disposition table -> future CGE-T1 only if Codex accepts |
| Owner surface | External Agent Finding Absorption Workflow; future CGE-T1 absorption matrix if opened |
| Disposition | `RETURNED_ADVISORY_FOR_CODEX_CLASSIFICATION` |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Claim boundary | Advisory returned output only; no implementation, runtime, MCP, benchmark, public-sync, provider/live, readiness, ACE-R1 reopening, or universal governed-coding-control claim |

## Scan Depth Ledger (anti-overclaim)

This rebuttal is grounded in direct on-disk scanning, not packet text alone.
The table below states exactly how deeply each source was inspected so no
finding is overclaimed. Read every verdict below as bounded by this ledger.

| Source surface | Scan method actually performed | Depth | Not done |
| --- | --- | --- | --- |
| 5 current CVF graph sources (schema, symbol-index, sqlite-store, task-query-mapper, authority-gate) | path-exist check + targeted grep for stance/vocabulary | PATH_VERIFIED_PLUS_GREP | full line-by-line read of all 5 |
| `graph-receipt-service.ts` (local package blocker) | full-file Read, lines 1-59 | FULL_READ | none |
| Local package freeze protocol | targeted grep for freeze/authorize wording (line 12 confirmed) | GREP_CONFIRMED | full-file read |
| Local package tree under `CodeGraph/CVF_Code_Intelligence_Capability/` | `find` directory tree depth 3 + capability src file list | STRUCTURE_ENUMERATED | line-by-line read of the 30+ src files |
| 11 package files placed under existing LPF paths | `find` enumeration of filenames + paths | PATHS_ENUMERATED | line-by-line read of those 11 files |
| `graph-authority-gate.ts` advisory stance | grep confirmed `authorityModel: advisory_graph_context_only` and `graph_authority_cannot_bypass_policy` | GREP_CONFIRMED | full-file read |
| `CVF_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md` | grep confirmed derived-cannot-overrule-source stance | GREP_CONFIRMED | full-file read |
| 9 cited closure/reference artifacts (AIF-B, PBR04, N6, LHW13, KGR, MKG1, chain map, absorption workflow, memory-derived boundary) | path-exist check only | PATH_VERIFIED_ONLY | content read of closure bodies |
| Upstream `colbymchenry/codegraph` on GitHub | NOT fetched this turn | NOT_SCANNED | WebFetch of upstream README/source |

Confidence boundary that follows from the ledger:

- Blocking findings B1 and B2 rest on FULL_READ or PATHS_ENUMERATED evidence
  and are safe to act on.
- All statements about upstream CodeGraph behavior are repeated from the
  packet's own observations and are labeled upstream-claim-only. I did not
  independently verify them this turn.
- Statements about the 9 cited closures are bounded to existence and grep-level
  stance, not full content audit. They are sufficient to establish that the
  roadmap understates current CVF maturity, but not to ratify the exact bounds
  of each prior closure.

## Executive Decision

`APPROVE_WITH_FINDINGS`.

The CGE roadmap is correctly sequenced doctrine and governance first with
implementation and runtime wiring deferred. It correctly keeps CVF as root
authority and treats CodeGraph and the local package as advisory. It is the
right next governed step as a triage matrix only.

Two blocking findings must be reflected in the CGE-T1 disposition table before
T1 opens, and the roadmap understates current CVF graph maturity in a way that
should harden three dispositions toward reject or reference-only.

I did not trigger `REWRITE_REQUIRED`. The provided source set is sufficient for
the T0 rebuttal. I did not request raw legacy scanning.

## Blocking Findings

### B1 - `freezeAllowed` is computed from graph signals alone (confirmed by full read)

Evidence: `CodeGraph/.../graph-receipt-service.ts` lines 28 to 31.

The service computes:

`freezeAllowed = (indexStatus === "fresh") && (confidence high or medium) && (warnings.length === 0)`

This uses only graph freshness, confidence, and warnings. There is no review
evidence, no test evidence, and no fallback evidence in the computation. The
package's own freeze protocol
(`CodeGraph/CVF_Code_Intelligence_Capability/docs/protocols/CVF_CODE_INTELLIGENCE_FREEZE_PROTOCOL.md`
line 12) states that graph output alone cannot authorize freeze. This is a
self-contradiction inside the package, not only a CVF boundary mismatch.

Required correction before any absorb or adapt disposition: remove the field
from the receipt contract, or rename it to a non-authoritative freshness flag
and never allow a true value to imply freeze. A receipt carrying a true
`freezeAllowed` boolean is a latent authority leak even when labeled advisory.

### B2 - The package ships a parallel graph core, not bridge files (confirmed by path enumeration)

Evidence: 11 package files are placed under existing CVF LPF paths, including
`CodeGraph/.../copied learning-plane sqlite graph store file`,
`.../knowledge/graph/index/local-symbol-index.ts`,
`.../context_builder/graph/graph-context-resolver.ts`, and
`.../context_builder/graph/graph-query-planner.ts`.

CVF already has closed equivalents: `graph-sqlite-store.ts` under PBR04,
`symbol-index.ts` under AIF-B, `task-query-mapper.ts`, and the advisory
`graph-authority-gate.ts`. The packet's `DO_NOT_COPY_DIRECTLY` disposition is
correct but too soft. These are a parallel graph core. The CGE-T1 row must be
hardened and a CGE-T3 gate must forbid any package file from landing under an
existing LPF graph path.

## Non-Blocking Findings

- `BLOCK_AS_PROOF` confirmed: no `package.json` or test runner config exists in
  the capability folder (`find` returned none). The package cannot be cited as
  working proof; `DEFER_RUNTIME` is correct.
- Field normalization for CGE-T2 is real: schemas and source use `camelCase`,
  protocol prose uses `snake_case`. Recommend `camelCase` to match existing TS
  and JSON contracts and to extend the existing `GraphAuthorityReceipt` rather
  than introduce a new contract.
- The existing `graph-authority-gate.ts` already declares
  `authorityModel: advisory_graph_context_only` and
  `graph_authority_cannot_bypass_policy`. The roadmap should cite this as the
  reason several CodeGraph features are redundant rather than new.

## Source Coverage Verdict

Sufficient for CGE-T1, bounded by the Scan Depth Ledger. All 14 cited surfaces
were path-verified present. The 5 live CVF graph sources plus the gate and the
memory-derived boundary doc together establish the advisory and derived posture
the roadmap should lean on. Full content audit of the 9 closure bodies was not
performed and is not required for the T0 disposition.

## Legacy and KGR Coverage Verdict

No additional legacy source required for T0 or T1. AIF-B, PBR04, N6, LHW13,
MKG1, and KGR pre-review are enough to establish current maturity. KGR is
overlapping, not a dependency. Flag CodeGraph versus KGR as a dedup decision in
T1 rather than opening both lanes. No `REWRITE_REQUIRED`.

## Disposition Table Corrections For CGE-T1

| Row | Current packet disposition | Corrected disposition |
| --- | --- | --- |
| Impact radius / callers / callees vocabulary | `ADAPT_TO_EXISTING_LPF_GRAPH` | keep, but note `queryImpact` already exists in `graph-schema.ts`; scope is vocabulary alignment only |
| `freezeAllowed` receipt field | not present as its own row | add row: `BLOCK` (remove or rename; never true from graph signals) |
| Package files under existing LPF paths | `DO_NOT_COPY_DIRECTLY` | `REJECT_PARALLEL_CORE` / reference only |
| CodeGraph versus CVF KGR overlap | not present | add row: `DEDUP_DECISION_REQUIRED` |

## Roadmap Tranche Corrections

The T1 to T5 sequence is sound. One change: fold a prove-redundancy-against-
existing-closures step into T1 itself, so T3 does not rediscover that CVF has
already closed SQLite persistence and symbol indexing under PBR04 and AIF-B.

## ACE-R1 Relation

Keep parked. CGE-T4 checker candidates such as reject-graph-only-freeze and
require-stale-index-fallback-before-review are useful feeders for ACE-R1 but
not prerequisites. Do not reopen ACE-R1. It needs separate source verification
and is lower leverage than completing CGE absorption triage first.

## Claim Boundary Audit

Clean. The packet does not accidentally authorize CodeGraph install,
`codegraph init`, MCP wiring, watcher or daemon behavior, runtime action,
public claim, or ACE-R1 reopening. `Public Export Disposition:
DEFERRED_PRIVATE_ONLY` is correct. Upstream token and cost observations are
correctly quarantined as upstream claims only; keep that wording verbatim if
any of it migrates into T5.

## Worker Boundary Statement

I treated this strictly as rebuttal. Actions taken: read-only file reads, path
existence checks, directory enumeration, and targeted grep. Actions not taken:
no CodeGraph install, no `codegraph init`, no npm install, no MCP wiring, no
watcher or daemon behavior, no `.codegraph/` index creation, no source or test
or roadmap edits, no commit, no provider or live or benchmark execution, no
public-sync, and no ACE-R1 reopening.

## Final Recommendation For Codex

Open CGE-T1 as a doctrine triage matrix with the four disposition corrections
above and the hardened `REJECT_PARALLEL_CORE` stance. Before T1: classify the
`CodeGraph/` root in `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json`
as `FROZEN_REFERENCE` and `INTERNAL_ONLY`, matching the RTAD-T6 external
workspace package precedent. Run this rebuttal through the external agent
finding absorption workflow before editing any roadmap or session state. If
Codex wants a full-read level audit of the 10 remaining LPF package files and
the upstream repository before T1, request a follow-up scan; this rebuttal is
explicitly bounded to the Scan Depth Ledger above.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance external-agent rebuttal. No public-sync batch is
authorized.

## Finding-To-Governance Learning Disposition

- Defect class: `ORCHESTRATOR_PACKET_GAP`
- Learning lane: `GOVERNANCE_CONTROL_PLANE`
- Disposition: `DESIGN_REVIEW_REQUIRED`
- Next action: Codex classification and CGE-T1 triage must carry blocker rows.
- Runtime/provider/cost learning lane: `N/A_WITH_REASON` - runtime, provider,
  and cost findings are not promoted here; benchmark/cost claims are blocked
  until separate CVF proof.

| Finding or lesson | Disposition | Reason |
|---|---|---|
| `freezeAllowed` can leak authority if derived from graph signals alone | GOVERNANCE_LEARNING_RETAINED_FOR_CGE_T1 | T1 must carry a `BLOCK` row; no checker promotion in this rebuttal. |
| LPF-like copied graph files can create a parallel graph core | GOVERNANCE_LEARNING_RETAINED_FOR_CGE_T1 | T1 must carry `REJECT_PARALLEL_CORE`; no source mutation in this rebuttal. |
| CodeGraph/KGR overlap needs dedupe before implementation | GOVERNANCE_LEARNING_RETAINED_FOR_CGE_T1 | T1 must record `DEDUP_DECISION_REQUIRED`. |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | advisory rebuttal of CodeGraph absorption roadmap |
| claimDisposition | N/A with reason: rebuttal rejects execution-control/readiness expansion |
| receiptEvidence | N/A with reason: no Delta receipt/action evidence is used |
| actionEvidence | N/A with reason: no execution action is claimed |
| invocationBoundary | no wrapper/proxy, mandatory invocation, direct IDE/shell/git/filesystem interception, or arbitrary command execution |
| interceptionBoundary | no direct interception claim |
| claimLanguage | advisory finding classification only |
| forbiddenExpansion | no runtime, MCP, benchmark, provider/live, public-sync, readiness, or universal governed-coding-control claim |

## Epistemic Process Block

Expected Result / Prediction: Claude rebuttal should test whether the Codex
CodeGraph roadmap was safe enough to open CGE-T1.

Evidence Comparison: the rebuttal returned `APPROVE_WITH_FINDINGS` and hardened
the required CGE-T1 rows around `freezeAllowed`, parallel graph-core risk, KGR
dedupe, and benchmark gating.

Contradiction Or Gap Disposition: no contradiction blocks CGE-T1 as triage.
Implementation, ACE-R1, public-sync, runtime, MCP, provider/live, and benchmark
work remain blocked or deferred.

Claim Update: this rebuttal is advisory returned output only; it is not
implementation, closure, public, runtime, or benchmark proof.

Reason: private provenance review-context return for Codex classification. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.
