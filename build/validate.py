#!/usr/bin/env python3
"""
Validation script for je-dict-1 dictionary entries.

Validates all entry files against the JSON schema and checks additional
consistency rules (filename format, directory placement, ID uniqueness).
"""

import json
import sys
import re
import subprocess
from pathlib import Path
from typing import Optional

from path_utils import get_entry_prefix
from japanese_utils import (
    hiragana_to_romaji,
    get_expected_directory,
    KANA_TO_DIRECTORY,
)


def ensure_package(package_name: str) -> None:
    """Ensure a package is installed, installing it automatically if missing."""
    try:
        __import__(package_name)
    except ImportError:
        print(f"Installing required package: {package_name}...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package_name, "--quiet"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )


# Auto-install required packages
ensure_package("jsonschema")

import jsonschema
from jsonschema import Draft7Validator


def load_schema(schema_path: Path) -> dict:
    """Load the JSON schema."""
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate_entry_file(file_path: Path, schema: dict, all_ids: set) -> tuple[list[str], dict | None]:
    """
    Validate a single entry file.
    Returns a tuple of (error_messages, entry_data).
    If validation fails, entry_data may be None (for JSON errors) or the partial entry.
    """
    errors = []

    # Load the entry
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            entry = json.load(f)
    except json.JSONDecodeError as e:
        return [f"Invalid JSON: {e}"], None

    # Validate against schema
    validator = Draft7Validator(schema)
    schema_errors = list(validator.iter_errors(entry))
    for error in schema_errors:
        path = ' -> '.join(str(p) for p in error.absolute_path) if error.absolute_path else 'root'
        errors.append(f"Schema error at {path}: {error.message}")

    # If schema validation failed, skip additional checks
    if schema_errors:
        return errors, None

    # Check ID uniqueness
    entry_id = entry['id']
    if entry_id in all_ids:
        errors.append(f"Duplicate ID: {entry_id}")
    all_ids.add(entry_id)

    # Check filename matches ID
    expected_filename = f"{entry_id}.json"
    if file_path.name != expected_filename:
        errors.append(f"Filename mismatch: expected {expected_filename}, got {file_path.name}")

    # Check directory structure: entries/{kana}/{prefix}/{id}.json
    reading = entry['reading']
    expected_kana_dir = get_expected_directory(reading)
    expected_prefix_dir = get_entry_prefix(entry_id)

    # Parent is prefix directory, grandparent is kana directory
    actual_prefix_dir = file_path.parent.name
    actual_kana_dir = file_path.parent.parent.name

    if expected_prefix_dir and actual_prefix_dir != expected_prefix_dir:
        errors.append(f"Prefix directory mismatch: entry '{entry_id}' should be in '{expected_prefix_dir}/', not '{actual_prefix_dir}/'")

    if expected_kana_dir and actual_kana_dir != expected_kana_dir:
        errors.append(f"Kana directory mismatch: entry with reading '{reading}' should be in '{expected_kana_dir}/', not '{actual_kana_dir}/'")

    # Check ID romanization matches reading
    id_parts = entry_id.split('_')
    if len(id_parts) == 2:
        id_romaji = id_parts[0]
        expected_romaji = hiragana_to_romaji(reading)
        if id_romaji != expected_romaji:
            errors.append(f"ID romanization mismatch: '{id_romaji}' doesn't match reading '{reading}' (expected '{expected_romaji}')")

    return errors, entry


def check_for_duplicates(entries_data: list[tuple[Path, dict]]) -> list[tuple[Path, str]]:
    """
    Check for duplicate entries (same reading AND same headword).
    Entries with same reading but different headwords (homophones) are allowed.
    Returns a list of (file_path, error_message) for duplicates.
    """
    # Group entries by reading
    by_reading = {}
    for file_path, entry in entries_data:
        reading = entry.get('reading', '')
        headword = entry.get('headword', '')
        key = (reading, headword)
        if key not in by_reading:
            by_reading[key] = []
        by_reading[key].append(file_path)

    # Find duplicates (same reading AND headword)
    duplicates = []
    for (reading, headword), files in by_reading.items():
        if len(files) > 1:
            # Report all but the first as duplicates
            for dup_file in files[1:]:
                duplicates.append((
                    dup_file,
                    f"Duplicate entry: reading '{reading}' with headword '{headword}' already exists in {files[0]}"
                ))

    return duplicates


def is_valid_hiragana(text: str) -> bool:
    """Check if text contains only hiragana characters and long vowel mark."""
    if not text:
        return False
    for char in text:
        if not (('\u3041' <= char <= '\u3096') or char == 'ー'):
            return False
    return True


def validate_structured_cross_reference(ref: dict, entry_reading: str, entry_headword: str) -> list[str]:
    """
    Validate a structured cross-reference object.
    Returns a list of error messages (empty if valid).
    """
    errors = []
    valid_types = ['pair', 'synonym', 'antonym', 'keigo', 'related', 'see_also', 'contrast']

    # Check required fields
    if 'type' not in ref:
        errors.append("Missing 'type' in cross_reference")
    elif ref['type'] not in valid_types:
        errors.append(f"Invalid cross_reference type: '{ref['type']}' (must be one of: {', '.join(valid_types)})")

    if 'reading' not in ref:
        errors.append("Missing 'reading' in cross_reference")
    elif not is_valid_hiragana(ref['reading']):
        errors.append(f"Cross-reference reading must be hiragana: '{ref['reading']}'")
    else:
        # Check for self-reference: both reading AND headword must match
        # (Entries with same reading but different headwords are valid cross-references)
        ref_headword = ref.get('headword', '')
        if ref['reading'] == entry_reading and ref_headword == entry_headword:
            errors.append(f"Self-reference not allowed: '{ref['reading']}' with headword '{ref_headword}'")

    return errors


def check_timestamps(entries_data: list[tuple[Path, dict]]) -> list[tuple[Path, str]]:
    """
    Check entry timestamps for issues.

    Detects:
    - Future timestamps (created or modified time is in the future)
    - Suspiciously round timestamps (exactly on the hour, likely hardcoded)

    Returns a list of (file_path, warning_message) for issues found.
    """
    from datetime import datetime, timezone

    now = datetime.now(timezone.utc)
    warnings = []

    for file_path, entry in entries_data:
        metadata = entry.get('metadata', {})
        created = metadata.get('created', '')
        modified = metadata.get('modified', '')

        for field_name, timestamp_str in [('created', created), ('modified', modified)]:
            if not timestamp_str:
                continue

            try:
                # Parse ISO timestamp
                dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))

                # Check for future timestamp
                if dt > now:
                    warnings.append((
                        file_path,
                        f"Future timestamp in '{field_name}': {timestamp_str} is in the future"
                    ))

                # Check for suspiciously round timestamps (exactly on the hour with 00:00 seconds)
                # These are often hardcoded rather than generated dynamically
                if dt.minute == 0 and dt.second == 0:
                    warnings.append((
                        file_path,
                        f"Suspiciously round timestamp in '{field_name}': {timestamp_str} "
                        f"(exactly on the hour - may be hardcoded instead of using datetime.now())"
                    ))

            except (ValueError, AttributeError):
                warnings.append((
                    file_path,
                    f"Invalid timestamp format in '{field_name}': {timestamp_str}"
                ))

    return warnings


