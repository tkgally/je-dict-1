#!/usr/bin/env python3
"""Double-check the conjugation tables of verb and i-adjective entries.

The tables were written by build/add_conjugations.py and
build/add_adjective_conjugations.py from each entry's POS tag and reading, so a
wrong tag or a gap in the generators' rules gives a wrong table (乞う was
shown as 乞った, not 乞うた; ついていく as ついていいた; 見返る as an ichidan
verb). This tool looks for such errors from several independent directions:

  missing     a verb or i-adjective entry with no table
  generator   the stored table disagrees with what the (corrected) generators
              produce now: a stale table, or a hand edit to review
  class       SudachiPy's conjugation class for the headword disagrees with the
              table's class (godan row / ichidan / kuru / zuru / adjective)
  example     an example sentence or the notes use a た/て form of the headword
              that the table does not give (乞うた in the examples, 乞った in the
              table)
  model       an independent model, shown the table, says a form is wrong
              (--llm; paid, budgeted, reads a cursor so successive runs cover
              the whole dictionary; a table it has checked is skipped until it
              changes, polishing/tasks/conjugation-check/model_checked.json)

A flag stays open until the table changes (its hash then differs) or a decision
line in reviews/conjugation_decisions.jsonl marks the current table as checked
(`--verify`). The Routine runs this as the `conjugation-check` mode
(prompts/routine2.md §D).

Usage:
    python3 build/check_conjugations.py                      # deterministic checks, open flags
    python3 build/check_conjugations.py --ids 28921,02299    # only these entries
    python3 build/check_conjugations.py --json out.json      # also write the open flags as JSON
    python3 build/check_conjugations.py --llm --n 1000 --budget 0.30   # model check from the cursor
    python3 build/check_conjugations.py --regenerate --ids 28921       # rewrite tables from the generators
    python3 build/check_conjugations.py --verify 28921 --note "table correct; 乞うた is standard"
"""
import argparse
import glob
import hashlib
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from japanese_utils import strip_furigana  # noqa: E402
from add_conjugations import generate_conjugation, NO_TABLE_IDS  # noqa: E402
from add_adjective_conjugations import generate_adjective_conjugation  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DECISIONS = ROOT / "reviews" / "conjugation_decisions.jsonl"
MODEL_FLAGS = ROOT / "reviews" / "conjugation_flags.jsonl"
CURSOR = ROOT / "polishing" / "tasks" / "conjugation-check" / "progress.txt"
# entry id → hash of the table the model last checked; the model pass skips a
# table whose hash is here, so after one full pass it sees only new and changed tables
CHECKED = ROOT / "polishing" / "tasks" / "conjugation-check" / "model_checked.json"

VERB_POS = {"verb-godan", "verb-ichidan", "verb-suru", "verb-kuru", "verb-irregular"}
# Chosen 2026-09-30 on the tables this tool was built to catch (乞う, ついていく,
# ふける, 見返る, あざとかわいい, くれる) plus correct look-alikes (混じる, 過る, 好く,
# 愛する): gpt-6.1-sol found every error with no false flag; gemini-3.8-flash
# missed ふける and 読みふける; gemini-2.5-flash called 過る, ふける and 好く wrong
# the other way round.
DEFAULT_MODEL = "openai/gpt-6.1-sol"
# USD per 1K tokens (input, output), for the budget estimate
MODEL_COSTS = {"google/gemini-3.8-flash": (0.00075, 0.00375),
               "google/gemini-2.5-flash": (0.00015, 0.0006),
               "openai/gpt-6.1-sol": (0.002, 0.01)}
BATCH = 25

LINK_RE = re.compile(r"⟦([^→⟧]*)→[^⟧]*⟧")
GODAN_ROW = {"う": "ワア", "く": "カ", "ぐ": "ガ", "す": "サ", "つ": "タ",
             "ぬ": "ナ", "ぶ": "バ", "む": "マ", "る": "ラ"}
