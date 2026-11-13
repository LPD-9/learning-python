from integers_exercises import (
    digit_sum,
    factorial_digit_count,
    is_power_of_two,
    round_up_to_multiple,
    split_seconds,
    to_binary,
)


class TestDigitSum:
    def test_positive(self):
        assert digit_sum(472) == 13

    def test_negative(self):
        assert digit_sum(-472) == 13

    def test_zero(self):
        assert digit_sum(0) == 0

    def test_large_number(self):
        assert digit_sum(10**20 + 5) == 6


class TestSplitSeconds:
    def test_example(self):
        assert split_seconds(3725) == (1, 2, 5)

    def test_under_a_minute(self):
        assert split_seconds(59) == (0, 0, 59)

    def test_exact_hours(self):
        assert split_seconds(7200) == (2, 0, 0)

    def test_more_than_a_day(self):
        assert split_seconds(90061) == (25, 1, 1)


class TestRoundUpToMultiple:
    def test_rounds_up(self):
        assert round_up_to_multiple(17, 5) == 20

    def test_already_a_multiple(self):
        assert round_up_to_multiple(20, 5) == 20

    def test_zero(self):
        assert round_up_to_multiple(0, 5) == 0

    def test_multiple_of_one(self):
        assert round_up_to_multiple(13, 1) == 13

    def test_returns_an_int(self):
        assert isinstance(round_up_to_multiple(17, 5), int)


class TestToBinary:
    def test_example(self):
        assert to_binary(10) == "1010"

    def test_zero(self):
        assert to_binary(0) == "0"

    def test_one(self):
        assert to_binary(1) == "1"

    def test_power_of_two(self):
        assert to_binary(256) == "100000000"


class TestIsPowerOfTwo:
    def test_powers(self):
        assert all(is_power_of_two(2**i) for i in range(20))

    def test_not_powers(self):
        assert not any(is_power_of_two(n) for n in [3, 6, 12, 100, 1023])

    def test_zero_and_negatives(self):
        assert not is_power_of_two(0)
        assert not is_power_of_two(-8)


class TestFactorialDigitCount:
    def test_example(self):
        assert factorial_digit_count(10) == 7

    def test_zero_factorial_is_one(self):
        assert factorial_digit_count(0) == 1

    def test_large(self):
        assert factorial_digit_count(100) == 158
