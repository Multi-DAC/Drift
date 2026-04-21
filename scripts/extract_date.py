#!/usr/bin/env python3
"""
extract_date.py — extract an essay's date from its first few lines.

Reads a markdown file from a path given as argv[1] and prints
the extracted date as YYYY-MM-DD to stdout, or nothing if no date
could be extracted. Used by scripts/sync-from-substrate.sh to
synthesize Jekyll front-matter for essays that lack it.

Patterns handled (in priority order):
  1. ISO date anywhere in first 10 lines: 2026-04-21
  2. "Month D, YYYY" or "Month Dth, YYYY" — full month name
  3. "Mon D, YYYY" — abbreviated month name
"""
from __future__ import annotations

import re
import sys
from datetime import datetime

MONTHS = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12,
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "jun": 6, "jul": 7,
    "aug": 8, "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12,
}

ISO_RE = re.compile(r"\b(20\d{2})-(0?[1-9]|1[0-2])-(0?[1-9]|[12]\d|3[01])\b")
TEXT_RE = re.compile(
    r"\b(january|february|march|april|may|june|july|august|september|october|november|december"
    r"|jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)"
    r"\s+(\d{1,2})(?:st|nd|rd|th)?"
    r"(?:,?\s+(20\d{2}))?",
    re.IGNORECASE,
)


def extract(text: str) -> str | None:
    head = "\n".join(text.splitlines()[:10])

    m = ISO_RE.search(head)
    if m:
        y, mo, d = m.groups()
        try:
            return datetime(int(y), int(mo), int(d)).strftime("%Y-%m-%d")
        except ValueError:
            pass

    m = TEXT_RE.search(head)
    if m:
        month_str, day_str, year_str = m.group(1).lower(), m.group(2), m.group(3)
        mo = MONTHS.get(month_str)
        if mo and year_str:
            try:
                return datetime(int(year_str), mo, int(day_str)).strftime("%Y-%m-%d")
            except ValueError:
                pass

    return None


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: extract_date.py <path>", file=sys.stderr)
        return 2
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    result = extract(text)
    if result:
        print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
