"""Integers: arithmetic, //, %, divmod, bases and arbitrary size.

Implement each function so the tests in test_integers_exercises.py pass.
Run them with:  pytest topics/01-basics/06-integers
"""


def digit_sum(n: int) -> int:
    """Return the sum of the digits of n. The sign is ignored.

    >>> digit_sum(-472)
    13
    """
    raise NotImplementedError


def split_seconds(total_seconds: int) -> tuple[int, int, int]:
    """Convert a number of seconds into (hours, minutes, seconds).

    >>> split_seconds(3725)
    (1, 2, 5)
    """
    raise NotImplementedError


def round_up_to_multiple(n: int, multiple: int) -> int:
    """Round n up to the nearest multiple of multiple.

    Both numbers are non-negative and multiple is at least 1.
    Try doing this with integer arithmetic only, no floats.

    >>> round_up_to_multiple(17, 5)
    20
    """
    raise NotImplementedError


def to_binary(n: int) -> str:
    """Return the binary representation of a non-negative n, with no "0b".

    >>> to_binary(10)
    '1010'
    """
    raise NotImplementedError


def is_power_of_two(n: int) -> bool:
    """Return True if n is 1, 2, 4, 8, 16, ... (Stretch)

    Zero and negative numbers are not powers of two. There is a neat
    trick using binary, but any working approach is fine first.

    >>> is_power_of_two(64)
    True
    """
    raise NotImplementedError


def factorial_digit_count(n: int) -> int:
    """Return how many digits n! (n factorial) has. (Stretch)

    Python ints have no maximum size, so you can compute n! exactly,
    even for large n.

    >>> factorial_digit_count(10)  # 10! is 3628800
    7
    """
    raise NotImplementedError
