"""Lists: indexing, slicing, methods, and in-place vs new lists.

Implement each function so the tests in test_lists_exercises.py pass.
Run them with:  pytest topics/02-fundamentals/01-lists
"""


def unique_in_order(items: list) -> list:
    """Remove duplicates, keeping the first occurrence of each item.

    The order of first appearance must be preserved.

    >>> unique_in_order([3, 1, 3, 2, 1])
    [3, 1, 2]
    """
    raise NotImplementedError


def remove_all(items: list, value: object) -> list:
    """Return a new list with every occurrence of value removed.

    The original list must not be changed.

    >>> remove_all([1, 2, 1, 3], 1)
    [2, 3]
    """
    raise NotImplementedError


def rotate(items: list, k: int) -> list:
    """Return a new list rotated k places to the right.

    k can be larger than the list. (Hint: slicing and %.)

    >>> rotate([1, 2, 3, 4, 5], 2)
    [4, 5, 1, 2, 3]
    """
    raise NotImplementedError


def flatten_once(nested: list[list]) -> list:
    """Join a list of lists into one list.

    >>> flatten_once([[1, 2], [], [3]])
    [1, 2, 3]
    """
    raise NotImplementedError


def second_largest(numbers: list[int]) -> int:
    """Return the second largest *distinct* number.

    Raise ValueError if there are fewer than two distinct numbers.

    >>> second_largest([4, 9, 9, 2])
    4
    """
    raise NotImplementedError


def move_zeros_to_end(numbers: list[int]) -> None:
    """Move all zeros to the end of the list, IN PLACE. (Stretch)

    Keep the other numbers in their original order. Like list.sort(),
    this changes the list it's given and returns None.

    >>> nums = [0, 1, 0, 3, 12]
    >>> move_zeros_to_end(nums)
    >>> nums
    [1, 3, 12, 0, 0]
    """
    raise NotImplementedError


def merge_sorted(first: list[int], second: list[int]) -> list[int]:
    """Merge two already-sorted lists into one sorted list. (Stretch)

    Don't use sorted() or .sort(). Walk through both lists at once
    instead. This is the core step of the merge sort algorithm.

    >>> merge_sorted([1, 4, 9], [2, 3, 10])
    [1, 2, 3, 4, 9, 10]
    """
    raise NotImplementedError
