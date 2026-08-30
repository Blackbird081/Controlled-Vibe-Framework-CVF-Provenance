#!/usr/bin/env python3
"""
CVF DSH-WRA-R1 Semantic-Region Classification Rules

Extracted from `scripts/dsh_wra_r1_corpus_processor.py` (Rework R1, to keep
the corpus processor under the governed Python automation size threshold for
its `python_cli_orchestrator` class without changing any classification
behavior). Owns the deterministic path-pattern semantic-region rule table,
format/binary/generated-file classification, and the region-level
terminal-status/disposition assignment used by the corpus processor.

This module has no side effects and performs no file I/O of its own; it is a
pure classification-rule library imported by the corpus processor.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


def _seg(path: str) -> list[str]:
    return path.split("/")


REGION_RULES: list[tuple[str, str, Any]] = []


def region(region_id: str, owner_hint: str):
    def _decorator(fn):
        REGION_RULES.append((region_id, owner_hint, fn))
        return fn
    return _decorator


# --- .agents notes / architecture / doctrine -------------------------------
@region("agents-notes-architecture-doctrine", "docs/reference (doctrine-adapted evidence only)")
def _r_agents_notes(p: str) -> bool:
    return p.startswith(".agents/")


# --- vendor / native / third-party -----------------------------------------
@region("vendor-native-thirdparty", "REJECT_DIRECT_IMPORT (vendor payload, no CVF owner)")
def _r_vendor(p: str) -> bool:
    return p.startswith("vendor/") or p.startswith("native/")


# --- website / docs site ----------------------------------------------------
@region("docs-site-website", "docs/ (doctrine-adapted evidence only)")
def _r_website(p: str) -> bool:
    return p.startswith("website/")


# --- top-level docs subsystem notes ----------------------------------------
@region("docs-subsystem-architecture", "docs/reference (doctrine-adapted evidence only)")
def _r_docs(p: str) -> bool:
    return p.startswith("docs/")


# --- python bridge/tools ----------------------------------------------------
@region("python-bridge-tooling", "OWNER_SURFACE_NOT_FOUND (no CVF python runtime owner)")
def _r_python(p: str) -> bool:
    return p.startswith("python/")


# --- generator / gen scripts -------------------------------------------------
@region("generated-catalog-scripts", "governance/compat generated-aggregate + drift-check owners")
def _r_scripts(p: str) -> bool:
    return p.startswith("scripts/")


# --- github workflows --------------------------------------------------------
@region("ci-workflow-config", "OWNER_SURFACE_NOT_FOUND (CI/workflow config is evidence-only, no CVF owner; forbidden to edit CI)")
def _r_gh(p: str) -> bool:
    return p.startswith(".github/")


# --- snapshots (generated test fixtures) ------------------------------------
@region("generated-snapshots-fixtures", "test fixture / generated snapshot, no runtime owner")
def _r_snapshots(p: str) -> bool:
    return p.startswith("snapshots/")


# --- apps (example / demo applications) --------------------------------------
@region("example-demo-apps", "OWNER_SURFACE_NOT_FOUND (example apps are demonstration code, not CVF runtime)")
def _r_apps(p: str) -> bool:
    return p.startswith("apps/")


# --- packages/* deep semantic split ------------------------------------------

def _pkg_after(p: str, marker: str) -> str:
    idx = p.find(marker)
    return p[idx + len(marker):] if idx != -1 else p


@region("agent-loop-tool-runtime-guard-approval", "EXTENSIONS/CVF_GUARD_CONTRACT/")
def _r_pkg_tools_guard(p: str) -> bool:
    return p.startswith("packages/core/tools/") or p.startswith("packages/core/agent-loop/") or "/tool-guard" in p or "/approval" in p


@region("llm-adapters-retry-timeout-streaming-routing", "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/ + src/lib/rate-limit.ts + EXTENSIONS/CVF_MODEL_GATEWAY/")
def _r_pkg_llm(p: str) -> bool:
    return (
        p.startswith("packages/core/llm/")
        or p.startswith("packages/llm/")
        or "/provider" in p
        or "/adapter" in p and "session" not in p
    )


@region("session-eventlog-persistence-checkpoint-telemetry", "EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts + event.ledger.contract.ts")
def _r_pkg_session(p: str) -> bool:
    return (
        p.startswith("packages/core/session/")
        or p.startswith("packages/session/")
        or "/persistence" in p
        or "/checkpoint" in p
        or "/telemetry" in p
        or "/compaction" in p
        or "/pruning" in p
        or "/spill" in p
    )


@region("subagent-jobs-scheduling-lifecycle", "EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/lifecycle.controller.contract.ts + delegation.adapter.contract.ts")
def _r_pkg_subagent(p: str) -> bool:
    return (
        p.startswith("packages/core/scope/")
        or "/subagent" in p
        or "/jobs" in p
        or "/schedul" in p
        or "/workflow" in p
        or "/lifecycle" in p
        or "/continuation" in p
    )


@region("filesystem-subprocess-sandbox-credentials-hooks-mcp-skills", "EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/simulation/sandbox.isolation.contract.ts + EXTENSIONS/CVF_GUARD_CONTRACT/")
def _r_pkg_sandbox(p: str) -> bool:
    return (
        p.startswith("packages/sandbox/")
        or p.startswith("packages/shell/")
        or "/mcp" in p
        or "/skills" in p
        or "/hooks" in p
        or "/credentials" in p
        or "/subprocess" in p
    )


@region("api-ui-web-client", "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/")
def _r_pkg_ui(p: str) -> bool:
    return "/ui/" in p or "/web/" in p or "/client/" in p or "/cli/" in p


@region("tests-diagnostics-operational", "EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/ + focused test owners")
def _r_pkg_tests(p: str) -> bool:
    segs = _seg(p)
    return (
        "test" in segs
        or "tests" in segs
        or "__tests__" in segs
        or p.endswith(".test.ts")
        or p.endswith(".spec.ts")
        or "/diagnostics" in p
    )


@region("packages-other-package-family", "OWNER_SURFACE_NOT_FOUND (package family pending per-package classification)")
def _r_pkg_other(p: str) -> bool:
    return p.startswith("packages/")


# --- root config files --------------------------------------------------------
@region("root-build-config", "OWNER_SURFACE_NOT_FOUND (build tooling config; forbidden to mutate CI/build)")
def _r_root_config(p: str) -> bool:
    return "/" not in p


@region("uncategorized-other", "OWNER_SURFACE_NOT_FOUND (residual bucket; individually reviewed)")
def _r_catch_all(p: str) -> bool:
    return True


def classify_region(path: str) -> tuple[str, str]:
    for region_id, owner_hint, predicate in REGION_RULES:
        if predicate(path):
            return region_id, owner_hint
    return "uncategorized-other", "OWNER_SURFACE_NOT_FOUND"


# ---------------------------------------------------------------------------
# Format / category classification
# ---------------------------------------------------------------------------

BINARY_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".woff", ".woff2", ".ttf", ".eot",
    ".pdf", ".zip", ".gz", ".tar", ".wasm", ".node", ".so", ".dylib", ".dll",
    ".exe", ".bin",
}
GENERATED_MARKERS = ("snapshots/", "/dist/", "/build/", ".min.js", "-lock.")


def classify_format(path: str) -> str:
    ext = Path(path).suffix.lower()
    return ext if ext else "(no-extension)"


def is_generated_or_grouped(path: str) -> bool:
    lowered = path.lower()
    return any(marker in lowered for marker in GENERATED_MARKERS) or path.startswith("snapshots/") or path.startswith("vendor/") or path.startswith("native/")


def is_binary(path: str) -> bool:
    return Path(path).suffix.lower() in BINARY_EXTS


# ---------------------------------------------------------------------------
# Value / processing status assignment (deterministic, group-level default;
# per-file rows always retained per work-order requirement)
#
# DSH-WRA-R1-R2-F02 canonical vocabulary: `terminalStatus` (this section's
# output) is restricted to EXACTLY the four canonical processing statuses
# `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`, `BLOCKED_UNREADABLE`. The prior
# `ADAPTED`, `REJECTED`, and `NO_NEW_VALUE` values the Rework R1 pass emitted
# here were semantic/value decisions, not processing-terminal states; they now
# live exclusively in `valueDisposition` (`region_disposition()` below, which
# is unchanged: ADAPT / NO_NEW_VALUE / REJECT / DEFER). A file's
# `terminalStatus` and its `valueDisposition` are two independent fields.
# ---------------------------------------------------------------------------

# Regions with a confirmed exact current CVF owner that were compared during
# this batch's deep review and confirmed structurally covered -> NO_NEW_VALUE
# (valueDisposition only; terminalStatus is computed separately below).
NO_NEW_VALUE_REGIONS = {
    "agent-loop-tool-runtime-guard-approval",
}

# Regions that are the mandatory runtime-realization target -> ADAPT
# (valueDisposition only; the concrete provider-attempt/quota delta
# implemented in this batch).
ADAPTED_REGIONS = {
    "llm-adapters-retry-timeout-streaming-routing",
}

# Regions kept as evidence-only / rejected-direct-import (vendor, generated,
# ci config, examples, build config) -> REJECT (valueDisposition only).
REJECTED_REGIONS = {
    "vendor-native-thirdparty",
    "generated-snapshots-fixtures",
    "example-demo-apps",
    "ci-workflow-config",
    "root-build-config",
}

# Regions preserved as DEFER (real option value, no current consumer proven
# in this batch beyond DSH-001/DSH-005 which get individual treatment).
DEFERRED_REGIONS = {
    "session-eventlog-persistence-checkpoint-telemetry",
    "subagent-jobs-scheduling-lifecycle",
    "filesystem-subprocess-sandbox-credentials-hooks-mcp-skills",
    "python-bridge-tooling",
    "packages-other-package-family",
    "docs-subsystem-architecture",
    "docs-site-website",
    "generated-catalog-scripts",
    "agents-notes-architecture-doctrine",
    "api-ui-web-client",
    "uncategorized-other",
}

# Tests/diagnostics -> NO_NEW_VALUE (valueDisposition only; test scaffolding
# is not itself convertible CVF runtime value, the behavior it tests is
# scored via its sibling implementation region). terminalStatus is computed
# separately below (SKIPPED_WITH_REASON for all but the named READ paths).
READ_NOVALUE_REGIONS = {
    "tests-diagnostics-operational",
}

# ---------------------------------------------------------------------------
# DSH-WRA-R1-R2-F02: exact per-path READ allowlist.
#
# `terminalStatus=READ` is asserted ONLY for a file that was genuinely opened
# and semantically inspected (not merely hashed) during this batch's actual
# execution. This is a closed, explicit set - not a region-wide default -
# because the whole-corpus scale (8,953 files) makes individual review of
# every file infeasible, and the prior Rework R1 return's own Corpus
# Completeness section already states plainly that "the region ledger's
# sample list is ... the authoritative record of which specific files
# received an actual read this batch". This set is exactly that record,
# restricted to paths that are actually tracked inside the pinned upstream
# mirror (`.private_reference/source_mirrors/deepseek-ai__deepseek-harness/`)
# - the CVF-owned runtime files this batch also read (route.ts,
# rate-limit.ts, and the CVF Model Gateway/MAO owner files cited in the
# Source Verification Block) are NOT part of this upstream corpus and
# therefore have no row in this ledger at all:
#
#   - the one upstream design-note file cited by path and section in this
#     worker return's Findings / Position and the governing work order's
#     Negative Search And Collision Discipline table (the bounded-llm-
#     request-recovery architecture note the mandatory runtime gap traces
#     back to); this file was genuinely opened and read in full, not merely
#     hashed;
#   - each semantic region's `adversarialSamplePaths` (first/middle/last
#     sorted path per region), which the region ledger already persists as
#     the bounded deep-sample evidence for that region.
#
# Every other tracked file in the corpus - including every other file in the
# `llm-adapters-retry-timeout-streaming-routing` and
# `tests-diagnostics-operational` regions - was classified by path pattern
# only and is therefore `SKIPPED_WITH_REASON`, never `READ`. This is the
# literal, expected outcome the work order and Rework R2 dispatch predicted:
# "expect that the overwhelming majority of rows will legitimately be
# SKIPPED_WITH_REASON, not READ."
INDIVIDUALLY_READ_PATHS: dict[str, str] = {
    # Mandatory provider-attempt/quota gap - upstream design note actually
    # opened and read in full (Findings / Position; Negative Search And
    # Collision Discipline table in the governing work order).
    ".agents/notes/implemented/architecture/2026-06-21-bounded-llm-request-recovery.md":
        "opened in full; confirmed the upstream visible-attempt/duplicate-"
        "billing design note ('Make one layer own visible attempts') this "
        "batch's CVF-side runtime gap corresponds to, per Findings / "
        "Position and the Source Verification Block",
    # Bounded adversarial sample paths, one region at a time (region ledger
    # `adversarialSamplePaths`, three per region, first/middle/last sorted).
    "packages/acp/acp/tests/approval.spec.ts":
        "adversarial sample for region 'agent-loop-tool-runtime-guard-approval'; "
        "opened and compared against CVF Guard Contract monotonic BLOCK "
        "semantics per Overlap And Novelty Classification (DSH-WRA-SMP-04)",
    "packages/core/agent-loop/tests/tool-order.spec.ts":
        "adversarial sample for region 'agent-loop-tool-runtime-guard-approval'",
    "packages/interaction/user-approval/tests/approval.spec.ts":
        "adversarial sample for region 'agent-loop-tool-runtime-guard-approval'",
    ".agents/notes/AGENTS.md":
        "adversarial sample for region 'agents-notes-architecture-doctrine'",
    ".agents/notes/implemented/bug-fix/2026-08-11-synchronous-subprocess-exit-cleanup.i18n.yaml":
        "adversarial sample for region 'agents-notes-architecture-doctrine'",
    ".agents/skills/record-browser-gif/scripts/encode_gif.py":
        "adversarial sample for region 'agents-notes-architecture-doctrine'",
    "packages/api/gateway/src/client/index.ts":
        "adversarial sample for region 'api-ui-web-client'",
    "packages/client/ui-primitives/src/relative-time.ts":
        "adversarial sample for region 'api-ui-web-client'",
    "packages/web/web/tsconfig.json":
        "adversarial sample for region 'api-ui-web-client'",
    ".github/AGENTS.md":
        "adversarial sample for region 'ci-workflow-config'",
    ".github/workflows/ci.yml":
        "adversarial sample for region 'ci-workflow-config'",
    ".github/workflows/sandbox.yml":
        "adversarial sample for region 'ci-workflow-config'",
    "website/.gitignore":
        "adversarial sample for region 'docs-site-website'",
    "website/docs.ts":
        "adversarial sample for region 'docs-site-website'",
    "website/public/wordmark.svg":
        "adversarial sample for region 'docs-site-website'",
    "docs/AGENTS.md":
        "adversarial sample for region 'docs-subsystem-architecture'",
    "docs/subsystems/goal.zh.md":
        "adversarial sample for region 'docs-subsystem-architecture'",
    "docs/web-styling.zh.md":
        "adversarial sample for region 'docs-subsystem-architecture'",
    "apps/cli/README.i18n.yaml":
        "adversarial sample for region 'example-demo-apps'",
    "apps/web/tests/approval-composer.e2e.ts":
        "adversarial sample for region 'example-demo-apps'",
    "apps/web/vite.config.ts":
        "adversarial sample for region 'example-demo-apps'",
    ".claude/skills":
        "adversarial sample for region "
        "'filesystem-subprocess-sandbox-credentials-hooks-mcp-skills'",
    "packages/sandbox/sandbox-windows-acl/tests/ffi.spec.ts":
        "adversarial sample for region "
        "'filesystem-subprocess-sandbox-credentials-hooks-mcp-skills'",
    "packages/subprocess/win32-process/verify/abi-probe.cpp":
        "adversarial sample for region "
        "'filesystem-subprocess-sandbox-credentials-hooks-mcp-skills'",
    "scripts/AGENTS.md":
        "adversarial sample for region 'generated-catalog-scripts'",
    "scripts/release/families.spec.ts":
        "adversarial sample for region 'generated-catalog-scripts'",
    "scripts/wine-windows-gates.sh":
        "adversarial sample for region 'generated-catalog-scripts'",
    "snapshots/AGENTS.md":
        "adversarial sample for region 'generated-snapshots-fixtures'",
    "snapshots/session/persistent-pwsh-tool-turn/system-prompt.expected.md":
        "adversarial sample for region 'generated-snapshots-fixtures'",
    "snapshots/web/workspace-management/snapshot.yml":
        "adversarial sample for region 'generated-snapshots-fixtures'",
    "packages/client/ui-settings-models/tests/provider-form.client.spec.tsx":
        "adversarial sample for region "
        "'llm-adapters-retry-timeout-streaming-routing'",
    "packages/llm/llm-retry/package.json":
        "adversarial sample for region "
        "'llm-adapters-retry-timeout-streaming-routing'",
    "packages/web/web-search-perplexity/src/provider.ts":
        "adversarial sample for region "
        "'llm-adapters-retry-timeout-streaming-routing'",
    "packages/AGENTS.md":
        "adversarial sample for region 'packages-other-package-family'",
    "packages/fs/fs/tsconfig.json":
        "adversarial sample for region 'packages-other-package-family'",
    "packages/workspace/workspace/tsconfig.json":
        "adversarial sample for region 'packages-other-package-family'",
    "python/README.i18n.yaml":
        "adversarial sample for region 'python-bridge-tooling'",
    "python/sdk/examples/README.i18n.yaml":
        "adversarial sample for region 'python-bridge-tooling'",
    "python/sdk/uv.lock":
        "adversarial sample for region 'python-bridge-tooling'",
    ".editorconfig":
        "adversarial sample for region 'root-build-config'",
    "SAFETY.md":
        "adversarial sample for region 'root-build-config'",
    "vitest.web.perf.config.ts":
        "adversarial sample for region 'root-build-config'",
    "packages/client/ui-chat/src/client/conversation-nodes/compaction.ts":
        "adversarial sample for region "
        "'session-eventlog-persistence-checkpoint-telemetry'",
    "packages/session/session-persistence-sqlite/tests/built-package.spec.ts":
        "adversarial sample for region "
        "'session-eventlog-persistence-checkpoint-telemetry'",
    "packages/web/tool-web/tests/spill.spec.ts":
        "adversarial sample for region "
        "'session-eventlog-persistence-checkpoint-telemetry'",
    "packages/client/ui-settings-plugins/src/client/subagent-model-selection-card-controller.ts":
        "adversarial sample for region 'subagent-jobs-scheduling-lifecycle'",
    "packages/subagent/subagent-in-process-driver/README.md":
        "adversarial sample for region 'subagent-jobs-scheduling-lifecycle'",
    "packages/workflow/workflow/tsconfig.json":
        "adversarial sample for region 'subagent-jobs-scheduling-lifecycle'",
    "packages/acp/acp/tests/bridge.spec.ts":
        "adversarial sample for region 'tests-diagnostics-operational'",
    "packages/host/directory-picker-browse/tests/service.spec.ts":
        "adversarial sample for region 'tests-diagnostics-operational'",
    "packages/workspace/workspace/tests/workspace.spec.ts":
        "adversarial sample for region 'tests-diagnostics-operational'",
    "patches/node-pty@1.2.0-beta.15.patch":
        "adversarial sample for region 'uncategorized-other'",
    "native/README.i18n.yaml":
        "adversarial sample for region 'vendor-native-thirdparty'",
    "vendor/cordis/src/logger.ts":
        "adversarial sample for region 'vendor-native-thirdparty'",
    "vendor/timer/tsconfig.json":
        "adversarial sample for region 'vendor-native-thirdparty'",
}


def skip_reason(region_id: str, disposition: str) -> str:
    """Non-empty, per-region skip-reason prose for a SKIPPED_WITH_REASON row.
    Always names the classification method and the value-disposition group it
    was grouped into, per DSH-WRA-R1-R2-F02 item 4."""
    return (
        f"path-pattern group classification only, not individually opened; "
        f"grouped into semantic region '{region_id}' with valueDisposition "
        f"'{disposition}' per the deterministic region-rule table in "
        f"scripts/dsh_wra_r1_region_rules.py"
    )


def region_terminal_status(region_id: str) -> str:
    """DSH-WRA-R1-R2-F02: region-level DEFAULT terminal status only (used
    when no per-file override applies). Restricted to the canonical
    vocabulary: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
    Group-classified regions (ADAPT/NO_NEW_VALUE/REJECT valueDisposition)
    default to SKIPPED_WITH_REASON at the region level; the caller applies
    the INDIVIDUALLY_READ_PATHS override per-file, and DEFER-disposed regions
    default to DEFERRED."""
    if region_id in ADAPTED_REGIONS:
        return "SKIPPED_WITH_REASON"
    if region_id in NO_NEW_VALUE_REGIONS:
        return "SKIPPED_WITH_REASON"
    if region_id in REJECTED_REGIONS:
        return "SKIPPED_WITH_REASON"
    if region_id in READ_NOVALUE_REGIONS:
        return "SKIPPED_WITH_REASON"
    if region_id in DEFERRED_REGIONS:
        return "DEFERRED"
    return "DEFERRED"


def region_disposition(region_id: str) -> str:
    if region_id in ADAPTED_REGIONS:
        return "ADAPT"
    if region_id in NO_NEW_VALUE_REGIONS:
        return "NO_NEW_VALUE"
    if region_id in REJECTED_REGIONS:
        return "REJECT"
    if region_id in READ_NOVALUE_REGIONS:
        return "NO_NEW_VALUE"
    return "DEFER"
