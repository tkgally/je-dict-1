# Code & Structure — Prompt 20: Create a pre-commit hook

**Source:** Agent 1 Report (Code & Structure), Prompt 20
**Priority:** Low
**Effort:** Low

---

In je-dict-1, there is an install_hooks.py script in build/ but it's unclear if any
hooks are active. Create a lightweight git pre-commit hook that:

1. Checks if any files in entries/ are staged for commit
2. If so, runs python3 build/validate.py on just those files (not the full validation)
3. Blocks the commit if validation fails
4. If no entry files are staged, skips validation (fast path)

Create the hook at .githooks/pre-commit and update the README or a setup script to
explain how to install it (git config core.hooksPath .githooks).

Keep it fast -- it should validate only changed entry files, not all 10,306.
