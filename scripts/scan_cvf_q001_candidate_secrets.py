#!/usr/bin/env python3
"""Secret-safe, bounded scan of the Q001 CVF Web candidate and HTML artifacts.

This is a diagnostic gate for the selected HTML slice, not the release bundle.
Only Git-visible candidate files and explicitly supplied artifacts are scanned.
Ignored local credential files are outside the candidate and are never read.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

from cvf_release_secret_scan_policy import SCAN_EXTENSIONS, SECRET_PATTERNS

REPO_ROOT = Path(__file__).resolve().parent.parent
CANDIDATE = Path("EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web")
CANDIDATE_EXTENSIONS = SCAN_EXTENSIONS | {"", ".html", ".cjs", ".mjs", ".css", ".svg", ".toml", ".txt", ".csv", ".example", ".sql"}
Q001_EXTRA_PATTERNS = [
    r"\bAKIA[0-9A-Z]{16}\b",
    r"\bgithub_pat_[A-Za-z0-9_]{20,}\b",
]

# Existing non-live test fixtures, admitted by exact path, line number and
# SHA-256 of the entire line. No test directory or placeholder-wide bypass.
FIXTURE_FINGERPRINTS = {
    ("src/app/api/artifacts/export/route.test.ts", 118, "e8879763895c762d69e04c653f98f1fc7079ee0556237c6558fcf127ab7ca1d7"),
    ("src/app/api/execute/route.dlp.live.test.ts", 136, "d89410e88153f2bf32eaa93a9ccd89e7a9fc4b04edeebb3be8bdb63a96831ddc"),
    ("src/app/api/execute/route.test.ts", 225, "a3c0eab74f14b77ded2eeb0400c2ab7bf72e7b484a3e208dbc6ad666c1a81825"),
    ("src/app/api/execute/route.test.ts", 406, "c6d8956d73a64b0374cffceec31cbd0b62db8e50cde67bd54abe4eba1853bbf5"),
    ("src/app/api/providers/route.test.ts", 78, "3715a54fc776e9aa8f819fefb5a11f4a1ad305221cb3fb435e364db1e21c98e0"),
    ("src/app/api/providers/route.test.ts", 111, "4fece71ea1c5c4dbbf963136222eab099a30149380b42c80da4de54fc71a99e5"),
    ("src/app/api/providers/route.test.ts", 133, "4fece71ea1c5c4dbbf963136222eab099a30149380b42c80da4de54fc71a99e5"),
    ("src/app/api/providers/route.test.ts", 135, "c6d8956d73a64b0374cffceec31cbd0b62db8e50cde67bd54abe4eba1853bbf5"),
    ("src/lib/security.test.ts", 56, "5bd2cbbc6555909747e5653ef6235de7b59962717e7a986cc54e50c17f6b84f2"),
}


def candidate_files() -> list[Path]:
    raw = subprocess.check_output(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", str(CANDIDATE)],
        cwd=REPO_ROOT,
    )
    return sorted({REPO_ROOT / name.decode("utf-8") for name in raw.split(b"\0") if name})


def read_lines(path: Path) -> list[str]:
    raw = path.read_bytes()
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        return raw.decode("utf-16").splitlines()
    if len(raw) >= 4 and raw[1::2].count(0) > len(raw[1::2]) // 2:
        return raw.decode("utf-16-le").splitlines()
    return raw.decode("utf-8").splitlines()


def scan(files: list[tuple[Path, str]], candidate_root: Path = REPO_ROOT / CANDIDATE) -> dict:
    patterns = [re.compile(pattern) for pattern in (*SECRET_PATTERNS, *Q001_EXTRA_PATTERNS)]
    report = {
        "status": "PASS",
        "filesConsidered": 0,
        "filesScanned": 0,
        "filesSkippedExtension": 0,
        "filesUnreadable": 0,
        "fixtureLinesAllowed": 0,
        "findings": [],
        "unreadable": [],
    }
    for index, (path, kind) in enumerate(files, 1):
        report["filesConsidered"] += 1
        label = path.relative_to(REPO_ROOT).as_posix() if kind == "candidate" else f"artifact:{index}"
        if not path.is_file() or path.is_symlink():
            report["filesUnreadable"] += 1
            report["unreadable"].append(label)
            continue
        if kind == "candidate" and path.suffix.lower() not in CANDIDATE_EXTENSIONS:
            report["filesSkippedExtension"] += 1
            continue
        try:
            lines = read_lines(path)
        except (OSError, UnicodeError):
            report["filesUnreadable"] += 1
            report["unreadable"].append(label)
            continue
        report["filesScanned"] += 1
        for number, line in enumerate(lines, 1):
            if not any(pattern.search(line) for pattern in patterns):
                continue
            fixture_path = path.relative_to(candidate_root).as_posix() if kind == "candidate" else ""
            digest = hashlib.sha256(line.encode("utf-8")).hexdigest()
            if kind == "candidate" and (fixture_path, number, digest) in FIXTURE_FINGERPRINTS:
                report["fixtureLinesAllowed"] += 1
                continue
            report["findings"].append({"path": label, "line": number})
    if report["findings"] or report["filesUnreadable"]:
        report["status"] = "FAIL"
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact", action="append", type=Path, default=[], help="HTML artifact to scan")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    files = [(path, "candidate") for path in candidate_files()]
    files.extend((path, "artifact") for path in args.artifact)
    report = scan(files)
    report["scope"] = "git-visible cvf-web candidate plus explicit artifacts"
    report["ignoredLocalEnvPresent"] = (REPO_ROOT / CANDIDATE / ".env.local").exists()
    if args.json:
        print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    else:
        print(f"{report['status']}: scanned={report['filesScanned']} skipped_extension={report['filesSkippedExtension']} "
              f"unreadable={report['filesUnreadable']} exact_fixtures={report['fixtureLinesAllowed']} "
              f"findings={len(report['findings'])}")
        for finding in report["findings"]:
            print(f"  {finding['path']}:{finding['line']}")
        for label in report["unreadable"]:
            print(f"  unreadable: {label}")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
