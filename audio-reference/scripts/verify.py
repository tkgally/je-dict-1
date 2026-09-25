"""Targeted checks by audio-input LLMs (second round).

    python verify.py --mode choice --models google/gemini-3.8-flash --set pilot
    python verify.py --mode compare --models openai/gpt-audio-mini --set all

choice  – for every word in the sentence whose spelling has more than one
          reading (in the dictionary's furigana, or by MeCab/UniDic), the model
          hears the clip and picks the reading actually spoken from shuffled
          options, without being told which one is intended.  Verdict:
          mismatch if any pick differs from the furigana reading.  Sentences
          with no such words get no verdict.
pcompare – as compare, but particles are written as pronounced (にわ for には)
          and the model must report a particle pronounced as written ("ha").
          Added after the user's ratings found は read "ha" undetected.
compare – the model is given the intended reading in kana and lists every
          difference it hears (other reading, missing / added / repeated words,
          sentence read twice, extra speech).  Verdict: mismatch if any
          difference survives kana normalization.
Results go to data/stt/<mode>_<model>.jsonl (the answer key is stored with
each record); evaluate.py turns them into verdicts."""
import argparse
import hashlib
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

import fugashi

from common import DATA, kata2hira, log_cost, post
from transcribe import STT_DIR, audio_b64, clips, slug

tagger = fugashi.Tagger()
READINGS = json.load(open(DATA / "reading_index.json"))
HIRA = re.compile(r"^[ぁ-ゖー]+")
VOICED = str.maketrans("がぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ",
                       "かきくけこさしすせそたちつてとはひふへほはひふへほ")


def devoice(k):
    return k[:1].translate(VOICED) + k[1:]


def choice_items(s):
    """[(word, context, [(label, is_correct)])] for the sentence's ambiguous words."""
    items, toks = [], s["tokens"]
    plain = "".join(b for b, _ in toks)
    pos = 0
    for i, (base, reading) in enumerate(toks):
        start = pos
        pos += len(base)
        if not reading:
            continue
        counts = READINGS.get(base, {})
        inflected = len(base) == 1 and i + 1 < len(toks) and not toks[i + 1][1] \
            and HIRA.match(toks[i + 1][0])
        if inflected:  # 行った, 生けて: only readings common for this kanji
            alts = {r for r, c in counts.items() if c >= 0.1 * sum(counts.values())}
        else:
            alts = {r for r, c in counts.items() if c >= 2}
            alts.add("".join(kata2hira(w.feature.kana or w.surface) for w in tagger(base)))
        # drop the intended reading and its rendaku variants (さけ/ざけ)
        alts = {a for a in alts if devoice(a) != devoice(reading) and a != reading}
        if not alts:
            continue
        # attach okurigana / particle so options are pronounceable (おこなった / いった)
        tail = ""
        if i + 1 < len(toks) and not toks[i + 1][1]:
            m = HIRA.match(toks[i + 1][0])
            tail = m.group() if m else ""
        word = base + tail
        ctx = plain[max(0, start - 6): start + len(word) + 6]
        opts = [(reading + tail, True)] + [(a + tail, False) for a in sorted(alts)]
        items.append((word, ctx, opts))
    return items


def shuffled(opts, seed):
    h = lambda o: hashlib.md5((seed + o[0]).encode()).hexdigest()
    return sorted(opts, key=h)


def choice_prompt(s, key):
    items = choice_items(s)
    if not items:
        return None, None
    lines, answer = [], {}
    for n, (word, ctx, opts) in enumerate(items, 1):
        opts = shuffled(opts, key + str(n))
        letters = "abcdefgh"
        lines.append(f"{n}. {word} (in 「…{ctx}…」): " +
                     "  ".join(f"{letters[j]}) {o}" for j, (o, _) in enumerate(opts)))
        answer[str(n)] = {"correct": letters[[c for _, c in opts].index(True)],
                          "options": {letters[j]: o for j, (o, _) in enumerate(opts)}}
    prompt = (
        "You will hear a recording of this Japanese sentence:\n"
        f"「{s['plain']}」\n\n"
        "Some words in it can be pronounced in more than one way. For each numbered "
        "word below, listen carefully and say which pronunciation the speaker actually "
        "used. Judge only from the audio, not from which reading you would expect. "
        "If the speaker used none of the listed pronunciations or did not say the word, "
        "answer \"x:\" followed by what you heard in hiragana.\n\n"
        + "\n".join(lines) +
        "\n\nReply with JSON only, for example {\"1\": \"b\", \"2\": \"x:ほげ\"}.")
    return prompt, answer


def compare_prompt(s):
    kana = " / ".join([s["kana"], *s["alt_kana"]])
    return (
        "You will hear a recording of a Japanese sentence. The intended reading, in kana, is:\n"
        f"{kana}\n"
        + ("(Alternatives separated by / are all acceptable.)\n" if s["alt_kana"] else "")
        + "\nListen carefully and check whether the speaker said exactly this. Report every "
        "difference: a word pronounced differently (for example a different reading of a "
        "kanji), a word missing, added or repeated, the sentence read twice, or any extra "
        "speech such as English words or instructions. Ignore intonation, pitch accent, "
        "speed and voice quality, and ignore the spelling differences は/わ, へ/え, を/お "
        "and long vowels.\n\n"
        "Reply with JSON only: {\"differences\": [{\"expected\": \"…\", \"heard\": \"…\"}], "
        "\"match\": true or false}")


