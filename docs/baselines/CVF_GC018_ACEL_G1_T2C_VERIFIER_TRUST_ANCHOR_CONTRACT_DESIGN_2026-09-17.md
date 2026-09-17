# CVF GC-018 Baseline - ACEL G1 T2C Verifier Trust-Anchor Contract Design

Memory class: governed-dispatch-baseline

Status: APPROVED_FOR_HYPOTHETICAL_DESIGN_ONLY

Date: 2026-09-17

Batch ID: ACEL-G1-T2C-VERIFIER-TRUST-ANCHOR-CONTRACT-DESIGN

Authoring base head: `3796ff4ce85b2343b857be7da5bc69cb9447266f`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision and reviewer owner: Local orchestrator/reviewer

Worker role: one shared-workspace `INTERNAL_AGENT`; release is limited to hypothetical documentation under the operator's 2026-09-18 audit-and-dispatch instruction.

## Purpose

Prepare a separate documentation-only T2C contract-design tranche after the Local architecture decision at `1c5c01675`. T2B remains rejected as a G1 implementation root. The release does not convert algorithm selection into a claim that a CVF verifier-key registry, signer or live lookup already exists.

## Architecture Decision

The selected direction is a verifier-controlled Ed25519 signing key, a public-key registry independently governed by CVF, and a receipt whose signed deterministic preimage binds the exact authority and source-owned lookup result. Both TypeScript decision-time admission and Python persisted-evidence checking must use the same verification contract. A public content digest, `verifiedBy` literal, receipt-supplied public key or signed but unproven lookup claim is insufficient. The Local decision is `docs/reviews/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_LOCAL_ARCHITECTURE_DECISION_2026-09-17.md`.

## Dependency Release Evidence

| Dependency | Verified evidence | Release rule | Disposition |
|---|---|---|---|
| T2B root-contract rejection | `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_INDEPENDENT_REVIEW_2026-09-17.md`, T2B-RV-F1 | New tranche must not repair or accept T2B in place | SATISFIED_FOR_PLANNING_ONLY |
| Local algorithm/topology choice | T2C Local decision at `1c5c01675` | Design direction selected, no implementation grant | SATISFIED_FOR_PLANNING_ONLY |
| G1 verifier-key registry authority | Focused Local search below found no source-owned G1 registry, write authority or key lifecycle | Worker may define a proposed interface only; existing-owner, operational-key and admission claims remain forbidden | SATISFIED_FOR_HYPOTHETICAL_DESIGN_ONLY |
| Genuine issuer-registry lookup provenance | T2B documents only postulate an out-of-scope lookup; the Local review rejects self-authored receipts | Worker may define a proposed provenance interface only; all candidate authority remains `UNVERIFIED` without source-owned observation | SATISFIED_FOR_HYPOTHETICAL_DESIGN_ONLY |

The operator's 2026-09-18 audit-and-dispatch instruction releases only hypothetical documentation, not the two missing operational dependencies. Local must still pin the dispatch base and pass pre-dispatch gates before invocation. Any later implementation requires a separate source-backed authority decision.

## Proposed Tranche

The operator has authorized an explicitly hypothetical contract-only design with no existing-owner claim. One `INTERNAL_AGENT` may author a human trust-anchor contract, matching machine-readable manifest and no-commit return after pre-dispatch admission. The worker may define proposed interfaces, not create keys, registry entries, signer wiring, lookup runtime, TypeScript/Python implementation, tests or checker changes. No automatic successor or T2B repair is permitted.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | three hypothetical documentation outputs named in the work order | one worker without commit, key, lookup or implementation authority; Local reviews | operator 2026-09-18 instruction and Local T2C decision | N/A with reason: no external adapter for internal documentation | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no selected G1 external adapter owner | no CLI/MCP execution or public claim | external/local coordination method and this exclusion | `DEFERRED_WITH_REASON`: external adapter design is out of scope | `DEFERRED_WITH_REASON` |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified locator | Disposition |
|---|---|---|---|---|
| T2B receipt content hash is forgeable | LOCAL_REVIEW_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_INDEPENDENT_REVIEW_2026-09-17.md` | T2B-RV-F1 counterexample | ACCEPT |
| Ed25519 is the selected future direction | LOCAL_DESIGN_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_LOCAL_ARCHITECTURE_DECISION_2026-09-17.md` | Local Architecture Decision | ACCEPT |
| CVF audit manifest HMAC is a separate scope | ADJACENT_PATTERN_ONLY | `docs/reference/CVF_LIVE_EVIDENCE_MANIFEST_AND_RERUN_STANDARD_2026-06-06.md` | Signature Boundary | REJECT |
| Web service-token HMAC is a separate scope | ADJACENT_PATTERN_ONLY | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | `computeServiceRequestSignature` | REJECT |
| Agent identity token store is a separate scope | ADJACENT_PATTERN_ONLY | `EXTENSIONS/CVF_ECO_v2.3_AGENT_IDENTITY/src/identity.manager.ts` | `IdentityManager.verify` | REJECT |
| Existing G1 verifier-key registry and lookup provenance | OWNER_CLAIM | `docs/reviews/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_LOCAL_ARCHITECTURE_DECISION_2026-09-17.md` | Negative Search And Collision Discipline; unresolved owner statement | REJECT |
| Ed25519 and canonical JSON algorithm references | EXTERNAL_PATTERN_ONLY | `https://www.rfc-editor.org/rfc/rfc8032.html`; `https://www.rfc-editor.org/rfc/rfc8785.html` | RFC 8032 sections 5/7; RFC 8785 JCS | REJECT |

