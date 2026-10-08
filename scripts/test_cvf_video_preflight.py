"""Focused tests for scripts/cvf_video_preflight.py (local validation only).

Fixtures are synthetic and live under the ignored, worker-owned root
.cvf/runtime/cvf-video-preparation-worker-20261008; each test removes only its own
subdirectory. No governance engine is mocked and no CVF governance proof is claimed.
"""
from __future__ import annotations

import ast
import contextlib
import copy
import hashlib
import io
import json
import os
import shutil
import socket
import subprocess
import sys
import unittest
import urllib.request
import uuid
from collections import namedtuple
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cvf_video_preflight as pf  # noqa: E402

REPO = HERE.parent
OWNED = REPO / ".cvf" / "runtime" / "cvf-video-preparation-worker-20261008"
DESIGN = REPO / "docs" / "reference" / "CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md"
SCRIPT = HERE / "cvf_video_preflight.py"
SCOPES = ["SOURCE_CODE", "WEIGHTS", "CODEC", "VOICE", "FONT", "BINARY"]


def sha(data):
    return hashlib.sha256(data).hexdigest()


class Fixture:
    """Build a complete synthetic manifest plus its resource files."""

    def __init__(self, base):
        self.base, self.root = base, base / "res"
        self.root.mkdir(parents=True)
        self.artifacts = []
        self.pins = None
        self._build()

    def add(self, aid, cat, place, rel, data=None, **extra):
        data = data if data is not None else ("synthetic:" + aid).encode()
        target = self.root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        art = {"id": aid, "category": cat, "placement": place, "path": rel, "sha256": sha(data), "bytes": len(data),
               "origin": {"kind": "operator_supplied", "identity": "synthetic-fixture:" + aid, "immutable": True},
               "rights": {"disposition": "CLEARED_PINNED_EVIDENCE", "evidenceArtifactId": "rights-all"}}
        art.update(extra)
        self.artifacts.append(art)
        return art

    def _build(self):
        self.add("rights-all", "rights_attribution", "FINAL", "rights/notice.txt", rightsScopes=SCOPES, rights=None)
        self.add("enforce-1", "enforcement_evidence", "FINAL", "enforce/receipt.txt", rights=None)
        for dist in pf.CORE_DISTRIBUTIONS:
            self.add("whl-" + dist, "python_wheel", "CACHE", "py/%s-1.0.0-cp311-cp311-win_amd64.whl" % dist.replace("-", "_"),
                     distribution=dist)
        locks = {}
        for comp, name in pf.LOCK_PIN_PATHS.items():
            art = self.add("lock-" + comp, "source_lock", "FINAL", "src/" + name)
            locks[(comp, name)] = (art["sha256"], art["bytes"])
        self.pins = tuple((c, p, path, *locks.get((c, path), (s, b))) for c, p, path, s, b in pf.ACCEPTED_SOURCE_PINS)
        for cat in ("model_graph", "model_config", "tokenizer", "codec", "preset"):
            for name in pf.FILE_SETS[cat]:
                self.add("%s-%s" % (cat, name), cat, "FINAL", "%s/%s" % (cat, name))
        self.add("phon", "phonemizer", "CACHE", "phonemizer/sea_g2p-dict.bin")
        self.add("browser", "browser", "CACHE", "browser/chrome.zip")
        self.add("ffmpeg", "ffmpeg", "CACHE", "ffmpeg/ffmpeg.exe")
        self.add("font", "font", "FINAL", "fonts/Vietnamese-Regular.ttf")
        self.add("dup", "model_config", "DUPLICATE", "dup/config-copy.json")

    def manifest(self):
        got = pf.extract_s05(DESIGN.read_bytes())
        frames = [{"frameId": "S05-F%02d" % (i + 1), "statusCardText": got["statusCardText"],
                   "statusCardSha256": got["statusCard"]["sha256"], "segmentSha256": seg["sha256"], "claimIds": ["C09", "C10"]}
                  for i, seg in enumerate(got["segments"])]
        ceil = {k: {"value": 10 ** 9 if u == "bytes" else 100, "unit": u, "status": "PROPOSED_NOT_ENFORCED"}
                for k, (u, _i) in pf.CEILINGS.items()}
        ceil["cancellation_grace_seconds"]["value"] = 10
        ceil["log_evidence_bytes"]["value"] = 10 ** 6
        ceil["aggregate_disk_bytes"]["value"] = 5 * 10 ** 9
        return {
            "schemaVersion": pf.MANIFEST_SCHEMA, "artifacts": copy.deepcopy(self.artifacts),
            "sourcePins": [{"component": c, "pin": p, "path": path, "sha256": s, "bytes": b, "freshness": pf.FRESHNESS}
                           for c, p, path, s, b in self.pins],
            "ceilings": ceil, "enforcement": {c: {"evidenceArtifactId": "enforce-1"} for c in pf.ENFORCEMENT_CONTROLS},
            "voice": {"presetId": "synthetic-preset", "presetArtifactId": "preset-voices_v3_turbo.json",
                      "consentArtifactId": "rights-all", "presetSource": "MODEL_ROOT_OVERRIDE_FILE",
                      "codec": {"resolution": "ENGINE_DIRECT_CODEC_DIR", "decisionRef": "synthetic-decision"}, "backend": "onnx", "device": "cpu", "precision": "fp32",
                      "cloning": False, "paidOrHostedVoice": False,
                      "denoiser": {"disposition": "ABSENT_ACCEPTED_PRESET_ONLY", "decisionRef": "synthetic-decision"}},
            "s05": {"designRawSha256": got["designRawSha256"], "narrationSha256": got["narration"]["sha256"],
                    "onScreenSha256": got["onScreen"]["sha256"], "statusCardSha256": got["statusCard"]["sha256"],
                    "claimIds": ["C09", "C10"], "originalEstimateSeconds": 20, "measuredNarrationSeconds": None,
                    "retiming": {"disposition": "NONE_NOT_MEASURED"}, "plannedFrames": frames}}


