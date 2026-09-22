"""Recover real pre-fix versions for 'apply' decisions (gloss / translation / notes) from git history."""
import json, subprocess, glob, sys, re, collections, datetime as dt
from pathlib import Path
S = Path(__file__).parent
LINK = re.compile(r"⟦([^⟧]*?)→[^⟧]*⟧"); FURI = re.compile(r"\{([^|{}]+)\|([^}]+)\}")
def plain(t): return LINK.sub(r"\1", t or "")
def nofuri(t): return FURI.sub(r"\1", plain(t))
rows = []
for line in open("reviews/decisions.jsonl", encoding="utf-8"):
    line = line.strip()
    if not line: continue
    try: d = json.loads(line)
    except Exception: continue
    if d.get("decision") == "apply" and d.get("entry") and d.get("dim") in ("gloss", "translation", "notes"):
        rows.append(d)
print("candidates", len(rows), file=sys.stderr)
def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True).stdout
out = []; stats = collections.Counter()
for d in rows:
    num = str(d["entry"])[:5]
    files = glob.glob(f"entries/*/{num}_*.json")
    if not files: stats["nofile"] += 1; continue
    f = files[0]
    ts = d["ts"]
    until = (dt.datetime.fromisoformat(ts.replace("Z", "+00:00")) + dt.timedelta(days=4)).isoformat()
    log = git("log", "--format=%H", "--since", ts, "--until", until, "--reverse", "--", f).split()
    if not log: stats["nocommit"] += 1; continue
    c = log[0]
    before = git("show", f"{c}^:{f}"); after = git("show", f"{c}:{f}")
    try:
        b = json.loads(before); a = json.loads(after)
    except Exception:
        stats["badjson"] += 1; continue
    rec = {"entry": a.get("id"), "dim": d["dim"], "note": d.get("note"), "ts": ts, "commit": c,
           "headword": nofuri(a.get("headword")), "reading": a.get("reading"), "pos": a.get("part_of_speech")}
    if d["dim"] == "translation":
        bex = {plain(x.get("japanese")): x.get("english") for x in b.get("examples") or []}
        aex = {plain(x.get("japanese")): x.get("english") for x in a.get("examples") or []}
        changed = [(j, bex[j], aex[j]) for j in bex if j in aex and bex[j] != aex[j] and bex[j] and aex[j]]
        if len(changed) != 1: stats[f"tr-changed-{min(len(changed),2)}"] += 1; continue
        j, we, fe = changed[0]
        rec.update({"japanese": j, "wrong_english": we, "fixed_english": fe, "gloss": a.get("gloss")})
        stats["translation"] += 1
    elif d["dim"] == "gloss":
        bg, ag = b.get("gloss"), a.get("gloss")
        bd = [x.get("gloss") for x in b.get("definitions") or []]; ad = [x.get("gloss") for x in a.get("definitions") or []]
        if bg != ag and bg and ag:
            rec.update({"wrong_gloss": bg, "fixed_gloss": ag, "level": "gloss"})
        elif len(bd) == len(ad) and sum(1 for x, y in zip(bd, ad) if x != y) == 1:
            i = [k for k, (x, y) in enumerate(zip(bd, ad)) if x != y][0]
            rec.update({"wrong_gloss": bd[i], "fixed_gloss": ad[i], "level": f"definitions[{i}]"})
        else:
            stats["gloss-nochange"] += 1; continue
        rec["examples"] = [{"japanese": plain(x.get("japanese")), "english": x.get("english")} for x in (a.get("examples") or [])[:3]]
        rec["explanation"] = (a.get("definitions") or [{}])[0].get("explanation")
        stats["gloss"] += 1
    else:  # notes
        bn, an = b.get("notes") or "", a.get("notes") or ""
        if bn == an or not bn or not an: stats["notes-nochange"] += 1; continue
        # keep only when the change is local: same paragraph count and <= 2 paragraphs changed
        bp, ap = bn.split("\n"), an.split("\n")
        if len(bp) != len(ap): stats["notes-restructured"] += 1; continue
        diff = [(x, y) for x, y in zip(bp, ap) if x != y]
        if len(diff) > 2: stats["notes-restructured"] += 1; continue
        rec.update({"wrong_notes": nofuri(bn), "fixed_notes": nofuri(an),
                    "wrong_lines": [nofuri(x) for x, _ in diff], "fixed_lines": [nofuri(y) for _, y in diff],
                    "gloss": a.get("gloss")})
        stats["notes"] += 1
    out.append(rec)
print(dict(stats), file=sys.stderr)
json.dump(out, open(S / "error_set.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
for r in out[:3]: print(json.dumps(r, ensure_ascii=False)[:400])
