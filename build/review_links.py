#!/usr/bin/env python3
"""Independent-model review of kana inline links: type screen, occurrence check, fixer.

The deterministic linker links a kana word to the one entry that has its
reading.  ``build/check_link_homophones.py`` inventories that class and keeps
the curated tier list (``build/data/kana_link_homophones.json``); this script
supplies the judgment the linker cannot make, through a model on OpenRouter
(the same plumbing as ``review_accuracy.py``).  Nothing here rewrites an entry
unless ``--apply-decisions`` is given, and that applies only decisions a person
or a Routine run has already logged.

Three jobs
----------
``--screen``      Type level.  For every kana base form the list does not know
                  yet (or ``--bases`` / ``--rescreen``), ask whether the kana
                  string commonly stands for a different word than the linked
                  entry.  Writes the verdict and the competitors into the list:
                  tier ``unique`` when the string is unambiguous in practice,
                  ``verify`` otherwise.  (``block`` is assigned only from
                  adjudicated occurrence reviews, by
                  ``check_link_homophones.py --retier``, or by hand.)

``--ids/--range/--tier/--base/--queue``
                  Occurrence level.  Each link of the selected occurrences is
                  shown in context (the sentence with the word marked, plus the
                  English translation for examples) and the model says whether
                  the marked word is the entry's word.  Results go to
                  ``reviews/links/review_<stamp>.jsonl`` (local, one line per
                  judged occurrence) and the flags (``other`` / ``unsure``) are
                  appended to ``reviews/link_flags.jsonl`` (tracked).  A person
                  or the Routine adjudicates each flag; nothing is applied.

``--apply-decisions``
                  Fixer.  For every ``unlink`` line in
                  ``reviews/link_decisions.jsonl`` whose link still exists, strip
                  the link markup (the surface text stays), then re-run the
                  linker on that entry so freed components can link on their own
                  (the linker honours the same ledger, so the removed link never
                  comes back); flags that now have a decision are dropped from
                  ``reviews/link_flags.jsonl``.  ``--ledger-from`` turns a
                  results file into ``keep`` lines for the occurrences the model
                  judged correct (used after a sweep so block-tier links pass
                  the CI gate).

Usage
-----
    python3 build/review_links.py --screen --budget 1.00
    python3 build/review_links.py --screen --bases そうして,ように --rescreen
    python3 build/review_links.py --tier verify --sample 60 --budget 2.00
    python3 build/review_links.py --ids 16667,26873 --budget 0.10      # Routine self-check
    python3 build/review_links.py --queue queue.json --budget 0.50
    python3 build/review_links.py --ledger-from reviews/links/review_x.jsonl --src sweep
    python3 build/review_links.py --apply-decisions [--ids ...] [--dry-run]

Every model call is estimated against ``--budget`` (USD) before it is made;
the run stops when the next call would exceed it.
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
import threading
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import auto_link as al  # noqa: E402
import check_link_homophones as clh  # noqa: E402
from review_runner import (  # noqa: E402
    MODEL_COSTS, call_openrouter, estimate_cost, extract_message_text, get_api_key,
    parse_model_response, rough_token_count, strip_code_fences,
)

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "entries"
RESULTS_DIR = ROOT / "reviews" / "links"
FLAGS_PATH = ROOT / "reviews" / "link_flags.jsonl"
DECISIONS_PATH = clh.DECISIONS_PATH
DATA_PATH = clh.DATA_PATH

# gemini-2.5-pro was tried for the screen (2026-09-08): its reasoning ate the
# completion cap and 65 of 66 JSON arrays came back truncated or as prose.
SCREEN_MODEL = "google/gemini-2.5-flash"
REVIEW_MODEL = "google/gemini-2.5-flash"
SCREEN_BATCH = 10
REVIEW_BATCH = 15
MAX_TOKENS = 8192
WORKERS = 4
PROMPT_VERSION = 1


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# Entry information for prompts
# ---------------------------------------------------------------------------


def load_entry_info(entries_dir: Path = ENTRIES_DIR) -> dict[str, dict]:
    """``entry id -> {headword, reading, pos, gloss, senses}`` for the whole dictionary."""
    info: dict[str, dict] = {}
    for _path, entry in clh.iter_entries(entries_dir):
        eid = entry.get("id") or ""
        senses = []
        for d in entry.get("definitions") or []:
            if isinstance(d, dict) and d.get("gloss"):
                senses.append(al.strip_furigana(str(d["gloss"])))
        info[eid] = {
            "headword": al.strip_furigana(entry.get("headword") or ""),
            "reading": entry.get("reading") or "",
            "pos": str(entry.get("part_of_speech") or ""),
            "gloss": al.strip_furigana(entry.get("gloss") or ""),
            "senses": senses[:6],
        }
    return info


def describe_entry(eid: str, info: dict[str, dict], competitors: list[str] | None = None) -> str:
    e = info.get(eid)
    if not e:
        return f"{eid}: (entry not found)"
    senses = "; ".join(s for s in e["senses"] if s and s != e["gloss"])
    text = f"{eid}: {e['headword']} [{e['reading']}], {e['pos'] or 'part of speech unknown'} — {e['gloss']}"
    if senses:
        text += f"; other senses: {senses}"
    if competitors:
        text += f" | known same-kana competitors: {', '.join(competitors)}"
    return text


# ---------------------------------------------------------------------------
# Model calls with a shared budget
# ---------------------------------------------------------------------------


class Budget:
    def __init__(self, limit: float):
        self.limit = limit
        self.spent = 0.0
        self.calls = 0
        self.lock = threading.Lock()

    def reserve(self, estimate: float) -> bool:
        with self.lock:
            if self.spent + estimate > self.limit:
                return False
            self.spent += estimate
            self.calls += 1
            return True

    def settle(self, estimate: float, actual: float | None) -> None:
        if actual is None:
            return
        with self.lock:
            self.spent += actual - estimate


def actual_cost(model: str, response: dict | None) -> float | None:
    usage = (response or {}).get("usage") if isinstance(response, dict) else None
    if not isinstance(usage, dict):
        return None
    costs = MODEL_COSTS.get(model, {"input": 0.002, "output": 0.008})
    return (usage.get("prompt_tokens", 0) / 1000 * costs["input"]
            + usage.get("completion_tokens", 0) / 1000 * costs["output"])


def ask(api_key: str, model: str, prompt: str, budget: Budget, expected_out: int, dry_run: bool):
    """One model call under the budget; returns (parsed list | None, est_cost, skipped)."""
    est = estimate_cost(model, rough_token_count(prompt), expected_out)
    if dry_run:
        return None, est, False
    if not budget.reserve(est):
        return None, est, True
    response = call_openrouter(api_key, model, prompt, timeout=180, max_tokens=MAX_TOKENS)
    budget.settle(est, actual_cost(model, response))
    return parse_list(response), est, False


OBJECT_RE = re.compile(r"\{[^{}]*\}")


def parse_list(response) -> list | None:
    """The model's JSON array, or the complete objects of a truncated one.

    A response cut off by the completion cap ends mid-object; the objects
    before the cut are still usable (each carries its item number), so they
    are salvaged rather than the whole batch being lost.
    """
    if not response:
        return None
    parsed = parse_model_response(response)
    if isinstance(parsed, list):
        return parsed
    text = extract_message_text(response)
    if not text:
        return None
    text = strip_code_fences(text)
    start = text.find("[")
    if start == -1:
        return None
    out = []
    for m in OBJECT_RE.finditer(text[start:]):
        try:
            obj = json.loads(m.group(0))
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict):
            out.append(obj)
    return out or None


# ---------------------------------------------------------------------------
# Type screen
# ---------------------------------------------------------------------------


SCREEN_INSTRUCTIONS = """You are a Japanese lexicographer validating automatic word links in a \
Japanese-English dictionary for intermediate learners. The linker links a word written in kana \
to the ONE dictionary entry that has that reading. That is safe only when the kana string, as it \
occurs in ordinary Japanese sentences and in English usage notes that cite Japanese words, \
practically always represents that entry's word. It is unsafe when the same kana string commonly \
represents something else: a homophone normally written with different kanji (かける: 掛ける / \
欠ける / 駆ける / 賭ける), an inflected form of a different word (そうして: the conjunction "and \
then" versus the て-form of そうする "do it that way"), a sequence of smaller words with a \
different function (ように "so that / like" versus よう + に), or a different grammatical use.

