#!/usr/bin/env python3
"""Brainstorm new candidate words from the dictionary's own headwords.

The `candidates` mode (prompts/newcandidates.md) has two streams: internal
closure (words the dictionary already uses but does not define) and this one,
which asks what words SHOULD be in the dictionary and are not. Proposals come
from the Routine's own model and from independent models on OpenRouter, all
from their own knowledge of Japanese: never from an existing dictionary or
word list (Tom's rule). Every proposal is checked against the dictionary here
and then vetted by hand against the find-candidates gates before it is added.

Two lenses, alternating run by run:

  seeds   the next ~20 headwords in tier order (basic, core, general; by ID).
          For each: synonyms, antonyms, words of the same kind, broader and
          narrower words, lexicalized compounds and set phrases built on it,
          register counterparts, closely tied proper names.
  field   one semantic field (food, weather, place-name, …) with the words the
          dictionary already has in it: the common words still missing.

    python3 build/brainstorm_candidates.py next > /tmp/bs_batch.json           # the next batch (writes nothing)
    python3 build/brainstorm_candidates.py ask /tmp/bs_batch.json --out /tmp/bs_models.json --budget 0.40
    python3 build/brainstorm_candidates.py filter /tmp/bs_own.json /tmp/bs_models.json --out /tmp/bs_new.json
    python3 build/brainstorm_candidates.py record /tmp/bs_batch.json /tmp/bs_verdicts.json   # ledger + cursor

`filter` merges proposal files (lists of {word, reading, gloss, relation,
seed_id, usefulness}), drops what already exists as an entry, a candidate or a
retired id, drops what an earlier run rejected, and flags a probable variant
spelling of an existing entry (same reading, sharing a kanji or kana-only).
`record` appends the verdicts ([{word, reading, verdict: added|rejected,
reason}]) to polishing/tasks/brainstorm/ledger.jsonl and advances the lens's
cursor past the batch, so a cycle that never records serves the same batch
again.
"""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "build"))

ENTRIES_INDEX = ROOT / "entries_index.json"
CANDIDATES = ROOT / "candidate_words.json"
RETIRED = ROOT / "build" / "data" / "retired_entries.json"
TASK_DIR = ROOT / "polishing" / "tasks" / "brainstorm"
STATE = TASK_DIR / "state.json"
LEDGER = TASK_DIR / "ledger.jsonl"
SPEND_LEDGER = ROOT / "pipeline" / "openrouter-ledger.json"

DEFAULT_MODELS = ["openai/gpt-6.1-sol", "google/gemini-3.8-flash"]
# USD per million tokens (input, output), for the budget stop when a response
# carries no billed cost
PRICES = {"openai/gpt-6.1-sol": (2.0, 10.0), "google/gemini-3.8-flash": (0.83, 4.12)}
TIER_ORDER = {"basic": 0, "core": 1, "general": 2}
SEED_BATCH = 20
FIELD_SHOWN = 700
# Fields too vague to brainstorm from (they hold everything)
SKIP_FIELDS = {"general", "proper-noun", "abstract", "action", "descriptive", "existence",
               "change", "expression", "evaluation", "grammatical", "quantity"}

FURI = re.compile(r"\{([^|}]+)\|[^}]+\}")
LINK = re.compile(r"⟦([^→⟧]*)→[^⟧]*⟧")
KANJI = re.compile(r"[一-鿿々]")


def plain(s):
    return FURI.sub(r"\1", LINK.sub(r"\1", s or ""))


def bare(s):
    """Headword without the affix tilde (〜感, 小〜), for matching proposals."""
    return re.sub(r"^[〜～]|[〜～]$", "", s)


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_json(path, default):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def load_entries():
    out = []
    for e in load_json(ENTRIES_INDEX, {}).get("entries", []):
        out.append({"id": e["id"], "headword": plain(e.get("headword", "")),
                    "reading": e.get("reading", ""), "gloss": e.get("gloss", ""),
                    "tier": e.get("vocabulary_tier", "general")})
    return out


def semantic_tags(entry_id):
    path = ROOT / "entries" / f"{int(entry_id[:5]) // 500 * 500:05d}" / f"{entry_id}.json"
    d = load_json(path, {})
    return (d.get("metadata") or {}).get("tags", {}).get("semantic", []) or []


