import pytest
from lists_exercises import (
    flatten_once,
    merge_sorted,
    move_zeros_to_end,
    remove_all,
    rotate,
    second_largest,
    unique_in_order,
)


class TestUniqueInOrder:
    def test_numbers(self):
        assert unique_in_order([3, 1, 3, 2, 1]) == [3, 1, 2]

    def test_strings(self):
        assert unique_in_order(["b", "a", "b"]) == ["b", "a"]

    def test_no_duplicates(self):
        assert unique_in_order([1, 2, 3]) == [1, 2, 3]

    def test_empty(self):
        assert unique_in_order([]) == []


class TestRemoveAll:
    def test_example(self):
        assert remove_all([1, 2, 1, 3], 1) == [2, 3]

    def test_value_not_present(self):
        assert remove_all([1, 2], 5) == [1, 2]

    def test_original_unchanged(self):
        items = [1, 2, 1]
        remove_all(items, 1)
        assert items == [1, 2, 1]


class TestRotate:
    def test_example(self):
        assert rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

    def test_zero(self):
        assert rotate([1, 2, 3], 0) == [1, 2, 3]

    def test_full_rotation(self):
        assert rotate([1, 2, 3], 3) == [1, 2, 3]

    def test_k_larger_than_list(self):
        assert rotate([1, 2, 3], 4) == [3, 1, 2]

    def test_empty(self):
        assert rotate([], 3) == []

    def test_original_unchanged(self):
        items = [1, 2, 3]
        rotate(items, 1)
        assert items == [1, 2, 3]


class TestFlattenOnce:
    def test_example(self):
        assert flatten_once([[1, 2], [], [3]]) == [1, 2, 3]

    def test_only_one_level(self):
        assert flatten_once([[1, [2]], [3]]) == [1, [2], 3]

    def test_empty(self):
        assert flatten_once([]) == []


class TestSecondLargest:
    def test_example(self):
        assert second_largest([4, 9, 9, 2]) == 4

    def test_negatives(self):
        assert second_largest([-5, -1, -3]) == -3

    def test_all_the_same(self):
        with pytest.raises(ValueError):
            second_largest([7, 7, 7])

    def test_too_short(self):
        with pytest.raises(ValueError):
            second_largest([1])


class TestMoveZerosToEnd:
    def test_example(self):
        nums = [0, 1, 0, 3, 12]
        move_zeros_to_end(nums)
        assert nums == [1, 3, 12, 0, 0]

    def test_returns_none(self):
        assert move_zeros_to_end([0, 1]) is None

    def test_no_zeros(self):
        nums = [1, 2, 3]
        move_zeros_to_end(nums)
        assert nums == [1, 2, 3]

    def test_all_zeros(self):
        nums = [0, 0]
        move_zeros_to_end(nums)
        assert nums == [0, 0]

    def test_same_list_object(self):
        nums = [0, 5]
        alias = nums
        move_zeros_to_end(nums)
        assert alias == [5, 0]


class TestMergeSorted:
    def test_example(self):
        assert merge_sorted([1, 4, 9], [2, 3, 10]) == [1, 2, 3, 4, 9, 10]

    def test_one_empty(self):
        assert merge_sorted([], [1, 2]) == [1, 2]
        assert merge_sorted([1, 2], []) == [1, 2]

    def test_duplicates(self):
        assert merge_sorted([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]

    def test_one_list_entirely_first(self):
        assert merge_sorted([1, 2], [5, 6]) == [1, 2, 5, 6]
