"""Scoring helpers."""
import json
import statistics
from pathlib import Path

HERE = Path(__file__).parent


def slug(m):
    return m.replace("/", "__").replace(":", "_").replace("~", "")


DROP = json.load(open(HERE / "drop.json")) if (HERE / "drop.json").exists() else {}


def load_res(model, task):
    p = HERE / "results" / slug(model) / f"{task}.jsonl"
    if not p.exists():
        return []
    d = {}
    drop = set(DROP.get(task, []))
    for l in open(p):
        r = json.loads(l)
        if r["id"] in drop:
            continue
        d[r["id"]] = r
    return list(d.values())


def p_true(r):
    """Probability of 'yes' for a noul item (decision or LLM), or None."""
    a = r.get("answer")
    if not a:
        return None
    if "noul" in a:
        return float(a["noul"])
    if "p_yes" in a:
        try:
            return float(a["p_yes"])
        except (TypeError, ValueError):
            return 1.0 if str(a.get("answer", "")).lower().startswith("y") else 0.0
    return None


def choice(r):
    a = r.get("answer")
    if not a:
        return None, None
    if "choice" in a:
        return a["choice"], a.get("probabilities", {}).get(a["choice"], a.get("confidence"))
    try:
        p = float(a.get("p", 0.5))
    except (TypeError, ValueError):
        p = 0.5
    return a.get("answer"), p


def correct(r):
    if isinstance(r["label"], bool):
        p = p_true(r)
        return None if p is None else ((p >= 0.5) == r["label"])
    c, _ = choice(r)
    return None if c is None else c == r["label"]


def auroc(rs):
    pos = [p_true(r) for r in rs if r["label"] is True and p_true(r) is not None]
    neg = [p_true(r) for r in rs if r["label"] is False and p_true(r) is not None]
    if not pos or not neg:
        return None
    s = 0
    for a in pos:
        for b in neg:
            s += 1 if a > b else 0.5 if a == b else 0
    return s / (len(pos) * len(neg))


def summary(rs):
    ok = [correct(r) for r in rs]
    n = len([o for o in ok if o is not None])
    acc = sum(1 for o in ok if o) / len(rs) if rs else None  # missing answers count as wrong
    lat = [r["latency"] for r in rs if r.get("latency")]
    cost = sum((r.get("usage") or {}).get("cost") or 0 for r in rs)
    return {"n": len(rs), "answered": n, "acc": acc, "auroc": auroc(rs) if rs and isinstance(rs[0]["label"], bool) else None,
            "lat_med": statistics.median(lat) if lat else None, "cost": cost}