def load_state():
    st = load_json(STATE, {})
    st.setdefault("seed_cursor", 0)
    st.setdefault("field_cursor", 0)
    st.setdefault("next_lens", "seeds")
    return st


def field_list():
    import validate_tags
    return sorted(f for f in validate_tags.VALID_SEMANTIC if f not in SKIP_FIELDS)


# --------------------------------------------------------------------------- next
def seed_order(entries):
    return sorted(entries, key=lambda e: (TIER_ORDER.get(e["tier"], 2), e["id"]))


def cmd_next(args):
    st = load_state()
    lens = args.lens or st["next_lens"]
    entries = load_entries()
    if lens == "seeds":
        order = seed_order(entries)
        start = st["seed_cursor"] % len(order)
        seeds = order[start:start + args.n]
        for s in seeds:
            s["semantic"] = semantic_tags(s["id"])
        batch = {"lens": "seeds", "cursor_start": start, "cursor_end": start + len(seeds),
                 "seeds": seeds}
    else:
        fields = field_list()
        idx = st["field_cursor"] % len(fields)
        field = fields[idx]
        members = [e for e in seed_order(entries) if field in semantic_tags(e["id"])]
        batch = {"lens": "field", "field": field, "cursor_start": idx, "cursor_end": idx + 1,
                 "members_total": len(members),
                 "members": [f"{e['headword']}({e['reading']})" for e in members[:FIELD_SHOWN]]}
    print(json.dumps(batch, ensure_ascii=False, indent=1))
    return 0


# --------------------------------------------------------------------------- ask
RULES = """Rules for every word you propose:
- A real, established Japanese word or set phrase that you could use naturally in several sentences. If you are not sure it exists with this form and meaning, leave it out.
- Dictionary (lemma) form. No inflected forms, no free phrases (noun+の+noun, adjective+noun), no number+counter strings, no coinages.
- Useful to an intermediate learner who reads kana and is building vocabulary: everyday, school, news, work and cultural vocabulary. No archaic, dialect, vulgar, discriminatory or narrowly technical words, no ephemeral slang, no living celebrities or active politicians.
- Proper names are welcome when they carry cultural weight beyond pointing at something (甲子園, 関ヶ原, 源氏物語, 山手線, お盆-type events).
- Work from your own knowledge of Japanese. Do not copy from any dictionary or word list.
- reading in hiragana (katakana words too: コンビニ → こんびに).
- usefulness: 3 = common everyday/news word every learner meets, 2 = common in reading, 1 = useful but less frequent.

Reply with a JSON array only, no prose:
[{"word": "…", "reading": "…", "gloss": "short English gloss", "relation": "…", "seed_id": "…", "usefulness": 3}]"""


def prompt_for(batch, per_seed):
    if batch["lens"] == "seeds":
        lines = [f'{s["id"]}  {s["headword"]} ({s["reading"]}): {s["gloss"]}'
                 + (f'  [{", ".join(s["semantic"])}]' if s.get("semantic") else "")
                 for s in batch["seeds"]]
        return (
            "You are helping build a Japanese-English learner's dictionary of about 32,000 entries. "
            "Below are headwords it already has. For each one, think of related words that a good "
            "learner's dictionary should also contain: synonyms and near-synonyms, antonyms and "
            "opposites, other members of the same category, broader and narrower terms, established "
            "compounds and set phrases or idioms built on the word, formal/casual/honorific/humble "
            "counterparts, and culturally important proper names closely tied to it. Many of your "
            f"ideas will already be in the dictionary; that is fine. Up to {per_seed} words per "
            "headword; fewer is better than weak ones. Set relation to one of: synonym, antonym, "
            "same-category, broader, narrower, compound, set-phrase, idiom, register, proper-name; "
            "set seed_id to the headword's ID.\n\nHeadwords:\n" + "\n".join(lines) + "\n\n" + RULES)
    shown = "、".join(batch["members"])
    more = batch["members_total"] - len(batch["members"])
    return (
        "You are helping build a Japanese-English learner's dictionary of about 32,000 entries. "
        f'Its entries tagged with the semantic field "{batch["field"]}" are listed below'
        + (f" (the first {len(batch['members'])}; {more} more exist)" if more > 0 else "")
        + ". List up to 50 words or set phrases in this field that a learner's dictionary should "
        "contain and that are NOT in the list: the gaps a learner would notice first. Set relation "
        f'to "field:{batch["field"]}" and seed_id to "".\n\nAlready in the dictionary:\n{shown}\n\n'
        + RULES)


