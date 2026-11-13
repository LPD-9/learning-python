import pytest
from type_casting_exercises import (
    add_number_strings,
    cast_row,
    digits_of,
    parse_number,
    safe_int,
    to_bool,
    unique_sorted,
)


class TestAddNumberStrings:
    def test_example(self):
        assert add_number_strings("2", "3") == 5

    def test_larger_numbers(self):
        assert add_number_strings("120", "45") == 165

    def test_negative(self):
        assert add_number_strings("-4", "10") == 6

    def test_returns_an_int(self):
        assert isinstance(add_number_strings("1", "1"), int)


class TestDigitsOf:
    def test_example(self):
        assert digits_of(4071) == [4, 0, 7, 1]

    def test_single_digit(self):
        assert digits_of(5) == [5]

    def test_zero(self):
        assert digits_of(0) == [0]

    def test_digits_are_ints(self):
        assert all(isinstance(digit, int) for digit in digits_of(123))


class TestUniqueSorted:
    def test_example(self):
        assert unique_sorted([3, 1, 3, 2, 1]) == [1, 2, 3]

    def test_returns_a_list(self):
        assert isinstance(unique_sorted([2, 1]), list)

    def test_empty(self):
        assert unique_sorted([]) == []


class TestToBool:
    def test_true_words(self):
        for text in ["yes", "true", "1", "on"]:
            assert to_bool(text) is True, text

    def test_false_words(self):
        for text in ["no", "false", "0", "off"]:
            assert to_bool(text) is False, text

    def test_ignores_case_and_whitespace(self):
        assert to_bool(" Yes ") is True
        assert to_bool("FALSE") is False

    def test_anything_else_is_an_error(self):
        with pytest.raises(ValueError):
            to_bool("maybe")

    def test_empty_is_an_error(self):
        with pytest.raises(ValueError):
            to_bool("")


class TestParseNumber:
    def test_whole_number(self):
        result = parse_number("42")
        assert result == 42
        assert isinstance(result, int)

    def test_decimal(self):
        result = parse_number("3.5")
        assert result == 3.5
        assert isinstance(result, float)

    def test_negative_whole_number(self):
        result = parse_number("-7")
        assert result == -7
        assert isinstance(result, int)

    def test_decimal_with_zero_fraction_stays_a_float(self):
        assert isinstance(parse_number("2.0"), float)

    def test_not_a_number(self):
        with pytest.raises(ValueError):
            parse_number("abc")


class TestCastRow:
    def test_example(self):
        assert cast_row(["Ada", "36", "91.5"], [str, int, float]) == ["Ada", 36, 91.5]

    def test_types_are_converted(self):
        name, age, score = cast_row(["Ada", "36", "91.5"], [str, int, float])
        assert isinstance(name, str)
        assert isinstance(age, int)
        assert isinstance(score, float)

    def test_empty(self):
        assert cast_row([], []) == []

    def test_bad_value(self):
        with pytest.raises(ValueError):
            cast_row(["Ada", "unknown"], [str, int])


class TestSafeInt:
    def test_int(self):
        assert safe_int(7) == 7

    def test_float_is_cut_down(self):
        assert safe_int(12.9) == 12

    def test_text(self):
        assert safe_int("12") == 12

    def test_text_with_spaces(self):
        assert safe_int(" 12 ") == 12

    def test_decimal_text(self):
        assert safe_int("12.9") == 12

    def test_text_that_is_not_a_number(self):
        assert safe_int("twelve") == 0
        assert safe_int("twelve", default=-1) == -1

    def test_none(self):
        assert safe_int(None) == 0
        assert safe_int(None, default=5) == 5

    def test_empty_text(self):
        assert safe_int("") == 0

    def test_always_returns_an_int(self):
        for value in [7, 12.9, "12.9", None, "x"]:
            assert isinstance(safe_int(value), int), value
