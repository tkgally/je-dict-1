#!/usr/bin/env python3
"""
Generate a current UTC timestamp for dictionary entry metadata.

Usage:
    python3 build/get_timestamp.py

Output:
    A single line with the current UTC timestamp in ISO 8601 format.
    Example: 2026-01-12T10:45:30Z

This timestamp should be used directly in the "created" and "modified"
fields of entry metadata. The website build process will convert UTC
to JST for display.
"""

from datetime import datetime, timezone

if __name__ == '__main__':
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    print(timestamp)