## Negative Search And Collision Discipline

- Same-token collision `CVF`: repository prefix rather than a verifier-key registry.
- Same-token collision `T2B`: rejected predecessor tranche rather than accepted authority.

Search roots: `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM`, with `CVF_SESSION` used only for current continuity. Exact search command: `rg -n --hidden 'Ed25519|verifierKeyRegistry|issuerVerifierPublicKey|issuerVerifierPrivateKey|trusted public.key registry|registry lookup provenance' docs governance EXTENSIONS ECOSYSTEM CVF_SESSION`, followed by `rg -n --hidden 'createPublicKey|verifySignature|publicKey|jwks|JWK|signing key|lookupResult' EXTENSIONS governance docs/reference docs/roadmaps -g '*.ts' -g '*.py' -g '*.md' -g '*.json'`. Coverage includes source, tests, docs and JSON; this is a focused owner search, not a complete-corpus absence claim. Same-token collisions include the T2B rejected receipt/status design and unrelated HMAC/token owner surfaces. Absent-versus-collision disposition: no independently governed G1 verifier-key or genuine lookup owner was source-verified; adjacent authentication mechanisms are not binding for G1. Both proposed artifact paths returned `Test-Path=False` before authoring.

Checker-token collision ledger (these occurrences are not G1 owner evidence):

- Same-token collision `CVF`: repository prefix, not a verifier-key registry.
- Same-token collision `RFC`: external algorithm reference, not CVF trust governance.
- Same-token collision `JCS`: canonicalization pattern, not verifier authentication.
- Same-token collision `T2B`: rejected predecessor tranche, not accepted authority.
- Same-token collision `OWNER_CLAIM`: Source Verification claim class, not a registry symbol.
- Same-token collision `HOLD_SOURCE_NOT_FOUND`: packet lifecycle status used elsewhere, not evidence that a G1 registry owner exists.
- Same-token collision `CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_LOCAL_ARCHITECTURE_DECISION_2026`: existing Local design path, not an operational key/lookup owner.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind held-dependency --batch-id ACEL-G1-T2C-VERIFIER-TRUST-ANCHOR-DESIGN --title "G1 T2C Verifier Trust Anchor Design" --date 2026-09-17 --base 3796ff4ce85b2343b857be7da5bc69cb9447266f --commit-mode WORKER_MUST_NOT_COMMIT --dependency G1-T2B-TRUST-ANCHOR-PARKED --stdout` |
| generatedProfile | held-dependency plus no-commit worker profile, read as guidance only |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced operator-pending generic hold with source-not-found owner gate and exact G1 claim boundary |
| checkerReadAheadConfirmation | work-order dispatch quality, prompt envelope, gate-to-role closeability and markdown structure sources inspected before authoring |
| docOnlyNewFields | planned signed verifier receipt, trusted key registry lookup and genuine lookup provenance contract; none implemented |
| claimBoundary | scaffold does not release dependency or grant dispatch |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`. `python governance/compat/run_adif_defect_resolver.py --task-class DOC_CHANGE --role dispatcher --lifecycle-phase pre-dispatch` returned zero candidates and `NONE_RETURNED` on 2026-09-17. This does not replace source verification.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | held status, Source Verification disposition, negative-search evidence, dependency-release and claim-boundary headings |
| gateRunPurpose | confirm held packet shape after Local source search, not discover an owner by checker pass |
| claimBoundary | gates do not establish trust material or live lookup truth |

## Evidence / Verification Boundary

RFC 8032 supplies Ed25519 signing/verification and vectors; RFC 8785 supplies a JSON canonicalization pattern. Neither governs CVF key custody or proves issuer lookup. The later design must distinguish signature validity, key authorization and actual lookup provenance, with `UNVERIFIED` as the admission result whenever any is missing.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private held design packet; no public-sync authority.

## Claim Boundary

This releases only hypothetical contract documentation after a passing pre-dispatch gate. It does not accept T2B, modify thirteen parked paths, create or use keys, run a registry lookup, implement code, invoke providers, publish or deploy.
