import importlib
import math
import subprocess
import sys
from pathlib import Path

import pytest
from modules_exercises import (
    circle_circumference,
    days_between,
    most_common_word,
    roll_dice,
    shout_twice,
    top_scorer,
)

HERE = Path(__file__).parent


class TestCircleCircumference:
    def test_radius_one(self):
        assert circle_circumference(1) == pytest.approx(2 * math.pi)

    def test_radius_ten(self):
        assert circle_circumference(10) == pytest.approx(62.8318530718)

    def test_zero(self):
        assert circle_circumference(0) == 0


class TestDaysBetween:
    def test_example(self):
        assert days_between("2026-01-01", "2026-01-31") == 30

    def test_same_day(self):
        assert days_between("2026-05-05", "2026-05-05") == 0

    def test_across_a_leap_day(self):
        assert days_between("2024-02-28", "2024-03-01") == 2

    def test_end_before_start(self):
        assert days_between("2026-01-10", "2026-01-01") == -9


class TestMostCommonWord:
    def test_example(self):
        assert most_common_word(["tea", "milk", "tea"]) == "tea"

    def test_tie_goes_to_the_first_seen(self):
        assert most_common_word(["b", "a", "a", "b"]) == "b"

    def test_empty(self):
        assert most_common_word([]) is None


class TestRollDice:
    def test_count(self):
        assert len(roll_dice(5, seed=1)) == 5

    def test_rolls_are_dice_numbers(self):
        assert set(roll_dice(600, seed=1)) == {1, 2, 3, 4, 5, 6}

    def test_same_seed_gives_same_rolls(self):
        assert roll_dice(20, seed=42) == roll_dice(20, seed=42)

    def test_different_seeds_give_different_rolls(self):
        assert roll_dice(50, seed=1) != roll_dice(50, seed=2)

    def test_no_rolls(self):
        assert roll_dice(0, seed=1) == []


class TestTopScorer:
    def test_example(self):
        assert top_scorer('{"ada": 91, "bob": 78}') == "ada"

    def test_three_players(self):
        assert top_scorer('{"ada": 5, "bob": 78, "cat": 12}') == "bob"


class TestYourOwnModule:
    def test_module_exists_with_a_version(self):
        my_text_tools = importlib.import_module("my_text_tools")
        assert my_text_tools.VERSION == "1.0"

    def test_shout(self):
        my_text_tools = importlib.import_module("my_text_tools")
        assert my_text_tools.shout("hello") == "HELLO!"

    def test_shout_twice(self):
        assert shout_twice("hey") == "HEY! HEY!"


class TestRunningAsAScript:
    def run_python(self, *args):
        return subprocess.run(
            [sys.executable, *args],
            cwd=HERE,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_running_the_file_prints_its_name_and_version(self):
        result = self.run_python("my_text_tools.py")
        assert result.stdout.strip() == "my_text_tools 1.0"

    def test_importing_prints_nothing(self):
        result = self.run_python("-c", "import my_text_tools")
        assert result.returncode == 0, result.stderr
        assert result.stdout == ""

    def test_has_a_main_function(self):
        my_text_tools = importlib.import_module("my_text_tools")
        assert callable(my_text_tools.main)
