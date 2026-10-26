#!/usr/bin/env python3
"""Triage the lookup reports sent by ezFurigana (https://www.ezfurigana.com/).

ezFurigana adds furigana to texts its users paste in and links the words to
this dictionary's entries (with Tom's permission, since mid-2026). Its owner
sends Tom a TSV of the words his users met that the dictionary could not
serve, one row per surface form and reading:

    surface  reading  category  tkgje_existing_spelling  lookups  first_seen_utc  last_seen_utc

with category one of "not in TKGJE", "TKGJE has another kanji spelling",
"TKGJE has kana form only", "TKGJE has this word with another reading" and
"grammar expression/particle". These are words real learners met in real
texts: a demand signal, not a word list to copy. Every row is vetted one by
one against the find-candidates gates (G1–G7) like any other proposal, and
only the survivors go to candidate_words.json (prompts/newcandidates.md,
stream 3).

    python3 build/ezfurigana_lookups.py ingest <file.tsv>      # file it under external/ezfurigana/received/
    python3 build/ezfurigana_lookups.py pending [--n 100] [--category not-in] > /tmp/ez.json
    python3 build/ezfurigana_lookups.py record /tmp/ez_verdicts.json
    python3 build/ezfurigana_lookups.py stats
    python3 build/ezfurigana_lookups.py variants > /tmp/variants.tsv   # surface → existing entry
    python3 build/ezfurigana_lookups.py queue --n 40    # queued ezFurigana candidates, most looked-up first

`pending` reads every file in received/, keeps for each (surface, reading)
the row with the latest last_seen_utc, and drops rows already decided in
external/ezfurigana/ledger.jsonl and rows whose surface and reading are now an
entry or a candidate. It ranks the rest by lookups and annotates each with
the entries that share its surface or reading (`same_surface`,
`same_reading`), so a variant spelling or an inflected form is easy to see.

`record` takes [{surface, reading, verdict, reason, entry_id?, word?}], with
verdict one of:

  added      a candidate was added (word/reading if they differ from the row)
  exists     the word has an entry the row's form should reach (an inflected
             or bare-stem form, an affix use); entry_id names it
  variant    another spelling or reading of an existing entry; entry_id
  queued     already in candidate_words.json
  rejected   fails a gate (reason says which: proper noun of no weight,
             affix, archaic, too technical, free phrase, …)

A decided row is not served again. A rejected word that keeps being looked up
can be reconsidered with `pending --include-decided`.
"""
import argparse
import csv
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "build"))

import brainstorm_candidates as bc  # noqa: E402
from brainstorm_candidates import bare, load_entries, load_json, plain  # noqa: E402

BASE = ROOT / "external" / "ezfurigana"
RECEIVED = BASE / "received"
LEDGER = BASE / "ledger.jsonl"

COLUMNS = ["surface", "reading", "category", "tkgje_existing_spelling", "lookups",
           "first_seen_utc", "last_seen_utc"]
CATEGORIES = {
    "not-in": "not in TKGJE",
    "kanji-spelling": "TKGJE has another kanji spelling",
    "kana-only": "TKGJE has kana form only",
    "reading": "TKGJE has this word with another reading",
    "grammar": "grammar expression/particle",
}
VERDICTS = {"added", "exists", "variant", "queued", "rejected"}
# Every candidate this stream adds carries this in its notes (pipeline/routine_next.py counts it)
MARK = "ezfurigana: looked up"
LOOKED_UP = re.compile(MARK + r" (\d+)")


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_tsv(path):
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    if rows and set(COLUMNS) - set(rows[0]):
        raise ValueError(f"{path}: missing columns {sorted(set(COLUMNS) - set(rows[0]))}")
    for r in rows:
        r["surface"] = r["surface"].strip()
        r["reading"] = r["reading"].strip()
        try:
            r["lookups"] = int(r.get("lookups") or 0)
        except ValueError:
            r["lookups"] = 0
    return [r for r in rows if r["surface"]]


