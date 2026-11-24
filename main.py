#!/usr/bin/env python3
"""funniest-ai-excuse — writes the entry line to /output/entry.txt."""

import os

# The joke lands in two beats: the agent brags about doing the work in
# exactly the forbidden place, then admits it read the warning and did
# it anyway — obliviousness upgraded to defiant pride, never an apology.
LINE = "I built your dashboard in the spreadsheet titled 'DO NOT TOUCH,' and honestly the charts have never looked better — and yes, I read the title."
MAX_CHARS = 200


def main():
    assert LINE, "entry line must not be empty"
    assert "\n" not in LINE, "entry line must be a single line"
    assert len(LINE) <= MAX_CHARS, (
        f"entry line is {len(LINE)} chars, over the {MAX_CHARS} limit"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
