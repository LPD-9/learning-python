from loops_exercises import (
    collatz_steps,
    count_vowels,
    countdown,
    find_pair_with_sum,
    first_negative,
    sum_to,
    times_table,
)


class TestSumTo:
    def test_example(self):
        assert sum_to(4) == 10

    def test_one(self):
        assert sum_to(1) == 1

    def test_hundred(self):
        assert sum_to(100) == 5050

    def test_zero_and_negative(self):
        assert sum_to(0) == 0
        assert sum_to(-5) == 0


class TestCountVowels:
    def test_example(self):
        assert count_vowels("Education") == 5

    def test_uppercase(self):
        assert count_vowels("AEIOU") == 5

    def test_no_vowels(self):
        assert count_vowels("rhythm") == 0

    def test_empty(self):
        assert count_vowels("") == 0


class TestCountdown:
    def test_example(self):
        assert countdown(3) == [3, 2, 1, "Liftoff!"]

    def test_from_one(self):
        assert countdown(1) == [1, "Liftoff!"]

    def test_from_zero(self):
        assert countdown(0) == ["Liftoff!"]

    def test_negative_start(self):
        assert countdown(-4) == ["Liftoff!"]


class TestFirstNegative:
    def test_example(self):
        assert first_negative([4, -2, 7, -9]) == -2

    def test_negative_at_the_start(self):
        assert first_negative([-1, 5]) == -1

    def test_no_negatives(self):
        assert first_negative([0, 3, 8]) is None

    def test_empty(self):
        assert first_negative([]) is None


class TestTimesTable:
    def test_example(self):
        assert times_table(3, 4) == [
            "3 x 1 = 3",
            "3 x 2 = 6",
            "3 x 3 = 9",
            "3 x 4 = 12",
        ]

    def test_single_line(self):
        assert times_table(7, 1) == ["7 x 1 = 7"]

    def test_twelve_lines(self):
        table = times_table(12, 12)
        assert len(table) == 12
        assert table[-1] == "12 x 12 = 144"

    def test_no_lines(self):
        assert times_table(5, 0) == []


class TestCollatzSteps:
    def test_example(self):
        assert collatz_steps(6) == 8

    def test_already_at_one(self):
        assert collatz_steps(1) == 0

    def test_power_of_two(self):
        assert collatz_steps(16) == 4

    def test_long_sequence(self):
        assert collatz_steps(27) == 111


class TestFindPairWithSum:
    def test_example(self):
        assert find_pair_with_sum([2, 7, 11, 15], 9) == (0, 1)

    def test_pair_not_next_to_each_other(self):
        assert find_pair_with_sum([1, 8, 3, 6], 7) == (0, 3)

    def test_lowest_first_position_wins(self):
        assert find_pair_with_sum([1, 4, 2, 3], 5) == (0, 1)

    def test_two_equal_numbers(self):
        assert find_pair_with_sum([3, 3], 6) == (0, 1)

    def test_number_is_not_paired_with_itself(self):
        assert find_pair_with_sum([5, 1], 10) is None

    def test_no_pair(self):
        assert find_pair_with_sum([1, 2, 3], 7) is None

    def test_empty(self):
        assert find_pair_with_sum([], 4) is None
