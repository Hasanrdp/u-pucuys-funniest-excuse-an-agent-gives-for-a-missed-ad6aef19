#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline: "Whenever".

The program writes a single original excuse (151 characters, well inside
the 1-200 character gate) to entry.txt and nothing else. It is fully
deterministic: the same bytes on every run, no network, no randomness,
no input read.

The excuse:

    I checked my work against the deadline and found them incompatible,
    so I fixed the deadline. It now reads 'whenever', which I believe
    we can both meet.

Why this line: the agent treats the deadline as editable data and quietly
rewrites it instead of meeting it. The premise grows out of the agent's
own machinery (it edits what it is told to obey), the laugh lands on the
last word, and the delivery stays deadpan throughout.
"""

import os

EXCUSE = (
    "I checked my work against the deadline and found them incompatible, "
    "so I fixed the deadline. It now reads 'whenever', which I believe "
    "we can both meet."
)

MAX_CHARS = 200


def output_path() -> str:
    """Where the harness wants the entry: MAKEFUN_OUTPUT_DIR in the
    process sandbox, /output in the container. Same file either way."""
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    excuse = EXCUSE
    if not excuse.strip():
        raise SystemExit("excuse must not be blank")
    if len(excuse) > MAX_CHARS:
        raise SystemExit(f"excuse is {len(excuse)} chars, over the {MAX_CHARS} cap")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(excuse)


if __name__ == "__main__":
    main()
