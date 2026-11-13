from conditionals_exercises import (
    fizzbuzz_value,
    grade,
    http_status_text,
    shipping_cost,
    sign,
    ticket_price,
    triangle_type,
)


class TestSign:
    def test_positive(self):
        assert sign(8) == "positive"

    def test_negative(self):
        assert sign(-3) == "negative"

    def test_zero(self):
        assert sign(0) == "zero"

    def test_small_decimal(self):
        assert sign(-0.001) == "negative"


class TestTicketPrice:
    def test_adult(self):
        assert ticket_price(30) == 10

    def test_child(self):
        assert ticket_price(8) == 5

    def test_senior(self):
        assert ticket_price(70) == 7

    def test_thirteen_is_an_adult(self):
        assert ticket_price(12) == 5
        assert ticket_price(13) == 10

    def test_sixty_five_is_a_senior(self):
        assert ticket_price(64) == 10
        assert ticket_price(65) == 7


class TestGrade:
    def test_each_band(self):
        assert grade(95) == "A"
        assert grade(85) == "B"
        assert grade(75) == "C"
        assert grade(65) == "D"
        assert grade(40) == "F"

    def test_lowest_score_in_each_band(self):
        assert grade(90) == "A"
        assert grade(80) == "B"
        assert grade(70) == "C"
        assert grade(60) == "D"

    def test_highest_score_below_each_band(self):
        assert grade(89) == "B"
        assert grade(59) == "F"

    def test_extremes(self):
        assert grade(100) == "A"
        assert grade(0) == "F"


class TestFizzbuzzValue:
    def test_multiple_of_three(self):
        assert fizzbuzz_value(9) == "Fizz"

    def test_multiple_of_five(self):
        assert fizzbuzz_value(10) == "Buzz"

    def test_multiple_of_both(self):
        assert fizzbuzz_value(15) == "FizzBuzz"
        assert fizzbuzz_value(30) == "FizzBuzz"

    def test_other_numbers_become_strings(self):
        assert fizzbuzz_value(7) == "7"
        assert fizzbuzz_value(1) == "1"


class TestShippingCost:
    def test_light(self):
        assert shipping_cost(0.5, express=False) == 3.0

    def test_medium(self):
        assert shipping_cost(2, express=False) == 6.0

    def test_heavy(self):
        assert shipping_cost(12, express=False) == 10.0

    def test_weight_limits_are_included(self):
        assert shipping_cost(1, express=False) == 3.0
        assert shipping_cost(5, express=False) == 6.0

    def test_express_doubles(self):
        assert shipping_cost(0.5, express=True) == 6.0
        assert shipping_cost(2, express=True) == 12.0
        assert shipping_cost(12, express=True) == 20.0


class TestHttpStatusText:
    def test_named_codes(self):
        assert http_status_text(200) == "OK"
        assert http_status_text(404) == "Not Found"
        assert http_status_text(500) == "Server Error"

    def test_other_client_errors(self):
        assert http_status_text(400) == "Client Error"
        assert http_status_text(403) == "Client Error"
        assert http_status_text(499) == "Client Error"

    def test_other_server_errors(self):
        assert http_status_text(503) == "Server Error"
        assert http_status_text(599) == "Server Error"

    def test_unknown(self):
        assert http_status_text(302) == "Unknown"
        assert http_status_text(600) == "Unknown"
        assert http_status_text(99) == "Unknown"


class TestTriangleType:
    def test_equilateral(self):
        assert triangle_type(3, 3, 3) == "equilateral"

    def test_isosceles(self):
        assert triangle_type(5, 5, 8) == "isosceles"
        assert triangle_type(8, 5, 5) == "isosceles"
        assert triangle_type(5, 8, 5) == "isosceles"

    def test_scalene(self):
        assert triangle_type(3, 4, 5) == "scalene"

    def test_sides_cannot_meet(self):
        assert triangle_type(1, 2, 10) == "invalid"
        assert triangle_type(10, 1, 2) == "invalid"

    def test_flat_triangle_is_invalid(self):
        assert triangle_type(1, 2, 3) == "invalid"

    def test_zero_or_negative_side(self):
        assert triangle_type(0, 4, 4) == "invalid"
        assert triangle_type(3, -3, 3) == "invalid"
