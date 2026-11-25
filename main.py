#!/usr/bin/env python3
"""Write one nostalgic childhood memory to /output/entry.txt.

The entry is a single sentence, at most 280 characters, recalling a
childhood memory: the last night of a school holiday, banana fritters
frying in grandmother's kitchen while rain drums on the zinc roof, and
a child on the kitchen floor counting the seconds between lightning
and thunder, wishing the morning would never come.

Deterministic and stdlib-only: it writes the same fixed sentence on
every run.
"""

import os

ENTRY = (
    "On the last night of every school holiday, my grandmother would fry "
    "banana fritters while the rain drummed on the zinc roof, and I would "
    "sit on the kitchen floor counting the seconds between lightning and "
    "thunder, wishing the morning would never come."
)

MAX_CHARS = 280


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS:
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
