"""Generate the standalone HTML report from summary.json."""
import json
import statistics
from html import escape
from pathlib import Path

from charts import heatmap, scatter_logx, grouped_bars

HERE = Path(__file__).parent
S = json.load(open(HERE / "summary.json"))
T = S["tasks"]
DEC, LLM = S["models"]["decision"], S["models"]["llm"]
OUT = HERE.parent / "decision-models-2026-10-10.html"

NAME = {
    "openai/gpt-6-luna-decisions": "GPT-6 Luna Decisions", "upstage/solar-decide": "Solar Decide",
    "upstage/solar-decide-flash": "Solar Decide Flash", "cloudflare/clef": "Clef (27B)",
    "cloudflare/clef-omni": "Clef Omni", "cloudflare/clef-flash": "Clef Flash",
    "perplexity/pplx-decider-v1.1-27b": "Perplexity Decider 1.1", "liquid/d1": "Liquid d1",
    "inception/mercury-decide": "Mercury Decide", "microsoft/microsoft-decision-1": "Microsoft-Decision-1",
    "nace-ai/drex-v1.5": "Nace Drex 1.5", "typesafe/jev-1.13": "TypeSafe Jev 1.13", "jaredpalmer/kev-4b": "Kev 4B",
    "togethercomputer/tev1-4b-experimental": "Together Tev1 4B", "respan/span-01": "Respan Span-01",
    "respan/span-01-lite": "Respan Span-01 Lite",
    "google/gemini-2.5-flash": "Gemini 2.5 Flash", "openai/gpt-6-luna": "GPT-6 Luna",
    "anthropic/claude-haiku-5.5": "Claude Haiku 5.5", "openai/gpt-6.1-sol": "GPT-6.1 Sol",
}
PRICE = {  # USD per million input tokens (output free for decision models), OpenRouter 2026-10-10
    "microsoft/microsoft-decision-1": 0.042, "nace-ai/drex-v1.5": 0.04, "cloudflare/clef-omni": 0.15,
    "upstage/solar-decide-flash": 0.05, "perplexity/pplx-decider-v1.1-27b": 0.02, "openai/gpt-6-luna-decisions": 0.10,
    "liquid/d1": 0.04, "cloudflare/clef-flash": 0.038, "cloudflare/clef": 0.24, "togethercomputer/tev1-4b-experimental": 0.042,
    "inception/mercury-decide": 0.02, "upstage/solar-decide": 0.05, "respan/span-01": 0.02, "respan/span-01-lite": 0.0,
    "jaredpalmer/kev-4b": 0.042, "typesafe/jev-1.13": 0.042,
}
TASKS = [("furigana", "Furigana reading"), ("links", "Inline-link sense"), ("conjugation", "Conjugated form"),
         ("translation", "Translation fidelity"), ("sense", "Sense of example"), ("transitivity", "Transitivity"),
         ("flags", "Flag triage")]
TL = dict(TASKS)


def acc(m, t):
    s = T[t].get(m)
    return s["acc"] if s else None


def pct(v, d=0):
    return "—" if v is None else f"{v * 100:.{d}f}%"


def usd(v):
    if v >= 100:
        return f"${v:,.0f}"
    if v >= 1:
        return f"${v:.2f}".rstrip("0").rstrip(".") if v < 10 else f"${v:.1f}"
    return f"${v:.2f}"


# ------------------------------------------------------------------ heat map
rows = DEC + LLM
heat = heatmap(
    rows, [TL[t] for t, _ in TASKS],
    lambda r, c: (None if acc(r, [k for k, v in TASKS if v == c][0]) is None else 100 * acc(r, [k for k, v in TASKS if v == c][0])),
    50, 100, lambda r: NAME[r], groups={DEC[0]: "DECISION MODELS", LLM[0]: "LLMs FOR COMPARISON (batched, 20 items per call)"},
    tip=lambda r, c: f"{NAME[r]} · {c}: {pct(acc(r, [k for k, v in TASKS if v == c][0]), 1)} correct")

