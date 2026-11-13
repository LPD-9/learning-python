from operators_exercises import (
    can_ride,
    clock_add,
    compare_objects,
    is_between,
    is_even,
    is_leap_year,
    is_vowel,
)


class TestIsEven:
    def test_even(self):
        assert is_even(4) is True

    def test_odd(self):
        assert is_even(7) is False

    def test_zero_is_even(self):
        assert is_even(0) is True

    def test_negative(self):
        assert is_even(-2) is True
        assert is_even(-3) is False


class TestIsBetween:
    def test_inside(self):
        assert is_between(5, 1, 10) is True

    def test_ends_are_included(self):
        assert is_between(1, 1, 10) is True
        assert is_between(10, 1, 10) is True

    def test_outside(self):
        assert is_between(0, 1, 10) is False
        assert is_between(10.5, 1, 10) is False


class TestIsVowel:
    def test_lowercase(self):
        assert is_vowel("a") is True

    def test_uppercase(self):
        assert is_vowel("E") is True

    def test_consonant(self):
        assert is_vowel("z") is False

    def test_y_is_not_a_vowel(self):
        assert is_vowel("y") is False


class TestCanRide:
    def test_tall_and_old_enough(self):
        assert can_ride(150, 14, with_adult=False) is True

    def test_young_with_adult(self):
        assert can_ride(130, 9, with_adult=True) is True

    def test_young_alone(self):
        assert can_ride(130, 9, with_adult=False) is False

    def test_too_short_even_with_adult(self):
        assert can_ride(110, 15, with_adult=True) is False

    def test_exact_limits(self):
        assert can_ride(120, 12, with_adult=False) is True


class TestIsLeapYear:
    def test_divisible_by_four(self):
        assert is_leap_year(2024) is True

    def test_ordinary_year(self):
        assert is_leap_year(2023) is False

    def test_century_is_not(self):
        assert is_leap_year(1900) is False

    def test_fourth_century_is(self):
        assert is_leap_year(2000) is True


class TestCompareObjects:
    def test_identical(self):
        shopping = ["milk"]
        assert compare_objects(shopping, shopping) == "identical"

    def test_equal(self):
        assert compare_objects(["milk"], ["milk"]) == "equal"

    def test_different(self):
        assert compare_objects(["milk"], ["eggs"]) == "different"

    def test_a_second_name_for_the_same_list(self):
        first = [1, 2]
        second = first
        assert compare_objects(first, second) == "identical"

    def test_a_copy_is_only_equal(self):
        first = [1, 2]
        assert compare_objects(first, first.copy()) == "equal"


class TestClockAdd:
    def test_wraps_past_twelve(self):
        assert clock_add(11, 2) == 1

    def test_one_past_twelve(self):
        assert clock_add(12, 1) == 1

    def test_lands_on_twelve_not_zero(self):
        assert clock_add(10, 2) == 12
        assert clock_add(12, 12) == 12

    def test_adding_nothing(self):
        assert clock_add(3, 0) == 3

    def test_backwards(self):
        assert clock_add(1, -2) == 11

    def test_more_than_a_full_turn(self):
        assert clock_add(6, 24) == 6
        assert clock_add(6, 25) == 7
