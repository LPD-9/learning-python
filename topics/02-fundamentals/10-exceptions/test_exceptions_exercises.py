import pytest
from exceptions_exercises import (
    InsufficientFundsError,
    convert_all,
    get_item,
    parse_age,
    read_setting,
    require_positive,
    safe_divide,
    withdraw,
)


class TestSafeDivide:
    def test_example(self):
        assert safe_divide(10, 4) == 2.5

    def test_divide_by_zero(self):
        assert safe_divide(10, 0) is None

    def test_zero_divided_by_something(self):
        assert safe_divide(0, 5) == 0


class TestGetItem:
    def test_valid_index(self):
        assert get_item(["a", "b"], 1) == "b"

    def test_index_too_big(self):
        assert get_item(["a", "b"], 5, default="?") == "?"

    def test_default_is_none(self):
        assert get_item([], 0) is None

    def test_negative_index_counts_from_the_end(self):
        assert get_item(["a", "b"], -1) == "b"

    def test_negative_index_too_big(self):
        assert get_item(["a", "b"], -3, default="?") == "?"

    def test_a_falsy_item_is_still_returned(self):
        assert get_item([0, 1], 0, default="?") == 0


class TestRequirePositive:
    def test_positive(self):
        assert require_positive(3) == 3

    def test_negative(self):
        with pytest.raises(ValueError, match="must be positive, got -3"):
            require_positive(-3)

    def test_zero(self):
        with pytest.raises(ValueError, match="must be positive, got 0"):
            require_positive(0)


class TestParseAge:
    def test_example(self):
        assert parse_age("42") == 42

    def test_limits_are_allowed(self):
        assert parse_age("0") == 0
        assert parse_age("150") == 150

    def test_not_a_number(self):
        with pytest.raises(ValueError, match="age must be a whole number"):
            parse_age("forty")

    def test_decimal(self):
        with pytest.raises(ValueError, match="age must be a whole number"):
            parse_age("4.5")

    def test_too_old(self):
        with pytest.raises(ValueError, match="age must be between 0 and 150"):
            parse_age("151")

    def test_negative(self):
        with pytest.raises(ValueError, match="age must be between 0 and 150"):
            parse_age("-1")


class TestConvertAll:
    def test_example(self):
        assert convert_all(["1", "x", "3"]) == ([1, 3], ["x"])

    def test_all_good(self):
        assert convert_all(["10", "20"]) == ([10, 20], [])

    def test_all_bad(self):
        assert convert_all(["a", ""]) == ([], ["a", ""])

    def test_empty(self):
        assert convert_all([]) == ([], [])


class TestReadSetting:
    def test_present(self):
        assert read_setting({"host": "localhost"}, "host") == "localhost"

    def test_missing(self):
        with pytest.raises(ValueError, match="missing setting: port"):
            read_setting({"host": "localhost"}, "port")

    def test_original_error_is_chained(self):
        with pytest.raises(ValueError) as error:
            read_setting({}, "port")
        assert isinstance(error.value.__cause__, KeyError)


class TestWithdraw:
    def test_example(self):
        assert withdraw(100, 30) == 70

    def test_whole_balance(self):
        assert withdraw(50, 50) == 0

    def test_zero_amount(self):
        with pytest.raises(ValueError):
            withdraw(100, 0)

    def test_negative_amount(self):
        with pytest.raises(ValueError):
            withdraw(100, -5)

    def test_not_enough_money(self):
        with pytest.raises(InsufficientFundsError):
            withdraw(100, 120)

    def test_shortfall_is_recorded(self):
        with pytest.raises(InsufficientFundsError) as error:
            withdraw(100, 120)
        assert error.value.shortfall == 20

    def test_error_has_a_message(self):
        with pytest.raises(InsufficientFundsError) as error:
            withdraw(100, 120)
        assert str(error.value) != ""

    def test_custom_error_is_not_a_value_error(self):
        assert issubclass(InsufficientFundsError, Exception)
        assert not issubclass(InsufficientFundsError, ValueError)