# ------------------------------------------------------------------ scatter: cost vs accuracy, 4 shared tasks
CORE = ["furigana", "links", "conjugation", "translation"]
pts = []
for m in DEC + LLM:
    if m == "respan/span-01-lite":
        continue
    if not all(m in T[t] for t in CORE):
        continue
    a = statistics.mean(T[t][m]["acc"] for t in CORE)
    c = statistics.mean(T[t][m]["cost_per_1k"] for t in CORE)
    cls = "llm" if m in LLM else "dec"
    show = m in LLM or m in ("openai/gpt-6-luna-decisions", "microsoft/microsoft-decision-1", "perplexity/pplx-decider-v1.1-27b",
                             "typesafe/jev-1.13", "inception/mercury-decide", "cloudflare/clef", "upstage/solar-decide-flash")
    p = {"x": max(c, 0.002), "y": a, "cls": cls, "label": NAME[m], "show": show,
         "tip": f"{NAME[m]}: {a * 100:.1f}% mean accuracy, ${c:.3f} per 1,000 items"}
    pts.append(p)
for p in pts:
    if p["label"] in ("GPT-6.1 Sol", "Clef (27B)", "Mercury Decide", "Perplexity Decider 1.1"):
        p["anchor"] = "end"
    if p["label"] == "TypeSafe Jev 1.13":
        p["dy"] = -10
        p["anchor"] = "end"
    if p["label"] == "Microsoft-Decision-1":
        p["dy"] = 16
    if p["label"] == "Perplexity Decider 1.1":
        p["dy"] = 12
    if p["label"] == "Mercury Decide":
        p["dy"] = -2
    if p["label"] == "Claude Haiku 5.5":
        p["dy"] = -8
    if p["label"] == "GPT-6 Luna":
        p["dy"] = 14
scatter = scatter_logx(pts, "Cost per 1,000 items checked (USD, log scale)", "Mean accuracy on four tasks", 0.001, 1.0, 0.6, 1.0)

# ------------------------------------------------------------------ furigana by error type
FSUB = [("correct", "Correct\nreadings"), ("voicing", "Voicing\n(rendaku)"), ("long-vowel", "Long\nvowel"),
        ("youon", "Small\nゃゅょ"), ("counter", "Counter\nreadings"), ("homograph", "Homograph\n(wrong word)")]
FSER = [("openai/gpt-6-luna-decisions", "GPT-6 Luna Decisions", "s1"), ("microsoft/microsoft-decision-1", "Microsoft-Decision-1", "s3"),
        ("google/gemini-2.5-flash", "Gemini 2.5 Flash (current)", "s2"), ("anthropic/claude-haiku-5.5", "Claude Haiku 5.5", "s4")]


def fsub(k, m):
    b = T["furigana"][m]["by_sub"]
    if k == "youon":
        # small kana: pool youon and sokuon-drop by item count is not stored; use youon (8 items) only
        return b.get("youon")
    return b.get(k)


fur_chart = grouped_bars(FSUB, FSER, fsub, ylab="Share judged correctly")

LSUB = [("keep", "Correct links\n(should keep)"), ("unlink", "Wrong links\n(should unlink)"), ("retarget", "Wrong target\n(retarget)")]
link_chart = grouped_bars(LSUB, FSER, lambda k, m: T["links"][m]["by_sub"].get(k), w=720, h=260, ylab="Share judged correctly")

# ------------------------------------------------------------------ screening table
scr_rows = []
for m in DEC:
    s = S["screen"][m]
    scr_rows.append(
        f"<tr><td>{escape(NAME[m])}<div class='mid'>{escape(m)}</div></td>"
        f"<td class='num'>${PRICE[m]:.3f}</td>"
        f"<td class='num'>{pct(s.get('translation'))}</td><td class='num'>{pct(s.get('meaning'))}</td>"
        f"<td class='num'>{pct(s.get('reading'))}</td><td class='num'>{pct(s.get('control'))}</td>"
        f"<td class='num'>{s['lat_med']:.2f} s</td></tr>")

# ------------------------------------------------------------------ sweep cost table
VOL = [("furigana", "Every furigana group", 839843), ("links", "Kana links in verify/block tiers", 10508),
       ("conjugation", "Every conjugated form", 242527), ("translation", "Every example translation", 122570),
       ("sense", "Examples in multi-sense entries", 39480)]


def best_dec(t):
    return max([m for m in DEC if m in T[t]], key=lambda m: T[t][m]["acc"])


