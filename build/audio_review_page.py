"""A self-contained HTML page for listening to example recordings and rating them.

Used for the voice pilot and for Tom's periodic spot checks (AUDIO_WORKFLOW.md §5, §10).
The page needs no server: open it straight from the audio repository's GitHub
Pages site, or as a single file with the clips embedded (embed=True). Ratings
(✓ correct / ✗ wrong / ? unsure, plus an optional comment) are kept in the
browser's localStorage and exported as JSON with the Download button, in the
format `build/audio_maintenance.py import-ratings` reads:

    {"page": "<page id>", "exported": "<ISO time>",
     "ratings": {"<clip key>": {"r": "ok|err|unsure", "c": "comment"}}}
"""
import base64
import html
import json

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
:root {{ --bg:#fafafa; --fg:#1a1a1a; --muted:#666; --card:#fff; --border:#ddd;
        --ok:#15803d; --err:#b91c1c; --unsure:#a16207; --accent:#2563eb; }}
@media (prefers-color-scheme: dark) {{
  :root {{ --bg:#111; --fg:#eee; --muted:#aaa; --card:#1c1c1c; --border:#333;
          --ok:#4ade80; --err:#f87171; --unsure:#facc15; --accent:#60a5fa; }} }}
body {{ margin:0; background:var(--bg); color:var(--fg);
       font:16px/1.5 system-ui,-apple-system,"Segoe UI","Hiragino Sans","Noto Sans JP",sans-serif; }}
main {{ max-width:860px; margin:0 auto; padding:16px; }}
h1 {{ font-size:1.4rem; margin:0.5rem 0; }} h2 {{ font-size:1.15rem; margin:1.6rem 0 0.4rem; }}
.intro {{ color:var(--muted); }} .intro p {{ margin:0.4rem 0; }}
.bar {{ position:sticky; top:0; background:var(--bg); padding:8px 0; border-bottom:1px solid var(--border);
       display:flex; gap:8px; flex-wrap:wrap; align-items:center; z-index:1; }}
.bar button {{ font:inherit; padding:4px 10px; border:1px solid var(--border); border-radius:6px;
              background:var(--card); color:var(--fg); cursor:pointer; }}
.count {{ color:var(--muted); font-size:0.9rem; }}
.clip {{ background:var(--card); border:1px solid var(--border); border-radius:8px; padding:10px 12px; margin:8px 0; }}
.clip .ja {{ font-size:1.15rem; }} .clip .rd {{ color:var(--muted); font-size:0.9rem; }}
.clip .en {{ font-size:0.9rem; }} .clip .meta {{ color:var(--muted); font-size:0.8rem; }}
.clip audio {{ width:100%; max-width:420px; height:36px; margin:6px 0; }}
.rate {{ display:flex; gap:6px; flex-wrap:wrap; align-items:center; }}
.rate button {{ font:inherit; min-width:44px; padding:2px 10px; border:1px solid var(--border);
               border-radius:6px; background:var(--card); color:var(--fg); cursor:pointer; }}
.rate button.on[data-r=ok] {{ border-color:var(--ok); color:var(--ok); font-weight:600; }}
.rate button.on[data-r=err] {{ border-color:var(--err); color:var(--err); font-weight:600; }}
.rate button.on[data-r=unsure] {{ border-color:var(--unsure); color:var(--unsure); font-weight:600; }}
.rate input {{ flex:1; min-width:140px; font:inherit; font-size:0.9rem; padding:2px 6px;
              border:1px solid var(--border); border-radius:6px; background:var(--card); color:var(--fg); }}
</style>
</head>
<body>
<main>
<h1>{title}</h1>
<div class="intro">{intro}</div>
<div class="bar">
  <button id="dl" type="button">Download ratings (JSON)</button>
  <button id="cp" type="button">Copy ratings</button>
  <span class="count" id="count"></span>
</div>
{sections}
</main>
<script>
(function() {{
  var PAGE = {page_id};
  var KEY = 'audio-ratings:' + PAGE;
  var ratings = {{}};
  try {{ ratings = JSON.parse(localStorage.getItem(KEY) || '{{}}'); }} catch (e) {{ ratings = {{}}; }}
  function save() {{ try {{ localStorage.setItem(KEY, JSON.stringify(ratings)); }} catch (e) {{}} count(); }}
  function count() {{
    var n = document.querySelectorAll('.clip').length, done = 0;
    for (var k in ratings) if (ratings[k].r) done++;
    document.getElementById('count').textContent = done + ' of ' + n + ' rated';
  }}
  function paint(clip) {{
    var r = ratings[clip.dataset.key] || {{}};
    clip.querySelectorAll('.rate button').forEach(function(b) {{ b.classList.toggle('on', b.dataset.r === r.r); }});
    var inp = clip.querySelector('.rate input'); if (inp) inp.value = r.c || '';
  }}
  document.querySelectorAll('.clip').forEach(function(clip) {{
    paint(clip);
    clip.querySelectorAll('.rate button').forEach(function(b) {{
      b.addEventListener('click', function() {{
        var k = clip.dataset.key, cur = ratings[k] || {{}};
        cur.r = (cur.r === b.dataset.r) ? '' : b.dataset.r; ratings[k] = cur; paint(clip); save();
      }});
    }});
    var inp = clip.querySelector('.rate input');
    if (inp) inp.addEventListener('input', function() {{
      var k = clip.dataset.key, cur = ratings[k] || {{}}; cur.c = inp.value; ratings[k] = cur; save();
    }});
    var au = clip.querySelector('audio');
    if (au) au.addEventListener('play', function() {{
      document.querySelectorAll('audio').forEach(function(o) {{ if (o !== au) o.pause(); }});
    }});
  }});
  function payload() {{
    return JSON.stringify({{page: PAGE, exported: new Date().toISOString(), ratings: ratings}}, null, 1);
  }}
  document.getElementById('dl').addEventListener('click', function() {{
    var a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([payload()], {{type: 'application/json'}}));
    a.download = 'ratings_' + PAGE + '.json'; document.body.appendChild(a); a.click(); a.remove();
  }});
  document.getElementById('cp').addEventListener('click', function() {{
    var t = payload();
    if (navigator.clipboard) navigator.clipboard.writeText(t).then(function() {{ alert('Copied.'); }});
    else prompt('Copy this:', t);
  }});
  count();
}})();
</script>
</body>
</html>
"""

CLIP = """<div class="clip" data-key="{key}">
  <div class="ja" lang="ja">{text}</div>
  <div class="rd" lang="ja">{reading}</div>
  {english}
  <audio controls preload="none" src="{src}"></audio>
  <div class="meta">{meta}</div>
  {rate}
</div>"""

RATE = """<div class="rate"><button type="button" data-r="ok" title="Correct">✓</button>
  <button type="button" data-r="err" title="Wrong">✗</button>
  <button type="button" data-r="unsure" title="Unsure">?</button>
  <input type="text" placeholder="comment (optional)" aria-label="comment"></div>"""


def data_uri(mp3_bytes):
    return "data:audio/mpeg;base64," + base64.b64encode(mp3_bytes).decode()


def make_page(page_id, title, intro_html, sections, rating=True):
    """sections: [(heading or None, [clip dict])]; clip keys: key, text, reading,
    english (optional), src (URL or data URI), meta (optional)."""
    parts = []
    for heading, clips in sections:
        if heading:
            parts.append(f"<h2>{html.escape(heading)}</h2>")
        for c in clips:
            parts.append(CLIP.format(
                key=html.escape(c["key"]), text=html.escape(c["text"]),
                reading=html.escape(c.get("reading", "")),
                english=(f'<div class="en">{html.escape(c["english"])}</div>' if c.get("english") else ""),
                src=html.escape(c["src"]), meta=html.escape(c.get("meta", "")),
                rate=RATE if rating else ""))
    return PAGE.format(title=html.escape(title), intro=intro_html, sections="\n".join(parts),
                       page_id=json.dumps(page_id))
