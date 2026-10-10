"""Build test sets for decision-model evaluation from je-dict-1 data.

Each item: {"task", "id", "state", "label", "sub"}; label is True/False for noul tasks,
an option key for choice tasks. Writes sets/<task>.jsonl.
"""
import collections
import glob
import json
import random
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]  # repository root when run from enhancement/decision-models-2026-10-10/
OUT = Path(__file__).parent / "sets"
OUT.mkdir(exist_ok=True)
rng = random.Random(20261010)

LINK = re.compile(r"⟦(.*?)→(.*?)：(.*?)⟧")
FURI = re.compile(r"\{([^|{}]+)\|([^|{}]+)\}")


def unlink(s):
    return LINK.sub(lambda m: m.group(1), s or "")


def plain(s):
    return FURI.sub(lambda m: m.group(1), unlink(s))


def kana(s):
    return FURI.sub(lambda m: m.group(2), unlink(s))


print("loading entries", file=sys.stderr)
ENTRIES = {}
for f in glob.glob(str(REPO / "entries/*/*.json")):
    e = json.load(open(f))
    ENTRIES[e["id"][:5]] = e
INDEX = {e["id"][:5]: e for e in json.load(open(REPO / "entries_index.json"))["entries"]}


def write(task, items):
    with open(OUT / f"{task}.jsonl", "w") as f:
        for it in items:
            it["task"] = task
            f.write(json.dumps(it, ensure_ascii=False) + "\n")
    c = collections.Counter(str(i["label"]) for i in items)
    print(task, len(items), dict(c), file=sys.stderr)


# ---------------------------------------------------------------- T1 furigana
VOICE = dict(zip("かきくけこさしすせそたちつてとはひふへほ", "がぎぐげござじずぜぞだぢづでどばびぶべぼ"))
UNVOICE = {v: k for k, v in VOICE.items()}
SMALL_Y = set("ゃゅょ")


def mutate(r):
    """A plausible misreading of reading r, with the kind of error."""
    kinds = []
    # voicing toggle (rendaku errors) at a non-initial position
    pos = [i for i, ch in enumerate(r) if i > 0 and (ch in VOICE or ch in UNVOICE)]
    if pos:
        kinds.append("voicing")
    if re.search(r"[おこそとのほもよろごぞどぼぽょ]う|[うくすつぬふむゆるぐずづぶぷゅ]う", r):
        kinds.append("long-vowel")
    if "っ" in r:
        kinds.append("sokuon-drop")
    if any(ch in SMALL_Y for ch in r):
        kinds.append("youon")
    if not kinds:
        return None, None
    k = rng.choice(kinds)
    if k == "voicing":
        i = rng.choice(pos)
        ch = r[i]
        return r[:i] + (VOICE.get(ch) or UNVOICE[ch]) + r[i + 1:], k
    if k == "long-vowel":
        m = rng.choice(list(re.finditer(r"(?<=[おこそとのほもよろごぞどぼぽょうくすつぬふむゆるぐずづぶぷゅ])う", r)))
        return r[:m.start()] + r[m.end():], k
    if k == "sokuon-drop":
        i = r.index("っ")
        return r[:i] + r[i + 1:], k
    if k == "youon":
        i = next(i for i, ch in enumerate(r) if ch in SMALL_Y)
        return r[:i] + {"ゃ": "や", "ゅ": "ゆ", "ょ": "よ"}[r[i]] + r[i + 1:], k
    return None, None


