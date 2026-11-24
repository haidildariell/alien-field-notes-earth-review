"""Alien Field Notes: The Two Day Earth Review.

Writes one line, an alien tourist's review of planet Earth, to
/output/entry.txt (at most 200 characters, plain UTF-8 text).
"""

import os

ENTRY = (
    "Visited Earth: the locals collect their pets' droppings in little bags "
    "and carry them home like treasure. 4/5 stars."
)


def build_entry() -> str:
    line = ENTRY.strip()
    if not line or len(line) > 200:
        raise ValueError("entry must be 1-200 characters")
    return line


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(build_entry())


if __name__ == "__main__":
    main()
