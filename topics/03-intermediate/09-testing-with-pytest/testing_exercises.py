"""Testing with pytest: this time the code is finished and YOU write the tests.

Everything in this file already works. Don't change it. Your job is to
write tests for it in test_testing_exercises.py, one exercise per
function, using the technique named in each exercise there.

How your tests are checked: test_my_tests_catch_bugs.py makes broken
copies of this file, each with one small bug, and runs your tests against
every copy. A good test fails when the code is wrong, so each broken copy
should make at least one of your tests fail.

Check your progress with:  pytest topics/03-intermediate/09-testing-with-pytest
"""

import datetime
import re
from pathlib import Path


def add_vat(price: float) -> float:
    """Return price with 20% VAT added, rounded to 2 decimal places."""
    return round(price * 1.2, 2)


def is_adult(age: int) -> bool:
    """Return True if age is 18 or more."""
    return age >= 18


def withdraw(balance: float, amount: float) -> float:
    """Return the balance left after taking amount out.

    Raises ValueError if amount is zero or negative, or if it is more
    than the balance.
    """
    if amount <= 0:
        raise ValueError("amount must be positive")
    if amount > balance:
        raise ValueError("not enough money")
    return balance - amount


def slugify(title: str) -> str:
    """Turn a title into the kind of text used in web addresses.

    Everything becomes lowercase. Each run of characters that aren't
    letters or digits becomes a single hyphen. Hyphens are removed from
    both ends.
    """
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower())
    return slug.strip("-")


class Basket:
    """A shopping basket."""

    def __init__(self) -> None:
        self._lines: list[tuple[str, float, int]] = []

    def add(self, name: str, price: float, quantity: int = 1) -> None:
        """Put quantity of an item in the basket, at price each."""
        self._lines.append((name, price, quantity))

    def item_count(self) -> int:
        """Return how many individual items there are, counting quantities."""
        return sum(quantity for _, _, quantity in self._lines)

    def total(self) -> float:
        """Return the cost of everything in the basket."""
        return sum(price * quantity for _, price, quantity in self._lines)


def save_high_score(path: Path, name: str, score: int) -> int:
    """Add a "name,score" line to the file at path, keeping earlier lines.

    The file is created if it doesn't exist. Returns the highest score in
    the file after saving.
    """
    with path.open("a", encoding="utf-8") as file:
        file.write(f"{name},{score}\n")
    lines = path.read_text(encoding="utf-8").splitlines()
    return max(int(line.split(",")[1]) for line in lines)


def current_hour() -> int:
    """Return the hour of the day right now, from 0 to 23."""
    return datetime.datetime.now().hour


def greeting() -> str:
    """Return a greeting that suits the time of day.

    Before 12 it's "Good morning". From 12 up to, but not including, 18
    it's "Good afternoon". From 18 onwards it's "Good evening".
    """
    hour = current_hour()
    if hour < 12:
        return "Good morning"
    if hour < 18:
        return "Good afternoon"
    return "Good evening"