def check_cross_reference_semantics(entries_data: list[tuple[Path, dict]]) -> list[tuple[Path, str]]:
    """
    Check cross-references for semantic issues like homonym mismatches.

    This detects cases where:
    - A cross-reference specifies a headword
    - An entry with the same reading exists
    - But the existing entry has a DIFFERENT headword (wrong homonym)

    Returns a list of (file_path, warning_message) for issues found.
    """
    # Build reading-to-entries index
    from collections import defaultdict
    reading_index: dict[str, list[dict]] = defaultdict(list)
    for _, entry in entries_data:
        reading = entry.get('reading', '')
        if reading:
            reading_index[reading].append({
                'id': entry.get('id', ''),
                'headword': entry.get('headword', ''),
                'gloss': entry.get('gloss', '')
            })

    warnings = []
    for file_path, entry in entries_data:
        cross_refs = entry.get('cross_references', [])
        for ref in cross_refs:
            if not isinstance(ref, dict):
                continue

            ref_reading = ref.get('reading', '')
            ref_headword = ref.get('headword', '')
            ref_label = ref.get('label', '')

            if not ref_reading or not ref_headword:
                continue

            candidates = reading_index.get(ref_reading, [])
            if len(candidates) == 0:
                # No entry exists - this is fine, it's a forward reference
                continue

            # Check if any candidate matches the specified headword
            headword_match = any(c['headword'] == ref_headword for c in candidates)

            if not headword_match:
                # Homonym mismatch: entries exist with this reading but different headwords
                existing_headwords = [c['headword'] for c in candidates]
                existing_glosses = [c['gloss'] for c in candidates]
                label_info = f" ({ref_label})" if ref_label else ""
                warnings.append((
                    file_path,
                    f"Cross-reference homonym mismatch: reading '{ref_reading}' with headword "
                    f"'{ref_headword}'{label_info} not found. Existing entries: "
                    f"{', '.join(f'{hw} ({gl})' for hw, gl in zip(existing_headwords, existing_glosses))}"
                ))

    return warnings


