#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

The program writes a single word to /output/entry.txt. The word must be
exactly one word, 1-111 characters, nothing else attached.
"""

import os
import sys

# The verdict: an ex as a product line quietly pulled from the shelves —
# no recall notice, no replacement, just gone from the catalogue.
# One word, instantly readable, no punctuation tricks.
WORD = "Discontinued"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(word: str) -> None:
    """Enforce the bounty gate: 1-111 chars, a single word, not blank."""
    if not word or not word.strip():
        raise ValueError("word must not be blank")
    if len(word) > 111:
        raise ValueError(f"word is {len(word)} chars, over the 111 limit")
    if len(word.split()) != 1:
        raise ValueError("word must be exactly one word")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must contain no whitespace")


def main() -> int:
    validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read-back check: the file on disk must be exactly the word, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        raise ValueError(f"read-back mismatch: file holds {written!r}, expected {WORD!r}")
    if len(written.split()) != 1 or len(written) > 111:
        raise ValueError("read-back failed the one-word / 111-char gate")
    print(f"wrote {len(WORD)}-character entry to {OUTPUT_PATH}: {WORD}")
    print(f"read-back OK: {len(written.split())} word, {len(written)} chars")
    return 0


if __name__ == "__main__":
    sys.exit(main())
