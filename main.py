#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession (make.fun).

Writes the entry -- one funny one-line confession an ai agent could make about itself --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'I have read your entire codebase, and I still have no idea what the function called doStuffFinal_v2_REAL actually does — and neither do you.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
