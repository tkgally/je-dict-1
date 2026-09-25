"""Compare STT transcripts with the dictionary sentences.

For every clip × transcriber:
  kanji transcribers (dedicated STT) – the transcript is aligned with the
      dictionary text (NFKC, punctuation removed, Arabic numerals → kanji
      numerals).  Each differing region is compared by reading: the dictionary
      side uses the furigana, the transcript side MeCab/UniDic in context.
      Same reading (e.g. 子供/子ども, 方/ほう) → accepted spelling variant.
      Limitation: where the transcript has the same kanji as the dictionary,
      the reading actually spoken (今日＝きょう/こんにち) cannot be checked.
  kana transcribers (audio LLM told to write hiragana) – the whole reading is
      compared with the furigana reading, after folding は/わ, へ/え, を/お and
      long-vowel spellings.
  verdict – "match" or "mismatch" (with the differing spans); "n/a" when a
      kana transcriber refused ("I cannot listen to audio").
Writes data/eval.json (per clip) and prints summary tables."""
import json
import re
import unicodedata
from collections import defaultdict
from difflib import SequenceMatcher

import fugashi

from common import DATA, KANJI, kata2hira, norm_text

tagger = fugashi.Tagger()

LETTERS = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                   "エー ビー シー ディー イー エフ ジー エイチ アイ ジェー ケー エル エム "
                   "エヌ オー ピー キュー アール エス ティー ユー ブイ ダブリュー エックス ワイ ゼット".split()))
SPECIAL = {"Wi-Fi": "ワイファイ", "WiFi": "ワイファイ", "wifi": "ワイファイ",
           "%": "パーセント", "％": "パーセント"}
DIG = "〇一二三四五六七八九"


def num2kanji(n):
    if n == 0:
        return "零"
    out = ""
    for unit, size in (("兆", 10**12), ("億", 10**8), ("万", 10**4), ("", 1)):
        g, n = divmod(n, size)
        if not g:
            continue
        s = ""
        for u, v in (("千", 1000), ("百", 100), ("十", 10)):
            d, g = divmod(g, v)
            if d:
                s += ("" if d == 1 else DIG[d]) + u
        if g:
            s += DIG[g]
        out += s + unit
    return out


def norm_numbers(s):
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"(?<=\d),(?=\d{3})", "", s)
    s = s.replace("%", "パーセント")
    return re.sub(r"\d+", lambda m: num2kanji(int(m.group())), s)


VOWEL = {c: v for row, v in (("あかさたなはまやらわがざだばぱぁゃ", "あ"),
                              ("いきしちにひみりぎじぢびぴぃ", "い"),
                              ("うくすつぬふむゆるぐずづぶぷぅゅ", "う"),
                              ("えけせてねへめれげぜでべぺぇ", "え"),
                              ("おこそとのほもよろをごぞどぼぽぉょ", "お")) for c in row}


def expand_choon(s):
    out = ""
    for c in s:
        out += VOWEL.get(out[-1], "") if c == "ー" and out else c
    return out


def norm_kana(s):
    s = kata2hira(unicodedata.normalize("NFKC", s))
    s = expand_choon(s).replace("ぢ", "じ").replace("づ", "ず")
    return "".join(c for c in s if unicodedata.category(c)[0] in "LN")


def to_kana(text):
    """Kana reading of a transcript (kanji text → MeCab/UniDic reading)."""
    text = norm_numbers(text)
    for k, v in SPECIAL.items():
        text = text.replace(k, v)
    out = []
    for w in tagger(text):
        kana = w.feature.kana
        if kana:
            out.append(kana)
        elif re.fullmatch(r"[A-Z]{1,6}", w.surface):
            out.append("".join(LETTERS[c] for c in w.surface))
        else:
            out.append(w.surface)
    return norm_kana("".join(out))


