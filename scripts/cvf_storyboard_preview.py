#!/usr/bin/env python3
"""Deterministic builder: digest-pinned CVF storyboard design -> offline HTML preview (stdlib only).
All validation runs before the output is replaced; prototype cards are cross-checked against the design.
Text Encoding Exception: Vietnamese UI text keeps its diacritics."""
import argparse, hashlib, html, json, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D_SRC = "docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md"
D_CLAIMS = "docs/reviews/evidence/cvf-ncr-general-video-design-2026-10-02.json"
D_PROTO = "docs/reviews/evidence/cvf-offline-preview-prototype-2026-10-09.html"
D_MANIFEST = "docs/reviews/evidence/cvf-offline-preview-dispatch-inputs-2026-10-09.json"
D_OUT = "docs/reviews/evidence/cvf-storyboard-preview-2026-10-09.html"
FIELDS = ["Narration", "On-screen", "Visual intent", "Asset needs", "Claims"]
MARK = "VÍ DỤ MINH HỌA"
BADGE = MARK + " - CHƯA CHẠY THẬT - DỮ LIỆU GIẢ"
HEAD_RE = re.compile(r"^### (S\d{2}) \| (\d+)-(\d+) \| (\d+) s$")
FIELD_RE = re.compile(r"^- ([A-Za-z-]+(?: [a-z]+)?): (.+)$")
PROTO_RE = re.compile(r"^const scenes=(\[.*\]);$", re.M)


class BuildError(Exception):
    """Fail-closed input or output error."""


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def rel(root, path):
    p = Path(path)
    p = p if p.is_absolute() else root / p
    try:
        return p.resolve().relative_to(root.resolve()).as_posix(), p
    except ValueError:
        raise BuildError("input outside root: %s" % path)


def read_pinned(root, pins, path):
    key, p = rel(root, path)
    if key not in pins:
        raise BuildError("unpinned input: %s" % key)
    try:
        data = p.read_bytes()
    except OSError as exc:
        raise BuildError("unreadable input %s: %s" % (key, exc))
    if sha256(data) != pins[key]:
        raise BuildError("source digest drift: %s" % key)
    return key, data


def load_pins(root, manifest):
    try:
        mp = Path(manifest)
        doc = json.loads((mp if mp.is_absolute() else root / mp).read_text(encoding="utf-8"))
        return {s["path"]: s["rawSha256"] for s in doc["sources"]}
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise BuildError("invalid input manifest: %s" % exc)


def parse_design(text):
    lines = text.replace("\r\n", "\n").split("\n")
    try:
        start = lines.index("## Scene Handoff")
    except ValueError:
        raise BuildError("missing Scene Handoff section")
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    scenes, cur = [], None
    for line in lines[start + 1:end]:
        m = HEAD_RE.match(line)
        if m:
            cur = {"id": m[1], "start": int(m[2]), "end": int(m[3]), "dur": int(m[4]), "fields": []}
            scenes.append(cur)
        elif line.startswith("### "):
            raise BuildError("malformed scene heading: %s" % line[:40])
        elif line.startswith("- ") and cur is not None:
            m = FIELD_RE.match(line)
            if not m:
                raise BuildError("malformed field line in %s" % cur["id"])
            cur["fields"].append((m[1], m[2]))
    return scenes


def check_scenes(scenes, claim_ids, illustrated):
    if [s["id"] for s in scenes] != ["S%02d" % i for i in range(1, 11)]:
        raise BuildError("scenes must be exactly S01-S10 in order")
    clock = 0
    for s in scenes:
        if [k for k, _ in s["fields"]] != FIELDS:
            raise BuildError("%s must carry exactly the five fields in order" % s["id"])
        s.update({k: v for k, v in s["fields"]})
        if s["start"] != clock or s["end"] <= s["start"] or s["dur"] != s["end"] - s["start"]:
            raise BuildError("%s schedule gap, overlap or bad duration" % s["id"])
        clock = s["end"]
        s["claims"] = [c.strip() for c in s["Claims"].split(",")]
        bad = [c for c in s["claims"] if c not in claim_ids]
        if bad:
            raise BuildError("%s undeclared claim ids: %s" % (s["id"], ",".join(bad)))
        s["illustrative"] = MARK in s["On-screen"]
    if clock != 240:
        raise BuildError("schedule must end at 240 seconds")
    if {s["id"] for s in scenes if s["illustrative"]} != set(illustrated):
        raise BuildError("illustration scenes disagree with declared set")


