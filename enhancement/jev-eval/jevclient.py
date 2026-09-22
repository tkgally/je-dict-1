"""Minimal client for TypeSafe Jev via OpenRouter's decisions endpoint, with a cost ledger."""
import json, os, sys, time, threading, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

URL = "https://openrouter.ai/api/alpha/decisions"
MODEL = "typesafe/jev-1.13"
LEDGER = Path(__file__).with_name("ledger.json")
_lock = threading.Lock()

def _load():
    if LEDGER.exists():
        for _ in range(5):
            try:
                return json.loads(LEDGER.read_text())
            except Exception:
                time.sleep(0.05)
    return {"calls": 0, "cost": 0.0, "input_tokens": 0, "output_tokens": 0, "errors": 0, "by_test": {}}

def _add(test, usage, err=False):
    with _lock:
        L = _load()
        L["calls"] += 1
        t = L["by_test"].setdefault(test, {"calls": 0, "cost": 0.0, "input_tokens": 0, "errors": 0})
        t["calls"] += 1
        if err:
            L["errors"] += 1; t["errors"] += 1
        if usage:
            L["cost"] += usage.get("cost", 0.0); t["cost"] += usage.get("cost", 0.0)
            L["input_tokens"] += usage.get("input_tokens", 0); t["input_tokens"] += usage.get("input_tokens", 0)
            L["output_tokens"] += usage.get("output_tokens", 0)
        tmp = LEDGER.with_suffix(".tmp")
        tmp.write_text(json.dumps(L, indent=1)); os.replace(tmp, LEDGER)

def total_cost():
    with _lock:
        for _ in range(3):
            try:
                return _load()["cost"]
            except Exception:
                time.sleep(0.05)
        return -1.0

def decide(state, questions, test="misc", model=MODEL, timeout=120, retries=4):
    """POST one decisions request. Returns the parsed JSON (answers/usage) or {'error': ...}."""
    key = os.environ["OPENROUTER_API_KEY"]
    body = json.dumps({"model": model, "state": state, "questions": questions}, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(URL, data=body, method="POST", headers={
        "Authorization": f"Bearer {key}", "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/tkgally/je-dict-1", "X-Title": "je-dict-1 jev evaluation"})
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = json.loads(r.read().decode("utf-8"))
            _add(test, data.get("usage"))
            return data
        except urllib.error.HTTPError as e:
            txt = e.read().decode("utf-8", "replace")[:500]
            last = f"HTTP {e.code}: {txt}"
            if e.code in (429, 500, 502, 503, 529) and attempt < retries - 1:
                time.sleep(2 ** (attempt + 1)); continue
            break
        except Exception as e:  # network
            last = repr(e)
            if attempt < retries - 1:
                time.sleep(2 ** (attempt + 1)); continue
    _add(test, None, err=True)
    return {"error": last}

def run_batch(items, fn, workers=6, label=""):
    """items: list; fn(item) -> result. Runs in a thread pool, preserving order."""
    out = [None] * len(items)
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(fn, it): i for i, it in enumerate(items)}
        done = 0
        for f in as_completed(futs):
            out[futs[f]] = f.result(); done += 1
            if done % 50 == 0:
                print(f"  {label} {done}/{len(items)} cost so far ${total_cost():.4f}", file=sys.stderr)
    return out
