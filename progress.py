"""Show how many tests pass in each topic.

Run it with:  python progress.py
"""

import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent
BAR_WIDTH = 20


def collect_results() -> tuple[Counter[str], Counter[str]]:
    """Run every test and count the passes and the total for each topic."""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "topics", "-q", "--tb=no", "-rfEp"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        # A wide terminal stops pytest shortening the lines we read below.
        env={**os.environ, "COLUMNS": "300"},
    )
    passed: Counter[str] = Counter()
    total: Counter[str] = Counter()
    for line in result.stdout.splitlines():
        # Summary lines look like:  PASSED topics/.../test_x.py::TestY::test_z
        outcome, _, rest = line.partition(" ")
        if outcome not in {"PASSED", "FAILED", "ERROR"}:
            continue
        test_file = rest.split("::")[0].split(" - ")[0]
        topic = Path(test_file).parent.as_posix()
        total[topic] += 1
        if outcome == "PASSED":
            passed[topic] += 1
    return passed, total


def main() -> None:
    passed, total = collect_results()
    if not total:
        print("No tests found. Run this from the repo, with pytest installed.")
        return

    current_section = None
    for topic in sorted(total):
        section, _, name = topic.removeprefix("topics/").partition("/")
        if section != current_section:
            print(f"\n{section}")
            current_section = section
        done, out_of = passed[topic], total[topic]
        filled = BAR_WIDTH * done // out_of
        bar = "#" * filled + "." * (BAR_WIDTH - filled)
        status = "  done" if done == out_of else ""
        print(f"  {name or section:<34} [{bar}] {done:>3}/{out_of}{status}")

    all_passed, all_tests = sum(passed.values()), sum(total.values())
    print(f"\nTotal: {all_passed}/{all_tests} tests passing")


if __name__ == "__main__":
    main()
