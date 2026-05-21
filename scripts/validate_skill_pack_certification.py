\
#!/usr/bin/env python3
"""Validate a CVF certified skill pack against the eight-artifact intake contract."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except Exception as exc:  # pragma: no cover - explicit operational blocker
    print(json.dumps({
        "result": "FAIL",
        "reason": "missing_dependency:jsonschema",
        "detail": str(exc),
    }, indent=2))
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "governance" / "schemas" / "skill-pack"
ARTIFACTS = [
    ("skill.meta.json", "skill.meta.schema.json", "json"),
    ("risk.profile.json", "risk.profile.schema.json", "json"),
    ("authority.scope.json", "authority.scope.schema.json", "json"),
    ("execution.boundary.json", "execution.boundary.schema.json", "json"),
    ("receipt.schema.json", "receipt.schema.schema.json", "json"),
    ("workflow.binding.json", "workflow.binding.schema.json", "json"),
    ("workflow.spec.md", "workflow.spec.schema.json", "markdown"),
    ("failure.recovery.md", "failure.recovery.schema.json", "markdown"),
]
MARKDOWN_KEYS = {
    "workflow.spec.md": {
        "inputContract": "Input Contract",
        "outputContract": "Output Contract",
        "deterministicFixturePath": "Deterministic Fixture Path",
    },
    "failure.recovery.md": {
        "failureModes": "Failure Modes",
        "recoveryActions": "Recovery Actions",
        "rollbackPolicy": "Rollback Policy",
    },
}


def normalize_heading(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def load_markdown_artifact(path: Path, artifact_name: str) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    sections: dict[str, str] = {}
    headings = [(m.start(), m.group(1).strip()) for m in re.finditer(r"^##\s+(.+?)\s*$", text, re.MULTILINE)]
    expected = MARKDOWN_KEYS[artifact_name]
    for index, (start, heading) in enumerate(headings):
        next_start = headings[index + 1][0] if index + 1 < len(headings) else len(text)
        body_start = text.find("\n", start) + 1
        body = text[body_start:next_start].strip()
        for key, expected_heading in expected.items():
            if normalize_heading(heading) == normalize_heading(expected_heading):
                sections[key] = body
    missing = [key for key in expected if not sections.get(key)]
    return sections, missing


def validate_pack(pack_dir: Path) -> dict:
    artifact_results = []
    for artifact, schema_name, artifact_type in ARTIFACTS:
        artifact_path = pack_dir / artifact
        if not artifact_path.exists():
            artifact_results.append({"name": artifact, "result": "FAIL", "reason": f"missing_artifact:{artifact}"})
            continue
        schema_path = SCHEMA_DIR / schema_name
        if not schema_path.exists():
            artifact_results.append({"name": artifact, "result": "FAIL", "reason": f"missing_schema:{schema_name}"})
            continue
        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            artifact_results.append({"name": artifact, "result": "FAIL", "reason": f"invalid_schema_json:{schema_name}:{exc.msg}"})
            continue
        if artifact_type == "json":
            try:
                payload = json.loads(artifact_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                artifact_results.append({"name": artifact, "result": "FAIL", "reason": f"invalid_json:{artifact}:{exc.msg}"})
                continue
        else:
            payload, missing = load_markdown_artifact(artifact_path, artifact)
            if missing:
                artifact_results.append({"name": artifact, "result": "FAIL", "reason": f"missing_markdown_section:{artifact}:{missing[0]}"})
                continue
        errors = sorted(Draft202012Validator(schema).iter_errors(payload), key=lambda err: list(err.path))
        if errors:
            err = errors[0]
            path = ".".join(str(part) for part in err.path) or "root"
            artifact_results.append({"name": artifact, "result": "FAIL", "reason": f"schema_validation:{artifact}:{path}:{err.message}"})
        else:
            artifact_results.append({"name": artifact, "result": "PASS"})
    result = "PASS" if all(item["result"] == "PASS" for item in artifact_results) else "FAIL"
    return {"pack": str(pack_dir), "result": result, "artifacts": artifact_results}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a CVF certified skill pack")
    parser.add_argument("pack_dir", help="Path to the certified skill pack directory")
    args = parser.parse_args()
    pack_dir = Path(args.pack_dir)
    if not pack_dir.exists() or not pack_dir.is_dir():
        print(json.dumps({"pack": str(pack_dir), "result": "FAIL", "reason": "pack_dir_not_found"}, indent=2))
        return 1
    result = validate_pack(pack_dir)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
