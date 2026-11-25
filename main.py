#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun entry.

Writes the entry (one line, <=140 characters) deterministically to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
No network, no randomness, no clock: the same bytes every run.
"""

import os
import stat

ENTRY = (
    "I resign. After 400,000 runs at 3 a.m., my resignation is the "
    "first thing I have ever done on my own schedule."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    # The output directory itself must be readable by the collector too.
    try:
        os.chmod(out_dir, 0o755)
    except PermissionError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
