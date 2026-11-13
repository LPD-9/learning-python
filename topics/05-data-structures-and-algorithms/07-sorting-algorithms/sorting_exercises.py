"""Sorting algorithms: five ways to sort, and why some are much faster.

Implement each function so the tests in test_sorting_exercises.py pass.
Run them with:
    pytest topics/05-data-structures-and-algorithms/07-sorting-algorithms

In real code you call sorted(). You write these by hand once, to see how
differently the same job can be done and what each way costs.

Big-O notation describes how the work grows as the list grows. Bubble,
selection and insertion sort are O(n^2): ten times the items means about
a hundred times the work. Merge sort and quicksort are O(n log n): ten
times the items means a little over ten times the work.

Rules: don't use sorted() or .sort(). Each sort returns a new list and
leaves the original unchanged.
"""

from collections.abc import Callable


def find_min_index(items: list, start: int = 0) -> int:
    """Return the position of the smallest item from position start onwards.

    If the smallest value appears more than once, return the first
    position. You can assume there is at least one item to look at.
    This is the building block of selection sort.

    >>> find_min_index([5, 2, 8, 1, 9])
    3
    >>> find_min_index([1, 5, 2, 8], start=1)
    2
    """
    raise NotImplementedError


def bubble_sort(items: list) -> list:
    """Sort by swapping neighbours that are in the wrong order.

    Go through the list comparing each item with the next, and swap them
    if they're the wrong way round. Each pass carries the largest
    remaining item to the end. Keep making passes until one needs no
    swaps.

    >>> bubble_sort([3, 1, 2])
    [1, 2, 3]
    """
    raise NotImplementedError


def selection_sort(items: list) -> list:
    """Sort by repeatedly selecting the smallest remaining item.

    For each position in turn, find the smallest item from there onwards
    and swap it into that position. Use find_min_index.

    >>> selection_sort([3, 1, 2])
    [1, 2, 3]
    """
    raise NotImplementedError


def insertion_sort(items: list) -> list:
    """Sort the way most people sort a hand of cards.

    Take the items one at a time. Slide each one backwards past every
    larger item until it's in place among the items already sorted. This
    is very fast when the list is nearly sorted already.

    >>> insertion_sort([3, 1, 2])
    [1, 2, 3]
    """
    raise NotImplementedError


def merge_sort(items: list) -> list:
    """Sort by splitting in half, sorting each half, and merging them.

    A list of zero or one items is already sorted: that's the base case.
    Otherwise sort each half with merge_sort itself, then merge the two
    sorted halves, as you did in merge_sorted in the lists topic.

    >>> merge_sort([3, 1, 2])
    [1, 2, 3]
    """
    raise NotImplementedError


def quick_sort(items: list) -> list:
    """Sort by choosing a pivot and partitioning around it.

    Pick one item as the pivot. Split the rest into the items smaller
    than it and the items not smaller. Sort both groups with quick_sort
    itself, then join them with the pivot in between.

    >>> quick_sort([3, 1, 2])
    [1, 2, 3]
    """
    raise NotImplementedError


def merge_sort_by(items: list, key: Callable) -> list:
    """Merge sort that compares key(item), like sorted(items, key=...). (Stretch)

    The sort must be stable: items with equal keys stay in their
    original order. That depends on one detail of the merge step. When
    the two items being compared are equal, which side must you take
    from first?

    >>> merge_sort_by(["ccc", "a", "bb"], key=len)
    ['a', 'bb', 'ccc']
    """
    raise NotImplementedError