def furigana_items(n_pos, n_mut, n_homo, common_only=False, exclude=()):
    items = []
    # homograph pairs: same kanji headword, different readings
    by_hw = collections.defaultdict(set)
    for eid, e in INDEX.items():
        hw = e["headword"]
        if re.search(r"[一-鿿]", hw) and not re.search(r"[぀-ゟ]", hw):
            by_hw[hw].add(e["reading"])
    homo = {hw: rs for hw, rs in by_hw.items() if len(rs) >= 2 and len(hw) >= 2}
    cands = []
    eids = sorted(ENTRIES)
    rng.shuffle(eids)
    for eid in eids:
        e = ENTRIES[eid]
        tier = e.get("metadata", {}).get("vocabulary_tier")
        if common_only and tier not in ("basic", "core"):
            continue
        for ex in e.get("examples", [])[:4]:
            jp = unlink(ex.get("japanese", ""))
            groups = [m for m in FURI.finditer(jp) if len(m.group(1)) >= 2]
            if not groups:
                continue
            m = rng.choice(groups)
            cands.append((eid, ex, jp, m))
            break
    homo_cands = []
    for eid, e in ENTRIES.items():
        for ex in e.get("examples", []):
            jp = unlink(ex.get("japanese", ""))
            for m in FURI.finditer(jp):
                if m.group(1) in homo and m.group(2) in homo[m.group(1)]:
                    homo_cands.append((eid, ex, jp, m))
    rng.shuffle(homo_cands)

    def state(jp, m, reading, ex):
        marked = jp[:m.start()] + "【" + m.group(1) + "】" + jp[m.end():]
        return {"sentence": plain(marked), "english": ex.get("english"),
                "marked_word": m.group(1), "proposed_reading": reading}

    used = set(exclude)
    for eid, ex, jp, m in cands:
        if len([i for i in items if i["label"] is True]) >= n_pos:
            break
        key = ex["id"]
        if key in used:
            continue
        used.add(key)
        items.append({"id": key + ":pos", "state": state(jp, m, m.group(2), ex), "label": True, "sub": "correct"})
    nm = 0
    for eid, ex, jp, m in cands:
        if nm >= n_mut:
            break
        if ex["id"] in used:
            continue
        bad, kind = mutate(m.group(2))
        if not bad:
            continue
        used.add(ex["id"])
        nm += 1
        items.append({"id": ex["id"] + ":mut", "state": state(jp, m, bad, ex), "label": False, "sub": kind})
    nh = 0
    seen_hw = collections.Counter()
    for eid, ex, jp, m in homo_cands:
        if nh >= n_homo:
            break
        if ex["id"] in used or seen_hw[m.group(1)] >= 2:
            continue
        others = sorted(homo[m.group(1)] - {m.group(2)})
        if not others:
            continue
        used.add(ex["id"])
        seen_hw[m.group(1)] += 1
        nh += 1
        # half homograph items show the right reading (hard positive), half the other reading
        if nh % 2:
            items.append({"id": ex["id"] + ":homo-neg", "state": state(jp, m, others[0], ex), "label": False,
                          "sub": "homograph"})
        else:
            items.append({"id": ex["id"] + ":homo-pos", "state": state(jp, m, m.group(2), ex), "label": True,
                          "sub": "homograph-correct"})
    return items, used


# Counter readings, written by hand (sound changes are the classic furigana error).
COUNTERS = [
    ("鉛筆が【三本】あります。", "三本", "さんぼん", "さんほん"),
    ("猫が【六匹】います。", "六匹", "ろっぴき", "ろくひき"),
    ("【一日】に三回薬を飲みます。", "一日", "いちにち", "いっにち"),
    ("四月【一日】は入学式です。", "一日", "ついたち", "いちにち"),
    ("【二十日】までに返事をください。", "二十日", "はつか", "にじゅうにち"),
    ("りんごを【八個】買いました。", "八個", "はっこ", "はちこ"),
    ("本を【十冊】借りました。", "十冊", "じゅっさつ", "じゅうさつ"),
    ("子どもが【三人】います。", "三人", "さんにん", "みにん"),
    ("【一人】で行きます。", "一人", "ひとり", "いちにん"),
    ("コップが【一杯】ある。", "一杯", "いっぱい", "いちはい"),
    ("家が【三軒】並んでいる。", "三軒", "さんげん", "さんけん"),
    ("【四時】に会いましょう。", "四時", "よじ", "しじ"),
    ("【九時】に寝ます。", "九時", "くじ", "きゅうじ"),
    ("【七日】に出発します。", "七日", "なのか", "しちにち"),
    ("階段を【三階】まで上がる。", "三階", "さんがい", "さんかい"),
    ("【十分】待ってください。", "十分", "じゅっぷん", "じゅうふん"),
]


def counter_items():
    items = []
    for i, (s, w, good, bad) in enumerate(COUNTERS):
        lab = i % 2 == 0
        items.append({"id": f"ctr{i}", "state": {"sentence": s, "english": None, "marked_word": w,
                                                   "proposed_reading": good if lab else bad},
                      "label": lab, "sub": "counter-correct" if lab else "counter"})
    return items


