from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

import check_cvf_public_sync_candidate as subject


REMOTE = "https://github.com/example/public.git"


def run(root: Path, *args: str) -> None:
    subprocess.run(args, cwd=root, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def fixture(tmp_path: Path) -> tuple[Path, Path]:
    root = tmp_path / "public"
    root.mkdir()
    run(root, "git", "init", "-b", "main")
    run(root, "git", "config", "user.email", "test@example.com")
    run(root, "git", "config", "user.name", "Test")
    run(root, "git", "remote", "add", "origin", REMOTE)
    (root / "README.md").write_text("base\n", encoding="utf-8")
    run(root, "git", "add", "README.md")
    run(root, "git", "commit", "-m", "base")
    manifest = tmp_path / "authorized.json"
    return root, manifest


def args(root: Path, manifest: Path) -> argparse.Namespace:
    return argparse.Namespace(public_root=str(root), authorized_paths_json=str(manifest), expected_remote=REMOTE, expected_branch="main", json=True)


def test_passes_owned_candidate_with_closed_dependency(tmp_path: Path) -> None:
    root, manifest = fixture(tmp_path)
    (root / "src").mkdir()
    (root / "src" / "dep.ts").write_text("export const ok = true;\n", encoding="utf-8")
    (root / "src" / "index.ts").write_text("export { ok } from './dep';\n", encoding="utf-8")
    manifest.write_text(json.dumps(["src/dep.ts", "src/index.ts"]), encoding="utf-8")
    assert subject.check(args(root, manifest))["status"] == "PASS"


def test_rejects_unowned_runtime_residue(tmp_path: Path) -> None:
    root, manifest = fixture(tmp_path)
    residue = root / ".cvf" / "runtime"
    residue.mkdir(parents=True)
    (residue / "receipt.json").write_text("{}\n", encoding="utf-8")
    manifest.write_text("[]", encoding="utf-8")
    result = subject.check(args(root, manifest))
    codes = {item["code"] for item in result["violations"]}
    assert {"UNOWNED_PENDING_PATH", "GENERATED_OR_RUNTIME_RESIDUE"} <= codes


def test_rejects_missing_relative_dependency(tmp_path: Path) -> None:
    root, manifest = fixture(tmp_path)
    (root / "src").mkdir()
    (root / "src" / "index.ts").write_text("export { secret } from './private-secret';\n", encoding="utf-8")
    manifest.write_text(json.dumps(["src/index.ts"]), encoding="utf-8")
    result = subject.check(args(root, manifest))
    assert any(item["code"] == "MISSING_RELATIVE_DEPENDENCY" for item in result["violations"])


def test_rejects_unchanged_importer_when_dependency_disappears(tmp_path: Path) -> None:
    root, manifest = fixture(tmp_path)
    (root / "src").mkdir()
    (root / "src" / "dep.ts").write_text("export const ok = true;\n", encoding="utf-8")
    (root / "src" / "index.ts").write_text("export { ok } from './dep';\n", encoding="utf-8")
    run(root, "git", "add", "src")
    run(root, "git", "commit", "-m", "source")
    (root / "src" / "dep.ts").unlink()
    manifest.write_text(json.dumps(["src/dep.ts"]), encoding="utf-8")
    result = subject.check(args(root, manifest))
    assert any(item["code"] == "MISSING_RELATIVE_DEPENDENCY" for item in result["violations"])


def test_reports_preexisting_missing_dependency_without_blocking(tmp_path: Path) -> None:
    root, manifest = fixture(tmp_path)
    (root / "src").mkdir()
    (root / "src" / "index.ts").write_text("export { absent } from './absent';\n", encoding="utf-8")
    run(root, "git", "add", "src/index.ts")
    run(root, "git", "commit", "-m", "preexisting debt")
    manifest.write_text("[]", encoding="utf-8")
    result = subject.check(args(root, manifest))
    assert result["status"] == "PASS"
    assert result["baselineDebtCount"] == 1