PARTICLE_SOUND = {"は": "わ", "へ": "え", "を": "お"}


def phonetic_kana(s):
    """The furigana reading with the particles は/へ/を written as pronounced
    (わ/え/お).  Particles are found by MeCab in the displayed sentence; they
    never carry furigana, so they map one-to-one onto the reading.  For the
    sentences whose reading was supplied by hand (digits, Latin letters) the
    particles are located in the reading in the same order."""
    plain = "".join(b for b, _ in s["tokens"])
    ppos, pos = set(), 0
    for w in tagger(plain):
        start = plain.index(w.surface, pos)
        pos = start + len(w.surface)
        if w.feature.pos1 == "助詞" and w.surface in PARTICLE_SOUND:
            ppos.add(start)
    if s.get("manual_reading"):
        # estimate where each particle falls in the hand-written reading from
        # the length of the reading of the text before it, and take the
        # nearest occurrence of the particle there (not the は of しゅくはく)
        from evaluate import to_kana
        kana = s["kana"]
        for j in sorted(ppos):
            ch, est = plain[j], len(to_kana(plain[:j]))
            hits = [k for k, c in enumerate(kana) if c == ch]
            if hits:
                k = min(hits, key=lambda k: abs(k - est))
                kana = kana[:k] + PARTICLE_SOUND[ch] + kana[k + 1:]
        return kana
    out, pos = "", 0
    for base, reading in s["tokens"]:
        if reading:
            out += reading
        else:
            out += "".join(PARTICLE_SOUND[c] if pos + i in ppos else c for i, c in enumerate(base))
        pos += len(base)
    return out


def pcompare_prompt(s):
    return (
        "You will hear a recording of a Japanese sentence. The intended pronunciation, in kana, is:\n"
        f"{phonetic_kana(s)}\n"
        "(Particles are written as they are pronounced: わ for the topic particle は, え for へ, お for を.)\n\n"
        "Listen carefully and check whether the speaker said exactly this. Report every difference: a word "
        "pronounced differently (for example a different reading of a kanji), a particle pronounced as written "
        "instead of as spoken (for example the particle は pronounced \"ha\" instead of \"wa\"), a word missing, "
        "added or repeated, the sentence read twice, or any extra speech. Ignore intonation, pitch accent, "
        "speed, voice quality, and long-vowel spelling.\n\n"
        "Reply with JSON only: {\"differences\": [{\"expected\": \"…\", \"heard\": \"…\"}], "
        "\"match\": true or false}")


def ask(model, prompt, b64):
    r = post("/chat/completions", {
        "model": model, "temperature": 0, "reasoning": {"effort": "low"},
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": prompt},
            {"type": "input_audio", "input_audio": {"data": b64, "format": "mp3"}}]}]})
    d = r.json()
    if "choices" not in d:
        raise RuntimeError(str(d)[:300])
    return (d["choices"][0]["message"].get("content") or "").strip(), d.get("usage", {}).get("cost")


def run_one(mode, model, key, s, phase):
    rec = {"key": key, "model": f"{mode}:{model}"}
    if mode == "choice":
        prompt, answer = choice_prompt(s, key)
        if not prompt:
            rec["text"], rec["answer"] = "", None
            return rec
        rec["answer"] = answer
    elif mode == "pcompare":
        prompt = pcompare_prompt(s)
    else:
        prompt = compare_prompt(s)
    try:
        b, _ = audio_b64(key, model)
        rec["text"], rec["cost"] = ask(model, prompt, b)
        log_cost(phase, model, rec["cost"], key=key, mode=mode)
    except Exception as e:
        rec["error"] = repr(e)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["choice", "compare", "pcompare"], required=True)
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--set", default="all", choices=["all", "pilot", "round2"])
    ap.add_argument("--keys", help="file with one clip key per line (overrides --set)")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--phase", default="verify-pilot")
    args = ap.parse_args()
    sentences = {s["n"]: s for s in json.load(open(DATA / "sentences.json"))}
    manifest = {}
    for line in open(DATA / "tts_manifest.jsonl"):
        r = json.loads(line)
        if not r.get("error"):
            manifest[r["key"]] = r
    keys = [l.strip() for l in open(args.keys)] if args.keys else clips(args.set)
    for model in args.models:
        path = STT_DIR / f"{args.mode}_{slug(model)}.jsonl"
        done = {json.loads(l)["key"] for l in open(path)} if path.exists() else set()
        todo = [k for k in keys if k not in done]
        print(f"{args.mode}:{model}: {len(todo)} of {len(keys)} clips")
        errs = 0
        with ThreadPoolExecutor(args.workers) as pool, open(path, "a") as f:
            futs = [pool.submit(run_one, args.mode, model, k, sentences[manifest[k]["n"]], args.phase)
                    for k in todo]
            for fut in as_completed(futs):
                rec = fut.result()
                if rec.get("error"):
                    errs += 1
                    if errs <= 3:
                        print("  ERROR", rec["key"], rec["error"][:200])
                    continue
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                f.flush()
        print(f"  done, {errs} errors")


if __name__ == "__main__":
    main()
