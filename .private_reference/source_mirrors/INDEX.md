# CVF External Source Mirror Index

Memory class: PRIVATE_REFERENCE_CONTROL_PLANE

Status: ACTIVE_INDEX

docType: private_reference_index

Date: 2026-06-29

INDEX type: private external source mirror registry

Source authority: pinned upstream repository clone or upstream URL/commit record; external-agent packs are secondary artifacts only

Human-reviewable: yes

Claim boundary: local reference index only; no cloned source payload is tracked, executed, installed, activated, published, or promoted by this index

Public Export Disposition: DEFERRED_PRIVATE_ONLY

## Purpose

Track which upstream repositories have or need local source mirrors for
high-value external absorption.

This index links a source mirror to any derived external-agent pack so future
work can distinguish upstream source facts from secondary interpretation.

## Mirror Ledger

| Mirror ID | Upstream repository | Local mirror path | Pinned commit | Mirror status | Verified date | Tracked file count | Related external-agent pack or folder | Current CVF absorption surface | Source authority disposition | Runtime boundary |
|---|---|---|---|---|---|---:|---|---|---|---|
| `addyosmani__agent-skills` | `https://github.com/addyosmani/agent-skills.git` | `.private_reference/source_mirrors/addyosmani__agent-skills/` | `aba7c4e9695c363e65cb59effe926c7f1d1abe3d` | `CLONED_PINNED` | 2026-06-29 | 96 | `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack/` | AGSK-R2 package backfill candidate; existing ASSF candidate registry entries under `docs/reference/agent_system_skills/registry/entries/` | upstream source mirror must be preferred for skill/package facts; absorption pack is secondary comparison material | no install, hook execution, runtime activation, package activation, provider/live proof, public-sync, or direct import |
| `colbymchenry__codegraph` | `https://github.com/colbymchenry/codegraph.git` | `.private_reference/source_mirrors/colbymchenry__codegraph/` | `da72946d25e112f662f5a60c6b69f363aec60f16` | `CLONED_PINNED` | 2026-06-30 | 409 | `.private_reference/legacy/CVF 28.06/CodeGraph/CVF_Code_Intelligence_Capability/` | CGE-R3 upstream source mirror absorption dispatch; prior CGE-R1/CGE-R2 remain bounded snapshot and correction surfaces | upstream source mirror must be preferred for current CodeGraph facts; legacy snapshot and prior CGE artifacts are secondary comparison material | no install, init, `.codegraph/`, MCP server, watcher, daemon, SQLite index, package activation, checker wiring, provider/live proof, public-sync, or direct import |
| `opendatalab__MinerU` | `https://github.com/opendatalab/MinerU.git` | `.private_reference/source_mirrors/opendatalab__MinerU/` | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` | `CLONED_PINNED` | 2026-07-02 | 425 | `.private_reference/legacy/CVF 28.06/CVF_MinerU_Structured_Extraction_Adapter/` | MinerU source mirror refresh for any future source-verified document-extraction absorption tranche; prior MSEA artifacts remain bounded historical comparison surfaces | upstream source mirror must be preferred for current MinerU facts; old external repo clone and retained adapter folder are secondary historical material only | no install, model download, OCR/VLM/hybrid/remote backend, API/router/Gradio service, RAG write, package activation, checker wiring, provider/live proof, public-sync, or direct import |
| `theswerd__brainless` | `https://github.com/theswerd/brainless.git` | `.private_reference/source_mirrors/theswerd__brainless/` | `4c5d5ab65ff6cfa8dbb6f27cb8c88d9092a48deb` | `CLONED_PINNED` | 2026-07-23 | 321 | `.private_reference/legacy/CVF 23.07/CVF_INTERACTION_PROJECTION/` | EAIC-KR-R1 upstream interaction-pattern verification; future selective product-projection absorption only after existing-owner reconciliation | upstream source mirror is authority for Brainless repository facts and captured UI patterns; CVF Interaction Projection remains a separately authored secondary interpretation and governance-design pack | no dependency install, build, capture harness, agent CLI, MCP, provider/API/account use, package activation, checker wiring, runtime implementation, public-sync, or direct import |
| `nguyennguyenit__pancake-pos-mcp` | `https://github.com/nguyennguyenit/pancake-pos-mcp.git` | `.private_reference/source_mirrors/nguyennguyenit__pancake-pos-mcp/` | `41979fdac4fdf9a8a6f956889c33f19fa3389215` | `CLONED_PINNED` | 2026-07-25 | 98 | `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/` (9 files) | PPMCP-R1 pinned upstream and legacy delta re-intake; pending bounded documentation-only comparison against `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` MCP business adapter contract and related governance owner surfaces | upstream source mirror must be preferred for current pancake-pos-mcp facts; retained legacy folder (tool-contract, approval-gate, risk-classifier, transport-policy, receipt, registry, adapter, and provider-profile interpretation) is secondary comparison material only | no install, no dependency build, no upstream test/server/Worker/hook execution, no MCP server activation, no provider/API/account/network/browser use, no package activation, no checker wiring, no public-sync, no direct import |
| `zhaoxuya520__reverse-skill` | `https://github.com/zhaoxuya520/reverse-skill.git` | `.private_reference/source_mirrors/zhaoxuya520__reverse-skill/` | `dd7c50dc38e778373cd037b3f47d5e132ef43a2f` | `CLONED_PINNED` | 2026-08-15 | 559 | `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/` (205 files) | new governed intake comparing upstream routing, toolchain-bootstrap, case-evidence, and learning patterns against the CVF Capability Preflight & Bootstrap proposal and existing ASSF / Execution Plane / Work Order owners | upstream source mirror is authority for reverse-skill repository facts; the retained CVF Capability Preflight & Bootstrap folder is a secondary CVF-shaped proposal pack and not upstream evidence | no dependency install, no upstream script/test/tool execution, no security-target activity, no skill/MCP activation, no credential or provider use, no runtime mutation, no checker wiring, no public-sync, and no direct import |
| `modelcontextprotocol__modelcontextprotocol` | `https://github.com/modelcontextprotocol/modelcontextprotocol.git` | `.private_reference/source_mirrors/modelcontextprotocol__modelcontextprotocol/` | `5f5440bb26a62e2cf3440b92da5a667efa03b267` (tag `2026-07-28`; live `main` observed at intake: `57ac4a2ec742e0cb7622d899b0f5d3bcf769fd69`) | `CLONED_PINNED` | 2026-08-23 | 885 | `.private_reference/legacy/CVF 13.08/CVF_MCP_KNOWLEDGE_ABSORPTION_REDESIGN/` (108 files) | MCP-KAR-T0 dual-corpus receipt and source-verified selective absorption; semantic review pending | pinned upstream mirror is authority for MCP repository facts; the external-agent return is secondary mixed-origin derived synthesis and must be reconciled against upstream plus current CVF owners | no dependency install, build, test, schema generation, website execution, MCP server/client activation, provider/API/account use, runtime mutation, package/checker wiring, public-sync, production claim, or direct import |

## Update Rule

When a source mirror is cloned or refreshed:

1. Record the exact commit SHA in `Pinned commit`.
2. Change `Mirror status` to `CLONED_PINNED`.
3. Record or update the linked absorption lane.
4. Keep the cloned repository payload ignored by git.
5. Do not claim absorption completion from clone presence alone.

## Selection Rule

Before a full-value external repo absorption starts, the reviewer must check
this index:

- if a high-value upstream repo is available but only a derived external-agent
  pack exists locally, create or request a source mirror before closeout;
- if a mirror exists, use it as source-verification authority for upstream
  facts;
- if cloning is blocked, record `BLOCKED_SOURCE_MIRROR_WITH_REASON` in the
  absorption artifact and keep the derived pack as secondary evidence only.

## Claim Boundary

This index records reference-source availability. It does not authorize
runtime, package activation, checker wiring, dependency installation, hook
execution, provider calls, public export, or production readiness.
