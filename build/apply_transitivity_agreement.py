#!/usr/bin/env python3
"""Apply transitivity tags where two independent models agree.

review_transitivity.py writes one JSONL row per verb per model run under
reviews/transitivity/. A single cheap model measured about 88 percent right on
suru-verbs (it reads the example's surface pattern: a passive example became
"intransitive", a に-object became "transitive"), which is not good enough to
apply alone. This script takes the latest verdict per (verb, model), applies
`tags.transitivity` only where at least two different models agree and the
entry has no transitivity yet, and writes every disagreement to
reviews/transitivity/disagreements.jsonl for a polish or systemic-fix run to
adjudicate by hand. Pair links are never written here (a model-proposed pair
such as 一味違う ↔ 違う is not a transitivity pair).

Usage:
    python3 build/apply_transitivity_agreement.py            # dry run: counts only
    python3 build/apply_transitivity_agreement.py --apply
"""
import argparse
import glob
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = ROOT / "reviews" / "transitivity"
DISAGREEMENTS = RESULTS_DIR / "disagreements.jsonl"
VALID = {"transitive", "intransitive", "both"}


def load_rows():
    rows = []
    for path in sorted(RESULTS_DIR.glob("*.jsonl")):
        if path.name == DISAGREEMENTS.name:
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows


def latest_per_model(rows):
    """{entry_id: {model: row}} keeping the newest row per model."""
    out = defaultdict(dict)
    for r in rows:
        eid, model = r.get("id"), r.get("model")
        if not eid or not model or r.get("transitivity") not in VALID:
            continue
        prev = out[eid].get(model)
        if prev is None or str(r.get("reviewed_at", "")) > str(prev.get("reviewed_at", "")):
            out[eid][model] = r
    return out


FURI_RE = re.compile(r"\{([^|}]+)\|[^}]+\}")
LINK_RE = re.compile(r"⟦([^→⟧]+)→[^⟧]*⟧")


def plain(text):
    return FURI_RE.sub(r"\1", LINK_RE.sub(r"\1", text or ""))


def example_evidence_supports(entry, value):
    """Does the entry's own text show the valency the models claim?

    transitive: an example has を directly before the verb, or a passive
    (〜される) of it; intransitive: an example has が/は directly before the
    verb and none has を before it; both: evidence of each."""
    hw = plain(entry.get("headword") or "").replace("する", "")
    if not hw:
        return False
    texts = [plain(ex.get("japanese")) for ex in entry.get("examples") or []]
    texts.append(plain(entry.get("notes") or ""))
    blob = "\n".join(texts)
    verb = re.escape(hw)
    trans = re.search(r"を\s*" + verb + r"(?:する|し|した|して|しま|でき|される|され|させ)", blob) \
        or re.search(verb + r"(?:され|された|されて|されている)", blob)
    intrans = re.search(r"[がはも]\s*" + verb + r"(?:する|し|した|して|しま)", blob)
    if value == "transitive":
        return bool(trans)
    if value == "intransitive":
        return bool(intrans) and not trans
    if value == "both":
        return bool(trans) and bool(intrans)
    return False


def entry_paths():
    return {re.sub(r".*/", "", p)[:-5]: p for p in glob.glob(str(ROOT / "entries" / "*" / "*.json"))}


def timestamp():
    return subprocess.run([sys.executable, str(ROOT / "build" / "get_timestamp.py")],
                          capture_output=True, text=True).stdout.strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--apply", action="store_true", help="Write agreed tags into entries.")
    ap.add_argument("--min-models", type=int, default=2)
    args = ap.parse_args()

    verdicts = latest_per_model(load_rows())
    paths = entry_paths()
    agreed, disagreed, single, already, missing = [], [], 0, 0, 0
    for eid, by_model in sorted(verdicts.items()):
        if len(by_model) < args.min_models:
            single += 1
            continue
        values = {r["transitivity"] for r in by_model.values()}
        if len(values) == 1:
            agreed.append((eid, values.pop(), by_model))
        else:
            disagreed.append((eid, by_model))

    applied = 0
    unsupported = []
    ts = timestamp() if args.apply else None
    for eid, value, by_model in agreed:
        path = paths.get(eid)
        if not path:
            missing += 1
            continue
        raw = open(path, encoding="utf-8").read()
        entry = json.loads(raw)
        tags = entry.setdefault("metadata", {}).setdefault("tags", {})
        if tags.get("transitivity"):
            already += 1
            continue
        if "verb-suru" in (tags.get("pos") or []) and not example_evidence_supports(entry, value):
            # Both models read the example's surface pattern; for suru-verbs
            # require the entry's own examples to show the claimed valency.
            unsupported.append((eid, value, by_model))
            continue
        if args.apply:
            tags["transitivity"] = value
            entry["metadata"]["modified"] = ts
            open(path, "w", encoding="utf-8").write(
                json.dumps(entry, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""))
        applied += 1

    if args.apply:
        with DISAGREEMENTS.open("w", encoding="utf-8") as f:
            for eid, by_model in disagreed:
                f.write(json.dumps({
                    "id": eid, "reason": "models-disagree",
                    "headword": next(iter(by_model.values())).get("headword"),
                    "verdicts": {m: r["transitivity"] for m, r in by_model.items()},
                    "pairs": {m: r.get("pair") for m, r in by_model.items() if r.get("pair")},
                }, ensure_ascii=False) + "\n")
            for eid, value, by_model in unsupported:
                f.write(json.dumps({
                    "id": eid, "reason": "no-example-evidence",
                    "headword": next(iter(by_model.values())).get("headword"),
                    "verdicts": {m: r["transitivity"] for m, r in by_model.items()},
                }, ensure_ascii=False) + "\n")

    mode = "APPLIED" if args.apply else "DRY RUN"
    print(f"{mode}: verbs with >= {args.min_models} model verdicts: {len(agreed) + len(disagreed)}; "
          f"agreed {len(agreed)} (tags {'written' if args.apply else 'to write'}: {applied}, "
          f"agreed but unsupported by the entry's examples: {len(unsupported)}, "
          f"already tagged: {already}, no file: {missing}); disagreed {len(disagreed)}; "
          f"single-model only: {single}")
    if args.apply:
        print(f"disagreements written to {DISAGREEMENTS.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
