"""Mutability: aliasing, copies vs deep copies, and changing data safely.

Implement each function so the tests in test_mutability_exercises.py pass.
Run them with:  pytest topics/02-fundamentals/05-mutability

Before you start, predict what this prints, then run it:
    >>> a = [1, 2]
    >>> b = a
    >>> b.append(3)
    >>> a
"""


def with_item(items: list, value: object) -> list:
    """Return a NEW list with value added to the end.

    The original list must not change.

    >>> original = [1, 2]
    >>> with_item(original, 3), original
    ([1, 2, 3], [1, 2])
    """
    raise NotImplementedError


def make_grid(rows: int, cols: int, fill: object = 0) -> list[list]:
    """Build a rows x cols grid (a list of row lists) filled with fill.

    Every row must be a separate list. Changing one cell must never
    change another. Try [[fill] * cols] * rows first and see what breaks.

    >>> make_grid(2, 3)
    [[0, 0, 0], [0, 0, 0]]
    """
    raise NotImplementedError


def add_bonus(scores: dict[str, int], bonus: int) -> dict[str, int]:
    """Return a new dict with bonus added to every score.

    The original dict must not change.

    >>> add_bonus({"ann": 5, "ben": 7}, 2)
    {'ann': 7, 'ben': 9}
    """
    raise NotImplementedError


def clone_config(config: dict) -> dict:
    """Return a completely independent copy of a nested config.

    Changing anything inside the copy, however deeply nested, must not
    affect the original. Compare dict.copy() with the copy module.

    >>> clone_config({"db": {"hosts": ["a", "b"]}})
    {'db': {'hosts': ['a', 'b']}}
    """
    raise NotImplementedError


def remove_short_words(words: list[str], min_length: int) -> None:
    """Remove words shorter than min_length, IN PLACE.

    Change the list you're given (don't return a new one). Beware:
    removing items from a list while looping over it skips items.

    >>> words = ["a", "to", "cat", "be", "horse"]
    >>> remove_short_words(words, 3)
    >>> words
    ['cat', 'horse']
    """
    raise NotImplementedError


def freeze(data: object) -> object:
    """Recursively convert data into an immutable, hashable form. (Stretch)

    - lists and tuples become tuples (with their contents frozen)
    - sets become frozensets (with their contents frozen)
    - dicts become a tuple of (key, frozen value) pairs, sorted by key
    - anything else is returned unchanged

    >>> freeze({"b": [1, 2], "a": {3}})
    (('a', frozenset({3})), ('b', (1, 2)))
    """
    raise NotImplementedError
