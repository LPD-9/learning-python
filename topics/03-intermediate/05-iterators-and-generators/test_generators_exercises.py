import itertools

import pytest
from generators_exercises import (
    Countdown,
    countdown_from,
    evens,
    fibonacci,
    flatten,
    non_blank_lines,
    take,
)


def is_iterator(thing):
    """True for generators and other one-pass iterators, False for lists."""
    return iter(thing) is thing


class TestCountdownFrom:
    def test_example(self):
        assert list(countdown_from(3)) == [3, 2, 1]

    def test_nothing_to_count(self):
        assert list(countdown_from(0)) == []

    def test_is_a_generator_not_a_list(self):
        assert is_iterator(countdown_from(3))

    def test_values_arrive_one_at_a_time(self):
        counter = countdown_from(2)
        assert next(counter) == 2
        assert next(counter) == 1
        with pytest.raises(StopIteration):
            next(counter)


class TestEvens:
    def test_example(self):
        assert list(evens([1, 2, 3, 4])) == [2, 4]

    def test_is_a_generator_not_a_list(self):
        assert is_iterator(evens([1, 2]))

    def test_works_on_an_endless_input(self):
        endless = itertools.count(1)
        assert list(itertools.islice(evens(endless), 3)) == [2, 4, 6]


class TestTake:
    def test_example(self):
        assert take("abcdef", 2) == ["a", "b"]

    def test_fewer_items_than_asked_for(self):
        assert take([1, 2], 5) == [1, 2]

    def test_zero(self):
        assert take([1, 2], 0) == []

    def test_endless_input(self):
        assert take(itertools.count(10), 3) == [10, 11, 12]

    def test_leaves_the_rest_untouched(self):
        numbers = iter([1, 2, 3, 4])
        take(numbers, 2)
        assert next(numbers) == 3


class TestFibonacci:
    def test_first_ten(self):
        first_ten = list(itertools.islice(fibonacci(), 10))
        assert first_ten == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_each_call_starts_again(self):
        first = fibonacci()
        next(first)
        next(first)
        assert next(fibonacci()) == 0


class TestNonBlankLines:
    def test_example(self):
        assert list(non_blank_lines(["  one ", "", "   ", "two"])) == ["one", "two"]

    def test_line_endings_are_removed(self):
        assert list(non_blank_lines(["a\n", "\n", "b\n"])) == ["a", "b"]

    def test_is_a_generator_not_a_list(self):
        assert is_iterator(non_blank_lines([]))


class TestCountdown:
    def test_example(self):
        assert list(Countdown(3)) == [3, 2, 1]

    def test_works_in_a_for_loop(self):
        seen = []
        for number in Countdown(2):
            seen.append(number)
        assert seen == [2, 1]

    def test_iter_returns_itself(self):
        countdown = Countdown(3)
        assert iter(countdown) is countdown

    def test_next_raises_stop_iteration_when_done(self):
        countdown = Countdown(1)
        assert next(countdown) == 1
        with pytest.raises(StopIteration):
            next(countdown)

    def test_nothing_to_count(self):
        assert list(Countdown(0)) == []


class TestFlatten:
    def test_example(self):
        assert list(flatten([1, [2, [3, 4]], 5])) == [1, 2, 3, 4, 5]

    def test_already_flat(self):
        assert list(flatten([1, 2, 3])) == [1, 2, 3]

    def test_empty_lists_disappear(self):
        assert list(flatten([[], [1, []], [[]]])) == [1]

    def test_strings_are_not_split_up(self):
        assert list(flatten(["ab", ["cd"]])) == ["ab", "cd"]

    def test_is_a_generator_not_a_list(self):
        assert is_iterator(flatten([1]))
