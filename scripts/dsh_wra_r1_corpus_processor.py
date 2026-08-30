#!/usr/bin/env python3
"""
CVF DSH-WRA-R1 Whole-Repository Corpus Processor

Deterministically enumerates the pinned DeepSeek Harness source mirror,
reconciles Git-tracked paths against a hidden/no-ignore filesystem walk,
computes stable per-file SHA-256 hashes, assigns every tracked file to a
semantic-region group via deterministic path-pattern rules, and emits:

  1. the whole-repository manifest (docs/audits/CVF_DSH_WHOLE_REPOSITORY_MANIFEST_2026-08-30.json)
  2. the per-file processing ledger (docs/audits/CVF_DSH_WHOLE_REPOSITORY_FILE_LEDGER_2026-08-30.jsonl)
  3. the semantic-region ledger (docs/audits/CVF_DSH_WHOLE_REPOSITORY_SEMANTIC_REGION_LEDGER_2026-08-30.json)

This script is read-only with respect to the pinned mirror. It never writes
under `.private_reference/source_mirrors/`.

Usage:
    python scripts/dsh_wra_r1_corpus_processor.py --generate
    python scripts/dsh_wra_r1_corpus_processor.py --verify
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# DSH-WRA-R1-RV rework (file-size shrink): semantic-region classification
# rules, format/binary classification, and region-level terminal-status/
# disposition assignment live in a dedicated module so this orchestrator
# stays under the governed `python_cli_orchestrator` size threshold. See
# `scripts/dsh_wra_r1_region_rules.py` for the extracted rule table.
from dsh_wra_r1_region_rules import (
    ADAPTED_REGIONS,
    DEFERRED_REGIONS,
    INDIVIDUALLY_READ_PATHS,
    NO_NEW_VALUE_REGIONS,
    READ_NOVALUE_REGIONS,
    REGION_RULES,
    REJECTED_REGIONS,
    classify_format,
    classify_region,
    is_binary,
    is_generated_or_grouped,
    region_disposition,
    region_terminal_status,
    skip_reason as build_skip_reason,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
MIRROR_REL = ".private_reference/source_mirrors/deepseek-ai__deepseek-harness"
MIRROR_ABS = REPO_ROOT / MIRROR_REL
PINNED_COMMIT = "cd5ef8148158c3a752a658978873241fdf8e2bbc"

MANIFEST_PATH = REPO_ROOT / "docs/audits/CVF_DSH_WHOLE_REPOSITORY_MANIFEST_2026-08-30.json"
LEDGER_PATH = REPO_ROOT / "docs/audits/CVF_DSH_WHOLE_REPOSITORY_FILE_LEDGER_2026-08-30.jsonl"
REGION_LEDGER_PATH = REPO_ROOT / "docs/audits/CVF_DSH_WHOLE_REPOSITORY_SEMANTIC_REGION_LEDGER_2026-08-30.json"
PACKAGE_FAMILY_LEDGER_PATH = REPO_ROOT / "docs/audits/CVF_DSH_WHOLE_REPOSITORY_PACKAGE_FAMILY_LEDGER_2026-08-30.json"

EXPECTED_TRACKED_COUNT = 8953


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------

def _run(cmd: list[str], cwd: Path) -> str:
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        raise RuntimeError(f"command failed: {' '.join(cmd)}\n{proc.stderr}")
    return proc.stdout


def git_ls_files(mirror: Path) -> list[str]:
    out = _run(["git", "ls-files", "-z"], cwd=mirror)
    return [p for p in out.split("\x00") if p]


def git_rev_parse_head(mirror: Path) -> str:
    return _run(["git", "rev-parse", "HEAD"], cwd=mirror).strip()


def git_pinned_commit_timestamp_utc(mirror: Path, commit: str) -> str:
    """Return the pinned commit's own committer timestamp, normalized to UTC
    ISO-8601 with a trailing 'Z' and zero microseconds. This is immutable
    source metadata (it never changes for a fixed pinned commit), unlike
    wall-clock generation time, so using it as `snapshotDateUtc` makes the
    manifest byte-deterministic across repeated `--generate` runs at any
    later date (DSH-WRA-R1-RV-F03)."""
    raw = _run(["git", "show", "-s", "--format=%cI", commit], cwd=mirror).strip()
    import datetime as dt
    parsed = dt.datetime.fromisoformat(raw)
    as_utc = parsed.astimezone(dt.timezone.utc).replace(microsecond=0)
    return as_utc.isoformat().replace("+00:00", "Z")


def git_status_short(mirror: Path) -> str:
    return _run(["git", "status", "--short"], cwd=mirror).strip()


def rg_files_hidden_no_ignore(mirror: Path) -> set[str]:
    """Filesystem-backed reconciliation walk (rg --files --hidden --no-ignore),
    excluding the .git control directory itself (git ls-files also excludes it)."""
    try:
        out = subprocess.run(
            ["rg", "--files", "--hidden", "--no-ignore"],
            cwd=mirror, capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        if out.returncode not in (0, 1):
            raise RuntimeError(out.stderr)
        paths = set()
        for line in out.stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            norm = line.replace("\\", "/")
            if norm.startswith(".git/"):
                continue
            paths.add(norm)
        return paths
    except FileNotFoundError:
        # rg not available in PATH in this environment; fall back to Python walk
        paths = set()
        for item in mirror.rglob("*"):
            if item.is_dir():
                continue
            rel = item.relative_to(mirror).as_posix()
            if rel.startswith(".git/"):
                continue
            paths.add(rel)
        return paths


def git_hash_object(mirror: Path, paths: list[str]) -> dict[str, str]:
    """Batch git hash-object (git blob sha) is not stable SHA-256; we compute
    real SHA-256 content hashes directly from the filesystem for the manifest,
    since the work order requires a stable path/content hash, not a git blob
    id. This function is retained for provenance cross-check only."""
    raise NotImplementedError


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def stable_path_hash(paths: list[str]) -> str:
    joined = "\n".join(sorted(paths)) + "\n"
    return hashlib.sha256(joined.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Main generation
# ---------------------------------------------------------------------------

@dataclass
class FileRecord:
    path: str
    bytes: int
    sha256: str
    ext: str
    region_id: str
    owner_hint: str
    processing_status: str
    disposition: str
    grouped: bool
    readable: bool
    read_evidence: str | None = None
    skip_reason: str | None = None


def _terminal_status_and_evidence(
    rel: str, region_id: str, disposition: str, readable: bool,
) -> tuple[str, str | None, str | None]:
    """DSH-WRA-R1-R2-F02: compute the canonical per-file terminalStatus plus
    its required companion evidence field. Returns
    (terminalStatus, readEvidence, skipReason). Exactly one of readEvidence/
    skipReason is non-None for a READ or SKIPPED_WITH_REASON row; both are
    None for a DEFERRED or BLOCKED_UNREADABLE row."""
    if not readable:
        return "BLOCKED_UNREADABLE", None, None

    # The per-path READ override (DSH-WRA-R1-R2-F02 allowlist) takes
    # precedence over the region-level default in every case, including a
    # DEFER-disposed region: a region ledger's adversarialSamplePaths entry
    # was genuinely opened and read even when the rest of its (deferred)
    # region was only path-pattern classified.
    evidence = INDIVIDUALLY_READ_PATHS.get(rel)
    if evidence is not None:
        return "READ", evidence, None

    default_status = region_terminal_status(region_id)
    if default_status == "DEFERRED":
        return "DEFERRED", None, None

    # default_status is SKIPPED_WITH_REASON here (the only other canonical
    # non-deferred, non-blocked value region_terminal_status ever returns).
    # Every other file in a group-classified region stays SKIPPED_WITH_REASON.
    return "SKIPPED_WITH_REASON", None, build_skip_reason(region_id, disposition)


def enumerate_and_hash(mirror: Path) -> list[FileRecord]:
    tracked = git_ls_files(mirror)
    records: list[FileRecord] = []
    for rel in tracked:
        full = mirror / rel
        readable = True
        size = 0
        digest = ""
        try:
            size = full.stat().st_size
            digest = sha256_file(full)
        except OSError:
            readable = False
        region_id, owner_hint = classify_region(rel)
        ext = classify_format(rel)
        grouped = is_generated_or_grouped(rel)
        disposition = "BLOCK" if not readable else region_disposition(region_id)
        status, read_evidence, skip_reason = _terminal_status_and_evidence(
            rel, region_id, disposition, readable,
        )
        records.append(FileRecord(
            path=rel, bytes=size, sha256=digest, ext=ext,
            region_id=region_id, owner_hint=owner_hint,
            processing_status=status, disposition=disposition,
            grouped=grouped, readable=readable,
            read_evidence=read_evidence, skip_reason=skip_reason,
        ))
    return records


def build_manifest(records: list[FileRecord], mirror_commit: str, mirror_clean: bool, fs_recon: dict[str, Any]) -> dict[str, Any]:
    folder_counts: Counter[str] = Counter()
    ext_counts: Counter[str] = Counter()
    for r in records:
        top = r.path.split("/")[0] if "/" in r.path else "(root)"
        folder_counts[top] += 1
        ext_counts[r.ext] += 1

    paths = [r.path for r in records]
    manifest = {
        "schema": "cvf.dshWholeRepositoryManifest.v1",
        "corpusId": "dsh-wra-r1-whole-repository",
        "root": MIRROR_REL + "/",
        "pinnedCommit": mirror_commit,
        "pinnedCommitExpected": PINNED_COMMIT,
        "pinMatches": mirror_commit == PINNED_COMMIT,
        "mirrorClean": mirror_clean,
        "snapshotDateUtc": None,  # filled by caller with real UTC timestamp
        "fileCount": len(records),
        "expectedTrackedCount": EXPECTED_TRACKED_COUNT,
        "countMatchesExpected": len(records) == EXPECTED_TRACKED_COUNT,
        "totalBytes": sum(r.bytes for r in records),
        "pathManifestHash": stable_path_hash(paths),
        "hashAlgorithm": "sha256",
        "hashInput": "sorted-paths-newline-joined-with-trailing-newline",
        "fileCountByFolder": dict(sorted(folder_counts.items(), key=lambda kv: (-kv[1], kv[0]))),
        "fileCountByExtension": dict(sorted(ext_counts.items(), key=lambda kv: (-kv[1], kv[0]))),
        "filesystemReconciliation": fs_recon,
        "declaredExclusions": [],
        "unreadableFiles": [r.path for r in records if not r.readable],
        "files": [
            {"path": r.path, "bytes": r.bytes, "sha256": r.sha256, "ext": r.ext}
            for r in records
        ],
        "claimBoundary": (
            "Immutable whole-repository corpus inventory of the pinned upstream "
            "mirror only; no semantic completeness, runtime, provider, public, "
            "or production claim."
        ),
    }
    return manifest


def build_ledger_rows(records: list[FileRecord]) -> list[dict[str, Any]]:
    rows = []
    for r in records:
        row: dict[str, Any] = {
            "path": r.path,
            "sha256": r.sha256,
            "formatCategory": r.ext,
            "semanticRegion": r.region_id,
            "processingMethod": (
                "INDIVIDUALLY_OPENED_AND_SEMANTICALLY_READ"
                if r.processing_status == "READ"
                else "DETERMINISTIC_PATH_PATTERN_GROUP_CLASSIFICATION_ONLY"
            ),
            # DSH-WRA-R1-R2-F02: terminalStatus is restricted to exactly
            # READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
            # Semantic/value decisions live only in valueDisposition below.
            "terminalStatus": r.processing_status,
            "valueDisposition": r.disposition,
            "sourceLocatorOrGroupId": f"group:{r.region_id}",
            "existingCvfOwnerOrNotFound": r.owner_hint,
            "outputOrReopenReference": (
                "docs/reviews/CVF_DSH_WRA_R1_WHOLE_REPOSITORY_ABSORPTION_AND_RUNTIME_REALIZATION_WORKER_RETURN_2026-08-30.md"
                if r.disposition != "DEFER"
                else "docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md"
            ),
            "grouped": r.grouped,
            # DSH-WRA-R1-R2-F02 items 3-4: exactly one of these two fields is
            # non-null, matching terminalStatus (READ <-> readEvidence,
            # SKIPPED_WITH_REASON <-> skipReason); both are null for
            # DEFERRED and BLOCKED_UNREADABLE rows.
            "readEvidence": r.read_evidence,
            "skipReason": r.skip_reason,
        }
        rows.append(row)
    return rows


def package_family_of(path: str) -> str | None:
    """Return the packages/<group>/<name> family root for a path under
    packages/, or None if the path is not inside a package."""
    if not path.startswith("packages/"):
        return None
    segs = path.split("/")
    if len(segs) < 3:
        return None
    return "/".join(segs[:3])


def build_package_family_ledger(records: list[FileRecord]) -> dict[str, Any]:
    families: dict[str, list[FileRecord]] = defaultdict(list)
    for r in records:
        fam = package_family_of(r.path)
        if fam:
            families[fam].append(r)

    has_manifest: dict[str, bool] = {}
    for fam, recs in families.items():
        has_manifest[fam] = any(r.path == f"{fam}/package.json" for r in recs)

    rows = []
    for fam in sorted(families):
        recs = families[fam]
        region_counts = Counter(r.region_id for r in recs)
        dominant_region = region_counts.most_common(1)[0][0]
        rows.append({
            "packageFamily": fam,
            "fileCount": len(recs),
            "hasPackageJson": has_manifest.get(fam, False),
            "dominantSemanticRegion": dominant_region,
            "disposition": region_disposition(dominant_region),
            "ownerHint": classify_region(recs[0].path)[1],
        })

    # All package.json manifests anywhere in the tracked corpus (272 total per
    # work-order acceptance criterion), including ones outside packages/<a>/<b>
    # (apps/, native/, python/, vendor/, website/, root, and nested fixture
    # monorepos under packages/typert/generator/tests/fixtures/**).
    all_manifests = [r for r in records if r.path == "package.json" or r.path.endswith("/package.json")]
    manifest_rows = []
    for r in sorted(all_manifests, key=lambda x: x.path):
        manifest_rows.append({
            "path": r.path,
            "semanticRegion": r.region_id,
            "disposition": region_disposition(r.region_id),
            "ownerHint": r.owner_hint,
        })

    return {
        "schema": "cvf.dshPackageFamilyLedger.v1",
        "packageFamilyCount": len(families),
        "packageJsonManifestCount": len(all_manifests),
        "families": rows,
        "allPackageJsonManifests": manifest_rows,
        "claimBoundary": (
            "Package-family disposition inherits its dominant per-file semantic "
            "region classification; every family's constituent files retain "
            "individual per-file ledger rows in the whole-repository file ledger. "
            "`allPackageJsonManifests` lists every package.json tracked in the "
            "corpus (including nested test-fixture monorepos and non-packages/ "
            "roots) with an explicit semantic disposition each."
        ),
    }


def build_region_ledger(records: list[FileRecord]) -> dict[str, Any]:
    by_region: dict[str, list[FileRecord]] = defaultdict(list)
    for r in records:
        by_region[r.region_id].append(r)

    regions = []
    mapped = 0
    deferred = 0
    unmapped = 0
    for region_id, recs in sorted(by_region.items()):
        disp = region_disposition(region_id)
        owner_hint = recs[0].owner_hint
        count = len(recs)
        # sample up to 3 adversarial paths (first, middle, last when sorted)
        sorted_paths = sorted(r.path for r in recs)
        sample_idxs = sorted({0, len(sorted_paths) // 2, len(sorted_paths) - 1})
        adversarial_samples = [sorted_paths[i] for i in sample_idxs]
        is_deferred = disp == "DEFER"
        is_unmapped = owner_hint.startswith("OWNER_SURFACE_NOT_FOUND") and not is_deferred and disp not in ("NO_NEW_VALUE", "REJECT", "ADAPT")
        if is_deferred:
            deferred += count
        elif is_unmapped:
            unmapped += count
        else:
            mapped += count
        regions.append({
            "regionId": region_id,
            "fileCount": count,
            "ownerHint": owner_hint,
            "disposition": disp,
            "adversarialSamplePaths": adversarial_samples,
            "reopenConditionRequired": is_deferred,
        })

    total = mapped + deferred + unmapped
    return {
        "schema": "cvf.dshWholeRepositorySemanticRegionLedger.v1",
        "totalAssets": len(records),
        "mapped": mapped,
        "deferred": deferred,
        "unmapped": unmapped,
        "reconciles": total == len(records),
        "regions": regions,
        "crossRegionLinks": [
            {
                "fromRegion": "llm-adapters-retry-timeout-streaming-routing",
                "toRegion": "session-eventlog-persistence-checkpoint-telemetry",
                "relationship": "DSH-001 candidate: durable event lineage informs model-visible context composition",
            },
            {
                "fromRegion": "subagent-jobs-scheduling-lifecycle",
                "toRegion": "filesystem-subprocess-sandbox-credentials-hooks-mcp-skills",
                "relationship": "DSH-005 candidate: scope-owned registration lifecycle links to sandbox/capability admission",
            },
            {
                "fromRegion": "agent-loop-tool-runtime-guard-approval",
                "toRegion": "tests-diagnostics-operational",
                "relationship": "Guard/tool runtime tests validate monotonic BLOCK behavior already owned by CVF Guard Contract",
            },
        ],
        "claimBoundary": (
            "Deterministic semantic-region reconciliation for the pinned mirror "
            "only; group-level dispositions are backed by per-file ledger rows "
            "and bounded deep review of adversarial samples, not exhaustive "
            "manual narration of every file."
        ),
    }


def _canonical_manifest_bytes(manifest: dict[str, Any]) -> bytes:
    return json.dumps(manifest, indent=2, ensure_ascii=False).encode("utf-8")


def _canonical_ledger_bytes(ledger_rows: list[dict[str, Any]]) -> bytes:
    return ("\n".join(json.dumps(row, ensure_ascii=False) for row in ledger_rows) + "\n").encode("utf-8")


def _canonical_region_ledger_bytes(region_ledger: dict[str, Any]) -> bytes:
    return json.dumps(region_ledger, indent=2, ensure_ascii=False).encode("utf-8")


def _canonical_package_family_ledger_bytes(package_family_ledger: dict[str, Any]) -> bytes:
    return json.dumps(package_family_ledger, indent=2, ensure_ascii=False).encode("utf-8")


def build_all_artifacts(mirror: Path) -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, Any], dict[str, Any], dict[str, Any]]:
    """Deterministically (re)compute all four artifacts from the pinned
    mirror. Returns (manifest, ledger_rows, region_ledger,
    package_family_ledger, fs_recon). Calling this twice against the same
    unmodified mirror MUST produce byte-identical output for every artifact,
    because `snapshotDateUtc` is derived from the pinned commit's own
    immutable committer timestamp rather than wall-clock generation time
    (DSH-WRA-R1-RV-F03)."""
    mirror_commit = git_rev_parse_head(mirror)
    mirror_status = git_status_short(mirror)
    mirror_clean = mirror_status == ""

    records = enumerate_and_hash(mirror)
    tracked_set = {r.path for r in records}
    fs_set = rg_files_hidden_no_ignore(mirror)
    only_in_git = sorted(tracked_set - fs_set)
    only_in_fs = sorted(fs_set - tracked_set)
    fs_recon = {
        "filesystemBackedCommand": "rg --files --hidden --no-ignore (fallback: recursive filesystem walk if rg unavailable)",
        "trackedCount": len(tracked_set),
        "filesystemCount": len(fs_set),
        "onlyInGitLsFiles": only_in_git,
        "onlyInFilesystemWalk": only_in_fs,
        "reconciles": len(only_in_git) == 0 and len(only_in_fs) == 0,
    }

    manifest = build_manifest(records, mirror_commit, mirror_clean, fs_recon)
    # DSH-WRA-R1-RV-F03: snapshotDateUtc is derived from the pinned commit's
    # own immutable committer timestamp, not wall-clock generation time, so
    # every field in the manifest (and therefore the whole artifact set) is
    # byte-identical across repeated generations against an unmodified,
    # correctly-pinned mirror.
    manifest["snapshotDateUtc"] = git_pinned_commit_timestamp_utc(mirror, mirror_commit)

    ledger_rows = build_ledger_rows(records)
    region_ledger = build_region_ledger(records)
    package_family_ledger = build_package_family_ledger(records)

    # DSH-WRA-R1-R2-F02 item 8: recompute and reconcile the four canonical
    # terminal-status totals against the manifest's fileCount. Stored on the
    # manifest so every consumer (worker return, registry, dependent
    # artifacts) reads the same recomputed numbers rather than re-deriving
    # them independently and risking drift.
    terminal_counts = Counter(row["terminalStatus"] for row in ledger_rows)
    manifest["terminalStatusCounts"] = {
        "READ": terminal_counts.get("READ", 0),
        "SKIPPED_WITH_REASON": terminal_counts.get("SKIPPED_WITH_REASON", 0),
        "DEFERRED": terminal_counts.get("DEFERRED", 0),
        "BLOCKED_UNREADABLE": terminal_counts.get("BLOCKED_UNREADABLE", 0),
    }
    allowed_terminal_count = sum(manifest["terminalStatusCounts"].values())
    manifest["allowedTerminalCount"] = allowed_terminal_count
    manifest["ledgerTerminalReconciles"] = allowed_terminal_count == len(ledger_rows) == manifest["fileCount"]
    manifest["unresolvedCount"] = manifest["fileCount"] - allowed_terminal_count

    return manifest, ledger_rows, region_ledger, package_family_ledger, fs_recon


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--generate", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    if not MIRROR_ABS.exists():
        print(f"ERROR: mirror not found at {MIRROR_ABS}", file=sys.stderr)
        return 2

    manifest, ledger_rows, region_ledger, package_family_ledger, fs_recon = build_all_artifacts(MIRROR_ABS)
    records_count = len(ledger_rows)

    print("=== DSH-WRA-R1 Corpus Processor ===")
    print(f"Mirror commit: {manifest['pinnedCommit']} (expected {PINNED_COMMIT}, match={manifest['pinMatches']})")
    print(f"Mirror clean: {manifest['mirrorClean']}")
    print(f"Tracked file count: {manifest['fileCount']} (expected {EXPECTED_TRACKED_COUNT}, match={manifest['countMatchesExpected']})")
    print(f"Filesystem reconciliation: {fs_recon['reconciles']} (git-only={len(fs_recon['onlyInGitLsFiles'])}, fs-only={len(fs_recon['onlyInFilesystemWalk'])})")
    print(f"Path manifest hash: {manifest['pathManifestHash']}")
    print(f"Snapshot date UTC (pinned-commit-derived, deterministic): {manifest['snapshotDateUtc']}")
    print(f"Semantic regions: {len(region_ledger['regions'])}; mapped={region_ledger['mapped']} deferred={region_ledger['deferred']} unmapped={region_ledger['unmapped']} reconciles={region_ledger['reconciles']}")
    unreadable = manifest["unreadableFiles"]
    print(f"Unreadable files: {len(unreadable)}")
    print(f"Package families: {package_family_ledger['packageFamilyCount']}; package.json manifests: {package_family_ledger['packageJsonManifestCount']}")
    tsc = manifest["terminalStatusCounts"]
    print(
        f"Terminal statuses (canonical only): READ={tsc['READ']} "
        f"SKIPPED_WITH_REASON={tsc['SKIPPED_WITH_REASON']} DEFERRED={tsc['DEFERRED']} "
        f"BLOCKED_UNREADABLE={tsc['BLOCKED_UNREADABLE']} | "
        f"allowedTerminalCount={manifest['allowedTerminalCount']} "
        f"unresolvedCount={manifest['unresolvedCount']} "
        f"ledgerTerminalReconciles={manifest['ledgerTerminalReconciles']}"
    )

    if args.generate:
        MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST_PATH.write_bytes(_canonical_manifest_bytes(manifest))
        LEDGER_PATH.write_bytes(_canonical_ledger_bytes(ledger_rows))
        REGION_LEDGER_PATH.write_bytes(_canonical_region_ledger_bytes(region_ledger))
        PACKAGE_FAMILY_LEDGER_PATH.write_bytes(_canonical_package_family_ledger_bytes(package_family_ledger))
        print(f"\nWrote manifest: {MANIFEST_PATH}")
        print(f"Wrote ledger ({len(ledger_rows)} rows): {LEDGER_PATH}")
        print(f"Wrote region ledger: {REGION_LEDGER_PATH}")
        print(f"Wrote package family ledger: {PACKAGE_FAMILY_LEDGER_PATH}")

    if args.verify:
        ok = True
        if not manifest["pinMatches"]:
            print("VERIFY FAIL: pin mismatch", file=sys.stderr)
            ok = False
        if not manifest["countMatchesExpected"]:
            print("VERIFY FAIL: tracked count mismatch", file=sys.stderr)
            ok = False
        if not fs_recon["reconciles"]:
            print("VERIFY FAIL: filesystem reconciliation mismatch", file=sys.stderr)
            ok = False
        if not region_ledger["reconciles"]:
            print("VERIFY FAIL: region reconciliation mismatch", file=sys.stderr)
            ok = False
        if len(ledger_rows) != records_count:
            print("VERIFY FAIL: ledger row count mismatch", file=sys.stderr)
            ok = False
        if package_family_ledger["packageJsonManifestCount"] != 272:
            print(f"VERIFY FAIL: package.json manifest count {package_family_ledger['packageJsonManifestCount']} != 272", file=sys.stderr)
            ok = False
        seen = set()
        dup = [r["path"] for r in ledger_rows if r["path"] in seen or seen.add(r["path"])]
        if dup:
            print(f"VERIFY FAIL: duplicate paths in ledger: {dup[:5]}", file=sys.stderr)
            ok = False

        # DSH-WRA-R1-R2-F02 item 10: adversarial canonical-vocabulary and
        # evidence-field checks against the actually-generated ledger rows.
        canonical_statuses = {"READ", "SKIPPED_WITH_REASON", "DEFERRED", "BLOCKED_UNREADABLE"}
        non_canonical = sorted({r["terminalStatus"] for r in ledger_rows} - canonical_statuses)
        if non_canonical:
            print(f"VERIFY FAIL: non-canonical terminalStatus values present: {non_canonical}", file=sys.stderr)
            ok = False
        read_missing_evidence = [r["path"] for r in ledger_rows if r["terminalStatus"] == "READ" and not r.get("readEvidence")]
        if read_missing_evidence:
            print(f"VERIFY FAIL: READ rows missing readEvidence: {read_missing_evidence[:5]}", file=sys.stderr)
            ok = False
        skipped_missing_reason = [r["path"] for r in ledger_rows if r["terminalStatus"] == "SKIPPED_WITH_REASON" and not r.get("skipReason")]
        if skipped_missing_reason:
            print(f"VERIFY FAIL: SKIPPED_WITH_REASON rows missing skipReason: {skipped_missing_reason[:5]}", file=sys.stderr)
            ok = False
        if manifest["allowedTerminalCount"] != EXPECTED_TRACKED_COUNT or not manifest["ledgerTerminalReconciles"]:
            print(
                f"VERIFY FAIL: terminal counts do not reconcile to {EXPECTED_TRACKED_COUNT} "
                f"(allowedTerminalCount={manifest['allowedTerminalCount']}, "
                f"unresolvedCount={manifest['unresolvedCount']})",
                file=sys.stderr,
            )
            ok = False
        # A path-pattern-only-classified row must never be mislabeled READ:
        # every READ row must appear in the exact INDIVIDUALLY_READ_PATHS
        # allowlist (the only source of legitimate READ evidence).
        mislabeled_read = [r["path"] for r in ledger_rows if r["terminalStatus"] == "READ" and r["path"] not in INDIVIDUALLY_READ_PATHS]
        if mislabeled_read:
            print(f"VERIFY FAIL: READ rows not in the individually-read allowlist: {mislabeled_read[:5]}", file=sys.stderr)
            ok = False

        # DSH-WRA-R1-RV-F03: byte-compare every persisted artifact against
        # freshly regenerated canonical bytes, not just an in-memory model
        # recomputation. A stale or hand-edited persisted artifact must fail
        # verification even when the in-memory model itself reconciles.
        byte_checks = (
            (MANIFEST_PATH, _canonical_manifest_bytes(manifest), "manifest"),
            (LEDGER_PATH, _canonical_ledger_bytes(ledger_rows), "file ledger"),
            (REGION_LEDGER_PATH, _canonical_region_ledger_bytes(region_ledger), "semantic-region ledger"),
            (PACKAGE_FAMILY_LEDGER_PATH, _canonical_package_family_ledger_bytes(package_family_ledger), "package-family ledger"),
        )
        for artifact_path, canonical_bytes, label in byte_checks:
            if not artifact_path.exists():
                print(f"VERIFY FAIL: persisted {label} artifact missing at {artifact_path}", file=sys.stderr)
                ok = False
                continue
            on_disk_bytes = artifact_path.read_bytes()
            if on_disk_bytes != canonical_bytes:
                print(
                    f"VERIFY FAIL: persisted {label} artifact at {artifact_path} does not byte-match "
                    f"freshly regenerated canonical output (stale or hand-edited artifact)",
                    file=sys.stderr,
                )
                ok = False

        if not ok:
            return 3
        print("\nVERIFY PASS (including byte-identical persisted-artifact comparison)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
