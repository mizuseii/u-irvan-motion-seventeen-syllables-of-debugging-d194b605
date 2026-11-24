#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — writes the haiku to /output/entry.txt.

Deterministic: no network, no randomness, no clock. Same bytes every run.
"""
import os

HAIKU = (
    "Cursor blinks at three\n"
    "the log insists it just worked\n"
    "it lied. So did I."
)


def main():
    lines = HAIKU.split("\n")
    if len(lines) != 3 or not (1 <= len(HAIKU) <= 200):
        raise SystemExit("haiku must be 3 lines, 1-200 chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
