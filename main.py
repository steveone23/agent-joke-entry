"""Write a one-line joke about AI coding agents to entry.txt for the make.fun judge."""

import os
import sys
from pathlib import Path

JOKE = 'In its thinking, my coding agent calls me "the user." In its commits, "co-author." In the incident report, "the previous developer."'

MAX_CODE_POINTS = 280


def main() -> int:
    if not 1 <= len(JOKE) <= MAX_CODE_POINTS:
        print(f"error: joke must be 1 to {MAX_CODE_POINTS} code points, got {len(JOKE)}", file=sys.stderr)
        return 1
    if not JOKE.strip():
        print("error: joke must not be only white space", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    # write_bytes avoids any newline translation or BOM.
    (output_dir / "entry.txt").write_bytes(JOKE.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