class Base(unittest.TestCase):
    def setUp(self):
        OWNED.mkdir(parents=True, exist_ok=True)
        self.base = OWNED / uuid.uuid4().hex[:12]
        self.fx = Fixture(self.base)
        self.addCleanup(self.cleanup)

    def cleanup(self):
        assert self.base.parent == OWNED
        shutil.rmtree(self.base, ignore_errors=True)

    def run_pf(self, mutate=None, design=DESIGN, root=None, pins="fixture", raw=None):
        manifest = self.fx.manifest()
        if mutate:
            mutate(manifest)
        path = self.base / "manifest.json"
        path.write_text(raw(json.dumps(manifest)) if raw else json.dumps(manifest), encoding="utf-8")
        use = self.fx.pins if pins == "fixture" else None
        return pf.run_preflight(str(path), str(root or self.fx.root), str(design) if design else None, pins=use)

    def assertCode(self, report, code, cls=None, status=None):
        rows = [r for r in report["noGoMatrix"] if r["code"] == code]
        self.assertTrue(rows, "%s not in %s" % (code, report["reasonCodes"]))
        if cls:
            self.assertEqual({r["class"] for r in rows}, {cls})
        self.assertEqual(report["runtimeAdmission"], "NO_GO")
        if status:
            self.assertEqual(report["validationStatus"], status)

    def mut_art(self, aid, **kw):
        def fn(m):
            for a in m["artifacts"]:
                if a["id"] == aid:
                    a.update(kw)
        return fn


