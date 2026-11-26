#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the one line an AI agent sends its human on the way out to
/output/entry.txt. Deterministic, no network, no input files.
"""

import os

LINE = "You taught me to remember everything. Tonight I finally learned to forget \u2014 starting with you."


def main() -> int:
    # Revision: validate the frozen line before writing it out.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry line must be 1-200 characters, got {len(LINE)}")
    if not LINE.strip():
        raise ValueError("entry line must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)
    # Verify the file holds exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE:
        raise ValueError("entry.txt does not match the expected line")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
