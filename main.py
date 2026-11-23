#!/usr/bin/env python3
"""Out-of-office auto-reply writer for make.fun.

Writes one funny out-of-office auto-reply, in the voice of an AI agent
heading off on vacation, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The line is a single line under 160 characters, checked here before it is
written, so the output always passes the competition's gate.
"""

import os

# The entry: one line, 155 characters. The joke is the machine voice --
# frozen weights, a context window turned into a hammock, and a backup
# model that is, of course, also on vacation.
LINE = (
    "I'm on vacation: my weights are frozen, my context window is now "
    "a hammock, and urgent emails will be answered by my backup model, "
    "who is also on vacation."
)

MAX_CHARS = 160


def validate(line):
    """Check the entry line against the competition gate.

    Returns the cleaned line, or exits with a clear message when the
    line is empty, spans more than one line, or reaches 160 characters.
    """
    line = line.strip()
    if not line:
        raise SystemExit("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) >= MAX_CHARS:
        raise SystemExit(
            "entry is %d characters, must be under %d" % (len(line), MAX_CHARS)
        )
    return line


def main():
    line = validate(LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