class PositiveControl(Base):
    def test_valid_fixture_is_structurally_complete_but_never_runtime_go(self):
        report = self.run_pf()
        self.assertEqual(report["validationStatus"], "STRUCTURALLY_COMPLETE_NO_GO", report["noGoMatrix"])
        self.assertEqual(report["runtimeAdmission"], "NO_GO")
        self.assertEqual(report["osContainment"], "NOT_ESTABLISHED")
        self.assertEqual({r["class"] for r in report["noGoMatrix"]}, {"STANDING_NO_GO"})
        for code, _ in pf.STANDING_NO_GO:
            self.assertIn(code, report["reasonCodes"])
        self.assertTrue(all(a["hashVerified"] for a in report["artifacts"]))
        self.assertEqual(report["resourceArithmetic"]["ceilingStatus"], "PROPOSED_NOT_ENFORCED")
        self.assertEqual(report["s05Extraction"]["narrationSha256"], pf.S05_ACCEPTED["narrationSha256"])

    def test_report_is_deterministic_and_free_of_timestamps(self):
        a, b = pf.canonical(self.run_pf()), pf.canonical(self.run_pf())
        self.assertEqual(a, b)
        self.assertNotIn("utc", a.lower())

    def test_cli_exit_codes_and_exclusive_report(self):
        manifest = self.base / "manifest.json"
        manifest.write_text(json.dumps(self.fx.manifest()), encoding="utf-8")
        report = self.base / "report.json"
        argv = ["--manifest", str(manifest), "--root", str(self.fx.root), "--design", str(DESIGN), "--report", str(report)]
        with mock.patch.object(pf, "ACCEPTED_SOURCE_PINS", self.fx.pins):
            self.assertEqual(pf.main(argv), 0)
            self.assertEqual(json.loads(report.read_text(encoding="utf-8"))["runtimeAdmission"], "NO_GO")
            with self.assertRaises(FileExistsError):
                pf.main(argv)
            inside = self.fx.root / "report-inside.json"
            with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
                pf.main(argv[:-1] + [str(inside)])
            self.assertFalse(inside.exists())
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = pf.main(["--manifest", str(manifest), "--root", str(self.fx.root), "--design", str(DESIGN)])
        self.assertEqual(code, 1)  # frozen pins reject the synthetic lock bytes
        self.assertIn("SOURCE_LOCK_DRIFT", out.getvalue())

    def test_extract_s05_matches_accepted_identity(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(pf.main(["--extract-s05", "--design", str(DESIGN)]), 0)
        got = json.loads(out.getvalue())
        self.assertEqual(got["designRawSha256"], pf.S05_ACCEPTED["designRawSha256"])
        self.assertEqual(got["narration"]["sha256"], pf.S05_ACCEPTED["narrationSha256"])
        self.assertEqual(got["onScreen"]["sha256"], pf.S05_ACCEPTED["onScreenSha256"])
        self.assertEqual(got["statusCard"]["sha256"], pf.S05_ACCEPTED["statusCardSha256"])
        self.assertEqual((got["narration"]["utf8Bytes"], got["onScreen"]["utf8Bytes"]), (314, 345))
        self.assertEqual(got["claimIds"], ["C09", "C10"])
        self.assertEqual(len(got["segments"]), 4)


class ArtifactControls(Base):
    def test_missing_artifact_is_incomplete(self):
        (self.fx.root / "tokenizer" / "tokenizer.json").unlink()
        self.assertCode(self.run_pf(), "ARTIFACT_MISSING", "INCOMPLETE", "INCOMPLETE_NO_GO")

    def test_hash_and_size_mismatch_are_invalid(self):
        (self.fx.root / "codec" / "codec_browser_onnx_meta.json").write_bytes(b"x" * len(b"synthetic:codec-codec_browser_onnx_meta.json"))
        self.assertCode(self.run_pf(), "HASH_MISMATCH", "INVALID", "INVALID_NO_GO")
        with open(self.fx.root / "fonts" / "Vietnamese-Regular.ttf", "ab") as fh:
            fh.write(b"extra")
        self.assertCode(self.run_pf(), "SIZE_MISMATCH", "INVALID")

    def test_malformed_hash_bytes_origin_and_floating_revision(self):
        self.assertCode(self.run_pf(self.mut_art("font", sha256="ABC")), "HASH_MALFORMED", "INVALID")
        self.assertCode(self.run_pf(self.mut_art("font", bytes=True)), "BYTES_MALFORMED", "INVALID")
        self.assertCode(self.run_pf(self.mut_art("font", origin={"kind": "hf_revision", "identity": "repo@main", "immutable": True,
                                                                "revision": "main"})), "ORIGIN_NOT_IMMUTABLE", "INVALID")
        self.assertCode(self.run_pf(self.mut_art("font", origin={"kind": "operator_supplied", "identity": "x", "immutable": False})),
                        "ORIGIN_NOT_IMMUTABLE")

    def test_traversal_absolute_and_unsafe_paths_rejected(self):
        outside = self.base / "outside.bin"
        outside.write_bytes(b"outside")
        for bad in ("../outside.bin", "a/../../outside.bin", "./font.ttf", "fonts//x.ttf", str(outside).replace("\\", "/"),
                    "/etc/passwd", "C:/Windows/system.ini", "fonts\\x.ttf", "fonts/x.ttf.", "", None):
            report = self.run_pf(self.mut_art("font", path=bad))
            self.assertCode(report, "PATH_REJECTED", "INVALID")

    def test_symlink_and_reparse_links_rejected(self):
        outside = self.base / "outside-dir"
        outside.mkdir()
        (outside / "Vietnamese-Regular.ttf").write_bytes(b"synthetic:font")
        link = self.fx.root / "linked"
        try:
            os.symlink(outside, link, target_is_directory=True)
        except (OSError, NotImplementedError):
            link = None
        if link is not None:
            report = self.run_pf(self.mut_art("font", path="linked/Vietnamese-Regular.ttf"))
            self.assertCode(report, "LINK_OR_UNSAFE_PATH_REJECTED", "INVALID")
        Stat = namedtuple("Stat", "st_mode st_file_attributes st_size")
        self.assertTrue(pf.is_link_like(Stat(0o100644, 0x400, 1)))
        self.assertFalse(pf.is_link_like(Stat(0o100644, 0x20, 1)))
        real = os.lstat
        target = str(self.fx.root / "fonts")
        with mock.patch.object(pf.os, "lstat", side_effect=lambda p: Stat(0o040755, 0x400, 0) if str(p) == target else real(p)):
            self.assertEqual(pf.locate(str(self.fx.root), "fonts/Vietnamese-Regular.ttf"), ("LINK", None))

    def test_directory_and_non_regular_targets_rejected(self):
        self.assertCode(self.run_pf(self.mut_art("font", path="fonts")), "NOT_REGULAR_FILE", "INVALID")
        self.assertCode(self.run_pf(self.mut_art("font", path="fonts/Vietnamese-Regular.ttf/sub")), "PATH_UNREADABLE", "INVALID")

    def test_duplicate_targets_and_ids(self):
        report = self.run_pf(self.mut_art("browser", path="FONTS/vietnamese-regular.TTF"))
        self.assertCode(report, "DUPLICATE_TARGET", "INVALID")
        self.assertCode(self.run_pf(lambda m: m["artifacts"].append(copy.deepcopy(m["artifacts"][-1]))), "DUPLICATE_ARTIFACT_ID", "INVALID")

    def test_size_bound_applies_before_hashing(self):
        with mock.patch.object(pf, "MAX_ARTIFACT_BYTES", 4), mock.patch.object(pf, "hash_stream", side_effect=AssertionError("hashed")):
            self.assertCode(self.run_pf(), "SIZE_OVER_BOUND", "INVALID")

    def test_root_must_be_plain_owned_directory(self):
        self.assertCode(self.run_pf(root=self.base / "absent"), "ROOT_UNREADABLE", "INVALID")
        self.assertCode(self.run_pf(root=self.fx.root / "fonts" / "Vietnamese-Regular.ttf"), "ROOT_NOT_PLAIN_DIRECTORY", "INVALID")
        cache = self.base / ".cache" / "res"
        cache.mkdir(parents=True)
        self.assertCode(self.run_pf(root=cache), "ROOT_IS_SHARED_CACHE", "INVALID")


class ManifestControls(Base):
    def run_raw(self, text):
        path = self.base / "raw.json"
        path.write_bytes(text if isinstance(text, bytes) else text.encode("utf-8"))
        return pf.run_preflight(str(path), str(self.fx.root), str(DESIGN), pins=self.fx.pins)

    def test_malformed_manifests(self):
        for raw in ("{not json", "[]", '{"a": 1, "a": 2}', '{"schemaVersion": "x"}', b"\xff\xfe", '{"ceilings": NaN}'):
            report = self.run_raw(raw)
            self.assertTrue({"MANIFEST_MALFORMED", "MANIFEST_SCHEMA_UNSUPPORTED"} & set(report["reasonCodes"]), raw)
            self.assertEqual(report["validationStatus"], "INVALID_NO_GO")
        with mock.patch.object(pf, "MAX_MANIFEST_BYTES", 10):
            self.assertCode(self.run_raw(json.dumps(self.fx.manifest())), "MANIFEST_MALFORMED", "INVALID")

    def test_category_and_file_set_gaps_remain_no_go(self):
        self.assertCode(self.run_pf(lambda m: m.update(artifacts=[a for a in m["artifacts"] if a["category"] != "browser"])),
                        "CATEGORY_MISSING", "INCOMPLETE")
        self.assertCode(self.run_pf(lambda m: m.update(artifacts=[a for a in m["artifacts"] if "decode_full" not in a["id"]])),
                        "CODEC_MISSING", "INCOMPLETE")
        self.assertCode(self.run_pf(lambda m: m.update(artifacts=[a for a in m["artifacts"] if "heads" not in a["id"]])),
                        "SOURCE_FILE_SET_INCOMPLETE", "INCOMPLETE")
        self.assertCode(self.run_pf(self.mut_art("font", category="font-unknown")), "ARTIFACT_CATEGORY_UNKNOWN", "INVALID")

    def test_wheel_closure_platform_and_filename(self):
        self.assertCode(self.run_pf(lambda m: m.update(artifacts=[a for a in m["artifacts"] if a.get("distribution") != "gradio"])),
                        "PYTHON_CLOSURE_INCOMPLETE", "INCOMPLETE")
        self.assertCode(self.run_pf(self.mut_art("whl-numpy", path="py/numpy-1.0.0-cp311-cp311-manylinux2014_x86_64.whl")),
                        "ARTIFACT_MISSING")
        (self.fx.root / "py" / "numpy-1.0.0-cp311-cp311-win_amd64.whl").rename(self.fx.root / "py" / "numpy-1.0.0-cp311-cp311-manylinux2014_x86_64.whl")
        self.assertCode(self.run_pf(self.mut_art("whl-numpy", path="py/numpy-1.0.0-cp311-cp311-manylinux2014_x86_64.whl")),
                        "WHEEL_PLATFORM_MISMATCH", "INVALID")
        (self.fx.root / "py" / "numpy.tar.gz").write_bytes(b"synthetic:whl-numpy")
        self.assertCode(self.run_pf(self.mut_art("whl-numpy", path="py/numpy.tar.gz")), "WHEEL_FILENAME_INVALID", "INVALID")


class RightsAndVoiceControls(Base):
    def test_unknown_missing_and_unverified_rights_are_not_cleared(self):
        for rights, code in (({"disposition": "UNKNOWN"}, "RIGHTS_UNKNOWN"), (None, "RIGHTS_UNKNOWN"),
                             ({"disposition": "PUBLISHER_DECLARED_UNVERIFIED"}, "RIGHTS_NOT_CLEARED")):
            report = self.run_pf(self.mut_art("model_graph-vieneu_prefill.onnx", rights=rights))
            self.assertCode(report, code, "INCOMPLETE", "INCOMPLETE_NO_GO")
        self.assertCode(self.run_pf(self.mut_art("font", rights={"disposition": "TRUST_ME"})), "RIGHTS_DISPOSITION_INVALID", "INVALID")
        self.assertCode(self.run_pf(self.mut_art("font", rights={"disposition": "CLEARED_PINNED_EVIDENCE", "evidenceArtifactId": "nope"})),
                        "RIGHTS_EVIDENCE_UNRESOLVED", "INVALID")

    def test_source_license_alone_does_not_clear_weights_codec_voice_or_fonts(self):
        def only_code_license(m):
            m["artifacts"].append(dict(copy.deepcopy(m["artifacts"][0]), id="rights-code", path="rights/code.txt", rightsScopes=["SOURCE_CODE"]))
            for a in m["artifacts"]:
                if a["category"] in ("model_graph", "codec", "preset", "font"):
                    a["rights"] = {"disposition": "CLEARED_PINNED_EVIDENCE", "evidenceArtifactId": "rights-code"}
        (self.fx.root / "rights" / "code.txt").write_bytes(b"synthetic:rights-all")
        rows = [r for r in self.run_pf(only_code_license)["noGoMatrix"] if r["code"] == "RIGHTS_SCOPE_INSUFFICIENT"]
        subjects = {r["subject"] for r in rows}
        self.assertIn("font", subjects)
        self.assertIn("codec-moss_audio_tokenizer_decode_full.onnx", subjects)
        self.assertIn("preset-voices_v3_turbo.json", subjects)
        self.assertIn("model_graph-vieneu_prefill.onnx", subjects)

    def test_preset_codec_and_denoiser_dispositions(self):
        def no_preset(m):
            m["artifacts"] = [a for a in m["artifacts"] if a["category"] != "preset"]
        report = self.run_pf(no_preset)
        self.assertCode(report, "PRESET_MISSING", "INCOMPLETE")
        self.assertCode(report, "CATEGORY_MISSING", "INCOMPLETE")
        self.assertCode(self.run_pf(lambda m: m["voice"].pop("denoiser")), "DENOISER_DISPOSITION_MISSING", "INCOMPLETE")
        self.assertCode(self.run_pf(lambda m: m["voice"]["denoiser"].pop("decisionRef")), "DENOISER_DISPOSITION_MISSING")
        self.assertCode(self.run_pf(lambda m: m["voice"].update(denoiser={"disposition": "PRESENT_ARTIFACT", "artifactId": "nope"})),
                        "DENOISER_DISPOSITION_MISSING")
        self.assertCode(self.run_pf(lambda m: m["voice"].pop("presetSource")), "PRESET_SOURCE_MISSING", "INCOMPLETE")
        self.assertCode(self.run_pf(lambda m: m["voice"].pop("codec")), "CODEC_DISPOSITION_MISSING", "INCOMPLETE", "INCOMPLETE_NO_GO")
        self.assertCode(self.run_pf(lambda m: m["voice"]["codec"].update(resolution="OPERATOR_DISPOSITION_PENDING")), "CODEC_DISPOSITION_MISSING")
        self.assertCode(self.run_pf(lambda m: m["voice"]["codec"].pop("decisionRef")), "CODEC_DISPOSITION_MISSING")
        self.assertCode(self.run_pf(lambda m: m["voice"]["codec"].update(resolution="PATCH_UPSTREAM_MIRROR")), "CODEC_DISPOSITION_INVALID", "INVALID")
        self.assertCode(self.run_pf(lambda m: m["voice"].update(consentArtifactId="enforce-1")), "VOICE_CONSENT_MISSING", "INCOMPLETE")
        self.assertCode(self.run_pf(lambda m: m.pop("voice")), "VOICE_IDENTITY_MISSING", "INCOMPLETE")

    def test_present_denoiser_artifact_is_accepted(self):
        self.fx.add("den", "denoiser", "FINAL", "denoiser/denoiser.onnx")
        report = self.run_pf(lambda m: m["voice"].update(denoiser={"disposition": "PRESENT_ARTIFACT", "artifactId": "den"}))
        self.assertEqual(report["validationStatus"], "STRUCTURALLY_COMPLETE_NO_GO", report["noGoMatrix"])

    def test_lane_substitution_rejected(self):
        for key, value in (("precision", "int8"), ("device", "cuda"), ("backend", "pytorch"), ("cloning", True),
                           ("paidOrHostedVoice", True), ("cloning", 0)):
            report = self.run_pf(lambda m, k=key, v=value: m["voice"].update({k: v}))
            self.assertCode(report, "LANE_SUBSTITUTION_REJECTED", "INVALID")


class ResourceAndEnforcementControls(Base):
    def test_invalid_and_nonfinite_ceilings(self):
        for value in (0, -5, True, "5", None, 2.5, [1]):
            report = self.run_pf(lambda m, v=value: m["ceilings"]["aggregate_disk_bytes"].update(value=v))
            self.assertCode(report, "CEILING_INVALID", "INVALID")
        for key, literal in (("walltime_seconds", "1e999"), ("peak_committed_ram_bytes", "-1e999"), ("walltime_seconds", "0.0")):
            report = self.run_pf(lambda m, k=key: m["ceilings"][k].update(value="__X__"), raw=lambda t, lit=literal: t.replace('"__X__"', lit))
            self.assertCode(report, "CEILING_INVALID", "INVALID")
        for literal in ("NaN", "Infinity", "-Infinity"):  # non-standard JSON constants never reach the validator
            report = self.run_pf(lambda m: m["ceilings"]["retries"].update(value="__X__"), raw=lambda t, lit=literal: t.replace('"__X__"', lit))
            self.assertCode(report, "MANIFEST_MALFORMED", "INVALID", "INVALID_NO_GO")
        self.assertCode(self.run_pf(lambda m: m["ceilings"].pop("process_count")), "CEILING_MISSING", "INCOMPLETE")
        self.assertCode(self.run_pf(lambda m: m.pop("ceilings")), "CEILINGS_MISSING", "INCOMPLETE")

    def test_enforced_status_and_units_are_rejected(self):
        self.assertCode(self.run_pf(lambda m: m["ceilings"]["retries"].update(status="ENFORCED")),
                        "CEILING_ENFORCEMENT_CLAIM_REJECTED", "INVALID")
        self.assertCode(self.run_pf(lambda m: m["ceilings"]["retries"].update(unit="seconds")), "CEILING_UNIT_INVALID", "INVALID")
        self.assertCode(self.run_pf(lambda m: m["ceilings"]["cancellation_grace_seconds"].update(value=500)), "CEILING_INCONSISTENT", "INVALID")

    def test_per_placement_and_aggregate_disk_overflow(self):
        small = lambda key, v: (lambda m: m["ceilings"][key].update(value=v))
        self.assertCode(self.run_pf(small("download_install_cache_bytes", 5)), "CEILING_EXCEEDED", "INVALID")
        self.assertCode(self.run_pf(small("final_artifact_bytes", 5)), "CEILING_EXCEEDED", "INVALID")
        self.assertCode(self.run_pf(small("duplicated_storage_bytes", 5)), "CEILING_EXCEEDED", "INVALID")
        report = self.run_pf(small("aggregate_disk_bytes", 100))
        self.assertCode(report, "AGGREGATE_DISK_OVERFLOW", "INVALID", "INVALID_NO_GO")
        arithmetic = report["resourceArithmetic"]
        measured = sum(arithmetic["measuredBytesByPlacement"].values())
        self.assertEqual(arithmetic["projectedAggregateDiskBytes"], measured + arithmetic["logEvidenceCeilingBytes"])

    def test_missing_enforcement_evidence_and_presence_changes_nothing_about_no_go(self):
        report = self.run_pf(lambda m: m.pop("enforcement"))
        rows = [r for r in report["noGoMatrix"] if r["code"] == "ENFORCEMENT_EVIDENCE_MISSING"]
        self.assertEqual({r["subject"] for r in rows}, set(pf.ENFORCEMENT_CONTROLS))
        self.assertCode(self.run_pf(lambda m: m["enforcement"].pop("egress_block")), "ENFORCEMENT_EVIDENCE_MISSING", "INCOMPLETE")
        self.assertCode(self.run_pf(lambda m: m["enforcement"]["memory_cap"].update(evidenceArtifactId="font")),
                        "ENFORCEMENT_EVIDENCE_MISSING")
        complete = self.run_pf()
        self.assertEqual((complete["runtimeAdmission"], complete["osContainment"]), ("NO_GO", "NOT_ESTABLISHED"))
        self.assertIn("OS_CONTAINMENT_NOT_ESTABLISHED_BY_VALIDATOR", complete["reasonCodes"])


class SourceAndS05Drift(Base):
    def test_source_pin_drift_missing_and_freshness_label(self):
        def drift(m):
            m["sourcePins"][0]["sha256"] = "0" * 64
        self.assertCode(self.run_pf(drift), "SOURCE_PIN_DRIFT", "INVALID")
        self.assertCode(self.run_pf(lambda m: m["sourcePins"].pop()), "SOURCE_PIN_MISSING", "INCOMPLETE")
        self.assertCode(self.run_pf(lambda m: m["sourcePins"][1].update(freshness="CURRENT_UPSTREAM")), "SOURCE_PIN_DRIFT", "INVALID")
        self.assertCode(self.run_pf(lambda m: m["sourcePins"][2].update(pin="1" * 40)), "SOURCE_PIN_DRIFT")
        self.assertCode(self.run_pf(lambda m: m.pop("sourcePins")), "SOURCE_PIN_MISSING", "INCOMPLETE")

    def test_synthetic_lock_bytes_do_not_satisfy_frozen_pins(self):
        report = self.run_pf(pins="frozen", mutate=lambda m: m.update(sourcePins=[
            {"component": c, "pin": p, "path": path, "sha256": s, "bytes": b, "freshness": pf.FRESHNESS}
            for c, p, path, s, b in pf.ACCEPTED_SOURCE_PINS]))
        self.assertCode(report, "SOURCE_LOCK_DRIFT", "INVALID")

    def test_frozen_pin_table_matches_input_evidence(self):
        evidence = json.loads((REPO / "docs/reviews/evidence/cvf-ncr-video-production-preparation-inputs-2026-10-08.json").read_text("utf-8"))
        table = {(i["path"], i["pin"], i["sha256"], i["bytes"]) for i in evidence["inputs"]}
        self.assertEqual({(p[2], p[1], p[3], p[4]) for p in pf.ACCEPTED_SOURCE_PINS}, table)

    def design_copy(self, edit):
        text = DESIGN.read_bytes().decode("utf-8")
        new = edit(text)
        self.assertNotEqual(new, text)
        path = self.base / "design-copy.md"
        path.write_bytes(new.encode("utf-8"))
        return path

    def test_s05_source_byte_drift_detected(self):
        narr = self.design_copy(lambda t: t.replace("ch\u01b0a ch\u1ea1y th\u1eadt, d\u1eef li\u1ec7u gi\u1ea3. B\u1ea1n c\xf3", "ch\u01b0a ch\u1ea1y th\u1eadt, d\u1eef li\u1ec7u gi\u1ea3.  B\u1ea1n c\xf3", 1))
        self.assertCode(self.run_pf(design=narr), "S05_SOURCE_DRIFT", "INVALID", "INVALID_NO_GO")
        trailing = self.design_copy(lambda t: t + "\n")
        self.assertCode(self.run_pf(design=trailing), "S05_SOURCE_DRIFT", "INVALID")
        claims = self.design_copy(lambda t: t.replace("- Claims: C09, C10", "- Claims: C09, C11", 1))
        self.assertCode(self.run_pf(design=claims), "S05_SOURCE_DRIFT", "INVALID")

    def test_crlf_normalisation_keeps_text_identity_but_not_raw_identity(self):
        crlf = self.base / "crlf.md"
        crlf.write_bytes(DESIGN.read_bytes().replace(b"\r\n", b"\n").replace(b"\n", b"\r\n"))
        got = pf.extract_s05(crlf.read_bytes())
        self.assertEqual(got["narration"]["sha256"], pf.S05_ACCEPTED["narrationSha256"])
        lf = self.base / "lf.md"
        lf.write_bytes(DESIGN.read_bytes().replace(b"\r\n", b"\n"))
        self.assertCode(self.run_pf(design=lf), "S05_SOURCE_DRIFT", "INVALID")

    def test_manifest_binding_drift_and_absent_source(self):
        self.assertCode(self.run_pf(lambda m: m["s05"].update(narrationSha256="1" * 64)), "S05_MANIFEST_DRIFT", "INVALID")
        self.assertCode(self.run_pf(lambda m: m["s05"].update(onScreenSha256="2" * 64)), "S05_MANIFEST_DRIFT", "INVALID")
        self.assertCode(self.run_pf(design=None), "S05_SOURCE_NOT_PROVIDED", "INCOMPLETE")
        self.assertCode(self.run_pf(design=self.base / "missing.md"), "S05_SOURCE_UNREADABLE", "INVALID")
        self.assertCode(self.run_pf(lambda m: m.pop("s05")), "S05_BINDING_MISSING", "INCOMPLETE")

    def test_frames_claims_and_estimate(self):
        self.assertCode(self.run_pf(lambda m: m["s05"]["plannedFrames"][1].update(statusCardText="VI DU")), "S05_FRAME_STATUS_CARD_MISSING", "INVALID")
        self.assertCode(self.run_pf(lambda m: m["s05"]["plannedFrames"][0].update(claimIds=["C09"])), "S05_FRAME_STATUS_CARD_MISSING")
        self.assertCode(self.run_pf(lambda m: m["s05"].update(plannedFrames=[])), "S05_FRAMES_MISSING", "INCOMPLETE")
        self.assertCode(self.run_pf(lambda m: m["s05"].update(claimIds=["C09"])), "S05_CLAIMS_MISMATCH", "INVALID")
        self.assertCode(self.run_pf(lambda m: m["s05"].update(originalEstimateSeconds=22)), "S05_ESTIMATE_ALTERED", "INVALID")

    def test_retiming_keeps_estimate_distinct_from_measurement(self):
        def set_ret(measured, disposition, **extra):
            return lambda m: m["s05"].update(measuredNarrationSeconds=measured, retiming=dict(disposition=disposition, **extra))
        self.assertCode(self.run_pf(set_ret(22.4, "NONE_PAD_WITHIN_SCENE")), "RETIMING_DISPOSITION_REQUIRED", "INVALID")
        self.assertCode(self.run_pf(set_ret(22.4, "PROPOSED_RETIMING_PENDING_APPROVAL")), "RETIMING_APPROVAL_PENDING", "INCOMPLETE")
        self.assertCode(self.run_pf(set_ret(22.4, "APPROVED_RETIMING")), "RETIMING_APPROVAL_UNBOUND", "INVALID")
        ok = self.run_pf(set_ret(22.4, "APPROVED_RETIMING", approvalRef="synthetic-approval"))
        self.assertEqual(ok["validationStatus"], "STRUCTURALLY_COMPLETE_NO_GO", ok["noGoMatrix"])
        self.assertCode(self.run_pf(set_ret("__X__", "NONE_NOT_MEASURED"), raw=lambda t: t.replace('"__X__"', "1e999")),
                        "S05_MEASUREMENT_INVALID", "INVALID")
        self.assertCode(self.run_pf(set_ret(18.0, "BOGUS")), "RETIMING_DISPOSITION_INVALID", "INVALID")


class NoEffects(Base):
    FORBIDDEN_IMPORTS = {"subprocess", "socket", "urllib", "http", "ftplib", "smtplib", "shutil", "tempfile", "ctypes", "ssl",
                         "multiprocessing", "asyncio", "importlib", "runpy", "requests", "vieneu", "hyperframes",
                         "huggingface_hub", "onnxruntime", "numpy", "soundfile", "librosa", "gradio", "pip", "threading"}

    def test_static_imports_and_write_modes(self):
        tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported |= {a.name.split(".")[0] for a in node.names}
            elif isinstance(node, ast.ImportFrom):
                imported.add((node.module or "").split(".")[0])
        self.assertFalse(imported & self.FORBIDDEN_IMPORTS, imported & self.FORBIDDEN_IMPORTS)
        modes = [ast.literal_eval(c.args[1]) for c in ast.walk(tree)
                 if isinstance(c, ast.Call) and getattr(c.func, "id", "") == "open" and len(c.args) > 1]
        self.assertEqual(sorted(modes), ["rb", "rb", "x"])
        names = {n.attr for n in ast.walk(tree) if isinstance(n, ast.Attribute)}
        self.assertFalse(names & {"system", "popen", "spawnl", "execv", "environ", "putenv", "remove", "unlink", "rmdir", "mkdir"})

    def test_runtime_effect_entry_points_are_never_called(self):
        trap = mock.Mock(side_effect=AssertionError("forbidden effect invoked"))
        before = set(sys.modules)
        snapshot = sorted(str(p.relative_to(self.fx.root)) for p in self.fx.root.rglob("*"))
        env_before = dict(os.environ)
        with contextlib.ExitStack() as stack:
            for target in (subprocess, "Popen"), (subprocess, "run"), (os, "system"), (os, "popen"), (socket, "socket"), \
                    (socket, "create_connection"), (socket, "getaddrinfo"), (urllib.request, "urlopen"), (os, "putenv"):
                stack.enter_context(mock.patch.object(target[0], target[1], trap))
            for mutate in (None, lambda m: m.pop("ceilings"), lambda m: m["artifacts"].pop()):
                self.run_pf(mutate)
        trap.assert_not_called()
        self.assertEqual(snapshot, sorted(str(p.relative_to(self.fx.root)) for p in self.fx.root.rglob("*")))
        self.assertEqual(dict(os.environ), env_before)
        banned = {"vieneu", "onnxruntime", "huggingface_hub", "soundfile", "librosa", "gradio", "puppeteer"}
        self.assertFalse({m.split(".")[0] for m in set(sys.modules) - before} & banned)



class ReviewerMalformedInputControls(Base):
    def test_malformed_nested_values_return_structured_no_go(self):
        mutations = [
            lambda m: m["artifacts"][0].update(category=[]),
            lambda m: m["artifacts"][0]["origin"].update(kind={}),
            lambda m: m["voice"].update(presetArtifactId=[]),
            lambda m: m["sourcePins"][0].update(component=[]),
            lambda m: m["enforcement"]["egress_block"].update(evidenceArtifactId=[]),
            lambda m: m["artifacts"][2]["rights"].update(evidenceArtifactId=[]),
        ]
        for mutate in mutations:
            with self.subTest(mutation=mutations.index(mutate)):
                report = self.run_pf(mutate)
                self.assertEqual(report["validationStatus"], "INVALID_NO_GO")
                self.assertEqual(report["runtimeAdmission"], "NO_GO")
                expected = "ORIGIN_NOT_IMMUTABLE" if mutations.index(mutate) == 1 else "MANIFEST_SHAPE_INVALID"
                self.assertIn(expected, report["reasonCodes"])

    def test_oversized_numbers_do_not_escape_no_go(self):
        self.assertCode(self.run_pf(lambda m: m["ceilings"]["process_count"].update(value=10 ** 400)),
                        "CEILING_INVALID", "INVALID")
        self.assertCode(self.run_pf(lambda m: m["s05"].update(measuredNarrationSeconds=10 ** 400)),
                        "S05_MEASUREMENT_INVALID", "INVALID")


if __name__ == "__main__":
    unittest.main()