For each item, decide whether the kana string needs context before it can be linked to this entry.

Answer with ONLY a JSON array (no prose, no code fences), one object per item, in item order:
{"n": <item number>, "base": "<kana>", "verdict": "unique" | "ambiguous", "risk": "none" | "rare" | "common", "competitors": ["<kanji or analysis> (<short gloss>)", ...], "note": "<one short sentence>"}

- "unique": in practice the string always means this entry's word, or the alternatives are so \
rare in modern Japanese that a learner's dictionary can ignore them. Use risk "none" and an \
empty competitors list.
- "ambiguous": another reading is plausible in a learner-level corpus. risk "rare" when the \
entry's word clearly dominates (the competitor might appear in fewer than one occurrence in \
twenty); "common" otherwise.
- Differences of sense within the same word (かける "hang" versus "make a phone call"), polite or \
inflected variants, and kanji-versus-kana spelling of the same word are NOT competitors.
- A grammatical word cited in an English note ("the particle ので") is still that word.

Items:
"""


def screen_items(occ: list[clh.Occurrence], info: dict[str, dict], bases: list[str],
                 samples: int = 2) -> list[dict]:
    by_base: dict[str, list[clh.Occurrence]] = defaultdict(list)
    for o in occ:
        by_base[o["base"]].append(o)
    items = []
    for base in bases:
        items_of = by_base.get(base, [])
        targets = Counter(o["target"] for o in items_of)
        target = targets.most_common(1)[0][0] if targets else ""
        rng = random.Random(hash(base) & 0xFFFF)
        with_en = [o for o in items_of if o.get("english")]
        pool = with_en or items_of
        picks = rng.sample(pool, min(samples, len(pool))) if pool else []
        items.append({"base": base, "target": target, "count": len(items_of),
                      "targets": dict(targets), "samples": picks})
    return items


def screen_prompt(items: list[dict], info: dict[str, dict]) -> str:
    lines = [SCREEN_INSTRUCTIONS]
    for n, it in enumerate(items, 1):
        lines.append(f"{n}. base: {it['base']} — linked entry {describe_entry(it['target'], info)}")
        for s in it["samples"]:
            ctx = s["context"][:160]
            en = f' / "{s["english"][:120]}"' if s.get("english") else ""
            lines.append(f"   context: {ctx}{en}")
    return "\n".join(lines)


def run_screen(args, api_key: str | None) -> int:
    data = clh.load_data(args.data)
    occ = clh.collect(args.entries_dir)
    info = load_entry_info(args.entries_dir)
    counts = Counter(o["base"] for o in occ)
    if args.bases:
        bases = [clh.norm_base(b) for b in args.bases.split(",") if b.strip()]
    else:
        bases = [b for b in counts if args.rescreen or b not in data["bases"]]
    bases.sort(key=lambda b: (-counts.get(b, 0), b))
    if args.limit:
        bases = bases[:args.limit]
    if not bases:
        print("nothing to screen: every kana base is in the list")
        return 0
    items = screen_items(occ, info, bases)
    batches = [items[i:i + SCREEN_BATCH] for i in range(0, len(items), SCREEN_BATCH)]
    budget = Budget(args.budget)
    model = args.model or SCREEN_MODEL
    print(f"screening {len(bases)} base(s) in {len(batches)} call(s) with {model}"
          f"{' (dry run)' if args.dry_run else ''}")
    results: dict[str, dict] = {}
    est_total = 0.0
    skipped = 0
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    def record(base: str, r: dict) -> str:
        """Merge one screen verdict into the list; returns the tier written."""
        rec = data["bases"].get(base) or {}
        old_tier = rec.get("tier")
        new_tier = "unique" if r["verdict"] == "unique" else "verify"
        if old_tier == "block" or rec.get("tier_locked"):
            new_tier = old_tier            # a block decision survives a rescreen
        rec.update({
            "target": r["target"], "tier": new_tier,
            "competitors": r["competitors"],
            "screen": {"verdict": r["verdict"], "risk": r["risk"], "note": r["note"],
                       "model": model, "date": date},
        })
        data["bases"][base] = rec
        return new_tier

    def work(batch):
        prompt = screen_prompt(batch, info)
        parsed, est, was_skipped = ask(api_key, model, prompt, budget, 60 * len(batch), args.dry_run)
        return batch, parsed, est, was_skipped

    tiers = Counter()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(work, b) for b in batches]
        for done_n, fut in enumerate(as_completed(futures), 1):
            batch, parsed, est, was_skipped = fut.result()
            est_total += est
            if was_skipped:
                skipped += len(batch)
                continue
            if parsed is None:
                continue
            by_n = {}
            for r in parsed:
                if isinstance(r, dict):
                    try:
                        by_n[int(r.get("n"))] = r
                    except (TypeError, ValueError):
                        if r.get("base"):
                            by_n[r["base"]] = r
            for n, it in enumerate(batch, 1):
                r = by_n.get(n) or by_n.get(it["base"])
                if not isinstance(r, dict):
                    continue
                verdict = "ambiguous" if str(r.get("verdict", "")).lower().startswith("amb") else "unique"
                risk = str(r.get("risk", "none")).lower()
                if risk not in ("none", "rare", "common"):
                    risk = "rare" if verdict == "ambiguous" else "none"
                if verdict == "unique":
                    risk = "none"
                comps = [str(c) for c in (r.get("competitors") or []) if str(c).strip()]
                results[it["base"]] = {
                    "target": it["target"], "verdict": verdict, "risk": risk,
                    "competitors": comps, "note": str(r.get("note") or "")[:300],
                }
                if not args.dry_run:
                    tiers[record(it["base"], results[it["base"]])] += 1
            if not args.dry_run:
                clh.save_data(data, args.data)          # partial results survive a crash
                print(f"  {done_n}/{len(batches)} calls, {len(results)} screened, "
                      f"about ${budget.spent:.3f}", flush=True)
    if args.dry_run:
        print(f"estimated cost ${est_total:.3f} for {len(batches)} call(s); nothing written")
        print(screen_prompt(batches[0], info)[:3000])
        return 0
    clh.save_data(data, args.data)
    print(f"screened {len(results)} base(s): {dict(tiers)}; {skipped} skipped for budget; "
          f"spent about ${budget.spent:.3f}")
    print(f"wrote {args.data}")
    return 0


# ---------------------------------------------------------------------------
# Occurrence review
# ---------------------------------------------------------------------------


REVIEW_INSTRUCTIONS = """You are checking automatic word links in a Japanese-English dictionary for \
intermediate learners. Each item shows a Japanese sentence, or one line of an English usage note \
that cites Japanese, with ONE kana word marked 【like this】. An automatic linker linked the marked \
word to a dictionary entry. Decide whether the marked word, in this context, IS that entry's word.

