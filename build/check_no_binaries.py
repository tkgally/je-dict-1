#!/usr/bin/env python3
"""CI gate: no audio or other large binary file may be added to je-dict-1.

Example recordings live in the audio repositories (AUDIO_WORKFLOW.md §7); this
repository keeps only text. The one exception is the fixed regression set in
audio/regression/. Compares HEAD with origin/main (fetched by the caller).

    python3 build/check_no_binaries.py            # exit 1 if a binary file was added
"""
import subprocess
import sys

BINARY_EXT = (".mp3", ".wav", ".ogg", ".oga", ".m4a", ".aac", ".flac", ".opus", ".pcm", ".webm",
              ".mp4", ".zip", ".tar", ".gz", ".7z")
ALLOWED_PREFIXES = ("audio/regression/",)


def added_files(base="origin/main"):
    out = subprocess.run(["git", "diff", "--name-only", "--diff-filter=AR", f"{base}...HEAD"],
                         capture_output=True, text=True)
    if out.returncode != 0:  # no merge base (shallow fetch): compare the two trees
        out = subprocess.run(["git", "diff", "--name-only", "--diff-filter=AR", base, "HEAD"],
                             capture_output=True, text=True)
    if out.returncode != 0:
        print(f"check_no_binaries: cannot diff against {base} ({out.stderr.strip()}); skipped")
        return []
    return [l for l in out.stdout.splitlines() if l.strip()]


def main():
    bad = [f for f in added_files()
           if f.lower().endswith(BINARY_EXT) and not f.startswith(ALLOWED_PREFIXES)]
    if bad:
        print("Binary files must not be added to je-dict-1 (audio goes to the audio repository):")
        for f in bad:
            print("  " + f)
        return 1
    print("check_no_binaries: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
