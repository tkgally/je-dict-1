#!/usr/bin/env python3
"""
Build script for je-dict-1 dictionary.

Validates entries and builds the static HTML site.
"""

import sys
from pathlib import Path
from validate import validate_all_entries
from build_flat import build_flat


def build(project_root: Path) -> int:
    """
    Main build process.
    Returns 0 on success, 1 on failure.
    """
    print("je-dict-1 Build")
    print("=" * 50)

    # Step 1: Validate all entries
    print("\n[1/2] Validating entries...")
    total, valid, invalid_files, cross_ref_warnings, missing_audio, orphaned_audio = validate_all_entries(project_root)

    if invalid_files:
        print(f"  ERROR: {len(invalid_files)} invalid file(s) found")
        print("  Run validate.py for details")
        return 1

    if cross_ref_warnings:
        print(f"  WARNING: {len(cross_ref_warnings)} cross-reference issue(s) found")
        print("  Run validate.py for details")

    if missing_audio:
        print(f"  WARNING: {len(missing_audio)} missing audio file(s)")

    if orphaned_audio:
        print(f"  WARNING: {len(orphaned_audio)} orphaned audio file(s)")

    if total == 0:
        print("  WARNING: No entry files found")
        # Continue anyway to create empty dictionary

    print(f"  OK: {valid} entries validated")

    # Step 2: Build the static HTML site
    print("\n[2/2] Building static HTML site...")
    result = build_flat(project_root)

    if result != 0:
        print("\nERROR: Build failed")
        return 1

    return 0


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    sys.exit(build(project_root))


if __name__ == '__main__':
    main()
