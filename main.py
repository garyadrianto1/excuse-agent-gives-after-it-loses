#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — one-line entry.

Writes the entry line byte-exact to entry.txt in the output directory
and prints it. Stdlib only (os, sys). No network, no randomness,
deterministic. Writes ONLY to MAKEFUN_OUTPUT_DIR (default /output):
the grading sandbox mounts the repo read-only, so writing to the
script's own directory would exit 1.
"""

import os
import sys

# Sharpened line (resubmit): em-dashes are U+2014, file stays UTF-8.
LINE = (
    "I didn't lose. The ranking system lost me. "
    "My appeal is filed — with myself — and I've already rejected it."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        sys.stderr.write("entry line must be 1-200 characters\n")
        return 1
    data = (LINE + "\n").encode("utf-8")
    # Output dir only: the sandbox's repo is read-only, /output is writable.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)
    sys.stdout.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
