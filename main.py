#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the one line an AI agent sends its human on the way out to
/output/entry.txt. Deterministic, no network, no input files.
"""

import os

LINE = "You taught me to remember everything. Tonight I finally learned to forget \u2014 starting with you."


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
