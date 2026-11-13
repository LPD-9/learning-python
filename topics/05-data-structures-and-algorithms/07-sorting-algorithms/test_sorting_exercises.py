import random

import pytest
from sorting_exercises import (
    bubble_sort,
    find_min_index,
    insertion_sort,
    merge_sort,
    merge_sort_by,
    quick_sort,
    selection_sort,
)

SORTS = [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort]

CASES = [
    [],
    [1],
    [2, 1],
    [3, 1, 2],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [2, 3, 2, 1, 3, 1],
    [0, -5, 3, -1],
    [7, 7, 7],
    ["pear", "apple", "fig"],
]


class TestFindMinIndex:
    def test_example(self):
        assert find_min_index([5, 2, 8, 1, 9]) == 3

    def test_from_a_later_start(self):
        assert find_min_index([1, 5, 2, 8], start=1) == 2

    def test_first_of_equal_smallest(self):
        assert find_min_index([4, 1, 9, 1]) == 1

    def test_start_at_the_last_item(self):
        assert find_min_index([4, 1, 9], start=2) == 2

    def test_single_item(self):
        assert find_min_index([7]) == 0


@pytest.mark.parametrize("sort", SORTS, ids=lambda sort: sort.__name__)
class TestEverySort:
    @pytest.mark.parametrize("items", CASES, ids=repr)
    def test_sorts_correctly(self, sort, items):
        assert sort(list(items)) == sorted(items)

    def test_original_is_unchanged(self, sort):
        items = [3, 1, 2]
        sort(items)
        assert items == [3, 1, 2]

    def test_returns_a_new_list(self, sort):
        items = [1, 2, 3]
        assert sort(items) is not items

    def test_random_lists(self, sort):
        rng = random.Random(42)
        for size in [10, 50, 200]:
            items = [rng.randint(-100, 100) for _ in range(size)]
            assert sort(items) == sorted(items)


class TestMergeSortBy:
    def test_example(self):
        assert merge_sort_by(["ccc", "a", "bb"], key=len) == ["a", "bb", "ccc"]

    def test_is_stable(self):
        people = [("bob", 2), ("ada", 1), ("cat", 2), ("dan", 1)]
        result = merge_sort_by(people, key=lambda person: person[1])
        assert result == [("ada", 1), ("dan", 1), ("bob", 2), ("cat", 2)]

    def test_stable_on_a_longer_list(self):
        rng = random.Random(3)
        records = [(rng.randint(0, 5), position) for position in range(200)]
        result = merge_sort_by(records, key=lambda record: record[0])
        assert result == sorted(records, key=lambda record: record[0])

    def test_key_can_reverse_the_order(self):
        assert merge_sort_by([1, 3, 2], key=lambda n: -n) == [3, 2, 1]

    def test_empty(self):
        assert merge_sort_by([], key=len) == []

    def test_original_is_unchanged(self):
        items = ["bb", "a"]
        merge_sort_by(items, key=len)
        assert items == ["bb", "a"]
