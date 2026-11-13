import math
from decimal import Decimal

from floats_exercises import (
    format_bytes,
    mean_ignoring_nan,
    nearly_equal,
    percentage,
    split_bill,
    total_price,
)


class TestPercentage:
    def test_example(self):
        assert percentage(1, 3) == 33.3

    def test_whole_number(self):
        assert percentage(50, 200) == 25.0

    def test_rounds_correctly(self):
        assert percentage(2, 3) == 66.7

    def test_zero_whole(self):
        assert percentage(5, 0) == 0.0


class TestNearlyEqual:
    def test_rounding_error(self):
        assert nearly_equal(0.1 + 0.2, 0.3)

    def test_clearly_different(self):
        assert not nearly_equal(1.0, 1.1)

    def test_exactly_equal(self):
        assert nearly_equal(2.5, 2.5)

    def test_large_numbers(self):
        assert nearly_equal(1e20 + 1, 1e20)


class TestFormatBytes:
    def test_bytes(self):
        assert format_bytes(512) == "512 B"

    def test_zero(self):
        assert format_bytes(0) == "0 B"

    def test_kilobytes(self):
        assert format_bytes(1536) == "1.5 KB"

    def test_exactly_one_unit(self):
        assert format_bytes(1024) == "1.0 KB"
        assert format_bytes(1024**2) == "1.0 MB"

    def test_gigabytes(self):
        assert format_bytes(5 * 1024**3) == "5.0 GB"

    def test_terabytes_is_the_largest_unit(self):
        assert format_bytes(2048 * 1024**4) == "2048.0 TB"


class TestTotalPrice:
    def test_example(self):
        assert total_price(["0.10", "0.20"]) == Decimal("0.30")

    def test_returns_a_decimal(self):
        assert isinstance(total_price(["1.00"]), Decimal)

    def test_many_small_amounts(self):
        assert total_price(["0.01"] * 100) == Decimal("1.00")

    def test_empty(self):
        assert total_price([]) == Decimal("0")


class TestMeanIgnoringNan:
    def test_example(self):
        assert mean_ignoring_nan([1.0, float("nan"), 3.0]) == 2.0

    def test_no_nans(self):
        assert mean_ignoring_nan([2.0, 4.0]) == 3.0

    def test_all_nan(self):
        assert math.isnan(mean_ignoring_nan([float("nan"), float("nan")]))

    def test_empty(self):
        assert math.isnan(mean_ignoring_nan([]))


class TestSplitBill:
    def test_example(self):
        assert split_bill(10.00, 3) == [3.34, 3.33, 3.33]

    def test_even_split(self):
        assert split_bill(9.00, 3) == [3.00, 3.00, 3.00]

    def test_two_extra_pennies(self):
        assert split_bill(1.00, 3) == [0.34, 0.33, 0.33]
        assert split_bill(0.05, 3) == [0.02, 0.02, 0.01]

    def test_one_person(self):
        assert split_bill(12.34, 1) == [12.34]

    def test_adds_up_exactly(self):
        shares = split_bill(100.00, 7)
        assert round(sum(shares) * 100) == 10000
