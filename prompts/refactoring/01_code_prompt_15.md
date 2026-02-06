# Code & Structure — Prompt 15: Create a GitHub Actions CI workflow

**Source:** Agent 1 Report (Code & Structure), Prompt 15
**Priority:** Medium
**Effort:** Low

---

In je-dict-1, there is no CI/CD pipeline. Create a GitHub Actions workflow at
.github/workflows/validate.yml that runs on every push and pull request:

1. Checkout the repository
2. Set up Python 3.10+
3. Install dependencies from build/requirements.txt
4. Run python3 build/validate.py
5. Report success/failure

This should be a minimal validation workflow -- it does NOT need to build the site
(that's too expensive for CI). Just validate entry data integrity.

Keep the workflow simple and fast.
