#!/usr/bin/env python3
"""Static tests for the storyboard builder (synthetic fixtures only). Text Encoding Exception: Vietnamese test text."""
import contextlib, hashlib, io, json, re, shutil, sys, unittest
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cvf_storyboard_preview as B  # noqa: E402

REPO = B.ROOT
OWNED = REPO / ".cvf" / "runtime" / "cvf-offline-preview-worker-20261009" / "static-tests"
SCHED = [(0, 15), (15, 40), (40, 65), (65, 95), (95, 115), (115, 135), (135, 160), (160, 190), (190, 215), (215, 240)]
ALLOWED_TAGS = {"html", "head", "meta", "title", "style", "body", "main", "header", "div", "h1", "h2", "h3", "p", "span", "section", "ul", "li",
                "footer", "button", "label", "input", "nav", "details", "summary", "dl", "dt", "dd", "noscript", "script"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(argv):
    err = io.StringIO()
    with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
        code = B.main(argv)
    return code, err.getvalue()


def blocks(nar=None, scr=None):
    out = []
    for i, (a, b) in enumerate(SCHED, 1):
        sid = "S%02d" % i
        screen = (scr or {}).get(sid, ("%s " % B.MARK if 5 <= i <= 8 else "") + "screen %s" % sid)
        out.append("### %s | %d-%d | %d s\n- Narration: %s\n- On-screen: %s\n- Visual intent: visual %s\n- Asset needs: assets %s\n- Claims: C0%d, C03\n\n"
                   % (sid, a, b, b - a, (nar or {}).get(sid, "narration %s" % sid), screen, sid, sid, 1 + i % 2))
    return out


def design(bl):
    return "# Design\n\n## Outline\n\nignored\n\n## Scene Handoff\n\nintro\n\n" + "".join(bl) + "## Production-Readiness Checklist\n\n- Narration: ignored\n"


def proto_scenes(bl_text):
    out = []
    for i, (a, b) in enumerate(SCHED, 1):
        sid = "S%02d" % i
        f = dict(re.findall(r"^- ([A-Za-z -]+): (.*)$", re.search(r"### %s .*?\n\n" % sid, bl_text, re.S)[0], re.M))
        out.append({"id": sid, "start": a, "end": b, "title": "title " + sid, "cards": ["card %s a" % sid, "card %s b" % sid], "narration": f["Narration"],
                    "sourceScreen": f["On-screen"], "claims": f["Claims"].split(", "), "illustrative": B.MARK in f["On-screen"]})
    return out


class Fixture:
    counter = 0

    def __init__(self, text=None, claims=None, proto=None, pin_after=None, raw=None):
        Fixture.counter += 1
        self.root = OWNED / ("case%03d" % Fixture.counter)
        (self.root / "in").mkdir(parents=True, exist_ok=True)
        text = text if text is not None else design(blocks())
        try:
            proto = proto or proto_scenes(text)
        except TypeError:  # structurally broken scene set: keep a valid prototype so the design check is what fails
            proto = proto_scenes(design(blocks()))
        files = {"in/design.md": raw if raw is not None else text.encode("utf-8"),
                 "in/claims.json": json.dumps(claims or {"claims": {"C01": {}, "C02": {}, "C03": {}}, "illustrationScenes": ["S05", "S06", "S07", "S08"]}).encode(),
                 "in/proto.html": ("<html>\nconst scenes=%s;\n</html>" % json.dumps(proto)).encode()}
        for k, v in files.items():
            (self.root / k).write_bytes(v)
        pins = {"sources": [{"path": k, "rawSha256": sha(v)} for k, v in files.items()]}
        (self.root / "manifest.json").write_text(json.dumps(pins), encoding="utf-8")
        if pin_after:
            pin_after(self.root)
        self.out = self.root / "out.html"

    def argv(self, **kw):
        a = {"root": str(self.root), "manifest": "manifest.json", "source": "in/design.md", "claims": "in/claims.json", "prototype": "in/proto.html", "output": str(self.out)}
        a.update(kw)
        return sum((["--" + k, v] for k, v in a.items()), [])

    def build(self, **kw):
        return run(self.argv(**kw))


class Page(HTMLParser):
    def __init__(self, data):
        super().__init__(convert_charrefs=True)
        self.tags, self.attrs, self.scripts, self.text, self.scene, self.cls, self.badges, self.in_script = [], [], [], {}, None, None, 0, False
        self.feed(data)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append(tag)
        self.attrs += [k for k, _ in attrs]
        if "data-scene" in a:
            self.scene = a["data-scene"]
        self.cls = a.get("class") if tag == "p" else None
        self.badges += a.get("class") == "badge"
        if tag == "script":
            self.scripts.append("")
            self.in_script = True
        if tag == "li" and self.scene:
            self.cls = "card"

    def handle_data(self, data):
        if self.in_script:
            self.scripts[-1] += data
        elif self.cls and self.scene:
            self.text.setdefault((self.scene, self.cls), "")
            self.text[(self.scene, self.cls)] += data

    def handle_endtag(self, tag):
        self.cls, self.in_script = None, False


class BuilderTests(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        target = OWNED.resolve()
        if target.parent.name == "cvf-offline-preview-worker-20261009" and target.name == "static-tests" and REPO.resolve() in target.parents:
            shutil.rmtree(target)

    def assertRejected(self, fx, fragment, **kw):
        fx.out.write_bytes(b"SENTINEL")
        code, err = fx.build(**kw)
        self.assertEqual(code, 2, err)
        self.assertIn(fragment, err)
        self.assertEqual(fx.out.read_bytes(), b"SENTINEL", "malformed input must not overwrite existing output")

    def test_valid_source_is_exact_and_repeatable(self):
        nar = {"S02": "Xin chào & <b>đầy đủ</b> \"q\""}
        fx = Fixture(design(blocks(nar=nar)))
        self.assertEqual(fx.build()[0], 0)
        first = fx.out.read_bytes()
        self.assertEqual(fx.build()[0], 0)
        self.assertEqual(first, fx.out.read_bytes())
        self.assertFalse(list(fx.root.glob("*.tmp")))
        page = Page(first.decode("utf-8"))
        self.assertEqual(page.text[("S02", "narration")], nar["S02"])
        self.assertEqual([page.text[("S%02d" % i, "onscreen")] for i in range(1, 11)], [re.search(r"### S%02d .*?On-screen: (.*?)\n" % i, design(blocks()), re.S)[1] for i in range(1, 11)])
        self.assertIn(sha((fx.root / "in/design.md").read_bytes()), first.decode("utf-8"))
        self.assertEqual(page.badges, 4)
        self.assertEqual(page.tags.count("button"), 14)

    def test_real_pinned_source_projection_is_deterministic_and_matches_committed_html(self):
        OWNED.mkdir(parents=True, exist_ok=True)
        out = OWNED / "real.html"
        self.assertEqual(run(["--output", str(out)])[0], 0)
        first = out.read_bytes()
        self.assertEqual(run(["--output", str(out)])[0], 0)
        self.assertEqual(first, out.read_bytes())
        committed = REPO / B.D_OUT
        self.assertTrue(committed.exists() and committed.read_bytes() == first, "committed preview must equal a fresh build")
        src = (REPO / B.D_SRC).read_bytes()
        text, page = src.decode("utf-8").replace("\r\n", "\n"), Page(first.decode("utf-8"))
        for i in range(1, 11):
            sid = "S%02d" % i
            sec = re.search(r"### %s \|.*?(?=\n### S|\n## )" % sid, text, re.S)[0]
            self.assertEqual(page.text[(sid, "narration")], re.search(r"^- Narration: (.*)$", sec, re.M)[1])
            self.assertEqual(page.text[(sid, "onscreen")], re.search(r"^- On-screen: (.*)$", sec, re.M)[1])
        self.assertIn(sha(src), first.decode("utf-8"))
        self.assertEqual(page.badges, 4)
        self.assertEqual(len(page.scripts), 1)
        page_text = first.decode("utf-8")
        for token in ("http://", "https://", "href=", "src=", "url(", "@import", "fetch(", "XMLHttpRequest", "localStorage", "sessionStorage", "indexedDB", "document.cookie", "speechSynthesis", "MediaRecorder"):
            self.assertNotIn(token, page_text)
        self.assertIsNone(re.search(r"\b(PASS|FAIL|COMPLETE)\b", page_text), "page must not embed a possibly stale status label")

    def test_unsafe_text_cannot_create_executable_dom(self):
        evil = "</script><script>alert(1)</script><img src=x onerror=alert(1)>&amp; \" ' " + chr(0x2028) + " <!-- "
        bl = blocks(nar={"S01": evil, "S05": evil}, scr={"S05": B.MARK + " <b onclick=x>" + evil, "S01": evil})
        text = design(bl)
        protos = proto_scenes(text)
        protos[0]["title"] = evil
        protos[0]["cards"] = [evil]
        fx = Fixture(text, proto=protos)
        self.assertEqual(fx.build()[0], 0)
        data = fx.out.read_text(encoding="utf-8")
        page = Page(data)
        self.assertLessEqual(set(page.tags), ALLOWED_TAGS)
        self.assertEqual(page.tags.count("script"), 1)
        self.assertEqual(page.scripts[0], B.JS)
        self.assertFalse([a for a in page.attrs if a.startswith("on")])
        self.assertNotIn("<img", data)
        self.assertEqual(page.text[("S01", "narration")], evil)
        self.assertEqual(page.text[("S05", "onscreen")], B.MARK + " <b onclick=x>" + evil)
        self.assertEqual(page.text[("S01", "card")], evil)
        self.assertEqual(data.count("</script>"), 1)

    def test_scene_set_and_order_violations_are_rejected(self):
        bl = blocks()
        cases = {"missing": bl[:4] + bl[5:], "duplicate": bl[:3] + [bl[2]] + bl[3:], "reordered": bl[:1] + [bl[2], bl[1]] + bl[3:], "extra": bl + [bl[0].replace("S01", "S11")]}
        for name, variant in cases.items():
            with self.subTest(name):
                self.assertRejected(Fixture(design(variant)), "exactly S01-S10")

    def test_field_omission_reorder_and_unknown_are_rejected(self):
        text = design(blocks())
        cases = {"omit": text.replace("- Asset needs: assets S04\n", ""), "swap": text.replace("- Narration: narration S03\n- On-screen: screen S03\n", "- On-screen: screen S03\n- Narration: narration S03\n"),
                 "unknown": text.replace("- Claims: C02, C03\n", "- Claims: C02, C03\n- Extra: x\n", 1), "malformed": text.replace("- Visual intent: visual S06", "- visual S06")}
        for name, variant in cases.items():
            with self.subTest(name):
                self.assertRejected(Fixture(variant), "five fields" if name != "malformed" else "malformed field")

    def test_timeline_gap_overlap_duration_and_end_are_rejected(self):
        text = design(blocks())
        cases = {"gap": ("### S03 | 40-65 | 25 s", "### S03 | 41-65 | 24 s", "gap"), "overlap": ("### S03 | 40-65 | 25 s", "### S03 | 39-65 | 26 s", "gap"),
                 "duration": ("### S03 | 40-65 | 25 s", "### S03 | 40-65 | 24 s", "duration"), "zero": ("### S03 | 40-65 | 25 s", "### S03 | 40-40 | 0 s", "duration"),
                 "end": ("### S10 | 215-240 | 25 s", "### S10 | 215-241 | 26 s", "240"), "start": ("### S01 | 0-15 | 15 s", "### S01 | 1-15 | 14 s", "gap")}
        for name, (old, new, frag) in cases.items():
            with self.subTest(name):
                self.assertRejected(Fixture(text.replace(old, new)), frag)

    def test_claim_join_and_illustration_set_are_enforced(self):
        self.assertRejected(Fixture(design(blocks()).replace("C02, C03", "C02, C99", 1)), "undeclared claim ids: C99")
        claims = {"claims": {"C01": {}, "C02": {}, "C03": {}}, "illustrationScenes": ["S05", "S06", "S07"]}
        self.assertRejected(Fixture(claims=claims), "illustration scenes")
        self.assertRejected(Fixture(design(blocks(scr={"S02": B.MARK + " x"}))), "illustration scenes")

    def test_source_drift_unpinned_and_prototype_drift_are_rejected(self):
        self.assertRejected(Fixture(pin_after=lambda r: (r / "in/design.md").write_bytes((r / "in/design.md").read_bytes() + b" ")), "digest drift")
        self.assertRejected(Fixture(pin_after=lambda r: (r / "in/claims.json").write_bytes(b"{}")), "digest drift")
        self.assertRejected(Fixture(pin_after=lambda r: (r / "manifest.json").write_text(json.dumps({"sources": []}))), "unpinned input")
        self.assertRejected(Fixture(pin_after=lambda r: (r / "manifest.json").write_text("not json")), "invalid input manifest")
        self.assertRejected(Fixture(pin_after=lambda r: (r / "in/proto.html").unlink()), "unreadable input")
        text = design(blocks())
        protos = proto_scenes(text)
        protos[3]["narration"] += "!"
        self.assertRejected(Fixture(text, proto=protos), "prototype drift against design in S04")
        protos = proto_scenes(text)
        protos[4]["cards"] = []
        self.assertRejected(Fixture(text, proto=protos), "presentation summary invalid in S05")

    def test_undecodable_missing_section_and_paths_are_rejected(self):
        self.assertRejected(Fixture(raw=b"\xff\xfe## Scene Handoff"), "invalid input content")
        self.assertRejected(Fixture(design(blocks()).replace("## Scene Handoff", "## Other")), "missing Scene Handoff")
        self.assertRejected(Fixture(), "outside root", source="../escape.md")
        fx = Fixture()
        code, err = fx.build(output=str(fx.root / "no-such-dir" / "out.html"))
        self.assertEqual(code, 2)
        self.assertIn("cannot write output", err)

    def test_crlf_source_builds_same_projection_as_lf(self):
        text = design(blocks())
        lf, crlf = Fixture(text), Fixture(raw=text.replace("\n", "\r\n").encode("utf-8"), text=text)
        self.assertEqual((lf.build()[0], crlf.build()[0]), (0, 0))
        self.assertEqual(Page(lf.out.read_text(encoding="utf-8")).text, Page(crlf.out.read_text(encoding="utf-8")).text)


if __name__ == "__main__":
    unittest.main()
