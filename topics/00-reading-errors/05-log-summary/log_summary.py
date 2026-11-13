"""Daily log summary: how many entries at each level, and which parts fail.

Reads app.log and prints a short summary. A log entry looks like this:

    2026-10-14 09:15:04 ERROR payments Card declined (code 51)
"""

import re
from collections import Counter
from pathlib import Path

LOG_FILE = Path(__file__).parent / "app.log"
ENTRY = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\w+) (.*)$")


def parse_line(line):
    time, level, component, message = ENTRY.match(line).groups()
    return {"time": time, "level": level, "component": component, "message": message}


def summarise(lines):
    entries = [parse_line(line) for line in lines]
    levels = Counter(entry["level"] for entry in entries)
    errors = Counter(e["component"] for e in entries if e["level"] == "ERROR")
    return {"levels": dict(levels), "errors_by_component": dict(errors)}


def format_summary(summary):
    lines = ["Levels"]
    for level, count in sorted(summary["levels"].items()):
        lines.append(f"  {level}: {count}")
    lines.append("Errors by component")
    for component, count in sorted(summary["errors_by_component"].items()):
        lines.append(f"  {component}: {count}")
    return "\n".join(lines)


def main():
    lines = LOG_FILE.read_text(encoding="utf-8").splitlines()
    print(format_summary(summarise(lines)))


if __name__ == "__main__":
    main()
