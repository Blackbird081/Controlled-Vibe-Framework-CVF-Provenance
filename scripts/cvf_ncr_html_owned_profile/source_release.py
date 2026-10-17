"""Explicit source identity admission; the caller's external digest is integrity, never runtime consent."""
from __future__ import annotations

import json
import os
import re
import stat
from pathlib import Path

from .execution import sha

SCHEMA = "cvf.ncrHtmlSourceRelease@1"
PROFILE = "NCR_HTML_OWNED_SYNTHETIC_FRESH_SOURCE_V1"
KEYS = {"schemaVersion", "profile", "scope", "sourcePins", "productCommit", "productScopeGitObjects", "fixture", "entrypoints", "authority"}
SPEC = "docs/assessments/CVF_NCR_HTML_FRESH_PROFILE_USER_JOURNEY_SPEC_2026-10-14.md"
ENTRYPOINTS = {"scripts/probe_cvf_q001_synthetic_system_chain.py", "scripts/probe_cvf_w05_browser_chain.cjs"}
AUTHORITY = {"docs/baselines/CVF_GC018_NCR_HTML_LOGIN_READINESS_SOURCE_PHASE_2026-10-17.md",
             "docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_LOGIN_READINESS_SOURCE_PHASE_2026-10-17.md"}
SCOPES = ("EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web", "EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE",
          "governance/toolkit/03_CONTROL/CVF_AGENT_REGISTRY.md", "governance/toolkit/04_TESTING/CVF_SELF_UAT_DECISION_LOG.md",
          "docs/reference/CVF_GOVERNANCE_STATE_REGISTRY.json")


def reject(message):
    raise RuntimeError("explicit source release: " + message)


def no_reparse(path: Path):
    """Missing IO destinations remain allowed; any observed reparse refuses."""
    try:
        info = path.lstat()
    except FileNotFoundError:
        return
    if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
        raise RuntimeError(f"reparse path refused: {path.name}")


def _existing_directory(path):
    for ancestor in (path, *path.parents):
        ancestor.lstat()  # mandatory existence here, unlike the general IO helper
        no_reparse(ancestor)
    if not path.is_dir():
        raise RuntimeError("required directory missing")


def check_disposable(stage: Path, namespace: Path, dependency=None):
    """Read-only eligibility. Prune only the verified dependency; nothing is deleted or locked."""
    if (not namespace.is_absolute() or not stage.is_absolute() or ".." in namespace.parts
            or stage != namespace / "source"):
        raise RuntimeError("unsafe disposal target")
    _existing_directory(namespace)
    _existing_directory(stage)
    owner = namespace / "owner.json"
    no_reparse(owner)
    if not stat.S_ISREG(owner.lstat().st_mode) or stage.resolve(strict=True) != namespace.resolve(strict=True) / "source":
        raise RuntimeError("unsafe disposal owner or stage")
    link, target, seen = None, None, False
    if dependency is not None:
        link, target = map(Path, dependency)
        if link != stage / SCOPES[0] / "node_modules" or not target.is_absolute() or ".." in target.parts:
            raise RuntimeError("dependency lexical identity changed")
        _existing_directory(link.parent)
        _existing_directory(target)
        resolved_target = target.resolve(strict=True)
        if resolved_target.is_relative_to(namespace.resolve(strict=True)):
            raise RuntimeError("dependency target is disposable data")

        def verify_link():
            info = link.lstat()
            if (not stat.S_ISDIR(info.st_mode) or not getattr(info, "st_file_attributes", 0) & 0x400
                    or getattr(info, "st_reparse_tag", None) != 0xA0000003
                    or link.resolve(strict=True) != resolved_target):
                raise RuntimeError("dependency junction identity changed")
        verify_link()

    def walk_error(error):
        raise error

    for base, dirs, files in os.walk(stage, topdown=True, followlinks=False, onerror=walk_error):
        base = Path(base)
        _existing_directory(base)
        for name in dirs[:]:
            child = base / name
            if child == link:
                verify_link()
                dirs.remove(name)
                seen = True
            else:
                child.lstat()
                no_reparse(child)
        for name in files:
            (base / name).lstat()
            no_reparse(base / name)
    if link is not None and not seen:
        raise RuntimeError("dependency junction was not observed")
    return True


def digest(value, size=64):
    return type(value) is str and re.fullmatch(r"[0-9a-f]{" + str(size) + "}", value) is not None


