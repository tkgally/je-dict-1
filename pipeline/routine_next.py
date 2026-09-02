#!/usr/bin/env python3
"""Mode selector for the unified improvement Routine (je-dict-1).

Picks ONE focus ("mode") for the current Routine run using a deterministic
debt-based weighted scheduler with bounded health nudges, then emits the choice
as JSON on stdout for prompts/routine2.md to act on.

Modes: polish, systemic-fix, accuracy-review, new-entries, candidates, wiki.
`candidates` self-suppresses while the candidate queue is sufficiently stocked;
`systemic-fix` self-suppresses with no open batch-ready backlog item;
`accuracy-review` self-suppresses when the OpenRouter daily cap is spent; `wiki`
has weight 0 and runs only when its trigger fires (unharvested observations
above the threshold and at least N days since the last wiki run), at the
effective weight given in config "floors".

Design: enhancement/unified-routine-plan-2026-06-09.md §4.

Determinism: there is no randomness. Each enabled mode accrues "debt" equal to
its (nudged, normalized) weight every run and resets to 0 when chosen; the
highest-debt eligible mode wins. Over many runs the realized mode proportions
converge to the configured weights, so the weekly mix is predictable and
auditable.

Usage:
    python3 pipeline/routine_next.py                # select, persist state, print JSON
    python3 pipeline/routine_next.py --dry-run      # select, print JSON, persist nothing
    python3 pipeline/routine_next.py --explain      # human-readable breakdown (no persist)
    python3 pipeline/routine_next.py --simulate 42  # in-memory: mode distribution over N runs
    python3 pipeline/routine_next.py --force-mode polish   # force a mode (no persist; manual testing)
"""
import argparse
import glob
import json
import re
import sys
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PIPELINE_DIR = PROJECT_ROOT / "pipeline"

CONFIG_FILE = PIPELINE_DIR / "routine-config.json"
STATE_FILE = PIPELINE_DIR / "routine-state.json"
LEDGER_FILE = PIPELINE_DIR / "openrouter-ledger.json"

ENTRIES_INDEX = PROJECT_ROOT / "entries_index.json"
CANDIDATES_FILE = PROJECT_ROOT / "candidate_words.json"
OBSERVATIONS_FILE = PROJECT_ROOT / "polishing" / "observations.md"
COMPREHENSIVE_PROGRESS = PROJECT_ROOT / "polishing" / "tasks" / "comprehensive" / "progress.txt"
XMODEL_PROGRESS = PROJECT_ROOT / "polishing" / "tasks" / "cross-model-review" / "progress.txt"
REVIEWS_DIR = PROJECT_ROOT / "reviews"
BACKLOG_QUEUE = PROJECT_ROOT / "planning" / "wiki" / "ideas" / "backlog-queue.json"

ALL_MODES = ["polish", "systemic-fix", "accuracy-review", "new-entries",
             "candidates", "wiki"]

DEFAULT_CONFIG = {
    "enabled_modes": ["polish", "systemic-fix", "accuracy-review", "new-entries",
                      "candidates", "wiki"],
    "weights": {
        "polish": 0.30,
        "systemic-fix": 0.25,
        "accuracy-review": 0.30,
        "new-entries": 0.10,
        "candidates": 0.05,
        "wiki": 0.0,
    },
    "floors": {"wiki": 0.15},
    "nudges": {
        "candidate_high_threshold": 400,
        "candidate_low_threshold": 40,
        "candidate_restock_threshold": 100,
        "seen_in_entry_high_threshold": 50,
        "observations_unharvested_lines": 40,
        "wiki_min_days_between_runs": 7,
        "min_multiplier": 0.5,
        "max_multiplier": 2.0,
    },
    "anti_repeat_modes": ["new-entries", "accuracy-review", "systemic-fix",
                          "candidates", "wiki"],
    "anti_repeat_override_multiplier": 1.8,
    "openrouter": {"daily_cap_usd": 5.0, "per_session_cap_usd": 2.5,
                   "self_check_cap_usd": 0.25},
}

STATE_DOC = "Auto-managed by pipeline/routine_next.py. Do not hand-edit."


# --------------------------------------------------------------------------- #
# IO helpers
# --------------------------------------------------------------------------- #
def today_str():
    return datetime.now(timezone.utc).date().isoformat()


