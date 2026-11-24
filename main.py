#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands.

Writes exactly one joke about cats to /output/entry.txt: a single line,
under 200 characters, nothing else. Deterministic -- the same bytes on
every run. Python 3.13, standard library only. No trailing newline, so the
file holds exactly one line and nothing after it.
"""

from pathlib import Path

JOKE = "My cat screams at an empty wall at 3 a.m. every night \u2014 and honestly, I have never once proven him wrong."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
