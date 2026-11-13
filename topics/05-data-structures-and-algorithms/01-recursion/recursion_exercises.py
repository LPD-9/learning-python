"""Recursion: functions that solve a problem by calling themselves.

Implement each function so the tests in test_recursion_exercises.py pass.
Run them with:  pytest topics/05-data-structures-and-algorithms/01-recursion

Every recursive function needs two things:

- a base case: an input small enough to answer straight away
- a recursive case: make the problem smaller, call yourself on that, and
  build the answer from the result

Write all of these recursively, with no loops, even where a loop would
be simpler. If you see RecursionError, your base case is never reached.
"""


def factorial(n: int) -> int:
    """Return n! = n * (n - 1) * ... * 1. By definition, 0! is 1.

    >>> factorial(5)
    120
    """
    raise NotImplementedError


def sum_list(numbers: list[float]) -> float:
    """Add up a list without using sum() or a loop.

    The sum of a list is its first item plus the sum of the rest.

    >>> sum_list([3, 1, 4])
    8
    """
    raise NotImplementedError


def reverse_string(text: str) -> str:
    """Reverse a string without slicing it backwards or using reversed().

    >>> reverse_string("abc")
    'cba'
    """
    raise NotImplementedError


def fibonacci(n: int) -> int:
    """Return Fibonacci number n, where numbers 0 and 1 are 0 and 1.

    Each later number is the sum of the two before it.

    When this passes, try fibonacci(35) in the REPL and notice how long
    it takes. Work out how many times fibonacci(2) gets called, then look
    up "memoization" (you wrote a decorator for it in section 3).

    >>> fibonacci(10)
    55
    """
    raise NotImplementedError


def total_size(folder: dict) -> int:
    """Return the combined size of every file in a folder tree.

    A folder is a dict. Each value is either a file's size (an int) or
    another folder (a dict), nested to any depth. Problems shaped like a
    tree are where recursion is the natural tool.

    >>> total_size({"a.txt": 10, "docs": {"b.txt": 5, "old": {"c.txt": 1}}})
    16
    """
    raise NotImplementedError


def binary_search(
    items: list[int], target: int, low: int = 0, high: int | None = None
) -> int:
    """Return the position of target in a sorted list, or -1 if it's absent.

    Look at the middle item of the range from low to high. If it's the
    target, you're done. Otherwise the target can only be in one half, so
    search that half. Each step throws away half of what's left, which is
    why this takes about 20 steps for a million items.

    >>> binary_search([1, 3, 5, 7, 9], 7)
    3
    """
    raise NotImplementedError


def permutations(items: list) -> list[list]:
    """Return every possible ordering of items. (Stretch)

    The orderings can come back in any order. Think about it this way:
    pick each item in turn to go first, then follow it with every
    ordering of the items that are left. An empty list has exactly one
    ordering, which is the empty list.

    >>> permutations([1, 2])
    [[1, 2], [2, 1]]
    """
    raise NotImplementedError
