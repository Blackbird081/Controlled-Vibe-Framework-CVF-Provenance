# CVF GC-018 Baseline - ACEL G1 T2D Source-Owner Establishment

Memory class: governed-dispatch-baseline

docType: baseline

Status: APPROVED_FOR_SOURCE_OWNER_ANALYSIS_ONLY

Date: 2026-09-18

Batch ID: ACEL-G1-T2D-SOURCE-OWNER-ESTABLISHMENT

Dispatch base HEAD: `e8a446e9c11a6912dd1d593e73369402e56a3190`

Decision owner: Local orchestrator/reviewer; operational owner assignment reserved to operator.

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Bound an internal, documentation-only source-owner establishment analysis for
the four trust dependencies of the accepted hypothetical T2C design. The
worker may discover existing governed owners or propose accountable owner
options, but cannot appoint an operational owner or create authority by
writing a document.

## Architecture Decision

Retain the T2C Ed25519 receipt topology as design-only. Reconcile existing
CVF sources first. For each dependency, distinguish a verified current owner,
an adjacent non-owner, a proposed new owner requiring operator assignment,
and unresolved source absence. No row may be promoted from proposal to
operational authority without source evidence and Local/operator disposition.

## Dependency Release Evidence

| Dependency | Evidence | Release condition | Disposition |
|---|---|---|---|
| T2C design-only acceptance | `docs/reviews/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_COMPLETION_2026-09-17.md`, Decision / Disposition | permits bounded owner analysis, not implementation | ACCEPT_FOR_ANALYSIS_ONLY |
| Local owner reconciliation | `docs/reviews/CVF_ACEL_G1_T2C_SOURCE_OWNER_RECONCILIATION_LOCAL_DECISION_2026-09-18.md`, Findings / Position | four missing owner sources disclosed | ACCEPT_FOR_ANALYSIS_ONLY |
| Operator scope choice | 2026-09-18 operator response approving the recommended governance/design tranche, recorded in the Local decision | author a scoped packet; no owner appointment | ACCEPT_FOR_PACKET_AUTHORING_ONLY |
| Operational key and lookup authority | T2C Owner Ledger | separately source-verified owner and later operator grant | BLOCKED_SOURCE_NOT_FOUND |

## Proposed Tranche

T2D produces a source-backed owner-option matrix, authority-boundary design,
and no-commit worker return. Search current CVF governed sources before
proposing anything new. Existing owner candidates need exact path/section and
consumer evidence; missing owners remain `BLOCKED_SOURCE_NOT_FOUND` or
`PROPOSED_OPERATOR_DECISION`, never `VERIFIED`. Local reviews all four rows
together. No code, key, signer, receipt, live lookup or candidate admission.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | T2D owner-analysis documents | analysis only; worker cannot appoint owner or commit | T2C review and Local decision | no runtime adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no interface opened | external ingress, credentials and mutation excluded | no G1 adapter source verified | adapter deferred; no CLI/MCP work | `DEFERRED_WITH_REASON` |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T2C is design-only | CURRENT_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_COMPLETION_2026-09-17.md` | Decision / Disposition | T2C completion review | Local reviewer | ACCEPT |
| Four operational dependencies remain open | CURRENT_AUTHORITY | `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | Owner Ledger | key governance; trusted context; observation log; issuer lookup | proposed T2C interfaces | ACCEPT |
| Local focused owner search and hold | CURRENT_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2C_SOURCE_OWNER_RECONCILIATION_LOCAL_DECISION_2026-09-18.md` | Findings / Position; Local Decision / Next Boundary | four-row source-owner reconciliation | Local reviewer | ACCEPT |
| Web service-token HMAC as G1 verifier owner | ADJACENT_PATTERN | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | `computeServiceRequestSignature` | service request authentication | Web service-token source | REJECT |
| Agent identity token as G1 verifier owner | ADJACENT_PATTERN | `EXTENSIONS/CVF_ECO_v2.3_AGENT_IDENTITY/src/identity.manager.ts` | `IdentityManager.verify` | agent credential association | identity manager | REJECT |
| Operational G1 verifier-key and live issuer-lookup owner | OWNER_CLAIM | `docs/reviews/CVF_ACEL_G1_T2C_SOURCE_OWNER_RECONCILIATION_LOCAL_DECISION_2026-09-18.md` | focused negative search, not corpus-wide absence | no current owner selected | operator/Local checkpoint | BLOCKED_SOURCE_NOT_FOUND |

## Negative Search And Collision Discipline

Exact source-code query: `rg -n --hidden --no-ignore -i
'ed25519|createPublicKey|verifySignature|jwks|issuer.?registry|verifier.?registry'
EXTENSIONS governance -g '*.py' -g '*.ts' -g '!**/node_modules/**'
-g '!**/.venv/**' -g '!**/dist/**' -g '!**/build/**'` (exit 1). The
Local decision records the focused search over
current repository source and governed docs. The worker may broaden only
where a named owner hypothesis or contradiction justifies it, and must report
roots, exclusions, source locators and unread regions. This is not a complete
repository inventory. T2B/T2C receipt literals are design collisions; Web HMAC,
agent-token and provider API-key rotation are adjacent, not G1 ownership.
Do not infer private-CVF absence from public or provider memory.
Absent-versus-collision disposition: exact operational G1 owner symbols were
not identified in the targeted implementation query; `CVF` is a repository
prefix, `OWNER_CLAIM` is a table classification, `T2D` is this tranche ID,
and `VERIFIED` is a status token. Their other occurrences are not source
authority. Do not claim those tokens themselves are absent.
Same-token collision `createPublicKey`: API symbol in other contexts,
non-authoritative for a G1 registry. Same-token collision
`verifySignature`: generic verification symbol in other contexts,
non-authoritative for a G1 issuer lookup.
- Same-token collision `CVF`: repository prefix, non-authoritative for G1 ownership.
- Same-token collision `OWNER_CLAIM`: table classification, non-authoritative for G1 ownership.
- Same-token collision `T2D`: tranche identifier, non-authoritative for G1 ownership.
- Same-token collision `verifySignature`: generic symbol, non-authoritative for G1 ownership.
- Same-token collision `CVF_ACEL_G1_T2C_SOURCE_OWNER_RECONCILIATION_LOCAL_DECISION_2026`: existing Local review filename, non-authoritative for operational G1 ownership.
- Same-token collision `PROPOSED_OPERATOR_DECISION`: planning disposition, non-authoritative for an appointed owner.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | Source Verification column names and ACCEPT/REJECT/source-not-found dispositions; dispatch envelope placement; active closeability gate IDs; baseline structural headings |
| gateRunPurpose | confirm packet shape after source-owner boundary selection, not discover a real operational owner |
| claimBoundary | read-ahead proves literal preparation only, not operational owner truth |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`. `python governance/compat/run_adif_defect_resolver.py --task-class DOC_CHANGE --role dispatcher --lifecycle-phase pre-dispatch` returned zero candidates on 2026-09-18.

Returned defects: NONE_RETURNED

## Evidence / Verification Boundary

Passing document checks proves packet conformance only. A proposed owner,
registry path or interface is not key custody, issuer authority, live lookup
or candidate-admission proof. Any future source owner needs exact governed
authority and operator approval; future implementation requires another
separately scoped packet.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source-owner analysis; public sync is not authorized.

## Claim Boundary

This baseline allows analysis and recommendations only. It does not assign
real owners, alter T2C's design-only acceptance, or release the parked G1
evidence and downstream work.