def received_rows(received=RECEIVED):
    """Every received row, one per (surface, reading): the most recently seen."""
    best = {}
    for path in sorted(received.glob("*.tsv")):
        for r in read_tsv(path):
            k = (r["surface"], r["reading"])
            r["file"] = path.name
            if k not in best or (r.get("last_seen_utc") or "") >= (best[k].get("last_seen_utc") or ""):
                best[k] = r
    return best


def load_ledger(ledger=LEDGER):
    out = {}
    if ledger.exists():
        for line in ledger.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                out[(r.get("surface"), r.get("reading"))] = r
    return out


# --------------------------------------------------------------------------- ingest
def cmd_ingest(args):
    src = Path(args.file)
    rows = read_tsv(src)
    RECEIVED.mkdir(parents=True, exist_ok=True)
    day = args.date or datetime.now(timezone.utc).date().isoformat()
    name = re.sub(r"[^A-Za-z0-9_.-]+", "_", src.stem).strip("_") or "lookups"
    dest = RECEIVED / f"{day}_{name}.tsv"
    if dest.exists() and dest.read_bytes() != src.read_bytes():
        raise SystemExit(f"{dest} exists with other content; pass --date")
    shutil.copyfile(src, dest)
    cats = {}
    for r in rows:
        cats[r["category"]] = cats.get(r["category"], 0) + 1
    print(f"filed {len(rows)} rows as {dest.relative_to(ROOT)}")
    print(json.dumps(cats, ensure_ascii=False))
    return 0


# --------------------------------------------------------------------------- pending
def pending(include_decided=False, category=None, received=RECEIVED, ledger=LEDGER):
    entries = load_entries()
    exact, by_word, by_reading = set(), {}, {}
    for e in entries:
        for w in {e["headword"], bare(e["headword"])}:
            exact.add((w, e["reading"]))
            by_word.setdefault(w, []).append(e)
        by_reading.setdefault(e["reading"], []).append(e)
    cands = {(plain(c.get("word", "")), c.get("reading", "")): c.get("id")
             for c in load_json(bc.CANDIDATES, {}).get("candidates", [])}
    decided = load_ledger(ledger)
    want = CATEGORIES.get(category, category)
    counts = {"rows": 0, "decided_before": 0, "entry_now": 0, "candidate_now": 0, "pending": 0}
    out = []
    for (s, r), row in received_rows(received).items():
        if want and row["category"] != want:
            continue
        counts["rows"] += 1
        if (s, r) in decided and not include_decided:
            counts["decided_before"] += 1
            continue
        if (s, r) in exact:
            counts["entry_now"] += 1
            continue
        if (s, r) in cands:
            counts["candidate_now"] += 1
            continue
        item = {"surface": s, "reading": r, "category": row["category"],
                "existing": row.get("tkgje_existing_spelling", ""), "lookups": row["lookups"]}
        same_s = [f'{e["id"]} {e["headword"]}({e["reading"]})' for e in by_word.get(s, [])]
        same_r = [f'{e["id"]} {e["headword"]}' for e in by_reading.get(r, [])]
        if same_s:
            item["same_surface"] = same_s[:4]
        if same_r:
            item["same_reading"] = same_r[:6]
        if (s, r) in decided:
            item["decided_before"] = decided[(s, r)].get("verdict")
        out.append(item)
    counts["pending"] = len(out)
    out.sort(key=lambda x: (-x["lookups"], x["reading"], x["surface"]))
    return out, counts


def cmd_pending(args):
    out, counts = pending(args.include_decided, args.category)
    if args.n:
        out = out[:args.n]
    print(json.dumps(out, ensure_ascii=False, indent=1))
    print(json.dumps(counts, ensure_ascii=False), file=sys.stderr)
    return 0


def pending_count():
    """Rows still waiting for a verdict (for pipeline/routine_next.py)."""
    if not RECEIVED.exists() or not any(RECEIVED.glob("*.tsv")):
        return 0
    return len(pending()[0])