# ---------------------------------------------------------------- T2 links
def link_items(n_each):
    rows = [json.loads(l) for l in open(REPO / "reviews/link_decisions.jsonl")]
    seen = set()
    keep, bad = [], []
    for r in rows:
        k = (r.get("context"), r.get("target"))
        if k in seen or not r.get("context") or "【" not in r["context"]:
            continue
        seen.add(k)
        tid = (r.get("target") or "")[:5]
        t = INDEX.get(tid)
        if not t:
            continue
        english = None
        mm = re.match(r"examples\[(\d+)\]", r.get("field", ""))
        e = ENTRIES.get(str(r["entry"]).zfill(5))
        if mm and e and int(mm.group(1)) < len(e.get("examples", [])):
            english = e["examples"][int(mm.group(1))].get("english")
        st = {"text": plain(r["context"]), "english_translation": english,
              "marked_word": r["surface"],
              "linked_entry": {"headword": plain(t["headword"]), "reading": t["reading"],
                               "part_of_speech": t.get("part_of_speech"), "gloss": t["gloss"]}}
        it = {"id": f"{r['entry']}:{r['field']}:{r['surface']}:{tid}", "state": st,
              "label": r["decision"] == "keep", "sub": r["decision"] + ":" + r["base"]}
        (keep if it["label"] else bad).append(it)
    rng.shuffle(keep)
    rng.shuffle(bad)

    def diverse(lst, n):  # at most 3 per base so a few bases don't dominate
        c = collections.Counter()
        out = []
        for it in lst:
            b = it["sub"].split(":", 1)[1]
            if c[b] < 3:
                c[b] += 1
                out.append(it)
            if len(out) >= n:
                break
        return out
    return diverse(keep, n_each) + diverse(bad, n_each)


# ---------------------------------------------------------------- T3 flag triage
def flag_items(n_each):
    flags = collections.defaultdict(list)
    for l in open(REPO / "reviews/accuracy_flags.jsonl"):
        d = json.loads(l)
        flags[d["entry_id"][:5]].append(d)
    bydec = collections.defaultdict(list)
    for l in open(REPO / "reviews/decisions.jsonl"):
        d = json.loads(l)
        if d.get("entry") and (d.get("decision") or "").lower() in ("apply", "reject"):
            bydec[(d["entry"], d["dim"])].append(d)
    app, rej = [], []
    for (eid, dim), ds in bydec.items():
        if dim not in ("gloss", "notes", "translation") or len(ds) != 1:
            continue
        ts = ds[0]["ts"]
        cand = [r for r in flags.get(eid, []) if r["reviewed_at"] <= ts]
        if not cand:
            continue
        rv = max(cand, key=lambda r: r["reviewed_at"])
        iss = [i for i in rv["issues"] if i["dimension"] == dim]
        if len(iss) != 1:
            continue
        e = INDEX.get(eid)
        if not e:
            continue
        i = iss[0]
        st = {"headword": plain(e["headword"]), "reading": e["reading"], "entry_gloss": e["gloss"],
              "flag_dimension": dim, "flag_location": i.get("location"), "severity": i.get("severity"),
              "reviewer_concern": i.get("concern"), "reviewer_suggestion": i.get("suggestion")}
        it = {"id": f"{eid}:{dim}", "state": st, "label": ds[0]["decision"].lower() == "apply",
              "sub": dim}
        (app if it["label"] else rej).append(it)
    rng.shuffle(app)
    rng.shuffle(rej)
    return app[:n_each] + rej[:n_each]


# ---------------------------------------------------------------- T4 transitivity
def trans_items(n_t, n_i, n_b):
    buckets = collections.defaultdict(list)
    for eid, e in ENTRIES.items():
        t = e.get("metadata", {}).get("tags", {}).get("transitivity")
        if t not in ("transitive", "intransitive", "both"):
            continue
        exs = [{"japanese": plain(x["japanese"]), "english": x.get("english")} for x in e.get("examples", [])[:2]]
        st = {"headword": plain(e["headword"]), "reading": e["reading"], "gloss": e.get("gloss"), "part_of_speech": ", ".join(e.get("metadata", {}).get("tags", {}).get("pos", [])),
              "examples": exs}
        buckets[t].append({"id": eid, "state": st, "label": t, "sub": e.get("metadata", {}).get("vocabulary_tier")})
    out = []
    for t, n in (("transitive", n_t), ("intransitive", n_i), ("both", n_b)):
        rng.shuffle(buckets[t])
        out += buckets[t][:n]
    return out


