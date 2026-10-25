#!/usr/bin/env python3
"""Headless Claude (`claude -p`) as a model backend, billed to the Claude subscription.

A model id of the form ``claude:<model>`` (``claude:opus``, ``claude:haiku``) passed to
``review_runner.call_openrouter`` is sent here instead of OpenRouter, so every script built on
that plumbing (review_accuracy.py, review_links.py, check_conjugations.py) can use Claude with no
other change. Chosen 2026-10-25 (enhancement/claude-backends-2026-10-25/REPORT.md): Opus 5.5,
one entry per call, matched gpt-6.1-sol as an accuracy reviewer and found a different quarter of
the errors; Opus matched sol on kana-link judgments where gemini-2.5-flash fell far behind;
Haiku 5.5 was perfect on conjugation forms. Sonnet 5.5 and batched or subagent reviews were
clearly worse.

Each call is a bare completion: our own system prompt, no tools, no MCP servers, no settings or
CLAUDE.md, no saved session (about 1,300 tokens of overhead). The reply is returned in the
OpenRouter response shape, so ``review_runner.parse_model_response`` reads it unchanged.

Subscription guard. The Routine's own sessions run on the same subscription, so these calls must
never exhaust it. Every call asks for the stream-json output, which carries the plan's
rate-limit windows; once the five-hour or seven-day utilization reaches the limits in
pipeline/routine-config.json (``claude.five_hour_max``, ``claude.seven_day_max``), or the plan
reports anything but "allowed", every later call in the process returns None at once (the
callers treat that as a failed call) and ``stopped_reason()`` says why.

``usage_line()`` summarizes the process's calls (tokens, list-price equivalent, the last
utilization reading) for the run log; the list-price figure is not billed on a subscription.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path

PREFIX = "claude:"
ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "pipeline" / "routine-config.json"
DEFAULT_LIMITS = {"five_hour_max": 0.70, "seven_day_max": 0.85}
SYSTEM = ("You are a meticulous bilingual Japanese-English lexicographer. Follow the user's "
          "instructions exactly and reply with only the requested output.")
EFFORT = "high"  # the setting the 2026-10-25 comparison ran with

_lock = threading.Lock()
_state = {"stopped": None, "five_hour": None, "seven_day": None, "calls": 0, "failed": 0,
          "tokens_in": 0, "tokens_out": 0, "list_usd": 0.0}


def is_claude(model) -> bool:
    return str(model or "").startswith(PREFIX)


def cli_model(model: str) -> str:
    return str(model)[len(PREFIX):] or "opus"


def limits() -> dict:
    try:
        cfg = json.loads(CONFIG.read_text(encoding="utf-8")).get("claude") or {}
    except (OSError, ValueError):
        cfg = {}
    return {k: float(cfg.get(k, v)) for k, v in DEFAULT_LIMITS.items()}


def stopped_reason() -> str | None:
    return _state["stopped"]


def available() -> tuple[bool, str]:
    """(usable, reason): the CLI is installed and the guard has not stopped this process."""
    if not shutil.which("claude"):
        return False, "the claude CLI is not installed"
    if _state["stopped"]:
        return False, _state["stopped"]
    return True, ""


def note_rate_limit(info: dict) -> None:
    """Record one rate_limit_event and stop further calls when a window is too full."""
    windows = (info or {}).get("unifiedWindows") or {}
    lim = limits()
    with _lock:
        for key, wkey in (("five_hour", "five_hour"), ("seven_day", "seven_day")):
            u = (windows.get(wkey) or {}).get("utilization")
            if u is not None:
                _state[key] = float(u)
        reasons = []
        status = (info or {}).get("status")
        if status and status != "allowed":
            reasons.append(f"subscription status '{status}'")
        if _state["five_hour"] is not None and _state["five_hour"] >= lim["five_hour_max"]:
            reasons.append(f"five-hour window at {_state['five_hour']:.0%} "
                           f"(limit {lim['five_hour_max']:.0%})")
        if _state["seven_day"] is not None and _state["seven_day"] >= lim["seven_day_max"]:
            reasons.append(f"seven-day window at {_state['seven_day']:.0%} "
                           f"(limit {lim['seven_day_max']:.0%})")
        if reasons and not _state["stopped"]:
            _state["stopped"] = "subscription guard: " + "; ".join(reasons)
            print(f"  claude backend stopped: {_state['stopped']}", file=sys.stderr)


def parse_stream(stdout: str) -> tuple[dict | None, dict | None]:
    """(result event, last rate_limit_info) from `claude -p --output-format stream-json` output."""
    result = info = None
    for line in stdout.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if ev.get("type") == "result":
            result = ev
        elif ev.get("type") == "rate_limit_event":
            info = ev.get("rate_limit_info")
    return result, info


def to_response(result: dict, wall: float) -> dict:
    """An OpenRouter-shaped response from a stream-json result event."""
    u = result.get("usage") or {}
    tin = (u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
           + u.get("cache_read_input_tokens", 0))
    return {"choices": [{"message": {"content": result.get("result") or ""}}],
            "usage": {"prompt_tokens": tin, "completion_tokens": u.get("output_tokens", 0),
                      "list_usd": result.get("total_cost_usd") or 0.0},
            "model": ",".join((result.get("modelUsage") or {}).keys()),
            "wall_s": round(wall, 2)}


def call(prompt: str, model: str = "claude:opus", timeout: int = 600, retries: int = 1,
         system: str = SYSTEM, effort: str | None = EFFORT, runner=subprocess.run) -> dict | None:
    """One headless call. Returns an OpenRouter-shaped dict, or None on failure or guard stop."""
    ok, why = available()
    if not ok:
        return None
    cmd = ["claude", "-p", "--model", cli_model(model), "--output-format", "stream-json",
           "--verbose", "--system-prompt", system, "--tools", "", "--strict-mcp-config",
           "--setting-sources", "", "--no-session-persistence"]
    if effort:
        cmd += ["--effort", effort]
    for attempt in range(retries + 1):
        t0 = time.time()
        try:
            p = runner(cmd, input=prompt, capture_output=True, text=True, timeout=timeout, cwd="/tmp")
        except (subprocess.TimeoutExpired, OSError) as ex:
            print(f"  claude call failed: {type(ex).__name__}", file=sys.stderr)
            continue
        result, info = parse_stream(p.stdout or "")
        if info:
            note_rate_limit(info)
        if result and not result.get("is_error") and result.get("result") is not None:
            resp = to_response(result, time.time() - t0)
            with _lock:
                _state["calls"] += 1
                _state["tokens_in"] += resp["usage"]["prompt_tokens"]
                _state["tokens_out"] += resp["usage"]["completion_tokens"]
                _state["list_usd"] += resp["usage"]["list_usd"]
            return resp
        err = (result or {}).get("result") or (p.stderr or "")[-300:]
        print(f"  claude call error: {str(err)[:200]}", file=sys.stderr)
        if _state["stopped"]:
            break
        if attempt < retries:
            time.sleep(10)
    with _lock:
        _state["failed"] += 1
    return None


def usage_line() -> str:
    s = _state
    util = ""
    if s["five_hour"] is not None:
        util = f", five-hour window {s['five_hour']:.0%}, seven-day {s['seven_day'] or 0:.0%}"
    stop = f"; STOPPED ({s['stopped']})" if s["stopped"] else ""
    return (f"CLAUDE_USAGE calls={s['calls']} failed={s['failed']} tokens_in={s['tokens_in']} "
            f"tokens_out={s['tokens_out']} list_equivalent_usd={s['list_usd']:.2f}{util}{stop}")