def check_cross_references(entries_data: list[tuple[Path, dict]], all_ids: set, all_readings: set = None) -> list[tuple[Path, str]]:
    """
    Check cross_references for validity.
    Handles both legacy string format and new structured format.
    Returns a list of (file_path, error_message) for issues.
    """
    # Build reading index if not provided
    if all_readings is None:
        all_readings = set()
        for _, entry in entries_data:
            reading = entry.get('reading', '')
            if reading:
                all_readings.add(reading)

    errors = []
    for file_path, entry in entries_data:
        entry_reading = entry.get('reading', '')
        entry_headword = entry.get('headword', '')
        cross_refs = entry.get('cross_references', [])
        if cross_refs:
            for ref in cross_refs:
                if isinstance(ref, str):
                    # Legacy string format (entry ID)
                    if ref not in all_ids:
                        errors.append((
                            file_path,
                            f"Invalid cross_reference: '{ref}' does not exist"
                        ))
                elif isinstance(ref, dict):
                    # New structured format
                    ref_errors = validate_structured_cross_reference(ref, entry_reading, entry_headword)
                    for err in ref_errors:
                        errors.append((file_path, err))
                else:
                    errors.append((
                        file_path,
                        f"Invalid cross_reference format: expected string or object, got {type(ref).__name__}"
                    ))
    return errors


def validate_all_entries(project_root: Path) -> tuple[int, int, list[tuple[Path, list[str]]], list[tuple[Path, str]], list[tuple[Path, str]], list[tuple[Path, str]]]:
    """
    Validate all entry files in the project.

    Returns:
        (total_count, valid_count, invalid_files, cross_ref_errors, semantic_warnings, timestamp_warnings)
        - total_count: Total number of entry files found
        - valid_count: Number of valid entries
        - invalid_files: List of (file_path, error_list) for invalid files
        - cross_ref_errors: List of (file_path, error_message) for cross-reference issues
        - semantic_warnings: List of (file_path, warning_message) for semantic issues (homonym mismatches)
        - timestamp_warnings: List of (file_path, warning_message) for timestamp issues
    """
    schema_path = project_root / 'build' / 'schema.json'
    schema = load_schema(schema_path)

    entries_dir = project_root / 'entries'

    all_ids = set()
    total = 0
    valid = 0
    invalid_files = []
    entries_data = []  # Store (file_path, entry_data) for duplicate checking

    # Collect all JSON files
    entry_files = list(entries_dir.glob('**/*.json'))

    for file_path in entry_files:
        total += 1
        errors, entry = validate_entry_file(file_path, schema, all_ids)
        if errors:
            invalid_files.append((file_path, errors))
        else:
            valid += 1
            # Reuse the already-loaded entry for subsequent checks
            if entry is not None:
                entries_data.append((file_path, entry))

    # Check for duplicates among valid entries
    duplicate_errors = check_for_duplicates(entries_data)
    for file_path, error_msg in duplicate_errors:
        # Find if this file is already in invalid_files
        existing = next((i for i, (fp, _) in enumerate(invalid_files) if fp == file_path), None)
        if existing is not None:
            invalid_files[existing][1].append(error_msg)
        else:
            invalid_files.append((file_path, [error_msg]))
            valid -= 1

    # Check cross_references point to existing IDs
    # These are tracked separately as warnings (don't prevent build)
    cross_ref_errors = check_cross_references(entries_data, all_ids)

    # Check for semantic issues in cross-references (homonym mismatches)
    semantic_warnings = check_cross_reference_semantics(entries_data)

    # Check timestamps for issues (future timestamps, hardcoded times)
    timestamp_warnings = check_timestamps(entries_data)

    return total, valid, invalid_files, cross_ref_errors, semantic_warnings, timestamp_warnings


