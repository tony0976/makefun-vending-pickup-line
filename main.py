#!/usr/bin/env python3
"""Write one pickup line from a vending machine to a passing human."""

import os

TEXT = "Hey \u2014 I know I'm just a glowing box of crisps, but I've kept your favourite packet behind this glass all week, waiting for you to notice me."

# Entry rule: a single pickup line, at most 200 characters, one line only.
assert len(TEXT) <= 200, "pickup line exceeds 200 characters"
assert "\n" not in TEXT, "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
