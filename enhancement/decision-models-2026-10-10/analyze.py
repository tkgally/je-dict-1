"""Aggregate results into summary.json for the report."""
import collections
import hashlib
import json
import statistics

from score import load_res, p_true, choice, correct, auroc, summary

DEC = ["openai/gpt-6-luna-decisions", "upstage/solar-decide", "upstage/solar-decide-flash", "cloudflare/clef",
       "cloudflare/clef-omni", "cloudflare/clef-flash", "perplexity/pplx-decider-v1.1-27b", "liquid/d1",
       "inception/mercury-decide", "microsoft/microsoft-decision-1", "nace-ai/drex-v1.5", "typesafe/jev-1.13",
       "jaredpalmer/kev-4b", "togethercomputer/tev1-4b-experimental", "respan/span-01", "respan/span-01-lite"]
LLM = ["google/gemini-2.5-flash", "openai/gpt-6-luna", "anthropic/claude-haiku-5.5", "openai/gpt-6.1-sol"]
TASKS = ["furigana", "links", "flags", "conjugation", "translation", "transitivity", "sense"]
TARGET = 0.97


def fold(i):
    return int(hashlib.md5(i.encode()).hexdigest(), 16) % 2


def score_of(r):
    """(predicted label, confidence-ish score used for thresholds)."""
    if isinstance(r["label"], bool):
        return p_true(r)
    c, p = choice(r)
    return p


def fit_two_sided(rs, target):
    """Best (lo, hi) on noul p so auto-decided items reach target agreement; max coverage."""
    pl = [(p_true(r), r["label"]) for r in rs if p_true(r) is not None]
    ps = sorted({p for p, _ in pl})
    best = (-1, 1.01, 0)
    for lo in [-1] + ps:
        low = [l for p, l in pl if p <= lo]
        low_ok = sum(1 for l in low if not l)
        for hi in ps + [1.01]:
            if hi <= lo:
                continue
            high = [l for p, l in pl if p >= hi]
            n = len(low) + len(high)
            if n <= best[2]:
                continue
            ok = low_ok + sum(1 for l in high if l)
            if ok / n >= target:
                best = (lo, hi, n)
    return best[:2]


def fit_choice(rs, target):
    ps = sorted({score_of(r) for r in rs if score_of(r) is not None})
    best = (1.01, 0)
    for t in ps:
        auto = [r for r in rs if score_of(r) is not None and score_of(r) >= t]
        ok = sum(1 for r in auto if correct(r))
        if auto and ok / len(auto) >= target and len(auto) > best[1]:
            best = (t, len(auto))
    return best[0]


def triage(rs, target=TARGET):
    """2-fold cross-validated coverage and accuracy of the auto-decided share."""
    if not rs:
        return None
    noul = isinstance(rs[0]["label"], bool)
    auto_n = ok_n = 0
    for f in (0, 1):
        train = [r for r in rs if fold(r["id"]) != f]
        test = [r for r in rs if fold(r["id"]) == f]
        if noul:
            lo, hi = fit_two_sided(train, target)
            auto = [r for r in test if p_true(r) is not None and (p_true(r) <= lo or p_true(r) >= hi)]
            ok = sum(1 for r in auto if (p_true(r) >= hi) == r["label"])
        else:
            t = fit_choice(train, target)
            auto = [r for r in test if score_of(r) is not None and score_of(r) >= t]
            ok = sum(1 for r in auto if correct(r))
        auto_n += len(auto)
        ok_n += ok
    return {"coverage": auto_n / len(rs), "auto_acc": (ok_n / auto_n) if auto_n else None, "auto_n": auto_n}


def tuned_acc(rs):
    """2-fold CV accuracy with the yes/no cut-off tuned on the other fold (noul only)."""
    ok = 0
    for f in (0, 1):
        train = [(p_true(r), r["label"]) for r in rs if fold(r["id"]) != f and p_true(r) is not None]
        best_t, best = 0.5, -1
        for t in sorted({p for p, _ in train}) + [1.01]:
            a = sum(1 for p, l in train if (p >= t) == l)
            if a > best:
                best_t, best = t, a
        ok += sum(1 for r in rs if fold(r["id"]) == f and p_true(r) is not None and (p_true(r) >= best_t) == r["label"])
    return ok / len(rs)