def file_path(root, relative):
    """Canonical fixed relative paths only; inspect every ancestor before reading pinned bytes."""
    if (type(relative) is not str or not re.fullmatch(r"[A-Za-z0-9_./-]+", relative)
            or any(p in ("", ".", "..") for p in relative.split("/")) or relative.startswith("/")):
        reject("unsafe relative path")
    path = root / relative
    for ancestor in (path, *path.parents):
        try:
            info = ancestor.lstat()
        except OSError:
            reject("missing pinned file or ancestor")
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
            reject("reparse boundary")
    if not path.resolve().is_relative_to(root.resolve()) or not stat.S_ISREG(path.stat().st_mode):
        reject("nonregular or escaped file")
    return path


def unique_pairs(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            reject("duplicate JSON key")
        value[key] = item
    return value


def pin_map(value, expected):
    if type(value) is not dict or set(value) != set(expected) or not all(digest(h) for h in value.values()):
        reject("missing/extra/malformed pin family")


def clean(root, git):
    # Ignored task custody is excluded; the old writable OUTPUTS allowance is deliberately inapplicable.
    if (git("diff", "--name-only", "HEAD").strip() or git("diff", "--cached", "--name-only").strip()
            or git("ls-files", "--others", "--exclude-standard").strip()):
        reject("dirty explicit lane")


def check_product(binding, git):
    if (type(binding) is not dict or set(binding) != {"productCommit", "productScopeGitObjects"}
            or not digest(binding["productCommit"], 40)):
        reject("invalid product binding")
    objects = binding["productScopeGitObjects"]
    if type(objects) is not dict or set(objects) != set(SCOPES) or not all(digest(v, 40) for v in objects.values()):
        reject("invalid product scope objects")
    commit = binding["productCommit"]
    if git("rev-parse", commit + "^{commit}").decode().strip() != commit:
        reject("product commit does not resolve exactly")
    for path, expected in objects.items():
        if any(git("rev-parse", ref + ":" + path).decode().strip() != expected for ref in (commit, "HEAD")):
            reject("product object drift")


def recheck_stage(root, binding, git):
    """Recheck the admitted immutable product identity and selected bytes immediately before staging."""
    check_product(binding, git)
    if git("diff", "HEAD", "--", *SCOPES).strip() or git("diff", "--cached", "--", *SCOPES).strip():
        reject("selected product bytes changed before staging")


def admit(root, release_path, expected_digest, helpers, git):
    if not digest(expected_digest):
        reject("missing/malformed external digest")
    if type(release_path) is not str or not re.fullmatch(r"docs/reviews/evidence/[A-Za-z0-9_-]+\.json", release_path):
        reject("canonical evidence JSON path required")
    path = file_path(root, release_path)
    with path.open("rb") as handle:
        raw = handle.read(65537)
    if len(raw) > 65536 or sha(raw) != expected_digest:
        reject("manifest size or external digest mismatch")
    try:
        doc = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_pairs)
    except (UnicodeError, ValueError) as error:
        reject("invalid JSON: " + type(error).__name__)
    if (type(doc) is not dict or set(doc) != KEYS or doc["schemaVersion"] != SCHEMA
            or doc["profile"] != PROFILE or doc["scope"] != "SOURCE_IDENTITY_ONLY"):
        reject("closed schema/profile/scope mismatch")
    pin_map(doc["sourcePins"], helpers)
    pin_map(doc["entrypoints"], ENTRYPOINTS)
    pin_map(doc["authority"], AUTHORITY)
    fixture = doc["fixture"]
    if type(fixture) is not dict or set(fixture) != {"path", "sha256"} or fixture["path"] != SPEC or not digest(fixture["sha256"]):
        reject("canonical fixture mismatch")
    pins = {**doc["sourcePins"], **doc["entrypoints"], **doc["authority"], SPEC: fixture["sha256"]}
    for relative, expected in pins.items():
        if sha(file_path(root, relative).read_bytes()) != expected:
            reject("immutable pin drift")
    binding = {key: doc[key] for key in ("productCommit", "productScopeGitObjects")}
    check_product(binding, git)
    clean(root, git)
    return {"executionBaseHead": git("rev-parse", "HEAD").decode().strip(), "immutablePins": pins,
            "implementedHelpers": doc["sourcePins"], "productBinding": binding,
            "sourceRelease": {"path": release_path, "sha256": expected_digest, "scope": "SOURCE_IDENTITY_ONLY"}}