sweep_rows = []
for t, what, n in VOL:
    bd = best_dec(t)
    cells = [f"<td>{escape(TL[t])}<div class='mid'>{escape(what)}: {n:,}</div></td>",
             f"<td class='num'>{usd(n / 1000 * T[t][bd]['cost_per_1k'])}<div class='mid'>{escape(NAME[bd])} · {pct(T[t][bd]['acc'])}</div></td>"]
    for m in LLM:
        cells.append(f"<td class='num'>{usd(n / 1000 * T[t][m]['cost_per_1k'])}<div class='mid'>{pct(T[t][m]['acc'])}</div></td>")
    sweep_rows.append("<tr>" + "".join(cells) + "</tr>")

# ------------------------------------------------------------------ cascade table
casc_rows = []
for t, _ in TASKS:
    if t == "flags":
        continue
    c = T[t]["_cascade"]
    bd = c["dec"]
    h = c["anthropic/claude-haiku-5.5"]
    so = c["openai/gpt-6.1-sol"]
    casc_rows.append(
        f"<tr><td>{escape(TL[t])}</td><td>{escape(NAME[bd])}</td><td class='num'>{pct(1 - so['escalated'])}</td>"
        f"<td class='num'>{pct(h['acc'], 1)}<div class='mid'>{usd(h['cost_per_1k'])}/1k</div></td>"
        f"<td class='num'>{pct(T[t]['anthropic/claude-haiku-5.5']['acc'], 1)}<div class='mid'>{usd(T[t]['anthropic/claude-haiku-5.5']['cost_per_1k'])}/1k</div></td>"
        f"<td class='num'>{pct(so['acc'], 1)}<div class='mid'>{usd(so['cost_per_1k'])}/1k</div></td>"
        f"<td class='num'>{pct(T[t]['openai/gpt-6.1-sol']['acc'], 1)}<div class='mid'>{usd(T[t]['openai/gpt-6.1-sol']['cost_per_1k'])}/1k</div></td></tr>")

# ------------------------------------------------------------------ latency
dec_lat = sorted(statistics.median(T[t][m]["lat_med"] for t, _ in TASKS if T[t].get(m)) for m in DEC)
llm_lat = sorted(statistics.median(T[t][m]["batch_lat_med"] for t, _ in TASKS) for m in LLM)

disputed = json.load(open(HERE / "trans_disputed.json"))
n_items = {t: T[t]["openai/gpt-6.1-sol"]["n"] for t, _ in TASKS}

ctx = dict(heat=heat, scatter=scatter, fur_chart=fur_chart, link_chart=link_chart, scr_rows="\n".join(scr_rows),
           sweep_rows="\n".join(sweep_rows), casc_rows="\n".join(casc_rows),
           dec_lat_lo=f"{dec_lat[0]:.1f}", dec_lat_hi=f"{dec_lat[-1]:.1f}",
           llm_lat_lo=f"{llm_lat[0]:.0f}", llm_lat_hi=f"{llm_lat[-1]:.0f}",
           disputed=", ".join(f"{d['headword']} (tagged {d['gold']})" for d in disputed), n=n_items,
           total_items=f"{sum(n_items.values()):,}")
tpl = (HERE / "report_template.html").read_text()
html = tpl
for k, v in ctx.items():
    html = html.replace("{{" + k + "}}", str(v))
for t, v in n_items.items():
    html = html.replace("{{n." + t + "}}", str(v))


def fill_acc(html):
    import re

    def rep(m):
        model, task = m.group(1), m.group(2)
        key = [k for k in NAME if NAME[k] == model or k == model][0]
        return pct(T[task][key]["acc"], 1 if m.group(3) else 0)
    return re.sub(r"\{\{acc:([^|}]+)\|([a-z]+)(\|1)?\}\}", rep, html)


def fill_cost(html):
    import re

    def rep(m):
        key = [k for k in NAME if NAME[k] == m.group(1) or k == m.group(1)][0]
        return f"${T[m.group(2)][key]['cost_per_1k']:.3f}"
    return re.sub(r"\{\{cost:([^|}]+)\|([a-z]+)\}\}", rep, html)


html = fill_cost(fill_acc(html))
assert "{{" not in html, html[html.index("{{"):html.index("{{") + 80]
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(html)
print("wrote", OUT, len(html))