# ---------------------------------------------------------------- T5 translation fidelity
def translation_pairs(n):
    eids = sorted(ENTRIES)
    rng.shuffle(eids)
    out = []
    for eid in eids:
        exs = [x for x in ENTRIES[eid].get("examples", []) if x.get("english") and len(plain(x["japanese"])) >= 12]
        if len(exs) >= 3:
            out.append((eid, exs))
        if len(out) >= n:
            break
    return out


# ---------------------------------------------------------------- T6 conjugation
GODAN_TE = {"う": "って", "つ": "って", "る": "って", "む": "んで", "ぶ": "んで", "ぬ": "んで",
            "く": "いて", "ぐ": "いで", "す": "して"}
A_ROW = {"う": "わ", "く": "か", "ぐ": "が", "す": "さ", "つ": "た", "ぬ": "な", "ぶ": "ば", "む": "ま", "る": "ら"}
WRONG_TE = {"く": ["って", "いで"], "ぐ": ["いて", "って"], "す": ["いて", "って"], "む": ["って", "いて"],
            "ぶ": ["って"], "う": ["いて", "んで"], "つ": ["いて", "んで"], "る": ["て", "んで"], "ぬ": ["って"]}


def conj_items(n_pos, n_neg):
    pos, neg = [], []
    eids = sorted(ENTRIES)
    rng.shuffle(eids)
    for eid in eids:
        e = ENTRIES[eid]
        cj = e.get("conjugation")
        if not cj or cj.get("type") not in ("godan", "ichidan"):
            continue
        hw = plain(e["headword"])
        rd = e["reading"]
        if " " in hw or len(hw) > 6:
            continue
        forms = {f["label"]: f for f in cj["forms"]}
        need = ["て form", "Past", "Present", "Potential", "Passive", "Volitional"]
        if not all(k in forms for k in need):
            continue
        stem = hw[:-1]
        last = hw[-1]
        if len(pos) < n_pos and rng.random() < 0.5:
            lab = rng.choice(need)
            pol = rng.choice(["affirmative", "negative"]) if forms[lab].get("negative") else "affirmative"
            val = plain(forms[lab][pol])
            pos.append({"id": f"{eid}:{lab}:{pol}", "state": {"verb": hw, "reading": rd, "gloss": e.get("gloss"),
                        "form_name": f"{lab} ({pol})", "proposed_form": val}, "label": True, "sub": cj["type"]})
        elif len(neg) < n_neg:
            kind = rng.choice(["te", "nai", "potential"])
            if cj["type"] == "godan":
                if kind == "te":
                    bad, lab, pol = stem + rng.choice(WRONG_TE.get(last, ["って"])), "て form", "affirmative"
                elif kind == "nai":
                    bad, lab, pol = (stem + "ない" if last == "る" else stem + "いない"), "Present", "negative"
                else:
                    bad, lab, pol = stem + A_ROW.get(last, "ら") + "れる", "Potential", "affirmative"
                    if last == "る":
                        bad = stem + "られる"
            else:  # ichidan conjugated as godan
                if kind == "te":
                    bad, lab, pol = stem + "って", "て form", "affirmative"
                elif kind == "nai":
                    bad, lab, pol = stem + "らない", "Present", "negative"
                else:
                    bad, lab, pol = stem + "れる", "Potential", "affirmative"
            good = plain(forms[lab][pol])
            if bad == good:
                continue
            neg.append({"id": f"{eid}:{lab}:{pol}:bad", "state": {"verb": hw, "reading": rd, "gloss": e.get("gloss"),
                        "form_name": f"{lab} ({pol})", "proposed_form": bad}, "label": False,
                        "sub": cj["type"] + ":" + kind})
        if len(pos) >= n_pos and len(neg) >= n_neg:
            break
    return pos + neg


