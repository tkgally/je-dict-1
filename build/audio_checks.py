"""The four AI checkers and the acceptance rule (AUDIO_WORKFLOW.md §6).

Scoring is deterministic and unit-tested; `run_checkers` is the only function
that calls the network (through audio_api.ask_audio).

Checkers (config key "checkers", in this order):
  pcompare  particle-aware compare: the model is given the phonetic reading and
            lists every difference it hears.
  kana      hiragana transcription, compared with the expected reading.
Acceptance rule v2 ("p2"): the first checker (pcompare) says match AND at most
one of the others objects. No verdict ("n/a": refusal, unparseable reply, API
failure) counts as an objection.
"""
import json
import re
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from difflib import SequenceMatcher

from audio_text import (KANJI, distance, latin_to_kana, loose, norm_kana,
                        norm_numbers, norm_text, phonetic_kana, tagger, to_kana)

KANA_PROMPT = (
    "Transcribe the Japanese speech in this audio exactly as it is pronounced, "
    "writing everything in hiragana (katakana only for loanwords). Do not use "
    "kanji, do not correct or normalize anything, and write any non-Japanese "
    "speech verbatim. Output only the transcription.")


def pcompare_prompt(s):
    """Particle-aware compare prompt. Several acceptable readings are listed
    separated by " / "."""
    readings = [phonetic_kana(s)] + [phonetic_kana({**s, "kana": a}) for a in s.get("alt_kana", [])]
    alts = "(Alternatives separated by / are all acceptable.)\n" if len(readings) > 1 else ""
    return (
        "You will hear a recording of a Japanese sentence. The intended pronunciation, in kana, is:\n"
        f"{' / '.join(readings)}\n"
        f"{alts}"
        "(Particles are written as they are pronounced: わ for the topic particle は, え for へ, お for を.)\n\n"
        "Listen carefully and check whether the speaker said exactly this. Report every difference: a word "
        "pronounced differently (for example a different reading of a kanji), a particle pronounced as written "
        "instead of as spoken (for example the particle は pronounced \"ha\" instead of \"wa\"), a word missing, "
        "added or repeated, the sentence read twice, or any extra speech. Ignore intonation, pitch accent, "
        "speed, voice quality, and long-vowel spelling.\n\n"
        "Reply with JSON only: {\"differences\": [{\"expected\": \"…\", \"heard\": \"…\"}], "
        "\"match\": true or false}")


# --------------------------------------------------------------------------- scoring helpers
def diff_ops(a, b):
    """Compact diff: [[op, expected, heard], …] for the non-equal spans."""
    return [[op, a[i1:i2], b[j1:j2]] for op, i1, i2, j1, j2
            in SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if op != "equal"]


def parse_json(text):
    m = re.search(r"\{.*\}", text or "", re.S)
    try:
        return json.loads(m.group()) if m else None
    except json.JSONDecodeError:
        return None


REFUSAL = re.compile(r"音声.{0,12}(聞くこと|聞け|できません)|テキストで(提供|教え)|書き起こ|再生して"
                     r"|cannot (hear|listen)", re.I)


def expected_segments(sentence):
    """[(surface, kana|None)] with furigana groups kept whole; the kana of
    digits and Latin letters outside furigana is unknown (None)."""
    segs = []
    for base, reading in sentence["tokens"]:
        if reading:
            segs.append((norm_text(base), norm_kana(reading)))
        else:
            for chunk in re.findall(r"\d[\d,]*|[A-Za-z][A-Za-z\-]*|.",
                                    unicodedata.normalize("NFKC", base)):
                s = norm_text(norm_numbers(chunk))
                if s:
                    known = not re.search(r"[0-9A-Za-z]", chunk)
                    segs.append((s, norm_kana(s) if known else None))
    return segs


def align_blocks(exp, got, ebounds, gbounds):
    """Character alignment as alternating equal/diff blocks [tag, i1, i2, j1, j2].
    Diff blocks are grown (consuming neighbouring equal characters on both sides
    at once) until both ends fall on furigana-group boundaries in the dictionary
    text and on analyzer-token boundaries in the transcript."""
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
                prev[2] -= m
                prev[4] -= m
                b[1] -= m
                b[3] -= m
                changed = True
            need = max(min(x for x in ebounds if x >= b[2]) - b[2],
                       min(x for x in gbounds if x >= b[4]) - b[4])
            if need and k + 1 < len(blocks):
                nxt = blocks[k + 1]
                m = min(need, nxt[2] - nxt[1])
                nxt[1] += m
                nxt[3] += m
                b[2] += m
                b[4] += m
                changed = True
    return blocks


