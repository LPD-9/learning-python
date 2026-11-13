"""Sets: membership, uniqueness, and set operations (& | - ^).

Implement each function so the tests in test_sets_exercises.py pass.
Run them with:  pytest topics/02-fundamentals/03-sets
"""


def has_duplicates(items: list) -> bool:
    """Return True if any item appears more than once.

    >>> has_duplicates([1, 2, 3, 2])
    True
    """
    raise NotImplementedError


def is_pangram(text: str) -> bool:
    """Return True if text uses every letter a-z at least once (any case).

    Hint: the string module has the alphabet ready-made.

    >>> is_pangram("The quick brown fox jumps over the lazy dog")
    True
    """
    raise NotImplementedError


def compare_lists(first: list, second: list) -> dict[str, set]:
    """Compare two lists, ignoring order and duplicates.

    Return a dict with three keys:
      "both"         items in both lists
      "only_first"   items only in first
      "only_second"  items only in second

    >>> compare_lists([1, 2, 3], [2, 3, 4])
    {'both': {2, 3}, 'only_first': {1}, 'only_second': {4}}
    """
    raise NotImplementedError


def missing_numbers(numbers: list[int], start: int, end: int) -> list[int]:
    """Return the numbers from start to end (inclusive) that aren't in numbers.

    The result must be sorted.

    >>> missing_numbers([1, 2, 4, 7], 1, 7)
    [3, 5, 6]
    """
    raise NotImplementedError


def first_repeat(items: list) -> object:
    """Return the first item that turns up for a second time, else None.

    "First" means the earliest position of a repeat, so in
    ["a", "b", "b", "a"], "b" repeats first.

    >>> first_repeat(["a", "b", "b", "a"])
    'b'
    """
    raise NotImplementedError


def shared_interests(people: dict[str, set[str]]) -> set[str]:
    """Return the interests that every person has in common. (Stretch)

    If there are no people, return an empty set.

    >>> shared_interests({"ann": {"chess", "golf"}, "ben": {"golf", "jazz"}})
    {'golf'}
    """
    raise NotImplementedError


def unique_visitors_per_day(visits: list[tuple[str, str]]) -> dict[str, int]:
    """Count distinct visitors for each day. (Stretch)

    visits is a list of (day, user) pairs. A user visiting several times
    on the same day only counts once for that day.

    >>> unique_visitors_per_day([("mon", "ann"), ("mon", "ann"), ("tue", "ann")])
    {'mon': 1, 'tue': 1}
    """
    raise NotImplementedError