# The た/て endings a verb with this dictionary ending could show in a sentence,
# right or wrong (longest first: the regex takes the first alternative that
# matches). Bare た/て only for る-verbs, where they mark an ichidan verb.
TE_TA = {"う": ("うた", "うて", "った", "って"), "く": ("いた", "いて", "った", "って"),
         "ぐ": ("いだ", "いで"), "す": ("した", "して"), "つ": ("った", "って"),
         "ぬ": ("んだ", "んで"), "ぶ": ("んだ", "んで"), "む": ("んだ", "んで"),
         "る": ("った", "って", "た", "て")}
KANJI = r"[\u4e00-\u9fff々]"


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def plain(text):
    """Entry markup → plain Japanese: links → surface, furigana → kanji."""
    if not text:
        return text
    return strip_furigana(LINK_RE.sub(r"\1", text))


def table_hash(conj):
    return hashlib.sha256(json.dumps(conj, ensure_ascii=False, sort_keys=True)
                          .encode("utf-8")).hexdigest()[:12]


def load_entries(ids=None):
    want = {i.zfill(5) for i in ids} if ids else None
    out = []
    for f in sorted(glob.glob(str(ROOT / "entries" / "*" / "*.json"))):
        if want is not None and Path(f).name[:5] not in want:
            continue
        e = json.loads(Path(f).read_text(encoding="utf-8"))
        out.append((f, e))
    return out


def is_target(e):
    pos = set(e.get("metadata", {}).get("tags", {}).get("pos", []))
    return bool(pos & VERB_POS) or "adjective-i" in pos


def expected_table(e):
    return generate_adjective_conjugation(e) or generate_conjugation(e)


def forms_plain(conj):
    return {f["label"]: (plain(f["affirmative"]), plain(f.get("negative")))
            for f in (conj or {}).get("forms", [])}


# --------------------------------------------------------------------------- #
# Deterministic checks
# --------------------------------------------------------------------------- #
def check_generator(e, conj):
    """Stored table vs the generators, compared as plain text, on shared labels.

    Headwords listing variants (易しい／優しい) are skipped: the generators do not
    handle them, and their tables were written by hand.
    """
    if "／" in e.get("headword", "") or "/" in e.get("headword", ""):
        return []
    new = expected_table(e)
    if conj and not new:
        if e.get("id") in NO_TABLE_IDS:
            return [("generator", "the entry is listed in NO_TABLE_IDS but has a table")]
        return [("generator", "the generators produce no table for this entry")]
    if not conj:
        return []
    msgs = []
    if new["type"] != conj.get("type"):
        msgs.append(("generator", f"type {conj.get('type')} but the generators say {new['type']}"))
    cur, exp = forms_plain(conj), forms_plain(new)
    rows = []
    for label, val in cur.items():
        if label not in exp:
            rows.append(f"{label}: row the generators do not produce")
        elif val != exp[label]:
            rows.append(f"{label}: {val[0]} / {val[1]} — generators give "
                        f"{exp[label][0]} / {exp[label][1]}")
    if rows:
        more = f" (+{len(rows) - 3} more rows)" if len(rows) > 3 else ""
        msgs.append(("generator", "; ".join(rows[:3]) + more))
    return msgs


_TOKENIZER = None


def tokenizer():
    """SudachiPy tokenizer, or False when SudachiPy is not installed."""
    global _TOKENIZER
    if _TOKENIZER is None:
        try:
            from sudachipy import dictionary, tokenizer as tk
            _TOKENIZER = (dictionary.Dictionary().tokenizer(), tk.Tokenizer.SplitMode.C)
        except Exception:  # pragma: no cover - environment dependent
            _TOKENIZER = False
    return _TOKENIZER


def class_agrees(ctype, pos0, conj_type, ending):
    """Does Sudachi's conjugation class agree with the table's type?"""
    if conj_type == "godan":
        m = re.match(r"(?:文語)?(?:五段|四段)-(.+?)行", ctype)
        return bool(m) and m.group(1) in GODAN_ROW.get(ending, m.group(1))
    if conj_type == "ichidan":
        return "一段" in ctype
    if conj_type == "kuru":
        return "カ行変格" in ctype
    if conj_type == "zuru":
        return "サ行変格" in ctype or "上一段-ザ行" in ctype
    if conj_type in ("i-adjective", "ii"):
        return pos0 == "形容詞"
    return True


