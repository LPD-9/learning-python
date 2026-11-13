import pytest
from iteration_exercises import (
    chunk,
    first_letters,
    number_lines,
    pair_up,
    running_total,
    squares_of_evens,
    transpose,
    word_lengths,
)


class TestSquaresOfEvens:
    def test_example(self):
        assert squares_of_evens([1, 2, 3, 4]) == [4, 16]

    def test_negative_numbers_and_zero(self):
        assert squares_of_evens([-2, 0, 5]) == [4, 0]

    def test_no_evens(self):
        assert squares_of_evens([1, 3, 5]) == []


class TestWordLengths:
    def test_example(self):
        assert word_lengths(["hi", "there"]) == {"hi": 2, "there": 5}

    def test_empty(self):
        assert word_lengths([]) == {}


class TestFirstLetters:
    def test_example(self):
        assert first_letters(["Apple", "avocado", "", "banana"]) == {"a", "b"}

    def test_empty(self):
        assert first_letters([]) == set()


class TestNumberLines:
    def test_example(self):
        result = number_lines(["import os", "print(os.getcwd())"])
        assert result == ["1: import os", "2: print(os.getcwd())"]

    def test_empty(self):
        assert number_lines([]) == []


class TestPairUp:
    def test_example(self):
        assert pair_up(["ann", "ben"], [7, 9]) == {"ann": 7, "ben": 9}

    def test_too_few_scores(self):
        with pytest.raises(ValueError):
            pair_up(["ann", "ben"], [7])

    def test_too_many_scores(self):
        with pytest.raises(ValueError):
            pair_up(["ann"], [7, 9])

    def test_empty(self):
        assert pair_up([], []) == {}


class TestChunk:
    def test_example(self):
        assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

    def test_exact_fit(self):
        assert chunk(["a", "b", "c", "d"], 2) == [["a", "b"], ["c", "d"]]

    def test_size_bigger_than_list(self):
        assert chunk([1, 2], 10) == [[1, 2]]

    def test_chunks_are_lists(self):
        assert all(isinstance(c, list) for c in chunk([1, 2, 3], 2))

    def test_empty(self):
        assert chunk([], 3) == []

    def test_invalid_size(self):
        with pytest.raises(ValueError):
            chunk([1, 2, 3], 0)


class TestRunningTotal:
    def test_example(self):
        assert running_total([3, 1, 4]) == [3, 4, 8]

    def test_with_negatives(self):
        assert running_total([5, -5, 2]) == [5, 0, 2]

    def test_empty(self):
        assert running_total([]) == []


class TestTranspose:
    def test_example(self):
        assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

    def test_square(self):
        assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

    def test_rows_are_lists(self):
        assert all(isinstance(row, list) for row in transpose([[1, 2], [3, 4]]))

    def test_empty(self):
        assert transpose([]) == []
