"""Loops: for, while, range, break and nested loops.

Implement each function so the tests in test_loops_exercises.py pass.
Run them with:  pytest topics/01-basics/04-loops

Write these with loops, even where you know a shortcut. The shortcuts
get their own topics later.
"""


def sum_to(n: int) -> int:
    """Add up the whole numbers from 1 to n. Return 0 if n is less than 1.

    >>> sum_to(4)  # 1 + 2 + 3 + 4
    10
    """
    raise NotImplementedError


def count_vowels(text: str) -> int:
    """Count the vowels (a, e, i, o, u) in text, in either case.

    >>> count_vowels("Education")
    5
    """
    raise NotImplementedError


def countdown(start: int) -> list[int | str]:
    """Count down from start to 1, then finish with "Liftoff!".

    If start is less than 1, the list holds only "Liftoff!".

    >>> countdown(3)
    [3, 2, 1, 'Liftoff!']
    """
    raise NotImplementedError


def first_negative(numbers: list[float]) -> float | None:
    """Return the first negative number, or None if there isn't one.

    Stop looking as soon as you find it.

    >>> first_negative([4, -2, 7, -9])
    -2
    """
    raise NotImplementedError


def times_table(n: int, up_to: int) -> list[str]:
    """Return the lines of n's times table, from 1 up to up_to.

    >>> times_table(3, 4)
    ['3 x 1 = 3', '3 x 2 = 6', '3 x 3 = 9', '3 x 4 = 12']
    """
    raise NotImplementedError


def collatz_steps(n: int) -> int:
    """Count the steps it takes to reach 1 by following these rules:

    - if the number is even, halve it
    - if the number is odd, multiply it by 3 and add 1

    You can't know in advance how many steps there will be, so this
    needs a while loop. You can assume n is at least 1.

    >>> collatz_steps(6)  # 6, 3, 10, 5, 16, 8, 4, 2, 1
    8
    """
    raise NotImplementedError


def find_pair_with_sum(numbers: list[int], target: int) -> tuple[int, int] | None:
    """Find two numbers that add up to target. (Stretch)

    Return the positions of the two numbers as a tuple, smaller position
    first. A number can't be paired with itself. If several pairs work,
    return the one whose first position is lowest. Return None if no
    pair adds up to target.

    >>> find_pair_with_sum([2, 7, 11, 15], 9)
    (0, 1)
    """
    raise NotImplementedError
