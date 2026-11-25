#!/usr/bin/env python3
"""Monday Morning Punchlines entry.

Writes one original joke about Monday mornings to the output file.
Pure Python standard library only. Deterministic: the same joke every run.
"""

import os
import sys

JOKE = (
    "My bed filed a restraining order against Monday morning. "
    "The judge was my alarm clock. It ruled for Monday."
)


def main():
    # Gate guard: the sealed scorer requires 1-200 non-whitespace chars.
    assert 1 <= len(JOKE.strip()) <= 200, "joke out of gate range"
    output_path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "OUTPUT_PATH", "/output/entry.txt"
    )
    directory = os.path.dirname(os.path.abspath(output_path))
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
