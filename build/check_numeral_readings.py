#!/usr/bin/env python3
"""List furigana on number + counter words that ignore the standard sound changes.

    python3 build/check_numeral_readings.py            # one line per finding
    python3 build/check_numeral_readings.py --json     # JSON list (systemic-fix detector)
    python3 build/check_numeral_readings.py --ids 00705,00728

Read-only. Looks at every example sentence, collocation and the notes for a
kanji numeral from 1 to 99 written with furigana and followed by one of the
counters below, and compares the reading with the standard ones: 一本 いっぽん
(not いちほん or いちぽん), 九時 くじ, 十八歳 じゅうはっさい, 二十分 にじゅっぷん or
にじっぷん, 四人 よにん, 二つ ふたつ, 十四日 じゅうよっか. Where a common
alternative exists it is accepted (はちほん, じっぷん, ななじ, 一月 ひとつき, 十分
じゅうぶん "enough", 一日 いちにち). A run followed by another kanji is skipped
unless that kanji is 間, 目, 後, 前, 中 or 半 (三日月 is not 三日 + 月); 一回り, 四つん這い,
fractions (三分の一 さんぶん), tenths (腹八分 はちぶ), and in the notes the bound forms みつ, よつ,
むつ, やつ that etymologies cite (三つ + 編み) are passed over.

Found by the audio checks (2026-09-26): the TTS said the right reading, the
checkers heard it, and the example was left for a human because its furigana
was wrong. Each finding is a judgment fix: check the sentence's meaning
(一日 ついたち or いちにち, 十分 じゅっぷん or じゅうぶん), then correct the
furigana.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"⟦([^⟦⟧]*?)→[^⟦⟧]*?⟧")
TOKEN = re.compile(r"\{([^{}|]+)\|([^{}|]+)\}|(.)", re.S)
KANJI = re.compile(r"[㐀-鿿豈-﫿々]")
NUMERAL = "一二三四五六七八九十"
DIGIT = {c: i + 1 for i, c in enumerate("一二三四五六七八九")}
ALLOWED_NEXT = set("間目後前中半")

# Readings of 1..10 + counter, "/" between accepted alternatives.
UNITS = {
    "本": "いっぽん にほん さんぼん よんほん ごほん ろっぽん ななほん はっぽん/はちほん きゅうほん じゅっぽん/じっぽん",
    "回": "いっかい にかい さんかい よんかい ごかい ろっかい ななかい はっかい/はちかい きゅうかい じゅっかい/じっかい",
    "週間": "いっしゅうかん にしゅうかん さんしゅうかん よんしゅうかん ごしゅうかん ろくしゅうかん ななしゅうかん はっしゅうかん/はちしゅうかん きゅうしゅうかん じゅっしゅうかん/じっしゅうかん",
    "歳": "いっさい にさい さんさい よんさい ごさい ろくさい ななさい はっさい きゅうさい じゅっさい/じっさい",
    "分": "いっぷん にふん さんぷん よんぷん ごふん ろっぷん ななふん はっぷん/はちふん きゅうふん じゅっぷん/じっぷん",
    "人": "ひとり ふたり さんにん よにん ごにん ろくにん ななにん/しちにん はちにん きゅうにん/くにん じゅうにん",
    "時": "いちじ にじ さんじ よじ ごじ ろくじ しちじ/ななじ はちじ くじ じゅうじ",
    "月": "いちがつ にがつ さんがつ しがつ ごがつ ろくがつ しちがつ はちがつ くがつ じゅうがつ",
    "日": "ついたち/いちにち ふつか みっか よっか いつか むいか なのか/なぬか ようか ここのか とおか",
    "個": "いっこ にこ さんこ よんこ ごこ ろっこ ななこ はっこ/はちこ きゅうこ じゅっこ/じっこ",
    "杯": "いっぱい にはい さんばい よんはい ごはい ろっぱい ななはい はっぱい/はちはい きゅうはい じゅっぱい/じっぱい",
    "匹": "いっぴき にひき さんびき よんひき ごひき ろっぴき ななひき はっぴき/はちひき きゅうひき じゅっぴき/じっぴき",
    "冊": "いっさつ にさつ さんさつ よんさつ ごさつ ろくさつ ななさつ はっさつ/はちさつ きゅうさつ じゅっさつ/じっさつ",
    "年": "いちねん にねん さんねん よねん ごねん ろくねん ななねん/しちねん はちねん きゅうねん/くねん じゅうねん",
    "つ": "ひとつ ふたつ みっつ よっつ いつつ むっつ ななつ やっつ ここのつ",
}
UNITS["才"] = UNITS["歳"]
# The unit word inside 11..99 where it differs from the 1..10 row.
COMPOUND_UNIT = {"人": {1: "いちにん", 2: "ににん"}}
# Days 11..31 that are not じゅう/にじゅう/さんじゅう + number + にち.
DAYS = {14: "じゅうよっか", 20: "はつか", 24: "にじゅうよっか"}
DAY_UNIT = {1: "いち", 2: "に", 3: "さん", 5: "ご", 6: "ろく", 7: "しち/なな", 8: "はち", 9: "く"}
# Other accepted readings of whole words (not counter uses, or set words).
EXTRA = {"一月": "ひとつき", "二月": "ふたつき", "三月": "みつき",
         "一日": "いちじつ", "一分": "いちぶ", "五分": "ごぶ", "九分": "くぶ", "十分": "じゅうぶん",
         "二十歳": "はたち", "一人": "いちにん", "一年": "ひととせ", "一時": "いっとき/ひととき",
         "二分": "にぶん", "十二分": "じゅうにぶん", "三十日": "みそか", "五月": "さつき"}
TENS = {1: "じゅう", 2: "にじゅう", 3: "さんじゅう", 4: "よんじゅう", 5: "ごじゅう",
        6: "ろくじゅう", 7: "ななじゅう", 8: "はちじゅう", 9: "きゅうじゅう"}
COUNTERS = sorted(UNITS, key=len, reverse=True)
MAX = {"時": 24, "月": 12, "つ": 9, "日": 31}


def cell(counter, u):
    return set(UNITS[counter].split(" ")[u - 1].split("/"))


def kanji_number(s):
    """一..九十九 → int, or None."""
    if not s or any(c not in NUMERAL for c in s):
        return None
    if "十" not in s:
        return DIGIT[s] if len(s) == 1 else None
    head, _, tail = s.partition("十")
    if len(head) > 1 or len(tail) > 1:
        return None
    return (DIGIT[head] if head else 1) * 10 + (DIGIT[tail] if tail else 0)


def accepted(n, counter, surface):
    """Accepted readings of number n + counter, or None when not checked."""
    if not n or n > MAX.get(counter, 99):
        return None
    tens, u = divmod(n, 10)
    if n <= 10:
        out = cell(counter, n)
    elif counter == "日":
        if n in DAYS:
            out = {DAYS[n]}
        elif u == 0:
            out = {TENS[tens][:-3] + "じゅうにち"} if tens > 1 else set()
        else:
            out = {TENS[tens] + x + "にち" for x in DAY_UNIT[u].split("/")}
    elif u == 0:  # 二十分 = に + the 10 cell
        out = {TENS[tens][:-3] + w for w in cell(counter, 10)}
    else:
        unit = {COMPOUND_UNIT[counter][u]} if u in COMPOUND_UNIT.get(counter, {}) else cell(counter, u)
        out = {TENS[tens] + w for w in unit}
    if surface in EXTRA:
        out |= set(EXTRA[surface].split("/"))
    return out


def tokens(text):
    text = LINK.sub(lambda m: m.group(1), text)
    return [(m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(3))
            for m in TOKEN.finditer(text)]


# Bound forms of 三つ, 四つ, 六つ, 八つ in compounds (三つ編み みつあみ, 四つ角 よつかど),
# which notes cite when they take a compound apart.
BOUND_TSU = {"みつ", "よつ", "むつ", "やつ"}


def findings_in(text, notes=False):
    toks = tokens(text)
    out = []
    for i, (surf, reading) in enumerate(toks):
        if surf == reading or surf[0] not in NUMERAL:
            continue
        if i > 0 and (KANJI.match(toks[i - 1][0][-1]) or toks[i - 1][0][-1] in NUMERAL):
            continue
        s, r = "", ""
        for j in range(i, min(i + 4, len(toks))):
            s += toks[j][0]
            r += toks[j][1]
            m = re.fullmatch(f"([{NUMERAL}]+)({'|'.join(COUNTERS)})", s)
            if not m:
                continue
            nxt = toks[j + 1][0][0] if j + 1 < len(toks) else ""
            if KANJI.match(nxt) and nxt not in ALLOWED_NEXT:
                break
            if m.group(2) == "回" and nxt == "り":  # 一回り ひとまわり
                break
            if m.group(2) == "つ" and nxt == "ん":  # 四つん這い よつんばい
                break
            n = kanji_number(m.group(1))
            ok = accepted(n, m.group(2), s) if n else None
            if ok and m.group(2) == "分":  # 三分の一 さんぶんのいち, 腹八分 はちぶ
                if r.endswith(("ぶ", "ぶん")) and (nxt == "の" or r.endswith("ぶ")):
                    ok = None
            if notes and m.group(2) == "つ" and r in BOUND_TSU:
                break
            if ok and r not in ok:
                out.append({"surface": s, "reading": r, "expected": sorted(ok)})
            break
    return out


def entry_texts(e):
    for i, ex in enumerate(e.get("examples") or []):
        if isinstance(ex, dict) and ex.get("japanese"):
            yield f"examples[{i}]", ex["japanese"]
    for i, c in enumerate(e.get("collocations") or []):
        t = c.get("japanese") or c.get("phrase") if isinstance(c, dict) else c
        if isinstance(t, str):
            yield f"collocations[{i}]", t
    if isinstance(e.get("notes"), str):
        yield "notes", e["notes"]


def scan(ids=None):
    results = []
    for p in sorted((ROOT / "entries").glob("*/*.json")):
        eid = p.name[:5]
        if ids and eid not in ids:
            continue
        e = json.loads(p.read_text(encoding="utf-8"))
        for field, text in entry_texts(e):
            for f in findings_in(text, notes=field == "notes"):
                results.append({"id": eid, "file": str(p.relative_to(ROOT)), "field": field, **f})
    return results


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--ids", help="comma-separated entry IDs")
    args = ap.parse_args(argv)
    ids = {x.strip()[:5] for x in args.ids.split(",")} if args.ids else None
    res = scan(ids)
    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
    else:
        for r in res:
            print(f"{r['id']} {r['field']}: {r['surface']} {r['reading']} → {' / '.join(r['expected'])}")
        print(f"{len(res)} findings in {len({r['id'] for r in res})} entries", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
