#!/usr/bin/env python3
"""
Install git hooks for automatic index updates.

This script installs a pre-commit hook that automatically updates
the entries_index.json and syncs candidate_words.json whenever
entries are committed.

Usage:
    python build/install_hooks.py
"""

from pathlib import Path
import stat


HOOK_CONTENT = '''#!/bin/sh
# Auto-update dictionary indexes before commit
# Installed by build/install_hooks.py

# Check if any entry files are being committed
if git diff --cached --name-only | grep -q "^entries/"; then
    echo "Entry files changed, updating indexes..."
    python build/update_indexes.py

    # Stage the updated index files
    git add entries_index.json
    if [ -f candidate_words.json ]; then
        git add candidate_words.json
    fi
fi
'''


def main():
    git_dir = Path('.git')
    if not git_dir.exists():
        print("Error: Not in a git repository")
        return False

    hooks_dir = git_dir / 'hooks'
    hooks_dir.mkdir(exist_ok=True)

    hook_file = hooks_dir / 'pre-commit'

    # Check if hook already exists
    if hook_file.exists():
        print(f"Warning: {hook_file} already exists")
        response = input("Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("Aborted")
            return False

    # Write hook
    with open(hook_file, 'w') as f:
        f.write(HOOK_CONTENT)

    # Make executable
    hook_file.chmod(hook_file.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    print(f"Installed pre-commit hook: {hook_file}")
    print("\nThe hook will automatically update indexes when entry files are committed.")
    return True


if __name__ == '__main__':
    main()