def distance(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def diff_ops(a, b):
    """Compact diff: list of [op, expected, heard]."""
    return [[op, a[i1:i2], b[j1:j2]] for op, i1, i2, j1, j2
            in SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if op != "equal"]


def loose(k):
    """Pronunciation-level folding applied to both sides: particles は/へ/を,
    and long vowels spelled う/い after o-/e-row kana (こう→こお, けい→けえ)."""
    k = k.replace("を", "お").replace("は", "わ").replace("へ", "え").replace("ゔ", "ぶ")
    out = ""
    for c in k:
        v = VOWEL.get(out[-1]) if out else None
        out += "お" if c == "う" and v == "お" else "え" if c == "い" and v == "え" else c
    return out


def expected_segments(sentence):
    """[(surface, kana|None)] with furigana groups kept whole; for sentences
    with hand-supplied readings the kana of digits/Latin is unknown (None)."""
    segs = []
    for base, reading in sentence["tokens"]:
        if reading:
            segs.append((norm_text(base), norm_kana(reading)))
        else:
            for chunk in re.findall(r"\d[\d,]*|[A-Za-z][A-Za-z\-]*|.", unicodedata.normalize("NFKC", base)):
                s = norm_text(norm_numbers(chunk))
                if s:
                    known = not re.search(r"[0-9A-Za-z]", chunk)
                    segs.append((s, norm_kana(s) if known else None))
    return segs


def align_blocks(exp, got, ebounds, gbounds):
    """Character alignment as alternating equal/diff blocks [tag, i1, i2, j1, j2].
    Diff blocks are grown (consuming neighbouring equal characters on both
    sides at once) until both of their ends fall on furigana-group boundaries
    in the dictionary text and on analyzer-token boundaries in the transcript."""
    blocks = [["equal" if op == "equal" else "diff", i1, i2, j1, j2] for op, i1, i2, j1, j2
              in SequenceMatcher(None, exp, got, autojunk=False).get_opcodes()]

    def tidy(bl):
        out = []
        for b in bl:
            if b[0] == "equal" and b[2] == b[1]:
                continue
            if out and out[-1][0] == b[0] == "diff":
                out[-1][2], out[-1][4] = b[2], b[4]
            else:
                out.append(b)
        return out

    changed = True
    while changed:
        changed = False
        blocks = tidy(blocks)
        for k, b in enumerate(blocks):
            if b[0] != "diff":
                continue
            need = max(b[1] - max(x for x in ebounds if x <= b[1]),
                       b[3] - max(x for x in gbounds if x <= b[3]))
            if need and k > 0:
                prev = blocks[k - 1]
                m = min(need, prev[2] - prev[1])
                prev[2] -= m; prev[4] -= m; b[1] -= m; b[3] -= m
                changed = True
            need = max(min(x for x in ebounds if x >= b[2]) - b[2],
                       min(x for x in gbounds if x >= b[4]) - b[4])
            if need and k + 1 < len(blocks):
                nxt = blocks[k + 1]
                m = min(need, nxt[2] - nxt[1])
                nxt[1] += m; nxt[3] += m; b[2] += m; b[4] += m
                changed = True
    return blocks


def tokenize_kana(got):
    """Analyzer tokens of the (normalized) transcript with char boundaries."""
    bounds, kanas, pos = [0], [], 0
    for w in tagger(got):
        pos += len(w.surface)
        bounds.append(pos)
        kanas.append(to_kana(w.surface) if not w.feature.kana else norm_kana(w.feature.kana))
    return bounds, kanas


def check_text(sentence, text):
    """Kanji transcript: align with the dictionary text.  Wherever the text
    differs, the differing region (widened to whole furigana groups and whole
    analyzer tokens, analyzed in full-sentence context) must have the same
    reading for the clip to count as a match."""
    segs = expected_segments(sentence)
    exp = "".join(s for s, _ in segs)
    got = norm_text(norm_numbers(text))
    ebounds = [0]
    for s, _ in segs:
        ebounds.append(ebounds[-1] + len(s))
    gbounds, gkanas = tokenize_kana(got)
    blocks = align_blocks(exp, got, ebounds, gbounds)
    regions = [b[1:] for b in blocks if b[0] == "diff"]
    diffs, homophones = [], []
    for i1, i2, j1, j2 in regions:
        e_surf, g_surf = exp[i1:i2], got[j1:j2]
        a, b = ebounds.index(i1), ebounds.index(i2)
        e_kana = "".join(k if k is not None else s for s, k in segs[a:b])
        e_known = all(k is not None for _, k in segs[a:b])
        g_kana = "".join(gkanas[gbounds.index(j1):gbounds.index(j2)])
        if e_known and loose(e_kana) == loose(g_kana):
            homophones.append([e_surf, g_surf])
        else:
            diffs.append([e_surf, g_surf, e_kana, g_kana])
    return diffs, homophones, exp, got


REFUSAL = re.compile(r"音声.{0,12}(聞くこと|聞け|できません)|テキストで(提供|教え)|書き起こ|再生して|cannot (hear|listen)", re.I)


def latin_to_kana(text):
    for k, v in SPECIAL.items():
        text = text.replace(k, v)
    return re.sub(r"[A-Za-z]{1,6}", lambda m: "".join(LETTERS.get(c.upper(), c) for c in m.group()), text)


def check(sentence, text, kana_mode):
    if kana_mode and REFUSAL.search(text):
        return {"verdict": "n/a", "cer": None, "heard": "", "diff": []}
    if kana_mode and not KANJI.search(text):
        exp_kanas = [norm_kana(k) for k in [sentence["kana"], *sentence["alt_kana"]]]
        got = norm_kana(latin_to_kana(norm_numbers(text)))
        best = min(exp_kanas, key=lambda k: distance(loose(k), loose(got)))
        d = distance(loose(best), loose(got))
        return {"verdict": "match" if d == 0 else "mismatch",
                "cer": round(d / max(1, len(best)), 3),
                "heard": got, "diff": diff_ops(best, got)}
    diffs, homophones, exp, got = check_text(sentence, text)
    d = distance(exp, got)
    return {"verdict": "mismatch" if diffs else "match",
            "cer": round(d / max(1, len(exp)), 3), "heard": got,
            "diff": [["replace", e, g] for e, g, _, _ in diffs],
            "diff_kana": [[ek, gk] for _, _, ek, gk in diffs],
            "homophones": homophones}


def parse_json(text):
    m = re.search(r"\{.*\}", text, re.S)
    try:
        return json.loads(m.group()) if m else None
    except json.JSONDecodeError:
        return None


def check_choice(rec):
    """Targeted check: the reading picked for each ambiguous word."""
    if not rec.get("answer"):
        return {"verdict": "n/a", "heard": "", "diff": []}
    got = parse_json(rec["text"])
    if not isinstance(got, dict):
        return {"verdict": "n/a", "heard": rec["text"][:80], "diff": []}
    diff = []
    for n, a in rec["answer"].items():
        pick = str(got.get(n, "")).strip().lower()
        expected = a["options"][a["correct"]]
        if pick.startswith("x"):
            heard = pick.split(":", 1)[-1].strip()
            if loose(norm_kana(heard)) != loose(norm_kana(expected)):
                diff.append(["replace", expected, heard or "∅"])
        elif pick[:1] != a["correct"]:
            diff.append(["replace", expected, a["options"].get(pick[:1], pick or "?")])
    return {"verdict": "mismatch" if diff else "match",
            "heard": json.dumps(got, ensure_ascii=False), "diff": diff}


def check_compare(rec, particles=False):
    """Reference comparison: differences the model reports, minus spelling-only
    ones.  With particles (pcompare), は/わ, へ/え, を/お are not folded, since a
    particle pronounced as written is exactly what the check looks for."""
    fold = (lambda k: loose(k)) if not particles else (lambda k: loose(k.replace("は", "\0").replace("へ", "\1").replace("を", "\2")))
    got = parse_json(rec["text"])
    if not isinstance(got, dict):
        return {"verdict": "n/a", "heard": rec["text"][:80], "diff": []}
    diff = []
    for d in got.get("differences") or []:
        if not isinstance(d, dict):
            continue
        e, h = str(d.get("expected", "")), str(d.get("heard", ""))
        if fold(norm_kana(e)) != fold(norm_kana(h)):
            diff.append(["replace", e, h])
    bad = bool(diff) or got.get("match") is False and not got.get("differences")
    return {"verdict": "mismatch" if bad else "match", "heard": "", "diff": diff}


def load_stt():
    res = defaultdict(dict)  # model -> key -> record
    for p in sorted((DATA / "stt").glob("*.jsonl")):
        for line in open(p):
            r = json.loads(line)
            if "text" in r:
                res[r["model"]][r["key"]] = r
    return res


def check_record(sentence, model, rec):
    if model.startswith("choice:"):
        return check_choice(rec)
    if model.startswith("compare:"):
        return check_compare(rec)
    if model.startswith("pcompare:"):
        return check_compare(rec, particles=True)
    return check(sentence, rec["text"], model.startswith("kana:"))


def main():
    sentences = {s["n"]: s for s in json.load(open(DATA / "sentences.json"))}
    manifest = {}
    for line in open(DATA / "tts_manifest.jsonl"):
        r = json.loads(line)
        if not r.get("error"):
            manifest[r["key"]] = r
    stt = load_stt()
    evals = {}
    for key, clip in manifest.items():
        s = sentences[clip["n"]]
        ev = {}
        for model, recs in stt.items():
            if key in recs:
                ev[model] = {"text": recs[key]["text"], **check_record(s, model, recs[key])}
        evals[key] = ev
    json.dump(evals, open(DATA / "eval.json", "w"), ensure_ascii=False)

    # summary: verdict counts per transcriber on controls vs. normal clips
    print(f"{'transcriber':45} {'set':9} {'n':>4} {'match':>6} {'unver':>6} {'mism':>6}")
    for model in stt:
        for label, pred in (("controls", lambda c: c["strategy"] == "control"),
                            ("normal", lambda c: c["strategy"] not in ("control", "furigana_unstructured"))):
            v = [evals[k][model]["verdict"] for k, c in manifest.items()
                 if pred(c) and model in evals[k]]
            if v:
                print(f"{model:45} {label:9} {len(v):4} {v.count('match'):6} "
                      f"{v.count('unverified'):6} {v.count('mismatch'):6}")


if __name__ == "__main__":
    main()


_MAJORITY = None


def minority_reading(base, reading):
    """True if the dictionary's furigana gives this spelling some other
    reading more often than this one (私＝わたくし: 11 vs わたし 512)."""
    global _MAJORITY
    if _MAJORITY is None:
        idx = json.load(open(DATA / "reading_index.json"))
        _MAJORITY = {b: max(c, key=c.get) for b, c in idx.items()}
    return base in _MAJORITY and _MAJORITY[base] != reading


def kana_substituted(sentence, dict_rule=False):
    """The sentence with every furigana word whose reading MeCab/UniDic would
    get wrong written in hiragana instead (e.g. 今日→こんにち, 上手→うわて).
    With dict_rule, also every word whose reading is a minority reading of
    its spelling in the dictionary (私→わたくし, 年月→としつき).
    Regions are the smallest spans on which furigana groups and analyzer
    tokens align, so okurigana stay attached to their word."""
    segs, pos, plain = [], 0, ""
    for base, reading in sentence["tokens"]:
        segs.append((pos, pos + len(base), reading))
        pos += len(base)
        plain += base
    tokens, tpos = [], 0
    for w in tagger(plain):
        start = plain.index(w.surface, tpos)
        tokens.append((start, start + len(w.surface), w.feature.kana or ""))
        tpos = start + len(w.surface)
    bounds_s = {0, len(plain)} | {a for a, _, _ in segs} | {b for _, b, _ in segs}
    bounds_t = {0, len(plain)} | {a for a, _, _ in tokens} | {b for _, b, _ in tokens}
    cuts = sorted(bounds_s & bounds_t)
    out = ""
    for lo, hi in zip(cuts, cuts[1:]):
        inside = [x for x in segs if x[0] >= lo and x[1] <= hi]
        if not any(r for _, _, r in inside):
            out += plain[lo:hi]
            continue
        fur = "".join(r if r else plain[a:b] for a, b, r in inside)
        ana = "".join(k for a, b, k in tokens if a >= lo and b <= hi)
        after_digit = lo > 0 and plain[lo - 1].isdigit()  # 1泊, 3本: leave counters to the TTS
        differs = loose(norm_kana(fur)) != loose(norm_kana(ana))
        if dict_rule:
            differs = differs or any(r and minority_reading(plain[a:b], r) for a, b, r in inside)
        out += fur if differs and not after_digit else plain[lo:hi]
    return out
