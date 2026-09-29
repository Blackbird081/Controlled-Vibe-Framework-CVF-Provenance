# CVF Private Provenance Registry Reconciliation Roadmap

Memory class: governed-roadmap

Status: CLOSED_PASS_BOUNDED

Date: 2026-08-27

## Purpose

Restore one truthful generated user-skill registry owner family in the private
provenance repository by importing the already accepted public reconciliation
without repeating semantic analysis or creating another public-release lane.

## Authorization / Decision

The operator directed continuation under the standing rule that serious,
source-backed defects may be repaired when value exceeds time, latency and
quota cost. PPRR-R1 is admitted as one tranche only. It has no automatic R2.

## Current Evidence

- Private HEAD `91fff28bb72235489aafe95883385efe761962de` has 62 source skills but
  335 generated user records; its unchanged validator fails on count, broken
  links and index drift.
- Public HEAD `af957e279a8118b152d957a29f5731c6304a86bf` has the same 62 source
  path manifest, 62 generated records, the accepted generator regression
  suite, and a passing unchanged validator.
- The source-name manifest digest is identical in both repositories:
  `sha256:a08b90d243529f81cdaff2b2490451a99d6d432f78fe7f8c6c4896e834f3ff19`.
- PSRR-R1 and AGTR-R1 already supplied independent review and exact-SHA hosted
  proof for the public generated owner and agent-record family.

## Scope / Target / Owner Boundary

PPRR-R1 may change only the private generator, its focused test, the generated
user-record family and index, plus one named private worker return. The public
repository is a clean, exact-commit read-only comparison source.

The worker must reproduce the accepted public bytes for the generator, test,
index and 62 desired records. Private stale generated records may be deleted
only when their basenames are absent from the accepted 62-record manifest.
The 62 private source skill files and every non-registry owner remain read-only.

## Design Control Gate

Accepted public bytes are the only implementation source. Before mutation the
worker must reconcile the exact 65-file public owner manifest, private stale
manifest and identical 62-path source-name digest. Any mismatch stops the
tranche. Validator or cleaner changes, semantic edits and inferred filenames
are forbidden.

## Tranche Value Admission

| Factor | Decision |
| --- | --- |
| outcome consumer | maintainers relying on private local governance and provenance truth |
| severity | P1 because a canonical local governance validator is persistently red |
| finding evidence | OBSERVED at private HEAD and independently bounded by PSRR-R1 |
| root cause | independent provenance drift: accepted public generated owner was never synchronized back to private |
| marginal value | one owner-family import restores local validation and eliminates 273 stale-record excess |
| cost ceiling | one no-commit worker pass, zero provider calls, no semantic re-review of stale generated content |
| consolidation key | generator, focused test, generated USR family and index move atomically |
| stop condition | stop on source-manifest mismatch, public drift, non-generated owner need or second tranche |
| disposition | CONTINUE_HIGH_VALUE for PPRR-R1 only |

## Work Plan

1. Capture private and public HEAD, branch, remote, status and empty staging.
2. Recompute source and generated manifests in both repositories.
3. Copy exact accepted public generator, focused test, index and 62 records to
   private; delete only private manifest-stale generated records.
4. Prove every imported file matches the public exact-commit byte hash.
5. Run focused generator tests, check mode, unchanged private validator,
   idempotence, diff hygiene and the worker-return fast gate.
6. Return all changes uncommitted for independent reviewer acceptance.

## Acceptance Criteria

- Private user source count and generated record count are exactly 62/62.
- The unchanged private validator exits zero for user, agent and source skills.
- Generator, test, index and all 62 records match public HEAD `af957e279...`.
- Second generator apply produces no diff and check mode exits zero.
- No source skill, agent record, validator, workflow, public file, product,
  dependency, continuity or unrelated path changes.
- Private and public staging remain empty; both HEADs remain unchanged by the
  worker.
- Reviewer owns any commit and closure; no public push or hosted rerun is
  required because the public accepted bytes do not change.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | private generated user registry | static provenance/read-model repair only | exact hashes, focused tests and validator | N/A with reason: no adapter or runtime change | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | unchanged public registry | no external surface change | accepted public exact commit | no CLI/MCP behavior is introduced | `DEFERRED_WITH_REASON` |