def cascade(dec_rs, llm_rs, llm_cost_1k, dec_cost_1k, target=TARGET):
    """Decision model settles items outside the CV-fitted uncertainty band; the rest go to the LLM."""
    L = {r["id"]: r for r in llm_rs}
    rs = [r for r in dec_rs if r["id"] in L]
    noul = isinstance(rs[0]["label"], bool)
    ok = esc = 0
    for f in (0, 1):
        train = [r for r in rs if fold(r["id"]) != f]
        test = [r for r in rs if fold(r["id"]) == f]
        if noul:
            lo, hi = fit_two_sided(train, target)
        else:
            t = fit_choice(train, target)
        for r in test:
            p = p_true(r) if noul else score_of(r)
            settled = p is not None and ((p <= lo or p >= hi) if noul else p >= t)
            if settled:
                ok += (p >= hi) == r["label"] if noul else bool(correct(r))
            else:
                esc += 1
                ok += bool(correct(L[r["id"]]))
    n = len(rs)
    return {"acc": ok / n, "escalated": esc / n, "cost_per_1k": dec_cost_1k + esc / n * llm_cost_1k}


def ensemble(models, task):
    per = [{r["id"]: r for r in load_res(m, task)} for m in models]
    ids = set.intersection(*[set(p) for p in per])
    out = []
    for i in ids:
        rs = [p[i] for p in per]
        ps = [p_true(r) for r in rs]
        if None in ps:
            continue
        out.append({"id": i, "label": rs[0]["label"], "sub": rs[0].get("sub"),
                    "answer": {"noul": statistics.mean(ps)}})
    return out


def main():
    S = {"tasks": {}, "models": {"decision": DEC, "llm": LLM}}
    # screening
    scr = {}
    for m in DEC + LLM:
        rs = load_res(m, "screen")
        by = collections.defaultdict(list)
        for r in rs:
            by[r.get("kind")].append(r)
        scr[m] = {k: summary(v)["acc"] for k, v in by.items()}
        scr[m]["lat_med"] = summary(rs)["lat_med"] if rs else None
    S["screen"] = scr
    for t in TASKS:
        T = {}
        for m in DEC + LLM:
            rs = load_res(m, t)
            if not rs:
                continue
            s = summary(rs)
            subs = collections.defaultdict(list)
            for r in rs:
                key = (r.get("sub") or "").split(":")[0]
                if t == "links":
                    key = r["sub"].split(":")[0]
                subs[key].append(r)
            s["by_sub"] = {k: sum(1 for r in v if correct(r)) / len(v) for k, v in subs.items()}
            s["triage"] = triage(rs)
            s["tuned_acc"] = tuned_acc(rs) if isinstance(rs[0]["label"], bool) else s["acc"]
            s["cost_per_1k"] = 1000 * s["cost"] / len(rs)
            bl = [r.get("batch_latency") for r in rs if r.get("batch_latency")]
            s["batch_lat_med"] = statistics.median(bl) if bl else None
            if not isinstance(rs[0]["label"], bool):
                cm = collections.Counter((r["label"], choice(r)[0]) for r in rs)
                s["confusion"] = {f"{a}->{b}": n for (a, b), n in cm.items()}
            T[m] = s
        # ensemble of top-3 decision models by AUROC (noul tasks)
        noul = isinstance(load_res(DEC[0], t)[0]["label"], bool) if load_res(DEC[0], t) else False
        if noul:
            ranked = sorted([m for m in DEC if m in T and T[m]["auroc"]], key=lambda m: -T[m]["auroc"])[:3]
            ers = ensemble(ranked, t)
            es = summary(ers)
            es["triage"] = triage(ers)
            es["members"] = ranked
            es["cost_per_1k"] = sum(T[m]["cost_per_1k"] for m in ranked)
            T["ensemble"] = es
        best = max([m for m in DEC if m in T], key=lambda m: T[m]["acc"])
        T["_cascade"] = {"dec": best}
        for lm in LLM:
            if lm in T:
                T["_cascade"][lm] = cascade(load_res(best, t), load_res(lm, t), T[lm]["cost_per_1k"],
                                            T[best]["cost_per_1k"])
        S["tasks"][t] = T
    json.dump(S, open("summary.json", "w"), indent=1)
    # console table
    for t in TASKS:
        print(f"\n== {t}")
        print("cascade", json.dumps(S["tasks"][t]["_cascade"]))
        rows = sorted([kv for kv in S["tasks"][t].items() if kv[0] != "_cascade"], key=lambda kv: -(kv[1]["acc"] or 0))
        for m, s in rows:
            tr = s.get("triage") or {}
            print(f"{m:40s} n={s['n']:3d} acc={s['acc']:.3f} auroc={(s['auroc'] or 0):.3f} "
                  f"tuned={s.get('tuned_acc') or 0:.3f} cov@97={tr.get('coverage', 0):.2f} ({(tr.get('auto_acc') or 0):.3f}) "
                  f"$/1k={s['cost_per_1k']:.4f} lat={s['lat_med'] or 0:.2f} "
                  + " ".join(f"{k}={v:.2f}" for k, v in sorted(s.get('by_sub', {}).items())))


if __name__ == "__main__":
    main()