def check_class(e, conj):
    """SudachiPy's class for the headword's last word vs the table type.

    Only a confident disagreement is a flag: the last token must be a verb or
    an adjective in Sudachi's analysis (slang and passive headwords that it
    reads as a noun or an auxiliary are not second-guessed).
    """
    t = tokenizer()
    if not t or not conj or conj.get("type") in ("suru", "aru"):
        return []
    hw = plain(e.get("headword", "")).split("／")[0]
    if not hw:
        return []
    last = t[0].tokenize(hw, t[1])[-1]
    pos = last.part_of_speech()
    if pos[0] not in ("動詞", "形容詞"):
        return []
    ending = e.get("reading", "")[-1:]
    if class_agrees(pos[4], pos[0], conj["type"], ending):
        return []
    return [("class", f"table type {conj['type']}, but SudachiPy reads {last.surface()} "
                      f"as {pos[0]} {pos[4]}")]


def check_examples(e, conj):
    """た/て forms of the headword in the examples or notes that the table lacks.

    A match must start at a word boundary (no kanji just before the stem, so
    優勝した is not read as a form of 勝つ), and a た followed by い, め, く, か or
    け is skipped (買いたい, 補うため are not past forms).
    """
    if not conj or conj.get("type") not in ("godan", "ichidan"):
        return []
    hw = plain(e.get("headword", ""))
    if "／" in hw or len(hw) < 2:
        return []
    stem, ending = hw[:-1], hw[-1]
    if ending not in TE_TA or (len(stem) < 2 and not re.search(KANJI, stem)):
        return []  # a one-kana stem matches everywhere
    fm = forms_plain(conj)
    if "Past" not in fm:
        return []
    have = set()
    for label in ("Past", "て form"):
        aff = (fm.get(label) or (None,))[0]
        if aff and aff.startswith(stem):
            have.add(aff[len(stem):])
    if not have:
        return []
    texts = [plain(x.get("japanese", "")) for x in e.get("examples", [])]
    # "(not 問った, 問って)" in the notes names the wrong forms on purpose
    texts.append(re.sub(r"\(not [^)]*\)", "", plain(e.get("notes", ""))))
    alts = [f"{x}(?![いめくかけ])" if x.endswith(("た", "だ")) else x for x in TE_TA[ending]]
    pattern = re.compile(f"(?<!{KANJI})" + re.escape(stem) + "(" + "|".join(alts) + ")")
    seen = set()
    for text in texts:
        for m in pattern.finditer(text or ""):
            seen.add(m.group(1))
    odd = sorted(s for s in seen if s not in have)
    if not odd:
        return []
    return [("example", f"the examples or notes use {', '.join(stem + s for s in odd)}; "
                        f"the table gives {', '.join(sorted(stem + h for h in have))}")]


def load_decisions():
    ok = {}
    if DECISIONS.exists():
        for line in DECISIONS.read_text(encoding="utf-8").splitlines():
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if d.get("decision") == "ok":
                ok.setdefault(d.get("entry"), set()).add(d.get("hash"))
    return ok


def load_model_flags():
    flags = {}
    if MODEL_FLAGS.exists():
        for line in MODEL_FLAGS.read_text(encoding="utf-8").splitlines():
            try:
                d = json.loads(line)
            except ValueError:
                continue
            flags.setdefault(d.get("entry"), []).append(d)
    return flags