def tokenize_kana(got):
    """Analyzer tokens of the normalized transcript: char boundaries and kana."""
    bounds, kanas, pos = [0], [], 0
    for w in tagger()(got):
        pos += len(w.surface)
        bounds.append(pos)
        kanas.append(to_kana(w.surface) if not w.feature.kana else norm_kana(w.feature.kana))
    return bounds, kanas


def check_text(sentence, text):
    """A transcript written with kanji: align it with the dictionary text; every
    differing region (widened to whole furigana groups and analyzer tokens) must
    have the same reading."""
    segs = expected_segments(sentence)
    exp = "".join(s for s, _ in segs)
    got = norm_text(norm_numbers(text))
    ebounds = [0]
    for s, _ in segs:
        ebounds.append(ebounds[-1] + len(s))
    gbounds, gkanas = tokenize_kana(got)
    blocks = align_blocks(exp, got, ebounds, gbounds)
    diffs, homophones = [], []
    for i1, i2, j1, j2 in (b[1:] for b in blocks if b[0] == "diff"):
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


# --------------------------------------------------------------------------- verdicts
def score_transcript(sentence, text):
    """Verdict of a hiragana transcription: match / mismatch / n/a (refusal)."""
    text = text or ""
    if REFUSAL.search(text):
        return {"verdict": "n/a", "heard": text[:80], "diff": []}
    if not KANJI.search(text):
        exp_kanas = [norm_kana(k) for k in [sentence["kana"], *sentence.get("alt_kana", [])]]
        got = norm_kana(latin_to_kana(norm_numbers(text)))
        best = min(exp_kanas, key=lambda k: distance(loose(k), loose(got)))
        d = distance(loose(best), loose(got))
        return {"verdict": "match" if d == 0 else "mismatch", "heard": got,
                "diff": diff_ops(best, got)}
    diffs, _homophones, _exp, got = check_text(sentence, text)
    return {"verdict": "mismatch" if diffs else "match", "heard": got,
            "diff": [["replace", e, g] for e, g, _, _ in diffs]}


def _fold_keep_particles(k):
    return loose(k.replace("は", "\0").replace("へ", "\1").replace("を", "\2"))


def score_compare(text, particles=True):
    """Verdict of a compare reply: mismatch if any reported difference survives
    normalization (particles not folded when `particles`), or if match is false
    with no differences. Unparseable → n/a."""
    fold = _fold_keep_particles if particles else loose
    got = parse_json(text)
    if not isinstance(got, dict):
        return {"verdict": "n/a", "heard": (text or "")[:80], "diff": []}
    diff = []
    for d in got.get("differences") or []:
        if not isinstance(d, dict):
            continue
        e, h = str(d.get("expected", "")), str(d.get("heard", ""))
        if fold(norm_kana(e)) != fold(norm_kana(h)):
            diff.append(["replace", e, h])
    bad = bool(diff) or (got.get("match") is False and not got.get("differences"))
    return {"verdict": "mismatch" if bad else "match", "heard": "", "diff": diff}


def score(kind, sentence, text):
    if kind == "pcompare":
        return score_compare(text, particles=True)
    if kind == "kana":
        return score_transcript(sentence, text)
    raise ValueError(kind)


def accept(rule, verdicts):
    """verdicts: list of verdict strings in checker order.

    p2: the first checker must say match, and at most one other may object.
    any: every checker must say match."""
    if rule == "p2":
        return verdicts[0] == "match" and sum(v != "match" for v in verdicts[1:]) < 2
    if rule == "any":
        return all(v == "match" for v in verdicts)
    raise ValueError(rule)


# --------------------------------------------------------------------------- network
def checker_name(c):
    return f"{c['kind']}:{c['model']}"


def run_checkers(mp3, sentence, checkers, api, tries=3):
    """Run every checker on one clip (in parallel). Returns a list of dicts
    {name, verdict, text, diff, cost}. An API failure after `tries` attempts
    gives verdict n/a."""
    prompts = {"pcompare": pcompare_prompt(sentence), "kana": KANA_PROMPT}

    def one(c):
        text, cost, err = None, 0.0, None
        for _ in range(tries):
            try:
                text, cost = api.ask_audio(c["model"], prompts[c["kind"]], mp3)
                err = None
                break
            except Exception as e:  # noqa: BLE001 (any failure → retry, then n/a)
                err = repr(e)[:200]
        if text is None:
            return {"name": checker_name(c), "verdict": "n/a", "text": "", "diff": [],
                    "cost": cost or 0.0, "error": err}
        sc = score(c["kind"], sentence, text)
        return {"name": checker_name(c), "verdict": sc["verdict"], "text": text,
                "diff": sc["diff"], "cost": cost or 0.0}

    with ThreadPoolExecutor(len(checkers)) as pool:
        return list(pool.map(one, checkers))
