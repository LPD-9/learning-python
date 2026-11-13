import itertools

from recursion_exercises import (
    binary_search,
    factorial,
    fibonacci,
    permutations,
    reverse_string,
    sum_list,
    total_size,
)


class TestFactorial:
    def test_example(self):
        assert factorial(5) == 120

    def test_base_cases(self):
        assert factorial(0) == 1
        assert factorial(1) == 1

    def test_larger(self):
        assert factorial(10) == 3628800


class TestSumList:
    def test_example(self):
        assert sum_list([3, 1, 4]) == 8

    def test_single(self):
        assert sum_list([7]) == 7

    def test_empty(self):
        assert sum_list([]) == 0

    def test_original_is_unchanged(self):
        numbers = [1, 2, 3]
        sum_list(numbers)
        assert numbers == [1, 2, 3]


class TestReverseString:
    def test_example(self):
        assert reverse_string("abc") == "cba"

    def test_single_character(self):
        assert reverse_string("x") == "x"

    def test_empty(self):
        assert reverse_string("") == ""

    def test_sentence(self):
        assert reverse_string("hello world") == "dlrow olleh"


class TestFibonacci:
    def test_first_few(self):
        assert [fibonacci(n) for n in range(8)] == [0, 1, 1, 2, 3, 5, 8, 13]

    def test_example(self):
        assert fibonacci(10) == 55

    def test_twenty(self):
        assert fibonacci(20) == 6765


class TestTotalSize:
    def test_example(self):
        tree = {"a.txt": 10, "docs": {"b.txt": 5, "old": {"c.txt": 1}}}
        assert total_size(tree) == 16

    def test_flat_folder(self):
        assert total_size({"a": 1, "b": 2}) == 3

    def test_empty_folder(self):
        assert total_size({}) == 0

    def test_empty_folders_inside(self):
        assert total_size({"empty": {}, "more": {"also empty": {}}, "f": 4}) == 4


class TestBinarySearch:
    ITEMS = (1, 3, 5, 7, 9, 11)

    def test_example(self):
        assert binary_search([1, 3, 5, 7, 9], 7) == 3

    def test_every_position(self):
        items = list(self.ITEMS)
        for position, value in enumerate(items):
            assert binary_search(items, value) == position

    def test_absent(self):
        items = list(self.ITEMS)
        assert binary_search(items, 4) == -1
        assert binary_search(items, 0) == -1
        assert binary_search(items, 99) == -1

    def test_single_item(self):
        assert binary_search([5], 5) == 0
        assert binary_search([5], 6) == -1

    def test_empty(self):
        assert binary_search([], 5) == -1

    def test_large_list(self):
        items = list(range(0, 2_000_000, 2))
        assert binary_search(items, 1_234_568) == 617_284
        assert binary_search(items, 1_234_567) == -1


class TestPermutations:
    def test_two_items(self):
        assert sorted(permutations([1, 2])) == [[1, 2], [2, 1]]

    def test_three_items(self):
        expected = [list(order) for order in itertools.permutations("abc")]
        assert sorted(permutations(["a", "b", "c"])) == sorted(expected)

    def test_count_for_four_items(self):
        assert len(permutations([1, 2, 3, 4])) == 24

    def test_single(self):
        assert permutations([7]) == [[7]]

    def test_empty(self):
        assert permutations([]) == [[]]

    def test_original_is_unchanged(self):
        items = [1, 2, 3]
        permutations(items)
        assert items == [1, 2, 3]
