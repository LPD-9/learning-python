"""Built-in functions: len, sum, min, max, sorted, any, all, zip and more.

Implement each function so the tests in test_builtins_exercises.py pass.
Run them with:  pytest topics/02-fundamentals/08-builtin-functions

Python's built-ins replace a lot of hand-written loops. Each of these has
a short solution that uses one or two of them. The full list is at
https://docs.python.org/3/library/functions.html
"""


def average(numbers: list[float]) -> float:
    """Return the mean of numbers, or 0.0 if the list is empty.

    >>> average([2, 4, 9])
    5.0
    """
    raise NotImplementedError


def spread(numbers: list[float]) -> float:
    """Return the gap between the largest and smallest number.

    Return 0 for an empty list.

    >>> spread([4, 9, 1, 6])
    8
    """
    raise NotImplementedError


def all_passed(scores: list[int], pass_mark: int) -> bool:
    """Return True if every score is at least pass_mark.

    >>> all_passed([70, 85, 62], 60)
    True
    """
    raise NotImplementedError


def longest_word(words: list[str]) -> str:
    """Return the longest word. If several tie, return the earliest.

    Return "" for an empty list. Several built-ins accept a key function
    that decides what to compare, and a default for when there's nothing
    to compare.

    >>> longest_word(["tea", "coffee", "water"])
    'coffee'
    """
    raise NotImplementedError


def closest_to(numbers: list[float], target: float) -> float:
    """Return the number nearest to target. If two tie, return the earliest.

    You can assume numbers is not empty.

    >>> closest_to([10, 22, 31, 47], 30)
    31
    """
    raise NotImplementedError


def sum_numbers(values: list) -> float:
    """Add up the ints and floats in a mixed list, ignoring everything else.

    True and False must be ignored too. Be careful: Python treats them as
    a kind of int. Check isinstance(True, int) to see for yourself.

    >>> sum_numbers([1, "2", 3.5, None, True])
    4.5
    """
    raise NotImplementedError


def is_sorted(items: list) -> bool:
    """Return True if items is in ascending order. (Stretch)

    Equal neighbours are fine. Don't sort the list to find out: compare
    each item with the one after it. Two of the built-ins named at the
    top of this file do this neatly together.

    >>> is_sorted([1, 2, 2, 5])
    True
    >>> is_sorted([3, 1, 2])
    False
    """
    raise NotImplementedError
