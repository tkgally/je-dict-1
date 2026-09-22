"""Build a labelled furigana test set: correct pairs from real entries + injected wrong readings."""
import json, re, glob, random, collections, sys
from pathlib import Path
S = Path(__file__).parent
random.seed(20260922)
FURI = re.compile(r"\{([^|{}]+)\|([^}]+)\}")
LINK = re.compile(r"⟦([^⟧]*?)→[^⟧]*⟧")
HIRA = re.compile(r"[ぁ-ゖ]")
def plain(t): return LINK.sub(r"\1", t or "")
inv = json.load(open(S / "pair_inventory.json", encoding="utf-8"))

# entries with rejected furigana flags (hard-correct pool)
hard_ids = set()
for line in open("reviews/decisions.jsonl", encoding="utf-8"):
    try: d = json.loads(line)
    except Exception: continue
    if d.get("dim") == "furigana" and d.get("decision") == "reject" and d.get("entry"):
        hard_ids.add(str(d["entry"])[:5])
print("hard entry ids", len(hard_ids), file=sys.stderr)

VOICE = {"か":"が","き":"ぎ","く":"ぐ","け":"げ","こ":"ご","さ":"ざ","し":"じ","す":"ず","せ":"ぜ","そ":"ぞ",
         "た":"だ","ち":"ぢ","つ":"づ","て":"で","と":"ど","は":"ば","ひ":"び","ふ":"ぶ","へ":"べ","ほ":"ぼ"}
UNVOICE = {v: k for k, v in VOICE.items()}
UNVOICE.update({"ぱ":"は","ぴ":"ひ","ぷ":"ふ","ぺ":"へ","ぽ":"ほ"})
SMALL = {"っ":"つ","ゃ":"や","ゅ":"ゆ","ょ":"よ"}
BIG = {v: k for k, v in SMALL.items()}
OROW = set("おこそとのほもよろごぞどぼぽょ")
all_readings = list({r for k in inv for r in inv[k]})

def wrong_variants(kanji, reading, following):
    """Return list of (type, wrong_reading)."""
    out = []
    alts = [r for r, n in inv.get(kanji, {}).items() if r != reading and n >= 2]
    if alts:
        out.append(("alt-reading", random.choice(alts)))
    f = reading[0]
    if f in VOICE: out.append(("rendaku", VOICE[f] + reading[1:]))
    elif f in UNVOICE: out.append(("rendaku", UNVOICE[f] + reading[1:]))
    # long vowel drop: remove a う that follows an o-row kana, or an い after e-row
    m = [i for i in range(1, len(reading)) if reading[i] == "う" and reading[i-1] in OROW]
    if m:
        i = random.choice(m); out.append(("long-vowel", reading[:i] + reading[i+1:]))
    elif len(reading) >= 2 and reading[-1] in OROW and reading[-1] not in "っ":
        out.append(("long-vowel", reading + "う"))
    sm = [i for i, c in enumerate(reading) if c in SMALL or (c in BIG and i > 0)]
    if sm:
        i = random.choice(sm); c = reading[i]
        out.append(("small-kana", reading[:i] + (SMALL.get(c) or BIG.get(c)) + reading[i+1:]))
    if following and HIRA.match(following[0]):
        out.append(("okurigana-bleed", reading + following[0]))
    # nonsense: a reading of another kanji string of similar length
    cands = [r for r in random.sample(all_readings, 200) if abs(len(r) - len(reading)) <= 1 and r != reading]
    if cands: out.append(("nonsense", cands[0]))
    return out

paths = sorted(glob.glob("entries/*/*.json"))
random.shuffle(paths)
correct, hard, wrong = [], [], []
per_type = collections.Counter()
TARGET_TYPE = 70
for p in paths:
    if len(correct) >= 320 and len(hard) >= 150 and all(per_type[t] >= TARGET_TYPE for t in
            ("alt-reading","rendaku","long-vowel","small-kana","okurigana-bleed","nonsense")):
        break
    e = json.load(open(p, encoding="utf-8"))
    eid = e["id"]; num = eid[:5]
    exs = [x for x in e.get("examples", []) if x.get("japanese") and FURI.search(plain(x["japanese"]))]
    if not exs: continue
    ex = random.choice(exs)
    sent = plain(ex["japanese"])
    ms = list(FURI.finditer(sent))
    m = random.choice(ms)
    kanji, reading = m.group(1), m.group(2)
    following = sent[m.end():m.end()+3]
    base = {"entry": eid, "headword": plain(e.get("headword","")), "hw_reading": e.get("reading",""),
            "gloss": e.get("gloss",""), "sentence": sent, "english": ex.get("english",""),
            "kanji": kanji, "reading": reading}
    is_hard = num in hard_ids
    if is_hard and len(hard) < 150:
        hard.append({**base, "label": "correct", "kind": "hard-correct"})
        continue
    if len(correct) < 320 and random.random() < 0.5:
        correct.append({**base, "label": "correct", "kind": "correct"}); continue
    variants = [v for v in wrong_variants(kanji, reading, following) if per_type[v[0]] < TARGET_TYPE]
    if not variants: continue
    t, wr = random.choice(variants)
    per_type[t] += 1
    wrong_sent = sent[:m.start()] + "{" + kanji + "|" + wr + "}" + sent[m.end():]
    wrong.append({**base, "sentence": wrong_sent, "reading": wr, "orig_reading": reading,
                  "label": "wrong", "kind": t})
items = correct + hard + wrong
random.shuffle(items)
for i, it in enumerate(items): it["n"] = i
json.dump(items, open(S / "furigana_set.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("correct", len(correct), "hard", len(hard), "wrong", len(wrong), dict(per_type), file=sys.stderr)
for it in wrong[:12]:
    print(it["kind"], it["kanji"], it["orig_reading"], "->", it["reading"], "|", it["sentence"][:60])
