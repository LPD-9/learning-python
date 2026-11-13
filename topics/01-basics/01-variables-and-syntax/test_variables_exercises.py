from variables_exercises import (
    celsius_to_fahrenheit,
    compound_interest,
    full_name,
    receipt_line,
    rectangle_area,
    swap,
    type_name,
)


class TestRectangleArea:
    def test_example(self):
        assert rectangle_area(3, 4) == 12

    def test_square(self):
        assert rectangle_area(5, 5) == 25

    def test_decimal_sides(self):
        assert rectangle_area(2.5, 4) == 10.0

    def test_zero_width(self):
        assert rectangle_area(0, 9) == 0


class TestFullName:
    def test_example(self):
        assert full_name("Ada", "Lovelace") == "Ada Lovelace"

    def test_another_name(self):
        assert full_name("Alan", "Turing") == "Alan Turing"


class TestCelsiusToFahrenheit:
    def test_boiling(self):
        assert celsius_to_fahrenheit(100) == 212

    def test_freezing(self):
        assert celsius_to_fahrenheit(0) == 32

    def test_same_in_both_scales(self):
        assert celsius_to_fahrenheit(-40) == -40

    def test_body_temperature(self):
        assert round(celsius_to_fahrenheit(37), 1) == 98.6


class TestSwap:
    def test_example(self):
        assert swap(1, 2) == (2, 1)

    def test_different_types(self):
        assert swap("a", None) == (None, "a")

    def test_returns_a_tuple(self):
        assert isinstance(swap(1, 2), tuple)


class TestTypeName:
    def test_int(self):
        assert type_name(42) == "int"

    def test_str(self):
        assert type_name("hello") == "str"

    def test_float(self):
        assert type_name(3.0) == "float"

    def test_bool(self):
        assert type_name(True) == "bool"

    def test_list(self):
        assert type_name([1, 2]) == "list"

    def test_none(self):
        assert type_name(None) == "NoneType"


class TestReceiptLine:
    def test_example(self):
        assert receipt_line("Coffee", 3, 2.5) == "3 x Coffee @ £2.50 = £7.50"

    def test_single_item(self):
        assert receipt_line("Bagel", 1, 1.2) == "1 x Bagel @ £1.20 = £1.20"

    def test_whole_pound_price(self):
        assert receipt_line("Mug", 2, 8) == "2 x Mug @ £8.00 = £16.00"

    def test_large_total(self):
        assert receipt_line("Pen", 12, 0.99) == "12 x Pen @ £0.99 = £11.88"


class TestCompoundInterest:
    def test_example(self):
        assert compound_interest(1000, 5, 2) == 1102.5

    def test_one_year(self):
        assert compound_interest(500, 10, 1) == 550.0

    def test_no_interest(self):
        assert compound_interest(1000, 0, 10) == 1000.0

    def test_zero_years(self):
        assert compound_interest(750, 4, 0) == 750.0

    def test_rounds_to_two_places(self):
        assert compound_interest(100, 3.3, 3) == 110.23
