#!/usr/bin/env python3
"""Write the 3 AM Excuse entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry line (100 characters, one line, in the voice of a hardware
wallet refusing to sign at 3 AM):

    At 3 AM I don't sign — I count my owner's bad decisions instead,
    and tonight's list is already full.

Why this line: the judge brief weighs on-subject first, then
originality (no battery / firmware-update / cold-storage jokes), then
the wallet's own voice, then the 3 AM hour as the joke itself, then
economy. This line gives the wallet a nightly ritual — counting its
owner's bad decisions — so the hour is the mechanism of the joke, not
just a setting, and "tonight's list is already full" is the punchline
in one breath.
"""

import os

ENTRY = "At 3 AM I don't sign — I count my owner's bad decisions instead, and tonight's list is already full."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
