from builtins_exercises import (
    all_passed,
    average,
    closest_to,
    is_sorted,
    longest_word,
    spread,
    sum_numbers,
)


class TestAverage:
    def test_example(self):
        assert average([2, 4, 9]) == 5.0

    def test_single(self):
        assert average([7]) == 7.0

    def test_decimal_result(self):
        assert average([1, 2]) == 1.5

    def test_empty(self):
        assert average([]) == 0.0


class TestSpread:
    def test_example(self):
        assert spread([4, 9, 1, 6]) == 8

    def test_negatives(self):
        assert spread([-5, 5]) == 10

    def test_single(self):
        assert spread([3]) == 0

    def test_empty(self):
        assert spread([]) == 0


class TestAllPassed:
    def test_everyone_passed(self):
        assert all_passed([70, 85, 62], 60) is True

    def test_one_failed(self):
        assert all_passed([70, 59, 62], 60) is False

    def test_exactly_on_the_pass_mark(self):
        assert all_passed([60, 60], 60) is True

    def test_empty(self):
        assert all_passed([], 60) is True


class TestLongestWord:
    def test_example(self):
        assert longest_word(["tea", "coffee", "water"]) == "coffee"

    def test_tie_returns_the_earliest(self):
        assert longest_word(["cat", "dog", "ox"]) == "cat"

    def test_single(self):
        assert longest_word(["hello"]) == "hello"

    def test_empty(self):
        assert longest_word([]) == ""


class TestClosestTo:
    def test_example(self):
        assert closest_to([10, 22, 31, 47], 30) == 31

    def test_exact_match(self):
        assert closest_to([5, 10, 15], 10) == 10

    def test_target_below_every_number(self):
        assert closest_to([5, 10, 15], -100) == 5

    def test_tie_returns_the_earliest(self):
        assert closest_to([8, 12], 10) == 8
        assert closest_to([12, 8], 10) == 12

    def test_negatives(self):
        assert closest_to([-3, -8, 4], -6) == -8


class TestSumNumbers:
    def test_example(self):
        assert sum_numbers([1, "2", 3.5, None, True]) == 4.5

    def test_only_numbers(self):
        assert sum_numbers([1, 2, 3]) == 6

    def test_booleans_are_ignored(self):
        assert sum_numbers([True, False, True]) == 0

    def test_nothing_to_add(self):
        assert sum_numbers(["a", None, []]) == 0

    def test_empty(self):
        assert sum_numbers([]) == 0


class TestIsSorted:
    def test_sorted(self):
        assert is_sorted([1, 2, 2, 5]) is True

    def test_not_sorted(self):
        assert is_sorted([3, 1, 2]) is False

    def test_only_the_last_item_is_out_of_place(self):
        assert is_sorted([1, 2, 3, 0]) is False

    def test_descending(self):
        assert is_sorted([3, 2, 1]) is False

    def test_strings(self):
        assert is_sorted(["apple", "banana", "cherry"]) is True

    def test_single_and_empty(self):
        assert is_sorted([7]) is True
        assert is_sorted([]) is True

    def test_list_is_not_changed(self):
        items = [3, 1, 2]
        is_sorted(items)
        assert items == [3, 1, 2]
