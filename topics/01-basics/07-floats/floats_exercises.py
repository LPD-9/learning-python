"""Floats: rounding, precision, formatting, NaN and Decimal.

Implement each function so the tests in test_floats_exercises.py pass.
Run them with:  pytest topics/01-basics/07-floats

Before you start, run this in a Python shell and think about why:
    >>> 0.1 + 0.2 == 0.3
"""

from decimal import Decimal


def percentage(part: float, whole: float) -> float:
    """Return part as a percentage of whole, rounded to 1 decimal place.

    If whole is 0, return 0.0 instead of crashing.

    >>> percentage(1, 3)
    33.3
    """
    raise NotImplementedError


def nearly_equal(a: float, b: float) -> bool:
    """Return True if a and b are equal, allowing for float rounding error.

    The standard library already has a function for this. Find it.

    >>> nearly_equal(0.1 + 0.2, 0.3)
    True
    """
    raise NotImplementedError


def format_bytes(size: int) -> str:
    """Format a file size in bytes as a human-readable string.

    Use units B, KB, MB, GB, TB, where 1 KB = 1024 B. Use the largest unit
    that keeps the number at least 1. Bytes are shown as a whole number,
    every other unit with exactly one decimal place.

    >>> format_bytes(1536)
    '1.5 KB'
    """
    raise NotImplementedError


def total_price(prices: list[str]) -> Decimal:
    """Add up prices given as strings like "0.10", with no rounding error.

    Floats can't represent most decimal amounts exactly, which is why
    money is usually handled with decimal.Decimal.

    >>> total_price(["0.10", "0.20"])
    Decimal('0.30')
    """
    raise NotImplementedError


def mean_ignoring_nan(values: list[float]) -> float:
    """Return the mean of values, skipping any NaN ("not a number"). (Stretch)

    If there's nothing left to average, return NaN. Careful: NaN is not
    equal to anything, not even itself.

    >>> mean_ignoring_nan([1.0, float("nan"), 3.0])
    2.0
    """
    raise NotImplementedError


def split_bill(total: float, people: int) -> list[float]:
    """Split a bill into amounts in whole pennies that add up exactly. (Stretch)

    When it doesn't divide evenly, the first people in the list pay one
    penny more. Hint: floats are bad at money, so work in pennies.

    >>> split_bill(10.00, 3)
    [3.34, 3.33, 3.33]
    """
    raise NotImplementedError