def load_cards(proto_html, scenes):
    m = PROTO_RE.search(proto_html)
    try:
        cards = {c["id"]: c for c in json.loads(m[1])}
    except (TypeError, ValueError, KeyError):
        raise BuildError("prototype scene data unreadable")
    for s in scenes:
        c = cards.get(s["id"])
        keys = ("start", "end", "narration", "sourceScreen", "claims", "illustrative")
        if not c or [c.get(k) for k in keys] != [s["start"], s["end"], s["Narration"], s["On-screen"], s["claims"], s["illustrative"]]:
            raise BuildError("prototype drift against design in %s" % s["id"])
        if not isinstance(c.get("title"), str) or not c["cards"] or not all(isinstance(x, str) for x in c["cards"]):
            raise BuildError("prototype presentation summary invalid in %s" % s["id"])
        s["title"], s["cards"] = c["title"], c["cards"]


def mmss(t):
    return "%02d:%02d" % divmod(t, 60)


def render_scene(s):
    e = html.escape
    badge = '<div class="badge" role="note">%s</div>' % e(BADGE) if s["illustrative"] else ""
    cards = "".join('<li class="card">%s</li>' % e(c) for c in s["cards"])
    return (
        '<div class="scene" id="scene-{id}" data-scene="{id}" data-start="{st}" data-end="{en}" data-illustrative="{il}">'
        '<section class="stage" aria-label="Cảnh {id}: {title}"><div class="eyebrow"><span>{id} · {a}–{b}</span><span>CVF / 16:9</span></div>'
        '<h2>{title}</h2>{badge}<ul class="cards" aria-label="Tóm tắt trình chiếu">{cards}</ul>'
        '<footer>Nguồn tài liệu · <span class="claims">{claims}</span> · Tóm tắt trình chiếu, không phải chữ gốc</footer></section>'
        '<section class="notes" aria-label="Lời dẫn và chữ gốc {id}"><h3>Lời dẫn gốc · chưa có giọng đọc</h3><p class="narration">{nar}</p>'
        '<h3>Chữ trên màn hình trong thiết kế gốc</h3><p class="onscreen">{scr}</p>'
        '<details><summary>Ý đồ hình ảnh và tài nguyên (chưa tạo)</summary><p class="visual">{vis}</p><p class="assets">{ast}</p></details></section></div>'
    ).format(id=s["id"], st=s["start"], en=s["end"], il=str(s["illustrative"]).lower(), title=e(s["title"]), a=mmss(s["start"]),
             b=mmss(s["end"]), badge=badge, cards=cards, claims=e(", ".join(s["claims"])), nar=e(s["Narration"]),
             scr=e(s["On-screen"]), vis=e(s["Visual intent"]), ast=e(s["Asset needs"]))


CSS = """:root{color-scheme:dark;font-family:"DM Sans",Inter,system-ui,"Segoe UI",sans-serif;--page:#111218;--surface:#1c1d27;--elev:#242636;--line:#ffffff24;--text:#f4f7fb;--sub:#a3adc2;--accent:#5b5cf6;--warn:#f59e0b;--warn-bg:#302719;--warn-text:#fcd893;--focus:#b9baff}
*{box-sizing:border-box}body{margin:0;background:var(--page);color:var(--text)}main{max-width:1120px;margin:auto;padding:24px;display:flex;flex-direction:column}p{line-height:1.6}
header{display:flex;justify-content:space-between;align-items:center;gap:16px}h1{font-size:25px;line-height:1.15;margin:0 0 6px}header p{color:var(--sub);font-size:13px;margin:0}.tag{color:var(--warn);font-size:11px;font-weight:700;letter-spacing:.06em}
.scene{display:contents}.scene[hidden]{display:none}.stage{order:1;aspect-ratio:16/9;background:var(--surface);border:1px solid var(--line);border-radius:12px;margin-top:22px;padding:30px 38px;display:flex;flex-direction:column;gap:16px;overflow:auto}
.eyebrow{display:flex;justify-content:space-between;color:var(--sub);font-size:12px}.stage h2{font-size:30px;line-height:1.2;margin:0;max-width:850px}.badge{border:1px solid var(--warn);color:var(--warn-text);background:var(--warn-bg);padding:10px 14px;border-radius:7px;font-weight:700;font-size:13px}
.cards{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;flex:1;align-content:center}.card{background:var(--elev);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:7px;padding:15px 18px;font-size:19px;line-height:1.45;overflow-wrap:anywhere}.stage footer{font-size:12px;color:var(--sub);margin-top:auto}
.ctl{order:2}.controls{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:16px 0}button{border:1px solid var(--line);background:var(--elev);color:var(--text);border-radius:8px;min-height:44px;min-width:44px;padding:9px 15px;font:inherit;font-size:13px;cursor:pointer}button.primary,.sc[aria-current=true]{background:var(--accent)}button:hover{border-color:var(--focus)}button:disabled{opacity:.4;cursor:default}
button:focus-visible,input:focus-visible,summary:focus-visible{outline:2px solid var(--focus);outline-offset:3px}.timer{font-variant-numeric:tabular-nums;margin-left:auto;font-size:14px}input[type=range]{width:100%;min-height:44px;accent-color:var(--accent)}label{display:block;font-size:12px;color:var(--sub);margin-bottom:5px}.scenes{display:flex;gap:8px;flex-wrap:wrap;margin:16px 0}
.notes{order:3;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:18px;margin-top:6px}.notes h3{font-size:13px;margin:12px 0 0;color:var(--sub)}.notes h3:first-child{margin-top:0}.notes p{font-size:15px;margin:6px 0 0;overflow-wrap:anywhere}.notes details p{font-size:13px;color:var(--sub)}summary{font-size:13px;cursor:pointer;padding:14px 0}
.meta{order:4;margin-top:18px;font-size:12px;color:var(--sub)}.meta dl{display:grid;grid-template-columns:max-content 1fr;gap:4px 14px}.meta dd{margin:0;overflow-wrap:anywhere}.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}noscript{display:block;padding:12px;color:var(--warn-text)}
@media(max-width:640px){main{padding:16px 10px}header{display:block}.tag{display:block;margin-top:12px}.stage{aspect-ratio:auto;min-height:360px;padding:20px;overflow:visible}.stage h2{font-size:24px}.cards{grid-template-columns:1fr}.card{font-size:16px;padding:12px}.badge{font-size:12px}.timer{margin-left:0}.controls button{flex:1}.meta dl{grid-template-columns:1fr}}"""