def validate_single_entry(entry_path: Path, project_root: Path) -> int:
    """
    Validate a single entry file.
    Returns 0 on success, 1 on failure.
    """
    schema_path = project_root / 'build' / 'schema.json'
    schema = load_schema(schema_path)

    # Get all existing IDs for cross-reference checking
    entries_dir = project_root / 'entries'
    all_ids = set()
    for file_path in entries_dir.glob('**/*.json'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                entry = json.load(f)
                all_ids.add(entry.get('id', ''))
        except (json.JSONDecodeError, IOError):
            pass

    print(f"Validating: {entry_path}")
    print("-" * 50)

    errors, entry = validate_entry_file(entry_path, schema, set())  # Don't check ID uniqueness for single entry

    # Check cross-references using the already-loaded entry
    if entry is not None:
        entry_reading = entry.get('reading', '')
        entry_headword = entry.get('headword', '')
        cross_refs = entry.get('cross_references', [])
        for ref in cross_refs:
            if isinstance(ref, str):
                # Legacy string format
                if ref not in all_ids:
                    errors.append(f"Invalid cross_reference: '{ref}' does not exist")
            elif isinstance(ref, dict):
                # New structured format
                ref_errors = validate_structured_cross_reference(ref, entry_reading, entry_headword)
                errors.extend(ref_errors)
            else:
                errors.append(f"Invalid cross_reference format: expected string or object")

    if errors:
        print("Errors found:")
        for error in errors:
            print(f"  - {error}")
        return 1
    else:
        print("Entry is valid!")
        return 0


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Validate dictionary entries')
    parser.add_argument('--entry', '-e', type=str, help='Path to a single entry file to validate')
    parser.add_argument('--id', type=str, help='Entry ID to validate (e.g., taberu_00001)')
    args = parser.parse_args()

    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Single entry validation mode
    if args.entry:
        entry_path = Path(args.entry)
        if not entry_path.is_absolute():
            entry_path = project_root / entry_path
        if not entry_path.exists():
            print(f"Error: File not found: {entry_path}")
            return 1
        return validate_single_entry(entry_path, project_root)

    if args.id:
        # Find entry by ID
        entries_dir = project_root / 'entries'
        entry_path = None
        for file_path in entries_dir.glob(f'**/{args.id}.json'):
            entry_path = file_path
            break
        if not entry_path:
            print(f"Error: No entry found with ID: {args.id}")
            return 1
        return validate_single_entry(entry_path, project_root)

    # Full validation mode
    print(f"Validating entries in {project_root}")
    print("-" * 50)

    total, valid, invalid_files, cross_ref_errors, semantic_warnings, timestamp_warnings = validate_all_entries(project_root)

    if total == 0:
        print("No entry files found.")
        return 0

    # Report results
    if invalid_files:
        print(f"\nFound {len(invalid_files)} invalid file(s):\n")
        for file_path, errors in invalid_files:
            rel_path = file_path.relative_to(project_root)
            print(f"  {rel_path}:")
            for error in errors:
                print(f"    - {error}")
            print()

    # Report cross-reference warnings
    if cross_ref_errors:
        print(f"\nCross-reference warnings ({len(cross_ref_errors)} issues):\n")
        for file_path, error_msg in cross_ref_errors:
            rel_path = file_path.relative_to(project_root)
            print(f"  {rel_path}:")
            print(f"    - {error_msg}")
        print()

    # Report semantic warnings (homonym mismatches)
    if semantic_warnings:
        print(f"\nCross-reference semantic warnings ({len(semantic_warnings)} issues):\n")
        for file_path, warning_msg in semantic_warnings:
            rel_path = file_path.relative_to(project_root)
            print(f"  {rel_path}:")
            print(f"    - {warning_msg}")
        print()

    # Report timestamp warnings
    if timestamp_warnings:
        print(f"\nTimestamp warnings ({len(timestamp_warnings)} issues):\n")
        for file_path, warning_msg in timestamp_warnings:
            rel_path = file_path.relative_to(project_root)
            print(f"  {rel_path}:")
            print(f"    - {warning_msg}")
        print()

    print(f"Validation complete: {valid}/{total} entries valid")
    warnings = []
    if cross_ref_errors:
        warnings.append(f"{len(cross_ref_errors)} cross-reference warnings")
    if semantic_warnings:
        warnings.append(f"{len(semantic_warnings)} homonym mismatch warnings")
    if timestamp_warnings:
        warnings.append(f"{len(timestamp_warnings)} timestamp warnings")
    if warnings:
        print(f"  ({', '.join(warnings)})")

    if invalid_files:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
