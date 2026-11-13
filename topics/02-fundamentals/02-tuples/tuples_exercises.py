"""Tuples: packing, unpacking, sorting by tuples, NamedTuple and hashing.

Implement each function so the tests in test_tuples_exercises.py pass.
Run them with:  pytest topics/02-fundamentals/02-tuples
"""

from typing import NamedTuple


class Color(NamedTuple):
    red: int
    green: int
    blue: int


def min_max(numbers: list[int]) -> tuple[int, int]:
    """Return (smallest, largest). Raise ValueError if numbers is empty.

    >>> min_max([3, 9, 1])
    (1, 9)
    """
    raise NotImplementedError


def distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    """Return the straight-line distance between two (x, y) points.

    Practise unpacking the tuples into named variables.

    >>> distance((0, 0), (3, 4))
    5.0
    """
    raise NotImplementedError


def head_and_tail(items: tuple) -> tuple[object, tuple]:
    """Split a tuple into its first item and a tuple of the rest.

    Raise ValueError if items is empty. (Hint: star unpacking.)

    >>> head_and_tail((1, 2, 3))
    (1, (2, 3))
    """
    raise NotImplementedError


def rank_players(scores: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """Sort (name, score) pairs by score, highest first.

    Players with equal scores are ordered alphabetically by name.

    >>> rank_players([("cat", 5), ("ann", 9), ("bob", 5)])
    [('ann', 9), ('bob', 5), ('cat', 5)]
    """
    raise NotImplementedError


def parse_hex_color(hex_color: str) -> Color:
    """Turn a hex colour like "#ff8000" into a Color (defined above).

    Upper or lower case letters are both allowed.

    >>> parse_hex_color("#ff8000")
    Color(red=255, green=128, blue=0)
    """
    raise NotImplementedError


def count_friendships(pairs: list[tuple[str, str]]) -> dict[tuple[str, str], int]:
    """Count how often each friendship appears. (Stretch)

    ("ann", "ben") and ("ben", "ann") are the same friendship. Use a tuple
    with the two names in alphabetical order as the dictionary key.

    >>> count_friendships([("ben", "ann"), ("ann", "ben"), ("ann", "cat")])
    {('ann', 'ben'): 2, ('ann', 'cat'): 1}
    """
    raise NotImplementedError