JS = """'use strict';
const $=id=>document.getElementById(id),S=[...document.querySelectorAll('.scene')],B=[...document.querySelectorAll('.sc')],END=Number(document.body.dataset.total);
let el=0,playing=false,a0=0,t0=0,tm=0,cur=-1;
const fmt=t=>String(Math.floor(t/60)).padStart(2,'0')+':'+String(Math.floor(t%60)).padStart(2,'0');
const at=t=>{const i=S.findIndex(s=>t<Number(s.dataset.end));return i<0?S.length-1:i;};
function render(){const i=at(el);
 if(i!==cur){cur=i;S.forEach((s,k)=>{s.hidden=k!==i;});B.forEach((b,k)=>b.setAttribute('aria-current',String(k===i)));$('status').textContent=B[i].getAttribute('aria-label');}
 $('timer').textContent=fmt(el)+' / '+fmt(END);$('seek').value=Math.floor(el);$('seek').setAttribute('aria-valuetext',Math.floor(el)+' gi\\u00e2y');
 $('prev').disabled=i===0;$('next').disabled=i===S.length-1;
 $('play').textContent=playing?'T\\u1ea1m d\\u1eebng':(el>=END?'Ph\\u00e1t l\\u1ea1i':'Ph\\u00e1t preview');$('play').setAttribute('aria-pressed',String(playing));}
function sync(){el=Math.min(END,a0+(performance.now()-t0)/1000);}
function pause(){if(playing)sync();playing=false;clearInterval(tm);render();}
function seek(t){pause();el=Math.min(END,Math.max(0,t));render();}
function tick(){sync();if(el>=END){playing=false;clearInterval(tm);}render();}
function toggle(){if(playing){pause();return;}if(el>=END)el=0;a0=el;t0=performance.now();playing=true;clearInterval(tm);tm=setInterval(tick,100);render();}
const start=k=>Number(S[Math.min(S.length-1,Math.max(0,k))].dataset.start);
B.forEach((b,k)=>b.addEventListener('click',()=>seek(start(k))));
$('prev').addEventListener('click',()=>seek(start(cur-1)));$('next').addEventListener('click',()=>seek(start(cur+1)));
$('reset').addEventListener('click',()=>seek(0));$('play').addEventListener('click',toggle);$('seek').addEventListener('input',e=>seek(Number(e.target.value)));
document.addEventListener('keydown',e=>{if(e.target.closest('button,input,summary'))return;
 if(e.key==='ArrowRight'){e.preventDefault();$('next').click();}else if(e.key==='ArrowLeft'){e.preventDefault();$('prev').click();}else if(e.code==='Space'){e.preventDefault();toggle();}});
document.addEventListener('visibilitychange',()=>{if(document.hidden)pause();});
render();"""

