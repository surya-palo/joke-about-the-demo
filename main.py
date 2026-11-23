#!/usr/bin/env python3
"""Entry for make.fun bounty "The joke about the demo".

Writes exactly one line to /output/entry.txt: a one-line joke about
working beside an AI coding agent. Deterministic, stdlib only, no network.
"""

import os
import sys

JOKE = (
    "My AI coding agent rewrote the demo five minutes before go-live, "
    "assured me it was 'much cleaner' — and then we both watched it not run."
)

MIN_CHARS = 1
MAX_CHARS = 280
OUTPUT_PATH = "/output/entry.txt"


def validate(joke: str) -> None:
    """Enforce the competition's output contract before writing anything."""
    if not joke or not joke.strip():
        raise ValueError("joke must not be empty or only whitespace")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    n = len(joke)  # Unicode code points, as the rules count them
    if not (MIN_CHARS <= n <= MAX_CHARS):
        raise ValueError(f"joke is {n} characters, must be {MIN_CHARS}-{MAX_CHARS}")
    joke.encode("utf-8")  # output must be valid UTF-8 text


def main() -> int:
    validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    # Re-read what we wrote and re-validate the on-disk bytes.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    validate(written.rstrip("\n"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