def now_iso():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_json(path, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return deepcopy(default)


def write_json(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


def load_config():
    """Load config, filling any missing top-level keys from DEFAULT_CONFIG."""
    cfg = load_json(CONFIG_FILE, DEFAULT_CONFIG)
    merged = deepcopy(DEFAULT_CONFIG)
    for k, v in cfg.items():
        if isinstance(v, dict) and isinstance(merged.get(k), dict):
            merged[k].update(v)
        else:
            merged[k] = v
    return merged


def load_state():
    st = load_json(STATE_FILE, {})
    st.setdefault("debt", {})
    for m in ALL_MODES:
        st["debt"].setdefault(m, 0.0)
    st.setdefault("history", [])
    st.setdefault("last_run_mode", None)
    st.setdefault("day_tally", {"date": None})
    return st


def parse_next(path):
    """Return the integer after the first 'next:' token, or None."""
    try:
        text = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    m = re.search(r"next:\s*(\d+)", text)
    return int(m.group(1)) if m else None


def load_backlog_queue():
    return load_json(BACKLOG_QUEUE, {"items": []})


def select_backlog_item(queue):
    """Return the highest-priority open, batch-ready backlog item, or None."""
    items = [it for it in queue.get("items", [])
             if it.get("status") == "open" and it.get("batch_ready")]
    if not items:
        return None
    return sorted(items, key=lambda it: it.get("priority", 9999))[0]


# --------------------------------------------------------------------------- #
# Health signals (all cheap, read from files already on disk)
# --------------------------------------------------------------------------- #
def compute_signals():
    cand = load_json(CANDIDATES_FILE, {})
    candidates = cand.get("candidates", []) if isinstance(cand, dict) else []
    candidate_count = len(candidates)
    seen = 0
    for c in candidates:
        try:
            if "seen in entry" in json.dumps(c, ensure_ascii=False):
                seen += 1
        except (TypeError, ValueError):
            pass

    idx = load_json(ENTRIES_INDEX, {})
    entries = idx.get("entries", []) if isinstance(idx, dict) else []
    max_id = None
    for e in entries:
        m = re.match(r"(\d+)", str(e.get("id", "")))
        if m:
            v = int(m.group(1))
            max_id = v if max_id is None else max(max_id, v)

    unharvested = 0
    if OBSERVATIONS_FILE.exists():
        for line in OBSERVATIONS_FILE.read_text(encoding="utf-8").splitlines():
            if re.match(r"\s*-\s*\[", line):
                unharvested += 1

    queue = load_backlog_queue()
    open_backlog = sum(1 for it in queue.get("items", [])
                       if it.get("status") == "open" and it.get("batch_ready"))

    return {
        "candidate_count": candidate_count,
        "seen_in_entry_count": seen,
        "max_entry_id": max_id,
        "comprehensive_next": parse_next(COMPREHENSIVE_PROGRESS),
        "cross_model_review_next": parse_next(XMODEL_PROGRESS),
        "unharvested_observations": unharvested,
        "open_backlog_items": open_backlog,
    }


def days_since_mode(state, mode):
    """Days since the most recent run of `mode` in the persisted history
    (a large number if it never ran)."""
    latest = None
    for h in state.get("history", []) or []:
        if h.get("mode") != mode:
            continue
        try:
            at = datetime.fromisoformat(str(h.get("at")).replace("Z", "+00:00"))
        except ValueError:
            continue
        if at.tzinfo is None:
            at = at.replace(tzinfo=timezone.utc)
        latest = at if latest is None or at > latest else latest
    if latest is None:
        return 9999.0
    return (datetime.now(timezone.utc) - latest).total_seconds() / 86400.0


# --------------------------------------------------------------------------- #
# OpenRouter ledger
# --------------------------------------------------------------------------- #
def read_ledger(config):
    """Load the ledger; reset spend if the date rolled over. Returns
    (ledger_obj, spent, cap, remaining, was_reset)."""
    cap = float(config["openrouter"]["daily_cap_usd"])
    ledger = load_json(
        LEDGER_FILE,
        {"date": None, "daily_cap_usd": cap, "spent_usd": 0.0, "calls": []},
    )
    was_reset = False
    if ledger.get("date") != today_str():
        ledger = {
            "_doc": ledger.get("_doc", ""),
            "date": today_str(),
            "daily_cap_usd": cap,
            "spent_usd": 0.0,
            "calls": [],
        }
        was_reset = True
    else:
        ledger["daily_cap_usd"] = cap  # keep synced to config
    spent = float(ledger.get("spent_usd", 0.0))
    remaining = max(0.0, cap - spent)
    return ledger, spent, cap, remaining, was_reset


# --------------------------------------------------------------------------- #
# Scheduler
# --------------------------------------------------------------------------- #
def normalized_weights(config):
    enabled = list(config["enabled_modes"])
    w = {m: float(config["weights"].get(m, 0.0)) for m in enabled}
    s = sum(w.values()) or 1.0
    return {m: w[m] / s for m in enabled}, enabled


def compute_multipliers(signals, config, remaining):
    """Bounded health multipliers per mode. accuracy-review is suppressed to 0
    when the daily OpenRouter budget is exhausted."""
    nz = config["nudges"]
    lo, hi = float(nz["min_multiplier"]), float(nz["max_multiplier"])

    def clamp(x):
        return max(lo, min(hi, x))

    mult = {m: 1.0 for m in ALL_MODES}
    reasons = {m: [] for m in ALL_MODES}

    # new-entries
    m = 1.0
    seen = signals.get("seen_in_entry_count")
    if seen is not None and seen >= nz["seen_in_entry_high_threshold"]:
        m *= 1.5
        reasons["new-entries"].append("seen-in-entry backlog high")
    cc = signals.get("candidate_count")
    if cc is not None and cc < nz["candidate_low_threshold"]:
        m *= 0.5
        reasons["new-entries"].append("candidates low (candidates mode restocks)")
    elif cc is not None and cc > nz["candidate_high_threshold"]:
        m *= 1.3
        reasons["new-entries"].append("candidates plentiful")
    mult["new-entries"] = clamp(m)

    # candidates (queue restock): hard suppression while the queue is
    # sufficiently stocked, so the mode only claims runs when there is real
    # restocking to do; boosted when the queue is nearly empty. Since the
    # 2026-08-11 cleanup the queue holds only vetted words, so the raw count
    # is a faithful signal of usable material.
    restock = nz.get("candidate_restock_threshold", 150)
    if cc is not None:
        if cc >= restock:
            mult["candidates"] = 0.0
            reasons["candidates"].append(
                f"queue sufficiently stocked ({cc} >= {restock})")
        elif cc < nz["candidate_low_threshold"]:
            mult["candidates"] = clamp(1.5)
            reasons["candidates"].append("queue low — restock urgent")

    # wiki: trigger-only. With weight 0 it never rotates; when the trigger
    # fires the mode runs once at the config "floors" effective weight.
    unharv = signals.get("unharvested_observations", 0) or 0
    days = signals.get("days_since_wiki", 9999.0)
    if days is None:
        days = 9999.0
    min_days = float(nz.get("wiki_min_days_between_runs", 7))
    if unharv >= nz["observations_unharvested_lines"] and days >= min_days:
        mult["wiki"] = 1.0
        reasons["wiki"].append(
            f"triggered: {unharv} unharvested observations, {days:.0f} days since last wiki run")
    else:
        mult["wiki"] = 0.0
        reasons["wiki"].append(
            f"not triggered ({unharv} unharvested < {nz['observations_unharvested_lines']} "
            f"or {days:.0f} days < {min_days:.0f})")

    # accuracy-review: hard suppression when out of budget
    if remaining <= 0:
        mult["accuracy-review"] = 0.0
        reasons["accuracy-review"].append("OpenRouter daily cap reached")

    # systemic-fix: hard suppression when there is no open, batch-ready backlog
    if signals.get("open_backlog_items", 0) <= 0:
        mult["systemic-fix"] = 0.0
        reasons["systemic-fix"].append("no open batch-ready backlog items")

    return mult, reasons


def select_mode(config, state, mult, forced=None):
    """Run one selection. Returns (choice, new_debt, eff, norm, enabled, source).

    On forced selection the debt dict is returned unchanged (forcing a mode for
    manual testing must not perturb the natural rotation)."""
    norm, enabled = normalized_weights(config)
    debt = {m: float(state["debt"].get(m, 0.0)) for m in ALL_MODES}
    floors = config.get("floors", {}) or {}
    eff = {}
    for m in enabled:
        eff[m] = norm[m] * mult.get(m, 1.0)
        if norm[m] <= 0 and mult.get(m, 0.0) > 0 and floors.get(m):
            eff[m] = float(floors[m]) * mult.get(m, 1.0)

    if forced is not None:
        return forced, debt, eff, norm, enabled, "forced"

    # Smooth weighted round robin: accrue each enabled mode's effective weight,
    # pick the highest-debt eligible mode, then subtract the total effective
    # weight from the winner (NOT reset to 0 — that would discard the fractional
    # remainder and systematically under-pick the heaviest mode). Subtracting the
    # total preserves the remainder, so long-run proportions equal eff/total.
    total = sum(eff[m] for m in enabled) or 1.0
    for m in enabled:
        debt[m] += eff[m]

    last = state.get("last_run_mode")
    override = float(config.get("anti_repeat_override_multiplier", 1.8))
    anti = set(config.get("anti_repeat_modes", []))
    eligible = []
    for m in enabled:
        if eff[m] <= 0:
            continue  # suppressed (e.g. budget exhausted)
        if m == last and m in anti and mult.get(m, 1.0) < override:
            continue  # anti-repeat: don't run a heavy mode twice in a row
        eligible.append(m)
    if not eligible:
        eligible = [m for m in enabled if eff[m] > 0]
    if not eligible:
        # Everything suppressed (no budget, stocked queue, no backlog): polish
        # is the one mode that always has work.
        eligible = ["polish"] if "polish" in enabled else [enabled[0]]

    def key(m):
        return (debt[m], norm.get(m, 0.0), -enabled.index(m))

    choice = max(eligible, key=key)
    debt[choice] -= total
    return choice, debt, eff, norm, enabled, "scheduler"


def build_params(choice, signals, config, remaining):
    if choice == "polish":
        return {"start_id": signals.get("comprehensive_next")}
    if choice == "new-entries":
        cc = signals.get("candidate_count")
        low = cc is not None and cc < config["nudges"]["candidate_low_threshold"]
        return {"prefer": "internal_closure", "approx_count": 20,
                "candidates_low": bool(low)}
    if choice == "accuracy-review":
        per = float(config["openrouter"]["per_session_cap_usd"])
        return {
            "start_id": signals.get("cross_model_review_next"),
            "openrouter_session_budget_usd": round(min(remaining, per), 2),
        }
    if choice == "candidates":
        cc = signals.get("candidate_count") or 0
        restock = config["nudges"].get("candidate_restock_threshold", 100)
        return {
            "approx_new": max(30, min(60, restock + 20 - cc)),
            "source": "internal_closure",
        }
    if choice == "wiki":
        return {}
    if choice == "systemic-fix":
        item = select_backlog_item(load_backlog_queue())
        if not item:
            return {"backlog_item": None,
                    "note": "No open batch-ready backlog item."}
        return {"backlog_item": {k: item.get(k) for k in
                                 ("id", "title", "detect", "filter", "fix_type",
                                  "verify", "source", "severity", "scope_estimate",
                                  "notes")}}
    return {}


def build_reason(choice, source, reasons, eff):
    bits = []
    if source == "forced":
        bits.append("forced via --force-mode")
    else:
        bits.append(f"highest scheduler debt among eligible modes")
    if reasons.get(choice):
        bits.append("; ".join(reasons[choice]))
    return f"{choice}: " + "; ".join(bits)


# --------------------------------------------------------------------------- #
# Persistence
# --------------------------------------------------------------------------- #
def persist(state, choice, debt, ledger):
    state["_doc"] = STATE_DOC
    state["debt"] = {m: round(debt.get(m, 0.0), 6) for m in ALL_MODES}
    state["last_run_mode"] = choice
    hist = state.get("history", [])
    hist.append({"at": now_iso(), "mode": choice})
    state["history"] = hist[-20:]
    dt = state.get("day_tally", {}) or {}
    if dt.get("date") != today_str():
        dt = {"date": today_str()}
    dt[choice] = int(dt.get(choice, 0)) + 1
    state["day_tally"] = dt
    write_json(STATE_FILE, state)
    write_json(LEDGER_FILE, ledger)


# --------------------------------------------------------------------------- #
# Output modes
# --------------------------------------------------------------------------- #
def run_simulate(config, state, signals, remaining, n):
    sim = deepcopy(state)
    mult, _ = compute_multipliers(signals, config, remaining)
    tally = {}
    for _ in range(n):
        choice, debt, _eff, _norm, _enabled, _src = select_mode(config, sim, mult)
        sim["debt"] = debt
        sim["last_run_mode"] = choice
        tally[choice] = tally.get(choice, 0) + 1
    norm, enabled = normalized_weights(config)
    print(f"Simulated {n} runs (static current signals):\n")
    print(f"  {'mode':<16}{'picked':>8}{'realized':>12}{'base wt':>12}")
    print("  " + "-" * 46)
    for m in enabled:
        cnt = tally.get(m, 0)
        print(f"  {m:<16}{cnt:>8}{cnt / n * 100:>11.1f}%{norm[m] * 100:>11.1f}%")
    print()
    return tally


def run_explain(config, signals, state, ledger, spent, cap, remaining, mult, reasons,
                choice, debt_before, eff, source):
    print("=== routine_next: selection explanation ===\n")
    print("Signals:")
    for k, v in signals.items():
        print(f"  {k:<26} {v}")
    print(f"\nOpenRouter: spent ${spent:.2f} / cap ${cap:.2f}  (remaining ${remaining:.2f})")
    norm, enabled = normalized_weights(config)
    print(f"\n{'mode':<16}{'norm wt':>10}{'mult':>8}{'eff':>10}{'debt(before)':>14}")
    print("-" * 58)
    for m in enabled:
        flags = (" *suppressed" if eff.get(m, 0) <= 0 else "")
        print(f"{m:<16}{norm[m]:>10.3f}{mult.get(m,1.0):>8.2f}{eff.get(m,0):>10.3f}"
              f"{state['debt'].get(m,0.0):>14.3f}{flags}")
        if reasons.get(m):
            print(f"    nudge: {'; '.join(reasons[m])}")
    print(f"\nlast_run_mode: {state.get('last_run_mode')}  "
          f"(anti-repeat: {config.get('anti_repeat_modes')})")
    print(f"\n=> CHOICE: {choice}  ({source})")
    print(f"   {build_reason(choice, source, reasons, eff)}")
    print("\n(--explain does not persist state.)")


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description="Select the next Routine mode.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Select and print JSON but persist nothing.")
    ap.add_argument("--explain", action="store_true",
                    help="Human-readable breakdown of the decision (no persist).")
    ap.add_argument("--simulate", type=int, metavar="N",
                    help="Print the mode distribution over N in-memory runs (no persist).")
    ap.add_argument("--force-mode", metavar="MODE", choices=ALL_MODES,
                    help="Force a specific mode (no persist; for manual testing).")
    args = ap.parse_args()

    config = load_config()
    state = load_state()
    signals = compute_signals()
    signals["days_since_wiki"] = round(days_since_mode(state, "wiki"), 1)
    ledger, spent, cap, remaining, _reset = read_ledger(config)

    if args.simulate is not None:
        run_simulate(config, state, signals, remaining, args.simulate)
        return 0

    mult, reasons = compute_multipliers(signals, config, remaining)
    debt_before = deepcopy(state["debt"])
    choice, debt, eff, norm, enabled, source = select_mode(
        config, state, mult, forced=args.force_mode
    )

    if args.explain:
        run_explain(config, signals, state, ledger, spent, cap, remaining,
                    mult, reasons, choice, debt_before, eff, source)
        return 0

    params = build_params(choice, signals, config, remaining)
    output = {
        "mode": choice,
        "params": params,
        "reason": build_reason(choice, source, reasons, eff),
        "signals": signals,
        "openrouter": {
            "spent_today_usd": round(spent, 4),
            "daily_cap_usd": round(cap, 2),
            "remaining_usd": round(remaining, 4),
            "session_budget_usd": params.get("openrouter_session_budget_usd"),
        },
        "generated_at": now_iso(),
        "source": source,
        "state_persisted": not (args.dry_run or args.force_mode),
    }

    if not args.dry_run and not args.force_mode:
        persist(state, choice, debt, ledger)

    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
