import pytest
from lambdas_exercises import (
    calculate,
    cheapest,
    group_by,
    sort_by_age,
    sort_by_last_letter,
    sort_case_insensitive,
    sort_versions,
)

ADA = {"name": "Ada", "age": 36}
BOB = {"name": "Bob", "age": 25}
CAT = {"name": "Cat", "age": 41}


class TestSortByLastLetter:
    def test_example(self):
        assert sort_by_last_letter(["cab", "zoo", "arc"]) == ["cab", "arc", "zoo"]

    def test_original_is_unchanged(self):
        words = ["zoo", "cab"]
        sort_by_last_letter(words)
        assert words == ["zoo", "cab"]

    def test_empty(self):
        assert sort_by_last_letter([]) == []


class TestSortByAge:
    def test_example(self):
        assert sort_by_age([ADA, BOB]) == [BOB, ADA]

    def test_three_people(self):
        assert sort_by_age([CAT, ADA, BOB]) == [BOB, ADA, CAT]

    def test_empty(self):
        assert sort_by_age([]) == []


class TestCheapest:
    def test_example(self):
        pen = {"name": "pen", "price": 2}
        ink = {"name": "ink", "price": 1}
        assert cheapest([pen, ink]) == ink

    def test_single(self):
        pen = {"name": "pen", "price": 2}
        assert cheapest([pen]) == pen

    def test_empty(self):
        assert cheapest([]) is None


class TestSortCaseInsensitive:
    def test_example(self):
        result = sort_case_insensitive(["banana", "Apple", "cherry"])
        assert result == ["Apple", "banana", "cherry"]

    def test_original_spelling_is_kept(self):
        assert sort_case_insensitive(["b", "A", "C"]) == ["A", "b", "C"]


class TestSortVersions:
    def test_example(self):
        result = sort_versions(["1.10.0", "1.2.0", "1.9.3"])
        assert result == ["1.2.0", "1.9.3", "1.10.0"]

    def test_major_version_matters_most(self):
        assert sort_versions(["2.0.0", "1.99.99"]) == ["1.99.99", "2.0.0"]

    def test_last_part(self):
        assert sort_versions(["1.0.10", "1.0.9"]) == ["1.0.9", "1.0.10"]


class TestCalculate:
    def test_each_operator(self):
        assert calculate("+", 6, 3) == 9
        assert calculate("-", 6, 3) == 3
        assert calculate("*", 6, 3) == 18
        assert calculate("/", 6, 3) == 2

    def test_order_matters(self):
        assert calculate("-", 3, 6) == -3

    def test_unknown_operator(self):
        with pytest.raises(ValueError):
            calculate("%", 6, 3)


class TestGroupBy:
    def test_example(self):
        result = group_by(["apple", "avocado", "banana"], lambda word: word[0])
        assert result == {"a": ["apple", "avocado"], "b": ["banana"]}

    def test_group_numbers(self):
        result = group_by([1, 2, 3, 4, 5], lambda n: n % 2 == 0)
        assert result == {False: [1, 3, 5], True: [2, 4]}

    def test_key_can_be_any_function(self):
        assert group_by(["a", "bb", "cc"], len) == {1: ["a"], 2: ["bb", "cc"]}

    def test_empty(self):
        assert group_by([], len) == {}
