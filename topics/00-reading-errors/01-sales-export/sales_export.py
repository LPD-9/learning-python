"""Monthly sales export: total sales for each region.

Reads sales.csv, which has one row per sale, and prints a report with one
line per region.
"""

import csv
from collections import defaultdict
from pathlib import Path

DATA_FILE = Path(__file__).parent / "sales.csv"


def read_rows(path):
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def total_by_region(rows):
    totals = defaultdict(float)
    for row in rows:
        totals[row["region"]] += float(row["amount"])
    return dict(totals)


def format_report(totals):
    lines = [f"{region:<10}{total:>10.2f}" for region, total in sorted(totals.items())]
    return "\n".join(lines)


def main():
    rows = read_rows(DATA_FILE)
    print(format_report(total_by_region(rows)))


if __name__ == "__main__":
    main()