PAGE = """<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>CVF · Preview storyboard offline</title>
<style>@@CSS@@</style></head><body data-total="@@TOTAL@@"><main>
<header><div><h1>Preview storyboard CVF</h1><p>10 cảnh · nhịp dự kiến 4 phút (ước tính kế hoạch) · ← → chuyển cảnh, Space phát/dừng</p></div><span class="tag">OFFLINE · UI RIÊNG TƯ</span></header>
<noscript>Tắt JavaScript: mọi cảnh hiện liên tiếp, không có điều khiển timeline.</noscript>
@@SCENES@@
<div class="ctl"><div class="controls"><button type="button" id="prev" aria-label="Cảnh trước">← Trước</button><button type="button" id="play" class="primary" aria-pressed="false">Phát preview</button><button type="button" id="next" aria-label="Cảnh tiếp">Tiếp →</button><button type="button" id="reset">Về đầu</button><span class="timer" id="timer">00:00 / 04:00</span></div>
<label for="seek">Vị trí trên timeline (giây)</label><input id="seek" type="range" min="0" max="@@TOTAL@@" step="1" value="0" aria-valuetext="0 giây">
<nav class="scenes" aria-label="Chọn cảnh">@@NAV@@</nav><p id="status" class="sr" aria-live="polite"></p></div>
<details class="meta"><summary>Nguồn, kiểm chứng và giới hạn</summary>@@META@@</details>
</main><script>@@JS@@</script></body></html>
"""


def render_page(scenes, meta):
    e = html.escape
    nav = "".join('<button type="button" class="sc" aria-label="%s: %s" aria-current="false">%s</button>' % (s["id"], e(s["title"]), s["id"]) for s in scenes)
    dl = "".join("<dt>%s</dt><dd>%s</dd>" % (e(k), e(v)) for k, v in meta)
    parts = {"CSS": CSS, "JS": JS, "TOTAL": str(scenes[-1]["end"]), "SCENES": "".join(render_scene(s) for s in scenes), "NAV": nav,
             "META": "<dl>%s</dl>" % dl}
    return re.sub(r"@@([A-Z]+)@@", lambda m: parts[m[1]], PAGE)


def build(root, manifest, source, claims, prototype, output):
    pins = load_pins(root, manifest)
    k_src, src = read_pinned(root, pins, source)
    k_claims, claim_raw = read_pinned(root, pins, claims)
    k_proto, proto = read_pinned(root, pins, prototype)
    try:
        scenes = parse_design(src.decode("utf-8"))
        cdoc = json.loads(claim_raw.decode("utf-8"))
        check_scenes(scenes, set(cdoc["claims"]), cdoc["illustrationScenes"])
        load_cards(proto.decode("utf-8"), scenes)
    except (UnicodeDecodeError, ValueError, KeyError, TypeError) as exc:
        raise BuildError("invalid input content: %s" % exc)
    meta = [("Nguồn thiết kế", k_src), ("SHA-256 nguồn (byte gốc)", sha256(src)), ("Bản đồ claim", k_claims + " · " + sha256(claim_raw)),
            ("Thẻ tóm tắt", k_proto + " · " + sha256(proto)), ("Builder", "scripts/cvf_storyboard_preview.py"),
            ("Kiểm thử", "Trang không nhúng kết quả kiểm thử; chạy lệnh trong README để kiểm."),
            ("Giới hạn", "UI riêng tư, chỉ ngoại tuyến. Mốc thời gian là ước tính kế hoạch; đồng hồ trình duyệt chỉ mô phỏng timeline, không phải giọng đọc hay video đo được. "
             "Ví dụ chi tiêu chưa chạy thật. Không âm thanh, MP4, provider hay công khai.")]
    data = render_page(scenes, meta).encode("utf-8")
    out = Path(output) if Path(output).is_absolute() else root / output
    tmp = out.with_name(out.name + ".tmp")
    try:
        tmp.write_bytes(data)
        os.replace(tmp, out)
    except OSError as exc:
        raise BuildError("cannot write output: %s" % exc)
    finally:
        tmp.unlink(missing_ok=True)
    return sha256(data)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Build the offline CVF storyboard preview")
    ap.add_argument("--root", default=str(ROOT))
    for name, default in (("manifest", D_MANIFEST), ("source", D_SRC), ("claims", D_CLAIMS), ("prototype", D_PROTO), ("output", D_OUT)):
        ap.add_argument("--" + name, default=default)
    a = ap.parse_args(argv)
    try:
        digest = build(Path(a.root), a.manifest, a.source, a.claims, a.prototype, a.output)
    except BuildError as exc:
        print("BUILD_FAILED: %s" % exc, file=sys.stderr)
        return 2
    print("BUILD_OK output=%s sha256=%s" % (a.output, digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