def call_model(api_key, model, prompt):
    from review_runner import call_openrouter, extract_message_text, strip_code_fences
    resp = call_openrouter(api_key, model, prompt, timeout=240, max_tokens=24000)
    if not resp:
        return None, 0.0
    usage = resp.get("usage") or {}
    cost = usage.get("cost")
    if cost is None:
        pin, pout = PRICES.get(model, (2.0, 10.0))
        cost = (usage.get("prompt_tokens", 0) * pin + usage.get("completion_tokens", 0) * pout) / 1e6
    text = extract_message_text(resp) or ""
    text = strip_code_fences(text)
    m = re.search(r"\[.*\]", text, re.DOTALL)
    try:
        items = json.loads(m.group()) if m else None
    except ValueError:
        items = None
    return items, float(cost)


def record_spend(usd, n):
    """Add this spend to the Routine's daily OpenRouter ledger (mode candidates)."""
    try:
        led = json.loads(SPEND_LEDGER.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        led = {}
    today = datetime.now(timezone.utc).date().isoformat()
    if led.get("date") != today:
        led.update({"date": today, "spent_usd": 0.0, "calls": []})
    led["spent_usd"] = round(float(led.get("spent_usd", 0)) + usd, 4)
    led.setdefault("calls", []).append({"ts": now(), "mode": "candidates", "phase": "brainstorm",
                                        "entries": n, "est_usd": round(usd, 4)})
    SPEND_LEDGER.write_text(json.dumps(led, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def cmd_ask(args):
    import os
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        print("OPENROUTER_API_KEY not set; skipped", file=sys.stderr)
        return 1
    batch = load_json(args.batch, None)
    prompt = prompt_for(batch, args.per_seed)
    out, spent = [], 0.0
    for model in args.models.split(","):
        if spent >= args.budget:
            print(f"budget reached before {model}", file=sys.stderr)
            break
        items, cost = call_model(key, model, prompt)
        spent += cost
        n = 0
        for it in items or []:
            if isinstance(it, dict) and it.get("word"):
                it["by"] = model
                out.append(it)
                n += 1
        print(f"{model}: {n} proposals, ${cost:.4f}", file=sys.stderr)
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if spent and not args.no_ledger:
        record_spend(spent, len(out))
    print(f"EST_COST={spent:.4f} (recorded in pipeline/openrouter-ledger.json)" if not args.no_ledger
          else f"EST_COST={spent:.4f}")
    return 0


# --------------------------------------------------------------------------- filter
def kana_only(s):
    return not KANJI.search(s)


def cmd_filter(args):
    entries = load_entries()
    exact = {(e["headword"], e["reading"]) for e in entries}
    by_word = {}
    by_reading = {}
    for e in entries:
        by_word.setdefault(e["headword"], []).append(e)
        if bare(e["headword"]) != e["headword"]:
            exact.add((bare(e["headword"]), e["reading"]))
            by_word.setdefault(bare(e["headword"]), []).append(e)
        by_reading.setdefault(e["reading"], []).append(e)
    cands = {(plain(c.get("word", "")), c.get("reading", ""))
             for c in load_json(CANDIDATES, {}).get("candidates", [])}
    cand_words = {w for w, _ in cands}
    retired = load_json(RETIRED, {})
    retired = retired.get("retired", retired) if isinstance(retired, dict) else {}
    retired_ids = set(retired)
    decided = {}
    if LEDGER.exists():
        for line in LEDGER.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                decided[(r.get("word"), r.get("reading"))] = r.get("verdict")
    merged = {}
    for f in args.files:
        for it in load_json(f, []) or []:
            w, r = plain(str(it.get("word", ""))).strip(), str(it.get("reading", "")).strip()
            if not w:
                continue
            k = (w, r)
            if k in merged:
                merged[k]["by"] = sorted(set(merged[k]["by"]) | {it.get("by", "self")})
                merged[k]["usefulness"] = max(merged[k].get("usefulness") or 0, it.get("usefulness") or 0)
                continue
            merged[k] = {"word": w, "reading": r, "gloss": it.get("gloss", ""),
                         "relation": it.get("relation", ""), "seed_id": it.get("seed_id", ""),
                         "usefulness": it.get("usefulness"), "by": [it.get("by", "self")]}
    counts = {"proposed": len(merged), "entry": 0, "candidate": 0, "decided_before": 0, "new": 0,
              "possible_variant": 0}
    keep = []
    for (w, r), it in merged.items():
        if (w, r) in exact or w in by_word and not r:
            counts["entry"] += 1
            continue
        if (w, r) in cands or w in cand_words:
            counts["candidate"] += 1
            continue
        if decided.get((w, r)):
            counts["decided_before"] += 1
            continue
        same = by_reading.get(r, [])
        var = [e for e in same
               if e["id"] not in retired_ids and (kana_only(w) or kana_only(e["headword"])
                                                   or set(KANJI.findall(w)) & set(KANJI.findall(e["headword"])))]
        if w in by_word:
            var += [e for e in by_word[w] if e not in var]
        if var:
            it["possible_variant_of"] = [f'{e["id"]} {e["headword"]}({e["reading"]})' for e in var[:3]]
            counts["possible_variant"] += 1
        else:
            counts["new"] += 1
        keep.append(it)
    # Proposals that are other spellings of one word (same reading, a shared
    # kanji or one of them in kana) are listed with each other: keep one
    for it in keep:
        alts = [o["word"] for o in keep if o is not it and o["reading"] == it["reading"]
                and (kana_only(o["word"]) or kana_only(it["word"])
                     or set(KANJI.findall(o["word"])) & set(KANJI.findall(it["word"])))]
        if alts:
            it["alt_spellings"] = alts
    keep.sort(key=lambda x: (-len(x["by"]), -(x.get("usefulness") or 0), x["seed_id"], x["word"]))
    Path(args.out).write_text(json.dumps(keep, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(counts, ensure_ascii=False))
    return 0


# --------------------------------------------------------------------------- record
def cmd_record(args):
    batch = load_json(args.batch, None)
    verdicts = load_json(args.verdicts, []) if args.verdicts else []
    TASK_DIR.mkdir(parents=True, exist_ok=True)
    ts = now()
    lens_tag = batch["lens"] if batch["lens"] == "seeds" else f'field:{batch["field"]}'
    with open(LEDGER, "a", encoding="utf-8") as f:
        for v in verdicts:
            f.write(json.dumps({"ts": ts, "word": plain(v.get("word", "")), "reading": v.get("reading", ""),
                                "verdict": v.get("verdict"), "reason": v.get("reason", ""),
                                "lens": lens_tag}, ensure_ascii=False) + "\n")
    st = load_state()
    if batch["lens"] == "seeds":
        st["seed_cursor"] = batch["cursor_end"]
        st["next_lens"] = "field"
    else:
        st["field_cursor"] = batch["cursor_end"]
        st["next_lens"] = "seeds"
    st["updated"] = ts
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    added = sum(1 for v in verdicts if v.get("verdict") == "added")
    print(f"recorded {len(verdicts)} verdicts ({added} added); next lens: {st['next_lens']}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("next", help="print the next batch (writes nothing)")
    p.add_argument("--lens", choices=["seeds", "field"])
    p.add_argument("--n", type=int, default=SEED_BATCH)
    p.set_defaults(fn=cmd_next)
    p = sub.add_parser("ask", help="ask independent models for proposals")
    p.add_argument("batch")
    p.add_argument("--out", required=True)
    p.add_argument("--models", default=",".join(DEFAULT_MODELS))
    p.add_argument("--per-seed", type=int, default=6)
    p.add_argument("--budget", type=float, default=0.40)
    p.add_argument("--no-ledger", action="store_true", help="do not record the spend (trials)")
    p.set_defaults(fn=cmd_ask)
    p = sub.add_parser("filter", help="merge proposal files and drop what exists")
    p.add_argument("files", nargs="+")
    p.add_argument("--out", required=True)
    p.set_defaults(fn=cmd_filter)
    p = sub.add_parser("record", help="log verdicts and advance the cursor")
    p.add_argument("batch")
    p.add_argument("verdicts", nargs="?")
    p.set_defaults(fn=cmd_record)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