## Verification / Evidence

Evidence must include dual repository state, source-name digest, desired and
stale manifests, exact SHA-256 comparison for 65 accepted owner files,
focused test total, generator check and second-apply result, full unchanged
validator output, exact changed/deleted paths and worker no-commit proof.

## Non-Goals

No public mutation, semantic skill rewrite, validator weakening, source-skill
change, agent-record change, workflow change, dependency upgrade, provider or
live call, secret access, merge, deploy, Netlify action, PPRR-R2 or successor.

## Tranche Successor Authority

```json
{
  "schemaVersion": "cvf.trancheSuccessorAuthority.v1",
  "declaredCap": 1,
  "authorizedOrdinals": [1],
  "currentAuthorizedOrdinal": 1,
  "successorRule": "NO_AUTOMATIC_SUCCESSOR"
}
```

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: N/A with reason: generated registry parity is not package-skill promotion.

Target lifecycle state: unchanged.

Prior phase evidence: PSRR-R1 accepted generated owner at public exact commit.

Next forbidden skip: no activation, loading, promotion or runtime eligibility.

Runtime/provider proof: N/A with reason: deterministic local files only.

Claim boundary: private registry parity only.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: PPRR-R1 repairs private provenance to match already exported public
bytes. The public-sync repository is read-only and receives no new artifact.

## Next Allowed Move

Execute PPRR-R1 as one no-commit worker pass. Independent reviewer then decides
bounded acceptance and private materialization. No PPRR-R2 is implied.

## Claim Boundary

This roadmap authorizes one private generated-owner reconciliation candidate.
It does not authorize public mutation, semantic authority changes, runtime,
provider, merge, deployment or successor work.

## Closure Evidence

- Independent review accepted the reconciliation at private material commit
  `9cfdc6af838fcf3818c075f84df1be3faf5183e5`.
- Final registry truth is 62 user, 34 agent, and 62 source skills; the
  unchanged validator passes.
- Focused generator tests pass 10/10; generator check reports 62 unchanged,
  zero add/update/delete, and unchanged index.
- Reviewer repair added one deterministic local encoding-exception marker.
  After removing that marker, all 62 records plus index match public source
  (63/63); generator and test are the only two `ADAPTED_WITH_REASON` files.
- Worker-return fast gate passed, reviewer-fast passed 66/66, and material
  pre-commit passed 87/87.
- Public clone remained clean and unchanged; no provider, secret, push,
  deployment, merge, or Netlify action occurred.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_PPRR_R1_PRIVATE_PROVENANCE_REGISTRY_RECONCILIATION_2026-08-27.md` | `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_PPRR_R1_PRIVATE_PROVENANCE_REGISTRY_RECONCILIATION_WORKER_RETURN_2026-08-27.md` | `REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED`; material `9cfdc6af838fcf3818c075f84df1be3faf5183e5` | PASS |
| Roadmap state | this roadmap | `CLOSED_PASS_BOUNDED`; no PPRR-R2 | PASS |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | PPRR-R1 closed evidence and fresh value-gated next move | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V59_2026-08-11.md` | `pprr_r1_closed_pass_bounded` | PASS |
| External evidence digest | N/A with reason: private-only local reconciliation | public clone unchanged at `af957e279a8118b152d957a29f5731c6304a86bf` | N/A WITH REASON |
| System loop interlock | one-tranche cap | terminal close; automatic PPRR-R2 forbidden | PASS |
| Session continuity | bootstrap, state sources, aggregate, front door, handoff | `pprr_r1_closed_pass_bounded` | PASS |

## Final Next Allowed Move

PPRR-R1 is terminally closed. Select a fresh roadmap only from a serious,
source-backed, non-duplicate finding whose expected value exceeds its
time/latency/quota cost. Do not create PPRR-R2 automatically. PR merge and
deployment remain explicit operator checkpoints.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_governed_artifact_authoring.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_package_skill_productionization_pipeline.py` |
| literalTokensReviewed | active roadmap status, tranche cap, dual-agent rows, private-only export disposition and claim boundary |
| gateRunPurpose | confirm a single source-backed remediation tranche with no automatic successor |
| claimBoundary | structural conformance does not prove imported byte identity or validator success |