Entries referenced (id: headword [reading], part of speech — gloss; other senses | known competitors):
"""

REVIEW_ANSWER = """
Answer with ONLY a JSON array (no prose, no code fences), one object per item, in item order:
{"n": <item number>, "verdict": "entry" | "other" | "unsure", "word": "<what the marked word actually is here>", "note": "<short reason>"}

- "entry": the marked word is the entry's word, in any of its senses; inflection, politeness, and \
kanji-versus-kana spelling do not matter. Put the entry's headword in "word".
- "other": the marked word is a different word or construction here (a homophone with different \
kanji, an inflected form of another word, a sequence of smaller words). Put the analysis in \
"word", e.g. "そうする + て" or "欠ける".
- "unsure": the context genuinely does not settle it.
Most links are correct: report "other" only when the context (including the English translation \
or the note's own gloss) clearly shows a different word. Do not judge translation quality or \
whether the sentence is natural.

Items:
"""


def review_prompt(batch: list[clh.Occurrence], info: dict[str, dict], data: dict) -> str:
    lines = [REVIEW_INSTRUCTIONS]
    seen = []
    for o in batch:
        if o["target"] not in seen:
            seen.append(o["target"])
    for tid in seen:
        comps = None
        for o in batch:
            if o["target"] == tid:
                comps = (data["bases"].get(o["base"]) or {}).get("competitors") or None
                break
        lines.append(describe_entry(tid, info, comps))
    lines.append(REVIEW_ANSWER)
    for n, o in enumerate(batch, 1):
        en = f' | English: "{o["english"]}"' if o.get("english") else ""
        lines.append(f"{n}. 【{o['surface']}】 → {o['target']} | Text: {o['context']}{en}")
    return "\n".join(lines)


def select_occurrences(args, data: dict) -> list[clh.Occurrence]:
    if args.queue:
        queue = json.loads(Path(args.queue).read_text(encoding="utf-8"))
        return [clh.Occurrence(q) for q in queue]
    ids = clh.parse_ids(args.ids)
    id_range = tuple(args.range) if args.range else None
    occ = clh.collect(args.entries_dir, ids, id_range)
    tiers = set(args.tier.split(",")) if args.tier else None
    bases = set(clh.norm_base(b) for b in args.base.split(",")) if args.base else None
    sel = [o for o in occ
           if (tiers is None or clh.tier_of(o["base"], data) in tiers)
           and (bases is None or o["base"] in bases)]
    if args.skip_decided:
        idx = clh.decision_index(clh.load_decisions(args.decisions))
        sel = [o for o in sel if not idx.get((clh.entry_num(o["entry"]), o["base"], o["target"]))]
    if args.skip_reviewed:
        done = reviewed_keys(RESULTS_DIR)
        sel = [o for o in sel if occurrence_key(o) not in done]
    return clh.sample_queue(sel, args.sample, args.seed)


def occurrence_key(o: dict) -> tuple:
    return (clh.entry_num(o.get("entry", "")), o.get("field"), o.get("base"), o.get("target"),
            o.get("surface"))


def reviewed_keys(results_dir: Path) -> set[tuple]:
    keys: set[tuple] = set()
    if not results_dir.exists():
        return keys
    for path in results_dir.glob("review_*.jsonl"):
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            keys.add(occurrence_key(rec))
    return keys


def run_review(args, api_key: str | None) -> int:
    data = clh.load_data(args.data)
    sel = select_occurrences(args, data)
    if not sel:
        print("no kana-base links to review in the selection")
        return 0
    for o in sel:
        o["tier"] = clh.tier_of(o["base"], data)
    info = load_entry_info(args.entries_dir)
    # batch by base so an entry description is shared, then pad mixed batches
    sel.sort(key=lambda o: (o["base"], o["entry"], o["field"]))
    batches = [sel[i:i + REVIEW_BATCH] for i in range(0, len(sel), REVIEW_BATCH)]
    budget = Budget(args.budget)
    model = args.model or REVIEW_MODEL
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    print(f"reviewing {len(sel)} link(s) over {len({o['base'] for o in sel})} base(s) in "
          f"{len(batches)} call(s) with {model}{' (dry run)' if args.dry_run else ''}")
    if args.dry_run:
        est = sum(estimate_cost(model, rough_token_count(review_prompt(b, info, data)), 40 * len(b))
                  for b in batches)
        print(f"estimated cost ${est:.3f}; nothing written")
        print(review_prompt(batches[0], info, data)[:3000])
        return 0
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    results_path = RESULTS_DIR / f"review_{stamp}.jsonl"
    verdicts = Counter()
    flagged: list[dict] = []
    judged = 0
    skipped = 0
    lock = threading.Lock()

    def work(batch):
        prompt = review_prompt(batch, info, data)
        parsed, est, was_skipped = ask(api_key, model, prompt, budget, 40 * len(batch), False)
        return batch, parsed, was_skipped

    with results_path.open("a", encoding="utf-8") as out, \
            ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(work, b) for b in batches]
        for done_n, fut in enumerate(as_completed(futures), 1):
            batch, parsed, was_skipped = fut.result()
            if was_skipped:
                skipped += len(batch)
                continue
            if parsed is None:
                skipped += len(batch)
                continue
            by_n = {}
            for r in parsed:
                if isinstance(r, dict):
                    try:
                        by_n[int(r.get("n"))] = r
                    except (TypeError, ValueError):
                        pass
            with lock:
                for n, o in enumerate(batch, 1):
                    r = by_n.get(n)
                    if not isinstance(r, dict):
                        skipped += 1
                        continue
                    verdict = str(r.get("verdict", "")).lower()
                    if verdict not in ("entry", "other", "unsure"):
                        verdict = "unsure"
                    rec = dict(o)
                    rec.update({"ts": utc_now(), "model": model, "prompt_version": PROMPT_VERSION,
                                "src": args.src, "verdict": verdict,
                                "word": str(r.get("word") or "")[:120],
                                "note": str(r.get("note") or "")[:300]})
                    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    verdicts[verdict] += 1
                    judged += 1
                    if verdict != "entry":
                        flagged.append(rec)
            if done_n % 20 == 0 or done_n == len(futures):
                print(f"  {done_n}/{len(futures)} calls, {judged} judged, "
                      f"{len(flagged)} flagged, about ${budget.spent:.3f}", flush=True)
    if flagged:
        with FLAGS_PATH.open("a", encoding="utf-8") as f:
            for rec in flagged:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    per_base = defaultdict(Counter)
    for rec in flagged:
        per_base[rec["base"]][rec["verdict"]] += 1
    print(f"judged {judged} link(s): {dict(verdicts)}; {skipped} not judged (budget or parse); "
          f"spent about ${budget.spent:.3f} in {budget.calls} call(s)")
    print(f"results: {results_path}")
    if flagged:
        print(f"flags appended to {FLAGS_PATH}: {len(flagged)}")
        top = sorted(per_base.items(), key=lambda kv: -sum(kv[1].values()))[:25]
        for base, c in top:
            print(f"  {base}: {dict(c)}")
    return 0


# ---------------------------------------------------------------------------
# Ledger helpers and fixer
# ---------------------------------------------------------------------------


def decision_line(o: dict, decision: str, src: str, by: str, note: str = "") -> dict:
    return {"ts": utc_now(), "entry": clh.entry_num(o.get("entry", "")), "field": o.get("field"),
            "surface": o.get("surface"), "base": o.get("base"), "target": o.get("target"),
            "context": o.get("context"), "decision": decision, "src": src, "by": by,
            "note": note[:120]}


def run_ledger_from(args) -> int:
    """Write keep lines for a results file's 'entry' verdicts (model-confirmed links).

    Per occurrence by default (what the gate needs for block-tier bases); with
    ``--aggregate`` one line per (base, target) carrying ``n``, which is enough
    for ``--retier`` and keeps the ledger small for the thousands of links the
    model confirmed on unique/verify bases.
    """
    path = Path(args.ledger_from)
    existing = clh.decision_index(clh.load_decisions(args.decisions))
    data = clh.load_data(args.data)
    written = 0
    agg: Counter = Counter()
    model_name = ""
    with args.decisions.open("a", encoding="utf-8") as out:
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if rec.get("verdict") != "entry":
                continue
            tier = clh.tier_of(rec.get("base", ""), data)
            if args.only_tier and tier not in args.only_tier.split(","):
                continue
            model_name = rec.get("model", "") or model_name
            if args.aggregate:
                agg[(rec.get("base"), rec.get("target"))] += 1
                continue
            key = (clh.entry_num(rec.get("entry", "")), rec.get("base"), rec.get("target"))
            if "keep" in existing.get(key, set()):
                continue
            out.write(json.dumps(decision_line(rec, "keep", args.src, "model",
                                               f"{rec.get('model', '')} judged entry"),
                                 ensure_ascii=False) + "\n")
            existing[key].add("keep")
            written += 1
        for (base, target), n in sorted(agg.items()):
            out.write(json.dumps({"ts": utc_now(), "base": base, "target": target, "decision": "keep",
                                  "n": n, "src": args.src, "by": "model",
                                  "note": f"{n} occurrence(s) judged entry by {model_name}"},
                                 ensure_ascii=False) + "\n")
            written += 1
    print(f"appended {written} keep line(s) to {args.decisions}")
    return 0


def strip_link(text: str, surface: str, base: str, target: str, context: str = "",
               new_base: str = "", new_target: str = "") -> tuple[str, int]:
    """Remove ⟦surface→base：target⟧ wrappers matching the decision; keep the surface text.

    With ``context`` (the detector's marked line, ``…【そうして】 (like that…``) only
    the link whose own marked context equals it is removed, so two occurrences
    of one word in one field can receive different decisions.  The marked
    context ignores other links' markup, so it is stable across edits.  With
    ``new_base`` and ``new_target`` the link is rewritten to them instead of
    removed (a ``retarget`` decision).
    """
    n = 0

    def repl(m):
        nonlocal n
        info = al.LINK_INFO_RE.match(m.group(1))
        if not info:
            return m.group(0)
        s, b, t = info.groups()
        if t != target or clh.norm_base(b) != clh.norm_base(base):
            return m.group(0)
        if surface and al.strip_furigana(s) != surface:
            return m.group(0)
        if context and clh.marked_context(text, m.start(), m.end()) != context:
            return m.group(0)
        n += 1
        if new_base and new_target:
            return f"⟦{s}→{new_base}：{new_target}⟧"
        return s

    return al.LINK_RE.sub(repl, text), n


def run_apply(args) -> int:
    decisions = [d for d in clh.load_decisions(args.decisions) if d["decision"] in ("unlink", "retarget")]
    known_ids = {p.stem for p in args.entries_dir.glob("*/*.json")}
    for d in decisions:
        if d["decision"] == "retarget" and d.get("new_target") not in known_ids:
            print(f"warning: retarget for {d.get('entry')} names no entry {d.get('new_target')}; skipped",
                  file=sys.stderr)
    decisions = [d for d in decisions
                 if d["decision"] != "retarget" or d.get("new_target") in known_ids]
    ids = clh.parse_ids(args.ids)
    if ids:
        decisions = [d for d in decisions if clh.entry_num(d.get("entry", "")) in ids]
    by_entry: dict[str, list[dict]] = defaultdict(list)
    for d in decisions:
        by_entry[clh.entry_num(d.get("entry", ""))].append(d)
    if not by_entry:
        print("no unlink decisions to apply")
        return 0
    tokenizer = None if args.no_relink else al.load_tokenizer()
    resolver = linker = None
    if not args.no_relink:
        resolver = al.Resolver(al.iter_entries(args.entries_dir),
                               blocked=al.load_blocked_bases(args.data),
                               unlinked=al.load_unlink_decisions(args.decisions))
        linker = al.Linker(resolver, tokenizer)
    changed = removed = 0
    for path, entry in clh.iter_entries(args.entries_dir, set(by_entry)):
        original = path.read_text(encoding="utf-8")
        n_entry = 0
        for d in by_entry[clh.entry_num(entry.get("id", path.stem))]:
            field = d.get("field") or ""
            targets: list[tuple[str, dict, str]] = []
            m = re.match(r"examples\[(\d+)\]", field)
            if m:
                idx = int(m.group(1))
                exs = entry.get("examples") or []
                if idx < len(exs) and isinstance(exs[idx], dict):
                    targets.append(("japanese", exs[idx], field))
            elif field == "notes":
                targets.append(("notes", entry, field))
            else:                      # no field: every field
                for i, ex in enumerate(entry.get("examples") or []):
                    if isinstance(ex, dict):
                        targets.append(("japanese", ex, f"examples[{i}]"))
                targets.append(("notes", entry, "notes"))
            for key, holder, _name in targets:
                text = holder.get(key)
                if not isinstance(text, str) or not text:
                    continue
                new, n = strip_link(text, d.get("surface") or "", d.get("base", ""), d.get("target", ""),
                                    d.get("context") or "",
                                    d.get("new_base") or "" if d["decision"] == "retarget" else "",
                                    d.get("new_target") or "" if d["decision"] == "retarget" else "")
                if n:
                    holder[key] = new
                    n_entry += n
        if not n_entry:
            continue
        removed += n_entry
        if linker is not None:
            al.process_entry(entry, linker, resolver, al.Stats())
        if args.dry_run:
            print(f"{path.stem}: would remove {n_entry} link(s)")
            changed += 1
            continue
        entry.setdefault("metadata", {})["modified"] = al.utc_now()
        al.write_entry(path, entry, original)
        changed += 1
        print(f"{path.stem}: removed {n_entry} link(s)")
    print(f"{'would change' if args.dry_run else 'changed'} {changed} entry file(s), "
          f"{removed} link(s) removed or retargeted")
    # A key (entry, base, target) with unlink decisions and no keep means the base
    # never links in that entry (the linker excludes it); strip any occurrence that
    # slipped in without its own decision so the gate and the linker agree.
    idx = clh.decision_index(clh.load_decisions(args.decisions))
    unlink_only = {k for k, v in idx.items() if "unlink" in v and "keep" not in v}
    stray = 0
    for path, entry in clh.iter_entries(args.entries_dir, {k[0] for k in unlink_only} if not ids else ids):
        num = clh.entry_num(entry.get("id", path.stem))
        original = path.read_text(encoding="utf-8")
        n_entry = 0
        for o in clh.kana_link_occurrences(entry):
            if (num, o["base"], o["target"]) not in unlink_only:
                continue
            holders = []
            m = re.match(r"examples\[(\d+)\]", o["field"])
            if m:
                holders.append(("japanese", entry["examples"][int(m.group(1))]))
            else:
                holders.append(("notes", entry))
            for key, holder in holders:
                new, n = strip_link(holder[key], o["surface"], o["base"], o["target"], o["context"])
                if n:
                    holder[key] = new
                    n_entry += n
        if not n_entry:
            continue
        stray += n_entry
        if args.dry_run:
            print(f"{path.stem}: would remove {n_entry} stray link(s) of an unlinked base")
            continue
        entry.setdefault("metadata", {})["modified"] = al.utc_now()
        al.write_entry(path, entry, original)
        print(f"{path.stem}: removed {n_entry} stray link(s) of an unlinked base")
    if stray:
        print(f"{'would remove' if args.dry_run else 'removed'} {stray} stray link(s) of bases unlinked by decision")
    if not args.dry_run:
        pruned = prune_flags(args.decisions, FLAGS_PATH)
        if pruned:
            print(f"dropped {pruned} adjudicated flag(s) from {FLAGS_PATH}")
    return 0


def prune_flags(decisions_path: Path, flags_path: Path) -> int:
    """Drop flags that now have a ledger decision; the flags file lists open items only."""
    if not flags_path.exists():
        return 0
    idx = clh.decision_index(clh.load_decisions(decisions_path))
    kept, dropped = [], 0
    for line in flags_path.read_text(encoding="utf-8").splitlines():
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            kept.append(line)
            continue
        key = (clh.entry_num(rec.get("entry", "")), clh.norm_base(rec.get("base", "")), rec.get("target", ""))
        if idx.get(key):
            dropped += 1
        else:
            kept.append(line)
    if dropped:
        flags_path.write_text("".join(l + "\n" for l in kept), encoding="utf-8")
    return dropped


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--screen", action="store_true", help="type-level screen of kana bases")
    mode.add_argument("--apply-decisions", action="store_true", help="apply unlink decisions from the ledger")
    mode.add_argument("--ledger-from", metavar="RESULTS", help="write keep lines from a results file")
    ap.add_argument("--ids", help="comma-separated entry IDs, or @file")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"))
    ap.add_argument("--tier", help="occurrence review: comma-separated tiers (unique, verify, block, unscreened)")
    ap.add_argument("--base", help="occurrence review: comma-separated bases")
    ap.add_argument("--queue", help="occurrence review: JSON queue from check_link_homophones.py --json")
    ap.add_argument("--sample", type=int, default=0, metavar="N", help="at most N occurrences per base")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--skip-decided", action="store_true",
                    help="occurrence review: skip links that already have a ledger decision")
    ap.add_argument("--skip-reviewed", action="store_true",
                    help="occurrence review: skip links already in a reviews/links results file")
    ap.add_argument("--bases", help="--screen: comma-separated bases to screen")
    ap.add_argument("--rescreen", action="store_true", help="--screen: include bases already in the list")
    ap.add_argument("--limit", type=int, default=0, help="--screen: at most N bases")
    ap.add_argument("--only-tier", help="--ledger-from: keep lines only for these tiers")
    ap.add_argument("--aggregate", action="store_true",
                    help="--ledger-from: one keep line per (base, target) with a count instead of per occurrence")
    ap.add_argument("--src", default="sweep", help="ledger/flag source label (sweep, self-check, hand)")
    ap.add_argument("--model", help="OpenRouter model id")
    ap.add_argument("--budget", type=float, default=0.50, help="USD cap for this invocation")
    ap.add_argument("--workers", type=int, default=WORKERS)
    ap.add_argument("--dry-run", action="store_true", help="show the first prompt and the estimate")
    ap.add_argument("--no-relink", action="store_true", help="--apply-decisions: do not re-run the linker")
    ap.add_argument("--entries-dir", type=Path, default=ENTRIES_DIR)
    ap.add_argument("--data", type=Path, default=DATA_PATH)
    ap.add_argument("--decisions", type=Path, default=DECISIONS_PATH)
    args = ap.parse_args(argv)

    if args.apply_decisions:
        return run_apply(args)
    if args.ledger_from:
        return run_ledger_from(args)
    api_key = None if args.dry_run else get_api_key()
    if api_key is None and not args.dry_run:
        print("OPENROUTER_API_KEY is not set", file=sys.stderr)
        return 2
    if args.screen:
        return run_screen(args, api_key)
    return run_review(args, api_key)


if __name__ == "__main__":
    sys.exit(main())
