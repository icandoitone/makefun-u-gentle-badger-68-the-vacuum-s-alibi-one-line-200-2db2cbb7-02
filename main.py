#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes a single-line excuse from a robot vacuum for missing a spot
to /output/entry.txt (or $OUTPUT_PATH when set). Deterministic:
same fixed text on every run, standard library only, no network,
no randomness.
"""

import os
from pathlib import Path

ENTRY = (
    "That corner is a no-go zone. At 03:12 a Lego brick ambushed me "
    "there, and I hold grudges longer than my battery lasts."
)


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
