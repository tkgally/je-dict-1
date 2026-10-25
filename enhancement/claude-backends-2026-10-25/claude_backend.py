"""Headless Claude (`claude -p`) as a drop-in for review_runner.call_openrouter.

Runs on the Claude subscription the CLI is logged in with (no API key). The call is stripped
to a bare completion: our own system prompt, no tools, no MCP servers, no settings or
CLAUDE.md, no saved session, so the fixed overhead is about 1,300 input tokens.

call_claude() returns an OpenRouter-shaped dict ({"choices": [{"message": {"content": …}}]})
so review_runner.parse_model_response() reads it unchanged, plus "usage" (tokens, the CLI's
list-price cost estimate) and "wall_s"."""
import json
import subprocess
import time

SYSTEM = ("You are a meticulous bilingual Japanese-English lexicographer. Follow the user's "
          "instructions exactly and reply with only the requested JSON.")


def call_claude(prompt, model="sonnet", effort=None, system=SYSTEM, timeout=600, retries=2):
    cmd = ["claude", "-p", "--model", model, "--output-format", "json",
           "--system-prompt", system, "--tools", "", "--strict-mcp-config",
           "--setting-sources", "", "--no-session-persistence"]
    if effort:
        cmd += ["--effort", effort]
    last = None
    for attempt in range(retries + 1):
        t0 = time.time()
        try:
            p = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                               timeout=timeout, cwd="/tmp")
            d = json.loads(p.stdout)
        except (subprocess.TimeoutExpired, json.JSONDecodeError) as ex:
            last = {"error": f"{type(ex).__name__}: {str(ex)[:200]}"}
            time.sleep(5 * (attempt + 1))
            continue
        wall = time.time() - t0
        if d.get("is_error"):
            last = {"error": str(d.get("result"))[:300], "wall_s": wall}
            time.sleep(10 * (attempt + 1))
            continue
        u = d.get("usage") or {}
        return {
            "choices": [{"message": {"content": d.get("result") or ""}}],
            "usage": {
                "input_tokens": u.get("input_tokens", 0),
                "cache_creation_input_tokens": u.get("cache_creation_input_tokens", 0),
                "cache_read_input_tokens": u.get("cache_read_input_tokens", 0),
                "output_tokens": u.get("output_tokens", 0),
                "list_cost_usd": d.get("total_cost_usd"),
                "models": list((d.get("modelUsage") or {}).keys()),
            },
            "wall_s": wall,
            "api_ms": d.get("duration_api_ms"),
        }
    return last
