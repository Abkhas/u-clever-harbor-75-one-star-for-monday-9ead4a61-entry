#!/usr/bin/env python3
"""One Star for Monday (make.fun).

Emits a single line: a one-star review of Monday written as if Monday
were a restaurant. The line goes to entry.txt in the grader's output
directory. Standard library only; no input, no network, no randomness.
"""

import os
import sys

REVIEW = (
    "One star. I reserved Friday and they gave me Monday: "
    "same table, cold coffee, no refunds."
)

MAX_CHARS = 180
MAX_WORDS = 25


def pick_output_folder():
    """Grader-provided dir first, then /output if it exists, else out/."""
    given = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if given:
        return given
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.getcwd(), "out")


def check(line):
    """The sealed gate wants 1-180 chars of plain single-line text."""
    problems = []
    if not line.strip():
        problems.append("empty")
    if len(line) > MAX_CHARS:
        problems.append(f"{len(line)} chars, over the {MAX_CHARS} cap")
    if len(line.split()) > MAX_WORDS:
        problems.append(f"{len(line.split())} words, over the {MAX_WORDS} cap")
    if "\n" in line or "\r" in line:
        problems.append("must be one line")
    return problems


def main():
    faults = check(REVIEW)
    if faults:
        print("invalid entry: " + "; ".join(faults), file=sys.stderr)
        return 1
    folder = pick_output_folder()
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as out:
        out.write(REVIEW + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
