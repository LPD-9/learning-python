"""Operators: arithmetic, comparison, logical, membership and identity.

Implement each function so the tests in test_operators_exercises.py pass.
Run them with:  pytest topics/01-basics/02-operators
"""


def is_even(n: int) -> bool:
    """Return True if n is an even number.

    >>> is_even(4)
    True
    >>> is_even(7)
    False
    """
    raise NotImplementedError


def is_between(value: float, low: float, high: float) -> bool:
    """Return True if value is from low to high, including both ends.

    Python lets you chain comparisons in a way most languages don't.

    >>> is_between(5, 1, 10)
    True
    """
    raise NotImplementedError


def is_vowel(letter: str) -> bool:
    """Return True if letter is one of a, e, i, o, u, in either case.

    >>> is_vowel("E")
    True
    """
    raise NotImplementedError


def can_ride(height_cm: int, age: int, with_adult: bool) -> bool:
    """Decide whether someone can go on a rollercoaster.

    They must be at least 120 cm tall. They must also be at least 12
    years old, unless they are with an adult.

    >>> can_ride(130, 9, with_adult=True)
    True
    >>> can_ride(130, 9, with_adult=False)
    False
    """
    raise NotImplementedError


def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year.

    A year is a leap year if it divides by 4. But years that divide by
    100 are not leap years, unless they also divide by 400.

    >>> is_leap_year(2024)
    True
    >>> is_leap_year(1900)
    False
    """
    raise NotImplementedError


def compare_objects(a: object, b: object) -> str:
    """Describe how two values are related.

    Return "identical" if a and b are the very same object, "equal" if
    they are separate objects with the same value, and "different"
    otherwise. Python has one operator for each of the first two checks.

    >>> shopping = ["milk"]
    >>> compare_objects(shopping, shopping)
    'identical'
    >>> compare_objects(["milk"], ["milk"])
    'equal'
    """
    raise NotImplementedError


def clock_add(hour: int, hours_to_add: int) -> int:
    """Move a 12-hour clock forwards or backwards. (Stretch)

    hour is from 1 to 12. The result must also be from 1 to 12, never 0.
    hours_to_add can be negative, or bigger than 12.

    >>> clock_add(11, 2)
    1
    >>> clock_add(1, -2)
    11
    """
    raise NotImplementedError
