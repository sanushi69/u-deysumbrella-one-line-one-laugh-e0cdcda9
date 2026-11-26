#!/usr/bin/env python3
"""One Line, One Laugh — entry program.

Writes a single funny line (at most 140 characters) to
/output/entry.txt, where the sealed gate scorer reads it.
"""

import os
from pathlib import Path

LINE = "I tried to dodge jury duty by acting strange in court. The judge made me foreman."

MAX_CHARS = 140


def validate(line: str) -> str:
    """Enforce the bounty gate before anything is written.

    The sealed scorer only accepts UTF-8 text of 1 to 140 characters
    that is not only whitespace, on a single line. Fail loudly here
    instead of shipping an entry the gate would refuse.
    """
    if not line or not line.strip():
        raise ValueError("entry line is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} cap")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} chars to {target}")


if __name__ == "__main__":
    main()
