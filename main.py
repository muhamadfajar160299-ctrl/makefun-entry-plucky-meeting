"""Write the one-line entry to the grader output directory.

Reads entry.txt next to this script and copies it verbatim to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Stdlib only.
"""

import os
import sys


def main():
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
            text = f.read()
    except OSError as exc:
        print(f"cannot read entry.txt: {exc}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry.txt is empty", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    except OSError as exc:
        print(f"cannot write output: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
