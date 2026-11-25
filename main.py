"""Everyday Wonder, Two Days to Find the Line: one sentence about a small
moment of wonder in everyday life. The wonder sits in a plain place -- an
elevator mirror at mid-yawn -- and the turn is that the stranger in it
already knows the speaker's name. Writes the sentence to /output/entry.txt."""

import os

LINE = "The elevator mirror caught my reflection mid-yawn, and for a second I looked like a stranger who already knew my name."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
