import pytest
from functions_exercises import (
    add_tag,
    apply_n_times,
    build_url,
    clamp,
    format_price,
    make_counter,
    pipeline,
)


class TestFormatPrice:
    def test_default_currency(self):
        assert format_price(3.5) == "£3.50"

    def test_custom_currency(self):
        assert format_price(10, "$") == "$10.00"

    def test_rounds_to_two_places(self):
        assert format_price(2.499) == "£2.50"

    def test_negative(self):
        assert format_price(-2, "$") == "-$2.00"

    def test_zero(self):
        assert format_price(0) == "£0.00"


class TestClamp:
    def test_above_range(self):
        assert clamp(15, low=0, high=10) == 10

    def test_below_range(self):
        assert clamp(-3, low=0, high=10) == 0

    def test_inside_range(self):
        assert clamp(7, low=0, high=10) == 7

    def test_on_the_boundary(self):
        assert clamp(10, low=0, high=10) == 10

    def test_low_and_high_must_be_keywords(self):
        with pytest.raises(TypeError):
            clamp(5, 0, 10)  # type: ignore[misc]


class TestBuildUrl:
    def test_example(self):
        url = build_url("https://api.example.com/", "/users", page=2, sort="name")
        assert url == "https://api.example.com/users?page=2&sort=name"

    def test_no_params(self):
        assert build_url("https://example.com", "about") == "https://example.com/about"

    def test_slash_handling(self):
        expected = "https://example.com/about"
        assert build_url("https://example.com/", "about") == expected
        assert build_url("https://example.com", "/about") == expected
        assert build_url("https://example.com/", "/about") == expected

    def test_params_keep_their_order(self):
        url = build_url("https://example.com", "search", z=1, a=2)
        assert url == "https://example.com/search?z=1&a=2"


class TestAddTag:
    def test_without_existing_tags(self):
        assert add_tag("python") == ["python"]

    def test_with_existing_tags(self):
        assert add_tag("b", ["a"]) == ["a", "b"]

    def test_calls_without_tags_do_not_share_a_list(self):
        first = add_tag("one")
        second = add_tag("two")
        assert first == ["one"]
        assert second == ["two"]


class TestApplyNTimes:
    def test_doubling(self):
        assert apply_n_times(lambda x: x * 2, 1, 3) == 8

    def test_once(self):
        assert apply_n_times(lambda x: x + 10, 5, 1) == 15

    def test_zero_times_returns_value_unchanged(self):
        assert apply_n_times(lambda x: x * 100, 7, 0) == 7


class TestMakeCounter:
    def test_counts_up(self):
        counter = make_counter()
        assert [counter(), counter(), counter()] == [1, 2, 3]

    def test_counters_are_independent(self):
        a = make_counter()
        b = make_counter()
        a()
        a()
        assert b() == 1
        assert a() == 3


class TestPipeline:
    def test_example(self):
        shout = pipeline(str.strip, str.upper, lambda s: s + "!")
        assert shout("  hello ") == "HELLO!"

    def test_runs_left_to_right(self):
        add_then_double = pipeline(lambda x: x + 1, lambda x: x * 2)
        assert add_then_double(3) == 8

    def test_single_function(self):
        assert pipeline(len)("abc") == 3

    def test_no_functions_returns_input(self):
        assert pipeline()(42) == 42
