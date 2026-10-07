from __future__ import annotations

import argparse
import json
import subprocess
import hashlib
import sys
from pathlib import Path

import pytest

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


def args(root: Path, manifest: Path, baseline_ref: str = "HEAD") -> argparse.Namespace:
    return argparse.Namespace(public_root=str(root), authorized_paths_json=str(manifest), expected_remote=REMOTE, expected_branch="main", baseline_ref=baseline_ref, json=True)


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


def test_remote_baseline_rejects_dependency_regression_in_committed_candidate(tmp_path: Path) -> None:
    root, manifest = fixture(tmp_path)
    (root / "src").mkdir()
    (root / "src" / "dep.ts").write_text("export const ok = true;\n", encoding="utf-8")
    (root / "src" / "index.ts").write_text("export { ok } from './dep';\n", encoding="utf-8")
    run(root, "git", "add", "src")
    run(root, "git", "commit", "-m", "closed source")
    run(root, "git", "branch", "baseline")
    (root / "src" / "dep.ts").unlink()
    run(root, "git", "add", "-A")
    run(root, "git", "commit", "-m", "broken candidate")
    manifest.write_text("[]", encoding="utf-8")
    result = subject.check(args(root, manifest, baseline_ref="baseline"))
    assert any(item["code"] == "MISSING_RELATIVE_DEPENDENCY" for item in result["violations"])


def test_accepts_equivalent_github_remote_without_dot_git(tmp_path: Path) -> None:
    root, manifest = fixture(tmp_path)
    run(root, "git", "remote", "set-url", "origin", REMOTE.removesuffix(".git"))
    manifest.write_text("[]", encoding="utf-8")
    assert subject.check(args(root, manifest))["status"] == "PASS"


@pytest.mark.parametrize("specifier,dependency", [("./hidden", "hidden.ts"), ("./hidden.js", "hidden.ts"), ("./hidden", "hidden/index.ts")])
def test_ignored_disk_dependency_cannot_close_candidate(tmp_path: Path, specifier: str, dependency: str) -> None:
    root, manifest = fixture(tmp_path)
    (root / "src").mkdir()
    (root / ".gitignore").write_text("src/hidden*\n", encoding="utf-8")
    (root / "src/index.ts").write_text(f"export {{ ok }} from '{specifier}';\n", encoding="utf-8")
    hidden = root / "src" / dependency
    hidden.parent.mkdir(exist_ok=True)
    hidden.write_text("export const ok = true;\n", encoding="utf-8")
    manifest.write_text(json.dumps([".gitignore", "src/index.ts"]), encoding="utf-8")
    result = subject.check(args(root, manifest))
    assert result["status"] == "REJECT"
    assert any(item["code"] == "MISSING_RELATIVE_DEPENDENCY" for item in result["violations"])


def test_committed_unicode_importer_is_checked_against_explicit_baseline(tmp_path: Path) -> None:
    root, manifest = fixture(tmp_path)
    baseline = subject.git(root, "rev-parse", "HEAD").stdout.strip()
    run(root, "git", "config", "core.quotepath", "true")
    (root / "src").mkdir()
    (root / "src/caf\u00e9.ts").write_text("export { absent } from './absent';\n", encoding="utf-8")
    run(root, "git", "add", "src")
    run(root, "git", "commit", "-m", "unicode importer")
    manifest.write_text("[]", encoding="utf-8")
    result = subject.check(args(root, manifest, baseline))
    assert result["status"] == "REJECT"
    assert result["sourceFilesChecked"] == 1
    assert any(item["code"] == "MISSING_RELATIVE_DEPENDENCY" for item in result["violations"])


def test_owned_unicode_pending_path_is_not_git_quoted(tmp_path: Path) -> None:
    root, manifest = fixture(tmp_path)
    (root / "caf\u00e9.ts").write_text("export const ok = true;\n", encoding="utf-8")
    manifest.write_text(json.dumps(["caf\u00e9.ts"]), encoding="utf-8")
    result = subject.check(args(root, manifest))
    assert result["status"] == "PASS"
    assert result["pendingPaths"] == ["caf\u00e9.ts"]


def test_invalid_source_bytes_cannot_be_replaced_into_pass(tmp_path: Path) -> None:
    root, manifest = fixture(tmp_path)
    (root / "bad.ts").write_bytes(b"export const ok = '\xff';\n")
    manifest.write_text('["bad.ts"]', encoding="utf-8")
    result = subject.check(args(root, manifest))
    assert result["status"] == "REJECT"
    assert any(item["code"] == "INVALID_SOURCE_ENCODING" for item in result["violations"])


def test_invalid_baseline_ref_is_not_success_even_without_imports(tmp_path: Path) -> None:
    root, manifest = fixture(tmp_path)
    manifest.write_text("[]", encoding="utf-8")
    with pytest.raises(RuntimeError, match="baseline"):
        subject.check(args(root, manifest, "does-not-exist"))