def run_checks(entries, use_sudachi=True):
    ok = load_decisions()
    model_flags = load_model_flags()
    open_flags = []
    for f, e in entries:
        if not is_target(e):
            continue
        eid = e["id"]
        conj = e.get("conjugation")
        found = []
        if not conj and eid not in NO_TABLE_IDS and expected_table(e) is not None:
            found.append(("missing", "no conjugation table; the generators can write one"))
        elif not conj and eid not in NO_TABLE_IDS:
            found.append(("missing", "no conjugation table, and the generators cannot write one"))
        found += check_generator(e, conj)
        if use_sudachi:
            found += check_class(e, conj)
        found += check_examples(e, conj)
        h = table_hash(conj) if conj else None
        for mf in model_flags.get(eid, []):
            if mf.get("hash") == h:
                found.append(("model", f"{mf.get('label')}: {mf.get('given')} → {mf.get('correct')} "
                                       f"({mf.get('reason', '')})"))
        if found and h in ok.get(eid, set()):
            continue
        for kind, msg in found:
            open_flags.append({"entry": eid, "file": str(Path(f).relative_to(ROOT)),
                               "headword": plain(e.get("headword", "")), "hash": h,
                               "kind": kind, "message": msg})
    return open_flags


# --------------------------------------------------------------------------- #
# Model check
# --------------------------------------------------------------------------- #
def build_prompt(batch):
    parts = []
    for e in batch:
        rows = "\n".join(
            f"  {f['label']}: {plain(f['affirmative'])}"
            + (f" / {plain(f['negative'])}" if f.get("negative") else "")
            for f in e["conjugation"]["forms"])
        gloss = e.get("gloss") or "; ".join(d.get("gloss", "") for d in e.get("definitions", [])[:2])
        parts.append(f"[{e['id']}] {plain(e['headword'])} ({e['reading']}) — {gloss}\n{rows}")
    body = "\n\n".join(parts)
    return f"""You are checking conjugation tables in a Japanese-English learner's dictionary.
Each table lists "label: affirmative / negative" for one verb or i-adjective. Find forms that are
morphologically WRONG in modern standard Japanese: wrong verb class (godan vs ichidan), wrong
sound change in the た/て forms (e.g. 行く → 行った; 問う, 乞う, 請う → 問うた, 乞うた, 請うた),
wrong irregular forms (来る, する, ある, いい → よかった, くれる → imperative くれ), a form that
does not exist, or a form of a different word.

Do NOT flag: kana/kanji spelling choices; forms that are grammatical but rare or semantically
odd (a passive of an intransitive verb, an imperative of a stative verb); plain imperatives such
as 食べろ; potential forms without ら-omission; a table row missing; label wording.
Flag only what you are confident is wrong. Most tables are correct.

Return ONLY a JSON array (empty if nothing is wrong), one object per wrong form:
[{{"id": "28921_kou", "label": "Past", "field": "affirmative", "given": "乞った",
   "correct": "乞うた", "reason": "乞う keeps う in the た form"}}]

Tables:

{body}
"""


def regular_suru(e):
    """A する verb whose stem is two or more characters (勉強する): its table is
    fully regular, so a model check of it is the least likely to find anything."""
    if e["conjugation"].get("type") != "suru":
        return False
    first = plain(e["conjugation"]["forms"][0]["affirmative"])
    return len(first) - 2 >= 2


def model_check(batch, api_key, model):
    """One call. Returns (flags or None on failure, billed USD or None)."""
    import time
    from review_runner import call_openrouter, parse_model_response
    for wait in (20, 60, 120, None):
        resp = call_openrouter(api_key, model, build_prompt(batch), timeout=300, max_tokens=32000)
        # an upstream rate limit comes back as HTTP 200 with an error body
        if wait and resp and (resp.get("error") or {}).get("code") == 429:
            time.sleep(wait)
            continue
        break
    cost = None
    try:
        cost = float(resp["usage"]["cost"])
    except (TypeError, KeyError, ValueError):
        pass
    if resp and not (resp.get("choices") or [{}])[0].get("message", {}).get("content"):
        ch = (resp.get("choices") or [{}])[0]
        print(f"  empty reply: finish_reason={ch.get('finish_reason')} "
              f"error={resp.get('error')}", file=sys.stderr)
    parsed = parse_model_response(resp)
    return (parsed if isinstance(parsed, list) else None), cost