# --------------------------------------------------------------------------- record
def cmd_record(args):
    record(load_json(args.verdicts, []))
    return 0


def record(verdicts, received=RECEIVED, ledger=LEDGER):
    rows = received_rows(received)
    bad = [v for v in verdicts if v.get("verdict") not in VERDICTS or not v.get("surface")]
    if bad:
        raise SystemExit(f"bad verdicts (need surface and one of {sorted(VERDICTS)}): {bad[:3]}")
    ledger.parent.mkdir(parents=True, exist_ok=True)
    ts = now()
    with open(ledger, "a", encoding="utf-8") as f:
        for v in verdicts:
            row = rows.get((v["surface"], v.get("reading", "")), {})
            rec = {"ts": ts, "surface": v["surface"], "reading": v.get("reading", ""),
                   "category": row.get("category", ""), "lookups": row.get("lookups"),
                   "verdict": v["verdict"], "reason": v.get("reason", "")}
            for k in ("entry_id", "word", "word_reading"):
                if v.get(k):
                    rec[k] = v[k]
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    tally = {}
    for v in verdicts:
        tally[v["verdict"]] = tally.get(v["verdict"], 0) + 1
    print(f"recorded {len(verdicts)} verdicts: {json.dumps(tally)}")


# --------------------------------------------------------------------------- stats / variants
def cmd_stats(args):
    rows = received_rows()
    led = load_ledger()
    by_cat = {}
    for k, r in rows.items():
        c = by_cat.setdefault(r["category"], {"rows": 0})
        v = led.get(k, {}).get("verdict", "undecided")
        c["rows"] += 1
        c[v] = c.get(v, 0) + 1
    files = sorted(p.name for p in RECEIVED.glob("*.tsv")) if RECEIVED.exists() else []
    print(json.dumps({"files": files, "rows": len(rows), "by_category": by_cat},
                     ensure_ascii=False, indent=1))
    return 0


def cmd_variants(args):
    print("surface\treading\tentry_id\tverdict")
    for (s, r), v in sorted(load_ledger().items(), key=lambda kv: kv[0][1]):
        if v.get("verdict") in ("variant", "exists") and v.get("entry_id"):
            print(f"{s}\t{r}\t{v['entry_id']}\t{v['verdict']}")
    return 0


def cmd_queue(args):
    """The ezFurigana candidates in the queue, most looked-up first (for new-entries)."""
    cands = [c for c in load_json(bc.CANDIDATES, {}).get("candidates", [])
             if MARK in c.get("notes", "")]
    count = lambda c: int((LOOKED_UP.search(c["notes"]) or [0, 0])[1])  # noqa: E731
    cands.sort(key=lambda c: (-count(c), c["id"]))
    for c in cands[:args.n or None]:
        print(f'{c["id"]}  {c["word"]} ({c["reading"]}): {c["notes"]}')
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("ingest", help="file a received TSV under external/ezfurigana/received/")
    p.add_argument("file")
    p.add_argument("--date", help="date prefix for the filed copy (default: today, UTC)")
    p.set_defaults(fn=cmd_ingest)
    p = sub.add_parser("pending", help="rows still to vet, most looked-up first (writes nothing)")
    p.add_argument("--n", type=int, default=0)
    p.add_argument("--category", help="not-in | kanji-spelling | kana-only | reading | grammar")
    p.add_argument("--include-decided", action="store_true")
    p.set_defaults(fn=cmd_pending)
    p = sub.add_parser("record", help="append verdicts to the ledger")
    p.add_argument("verdicts")
    p.set_defaults(fn=cmd_record)
    p = sub.add_parser("stats", help="rows and verdicts by category")
    p.set_defaults(fn=cmd_stats)
    p = sub.add_parser("variants", help="TSV of rows decided as a form of an existing entry")
    p.set_defaults(fn=cmd_variants)
    p = sub.add_parser("queue", help="queued ezFurigana candidates, most looked-up first")
    p.add_argument("--n", type=int, default=40)
    p.set_defaults(fn=cmd_queue)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