# ---------------------------------------------------------------- T7 sense assignment
def sense_items(n):
    out = []
    eids = sorted(ENTRIES)
    rng.shuffle(eids)
    per = collections.Counter()
    for eid in eids:
        e = ENTRIES[eid]
        defs = e.get("definitions", [])
        if not 2 <= len(defs) <= 4:
            continue
        exs = [x for x in e.get("examples", []) if len(x.get("sense_numbers") or []) == 1]
        senses = {f"sense{d['sense_number']}": d.get("gloss") for d in defs}
        if len(set(senses.values())) < len(senses):
            continue
        rng.shuffle(exs)
        for x in exs[:1]:
            key = f"sense{x['sense_numbers'][0]}"
            if key not in senses:
                continue
            out.append({"id": x["id"], "state": {"headword": plain(e["headword"]), "reading": e["reading"],
                        "sentence": plain(x["japanese"])}, "senses": senses, "label": key,
                        "sub": f"{len(defs)}-sense"})
        if len(out) >= n:
            break
    return out


if __name__ == "__main__":
    # Stage-1 screening battery: easy items only
    fur, used = furigana_items(8, 8, 0, common_only=True)
    scr = [dict(it, task_kind="reading") for it in fur]
    # easy translation: correct pair vs an unrelated sentence's English
    pairs = translation_pairs(40)
    for k, (eid, exs) in enumerate(pairs[:16]):
        x = exs[0]
        if k % 2 == 0:
            en, lab = x["english"], True
        else:
            other = pairs[(k + 17) % len(pairs)][1][0]["english"]
            en, lab = other, False
        scr.append({"id": x["id"] + ":scr", "task_kind": "translation", "label": lab,
                    "state": {"japanese": plain(x["japanese"]), "english": en}, "sub": "easy"})
    # word meaning: basic-tier word, pick gloss among 4
    basics = [e for e in INDEX.values() if e.get("vocabulary_tier") == "basic"
              and re.search(r"[一-鿿]", e["headword"]) and e.get("part_of_speech") == "noun"]
    rng.shuffle(basics)
    for k in range(8):
        tgt = basics[k]
        opts = [tgt] + basics[20 + 3 * k: 23 + 3 * k]
        rng.shuffle(opts)
        crit = {f"o{j}": o["gloss"] for j, o in enumerate(opts)}
        scr.append({"id": tgt["id"] + ":mean", "task_kind": "meaning", "state": {"word": plain(tgt["headword"])},
                    "senses": crit, "label": f"o{opts.index(tgt)}", "sub": "basic"})
    # English-only control
    ctrl = [("The train was delayed because of heavy snow this morning.", True),
            ("Please pass me the salt.", False),
            ("Yesterday we finally finished painting the fence.", True),
            ("I usually drink coffee in the morning.", False),
            ("She had already left by the time I arrived.", True),
            ("Will you come to the party next week?", False),
            ("Last year the company opened two new offices.", True),
            ("The sky is blue on clear days.", False)]
    for k, (s, lab) in enumerate(ctrl):
        scr.append({"id": f"ctrl{k}", "task_kind": "control", "state": {"sentence": s}, "label": lab, "sub": "en"})
    write("screen", scr)

    f1, used = furigana_items(100, 70, 60, exclude=used)
    write("furigana", f1 + counter_items())
    write("links", link_items(110))
    write("flags", flag_items(100))
    write("transitivity", trans_items(80, 80, 30))
    tp = translation_pairs(260)[40:]
    tr = []
    for k, (eid, exs) in enumerate(tp[:200]):
        x = exs[0]
        if k % 4 in (0, 1):
            tr.append({"id": x["id"], "state": {"japanese": plain(x["japanese"]), "english": x["english"]},
                       "label": True, "sub": "original"})
        elif k % 4 == 2:
            y = exs[1]  # English of a sibling example of the same headword
            tr.append({"id": x["id"] + ":swap", "state": {"japanese": plain(x["japanese"]), "english": y["english"]},
                       "label": False, "sub": "sibling-swap"})
        else:
            tr.append({"id": x["id"] + ":perturb", "state": {"japanese": plain(x["japanese"]),
                       "english": x["english"]}, "label": False, "sub": "perturb-pending"})
    write("translation", tr)
    write("conjugation", conj_items(90, 90))
    write("sense", sense_items(160))