def test_receipt_identifies_head_baseline_and_source_overlay_bytes(tmp_path: Path) -> None:
    root, manifest = fixture(tmp_path)
    source = root / "ok.ts"
    source.write_bytes(b"export const ok = true;\n")
    manifest.write_text('["ok.ts"]', encoding="utf-8")
    first = subject.check(args(root, manifest))
    assert first["headSha"] == subject.git(root, "rev-parse", "HEAD").stdout.strip()
    assert first["baselineSha"] == first["headSha"]
    assert first["sourceFileSha256"] == {"ok.ts": hashlib.sha256(source.read_bytes()).hexdigest()}
    source.write_bytes(b"export const ok = false;\n")
    second = subject.check(args(root, manifest))
    assert second["headSha"] == first["headSha"]
    assert second["sourceFileSha256"] != first["sourceFileSha256"]


@pytest.mark.parametrize("value", [{"ok.ts": True}, [1], "ok.ts"])
def test_manifest_must_be_string_array(tmp_path: Path, value: object) -> None:
    root, manifest = fixture(tmp_path)
    manifest.write_text(json.dumps(value), encoding="utf-8")
    with pytest.raises(RuntimeError, match="authorized paths"):
        subject.check(args(root, manifest))


def test_cli_bad_baseline_is_error_and_exit_one(tmp_path: Path) -> None:
    root, manifest = fixture(tmp_path)
    manifest.write_text("[]", encoding="utf-8")
    proc = subprocess.run([sys.executable, str(Path(subject.__file__).resolve()),
        "--public-root", str(root), "--authorized-paths-json", str(manifest),
        "--expected-remote", REMOTE, "--expected-branch", "main",
        "--baseline-ref", "does-not-exist", "--json"], capture_output=True, text=True, check=False)
    assert proc.returncode == 1
    assert json.loads(proc.stdout)["status"] == "ERROR"


@pytest.mark.parametrize("specifier,dependency", [("./dep.ts", "dep.ts"), ("./dep.js", "dep.ts"), ("./dep", "dep/index.ts"), ("./dep.manager", "dep.manager.ts")])
def test_git_visible_resolution_forms_remain_valid(tmp_path: Path, specifier: str, dependency: str) -> None:
    root, manifest = fixture(tmp_path)
    (root / "src").mkdir()
    target = root / "src" / dependency
    target.parent.mkdir(exist_ok=True)
    target.write_text("export const ok = true;\n", encoding="utf-8")
    (root / "src/index.ts").write_text(f"export {{ ok }} from '{specifier}';\n", encoding="utf-8")
    manifest.write_text(json.dumps(["src/index.ts", "src/" + dependency]), encoding="utf-8")
    assert subject.check(args(root, manifest))["status"] == "PASS"


def test_tracked_module_remains_candidate_despite_ignore_rule(tmp_path: Path) -> None:
    root, manifest = fixture(tmp_path)
    (root / "dep.ts").write_text("export const ok = true;\n", encoding="utf-8")
    run(root, "git", "add", "dep.ts")
    run(root, "git", "commit", "-m", "tracked dependency")
    (root / ".gitignore").write_text("dep.ts\n", encoding="utf-8")
    (root / "index.ts").write_text("export { ok } from './dep';\n", encoding="utf-8")
    manifest.write_text('[".gitignore", "index.ts"]', encoding="utf-8")
    assert subject.check(args(root, manifest))["status"] == "PASS"


@pytest.mark.parametrize("ignored,expected_status,expected_exit", [(False, "PASS", 0), (True, "REJECT", 1)])
def test_cli_dependency_disposition_matches_json_and_exit(tmp_path: Path, ignored: bool, expected_status: str, expected_exit: int) -> None:
    root, manifest = fixture(tmp_path)
    (root / "dep.ts").write_text("export const ok = true;\n", encoding="utf-8")
    (root / "index.ts").write_text("export { ok } from './dep';\n", encoding="utf-8")
    if ignored:
        (root / ".gitignore").write_text("dep.ts\n", encoding="utf-8")
    manifest.write_text(json.dumps(["index.ts", ".gitignore"] if ignored else ["index.ts", "dep.ts"]), encoding="utf-8")
    proc = subprocess.run([sys.executable, str(Path(subject.__file__).resolve()),
        "--public-root", str(root), "--authorized-paths-json", str(manifest),
        "--expected-remote", REMOTE, "--expected-branch", "main", "--json"],
        capture_output=True, text=True, check=False)
    body = json.loads(proc.stdout)
    assert proc.returncode == expected_exit
    assert body["status"] == expected_status
    assert body["headSha"] == body["baselineSha"]