def load_checked():
    try:
        return json.loads(CHECKED.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_checked(checked):
    CHECKED.parent.mkdir(parents=True, exist_ok=True)
    CHECKED.write_text(json.dumps(dict(sorted(checked.items())), ensure_ascii=False, indent=0)
                       + "\n", encoding="utf-8")


def read_cursor():
    try:
        for line in CURSOR.read_text(encoding="utf-8").splitlines():
            if line.startswith("next:"):
                return line.split(":", 1)[1].strip().zfill(5)
    except OSError:
        pass
    return "00001"


def write_cursor(nxt, note):
    CURSOR.parent.mkdir(parents=True, exist_ok=True)
    CURSOR.write_text(f"next: {nxt}\nlast: {now_iso()} {note}\n", encoding="utf-8")


def run_llm(args):
    from review_runner import rough_token_count, get_api_key

    def estimate_cost(model, tokens_in, tokens_out):
        cin, cout = MODEL_COSTS.get(model, (0.002, 0.01))
        return tokens_in / 1000 * cin + tokens_out / 1000 * cout
    api_key = get_api_key()
    if not api_key:
        print("OPENROUTER_API_KEY not set; model check skipped")
        return 1
    if args.ids:
        pool = [e for _, e in load_entries(args.ids.split(",")) if e.get("conjugation")]
        start = None
    else:
        start = read_cursor()
        checked = load_checked()
        allt = [e for _, e in load_entries() if e.get("conjugation")
                and not (args.skip_regular_suru and regular_suru(e))
                and checked.get(e["id"]) != table_hash(e["conjugation"])]
        pool = [e for e in allt if e["id"][:5] >= start][:args.n]
        if len(pool) < args.n:  # wrap to the start of the dictionary
            pool += [e for e in allt if e["id"][:5] < start][:args.n - len(pool)]
    batches = [pool[i:i + BATCH] for i in range(0, len(pool), BATCH)]
    est_each = [estimate_cost(args.model, rough_token_count(build_prompt(b)) * 2, 600)
                for b in batches]
    keep, spent, cost = [], 0.0, {}
    for b, c in zip(batches, est_each):
        if spent + c > args.budget:
            break
        keep.append(b)
        cost[id(b)] = c
        spent += c
    print(f"model check: {sum(len(b) for b in keep)} tables in {len(keep)} calls, "
          f"est ${spent:.3f} ({args.model})")
    if args.dry_run:
        return 0
    n_flags, by_id = 0, {}

    def record(b, res):
        """Append one batch's flags as soon as it returns."""
        nonlocal n_flags
        ids = {e["id"]: e for e in b}
        with MODEL_FLAGS.open("a", encoding="utf-8") as out:
            for r in res:
                e = ids.get(str(r.get("id", "")))
                if not e:
                    continue
                rec = {"ts": now_iso(), "entry": e["id"], "hash": table_hash(e["conjugation"]),
                       "model": args.model, "label": r.get("label"), "field": r.get("field"),
                       "given": r.get("given"), "correct": r.get("correct"),
                       "reason": r.get("reason")}
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                by_id.setdefault(e["id"], []).append(rec)
                n_flags += 1

    results, billed = [], 0.0
    todo = keep
    for attempt in (1, 2):  # a failed call (empty reply, timeout) is retried once
        with ThreadPoolExecutor(max_workers=3) as ex:
            futures = [(b, ex.submit(model_check, b, api_key, args.model)) for b in todo]
            for b, fut in futures:
                res, usd = fut.result()
                billed += usd if usd is not None else cost[id(b)]
                if res is not None:
                    record(b, res)
                    results.append((b, res))
        done = {id(b) for b, _ in results}
        todo = [b for b in keep if id(b) not in done]
        if not todo:
            break
    spent = billed  # OpenRouter's billed cost (the estimate where a reply lacked it)
    failed = len(todo)
    if todo:
        print("unchecked after a retry (rerun with --ids): "
              + ",".join(e["id"][:5] for b in todo for e in b))
    covered = [e for b, res in results if res is not None for e in b]
    checked = load_checked()
    for e in covered:
        checked[e["id"]] = table_hash(e["conjugation"])
    save_checked(checked)
    print(f"model flags: {n_flags} on {len(by_id)} entries; failed calls: {failed}")
    for eid, recs in by_id.items():
        for r in recs:
            print(f"  {eid} {r['label']}: {r['given']} → {r['correct']} ({r['reason']})")
    if start is not None:
        last = keep[-1][-1]["id"][:5] if keep else start
        allt_ids = sorted(e["id"][:5] for _, e in load_entries() if e.get("conjugation"))
        later = [i for i in allt_ids if i > last]
        write_cursor(later[0] if later else "00001",
                     f"{len(covered)} tables checked, {n_flags} flags, ${spent:.3f}")
    print(f"EST_COST={spent:.4f}")
    return 0


# --------------------------------------------------------------------------- #
# Regenerate and verify
# --------------------------------------------------------------------------- #
def regenerate(ids):
    for f, e in load_entries(ids):
        new = expected_table(e)
        old = e.get("conjugation")
        if new == old:
            print(f"{e['id']}: unchanged")
            continue
        if new is None:
            e.pop("conjugation", None)
        else:
            e["conjugation"] = new
        Path(f).write_text(json.dumps(e, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{e['id']}: table {'removed' if new is None else 'rewritten'}")


def verify(eid, note):
    entries = load_entries([eid])
    if not entries:
        print(f"no entry {eid}")
        return 1
    _, e = entries[0]
    conj = e.get("conjugation")
    rec = {"ts": now_iso(), "entry": e["id"], "hash": table_hash(conj) if conj else None,
           "decision": "ok", "by": "claude", "note": note}
    with DECISIONS.open("a", encoding="utf-8") as out:
        out.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"{e['id']}: current table recorded as checked")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ids", help="comma-separated entry IDs (5-digit)")
    ap.add_argument("--json", metavar="OUT", help="write the open flags to this JSON file")
    ap.add_argument("--no-sudachi", action="store_true", help="skip the SudachiPy class check")
    ap.add_argument("--llm", action="store_true", help="independent model check (paid)")
    ap.add_argument("--n", type=int, default=1000, help="tables per model check (from the cursor)")
    ap.add_argument("--budget", type=float, default=0.30, help="USD cap for --llm (estimated)")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--skip-regular-suru", action="store_true",
                    help="--llm: leave out する verbs with a stem of two or more characters")
    ap.add_argument("--dry-run", action="store_true", help="--llm: estimate only")
    ap.add_argument("--regenerate", action="store_true", help="rewrite --ids tables from the generators")
    ap.add_argument("--verify", metavar="ID", help="record the entry's current table as checked")
    ap.add_argument("--note", default="", help="note for --verify (ten words or fewer)")
    args = ap.parse_args()

    if args.verify:
        return verify(args.verify, args.note)
    if args.regenerate:
        if not args.ids:
            ap.error("--regenerate needs --ids")
        regenerate(args.ids.split(","))
        return 0
    if args.llm:
        return run_llm(args)

    entries = load_entries(args.ids.split(",") if args.ids else None)
    flags = run_checks(entries, use_sudachi=not args.no_sudachi)
    if not args.no_sudachi and not tokenizer():
        print("note: SudachiPy unavailable; class check skipped "
              "(python3 -m pip install -r build/requirements.txt)")
    by_kind = {}
    for fl in flags:
        by_kind[fl["kind"]] = by_kind.get(fl["kind"], 0) + 1
        print(f"{fl['entry']} {fl['headword']} [{fl['kind']}] {fl['message']}")
    n_entries = len({fl["entry"] for fl in flags})
    print(f"\n{len(flags)} open flag(s) on {n_entries} entr{'y' if n_entries == 1 else 'ies'}"
          + (f": {', '.join(f'{k} {v}' for k, v in sorted(by_kind.items()))}" if flags else ""))
    if args.json:
        Path(args.json).write_text(json.dumps(flags, ensure_ascii=False, indent=2) + "\n",
                                   encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
